# The original-zeta resolvent, global projectors, and every multiplicity jet

Independent mathematical derivation, 24 September 2026. Proof locators RZ1–RZ12.

This note works on the entire quotient already constructed in GLOBAL_MELLIN_SYNTHESIS.md, S1–S7, and GLOBAL_CANONICAL_MELLIN_INVOLUTION.md, G1–G5. Those portions were read for this derivation. S5 supplies the equality between the closed original source image and the ideal of all actual nontrivial-zero jets. That synthesis theorem is an input here, not a result reproved or attributed to this note. The source Fourier, Mellin, dilation and reflection conventions are retained exactly.

Every zero below is a zero of the original Riemann zeta function with its actual multiplicity. No simplicity, critical-line location, positivity or RH assumption is made. All operations are on the named function spaces and their quotient; they put no addition, coordinate or metric on the user's supporting datum.

## RZ1. Spaces, full multiplier, and the operator domain

Let
\[
\mathcal A=\left\{k\in C^\infty(\mathbb R_{>0}):
p_{N,j}(k):=\sup_{u>0}(u^N+u^{-N})
|(u\partial_u)^jk(u)|<\infty\quad(N,j\geq0)\right\},
\tag{RZ1.1}
\]
and let \(\mathcal B\) be the entire functions with every seminorm
\[
b_{A,M}(F)=
\sup_{|\operatorname{Re}s|\leq A}
(1+|\operatorname{Im}s|)^M|F(s)|<\infty.
\tag{RZ1.2}
\]
Integer nonnegative \(A,M,N,j\) suffice. The exact topological isomorphism from S1 is
\[
\mathcal Mk(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u}.
\tag{RZ1.3}
\]

Write \(\mathscr Z\) for the set of distinct original nontrivial zeros, and \(m_\rho\) for the full positive multiplicity of \(\rho\in\mathscr Z\). Define the closed ideal
\[
\mathcal I=\{F\in\mathcal B:
F^{(j)}(\rho)=0\quad
(\rho\in\mathscr Z,\ 0\leq j<m_\rho)\},
\qquad \mathcal Q=\mathcal B/\mathcal I.
\tag{RZ1.4}
\]
The source quotient \(\mathcal A/\overline{\mathcal E(\mathcal S_0^{\mathrm{even}})}\) is identified with this quotient by the already proved S5. A bracket \([F]\) denotes its class. We use the quotient Fréchet topology, not an unspecified product topology on jets.

The exact retained element of \(\mathcal I\) is
\[
F_0(s)=\mathcal Mk_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\tag{RZ1.5}
\]
where
\[
k_0(u)=u^{1/2}\sum_{n\geq1}f_0(nu),\qquad
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2}.
\tag{RZ1.6}
\]
The whole product (RZ1.5) has its entire continuation. Its zeros and their orders are exactly \((\rho,m_\rho)\). Its exceptional values are
\[
F_0(0)=F_0(1)=\frac18,
\tag{RZ1.7}
\]
and, for every positive integer \(r\),
\[
\begin{aligned}
F_0(-2r)
&=\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\,\zeta'(-2r)\\
&=F_0(1+2r)\\
&=\frac{(1+2r)(2r)}8
\pi^{-(1+2r)/2}\Gamma((1+2r)/2)\zeta(1+2r)\ne0 .
\end{aligned}
\tag{RZ1.8}
\]
These are the original endpoint, Gamma-pole and trivial-zero cancellations, with their resulting values retained. They are inputs established in S2 and G4; the function \(\zeta\) is not replaced by another function in the arithmetic argument.

Define on all of \(\mathcal B\)
\[
\mathsf L F(s)=sF(s).
\tag{RZ1.9}
\]
For all \(A,M\),
\[
b_{A,M}(\mathsf LF)\leq(A+1)b_{A,M+1}(F).
\tag{RZ1.10}
\]
Multiplication by \(s\) preserves every required zero order, so \(\mathsf L\mathcal I\subseteq\mathcal I\). It therefore induces a continuous operator \(L\) on all of \(\mathcal Q\); its domain is the entire quotient.

On \(\mathcal A\), the exact corresponding operator is
\[
\mathsf D=\frac12-u\partial_u.
\tag{RZ1.11}
\]
Indeed integration by parts, whose two boundary terms vanish by (RZ1.1), gives
\[
\mathcal M(u\partial_u k)(s)=-(s-\tfrac12)\mathcal Mk(s),
\qquad
\mathcal M(\mathsf Dk)(s)=s\mathcal Mk(s).
\tag{RZ1.12}
\]
Moreover
\[
p_{N,j}(\mathsf Dk)
\leq\tfrac12p_{N,j}(k)+p_{N,j+1}(k).
\tag{RZ1.13}
\]
The variable of \(L\) is thus the original \(s\), not \(s-\tfrac12\).

## RZ2. Estimates for evaluation, multiplication and entire division

For a fixed \(z\in\mathbb C\), positive radius \(r\), and \(j\geq0\), the Cauchy integral formula gives
\[
\frac{|F^{(j)}(z)|}{j!}
\leq r^{-j}b_{A,0}(F)
\quad\text{when }A\geq|\operatorname{Re}z|+r.
\tag{RZ2.1}
\]
Consequently every jet functional is continuous and \(\mathcal I\) is closed. It is an ideal because the Leibniz formula preserves a zero of any specified finite order under multiplication by an entire function.

For completeness, the quotient used here is itself complete. The increasing seminorms \(b_{j,j}\), \(j\geq1\), generate the topology of \(\mathcal B\); their quotient seminorms generate that of \(\mathcal Q\). From a Cauchy sequence in the quotient choose a subsequence whose \(j\)-th consecutive difference has quotient seminorm below \(2^{-j}\) for \(b_{j,j}\). Lift that difference to \(H_j\in\mathcal B\) with \(b_{j,j}(H_j)<2^{1-j}\). The series \(\sum_jH_j\) converges in every fixed seminorm: after its index exceeds that seminorm's indices, the displayed geometric bound controls the tail. Completeness of \(\mathcal B\) therefore gives a limit of the lifted partial sums. Its quotient class is the limit of the selected subsequence and hence of the original Cauchy sequence. Closedness of \(\mathcal I\) makes the quotient Hausdorff. This proves the stated complete Fréchet domain.

