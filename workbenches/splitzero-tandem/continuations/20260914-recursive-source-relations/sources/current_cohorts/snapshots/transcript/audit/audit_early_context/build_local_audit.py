from pathlib import Path
import hashlib,json,re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
SOURCE=ROOT/'output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0001_U0015.md'
raw=SOURCE.read_bytes(); text=raw.decode('utf-8'); lines=text.splitlines()
heads=[]
for index,line in enumerate(lines,1):
    m=re.fullmatch(r'## ([UA]\d{4}) \| ([^|]+) \| (user|assistant) \| chain (\d+)',line)
    if m: heads.append(dict(locator=m[1],node_id=m[2].strip(),role=m[3],chain=int(m[4]),line_start=index))
for i,h in enumerate(heads): h['line_end']=heads[i+1]['line_start']-1 if i+1<len(heads) else len(lines)
byid={h['locator']:h for h in heads}
classes={
'U0008':'superseded request: withdrawn explicitly by U0010',
'U0009':'feedback record: superseded negative-branch exchange; historical evidence only',
'A0446':'interim plan in superseded negative-branch exchange',
'A0466':'interim result in superseded negative-branch exchange',
'A0473':'completed polynomial calculation; proposed NS extension superseded by U0010',
'U0010':'explicit scope change: withdraw negative detour; retain workbench integration',
'A0474':'interim integration plan',
'A0533':'interim relevant arithmetic-kernel-jet provenance',
'A0546':'relevant arithmetic quotient precursor; other fluid/gauge exposition context',
'U0011':'relevant original heat/BCM/arithmetic mechanism request',
'A0548':'interim plan for exact thermal/cooling/quartet bridge',
'A0574':'interim claim of four-channel construction',
'A0598':'substantive relevant bridge, scoped obstruction, finite model and uncertified arithmetic test',
'U0012':'controlling precision and full-Shimura correction request',
'A0618':'substantive corrected sign and typed cooling/cutoff maps; genuine unfinished analytic transfer',
}

records=[]
def add(id,loc,span,quote,request,objects,proved,missing,scope,next_step,status='incomplete continuation'):
    h=byid[loc]
    body='\n'.join(lines[h['line_start']-1:h['line_end']])
    if quote not in body: raise ValueError((id,'quote not exact',quote))
    if not(h['line_start']<=span[0]<=span[1]<=h['line_end']): raise ValueError((id,'invalid lines'))
    records.append(dict(id=id,locator=loc,node_id=h['node_id'],chain=h['chain'],passage_lines=span,quote=quote,user_request=request,objects_and_maps=objects,what_was_proved=proved,what_remained_uncalculated=missing,obstruction_scope=scope,concrete_next_derivation=next_step,status=status))

add('EC08','A0473',[973,1009],
'The field U itself is stationary' if False else 'Its trajectory travels to increasingly negative spatial infinity, where its coefficients and derivatives are already large.',
'U0008 asked whether the original −1/4 fibre carries negative blowup; U0010 subsequently says to omit this negative detour.',
'Original polynomial F with det DF=−2, U=2W1+6F3W2, gamma_minus, Euclidean strain tensor; no tau cohomology is present.',
'The response computes explicit finite-time inverse escape and signed strain asymptotics for a polynomial vector field. It distinguishes spatial escape from blowup at a finite spatial point.',
'The bounded-region finite-energy, endpoint-smooth-force extension is not established, but U0010 withdraws this as the requested route.',
'Its scope is one polynomial lift and its physical extension. It cannot obstruct the later theta/absolute-base construction.',
'Do not revive the discarded negative detour. Retain the signed polynomial calculations only as historical context; continue the released-fluid and later tau source.',
'superseded by explicit user instruction')

add('EC10','A0546',[1074,1090],
'The distinction is the **order of operations**: lifting into an actual test function and then quotienting is not the same map as quotienting first and taking a jet.',
'U0010 asks to integrate the actual workbench additions; U0011 asks for more than a generic non-self-adjointness statement.',
'Four-jet lift L_k into original arithmetic tests followed by quotient; [T]=0, [(log x)T] nonzero under the imported trace-ideal hypotheses.',
'The response retains the source-dependent nonzero map and explicitly marks its hypotheses as imported. It does not equate every jet construction.',
'Its full pairing sign and finite quadrature/rounding certification remain uncalculated in this response; the linked kernel paper itself is not independently re-audited by this early-context lane.',
'Nonzero class is not a signed arithmetic witness. Conversely failure to sign the pairing does not erase the proved nonzero map.',
'Use the original later full Mellin-jet map J_Z and K_tau residue injection, retaining multiplicities and supported zeros; calculate the actual trace contraction and global theta relation, without changing to a residue-only packet.',
'relevant retained precursor')

