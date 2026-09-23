# The original three-point fibre, the prime-zero endpoints, and the heat sign change

This calculation answers the specific comparison between the target $(-1/4,0,0)$ of the original polynomial map and the pole pairing at $s=0,1$. It proves an isomorphism preserving the specified involution and trace, retains the third inverse point and the infinitesimal at infinity, and computes the exact change to the completed zeta function when its endpoint factor is moved. Positivity proved here concerns these finite trace forms. The complete zeta-zero form is retained in the completion calculation.

The original polynomial and three points are [Tao, displayed formula (1) and the following equalities](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/). Earlier programme proofs are [the complete inverse chart, `eq:retained-cubic`, `eq:retained-inverse`, and `eq:retained-heat`](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/ac168d55cbb400a6c8926a00d67909ba65646ac5/satellites/23_source_mechanism_transfer.tex#L45), [the original heat trajectories](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/ac168d55cbb400a6c8926a00d67909ba65646ac5/satellites/26_incompressible_fibre_heat.tex#L389), and [EFI7–EFI15, including the projective graph and dual-number fibre](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/ESCAPING_FIBRE_INFINITESIMAL_DERIVATION.md#L89). The complete arguments needed for this comparison follow.

## 1. Original coordinates and the entire target line

Write the third source coordinate as $W$; this is the identity renaming of the $w$ in the cited source, to distinguish it from quotient generators. The original map is
\[
\begin{aligned}
F_1&=(1+xy)^3W+y^2(1+xy)(4+3xy),\\
F_2&=y+3x(1+xy)^2W+3xy^2(4+3xy),\\
F_3&=2x-3x^2y-x^3W.
\end{aligned}\tag{HEB1}
\]
Its target coordinates remain $(a,b,c)$. On $b=c=0$, the complete inverse curve has the scheme decomposition
\[
F^{-1}\{(a,0,0):a\in\mathbb C\}
\simeq\operatorname{Spec}\mathbb C[a]\ \sqcup\ 
\operatorname{Spec}\mathbb C[r,r^{-1}],
\tag{HEB2}
\]
with maps to the target respectively $a\mapsto a$ and $a\mapsto-r^2$. The source coordinates on the two components are
\[
(x,y,W)=(0,0,a),\qquad
(x,y,W)=\left(-\frac1{2r},3r,26r^2\right).
\tag{HEB3}
\]

**Proof.** Put $K=2-3xy-x^2W$. Then $F_3=xK$ and
$K+x(3y+xW)=2$. In the coordinate ring defined by $F_1-a,F_2$, the ideals $(x)$ and $(K)$ are comaximal. Their intersection is their product: if $v\in(x)\cap(K)$, multiply $v$ by a representation $1=j_x+j_K$ with $j_x\in(x)$ and $j_K\in(K)$; each summand is in $(xK)$. The converse inclusion is immediate. The Chinese remainder map therefore splits the quotient by $F_3$ into these two components, with no lost scheme structure.

On $x=0$, $F_2=y$ and $F_1=W+4y^2$, giving the first component. On $K=0$, $x$ is a unit with inverse $(3y+xW)/2$. Set $\alpha=1/x$ and $r=y+1/x$. Solving $F_3=0$ gives
$W=5\alpha^2-3r\alpha$. Direct substitution gives
\[
F_2=4r+2\alpha,\qquad F_1=r^2+r\alpha.
\tag{HEB4}
\]
Consequently $\alpha=-2r$, $a=-r^2$, and (HEB3) follows. Conversely (HEB3) satisfies all three target equations and recovers $r=y+1/x$. These mutually inverse coordinate substitutions prove (HEB2). Explicit component idempotents are $K/2$ for the finite component and $(3xy+x^2W)/2$ for the escaping component. Their sum is one and their product is zero. $\square$

At $a=-1/4$, the two roots are $r=-1/2,+1/2$. The complete fibre is precisely
\[
\begin{array}{c|c}
\text{component coordinate}&(x,y,W)\\\hline
\text{finite}&(0,0,-1/4)\\
r=-1/2&(1,-3/2,13/2)\\
r=+1/2&(-1,3/2,13/2).
\end{array}\tag{HEB5}
\]
Thus the number $1/4$ in the root relation is exactly the negative of the original target coordinate, rather than a new choice of scale.

This target is not the only noninjective one. Every $a\ne0$ has the separate finite point and two distinct complex points in (HEB3). For example at $a=+1/4$ these are
\[
(0,0,1/4),\qquad(i,3i/2,-13/2),\qquad(-i,-3i/2,-13/2).
\tag{HEB6}
\]
Direct substitution or (HEB3) proves all three images are $(1/4,0,0)$. The two nonreal points cannot be dropped when discussing complex injectivity.

## 2. Compactification and the involution

In source projective coordinates $[X:Y:Z:T]$, whose affine coordinates are $(x,y,W)=(X/T,Y/T,Z/T)$, the escaping graph extends to
\[
r\longmapsto\bigl([1:-6r^2:-52r^3:-2r],\ a=-r^2\bigr).
\tag{HEB7}
\]
The displayed graph is closed in $\mathbb P^3\times\mathbb A^1$: it is the scheme defined by $Y=6aX$, $Z=-26aT$, and $T^2+4aX^2=0$. These equations have no projective point with $X=0$, because they would successively force $Y=T=Z=0$. In the chart $X=1$ its coordinate ring is $\mathbb C[a,T]/(T^2+4a)$, and the mutually inverse substitutions $r=-T/2$, $a=-r^2$ identify this ring with $\mathbb C[r]$. Substitution recovers exactly all four coordinates in (HEB7), proving the asserted scheme equality. The coordinate $T/X=-2r$ is its inverse coordinate, so the graph is exactly the affine $r$-line. Its fibre at $a=0$ is the length-two algebra $\mathbb C[r]/(r^2)$ supported at $[1:0:0:0]$. The finite component remains $[0:0:a:1]$, disjoint from (HEB7). Hence the compactified inverse graph over the target line is finite flat of rank three, with coordinate algebra
\[
\mathcal C=\mathbb C[a]\times\mathbb C[a,r]/(r^2+a).
\tag{HEB8}
\]
Freeness of the second factor in the basis $1,r$ follows by division by its monic relation. The original affine inverse curve (HEB2) is obtained by removing the point $r=0$ from the second component, not by quotienting away its infinitesimal.

The original source involution and its target map are
\[
R(x,y,W)=(-x,-y,W),\qquad
F\circ R=(F_1,-F_2,-F_3).
\tag{HEB9}
\]
Every term of (HEB1) verifies this equality: $xy,y^2,x^2W$ remain fixed and the indicated odd factors change sign. Thus $R$ preserves our target line, fixes the finite component, and sends $r=y+1/x$ to $-r$. For real $a$, compose this algebraic reflection with coefficient conjugation to obtain
\[
r^\#=-r,\qquad z^\#=\bar z\quad(z\in\mathbb C).
\tag{HEB10}
\]
The relation $r^2+a$ is stable and $\#^2=1$, so this is a well-defined conjugate-linear ring involution. It is not ordinary coefficient conjugation with $r$ fixed; (HEB9) is the exact map connecting the two.

## 3. An isometry with the actual endpoint pairing

For a compactly supported smooth complex test $f$ on $\mathbb R$, retain
\[
\widehat f(z)=\int_{\mathbb R}f(v)e^{-ivz}\,dv,
\qquad M_f(s)=\widehat f\bigl((s-1/2)/i\bigr).
\tag{HEB11}
\]
Set $A=M_f(0)=\widehat f(i/2)$ and $B=M_f(1)=\widehat f(-i/2)$. The endpoint contribution is
\[
W_0(f,g)=\overline A_f B_g+\overline B_f A_g.
\tag{HEB12}
\]
Use uppercase $A,B$ here to avoid confusion with the original target $a,b,c$.

At the exact target $a=-1/4$, there are mutually inverse algebra maps
\[
\begin{aligned}
\mathbb C[s]/(s(s-1))&\longrightarrow
\mathbb C[r]/(r^2-1/4),&s&\longmapsto1/2+r,\\
\mathbb C[r]/(r^2-1/4)&\longrightarrow
\mathbb C[s]/(s(s-1)),&r&\longmapsto s-1/2.
\end{aligned}\tag{HEB13}
\]
They respect the relations by expansion and are inverse on their generators. Under (HEB13), $s^\#=1-s$. Evaluation at $r=-1/2,+1/2$ maps the second algebra isomorphically to $\mathbb C^2$, with inverse
\[
(A,B)\longmapsto p_{A,B}=(A+B)/2+(B-A)r.
\tag{HEB14}
\]
Both evaluations and the coefficient formula prove the inverse assertion. The involution acts on endpoint values as $(A,B)^\#=(\overline B,\overline A)$.

For $E_a=\mathbb C[r]/(r^2+a)$, define the regular trace by the trace of its multiplication operator. In the basis $(1,r)$,
\[
L_r=\begin{pmatrix}0&-a\\1&0\end{pmatrix},\qquad
\operatorname{Tr}_{E_a}(c+dr)=2c.
\tag{HEB15}
\]
Multiplying $(\bar c-\bar d r)(e+kr)$ gives scalar coefficient $\bar ce+a\bar dk$, and hence
\[
q_a(c+dr,e+kr):=\operatorname{Tr}_{E_a}((c+dr)^\#(e+kr))
=2\bar ce+2a\bar dk.
\tag{HEB16}
\]
In particular substitution of (HEB14) gives
\[
q_{-1/4}(p_{A,B},p_{A,B})
=\tfrac12|A+B|^2-\tfrac12|A-B|^2
=2\operatorname{Re}(A\overline B).
\tag{HEB17}
\]
Polarization, or the same multiplication with two inputs, proves equality with (HEB12) in both slots. These are isomorphisms of algebras with involution and isometries of the trace pairings. They do not identify the separate third component with either endpoint. On the whole algebra (HEB8) the form is
\[
q^{\rm full}_a(v,c+dr)=|v|^2+2|c|^2+2a|d|^2.
\tag{HEB18}
\]

## 4. The original heat clock crosses the sign boundary

Retain the original forward heat parameter $h$, with its original speed and initial target:
\[
a(h)=-1/4+2h,\qquad b=c=0,\qquad
r^2=1/4-2h.
\tag{HEB19}
\]
The original cubic on this line is $P=-2r^2-2a$; it satisfies $\partial_hP=-4=\partial_r^2P$. Thus (HEB19) is the original coefficient heat flow. The exact pulled-back form in the free basis $(1,r)$ is
\[
G_h=\begin{pmatrix}2&0\\0&4h-1/2\end{pmatrix},
\qquad q_h(r,r)=4h-1/2.
\tag{HEB20}
\]
It has one positive and one negative direction for $h<1/8$; at $h=1/8$ it has one positive direction and radical $\mathbb C r$; for $h>1/8$ it is positive definite. This follows directly from the two real diagonal entries. In the full rank-three algebra (HEB18), the finite point adds a positive direction in every case.

At the collision $r\ne0$ as an algebra element and $r^2=0$: division by the monic polynomial gives independent classes $1,r$. It is the trace pairing of this nonzero infinitesimal that vanishes. Under the supported embedding into $G(E_0)$ its square is the supported zero $e$, distinct from the global unsupported zero $\tau$. No positivity conclusion follows from identifying either of these zeros with the other.

The two spectral coordinates obtained from (HEB13) throughout the family are
\[
s_\pm(h)=1/2\pm\sqrt{1/4-2h}.
\tag{HEB21}
\]
At $h=0$ they are the actual endpoints $0,1$. At $h=1/8$ they coincide at $1/2$ with multiplicity two. At $h>1/8$ they lie on the critical line, at $1/2\pm i\sqrt{2h-1/4}$. In the original source, however, the corresponding $x,y$ have become nonreal; the original real trajectories escape to infinity at the collision. Formula (HEB7) gives the continuation as a complex algebraic graph, not a finite continuation in $\mathbb R^3$.

There is also an operator version with the metric retained. Put $S=I/2+L_r$ and $D=(S-I/2)/i=-iL_r$. Direct multiplication gives
\[
L_r^*G_h=-G_hL_r,\qquad D^*G_h=G_hD.
\tag{HEB22}
\]
For $h>1/8$, $G_h$ is positive definite, so if $Dv=\lambda v$ with $v\ne0$, the equality of the two pairings gives $\lambda=\bar\lambda$. Thus $S$ has real part $1/2$ on every eigenvalue. At the collision, $D$ is a nonzero nilpotent; it cannot be self-adjoint for any positive definite metric, because that would give $\|Dv\|^2=\langle v,D^2v\rangle=0$ for every $v$. Its specified semidefinite trace metric retains exactly the radical already computed. This is a complete finite-dimensional positivity and spectral calculation.

## 5. Moving this factor in the completed zeta function

Define
\[
q_h(s)=s(s-1)+2h,\quad q_0=s(s-1),\quad
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad
2\xi(s)=q_0(s)\Lambda(s).
\tag{HEB23}
\]
The entire endpoint test $M_f$ has a unique class modulo $q_h$: for two distinct roots use their two values, and at a double root use its value and first derivative. Existence follows by degree-one interpolation; uniqueness follows because a polynomial of degree at most one with the two required vanishing conditions is zero. The involution is the same $s^\#=1-s$ with conjugate coefficients. Its trace pairing is
\[
P_h(f,g)=\sum_{q_h(\rho)=0}^{\rm mult}
\overline{M_f(1-\bar\rho)}M_g(\rho).
\tag{HEB24}
\]
This equals (HEB16) for those interpolating classes: multiplication matrices at distinct roots are diagonalized by evaluation, and at a double root their trace is twice their scalar coefficient. Therefore $P_0=W_0$, $P_{1/8}(f,f)=2|M_f(1/2)|^2$, and
\[
P_h(f,f)=|M_f(s_+(h))|^2+|M_f(s_-(h))|^2\ge0
\quad(h>1/8).
\tag{HEB25}
\]

An exact realization of this moving denominator is
\[
\Lambda_h(s)=\frac{2\xi(s)}{q_h(s)}
=\Lambda(s)\frac{q_0(s)}{q_h(s)}.
\tag{HEB26}
\]
As identities of meromorphic functions and signed divisors,
\[
\frac{\Lambda_h'}{\Lambda_h}
=\frac{\Lambda'}{\Lambda}+\frac{q_0'}{q_0}-\frac{q_h'}{q_h},
\qquad
\operatorname{div}\Lambda_h=\operatorname{div}\xi-\operatorname{div}q_h.
\tag{HEB27}
\]
Logarithmic differentiation proves the first identity; factoring at each point proves the second, including cancellations when a zero of $q_h$ coincides with a zero of $\xi$. One must keep those cancellations; at such a parameter, the factor trace (HEB24) is not a list of uncancelled poles of $\Lambda_h$.

Here is the exact effect on Weil's formula. Write its original decomposition as
\[
W(f,g)=P_0(f,g)+\mathcal A(f,g)-\mathcal P(f,g),
\tag{HEB28}
\]
where $\mathcal A$ is the original archimedean term and $\mathcal P$ the original rational-prime term. Define the archimedean term for the modified completion by
\[
\mathcal A_h=\mathcal A+P_0-P_h.
\tag{HEB29}
\]
Then exactly
\[
W=P_h+\mathcal A_h-\mathcal P.
\tag{HEB30}
\]
This is both an algebraic identity of forms and the residue identity supplied by the rational logarithmic correction in (HEB27). Indeed $q_j'/q_j$ has residue equal to the root multiplicity at every root of $q_j$, so pairing these finite divisors with $M_f^\#M_g$ gives $P_0-P_h$. The remaining zeta factor and its prime logarithmic derivative are unchanged. Thus the sign change of the endpoint receiver can be made exact while preserving the complete original zero form $W$, but it is accompanied by the equally exact correction (HEB29). Positivity of (HEB25) alone is not positivity of the complete form (HEB30).

For clarity, $\Lambda_h$ in (HEB26) is a rationally modified completion of the original $\zeta$. It is not the Hurwitz family $\zeta(s,1+t)$ and it is not the de Bruijn–Newman heat evolution of $\xi$. Each has its own proved map and parameter. Replacing any of them by (HEB26) without its correction would change the calculation.

## 6. The integral coefficient before quadratic base change

Before choosing the heat clock, the integral algebra is
\[
E_{\mathbb Z}=\mathbb Z[u,r]/(r^2-u),\qquad
\sigma(r)=-r,\quad\sigma(u)=u.
\tag{HEB31}
\]
The geometric substitutions are $u=-a$ and, over $\mathbb Z[1/2]$, $u=1/4-2h$. The ramified coefficient family used for the reflected analytic pair is the exact base change $u\mapsto d^2$, $r\mapsto w$. The image has $u\ge0$ when $d$ is real. The original heat line instead has access to both signs of $u$. These are different maps from the same coefficient space; neither map is omitted.

For the integral Frobenius lift $\Phi_p(u)=u^p$, $\Phi_p(r)=r^p$, coefficient integers fixed, the relation is preserved and the reduction modulo $p$ is Frobenius. The ring is torsionfree, so $\delta_p(x)=(\Phi_p(x)-x^p)/p$ is defined. Direct computation on the generator at $p=2$ gives
\[
(\sigma\Phi_2-\Phi_2\sigma)(r)=2u,
\qquad(\sigma\delta_2-\delta_2\sigma)(r)=u,
\qquad q_u(r,r)=-2u.
\tag{HEB32}
\]
Thus the divided arithmetic defect is the same coefficient whose sign controls the real reflected form, through explicit integral and complex realizations. In the collision quotient $u=0$, $r$ survives with $r^2=0$. There is no claim that a $p$-adic coefficient has an intrinsic real sign, or that quotienting by $u$ chooses the positive real half-line. The complete quotient, conormal and prism maps are calculated in WRF; (HEB31)–(HEB32) give the exact common source needed here.

The accompanying `check_endpoint_heat_bridge.py` verifies the original three images, the inverse chart, source reflection, matrix isometry, and rational logarithmic correction using exact rational symbolic arithmetic. Its finite verification scope is recorded in `ENDPOINT_HEAT_BRIDGE_CHECKS.json`. All arguments above are supplied independently of that check.


The earlier first-order vanishing in the ramified observed family also has an exact clock map. Under $u=d^2$ and $u=1/4-2h$,
\[
h=\frac18-\frac{d^2}{2},\qquad r^2=d^2,\qquad q(r,r)=-2d^2.
\tag{HEB32a}
\]
Thus modulo $d^2$ the algebra is the constant dual-number algebra and this paired value vanishes, while its coefficient of $d^2$ is exactly $-2$. The first derivative of the displayed heat clock in $d$ is zero at zero and its second derivative is $-1$. This is why first-order vanishing in $d$ does not itself choose the positive side of the heat clock: real $d$ maps to $h\le1/8$. The original real heat parameter and this quadratic pullback are both retained through the displayed polynomial map.

## 7. An admissible test through the vanishing infinitesimal and positive quarter

The sign comparison can be evaluated on an actual compactly supported smooth test. Let
\[
\psi(v)=C\begin{cases}\exp\bigl(-1/(1-v^2)\bigr),&|v|<1,\\0,&|v|\ge1,\end{cases}
\qquad \int_{\mathbb R}\psi(v)\,dv=1,\qquad f=\psi'.
\tag{HEB33}
\]
The constant $C$ is the reciprocal of the positive finite integral of the displayed function. The function is even, nonnegative, smooth and compactly supported: each one-sided derivative at $|v|=1$ is an exponential of a negative reciprocal times a polynomial in reciprocal powers, hence tends to zero. This last assertion follows from $t^{-m}e^{-1/t}\to0$ for every nonnegative integer $m$ as $t\downarrow0$, proved by the exponential series bound $e^{1/t}\ge t^{-(m+1)}/(m+1)!$. Thus $f$ is an admissible real odd test in (HEB11).

Define the entire function $B(t)=\int\psi(v)e^{-tv}\,dv$. Entirety and differentiation under the integral follow uniformly on every compact set of $t$ from $|v|\le1$. Integration by parts, with zero boundary values, gives
\[
M_f(s)=(s-1/2)B(s-1/2),\qquad B(-t)=B(t),\qquad B(0)=1.
\tag{HEB34}
\]
The first equality uses the exact Fourier convention (HEB11); the second follows by $v\mapsto-v$. In particular $M_f(1/2)=0$ and $M_f'(1/2)=1$. Hence its class at the collision is precisely the nonzero class $r$ in $\mathbb C[r]/r^2$. Its value vanishes, its first derivative survives, and its reflected regular trace pairing is zero, by (HEB16).

For every real $a$, introduce the entire coefficient function
\[
b(a)=\sum_{k=0}^{\infty}\frac{(-a)^k}{(2k)!}\int\psi(v)v^{2k}\,dv.
\tag{HEB35}
\]
The moments have absolute value at most one, so the series converges uniformly on bounded subsets of $a$. The even series of $B$ and the relation $r^2=-a$ give exactly $[M_f]=b(a)r$ in $E_a$, including its double-root class at zero. Equivalently $b(a)=\int\psi(v)\cos(\sqrt a\,v)\,dv$ for $a\ge0$ and $b(a)=\int\psi(v)\cosh(\sqrt{-a}\,v)\,dv$ for $a\le0$. The exponential series and uniform convergence on $|v|\le1$ prove both formulas, with no choice of complex square root needed.

Put $b_0=b(-1/4)=\int\psi(v)\cosh(v/2)\,dv$ and $b_1=b(1/4)=\int\psi(v)\cos(v/2)\,dv$. Both are strictly positive: the integrands are nonnegative, and $\cos(v/2)\ge\cos(1/2)>0$ on the support. Formula (HEB16) consequently gives the exact values and the actual compensation
\[
\begin{aligned}
P_0(f,f)&=-\tfrac12 b_0^2<0,\\
P_{1/8}(f,f)&=0,\\
P_{1/4}(f,f)&=\tfrac12 b_1^2>0,\\
(\mathcal A_{1/4}-\mathcal A)(f,f)
&=-\tfrac12(b_0^2+b_1^2)<0.
\end{aligned}
\tag{HEB36}
\]
The fourth equality follows from (HEB29), and cancels exactly the gain $P_{1/4}(f,f)-P_0(f,f)$. All values belong to the same admissible test $f$, without replacing it by an arbitrary endpoint vector or a polynomial outside the test space. This proves both the actual sign crossing and its complete explicit-formula compensation. It does not assign a sign to the remaining total $W(f,f)$: that total is unchanged by (HEB30).

