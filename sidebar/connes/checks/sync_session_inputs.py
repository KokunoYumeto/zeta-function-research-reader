"""One bounded audit of user-role input in this task's exact session file."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SESSION = Path(r"[local]/.codex\sessions\2026\09\08\rollout-2026-09-08T15-54-26-01a0814c-728a-75c2-9ca1-dceb824f32a0.jsonl")
target = ROOT / "logbook" / "user_inputs_verbatim.md"
with target.open(encoding="utf-8", newline="") as stream:
    current = stream.read()
normalized = current.replace("\r\n", "\n").replace("\r", "\n")
pending = []
added = 0
with SESSION.open(encoding="utf-8") as stream:
    for line in stream:
        item = json.loads(line)
        payload = item.get("payload", {})
        if (item.get("type") != "response_item"
                or payload.get("type") != "message"
                or payload.get("role") != "user"):
            continue
        value = "\n".join(part.get("text", "")
                          for part in payload.get("content", [])
                          if part.get("type") in ("input_text", "text"))
        comparable = value.replace("\r\n", "\n").replace("\r", "\n")
        if value and comparable not in normalized:
            pending.append("\n\n---\n\n" + value + "\n")
            normalized += "\n\n---\n\n" + comparable + "\n"
            added += 1
with target.open("a", encoding="utf-8", newline="") as stream:
    stream.writelines(pending)
print(json.dumps({"new_verbatim_inputs": added, "audit": "one exact session file"}))
