# Independent audit: actual polynomial boundary density and the complete jet graph

Date: 2026-09-12. This report reviews `arithmetic_input.tex` (A1--A15), `arithmetic_moments.tex` (AM.6), `kernel_convergence.tex` (GC.1--GC.2), `jet_topology.tex` (JT1--JT3), and `coherent_tensor_integration.tex` (CT.1--CT.26) in the active Split Zero continuation. It introduces no alternative source, packet, arithmetic multiplier, or metric. The conclusions below hold for every nonempty finite packet of actual nontrivial zeros with their complete orders, and every integer tensor degree k >= 1. Reflection stability is not needed for the density, graph, determinant, or inverse-kernel conclusions.

## 1. The exact Hilbert maps

Retain

\[
g(s)=2\xi(s),\quad h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\quad
d=\deg h,\quad s_j=\tfrac12+it_j,\quad v_h=g/h,
\]
\[
d\nu_h(t)=|v_h(1/2+it)|^2\frac{dt}{2\pi},\qquad
d\eta_k(\mathbf t)=\prod_{j=1}^k\frac{dt_j}{2\pi},\qquad
d\nu_h^{\otimes k}=|v_h^{\otimes k}(\mathbf s)|^2d\eta_k.
\]

Here the product multiplier is the actual function
\(v_h^{\otimes k}(\mathbf s)=\prod_j v_h(s_j)\). Complete multiplicities make every removed singularity of v_h removable and make \(\upsilon_h=j_hv_h\) a unit of \(E_h=\mathbb C[s]/(h)\). The nonzero entire function v_h has isolated zeros. On the original line its zero set is discrete, hence Lebesgue null. Its product vanishes only on the union of the corresponding coordinate null sets, which is null for eta_k.

The original logarithmic map

\[
(\mathcal L_kF)(\mathbf y)=e^{(y_1+\cdots+y_k)/2}
F(e^{y_1},\ldots,e^{y_k})
\]

is unitary from \(\mathcal H_k=L^2((0,\infty)^k,d^kx)\) to \(L^2(\mathbb R^k,d^ky)\), by \(d^kx=e^{\sum y_j}d^ky\). Its Fourier transform with the retained plus sign is

\[
(\mathcal M_kF)(\mathbf s)=\int_{(0,\infty)^k}
F(\mathbf x)\prod_j x_j^{s_j}\frac{dx_j}{x_j}
=\int_{\mathbb R^k}(\mathcal L_kF)(\mathbf y)e^{i\mathbf t\cdot\mathbf y}d^ky.
\]

Plancherel gives the unitary map
\(\mathcal M_k:\mathcal H_k\longrightarrow L^2(\eta_k)\), with inverse carrying exactly the measure \(\prod dt_j/(2\pi)\).

Multiplication by the retained product v_h defines another unitary surjection

\[
V_{h,k}:L^2(\nu_h^{\otimes k})\longrightarrow L^2(\eta_k),
\qquad P\longmapsto v_h^{\otimes k}P.
\tag{CD.1}
\]

Norm equality is precisely the definition of nu_h. For surjectivity, if Q belongs to the target, put \(P=Q/v_h^{\otimes k}\) outside its null zero set and assign any value on that set. Then P belongs to the source, its norm equals the target norm of Q, and its image equals Q almost everywhere. Consequently

\[
\overline{\mathcal T}_{h,k}=\mathcal M_k^{-1}V_{h,k}:
L^2(\nu_h^{\otimes k})\longrightarrow\mathcal H_k
\tag{CD.2}
\]

is a unitary surjection. On actual polynomials this is exactly the source map
\(\mathcal T_h^{(k)}P=P(D_1,\ldots,D_k)F_h^{\otimes k}\), because each original factor has Mellin transform \(v_h\) and D_j has multiplier s_j. This proves the extension and its inverse; no replacement of the arithmetic functions is involved. Values discarded on line-null sets occur solely in an L2 equivalence class, not in the original entire Mellin functions or the finite jet algebra.

## 2. Polynomial density with an explicit uniqueness argument

We first prove a general fact needed for the original measure. Let mu be a finite positive Borel measure on \(\mathbb R^k\) satisfying

\[
\int e^{a\|\mathbf t\|_1}d\mu(\mathbf t)<\infty
\qquad\text{for some }a>0.
\tag{CD.3}
\]

Then complex polynomials in \(s_j=1/2+it_j\), equivalently complex polynomials in t_j under the exact inverse \(t_j=(s_j-1/2)/i\), are dense in L2(mu).

