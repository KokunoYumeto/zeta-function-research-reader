# Review and integration of the accepted tau-base scaling, reflection, and unit gauge

13 September 2026. This is a bounded review and exact dependency intake, not a new proof lane. The full accepted scaling proof, full reflection proof RW1–RW23, full formal-unit proof UG1–UG19, and their prose reviews and final acceptance records were read. Their named source interfaces are retained locally, with all copied bytes and hashes recorded in `REMOTE_INTAKE_MANIFEST.json`.

## 1. Disposition and the resolved source correction

The actual theta, exponential-flow, reflection, right-adjoint, and formal-unit maps checked below are mathematically consistent with the original `A_tau` and `K_tau`. The requested original scaling proof had one narrow domain defect in Section 6: after fixing arbitrary real `p>0`, its separate global algebraic curve map `z -> z^p` required an integer exponent. The owner corrected this paragraph during the review. Both versions are retained:

- Requested accepted original: `f1_scaling_frobenius/ACTUAL_TAU_SCALING_AND_EXPONENTIAL_FLOW.md`, SHA256 `209385837d3fbdc72b1f0d1164c9f6b261f312243f4427befe7148729f934029`.
- Current owner-corrected version: `f1_scaling_frobenius/ACTUAL_TAU_SCALING_AND_EXPONENTIAL_FLOW_DOMAIN_CORRECTED.md`, SHA256 `4e4cb66e3cbbff6379ae389ddaaad65045ac0ed380f17a87ac7c4241c45e6c08`.

The verified delta only restricts that curve-map paragraph to positive integer `p` and adds its correction record. The theta dilation, full-jet action, finite flow, and moment line remain defined for every real `p>0`. For the curve map, `n>=1` gives the ring map `C[z] -> C[z]`, `z -> z^n`, with pullbacks `dz/z -> n dz/z` and divisor depth one to depth `n`. Nonintegral powers do not define this global algebraic map. This issue is now resolved in the corrected retained version; it does not concern the original theta action.

The reflection proof remains exactly SHA256 `111f4c3ea74fa3985352d4a29a65826ee10c883c18de20230f54a7b9f15472f2`. No further mathematical error was found in its stated maps. Its final mention of the direct arithmetic unit is an inclusion-coordinate reminder; the precise residue-conversion direction is the inverse unit, now explicitly carried by accepted UG19 below.

## 2. Connection to the actual absolute-base complex

The common original object is

\[
C=\mathsf A_\tau(\mathcal T)
=[V\oplus V\xrightarrow{\Theta(v-\widehat w)}\mathscr B],
\quad H^0(C)=\{(\widehat w,w):w\in V\},\quad H^1(C)=Q.
\]

The accepted scaling map is the sheaf/chain automorphism

\[
U_p^0(v,w)=(U_pv,pU_{1/p}w),\qquad U_p^1F=U_pF,
\quad U_pF(x)=F(x/p).
\]

Its inverse convention is `L_p=U_(1/p)`, with second leg `p^(-1)L_(1/p)`. The identity `Fourier(U_p w)=p U_(1/p) Fourier(w)` verifies the original differential and second-leg scalar. The support masks remain fixed, and the sigma stalk only records the support skeleton. These maps act on the global pushforward; they do not replace that pushforward by restriction to sigma.

For the full original arithmetic packet, `J_Z U_p=p^A J_Z` and `J_Z L_p=p^(-A) J_Z`, where the entire action on every full local algebra is

\[
p^{\pm A}|_\rho=p^{\pm\rho}
\sum_{j=0}^{m_\rho-1}\frac{(\pm\log p)^j}{j!}N_\rho^j.
\]

The accepted finite source correction `K_a`, with `a=log p`, is exactly the source integral `c_(-a)` in the local proof `theta_scaling_cocycle.md`: substitute `r=-s` in its oriented integral. Thus

\[
L_pR_{\rm ref}-R_{\rm ref}p^{-A}=\Theta K_{\log p},
\quad H^+=(K_{\log p},0),\quad H^-=(0,-\widehat{K_{\log p}}).
\]

