from pathlib import Path
from datetime import datetime
import hashlib
import json

root=Path(__file__).resolve().parents[3]
work=root/'work/rh_counterfactual_20260913'
total=work/'total_object'
goal=work/'CORRECTED_ACTIVE_GOAL.md'
text=goal.read_text(encoding='utf-8-sig')
text=text.replace('Include the user\'s expressly requested “mixed weightlessing” in this same goal: carry mixed weights and their boundary control through the original mixed-support objects to the arithmetic theta source.', 'Use the existing mixed-support construction, mixing the different split-support types, and calculate Deligne-analogous control on those actual objects and their arithmetic theta source. The user has corrected a speech-to-text error; no additional concept was requested.')
text=text.replace('this durable file records the user\'s mixed-weightlessing addition', 'this durable file records the continuing mixed-support calculation and the corrected user intent')
text=text.replace('Carry out mixed weightlessing on every independent coefficient face', 'Calculate the mixed-support maps and their weight and boundary control on every independent coefficient face')
goal.write_text(text,encoding='utf-8')
changes={
 total/'README_MIXED_EDITION.md': [
 ('The total original counterfactual object and mixed weightlessing','The total original counterfactual object and mixed support'),
 ('Mixed weightlessing is expressly part of the continuing research goal', 'The existing mixed-support calculation and its Deligne comparison remain part of the continuing research goal')],
 total/'MIXED_EDITION_CALCULATION.md': [
 ('The latest direct user addition is mixed weightlessing as part of the existing research goal. CORRECTED_ACTIVE_GOAL.md includes it; the old version is preserved.', 'The user clarified that the intended subject is the existing mixed-support programme, mixing the different split-support types and calculating Deligne-analogous control. The assistant incorrectly promoted a speech-to-text error to a technical label. That label has been withdrawn from the current instructions and manuscript; historical messages remain preserved. CORRECTED_ACTIVE_GOAL.md now records the corrected intent.')],
 root/'output/tau_split_zero_counterfactual_continuation_20260913/scripts/assemble_continuation.py': [
 ('Mixed weightlessing: filtrations, extensions and the original arithmetic class','Mixed support: filtrations, extensions and the original arithmetic class')]
}
for path,replacements in changes.items():
    body=path.read_text(encoding='utf-8-sig')
    for old,new in replacements:
        if old not in body: raise RuntimeError(f'Missing replacement in {path}: {old}')
        body=body.replace(old,new)
    path.write_text(body,encoding='utf-8')
messages=[
"What the fuck is mixed weightlessness? Are you schizophrenic? I'm using speech-to-text. Did you just hallucinate a whole concept based on a speech-to-text error? What the fuck is wrong with you?",
"Mixed wait. Sorry, mixed support. What? It's the same fucking... just mixed. The mixed thing. The fucking mixed. Whatever. If you can't figure out, it's the same research program, dumbass.",
"# Files pasted by the user:\n\n## \"Yeah, okay. I don't think you really heard me when I said I need you to constru…\": local:user-profile\\.codex/attachments/92e51a1b-2c4c-44ed-ad1d-c6de038c460e/pasted-text.txt\n\n## My request:\nIt's the stupidest shit ever. You take the thing that Pierre Deligne did. Also, you're being compacted, idiot. You take the thing that Pierre Deligne did with his mixed homology mixed thing. You find the mixed thing in our program, which to my knowledge is mixed support, mixed between the different types of split support, mixing them. And then you control. And if you do it right, ta-da, Riemann hypothesis. Or, Riemann hypothesis is false."
]
stamp=datetime.now().astimezone().isoformat()
for path in [work/'USER_INPUTS_VERBATIM.md',work/'shared_thread_audit/THIS_SESSION_USER_INPUTS_VERBATIM.md']:
    with path.open('a',encoding='utf-8') as f:
        f.write('\n\n## Speech-to-text correction and continuing mixed-support instruction — '+stamp+'\n')
        for message in messages:f.write('\n```text\n'+message+'\n```\n')
attachment=Path('local:user-profile/.codex/attachments/92e51a1b-2c4c-44ed-ad1d-c6de038c460e/pasted-text.txt')
copy=work/'shared_thread_audit/USER_ATTACHMENT_20260913_STT_CORRECTION.txt'
copy.write_bytes(attachment.read_bytes())
record=('\n\n## Correction of assistant-invented terminology — '+stamp+'\n\n'
 'The user explicitly identified the previous phrase as a speech-to-text error and clarified mixed support within the same research programme. The assistant had incorrectly called it an express addition and propagated an invented technical label. Current goal, draft README, calculation record and chapter generator have been corrected. Historical user text and past assistant messages are retained as provenance, not current mathematical terminology. No separate mathematical concept is asserted. The same independent mixed-support faces, original source maps, Deligne comparison and actual boundary/metric control remain the task. The active goal was not closed or replaced. The coordinating task and boundary agent were notified.\n\n'
 'Latest pasted transcript was read in full and copied byte for byte to '+str(copy)+'; SHA256 '+hashlib.sha256(copy.read_bytes()).hexdigest()+'. It corroborates the visible direct user correction.\n')
for path in [work/'WORK_LOG.md',work/'CURRENT_CALCULATION.md']:
    with path.open('a',encoding='utf-8') as f:f.write(record)
print(json.dumps({'corrected_current_files':len(changes)+1,'goal_characters':len(text),'attachment_sha256':hashlib.sha256(copy.read_bytes()).hexdigest()},indent=2))
