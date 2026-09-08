"""Copy exact coordination messages from the one authoritative task session."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
SESSION=Path(r"[local]/.codex\sessions\2026\09\08\rollout-2026-09-08T15-54-26-01a0814c-728a-75c2-9ca1-dceb824f32a0.jsonl")
target=ROOT/"logbook"/"delegated_directives_verbatim.md"
with target.open(encoding="utf-8",newline="") as stream:
    current=stream.read()
normalized=current.replace("\r\n","\n").replace("\r","\n")
pending=[]
def strings(value):
    if isinstance(value,str):
        yield value
    elif isinstance(value,dict):
        for child in value.values():
            yield from strings(child)
    elif isinstance(value,list):
        for child in value:
            yield from strings(child)
added=0
with SESSION.open(encoding="utf-8") as stream:
    for line in stream:
        for value in strings(json.loads(line).get("payload",{})):
            start=value.find("<codex_delegation>")
            end=value.find("</codex_delegation>",start)
            if start>=0 and end>=0:
                message=value[start:end+len("</codex_delegation>")]
                comparable=message.replace("\r\n","\n").replace("\r","\n")
                if comparable not in normalized:
                    pending.append("\n\n---\n\n"+message+"\n")
                    normalized+="\n\n---\n\n"+comparable+"\n"
                    added+=1
with target.open("a",encoding="utf-8",newline="") as stream:
    stream.writelines(pending)
print(json.dumps({"new_coordination_inputs":added,"scope":"one exact session"}))