add('EC11A','A0598',[1153,1231],
'An RH counterexample would have to emerge from the remaining, globally structured part of the completed Mellin transform—not merely reproduce this leading heat divergence.',
'U0011 asks for the exact image of the fluid/heat origin in BCM and the arithmetic spectrum.',
'N|n>=n|n>, H_BC=log N, heat semigroup exp(−pi x N²), Gamma-Mellin transform and the Poisson theta expansion.',
'The Gamma integral and the small-time term 1/(beta−1) explicitly connect the arithmetic heat endpoint to the BC Gibbs pole.',
'This local leading-term computation does not compute the global remainder that contains the original theta quotient and zeros.',
'It proves the scope of the leading heat singularity; it is not a proof that the global theta program cannot yield further arithmetic information.',
'Keep both endpoint terms and the complete Poisson theta remainder when passing to the original B/Theta V. The late accepted tau construction, not this leading thermal pole, is the continuation object.',
'completed local calculation with limited scope')

add('EC11B','A0598',[1274,1312],
'The important missing identification is whether an NS-derived object actually represents that character in the arithmetic quotient.',
'U0011 requests a concrete thermodynamic and spectral map, with the blowing-up source retained.',
'Logarithmic scale s=−log(1−t), centered character Lambda^(rho−1/2), and source quotient.',
'The growth/chirp coordinate identity is exact, but it does not identify a specific source test or quotient class.',
'An actual equivariant map from the retained cutoff test to the uncentered theta quotient and its full jets is absent here.',
'A missing identification is not nonexistence; it specifies the morphism to calculate.',
'Completed in NS_CUTOFF_THETA_SCALING.md equations (1)–(9): Cg=r^(−1/2)g, MF(s)=s(s−1)Mb(s−1/2), original two-leg chain map, actual-zero full jet multiplier and right-adjoint residue evaluation.',
'completed supplementary calculation in this audit')

add('EC11C','A0598',[1428,1520],
'We cannot replace that weight by an arbitrary rank-one projector onto a negative direction.',
'U0011 asks how the original absorption operator could register a quartet/cancellation mechanism; U0012 requires its exact original sign.',
'P=diag(0,I), U=[[A,B],[C,D]], D_script=P−U*PU, arithmetic multipliers theta(g*g*) on the source trace domain.',
'The full block form gives ||By||²−||Cx||²−2Re<Cx,Dy>. The response correctly limits the compact perturbation example and restricts arithmetic tests to allowed convolution weights.',
'It does not compute a signed bound for the actual local-factor U and the full allowed class. The initial sign-reversed scalar is later explicitly related to the original source scalar by A0618.',
'Compact leakage invalidates an inference from compactness alone to positivity. It does not prove the opposite sign for the actual arithmetic trace, nor global failure of any tau-base argument.',
'Resume the actual semilocal local-factor operator, original W scalar and trace-class domain. Retain the C*D cross term and full archimedean subtraction. Do not use arbitrary projector tests as a substitute.',
'legitimate scoped obstruction; sign presentation repaired by A0618')

add('EC11D','A0598',[1522,1672],
'It does not assume that interpolation eliminates all other zeros.',
'U0011 asks for the quartet mechanism and an actual arithmetic ansatz rather than a verbal RH criterion.',
'Actual functional-equation quartet symmetry; finite interpolation a=1,b=−1; auxiliary five-state F_eta=3+2exp(eta)cos z; actual Riemann heat kernel separately.',
'The quartet contribution is 4Re(a conjugate(b)); the finite thermal system explicitly shows positive equilibrium states can coexist with off-real observable zeros. The response labels the five-state model as distinct.',
'The finite interpolation has no global rest-of-zero-set control. The auxiliary model provides no analytic estimate for the original Riemann kernel.',
'This is an auxiliary example, not itself a false proof. It would become a scope substitution only if used to close or replace the original arithmetic calculation.',
'Retain the original Theta and full analytic source. Use finite jets only as exact observations of Q, with all omitted spectral and boundary contributions calculated rather than declared negligible.',
'auxiliary model with explicitly limited scope')

add('EC11E','A0598',[1686,1755],
'Proving that the bound persists for the **actual** Riemann heat family is the part not established here.',
'U0011 requested the actual heat mechanism and attempted proof rather than a restated criterion.',
'Xi_eta(s)=8H_eta(−2i(s−1/2)), PDE partial_eta Xi=(1/4)partial_s²Xi; adjacent gap d and exterior zero interaction.',
'The coordinate PDE and gap identity (d²)prime=8−4d² sum exterior 1/((b−x_j)(a−x_j)) retain the exterior terms. Positive eta breaks the raw termwise Dirichlet expansion, while the completed kernel still defines the family.',
'The response supplies a sufficient inequality with theta<2 and an initial gap inequality; it does not prove either for the actual family over the needed interval.',
'The displayed conditional collision mechanism is not a completed calculation for the Riemann kernel. Divergence of the raw Dirichlet series does not invalidate the completed kernel.',
'Do not promote the sufficient inequalities to proved input. Under the later accepted tau program, continue its original theta analytic estimates; revisit this heat route only as a specifically requested auxiliary calculation, retaining the completed kernel.',
'unproved sufficient criterion; not a conclusion about the later tau program')

