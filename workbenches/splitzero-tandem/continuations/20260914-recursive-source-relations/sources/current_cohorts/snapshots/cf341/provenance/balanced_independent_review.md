# Independent adversarial review of the balanced kernel and derived packet comparison

## Verdict and repair status

The full-source assertions BK.1–BK.23 and DP.1–DP.5 are mathematically correct on their specified original objects. The original draft's extension of DP.2 to **every** admitted source fibre was false. An actual proper-label counterexample, using only the original Gaussian and its literal dilation, has now been proved completely in `proper_label_spectral_kernel.tex` (PL.1–PL.15).

The root author's subsequent repair was read in full: BK.24 and DP.6–DP.8 correctly retain the exact proper-label transition kernel, and the previous universal-fibre wording has been replaced by the specified full-source comparisons. These repairs resolve the blocking scope defect. No author's file was edited by this reviewer.

The only additional clarification recommended is an explicit bridge from the original dilation action to multiplication by `a^s`; the computation is given below. This is an exact action clarification, not an additional arithmetic hypothesis.

## Files and source material read

- `segment29_40/original_balanced_kernel.tex`, full initial proof and its revised ending through BK.24.
- `derived_packet_comparison.tex`, full initial proof and subsequent repaired ending DP.6–DP.8.
- `turns/A1427.md`, especially its exact `O tensor_C Q -> O tensor_A Q -> O/(g)` comparison and source-label enlargement.
- The original `output/split_zero_rh_tandem_2026-09-12/tex/arithmetic_input.tex`, including A1–A19.

An independent secondary reviewer separately checked BK.8–BK.23 and DP.1–DP.5. Both reviews agreed on the full-source validity and the proper-label defect. No Lean process was started.

## Analytic verification

1. **The full-plane `H_phi` is entire.** Even smooth Taylor subtraction at the origin gives meromorphic continuation of `M_+ phi` with at most simple poles at negative even integers. The zeros of `1/Gamma(s/2)` cancel those poles. At `s=0`, the retained condition `phi(0)=0` eliminates the original Mellin pole, while `s Gamma(s/2) -> 2`; there is no remaining singularity. At `s=1`, evenness and the retained full integral condition give `M_+ phi(1)=0`. The coefficient at that removable point is exactly `H_phi(1)=2(M_+ phi)'(1)`. No missing factor of two or sign was found.

2. **Full-plane Euler inverse on the target.** The upper and lower integral representations in BK.5 have the stated exponents and denominators. They give the full strong Schwartz estimates on the zero-Mellin kernel. Euler differentiation preserves those estimates. The only homogeneous solution is `c x^(-rho)`, excluded by the target's decay requirements unless `c=0`.

3. **Source inverse for positive real part.** The lower integral `-integral_0^1 u^(rho-1) phi(xu) du` is smooth and even across zero, with its retained value zero. Differentiation adds `u^k`; domination is valid since `Re(rho)+k>0`. The upper integral gives Schwartz decay at infinity. For `rho != 1`, the source integral is recovered from `(1-rho) integral psi=integral phi=0`.

4. **The endpoint `rho=1`.** The identity `M_+(S_1 phi)(s)=M_+phi(s)/(s-1)` gives `integral_R S_1 phi=2(M_+phi)'(1)=H_phi(1)=0`. The proof does not divide by `1-rho` at the endpoint. This part closes the endpoint that the original strip-only A6 had not covered.

5. **Fourier reflection sign.** With the stated Fourier convention, `F D=(1-D)F` and `F^2=1` on even functions. For `lambda=1-rho`, `(D-rho)(-F S_lambda F)=F(D-lambda)S_lambda F=1`. Thus the minus sign in BK.7 is required and correct. The reflection also covers `rho=0` via the already-checked `lambda=1` endpoint. No negative-even source coordinate has been silently excluded.

## Algebraic verification

1. Iteration of the exact first-order ranges computes the full jets for every nonconstant polynomial. The resulting inverse is independent of factor order by injectivity of the polynomial operator.
2. The source jet map is onto from the original `H_{P(D)phi_*}=P`. The target jet map is onto from independence of the explicitly retained exponential-polynomial moment functions; the differential-operator proof in the draft is valid.
3. The connecting arrow in BK.11 is the actual snake map `h(D)F=Theta phi -> j_h H_phi`. Its injectivity, independence of representatives, and explicit inverse using `S_h Theta(P(D)phi_*)` all check.
4. The torsion-free PID argument proves flatness of `O` as an `A`-module. Its use on both kernels and cokernels is justified.
5. The actual torsion map under `b` is `[v] -> [(g/h)v]`. The full unit `u/a`, the powers `z^(m-n)`, and the cases `m=0` or `n=0` are all correct. No local unit has been replaced by its value or deleted.
6. BK.17 with the two isomorphisms in BK.14 proves both injectivity and surjectivity of every nonzero polynomial on the full-source `K`. The extension of scalars to `Frac(O)` follows from actual invertibility of every nonzero germ.
7. The local splitting is canonical: the inverse of `b` on `M[z^m]` is uniquely determined, and the kernel has no `z`-torsion. The argument identifies all torsion of `M`, including complete repeated-zero blocks.
8. The Gaussian `F_0(x)=exp(-(log x)^2)` belongs to the actual target space; its entire Mellin transform is exactly `sqrt(pi) exp(s^2/4)` and is nowhere zero. Given the explicitly stated Hardy infinite-zero theorem, any polynomial relation `P(D)F_0=Theta phi` forces `P=0`. Flatness therefore really does give `g tensor q_0 != 0`, and the written cycle `g tensor F_0-H_0 tensor Theta phi_*` represents it.
9. Both `Hom_A(E,K)=0` and `Hom_A(K,E)=0` for finite-dimensional `E` follow from the two directions of polynomial invertibility. The qualification about arbitrary subquotients of proper submodules is necessary and correctly retained.