To prove this, suppose u is orthogonal to them. Set \(d\lambda=\overline u\,d\mu\). Cauchy--Schwarz gives

\[
\int e^{(a/2)\|\mathbf t\|_1}d|\lambda|
\le \|u\|_{L^2(\mu)}
\left(\int e^{a\|\mathbf t\|_1}d\mu\right)^{1/2}<\infty.
\tag{CD.4}
\]

For a fixed nonzero real vector xi, define
\(F_\xi(z)=\int e^{iz\xi\cdot\mathbf t}d\lambda(\mathbf t)\).
It is holomorphic in the strip
\( |\operatorname{Im}z|<a/(2\|\xi\|_\infty)\).
Indeed on a smaller closed strip every differentiated integrand is bounded by a constant times \(e^{(a/2)\|\mathbf t\|_1}\), since a fixed power of \(\|\mathbf t\|_1\) is absorbed by the strict exponential margin. Dominated differentiation gives

\[
F_\xi^{(n)}(0)=i^n\int(\xi\cdot\mathbf t)^n d\lambda=0
\quad(n\ge0).
\]

The last integrand is an actual polynomial, so the equality follows from orthogonality. The Taylor series vanishes on a neighborhood of zero; the one-variable identity theorem on this connected strip gives \(F_\xi(1)=0\). At xi=0 the same assertion is the zero constant moment. Thus the full Fourier transform
\(\widehat\lambda(\xi)=\int e^{i\xi\cdot\mathbf t}d\lambda\) vanishes on \(\mathbb R^k\).

For completeness this entails lambda=0 without appealing to moment determinacy. Let

\[
\gamma_\epsilon(x)=(4\pi\epsilon)^{-k/2}
e^{-|x|^2/(4\epsilon)}
=(2\pi)^{-k}\int e^{-\epsilon|\xi|^2}e^{-i\xi\cdot x}d^k\xi.
\]

The last equality is the product of the elementary one-variable Gaussian integrals. Fubini is justified by the finite total variation of lambda and the integrability of \(e^{-\epsilon|\xi|^2}\). Hence

\[
(\gamma_\epsilon*\lambda)(x)
=(2\pi)^{-k}\int e^{-\epsilon|\xi|^2}e^{-i\xi\cdot x}
\widehat\lambda(\xi)d^k\xi=0.
\]

For every compactly supported continuous f, another absolutely justified Fubini interchange yields \(\int (f*\gamma_\epsilon)d\lambda=0\). The functions \(f*\gamma_\epsilon\) converge uniformly to f: split the convolution displacement into a ball where uniform continuity bounds the difference, and its complement, whose Gaussian mass tends to zero after the change of variables by \(\sqrt\epsilon\). Thus \(\int f\,d\lambda=0\) for every such f. Uniqueness of a finite regular Borel measure from its compactly supported continuous test functions gives lambda=0, and its density \(\overline u\) with respect to mu is zero almost everywhere. The orthogonal complement of the polynomials is zero, proving density.

## 3. The actual boundary ideal is dense

The arithmetic exponential decay in JT1--JT3 gives, for each \(0<b<\pi/4\),
\(|g(1/2+it)|\le C_b e^{-b|t|}\). GC.2 proves
\(\int e^{a|t|}d\nu_h(t)<\infty\) for every \(0<a<\pi/2\), retaining the removed critical zeros by the entire quotient. The same estimate directly proves

\[
\int e^{a|t|}|g(1/2+it)|^2\frac{dt}{2\pi}<\infty
\quad(0<a<\pi/2).
\tag{CD.5}
\]

Define the *actual weighted product measure*

\[
d\mu_{h,k}(\mathbf t)=|h(s_1)|^2d\nu_h^{\otimes k}(\mathbf t)
=|g(s_1)|^2\frac{dt_1}{2\pi}\prod_{j=2}^k d\nu_h(t_j).
\tag{CD.6}
\]

This equality retains h exactly, including its complete multiplicities; it follows from \(|h v_h|^2=|g|^2\). By product integration and (CD.5), mu_h,k satisfies (CD.3) for every a in the displayed interval. Hence polynomials are dense in L2(mu_h,k).

Now the specified multiplication map

\[
U_{h,1}:L^2(\mu_{h,k})\longrightarrow L^2(\nu_h^{\otimes k}),
\qquad P\longmapsto h(s_1)P
\tag{CD.7}
\]