add('EC11F','A0598',[1757,1883],
'The calculation uses floating-point quadrature, not certified intervals.',
'U0011 requests an arithmetic realization of the concentration/cross-term mechanism.',
'Original bump chi_L, Ephi, two reflected chirped packets, pole-cancelling D_y²−1/4, five-dimensional restriction of the unchanged Weil form, Schur complement q0−b^T A^(−1)b.',
'The test has exact compact support and pole cancellation; the response retains prime powers, archimedean subtraction and the exact tail. It reports 18 floating-point searches and positive minima, expressly without certification.',
'All finite quadrature and roundoff enclosures are absent. The minimum establishes neither global positivity nor a negative witness and is not shown to arise dynamically from the NS pulses.',
'Finite positive searches cannot reject the full original test space; numerical convergence is not proof at a small eigenvalue.',
'If this exact packet calculation is reused, recover its original code/parameters and enclose every error. For the tau continuation, keep the full original Theta rather than replacing the source with this finite packet family.',
'unfinished certification and transfer; no false witness claimed')

add('EC11G','A0598',[1885,1905],
'it does not yet determine the sign of its Weil pairing.',
'U0011 asks what the existing arithmetic work actually contributes.',
'The logarithmic multiplier on the retained theta radical, the original trace-ideal lift and quotient pairing; weighted ambient L² norm separately.',
'The response retains that log multiplication differentiates the Mellin transform and can remove a zero order, unlike multiplicative translations or log derivatives that preserve the zeta factor.',
'The actual pairing on that surviving class is not signed, and no continuous global pairing transfer is calculated here.',
'Small ambient norm or an uncomputed sign cannot be used to annihilate the quotient class.',
'Use the complete later residue injection into Hom(Q,L1) and trace contraction Gprime, with all nilpotents and labels. The new appendix (3a)–(3c) also computes the exact early E-to-Theta factor 1/2 and every cutoff product term.',
'retained nonzero map with unfinished pairing')

add('EC12A','A0618',[1999,2348],
r'The positive numbers previously reported were values of \(Q_{\mathrm{previous}}\). They were not positive values of equation (20)’s left-hand side, and were not counterexamples.',
'U0012 requires exact signs, typed morphisms, and proof instead of separation rhetoric.',
'Source scalar sum_v W_v(g*g*) <=0, exact factor 1/2 trace M_f U*[2P−I,U], original local-factor U, full admissibility; BC groupoid, Haar state and sigma_i.',
'A0618 explicitly gives Q_previous=−sum_v W_v, computes the opposite block form without changing source sign, and constructs KMS_1 by the groupoid/Haar measure identity without an RH assumption.',
'Actual signed arithmetic control is still missing; the sign and KMS dependency themselves are repaired rather than abandoned.',
'The existence of KMS_1 is not an RH conclusion, and this is established through the construction. The sign correction does not turn any previous positive Q_previous value into a counterexample.',
'Preserve the exact A0618 source scalar and convolution convention in every later comparison. Do not reopen the resolved sign discrepancy or treat KMS-state existence as the desired weight theorem.',
'completed repair; retain as authoritative early sign dictionary')

add('EC12B','A0618',[2352,2696],
r'**At this arrow, \(\beta\) is unchanged.**',
'U0012 requests the full Shimura version and an exact morphism after every nonidentity claim.',
'Full datum (G,X,V,M,L,K,K_M), quotient stack, determinant d_phi, level multiplicity m_K, operator-field cooling Pi, dual scaling theta_lambda and cyclic cokernel q_beta.',
'The response supplies the same-t dynamics inclusion of rank-one BC and computes Pi_(epsilon,H)(theta_lambda X)=Pi_(epsilon,H+log lambda I)(X). It retains the operator field and possible Dixmier–Douady twisting. q_beta delta_beta,0=0 is the exact cokernel factorization identity.',
'A specific NS input is not shown to lie outside the cooling image, and no global Shimura arithmetic pairing is supplied for every possible datum.',
'Only maps factoring through the specified cooling image have zero quotient. No assertion that every map factors that way is justified. This cannot erase the distinct Q or supported H1 of the later A_tau construction.',
'Compute the actual factorization or nonfactorization on the original source. In the late tau program use its derived res_sigma comparison and homotopy fibre, rather than substituting the generic stalk or an unrelated cooling cokernel.',
'completed typed maps and strictly scoped quotient obstruction')

