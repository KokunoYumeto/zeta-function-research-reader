# Independent derivation of the local algebra and moving quotient

The mathematical claims in RLA1–35 and RQT1–19 survive this independent check. In particular, the branch injection in RLA17 is valid, the annihilator in RLA18 is exact, and the two-angle formula RQT10 and determinant product RQT13 use the original Gamma metric. RQT16 matches the actual supplied audit equation (11), read directly in its section 2.4, including its factorial and every Gamma factor. The following calculations give the reasons and an additional complete result: `REAL_PAIR_ANGLE_CONSTANTS.tex`, RQT20–22, evaluates both angle constants rather than only their orders.

## Sources actually read

The full text of `REAL_PAIR_LOCAL_ALGEBRA.tex` RLA1–35 and `REAL_PAIR_MOVING_QUOTIENT.tex` RQT1–19 was read. The former snapshot has SHA256 `28331cce44339ee3831538399f5c5ba615f024c8c74174e1a28a121fac7b69d9`; the latter reviewed snapshot has SHA256 `aa70ca553789e0e98be7c9f8c581d0f96a28bf08da73512dea799e30e28f3243`. WCF's original source was read at WCF1–13 and WCF19a and adjacent determinant text, to check the frames, full coefficient bound, and original source order. The supplied audit was read directly, rather than inferred from later references: its text has SHA256 `9a98d176f44bde876d25c78724d4019187964134004e78492fbc999ab4b4156e`. It is chatbot-authored supplied material, not a human literature source, and its private correspondence is not reproduced here.