is a unitary surjection. Its norm equality is (CD.6). Its inverse divides by h(s_1) away from finitely many coordinate hyperplanes, a set null for the absolutely continuous product measure, and satisfies the identical norm equality. Thus the image of the polynomial subspace,
\(h(s_1)\mathbb C[s_1,\ldots,s_k]\), is dense in \(L^2(\nu_h^{\otimes k})\).

This subspace is contained in the actual ideal

\[
\mathcal I_{h,k}=(h(s_1),\ldots,h(s_k))
=\bigcup_{M\ge k(d-1)}\mathcal I_{h,k,M}.
\tag{CD.8}
\]

The union equality holds because each polynomial has finite total degree and the spaces are defined by intersection with the degree bound. Therefore this actual ideal is dense in L2(nu_h^tensor k). Applying the unitary map (CD.2), whose action on each ideal polynomial is the original tensor boundary with the Koszul signs proved in CT.11, gives

\[
\overline{\bigcup_{M\ge k(d-1)}\mathcal B_M}^{\mathcal H_k}
=\mathcal H_k,
\qquad \mathcal B_M=\mathcal T_h^{(k)}\mathcal I_{h,k,M}.
\tag{CD.9}
\]

Every approximant is an original boundary in the specified total-degree family. The proof does not enlarge the correction space to arbitrary theta functions.

## 4. The constructed total-degree representatives and kernels have exact limits

The finite-dimensional subspaces B_M are nested. For f in H_k and any epsilon>0, (CD.9) supplies b in some B_M0 with \(\|f-b\|<\epsilon\). Orthogonal projection minimizes distance, so, for every M>=M0,

\[
\|(I-P_{\mathcal B_M})f\|\le\|f-b\|<\epsilon.
\]

Thus the **original orthogonal projections** converge strongly to the identity. CT.13 therefore gives

\[
R_M=(I-P_{\mathcal B_M})s_h^{\otimes k}\longrightarrow0
\quad\text{in operator norm }E_h^{\otimes k}\to\mathcal H_k.
\tag{CD.10}
\]

The operator-norm assertion follows from finite dimension: in the retained Euclidean basis e_1,...,e_N, N=d^k,
\(\|R_M\|^2\le\sum_{j=1}^N\|R_Me_j\|^2\to0\).
In particular, all of the following are conclusions for these actual source representatives:

\[
G_M=R_M^*R_M\longrightarrow0,\quad
\det G_M\longrightarrow0,\quad
\|W_M\|\le(2\|A^{(k)}\|+k)\|G_M\|\longrightarrow0.
\tag{CD.11}
\]

They are ordinary matrix norms in the retained basis. Every finite G_M remains strictly positive, because the actual complete jet identity remains
\(J^{(k)}R_M=I\). There is no limiting passage through J^(k) in (CD.10).

The full arithmetic interpolation matrix is
\(\mathcal C_M=J_{k,M}M_{k,M}^{-1}J_{k,M}^*=G_M^{-1}\).
Its smallest eigenvalue equals \(1/\|G_M\|\), so

\[
\lambda_{\min}(\mathcal C_M)\longrightarrow+\infty.
\tag{CD.12}
\]

The remainder-only kernel retains the exact unit map
\(\mathcal C_M=U_{\upsilon_h^{\otimes k}}K_MU_{\upsilon_h^{\otimes k}}^*\).
Writing U for that fixed invertible matrix, its inverse relation is
\(K_M=U^{-1}\mathcal C_M(U^{-1})^*\). Therefore
\(\lambda_{\min}(K_M)\ge\lambda_{\min}(\mathcal C_M)/\|U\|^2\to+\infty\).
This covers every critical-line factor and every nilpotent jet at once. It is compatible with the convergence of the separately typed off-line Gaussian resolvent in GC.23: the exact arithmetic interpolation matrix is the inverse of the degenerating representative metric.

The absolute limit of W_M does not imply convergence of its relative control. The precise quantity remains
\(S_M=G_M^{-1/2}W_MG_M^{-1/2}\), with both inverse metric factors diverging in (CD.12). The exact CT.23--CT.26 inequalities continue to govern this same quantity. No estimate of S_M is gained by dropping those factors.

## 5. The full jet graph and its exact quotient

Let
\(\mathscr S_{h,k}=\mathcal T_h^{(k)}\mathbb C[s_1,\ldots,s_k]\)
with its original map

\[
J^{(k)}\mathcal T_h^{(k)}P
=U_{\upsilon_h^{\otimes k}}[P]_{(h(s_1),\ldots,h(s_k))}.
\tag{CD.13}
\]

