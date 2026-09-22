# Canonical mixed cubic probes recover the original support and signed current

22 September 2026. The node deformation supplies the complete family \(T_g\) whose square is the original rank-one arithmetic primitive. We calculate its finite averages after the original observation, including every hidden return. Keeping the two original support blocks in their order recovers the exact signed current with a uniformly bounded factor. Averaging positive second moments also recovers the actual measured support.

## 1. Original metrics, support blocks, and finite family

At every original cutoff \(q-1\le N\le2q\), retain the full quotient \((E,G_N)\), \(q=(k+1)^2\), \(k\equiv1\pmod4\), \(k\ge17\), original quartet, period, branch and arithmetic unit. The exact action, from OCP5–7, is
\[
M=C+R,\quad C=C^\dagger,\quad R=\epsilon f e^\dagger,\quad
\epsilon>0,\quad \|e\|=\|f\|=1,\quad e^\dagger f=0.
\tag{MP1}
\]
Every source adjoint in this proof is the \(G_N\)-adjoint. The original onto map \(\Lambda:E\to B\), its complete quotient metric and minimum section give
\[
Q_B=(\Lambda G_N^{-1}\Lambda^*)^{-1},\quad
L=G_N^{-1}\Lambda^*Q_B,\quad
J=LQ_B^{-1/2},\quad J^\dagger J=I_B,\quad P=JJ^\dagger=L\Lambda .
\tag{MP2}
\]
Thus \(P\) is the actual orthogonal observation projection and \(I-P\) projects onto the full original invariant kernel. The operator \(\Phi(F)=J^\dagger FJ\) is written in the isometric coordinates of the original \(Q_B\) metric. Its complete product defect is
\[
\Phi(FG)-\Phi(F)\Phi(G)=J^\dagger F(I-P)GJ.
\tag{MP3}
\]
This follows by inserting \(JJ^\dagger=P\); it does not assume that \(\Phi\) preserves products.

Let
\[
\Pi=ee^\dagger+ff^\dagger,\quad P_H=I-\Pi,\quad
H=\{e,f\}^{\perp_{G_N}},\quad d_H=\dim H=q-2.
\]
The original support and observed source columns are
\[
u=J^\dagger e,\quad v=J^\dagger f,\quad
A=J^\dagger\Pi J=uu^*+vv^*,\quad
a=u^*u,\quad \beta=v^*v,\quad r=u^*v,\quad
R_B=\Phi(R)=\epsilon vu^*.
\tag{MP4}
\]
Keep \(A\), a positive contraction, with its actual nonidempotence. Define
\[
Z=\frac{J^\dagger P_HJ}{d_H}=\frac{I_B-A}{d_H},\qquad
s=\operatorname{tr}Z
=\frac{\dim B-a-\beta}{d_H}
=1-\frac{\operatorname{tr}(P_H(I-P))}{d_H}.
\tag{MP5}
\]
All traces are the metric traces of the stated finite spaces. In particular \(0\preceq Z\preceq I_B/d_H\) and \(0\le s\le1\).

Take any complete orthonormal basis \(g_1,\ldots,g_{d_H}\) of the actual space \(H\). The finite averaging operation used below is
\[
\mathbb E F(g)=\frac1{4d_H}\sum_{j=1}^{d_H}\sum_{\lambda\in\{1,i,-1,-i\}}F(\lambda g_j).
\tag{MP6}
\]
There is no distinguished basis vector or omitted direction. We prove that each displayed average is independent of the chosen orthonormal basis. The family is a finite exact realization of the required second moments, not a stochastic approximation.

For each unit \(g\in H\), define the original mixed cubic operator and its two ordered support blocks:
\[
T_g=\sqrt\epsilon(fg^\dagger+ge^\dagger),\quad
X_g=\Pi T_gP_H=\sqrt\epsilon fg^\dagger,\quad
Y_g=P_HT_g\Pi=\sqrt\epsilon ge^\dagger.
\tag{MP7}
\]
Orthogonality gives
\[
X_gY_g=R,\quad Y_gX_g=0,\quad
X_g^2=Y_g^2=0,\quad T_g^2=R,\quad T_g^3=0.
\tag{MP8}
\]
These are exactly the mixed support maps supplied by NI9–13/SO9. The order of \(X_g,Y_g\) matters before and after observation.

## 2. All quadratic averages, with phases and hidden terms retained

