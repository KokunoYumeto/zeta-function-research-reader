# Independent audit of exterior trace amplification

Date: 12 September 2026. This review proves the new exterior and determinant calculations from the canonical cyclic source data, checks every multiplicity and map used in the amplification, and records the exact scope of the finite evidence. The analytic theta construction already supplied to the cumulative paper is a retained input. This review does not claim to have reconstructed the whole historical analytic corpus, run Lean, or proved an arithmetic subcubic upper estimate.

## Source identity and complete reading

The delivered `Tau_Exterior_Trace_Amplification_2026-09-12.zip` has SHA-256 `168f977a9b54cf461f564e099fe55dc7b8feffbc09c563f541e0be2bb5746a94` and 35 file members. Its manifest lists the 34 members other than the manifest itself. The complete 1,164-line `NOTE.tex` was read in three consecutive ranges, together with the full mathematical Markdown (including the middle range separately after an output truncation), the delivered amplification paste, the entire checker, and the handoff, programme-state, source-review, checks and README files.

| Object | Bytes | SHA-256 |
|---|---:|---|
| `NOTE.tex` | 34,300 | `c7050e1c2f76b31b72af1d237efd29f656fd34a92492e5a11f76d8bc55b2acd9` |
| `RESEARCH_NOTE.md` | 30,446 | `16c3e44879402dee9d8b2a7bc4be911fbfbb588978e01b418d0201cfdb5a970d` |
| `check_exterior_trace.py` | 12,060 | `ce667f43f0e74db89867c84066ae0b367f265ee33b145cbd0822f5a8e2d841e0` |
| `MANIFEST.sha256.json` | 4,536 | `70e0fb6e869ab8202d6037be1848488d78f72c0a42187ecbdca469fa86dd4f99` |

The older cyclic archive is a separate 43-member object with 42 manifest entries, SHA-256 `e0e4d0ecda69e4738dcb4cdd3b750e623d863eac8b44f353737393e720a840a7`. Its complete source is not bundled inside the exterior ZIP. The exterior source's old receipts about that archive must retain their date and scope.

The source's main claims are correct. The arithmetic unit, original mass, factorial, tensor signs, generalized-eigenspace multiplicities, oblique spectral projection and metric projection all survive in the proof. The equality and cross-map calculation in the companion continuation supplies an additional exact refinement.

## 1. Retained original objects and the cyclic map

Fix an integer `k >= 1` and a nonempty, finite, reflection-stable packet of actual zeros with complete orders. Write

\[
h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\qquad
E_h=\mathbb C[s]/(h),\qquad
B_k=E_h^{\otimes k},\qquad S=\sum_{i=1}^k s_i.
\]

The original function is

