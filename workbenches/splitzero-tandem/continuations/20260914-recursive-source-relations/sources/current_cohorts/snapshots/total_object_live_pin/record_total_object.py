"""Durable bounded transcript audit and exact current-work record."""
from pathlib import Path
import datetime, json, shutil

WORK=Path(__file__).resolve().parents[1]
REPO=WORK.parents[1]/'output/tau_split_zero_counterfactual_continuation_20260913'
SESSION=Path(r'local:user-profile\.codex\sessions\2026\09\13\rollout-2026-09-13T07-00-56-01a09923-cfae-7353-82d0-a47f6c90e839.jsonl')
records=[]
with SESSION.open(encoding='utf8') as stream:
    for line in stream:
        row=json.loads(line); p=row.get('payload',{})
        if row.get('type')=='response_item' and p.get('role')=='user':
            body='\n'.join(c.get('text','') for c in p.get('content',[])
                           if c.get('type') in ('input_text','text'))
            records.append((row.get('timestamp',''),body))
text=['# Complete user-channel provenance in the current session\n\n',
      'Every user-channel response item is retained literally below. Internal coordinator envelopes are transport provenance, not additional human requests.\n']
for i,(ts,body) in enumerate(records,1):
    text.append(f'\n## Record {i} — {ts}\n\n{body}\n')
(WORK/'shared_thread_audit/THIS_SESSION_USER_INPUTS_VERBATIM.md').write_text(''.join(text),encoding='utf8')
ts=datetime.datetime.now().astimezone().isoformat()
with (WORK/'USER_INPUTS_VERBATIM.md').open('a',encoding='utf8') as f:
    f.write(f'\nBounded JSONL audit at {ts}: {len(records)} literal user-channel records retained in shared_thread_audit/THIS_SESSION_USER_INPUTS_VERBATIM.md. It includes the request to identify the exact programme elements giving Deligne’s analogous final contradiction and the request to locate Weil II LaTeX.\n')