The relation between the accepted remote result and the locally evaluated incomplete-gamma formula is an exact change of time parameter. The local proof supplies its quantitative Schwartz estimates and its finite/global section bridge. The original joint degree-zero group and support-face homotopy difference remain present in this comparison.

## 3. Exact exponential-flow and reflection maps already completed

The retained polynomial family has differential `D_(u,t)=u partial_S+chi(S)-t`, with its original monic polynomial and full coefficient basis. The accepted commutator calculation `[D,L]=0` for `L=u partial_t-S` gives the actual formal cochain map

\[
\exp(aL)P(u,t,S)=e^{-aS}P(u,t+ua,S).
\]

This is an `a`-adic cochain map. The finite cohomology matrix is an entire, invertible map with the exact fibre direction

\[
C_a(u,t):H_{u,t+ua}\longrightarrow H_{u,t},\qquad
\partial_aC_a=-C_aA(t+ua),\quad C_0=I.
\]

The accepted period equation gives `C_a=Pi(u,t)^(-1) Pi(u,t+ua)` when `u!=0`. Its special-fibre action is `C_a(0,0)=exp(-aA)`, so `a=log p` gives the literal `L_p=U_(1/p)` action on the same coefficient packet. The fixed-fibre period conjugate `Pi p^(-A) Pi^(-1)` is also retained with its own endpoints. These two maps are not identified away from their stated common special-fibre coefficient action.

For the original symmetry-stable cyclic tensor packet, reflection has coefficient matrix `R:P(S)->P(k-S)`, parity `epsilon=(-1)^q`, and parameter map `r(u,t)=(-epsilon u,epsilon t)`. The verified cochain components are `epsilon R` in degree zero and `R` in degree one. Their exact finite flow relation is

\[
RC_a(u,t)R=e^{-ka}C_{-a}(-\varepsilon u,\varepsilon t),
\quad Rp^AR=p^kp^{-A}.
\]

The source constant `Phi(k)` remains in the horizontal contour gauge `exp((Phi(k)-kt)/u)R`; the reflected contour has the displayed one-form minus sign. The regular finite identity above extends over the special fibre without assigning a value there to that essential exponential. The accepted proofs already calculate all these maps; this review does not substitute a frozen matrix flow or delete a nilpotent block.

## 4. The actual tau-base right adjoint and residue units

The original adjoint is

\[
K_\tau(W)=[I_\eta(W)\xrightarrow{(+\mathrm{res},-\mathrm{res})}
I_+(W)\oplus I_-(W)],\quad\text{degrees }-1,0,
\]

with `RHom(T,K_tau(W))=RHom(A_tau(T),W)`. Its k-fold form has the source shift `K_(tau,k)(L_k) ~= S_(eta,...,eta)L_k[k]`. The actual moment line is `U_p:L_k -> L_k`, multiplier `p^k`. Hence its degree-minus-k dual action is

\[
(U_p\lambda)(v)=p^k\lambda(U_p^{-1}v).
\]

On the full finite coefficient dual this is `p^k(p^A)^(-T)`. The accepted family transport

\[
(T_a^\vee\lambda)(t)=e^{-ka}C_a(u,t)^{-T}\lambda(t+ua)
\]

has exactly that inverse-dilation special fibre. Its evaluation identity and generator `u partial_t+A(t)^T-kI` were checked against the original moment line and the shifted endpoints. The finite polynomial residue matrix `S` and `J=R^T S` satisfy the accepted identity `A(t)^T J+J A(epsilon t)=kJ`; this transports the stated bilinear coefficient pairing, not an assigned positive metric.

For raw one-packet coefficient arguments, the precise arithmetic residue join is

\[
R_Z(f,v)=\mathscr S_h(f^\dagger,\epsilon_hv),\qquad
\epsilon_h=j_h(h/g)=\upsilon_h^{-1},\quad
\upsilon_h=j_h(g/h).
\]

This is the direction used in scaling Section 4 and in accepted UG19. The direct unit `upsilon_h` belongs to the source's literal cyclic inclusion `eta[P]=upsilon_h^(tensor k)P(sum A_i)1`. Both maps and both units remain in the composed arrow. The existing finite residue-dual map to `K_tau(L_1)` and its tensor/cyclic restriction therefore use the same full Taylor coefficients, the same alternating dagger signs, and the same moment factor. No direct unit is substituted for its inverse in the raw residue formula.