add('EC12C','A0618',[2698,2818],
'**Its value has not been proved positive. Its factorization through—or survival modulo—the cooling image has not been proved either.**',
'U0011/U0012 request the actual source-to-arithmetic transfer, with unchanged viscosity, signs, domains, constants and action.',
'Unaveraged angular integral a_u; moving compact cutoff chi; T_chi(u)=(D_r²−1/4)(chi a_u); original NS equation and full W scalar.',
'Admissibility is proved by two integrations by parts, all four radial product terms and the full time derivative are retained, and the arithmetic composition is typed.',
'The displayed answer stops at an unspecified I and equations to prove: its physical/arithmetic action, quotient survival and signed scalar are not completed.',
'This identifies a genuine unfinished calculation. It does not establish impossibility, and the later tau model supplies a specific quotient/adjoint target that must be retained.',
'Completed in NS_CUTOFF_THETA_SCALING.md/.tex: full constant and variable scaling, retained viscosity, original two-leg action, all Mellin jets, residue dual, exact scalar invariance, and extra time-dependent force. The remaining actual-source estimate concerns changing anisotropic profile and cutoff, not pure transported dilation.',
'partly completed here; actual original-source analytic estimate remains')

coverage=[]
for h in heads:
    if 624<=h['line_start']<=2818:
        coverage.append({**h,'read_status':'read completely','coverage_class':classes[h['locator']]})
assert len(coverage)==len(classes)
chunks=[[624,803],[804,1013],[1014,1233],[1234,1453],[1454,1683],[1684,1913],[1914,2133],[2134,2358],[2359,2578],[2579,2818]]
assert [n for a,b in chunks for n in range(a,b+1)]==list(range(624,2819))
doc=dict(title='Early context local audit U0008–U0012',source=dict(path=SOURCE.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(raw).hexdigest(),line_count=len(lines)),read_coverage=dict(ranges=chunks,all_lines_read=True,method='complete contiguous displayed chunks; no keyword-only sampling'),coverage_nodes=coverage,passages=records,new_complete_calculation=dict(markdown='NS_CUTOFF_THETA_SCALING.md',latex='NS_CUTOFF_THETA_SCALING.tex'),limits=['This lane did not retrieve every sandbox-linked historical artifact. What a response says its linked notebook proves is recorded as a source claim, not an independent notebook audit.','Primary Tau_Base NOTE.md read completely; its hash checked by the parent and retained here.','Early segment predates A_tau and K_tau; their names are used for present continuation, not retroactively attributed to early responses.'])
(HERE/'audit_local.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

out=['# Early-context local audit: U0008–U0012','',f'Source SHA256: `{doc["source"]["sha256"]}`. Every line 624–2818 was read in the ten complete contiguous chunks recorded in `audit_local.json`. The retained early response text, not inaccessible historical sandbox notebooks, is the evidence audited here. The entire later Tau Base NOTE.md was also read to anchor the current continuation.','',
'The central unfinished early calculation is A0618’s actual cutoff-to-arithmetic action and survival calculation. The accompanying complete proof now supplies its exact dilation map into the original theta complex and full jets. This is supplementary context: the late accepted absolute-tau program remains the primary task. U0010 expressly withdraws the negative branch, so no redo prompt should revive it.','',
'## Complete local turn coverage','', '| Turn | Node | Chain | Lines | Classification |','|---|---|---:|---:|---|']
for h in coverage: out.append(f'| {h["locator"]} | `{h["node_id"]}` | {h["chain"]} | {h["line_start"]}–{h["line_end"]} | {h["coverage_class"]} |')
for r in records:
    out+=['',f'## {r["id"]}: {r["locator"]}, lines {r["passage_lines"][0]}–{r["passage_lines"][1]}','',f'Node `{r["node_id"]}`, chain {r["chain"]}. Status: **{r["status"]}**.','',f'> {r["quote"]}','',f'**User request.** {r["user_request"]}','',f'**Original objects and maps.** {r["objects_and_maps"]}','',f'**What was actually proved.** {r["what_was_proved"]}','',f'**What was left uncalculated.** {r["what_remained_uncalculated"]}','',f'**Exact scope.** {r["obstruction_scope"]}','',f'**Concrete continuation.** {r["concrete_next_derivation"]}']
(HERE/'AUDIT_LOCAL.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
users='\n\n'.join('\n'.join(lines[h['line_start']-1:h['line_end']]).rstrip() for h in coverage if h['role']=='user')
(HERE/'USER_INPUTS_LOCAL_VERBATIM.md').write_text('# Exact retained user inputs U0008–U0012\n\n'+users+'\n',encoding='utf-8')
print(json.dumps(dict(nodes=len(coverage),passages=len(records),exact_quotes_verified=True,line_coverage=[624,2818],output_files=['AUDIT_LOCAL.md','audit_local.json','USER_INPUTS_LOCAL_VERBATIM.md']),indent=2))
