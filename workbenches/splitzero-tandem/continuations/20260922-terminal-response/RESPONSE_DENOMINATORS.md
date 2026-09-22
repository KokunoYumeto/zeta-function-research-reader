# The two original response denominators have different evaluated growth rates

Result SZ-20260922-027, root derivation, 22 September 2026. This is a continuation of the sealed 026 edition, which remains unchanged. All norms and adjoints below use the original arithmetic quotient metric. The finite argument determines the two denominator amplification rates separately and bounds the actual response ratios. It retains their complex phases and does not assign the residual marked-current sign.

The two denominators are inner products of the fixed terminal eigenclass with the last two source-polynomial classes. Each amplification compares the product of their squared norms with their squared overlap. A large amplification means a small overlap relative to those norms. Earlier work evaluated the product of the two amplifications; it did not identify which overlap was small. The eigenclass equation now proves that the first carries the exponential cost. This matters because the same denominators occur in the two complex response ratios used to calculate the observed, hidden and mixed arithmetic currents.

## 1. Original objects and exact phase dictionary

Retain the stipulated simple quartet, original admitted period and arithmetic unit, source measure, all invariant columns, and every source-minimum fibre. Write
\[
k\equiv1\pmod4,\quad k\ge17,\quad q=(k+1)^2,\quad q_0=(k-7)^2,
\quad q-1\le N\le2q,
\]
\[
Q_k(y)=\prod_{a,b=0}^k\bigl[y-(2b-k)\gamma+i(2a-k)\delta\bigr],
\quad E=\mathbb C[y]/Q_k,\quad S=k/2+iy,
\]
\[
M[p]=[yp],\qquad \mathscr A=kI/2+iM,\qquad
\omega=k\gamma-ik\delta,\quad d=k\delta>0.
\tag{RD1}
\]
The full metric \(G_N\), onto map \(\Lambda:E\to B\), kernel \(K=\ker\Lambda\), and original minimum section are
\[
Q_{B,N}=(\Lambda G_N^{-1}\Lambda^*)^{-1},\quad
L_N=G_N^{-1}\Lambda^*Q_{B,N},\quad
P=L_N\Lambda,\quad Q=I-P.
\tag{RD2}
\]
Thus \(P,Q\) are the actual complementary \(G_N\)-orthogonal projections. The notation \(Q\) for the projection is distinct from the polynomial \(Q_k\).

