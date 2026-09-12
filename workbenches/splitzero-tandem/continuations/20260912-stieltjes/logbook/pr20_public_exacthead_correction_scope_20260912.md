# PR20 exact-head public correction scope and merge handoff

This is a source-level correction audit for the existing public note at exact head `2144c358c2b41aa235b15cf0fa472289aec8673f`, based on the already retained complete five-blob remote verification and a fresh read of all 157 public-note lines. It is not a new claim about moving branch status. No remote branch, delivered source, builder, main TeX, or frozen appendix was edited. No Lean run was performed.

## Exact edition

Public Git path: `workbenches/tau-sum-connection/RESEARCH_NOTE.md`.

Exact public Git blob: `b6ce06a0270b00cb470bdd2823fc03fa91d895e6`.

Local byte-identical witness: `output/split_zero_rh_tandem_2026-09-12/sources/web_sum_connection_delivery/Tau_Sum_Connection_Control/PUBLIC_NOTE.md`.

Bytes: 10623. SHA256: `0221fa2e3e976874459c2a956cd953896522de3a7cd832125e70c2a4d59eb7c9`.

This audit recomputed the byte count, SHA256 and Git blob from the local public witness. The original source audit and `checks/sum_connection_delivery_replay/replay_receipt.json` retain verification of all five exact-head public blobs. Its base is `33b29f706008124886614ba4bd55bffc489df9e2`.

The expanded witness is a different object: full `NOTE.tex` has 32564 bytes and full `RESEARCH_NOTE.md` has 28995 bytes. The following corrections were initially found while reading those full editions. A correction in the expanded edition is not automatically a claim about the shorter public source.

## Four corrections, exact public applicability

| Expanded-source issue | Exact expanded locator | Public locator and finding |
|---|---|---|
| Local multiplication by h' was described as reading the input top coefficient | NOTE 476–477; full RESEARCH_NOTE 266 | The incorrect sentence is absent. Public 105–108 give the correct conormal row `(a_i) -> k^{-1}sum h_i'a_i`; 120–122 give its complete arithmetic unit and g' identification. No public repair for this issue. |
| Binomial free-module rank could be read as the derivative-image rank | NOTE 557; full RESEARCH_NOTE 318 | Public 133–141 give `gr_I P = E[eta_1,...,eta_k]` and the exact degree-minus-one operator `k^{-1}sum h_i' partial_eta_i`; they make no binomial derivative-image rank claim. No public repair for this issue. |
| Positive-degree monic freeness applied without explicitly separating h=1 | Full NOTE 131–133 states broad seed applicability; positive-degree division argument follows later | Public 17 says a finite packet, without the word nonempty. Public 101 asserts that P is free over `C[h(s_1),...,h(s_k)]` with basis `s^alpha`, `0<=alpha_i<d`. This proof statement requires `d>=1`. If finite packet includes the empty packet, that one sentence has a genuine boundary-case defect. Restrict the displayed freeness proof to d>=1 and state the zero quotient case separately, or define the algebraic packet to be nonempty at line 17. |
| Bare derivative arrow was drawn with ordered-pair graph as target | NOTE (8.2), 666–669; full RESEARCH_NOTE 388–391 | Public 86 already retains the graph of `(j nabla c_P, N c_P)` and explicitly recovers the derivative by addition; public 69–72 proves this orthogonal decomposition. Public 53 also types the scalar pair-to-derivative map by addition. The bad arrow occurs only in the expanded source. No public repair for this issue. |

A further wording issue from the expanded source, inclusion of the scalar amplitude line in an arbitrary chosen polynomial frame, is not asserted in the public note. Public 57–72 defines its independent relative frame and connection directly. The public note therefore does not need the separate constant-polynomial-in-span hypothesis for an inclusion it does not claim.

## Exact boundary-case repair and proof

A replacement for public line 101 that preserves every stated object is:

> For d>=1, monic division proves the isomorphism: P is free over C[h(s_1),...,h(s_k)] with basis s^alpha, 0<=alpha_i<d; only degrees zero and one in the latter variables survive modulo I^2. For the empty seed h=1, I=P, so E, E^[2] and I/I^2 are zero and the displayed quotient and conormal maps are the unique zero maps; the analytic definitions and estimates above remain unchanged.

