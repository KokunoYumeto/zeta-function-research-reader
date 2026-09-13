# Complete source and proof audit: Toda volume control delivery

This audit accepts the displayed determinant, phase, curvature and finite-control identities with the exact hypotheses and typing recorded below. One scalar/vector notation error in the endpoint prose needs correction. Two coordinate/adjoint conventions and the quartet-only degree equality need to be explicit in the integrated continuation. The audit also computes the individual outgoing and incoming curvature costs; their shared positive term cancels in their difference. No supplied archive member was edited.

## 1. Exact delivery, reading, and execution provenance

Here `W` denotes the math workspace and `R= W/output/split_zero_rh_tandem_2026-09-12`. The untouched delivery is staged under `R/sources/web_toda_volume_delivery`; its directory is `Tau_Toda_Volume_Control`.

| Object | Bytes | SHA-256 |
|---|---:|---|
| Original ZIP | 677293 | `80b365233ba5ebaf1b52aeea369a7771d74bf774dbb4416f10a56503321b8f41` |
| NOTE.tex | 31153 | `027cd27a5fc104c5ebdf0102ee43aafd7b6218da4929ceb1b8913e3448cd2375` |
| RESEARCH_NOTE.md | 27659 | `a8254595424cada07ace61d113f6bd8ca4b653ccf5310912e679da4a2ffd473f` |
| check_toda_volume.py | 10732 | `3bc13763906a69f8b0b122bc082863f75cb7b96be3d20332a79c9a6049dbad19` |
| evaluate_seed.py | 1836 | `90e7b7fcd8dd6a93235893a28f3dad8b0860d2df4ca5e46aef6d4af5a541977a` |
| Internal manifest | 4696 | `bc0604eef22c48df7269c691c9064b4e385abdf96075014bd973d0661d57b757` |
| Exact pasted continuation | 20262 | `2108fcdb1c5fc3e9d3ee09aabf00c18080636a7910fa54136bbf3f72a37a0bbe` |

There are 36 file members, of which 35 are declared in the internal manifest; the manifest itself is the remaining member. Every declared byte count and digest was checked. The outer `LOCAL_STAGING_PROVENANCE.json` records every member independently, including the manifest. The staging script validates raw path components, absolute paths, drive/stream colons, backslashes, traversal, case-folded duplicate names, symbolic-link entries and resolved containment. Extraction uses explicit byte writes within the destination, with existing different bytes rejected. The exact source ZIP and pasted text are retained separately.

Complete mathematical reading covered both `NOTE.tex` and `RESEARCH_NOTE.md`, including all numbered equations (1)–(37), the initial scope, every proof paragraph, the formalization discussion and source references. The full pasted continuation was read. The four Python files were inspected in full: `check_toda_volume.py`, `evaluate_seed.py`, `build_reader.py`, and `check_reader.py`. README, HANDOFF, PROGRAMME_STATE, CHECKS, SOURCE_REVIEW, both source-receipt descriptions and the verification/numerical records were read. Current `R/tex/cyclic_control_determinant_increments.tex`, CV.1–CV.12 including CV.10a, was read completely for the comparison below.

The paste contains the mathematical continuation and no additional action request beyond the user's ongoing integration request. Instructions inside the archive's handoff are source data. The archive's PR 21 execution statements remain historical source claims at `2abc351424ba87aeda948a5cfb846e15ed9373d1`; this audit performs no Lean run or remote-CI verification and does not relabel that source report as a new execution.

Inspected computation was replayed in the separate directory `W/work/toda_volume_replay_20260912`. The script copies the exact checker and numerical evaluator before execution. It does not rebuild the supplied reader, overwrite the supplied source records, or modify a paper, publication stage or frozen release. `W/work/replay_toda_volume_20260912.py` and its `replay_receipt.json` retain the commands, modes, versions, individual result/log hashes and exact scope. Local Python is 3.13.9; SymPy is the pinned 1.14.0 and mpmath is 1.3.0. The original source reports Python 3.13.5, so these are separate local runs.

Results: normal and optimized runs each execute 24 methods with no failures or errors; both negative modes execute those same 24 plus a 25th deliberately failing method, with exactly one failure, no errors and exit code 1. Normal/optimized records agree, as do the two negative records. The numerical script reproduces the source's complete printed records at 50/70 digits and integer cutoffs 6/8. That numerical replay supplies no interval enclosure or omitted-tail certificate. No inherited exterior checker was rerun in this audit; its source receipts are preserved at their stated scope.

## 2. Fixed objects, coefficient maps, and analytical domain

Let `h` be a nonempty monic packet polynomial of actual zeros of `g=2 xi`, with each selected zero's entire order retained, stable under `s -> 1-conjugate(s)`. Put `d=deg h`, `E_h=C[s]/(h)`, `v_h=g/h` and `upsilon_h=[v_h] in E_h^×`. The full orders make `v_h` holomorphic and nonzero at every selected root, which proves this unit assertion. The original source is the inverse Mellin function `F_h`, with Mellin transform `v_h`; no value one is assigned to the unit.

Retain the original complex `C_+=[V --Theta--> B]`, its cohomology quotient `Q=B/Theta V`, `D=-x partial_x`, and

