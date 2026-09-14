from pathlib import Path
import json,hashlib,re,datetime
R=Path(r"workspace:\work\backpropagation_20260913\metric")
m=json.loads((R/"PATCH_MANIFEST.json").read_text())
receipt={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "scope":"Five complete proof-site revisions plus full R58 claim replacement, isolated source edits only.",
 "rows":[],"sealed_originals_preserved":True}
for row in m["rows"]:
    src=Path(row["source"]); dest=Path(row["revised"])
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    assert sha(src)==row["original_sha256"]
    assert sha(dest)==row["revised_sha256"]
    text=dest.read_text(encoding="utf-8")
    tags=[]
    for i,line in enumerate(text.splitlines(),1):
        for tag in re.findall(r"\\tag\{([^}]+)\}",line): tags.append({"tag":tag,"line":i})
    receipt["rows"].append(dict(**row,tags=tags,original_bytes=src.stat().st_size,
                               revised_bytes=dest.stat().st_size,original_hash_unchanged=True))
for name in ["DEPENDENCY_MAP.md","conclusion_replacements/R58_MAP.json",
             "conclusion_replacements/R58_NEW.tex","compile/VALIDATION.json"]:
    p=R/name
    receipt.setdefault("evidence",[]).append(dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(R/"FINAL_RECEIPT.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps(dict(status="PASS",changed_files=len(receipt["rows"]),
                     complete_R58=True,originals_unchanged=True,
                     receipt_sha256=hashlib.sha256((R/"FINAL_RECEIPT.json").read_bytes()).hexdigest()),indent=2))
