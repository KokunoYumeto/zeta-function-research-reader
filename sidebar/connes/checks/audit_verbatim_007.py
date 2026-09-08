"""One bounded canonical audit; preserve individual messages and raw newlines."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
SESSION=Path(r"[local]/.codex\sessions\2026\09\08\rollout-2026-09-08T15-54-26-01a0814c-728a-75c2-9ca1-dceb824f32a0.jsonl")
records=[]
with SESSION.open(encoding="utf-8") as stream:
    for number,line in enumerate(stream,1):
        item=json.loads(line)
        p=item.get("payload",{})
        if (item.get("type")=="response_item" and p.get("type")=="message"
                and p.get("role")=="user"):
            texts=[part.get("text","") for part in p.get("content",[])
                   if part.get("type") in ("input_text","text")]
            records.append({"session_line":number,"timestamp":item.get("timestamp"),
                            "texts":texts,"sha256":[hashlib.sha256(t.encode("utf-8")).hexdigest() for t in texts]})
target=ROOT/"logbook"/"user_inputs_verbatim_canonical_007.md"
with target.open("w",encoding="utf-8",newline="") as stream:
    stream.write("# Canonical user-input audit, continuation 007\n\nEvery user-role message in the exact task session is retained in order, including repeated messages. Message text below preserves its decoded original Unicode and newlines. Historical append logs are retained; their former newline conversion could produce duplicate entries. JSON receipt provides exact text arrays and hashes. This audit is bounded to the recorded session lines.\n")
    for record in records:
        stream.write(f"\n\n---\n\nSession line {record['session_line']}; timestamp {record['timestamp']}\n\n")
        for text in record["texts"]:
            stream.write(text)
            stream.write("\n")
receipt={"session":str(SESSION),"message_count":len(records),"records":records}
with (ROOT/"logbook"/"user_inputs_canonical_receipt_007.json").open("w",encoding="utf-8",newline="") as stream:
    json.dump(receipt,stream,ensure_ascii=False,indent=2)
    stream.write("\n")
print(json.dumps({"messages":len(records),"last_user_session_line":records[-1]["session_line"] if records else None}))