Let \(p_n^y\) be the original real monic orthogonal polynomials, with full squared source norms \(\omega_n\), and put
\[
b_n^y=[p_n^y],\quad E_N=\|b_N^y\|_{G_N}^2,\quad
F_N=\|b_{N+1}^y\|_{G_N}^2,
\]
\[
e=b_N^y/\sqrt{E_N},\quad f=b_{N+1}^y/\sqrt{F_N},\quad
\epsilon=\sqrt{E_NF_N}/\omega_N.
\tag{RD3}
\]
These unit vectors only express the already defined NCE20 ratios; no source measure or metric is changed. The original full action has the exact decomposition
\[
M=C+\epsilon f e^{\dagger_{G_N}},\quad C^{\dagger_{G_N}}=C,
\quad \langle e,f\rangle_{G_N}=0,
\quad \|C\|_{G_N}\le c_N:=2(N+1)\sqrt{u_k/\ell_k}.
\tag{RD4}
\]
This is [OCP5–7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/OBSERVED_CURRENT_PLANE.tex#L90) and [RC22–25](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L190) of the complete 026 proofs. Its coefficient proof is worth retaining: multiplication by real \(y\), compressed to the complete attained source section, is selfadjoint; its only omitted polynomial is the leading coefficient times \(p_{N+1}^y\). The leading coefficient is \((b_N^y)^*G_N/\omega_N\). The two outgoing classes have opposite parities in the even source and even relation ideal. This proves RD4, including its rank-one orientation and orthogonality. The bound for \(C\) is the full Gamma multiplication bound transported by the two original source inequalities through degree \(2q+2\).

Let \(x=v_+\) be the original terminal cardinal, so \(Mx=\omega x\). Put
\[
A=\langle e,x\rangle_{G_N},\quad B_f=\langle f,x\rangle_{G_N},
\quad E_x=\|x\|_{G_N}^2,
\quad D_N=|\omega|+c_N.
\tag{RD5}
\]
The subscript on \(B_f\) distinguishes this scalar from the observation space. Inner products are conjugate linear in their first argument.

The physical monic classes are exactly \(b_n^S=i^n b_n^y\), under the pullback \(S=k/2+iy\). Therefore the original NCE1 Gram entries obey
\[
F_{13}^{S}=(-i)^N\sqrt{E_N}\,A,\qquad
F_{23}^{S}=(-i)^{N+1}\sqrt{F_N}\,B_f.
\tag{RD6}
\]
This is the complete diagonal unit-phase change between the two boundary rows. It gives the actual current coefficient and the original NCE20 amplifications:
\[
\mathfrak c=\frac{\overline{F_{13}^{S}}F_{23}^{S}}{\omega_NE_x}
=-i\epsilon\frac{\overline A B_f}{E_x},\qquad
\alpha_{\rm resp}=\frac{E_x}{|A|^2},\quad
\beta_{\rm resp}=\frac{E_x}{|B_f|^2}.
\tag{RD7}
\]
Equations RD6–7 prove the typed correspondence to the earlier three-column calculation, including its imaginary phase. That calculation is retained at [NCE1–21, especially NCE9 and NCE20–21](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L109583).

## 2. Separate finite bounds for both denominators

The eigenclass equation and RD4 give
\[
\epsilon f A=(\omega I-C)x,\qquad
\epsilon|A|\le D_N\sqrt{E_x}.
\tag{RD8}
\]
Taking the inner product with \(x\) in RD4, the \(C\)-term is real. Since \(\Im\omega=-d\),
\[
\epsilon\Im(\overline{B_f}A)=-dE_x,
\qquad
\Re\mathfrak c=d,
\qquad
\epsilon|A B_f|\ge dE_x.
\tag{RD9}
\]
In particular both denominators are nonzero for every original cutoff, independently of a nonvanishing period minor. Since \(|A|,|B_f|\le\sqrt{E_x}\), RD8–9 prove the complete finite bounds
\[
\boxed{
\max\{1,\epsilon^2/D_N^2\}\le\alpha_{\rm resp}
\le\epsilon^2/d^2,
\qquad
1\le\beta_{\rm resp}\le D_N^2/d^2.
}
\tag{RD10}
\]
For the last inequality, use RD8 in RD9 to obtain
\(|B_f|\ge d\sqrt{E_x}/D_N\). For the upper bound on \(\alpha_{\rm resp}\), use \(|B_f|\le\sqrt{E_x}\) in RD9. No estimate of a determinant has been substituted for an individual column. The exact product remains
\[
\alpha_{\rm resp}\beta_{\rm resp}
=\epsilon^2/|\mathfrak c|^2,
\tag{RD11}
\]
as in NCE21, but RD10 now evaluates which factor carries the exponential scale.

Retain the literal source-comparison constants through degree \(2q+2\). FW7 and RC22 give
\(\log(u_k/\ell_k)=O_h(k+\log q)\). The full monic-profile estimate and RC25 give
\[
\log\epsilon=q\psi(t_N)+O_{h,\varpi}(k\log q),
\qquad t_N=(N+1-q)/q.
\tag{RD12}
\]
Because \(d=k\delta\), \(|\omega|=k\sqrt{\delta^2+\gamma^2}\), and \(N\le2q\),
\[
0\le\log(D_N/d)=O_h(k+\log q).
\tag{RD13}
\]
Indeed \(u_k/\ell_k\ge1\), and each summand of \(D_N/d\) is bounded by an original fixed constant times \(q\sqrt{u_k/\ell_k}/k\). Its logarithm has the claimed bound. Combining RD10–13 proves
\[
\boxed{
\log\alpha_{\rm resp}=2q\psi(t_N)+O_{h,\varpi}(k\log q),
\qquad
0\le\log\beta_{\rm resp}=O_h(k+\log q).
}
\tag{RD14}
\]
The conclusion is uniform on the complete original cutoff window. It is an evaluation of the separate leading rates; it does not declare \(\beta_{\rm resp}\) constant or determine its smaller terms.

The four original cutoffs have \(t_N=0,1/q,1,1+1/q\) and signs \(+,+,-,-\). The retained profile satisfies \(\psi(t)-\psi(0)=O(t|\log t|)\) at zero and has a bounded derivative near one. Thus RD14 gives
\[
\boxed{
\mathcal R\log\alpha_{\rm resp}
=4[\psi(0)-\psi(1)]q+O_{h,\varpi}(k\log q)
=2C_\partial q+O_{h,\varpi}(k\log q),
}
\]
\[
\mathcal R\log\beta_{\rm resp}=O_h(k+\log q).
\tag{RD15}
\]
Here \(C_\partial=2[\psi(0)-\psi(1)]\) is the exact previously evaluated coefficient. The endpoint estimates follow directly from RC1–10: \(t=z+O(z^2)\), while the only unbounded derivative at zero is the displayed \(\log z\) term. The smooth elliptic parameter at \(t=1\) lies strictly below one. Hence no omitted endpoint is absorbed without a bound.

## 3. The actual responses also have finite bounds

Keep the actual kernel projector \(Q\), and define its three original energies
\[
\alpha_K=\|Qe\|^2,\qquad \beta_K=\|Qf\|^2,
\qquad \theta_K=\|Qx\|^2/E_x.
\tag{RD16}
\]
All lie in \([0,1]\). These quantities do not replace any kernel columns. The unchanged physical response ratios are
\[
U=\frac{\langle e,Qx\rangle}{A},\qquad
V=\frac{\langle f,Qx\rangle}{B_f}.
\tag{RD17}
\]
The same unit phase in numerator and denominator cancels by RD6, proving that RD17 is exactly NCE14. Orthogonality of \(Q\) and Cauchy–Schwarz give
\[
|\langle e,Qx\rangle|^2\le\alpha_K\theta_KE_x,
\qquad
|\langle f,Qx\rangle|^2\le\beta_K\theta_KE_x.
\]
Therefore RD10 gives
\[
\boxed{
|U|\le\frac{\epsilon\sqrt{\alpha_K\theta_K}}d,
\qquad
|V|\le\frac{D_N\sqrt{\beta_K\theta_K}}d.
}
\tag{RD18}
\]
Every original cross term remains in these ratios. The sharper RC25 bound
\(\epsilon\sqrt{\alpha_K}\le\exp[O_{h,\varpi}(k\log q)]\)
and RD13 now imply
\[
\log(1+|U|)=O_{h,\varpi}(k\log q),\qquad
\log(1+|V|)=O_h(k+\log q).
\tag{RD19}
\]
Consequently each of the exact NCE15 products
\[
P_K=\overline U V,\quad P_B=(1-\overline U)(1-V),\quad
P_\times=\overline U+V-2\overline U V
\tag{RD20}
\]
has \(\log(1+|P_X|)=O_{h,\varpi}(k\log q)\). This follows by the triangle inequality and RD19, without removing any of the three terms. Their exact currents remain
\[
\Phi_X/(2E_x)=\Re(\mathfrak c P_X),\qquad
P_K+P_B+P_\times=1.
\tag{RD21}
\]
The full source sign \(\Re\mathfrak c=d>0\) is retained. The complex factors in RD20 still determine the separate signs. In particular, RD19 is not an arithmetic-scale error estimate: a subexponential factor can still amplify an error of polynomial size. The next signed calculation must retain the actual products, rather than discarding them because their exponential rate is zero.

## 4. Receivers and provenance

RD10 and RD14 strengthen the formerly product-only statement NCE21. RD18–21 carry those individual bounds into the same original EC37–41/NCE14–17 responses. They hold for the stipulated source eigenclass without the additional large-period corner guard used for RC40–44. Any later division by the observed norm retains that guard or another proved norm estimate.

The complete preceding programme proofs are NCE1–21 at the pinned link above; [OCP1–14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/OBSERVED_CURRENT_PLANE.tex#L36) and [RC22–27](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L190) in the sealed 026 edition; and the full source inequality [FW7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L120040). The new argument RD8–21 is given in full here. Human inputs to the retained source and monic estimates are R. A. Askey and R. Roy, [DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6); T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt, [DLMF 18.22.8](https://dlmf.nist.gov/18.22.E8) and [18.23.7](https://dlmf.nist.gov/18.23.E7); and B. C. Carlson for the [elliptic series](https://dlmf.nist.gov/19.5.E1). Their original equation sources and actual prior reading records remain in the preceding source bank; they are not claimed as authors of the programme-specific denominator estimates.