For \(F,G\in\mathcal B\), and a nonnegative integer \(r\),
\[
b_{A,M}(FG)\leq b_{A,0}(F)b_{A,M}(G),
\tag{RZ2.2}
\]
\[
b_{A,M}((s-z)^rF)
\leq(A+|z|+1)^r b_{A,M+r}(F).
\tag{RZ2.3}
\]
Thus multiplication by a fixed member of \(\mathcal B\), and by every fixed polynomial, is continuous on \(\mathcal B\).

We need entire division, including its local estimate. Suppose that \(H\in\mathcal B\) vanishes at \(z\) to order at least \(r\geq1\). Then
\[
D_{z,r}H(s)=\frac{H(s)}{(s-z)^r}
\tag{RZ2.4}
\]
extends to an entire member of \(\mathcal B\), continuously on the closed subspace with that vanishing condition. Outside \(|s-z|<1\), its weighted absolute value is at most that of \(H\). Inside \(|s-z|\leq1\), the holomorphic quotient and the maximum principle on \(|s-z|\leq2\) give
\[
|D_{z,r}H(s)|
\leq 2^{-r}\sup_{|w-z|=2}|H(w)|.
\tag{RZ2.5}
\]
The weight in that smaller disk is at most \((2+|\operatorname{Im}z|)^M\). Taking any integer \(A'\geq\max(A,|\operatorname{Re}z|+2)\) proves, for example,
\[
b_{A,M}(D_{z,r}H)
\leq b_{A,M}(H)
+2^{-r}(2+|\operatorname{Im}z|)^M b_{A',0}(H).
\tag{RZ2.6}
\]
The same estimate is uniform as \(z\) ranges over a fixed compact set. The quotient at \(s=z\) is the corresponding Taylor coefficient, so no singular integral is hidden in this assertion.

All further divisions in this note are applications of this estimate or the first-order version with a constructed vanishing numerator.

## RZ3. The continuous global resolvent

For \(\lambda\notin\mathscr Z\), define on all of \(\mathcal B\)
\[
\boxed{\quad
\mathscr R_\lambda F(s)=
\frac{F(s)-F_0(s)\,F(\lambda)/F_0(\lambda)}
{\lambda-s}.
\quad}
\tag{RZ3.1}
\]
The numerator is in \(\mathcal B\), vanishes at \(s=\lambda\), and \(F_0(\lambda)\ne0\). The removable value is exactly
\[
\mathscr R_\lambda F(\lambda)
=-F'(\lambda)+F_0'(\lambda)\frac{F(\lambda)}{F_0(\lambda)}.
\tag{RZ3.2}
\]
The negative sign is caused by the denominator \(\lambda-s\). RZ2 proves that \(\mathscr R_\lambda F\in\mathcal B\).

Here is the needed uniform continuity statement. Let \(K\) be nonempty and compact in \(\mathbb C\setminus\mathscr Z\). Set
\[
c_K=\min_{\lambda\in K}|F_0(\lambda)|>0,\qquad
B_K=\sup_{\lambda\in K}|\operatorname{Re}\lambda|,\qquad
T_K=\sup_{\lambda\in K}|\operatorname{Im}\lambda|.
\]
For each \(A,M\), choose an integer
\(A'\geq\max(A,B_K+2)\).
Evaluation is bounded by \(b_{A',0}(F)\), so the numerator in (RZ3.1) satisfies
\[
b_{A,M}\!\left(F-F_0\frac{F(\lambda)}{F_0(\lambda)}\right)
\leq b_{A,M}(F)+c_K^{-1}b_{A,M}(F_0)b_{A',0}(F).
\tag{RZ3.3}
\]
Write \(G_\lambda=F-F_0F(\lambda)/F_0(\lambda)\) for the numerator. Applying (RZ2.6) once, with the output strip \(A\), gives
\[
b_{A,M}(\mathscr R_\lambda F)
\leq b_{A,M}(G_\lambda)
+\frac12(2+T_K)^M b_{A',0}(G_\lambda).
\]
The second term requires only a bound on the numerator itself, not another division. Directly,
\[
b_{A',0}(G_\lambda)
\leq\left(1+c_K^{-1}b_{A',0}(F_0)\right)b_{A',0}(F).
\]
Combining this with (RZ3.3) gives the explicit finite constant
\[
C_{K,A,M}
=1+c_K^{-1}b_{A,M}(F_0)
+\frac12(2+T_K)^M
\left(1+c_K^{-1}b_{A',0}(F_0)\right)
\]
and proves
\[
\sup_{\lambda\in K}b_{A,M}(\mathscr R_\lambda F)
\leq C_{K,A,M}b_{A',M}(F).
\tag{RZ3.4}
\]
The condition \(A'\geq\max(A,B_K+2)\) already contains every radius-two disk centered at a point of \(K\). Thus the same \(A'\) controls the division disk and both numerator bounds; no further enlargement to \(A'+2\) is needed. Only this stated increase of the strip index has been used.

If \(F\in\mathcal I\), its numerator in (RZ3.1) vanishes to order at least \(m_\rho\) at every \(\rho\). Since \(\lambda-\rho\ne0\), division preserves each such order. Thus
\[
\mathscr R_\lambda\mathcal I\subseteq\mathcal I.
\tag{RZ3.5}
\]
The induced operator \(R_\lambda\) is continuous on \(\mathcal Q\). More explicitly, with quotient seminorms
\[
q_{A,M}([F])=\inf_{H\in\mathcal I}b_{A,M}(F+H),
\]
equation (RZ3.4) gives
\[
\sup_{\lambda\in K}q_{A,M}(R_\lambda[F])
\leq C_{K,A,M}q_{A',M}([F]).
\tag{RZ3.6}
\]
For the supremum, this follows by using the same representative \(F+H\) for every \(\lambda\), then taking the infimum.

The exact identities before taking the quotient are
\[
(\lambda-\mathsf L)\mathscr R_\lambda F
=F-F_0\,\frac{F(\lambda)}{F_0(\lambda)},
\qquad
\mathscr R_\lambda((\lambda-\mathsf L)F)=F.
\tag{RZ3.7}
\]
The correction in the first identity belongs to \(\mathcal I\). Therefore on the actual quotient
\[
\boxed{R_\lambda=(\lambda-L)^{-1}
\quad(\lambda\notin\mathscr Z).}
\tag{RZ3.8}
\]
Although \(F(\lambda)\) by itself generally does not descend to this quotient, the full expression (RZ3.1) does, by (RZ3.5). In fact \(F_0(\lambda)\ne0\) already proves that evaluation at such a \(\lambda\) does not annihilate \(\mathcal I\). The correction term is essential.

For example the endpoint resolvents use exactly
\[
\mathscr R_0F(s)=\frac{F(s)-8F_0(s)F(0)}{-s},
\qquad
\mathscr R_1F(s)=\frac{F(s)-8F_0(s)F(1)}{1-s}.
\tag{RZ3.9}
\]
At \(\lambda=-2r\), (RZ3.1) uses the nonzero value (RZ1.8). Thus \(0,1\) and the original trivial zeros are resolvent points of this specified nontrivial-zero quotient. Their full original multiplier contributions have been evaluated, not dropped.

## RZ4. Parameter holomorphy and the source resolvent

The numerator
\[
F(s)F_0(\lambda)-F_0(s)F(\lambda)
\tag{RZ4.1}
\]
vanishes on the diagonal \(s=\lambda\). Its division by \(\lambda-s\) is holomorphic jointly in the two variables: locally expand both entire functions into power series, or factor each difference by the integral of its derivative along the segment from \(\lambda\) to \(s\). Dividing additionally by \(F_0(\lambda)\) is holomorphic when \(\lambda\notin\mathscr Z\). Hence \(\lambda\mapsto\mathscr R_\lambda F(s)\) is pointwise holomorphic.

Together with (RZ3.4), this is holomorphy in the topology of \(\mathcal B\), and in the topology of uniform convergence on bounded subsets for the operator family. Here are the details needed for that conclusion. On a small closed parameter disk contained in the resolvent set, the family is uniformly bounded in each output seminorm by one input seminorm. Cauchy's formula in \(\lambda\) can therefore be integrated in each seminorm; completeness of \(\mathcal B\) puts the integral in \(\mathcal B\). Pointwise Cauchy equality identifies this integral with the given entire function of \(s\). The Cauchy remainder estimate on a slightly larger disk bounds the difference-quotient remainder in any output seminorm by a constant times \(|h|\) and one input seminorm. Taking the supremum over any bounded input set proves operator holomorphy in that topology. The identical argument, using (RZ3.6), applies to the quotient.

In particular contour integrals of \(R_\lambda\) on compact contours in the resolvent set are well defined continuous operators on the complete Fréchet quotient. The usual resolvent identity follows directly from the two inverse identities:
\[
R_\lambda-R_\mu=(\mu-\lambda)R_\lambda R_\mu.
\tag{RZ4.2}
\]

The full source representative is also explicit. If \(F=\mathcal Mk\), then
\[
\begin{aligned}
(\mathscr r_\lambda k)(u)
&=\frac1{2\pi}\int_{\mathbb R}
\frac{F(\tfrac12+it)-
F_0(\tfrac12+it)F(\lambda)/F_0(\lambda)}
{\lambda-\tfrac12-it}\,u^{-it}\,dt .
\end{aligned}
\tag{RZ4.3}
\]
If the denominator vanishes on this line, the integrand has the removable value (RZ3.2). Its Mellin transform is (RZ3.1).

For precision, every \(H\in\mathcal B\) has inverse
\[
k_H(e^x)=\frac1{2\pi}\int_{\mathbb R}
H(\tfrac12+it)e^{-itx}\,dt .
\tag{RZ4.4}
\]
Take \(c=\tfrac12+N+1\) for \(x\geq0\), and \(c=\tfrac12-N-1\) for \(x\leq0\). The proven strip contour shift gives
\[
\frac{d^j}{dx^j}k_H(e^x)
=\frac{e^{-(c-1/2)x}}{2\pi}
\int_{\mathbb R}[-(c-\tfrac12+it)]^j
H(c+it)e^{-itx}\,dt.
\tag{RZ4.5}
\]
Since \(\int_{\mathbb R}(1+|t|)^{-2}dt=2\), this yields the explicit estimate
\[
\sup_x e^{N|x|}
\left|\frac{d^j}{dx^j}k_H(e^x)\right|
\leq\frac{(N+2)^j}{\pi}b_{N+2,j+2}(H),
\tag{RZ4.6}
\]
and consequently
\[
p_{N,j}(k_H)\leq
\frac{2(N+2)^j}{\pi}b_{N+2,j+2}(H).
\tag{RZ4.7}
\]
The notation \(d^j/dx^j\,k_H(e^x)\) denotes derivatives of the composite function. These estimates prove that (RZ4.3) belongs to \(\mathcal A\), continuously and uniformly on compact resolvent-parameter sets.

The exact source identities are
\[
(\lambda-\mathsf D)\mathscr r_\lambda k
=k-k_0\frac{\mathcal Mk(\lambda)}{F_0(\lambda)},
\qquad
\mathscr r_\lambda((\lambda-\mathsf D)k)=k.
\tag{RZ4.8}
\]
The first correction lies in the original source image because \(k_0=\mathcal Ef_0\). The whole closed source image is preserved by \(\mathscr r_\lambda\), by S5 and (RZ3.5).

## RZ5. Global representatives of every actual zero jet

Fix an actual zero \(\rho\), and write \(m=m_\rho\). Put
\[
A_\rho(s)=\frac{F_0(s)}{(s-\rho)^m}.
\tag{RZ5.1}
\]
It is entire, belongs to \(\mathcal B\) by RZ2, and
\[
a_r:=\frac{A_\rho^{(r)}(\rho)}{r!}
=\frac{F_0^{(m+r)}(\rho)}{(m+r)!},
\qquad a_0\ne0.
\tag{RZ5.2}
\]
Define the coefficients of the reciprocal Taylor polynomial by
\[
b_0=a_0^{-1},\qquad
b_r=-a_0^{-1}\sum_{h=1}^r a_hb_{r-h}
\quad(1\leq r<m),
\tag{RZ5.3}
\]
and set
\[
B_\rho(s)=\sum_{r=0}^{m-1}b_r(s-\rho)^r,\qquad
e_\rho(s)=A_\rho(s)B_\rho(s).
\tag{RZ5.4}
\]
The recursion says exactly
\[
e_\rho(s)=1+O((s-\rho)^m)\quad(s\to\rho).
\tag{RZ5.5}
\]
Every function in (RZ5.4) after multiplication by \(A_\rho\) belongs to \(\mathcal B\), by the polynomial estimate (RZ2.3).

At each other actual zero \(\sigma\ne\rho\), the denominator in (RZ5.1) is nonzero. Hence \(A_\rho\), \(e_\rho\), and \(e_\rho(s)(s-\rho)^j\) vanish there to order at least \(m_\sigma\). This holds at every other zero simultaneously, without a finite interpolation range.

Define, for \(0\leq j<m\),
\[
E_{\rho,j}(s)=e_\rho(s)(s-\rho)^j,\qquad
D_{\rho,j}(s)=\frac1{j!}E_{\rho,j}(s).
\tag{RZ5.6}
\]
The complete exact jet statement is
\[
E_{\rho,j}^{(k)}(\sigma)
=j!\,\mathbf1_{\{\sigma=\rho,\ k=j\}}
\quad(\sigma\in\mathscr Z,\ 0\leq k<m_\sigma),
\tag{RZ5.7}
\]
and \(D_{\rho,j}^{(k)}(\sigma)\) is the same expression without \(j!\). Thus these are global representatives for each individual derivative coordinate, including its factorial.

They have actual prequotient source representatives
\[
k_{\rho,j}(u)=\frac1{2\pi}\int_{\mathbb R}
e_\rho(\tfrac12+it)(\tfrac12+it-\rho)^j u^{-it}\,dt,
\qquad \mathcal Mk_{\rho,j}=E_{\rho,j}.
\tag{RZ5.8}
\]
The estimate (RZ4.7), with \(H=E_{\rho,j}\), proves every source seminorm is finite. In particular these representatives belong to the whole \(\mathcal A\), rather than merely defining distributions or a finite set of prescribed values. They do not belong to the annihilated source image when the indicated jet is nonzero; that would contradict (RZ5.7) and S5.

All multiplier derivatives in the recursion can be retained explicitly in terms of the original zeta. Set only for displaying these derivatives
\[
C(s)=\frac18s(s-1)\pi^{-s/2}\Gamma(s/2).
\tag{RZ5.9}
\]
At the nontrivial zero \(\rho\), \(C\) is holomorphic and nonzero. The exact coefficient formula is
\[
a_r=
\sum_{h=0}^r
\frac{C^{(h)}(\rho)}{h!}\,
\frac{\zeta^{(m+r-h)}(\rho)}{(m+r-h)!}.
\tag{RZ5.10}
\]
No derivative term has been suppressed: derivatives of \(\zeta\) of order less than \(m\) vanish by the definition of its actual multiplicity. For \(P(s)=s(s-1)\),
\[
C^{(h)}(s)
=\frac{\pi^{-s/2}}8
\sum_{\substack{a+b+c=h\\0\leq a\leq2}}
\frac{h!}{a!\,b!\,c!}\,
P^{(a)}(s)
\left(-\frac{\log\pi}{2}\right)^b
2^{-c}\Gamma^{(c)}(s/2),
\tag{RZ5.11}
\]
where \(P^{(0)}=s(s-1)\), \(P'=2s-1\), and \(P''=2\).

At an exceptional point \(z\in\{0,1,-2,-4,\ldots\}\), the same entire representatives have the full value
\[
E_{\rho,j}(z)=F_0(z)B_\rho(z)(z-\rho)^{j-m},
\tag{RZ5.12}
\]
with \(F_0(z)\) given by (RZ1.7)–(RZ1.8). These values have not been forced to vanish or removed from the source functions. Evaluation at these points is not a quotient character, as RZ3 already proves.

## RZ6. Continuous projectors and exact generalized eigenspaces

For a holomorphic germ \(H\) at \(\rho\), write
\[
\operatorname{Tay}_{\rho,<r}H(s)
=\sum_{j=0}^{r-1}\frac{H^{(j)}(\rho)}{j!}(s-\rho)^j
\quad(r\geq1).
\tag{RZ6.1}
\]
The promised finite-rank lift on the entire function space is
\[
\boxed{\quad
\mathscr P_\rho F(s)=
A_\rho(s)\operatorname{Tay}_{\rho,<m}
\left(\frac{F}{A_\rho}\right)(s).
\quad}
\tag{RZ6.2}
\]
The quotient \(F/A_\rho\) is used only as a germ at \(\rho\), where \(A_\rho(\rho)\ne0\). The displayed output is a globally defined entire function. It belongs to \(\mathcal B\) as a finite polynomial times \(A_\rho\). Its coefficients are fixed finite linear combinations of the jets of \(F\) at \(\rho\), so (RZ2.1) proves continuity.

The output has exactly the same first \(m\) Taylor coefficients as \(F\) at \(\rho\), and has every required vanishing jet at all other zeros. Moreover
\[
\mathscr P_\rho^2=\mathscr P_\rho,\qquad
\mathscr P_\rho\mathcal I=\{0\},\qquad
\mathscr P_\rho\mathscr P_\sigma=0\quad(\rho\ne\sigma).
\tag{RZ6.3}
\]
For the first equality, divide \(\mathscr P_\rho F\) by \(A_\rho\); its quotient is already a polynomial of degree below \(m\), so its Taylor truncation is unchanged. For the second, \(F/A_\rho\) has a zero of order at least \(m\) at \(\rho\). For the third, \(\mathscr P_\sigma F\) has a zero of order at least \(m_\rho\) at \(\rho\), and the same Taylor argument applies.

Consequently the quotient projector
\[
P_\rho[F]=[\mathscr P_\rho F]=[e_\rho F]
\tag{RZ6.4}
\]
is well defined and continuous. To verify the second equality, both functions have the jets of \(F\) at \(\rho\) and zero jets at every other zero; their difference is in \(\mathcal I\). Equivalently
\[
P_\rho[F]=
\sum_{j=0}^{m-1}\frac{F^{(j)}(\rho)}{j!}[E_{\rho,j}]
=\sum_{j=0}^{m-1}F^{(j)}(\rho)[D_{\rho,j}].
\tag{RZ6.5}
\]
The range \(\mathcal Q_\rho=P_\rho\mathcal Q\) has dimension exactly \(m\), since (RZ5.7) proves independence and (RZ6.5) proves spanning.

The lift \(\mathscr P_\rho:\mathcal B\to\mathcal B\) annihilates \(\mathcal I\), so it also defines a continuous map \(\mathcal Q\to\mathcal B\), by the defining quotient topology. On \(\mathcal Q_\rho\) it is a continuous choice of source representative. In addition
\(\mathcal Q=\mathcal Q_\rho\oplus\ker P_\rho\)
is a topological direct sum: the forward map sends \(x\) to \((P_\rho x,x-P_\rho x)\), and its continuous inverse adds the two components. This is a split finite-dimensional spectral block of the full quotient.

This range is exactly the actual generalized eigenspace:
\[
\mathcal Q_\rho=\ker(L-\rho)^m.
\tag{RZ6.6}
\]
The inclusion from left to right follows from the required local orders, or from \((s-\rho)^m e_\rho=F_0B_\rho\). Conversely, if \((s-\rho)^mF\in\mathcal I\), then at every other zero \(\sigma\) the factor \((s-\rho)^m\) is an invertible holomorphic germ, so \(F\) has all required zero jets there. At \(\rho\), \(F-\mathscr P_\rho F\) has all required zero jets by construction. Hence \([F]=P_\rho[F]\), proving the reverse inclusion.

Put \(N_\rho=(L-\rho)|_{\mathcal Q_\rho}\). Its complete action is
\[
N_\rho[E_{\rho,j}]=
\begin{cases}
[E_{\rho,j+1}],&j<m-1,\\
0,&j=m-1.
\end{cases}
\tag{RZ6.7}
\]
In derivative-coordinate representatives,
\[
N_\rho[D_{\rho,j}]=(j+1)[D_{\rho,j+1}]
\quad(j<m-1).
\tag{RZ6.8}
\]
Thus \(N_\rho^m=0\) and \(N_\rho^{m-1}\ne0\); its ranks are
\(\operatorname{rank}N_\rho^r=m-r\) for \(0\leq r<m\).
In particular \([E_{\rho,m-1}]\ne0\) is an eigenvector with eigenvalue \(\rho\).

It now follows from RZ3 and this eigenvector that the finite continuous spectrum is exactly
\[
\boxed{\operatorname{Spec}(L)=\mathscr Z.}
\tag{RZ6.9}
\]
Here the resolvent set means those \(\lambda\in\mathbb C\) for which \(\lambda-L\) has an everywhere-defined continuous inverse. No Banach-space spectral convention is being silently substituted.

The family of projectors also separates the complete quotient:
\[
\bigcap_{\rho\in\mathscr Z}\ker P_\rho=\{0\}.
\tag{RZ6.10}
\]
Indeed every vanishing projector forces all the corresponding actual jets to vanish, and S5 identifies their common kernel with \(\mathcal I\). This is a statement on every quotient class. It does not assume convergence of an infinite sum of projectors.

## RZ7. Riesz contour formula, every Laurent coefficient, and signs

Choose a positively oriented circle \(\gamma_\rho\) enclosing \(\rho\) and no other zero. Its radius can be chosen positive because the zeros of the nonzero entire \(F_0\) are isolated. On that contour, RZ3–RZ4 give a holomorphic, locally equicontinuous resolvent.

We first compute its integral at the level of \(\mathcal B\):
\[
\frac1{2\pi i}\int_{\gamma_\rho}
\mathscr R_\lambda F\,d\lambda=\mathscr P_\rho F.
\tag{RZ7.1}
\]
For \(s\) outside the closed circle, the first term \(F(s)/(\lambda-s)\) in (RZ3.1) has integral zero. Put \(t=\lambda-\rho\), \(d=s-\rho\), and write locally
\[
\frac{F(\rho+t)}{A_\rho(\rho+t)}
=\sum_{\ell\geq0}h_\ell t^\ell.
\tag{RZ7.2}
\]
The remaining term is
\[
-F_0(s)\,
\frac{t^{-m}\sum_{\ell\geq0}h_\ell t^\ell}{t-d}.
\]
Since
\[
\frac1{t-d}=-\sum_{r\geq0}\frac{t^r}{d^{r+1}},
\tag{RZ7.3}
\]
its residue is
\[
F_0(s)\sum_{\ell=0}^{m-1}
\frac{h_\ell}{(s-\rho)^{m-\ell}}
=A_\rho(s)\sum_{\ell=0}^{m-1}h_\ell(s-\rho)^\ell.
\tag{RZ7.4}
\]
The two negative signs cancel. This is (RZ6.2). Both sides of (RZ7.1) are entire functions of \(s\), so equality outside the circle proves equality everywhere. This also handles \(s\) on or inside the contour without separating singular terms there.

Passing to the quotient proves the actual Riesz formula
\[
\boxed{\quad
P_\rho=\frac1{2\pi i}\int_{\gamma_\rho}
(\lambda-L)^{-1}\,d\lambda.
\quad}
\tag{RZ7.5}
\]
Thus the explicit projectors are the Riesz projectors of the actual continuous operator, not merely finite interpolation maps.

Every principal Laurent coefficient has an equally explicit global lift. For \(0\leq r<m\),
\[
\mathscr C_{\rho,r}F(s)
=A_\rho(s)(s-\rho)^r
\operatorname{Tay}_{\rho,<m-r}
\left(\frac{F}{A_\rho}\right)(s),
\tag{RZ7.6}
\]
and
\[
\frac1{2\pi i}\int_{\gamma_\rho}
(\lambda-\rho)^r\mathscr R_\lambda F\,d\lambda
=\mathscr C_{\rho,r}F.
\tag{RZ7.7}
\]
For \(r\geq m\) this integral is zero. The proof repeats (RZ7.3): the residue condition becomes \(\ell+\text{summation index}=m-r-1\), giving exactly (RZ7.6).

The induced coefficient is
\[
[\mathscr C_{\rho,r}F]
=(L-\rho)^rP_\rho[F].
\tag{RZ7.8}
\]
Indeed replacing the Taylor truncation of length \(m-r\) by the one of length \(m\) changes the result by \(F_0(s)P(s)\), where \(P\) is a polynomial. This product belongs to \(\mathcal B\) by (RZ2.3) and to \(\mathcal I\) by its full zero orders; no claim that \(P\) itself belongs to \(\mathcal B\) is needed.

There is also a one-step identity retaining the exact source correction. With the coefficients \(h_j\) of (RZ7.2), and with \(\mathscr C_{\rho,m}=0\),
\[
(s-\rho)\mathscr C_{\rho,r}F(s)
-\mathscr C_{\rho,r+1}F(s)
=F_0(s)h_{m-r-1}
\quad(0\leq r<m).
\tag{RZ7.11}
\]
It follows by subtracting the two Taylor polynomials, whose sole remaining term has degree \(m-r-1\). These corrections are present on \(\mathcal B\), even though their quotient classes vanish. In particular
\[
s\mathscr P_\rho F-\mathscr P_\rho(sF)
=F_0h_{m-1},
\tag{RZ7.12}
\]
so \(P_\rho L=LP_\rho\) is exact on \(\mathcal Q\) with the displayed correction at the representative level.

There is a meromorphic operator family on the whole finite \(\lambda\)-plane. To see this directly before quotienting, the jointly holomorphic divided expression in RZ4 is divided only by \(F_0(\lambda)\). Near \(\rho\), its pole order is at most \(m\); the uniform seminorm estimates on a surrounding circle and the parameter Cauchy formula give its Laurent expansion in continuous operators, uniformly on bounded input sets. Consequently on \(\mathcal Q\),
\[
R_\lambda=
\sum_{r=0}^{m-1}
\frac{(L-\rho)^rP_\rho}{(\lambda-\rho)^{r+1}}
+\text{a holomorphic operator family near }\rho .
\tag{RZ7.9}
\]
The pole order is exactly \(m\), because its last coefficient has rank one and is nonzero by (RZ6.7). More generally its coefficient of order \((\lambda-\rho)^{-r-1}\) has rank \(m-r\).

On the actual block, the resolvent is the finite algebraic identity
\[
R_\lambda|_{\mathcal Q_\rho}
=\sum_{r=0}^{m-1}\frac{N_\rho^r}{(\lambda-\rho)^{r+1}}.
\tag{RZ7.10}
\]
Multiplication by \((\lambda-\rho)I-N_\rho\) telescopes to the identity because \(N_\rho^m=0\), verifying every sign independently of the contour calculation.

## RZ8. The entire unshifted arithmetic action

For every positive real \(a\), define
\[
T_aF(s)=a^sF(s),\qquad a^s=e^{s\log a},
\tag{RZ8.1}
\]
where \(\log a\) is the real logarithm. This preserves \(\mathcal B\) and its ideal \(\mathcal I\), since the multiplier is entire and nowhere zero. The exact estimates are
\[
b_{A,M}(T_aF)\leq
\max(a^A,a^{-A})\,b_{A,M}(F),
\tag{RZ8.2}
\]
and on the source,
\[
\mathcal M^{-1}T_a\mathcal Mk(u)
=a^{1/2}k(u/a)=a^{1/2}V_ak(u),
\tag{RZ8.3}
\]
\[
p_{N,j}(a^{1/2}V_ak)
\leq a^{1/2}\max(a^N,a^{-N})p_{N,j}(k).
\tag{RZ8.4}
\]
Both the factor \(a^{1/2}\) and the original Mellin variable \(s\) are retained.

These operators obey \(T_aT_b=T_{ab}\) and \(T_1=I\). In the real parameter \(t=\log a\), they form a strongly smooth group whose generator is \(L\):
\[
\frac{d^r}{dt^r}T_{e^t}[F]=L^rT_{e^t}[F].
\tag{RZ8.5}
\]
For a direct topological justification, on a bounded real \(t\)-interval the derivative multipliers \(s^re^{ts}\) satisfy (RZ8.2) followed by (RZ1.10) repeatedly. Taylor's integral remainder for real \(t\) gives difference-quotient convergence in every seminorm, using one additional power of \(s\). Equivalently (RZ8.4) and the logarithmic derivative bounds give the same assertion on \(\mathcal A\).

In this explicit real-parameter multiplier sense we write
\[
\boxed{n^L=T_n=\sqrt n\,V_n\quad(n=1,2,3,\ldots).}
\tag{RZ8.6}
\]
This notation is justified by the multiplier and group formulas just proved. It does not assume convergence of the exponential power series of a continuous operator in a nonnormable Fréchet space. Such a series convergence is unnecessary here.

On every actual multiplicity block,
\[
T_n[E_{\rho,j}]
=n^\rho\sum_{r=0}^{m_\rho-1-j}
\frac{(\log n)^r}{r!}[E_{\rho,j+r}].
\tag{RZ8.7}
\]
This follows by taking the full Taylor series of \(n^s=n^\rho e^{(s-\rho)\log n}\) at \(\rho\), retaining all terms that survive modulo the order \(m_\rho\). All other-zero jets still vanish. Thus
\[
T_n|_{\mathcal Q_\rho}
=n^\rho\sum_{r=0}^{m_\rho-1}
\frac{(\log n)^r}{r!}N_\rho^r .
\tag{RZ8.8}
\]
On this block the eigenvalue is \(n^\rho\), with algebraic multiplicity \(m_\rho\); its modulus is exactly \(n^{\operatorname{Re}\rho}\). No conclusion that this modulus is \(\sqrt n\) has been assumed.

For the original unscaled derivative jets, the complete triangular formula is
\[
(T_nF)^{(j)}(\rho)
=n^\rho\sum_{\ell=0}^j
\binom j\ell(\log n)^{j-\ell}F^{(\ell)}(\rho).
\tag{RZ8.9}
\]
Equivalently, on the representatives of individual derivative coordinates,
\[
T_n[D_{\rho,j}]
=n^\rho\sum_{r=0}^{m_\rho-1-j}
\binom{j+r}{r}(\log n)^r[D_{\rho,j+r}].
\tag{RZ8.10}
\]
These formulas also cover \(n=1\) with its identity action. The trace of this finite block is \(m_\rho n^\rho\), since every positive power of \(N_\rho\) has zero diagonal.

For \(n>1\), the arithmetic operator itself retains the full Jordan length \(m_\rho\). Indeed
\[
n^{-\rho}T_n-I=N_\rho H_n(N_\rho),\qquad
H_n(z)=\sum_{r=1}^{m_\rho}\frac{(\log n)^r}{r!}z^{r-1},
\quad H_n(0)=\log n\ne0.
\tag{RZ8.11}
\]
The last possible term is harmless because \(N_\rho^{m_\rho}=0\). The polynomial \(H_n(N_\rho)\) is invertible: its nonzero constant term times the identity has a nilpotent correction, whose inverse is its finite geometric series. Hence \((T_n-n^\rho I)^r\) has the same rank as \(N_\rho^r\), including the nilpotence index \(m_\rho\).

Different zero blocks are never identified merely because one arithmetic operator has coincident eigenvalues. For a fixed \(n>1\),
\[
n^\rho=n^\sigma
\quad\Longleftrightarrow\quad
\rho-\sigma=\frac{2\pi i k}{\log n}
\ \text{for some }k\in\mathbb Z.
\tag{RZ8.12}
\]
The full family separates the original \(s\)-values. Already equality at both \(n=2\) and \(n=3\) implies \(k\log3=l\log2\), hence \(3^k=2^l\) for integers \(k,l\). Unique prime factorization forces \(k=l=0\), so \(\rho=\sigma\). This statement retains the exact phase periods of each individual operator.

## RZ9. Reflection acts on every jet, including its sign

The exact source involution is \(k^\#(u)=\overline{k(1/u)}\). On \(\mathcal B\) it is
\[
F^\#(s)=\overline{F(1-\overline s)}.
\tag{RZ9.1}
\]
It is conjugate-linear and continuous:
\[
b_{A,M}(F^\#)\leq b_{A+1,M}(F).
\tag{RZ9.2}
\]
The original functional equation and conjugation preserve zero multiplicities under
\[
\rho^\#=1-\overline\rho,\qquad
m_{\rho^\#}=m_\rho.
\tag{RZ9.3}
\]
Thus \(\mathcal I\) is invariant and the involution descends to the whole quotient. Its derivative formula is
\[
(F^\#)^{(j)}(\rho^\#)
=(-1)^j\overline{F^{(j)}(\rho)}.
\tag{RZ9.4}
\]
To prove it, put \(s=\rho^\#+h\); then \(1-\overline s=\rho-\overline h\), and conjugate the full local Taylor series.

Applying (RZ9.4) to the isolating jets gives
\[
[E_{\rho,j}]^\#=(-1)^j[E_{\rho^\#,j}],
\qquad
[D_{\rho,j}]^\#=(-1)^j[D_{\rho^\#,j}].
\tag{RZ9.5}
\]
These are equalities of actual quotient classes because all their zero jets agree globally. In particular
\[
(P_\rho x)^\#=P_{\rho^\#}(x^\#),
\qquad
(Lx)^\#=(1-L)x^\#,
\tag{RZ9.6}
\]
\[
(T_ax)^\#=a^{1-L}x^\#=aT_a^{-1}x^\#.
\tag{RZ9.7}
\]
For the nilpotent parts, (RZ9.6) reads
\[
(N_\rho x)^\#=-N_{\rho^\#}x^\#
\quad(x\in\mathcal Q_\rho).
\tag{RZ9.8}
\]
The sign is essential and does not disappear when a zero happens to be on the critical line.

For the specific source representatives constructed here, (RZ9.5) holds even before passage to the quotient. The source symmetry \(F_0^\#=F_0\) gives
\[
A_\rho^\#=(-1)^{m_\rho}A_{\rho^\#}.
\tag{RZ9.9}
\]
Applying reflection to the uniquely determined reciprocal Taylor polynomial gives
\[
B_\rho^\#=(-1)^{m_\rho}B_{\rho^\#}.
\tag{RZ9.10}
\]
Indeed the reflected product is one modulo the required order, and the reciprocal polynomial of degree below \(m_\rho\) is unique by the recursion (RZ5.3). The two signs cancel in the product \(e_\rho^\#=e_{\rho^\#}\). Multiplying by the reflected factor \((s-\rho)^j\) supplies exactly the remaining \((-1)^j\) in (RZ9.5). Thus the corresponding source functions in (RZ5.8) also satisfy the exact reflected identity.

## RZ10. The actual reflected Weil form and its block trace

Use the existing source-derived form from G5, written on this exact quotient:
\[
W([F],[G])
=\sum_{\rho\in\mathscr Z}m_\rho\,
\overline{F(\rho^\#)}G(\rho).
\tag{RZ10.1}
\]
This is conjugate-linear in the first input and linear in the second. Its absolute convergence and continuity follow already from the weaker zero-count bound proved in S2,
\[
\sum_{|\rho|\leq R}m_\rho\leq C(R+2)^{3/2}.
\tag{RZ10.2}
\]
Indeed \(0<\operatorname{Re}\rho<1\), the reflected zero has the same imaginary part, and
\[
|F(\rho^\#)G(\rho)|
\leq b_{1,2}(F)b_{1,2}(G)(1+|\operatorname{Im}\rho|)^{-4}.
\]
The sum of the last weights with multiplicities is finite by grouping zeros into dyadic height intervals and applying (RZ10.2). Therefore
\[
|W([F],[G])|
\leq C_W b_{1,2}(F)b_{1,2}(G).
\tag{RZ10.3}
\]
It descends because \(\mathcal I\) annihilates every displayed value. Taking infima over representatives also proves a bound by \(C_Wq_{1,2}([F])q_{1,2}([G])\). Reflection and multiplicity preservation prove Hermitian symmetry by relabelling the absolutely convergent sum.

The word trace here has an exact interpretation on the constructed blocks. Multiplication by any \(H\in\mathcal B\) preserves \(\mathcal Q_\rho\); in the basis \([E_{\rho,j}]\), its diagonal entries are all \(H(\rho)\). Hence
\[
\operatorname{Tr}_{\mathcal Q_\rho}(M_H)=m_\rho H(\rho),
\tag{RZ10.4}
\]
and
\[
W([F],[G])
=\sum_{\rho\in\mathscr Z}
\operatorname{Tr}_{\mathcal Q_\rho}(M_{F^\#G}).
\tag{RZ10.5}
\]
This is the absolutely convergent sum of the specified finite-dimensional block traces. It does not assert a trace-class operator on an unstated Hilbert completion.

Every block entry is explicit:
\[
\boxed{\quad
W([E_{\rho,j}],[E_{\sigma,k}])
=m_\sigma\,
\mathbf1_{\{\rho=\sigma^\#\}}
\mathbf1_{\{j=0\}}\mathbf1_{\{k=0\}}.
\quad}
\tag{RZ10.6}
\]
The same formula holds for \(D_{\rho,j}\), since only the zeroth representative contributes. This is immediate from all-zero isolation (RZ5.7).

If \(\rho=\rho^\#\), the form on \(\mathcal Q_\rho\) has one positive direction of squared length \(m_\rho\) and radical of dimension \(m_\rho-1\). If \(\rho\ne\rho^\#\), put \(m=m_\rho=m_{\rho^\#}\). On the two constant-jet representatives its matrix is exactly
\[
\begin{pmatrix}0&m\\m&0\end{pmatrix}.
\tag{RZ10.7}
\]
Its values on the sum and difference of those representatives are \(2m\) and \(-2m\), respectively. The entire paired space \(\mathcal Q_\rho\oplus\mathcal Q_{\rho^\#}\) has one positive direction, one negative direction, and radical dimension \(2(m-1)\).

Globally the radical is precisely
\[
\operatorname{rad}W
=
\{[F]\in\mathcal Q:F(\rho)=0\text{ for all }\rho\in\mathscr Z\}.
\tag{RZ10.8}
\]
One inclusion follows from (RZ10.1). Conversely, pairing with \([E_{\sigma,0}]\) gives
\(m_\sigma\overline{F(\sigma^\#)}\); if every such pairing vanishes, every zero value is zero. Higher multiplicity jets therefore remain real nonzero quotient data even though this ordinary trace form cannot detect them.

## RZ11. Full arithmetic similitude, reflected adjoints, and the exact sign question

For every \(a>0\), with no restriction on the real parts of the actual zeros,
\[
\begin{aligned}
W(T_ax,T_ay)
&=\sum_\rho m_\rho\,
\overline{a^{\rho^\#}F(\rho^\#)}
a^\rho G(\rho)\\
&=\sum_\rho m_\rho\,a^{\overline{\rho^\#}+\rho}
\overline{F(\rho^\#)}G(\rho)\\
&=aW(x,y),
\end{aligned}
\tag{RZ11.1}
\]
because \(\overline{\rho^\#}=1-\rho\). In particular
\[
\boxed{W(n^Lx,n^Ly)=nW(x,y),\qquad n^L=\sqrt n\,V_n.}
\tag{RZ11.2}
\]
This preserves the full unshifted arithmetic factor. Dividing both arguments by the displayed \(\sqrt n\) recovers the earlier exact invariance of \(V_n\), but the original \(n^L\) is the operator in (RZ11.2).

The corresponding identities for the pairing are
\[
W(Lx,y)=W(x,(1-L)y),
\tag{RZ11.3}
\]
\[
W(T_ax,y)=W(x,aT_a^{-1}y),
\qquad
W(P_\rho x,y)=W(x,P_{\rho^\#}y).
\tag{RZ11.4}
\]
For the first equation, conjugation of the first factor changes the spectral scalar \(\rho^\#\) into \(1-\rho\). The second follows by the same direct scalar calculation, and the projector identity follows by its global zero-jet support. These are identities for a possibly indefinite and degenerate form, not adjoint assertions for an unconstructed positive Hilbert norm.

For the resolvent there is a further retained sign:
\[
W(R_\lambda x,y)
=-W(x,R_{\,1-\overline\lambda}y)
\quad(\lambda\notin\mathscr Z).
\tag{RZ11.5}
\]
The reflected parameter is also outside \(\mathscr Z\) by (RZ9.3). Directly,
\[
\frac1{\overline\lambda-\overline{\rho^\#}}
=-\frac1{1-\overline\lambda-\rho},
\]
which proves (RZ11.5) term by term in the convergent form. Equivalently it follows by taking the pairing adjoint of \(\lambda-L\) using (RZ11.3).

On an off-line pair the actual eigenvalues obey
\[
n^{\rho^\#}=\frac{n}{\overline{n^\rho}},
\qquad
|n^\rho|=n^{\operatorname{Re}\rho},\qquad
|n^{\rho^\#}|=n^{1-\operatorname{Re}\rho}.
\tag{RZ11.6}
\]
Their reflected pairing therefore has the exact factor \(n\) even when neither modulus is \(\sqrt n\). The complete nilpotent coefficients of their action remain (RZ8.7)–(RZ8.10); their absence from the value trace is accounted for by the radical (RZ10.8), not by removal of the corresponding vectors.

These explicit representatives also give the precise positivity equivalences for this specified form. The form \(W\) is positive semidefinite exactly when every actual zero satisfies \(\rho=\rho^\#\): the forward implication follows from the negative vector in (RZ10.7), and the reverse implication follows from the convergent sum \(\sum_\rho m_\rho|F(\rho)|^2\). It is positive definite exactly when, in addition, all multiplicities are one. If a multiplicity exceeds one, (RZ5.7) gives a nonzero higher-jet radical vector. If all multiplicities are one, zero values at every zero mean membership in \(\mathcal I\), so no nonzero quotient vector can have zero squared length in the positive case.

These are proved equivalences and explicit block signatures. No positive-semidefiniteness assertion or RH conclusion has been inserted.

## RZ12. Exact scope and retained source information

The resolvent acts continuously on the entire Fréchet quotient and has exactly the actual original nontrivial zeros as its finite spectrum. Its poles have exactly their original multiplicities. The projectors are simultaneously actual contour projectors, explicit continuous finite-rank lifts on the full source function space, and isolators of the full jet at one zero with every other-zero jet zero. Every source representative has all endpoint and derivative seminorms controlled by (RZ4.7).

The full multiplier \(s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/8\), its endpoint values, the finite values at the original trivial zeros, and all local derivative contributions remain explicit. The arithmetic action is the original-variable operator \(n^L=\sqrt nV_n\), with every logarithmic multiplicity term and the exact reflected form. The independent source synthesis S5 is used on its actual domain; no finite numerical experiment, unrestricted jet-product identification, positive completion, or RH assumption replaces it.
