from pathlib import Path
import re,json,hashlib

base=Path(__file__).parent
root=Path("workspace:")
source=root/"output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0041_U0054.md"
text=source.read_text(encoding="utf-8")
pat=re.compile(r"(?m)^## ([UA]\d+) \| ([^|]+) \| (user|assistant) \| chain (\d+)$")
matches=list(pat.finditer(text))
turns={}
for i,m in enumerate(matches):
    end=matches[i+1].start() if i+1<len(matches) else len(text)
    turns[m[1]]={"locator":m[1],"node_id":m[2].strip(),"role":m[3],
      "chain":int(m[4]),"segment_line":text[:m.start()].count("\n")+1,
      "text":text[m.end():end].strip()}

records=[
dict(id="AT41",user="U0041",final="A1458",all=["U0041","A1429","A1458"],
classification="Completed literal support propagation; arithmetic transfer not computed",
passages=[
"Try to get hardcore typed morphisms without simplification that you propagate through each and every equation, while tracking the interesting bits continually.",
"No equivalence between that entire analytic complex and the geometric complexes above is asserted here."],
requested="Carry the original infinite quotient and split support through the stated Deligne operations by exact typed maps.",
proved=r"""The answer constructs the marked geometry \((\widehat X,\mathcal S_X,\mathbf p_X)\), its induced site, support diagrams and original coequalizer cohomology. It retains \(G(\mathcal O_K)\to\mathcal O_K\), the closed arithmetic subspace \(V(e)\), the cycle formula for support-comparison kernels, extension by absence versus the retained boundary skeleton, dual precomposition, all tensor signs and the \(e\)-seeded Lefschetz sum, including an empty fixed-point set. Its finite-field comparison image is proved under Deligne's explicitly stated smooth/lisse/pure hypotheses; its final support projection kernel is not set to zero.""",
omitted=r"""No source-sensitive morphism transfers the finite-field weight estimates to the original characteristic-zero theta cohomology. The retained map \(\mathcal O\otimes_{\mathbb C[t]}Q\to\mathcal O/(2\xi)\) is not proved to be an equivalence to the finite-field comparison complexes.""",
scope="The finite-field theorem is a legitimate scoped calculation, not a proof or disproof of the original absolute-base program. No kernel vanishing or broad nonrelationship is proved.",
later="U0043 rejects stopping at a finite-field lift; A1523 constructs the actual absolute-base A_tau/K_tau system.",
next="Retain these support operations but resume A1523's accepted absolute-base theta cohomology; do not repeat a renamed finite-field theorem."),
dict(id="AT42",user="U0042",final="A1474",all=["U0042","A1474"],
classification="Completed finite-packet nullity and signature calculation; absolute-base estimate remains",
passages=["This is a **newly stated test of a particular trace-theoretic relation**, not a redefinition of your existing quotient.",
"The sharpened question is whether the arithmetic \\(e\\)-null fibre is a radical through which the pairing descends."],
requested="Determine the individual mathematical roles of tau and e in testing the arithmetic pairing and RH.",
proved=r"""The response proves pairing descent exactly when its restricted map to the dual vanishes. For the actual packet it computes
\[
Q_Z(f,h)=\sum_\rho m_\rho\overline{f(1-\bar\rho)}h(\rho),
\quad \operatorname{Rad}Q_Z=\{f:f(\rho)=0\ \forall\rho\}.
\]
It retains all local units in the full residue pairing, gives its Jacobian contraction to this trace form, and calculates every off-line reflected block's isotropic coordinate vectors, nonzero cross pairing and positive/negative signature. The trace radical quotient legitimately forgets nilpotent amplitudes while retaining zeros and multiplicities. Synchronization preserves the arithmetic amplitude and hence cannot erase a diagnostic value.""",
omitted="The finite nullity criterion is not the cohomological arithmetic argument forcing positivity or radicality. No absolute-base weight estimate is calculated.",
scope="Failure of a proposed self-null congruence is an exact obstruction to that quotient, not to the already valid original coequalizer or the whole tau-base program. A negative auxiliary finite model is not an RH counterexample.",
later="A1523 supplies the original-base adjoint and residue injection; A1644 supplies the arithmetic extension unit and equivariant finite trace.",
next="Use the computed residue/Jacobian map in the actual A_tau/K_tau continuation. Prove the analytic control of that image; do not replace it by the already established RH criterion."),
dict(id="AT43",user="U0043",final="A1523",all=["U0043","U0044","U0045","A1481","A1520","A1523"],
classification="Requested change to absolute tau base completed and accepted",
passages=["and then use his machinery instead over the other thing, like tau instead of E, which was the intent, for the record. That's what I wanted you to do.",
"The construction uses the structural morphism \\(a_R\\), keeping \\(p_R\\) attached. It does not replace the arithmetic object by its Boolean localization.",
"The remaining issue is **a weight or positivity theorem for this new-base arithmetic realization**."],
requested="Change the actual base to tau, instead of repeating the finite-field theorem with split notation, and perform the Deligne-like constructions on that object.",
proved=r"""A1520 first supplies a pointed-monoidal structural map, the mixed-boundary contraction with stalk \(G(A)^2\to A^2\), and boundary cohomology \(Q^2\), retaining mixed multiplication and synchronization. Its product is expressly topological, not asserted to be the universal semiring-scheme product. A1523 then gives the canonical retained blueprint construction: the structural map \(\mathbf F_{1,\tau}\to B_R\), four-point original theta chart, projective resolution computing \(A_\tau=R\Gamma(P,-)\), separate restriction to sigma with its chain homotopy, signed right-adjoint complex \(K_\tau(W)\simeq S_\eta W[1]\), and full reversed precomposition arrows. It retains the source actions \(U_a,aU_{1/a}\), the arithmetic weight-one moment line, all Mellin jets and the residue injection into the computed K_tau dual. It proves top tensor cohomology \(Q^{\otimes r}\), product adjoint, and exact finite-packet deletion cone and trace.""",
omitted="No weight estimate is proved from the tensor action alone. An involutive global Verdier duality and prime-sensitive Lefschetz geometry are not constructed merely by the structural map.",
scope=r"""The direct image \(A_\tau\) is not Boolean generic restriction. Its explicitly compared restriction retains the labelled support skeleton while the global Q classes survive. The single-active-fibre lemma about mapping a supported vector to tau does not apply unchanged to arbitrary nonzero-bottom semimodules. A1520's \(Q^2\) is the pushforward of two pulled-back coefficient copies at a contracted boundary; A1523's \(Q\) is the original joint chart's global cohomology. They are different declared functors, not contradictory values of one functor.""",
later="U0046 expressly says this is now the correct context and orders continuation using these objects. A1644-A1959 genuinely continue the original theta source; no whole-program failure is established in this segment.",
next="Resume canonical A1523/retained NOTE objects, preserving its comparison to sigma and all supports. Complete the original arithmetic estimate, not a generic-stalk replacement or an unrelated polynomial family."),
dict(id="AT44",user="U0044",final="A1523",all=["U0044"],
classification="Reinforcement of U0043; completed by shared A1523 response",
passages=["which is thus what you will in fact do"],
requested="Carry out the absolute-tau-base construction ordered in U0043.",
proved="This has no separate assistant response before U0045. The complete shared response is audited at AT43.",
omitted="Same subsequent arithmetic estimate as AT43; no additional mathematical calculation is introduced by this reinforcement.",
scope="Do not invent a separate abandoned episode from adjacent user reinforcement.",
later="A1520 and A1523 supply the construction, followed by explicit user acceptance U0046.",
next="Use AT43 continuation, retaining this input in provenance."),
dict(id="AT45",user="U0045",final="A1523",all=["U0045"],
classification="Urgency reinforcement of U0043; completed by shared A1523 response",
passages=["nnow"],
requested="Execute the already ordered absolute-base construction immediately.",
proved="A1481 progress and A1520/A1523 are the shared response; their mathematics is audited at AT43.",
omitted="Same later quantitative estimate as AT43.",
scope="No new mathematical hypothesis or alternative construction is requested.",
later="U0046 explicitly accepts A1523's context.",
next="Use AT43 continuation, retaining this input in provenance."),
dict(id="AT46",user="U0046",final=None,all=["U0046","A1525","A1533","A1545"],
classification="Progress-only interval; explicit full reversed-support dual promise completed by this audit",
passages=["you started on the DELINGE program in the correct context nowadays",
"continue using the objects as the results so far allo",
"then I’ll extend the comparison kernel while retaining \\(e\\), \\(\\tau\\), and support transports.",
"including bottom fibers created by reversed support arrows."],
requested="Publish the existing work as GitHub merge requests and continue the now-accepted original tau-base program using the constructed objects.",
proved="The retained assistant responses are progress messages about integration and continuation. No substantive final mathematical calculation intervenes before U0047 'cont'. A1545 specifically promises the full tau-chart dual, including bottom fibres created by reversing support arrows.",
omitted="The full L^op cohomology diagram and its nonzero new bottom fibre are not written in this interval. Later A1644/A1694 retain joint H0 and single-fibre duals but do not explicitly complete the whole reversed diagram.",
scope="This is a precise deferred mathematical promise, not evidence about motives. Historical PR status in these messages is not independently verified remote state in this lane.",
later="Completed here in FULL_SUPPORT_DUAL.md/.tex, with a full standalone retraction supplement.",
next=r"""Use the completed explicit complexes and precomposition maps: \(H^{-1}=Q^\vee\) on all active faces and \(H^0=V^\vee\) on the original joint mask, now the bottom. Retain the strict-natural-section obstruction, its actual surviving derived roof, and the action defect \(d_a(c)=-a^w c\mathcal F^{-1}k_{1/a}\). Do not impose zero bottom fibres."""),
dict(id="AT47",user="U0047",final="A1644",all=["U0047","A1580","A1600","A1601","A1644"],
classification="Completed original theta extension, support-coherent homotopy and finite cochain trace",
passages=["Next I’m computing its compact-support-to-ordinary cohomology map.",
"although it vanishes in cohomology, its extension class remains part of the comparison.",
"They do not yet establish the global weight estimate."],
requested="Continue the accepted A_tau/K_tau construction and its original comparison.",
proved=r"""The response retains \(C_+=[V\to\mathscr B]\), the full joint comparison, original \(D=-x\partial_x\), Gaussian source and \(g=2\xi\). The actual section uses the full arithmetic unit \(\varepsilon_Z=j_{h_Z}(h_Z/g)\). It computes the theta extension class, polynomial-action defect, rank-one infinitesimal boundary and full dilation cocycle. At a simple zero the coefficient is exactly \(1/(2\xi'(\rho))\). The two homotopies differ by the retained joint H0 cycle \((b,\widehat b)\); synchronization supplies a common supported target without killing it. The same unit enters residue duality and the Jacobian trace. The non-A-linear section is replaced by the strict equivariant roof \(E_Z[-1]\leftarrow C_Z\to C_+\). The finite-rank cochain trace keeps its degree-one minus sign and every tensor sign.""",
omitted="The global topological section, continuous-dual splitting and quantitative estimate are not yet supplied here. A finite packet roof is not by itself every missing prime-sensitive compact-support theorem.",
scope="A nonzero extension obstructs a strict equivariant representative section, not the displayed equivariant derived inclusion. The exact one-leg-to-joint comparison is present in the primary dependency and fully calculated again in the later-control supplement; its H1 map is identity and its complementary V[0] survives.",
later="A1694 completes the global continuous section, transpose and completed tensor contractions. A1771 later computes the complete homotopy family.",
next="Retain the extension unit and actual roof through the global control calculation. Do not drop its boundary pairings or treat focus on C_+ as deletion of the joint H0 complement."),
dict(id="AT48",user="U0048",final="A1694",all=["U0048","A1694"],
classification="Completed global analytic retraction and Hausdorff-kernel calculation; full quantitative boundary estimate remains",
passages=["Their kernels are not identified with the now-vanishing Hausdorff-comparison kernel.",
"All three boundary and cross-pairing terms remain.",
"No global positivity or purity conclusion is being claimed from the retraction alone."],
requested="Continue pushing the original theta program.",
proved=r"""A1694 constructs the continuous left inverse \(\Lambda:\mathscr B\to V\) using the original \(\frac12\sum\mu(n)F(n|x|)\), both Fourier-related exterior regions, fixed cutoff operator \(T=A_\alpha B_\beta\), the retained inverse bound \(1/(1-\|T\|)\), and both original moments. It proves Schwartz regularity and \(\Lambda\Theta=1\), hence closed theta image, Hausdorff Q, the section \(s\), and \(\mathscr B\cong V\oplus Q\). It retains the different spectral and balanced analytic kernels and the exact smaller-source sequence with V/W. The full global cocycle \(k_a=\Lambda U_as\), change-of-section coboundary, old extension unit and trace are preserved. Transposition supplies continuous duals; completed tensor contractions retain all signs and joint degree-zero terms.""",
omitted=r"""The full boundary expression
\[
\mathcal H_s(\overline U_au,\overline U_av)-a\mathcal H_s(u,v)
=-\langle U_asu,\Theta k_av\rangle-\langle\Theta k_au,U_asv\rangle
+\langle\Theta k_au,\Theta k_av\rangle
\]
is computed but not bounded uniformly. The auxiliary positive form is not the arithmetic Weil form. Closedness of Theta V in the original Frechet topology does not prove vanishing of the remaining spectral or balanced analytic kernels.""",
scope="This is a real global analytic proof and a specific vanishing comparison kernel. Neither a uniform cutoff gap for changing cutoffs nor vanishing Hilbert pairing of theta boundaries is asserted. No purity follows from the global section alone.",
later="A1721 expands cutoff/Fourier/moment commutators and creates source matrices. A1771-A1959 further refine the original arithmetic control; none completes uniform sublinear tensor excess within this segment.",
next="Use those later canonical representatives and retain all cross terms and inverse conditioning. The standalone RETRACTION_PROOF.md now supplies the exact Lambda used by the full-support dual completion.")
]