## 5. Accepted formal gauge: completed scope and remaining analytic calculation

The full accepted formal proof is retained at `f1_unit_gauge/ACTUAL_TAYLOR_UNIT_FORMAL_GAUGE.md`, SHA256 `9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f`. Its independent final review is `e32e978870e65ea375040762432a3cfe479068ebe6cfd800086a2d35d55da6d0`, and its root acceptance is `ad39808a669eafba1e67793c91b4e320d9fc1426bf6194d83735227b052a0d1d`.

The accepted result is the actual formal quasi-isomorphism

\[
\widehat C\xrightarrow{i}\widehat C_\nu
\xrightarrow{\times\nu}\widehat C_\nu^\nu,
\quad \nu=\operatorname{rem}_h\upsilon_h,
\quad D^\nu=u\partial_s+h-t-u\nu'/\nu.
\]

Its pole module is the explicitly retained `M=C[s,nu^(-1)]/C[s]`. Multiplication by `h` is invertible on this module, and the ordered inverse

\[
J=\sum_{n\geq0}\bigl(-H(u\partial_s-t)\bigr)^nH
\]

contracts its quotient complex coefficientwise in `C[[u,t]]`. The completed rings allow denominator order to grow with the formal coefficient; no uniform denominator is silently imposed. The proper-rational section and the displayed `K=sigma J pi`, `r^0=I-KD`, `r^1=I-DK` prove the retraction. The gauge inverse up to homotopy is the actual `r M_(nu^(-1))`. These are proved operators, not assumed pole-kernel vanishings.

The same formal scaling generator commutes with the inclusion and multiplication by the full unit. The signed external-product contraction on cofinal rectangular truncations is explicitly given. At the special fibre it induces `M_(upsilon_h)^(tensor k)`; composition with the original cyclic sum inclusion is exactly `eta`, without making the tensor unit a function of the sum coordinate alone. UG19 uses the original reflection-stable packet for its dagger domain. Both earlier review comments about the tensor completion and dagger domain were resolved in the accepted text; neither remains an outstanding item.

**Actual remaining analytic calculation:** construct continuation or evaluation of this specific formal localization/gauge at nonzero complex `u`, calculate the additional `nu`-pole and contour contributions, and control the resulting comparison in the original theta Gram and relation-volume topology. The formal proof only establishes coefficientwise convergence of its ordered pole inverse. The entire finite matrix `C_a` does not by itself establish analytic convergence of `J` or an analytic localization equivalence. The completed formal localization, gauge, tensor, dagger, and special-fibre maps need not be requested again as missing work.

## 6. Retention and verification scope

There are 23 byte-verified retained source/evidence files, totalling 302,370 bytes before this review and its manifest. The manifest records every source locator, exact byte count, current SHA256, expected-pin match where supplied, and byte-for-byte target comparison. The requested pre-correction scaling bytes were recovered from the existing archived v19 intake after the owner updated its working copy; the corrected working copy was separately retained. No retained original was edited.

Nine direct source interfaces are copied in full under `source_interfaces`: the complete Tau Base note, arithmetic input, DS sidebar, XD determinant extension, original exponential note, translation bridge, primary-source correction, carrier definitions, and retained primary-source review. This supplies the local definitions and previously completed calculations actually invoked by the accepted notes. Standard published theorems remain cited in those files; no new literature theorem or full-paper inspection is claimed by this intake.

Read scope beyond the three accepted proofs: full supporting prose reviews and final acceptance; the previously completed full Tau Base/arithmetic reads; DS66–DS69 and XD12–XD22 for the exact family and period maps; complete primary-source correction and retained primary review. The source-interface files are retained completely even where this bounded review reread only those specified passages.

The accepted check scripts and their normal/optimized records are retained as supporting evidence. This task did not rerun them and does not report their prior successes as a new execution. No new Lean run, source-owner edit, shared-master edit, or remote publication was performed.
