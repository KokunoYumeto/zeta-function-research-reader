# Independent proof of RCX30–32, including the noncommutative fourth jet

Date: 2026-09-13. Source read: `WORK/residue_constituent_extension_20260913.tex`, RCX27 and RCX30–32. No checker or symbolic computation program was executed for this proof. The source and the sealed replay directory were not edited. The matrix products below retain their indicated order.

## 1. Period derivatives and actual Taylor coefficients

Let \(E=\mathbb C^q\), let \(A,R\in\operatorname{End}_{\mathbb C}(E)\), and fix the original scalar \(u\in\mathbb C^\times\). Write \(A_t=A+tR\). Let the original holomorphic invertible period matrix satisfy

\[
\Pi'(t)=-\Pi(t)A_t/u.
\]

Define endomorphisms \(Q_0=\operatorname{id}_E\) and \(Q_{n+1}=Q_n'-A_tQ_n/u\). If \(\Pi^{(n)}=\Pi Q_n\), the product rule gives

\[
\Pi^{(n+1)}=\Pi'Q_n+\Pi Q_n'
=\Pi\bigl(Q_n'-A_tQ_n/u\bigr)=\Pi Q_{n+1}.
\]

The identity starts at \(n=0\), so induction proves it for every \(n\geq0\). In particular,

\[
\begin{aligned}
Q_1&=-A_t/u,\\
Q_2&=A_t^2/u^2-R/u,\\
Q_3&=-A_t^3/u^3+(RA_t+2A_tR)/u^2,\\
Q_4&=A_t^4/u^4
-\bigl(RA_t^2+2A_tRA_t+3A_t^2R\bigr)/u^3
+3R^2/u^2.
\end{aligned}
\]

Here \(Q_2'=(RA_t+A_tR)/u^2\), while \(-A_tQ_2/u=-A_t^3/u^3+A_tR/u^2\), proving the displayed \(Q_3\). For the fourth derivative the two contributions are exactly

\[
\begin{aligned}
Q_3'&=-\bigl(RA_t^2+A_tRA_t+A_t^2R\bigr)/u^3+3R^2/u^2,\\
-A_tQ_3/u&=A_t^4/u^4-\bigl(A_tRA_t+2A_t^2R\bigr)/u^3.
\end{aligned}
\]

Their sum proves \(Q_4\), including its coefficient \(3\) of \(R^2\).

Now define the actual Taylor coefficients \(B_n\) by

\[
\Pi(t)=\sum_{n\geq0}B_nt^n,\qquad B_n=\Pi^{(n)}(0)/n!,
\qquad B_{-1}=0.
\]

Thus \(B_0=\Pi(0)\); it has not been replaced by an identity matrix. Multiplication of this convergent series by the degree-one polynomial \(A+tR\), followed by coefficient comparison in the period equation, gives

\[
\boxed{(n+1)B_{n+1}=-(B_nA+B_{n-1}R)/u\quad(n\geq0).}
\]

Consequently the actual coefficients through degree four are

\[
\begin{aligned}
B_1&=-\Pi(0)A/u,\\
B_2&=\Pi(0)\left(A^2/(2u^2)-R/(2u)\right),\\
B_3&=\Pi(0)\left(-A^3/(6u^3)+(RA+2AR)/(6u^2)\right),\\
B_4&=\Pi(0)\left(A^4/(24u^4)
-(RA^2+2ARA+3A^2R)/(24u^3)+R^2/(8u^2)\right).
\end{aligned}
\]

These equal \(\Pi(0)Q_n(0)/n!\), as the derivative proof already requires. More explicitly, differentiating the original equation \(n\) times gives, for \(n\geq1\),

\[
\Pi^{(n+1)}=-\bigl(\Pi^{(n)}A_t+n\Pi^{(n-1)}R\bigr)/u,
\]

because the second and higher derivatives of \(A_t\) vanish. Left multiplication by \(\Pi(t)^{-1}\) proves the exact second expression

\[
Q_{n+1}=-(Q_nA_t+nQ_{n-1}R)/u.
\]

It is consistent with the first recursion; their equality also gives

\[
Q_n'=(A_tQ_n-Q_nA_t-nQ_{n-1}R)/u.
\]

These identities explain precisely why the differential recursion has \(A_tQ_n\), whereas the Taylor recursion has \(B_nA\). Neither change of order is an assumption of commutativity.

## 2. Ordered compositions give the fourth trace-log derivative

Let \(\iota:F\hookrightarrow E\) denote the inclusion written \(I\) in the source. Keep \(H_0=\Pi(0)^*\Pi(0)\), and define

\[
K(t)=\iota^*\Pi(0)^*\Pi(t)\iota,\qquad
K_0=\iota^*H_0\iota>0,\qquad
D_n=K_0^{-1}\iota^*H_0Q_n(0)\iota.
\]

Here \(K(t),D_n\in\operatorname{End}_{\mathbb C}(F)\), and \(K_0\) is invertible. The exact Taylor expansion is

\[
K_0^{-1}K(t)=\operatorname{id}_F+Z(t),\qquad
Z(t)=\sum_{n=1}^4D_nt^n/n!+O(t^5).
\]

Choose the local determinant logarithm \(\phi(t)=\log\det K(t)\) with \(\phi(0)=\log\det K_0\). The following argument proves the trace-log identity without commuting any factors. On a sufficiently small disc, \(\|Z(t)\|<1\) in a submultiplicative matrix norm. The series

\[
f(t)=\sum_{m\geq1}\frac{(-1)^{m+1}}m\operatorname{Tr}(Z(t)^m)
\]

and its differentiated series converge locally uniformly there. The product rule and cyclic trace give

\[
\frac d{dt}\operatorname{Tr}(Z^m)
=\sum_{j=0}^{m-1}\operatorname{Tr}(Z^jZ'Z^{m-1-j})
=m\operatorname{Tr}(Z^{m-1}Z').
\]

Therefore \(f'=\operatorname{Tr}((\operatorname{id}_F+Z)^{-1}Z')\). Determinant multilinearity gives

\[
\det(M+hM')=\det M\bigl(1+h\operatorname{Tr}(M^{-1}M')+O(h^2)\bigr)
\]

for invertible \(M\), since in the coefficient of \(h\) in \(\det(\operatorname{id}_F+hN)\) the only surviving terms are the diagonal entries of \(N\). Applying this formula to \(M=K_0^{-1}K\) proves \(\phi'=f'\). Their constants satisfy \(f(0)=0\), so

\[
\phi(t)-\phi(0)=f(t).
\]

The ordered compositions of \(4\) now give all terms. They are \((4)\) at length one; \((1,3),(2,2),(3,1)\) at length two; \((1,1,2),(1,2,1),(2,1,1)\) at length three; and \((1,1,1,1)\) at length four. Lengths greater than four have degree at least five. Thus

\[
\begin{aligned}
[t^4]\operatorname{Tr}Z&=\operatorname{Tr}(D_4)/24,\\
[t^4]\bigl(-\operatorname{Tr}(Z^2)/2\bigr)
&=-\tfrac12\operatorname{Tr}\left((D_1D_3+D_3D_1)/6+D_2^2/4\right),\\
[t^4]\bigl(\operatorname{Tr}(Z^3)/3\bigr)
&=\tfrac16\operatorname{Tr}(D_1^2D_2+D_1D_2D_1+D_2D_1^2),\\
[t^4]\bigl(-\operatorname{Tr}(Z^4)/4\bigr)
&=-\operatorname{Tr}(D_1^4)/4.
\end{aligned}
\]

Multiplication by \(4!=24\) gives the unsymmetrized expression

\[
\phi^{(4)}(0)=\operatorname{Tr}\left(
D_4-2(D_1D_3+D_3D_1)-3D_2^2
+4(D_1^2D_2+D_1D_2D_1+D_2D_1^2)-6D_1^4\right).
\]

Finally, cyclic trace equates the two traces involving \(D_1,D_3\), and equates the three traces involving two copies of \(D_1\) and one of \(D_2\). It proves exactly

\[
\boxed{\phi^{(4)}(0)=\operatorname{Tr}\left(
D_4-4D_1D_3-3D_2^2+12D_1^2D_2-6D_1^4\right).}
\]

This is RCX32. The consolidation is an equality after taking trace, with no asserted equality between the corresponding untraced matrix products.

## 3. Exact evaluation for the supplied fixture

Retain \(\chi(S)=S^3+2S\), coefficient basis \((1,S,S^2)\), \(F=\operatorname{span}(S,S^2)\), and

\[
A=\begin{pmatrix}0&0&0\\1&0&-2\\0&1&0\end{pmatrix},\quad
R=e_0e_2^T,\quad
B=\begin{pmatrix}1&(1+i)/2&(2-i)/3\\0&1&(1+2i)/3\\0&0&1\end{pmatrix},\quad
H_0=B^*B,\quad u=3/2.
\]

The matrix \(B\) here is the supplied fixed matrix; the indexed \(B_n\) above are actual Taylor coefficients. Let \(\iota=[e_1,e_2]\), let \(f_0,f_1\) be this ordered basis of \(F\), and put

\[
J=\begin{pmatrix}0&-2\\1&0\end{pmatrix},\quad
L=(0,1),\quad \varepsilon=(1,0),\quad \kappa=1/u=2/3.
\]

In particular \(A\iota=\iota J\), \(R\iota=e_0L\), \(Ae_0=e_1\), \(A^2e_0=e_2\), \(R^2=0\), and \(J^2=-2\operatorname{id}_F\). The noncommutativity is present: \(AR=e_1e_2^T\), whereas \(RA=e_0e_1^T\). Direct multiplication gives

\[
H_0=\begin{pmatrix}
1&(1+i)/2&(2-i)/3\\
(1-i)/2&3/2&(3+i)/6\\
(2+i)/3&(3-i)/6&19/9
\end{pmatrix},\quad
K_0=\begin{pmatrix}3/2&(3+i)/6\\(3-i)/6&19/9\end{pmatrix},
\]

\[
\det K_0=26/9,\qquad
K_0^{-1}=\begin{pmatrix}
19/26&-(9+3i)/52\\-(9-3i)/52&27/52
\end{pmatrix},\qquad
v=K_0^{-1}\iota^*H_0e_0
=\begin{pmatrix}(7-12i)/26\\(15+15i)/52\end{pmatrix}.
\]

These formulas retain the full supplied Hermitian form. Since \(K_0^{-1}\iota^*H_0\iota=\operatorname{id}_F\), substitution in the proved \(Q_n\) expressions gives

\[
\begin{aligned}
D_1&=-\kappa J,\\
D_2&=-2\kappa^2\operatorname{id}_F-\kappa vL,\\
D_3&=2\kappa^3J+\kappa^2(v\varepsilon+2f_0L),\\
D_4&=4\kappa^4\operatorname{id}_F-\kappa^3(-2vL+2f_0\varepsilon+3f_1L).
\end{aligned}
\]

For the last line, the three ordered words in \(Q_4\) respectively map to \(-2vL\), \(f_0\varepsilon\), and \(f_1L\), before their coefficients \(1,2,3\) are applied. Put \(b=Lv=(15+15i)/52\). The rank-one identity \(\operatorname{Tr}(xy)=yx\) for a column \(x\) and row \(y\), together with \(J^2=-2\operatorname{id}_F\), gives the full trace evaluation

\[
\begin{aligned}
\operatorname{Tr}D_4&=8\kappa^4+2\kappa^3b-5\kappa^3,\\
\operatorname{Tr}(D_1D_3)&=8\kappa^4+2\kappa^3b-2\kappa^3,\\
\operatorname{Tr}(D_2^2)&=8\kappa^4+4\kappa^3b+\kappa^2b^2,\\
\operatorname{Tr}(D_1^2D_2)&=8\kappa^4+2\kappa^3b,\\
\operatorname{Tr}(D_1^4)&=8\kappa^4.
\end{aligned}
\]

For example, the second line uses \(\varepsilon Jv=-2b\) and \(LJf_0=1\); the third uses \((vL)^2=bvL\). These contractions prove the displayed traces without exchanging matrix factors. In RCX32 their \(\kappa^4\) contributions have total coefficient \(8-32-24+96-48=0\), and the retained remaining terms are

\[
\phi^{(4)}(0)=3\kappa^3+6\kappa^3b-3\kappa^2b^2
=\frac89+\frac{20+20i}{39}-\frac{75i}{338}
=\boxed{\frac{164}{117}+\frac{295}{1014}i}.
\]

No discrepancy was found in RCX30–32. This fixture value is a hand-derived prediction for the parent's independent executable comparison, not an execution claim.