It is surjective: the remainder basis has each coordinate degree below d, hence total degree at most k(d-1), and the displayed unit is invertible. Its kernel is exactly the union of B_M by the monic-division proof in CT.11. Consider its graph as a linear subspace of the Hilbert direct sum:

\[
\Gamma_J=\{(F,J^{(k)}F):F\in\mathscr S_{h,k}\}
\subset\mathcal H_k\oplus E_h^{\otimes k}.
\]

For any pair (f,u), choose the original finite representative \(s_h^{\otimes k}u\). By (CD.9) there are b_n in the union of B_M with
\(b_n\to f-s_h^{\otimes k}u\). Then
\((s_h^{\otimes k}u+b_n,u)\in\Gamma_J\)
and this sequence converges to (f,u). Hence

\[
\overline{\Gamma_J}=\mathcal H_k\oplus E_h^{\otimes k},
\qquad
\overline{\{(b,0):b\in\bigcup_M\mathcal B_M\}}
=\mathcal H_k\oplus0.
\tag{CD.14}
\]

In particular, the specific family \((R_Mu,u)\) tends to \((0,u)\) for every complete jet u. For nonzero u this proves directly that the graph closure is a multivalued closed linear relation, not the graph of an operator on H_k.

The strongest quotient comparison here is the continuous surjective map

\[
q_2:\mathcal H_k\oplus E_h^{\otimes k}\longrightarrow E_h^{\otimes k},
\quad(f,u)\longmapsto u,
\]

with exact kernel H_k⊕0. It induces the isometric linear isomorphism

\[
(\mathcal H_k\oplus E_h^{\otimes k})/(\mathcal H_k\oplus0)
\longrightarrow E_h^{\otimes k},\qquad[(f,u)]\longmapsto u,
\tag{CD.15}
\]

whose inverse is \(u\mapsto[(0,u)]\). Indeed all representatives of this class have second coordinate u, and the infimum of their direct-sum norms is \(\|u\|\), attained at (0,u). On the original graph this is exactly the complete jet quotient; the completion has retained every coordinate in its second factor. This supplies the typed relation between the dense Hilbert boundary and the nonzero original arithmetic quotient.

## 6. Relative source cost and the determinant telescope

Retain CT.20--CT.26, including
\(\Delta_M=G_M-G_{M+1}=Y_M^*Y_M\),
\(\tau_M=\operatorname{Tr}(G_M^{-1}\Delta_M)\),
\(\chi_M=\operatorname{Tr}(G_M^{-1}C_M^*C_M)\),
and the original spectral sum \(\mathcal D_k\). Put

\[
T_M=G_M^{-1/2}\Delta_MG_M^{-1/2},\qquad
\pi_M=\det G_{M+1}/\det G_M=\det(I-T_M).
\]

All eigenvalues t_i of T_M belong to [0,1), since G_M+1 is strictly positive. Integration of \((1-t)^{-1}\) gives

\[
-\log(1-t)=\int_0^t\frac{du}{1-u}\ge t,
\]

with strict inequality for t>0. Summing gives
\(\tau_M\le-\log\pi_M\), with equality exactly when Delta_M=0. CT.24 gives \(\mathcal D_k^2\le\tau_M\chi_M\).

If \(\mathcal D_k>0\), both tau_M and chi_M are positive at every finite level, so division by chi_M is legitimate and, for integers \(k(d-1)\le a<b\),

\[
\boxed{\quad
\mathcal D_k^2\sum_{M=a}^{b-1}\frac1{\chi_M}
\le\sum_{M=a}^{b-1}\tau_M
<\sum_{M=a}^{b-1}(-\log\pi_M)
=\log\frac{\det G_a}{\det G_b}.
\quad}
\tag{CD.16}
\]

The last equality is an exact finite telescoping product. When D_k=0, retain the unconditional middle non-strict inequality without forming any undefined reciprocal 1/chi_M. Formula (CD.11) makes the right-hand side diverge to +infinity as b tends to infinity with a fixed. The direction of (CD.16) does not imply that \(\sum 1/\chi_M\) diverges.

There is, however, an unconditional conclusion for the relative losses themselves:

\[
\sum_{M=a}^\infty\tau_M=+\infty.
\tag{CD.17}
\]

To prove it, suppose the sum were finite. Then tau_M tends to zero, so eventually every eigenvalue of T_M is at most tau_M <= 1/2. The same integral satisfies \(-\log(1-t)\le2t\) on that interval. Thus \(-\log\pi_M\le2\tau_M\) eventually. The finitely many earlier terms are finite because each pi_M>0; consequently the sum of negative logs would be finite, contradicting the determinant limit in (CD.11). This proof requires neither reflection nor a nonzero D_k.