Put \(w_g=J^\dagger g\), so
\[
T_{B,g}=\Phi(T_g)=\sqrt\epsilon(vw_g^*+w_gu^*),\quad
X_{B,g}=\sqrt\epsilon vw_g^*,\quad Y_{B,g}=\sqrt\epsilon w_gu^*.
\tag{MP9}
\]
For \(g=\lambda g_j\), \(w_g=\lambda w_j\); hence
\[
\mathbb E(w_gw_g^*)=Z,\qquad
\mathbb E\|w_g\|^2=s,\qquad
\frac14\sum_\lambda\lambda^2
=\frac14\sum_\lambda\bar\lambda^2=0.
\tag{MP10}
\]
The first equality uses \(\sum_j g_jg_j^\dagger=P_H\). This proves basis independence, since the final expression depends only on the original projection \(P_H\).

Multiplying MP9, the terms with phase \(\lambda^{\pm2}\) cancel, and the remaining exact averages are
\[
\boxed{\mathbb E\,T_{B,g}^2=sR_B+\epsilon rZ,}
\tag{MP11}
\]
\[
\boxed{\mathbb E(T_{B,g}^*T_{B,g})
=\epsilon(\beta Z+suu^*),\qquad
\mathbb E(T_{B,g}T_{B,g}^*)
=\epsilon(aZ+svv^*).}
\tag{MP12}
\]
For example, the four terms in \(T_{B,\lambda g_j}^2/\epsilon\) are
\[
\bar\lambda^2v(w_j^*v)w_j^*
+\|w_j\|^2vu^*+r\,w_jw_j^*
+\lambda^2w_j(u^*w_j)u^*.
\]
This verifies that the coefficient of \(Z\) in MP11 is \(r=u^*v\), not its conjugate. The adjoint square average is therefore
\(\mathbb E(T_{B,g}^*)^2=sR_B^*+\epsilon\bar r Z\).
The same multiplication gives MP12: its omitted cross terms carry exactly \(\lambda^{\pm2}\).

On the full source, without observation,
\[
T_g^\dagger T_g=\epsilon(gg^\dagger+ee^\dagger),\qquad
T_gT_g^\dagger=\epsilon(ff^\dagger+gg^\dagger).
\]
Using MP3 and MP10–12 gives the complete hidden returns
\[
\boxed{\mathbb E\,J^\dagger T_g(I-P)T_gJ
=(1-s)R_B-\epsilon rZ,}
\tag{MP13}
\]
\[
\boxed{\begin{aligned}
\mathbb E\,J^\dagger T_g^\dagger(I-P)T_gJ
&=\epsilon[(1-\beta)Z+(1-s)uu^*],\\
\mathbb E\,J^\dagger T_g(I-P)T_g^\dagger J
&=\epsilon[(1-a)Z+(1-s)vv^*].
\end{aligned}}
\tag{MP14}
\]
Both expressions in MP14 are positive semidefinite, as are their unaveraged complete squares. The adjoint of MP13 is the corresponding adjoint-square hidden return. The full original kernel appears in every \(I-P\); no conductor-only kernel has been substituted.

The ordered products require no phase averaging at all: each pair of phases cancels within the product. The complete basis average, equivalently MP6, gives
\[
\boxed{\mathbb E(X_{B,g}Y_{B,g})=sR_B,\qquad
\mathbb E(Y_{B,g}X_{B,g})=\epsilon rZ.}
\tag{MP15}
\]
Indeed \(X_{B,g}Y_{B,g}=\|w_g\|^2R_B\), whereas
\(Y_{B,g}X_{B,g}=\epsilon r w_gw_g^*\).
The corresponding exact hidden products are
\[
\boxed{\mathbb E\,J^\dagger X_g(I-P)Y_gJ=(1-s)R_B,\qquad
\mathbb E\,J^\dagger Y_g(I-P)X_gJ=-\epsilon rZ.}
\tag{MP16}
\]
Thus the reverse product, which is zero on the source, is exactly cancelled by its actual hidden return after observation.

The four positive ordered hidden returns are likewise
\[
\begin{aligned}
\mathbb E J^\dagger X_g^\dagger(I-P)X_gJ&=\epsilon(1-\beta)Z,\\
\mathbb E J^\dagger Y_g^\dagger(I-P)Y_gJ&=\epsilon(1-s)uu^*,\\
\mathbb E J^\dagger X_g(I-P)X_g^\dagger J&=\epsilon(1-s)vv^*,\\
\mathbb E J^\dagger Y_g(I-P)Y_g^\dagger J&=\epsilon(1-a)Z .
\end{aligned}
\tag{MP17}
\]
This is proved either by direct substitution of MP7 or by subtracting the respective observed positive product from its complete source product. Adding the first two and last two gives exactly MP14.

