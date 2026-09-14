from pathlib import Path
from datetime import datetime
import json
import hashlib
import fitz

root=Path(__file__).resolve().parents[3]
work=root/'work/rh_counterfactual_20260913'
folder=root/'output/Mixed_Support_Web_Continuation_2026-09-13'
stamp=datetime.now().astimezone().isoformat()
messages=["Yeah, that calculation, can you make the prompt for the web session that makes it do that?","And open a folder, and in that folder put the prompt and any files you want me to drag into the web session, noting you can only do up to 20 different files per drag."]
for p in [work/'USER_INPUTS_VERBATIM.md',work/'shared_thread_audit/THIS_SESSION_USER_INPUTS_VERBATIM.md']:
    with p.open('a',encoding='utf8') as f:
        f.write('\n\n## Direct user web-prompt and folder request — '+stamp+'\n')
        for m in messages:f.write('\n```text\n'+m+'\n```\n')
manifest=json.loads((folder/'12_SOURCE_MANIFEST.json').read_text(encoding='utf8'))
for row in manifest['files']:
    if hashlib.sha256((folder/row['file']).read_bytes()).hexdigest()!=row['sha256']:raise RuntimeError('Hash mismatch')
with fitz.open(folder/'04_ORIGINAL_PROGRAMME.pdf') as pdf: pages=len(pdf)
if pages!=821:raise RuntimeError('Original programme page count changed')
note=('\n\n## Web continuation handoff and exact remaining work — '+stamp+'\n\n'
 'User requested a prompt and an opened folder, maximum20 files per drag. The handoff folder is '+str(folder)+', with13 flat files (prompt plus12 attachments), approximately6.98MB. File00 is the ready-to-paste prompt. All copied hashes and complete joined source byte blocks pass; the original programme PDF has821 pages. File03 is the fully flattened preserved248-page source (not newly compiled), with old TO/CAU explicitly superseded by current file02 and MCF in file01. File01 is the final AW-inclusive coordinating package, unchanged. Files02/05 retain actual independent coordinate-product, quadratic/negacyclic and higher-lattice carriers with their exact maps, prime branches and ideals. File06 retains fullWDB and earlierDeligne arguments; files07/08 are currentS20 exports. File09 now contains the complete reviewed SP.1–36 and SPF.1–29 single-primary boundary calculation (hash80dcbc843df223a8b65fd92f728deba1b28e540c748e08dabbdf47a6f28958ea). File11 retains exactPR29 Git blobs through its extraction manifest. File10 includes the proved F1=Theta(phi_*) endpoint reading correction, accepted by source owner, plus exact previous/current map and AW/SP comparisons.\n\n'
 'Prompt independent review corrections preserve WDB twist(c alpha)^2, compact-to-ordinary image scope for duality, MAI tensor domain, and explicit operations across all actual support types. The task is the same existing mixed-support programme, not an invented speech-to-text concept. It directs continuation past the completed single-primary case to tensor invariants, mixed-primary coupling, source comparison and the original signed arithmetic control.\n\n'
 'Fresh get_goal returned null, contrary to stale usageLimited state in earlier continuity notes. Two create_goal attempts exceeded theAPI4000characterlimit and made no change; local length validation then shortened to3986characters, and create_goal succeeded with active status. Exact objective is retained in total_object/RESTORED_TOOL_GOAL_20260913.md. No unfinished goal was closed.\n\n'
 'Cumulative manuscript integration remains unfinished: assembler now has MFC/CFA/MAI/WDB plus mainMCF/MW/MRE/SP/BC, but needs latestAW, full newprimarysource, explicit empty-packet readingcorrection, final assembly/build/QA and dynamic seal. The old248PDF/ZIP remain preserved intermediates; no new cumulativePDF or ZIP was claimed. Root fixed actualPython encoding spelling utf-8-sig in the webbuilder and cumulativeassembler. No RH endpoint, remote publication or Lean run occurred.\n')
for p in [work/'WORK_LOG.md',work/'CURRENT_CALCULATION.md']:
    with p.open('a',encoding='utf8') as f:f.write(note)
receipt={'at':stamp,'folder':str(folder),'files':13,'original_pdf_pages':pages,'manifest_sha256':hashlib.sha256((folder/'12_SOURCE_MANIFEST.json').read_bytes()).hexdigest(),'all_handoff_hashes':'PASS','scope':'Prompt and source handoff complete; mathematical research goal remains active.'}
(work/'total_object/WEB_HANDOFF_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf8')
print(json.dumps(receipt,indent=2))