\[
g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Since each order in `h` is complete, `v_h=g/h` is holomorphic and nonzero at every packet root. Thus `upsilon_h=j_h(v_h)` is a unit in `E_h`; its inverse is the finite Taylor inverse in each CRT factor. Retain `U_k=upsilon_h^{tensor k}`.

At an ordered root tuple, let `z_i=s_i-rho_i`. The local factor of `B_k` is

\[
\mathbb C[z_1,\ldots,z_k]/(z_1^{m_{\rho_1}},\ldots,z_k^{m_{\rho_k}}).
\]

Put `r=sum_i(m_{rho_i}-1)`. Every monomial in `(sum_i z_i)^{r+1}` has some exponent at least its corresponding `m_{rho_i}`, so that power vanishes. The power of degree `r` has surviving monomial `prod_i z_i^{m_{rho_i}-1}` with coefficient

\[
\frac{r!}{\prod_i(m_{\rho_i}-1)!}\ne0.
\]

The nilpotent length is exactly `r+1`. If distinct tuples have the same sum `lambda`, the direct product of their local factors has minimal exponent equal to the maximum of their lengths. Therefore

\[
\ell_\lambda=\max_{\sum_i\rho_i=\lambda}
\left(1+\sum_i(m_{\rho_i}-1)\right),\qquad
\chi(S)=\prod_\lambda(S-\lambda)^{\ell_\lambda}
\]

is the minimal polynomial of multiplication by `S` on the full tensor algebra. This proof retains collisions: tuple multiplicities are not added into the cyclic exponent. On the cyclic image the generalized eigenspace dimension is `ell_lambda`, whereas the dimension of the entire tensor generalized eigenspace can be larger.

The typed algebra injection

\[
\alpha:\ C=\mathbb C[S]/(\chi)\longrightarrow B_k^{S_k},\qquad
[P]\longmapsto P(S)
\]

is well defined by the minimal-polynomial calculation and injective by its kernel calculation. Its image is invariant under permutations because `S` is. The arithmetic injection is the module map

\[
\eta=M_{U_k}\alpha:C\longrightarrow B_k^{S_k}.
\]

Its module left inverse is the source's `S`-equivariant cyclic retraction, and the full complement remains. The factor `M_{U_k}` is invertible but is not a unital algebra map unless `U_k=1`; the exact algebra-to-module connection is the displayed composition and inverse unit multiplication.

Reflection `rho -> 1-conj(rho)` sends a tuple sum `lambda` to `k-conj(lambda)`. It preserves every `m_rho`, hence every tuple length and each collision maximum `ell_lambda`. Consequently

\[
2\Re\operatorname{Tr}A=kq,\qquad A=M_S\in\operatorname{End}_{\mathbb C}(C),\quad q=\deg\chi.
\]

## 2. Canonical representatives and rank-two spectrum

Keep the actual source map

\[
\mathcal V P=P(D_1+\cdots+D_k)(F_h^{\otimes k}),\qquad
\mathcal M F_h=g/h,
\]

and its exact norm

\[
\|\mathcal VP\|^2=\int_{\mathbb R}|P(k/2+iu)|^2m_{h,k}(u)\,du,
\quad m_{h,k}=w_h^{*k},\quad
w_h(t)=\left|\frac{(g/h)(1/2+it)}{\sqrt{2\pi}}\right|^2.
\]

The mass is `mu_h^k`; no division by mass is made. In the source's literal monic polynomials `p_j(S)`, `omega_j=||Vp_j||^2` and `omega_0=mu_h^k`. For `N>=q-1`, the first `q` remainder columns `b_j=[p_j]_chi` form a basis, since the monic change of basis is triangular. Thus

\[
K_N=\sum_{j=0}^N\frac{b_jb_j^*}{\omega_j}>0,
\qquad G_N=K_N^{-1}>0.
\]

Writing a polynomial `P=sum_j t_j p_j`, its constraint is `sum_j t_j b_j=u`. The minimum is attained at `t_j=b_j^*G_Nu/omega_j`: substitution gives `K_NG_Nu=u`. For any other admissible coefficient vector, its difference `d` satisfies `sum_j d_j b_j=0`, so its inner product with the displayed minimum is `sum_j overline(d_j)b_j^*G_Nu=0`. This proves the canonical section and the exact orthogonal decomposition, including its kernel:

\[
R_Nu=\mathcal V\sum_{j=0}^Np_j\frac{b_j^*G_Nu}{\omega_j},
\qquad R_N^*R_N=G_N.
\]

The source jet and cohomology identities remain `J^{(k)}R_N=eta` and `q^{(k)}R_N=sigma_h^{tensor k} eta`. Its proved finite-section identity is

\[
W_N=A^*G_N+G_NA-kG_N
=\frac{G_N(b_{N+1}b_N^*+b_Nb_{N+1}^*)G_N}{\omega_N}.
\]

The antidual raising map `G_N:C -> C^#` sends `v` to `(w -> w^*G_Nv)`, so

\[
H=G_N^{-1}W_N=A^{\sharp_{G_N}}+A-kI_C
\]

is an endomorphism of the same coefficient space. It is `G_N` self-adjoint, has rank at most two, and has trace zero by the preceding reflection calculation. A self-adjoint rank-one endomorphism with zero trace is zero; otherwise the rank is two and the two nonzero real eigenvalues are opposite. Thus they are `+epsilon,-epsilon` for a unique nonnegative `epsilon`, with `epsilon=0` meaning `H=0`.

The exact two-column computation can be performed without replacing coordinates. Set `u=b_N`, `v=b_{N+1}`, and `omega=omega_N`. Then

\[
H=(vu^*G_N+uv^*G_N)/\omega,
\quad a=u^*G_Nu,\quad d=v^*G_Nv,\quad c=u^*G_Nv.
\]

Multiplication gives

\[
\operatorname{Tr}H=2\Re c/\omega,
\qquad
\frac12\operatorname{Tr}H^2=
\frac{ad+\Re(c^2)}{\omega^2}.
\]

The zero trace implies `Re(c)=0`; therefore `Re(c^2)=-|c|^2` and

\[
\epsilon^2=\frac{ad-|c|^2}{\omega^2}.
\]

This also proves that the source's purely imaginary cross term has the correct sign. Cauchy--Schwarz makes the numerator nonnegative. When the two columns are dependent the formula is still valid, including zero; no inverse of their 2-by-2 Gram has been used.

## 3. Exact exterior metric and generator

For `0<=p<=q`, the original alternating quotient is `wed:C^{tensor p}->wedge^p C`. The unscaled injection is

\[
\operatorname{Alt}_p(v_1\wedge\cdots\wedge v_p)
=\sum_{\pi\in S_p}\operatorname{sgn}(\pi)
v_{\pi(1)}\otimes\cdots\otimes v_{\pi(p)}.
\]

Each term maps under `wed` to `sgn(pi)^2` times the starting wedge, hence `wed Alt_p=p! I`. This gives the explicit left inverse `wed/p!`; it does not rescale the source representative. The case `p=0` uses `C^{tensor 0}=wedge^0 C=mathbb C`, the identity map and `0!=1`. For `p>q` the wedge space is zero.

For decomposable wedges `v,w`, expand the tensor inner product of both alternating sums. Setting the relative permutation to `sigma^{-1}pi` leaves `p!` identical copies of the determinant. Thus

\[
\langle\operatorname{Alt}_p v,\operatorname{Alt}_p w\rangle_{G_N^{\otimes p}}
=p!\det(\langle v_i,w_j\rangle_{G_N})_{i,j}.
\]

The determinant form is positive definite: its value on a nonzero decomposable vector is the Gram determinant of an independent list, and the alternating injection supplies a positive-definite form on the entire finite-dimensional wedge space. In the original increasing-index wedge basis its matrix is the compound matrix `G_N^{[p]}=(det(G_N)_{I,J})`.

The additive exterior generator is

\[
A^{[p]}(v_1\wedge\cdots\wedge v_p)
=\sum_{j=1}^pv_1\wedge\cdots\wedge Av_j\wedge\cdots\wedge v_p.
\]

It is related to the multiplicative exterior map by the product rule:

\[
\frac{d}{dt}\bigwedge^p(e^{tA})=A^{[p]}\bigwedge^p(e^{tA}),
\quad \bigwedge^p(e^{0A})=I.
\]

Uniqueness of the finite-dimensional linear ODE, proved directly by differentiating `e^{-tA^{[p]}} wedge^p(e^{tA})`, gives `wedge^p(e^{tA})=e^{tA^{[p]}}`. Its derivative at zero is the stated additive generator.

Differentiating the determinant pairing in one entry at a time gives `(A^{[p]})^{sharp}=(A^{sharp})^{[p]}`. Since `(kI)^{[p]}=kpI`, the exact identity is

\[
(A^{[p]})^*G_N^{[p]}+G_N^{[p]}A^{[p]}-kpG_N^{[p]}
=G_N^{[p]}H^{[p]}.
\]

For `epsilon>0`, retain the actual `G_N` orthogonal eigenspaces `L_+,Z_0,L_-` of `H`, of dimensions `1,q-2,1`. The direct sum of all wedge maps from their inclusions is an isomorphism

\[
\begin{aligned}
\bigwedge^pC={}&\bigwedge^pZ_0
\oplus(L_+\wedge\bigwedge^{p-1}Z_0)\\
&\oplus(L_-\wedge\bigwedge^{p-1}Z_0)
\oplus(L_+\wedge L_-\wedge\bigwedge^{p-2}Z_0).
\end{aligned}
\]

Orthogonality follows by the determinant pairing, since pairing vectors with different numbers of factors in one summand gives a zero row or column. The additive `H` eigenvalues on these four spaces are respectively `0,+epsilon,-epsilon,0`. The two nonzero multiplicities are `binomial(q-2,p-1)`, positive exactly for `1<=p<=q-1`. Thus the allowance is exactly `epsilon` on these exterior degrees. At `p=q` and `p=0` the additive control is zero; if `epsilon=0` it is zero for every degree.

## 4. Original cochains, support maps and full-product minimum

Let `mathcal C_k=C_+^{completed tensor k}`, with `C_+=[V ->Theta mathscr B]` in degrees zero and one. The canonical section has target `mathcal C_k^k`; the supplied primitive has target `mathcal C_k^{k-1}` and satisfies

\[
D^{(k)}R_N-R_NA=dK_N^{\rm prim}.
\]

The actual exterior representative and primitive are

\[
R_{N,p}=R_N^{\otimes p}\operatorname{Alt}_p,
\]

\[
K_{N,p}^{\rm prim}=
\sum_{j=1}^p(-1)^{k(j-1)}
R_N^{\otimes(j-1)}\otimes K_N^{\rm prim}\otimes
R_N^{\otimes(p-j)}\operatorname{Alt}_p.
\]

Their targets are respectively degrees `kp` and `kp-1` of the same `kp`-fold original complex. On the `j`th summand of the primitive, the tensor differential contributes exactly `(-1)^{k(j-1)}` from the preceding top-degree factors. Derivatives of the other top-degree factors are zero. Hence the displayed coefficient and the differential sign multiply to one. Adding the `p` remaining terms and using the intertwining identity for `Alt_p` proves

\[
D^{(kp)}R_{N,p}-R_{N,p}A^{[p]}=dK_{N,p}^{\rm prim}.
\]

At the cochain level, adjacent block swaps of two degree-`k` elements have Koszul sign `(-1)^{k^2}=(-1)^k`. A permutation therefore acts in top degree as `T_pi=sgn(pi)^k P_pi`. The chain operator

\[
\mathsf A_{p,k}=\frac1{p!}\sum_{\pi\in S_p}
\operatorname{sgn}(\pi)^{k+1}T_\pi
\]

is idempotent: in its square, for each fixed product permutation there are `p!` pairs of factors and their characters multiply to the character of the product. Its top-degree action is `Alt_p wed/p!` because the two powers of the sign give `sgn(pi)`. It commutes with `d`, and therefore its image and the image of `1-mathsf A_{p,k}` split cycles and boundaries. The explicit maps from image cohomology to full cohomology and back are induced by inclusion and this idempotent; their composites are the identity on image cohomology and the induced idempotent on the full quotient. Both complexes and both cohomologies remain.

The source Gram and finite observations are exactly

\[
R_{N,p}^*R_{N,p}=p!G_N^{[p]},\quad
J^{(kp)}R_{N,p}=I_{k,p}:=\eta^{\otimes p}\operatorname{Alt}_p,
\]

\[
q^{(kp)}R_{N,p}=(\sigma_h^{\otimes k}\eta)^{\otimes p}\operatorname{Alt}_p.
\]

For an explicit left inverse to the last map, take the original finite-jet descent in each `k`-block, then the invariant Reynolds projection, then the supplied `pi` with `pi eta=I`, tensor these maps, and finally apply `wed/p!`. On the displayed image the result is `I`. This establishes the injection without taking a quotient by a topological closure or presuming that an arbitrary completed tensor preserves every injection.

For the reconstructed split lift, a linear map `f:M->N` acts by `G(f)(tau)=tau` and `G(f)(x^bullet)=f(x)^bullet`. With the original operations `tau+x=x`, `tau x=tau`, and `x^bullet+y^bullet=(x+y)^bullet`, linearity verifies addition and scalar compatibility case by case. Thus `G(f)(e)=e` even if `f` has a kernel. In a support diagram, the same formula is used in each coefficient fibre and the prescribed support map carries labels; a sum uses the join of its actual input labels. A term whose coefficient vanishes remains at the receiving fibre zero. In particular, the map to cohomology sends `dK` to its receiving supported zero; only an externally absent input is sent to external absence. The character average requires the already specified orbit-join support map, not an identification of distinct active labels.

For the full `kp`-variable degree space, choose `M>=max(pN,kp(deg h-1))`. The degree of a product of `p` degree-`N` block polynomials is at most `pN`; the bound `kp(deg h-1)` includes every monic remainder basis vector for the full quotient. Thus the full-jet canonical section exists in that same degree space. Since `I_{k,p}` intertwines `A^{[p]}` with multiplication by the total sum, the difference

\[
\Delta=R_{N,p}-R_{kp,M}^{\rm full}I_{k,p}
\]

has zero full jets. The original monic division gives its numerator in `(h(s_1),...,h(s_{kp}))`; the already constructed division primitives give an original theta boundary. Minimum-norm orthogonality gives

\[
p!G_N^{[p]}=I_{k,p}^*G_{kp,M}^{\rm full}I_{k,p}+\Delta^*\Delta.
\]

Multiplying this equality on the left and right by the corresponding generators and subtracting the literal weight `kp` gives

\[
\begin{aligned}
W_{N,p}^{\rm source}={}&I_{k,p}^*W_{kp,M}^{\rm full}I_{k,p}\\
&+(A^{[p]})^*\Delta^*\Delta+\Delta^*\Delta A^{[p]}-kp\Delta^*\Delta.
\end{aligned}
\]

This proves the metric comparison with its complete boundary correction; an inverse-compression identity for an oblique projector is never required.

## 5. Determinant line, full spectral blocks and projectors

Let `V=C_>=direct sum_{Re lambda>k/2} C_lambda`, and set `p=dim V=sum ell_lambda`. All generalized eigenspaces are full CRT factors. If `p>0`, reflection implies `p<q`. The map `wedge^p V -> wedge^p C -> R_{N,p} mathscr B^{completed tensor kp}` is injective by the previous left inverse.

The additive action on `det V` is `zeta_>=Tr(A|V)`: expanding a wedge of a basis, an off-diagonal replacement repeats another basis vector and vanishes. Every diagonal entry remains once. On a local factor, multiplication by `S` is `lambda I` plus the nilpotent shift in its full `ell_lambda`-element monic basis, so its trace is `ell_lambda lambda`. Thus

\[
L=2\Re\zeta_>-kp
=\sum_{\Re\lambda>k/2}\ell_\lambda(2\Re\lambda-k).
\]

On a nonzero determinant vector its actual source control Rayleigh quotient is exactly `L`, since both Gram and control contain the same displayed `p!`. The exterior order bound therefore proves `0<=L<=epsilon`. For `p=0`, `L=0` and the inequality holds directly. Reflection also proves

\[
L=\frac12\sum_\lambda\ell_\lambda|2\Re\lambda-k|
=\sum_\lambda\ell_\lambda|\Re\lambda-k/2|.
\]

For an original column inclusion `B:mathbb C^p->C` of `V`, set `G_>=B^*G_NB>0`. The determinant source norm is `p! det G_>`. In these coordinates put `A_>=B^{-1} A B`, where `B^{-1}` means its inverse from `V` to its specified coordinate space. For `a>0`, `U_>(a)=exp((log a)A_>)`. The determinant of its exponential is `exp((log a)Tr A_>)`: this follows by differentiating the determinant on the invertible matrix exponential and solving its scalar ODE. Consequently

\[
\det(U_>(a)^*G_>U_>(a))=a^{kp+L}\det G_>.
\]

The order estimate integrates to the source's two-sided powers for `a>=1`; for `0<a<=1` the order of the two exponents reverses. The exact volume equality itself holds for every positive `a`.

Let `Q=e_>(A)` be the CRT spectral projector and

\[
P=B(B^*G_NB)^{-1}B^*G_N.
\]

The extraction `L_B=(B^*G_NB)^{-1}B^*G_N` obeys `L_B B=I`, so `P^2=P`, `P^{sharp}=P`, and its range is `V`. Both `P` and `Q` are identity on that range. This proves `QP=P`, `PQ=Q`, and by direct expansion `(P-Q)^2=0`. In the orthogonal decomposition `V direct sum V^{perp_G}`, invariance of `V` puts `A` in the form `[[A_>,T],[0,A_0]]`; therefore `Tr(PA)=Tr A_>=Tr(QA)`. Gram self-adjointness of `P` also gives `Tr(P A^{sharp})=conj(Tr(PA))`. Hence `Tr(PH)=L`.

For `epsilon>0`, polynomial functional calculus gives the two rank-one orthogonal control projections

\[
F_\pm=(H^2\pm\epsilon H)/(2\epsilon^2),\qquad
H=\epsilon(F_+-F_-).
\]

Since `P` and `F_pm` are orthogonal projections,

\[
\|(1-P)F_+\|_{\rm HS,G}^2=1-\operatorname{Tr}(PF_+),\quad
\|PF_-\|_{\rm HS,G}^2=\operatorname{Tr}(PF_-).
\]

These equalities follow by inserting their self-adjoint idempotences into `Tr(T^{sharp}T)` and cycling the finite trace. Substitution proves the full source slack formula. The complement has its original finite trace `Tr((1-Q)f(A))`. The contour expression is obtained from each local resolvent expansion: the coefficient of `(z-lambda)^{-1}` in `z Tr((zI-A)^{-1})` is `ell_lambda lambda`; higher nilpotent powers have zero trace. A positively oriented contour enclosing exactly the positive blocks therefore gives `zeta_>`.

A scope qualification applies to the source's phrase that the complementary cochain idempotent has its own cohomology and trace. The chain calculation proves a splitting of the entire original cohomology. Its ordinary finite trace is defined after restriction to the retained finite invariant arithmetic module, such as `C^{tensor p}` embedded by the block source sections and then observed in cohomology. The character idempotent restricts to this finite module, commutes with its additive generator, and the direct-sum isomorphism from its image and kernel proves `Tr(f(A_tot))=Tr(f(A_tot)|image)+Tr(f(A_tot)|kernel)` there. No ordinary trace on the entire possibly infinite-dimensional theta cohomology follows solely from the existence of an idempotent. All trace calculations in the exterior determinant theorem take place on the displayed finite modules and need no such additional trace.

The companion equality continuation proves the additional exact cross-map estimate and all equality cases. It does not change these source formulas.

## 6. Quartet count and every collision

Now take `h` to consist of the complete four distinct roots

\[
\rho_{\varepsilon,\eta}=\tfrac12+\varepsilon\delta+i\eta\gamma,
\quad \delta>0,\quad\gamma>0,\quad m_{\rho_{\varepsilon,\eta}}=m\ge1.
\]

The four roots are distinct because both real parameters are nonzero. Reflection and complex conjugation preserve the order of a zero under their invertible local coordinate maps, so an actual off-line nonreal zero supplies exactly these equal-order roots.

The conjugation identity used here also follows in the original presentation. On `Re s>1`, termwise conjugation of the absolutely convergent zeta series gives `conj(zeta(s))=zeta(conj(s))`; conjugating the Euler integral for `Gamma(s/2)` and the real-base factor `pi^{-s/2}` gives the same identity for every other factor of `g`. The polynomial `s(s-1)` has real coefficients. Therefore `g(conj(s))=conj(g(s))` in that half-plane and, by the identity theorem, for its entire continuation. If `g(rho+z)=z^m v(z)` with `v(0)!=0`, conjugation gives `g(conj(rho)+z)=z^m conj(v(conj(z)))`, and reflection gives `g(1-rho+z)=(-z)^m v(-z)`. Their leading coefficients are nonzero, proving equal full orders with the displayed signs retained.

For `0<=a,b<=k`, the interval

\[
\max(0,a+b-k)\le t\le\min(a,b)
\]

contains an integer. Indeed `0<=min(a,b)`, and `a+b-k<=a,b` because `a,b<=k`. The occupation table

\[
\begin{array}{c|cc}
 & +i\gamma & -i\gamma\\\hline
+\delta&t&a-t\\
-\delta&b-t&k-a-b+t
\end{array}
\]

has nonnegative integer entries and the required row and column sums. Thus all the sums

\[
\lambda_{a,b}=k/2+\delta(2a-k)+i\gamma(2b-k)
\]

occur. Conversely every tuple has such margins. Equality of two sums implies separately `2delta(a-a')=0` and `2gamma(b-b')=0`; hence `a=a'` and `b=b'`. Different tables can collide at one margin pair, but every such tuple has the same local length `ell_k=1+k(m-1)`. The collision maximum remains exactly that length. Therefore

\[
\chi_{h,k}=\prod_{a,b=0}^k(S-\lambda_{a,b})^{\ell_k},
\quad q=\ell_k(k+1)^2.
\]

The condition `Re(lambda)>k/2` is exactly `a>k/2`; its number of allowed `a` is `ceil(k/2)`. Thus `p=ell_k(k+1)ceil(k/2)`. Each positive margin contributes `2delta(2a-k)` per local dimension. Summing gives

\[
L=2\delta\ell_k(k+1)\sum_{a=\lfloor k/2\rfloor+1}^k(2a-k).
\]

For `k=2n`, put `a=n+j`, `1<=j<=n`: the last sum is `sum 2j=n(n+1)`. For `k=2n+1`, put `a=n+1+j`, `0<=j<=n`: it is `sum(1+2j)=(n+1)^2`. Both equal `floor((k+1)^2/4)`, giving exactly

\[
\boxed{\epsilon_{h,k,N}^{\rm cyc}\ge
2\delta[1+k(m-1)](k+1)\left\lfloor\frac{(k+1)^2}{4}\right\rfloor},
\qquad N\ge[1+k(m-1)](k+1)^2-1.
\]

The imaginary contribution to the determinant trace vanishes by the explicit finite sum `sum_{b=0}^k(2b-k)=0`, not by deleting a conjugate block. The leading term is `delta k^3/2` when `m=1`; for `m>1` it is `delta(m-1)k^4/2`. These leading coefficients follow from the two parity polynomials just computed.

If the packet contains additional complete roots, the displayed formula for its entire `chi` and dimension must be replaced by the actual larger packet polynomial. The quartet lower bound survives: each quartet sum is still present and its length in the larger packet is at least `ell_k`; any additional positive sums add nonnegative contributions. The required degree is then the actual larger `deg chi-1`, not merely the quartet threshold.

Here is the exact map behind that comparison. For packet polynomials `h|H` with complete unchanged orders on the roots of `h`, reduction gives `pi:B_H->B_h`; multiplication by the total sum intertwines, so `chi_h|chi_H` and there is the unital quotient `r:C_H->C_h`. Put `q_0=H/h`. Its jets on the roots of `h` are units. The module map

\[
F=M_{j_h(q_0)^{\otimes k}}\pi:B_H\longrightarrow B_h
\]

satisfies `F eta_H=eta_h r`, because `(g/h)=q_0(g/H)` before taking any jets. The corresponding original amplitude map is multiplication by `prod_i q_0(s_i)` in Mellin coordinates, equivalently `prod_i q_0(D_i)` on the original source. It retains the degree increase and every unit; it does not identify the two canonical metrics.

For `delta=0`, the displayed four-root list collapses to a critical pair and every real defect is zero. For `gamma=0`, it collapses to a real reflected pair, whose cyclic dimension is `ell_k(k+1)` and whose lower bound lacks the factor `k+1`. These collapsed presentations are related by the explicit equal-coordinate identification of their root sets; one must rebuild `h` with the original distinct roots and their actual orders, rather than count duplicates as new roots. The nonreal quartet theorem explicitly assumes both parameters positive.

There is no omitted actual real zero in `0<s<1`. The alternating series `eta(s)=sum_{n>=1}(-1)^{n-1}n^{-s}` converges there. Its even partial sums equal sums of positive pairs `(2j-1)^{-s}-(2j)^{-s}`, and their limit is at least the first positive pair, so `eta(s)>0`. The identity `eta(s)=(1-2^{1-s})zeta(s)` follows first from absolutely convergent series for `Re s>1` and then by continuation into `Re s>0`, away from the removable singularity at one. For `0<s<1` the factor is strictly negative, so `zeta(s)<0`. Thus any actual nontrivial off-line zero is nonreal and its full quartet is covered.

## 7. Empty and low-dimensional cases

For `h=1`, the ideal `(h(s_1),...,h(s_k))` is the whole polynomial ring and every positive-depth quotient is zero. The finite cyclic module is zero, `q=0`, and there is no positive-dimensional Gram inverse or positive spectral determinant line. The split module `G(0)` still has its two distinct elements `e` and `tau`; their coefficient maps are the unique maps prescribed above. The analytic function `g` remains nonzero and its norm is not used to manufacture a finite spectral packet.

For a nonempty packet with `q=1`, reflection forces the unique sum's real part to be `k/2`, and the self-adjoint traceless control is zero. The only positive exterior degree is the top degree, with zero additive control. For `epsilon=0`, `A^{sharp}+A=kI`; thus shifting by `kI/2` gives a Gram skew-adjoint endomorphism, which is diagonalizable with imaginary spectrum, so every sum has zero real defect. This conclusion concerns the actual finite operator and retains the original Gram through the displayed equality.

For `p=0`, the trace inequality reads `0<=epsilon`; the determinant convention is `det(0)=mathbb C`. For `p=q`, the full determinant control is zero by trace reflection. A nonempty positive spectral subspace never has `p=q`, since it has a distinct reflected negative partner of equal dimension. Critical-line nontrivial Jordan factors are fully retained; their zero real trace contribution does not force their numerical control to vanish.

## 8. Exact meaning of the analytic target

The established theorem is the lower estimate for the source's precise `epsilon`. The remaining analytic quantity is

\[
\frac{\sqrt{a_Nd_N-|c_N|^2}}{k^3\omega_N},
\qquad N=N(k)\ge[1+k(m-1)](k+1)^2-1.
\]

For a fixed actual quartet its positive lower bound has limit `delta/2` after division by `k^3` in the simple case, and grows linearly in `k` for repeated roots. Consequently the requested upper behavior would contradict the existence of that packet. No upper estimate is supplied by the lower-bound argument itself. Constants depending on a fixed `h` do not affect this contradiction. The degree threshold grows quadratically for simple roots and cubically for repeated roots. The scalar constant-column Fisher identity cannot control the required growing polynomial degree without its missing calculation.

All polynomial moments remain those of `w_h`, with the literal mass and the derivative term

\[
\frac1k\mathcal N_h(z)\mathcal M_h(z)^{k-1}
+\frac{k-1}{4k}z^2\mathcal M_h(z)^k.
\]

Their passage to the inverse interpolation matrix is still part of the arithmetic problem. The new equality theorem and off-diagonal correction characterize precisely when the determinant lower bound is attained; they do not provide an asymptotic upper estimate for this matrix.

## 9. Finite checks and primary-reference scope

The reusable `scripts/replay_exterior_trace_delivery.py` verifies all 35 exterior archive members against their staged original bytes, all 34 exterior manifest entries, the separately supplied 43-member/42-entry cyclic archive, and the identities asserted by the source's historical receipt. It executes a copy of the completely inspected checker in normal, optimized, negative-normal and negative-optimized modes, with every output confined to `checks/exterior_trace_delivery_replay`. It pins SymPy 1.14.0 and records the actual Python version separately from the source's recorded Python 3.13.5. Its local replay receipt is the authoritative execution evidence.

The checker has 22 declared methods. Its exterior Gram and generator methods test actual exact finite matrices, including a non-diagonal positive Gram and nonnormal operator. Its canonical Gaussian computations use the declared mass `7^k`, with quartet examples at `k=1,2`. The repeated-jet trace test explicitly retains a three-dimensional Jordan block. Quartet grids are enumerated only for the declared small degrees; the all-degree proof is Section 6 above. The Koszul methods check the two scalar parity factors and permutation parity. They do not instantiate the full topological theta complex. The supported-zero methods use declared toy records and quotient remainders; they do not certify every reconstructed support diagram. Those full statements rely on the explicit written maps and existing source constructions, not the fixture names.

The actual old local cyclic replay can be attached with `--cyclic-replay-receipt`. The exterior replay validates every listed output byte in that receipt before recording its four results. It labels that as adopted earlier fresh local evidence, not a second execution of the cyclic checker. The exterior ZIP's historical 24-method statements alone are not treated as new local runs.

Primary reference pages were checked directly on 12 September 2026:

- [Stacks Project, Tag 0GWN](https://stacks.math.columbia.edu/tag/0GWN): the tensor differential and degree-dependent commutativity sign agree with the explicit calculation in Section 4.
- [DLMF 25.4](https://dlmf.nist.gov/25.4): equations 25.4.3 and 25.4.4 retain the reflection and the literal factor `1/2` in `xi`, hence the source's `g=2xi`.
- [Overton and Womersley, SIAM 13(1), 41–45](https://epubs.siam.org/doi/10.1137/0613006): the official abstract attributes the extremal eigenvalue-sum principle to Ky Fan. The rank-two proof used here is written in full above; no reading of an inaccessible full article is claimed.

No source command was treated as an instruction to change branches, publish, contact another task, or run Lean. Original source bytes and frozen editions remain untouched by this review.

## 10. Completed local replay result

The fresh replay completed successfully under Python 3.13.9 and SymPy 1.14.0. Normal and optimized modes each executed all 22 methods with zero failures and zero errors. Each negative mode executed those same 22 methods and produced exactly one intended failure, zero errors, and exit status one. Successful JSON records agree byte-for-byte; negative JSON records also agree byte-for-byte. All exterior and cyclic source bytes and both archives remained unchanged.

The authoritative receipt is `checks/exterior_trace_delivery_replay/replay_receipt.json`, SHA-256 `4539829ce3b6699a232cb10ff351fe21a9a4d12406dde8fb5710f7f6e96b8aa6`. It records all 35/34 exterior and 43/42 cyclic archive/manifest comparisons. It also validates all 16 listed output files in the earlier independent cyclic replay before adopting that replay's successful 24-method normal/optimized runs and its two exactly-one-failure controls. The older cyclic checker was not redundantly executed by this exterior audit.

The equality continuation has additionally received an independent mathematical derivation of its determinant-slack identity and its full critical generalized-block proof. This is a second written proof check; it is not a numerical or formal certificate.