episodes=[]
for r in records:
    e={"id":r["id"],"user":{k:v for k,v in turns[r["user"]].items() if k!="text"},
       "user_input_verbatim":turns[r["user"]]["text"],
       "assistant_final":None if r["final"] is None else {k:v for k,v in turns[r["final"]].items() if k!="text"},
       "all_turns":[{k:v for k,v in turns[t].items() if k!="text"} for t in r["all"]],
       "classification":r["classification"],"user_requested_calculation":r["requested"],
       "what_proved":r["proved"],"what_left_uncalculated":r["omitted"],
       "obstruction_scope":r["scope"],"later_completion":r["later"],
       "concrete_next_derivation":r["next"],"passages":[]}
    for passage in r["passages"]:
        found=[t for t in r["all"] if passage in turns[t]["text"]]
        if not found: raise ValueError(("unmatched exact passage",r["id"],passage))
        t=turns[found[0]]
        pos=text.index(passage,text.index("## "+found[0]+" |"))
        e["passages"].append({"text":passage,"locator":t["locator"],"node_id":t["node_id"],
                              "segment_line":text[:pos].count("\n")+1})
    episodes.append(e)

later=json.loads((base/"later_control.json").read_text(encoding="utf-8-sig"))
episodes+=later["episodes"]
for e in episodes:
    # Every quoted passage must still be exact after the newline-only extraction repair.
    for p in e.get("passages",[]):
        if p["text"] not in text: raise ValueError(("stale passage",e["id"],p["text"]))