## 3. Exact isolation of the original signed current

The original centered arithmetic current is
\[
W_B=J^\dagger i(M-M^\dagger)J=i(R_B-R_B^*),
\qquad \operatorname{tr}W_B=-2\epsilon\Im r.
\tag{MP18}
\]
For every original observed vector \(b\), its physical current is the quadratic form of \(W_B\) on \(Q_B^{1/2}b\); the central scalar \(kI/2\) is removed by the same centered-current definition in OCP8. It has not been inserted or changed here.

The Hermitian ordered mixed probe is
\[
\mathcal C_{\rm ord}
=i\,\mathbb E(X_{B,g}Y_{B,g}-Y_{B,g}^*X_{B,g}^*)
=sW_B.
\tag{MP19}
\]
When \(s>0\), this recovers the entire original current, including every marked-class pairing:
\[
\boxed{W_B=s^{-1}\mathcal C_{\rm ord}.}
\tag{MP20}
\]
For every Hermitian perturbation \(E\), this inverse has exactly the operator-norm error
\(\|s^{-1}E\|=\|E\|/s\). Thus its amplification is exactly \(1/s\); it is not an unspecified conditioning factor. For a particular observed vector \(\widehat b\), its current is exactly
\(\widehat b^*\mathcal C_{\rm ord}\widehat b/s\). This identifies the actual probe whose numerical or analytic value would evaluate the residual sign, without assigning that unknown value.

The unordered square average also has an exact current receiver. Put
\[
\mathcal C_{\rm sq}
=i\,\mathbb E[T_{B,g}^2-(T_{B,g}^*)^2].
\]
Then MP11 gives
\[
\mathcal C_{\rm sq}=sW_B+(\operatorname{tr}W_B)Z,\qquad
\operatorname{tr}\mathcal C_{\rm sq}=2s\operatorname{tr}W_B,
\]
\[
\boxed{W_B=\frac{\mathcal C_{\rm sq}}s
-\frac{\operatorname{tr}\mathcal C_{\rm sq}}{2s^2}Z.}
\tag{MP21}
\]
The averaged hidden signed return is
\((1-s)W_B-(\operatorname{tr}W_B)Z\); adding it to the observed expression gives the complete \(W_B\), with no remaining trace term.

For \(n=\dim B\ge2\), the exact induced operator norm of the Hermitian inverse map in MP21 is
\[
\boxed{\left\|E\longmapsto \frac Es-\frac{\operatorname{tr}E}{2s^2}Z\right\|
_{\mathrm{Herm,op}\to\mathrm{Herm,op}}
=\frac1s+\frac{(n-2)\|Z\|}{2s^2}
\le\frac3{2s}.}
\tag{MP22}
\]
To prove this, fix a unit vector \(b\), set \(\zeta=b^*Zb\), and pair the output with \(b\). The resulting real linear functional on Hermitian \(E\) is trace pairing with
\[
F_b=s^{-1}bb^*-\frac{\zeta}{2s^2}I_B.
\]
Since \(0\le\zeta\le\operatorname{tr}Z=s\), its eigenvalue on \(b\) is positive and its other \(n-1\) eigenvalues are nonpositive. Its trace norm is exactly
\(1/s+(n-2)\zeta/(2s^2)\).
The supremum over \(\|E\|\le1\) is that trace norm, attained by the Hermitian sign of \(F_b\). Taking \(b\) in the top eigenspace of \(Z\) proves equality in MP22. Finally \(\|Z\|\le1/d_H\) and
\(s=(n-\operatorname{tr}A)/d_H\ge(n-2)/d_H\), since \(\operatorname{tr}A\le2\). These give its final upper bound. All signs and trace corrections in this inverse are therefore quantitatively controlled.

## 4. The original rank theorem makes the recovery factor uniformly bounded

The original simple-quartet five-orbit observation has the proved bound
\[
n=\operatorname{rank}\Lambda\ge
r_k^-:=\left\lfloor\frac{(k+1)^2}{5}\right\rfloor+\mathbf1_{5\mid k}.
\tag{MP23}
\]
Here the observation, period-dependent transformed quadric and rank are exactly those of the source OCS25–32. The relevant finite argument is reproduced to identify what is being used.