The exact original-metric source is [WCF1–6 and the following forward estimates](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/WEIGHTED_CONDUCTOR_FORWARD.tex#L28). Its DLMF references for the Meixner–Pollaczek weight, norm, recurrence and generating function remain attached to that source. This review imports no fresh external theorem and claims no new reading of DLMF. The complete RPD directional source was derived and checked in the preceding mathematical task; RPD13–30 supplies the inverse matrix limits used in the added angle proof. RPZ's full-series certificate and provenance remain unchanged.

## The actual analytic object and its inverse parameter maps

Let the certified point be (p_*), and put (G=f_1f_2), (B=G_\xi(0,p_*)\ne0), (A_z=G_z(0,p_*)), (A_x=G_x(0,p_*)), and (\Delta=\Im(\overline{A_z}A_x)\ne0). The coefficient-reflected function is (G^\#(\xi,p)=\overline{G(\bar\xi,\bar p)}). This is holomorphic, whereas pointwise conjugation at a complex parameter would not be. The complex derivative of ((G(0,p),G^\#(0,p))) is

\[
J_\mathbb C=\begin{pmatrix}A_z&A_x\\\overline{A_z}&\overline{A_x}\end{pmatrix},
\qquad \det J_\mathbb C=-2i\Delta.
\]

The inverse printed in RLA4 is its literal adjugate divided by this determinant. Its contraction iteration is valid on a sufficiently small complex ball: the derivative of the iteration is zero at the center, hence at most (1/2) on a smaller closed ball; sufficiently small target values move the center by at most one quarter of the radius. The iterates remain inside the ball and converge geometrically and uniformly on smaller parameter sets. The Cauchy integral formula then gives a holomorphic limit. Uniqueness proves both inverse compositions. This proves the exact two-parameter coordinate map and restores both original coordinates after every use of the new pair.

With (\omega(t)=-i\arctan t), the two actual factors (F_+=G(\omega(t),p)), (F_-=G^\#(\omega(t),p)) have derivatives (-iB,-i\bar B) at the base point. The two scalar contraction arguments in RLA5 therefore produce their actual roots (\alpha(p),\beta(p)). The integral division in RLA6 is exact, so

\[
g(t,p)=U(t,p)(t-\alpha)(t-\beta),\qquad U(0,p_*)=-|B|^2=-b.
\]

All unit coefficients are retained. Differentiating the root equations gives (D\alpha=-i(A_z,A_x)/B) and (D\beta=-i(\bar A_z,\bar A_x)/\bar B), with determinant (2i\Delta/b\ne0). RLA9 supplies the inverse by a second contraction; it does not stop at the derivative determinant.

The signs in the reflection also check. Since (\overline{\omega(-\bar t)}=\omega(t)), uniqueness gives (\beta=-\alpha^\sharp). Thus on the real parameter slice (\beta=-\bar\alpha), not (+\bar\alpha). In particular

\[
g_0=U_0\alpha\beta=-U_0|\alpha|^2>0
\]

away from the certified point in a sufficiently small real neighborhood, because (U_0) remains negative there. The two complex parameter branches (\alpha=0) and (\beta=0) meet transversely. The spectral collision curve (\alpha=\beta\ne0) has (g_0\ne0) and is therefore not a singular locus of the finite old conductor.

## The complete finite module and an explicit presentation comparison

Set (R=\mathbb C\{\alpha,\beta\}), (q=t^2-(\alpha+\beta)t+\alpha\beta), and (R_N=R[t]/(t^N)). Since (U_0) is a unit, multiplication by (U\bmod t^N) is invertible with exactly the recurrence printed in RLA11. Therefore the target identity induces

\[
\operatorname{coker}L_N(g)=R_N/(g)=R_N/(q)=R[t]/(q,t^N)=\mathcal M_N.
\]

The source change is (L_N(U)); it is not an isometry. Polynomial division by the monic quadratic gives the free rank-two module (R[t]/q) with basis (1,t). Multiplication by (t) has matrix

\[
C=\begin{pmatrix}0&-\alpha\beta\\1&\alpha+\beta\end{pmatrix}.
\]

The columns of (C^N) are the remainders of (t^N) and (t^{N+1}). Every multiplier modulo (q) has degree at most one, so these generate the entire image of multiplication by (t^N). This proves (\mathcal M_N\simeq\operatorname{coker}C^N), including (N=1).

The identity of Fitting ideals with the original (N\times N) presentation has an explicit generator/relation proof. Start with generators (1,t,\ldots,t^{N+1}) and relations

\[
q,tq,\ldots,t^{N-1}q,\ t^N,\ t^{N+1}.
\]

Eliminating the generators (t^N,t^{N+1}) by the last two unit-coefficient relations gives the original (N)-generator multiplication-by-(q\bmod t^N) presentation. Alternatively, eliminate (t^2,\ldots,t^{N+1}) successively by the first (N) relations, each having leading coefficient one. The two remaining generators are (1,t); the two remaining relations are precisely the columns of (C^N). Each elimination removes an identity block, so the stated Fitting ideals agree by the determinant expansion for minors. This supplies a direct presentation-level justification, without relying on agreement of fibers.

Writing (h_n=\sum_{j=0}^n\alpha^{n-j}\beta^j), one obtains exactly

\[
C^N=\begin{pmatrix}-\alpha\beta h_{N-2}&-\alpha\beta h_{N-1}\\h_{N-1}&h_N\end{pmatrix},
\quad \operatorname{Fitt}_0=(\alpha^N\beta^N),
\quad \operatorname{Fitt}_1=(h_{N-1},\alpha\beta h_{N-2}).
\]

For (N\ge2), the latter ideal vanishes only at the origin: on either branch its first generator is the nonzero root raised to (N-1); off both branches, two consecutive (h)'s cannot vanish because backward recurrence would give (h_0=0). For (N=1), (h_0=1) makes the first Fitting ideal (R), consistent with the one-generator presentation.

## Branch gluing and the annihilator

The evaluation embedding

\[
R[t]/q\longrightarrow R^2,\qquad a+bt\longmapsto(a+b\alpha,a+b\beta)
\]

has image (\mathcal L=\{(v_+,v_-):v_+-v_-\in(\alpha-\beta)\}). The inverse on this lattice is (b=(v_+-v_-)/(\alpha-\beta)), (a=v_+-b\alpha). Division here is justified by membership in the principal ideal; it is not inversion of (\alpha-\beta) in the local ring.

Multiplication by (t^N) becomes (\operatorname{diag}(\alpha^N,\beta^N)) acting on that lattice. The potentially dangerous point in RLA17 is whether quotienting the lattice injects into the quotient of the ambient (R^2). It does. Suppose ((\alpha^Nr,\beta^Ns)\in\mathcal L). Modulo (\alpha-\beta), one has

\[
\alpha^N(r-s)=0\quad\text{in }R/(\alpha-\beta)\simeq\mathbb C\{\alpha\}.
\]

Multiplication by (\alpha^N) is injective in this one-variable integral domain. Hence (r-s\in(\alpha-\beta)), so ((r,s)\in\mathcal L). Thus

\[
\mathcal L\cap\bigl((\alpha^N)\oplus(\beta^N)\bigr)
=\operatorname{diag}(\alpha^N,\beta^N)\mathcal L.
\]

This proves precisely the asserted injection, with no missing torsion term. The difference map to (R/(\alpha-\beta,\alpha^N)) is well defined because (\beta^N\equiv\alpha^N) modulo (\alpha-\beta). A pair in its kernel can be adjusted by a multiple of (\alpha^N) in its first coordinate so that its difference is divisible by (\alpha-\beta). It therefore comes from the lattice. The difference map is onto by using pairs ((r,0)). These arguments prove the full short exact sequence RLA17.

Both projections of (\mathcal M_N) onto the branch modules are onto: constant polynomials already give any chosen residue in either component. An annihilator must therefore lie in both ((\alpha^N)) and ((\beta^N)). Conversely any element of their intersection kills the ambient direct sum and hence the embedded module. Finally the convergent two-variable power series show

\[
(\alpha^N)\cap(\beta^N)=(\alpha^N\beta^N).
\]

This verifies RLA18 exactly.

The gluing quotient has complex length (N), since it is (\mathbb C\{\alpha\}/(\alpha^N)). The module is not the direct sum of its two branch modules for any (N\ge1). At (N=1), its minimal number of generators is one, whereas the direct sum needs two. At (N\ge2), its first Fitting ideal contains the nonzero homogeneous polynomial (h_{N-1}) of degree (N-1), whereas the first Fitting ideal of (R/(\alpha^N)\oplus R/(\beta^N)) is ((\alpha^N,\beta^N)), all of whose elements have order at least (N). Isomorphic modules have the same Fitting ideals by the presentation argument above. This proves the nonidentity without discarding the exact embedding and gluing morphism relating them.

## Exact relation of that module to the original metric operator

For the original weighted matrix (B=D_\rho^{-1}T_D(g)D_\rho), coefficient reversal (J_N) gives (T_D(g)=J_NL_N(g)J_N). Thus the source and target coordinate morphisms in RLA22 intertwine the actual matrix with multiplication by the complete series modulo (t^N). Transporting the original orthonormal coefficient norm gives

\[
W_{N,s}=J_ND_\rho^{-2}J_N,
\]

exactly RLA23. Applying the source change (L_N(U)) produces the Gram ((L_N(U)^{-1})^*W_{N,s}L_N(U)^{-1}); the target Gram stays (W_{N,s}). This keeps the complete analytic unit's norm effect.

For the finite Schur presentation, direct block multiplication gives

\[
\begin{pmatrix}I&0\\-R_0P^{-1}&I\end{pmatrix}
\begin{pmatrix}P&Q\\R_0&S_0\end{pmatrix}
\begin{pmatrix}P^{-1}&-P^{-1}Q\\0&I\end{pmatrix}
=\begin{pmatrix}I&0\\0&S_0-R_0P^{-1}Q\end{pmatrix}.
\]

The pivot is invertible near the base point because its diagonal there is (-b\rho_{i+2}/\rho_i\ne0). The source column permutation is unitary and has sign ((-1)^{2(N-2)}=1). Consequently the residual determinant and both Grams in RLA27 have the stated signs and factors. In particular, the singular values are determined by the generalized Hermitian eigenvalue equation RLA28 with both Grams present. They cannot be inferred from (C^N) or the residual (2\times2) matrix with an arbitrarily assigned Euclidean norm.

The actual order table RLA29 follows by multiplying the full unit by ((t-\alpha)(t-\beta)). At order (v=0,1,2), the original quotient matrix in RLA30 has diagonal (g_v\rho_{j+v}/\rho_j\ne0). The old fixed-space kernel is nevertheless nonzero at (v>0). The descending coefficient equations in RLA32 use the coefficient of (S'^k), namely (\sum_{n\ge k}\binom nk\mu_{n-k}c_n); setting the lower (v) coefficients as separately retained data makes the inverse exact. RLA33 is its literal (v=1) specialization. RLA35's conjugate-linear Gram expands ((c-iy)^j(c+iy)^k) with the correct factors ((-i)^ai^d), and retains every cross term in the reconstructed four-state source.

## The moving quotient and the two angles

The projection in RQT1 is essential. It defines a surjective (N\times(N+2)) matrix (R=[L\ H]) near the root, but its kernel off the order-two locus is not the kernel of the unprojected operator. The text makes this distinction explicitly and proves the exact map on each actual-order domain.

With (Z=H^{-1}L), the kernel is ((l,-Zl)), and each quotient class is determined by (w=h+Zl). Minimizing (\|l\|^2+\|w-Zl\|^2) gives the unique normal equation ((I+Z^*Z)l=Z^*w). It yields (l=Z^*Mw,h=Mw), with (M=(I+ZZ^*)^{-1}), and squared quotient norm (w^*Mw). The isometries in RQT5 therefore satisfy (Q_+^*Q_+=I), (Q_K^*Q_K=I), (Q_K^*Q_+=0). Their combined dimensions are (N+2), proving the full orthogonal decomposition. The exact quotient matrix is (\widetilde A=HM^{-1/2}).

For any actual-order insertion (J_v), the factorization (A_v=\widetilde A T_v), (T_v=Q_+^*J_v), follows from (RQ_K=0), not from a determinant comparison alone. Its Gram correction is (E_v=T_v^*T_v). Taking squared absolute determinants gives RQT8 with every original weight. At the root (J_2=Q_+), so that correction is exactly the identity; it is not the identity on the other strata by assumption.

For the old source, let (F=J_0^*Q_K) and (V=J_{\rm tail}^*Q_K). Then

\[
E_0=I_N-FF^*,\qquad F^*F=I_2-V^*V.
\]

The positive eigenvalues of (FF^*) and (F^*F) coincide with multiplicities. Adding the (N-2) zero eigenvalues of (FF^*) gives exactly

\[
\operatorname{spec}(E_0)=\{1\text{ repeated }N-2\}\cup\operatorname{spec}(V^*V).
\]

This proves RQT10 even when either eigenvalue is zero or one, and at the endpoint (N=2). Since (V=-Z_{\rm bot}(I+Z^*Z)^{-1/2}), its two singular values are the actual sines of the kernel/source angles in the original metric.

The old matrix factors through (H) as

\[
H^{-1}B(l,m)=(Z_{\rm top}l+m,Z_{\rm bot}l).
\]

Swapping blocks of widths two and (N-2) has positive sign, so (\det Z_{\rm bot}=g_0^N/\det H). Thus

\[
d_1d_2=|\det V|
=\frac{|g_0|^N}{|\det H|\sqrt{\det(I+Z^*Z)}}
=\frac{|g_0|^N}{\sqrt{\det(RR^*)}},
\]

which independently verifies RQT13. The second equality of determinants uses the common nonzero eigenvalues of (ZZ^*) and (Z^*Z). Submultiplicativity applied to both (B^{-1}=T_0^{-1}\widetilde A^{-1}) and (T_0^{-1}=B^{-1}\widetilde A) proves both inequalities in RQT14. No individual singular-value constant is preserved merely because the extra factor is bounded.

## Literal equation (11), with the actual order on every stratum

The supplied audit uses (d=D+1), (N_{\rm audit}=D+v), (b_s=s/2), and the shifted symbol (t^{-v}e^{-4\omega}E_A(\omega)). RQT uses (N=D+1), (n_v=D+v), and the unshifted (g=e^{-4\omega}E_A(\omega)). The exact translation is therefore (d_{\rm audit}=N_{\rm RQT}), (N_{\rm audit}=n_v), and ((g_j)_{\rm audit}=(g_{j+v})_{\rm RQT}). With that dictionary, the coefficients and all domains agree.

The audit's coefficient estimate follows from the original Cayley powers. Their real exponent is bounded by (4\delta), their imaginary exponent by (4\gamma), so Cauchy at radius (m/(m+1)) gives (e^{1+2\pi\gamma}A_{\rm abs}(2m+1)^{4\delta}). The (m=0) coefficient obeys the same estimate directly. For (s=1), the weight induction is exact because

\[
(4n+5)(n+\tfrac12)^2-(4n+1)(n+1)^2=\tfrac14>0.
\]

For (s=a_{\rm amp}\ge9), the weights decrease. Thus RQT15 equals the audit's forward constant, with its original (a_{\rm amp}=4\ell+1\ge9) restriction inherited from WCF. This is a fixed-quartet finite-matrix bound; it does not assert uniformity in the cutoff, amplification or quartet beyond its displayed dependence.

The determinant of the actual-order matrix is

\[
\det A_v=\left(\frac{(-i)^v\mu_v}{v!}\right)^N
\prod_{j=0}^D\frac{\rho_{j+v}}{\rho_j}.
\]

Multiplying its singular values yields the complementary exterior identity. The reciprocal Gamma ratio is exactly

\[
\prod_{j=0}^D\frac{\rho_j}{\rho_{j+v}}
=\prod_{j=0}^D\prod_{k=1}^v
\left(\frac{j+b_s+k-1}{j+k}\right)^{1/2}.
\]

Substitution proves the audit's equation (11) verbatim as a mathematical formula, without importing any of that audit's unverified programme commentary. Finally (A_v=\widetilde A T_v) gives

\[
|\det A_v|=\sqrt{\det(RR^*)}\sqrt{\det E_v},
\]

so RQT16 is its exact rewritten denominator. On the order-zero domain the second factor is (d_1d_2). At the certified order-two point (E_2=I), and (\mu_2/2=b>0). The finite actual-order bound and the divergent old-domain bound therefore concern the stated different domains, connected by an explicit source map and its exact Gram correction. There is no false inference from the bounded moving quotient to bounded old inverse.

The original audit allows exterior rank zero as well. RQT16's complementary-exterior identity and bound remain valid there: the identity is (1=|\det A_v|/|\det A_v|), and the bound follows from (|\det A_v|\le\|A_v\|^N\le U^N). RQT14's two-angle costs are specifically stated for ranks one through (N), as appropriate. The scalar (D=0) formulas in RQT19 are correct separately and avoid forcing a two-angle count into a one-dimensional section.

## New exact constants and verification limits

The added `REAL_PAIR_ANGLE_CONSTANTS.tex`, RQT20–22, evaluates the limit of (T_0^{-1}=B^{-1}\widetilde A). At a nonresonant direction only the last row of (H_*) contributes. At resonance both final rows contribute, giving the exact leading corner

\[
\Omega=\begin{pmatrix}
eH_{D-1}\rho_{D+1}/\rho_0&(fH_{D-1}+eK_D)\rho_{D+2}/\rho_0\\
0&eH_{D-1}\rho_{D+2}/\rho_1
\end{pmatrix},\qquad e=-b,\quad f=g_3(p_*).
\]

This shows why the original (g_3) and the two extra Gamma weights matter even though only two angles disappear. The full proof handles the finite angular crossover by replacing (K_D) by (K_D+L\kappa_D), and the (0<q<1) paths with exponents (D+2-q,D+q). Its determinant is the reciprocal of the exact angle-product constant. All remaining section singular values are exactly one, as already proved in RQT10.

Independent symbolic checks executed during this review verified the weight-induction difference (1/4), the full symbolic multiplication of the resonant inverse corner by the final two rows of (H_*), and its weighted determinant. An exact rational (3\times2) matrix (Z) with full rank was used to check (M=I-ZWZ^*) and the characteristic polynomial identity giving one unit eigenvalue plus the two eigenvalues of (V^*V). These are finite corroborations; the arguments above prove all dimensions. They are not a second full-series root certificate, and no such rerun is claimed.

One cosmetic issue was reported in the reviewed RQT4 snapshot: the norm exponent contained a literal comma, `^{,2}`. Replacing it by `^2` changes no mathematics. No correction of a mathematical statement in RLA or RQT was required by this review. No shared source, cumulative artifact, frozen edition or publication packet was edited by this derivation; the complete new angle proof and this mathematical review are separate files.