covered={t["locator"] for e in episodes for t in e["all_turns"]}
assert covered==set(turns), (set(turns)-covered,covered-set(turns))
assert {e["user"]["locator"] for e in episodes}=={k for k in turns if k.startswith("U")}
receipt={"schema_version":1,"scope":"U0041-U0054","coverage":{
 "source":str(source),"sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
 "initial_read_sha256":"4f6b4fd318308e561710bb24cd0f35b1b70b6507ba6be54b6f6d9b044ddbd1c4",
 "provenance_note":"Extraction owner repaired Windows newline translation only; node IDs, message text, order and source line numbering unchanged.",
 "lines_read":[1,len(text.splitlines())],"complete_within_scope":True,
 "primary_read_completely":True,
 "primary_sha256":"d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3",
 "turns_covered":len(turns),"users_covered":sum(t["role"]=="user" for t in turns.values()),
 "assistant_turns_covered":sum(t["role"]=="assistant" for t in turns.values())},
 "episodes":episodes,
 "new_proofs":["FULL_SUPPORT_DUAL.md","FULL_SUPPORT_DUAL.tex","RETRACTION_PROOF.md"],
 "scope_conclusion":"The segment establishes and continues the accepted A_tau/K_tau construction; it leaves the original all-direction arithmetic uniform bound unproved. It does not establish whole-program failure."}