In the source's exact four Fourier coordinates, with weights \(1,2,3,4\) modulo five, let \(\mathcal R_k\) be the degree-\(k\) polynomial space and \(\mathcal I_k\) its weight-zero span. The original transformed quadric is the nonzero
\(Q(x)=Q_0(\mathsf H^{-1}x)\), where
\(Q_0=t_{++}t_{--}-t_{+-}t_{-+}\) and \(\mathsf H\) is the actual invertible period-and-unit matrix. Homogeneous restriction to the original exponential curve has kernel exactly \(Q\mathcal R_{k-2}\). The proof groups monomials by their two counts \((a,b)\): their \(q=(k+1)^2\) exponents are distinct because \(\delta,\gamma>0\), so their exponential functions are independent by the Vandermonde determinant. Within a fixed pair, monomial differences are divisible by \(Q_0\) using \(A^j-B^j=(A-B)\sum_{\ell=0}^{j-1}A^{j-1-\ell}B^\ell\). Transforming by the same \(\mathsf H\) proves the stated kernel. Thus
\[
n=\dim\mathcal I_k-\dim(\mathcal I_k\cap Q\mathcal R_{k-2}).
\]
Fix a multiplicative monomial order and the actual leading monomial \(x^\mu\) of \(Q\). A row-echelon basis of the intersection has distinct weight-zero leading monomials, each divisible by \(x^\mu\). Its dimension is at most the number of degree-\(k-2\) monomials of weight \(-\operatorname{wt}\mu\). This retains the actual quadric rather than choosing generic coefficients.

For an explicit count, let \(D_j=\binom{j+3}{3}\) and
\(\varepsilon_j=1\) for \(j\equiv0\bmod5\), \(-1\) for \(j\equiv1\bmod5\), and zero otherwise. The root-of-unity filter gives
\[
d_{5,j,0}=(D_j+4\varepsilon_j)/5,\qquad
d_{5,j,r}=(D_j-\varepsilon_j)/5\quad(r\ne0).
\]
Indeed for every nontrivial fifth root \(\zeta^\ell\),
\(\prod_{a=1}^4(1-\zeta^{\ell a}z)^{-1}=(1-z)/(1-z^5)\); its degree-\(j\) coefficient is exactly \(\varepsilon_j\). Substituting in the leading-monomial bound gives
\(n\ge d_{5,k,0}-\max_r d_{5,k-2,r}\).
Since \(D_k-D_{k-2}=(k+1)^2\), the five residues of \(k\bmod5\) give precisely MP23. This reproduces the finite count in the cited original map, without a genericity assumption.

Combining MP5 and MP23 gives, at every original cutoff,
\[
\boxed{s\ge
\frac{\lfloor q/5\rfloor+\mathbf1_{5\mid k}-2}{q-2}>0,\qquad
\frac1s\le
\frac{q-2}{\lfloor q/5\rfloor+\mathbf1_{5\mid k}-2}
\le\frac{1610}{309}<6.}
\tag{MP24}
\]
For the last uniform bound use \(q\ge324\) and
\(\lfloor q/5\rfloor-2\ge q/5-3\). The function
\(5(q-2)/(q-15)\) decreases for \(q>15\), and its value at \(324\) is \(1610/309\). Thus the ordered current recovery is uniformly bounded; the unordered inverse MP22 is at most \(805/103<9\).

The exact obstruction to these receivers is also specified: \(s=0\) if and only if \(P_HJ=0\), equivalently \(\operatorname{im}J\subseteq\operatorname{span}\{e,f\}\). This follows from
\(d_Hs=\|P_HJ\|_{\rm HS}^2\).
In that case every \(w_g\), and hence every observed mixed cubic probe, vanishes; the current in the supported two-plane can still be nonzero. The proved original rank bound excludes precisely this obstruction, because \(n\ge64>2\).

## 5. Positive mixed probes recover the actual measured support

