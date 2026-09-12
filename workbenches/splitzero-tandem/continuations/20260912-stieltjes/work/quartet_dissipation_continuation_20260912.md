# Quartet derivative dissipation continuation — 12 September 2026

Status: completed independent mathematics tranche, ready for parent integration. The new proof fragment is separate from every frozen source and the frozen 216-page edition. This file contains the entire final proof source below, not an abbreviated mathematical account.

## Task and provenance

Parent instruction, verbatim:

> Concrete independent next mathematics, separate new files only; frozen216edition immutable. Investigate exact factor-one strengthening of FE.24--25 under actual quartet parity AP.10--13. Domain parity of Y_M and C_M should make -(Y*C+C*Y) off-diagonal, so epsilon=||Ytilde*Ctilde|| <=||Ytilde||||Ctilde|| without factor2. Full identities: ||Ytilde||²=lambda/(1+lambda), Ctilde*Ctilde=V(I+U*U)V*, chi=Tr of same; epsilon²<=lambda/(1+lambda)*chi. Prove exact source/target maps from actual b,H,F,E+,G,Omega with all signs and zero ranks; derive corresponding complete determinant lower bound with 4k²delta_*² rather than k²delta_*². Independently check that rankzero and delta0 are retained and whether stronger operator-norm replacement of chi holds. Save full proof work/quartet_dissipation_continuation_20260912.md plus tex fragment ONLY if genuinely new to existing AP/FE; do not edit main/frozenfiles. Root pursues actual theta norm growth via local canonical literature; no need spawn.

Later parent steering, verbatim:

> Keep k=1 exact cost identity and all zero cases. Please finish separate full TeX proof fragment with source original symbols before next review. I am writing full theta_stieltjes_pair.tex quadratic-cover/positive measure map; literature lane has exact gamma-reference determinant norms and will write another full fragment. Frozen releaseE/owner publication untouched.

Read and compared the complete current `frontier_energy_dissipation.tex` and `arithmetic_frontier_parity.tex`. FE.24 contains the coefficient four in the original source derivative estimate; FE.25 contains the corresponding coefficient one on the squared spectral displacement. AP.15 proves the exact norm of the single quartet frontier block and AP.17 proves its recurrence estimate. The source derivative factor-one estimate, its operator-norm cost, the corresponding determinant estimates, and the one-variable exact source energy/volume identity were absent from those complete texts.

Exact SHA256 hashes:

| Object | SHA256 |
|---|---|
| New `tex/quartet_dissipation_continuation.tex` | `7f6e76ef6d6a7126eb52c4e02d0448f7d7d69b50c163f250f2a99ff096f1fea0` |
| Read `tex/frontier_energy_dissipation.tex` | `03b2073d0018652d3bc2a857bd71a2e717547dab8fcd434f1cd6039fe22e9c28` |
| Read `tex/arithmetic_frontier_parity.tex` | `ef45217a8d73062180c4adb6e8a8435db0c2fec4a0806e3155c8ecd29cde4ef9` |
| Unchanged frozen 216-page PDF | `43d3988bcfa0c84b45732b8ae9feb075d42c75dd67ef0167e9afc1ddaad31370` |

The three TeX paths in the table are relative to `output/split_zero_rh_tandem_2026-09-12`. The PDF is that directory's `Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf`. The two original source hashes and frozen PDF hash were checked again after finishing the new fragment and remain unchanged.

## Deliverable and exact result locations

The new proof is `output/split_zero_rh_tandem_2026-09-12/tex/quartet_dissipation_continuation.tex`. It contains three theorem statements, complete proofs, the original construction and reflection, and fifteen explicitly tagged formulas:

- QD.1–QD.5 retain the actual full-order arithmetic packet, original monomial remainder coordinates, all polynomial norms, the graph map `b`, its actual layer target, and the exact Hilbert isometries. The derivative map `C_D` is explicitly identified with the previously defined `C_M`; the new spelling only avoids collision with the residue reflection `C`.
- QD.6 proves both domain parities and the signed exact composite `−Yhat* Chat = UV*`. The target reflection is also proved on the entire original layer; it has the single sign `eta` for both maps. This distinguishes domain and target parity by explicit identities rather than discarding either.
- QD.8–QD.9 give the new factor-one estimate and the stronger cost `zeta = ||C_M G_M^(−1/2)||op²`, with its complete original matrix and trace formulas. The proof permits every zero rank.
- QD.10 is the undivided zero-safe chain. QD.11–QD.12 prove the improved finite source determinant bounds with `4 k² delta_*²`, all divisions and logarithms justified. They retain every nilpotent jet through the original CRT eigenline proof. The stagewise bound using the actual positive `epsilon_M²` is retained even when `delta_*=0`.
- QD.13 states the explicit accumulated recurrence consequence already implicit in AP.17. It is labelled as that consequence, not claimed as a separate new operator theorem.
- QD.14–QD.15 prove the further exact one-variable arithmetic identity: `zeta_M=chi_M` and `epsilon_M²=(1−pi_M)chi_M`. This uses the actual one-dimensional graph layer when `k=1`, with an explicit unit vector `J_b 1` and exact row maps. No synthetic fixture or supposition about the location of zeros is used.

The zero derivative-cost case remains undivided: it forces zero weight and does not force the metric update to vanish. Zero frontier update and zero spectral displacement are separately retained with their exact original maps.

## Verification and integration boundary

The fragment was compiled with the current cumulative paper's exact preamble in a separate five-page review wrapper under `work/quartet_dissipation_review_20260912`. XeLaTeX exits successfully; the final log contains no overfull box, missing character, undefined reference, or warning. This isolated review does not modify or rebuild the frozen edition. A Poppler rendering of all five pages was visually inspected for overlap, clipping, equation-tag collisions and missing glyphs; none was found. The final receipt is `work/quartet_dissipation_review_20260912/verification_receipt.json`.

No numerical fixture was used to replace the analytic proof. The rank-one equality establishes the exact coefficient in the actual one-variable arithmetic family. This tranche proves finite identities and finite determinant constraints; it does not manufacture an asymptotic upper bound for the original theta energies. Parent owns the next combined source and PDF integration.

## Full theorem and proof source

The fenced text below is a complete byte-for-text copy of the final fragment (apart from the Markdown fence), with all definitions, signs, displayed maps, zero cases, theorem statements and proofs preserved.