old=WORK/'CURRENT_CALCULATION.md'
history=WORK/'total_object/CURRENT_CALCULATION_109PAGE_HISTORY.md'
if not history.exists():shutil.copy2(old,history)
current=r'''# Current calculation: one total original counterfactual object

The outcome requested is the construction of the total counterfactual object from the entire actual tau-based Split-Zero programme, then pursuit of a contradiction excluding every actual offcritical zero or an actual disproof. The latest request identifies Deligne's final amplification/exclusion mechanism in this same programme. No RH endpoint is established. get_goal reports usageLimited; the goal was not marked complete or replaced. The exact 3951-character objective remains CORRECTED_ACTIVE_GOAL.md. User instructions and corrected workflow persist here.

## Actual object and exhaustive arithmetic map

For U={0<Re(s)<1, Re(s) != 1/2}, define B_U by the original condition p(D)F in Theta V for some monic p with roots in U. This definition uses every admitted polynomial and no preselected zeros. The single tensor DGA is T_U=directsum_k [V -> B_U]^(tensor_C k). It injects into the full original two-leg tau tensor DGA by v -> (v/2,-hat(v)/2), F -> F. The represented diagram attaches its full coherent comparison, full kernel and diagonal, actual absolute base, support, F1 arithmetic scalar map, finite full jets, tensor/conormal observations, norms, phase generators and divisor maps with their correct domains. The whole background is not an RH detector; its marked H1 is.

TO.1–10 and CAU.1–37 prove H1=[offcritical polynomial torsion of Q] is exactly the direct sum of O_rho/(g) at all actual offcritical zeros. The original Euler inverse gives a nonzero actual source lift of every nonzero such jet. AG.1–38 plus AG36a–e prove the one-object divisor gluing, full-unit tensor transitions, complementary cyclic components and all-depth distributed injection. Inclusions go through full joint tensor algebras; they do not falsely preserve distinguished cyclic subspaces. All original labels, source relations, units and nilpotents remain.

## Exact Deligne analogue, evaluated

For an actual offcritical quartet with rho=1/2+delta+i gamma, delta>0, full order m, the full tensor retains eigenvalue k rho and nilpotent order ell_k=1+k(m-1). Its complete cyclic dimension is q_k=ell_k(k+1)^2. The original critical-line phase generator is D=-partial_r+k/2 on its exact twisted H1 domain. The connecting map is DR-RA=B. On the offending full-jet eigenvector, ||Bv||^2/||Rv||^2=k^2 delta^2 plus the positive original frequency dispersion. The full nilpotent Sylvester inverse is explicit. PAM.1–27 and PSC.1–64 prove all maps and source norms.

Two actual gluing differences can both be made <=1/(k+1) by the fully costed period choice in PSC.42. Nevertheless the full generator boundaries retain order k q_k in the same metric (PSC.43–49). At N=q_k-1 the gluing error is exactly zero, while the literal original residue boundary is f_chi,theta tensor ell, nonzero. Its exact squared operator and HS norm is epsilon_theta^2+(Im alpha)^2+omega_q/omega_(q-1)>epsilon_theta^2>=L_k^2 (PSC.50–64). Vanishing gluing is therefore not the required spectral exclusion.

AAM.1–36 evaluates the same original arithmetic four-window comparison. The exact coupled product is epsilon_bar=exp(Omega/(4q)) exp((B-P-Phi)/(4q))>=L_k, where L_k=2delta ell_k(k+1)floor((k+1)^2/4) and L_k/(kq_k)->delta/2. The norm factor divided by L_k is asymptotic to 8/(e delta k); the other actual quotient factor has liminf after division by k at least e delta/8. Neither factor may be removed. The proved angle-comparison overhead has (2q_k-1)Lambda_k/L_k -> 4d_h/delta>0, with Lambda_k/k->d_h>pi/2 and all source constants retained. Existing upper comparisons therefore supply no Deligne shrinking exclusion for the same amplified control. Fixed-k Gram decay retains divergent inverse Gram factors and the nonzero original arithmetic observation.

The actual coefficient-purity trace retract preserves the arithmetic eigenvalue under dilation; it does not impose a finite-field weight theorem on that eigenvalue. All original theta and support maps remain in the diagram. These calculations establish an exact connection and explicit surviving boundary, not a claim that no further arithmetic estimate is possible.

## Deligne and Weil II source recovery

DELIGNE_AMPLIFICATION.md and its included TeX prove the full finite contradiction from Weil I Lemma7.1 and paragraph7.3, printed pages298/301: q^(D/2±1/2), actual even product X^k over the same field, nonzero Kunneth eigenclass alpha^k, then exponent error 1/(2k). Every conjugate and odd-dimensional algebraicity is covered. For nonzero epsilon, k=2(floor(1/(4|epsilon|))+1) gives the finite contradiction. No finite-field estimate is assumed on the Split-Zero source.

WEIL_II_AMPLIFICATION.md locates the other exact recalled passage: Weil II1.8.1, radius q^(-(beta+2)/2), return to1.4.3, boundary pole exclusion, injective inertia-invariant tensor map, weight bound beta+2/k. This is an upper boundary-weight bound, not equality. Both notes passed independent review.

The existing complete Weil II LaTeX is found and indexed in workspace:/RESEARCH_SOURCE_INDEX.md, with detailed hashes in total_object/WEIL_II_SOURCE_LOCATOR.md. Current complete French/English S20 exports and historical complete English math-mode source have distinct status. The historical English denominator H0 in1.8.1.1 is incorrect; the current S20 H_c^2 is used. Source originals were preserved.

## Repository and validation

Frozen109-page baseline and its old source ZIP remain unchanged. New standalone repository: output/tau_split_zero_counterfactual_continuation_20260913. Master tex/main.tex includes31 complete proof modules:13 prior and18 new exact-byte inputs. Original821-page source closure, full shared-thread audit and both user attachments remain in the repository. New authored modules and reviews are under total_object_sources/ and continuation_sources/. At this record the new224-page reader has three clean XeLaTeX passes and repository validation PASS:31 integrity records,261 labels,120 references, no missing inputs/refs, duplicate labels, overflowing text, missing glyphs or blank pages. PDF SHA08a5293305eb1fd7b0ce22816a2ded717d002bf7a5f44e7177560efbb3a1b5eb. Final visual QA is running. The new ZIP target is Tau_Split_Zero_Total_Counterfactual_Source.zip; do not overwrite the frozen baseline archive. Root formatting repair CA21 and independently approved AG formatting repairs changed no mathematics.

The full source-ordered public-thread reading and independent5349-message hash comparison are preserved; do not redo it. Current user-channel transcript is rewritten by the bounded audit associated with this record. Keep coordinator messages separate from human requests. No Lean or remote publication occurred. PDF authoring marker already ran once for this cumulative operation; do not repeat.

## Latest coordinating programme input

Main task Split Zero to GCT bridge (01a08256-1eac-7cb3-9f74-6c095b18e74c) reports original H15 and shifted H15^1 certified positive from original g=2xi theta moments. TC.1–28 is work/tau_theta_hankel_error_control_20260913.tex; certificate files are work/theta_certified_hankel_20260913; WBR.1–41 is work/rh_counterfactual_workbench_intake_20260913/WORKBENCH_INDEPENDENT_PROOF.md. This is finite positivity, not a general RH result. Agent finite_disproof_certificate is proving the exact additive attachment and its finite separator exclusion to our existing total object; AAM remains unchanged. Record this input and its concrete exact map, without treating it as a new task or replacing the total-object objective.

## Immediate remaining local work

Complete visual QA, record any precise repairs, seal current source ZIP and refresh final receipts/README. Integrate a reviewed finite-Hankel attachment at its actual scope if ready, or preserve its new source receipt separately without misrepresenting it as part of the already-built224-page edition. Report the exact connected amplification calculation to the user with full source links and Weil II location. Research goal remains unfinished because neither an exhaustive contradiction nor an actual offcritical zero has been established.
'''
old.write_text(current,encoding='utf8')
with (WORK/'WORK_LOG.md').open('a',encoding='utf8') as f:
    f.write(f'\n## {ts} — Total object and exact Deligne match constructed\n\n'+current.split('\n',2)[2]+f'\n\nBounded current transcript audit retained {len(records)} records.\n')
print(json.dumps({'records':len(records),'recorded_at':ts,'state':'mathematics and224-page build recorded; visual QA pending'}))
