from pathlib import Path
import json,hashlib,runpy
P=Path(__file__).parent
out=P/"extracted_sources";out.mkdir(exist_ok=True)
data=(P/"RETAINED_COMPLETE_PROOF_SOURCES.tex").read_bytes()
for r in json.loads((P/"SOURCE_LEDGER.json").read_text(encoding="utf-8"))["retained_source_offsets"]:
    b=data[r["offset"]:r["offset"]+r["length"]]
    if hashlib.sha256(b).hexdigest()!=r["sha256"]:raise ArithmeticError(r["file"])
    (out/r["file"]).write_bytes(b)
for n in ["check_memory_energy.py","check_rational_filters.py","check_reduced_model.py"]:
    runpy.run_path(str(P/n),run_name="__main__")