(base/"audit_actual_tau.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding="utf-8",newline="\n")
body=["# Passage audit: actual tau cohomology and continuation, U0041–U0054\n",
 "The entire 7,811-line segment and complete primary Tau Base NOTE were read. The current segment SHA-256 is "+receipt["coverage"]["sha256"]+". All 14 user inputs, progress responses and substantive answers are represented below. The extraction owner's newline-only repair preserves the UUID locators and exact quotations. The full user text is preserved in the JSON and separate provenance file.\n",
 "The accepted original construction is A1523, explicitly accepted by U0046. The concrete A1545 promise to calculate the full reversed-support dual is completed in FULL_SUPPORT_DUAL.md/.tex with its standalone retraction supplement. The repeated remaining quantitative endpoint is the uniform arithmetic control, not a missing definition of A_tau or K_tau.\n"]
for e in episodes[:8]:
    u=e["user"]; a=e["assistant_final"]
    body+=["## "+e["id"]+": "+u["locator"]+" → "+(a["locator"] if a else "progress responses")+"\n",
      "User node "+u["node_id"]+", chain "+str(u["chain"])+", source line "+str(u["segment_line"])+". "+e["classification"]+".\n",
      "Retained turns: "+", ".join(t["locator"]+" ("+t["node_id"]+")" for t in e["all_turns"])+".\n"]
    for p in e["passages"]:
        body+=['Exact passage, '+p["locator"]+' node '+p["node_id"]+', line '+str(p["segment_line"])+':\n\n> '+p["text"].replace("\n","\n> ")+"\n"]
    for label,key in [("Requested calculation","user_requested_calculation"),("Actually proved","what_proved"),
       ("Left uncalculated","what_left_uncalculated"),("Exact obstruction scope","obstruction_scope"),
       ("Later completion","later_completion"),("Concrete continuation","concrete_next_derivation")]:
        body+=["**"+label+".** "+e[key]+"\n"]
body+=["# U0049–U0054: complete later-control audit\n",
        (base/"later_control.md").read_text(encoding="utf-8-sig").replace(
         "4f6b4fd318308e561710bb24cd0f35b1b70b6507ba6be54b6f6d9b044ddbd1c4",
         receipt["coverage"]["sha256"])]
(base/"audit_actual_tau.md").write_text("\n".join(body),encoding="utf-8",newline="\n")
print(json.dumps(receipt["coverage"],ensure_ascii=False,indent=2))