Here is the complete reason for both parts. For d>=1, the monomials `s^alpha prod h(s_i)^{q_i}`, with `0<=alpha_i<d` and `q_i>=0`, have distinct leading monomials `prod s_i^{alpha_i+d q_i}` with coefficient one. Every ordinary monomial reduces to a finite linear combination of these by monic division in the ordered variables. The leading monomial of a finite alleged dependence has a unique summand, proving linear independence. Hence P is free over the polynomial subalgebra in the h_i with that basis. Modulo I^2, the h-degree is at most one. Consequently `I/I^2` is the direct sum of k copies of E, with the exact map `(a_i) -> [sum h_i tilde a_i]` at public 98–99. Differentiating gives the stated row, because each differentiated coefficient is multiplied by h_i and vanishes modulo I.

For h=1, every h_i is 1, so I=P and I^r=P for every r>=1. Thus `P/I=0`, `P/I^2=0`, and `I/I^2=0`. Both the quotient and derivative maps are the unique map between zero modules. Every associated graded piece `I^r/I^{r+1}` is zero as well. In particular the exact sequence and E^k-to-conormal isomorphism remain correct in the zero case; the freeness sentence alone cannot be used there. Indeed its displayed basis would be empty, whereas P is nonzero over `C[h_i]=C`. This explicit zero-quotient morphism is the exact continuation of the original construction, rather than an assumption replacing a calculation.

The antecedent PR17 full witness explicitly says 'finite nonempty packet' at its NOTE line 132. Accordingly the public PR20 proof is mathematically sound on the inherited nonempty packet domain. Because PR20 line 17 states the scope afresh and the full PR20 continuation also uses the empty theta seed analytically, the explicit separation above prevents the next standalone reader from silently extending the positive-degree freeness claim to h=1.

## Exact maps behind the other corrections

For the local coefficient statement, write `h=q(z)z^m`, `q(0)!=0`, and `a=sum_{j=0}^{m-1}a_j z^j` in `C[z]/z^m`. Then `h'=q'(z)z^m+m q(z)z^{m-1}`. Therefore `[h'a]=m q(0)a_0 z^{m-1}`. The map reads a_0 and outputs the top surviving coefficient. For m=2 and q=1, it sends 1 to 2z and z to 0. The public conormal row at 105–108 gives exactly this map without the erroneous input description.

For higher layers, `I^r/I^{r+1}` is a free E-module on the h-monomials of degree r, of rank `binomial(k+r-1,r)`. This is the domain module rank. Its differential maps the monomial `a eta^alpha` to `k^{-1}sum_i alpha_i h_i' a eta^{alpha-e_i}`. Thus its image is the image of this actual matrix over E, not an unspecified module of that same rank. In the one-variable local case already calculated, the r=1 row can have one-dimensional complex image even when its E-domain has complex dimension m. Public 133–141 states only the correct matrix.

For the graph map, put `Z=partial_u(j c_P)`. Public 69 gives `Z=j(c_P'+Gamma c_P)+N c_P`; since `j^*N=0`, projection yields `Pi Z=j(c_P'+Gamma c_P)` and `(1-Pi)Z=N c_P`. The exact map from the derivative image to the ordered graph is `Z -> (Pi Z,(1-Pi)Z)`, with inverse `(Z_1,Z_2) -> Z_1+Z_2`. Composing addition with `-i U_k^{-1}` and the original full-jet map gives the asserted arithmetic map on the graph. This is precisely what public line 86 says. A bare derivative with graph codomain in the longer drawing requires this projection-pair arrow to be inserted; the public edition already contains it.

## Validation scope for the handoff

The delivered twenty-method checker was read in full before execution. The retained replay has twenty passing methods in normal mode and twenty in optimized mode, using the declared SymPy 1.14.0. Both deliberately added failing controls ran twenty-one methods and failed exactly the injected method, returning nonzero status. Those finite tests support their explicit identities; this source review supplies the proof and scope analysis above. They are not Lean certificates and do not establish a uniform arithmetic control bound or RH.

Conclusion for this exact head: the nonempty-packet algebra reviewed here is clean; three of the four expanded-source corrections are absent or already correctly resolved in the public source. The only public clarification identified is the d>=1 scope of line 101 and explicit h=1 zero case. If the note is required to cover the empty seed algebraically without relying on the inherited nonempty convention, make that concrete textual repair. This audit does not merge, mutate, or approve a moving head.