The nonzero-Gaussian argument imports the named classical Hardy theorem; it does not prove that theorem internally. This is a declared actual arithmetic input, not an RH assumption. A distribution claiming to contain an internal proof of every imported arithmetic theorem should retain the actual Hardy proof or another complete proof that `g` has infinitely many distinct zeros. This review does not reclassify a citation as an internal proof.

## Derived verification

DP.2 is correct for `M=O tensor_A (B/Theta V)`. Tensoring the two-term free resolution of `O/(h)` gives exactly `[K --h--> K]`, `[M --h--> M]`, and `[O/(g) --h--> O/(g)]`. The first complex is acyclic because the actual multiplication by `h` is invertible on the full-source `K`. Both the degree-minus-one kernel and degree-zero quotient therefore survive bijectively.

The formulas for the shorter and longer thickenings in DP.4 retain the complete actual zero order. DP.5 is the Taylor action of multiplication by `a^s` on the retained arithmetic local algebra, with every nilpotent power present.

The repaired DP.6 is the exact balanced source-label transition. Applying the same resolution to `0 -> L_W -> K_W -> K -> 0` proves the repaired DP.7 and DP.8, since its quotient complex on `K` is acyclic. These are valid exact repairs.

## Blocking finding in the original draft: proper labels

The initial DP conclusion asserted the derived quasi-isomorphism in every original supported fibre. Original fibres may have different admitted invariant source spaces, so this does not follow from a proof for the full `V`.

The counterexample now proved in PL.1–PL.15 retains an admitted label that already contains the original arithmetic generator:

`psi(x)=phi_*(2x)`, `H_psi(s)=2^(-s)`, and `W=A phi_* direct-sum A psi`.

For every complex `rho`, the actual full-plane inverse gives

`chi_rho=S_rho^V(psi-2^(-rho)phi_*)`, with `H_chi_rho=(2^(-s)-2^(-rho))/(s-rho)`.

The two exponential-polynomial coefficients are independent, proving both `W` is free of rank two and `chi_rho` is not in `W`. Therefore the actual class `[Theta chi_rho]_W` is nonzero, is killed by `t-rho`, and maps to zero under Mellin evaluation modulo the unchanged `g`. Flatness preserves its nonzero copy of `O/(s-rho)` at the stalk `rho`. This directly refutes the claimed polynomial invertibility on that proper-label kernel and the corresponding derived quasi-isomorphism.

The exact relation to the valid full-source theorem is

`0 -> V/W -> Q_W -> Q -> 0`,

`0 -> O tensor_A(V/W) -> M_W -> M -> 0`, and

`0 -> O tensor_A(V/W) -> K_W -> K -> 0`.

The explicit torsion class is killed by the specified source-label transition to `V`, at the supported zero of that fibre. It is not sent to external absence. The proof neither exhibits an off-critical zero nor relies on one.

## Exact dilation-action clarification

Define the actual dilation by `R_aF(x)=F(x/a)` and the identical formula on the source, for real `a>0`. It preserves both original spaces and their source moments. Direct differentiation gives `D R_a=R_a D`; termwise substitution in theta gives `Theta R_a=R_a Theta`; the Mellin change of variable `x=ay` gives `M(R_aF)(s)=a^s MF(s)`.

Thus `beta` intertwines the induced dilation on `M` with multiplication by `a^s` on `O/(g)`. It induces the same action on finite derived observations because DP.2 is a quasi-isomorphism and the intertwining holds on both terms of the resolution. This proves the asserted arithmetic action without assuming that polynomial balancing alone identifies the two actions on all of `M`. Their difference on the full `M` can lie in `K`.

At a smaller label, an actual dilation acts within that label only if it preserves its admitted source; otherwise it has its specified transport to the dilated source label. Multiplication by holomorphic germs on the balanced modules remains an internal action regardless. These two domains of action should not be conflated.

## Provenance

Delegated review request (verbatim):

> Independent adversarial mathematical review needed, bounded: read FULL proof module work/rh_counterfactual_20260913/shared_thread_audit/segment29_40/original_balanced_kernel.tex and root derived_packet_comparison.tex. Verify every claim esp H_phi entire all complex plane, Euler inverse at rho1/Fourier reflection sign, all-polynomial snake maps, balanced kernel field structure/canonical local splitting and explicit actual nonzero Gaussian class. Read original arithmetic_input.tex and source conversation A1427.md as needed. No assumed missing theorem or model substitution. Check DP derived tensor conclusion matches proved BK. No Lean. Write work/rh_counterfactual_20260913/shared_thread_audit/balanced_independent_review.md with precise blocking findings/repairs. Do not edit author's files initially; message urgent issues.

Follow-up proof request (verbatim):

> Excellent catch. Please write FULL proved original proper-label example incl exact arithmetic ψ dilation constant Hψ=2^-s, A-linear independence and χ∉W exponential-polynomial proof, exact source-label transition to fullV killing [Thetaχ], and its polynomial-torsion interpretation. Root will scope DP final paragraph to the three original full-V mask fibres (single ± /joint), not arbitrary admitted W, and append full typed transition 0→V/W→Q_W→Q→0 under balanced flatness to relate general labels. Your example is valuable new adversarial continuation, not a model substitution. Own proof module proper_label_spectral_kernel.tex prefix PL; no remote edits.
