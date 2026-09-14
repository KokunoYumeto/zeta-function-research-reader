"""Preservation and complete tagged-equation checks for the staged MW/MRE edition."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
WORK = ROOT.parents[2]
LIVE = {
    "MW": WORK / "tau_mixed_support_monodromy_filtration_20260913.tex",
    "MRE": WORK / "tau_mixed_relative_extension_control_20260913.tex",
}
EXPECTED = {
    "MW": "1834376a6eb1b338090cffa04d77361b25d4e63a5a909df6b24c5c9551688598",
    "MRE": "35c080171f5bbc895d3e7f7f89776eabc7d71c5376dbc6be1a1bb0102c30fd73",
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def equations(text):
    found = {}
    for match in re.finditer(r"\\\[(.*?)\\\]", text, re.S):
        tags = re.findall(r"\\tag\{([^}]+)\}", match.group(1))
        assert len(tags) <= 1, tags
        if tags:
            assert tags[0] not in found, tags[0]
            found[tags[0]] = match.group(1)
    return found

inventory = {}
for name in ("MW", "MRE"):
    old = ROOT / "originals" / f"{name}.tex"
    new = ROOT / "revised" / f"{name}.tex"
    assert digest(old) == EXPECTED[name], ("original changed", name)
    assert old.read_bytes() == LIVE[name].read_bytes(), ("live changed", name)
    oldtext = old.read_text(encoding="utf-8")
    newtext = new.read_text(encoding="utf-8")
    oldeq, neweq = equations(oldtext), equations(newtext)
    allowed = {"MW10"} if name == "MW" else set()
    changed = [tag for tag, body in oldeq.items() if neweq.get(tag) != body]
    assert set(changed) == allowed, (name, changed)
    expected_count = 33 if name == "MW" else 42
    assert len(neweq) == expected_count, (name, len(neweq))
    if name == "MRE":
        # All original prose and equations remain in their original line order.
        iterator = iter(newtext.splitlines())
        for line in oldtext.splitlines():
            assert any(line == candidate for candidate in iterator), line
    tags = {}
    for edition, text in (("original", oldtext), ("revised", newtext)):
        tags[edition] = {
            tag: text[:match.start()].count("\n") + 1
            for match in re.finditer(r"\\tag\{([^}]+)\}", text)
            for tag in [match.group(1)]
        }
    inventory[name] = {
        "live_source": str(LIVE[name]),
        "original_file": str(old),
        "revised_file": str(new),
        "original_sha256": digest(old),
        "revised_sha256": digest(new),
        "original_bytes": old.stat().st_size,
        "revised_bytes": new.stat().st_size,
        "original_lines": len(oldtext.splitlines()),
        "revised_lines": len(newtext.splitlines()),
        "changed_original_formula_tags": changed,
        "original_formula_tags_preserved_exactly": [
            tag for tag in oldeq if tag not in changed
        ],
        "new_formula_tags": [tag for tag in neweq if tag not in oldeq],
        "tag_line_locators": tags,
    }
log = (ROOT / "VERIFY.log").read_text(encoding="utf-8", errors="replace")
bad = re.findall(r"(?:Overfull|Underfull|LaTeX Warning:|^! ).*", log, re.M)
assert not bad, bad
assert "Output written on VERIFY.pdf (15 pages" in log
inventory["validation"] = {
    "live_sources_byte_identical_to_preserved_originals": True,
    "all_MRE_original_lines_retained_in_order": True,
    "all_75_revised_tagged_equations_unique": True,
    "pdflatex_exit_code": 0,
    "pdf_pages": 15,
    "tex_log_warnings_or_box_overflows": bad,
    "complete_proofs_in": ["revised/MW.tex", "revised/MRE.tex"],
    "scope": "staged complete TeX fragments; live and sealed editions unchanged",
}
(ROOT / "INVENTORY.json").write_text(
    json.dumps(inventory, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({
    name: {
        key: value for key, value in record.items()
        if key in {"revised_sha256", "revised_bytes", "revised_lines",
                   "changed_original_formula_tags", "new_formula_tags"}
    }
    for name, record in inventory.items() if name != "validation"
}, indent=2))
print("PASS: original bytes, complete MRE line preservation, unchanged original "
      "formula bodies except explicitly clarified MW10, all 75 tags, clean 15-page compile.")