Let \(t=\operatorname{tr}A=a+\beta\) and
\[
\mathcal P_2=\mathbb E(T_{B,g}^*T_{B,g}+T_{B,g}T_{B,g}^*).
\]
The two positive moments in MP12 give the exact polynomial receiver
\[
\boxed{\mathcal P_2=\frac\epsilon{d_H}
\bigl[tI_B+(n-2t)A\bigr],\qquad
\operatorname{tr}\mathcal P_2=\frac{2\epsilon}{d_H}t(n-t).}
\tag{MP25}
\]
To verify it, add MP12 to obtain
\(\epsilon(tZ+sA)\), then substitute \(Z=(I-A)/d_H\) and \(s=(n-t)/d_H\).
Here \(0\le t\le2\), whereas the original \(n\ge64\), so \(n-2t>0\). Consequently
\[
\boxed{t=\frac{n-\sqrt{n^2-2d_H\operatorname{tr}\mathcal P_2/\epsilon}}2,\qquad
A=\frac{d_H\mathcal P_2/\epsilon-tI_B}{n-2t}.}
\tag{MP26}
\]
The displayed square-root branch is forced by \(0\le t\le2<n/2\); the other quadratic root is outside this interval. These are recoveries of \(A\), not replacements of it by an idempotent. Its full original defect is still
\[
A-A^2=J^\dagger\Pi(I-P)\Pi J,
\]
whose spectrum and terminal-class consequences are calculated by the companion support proof.

There is a finite stability bound on this exact positive-data image. Write
\(\mathcal D=(d_H/\epsilon)\mathcal P_2=tI+(n-2t)A\).
For any two actual admissible support contractions \(A_0,A_1\) of rank at most two, set \(\eta=\|\mathcal D_1-\mathcal D_0\|\). Their traces give
\[
|t_1-t_0|
\le\frac{n\eta}{2(n-4)},\qquad
\boxed{\|A_1-A_0\|\le
\frac{\eta}{n-4}\left(1+\frac n{2(n-4)}\right).}
\tag{MP27}
\]
Indeed the trace difference is \(2(n-t_1-t_0)(t_1-t_0)\), and its modulus is at most \(n\eta\). Also
\[
(n-2t_1)(A_1-A_0)
=\mathcal D_1-\mathcal D_0-(t_1-t_0)(I-2A_0).
\]
Since \(0\preceq A_0\preceq I\), \(\|I-2A_0\|\le1\); both denominators are at least \(n-4>0\). This proves MP27. The estimate describes the inverse on its actual spectral image and does not assign an admissible support to arbitrary corrupted data.

## 6. Exact programme consequence and retained signed target

Equations MP19–24 show that the complete finite mixed family computes the original signed-current operator with a bounded loss. For every prescribed original terminal vector \(x\), put \(b=Q_B^{1/2}\Lambda x\). The same finite average gives
\[
\boxed{\Phi_N(\Lambda x)=
\frac{i}{s}\,\mathbb E\left[
b^*X_{B,g}Y_{B,g}b-b^*Y_{B,g}^*X_{B,g}^*b\right].}
\tag{MP28}
\]
The identity holds before any asymptotic expansion and at all four original cutoffs separately. It preserves the complete source minimum and every hidden return. The bounded factor does not evaluate an unevaluated complex product: the residual arithmetic sign still requires the value of the ordered quadratic average on the actual terminal vector. In particular relative errors measured against the large scale \(\epsilon\) need not be small on the terminal current's smaller scale. MP20 quantifies the inverse error in absolute operator norm, so that distinction is explicit.

The node data have therefore supplied canonical finite probes for the actual original support and current, rather than an arbitrary distinguished square root. The averaged reverse product and every complementary return are part of the exact calculation.

## Sources and proof locators

- Original source action and its complete minimum: [OCP5–7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/OBSERVED_CURRENT_PLANE.tex#L90).
- Actual metric isometry and product receiver: [CE2–3](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/EVOLUTION_PROOF.md#L18), with the full hidden rank-one return at [CE24–26](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/EVOLUTION_PROOF.md#L255).
- Actual period quadric and five-orbit rank: [OCS28–32](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L10987), with [OCS31–32](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L11073).
- Complete original node representation and mixed cubic family: [NI8–13 in NATIVE_DUAL_NUMBER_RECEIVER.md, pinned node edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6af54ea3c8ef99127af327f3103e086c68d482c2/workbenches/splitzero-tandem/branches/identity-absorber-square/NATIVE_DUAL_NUMBER_RECEIVER.md). The same edition retains the full support-algebra continuation NI17–29 and its [ID1–24 idempotent-deformation companion](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6af54ea3c8ef99127af327f3103e086c68d482c2/workbenches/splitzero-tandem/branches/identity-absorber-square/IDEMPOTENT_DEFORMATION.md). The mixed block formulas used here are explicitly rederived in MP7–8 and MP15–17.

The finite matrix, trace and root-of-unity calculations used here are proved in full. No additional external theorem is used. Human provenance for the inherited original-source construction remains in the cited complete programme proofs, including the DLMF Gamma and orthogonal-polynomial authors; these new finite averages do not alter those source attributions.