```tex
\section{Quartet parity in the original derivative energy and volume loss}
\label{sec:quartet-dissipation-continuation}

This continuation retains the original maps of (FE.3)--(FE.9)
and the actual quartet reflection of (AP.7)--(AP.13).  Their
combination proves an exact block identity for the two maps into
the original theta relation layer.  It yields a stronger derivative
energy estimate than (FE.24), including an operator-norm version
and the resulting finite accumulated determinant bounds.

\subsection{Original maps, their spaces, and the reflection}

Fix a nonempty packet of actual zeros, with every selected zero's
full multiplicity, closed under conjugation and under
\(\rho\mapsto1-\overline\rho\).  Keep
\[
 h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\quad d=\deg h,
 \quad g=2\xi,\quad v_h=g/h,\quad
 \upsilon=j_hv_h,\quad E_k=(\mathbb C[s]/h)^{\otimes k}.
\]
Here \(k\geq1\), \(M\geq k(d-1)\), and the original
generator is \(A_k=\sum_{j=1}^kA_{h,j}\).  Let \(G=G_M>0\)
be the actual degree-\(M\) minimum metric in the original
monomial remainder basis, and let
\(R=R_M:E_k\to\mathcal H_k=L^2(\mathbb R_{>0}^k,d^kx)\)
be its original representative, so \(R^*R=G\).

For the unchanged measure
\(d\nu_h(t)=|v_h(1/2+it)|^2dt/(2\pi)\), let \(q_j\)
be the monic orthogonal polynomials and
\(\kappa_j=\|q_j\|_{\nu_h}^2\).  Write
\(q_\beta=\prod_jq_{\beta_j}\),
\(\kappa_\beta=\prod_j\kappa_{\beta_j}\), and
\(z_\beta=U_{\upsilon^{\otimes k}}[q_\beta]\).
With the original ordering of \(|\beta|=M+1\), retain
\[
 \begin{gathered}
 r=\binom{M+k}{k-1},\quad
 \Omega=\operatorname{diag}(\kappa_\beta)>0,\quad
 F=[z_\beta]:\mathbb C^r\to E_k,\\
 E_+=[w_\beta]:\mathbb C^r\to E_k,\qquad
 w_\beta=\sum_{j:\beta_j>0}
                  \frac{\kappa_{\beta_j}}{\kappa_{\beta_j-1}}
                       z_{\beta-e_j},\\
 T_+=[\mathcal T_h^{(k)}q_\beta]:\mathbb C^r\to\mathcal H_k,
 \qquad b=T_+-RF:\mathbb C^r\xrightarrow{\sim}\mathcal E_M,\\
 H=b^*b=\Omega+F^*GF>0.
 \end{gathered}                                                     \tag{QD.1}
\]
The space \(\mathcal E_M\) is the actual next theta relation
layer with its inherited \(L^2\) norm.  The column Gram of
\(T_+\) is \(\Omega\); its image is perpendicular to the old
polynomial space containing \(R(E_k)\).  Thus expanding its
Gram proves \(H\) in (QD.1).  The leading degree map gives
the inverse of \(b\): each layer vector's highest polynomial
coefficient determines it, and subtracting that graph image
leaves a vector both in the old relation space and perpendicular
to it.  In particular \(b\) is a bijection onto the original
layer, with no arbitrary Hilbert replacement.

The two original maps into that same layer and their weight are
\[
 \begin{gathered}
 Y=-bH^{-1}F^*G:E_k\to\mathcal E_M,\qquad
 C_D=b\Omega^{-1}E_+^*G:E_k\to\mathcal E_M,\\
 \Delta=Y^*Y=G-G_{M+1},\qquad
 W=A_k^*G+GA_k-kG=-(Y^*C_D+C_D^*Y).
 \end{gathered}                                                     \tag{QD.2}
\]
The notation \(C_D\) is explicitly the map \(C_M\) of (FE.5),
and does not denote the inverse interpolation matrix.  Its
formula records the top polynomial coefficient of the original
Euler defect; the graph projection and the original theta
primitive in (FE.3)--(FE.5) supply its actual source realization.
The weight identity also follows directly by inserting the two
displayed maps and cancelling the middle \(b^*b=H\).

Let \(C:E_k\to E_k\) replace each residue variable \(s_j\)
by \(1-s_j\), and let
\[
 (\mathfrak t_kf)(x_1,\ldots,x_k)
   =\left(\prod_jx_j^{-1}\right)
                           f(x_1^{-1},\ldots,x_k^{-1}).
\]
The original packet symmetries and functional equation give
\(h(1-s)=(-1)^dh(s)\),
\(v_h(1-s)=(-1)^dv_h(s)\), and
\(q_j(1-s)=(-1)^jq_j(s)\).  For the last identity, the
reflected polynomial with its sign restored is monic and has
the same lower-degree orthogonality for the even density;
uniqueness of the monic orthogonal polynomial proves equality.
The variable change \(x_j\mapsto x_j^{-1}\) proves that
\(\mathfrak t_k\) is a unitary involution for \(d^kx\), with
Mellin action \(s_j\mapsto1-s_j\).  Thus it preserves total
degree, the relation ideal and the unique constrained minimum.
Writing \(\eta=(-1)^{kd+M+1}\), one obtains
\[
 \mathfrak t_kR=RC,\quad C^2=I,\quad C^*GC=G,\quad
 CF=\eta F,\quad CE_+=-\eta E_+,\quad
 \mathfrak t_kb=\eta b.                                      \tag{QD.3}
\]
The last equality uses both
\(\mathfrak t_kT_+=\eta T_+\) and \(CF=\eta F\).
It states the exact target reflection on the whole original
relation layer, since \(b\) is onto.

For explicit coordinate isometries put
\[
 \begin{gathered}
 P=G^{1/2}CG^{-1/2},\quad P^*=P,\quad P^2=I,\qquad
 U=G^{1/2}F\Omega^{-1/2},\quad
 V=G^{1/2}E_+\Omega^{-1/2},\\
 \widehat Y=YG^{-1/2},\qquad
 \widehat C=C_DG^{-1/2}:\mathbb C^{d^k}\to\mathcal E_M,\qquad
 J_b=bH^{-1/2}:\mathbb C^r\xrightarrow{\sim}\mathcal E_M.
 \end{gathered}                                                   \tag{QD.4}
\]
The matrix \(G^{1/2}\) is the isometry from \((E_k,G)\)
to its Euclidean coordinate space, with inverse \(G^{-1/2}\).
Similarly \(\Omega^{1/2}\) records the original polynomial
norms, and \(J_b\) is a unitary map with inverse
\(H^{-1/2}b^*\).  No commutation of \(H\) with \(\Omega\)
is assumed.  In these exact coordinates,
\[
 \widehat Y=-J_bH^{-1/2}F^*G^{1/2},\qquad
 \widehat C=J_bH^{1/2}\Omega^{-1}E_+^*G^{1/2}.
                                                                    \tag{QD.5}
\]

\subsection{The single original boundary block}

\begin{theorem}[Exact quartet derivative block and its energy bound]
The two original domain parities and their entire block relation are
\[
 YC=\eta Y,\qquad C_DC=-\eta C_D,\qquad
 \widehat YP=\eta\widehat Y,\qquad
 \widehat CP=-\eta\widehat C,\qquad
 -\widehat Y^*\widehat C=UV^*.                              \tag{QD.6}
\]
Let
\[
 \begin{gathered}
 S=G^{-1/2}WG^{-1/2},\qquad \epsilon=\|S\|_{\rm op},\qquad
 \lambda=\|UU^*\|_{\rm op},\qquad
 \pi=\frac{\det G_{M+1}}{\det G},\\
 \zeta=\|\widehat C\|_{\rm op}^2,\qquad
 \chi=\|\widehat C\|_{\rm HS}^2.
 \end{gathered}                                                   \tag{QD.7}
\]
Then all these actual finite quantities satisfy
\[
 \boxed{\epsilon=\|\widehat Y^*\widehat C\|_{\rm op}
                    =\|UV^*\|_{\rm op},\qquad
 \epsilon^2\leq\frac{\lambda}{1+\lambda}\zeta
              \leq\frac{\lambda}{1+\lambda}\chi.}          \tag{QD.8}
\]
The operator-norm cost and the trace cost are exactly
\[
 \begin{gathered}
 \widehat C^*\widehat C=V(I+U^*U)V^*,\qquad
 \zeta=\lambda_{\max}\bigl(V(I+U^*U)V^*\bigr),\\
 \chi=\operatorname{Tr}\bigl(V(I+U^*U)V^*\bigr)
       =\|V\|_{\rm HS}^2+\|VU^*\|_{\rm HS}^2.
 \end{gathered}                                                   \tag{QD.9}
\]
In particular the operator-norm replacement of \(\chi\)
in (QD.8) is valid without a rank assumption.
\end{theorem}

\begin{proof}
From \(C^*GC=G\) and \(C^2=I\) one gets \(GC=C^*G\).
Thus \(F^*GC=(CF)^*G=\eta F^*G\), and similarly
\(E_+^*GC=-\eta E_+^*G\).  Substitution in (QD.2) proves
the first two parities, and the coordinate change proves the next
two.  Equations (QD.2) and \(b^*b=H\) give, in the order shown,
\[
 \widehat Y^*\widehat C
 =-G^{1/2}FH^{-1}H\Omega^{-1}E_+^*G^{1/2}=-UV^*.
\]
Decompose \(\mathbb C^{d^k}=\ker(P-\eta I)\oplus
\ker(P+\eta I)\), orthogonally.  The first map in (QD.6)
annihilates the second summand and the second map annihilates
the first.  Consequently \(X=\widehat Y^*\widehat C\)
maps the second summand into the first and vanishes on the first.
The actual weight is
\[
 S=-(X+X^*)=
 -\begin{pmatrix}0&X_{+-}\\X_{+-}^*&0\end{pmatrix}.
\]
Squaring gives diagonal blocks \(X_{+-}X_{+-}^*\) and
\(X_{+-}^*X_{+-}\).  Their largest eigenvalues both equal
\(\|X_{+-}\|^2\) when this map is nonzero, by its singular
value decomposition; if it is zero both blocks vanish.  Hence
\(\|S\|=\|X\|\), including empty parity summands and all
zero ranks.

The retained Gram identity in (QD.1) is
\(H=\Omega^{1/2}(I+U^*U)\Omega^{1/2}\).  Substitution gives
\[
 \widehat Y^*\widehat Y
   =U(I+U^*U)^{-1}U^*
   =UU^*(I+UU^*)^{-1}.
\]
The second equality follows by multiplying
\((I+UU^*)U=U(I+U^*U)\) by its positive invertible factors.
Thus \(\|\widehat Y\|^2=\lambda/(1+\lambda)\), also
when \(\lambda=0\).  Submultiplicativity in the exact
identity \(\epsilon=\|\widehat Y^*\widehat C\|\)
proves the first inequality of (QD.8).  On the other hand
\(\widehat C=b\Omega^{-1/2}V^*\), so its Gram is exactly
\(V\Omega^{-1/2}H\Omega^{-1/2}V^*=V(I+U^*U)V^*\).
This proves (QD.9).  A positive finite matrix has largest
eigenvalue at most its trace, proving \(\zeta\leq\chi\)
and the second inequality.
\end{proof}

This is an actual-source strengthening of (FE.24): its general
factor \(4\) is replaced by \(1\) under the proved original
quartet parity.  The retained derivative map still lands in the
original \(\mathcal E_M\); only the displayed exact isometries
were used to calculate its norm.

\subsection{Complete determinant constraints, including zero cases}

Set \(\delta_* =\max_{\rho\in Z}|\operatorname{Re}\rho-1/2|\)
and \(q_*=4k^2\delta_*^2\).  The name \(q_*\) denotes
this nonnegative scalar, not an orthogonal polynomial.  All
original packet multiplicities remain in \(E_k,A_k,G_M\).

\begin{theorem}[Quartet derivative cost and accumulated volume]
At every admitted degree, including \(\delta_*=0\),
\[
 \boxed{q_*\leq\epsilon^2
       \leq\frac{\lambda}{1+\lambda}\zeta
       \leq(1-\pi)\zeta
       \leq(1-\pi)\chi.}                                \tag{QD.10}
\]
If \(\delta_*>0\), the exact source quantities necessarily obey
\[
 \begin{gathered}
 \zeta>q_*,\qquad \chi\geq\zeta>q_*,\qquad
 \lambda\geq\frac{q_*}{\zeta-q_*}
                \geq\frac{q_*}{\chi-q_*},\\
 \boxed{\log\frac{\det G_M}{\det G_{M+1}}
       \geq-\log\left(1-\frac{q_*}{\zeta_M}\right)
       \geq-\log\left(1-\frac{q_*}{\chi_M}\right).}
 \end{gathered}                                                   \tag{QD.11}
\]
For \(\delta_*>0\) and any integers \(k(d-1)\leq a<b\), this gives
\[
 \boxed{\log\frac{\det G_a}{\det G_b}
   \geq\sum_{M=a}^{b-1}-\log\left(1-
                                 \frac{4k^2\delta_*^2}{\zeta_M}\right)
   \geq\sum_{M=a}^{b-1}-\log\left(1-
                                 \frac{4k^2\delta_*^2}{\chi_M}\right).}
                                                                    \tag{QD.12}
\]
Every denominator in (QD.11)--(QD.12) is positive, and every
logarithm has a strictly positive argument, by the preceding inequalities.
\end{theorem}

\begin{proof}
For every selected centre \(\rho\), the original finite
algebra has a nonzero eigenvector of \(A_h\) with eigenvalue
\(\rho\): in its local factor use \((s-\rho)^{m_\rho-1}\)
and put zero in the other full CRT factors.  Its \(k\)-fold
tensor is nonzero and has eigenvalue \(k\rho\) for \(A_k\).
The quotient of \(W=A_k^*G+GA_k-kG\) on that original vector
is exactly \(2k\operatorname{Re}\rho-k\).  The operator
norm of its Hermitian relative matrix is at least the absolute
value of this Rayleigh quotient.  Taking the largest displacement
and squaring proves \(q_*\leq\epsilon^2\), with no
semisimplicity assumption.

The inverse update is
\(G_{M+1}^{-1}=G_M^{-1}+F\Omega^{-1}F^*\).  Conjugating
by the original metric isometry gives
\[
 \pi=\det(I+UU^*)^{-1}
       =\prod_i(1+\lambda_i)^{-1},
\]
where all positive eigenvalues of \(UU^*\) occur with their
multiplicities; the empty product is one.  Since the product
is at least \(1+\lambda\),
\(\pi\leq(1+\lambda)^{-1}\), and therefore
\(\lambda/(1+\lambda)\leq1-\pi\).  Insert (QD.8)
and \(\zeta\leq\chi\) to prove (QD.10).

When \(q_*>0\), (QD.10) implies \(\lambda>0\) and
\(\zeta>0\).  Because \(\lambda/(1+\lambda)<1\),
it then implies \(\zeta>q_*\).  Rearranging its first
cost inequality gives
\(\lambda(\zeta-q_*)\geq q_*\), proving the lower
bound for \(\lambda\).  The function \(x\mapsto
q_* /(x-q_*)\) decreases for \(x>q_*\), proving its
comparison with the bound using \(\chi\).
Finally \(\pi^{-1}\geq1+\lambda\geq
\zeta/(\zeta-q_*)\).  Apply the increasing logarithm,
and use \(\zeta\leq\chi\), to obtain (QD.11).
Adding the finite inequalities telescopes their original
determinants and proves (QD.12).
\end{proof}

At \(\delta_*=0\), (QD.10) remains the complete undivided
statement.  No value is assigned to \(0/0\) when a derivative
cost is zero.  If \(F=0\), then \(U=Y=0\),
\(\lambda=0\), \(\pi=1\) and \(W=0\); the derivative
map \(C_D\) and its cost can still be nonzero.  Conversely
\(\zeta=0\) means \(C_D=0\), and the injectivity of
\(b\Omega^{-1/2}\) gives \(V=E_+=0\); then \(W=0\)
while the metric can still contract through \(F\).  These
are retained source cases, and neither is excluded by division.

The same proof also gives the stagewise estimate with \(q_*\)
replaced by the actual \(\epsilon_M^2\) whenever
\(\epsilon_M>0\), since then \(\zeta_M>\epsilon_M^2\).
Thus a positive boundary cost remains detected even when every
selected centre has real part \(1/2\); no nilpotent contribution
has been removed by using a zero spectral displacement.

For comparison with (FE.22)--(FE.23), retain the actual positive
recurrence quantity
\[
 \Gamma_{k,M}=\max_{|\alpha|=M}\sum_{j=1}^k
       \left(a_{\alpha_j+1}+(k-1)a_{\alpha_j}\right),
 \quad a_j=\kappa_j/\kappa_{j-1},\quad a_0=0.
\]
The proved arithmetic incidence bound (AP.20) is
\(VV^*\preceq\Gamma_{k,M}I\), and therefore
\(\epsilon_M^2=\|UV^*\|^2\leq\Gamma_{k,M}\lambda_M\).
It yields, for all \(\delta_*\geq0\), the finite consequence
\[
 \log\frac{\det G_a}{\det G_b}
 \geq\sum_{M=a}^{b-1}\log\left(1+
                             \frac{4k^2\delta_*^2}{\Gamma_{k,M}}\right).
                                                                    \tag{QD.13}
\]
Here \(\Gamma_{k,M}>0\) because every \(a_{\alpha_j+1}>0\).
This is the explicit accumulated determinant consequence of the
already proved quartet operator estimate (AP.17), whereas
(QD.8)--(QD.12) additionally use the original derivative energy
and its stronger operator-norm cost.  Neither chain asserts an
upper asymptotic estimate for those arithmetic quantities.

\subsection{Exact energy--volume equality for the original one-variable layer}

\begin{theorem}[One-variable arithmetic equality]
For \(k=1\), at every admitted original degree \(M\),
\[
 \boxed{\zeta_M=\chi_M,\qquad
 \epsilon_M^2=\frac{\lambda_M}{1+\lambda_M}\chi_M
                    =(1-\pi_M)\chi_M.}                    \tag{QD.14}
\]
These equalities include \(F=0\), \(E_+=0\), and
\(\delta_*=0\).  Whenever \(\chi_M>0\), they give the
exact original determinant identity
\[
 \boxed{\log\frac{\det G_M}{\det G_{M+1}}
     =-\log\left(1-\frac{\epsilon_M^2}{\chi_M}\right),
 \qquad 0\leq\epsilon_M^2<\chi_M.}                        \tag{QD.15}
\]
\end{theorem}
\begin{proof}
For \(k=1\), (QD.1) has \(r=1\) at every \(M\).
The actual graph isometry \(J_b:\mathbb C\to\mathcal E_M\)
therefore proves that this original relation layer is
one-dimensional.  Let \(e=J_b1\), so \(\|e\|=1\).
There are unique row maps \(y,c:\mathbb C^d\to\mathbb C\)
with \(\widehat Y=e y\) and \(\widehat C=e c\).
Their actual cross-pairing is \(\widehat Y^*\widehat C=y^*c\).
Its norm is \(\|y\|\|c\|\): the upper bound is
submultiplicativity, and if both rows are nonzero, evaluating
on the unit vector \(c^*/\|c\|\) attains it.  If either
row is zero the claimed equality is zero on both sides.
The positive matrix \(c^*c\) has its only possible
positive eigenvalue \(\|c\|^2\); thus its largest
eigenvalue and trace agree, including \(c=0\).
Equations (QD.8)--(QD.9) now prove
\(\epsilon_M^2=\|\widehat Y\|^2\chi_M
=\lambda_M\chi_M/(1+\lambda_M)\) and \(\zeta_M=\chi_M\).

The matrix \(U\) has one column, so \(UU^*\) has rank
at most one.  Its determinant product consequently gives
\(\pi_M=(1+\lambda_M)^{-1}\), including \(U=0\).
This proves the last equality in (QD.14).  If \(\chi_M>0\),
division gives \(1-\epsilon_M^2/\chi_M=\pi_M>0\),
and applying the logarithm proves (QD.15).
If \(\chi_M=0\), one retains (QD.14); it sets
\(\epsilon_M=0\) and imposes no additional value on
\(\pi_M\).  In particular the possible contraction from
\(F\) remains present in the zero derivative-cost case.
\end{proof}

The equality (QD.14) is proved for the actual one-variable
arithmetic source and its original one-dimensional relation
layer.  Thus the coefficient one in (QD.8) is an exact
source identity throughout this family, at all nonzero or
zero frontier ranks; no auxiliary model is required to test it.

```
