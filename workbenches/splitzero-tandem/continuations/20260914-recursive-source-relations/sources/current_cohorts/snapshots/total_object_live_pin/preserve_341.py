"""Preserve the verified 341-page edition before the next cumulative build."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "output"
READER = OUT / "tau_split_zero_counterfactual_continuation_20260913"
RECORDS = Path(__file__).resolve().parent / "preserved_341"


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def main():
    RECORDS.mkdir(exist_ok=True)
    pairs = [
        (READER / "Tau_Split_Zero_Total_Counterfactual.pdf",
         OUT / "Tau_Split_Zero_Total_Counterfactual_341page_Intermediate.pdf",
         "b923ea59918ad74e9573ac867de283b7da6c6fea127ed428cfa6148ed1cbabd7"),
        (OUT / "Tau_Split_Zero_Total_Counterfactual_Source.zip",
         OUT / "Tau_Split_Zero_Total_Counterfactual_Source_341page_Intermediate.zip",
         "0ebc9c90273aa67b01061686109d81070e043388d0d7c3c4315bc277cabebdb7"),
    ]
    files = []
    for source, target, expected in pairs:
        if sha(source) != expected:
            raise RuntimeError(f"Unexpected source edition: {source}")
        if target.exists():
            if sha(target) != expected:
                raise RuntimeError(f"Refusing to overwrite a different snapshot: {target}")
        else:
            shutil.copy2(source, target)
        if sha(target) != expected:
            raise RuntimeError(f"Snapshot copy failed: {target}")
        files.append({"source": str(source), "preserved": str(target),
                      "sha256": expected, "bytes": target.stat().st_size})
    with zipfile.ZipFile(pairs[1][1]) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"Source archive CRC failure: {bad}")
        archive_entries = len(archive.infolist())
    for relative in ["provenance/TOTAL_OBJECT_EDITION.json",
                     "provenance/CONTINUATION_INPUT_MANIFEST.json",
                     "build/visual_qa/FINAL_VISUAL_QA_RECEIPT.json"]:
        source = READER / relative
        target = RECORDS / Path(relative).name
        if target.exists() and sha(target) != sha(source):
            raise RuntimeError(f"Preservation receipt already differs: {target}")
        if not target.exists():
            shutil.copy2(source, target)
    receipt = {"at": datetime.now(timezone.utc).isoformat(), "pages": 341,
               "files": files, "archive_entries": archive_entries,
               "archive_crc": "PASS", "goal_status_changed": False,
               "delivered_web_folder_changed": False}
    destination = RECORDS / "PRESERVATION_RECEIPT.json"
    if not destination.exists():
        destination.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