\[
g(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

At fixed tensor degree `k>=1`, set `c=k/2`, `S=sum_i s_i`, `I=(h(s_1),...,h(s_k))`. The cyclic annihilator is the original monic polynomial

\[
\chi(S)=\prod_{\lambda}(S-\lambda)^{\ell_\lambda},\qquad
\ell_\lambda=\max_{\sum_i\rho_i=\lambda}\left(1+\sum_i(m_{\rho_i}-1)\right),
\quad C_S=\mathbb C[S]/(\chi),\quad q=\deg\chi\ge1.
\]

The maximum includes all collisions of sums. On an ordered root component the nilpotent part is `z_1+...+z_k` in `C[z_i]/(z_i^{m_i})`; its power of degree `sum(m_i-1)` has the nonzero top coefficient `sum(m_i-1)!/product(m_i-1)!`, and every greater-degree monomial vanishes. This proves the local exponent, hence the stated maximum. The retained cyclic injection and arithmetic source are

\[
\alpha:C_S\hookrightarrow(E_h^{\otimes k})^{S_k},\quad[P]\mapsto[P(S)],
\qquad \eta=M_{\upsilon_h^{\otimes k}}\alpha,
\]
\[
\mathcal V P=P(D_1+\cdots+D_k)F_h^{\otimes k},\quad
J^{(k)}\mathcal V=\eta\pi_\chi,\quad
q^{(k)}\mathcal V=\sigma_h^{\otimes k}\eta\pi_\chi.
\]

The map `alpha` is a unital algebra injection; `eta` is the specified module injection. Multiplication by the original unit gives the exact relation between them. The norm calculation uses

\[
w_h(t)=\frac{|v_h(1/2+it)|^2}{2\pi},\quad
m_k=w_h^{*k},\quad \mu_h=\int_{\mathbb R}w_h(t)\,dt,
\]
\[
\|\mathcal VP\|^2=\int_{\mathbb R}|P(c+iu)|^2m_k(u)\,du,
\qquad\int m_k=\mu_h^k.
\]

The function `v_h` is nonzero entire, so its zeros on the integration line are discrete; `w_h` is positive almost everywhere. This already suffices for positive polynomial Grams. For `k>=2`, each convolution integrand is positive almost everywhere in its integration variables for every fixed sum, so `m_k(u)>0` at each real `u` where the integral is evaluated by its continuous version. No zero of the line restriction has been discarded from the source function.

The source's sufficient exponential bound is correct. Summation by parts of the alternating Dirichlet series on `Re s=1/2` gives `|eta(s)|<=C(1+|s|)`; its denominator has modulus at least `sqrt(2)-1`. Thus `zeta` has a polynomial bound of degree one there. The fixed-strip gamma estimate gives `|Gamma(1/4+it/2)|<=C(1+|t|)^(-1/4) exp(-pi|t|/4)` outside a compact set. This is the standard vertical-strip consequence of the gamma expansion in [DLMF 5.11](https://dlmf.nist.gov/5.11). Multiplying by `s(s-1)` and dividing by the original degree-`d` monic `h` gives exactly

\[
w_h(t)\le C_h(1+|t|)^{11/2-2d}e^{-\pi|t|/2}.
\]

Compact intervals cause no singularity because the selected zero factors have been removed with their complete orders. Every polynomially weighted differentiated Laplace integral therefore converges locally uniformly on `|Re theta|<pi/2`. In that strip,

\[
M_h(\theta)=\int e^{\theta t}w_h(t)\,dt,\quad
Z(\theta)=M_h(\theta)^k,\quad
Z^{(j)}(\theta)=\int u^je^{\theta u}m_k(u)\,du.
\]

The last formula follows from the full `k`-fold convolution integral and Fubini; no probability normalization or missing tensor mass is used. Positivity and the Hilbert spaces below concern real `theta` with `|theta|<pi/2`, while holomorphic differentiation concerns the complex strip.

## 3. Relation filter, determinant line, and higher-depth comparison

With coefficientwise conjugation denoted by an overbar, set

\[
Z_\chi=\overline\chi(c-i\partial_\theta)\chi(c+i\partial_\theta)Z.
\]

Each occurrence of `partial_theta` under the integral multiplies by the original variable `u`. Consequently, retaining both signs and all coefficients,

\[
Z_\chi(\theta)=\int|\chi(c+iu)|^2e^{\theta u}m_k(u)\,du>0.
\]

The typed linear observation is `L_theta(P)=int P(c+iu)e^{theta u}m_k du`, with `L_theta(SP)=(c+i partial_theta)L_theta(P)`. The preceding norm formula is the sesquilinear Gram observation of the source multiplication map, not an assertion identifying two scalar ideals.

Precisely, let `P_n=C[S]_{<=n}`, with `P_{-1}=0`. At `N>=q-1`, monic division gives the exact sequence

\[
0\longrightarrow\mathcal P_{N-q}\xrightarrow{M_\chi}\mathcal P_N
\xrightarrow{\pi_\chi}C_S\longrightarrow0.
\]

Injectivity of `M_chi` follows in the polynomial integral domain, its image is precisely the kernel by division, and all residue classes have unique representatives of degree below `q`. The image under `mathcal V` consists of the admitted theta relations. Its quotient map sends `(lambda_N,chi Q)` to `(lambda_N,0)` and sends external `tau` to `tau`; the original support label survives. The source multiplication map has Gram

\[
\langle M_\chi P,M_\chi Q\rangle_\theta
=\int\overline{P(c+iu)}Q(c+iu)|\chi(c+iu)|^2e^{\theta u}m_k(u)\,du.
\]

This proves exactly how the positive relation metric precedes its supported-zero observation. Its value is additional source information and is not reconstructible from only the zero quotient image.

For higher original depth, `K_r={P:P(S) in I^r}=(chi_r)`. The actual relationship to scalar powers is the quotient map

\[
\mathbb C[S]/(\chi_1^r)\longrightarrow\mathbb C[S]/(\chi_r)
\hookrightarrow\mathbb C[s_1,\ldots,s_k]/I^r.
\]

Indeed `chi_1(S) in I` implies `chi_1(S)^r in I^r`, hence `chi_r` divides `chi_1^r`; the kernel of the first map is `(chi_r)/(chi_1^r)`, and the second map is injective by the definition of the pullback. The original derivative `(1/k)sum partial_{s_i}` maps `I^{r+1}` into `I^r`, so it induces `delta_r`, and on a composed polynomial it gives `P'(S)` because its value on `S` is one. Thus `chi_r` divides `chi_{r+1}'`, proving the source-to-target compatibility of the derivative. For every retained multiplier `U`,

\[
\delta_r[UP(S)]=[UP'(S)]+[(\partial U)P(S)].
\]

The second term is retained in the full target. The Gram weight `|chi_1|^2` above changes none of these ideals, quotient maps or derivative terms.

Define the two moment determinants, including their empty values,

\[
\mathfrak D_n=\det[Z^{(i+j)}]_{0\le i,j<n},\quad
\mathfrak B_n=\det[Z_\chi^{(i+j)}]_{0\le i,j<n},\quad
\mathfrak D_0=\mathfrak B_0=1.
\]

A nonzero polynomial cannot vanish on the full-measure support of either positive measure, so both Grams are positive definite. The exact coordinate transformation is

\[
S^j=(c+iu)^j=\sum_{r=0}^j\binom jr c^{j-r}i^ru^r.
\]

On dimension `n` its determinant is `i^{n(n-1)/2}`. A Gram transforms by conjugate congruence, so its determinant multiplier is precisely one. All triangular coefficients and phases remain available in the map.

Expansion of both Vandermonde determinants in the integral, followed by Fubini, proves

\[
\mathfrak D_n=\frac1{n!}\int_{\mathbb R^n}\prod_{i<j}(u_i-u_j)^2
\prod_{j=1}^ne^{\theta u_j}m_k(u_j)\,d^nu.
\]

There are `n!` equal contributions for each permutation after relabeling variables, giving the displayed factorial. For `mathfrak B_n` the integrand additionally contains `product_j|chi(c+iu_j)|^2`. The mass scales as `(mu_h^k)^n` in the first integral.

Let `H_theta=L²(e^{theta u}m_k du)`. Multiplication by `e^{theta u/2}` is the exact onto isometry `H_theta -> H_0`, with inverse multiplication by `e^{-theta u/2}`. The images of the finite polynomial source are specified separately under that isometry; its image need not be a polynomial. At zero tilt the observation is the original arithmetic norm.

In fixed monic remainder coordinates let `J_N` be the reduction matrix and `M_N` the source Gram. Stars on these displayed coefficient matrices mean conjugate transpose with the fixed Euclidean coordinate pairing. The weighted adjoint of `J_N` into the source is `M_N^{-1}J_N^*`. Consequently

\[
K_N=J_NM_N^{-1}J_N^*,\quad G_N=K_N^{-1},\quad
\widehat R_N=M_N^{-1}J_N^*G_N.
\]

Direct multiplication gives `J_N Rhat_N=1`. Its image is orthogonal to the kernel of `J_N`, since `z^*M_N Rhat_N=(J_Nz)^*G_N=0`. Every other lift differs by a kernel vector, so Pythagoras proves uniqueness and minimum norm. The minimum Gram is `Rhat_N^*M_N Rhat_N=G_N`. The arithmetic realization is `R_N=mathcal V Rhat_N`, with fixed full jets `eta` and the fixed original class `sigma_h^{tensor k}eta` at every tilt.

In the ordered source basis `(1,...,S^{q-1},chi,...,chi S^{N-q})`, the basis determinant is one. The relation block Gram has determinant `mathfrak B_{N-q+1}`. Subtracting its orthogonal projections from the first `q` vectors is a triangular operation of determinant one, and the remaining Gram is `G_N`. Hence

\[
V_N:=\det G_N=\frac{\mathfrak D_{N+1}}{\mathfrak B_{N-q+1}}.
\]

This also proves the metric assertion for the determinant-line map: wedge the written relation columns together with the written quotient lifts in their fixed order, then use the orthogonal lifts to evaluate its norm. For `h=1`, `chi=1`, `C_S=0`, both determinants coincide and this ratio is exactly the zero-dimensional determinant one. The two-element split lift `{tau,e}` remains, while the analytic seed is nonzero.

## 4. Both Toda flows and the complete curvature maps

For either fixed positive base measure `dmu`, deform it by `e^{theta u}`. Let `Q_j` be the monic real orthogonal polynomials, and let `h_j` be their full squared norms. Multiplication by `u` is symmetric. Pairing `uQ_j` with `Q_l`, `l<j-1`, gives zero by orthogonality and degree. Leading coefficients and the pairing with `Q_{j-1}` therefore give

\[
uQ_j=Q_{j+1}+b_jQ_j+a_jQ_{j-1},\quad
a_j=h_j/h_{j-1},\quad a_0=0.
\]

The derivative of a monic `Q_j` has degree at most `j-1`. Differentiate its orthogonality with `Q_l`. For `l<j-1`, both the differentiated lower polynomial and `uQ_l` have degree below `j`, so the coefficient pairing vanishes. For `l=j-1`, the pairing is `-h_j`. Thus `partial_theta Q_j=-a_jQ_{j-1}`. Differentiating `h_j` makes its lower-polynomial derivative terms vanish, yielding `(log h_j)'=b_j`. Finally,

\[
b_j'=\frac{\int u^2Q_j^2e^{\theta u}d\mu}{h_j}-2a_j-b_j^2
=(a_{j+1}+a_j+b_j^2)-2a_j-b_j^2=a_{j+1}-a_j.
\]

Taking the product of the first `n` norms and telescoping proves

\[
(\log\mathfrak D_n)''=a_n,
\qquad \mathfrak D_n\mathfrak D_n''-(\mathfrak D_n')^2
=\mathfrak D_{n+1}\mathfrak D_{n-1},\quad n\ge1.
\]

The same proof applies to the fixed relation multiplier `|chi(c+iu)|²`; it is independent of the tilt. Set `omega_j=mathfrak D_{j+1}/mathfrak D_j`, `nu_j=mathfrak B_{j+1}/mathfrak B_j`, and `beta_m=nu_m/nu_{m-1}` for `m>=1`, with `beta_0=0`. Their original `S`-monic norms coincide with these norms through the phases `i^j`. For `m=N-q+1>=0` and `ell_N=log V_N`,

\[
\ell_N''=a_{N+1}-\beta_m,
\qquad a_{N+1}=\omega_{N+1}/\omega_N.
\]

At `m=0` the second term is zero because `log mathfrak B_0=0`. There is no negative-index determinant in this convention. These classical moment/orthogonal-polynomial identities are also situated in [DLMF 18.2](https://dlmf.nist.gov/18.2); the calculation here proves the particular identities and retains the actual measures.

For the matrix refinement, write `R:C_S -> P_N subset H_theta` for the polynomial minimum section, `D_N=chi P_{N-q}` for the boundary space, and `P_D,P_N` for the orthogonal projections in the current weighted Hilbert space. Put `Xf=uf` on the domain containing all polynomials. Differentiating `J_NR=1` gives `R'` in `D_N`. Differentiating `<d,Rx>_theta=0` for every fixed `d in D_N` gives `<d,R'x>_theta=-<d,XR x>_theta`. Therefore

\[
R'=-P_DXR.
\]

This is a genuine original boundary map. Write its polynomial value as `chi Q_x` by monic division and apply the retained factor-by-factor theta primitive; its jet is zero, and both Koszul primitive/differential signs remain the paired signs of the previous source construction. Its derivative does not change the target class.

The finite maps and their types are

\[
O_N=(1-P_N)XR:C_S\to\mathcal P_{N+1}\cap\mathcal P_N^\perp,
\qquad I_N=P_DXR:C_S\to\mathcal D_N.
\]

Hilbert adjoints into the fixed coordinate dual use the current weighted source product. Differentiating `G=R^*R`, including the change of measure, gives

\[
G'=R^*XR,\qquad G''=R^*X^2R-2R^*XP_DXR.
\]

The projection onto the image of `R` is `P_R=RG^{-1}R^*`. Since `P_N=P_R+P_D` as an orthogonal sum,

\[
G''-G'G^{-1}G'=R^*X(1-P_R-2P_D)XR
=O_N^*O_N-I_N^*I_N.
\]

The outgoing target is one-dimensional, hence its rank is at most one. For the incoming map, `X` sends `chi P_{N-q-1}` into `D_N`, so its pairing against `R` vanishes on this codimension-one subspace of `D_N`; hence the adjoint of `I_N` has rank at most one. If `D_N=0`, the incoming map is zero.

The individual trace costs require the following retained shared term. For `N>=q`, set `delta_N=V_N/V_{N-1}=omega_N/nu_{m-1}`. In real polynomial coordinates write `d_j=[Q_j]`. The highest coefficient of `R` is `d_N^*G/omega_N`, so

\[
O_N=Q_{N+1}\frac{d_N^*G}{\omega_N},\qquad
\operatorname{Tr}(G^{-1}O_N^*O_N)
=a_{N+1}(1-\delta_N).
\]

Here `d_N^*Gd_N/omega_N=1-delta_N` follows directly from the kernel determinant update proved in the next section. To compute the incoming term, transport the original `chi` to `psi(u)=i^{-q}chi(c+iu)` and let `Qtilde_j` be the monic polynomials for `|psi|²e^{theta u}m_kdu`; `|psi|²=|chi(c+iu)|²`. The unit vector in the highest boundary direction is

\[
e_D=\psi Qtilde_{m-1}/\sqrt{\nu_{m-1}}.
\]

Its `X`-image modulo the boundary has full squared norm `beta_m`, by the relation three-term recurrence. Its outgoing degree-`N+1` component has squared norm `omega_{N+1}/nu_{m-1}=a_{N+1}delta_N`, because its leading coefficient is `1/sqrt(nu_{m-1})`. The remaining orthogonal component is in the minimum quotient image and equals the incoming-adjoint contribution. Thus

\[
\operatorname{Tr}(G^{-1}I_N^*I_N)
=\beta_m-a_{N+1}\delta_N\ge0.
\]

Their difference is `a_{N+1}-beta_m`, proving the scalar curvature with both costs retained. At `N=q-1`, `I_N=0` and the outgoing trace is `a_q`. In particular, it would be incorrect to identify the outgoing cost alone with `a_{N+1}` for general `N>=q`, or the incoming cost alone with `beta_m`. The source's net identity (22) is correct; this computation completes its individual trace dictionary.

## 5. Phase, scalar control, exact endpoint, and CV.1–CV.12

The ring isomorphism `F:C[S] -> C[u]`, `F(P)=P(c+iu)`, has inverse `Q -> Q((S-c)/i)`. Dagger stability gives `overline{chi(c+iu)}=(-1)^q chi(c+iu)` for real `u`, so `psi=i^{-q}F(chi)` has real coefficients and leading coefficient one. Multiplication by the retained scalar `i^{-q}` identifies the ideals `(Fchi)` and `(psi)`. It induces the quotient isomorphism `C_S -> C_u=C[u]/(psi)`; all original arithmetic maps are transported along its inverse.

In the fixed remainder bases let `B` be its constant matrix. Its entries are `B_{rj}=binom(j,r)c^{j-r}i^r` for `0<=r<=j<q`, and `det B=i^{q(q-1)/2}`. The exact metric and kernel comparisons are

\[
G_S=B^*G_uB,\quad K_S=B^{-1}K_u(B^*)^{-1},\quad
A_u=BA_SB^{-1}=cI+iT_u,
\]
\[
R_S=R_uB,\qquad \eta_u=\eta_SB^{-1},\qquad
\det G_S=\det G_u.
\]

Thus `ell_N` and its tilt derivative are unchanged by this specified coordinate map. The real matrix `T_u` is multiplication by `u` on `C_u`; `sigma=Tr T_u=Tr((A_S-cI)/i)` is real. Positive real weights give real monic `Q_j`; the original monic `p_j(S)` obey `F(p_j)=i^jQ_j` with their norms unchanged. These formulas supply the exact morphism rather than suppressing a coordinate phase.

Let `d_j=[Q_j] in C_u`. The canonical lift is

\[
R_Nx=\sum_{j=0}^NQ_j\frac{d_j^*G_Nx}{\omega_j}.
\]

It has highest coefficient `d_N^*G_N/omega_N`. The original next relation is `bfrak_N=Q_{N+1}-R_Nd_{N+1}`. It has zero quotient and `R_N^*bfrak_N=-G_Nd_{N+1}`, since `Q_{N+1}` is orthogonal to the degree-`N` source. The difference

\[
XR_N-R_NT_u-\mathfrak b_N\frac{d_N^*G_N}{\omega_N}
\]

has zero quotient and degree at most `N`, hence lies in `D_N`. Multiplying by `R_N^*`, and then taking the trace after `G_N^{-1}`, gives

\[
\ell_N'=\operatorname{Tr}(G_N^{-1}R_N^*XR_N)
=\sigma-\frac{d_N^*G_Nd_{N+1}}{\omega_N}.
\]

Transport through the original polynomial phases gives exactly

\[
\frac{b_N^*G_Sb_{N+1}}{\omega_N}=i(\sigma-\ell_N'),
\qquad b_j=[p_j]_\chi.
\]

This holds for every real tilt in the admitted interval, including a noneven tilted measure. The purely imaginary cross term follows from a real polynomial quotient and metric; evenness is not needed.

For `N>=q`, minimum-norm comparison gives `0<G_N<=G_{N-1}` and hence `0<delta_N<=1`. Direct rank-one determinant updates, with `K_N=K_{N-1}+b_Nb_N^*/omega_N`, give

\[
\frac{b_N^*G_Nb_N}{\omega_N}=1-\delta_N,\quad
\frac{b_{N+1}^*G_Nb_{N+1}}{\omega_{N+1}}=\delta_{N+1}^{-1}-1.
\]

Set `v_N=-log delta_N>=0` and `a_{N+1}=omega_{N+1}/omega_N`. The inherited rank-two control is the Hermitian pair associated to `W=A^*G+GA-kG`; reflection gives trace zero and nonzero eigenvalues `+epsilon,-epsilon`. Substitution into its two-vector Gram determinant gives

\[
\epsilon_N^2=a_{N+1}(1-e^{-v_N})(e^{v_{N+1}}-1)
-(\sigma-\ell_N')^2.
\]

The entire expression is nonnegative because it is the original two-vector Gram determinant divided by `omega_N²`. Its individual subtraction terms have not been assigned arbitrary signs.

For `s_N=(v_N+v_{N+1})/2` and `t_N=(v_{N+1}-v_N)/2`, direct multiplication gives

\[
(1-e^{-v_N})(e^{v_{N+1}}-1)
=\sinh^2s_N-(e^{t_N}-\cosh s_N)^2.
\]

Therefore both nonnegative losses are retained in

\[
\epsilon_N^2=a_{N+1}\sinh^2s_N
-a_{N+1}(e^{t_N}-\cosh s_N)^2-(\sigma-\ell_N')^2,
\]

and, with `mathcal R_N=e^{2s_N}=V_{N-1}/V_{N+1}>=1`,

\[
\epsilon_N\le\sqrt{a_{N+1}}\frac{\mathcal R_N-1}{2\sqrt{\mathcal R_N}}.
\]

This bound holds at a fixed admitted degree and tilt. The original arithmetic allowance corresponds to zero tilt. It gives no automatic estimate as `k` and the admitted degree grow.

The exact equality condition for the first squared loss is also retained. The literal volume substitution gives

\[
e^{t_N}-\cosh s_N
=\frac{2V_N-V_{N-1}-V_{N+1}}{2\sqrt{V_{N-1}V_{N+1}}}.
\]

Thus equality in the finite upper bound holds precisely when `2V_N=V_{N-1}+V_{N+1}` and `sigma-ell_N'=0`. Equal successive logarithmic contractions do not generally make this loss vanish. The source's descriptive word “imbalance” should be accompanied by this exact arithmetic-volume midpoint formula.

At the first admitted degree `N=q-1`, no inverse or logarithm of a preceding singular kernel is used. Expand the original annihilator as `chi=p_q+sum_{j<q}gamma_j p_j`. Orthogonality and the monic leading term give

\[
\nu_0=\|\chi\|^2=\omega_q+\sum_{j<q}|\gamma_j|^2\omega_j,
\quad b_q=-\sum_{j<q}\gamma_jb_j,
\quad b_i^*G_{q-1}b_j=\delta_{ij}\omega_j\ (i,j<q).
\]

Consequently `b_q^*G_{q-1}b_q=nu_0-omega_q`, while the final included column has leverage one. The endpoint radius is exactly

\[
\epsilon_{q-1}^2=\frac{\nu_0-\omega_q}{\omega_{q-1}}
-(\sigma-\ell_{q-1}')^2
=\frac{\sum_{j<q-1}|\gamma_j|^2\omega_j}{\omega_{q-1}}.
\]

The first phase identity gives `gamma_{q-1}=-i(sigma-ell')`. This is precisely CV.11–CV.12. At `q=1`, the last sum is empty and the radius is zero, with the coordinate module still retained.

**Actual source typo:** NOTE.tex line 744 (RESEARCH_NOTE.md endpoint prose) says `d_N=nu_0-omega_q`; `d_j` was defined as the vector `[Q_j]` in the real quotient. Its correctly typed replacement is

\[
d_q^*G_{q-1}d_q=b_q^*G_{q-1}b_q=\nu_0-\omega_q.
\]

The displayed source equation (27) is correct. This replacement repairs the sentence; it does not change the theorem.

For the full CV dictionary distinguish `D_N^{CV}=det K_N` from the source moment determinant `mathfrak D_n`. At the original observation,

\[
D_N^{CV}=V_N^{-1}=\frac{\mathfrak B_{N-q+1}}{\mathfrak D_{N+1}}.
\]

The determinant of the omitted-direction kernel in CV.2 satisfies, for `N>=q`,

\[
\frac{\widetilde D_N^{CV}}{D_N^{CV}}
=\frac{\delta_N}{\delta_{N+1}}
+\frac{(\sigma-\ell_N')^2}{a_{N+1}}.
\]

This follows by substituting the two leverage identities and the phase into CV.3, including its positive complex cross-term sign. Hence

\[
\frac{D_{N+1}^{CV}+D_{N-1}^{CV}-D_N^{CV}-\widetilde D_N^{CV}}{D_N^{CV}}
=(1-\delta_N)(\delta_{N+1}^{-1}-1)
-\frac{(\sigma-\ell_N')^2}{a_{N+1}},
\]

and CV.4 is exactly the Toda radius formula. At `N=q-1`, `D_{N-1}^{CV}=0`; the same determinant algebra uses that zero determinant directly and the separate endpoint above, without defining a nonexistent volume logarithm.

CV.10 identifies this signed determinant numerator with its complete positive minor sum `Delta_N`. CV.10a constructs the original source vector `zeta_N`, with `||zeta_N||²=Delta_N` and literal tensor-source norm `q!Delta_N` under `mathcal V^{tensor q}Alt_q`. Therefore the new determinant-flow expression retains the exact original exterior source map and factorial:

\[
\epsilon_N^2=a_{N+1}\frac{\|\zeta_N\|^2}{D_N^{CV}},\qquad
\|\mathcal V^{\otimes q}\operatorname{Alt}_q\zeta_N\|^2=q!\|\zeta_N\|^2.
\]

No omitted-direction inverse is needed. The new phase derivative computes an ingredient of the same positive sum and arithmetic control, rather than changing the source family or target metric.

## 6. Exterior inequality and literal quartet scope

The preceding exterior proof gives `L_{h,k}<=epsilon_N`, where

\[
L_{h,k}=\sum_{\Re\lambda>k/2}\ell_\lambda(2\Re\lambda-k).
\]

The full multiplicity is the cyclic nilpotent length at each summed eigenvalue. Combining the nonnegative upper bound with this lower bound and applying the increasing function `arsinh` gives

\[
\log\frac{V_{N-1}}{V_{N+1}}
\ge2\operatorname{arsinh}\left(\frac{L_{h,k}}{\sqrt{a_{N+1}}}\right),\quad N\ge q,
\]

or equivalently `4 mathcal R_N L_{h,k}² <= a_{N+1}(mathcal R_N-1)²`. Summing at `N=N_0+2j` cancels the intermediate logarithms exactly, yielding the stated inequality from `V_{N_0-1}` to `V_{N_0+2r-1}` with the source recurrence indices `N_0+2j+1`. These are necessary volume contractions; decreasing minimum volume does not annihilate the fixed arithmetic jets.

For the equality `q=[1+k(m-1)](k+1)²`, the packet polynomial must be exactly the chosen complete nonreal quartet

\[
h(s)=\prod_{\varepsilon,\eta\in\{\pm1\}}
(s-(1/2+\varepsilon\delta+i\eta\gamma))^m,
\quad \delta>0,\quad\gamma>0.
\]

Then its distinct sums are `k/2+delta(2a-k)+i gamma(2b-k)` for `0<=a,b<=k`, each with cyclic length `ell_k=1+k(m-1)`. Their positive real defects sum to

\[
L_k=2\delta\ell_k(k+1)\left\lfloor\frac{(k+1)^2}{4}\right\rfloor.
\]

The real and imaginary coordinates make those `(k+1)²` sums distinct. The sum over positive `2a-k` is `floor((k+1)²/4)`. This proves the count without assuming algebraic independence of zero ordinates.

For a larger reflection-stable packet containing the quartet, each ordered quartet tensor component is a CRT summand of the larger tensor algebra. The larger nilpotent length at each quartet sum is the maximum over all components and is at least `ell_k`; thus the displayed quartet expression remains a lower bound for `L_{h,k}`. Its degree equality need not persist. All moments, recurrence coefficients, determinant sequences and admission thresholds must use the actual larger packet, with `N>=deg chi_{h,k}` for the two-step volume formula. This is the required scope clarification when propagating source equation (32).

For the exact quartet, conjugation stability makes `w_h`, hence `m_k`, even. The summed relation has the matching symmetry, so `|chi(c+iu)|²` is even. Their Hankel determinants are even in `theta` by `u->-u`, and the summed trace of `T` is zero. Thus the phase vanishes at zero tilt by the additional symmetry. A nonzero tilt changes the measure and generally restores it.

The unproved arithmetic endpoint remains an upper estimate, along permitted growing degrees, for

\[
\frac{\sqrt{a_{N(k)+1}}}{k^3}
\frac{\mathcal R_{N(k)}-1}{2\sqrt{\mathcal R_{N(k)}}},\quad N(k)\ge q,
\]

or for the sharper expression retaining both squares. The supplied source correctly reports that it has not proved this quantity tends to zero. The exact maps and finite inequalities above are established independently of that missing asymptotic; it is not an additional assumed hypothesis of their proofs.

## 7. Original theta input and numerical-source scope

The source's analytic continuation retains the exact log/Fourier map. To specify the needed bounds on all fixed contours, start for `Re s>1` with `zeta(s)=s int_1^infinity floor(x)x^{-s-1}dx`, obtained by interchanging the absolutely convergent sum and integral. Splitting `floor(x)=x-{x}` gives

\[
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.
\]

The remaining integral is holomorphic for `Re s>0`, furnishing the same identity there by analytic continuation. For `sigma>=1/2` and `|t|>=1`, its absolute value is bounded by `|s|/|s-1|+|s|/sigma`, hence polynomially in `|t|`, uniformly on compact ranges of `sigma`. For `sigma<1/2`, use the retained functional equation `g(s)=g(1-s)` to transfer to the line `1-sigma>1/2`. The gamma estimate and the original monic division then give `|v_h(sigma+it)|<=C(1+|t|)^B exp(-pi|t|/4)` on every fixed vertical contour, and uniformly across each bounded horizontal interval of real parts, outside a compact set. Compact sets are harmless since `v_h` is entire. Horizontal connecting contour segments vanish by the same exponential bound. Consequently Mellin inversion may be shifted to any fixed real `sigma`; on each closed sector `|arg z|<=alpha<pi/4` the integrand is dominated by a polynomial times `exp[-(pi/4-alpha)|t|]`. Differentiation is dominated too. The contour formula gives `|F_h(z)|<=C_{sigma,alpha}|z|^{-sigma}`; choosing positive and negative contours supplies both rapid endpoint bounds. These are the bounds used for the following contour move.

For real `|theta|<pi/2`, put

\[
E_\theta F_h(y)=e^{(y+i\theta/2)/2}F_h(e^{y+i\theta/2}).
\]

Insertion of Mellin inversion on `Re s=1/2` gives

\[
E_\theta F_h(y)=\frac1{2\pi}\int e^{-ity}e^{\theta t/2}v_h(1/2+it)\,dt.
\]

Thus its Fourier transform with kernel `e^{ity}` is the stated `e^{theta t/2}v_h(1/2+it)`. Plancherel has its full factor `1/(2pi)`; substituting `x=e^y`, with `dy=dx/x`, cancels the factor `x` from `|e^{y/2}|²`. The retained phase `e^{i theta/4}` has unit modulus. Consequently

\[
M_h(\theta)=\int_0^\infty|F_h(e^{i\theta/2}x)|^2dx.
\]

Dagger stability gives `F_h(1/conjugate(z))=(-1)^d conjugate(z) conjugate(F_h(z))`, first by Mellin uniqueness on the positive axis and then analytically throughout the sector. For `z=e^{i theta/2}x`, its norm identity is `|F_h(e^{i theta/2}/x)|²=x²|F_h(e^{i theta/2}x)|²`. Changing variables `x->1/x` on the interval `(0,1)` therefore gives the full factor two in

\[
M_h(\theta)=2\int_1^\infty|F_h(e^{i\theta/2}x)|^2dx.
\]

The degree sign was retained before the norm. This endpoint relation does not by itself assert that `M_h` is even in the tilt; conjugation stability supplies that further symmetry when available.

For `h=1`, retain the original seed

\[
f_0(z)=2\sum_{n\ge1}\sum_{r=1}^2c_r(\pi n^2)^rz^{2r}e^{-\pi n^2z^2},
\quad c_1=-6,\quad c_2=4.
\]

On the exterior interval the product of this series and its conjugate converges absolutely and locally uniformly for the admitted real tilt, with dominating Gaussian exponent proportional to `(m²+n²)cos(theta)x²`. The integral of each product term is

\[
\int_1^\infty x^{2r+2s}e^{-Cx^2}dx
=\frac{\Gamma(r+s+1/2,C)}{2C^{r+s+1/2}},\quad\Re C>0,
\]

where `C=pi(m²e^{i theta}+n²e^{-i theta})`. The complex power is the holomorphic branch on the right half-plane agreeing with the positive real power. The exterior factor two, the two original seed factors two, and this integral's factor one-half give exactly the coefficient four in

\[
M_1(\theta)=4\sum_{m,n\ge1}\sum_{r,s=1}^2
c_rc_s(\pi m^2)^r(\pi n^2)^s e^{i\theta(r-s)}
\frac{\Gamma(r+s+1/2,C_{mn}(\theta))}{C_{mn}(\theta)^{r+s+1/2}}.
\]

Polynomial factors from any fixed number of tilt derivatives remain dominated on compact subintervals, so the termwise derivatives used for the moments are valid. The source bounds establish convergence but give no numerical enclosure for the omitted square of indices in its finite script.

The script's derivative polynomial is correct: writing `z=pi n²x²`, `D[p(z)e^{-z}]=2z(p-p')e^{-z}`. For `p=4z²-6z`, this yields `8z³-28z²+12z`, exactly as implemented. Under the log/Fourier map `D-1/2` has multiplier `it`, so

\[
M_1''(0)=\|(D-1/2)f_0\|^2.
\]

Evenness gives `M_1'(0)=0`. Taking two derivatives of the literal tensor power and dividing by its mass gives

\[
a_1^{(k)}=\frac{(M_1^k)''(0)}{M_1(0)^k}
=k\frac{M_1''(0)}{M_1(0)}.
\]

The copied numerical evaluator independently reproduces the source's printed values `M1(0)=1.279007247846485140479533592267193274492`, `M1(0.1)=1.345907178458249796968220592357629805161`, `M1''(0)=13.05554930257055843539268465812319368243`, and the ratio `10.207564753485721688865761252237555175`. All are reported as numerical values only. The separate theta-input lane is developing interval/tail certificates as new work; no such certificate is retroactively attributed to this ZIP. Its `h=1` finite arithmetic quotient remains zero.

## 8. Exact checker coverage and limits of each method

The checker constructs Gaussian moments by their full mass, mean and variance formula. It builds the complete source moment matrix, quotient-reduction columns, kernel, minimum Gram and representative independently, forms the original action `A=3I/2+iT`, and compares its matrix control radius `Tr((K W)²)/2` to the scalar determinant formula. Its acceptance checks use exceptions and unittest rather than removable Python `assert`. No subprocess or network call occurs in the checker. `evaluate_seed.py` uses mpmath and writes its numerical record only. `build_reader.py` invokes Pandoc and changes NOTE/HTML; it was inspected but not executed. `check_reader.py` launches a hard-coded Linux Chromium and records screenshots/dimensions; it was inspected but not run locally and has no independent mathematical verification role.

| Method | Exact implemented scope |
|---|---|
| 01 | Monic norm equals adjacent source Hankel ratio for Gaussian moments through degree four, mean 1/3, variance 2, mass 11. |
| 02 | Source/relation volume equals direct canonical determinant for four listed relations and degrees; also checks the right-inverse equation. |
| 03 | Literal multiplication-by-relation columns lie in the reduction kernel and are orthogonal to the minimum representative. |
| 04 | Noneven quadratic relation at degree three: direct radius `1156/333`, logarithmic volume derivative `-52/111`, and nonzero phase subtraction. |
| 05 | Even quadratic relation with means 1/2 and -2/3; scalar radius equals the direct matrix result and phase is nonzero. |
| 06 | Two repeated-root relations at degree equal to relation degree; determinant and full radius identities. |
| 07 | Three explicit relations at first admitted degree `q-1`; zero preceding leverage ratio and endpoint radius. |
| 08 | Direct quotient inner product of consecutive monic polynomials equals trace-minus-volume-derivative for a noneven tilted fixture. |
| 09 | Three explicit two-step determinant upper bounds compared to the independently constructed control radius. |
| 10 | Exact symbolic algebraic two-loss identity for positive formal variables `x,y`. |
| 11 | Hankel–Toda source identity for a three-atom positive measure, determinant orders one and two, strictly below support exhaustion. |
| 12 | Same three-atom calculation after its explicit quadratic relation filter. |
| 13 | The scalar trace of the matrix-curvature construction equals the Toda difference in one Gaussian fixture. This test does not separately assert the full matrix identity or each incoming/outgoing trace formula. |
| 14 | Multiplying the source mass by three scales `G,V,mathfrak D,mathfrak B` by their exact dimensions and leaves the radius unchanged. |
| 15 | Source-coordinate Gram determinant and polynomial leading-phase comparison for `S=3/2+iu`. Despite the method's word “unit”, it does not test the actual arithmetic Taylor unit or its derivative. |
| 16 | Exact three-fold finite-atomic convolution and differential relation filter. |
| 17 | Empty relation `chi=1` gives determinant ratio one and retains two distinct split labels; this is not a full semimodule operation-table test. |
| 18 | A nonzero source relation has positive original norm and quotient value at an active support label; active zero is distinguished from the absent label. |
| 19 | In `I=(z1²,z2²)`, `S^5` vanishes modulo `I²` while `S^4` survives; positive norm-square observation is retained. |
| 20 | Quartet sum count for `k=1,...,8`, displacement 1/4 and common multiplicity two (`ell=1+k`). It is not a test of all multiplicities or actual zero locations. |
| 21 | Even quartic fixture at zero mean gives zero phase and the expected radius without that vanishing term. |
| 22 | Tilted even quadratic has nonzero phase and exactly the phase-square difference between raw and complete radii. |
| 23 | Explicit radius grows from 4 at degree one to 16/3 at degree two, preventing an unwarranted monotonicity inference for the control. |
| 24 | Positive first relation determinant accompanies zero polynomial-reduction value. |
| Negative | A separate `1=2` check is intentionally added as method 25; it fails identically in both interpreter modes. |

The current independent replay establishes exactly these finite identities and the printed numerical seed agreement. It does not certify actual zeta-zero coordinates, the full infinite integrals, unexecuted Lean source, or a tensor-degree-uniform estimate. The general proof of the full curvature identity and its individual costs is supplied above and in the independently authored phase/curvature review. No test count is substituted for that proof.

The complete independent mathematical companion is `W/work/toda_phase_curvature_independent_review_20260912.md`, 20317 bytes, SHA-256 `3d3b9e8ebe06b4f28b4af09e10034bbd97d1f02bd8706a91b80db852504eb704`. It was read in full during this audit. Its exact endpoint, adjoint and shared-curvature calculations agree with the derivations above. A control-character typo in its displayed fraction was repaired before this final pin.

## 9. Integration corrections and accepted mathematical status

1. Replace the endpoint scalar/vector sentence at NOTE line 744 by the full scalar pairing `d_q^*G_{q-1}d_q=nu_0-omega_q` in the correct real quotient coordinates. Equation (27) is unchanged.
2. State the coefficient conjugate-transpose and weighted Hilbert-adjoint conventions around (15) explicitly. The exact weighted adjoint `M_N^{-1}J_N^*` and the constant quotient-coordinate matrix above remove the ambiguity without altering the source Gram.
3. Retain both individual curvature costs `a_{N+1}(1-delta_N)` and `beta_m-a_{N+1}delta_N`. Only their difference is the Toda curvature. This supplies a stronger exact map-level statement than the source's net trace sentence.
4. Attach the exact-quartet packet hypothesis to the degree equality in (32). For larger packets preserve the proved quartet lower bound and use their actual annihilator degree and actual arithmetic measure.
5. Preserve the original numerical and formalization source scopes. New interval or formal evidence belongs in its own dated continuation and receipt.

With these explicit repairs/clarifications, no incorrect displayed determinant, phase, upper-control, endpoint, or theta coefficient formula was found in this delivery. Its substantive relation to CV.1–CV.12 is the exact reciprocal source/boundary determinant ratio and the tilt derivative computing the full original cross term. The original source, all masses, polynomial phases, quotient kernel, arithmetic unit, tensor signs, nilpotent lengths and supported-zero label remain present. The remaining large-degree arithmetic estimate is still to be proved; none has been silently supplied as an assumption.