## 7. Finite derivative norms: a valid extension and its precise scope

For a finite set Lambda of multi-indices containing 0, put
\(w_\Lambda(\mathbf t)=\sum_{\alpha\in\Lambda}\prod_j|s_j|^{2\alpha_j}\).
The original joint derivative norm
\(\|F\|_\Lambda^2=\sum_{\alpha\in\Lambda}\|D^\alpha F\|^2\)
is exactly the Mellin norm with measure w_Lambda eta_k on its maximal graph domain H_Lambda. Multiplication by any fixed polynomial preserves the availability of a positive exponential moment after choosing a strict exponent margin below pi/2. Therefore
\(w_\Lambda|h(s_1)|^2\nu_h^{\otimes k}\)
satisfies (CD.3). Repeating (CD.7)--(CD.9) in this specified weighted norm proves the original polynomial boundaries dense in H_Lambda and repeats (CD.14)--(CD.15) with H_Lambda in place of H_k.

This proves a graph-density statement for the same polynomial ideal. It does **not** assert convergence of the original L2-minimal representatives R_M in the stronger norm: those representatives minimize the unweighted norm specified in CT.12--CT.13. No commutation of an unbounded D_j with those original orthogonal projections has been assumed.

## Audit verdict

The proposed density theorem, actual total-degree limits, complete jet graph, and determinant telescope are valid with the hypotheses stated above. The strict telescope (CD.16), coercive divergence of the full interpolation kernels (CD.12), and divergent accumulated relative loss (CD.17) are further exact consequences. No endpoint RH statement or upper bound on the remaining relative source quantities follows from these density results alone; the equations above retain those quantities explicitly.

## Direct cumulative-source review

After writing the independent derivation above, I read the complete root source `tex/joint_density_dissipation.tex`, including JD.1--JD.15 and the later JD.9a--JD.9b addition. The reviewed file SHA-256 was `ee784e00c83ff44895b3264d43959de221496fbbc8fd794730f365b883c890d6`. Its formulas and proofs pass this independent audit. No direct edits were made to that TeX fragment.

The exact Split-Zero lift in JD.12 also passes: for each scalar in G(C), linearity retains its action on the represented fibre, including the represented zero scalar, while the external scalar zero sends every element to the external zero. Addition with the external zero remains the identity. The limit sends a supported vector to the supported Hilbert zero and sends the external zero to the external zero. The convergence follows uniformly on every bounded subset of the supported input fibre from the actual operator-norm limit, while the external point is fixed for all M.

A second independent lane, `density_refinement`, verified the full determinant argument and obtained the exact nonnegative decomposition

\[
\log\frac{\det G_a}{\det G_b}
=\mathcal D_k^2\sum_{M=a}^{b-1}\chi_M^{-1}
+\sum_{M=a}^{b-1}\left(\tau_M-\frac{\mathcal D_k^2}{\chi_M}\right)
+\sum_{M=a}^{b-1}\sum_{j=2}^\infty\frac{\operatorname{Tr}(T_M^j)}j
\quad(\mathcal D_k>0).
\]

The convergent series at each finite M is the scalar identity for -log(1-t) applied to every eigenvalue in [0,1). Moreover, the original layer identity and the actual limit give the two distinct exact conclusions

\[
\sum_{M=a}^\infty\|Y_M\|_{\mathrm{HS}}^2=\operatorname{Tr}G_a,
\qquad
\sum_{M=a}^\infty\|Y_MG_M^{-1/2}\|_{\mathrm{HS}}^2=\infty.
\]

The first is the trace of the finite telescoping identity followed by G_b→0; the second is (CD.17). These statements preserve the actual original maps and specify exactly how the absolute and relative accumulated boundary losses are related.

## Final cumulative-source pin

I reread the complete final `tex/joint_density_dissipation.tex` after the root added JD.11a and JD.16. The final reviewed SHA-256 is `104dfc3530938dd3de04a7ad320ddb85a236db075d7367bead4ca7d6f34d65e5`. The isometric quotient in JD.11a, matrix-norm telescoping series, absolute Hilbert--Schmidt energy identity, and divergent relative energy series in JD.16 all pass. Their proofs cover every full packet, tensor degree k>=1, zero finite layer, critical-line packet, and nilpotent factor without an endpoint assumption. No source correction was needed. This hash is ready for cumulative PDF integration.
