---
title: "Split-Zero: escaping fibres and separated-zeta positivity"
date: "Proofs of 22 September 2026; edition of 23 September 2026"
---

This edition contains the complete eight derivations in the order listed below. Its finite algebra, analytic explicit formulas and exact comparison maps retain their own hypotheses. The source and reading guide follows the proofs.


\clearpage

# The escaping inverse fibre, its infinitesimal boundary, and its trace form

This derivation retains the original polynomial map, its target coordinates, and its heat constants. It computes an actual dual-number fibre at every double collision, the larger boundary at a triple collision, the exact maps under which infinitesimals vanish, and the signatures of the associated finite trace forms. It does not identify these finite trace forms with the classical Weil distribution. No off-critical zero of the Riemann zeta function is asserted.

## Sources actually read

The complete original LaTeX files `tex/satellites/26_incompressible_fibre_heat.tex` and `tex/satellites/23_source_mechanism_transfer.tex` in the local `Zeta-Function-Foundation` repository were read for this calculation. The received source formulas are `eq:ifh-original`, `eq:ifh-det`, `eq:ifh-chart`, `eq:ifh-target-chart`, `eq:ifh-target-flow`, `eq:ifh-triple`, `eq:retained-node-map`, and `eq:retained-arithmetic-extension`. Their original-map provenance is [Tao's displayed map and explanation](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/) and [Speyer's marked-factor discussion](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/), as cited in those programme sources. The full-support definition used below is reproduced in FSR1–FSR7 of [full-support reconstruction proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/FULL_SUPPORT_RECONSTRUCTION_DERIVATION.md); its first 70 lines were read. The results below supply their own algebraic proofs.

The exact read coverage was lines 1–480 of the first file, SHA256
`72058517553FF3A2C35699844FA95BBA9EC695E774E0E3D4CF33CF7B84DA51DD`,
and lines 1–666 of the second file, SHA256
`D8A65C46B78A5ACE521A164AABC99F246908058E36B60C35BCE938D51C020898`.
These are local programme source versions, not author-source archives.

The forward heat time called tau in the source is denoted $h$ here, solely to keep it distinct from the global absorber $\tau_L$. The displacement from a specified collision is $d=h-h_c$. All original spatial and target coordinates are retained.

## 1. Original map and projective inverse chart

Over $\mathbb C$, write
\[
\begin{aligned}
F_1&=(1+xy)^3w+y^2(1+xy)(4+3xy),\\
F_2&=y+3x(1+xy)^2w+3xy^2(4+3xy),\\
F_3&=2x-3x^2y-x^3w.
\end{aligned}
\tag{EFI1}
\]
The target is $(a,b,c)$. Define
\[
P(r)=cr^3-2r^2+br-2a,\qquad
\alpha=\frac{P'(r)}2,\qquad
H(r,\alpha,c)=\left(\frac1\alpha,r-\alpha,
5\alpha^2-3r\alpha-c\alpha^3\right).
\tag{EFI2}
\]
Direct substitution before imposing $P=0$ gives
\[
F\circ H=(r^2+r\alpha-cr^3,\ 4r+2\alpha-3cr^2,\ c).
\tag{EFI3}
\]
Consequently $F_2=b$ is exactly $2\alpha=P'(r)$, and then
$2(F_1-a)=P(r)$. Conversely, from a finite point with $x\ne0$,
recover $\alpha=1/x$ and $r=y+1/x$; solving $F_3=c$
recovers every coordinate of EFI2. This proves that simple roots of $P$
are in bijection with all inverse points with $x\ne0$. No multiple root
supplies a finite point in this chart. On the excluded hyperplane,
\[
F(0,y,w)=(w+4y^2,y,0).
\tag{EFI4}
\]
Thus a separate finite point $(0,b,a-4b^2)$ exists exactly when $c=0$.

Put projective coordinates $[X:Y:W:T]$ on the compactification of the
source, with affine coordinates $(x,y,w)=(X/T,Y/T,W/T)$. Multiplying
the homogeneous representative of EFI2 by $\alpha$ gives the
everywhere defined map
\[
\overline H(r,\alpha,c)=
[1:\alpha(r-\alpha):5\alpha^3-3r\alpha^2-c\alpha^4:\alpha].
\tag{EFI5}
\]
It agrees with the actual inverse point when $\alpha\ne0$. Every
point with $\alpha=0$ maps to
\[
p_\infty=[1:0:0:0].
\tag{EFI6}
\]
This equality of projective points does not identify their infinitesimal
neighbourhoods. Those neighbourhoods are computed below.

## 2. The original two escaping trajectories give exact dual numbers

On the original target line $b=c=0$, the entire root cover is
\[
a=-r^2,\qquad \alpha=-2r,
\qquad (x,y,w)=\left(-\frac1{2r},3r,26r^2\right)\quad(r\ne0).
\tag{EFI7}
\]
These equalities follow by substituting $c=b=0$ in EFI2. In particular,
the projective graph is
\[
(r,a)\longmapsto
\bigl([1:-6r^2:-52r^3:-2r],\ a=-r^2\bigr).
\tag{EFI8}
\]
In the projective chart $X=1$, its coordinate $T/X=-2r$ recovers $r$.
Hence this map identifies the graph closure with the affine $r$-line;
its completed local ring at the escaping point is $\mathbb C[[r]]$.
The base parameter map is exactly
\[
\mathbb C[[a]]\longrightarrow\mathbb C[[r]],\qquad a\longmapsto-r^2.
\tag{EFI9}
\]
The scheme fibre over $a=0$ is therefore
\[
\mathbb C[[r]]/(a)=\mathbb C[r]/(r^2)
\xrightarrow[\sim]{r\mapsto\epsilon}
D:=\mathbb C[\epsilon]/(\epsilon^2).
\tag{EFI10}
\]
The inverse is $\epsilon\mapsto r$. The class $r$ is nonzero because
the two residue classes $1,r$ are linearly independent. Thus dual numbers
arise from the special fibre of the actual inverse map; they have not been
introduced by a resemblance of notation.

The additional finite point of EFI4 is $(0,0,a)$ and survives at $a=0$.
It is a different component of the compactified inverse fibre. The
length-two point EFI10 is supported at infinity, while this extra point
is supported at the finite origin. Keeping both preserves total fibre
length three on this line.

The original forward heat orbit has
\[
a=-\frac14+2h,\qquad r^2=\frac14-2h,
\qquad d=h-\frac18,\qquad r^2=-2d.
\tag{EFI11}
\]
For $h<1/8$, taking $r=\mp\sqrt{1-8h}/2$ in EFI7 recovers exactly
\[
\gamma_\pm(h)=
\left(\pm(1-8h)^{-1/2},
\mp\frac32(1-8h)^{1/2},\frac{13}2(1-8h)\right).
\tag{EFI12}
\]
Thus the dual-number boundary is attached to those same escaping
trajectories with the same time constant.

### The exact cancellation and the retained tangent

For a holomorphic germ $f(r)=\sum_{n\ge0}f_nr^n$ on the graph, the
sheet involution is $\sigma(r)=-r$. The trace is
\[
\operatorname{Tr}(f)=f(r)+f(-r)=2\sum_{n\ge0}f_{2n}r^{2n}.
\tag{EFI13}
\]
This is a map to $\mathbb C[[a]]$ under EFI9. Its kernel is exactly
$r\mathbb C[[a]]$, and the trace divided by two has the even-section
inclusion as a right inverse. This proves exactly what the sheet trace
forgets.

The antisymmetric functional satisfies
\[
\frac{f(r)-f(-r)}{2r}\longrightarrow f_1=f'(0)
\quad\text{as }r\longrightarrow0.
\tag{EFI14}
\]
The equality follows directly from its power series, which equals
$f_1+f_3r^2+f_5r^4+\cdots$. On a germ pulled back from $a=-r^2$, the
numerator is identically zero. On the projective coordinate $T/X=-2r$,
the limit is $-2$. Therefore the retained limit is a nonzero tangent
functional at $p_\infty$, killed by projection to the target. Its
algebra map is precisely EFI10.

This limit does not assign a finite value to the pole $x=-1/(2r)$.
Indeed the two sheet sums and the quadratic moment are
\[
x(r)+x(-r)=0,
\qquad x(r)-x(-r)=-\frac1r,
\qquad x(r)^2+x(-r)^2=\frac1{2r^2}=-\frac1{2a}.
\tag{EFI15}
\]
Thus a first-moment cancellation coexists with a divergent second moment.
The latter is the explicit retained defect in any proposed assertion that
all observables cancel.

## 3. Every double collision in the given heat family

Fix a double root $r_0$ at a target $(a_0,b_0,c_0)$. Put
\[
q_0=3c_0r_0-2\ne0,\qquad t=r-r_0,
\qquad a=a_0+2d,\quad b=b_0+6c_0d,\quad c=c_0.
\tag{EFI16}
\]
The inequality $q_0\ne0$ says exactly that the root has multiplicity
two rather than three, since $P''(r_0)=2q_0$. Taylor expansion of this
cubic is an exact identity, with no omitted remainder:
\[
P=q_0t^2+c_0t^3+2q_0d+6c_0dt.
\tag{EFI17}
\]
In the completed local ring at $(d,t)=(0,0)$, the factor
$2q_0+6c_0t$ is a unit. Hence EFI17 is equivalent to
\[
d=-\frac{t^2(q_0+c_0t)}{2q_0+6c_0t},
\qquad
\alpha=q_0t+\frac32c_0t^2+3c_0d.
\tag{EFI18}
\]
The completed root ring is $\mathbb C[[t]]$ with exactly this base
map. The coefficient of $t$ in $\alpha$ is $q_0\ne0$. A formal
series with a nonzero linear coefficient has a unique inverse series:
its coefficient of degree one is determined by division by $q_0$, and
at every later degree the new unknown enters multiplied by the same
nonzero $q_0$. This recursive argument proves
$\mathbb C[[\alpha]]=\mathbb C[[t]]$.

Since $T/X=\alpha$ is a coordinate of the projective graph, the graph
completion is this same ring. In EFI18 the coefficient multiplying
$t^2$ is a unit, so the special fibre is
\[
\mathbb C[[t]]/(d)=\mathbb C[t]/(t^2).
\tag{EFI19}
\]
The projective tangent has
\[
T/X=q_0t,\qquad Y/X=r_0q_0t,\qquad W/X=0
\quad\text{modulo }t^2.
\tag{EFI20}
\]
This retains the original constants and the actual tangent direction.
For $c_0=0$, one has $q_0=-2$, and EFI18 gives exactly
$d=-t^2/2$, including the quadratic calculation above.

## 4. Triple collision: root fibre and projective graph fibre differ by exact maps

Now fix $c\ne0$ and the triple target
\[
r_* =\frac{2}{3c},\qquad
a_* =\frac{4}{27c^2},\qquad b_* =\frac4{3c}.
\tag{EFI21}
\]
Along its heat orbit $a=a_*+2d, b=b_*+6cd$, put $z=r-r_*$.
The exact equations are
\[
P=c(z^3+6dz),\qquad
\alpha=\frac{3c}{2}z^2+3cd.
\tag{EFI22}
\]
Let $R=\mathbb C[d]$ and
\[
B=R[z]/(z^3+6dz).
\tag{EFI23}
\]
It is free of rank three over $R$, with ordered basis $1,z,z^2$,
by division by the displayed monic cubic. Its completed local ring is
$\widehat B=\mathbb C[[d,z]]/(z^3+6dz)$. Its special root fibre is
\[
B_0=B/(d)=\mathbb C[z]/(z^3).
\tag{EFI24}
\]
This is a length-three infinitesimal, rather than a length-two one.
It has the surjection $B_0\to D, z\mapsto\epsilon$, with kernel
$(z^2)$. It also contains the subalgebra
$\mathbb C[z^2]\cong D$, with $\epsilon\mapsto z^2$.
There is no retraction of this latter inclusion: any homomorphism
$B_0\to D$ sends $z$ to a nilpotent multiple of $\epsilon$, whose
square is zero, whereas a retraction would have to send $z^2$ to
$\epsilon\ne0$.

### The graph closure itself

In the projective chart $X=1$, write
\[
\eta=Y/X=\alpha(r_*+z-\alpha),\qquad
\omega=W/X=5\alpha^3-3(r_*+z)\alpha^2-c\alpha^4.
\tag{EFI25}
\]
The projective graph algebra is the $R$-subalgebra
$A=R[\alpha,\eta,\omega]\subset B$. Define
\[
u=z^2=\frac{2}{3c}(\alpha-3cd),
\qquad
v=dz=-\frac{\eta-r_*\alpha+\alpha^2}{6c}.
\tag{EFI26}
\]
The second equality follows because
$\alpha z=(3c/2)z^3+3cdz=-6cdz$. Thus $u,v\in A$.
Conversely $\alpha=(3c/2)u+3cd$,
$\eta=r_*\alpha-\alpha^2-6cv$, and
\[
\omega=5\alpha^3-3r_*\alpha^2+18c\alpha v-c\alpha^4.
\tag{EFI27}
\]
All projective coordinates therefore belong to $R[u,v]$, proving
$A=R[u,v]$ inside $B$.

Products in this ring satisfy exactly
\[
u^2=-6du,\qquad uv=-6dv,\qquad v^2=d^2u.
\tag{EFI28}
\]
For example $u^2=z^4=-6dz^2$, and the other identities follow in
the same manner. Every word in $u,v$ reduces, by these identities, to
an $R$-linear combination of $1,u,v$. These three elements are
linearly independent in $B$: a relation would have coefficients
$A_0+A_1z^2+A_2dz=0$, and the basis $1,z,z^2$ forces
$A_0=A_1=dA_2=0$; the polynomial ring $R$ has no $d$-torsion.
Hence
\[
A\cong
R[u,v]/(u^2+6du,\ uv+6dv,\ v^2-d^2u),
\qquad A=R\oplus Ru\oplus Rv.
\tag{EFI29}
\]
This proves that the displayed relations are complete.

For $d\ne0$, $z=v/d$, so $A[d^{-1}]=B[d^{-1}]$, which is
the original three-point inverse graph. The algebra $B$ is finite
over $R\subset A$, hence is finite over $A$. The image of its
map to the affine projective-coordinate chart is closed, and its
coordinate algebra is exactly the subalgebra $A$. Equivalently, any
polynomial vanishing on the graph with $d\ne0$ is zero in
$A[d^{-1}]$; since $A$ is $R$-free, it was already zero in $A$.
These two facts prove that EFI29 is the scheme-theoretic graph closure.

Its completion is obtained by replacing $R$ with
$\mathbb C[[d]]$ in EFI29. Its special fibre is
\[
A_0=A/(d)=\mathbb C[u,v]/(u^2,uv,v^2).
\tag{EFI30}
\]
It has two independent square-zero directions. The total graph is
flat of rank three over the $d$-line, as the proved basis shows.
This is the exact scheme in which all three escaping branches converge
at $p_\infty$.

The inclusion $A\hookrightarrow B$ induces
\[
j_0:A_0\longrightarrow B_0,\qquad
u\longmapsto z^2,\quad v\longmapsto0.
\tag{EFI31}
\]
Its kernel is $\mathbb C v$, its image is
$\mathbb C\oplus\mathbb C z^2\cong D$, and its cokernel as a vector
space is $\mathbb C z$. In particular, the vanishing class $v$
is nonzero in the projective special fibre; its vanishing names this
specific morphism, not the absence of an infinitesimal.

The failure of injectivity after specializing has a complete exact
sequence. From the two $R$-bases,
\[
0\longrightarrow A\longrightarrow B\longrightarrow R/(d)
\longrightarrow0,
\tag{EFI32}
\]
where the last map takes the coefficient of $z$ modulo $d$.
Tensoring the elementary resolution
$0\to R\xrightarrow{d}R\to R/(d)\to0$ proves
\[
0\longrightarrow\mathbb C v\longrightarrow A_0
\xrightarrow{j_0}B_0\longrightarrow\mathbb C z\longrightarrow0.
\tag{EFI33}
\]
The first map can be checked without invoking derived notation:
the omitted generator $z\in B/A$ is killed by $d$, and $dz=v\in A$
is its connecting class. This is the precise retained defect of
specialization.

### Each original branch and its poles

The central root has $z=0,\ \alpha=3cd$. Each outer root has
$z^2=-6d,\ \alpha=-6cd$. After the common parameter substitution
$d=-q^2/6$, the three roots are $z=0,q,-q$, and
\[
\alpha_{\rm central}=-\frac c2q^2,
\qquad \alpha_{\rm outer}=cq^2.
\tag{EFI34}
\]
All projective coordinates in EFI25 converge to EFI6, with $T/X$
of order two in $q$. The outer branch distinction first enters
$\alpha z$ in order three. The exact sum and sum of squares of
the original $x$-coordinates are
\[
\sum x_i=\frac1{3cd}+2\left(-\frac1{6cd}\right)=0,
\qquad
\sum x_i^2=\frac1{6c^2d^2}.
\tag{EFI35}
\]
The second expression is a nonzero pole, so cancellation of the sum
does not cancel the family of observables.

## 5. Exact positivity of the finite trace forms

These forms are attached to the root and graph algebras just proved.
They are not identified here with the Weil form. Their value is that
they calculate exactly what trace-vanishing of an infinitesimal can
and cannot imply.

For real $a$, let $B_a=\mathbb C[r]/(r^2+a)$, with the conjugation
that conjugates coefficients and fixes $r$. Define
\[
\langle f,g\rangle_a=
\operatorname{Tr}_{B_a/\mathbb C}(M_{\overline f g}),
\tag{EFI36}
\]
where $M_b$ means multiplication by $b$. In basis $1,r$,
$\operatorname{Tr}(1)=2$, $\operatorname{Tr}(r)=0$, and
$\operatorname{Tr}(r^2)=-2a$. Thus the Gram matrix is
\[
G_2(a)=\begin{pmatrix}2&0\\0&-2a\end{pmatrix}.
\tag{EFI37}
\]
It is positive definite for $a<0$, has inertia $(1,1,0)$ for
$a>0$, and has radical $\mathbb C r$ at $a=0$. Here inertia
lists positive, negative, and zero dimensions. In particular, a
nonzero dual-number direction can be trace-null at the collision and
become negative on one side of that collision.

For real $d$, use $B_d=\mathbb C[z]/(z^3+6dz)$ with coefficient
conjugation fixing $z$. Multiplication in basis $1,z,z^2$ gives
\[
\operatorname{Tr}(1)=3,\quad
\operatorname{Tr}(z)=0,\quad
\operatorname{Tr}(z^2)=-12d,\quad
\operatorname{Tr}(z^3)=0,\quad
\operatorname{Tr}(z^4)=72d^2.
\tag{EFI38}
\]
For example the matrix of $M_z$ has columns
$(0,1,0)^T,(0,0,1)^T,(0,-6d,0)^T$, and squaring it proves the
second moment; the last two follow from $z^3=-6dz$. The Gram matrix is
\[
G_3(d)=
\begin{pmatrix}
3&0&-12d\\0&-12d&0\\-12d&0&72d^2
\end{pmatrix},
\qquad \det G_3(d)=-864d^3.
\tag{EFI39}
\]
For $d\ne0$, the $1,z^2$ block has positive first entry and
determinant $72d^2>0$, so completing the square makes both of its
directions positive. The remaining entry is $-12d$. Hence the
inertia is $(3,0,0)$ when $d<0$, $(2,1,0)$ when $d>0$, and
$(1,0,2)$ at $d=0$. At the latter point the radical is the entire
nilpotent ideal $(z)subset B_0$.

For the graph algebra $A_d$, in the retained basis $1,u,v$, the
same computation using EFI28 gives
\[
G_{\rm graph}(d)=
\begin{pmatrix}
3&-12d&0\\-12d&72d^2&0\\0&0&-12d^3
\end{pmatrix},
\qquad \det G_{\rm graph}(d)=-864d^5.
\tag{EFI40}
\]
To verify that this is the trace intrinsic to $A_d$, rather than an
unproved transport of trace, multiply $1,u,v$ using EFI28. The
diagonal entries of $M_u$ are $0,-6d,-6d$, and those of $M_v$
are all zero. Thus $\operatorname{Tr}(u)=-12d$ and
$\operatorname{Tr}(v)=0$, from which every entry follows.
The inertias are exactly those of EFI39, while at $d=0$ the
radical is the two-dimensional ideal $(u,v)$.

The trace forms before and after the graph inclusion are related by
the exact basis map $(1,u,v)\mapsto(1,z^2,dz)$. Thus the change of
determinant is the factor $d^2$. The quotient of length one in
EFI32 is recorded by two additional orders of discriminant vanishing,
not by cancellation of the sign on $d>0$.

The full original cubic has discriminant $c^4\det G_3(d)$, namely
$-864c^4d^3$. The factor $c^4$ is retained because the displayed
polynomial is $c(z^3+6dz)$, and each of the three root differences
is unchanged while a cubic discriminant has leading-coefficient power
four. This agrees with its exact coefficient heat discriminant.

## 6. The zero-prime globalization and the infinitesimal fibre

Let $L$ be a nontrivial bounded distributive lattice and $R$ a
nonzero commutative unital ring. The programme semiring is
\[
G_L(R)=\{(0,\lambda):\lambda\in L\}
\cup\{(r,1_L):r\in R\},
\quad
(r,\lambda)+(s,\mu)=(r+s,\lambda\vee\mu),
\quad
(r,\lambda)(s,\mu)=(rs,\lambda\wedge\mu).
\tag{EFI41}
\]
Its global additive identity is
$\tau_L=(0,0_L)$, whereas its supported zero is
$e_L=(0,1_L)\ne\tau_L$. Write $Z_L=\{(0,\lambda)\}$.
Multiplying by $e_L$ proves $e_LG_L(R)=Z_L$.

The amplitude projection
\[
\rho_R:G_L(R)\longrightarrow R,\qquad (r,\lambda)\longmapsto r
\tag{EFI42}
\]
preserves addition, multiplication, and both the global zero and unit.
The ideal $Z_L$ is prime exactly when $R$ is a domain. Indeed
membership of $xy$ in $Z_L$ is exactly $\rho_R(x)\rho_R(y)=0$,
and every ring element occurs as a supported amplitude. This proves
both implications, including the need for the domain hypothesis.
For $R=\mathbb Z$, the supported-zero prime is therefore the
established prime of the original programme; this is not a new claim.

A ring homomorphism $f:R\to R'$ induces the semiring map
\[
G_L(f):G_L(R)\longrightarrow G_L(R'),\qquad
(r,\lambda)\longmapsto(f(r),\lambda).
\tag{EFI43}
\]
It is defined even when a nonzero $r$ maps to zero: its top support
remains top, so the image is $e_L$, not $\tau_L$. The operation
identities follow by applying $f$ to amplitudes and leaving the
lattice operations unchanged.

In particular EFI10 induces
\[
G_L(\mathbb C[[r]])\longrightarrow G_L(D),\qquad
\widehat r\longmapsto\widehat\epsilon=:\eta,
\qquad \eta^2=e_L\ne\tau_L.
\tag{EFI44}
\]
Here $\widehat r=(r,1_L)$. The image infinitesimal $\eta$ is
not itself $e_L$, because its amplitude $\epsilon$ is nonzero.
Consequently $Z_L$ is not prime in $G_L(D)$: $\eta^2\in Z_L$
but $\eta\notin Z_L$. The same calculation holds for the two
nilpotent directions of $G_L(A_0)$ and the nonzero nilpotents of
$G_L(B_0)$. The change is forced by the actual amplitude ring;
it cannot be avoided by relabelling $e_L$ as $\tau_L$.

The prime map remains completely explicit. For a ring prime
$\mathfrak p\subset R$, set
\[
Q_{\mathfrak p}=
Z_L\cup\{(r,1_L):r\in\mathfrak p\}.
\tag{EFI45}
\]
The product test through $\rho_R$ proves this is prime. In the
dual-number ring every prime contains $\epsilon$, because
$\epsilon^2=0$; the quotient by $(\epsilon)$ is the field
$\mathbb C$. Thus its unique ring prime is $(\epsilon)$,
and the arithmetic prime at the collision is
\[
Q_{(\epsilon)}\subset G_L(D),\qquad
G_L(f)^{-1}(Q_{(\epsilon)})=Q_{(r)}
\subset G_L(\mathbb C[[r]]).
\tag{EFI46}
\]
The contraction follows from $f^{-1}((\epsilon))=(r)$.
The pure support primes $Z_{\mathfrak a}$, for lattice prime ideals
$\mathfrak a\subset L$, contract to the identical support primes:
a top-supported amplitude always has top support under EFI43, and
a proper lattice ideal does not contain $1_L$. This proves the
full prime-contraction description for this map.

In the scalar support case $L=\{0,1\}$, the domain family has
\[
(\tau)\subsetneq(e)\subsetneq Q_{(r)}.
\tag{EFI47}
\]
The infinitesimal fibre instead has the two prime ideals
$(\tau)\subsetneq Q_{(\epsilon)}$. Its missing intermediate prime
has not been silently deleted: $(e)$ remains an ideal, and EFI44
is its explicit failure of primality. The spectrum map contracts
these two primes to $(\tau)$ and $Q_{(r)}$, respectively.

### Why the pole still needs the compactified boundary

Let $R=\mathbb C[[r]]$ and $K=\mathbb C((r))$. The inclusion
$G_L(R)\hookrightarrow G_L(K)$ is injective because amplitudes and
supports are individually preserved. The finite inverse expression
$x=-1/(2r)$ belongs to the latter amplitude ring, not the former.
If an element $X\in G_L(R)$ extended it while satisfying
$\widehat{-2r}\,X=\widehat1$, applying EFI42 would give
$-2r\rho_R(X)=1$ in $R$, impossible by its constant term.
At the special fibre, $\eta X=\widehat1$ is also impossible,
since amplitudes would assert that the nilpotent $\epsilon$ is
invertible. This proves the precise nonextension; EFI8–EFI10 supply
the compactified object and its nonzero infinitesimal in its place.

## 7. Support-valued retention of the calculated trace signatures

Assume $L$ is finite. Define the contracted meet algebra
\[
C_L=\mathbb C[L,\wedge]/([0_L]).
\tag{EFI48}
\]
For every $a\ne0_L$, evaluation
$\chi_a([\lambda])=1$ when $a\le\lambda$, and zero otherwise,
is multiplicative. In any linear extension of the finite order on
$L\setminus\{0_L\}$, their incidence matrix is triangular with
ones on the diagonal. Hence the joint evaluation is an algebra
isomorphism $C_L\cong\mathbb C^{L\setminus\{0_L\}}$.
Let $E_a$ denote its coordinate idempotents. Thus
$E_aE_b=\delta_{ab}E_a$ and $\sum_aE_a=1$.

For any one of the finite algebras $V$ above, extend it to
$C_L\otimes V$ and give the coefficient algebra the conjugation
fixing each $E_a$. For $x=\sum_aE_a\otimes x_a$ and
$y=\sum_aE_a\otimes y_a$, define the support-valued trace form
\[
\mathcal T_L(x,y)=\sum_a E_a
\operatorname{Tr}_V(M_{\overline{x_a}y_a}).
\tag{EFI49}
\]
This is exactly the trace of the multiplication endomorphism over
$C_L$, because the product decomposition makes its matrix blockwise
the multiplication matrix over $V$. Each $\chi_a$ sends EFI49
to the already calculated finite trace form on $V$, while
$v\mapsto E_a\otimes v$ provides its supported section.

For positive real weights $w_a>0$, applying
$\ell(\sum t_aE_a)=\sum w_at_a$ gives a Hermitian form which is a
direct sum of positively weighted copies of the original form.
For example, for $a>0$ in the quadratic family and any nonzero
support idempotent $E_j$,
\[
\ell\mathcal T_L(E_j\otimes r,E_j\otimes r)=-2w_ja<0.
\tag{EFI50}
\]
For $d>0$, the triple root direction $E_j\otimes z$ has value
$-12w_jd<0$, and the graph direction $E_j\otimes v$ has value
$-12w_jd^3<0$. At the collision these nonzero infinitesimal
directions are radical directions in every supported component.
The support extension therefore retains both the vanishing at the
collision and the computed sign on either side. It does not itself
prove that the corrected Weil form equals this trace extension.

## 8. Exact result available for the arithmetic continuation

The actual inverse map supplies a finite cover whose double special
fibre is dual numbers, and whose triple projective special fibre has
two independent square-zero directions. The sheet trace, graph-to-root
specialization, and target projection each have different computed
kernels: EFI13, EFI31–EFI33, and EFI14. Their kernels are retained
objects, with explicit connecting maps. The original pole observable
has the nonzero second moments EFI15 and EFI35. The trace signatures
are EFI37, EFI39, EFI40, and their support-valued forms are EFI49.

The exact arithmetic interface already present in the read source is
the finite scalar extension $s\mapsto-r^2/2$ of its specified
arithmetic quotient, with multiplication matrix
$\begin{pmatrix}0&-2S\\I&0\end{pmatrix}$. Its square is
$-2\operatorname{diag}(S,S)$. These identities transport the
two-sheet geometry while preserving the original spectral coordinate.
They do not identify an arbitrary value of the collision parameter
with a zero of that arithmetic operator. A corrected Weil calculation
must carry its actual test-function map and trace through this
interface; no positivity conclusion about that different form has
been substituted for this calculation.

## 9. Exact bridge to the previously observed deformation

The first 135 lines of the programme's
OBSERVED_COTANGENT_FROBENIUS_DERIVATION.md were additionally read.
Its original coefficients in OCF1–OCF3 are
$a_{\rm obs}>0$, $\varepsilon_{\rm obs}>0$,
$r_{\rm obs}\in\mathbb C$,
\[
\lambda(s)=a_{\rm obs}s+\varepsilon_{\rm obs}r_{\rm obs}
=a_{\rm obs}(s-s_*),\qquad
s_*=-\frac{\varepsilon_{\rm obs}r_{\rm obs}}{a_{\rm obs}},
\qquad
A_{\rm obs}=\mathbb C[s,z_{\rm obs}]
/(z_{\rm obs}^2-\lambda(s)z_{\rm obs}).
\tag{EFI51}
\]
The subscripts distinguish the observed coefficients from the original
map's target $a$ and inverse-root coordinate $r$. They do not alter
any coefficient.

Retain the escaping cover from EFI7 as
$C_{\rm esc}=\mathbb C[a,r]/(r^2+a)$ over $\mathbb C[a]$.
Define the base map
\[
\mathbb C[a]\longrightarrow\mathbb C[s],\qquad
a\longmapsto-\frac{\lambda(s)^2}{4}.
\tag{EFI52}
\]
Its pullback is
\[
C_{\rm esc}\otimes_{\mathbb C[a]}\mathbb C[s]
=\mathbb C[s,r]/\left(r^2-\frac{\lambda(s)^2}{4}\right).
\tag{EFI53}
\]
There is the exact $\mathbb C[s]$-algebra isomorphism
\[
\begin{aligned}
\Psi:A_{\rm obs}&\longrightarrow
C_{\rm esc}\otimes_{\mathbb C[a]}\mathbb C[s],
&
z_{\rm obs}&\longmapsto r+\frac{\lambda}{2},\\
\Psi^{-1}:C_{\rm esc}\otimes_{\mathbb C[a]}\mathbb C[s]
&\longrightarrow A_{\rm obs},
&
r&\longmapsto z_{\rm obs}-\frac{\lambda}{2}.
\end{aligned}
\tag{EFI54}
\]
For proof,
\[
\left(z_{\rm obs}-\frac\lambda2\right)^2-\frac{\lambda^2}{4}
=z_{\rm obs}^2-\lambda z_{\rm obs}.
\tag{EFI55}
\]
This verifies both quotient relations, and both compositions fix their
generators. Thus the previously observed deformation is the specified
base change of the actual escaping cover. This is an isomorphism of
these full families, rather than an identification only of their
special fibres. The base map is quadratic and is part of the result.

Under EFI54 the sheet involution $r\mapsto-r$ becomes exactly
\[
z_{\rm obs}\longmapsto\lambda-z_{\rm obs}.
\tag{EFI56}
\]
The two observed factors $z_{\rm obs}=0,\lambda$ correspond to
$r=-\lambda/2,+\lambda/2$. Consequently the original source coordinates
along these sheets, for $\lambda\ne0$, are respectively
\[
\left(\frac1\lambda,-\frac32\lambda,\frac{13}2\lambda^2\right),
\qquad
\left(-\frac1\lambda,\frac32\lambda,\frac{13}2\lambda^2\right).
\tag{EFI57}
\]
Substitution into EFI1 gives
$(a,b,c)=(-\lambda^2/4,0,0)$, as already proved by EFI3.
The additional finite point is $(0,0,-\lambda^2/4)$. Hence the
isomorphism carries the actual inverse branches and their remaining
finite point, not just the root equation.

### The infinitesimal deformation that vanishes to first order

Put $\delta=s-s_*$ and $\kappa=a_{\rm obs}>0$, so that
$\lambda=\kappa\delta$. Over the first-order base
$T_1=\mathbb C[\delta]/(\delta^2)$, EFI54 gives
\[
A_{\rm obs}\otimes_{\mathbb C[s]}T_1
\xrightarrow[\sim]{r=z_{\rm obs}-\kappa\delta/2}
T_1[r]/(r^2)
 =T_1\otimes_{\mathbb C}\mathbb C[r]/(r^2).
\tag{EFI58}
\]
The relation follows because the full centered equation is
\[
r^2=\frac{\kappa^2\delta^2}{4}.
\tag{EFI59}
\]
Thus the first-order deformation is a product. This is the exact
sense in which the deformation class vanishes at first order.
The class $r$ itself is nonzero, since $1,r$ are a free $T_1$-basis.
The map and its inverse in EFI58 reduce to the identity on the
central dual-number fibre. Its first-order triviality has therefore
not been obtained by removing that fibre.

At second order let $T_2=\mathbb C[\delta]/(\delta^3)$. Then the
family is not isomorphic over $T_2$ to $T_2[\epsilon]/(\epsilon^2)$.
To prove this assertion completely, every element of the centered
family has a unique form $A+B r$, with $A,B\in T_2$. If it is the
image of $\epsilon$ under such an isomorphism, its reduction modulo
$\delta$ must generate the nilpotent ideal of
$\mathbb C[r]/(r^2)$. Therefore $B$ has nonzero constant term and is
a unit. The equation $(A+Br)^2=0$ gives, in the free basis $1,r$,
\[
2AB=0,\qquad
A^2+B^2\frac{\kappa^2\delta^2}{4}=0.
\tag{EFI60}
\]
Since $2B$ is a unit, the first equation forces $A=0$. The second
then asserts that the nonzero class $\delta^2$ in $T_2$ is zero
after multiplication by the unit $B^2\kappa^2/4$, a contradiction.
Thus the first-order triviality has an explicitly nontrivial
second-order continuation.

This supplies a precise distinction between a vanishing tangent
deformation and a vanishing family. The original escape parameter is
$a=-\kappa^2\delta^2/4$: its first derivative is zero at the collision,
and its second derivative there is exactly $-\kappa^2/2$.

### Trace form and discriminant transported through the isomorphism

Along the real displacement line $s=s_*+\delta$, $\delta\in\mathbb R$,
the original coefficient $\lambda=\kappa\delta$ is real, even when
$s_*$ is not real. Coefficient conjugation fixes this real parameter
and fixes $z_{\rm obs}$. The multiplication trace in basis
$1,z_{\rm obs}$ is
\[
G_{\rm obs}(\lambda)=
\begin{pmatrix}2&\lambda\\\lambda&\lambda^2\end{pmatrix}.
\tag{EFI61}
\]
Indeed $\operatorname{Tr}(1)=2$,
$\operatorname{Tr}(z_{\rm obs})=\lambda$, and
$\operatorname{Tr}(z_{\rm obs}^2)=\lambda^2$, by multiplication in
the free basis. For the centered basis $1,r$, the basis-change matrix
from its coordinates to the original basis is
\[
Q=\begin{pmatrix}1&-\lambda/2\\0&1\end{pmatrix},\qquad
Q^*G_{\rm obs}Q=
\begin{pmatrix}2&0\\0&\lambda^2/2\end{pmatrix}.
\tag{EFI62}
\]
Direct multiplication verifies this equality. It is precisely the
pullback of EFI37 through $a=-\lambda^2/4$:
$-2a=\lambda^2/2$. In particular, the observed real-displacement
family is positive definite away from the collision and positive
semidefinite at the collision, with radical $\mathbb C r$ there.
Its real base image lies on $a\le0$; this is why it does not enter
the negative-sign side $a>0$ of EFI37.

The discriminants satisfy, with every coefficient retained,
\[
\operatorname{disc}(r^2+a)=-4a,\qquad
(-4a)\big|_{a=-\lambda^2/4}=\lambda^2
=a_{\rm obs}^2(s-s_*)^2
=\det G_{\rm obs}.
\tag{EFI63}
\]
The original quadratic in EFI2 is $-2(r^2+a)$, whose polynomial
discriminant is $-16a$; its pullback is $4\lambda^2$.
This extra factor four belongs to the polynomial's retained leading
coefficient. It is not the trace discriminant in the monic algebra
basis $1,r$.

The map EFI54 also induces the isomorphism of programme semirings
$G_L(\Psi)$ by EFI43, preserving every support label, $\tau_L$,
and $e_L$ individually. At $\delta=0$ it recovers
$\widehat r^2=e_L\ne\tau_L$. Thus the actual bridge carries the
infinitesimal, its zero-prime contraction, and its trace form; no
identification of $\tau_L$ with supported zero is used.

## 10. Differential bridge and the primes of the full families

Retain every coordinate of EFI51–EFI55, with
$\kappa=a_{\rm obs}$. Differentiating those exact polynomial maps gives
\[
dr=dz_{\rm obs}-\frac\kappa2\,ds,\qquad
da=-\frac{\kappa\lambda}{2}\,ds,\qquad
2r\,dr+da=(2z_{\rm obs}-\lambda)\,dz_{\rm obs}
-\kappa z_{\rm obs}\,ds.
\tag{EFI64}
\]
For proof substitute $2r=2z_{\rm obs}-\lambda$ in the first two
equalities: the coefficient of $ds$ is
$-\kappa(2z_{\rm obs}-\lambda)/2-\kappa\lambda/2
=-\kappa z_{\rm obs}$. Thus EFI64 is exactly the differential of
$r^2+a=z_{\rm obs}^2-\lambda z_{\rm obs}$.
It induces the map between the differential-module presentations
\[
\frac{C_{\rm esc}\,da\oplus C_{\rm esc}\,dr}
     {C_{\rm esc}(da+2r\,dr)}
\longrightarrow
\frac{A_{\rm obs}\,ds\oplus A_{\rm obs}\,dz_{\rm obs}}
     {A_{\rm obs}((2z_{\rm obs}-\lambda)dz_{\rm obs}
                    -\kappa z_{\rm obs}ds)}
\tag{EFI65}
\]
with scalars extended by EFI52–EFI54. These are the universal modules
of differentials: a derivation on a polynomial ring is determined by
its values on the two generators, and descends to the quotient
exactly when it annihilates the differential of the displayed
relation. This proves the presentations and the induced map without
assuming smoothness at a collision.

The tangent-deformation comparison can also be proved directly.
Over $\mathbb C[\eta]/(\eta^2)$, replacing $r$ by
$r+\eta h(r)$ changes the first-order coefficient of a relation
$r^2+\eta g(r)$ by $2rh(r)$; multiplying its defining relation by
the unit $1+\eta k(r)$ changes it by $k(r)r^2$. The retained class
of that coefficient is therefore
\[
[g]\in\mathbb C[r]/(r^2,2r)=\mathbb C.
\tag{EFI66}
\]
For the original escaping unfolding $r^2+a$, the displacement
$a=\eta$ gives $[g]=[1]\ne0$. For the observed unfolding
$z_{\rm obs}^2-\kappa\delta z_{\rm obs}$, the displacement
$\delta=\eta$ gives $[g]=[-\kappa z_{\rm obs}]=0$.
The explicit centering in EFI58 proves actual first-order triviality,
not merely the vanishing of an invariant. Equivalently,
$da/d\delta=-\kappa^2\delta/2$ vanishes at $\delta=0$.
EFI60 proves exactly what survives at second order.

Primality of supported zero must be checked on the total family
as well as on each fibre. The original escape algebra
$C_{\rm esc}\cong\mathbb C[r]$ is a domain, so $Z_L=(e_L)$ is prime
in $G_L(C_{\rm esc})$. In the observed total family,
$z_{\rm obs}(z_{\rm obs}-\lambda)=0$ with both factors nonzero.
Their nonvanishing follows from the free basis $1,z_{\rm obs}$ and
the nonzero polynomial $\lambda=\kappa(s-s_*)$. Hence $(e_L)$
is not prime in $G_L(A_{\rm obs})$.

There is a precise splitting map between the prime sets. The two
ideals $\mathfrak p_0=(z_{\rm obs})$ and
$\mathfrak p_1=(z_{\rm obs}-\lambda)$ are prime, since their
quotients are each $\mathbb C[s]$. Their intersection is zero:
an element $A(s)+B(s)z_{\rm obs}$ vanishes on both branches only
when $A=0$ and $B\lambda=0$, which force $A=B=0$.
They are the only minimal primes, since any prime must contain
one factor of $z_{\rm obs}(z_{\rm obs}-\lambda)$.
Under the composite map
$\iota:C_{\rm esc}\to A_{\rm obs}$, $r\mapsto z_{\rm obs}-\lambda/2$,
obtained from base change and $\Psi^{-1}$ in EFI54,
$r$ restricts to $-\kappa(s-s_*)/2$ and
$+\kappa(s-s_*)/2$ on these branches. Both substitutions are
injective maps $\mathbb C[r]\to\mathbb C[s]$. Consequently
\[
Q_{\mathfrak p_0}\cap Q_{\mathfrak p_1}=Z_L,\qquad
G_L(\iota)^{-1}(Q_{\mathfrak p_i})=Z_L
\quad(i=0,1),
\tag{EFI67}
\]
with $Z_L$ on the right denoting the zero-amplitude ideal
in $G_L(C_{\rm esc})$. Thus the original supported-zero prime has two
arithmetic prime points over it, whose intersection is the retained
nonprime zero-amplitude ideal. At the collision both lie below
$Q_{(z_{\rm obs},\lambda)}$, whose contraction is $Q_{(r)}$.
The last contraction follows by evaluating $r$ at zero and
retaining the constant coefficient of any polynomial in $r$.

The triple total families have the same domain issue already before
specialization. In $B$ and $A$ respectively,
\[
z(z^2+6d)=0,\qquad u(u+6d)=0,
\tag{EFI68}
\]
with both factors nonzero. For $B$ this follows from its free basis
$1,z,z^2$; for $A$ it follows from its free basis $1,u,v$.
Thus their supported-zero ideals are not prime either.
Their individual arithmetic primes and their contractions are
always the inverse images of the ring primes under EFI42, as
proved in EFI45. This statement retains the established prime
$(e)$ over domain amplitudes such as $\mathbb Z$ and $\mathbb C[r]$,
and also retains the exact zero-divisor products created by the
actual base change and collision.

## Exact algebra checks

The companion script check_escaping_fibre_infinitesimal.py passes 23 exact
polynomial, rational, matrix, and discriminant identities. Its recorded
output is ESCAPING_FIBRE_EXACT_CHECKS.json. These checks include the
original determinant, original inverse composition, both observed
branches in the original map, graph-algebra coordinates and products,
the two trace matrices, their determinants, and EFI54–EFI63. The
ring-theoretic completeness, exact-sequence, and nontrivial
second-order arguments are proved in the text rather than inferred
from finite sampling.


![The exact cover a=-r² and finite trace eigenvalues; the observed-family pullback retains the collision generator. The triple graph map retains its kernel. Proof: EFI7–EFI15, EFI23–EFI40, EFI51–EFI68.](figures/25_escaping_trace.png)

\clearpage

# Infinitesimal vanishing, retained currents, and support-valued positivity

22 September 2026. This note computes the several different vanishing statements at the observed collision, the complete signs that survive, and the exact class of corrections capable of changing them. The calculations retain the original observation, metric, Hermitian summand, amplitude multiplier, and full support algebra. No off-line zero of the Riemann zeta function is asserted to exist.

The incoming public programme proofs are [*The observed infinitesimal collision and the full arithmetic operator*, OC1–OC17](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_COLLISION.md); [*Observed support at the shifted nilpotent collision*, OSP1–OSP42](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_SUPPORT_PROPAGATION.md); and [*Cotangent and Frobenius calculations for the observed collision*, OCF1–OCF23 and OIF1–OIF36](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_COTANGENT_FROBENIUS.md). The additional complete local dependencies are [full-support reconstruction proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/FULL_SUPPORT_RECONSTRUCTION_DERIVATION.md), FSR1–FSR36; [finite Weil packet proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/WEIL_PACKET_DERIVATION.md), WP1–WP57; and [analytic Weil packet proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/WEIL_PACKET_ANALYTIC_DERIVATION.md), WA1–WA30. Their complete sources accompany this derivation; no public link is asserted for an unpublished dependency. The cited proofs retain their original human citations. This is a further finite derivation and an application of the already proved analytic identity WA24, not a replacement for its analytic proof.

## 1. Original operators and the collision

Keep the original source data and metric from OC1–OC3:
\[
M=C+R,\quad C=C^\dagger,\quad R=\epsilon fe^\dagger,
\quad e^\dagger e=f^\dagger f=1,\quad e^\dagger f=0,\quad\epsilon>0,
\]
\[
J=G_N^{-1}\Lambda^*Q_B^{1/2},\quad
Q_B=(\Lambda G_N^{-1}\Lambda^*)^{-1},\quad J^\dagger J=I_B,
\quad C_B=J^\dagger CJ=C_B^*.
\tag{ISP1}
\]
Here the original arithmetic quotient, cutoff, and observation remain those of OC1: \(q=(k+1)^2\), \(k\ge17\), \(k\equiv1\pmod4\), \(q-1\le N\le2q\), and the original surjection \(\Lambda:E\to B\). The star is the adjoint in the Euclidean coordinates supplied by the isometry \(J\); it does not change the original metric.

Write
\[
u=J^\dagger e,\quad v=J^\dagger f,\quad
a=u^*u,\quad r=u^*v,\quad d=v^*v,\quad
\Delta=ad-|r|^2>0.
\]
The measured area statement in OC3 supplies this strict inequality. Define
\[
g=u/\sqrt a,\qquad
h=\frac{v-(r/a)u}{\sqrt{\Delta/a}},\qquad
b=\epsilon\sqrt\Delta>0,\qquad P=gg^*+hh^*.
\tag{ISP2}
\]
The numerator defining \(h\) has inner product zero with \(u\), because \(u^*v-(r/a)u^*u=0\). Its squared norm is \(d-|r|^2/a=\Delta/a\). Thus \(g,h\) are an orthonormal pair and \(P\) is their orthogonal projector.

The exact observed family is
\[
F_B(s)=(\epsilon v+su)u^*,\qquad
M_B(s)=C_B+F_B(s),\qquad
\lambda(s)=as+\epsilon r.
\tag{ISP3}
\]
Direct multiplication gives \(F_B(s)^2=\lambda(s)F_B(s)\). On the original orthogonal plane \(S=\operatorname{im}P\), and on its orthogonal complement \(H\), respectively, it is
\[
F_B(s)|_S=\begin{pmatrix}\lambda(s)&0\\b&0\end{pmatrix},
\qquad F_B(s)|_H=0.
\tag{ISP4}
\]
At the collision parameter
\[
s_*=-\epsilon r/a,
\quad N=F_B(s_*)=\epsilon\bigl(v-(r/a)u\bigr)u^*=bhg^*,
\quad N^2=0,\quad Ng=bh\ne0.
\tag{ISP5}
\]
The map \(\mathbb C[\eta]/(\eta^2)\to\operatorname{End}(B)\), \(1\mapsto I_B\), \(\eta\mapsto N\), is injective. Indeed a relation \(cI_B+\ell N=0\) applied to \(h\) gives \(c=0\), and then applied to \(g\) gives \(\ell b=0\), hence \(\ell=0\). Its image is exactly the generated algebra. The supported version sends its unit to \(P\) and has the same proof on \(S\).

## 2. Exactly what vanishes

For the isolated nilpotent operator, for every scalar \(t\),
\[
\operatorname{tr}(N^j)=0\quad(j\ge1),\qquad
\det(I_B-tN)=1,\qquad
(I_B-tN)^{-1}=I_B+tN.
\tag{ISP6}
\]
In the basis \(g,h\), \(N\) is strictly triangular, and is zero on \(H\). This proves the trace and determinant assertions; multiplication proves the inverse. A marked matrix element retains the exact term
\[
x^*((I_B-tN)^{-1}-I_B)y
=tb(x^*h)(g^*y).
\tag{ISP7}
\]
For \(x=h,y=g\), this term is \(tb\), which is nonzero when \(t\ne0\). Vanishing of the isolated trace series therefore has an explicit kernel and a nonzero receiver.

The family algebra itself is
\[
\mathcal A=\mathbb C[t,z]/(z(z-at)),\qquad t=s-s_*.
\]
The invertible change \(\xi=z-at/2\), with inverse \(z=\xi+at/2\), gives
\[
z(z-at)=\xi^2-a^2t^2/4.
\tag{ISP8}
\]
Over \(\mathbb C[t]/(t^2)\), this is an isomorphism with the constant dual-number family, and it reduces to the identity on the fibre \(t=0\). Thus its first-order deformation class vanishes. Over \(\mathbb C[t]/(t^3)\), the trace discriminant in the basis \(1,z\) equals \(a^2t^2\ne0\); the constant dual-number family's trace discriminant is zero. To compute it, multiplication by \(z\) has trace \(at\), and multiplication by \(z^2=at z\) has trace \(a^2t^2\). The trace matrix is therefore
\(\left(\begin{smallmatrix}2&at\\at&a^2t^2\end{smallmatrix}\right)\), with determinant \(a^2t^2\). An invertible basis change multiplies its determinant by a unit square. Hence it cannot turn this nonzero discriminant into zero. The first nontrivial order is exactly two.

The original operator representation and its metric retain additional information. Work now over \(\mathbb C[t]/(t^2)\), and put
\[
K=\frac{a}{2b}gh^*,\qquad T=I_B+tK,\qquad T^{-1}=I_B-tK.
\]
Since \([K,N]=(a/2)(gg^*-hh^*)\), direct multiplication proves
\[
F_B(s_*+t)=TNT^{-1}+\frac{at}{2}P,
\]
\[
T^{-1}M_B(s_*+t)T
=C_B+N+t\left([C_B,K]+\frac a2P\right).
\tag{ISP9}
\]
Here \(C_B\) remains the original operator on all of \(B\); it need not preserve \(S\). These formulas follow by expanding products and using \(t^2=0\). If the formal parameter is given the real involution \(t^*=t\), then
\[
T^*T=I_B+t(K+K^*).
\tag{ISP10}
\]
The coefficient \(K+K^*\) is nonzero, because \((K+K^*)h=(a/(2b))g\). Thus this coordinate trivialization is not unitary for the original metric. Equations ISP9–ISP10 retain the exact operator and metric changes attached to the vanishing deformation class.

There is also a choice-dependent Frobenius vanishing. Over a torsionfree integral collision ring \(D_p=K_p[\eta]/\eta^2\) with the coefficient Frobenius specified in OIF33, every lift is
\[
\Phi_c(\eta)=pc\eta,\qquad c\in K_p.
\tag{ISP11}
\]
To verify this, write an image as \(A+B\eta\). Its square is zero, so the coefficient domain forces \(A=0\). Its reduction must equal \(\eta^p=0\), forcing \(B\in pK_p\); the converse is immediate. The corrected lift has \(c=0\), so kills \(\eta\), whereas the earlier multiplicative lift has \(c=1\) and sends it to \(p\eta\ne0\). The same underlying nilpotent algebra therefore does not determine this Frobenius vanishing without the specified lift.

## 3. The full arithmetic determinant does not vanish infinitesimally

Keep \(C_B\) in the characteristic polynomial, and let \(n=\dim B\). Rank-one determinant expansion gives
\[
\det(\zeta I_B-C_B-N)
=\det(\zeta I_B-C_B)
-b\,g^*\operatorname{adj}(\zeta I_B-C_B)h.
\tag{ISP12}
\]
For a proof, expand the determinant column by column. Every term containing at least two columns from \(bhg^*\) vanishes because those columns are proportional to \(h\). The terms containing exactly one such column sum to the displayed adjugate contraction, with the minus sign from the subtracted perturbation. This proof is a polynomial identity and does not require an inverse.

In particular, the isolated identity \(\det(I-tN)=1\) does not remove the second term of ISP12. On the plane, the concrete Hermitian choice
\(C_B|_S=\left(\begin{smallmatrix}0&c\\c&0\end{smallmatrix}\right)\), \(c\in\mathbb R\setminus\{0\}\), gives
\[
\det(\zeta I_S-C_B|_S-N|_S)=\zeta^2-c(c+b),
\qquad \det(\zeta I_S-C_B|_S)=\zeta^2-c^2.
\tag{ISP13}
\]
This example disproves an inference from nilpotence alone; it is not substituted for the native \(C_B\).

For the actual family, define
\[
p_*(\zeta)=\det(\zeta I_B-M_B(s_*)),\qquad
q_*(\zeta)=u^*\operatorname{adj}(\zeta I_B-M_B(s_*))u.
\]
The same polynomial expansion proves, exactly for every \(t\),
\[
p_{s_*+t}(\zeta)=p_*(\zeta)-tq_*(\zeta).
\tag{ISP14}
\]
Moreover \(q_*\) has degree \(n-1\) and leading coefficient \(u^*u=a>0\): the adjugate of \(\zeta I_B-M_B(s_*)\) has leading coefficient \(\zeta^{n-1}I_B\). Consequently the full characteristic polynomial has a nonzero first derivative in the original parameter, even though the abstract algebra deformation class in ISP8 vanishes. Equivalently, \(\operatorname{tr}M_B(s_*+t)=\operatorname{tr}M_B(s_*)+at\). These statements concern the actual original family.

## 4. The signed current survives with both signs

Use exactly the programme convention
\[
W_B(s)=i(M_B(s)-M_B(s)^*).
\]
The retained Hermitian term cancels in this particular difference because \(C_B=C_B^*\). It remains in ISP12–ISP14. Direct conjugate transposition of ISP4 gives
\[
W_B(s)|_S=
\begin{pmatrix}-2\operatorname{Im}\lambda(s)&-ib\\ib&0\end{pmatrix},
\qquad W_B(s)|_H=0.
\tag{ISP15}
\]
At the infinitesimal collision,
\[
W_*:=W_B(s_*)=i(N-N^*),\qquad
W_*^2=b^2P,
\]
\[
W_*\frac{g+ih}{\sqrt2}=b\frac{g+ih}{\sqrt2},\qquad
W_*\frac{g-ih}{\sqrt2}=-b\frac{g-ih}{\sqrt2}.
\tag{ISP16}
\]
These follow by multiplying the two-by-two matrix, or by using \(Ng=bh,Nh=0,N^*h=bg,N^*g=0\). Its inertia on \(B\) is \((1,1,n-2)\). For \(y=c_g g+c_hh+y_H\),
\[
y^*W_*y=2b\operatorname{Im}(\overline{c_g}c_h).
\tag{ISP17}
\]
Thus the two unit eigenvectors in ISP16 have values \(+b\) and \(-b\), not zero.

The current correction from the original parameter \(s=0\) is exactly
\[
W_*-W_B(0)=2\epsilon\operatorname{Im}(r)gg^*.
\tag{ISP18}
\]
For every complex parameter \(s\), the determinant of its active matrix in ISP15 is \(-b^2<0\). Consequently that rank-one displacement cannot make the current positive semidefinite. Along the real displacement \(s=s_*+t\), \(t\in\mathbb R\), the full current is exactly constant, \(W_B(s_*+t)=W_*\), because \(\lambda(s_*+t)=at\) is real.

## 5. All Hermitian corrections on the current plane

Write an arbitrary Hermitian correction on \(S\) as
\[
D=\begin{pmatrix}\alpha&c\\\overline c&\delta\end{pmatrix},
\qquad\alpha,\delta\in\mathbb R,\quad c\in\mathbb C.
\]
Then the complete set of corrections giving a nonnegative form is
\[
\boxed{W_*+D\succeq0
\quad\Longleftrightarrow\quad
\alpha\ge0,\ \delta\ge0,\ \alpha\delta\ge|c-ib|^2.}
\tag{ISP19}
\]
For necessity evaluate on \(g,h\), obtaining the diagonal inequalities, and use the nonnegative determinant. For sufficiency, when \(\alpha>0\), complete the square:
\[
\alpha\left|x+\frac{c-ib}{\alpha}y\right|^2
+\left(\delta-\frac{|c-ib|^2}{\alpha}\right)|y|^2\ge0.
\]
When \(\alpha=0\), the determinant inequality forces \(c-ib=0\), and the form is \(\delta|y|^2\). This proves every boundary case as well as the positive-definite case.

In particular, an orthogonal-support correction \(tP\), \(t\in\mathbb R\), gives positivity exactly for \(t\ge b\). A correction supported only on \(gg^*\), or only on \(hh^*\), never suffices. The equality \(e^2=e\) by itself supplies no scalar coefficient \(t\); ISP19 states the exact correction needed by the operator it would act on.

The analogous complete classification for a larger support space is as follows. Let \(X,Z\) be finite-dimensional Hermitian spaces and let
\[
\mathcal Q=\begin{pmatrix}H&A\\A^*&D\end{pmatrix}
\quad\text{on }X\oplus Z,
\qquad H=H^*,\quad D=D^*.
\]
Let \(D^+\) be the operator equal to the reciprocal of each nonzero eigenvalue of \(D\) and zero on its kernel. Then
\[
\boxed{\mathcal Q\succeq0\quad\Longleftrightarrow\quad
D\succeq0,\quad A(\ker D)=0,\quad H-AD^+A^*\succeq0.}
\tag{ISP20}
\]
To prove necessity, first restrict to \(Z\). For \(z_0\in\ker D\), the value on \((x,tz_0)\) is \(x^*Hx+2\operatorname{Re}(t x^*Az_0)\). Its nonnegativity for every complex \(t\) forces \(Az_0=0\). Thus \(A^*x\) belongs to \((\ker D)^\perp=\operatorname{im}D\). For all \(x,z\), exact multiplication now gives
\[
\langle(x,z),\mathcal Q(x,z)\rangle
=x^*(H-AD^+A^*)x
+(z+D^+A^*x)^*D(z+D^+A^*x).
\tag{ISP21}
\]
Set \(z=-D^+A^*x\) for the last necessary inequality. Conversely ISP21 proves positivity from the three displayed conditions. This proof constructs the minimizing support coordinate and includes singular \(D\).

For a fixed Hermitian correction \(R\) to the old block, replace \(H\) in ISP20 by \(H+R\); the result classifies every such corrected extension. Adding independent support coordinates and mixed blocks while leaving \(H\) unchanged cannot remove an old negative value: it is still the value on \((x,0)\). Indeed minimizing over the added positive coordinates subtracts \(AD^+A^*\), exactly as ISP21 records.

## 6. Full support and every positive scalar trace

Retain the finite bounded distributive lattice \(L\), the actual semiring \(G_L(R)\), and its supported zero \(e_L\), with \((e_L)=Z_L\) prime when \(R\) is a domain. This is prior programme mathematics, not a new result here. The contracted multiplicative algebra is the proved product
\[
\Gamma_L=\mathbb C[(G_L(R),\times)]/([\tau_L])
\cong C_L\times D_R,
\quad C_L=\mathbb C[(L,\wedge)]/([0_L]).
\tag{ISP22}
\]
In this algebra \([e_L]\) is the identity of the \(C_L\) factor. It is a multiplicative idempotent, not the square-zero operator \(N\) of ISP5. The latter comes from the separate, explicitly specified deformation/observation receiver. The exact role of the former in the following coefficient extension is multiplication by the support identity.

FSR11–FSR14 give
\[
C_L=\bigoplus_{a\in L\setminus\{0\}}\mathbb CE_a,
\quad E_aE_b=\delta_{ab}E_a,\quad E_a^*=E_a,
\quad\sum_aE_a=1_{C_L}.
\tag{ISP23}
\]
For completeness, the characters are \(\eta_a([\lambda])=1_{a\le\lambda}\); their incidence matrix is triangular with diagonal one, hence invertible. Its inverse gives \(E_a=\sum_{\lambda\le a}\mu(\lambda,a)[\lambda]\). Applying every character proves the stated multiplication and unit identities.

Every positive complex-linear scalar functional on \(C_L\) is uniquely
\[
\ell\Bigl(\sum_ac_aE_a\Bigr)=\sum_at_ac_a,
\qquad t_a\ge0.
\tag{ISP24}
\]
Indeed \(E_a=E_a^*E_a\) forces \(\ell(E_a)\ge0\); conversely the displayed coefficients give \(\ell(v^*v)=\sum_at_a|v_a|^2\ge0\). It is faithful on positive elements precisely when every \(t_a>0\).

Extend the actual current coefficientwise to \(B_L=C_L\otimes B\), retaining \(1\otimes C_B\) in its full arithmetic operator. Its support-valued form is
\[
\mathcal W_L(x,y)=\sum_aE_a x_a^*W_*y_a,
\qquad x=\sum_aE_a\otimes x_a.
\tag{ISP25}
\]
For every \(a\) with \(t_a>0\), the exact vector
\[
x_a^-=E_a\otimes(g-ih)/\sqrt2
\quad\text{has}\quad
\mathcal W_L(x_a^-,x_a^-)=-bE_a,
\qquad\ell\mathcal W_L(x_a^-,x_a^-)=-bt_a<0.
\tag{ISP26}
\]
Thus every nonzero positive functional retains a negative direction for this form. If exactly \(r\) of the weights are positive and \(d_L=|L|-1\), its scalar inertia is
\[
(r,r,(n-2)r+n(d_L-r)).
\tag{ISP27}
\]
This follows by using the two eigenvectors in ISP16 and a basis of \(H\) in every sector; the sectors of weight zero contribute their entire \(n\)-dimensional space to the radical.

The same proof applied to the full finite Weil pairing FSR28, whose scalar inertia is \((2,2,4m-4)\), gives
\[
\operatorname{inertia}(\ell\mathbb B_L)
=(2r,2r,(4m-4)r+4m(d_L-r)).
\tag{ISP28}
\]
In particular, the regular trace has all weights one. Boolean branch traces select only join-irreducible sectors and put zero weights on the remaining mixed sectors; zero observation there does not prove zero full form. For \(L=\mathbb B^2\), the mixed projector \(w=[1]-[a]-[b]\) obeys \(w^2=w\ne0\), both branch traces kill it, and FSR34–FSR35 give the exact value \(-2m w\) on the specified mixed negative packet.

## 7. Exact maps from the collision current to a quartet packet

This section constructs a finite comparison without identifying it with the native period observation. Let \(\rho=1/2+\delta+i\gamma\), \(0<\delta<1/2\), \(\gamma>2\), and use the four distinct points
\[
(\alpha_1,\alpha_2,\alpha_3,\alpha_4)
=(\rho,1-\overline\rho,\overline\rho,1-\rho).
\]
For \(m\ge1\), let \(d(s)=\prod_i(s-\alpha_i)\), \(h(s)=d(s)^m\), \(E_h=\mathbb C[s]/(h)\), and let \(e_i\) be the full primary idempotents. Let \(U=M_{j_h(v)}\) be the original amplitude unit, with its full Taylor coefficients and nonzero values \(v(\alpha_i)\). Let \(a_h=\operatorname{ev}U:E_h\to\mathbb C^4\). The finite pairing is
\[
B_h(x,y)=m\bigl(\overline{(a_hx)_2}(a_hy)_1+
\overline{(a_hx)_1}(a_hy)_2+
\overline{(a_hx)_4}(a_hy)_3+
\overline{(a_hx)_3}(a_hy)_4\bigr).
\tag{ISP29}
\]
These algebraic data can be defined for arbitrary such points and an arbitrary specified unit; they do not assert a zeta zero.

Define the typed injective linear map
\[
\mathcal I:S\longrightarrow E_h,
\quad c_gg+c_hh\longmapsto
\sqrt{b/m}\,U^{-1}(c_ge_1-ic_he_2).
\tag{ISP30}
\]
Applying \(a_h\) gives \(\sqrt{b/m}(c_g,-ic_h,0,0)\), so injectivity follows. Substitution in ISP29 gives the exact isometry
\[
B_h(\mathcal I x,\mathcal I y)=x^*W_*y\qquad(x,y\in S).
\tag{ISP31}
\]
Explicitly the right side is \(-ib\overline{x_g}y_h+ib\overline{x_h}y_g\), and the left side has the same two coefficients. This is an isometry of Hermitian forms, whose signs are indefinite; it is not asserted to preserve the original positive norm.

There is also a nilpotent operator on the complete packet, including all its jets:
\[
\mathcal N_h(x)=-ib\,(a_hx)_1 U^{-1}e_2.
\tag{ISP32}
\]
Since \((a_hU^{-1}e_2)_1=0\), it has square zero. It is nonzero on \(U^{-1}e_1\), and direct substitution proves
\[
\mathcal N_h\mathcal I=\mathcal I N|_S.
\tag{ISP33}
\]
This comparison preserves the constant \(b\), its complex phase, and the original \(U\). It sends the radical \(J_h=(d)/(d^m)\) to zero by the formula for \(a_h\); every radical jet remains in the domain and in \(U\). Extending ISP30–ISP33 by \(C_L\otimes-\) gives the identical maps in every support sector. The construction is explicit and depends on the chosen quartet; equality with the original period receiver has not been asserted or assumed.

## 8. Interpolation removes endpoint terms without changing any packet jet

Since none of the four points is \(0\) or \(1\), \(h(0)h(1)\ne0\). For a polynomial \(q\), set
\[
\boxed{\mathcal R_hq(s)=q(s)-h(s)
\left((1-s)\frac{q(0)}{h(0)}+s\frac{q(1)}{h(1)}\right).}
\tag{ISP34}
\]
This is a linear polynomial map. Substitution at the two endpoints gives
\[
\mathcal R_hq(0)=\mathcal R_hq(1)=0,
\qquad\mathcal R_hq\equiv q\pmod h.
\tag{ISP35}
\]
The latter congruence preserves the derivatives of every order \(0,\ldots,m-1\) at every \(\alpha_i\), because \(h\) has order \(m\) there. Conversely divisibility by \(h\) is exactly the kernel of the complete quartet jet map, by successive division by the four distinct linear factors. Therefore every original packet class, including every nilpotent jet and the entire action of \(U\), is retained by this map.

Let \(s_h:E_h\to\mathbb C[s]\) select the unique representative of degree below \(4m\), as supplied by monic polynomial division. The composite
\[
\widetilde s_h=\mathcal R_hs_h:
E_h\longrightarrow s(s-1)\mathbb C[s]
\tag{ISP36}
\]
is a linear section of polynomial reduction modulo \(h\), with degree at most \(4m+1\). Its image has dimension \(4m\), and every class has exactly the stated lift. In particular this endpoint condition does not constrain any quartet jet.

The same statement holds for arbitrary specified finite endpoint orders. For \(K\ge1\), put \(b_K(s)=s^K(s-1)^K\). It is a unit in \(E_h\), because each \(b_K(\alpha_i)\ne0\). An explicit inverse is obtained by the finite Taylor reciprocal in each factor \(\mathbb C[t_i]/(t_i^m)\), followed by the primary idempotent inverse of the jet map. Consequently
\[
\widetilde s_{h,K}(x)=b_K\,s_h\bigl([b_K]^{-1}x\bigr)
\tag{ISP37}
\]
is a linear section of reduction modulo \(h\) whose values vanish to order at least \(K\) at both \(0\) and \(1\). Multiplication followed by reduction proves the section identity exactly. This constructs the connecting map for every finite endpoint jet constraint.

## 9. Consequence for the explicit formula and zero-prime corrections

The following application concerns the programme's counterfactual zeta packet used in WP1–WP4 and WA1–WA2: its four specified points have exact zero order \(m\) for \(g=2\xi\), so \(v=g/h\) is entire and has nonzero values there. This is the established test of an off-line packet; it is not an existence claim.

For two polynomials \(q_1,q_2\), use exactly
\[
q^\#(s)=\overline{q(1-\overline s)},\qquad
A_{q_1,q_2}(s)=q_1^\#(s)q_2(s)v(s)^2.
\tag{ISP38}
\]
Let \(\widetilde q_i=\mathcal R_hq_i\). Equations ISP35 and WP21 prove that the original full primary amplitude jets of \(\widetilde q_iv\) and \(q_iv\) agree. Furthermore
\[
A_{\widetilde q_1,\widetilde q_2}(0)
=A_{\widetilde q_1,\widetilde q_2}(1)=0.
\tag{ISP39}
\]
Indeed the factor \(\widetilde q_2\) vanishes at both endpoints. This conclusion also follows by evaluating the reflected first factor; no positivity inference is used.

Take the full-jet negative class
\[
x_-=U^{-1}(e_1-e_2),\qquad
\widetilde q_- =\widetilde s_h(x_-).
\tag{ISP40}
\]
Its four amplitude values are exactly \((1,-1,0,0)\), hence
\[
B_h([\widetilde q_-],[\widetilde q_-])=-2m.
\tag{ISP41}
\]
Its Fourier-coordinate polynomial is \(\widetilde P_-(z)=\widetilde q_-(1/2+iz)\); define \(F_-(z)=\widetilde P_-(z)v(1/2+iz)\),
\[
K_-(t)=|F_-(t)|^2,\qquad
k_-(u)=\frac1{2\pi}\int_{\mathbb R}K_-(t)e^{itu}\,dt.
\]
WA9–WA16 apply to every polynomial, so the increased degree in ISP36 changes their constants but not the proved admissibility, exponential strip decay, or absolute convergence. Substitution into the full analytic identity WA24, using ISP39, gives
\[
\boxed{-2m=
\frac1{2\pi}\int_{\mathbb R}|F_-(t)|^2
\left(\operatorname{Re}\psi(\tfrac14+\tfrac{it}{2})-\log\pi\right)dt
-\sum_{n\ge2}\frac{\Lambda_{\rm ar}(n)}{\sqrt n}
\bigl(k_-(\log n)+k_-(-\log n)\bigr).}
\tag{ISP42}
\]
This is the exact endpoint-free arithmetic expression for that packet, with every sign and transform convention retained. It does not prove that this packet exists for zeta, and does not prove nonnegativity of the arithmetic expression.

More generally let \(\mathcal E(q)\) be the vector of any fixed finite list of derivatives at \(0,1\), and let \(D=D^*\) be any matrix on that vector space. Every correction
\[
\mathcal D(q_1,q_2)=\mathcal E(q_1)^*D\mathcal E(q_2)
\tag{ISP43}
\]
vanishes on the image of ISP37 for sufficiently large \(K\). Yet that image surjects onto every packet jet and contains the negative class ISP40. The same conclusion holds if \(\mathcal E\) takes the endpoint jets of \(qv\): multiplication by the entire function \(v\) preserves the required vanishing orders. Thus no correction factoring solely through finitely many endpoint evaluations or endpoint derivatives makes this packet form positive. This is a classification of that class of corrections, not an assumption that all effects of the zero prime belong to it.

In full support, choose any sector \(E_a\) and lift the polynomial as \(E_a\widetilde q_-\). Its exact support-valued form is \(-2mE_a\), while all the specified endpoint jets are zero. A positive scalar trace with weight \(t_a>0\) reads \(-2mt_a<0\), by ISP24. Mixed sectors obey the same calculation, including sectors omitted by every separate Boolean branch.

The proved zero-prime structure therefore changes the spectrum and enlarges the retained coefficient and observation spaces, as FSR1–FSR22 specify. A corrected analytic formula must supply its actual distribution or operator on these spaces. The results above already settle three concrete possibilities: nilpotence alone does not kill the observed current; coefficientwise full-support extension does not change its surviving signs; and a finite endpoint correction cannot erase the explicit negative quartet test. The spaces and maps exposed by these statements are ISP20–ISP21, ISP23–ISP28, and ISP34–ISP43. They retain the objects on which a further arithmetic correction must act.

## 10. The endpoint pairing also has a computable sign

For this quartet polynomial,
\[
h(0)=h(1)=\bigl(|\rho|^2|1-\rho|^2\bigr)^m>0,
\qquad v(0)=v(1)=c_0:=1/h(0)>0.
\]
The first equality follows by grouping the conjugate factors and using the reflection permutation of the four roots. The second uses the exact convention \(g(0)=g(1)=1\) of WA1. Hence for endpoint vectors \(e(q)=(q(0),q(1))\), the pole pairing itself is
\[
\begin{aligned}
A_{q_1,q_2}(0)+A_{q_1,q_2}(1)
&=c_0^2\bigl(\overline{q_1(1)}q_2(0)+\overline{q_1(0)}q_2(1)\bigr)\\
&=e(q_1)^*\,c_0^2\begin{pmatrix}0&1\\1&0\end{pmatrix}e(q_2).
\end{aligned}
\tag{ISP44}
\]
Thus the pole contribution by itself has one positive and one negative endpoint direction. Evaluation onto \(\mathbb C^2\) is surjective by the polynomial \((1-s)c+sd\), so both directions occur. This computes the actual contribution already present in WA24; it does not assign an unproved coefficient to the additional prime \((e_L)\). The section ISP36 kills both of these directions while preserving every packet jet.

## 11. Exact finite verification

The reproducible script `check_infinitesimal_support_positivity.py` passed 38 exact symbolic checks, recorded in `INFINITESIMAL_SUPPORT_POSITIVITY_CHECKS.json`. The checks include the nilpotent/current identities, both signed eigenvectors, the first-order conjugation with a Hermitian matrix coupling the current plane to its complement, the full characteristic polynomial, the current-to-packet isometry and intertwiner, every retained jet in a multiplicity-two quartet example, endpoint vanishing through order two in the higher-order section, the singular-block square-completion identity, and the eight exact module/metric identities of ISP46–ISP53. The calculations use exact rational and symbolic coefficients. The finite sample points are not asserted to be zeta zeros. These checks support the displayed algebraic calculations; they do not replace the general proofs above or assert a new analytic positivity theorem.


## 12. The positive escaping trace and the original observed metric

The escaping-family isomorphism EFI52–EFI55 uses the exact base map \(a_{\rm esc}=-\lambda^2/4\) and coordinate \(r_{\rm esc}=z_{\rm obs}-\lambda/2\). Along the real displacement \(s-s_*\), the observed coefficient \(\lambda=a(s-s_*)\) is real. Its algebra multiplication trace in the basis \(1,z_{\rm obs}\) is
\[
G_{\mathrm{tr}}(\lambda)=\begin{pmatrix}2&\lambda\\\lambda&\lambda^2\end{pmatrix}.
\tag{ISP45}
\]
Indeed \(z_{\rm obs}^2=\lambda z_{\rm obs}\), multiplication by \(z_{\rm obs}\) has trace \(\lambda\), and multiplication by its square has trace \(\lambda^2\), while the identity has trace two. The centered coordinate \(r_{\rm esc}=z_{\rm obs}-\lambda/2\) gives the congruent matrix \(\operatorname{diag}(2,\lambda^2/2)\). Thus this form is positive definite for real \(\lambda\ne0\), and has one-dimensional radical at zero. The following calculation gives its exact relationship to the original metric and current.


Write \(z=z_{\rm obs}\) for the retained observed generator. Retain \(S=\operatorname{span}\{g,h\}\) with its original orthonormal frame, and \(b=\epsilon\sqrt\Delta>0\). The supported receiver is
\[
\rho_\lambda:\mathbb C[z]/(z^2-\lambda z)\longrightarrow\operatorname{End}(S),
\quad 1\mapsto I_S,\quad z\mapsto F_\lambda=
\begin{pmatrix}\lambda&0\\b&0\end{pmatrix}.
\tag{ISP46}
\]
It is a homomorphism because \(F_\lambda^2=\lambda F_\lambda\). It is injective: a linear relation \(cI_S+dF_\lambda=0\) applied to \(h\) gives \(c=0\), and applied to \(g\) then gives \(db=0\). The cyclic module map from its regular representation to \(S\) is
\[
T_\lambda:\mathbb C[z]/(z^2-\lambda z)\longrightarrow S,
\quad 1\mapsto g,\quad z\mapsto\lambda g+bh,
\quad [T_\lambda]_{(1,z),(g,h)}=
\begin{pmatrix}1&\lambda\\0&b\end{pmatrix}.
\tag{ISP47}
\]
Its determinant is \(b\ne0\). Direct multiplication proves \(F_\lambda T_\lambda=T_\lambda M_z\), where \(M_z=\left(\begin{smallmatrix}0&0\\1&\lambda\end{smallmatrix}\right)\). Thus regular multiplication and the supported receiver have the same ordinary traces.

The algebra involution used in ISP45 fixes \(z\) when \(\lambda\) is real. Its image is not fixed by the original matrix adjoint:
\[
\rho_\lambda(z^*)-\rho_\lambda(z)^*
=F_\lambda-F_\lambda^*=-iW_*,
\quad W_*=\begin{pmatrix}0&-ib\\ib&0\end{pmatrix}.
\tag{ISP48}
\]
The equality follows by conjugate transposition. It is nonzero for every real \(\lambda\), including zero. Thus the exact map relating the forms is a faithful algebra receiver with this specified adjoint defect.

There are three retained Hermitian forms on the same two-dimensional coordinate space. The algebra multiplication trace gives ISP45. Pulling back the original vector metric through ISP47 gives
\[
G_{\mathrm{vec}}=T_\lambda^*T_\lambda
=\begin{pmatrix}1&\lambda\\\lambda&\lambda^2+b^2\end{pmatrix}.
\tag{ISP49}
\]
Pulling back the matrix Hilbert–Schmidt metric through ISP46 gives
\[
G_{\mathrm{HS}}=
\begin{pmatrix}
\operatorname{Tr}(I_S)&\operatorname{Tr}(F_\lambda)\\
\operatorname{Tr}(F_\lambda^*)&\operatorname{Tr}(F_\lambda^*F_\lambda)
\end{pmatrix}
=\begin{pmatrix}2&\lambda\\\lambda&\lambda^2+b^2\end{pmatrix}.
\tag{ISP50}
\]
Every entry follows by multiplying the displayed matrix \(F_\lambda\). In particular
\[
G_{\mathrm{HS}}-G_{\mathrm{tr}}
=\begin{pmatrix}0&0\\0&b^2\end{pmatrix},
\qquad \|\rho_0(z)\|_{\mathrm{HS}}^2=b^2>0.
\tag{ISP51}
\]
The trace-null generator at collision has a nonzero, exactly measured operator norm. The supported unit in ISP46 has rank two. Using instead the full unital receiver \(1\mapsto I_B\) changes the upper-left entry of ISP50 to \(\dim B\); it does not change its other three entries.

The trace pairing makes multiplication by the real generator self-adjoint, as matrix multiplication verifies:
\[
G_{\mathrm{tr}}M_z=M_z^*G_{\mathrm{tr}}.
\]
For the positive matrix metric the exact defect is instead
\[
G_{\mathrm{HS}}M_z-M_z^*G_{\mathrm{HS}}
=\begin{pmatrix}0&-b^2\\b^2&0\end{pmatrix}.
\tag{ISP52}
\]
This is obtained by subtracting the two products, with no limiting argument. Thus the extra positive term in ISP51 has a specified effect on multiplication adjoints; it cannot be added while asserting unchanged adjoint compatibility.

Finally, transporting the trace form itself to the original vector plane gives
\[
Q_\lambda=(T_\lambda^{-1})^*G_{\mathrm{tr}}T_\lambda^{-1}
=\begin{pmatrix}2&-\lambda/b\\-\lambda/b&\lambda^2/b^2\end{pmatrix},
\quad\det Q_\lambda=\lambda^2/b^2.
\tag{ISP53}
\]
The inverse \(T_\lambda^{-1}=\left(\begin{smallmatrix}1&-\lambda/b\\0&1/b\end{smallmatrix}\right)\) proves the formula by multiplication. This positive metric for \(\lambda\ne0\) makes \(F_\lambda\) self-adjoint; at the collision it becomes degenerate and kills \(h\). There cannot be a positive definite metric making the nonzero \(N=bhg^*\) self-adjoint: that would imply \(\langle Nx,Nx\rangle=\langle x,N^2x\rangle=0\) for every \(x\), forcing \(N=0\). The explicitly constructed degenerate metric ISP53 is the retained limiting object, while the original positive metric and the current \(W_*\) remain unchanged.

The Hermitian summand \(C_B\) of the full arithmetic operator remains in ISP12–ISP14. The present algebra comparison concerns \(F_\lambda\), and makes no commutation assertion about \(C_B\) or identification of the trace metric with the classical Weil form.


![The same nonzero infinitesimal has zero algebraic trace and nonzero matrix norm; its current has both signs in the original metric. Proof: ISP5–ISP6, ISP18–ISP20, ISP45–ISP53.](figures/26_infinitesimal_forms.png)

\clearpage

# The logarithmic arithmetic distribution of the separated-support zeta sheet

This calculation uses the actual interpolation in the programme's *Secondary Note on Split-Zero Globalization*, canonical source PUBUNIT-B1A260A5E731EA568C353AA4, equations under `def:hurwitz-specialization`, `thm:universal-taylor-deformation`, `thm:arithmetic-kernels-riemann`, and `cor:first-log-jet-explicit`. It also uses *Split-Zero Support Repair*, `some considerrations.tex`, sections “Conservative ideal and zeta side” and “Shifted zeta deformation”. These are prior programme results. The supported-zero prime is also a prior result of Paper 1, attributed by the user to Gemini Pro 2.5. The calculation below derives the signed arithmetic distribution that replaces the prime-power distribution for this particular separated sheet. It does not assign an arbitrary finite norm to the supported-zero prime.

## NL1. The original scalar maps and the actual analytic family

Let \(R=\mathbb Z\), and let \(G(R)=R\sqcup\{\tau\}\). Addition and multiplication on supported elements are their ring operations; \(\tau+x=x\) and \(\tau x=\tau\). Write \(e=0_R\), so \(e\ne\tau\), \(e^2=e\), and \(er=e\) for every supported \(r\). The two maps
\[
p:G(R)\to R,\quad p(r)=r,\ p(\tau)=0,
\qquad
\chi:G(R)\to\mathbb B,\quad \chi(r)=1,\ \chi(\tau)=0
\tag{NL1}
\]
preserve both operations and units, directly by these laws. The prime ideal \((e)=\{\tau,e\}\) is \(p^{-1}(0)\); its complement consists of nonzero integers and is multiplicatively closed. This proves its primality without identifying its generator with the semiring zero.

The separated residue map \(G(\mathbb Z)\to G(\mathbb Z/n\mathbb Z)\), obtained by reducing the supported amplitude and keeping \(\tau\), has target cardinality \(n+1\). This holds also for \(n=1\): the zero ring has a supported zero and the distinct \(\tau\). Composing with amplitude gives \(\mathbb Z/n\mathbb Z\), of cardinality \(n\). Thus the two defined sums are
\[
F_0(s)=\sum_{n\ge1}n^{-s}=\zeta(s),\qquad
F_1(s)=\sum_{n\ge1}(n+1)^{-s}=\zeta(s)-1.
\tag{NL2}
\]
Their interpolation is
\[
F_t(s)=\sum_{n\ge1}(n+t)^{-s}=\zeta(s,1+t),\qquad t\ge0,\quad\Re s>1.
\tag{NL3}
\]
Here \(t\) is a real shift parameter, not the semiring element \(\tau\). The equality with Hurwitz zeta is the defining series with its index translated; compare the original TeX formulas at [DLMF 25.11.1](https://dlmf.nist.gov/25.11.E1) and [25.11.3](https://dlmf.nist.gov/25.11.E3).

The prime \((e)\) cannot be inserted into the old ideal Euler product with a positive finite multiplicative norm extending the integer ideal norm. Indeed \((e)I_{(n)}=(e)\); a multiplicative norm \(h\) would satisfy \(h((e))=n h((e))\), so \(h((e))=0\) for \(n=2\). This equality specifies the obstruction. The separated residue sum (NL3) is a different, already defined analytic receiver of support. Its logarithmic distribution is now calculated in full.

## NL2. A convergent expansion with every multiplicative interaction retained

Put
\[
b=1+t,\qquad r_n=\frac{n+t}{1+t}\quad(n\ge2),\qquad
H_t(s)=\sum_{n\ge2}r_n^{-s}.
\tag{NL4}
\]
Every \(r_n>1\), and
\[
F_t(s)=b^{-s}(1+H_t(s)).
\tag{NL5}
\]
There exists \(\sigma_0>1\) with \(H_t(\sigma_0)<1\). To prove this, fix any \(\sigma_1>1\). The terms \(r_n^{-\sigma}\) tend to zero as \(\sigma\to\infty\), and for \(\sigma\ge\sigma_1\) they are dominated by the summable sequence \(r_n^{-\sigma_1}\). Dominated convergence gives \(H_t(\sigma)\to0\).

On every closed half-plane \(\Re s\ge\sigma_0\) with \(H_t(\sigma_0)<1\), the series
\[
\log F_t(s)=-s\log b+
\sum_{k\ge1}\frac{(-1)^{k+1}}{k}
\sum_{n_1,\ldots,n_k\ge2}
(r_{n_1}\cdots r_{n_k})^{-s}
\tag{NL6}
\]
uses the holomorphic logarithm of \(1+H_t\) defined by its power series. Its absolute sum is at most \(\sum_{k\ge1}H_t(\sigma_0)^k/k<\infty\). Differentiation is locally uniformly justified: for a slightly smaller abscissa still exceeding 1 and with \(H_t<1\),
\[
J_t(\sigma)=\sum_{n\ge2}(\log r_n)r_n^{-\sigma}<\infty,
\]
and the absolute sum of the differentiated length terms of length \(k\), after the factor \(1/k\), is \(J_t(\sigma)H_t(\sigma)^{k-1}\). Summing this geometric bound proves
\[
-\frac{F_t'(s)}{F_t(s)}
=\log b+
\sum_{k\ge1}\frac{(-1)^{k+1}}{k}
\sum_{n_1,\ldots,n_k\ge2}
\log(r_{n_1}\cdots r_{n_k})
(r_{n_1}\cdots r_{n_k})^{-s}.
\tag{NL7}
\]
No factor indexed by an ordinary prime has been assumed.

Define the signed measure on \([0,\infty)\)
\[
\nu_t=(\log b)\delta_0+
\sum_{k\ge1}\frac{(-1)^{k+1}}k
\sum_{n_1,\ldots,n_k\ge2}
\ell(n_1,\ldots,n_k)\delta_{\ell(n_1,\ldots,n_k)},
\quad
\ell(n_1,\ldots,n_k)=\sum_i\log r_{n_i}.
\tag{NL8}
\]
It is locally finite: if \(\ell\le M\), then \(k\le M/\log r_2\), and every \(r_{n_i}\le e^M\), leaving finitely many tuples. Equal lengths are added with their exact signed multiplicities. The same bound proving (NL7) gives \(\int e^{-\sigma\ell}|d\nu_t|<\infty\) in the stated right half-plane. Its Laplace transform is exactly \(-F_t'/F_t\).

## NL3. An explicit negative arithmetic atom at the separated endpoint

At \(t=1\), \(b=2\), \(r_n=(n+1)/2\), and
\[
H_1(4)=\sum_{m\ge3}(2/m)^4
\le\frac{16}{81}+\int_3^\infty16x^{-4}\,dx
=\frac{32}{81}<1.
\tag{NL9}
\]
Thus (NL7) holds, in particular, for \(\Re s\ge4\), with the convergence estimate just proved. There is a positive atom
\[
\nu_1(\{\log(3/2)\})=\log(3/2).
\tag{NL10}
\]
Only the one-term tuple \(n_1=2\) has that length: a tuple of at least two terms has product at least \((3/2)^2\).

There is also the exact negative atom
\[
\boxed{\nu_1(\{\log(9/4)\})=-\log(3/2).}
\tag{NL11}
\]
For a one-term tuple, \((n+1)/2=9/4\) would give \(n=7/2\), impossible. A tuple of at least three terms has product at least \(27/8>9/4\). For two terms both factors are at least \(3/2\), so equality forces both to be \(3/2\), that is, the single ordered tuple \((2,2)\). Its coefficient in (NL8) is \(-\tfrac12\log(9/4)=-\log(3/2)\). This proves (NL11) with no truncation.

Consequently the logarithmic arithmetic distribution for the actual separated sheet is signed. The original von Mangoldt distribution, \(\sum_{n\ge2}\Lambda(n)\delta_{\log n}\), cannot be reused for this sheet. The negative atom alone is not a negative value of the full Weil form: the gamma, divisor, reflection-defect, and boundary terms of a complete contour identity must also be retained. It is an exact arithmetic coefficient that such an identity must contain.

## NL4. The first infinitesimal is nonzero and contains mixed prime data

For \(|t|<1\), the binomial series gives, locally uniformly for \(\Re s>1\),
\[
F_t(s)=\zeta(s)-t\,s\zeta(s+1)+O(t^2).
\tag{NL12}
\]
For completeness, fix a compact set of \(s\) and a radius \(r<1\). The Taylor remainder in \((1+t/n)^{-s}\) is bounded by a constant times \(|t|^2/n^2\), uniformly on that compact set; after multiplication by \(n^{-s}\) it is summable. This proves the asserted termwise expansion and its holomorphic derivatives.

The Euler product of \(\zeta\), used only at \(t=0\), gives
\[
Q(s)=\frac{\zeta(s+1)}{\zeta(s)}
=\sum_{n\ge1}\alpha(n)n^{-s},\qquad
\alpha(1)=1,\quad
\alpha(n)=(-1)^{\omega(n)}\frac{\prod_{p\mid n}(p-1)}{n}.
\tag{NL13}
\]
Indeed the local series is
\[
\frac{1-p^{-s}}{1-p^{-s-1}}
=1-\sum_{j\ge1}\frac{p-1}{p^j}p^{-js}.
\]
Its absolute product converges for \(\Re s>1\); multiplying the series proves (NL13). Thus
\[
\left.\partial_t\log F_t(s)\right|_{t=0}=-sQ(s),
\qquad
\left.\partial_t\left(-\frac{F_t'}{F_t}\right)\right|_{t=0}
=Q(s)+sQ'(s)
=\sum_{n\ge1}\alpha(n)(1-s\log n)n^{-s}.
\tag{NL14}
\]
The derivative series is absolutely convergent on compact subsets of \(\Re s>1\), since \(|\alpha(n)|\le1\) and \(\sum(1+\log n)n^{-\sigma}<\infty\). For real \(s>1\), \(sQ(s)>0\), so the first deformation of \(\log F_t\) does not vanish. This infinitesimal is not the first-order-trivial node deformation from the observed collision.

Equation (NL14) is equivalently the Laplace transform of the locally finite distribution
\[
\dot\nu_0=
\sum_{n\ge1}\alpha(n)
\bigl(\delta_{\log n}-(\log n)\delta'_{\log n}\bigr).
\tag{NL15}
\]
Here \(\langle\delta'_\ell,f\rangle=-f'(\ell)\), so its Laplace transform is \(s e^{-s\ell}\). This fixes the derivative sign in (NL15).

The dot also denotes the actual distributional derivative of (NL8), not only a matching transform. On a fixed compact length interval and for \(0\le t\le1\), the inequalities \(r_2(t)\ge3/2\) and \(r_n(t)\ge(n+1)/2\) give a uniform finite bound on the tuples which can enter. Differentiating their smooth moving atoms therefore defines the derivative on every compactly supported smooth test. For weighted Laplace tests, \(|\partial_t\log r_n|\le1\). A tuple of length \(k\) has length derivative bounded by \(k\); differentiating its coefficient and its exponential introduces at most one further factor \(k\), together with its original length. On a sufficiently far right half-plane, uniformly in a neighborhood of zero, the sums are bounded by geometric series of the forms \(\sum k B^k\) and \(\sum k D B^{k-1}\), with \(B<1\) and \(D<\infty\) as above. Thus Laplace transformation commutes with differentiation. At zero all tuple lengths are logs of positive integers. The resulting distribution has the form \(\sum_n(a_n\delta_{\log n}+b_n\delta'_{\log n})\). These coefficients are uniquely determined by its Laplace transform: multiply the difference of two such transforms by the exponential of its least remaining length and let the real argument tend to infinity; the leading polynomial of degree at most one must be zero, and induction removes every length. The exponentially weighted convergence just proved bounds the remaining tail in each step. Comparing with (NL14) proves exactly \(a_n=\alpha(n)\), \(b_n=-(\log n)\alpha(n)\), as in (NL15).

For distinct primes \(p,q\),
\[
\alpha(pq)=\frac{(p-1)(q-1)}{pq}\ne0.
\tag{NL16}
\]
These are supported at products of distinct primes, whereas the original von Mangoldt coefficients vanish there. The deformation therefore has explicitly nonzero mixed-prime terms already at first order; they cannot be removed by keeping only a modified weight at each prime power.

## NL5. Full finite support and exact specialization

For a finite bounded distributive support lattice \(L\), the actual set is
\[
G_L(R)=\{(0,\lambda):\lambda\in L\}\cup\{(r,1_L):r\in R\}.
\tag{NL17}
\]
Let \(c=|L|-1\). Its separated residue over \(\mathbb Z/n\mathbb Z\) has \(n+c\) elements: \(n\) supported top elements and \(|L|-1\) lower support elements. Hence its scalar cardinality receiver is
\[
F_c(s)=\sum_{n\ge1}(n+c)^{-s}
=\zeta(s)-\sum_{n=1}^{c}n^{-s}.
\tag{NL18}
\]
This proves exactly how (NL3) receives the full support count. It does not identify different support labels with one another in \(G_L\). The cardinality map forgets that distinction; the full meet-algebra coefficients and their primitive idempotents remain separate in the programme's full-support reconstruction. Formula (NL8) applies with \(t=c\) to the count receiver. All logarithmic product tuples, including their collisions in the length variable, are retained.

## NL6. Consequence for the positivity calculation

There are three exact facts to carry forward. First, the supported-zero prime remains a nontrivial prime of \(G(\mathbb Z)\); no positive finite multiplicative ideal norm extending the old norm can give it an ordinary new Euler factor. Second, the programme already supplies a different analytic receiver, the separated quotient-size interpolation (NL3), whose logarithmic derivative is (NL7), with the explicit signed atom (NL11). Third, its infinitesimal variation is (NL14), not zero. A corrected explicit formula for this receiver must use these arithmetic terms and its own completed divisor. The exact escaping-fibre trace and observed-operator current are calculated in the accompanying derivations; equality with a Weil form requires the actual map, not an identification of their names.

The two primitive-defect source files in folders 3 and 4 are byte-identical (SHA256 `2f3289f6a04105d3f15fe5f7c36dde286515e61f465caf1582f9808e19f3d2f7`). Their negative augmentation retains the kernel of a scalar cancellation. That same instruction is followed here: the full signed length distribution (NL8) and mixed-prime distribution (NL15) are retained rather than discarded when an ordinary Euler presentation fails.


![All nonzero positive-length atoms through ratio 3, and the exact first arithmetic coefficients; the zero-length mass is stated separately. Proof: NL7–NL16.](figures/24_non_eulerian_lengths.png)

\clearpage

# The actual separated zeta sheet, its explicit formula, and its positivity defect

This calculation uses the quotient-size interpolation in the supplied original LaTeX. It retains the supported arithmetic zero \(e\), the unsupported element \(\tau\), the distinct residue quotients, the completed-function endpoint residues, every gamma pole crossed by the contour, and the functional-equation defect. The final countertest concerns this particular shifted zeta sheet. It is not a counterexample to the classical Riemann hypothesis.

Source coverage for this derivation: `globalization nte/2/split_zero_secondary_note.tex`, lines 1111–1555, read in full; `globalization nte/4/split_zero_defect_preprint (1).tex`, lines 500–854, read in full; the standing definitions, quotient sheets, and shifted-deformation sections of `globalization nte/5/some considerrations.tex` were read in the returned source text. The whole-file read of the latter was truncated in an unrelated middle section and is not recorded as complete. The relevant named results are `thm:universal-taylor-deformation`, `cor:jets`, `thm:arithmetic-kernels-riemann`, `cor:first-log-jet-explicit`, `prop:hurwitz-standard-package`, and the defect preprint's “Endpoint residues” and “Invariant/anti-invariant decomposition.” The secondary note lists The Clankers; `some considerrations.tex` lists "The Clankers / prepared in continuation"; the defect preprint has a blank author field. The source-reading ledger maintained by the root task records canonical source IDs. This file supplies the additional proofs below; it does not claim those older formulas as new.

## SW1. The typed quotient maps and the interpolation they actually give

Let \(S=G(\mathbb Z)=\mathbb Z\sqcup\{\tau\}\), with \(e=0_{\mathbb Z}\ne\tau\). For \(n\ge1\), the two successive surjections are
\[
S\xrightarrow{\pi_n}G(\mathbb Z/n\mathbb Z)
\xrightarrow{p_n}\mathbb Z/n\mathbb Z,
\qquad
\pi_n(\tau)=\tau_n,\quad \pi_n(a)=a\bmod n,
\quad p_n(\tau_n)=0.
\tag{SW1}
\]
The first target has \(n+1\) elements, and the second has \(n\). Their zero fibres in the source are respectively \(\{\tau\}\) and \(\{\tau\}\cup n\mathbb Z\). These statements follow directly from the definitions, including at \(n=1\), when the first quotient has two elements.

The two Dirichlet sums, and the supplied interpolation between their numerical weights, are
\[
F_t(s)=\sum_{n\ge1}(n+t)^{-s}=\zeta(s,1+t),\qquad
F_0=\zeta,\quad F_1=\zeta-1,
\quad 0\le t\le1.
\tag{SW2}
\]
Initially these equalities hold for \(\Re s>1\). The identity at \(t=1\) is a change of index in an absolutely convergent series. The intermediate values are numerical interpolation of the cardinality weights; they are not asserted to count a nonintegral number of elements in a quotient.

In particular, SW2 is not the separate prime-weight Euler product \(\prod_p(1-(p+1)^{-s})^{-1}\). Its distinction from that product is proved with the actual quotient maps in TN1–TN9 of [prime-norm comparison proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/TAU_WEIL_NORM_RECONSTRUCTION.md). For example the weights satisfy \((m+1)(n+1)-(mn+1)=m+n\); retaining the labels gives the multiplicative vector \((1,n)\), while summing its entries gives the nonmultiplicative number \(n+1\).

## SW2. Analytic continuation and estimates used below

Write \(a=1+t\in[1,2]\). For any integer \(M\ge1\), Euler summation with \(2M\) derivatives gives
\[
\begin{split}
F_t(s)={}&\frac{a^{1-s}}{s-1}+\frac{a^{-s}}2
 +\sum_{j=1}^{M}\frac{B_{2j}}{(2j)!}(s)_{2j-1}a^{1-s-2j}\\
&-\frac{(s)_{2M}}{(2M)!}
\int_0^\infty \widetilde B_{2M}(x)(x+a)^{-s-2M}\,dx,
\qquad \Re s>1-2M.
\end{split}
\tag{SW3}
\]
Here \(\widetilde B_k(x)=B_k(\{x\})\), and \((s)_j=s(s+1)\cdots(s+j-1)\). To check the formula, apply integration by parts on every interval \([n,n+1]\), using \(B_k'=kB_{k-1}\), \(B_k(1)=B_k(0)\) for \(k\ne1\), and \(B_1(1)-B_1(0)=1\). Summing the first boundary jumps gives the values \((n+a)^{-s}\). The remaining boundaries at the lower end are the displayed half-value and even Bernoulli terms; the upper boundaries tend to zero for \(\Re s>1\). The derivative of order \(j\) of \((x+a)^{-s}\) is \((-1)^j(s)_j(x+a)^{-s-j}\), giving the sign of the remainder. This proves SW3 first for \(\Re s>1\). Since \(\widetilde B_{2M}\) is bounded, its integral is absolutely and locally uniformly convergent for \(\Re s>1-2M\), so it proves the asserted continuation there.

Letting \(M\) increase proves that \(F_t\) is meromorphic on \(\mathbb C\) with its sole pole at 1, simple of residue 1. On each fixed vertical strip, away from that pole, SW3 bounds \(F_t(s)\) by a fixed polynomial in \(1+|\Im s|\), uniformly for \(t\in[0,1]\). Indeed choose \(2M\) larger than one minus the left edge; the integral of \((x+a)^{-\Re s-2M}\) is bounded uniformly on that strip, and \((s)_{2M}\) is a polynomial. Derivatives in \(s\) satisfy the same kind of bound by Cauchy's formula in a slightly larger strip. These estimates, rather than a numerical approximation to a zero sum, justify every infinite vertical integral below.

## SW3. The first infinitesimal is explicit and does not vanish

Termwise differentiation, dominated uniformly on compact subsets of \(\Re s>1\), gives
\[
\partial_t F_t(s)=-sF_t(s+1),\qquad
\partial_t^jF_t(s)=(-1)^j(s)_j F_t(s+j).
\tag{SW4}
\]
Analytic continuation gives these meromorphic identities everywhere. In the dual-number ring \(\mathbb C[\epsilon]/(\epsilon^2)\), the precise specialization is
\[
F_\epsilon(s)=\zeta(s)-\epsilon s\zeta(s+1),\qquad
\log F_\epsilon=\log\zeta-\epsilon Q,
\quad Q(s)=s\frac{\zeta(s+1)}{\zeta(s)}.
\tag{SW5}
\]
The logarithm equality is local on any open set where \(\zeta\ne0,\infty\); its differentiated form is a global meromorphic identity. In particular
\[
\left.\partial_t\frac{F_t'}{F_t}\right|_{t=0}=-Q'(s),
\qquad
\left.\partial_t\left(-\frac{F_t'}{F_t}\right)\right|_{t=0}=Q'(s).
\tag{SW6}
\]
The nilpotence \(\epsilon^2=0\) does not make the coefficient of \(\epsilon\) zero: at \(s=2\), that coefficient in \(F_\epsilon\) is \(-2\zeta(3)\ne0\).

For \(\Re s>1\), multiplying the absolutely convergent series of \(1/\zeta(s)\) and \(\zeta(s+1)\) yields
\[
Q(s)=s\sum_{n\ge1}\alpha(n)n^{-s},\quad
\alpha(1)=1,\qquad
\alpha(n)=(-1)^{\omega(n)}\frac{\prod_{p\mid n}(p-1)}n.
\tag{SW7}
\]
The local factor is
\((1-p^{-s})/(1-p^{-s-1})=1-\sum_{k\ge1}(p-1)p^{-k}p^{-ks}\), which proves the displayed coefficients. Their series is absolutely convergent on \(\Re s>1\), also after one logarithmic differentiation. Thus
\[
Q'(s)=\sum_{n\ge1}\alpha(n)(1-s\log n)n^{-s}.
\tag{SW8}
\]
This first jet includes all squarefree-prime support combinations in \(\alpha(n)\); it is not a single new prime-power term.

## SW4. Endpoint residues, logarithmic orders, and the full reflection defect

Use exactly the supplied completion
\[
\Lambda_t(s)=\pi^{-s/2}\Gamma(s/2)F_t(s),\qquad
\ell_t(s)=\Lambda_t'(s)/\Lambda_t(s).
\tag{SW9}
\]
SW3 at zero, or the first Bernoulli polynomial, gives \(F_t(0)=-1/2-t\). Hence
\[
\operatorname {Res}_0\Lambda_t=-1-2t,\qquad
\operatorname {Res}_1\Lambda_t=1,
\quad
\operatorname {PP}_{0,1}\Lambda_t
=\frac{1+t}{s(s-1)}-t\frac{2s-1}{s(s-1)}.
\tag{SW10}
\]
Both poles are simple for \(0\le t\le1\). Consequently
\[
\operatorname {Res}_0\ell_t=\operatorname {Res}_1\ell_t=-1.
\tag{SW11}
\]
For proof, a nonzero principal coefficient gives \(\Lambda_t=(s-b)^{-1}u_t(s)\), with \(u_t(b)\ne0\); its logarithmic derivative is \(-1/(s-b)+u_t'/u_t\). Thus the weight of the endpoint in a logarithmic explicit formula is its order, not the coefficient \(-1-2t\) of the original completed function.

At every negative even integer \(-2j\), \(j\ge1\), the precise order is
\[
\operatorname {ord}_{-2j}\Lambda_t
=\operatorname {ord}_{-2j}F_t-1.
\tag{SW12}
\]
This formula also retains exceptional parameter values at which a Hurwitz zero cancels a gamma pole. At \(t=1\), \(F_1(-2j)=-1\), so all these completed poles are present and simple. In particular multiplying only by \(s(s-1)\) does not make \(\Lambda_1\) entire.

Define the additive and logarithmic reflection defects by
\[
\Delta_t(s)=\Lambda_t(s)-\Lambda_t(1-s),\qquad
d_t(s)=\ell_t(s)+\ell_t(1-s)
=\frac d{ds}\log\frac{\Lambda_t(s)}{\Lambda_t(1-s)}.
\tag{SW13}
\]
These are explicit meromorphic objects. Their signs follow by the chain rule. At \(t=0\), the classical functional equation gives both defects zero. SW5–SW6 give the complete infinitesimal logarithmic defect
\[
\dot d_0(s)=-Q'(s)-Q'(1-s).
\tag{SW14}
\]
Its endpoint residues vanish because \(Q\) is regular at both endpoints: \(Q(0)=-2\), from \(s\zeta(s+1)\to1\), and \(Q(1)=0\). This vanishing is only a statement about these two residues. It does not set SW14 or the moving zero divisor to zero.

## SW5. Exact contour identity before invoking any positivity

For entire functions \(f,g\), set
\[
f^\#(s)=\overline{f(1-\bar s)},\qquad A(s)=f^\#(s)g(s),
\quad K(u)=A(1/2+iu),\quad
k(v)=\frac1{2\pi}\int_{\mathbb R}K(u)e^{iuv}\,du.
\tag{SW15}
\]
In the formulas below the entire tests have Gaussian decay, up to a polynomial factor, in each fixed vertical strip. We construct such tests explicitly in SW9. The more general finite-rectangle residue identity requires no decay hypothesis.

Fix \(c>1\) and let \(a_c=1-c\). First take a finite rectangle with these two real edges and imaginary edges \(\pm T\), avoiding nonremovable poles on its boundary. The residue theorem gives
\[
\frac1{2\pi i}\oint\ell_t(s)A(s)\,ds
=\sum_{F_t(\rho)=0\ \mathrm{inside}}m_\rho A(\rho)
-A(1)-\sum_{j\ge0:\,-2j\ \mathrm{inside}}A(-2j).
\tag{SW16}
\]
Zeros and gamma poles are written separately, so exact cancellations in SW12 occur by addition of their integer orders. All quantities in SW16 are finite.

If \(\ell_t A\), \(\ell_t(s)A(1-s)\), and \(\ell_t(1-s)A(1-s)\) have only finitely many nonremovable poles in the strip and their horizontal integrals tend to zero, then taking \(T\to\infty\) gives
\[
\begin{split}
Z_{t,c}(A)-A(1)-\sum_{j\ge0:\,-2j>1-c}A(-2j)
={}&\frac1{2\pi i}\int_{\Re s=c}
\ell_t(s)(A(s)+A(1-s))\,ds\\
&-\frac1{2\pi i}\int_{\Re s=c}d_t(s)A(1-s)\,ds.
\end{split}
\tag{SW17}
\]
Here \(Z_{t,c}(A)\) is the finite sum of the zero terms not annihilated by \(A\), counted with multiplicity. The actual tests in SW9 satisfy every property in this sentence by a displayed cancellation identity, so SW17 is used below without a missing analytic assumption. For the sign, the left upward integral becomes the right upward integral of \(\ell_t(1-s)A(1-s)\); the positive contour subtracts it. Substituting \(\ell_t(1-s)=d_t(s)-\ell_t(s)\) proves SW17.

## SW6. The non-Eulerian arithmetic term and the completed formula

Put \(a=1+t\), \(r_n=(n+t)/a\) for \(n\ge2\), and choose \(c\) so large that \(\sum_{n\ge2}r_n^{-c}<1\). Write \(r_{\boldsymbol n}=\prod_{i=1}^k r_{n_i}\). Absolute convergence of the logarithm series gives
\[
-\frac{F_t'}{F_t}(s)=\log a+
\sum_{k\ge1}\frac{(-1)^{k+1}}k
\sum_{n_1,\ldots,n_k\ge2}
\log r_{\boldsymbol n}\,r_{\boldsymbol n}^{-s}.
\tag{SW18}
\]
To verify differentiation and absolute convergence, take a slightly smaller real part on which the sum is still less than 1. Its positive margin bounds the differentiated geometric series. Explicitly, if \(B(c)=\sum r_n^{-c}<1\) and \(D(c)=\sum(\log r_n)r_n^{-c}<\infty\), the sum of the absolute differentiated terms is \(\sum_{k\ge1}D(c)B(c)^{k-1}=D(c)/(1-B(c))\). The general-length derivation and its signed atoms are developed independently in [non-Eulerian length proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/NON_EULERIAN_LENGTH_DERIVATION.md).

Define the absolutely convergent functional
\[
\begin{split}
\mathcal L_t(k)={}&2\log(a)k(0)\\
&+\sum_{k_0\ge1}\frac{(-1)^{k_0+1}}{k_0}
\sum_{n_1,\ldots,n_{k_0}\ge2}
\frac{\log r_{\boldsymbol n}}{\sqrt{r_{\boldsymbol n}}}
\left[k(\log r_{\boldsymbol n})+k(-\log r_{\boldsymbol n})\right].
\end{split}
\tag{SW19}
\]
Gaussian strip decay implies \(|k(v)|\le C_R e^{-R|v|}\) for every fixed \(R>0\): shift the vertical contour defining \(k\) by \(R\) in the appropriate direction. Choose \(R=c-1/2\), or a slightly larger value, and the absolute majorant just proved for SW18 proves convergence of SW19. All exchanges of its sum and integral are therefore justified.

Let
\[
w_\infty(u)=\Re\psi(1/4+iu/2)-\log\pi,\qquad
\mathcal D_{t,c}(A)=\frac1{2\pi i}\int_{\Re s=c}d_t(s)A(1-s)\,ds.
\tag{SW20}
\]
Then SW17 is exactly
\[
\boxed{\begin{aligned}
Z_{t,c}(A)={}&A(1)+\sum_{j\ge0:\,-2j>1-c}A(-2j)\\
&+\frac1{2\pi}\int_{\mathbb R}K(u)w_\infty(u)\,du
-\mathcal L_t(k)-\mathcal D_{t,c}(A).
\end{aligned}}
\tag{SW21}
\]
For completeness, \(\ell_t=-\tfrac12\log\pi+\tfrac12\psi(s/2)+F_t'/F_t\). The gamma part can be moved from \(c\) to \(1/2\) without crossing a gamma pole, and reflection of the integration variable gives \(w_\infty\). The digamma series on \(\Re(s/2)>0\) bounds it polynomially, so Gaussian decay kills the horizontal edges. A term \(r^{-s}\) in SW18 integrates to \(r^{-1/2}[k(-\log r)+k(\log r)]\), by shifting its entire integrand to the critical line. The constant gives \(2\log(a)k(0)\). Finally the minus sign of \(\mathcal D\) is the sign derived in SW17. This proves every sign and endpoint contribution in SW21.

At \(t=0\), \(d_0=0\), and SW18 reduces to the usual logarithmic prime-power series. For tests annihilating the classical trivial zeros, \(A(-2j)=0\) for \(j\ge1\). SW21 then has exactly the two endpoints, archimedean term, and prime term in WA24. At \(t=1\), neither the negative-even terms nor \(\mathcal D_{1,c}\) can be dropped merely because the original endpoint principal part has been computed.

## SW7. Local variation of the original zero packet

Let \(\rho\) be an actual zero of \(\zeta\), of multiplicity \(m\), and take a small circle containing no other zero and neither endpoint. Its continuation as a zero cluster of \(F_t\) is counted by
\[
T_t(A)=\frac1{2\pi i}\oint \frac{F_t'(s)}{F_t(s)}A(s)\,ds.
\tag{SW22}
\]
The compact boundary is zero-free at \(t=0\), so uniform continuity makes it zero-free for all sufficiently small \(t\). The argument principle proves that this is the sum of \(A\) over the moving cluster, counted with multiplicities. Differentiating on that compact contour and integrating an exact derivative gives
\[
\dot T_0(A)=-\frac1{2\pi i}\oint Q'(s)A(s)\,ds
=\operatorname {Res}_{s=\rho}\bigl(Q(s)A'(s)\bigr).
\tag{SW23}
\]
The integration-by-parts equality follows from the zero contour integral of \((QA)'\). It does not require the zero to be simple. If it is simple, the result is
\[
\dot\rho(0)=\frac{\rho\zeta(\rho+1)}{\zeta'(\rho)},\qquad
\dot T_0(A)=\dot\rho(0)A'(\rho).
\tag{SW24}
\]
For a nontrivial zero, the numerator is nonzero because \(\rho\ne0\) and \(\Re(\rho+1)>1\). Thus a simple nontrivial zero has a nonzero first displacement in this interpolation. For a multiple zero, SW23 retains the full residue of order up to \(m\), rather than assuming a differentiable labeling of its individual branches.

The arithmetic first variation on the right-hand side is explicit as well. With the conventions of SW15, the integral of \(-Q'(s)(A(s)+A(1-s))\) on a right line is
\[
\sum_{n\ge1}\frac{\alpha(n)}{\sqrt n}
\left[
\left(\frac{\log n}2-1\right)(k(-\log n)+k(\log n))
+\log n\,(k'(-\log n)-k'(\log n))
\right].
\tag{SW25}
\]
To verify it, differentiation of the Fourier integral gives
\(\frac1{2\pi}\int(1/2+iu)K(u)e^{iuv}du=\tfrac12 k(v)+k'(v)\). Reflection replaces the second derivative term by its negative. Insert SW7 and differentiate termwise. Absolute convergence follows from the same exponential contour bounds for \(k,k'\). The reflection correction SW14 remains alongside SW25; omitting it is not a deformation of the same contour identity.

## SW8. The exact symmetric lift and the missing Hermitian property

Let
\[
G_t(s)=(s-1)F_t(s),\qquad
H_t(s)=G_t(s)G_t(1-s)=-s(s-1)F_t(s)F_t(1-s).
\tag{SW26}
\]
Both \(G_t\) and \(H_t\) are entire by SW3. They have real conjugation symmetry, and \(H_t(1-s)=H_t(s)\). The actual map is the multiplicative norm for the involution on entire functions,
\[
N:\mathcal O(\mathbb C)\longrightarrow\mathcal O(\mathbb C)^{s\mapsto1-s},
\qquad N(G)(s)=G(s)G(1-s).
\tag{SW27}
\]
It satisfies \(N(G_1G_2)=N(G_1)N(G_2)\), and its divisor is the original divisor plus its reflected divisor, with multiplicities. It is not asserted to be additive or to preserve the zero count without doubling. On the critical line \(H_t(s)=|G_t(s)|^2\ge0\).

The zero pairing of \(H_t\), on finite packets closed under \(\rho\mapsto1-\bar\rho\), is Hermitian. Proof: applying complex conjugation and this permutation to \(\sum m_\rho\overline{f(1-\bar\rho)}g(\rho)\) exchanges \(f\) and \(g\). By contrast, a divisor lacking that permutation symmetry need not define a Hermitian form. The next calculation proves the failure, and a negative direction in the symmetric lift, for the specific endpoint \(t=1\).

## SW9. A fully explicit negative test for the separated endpoint

The exact special values are
\[
F_1(-20)=-1,\qquad
F_1(-19)=\frac{174611}{6600}-1=\frac{168011}{6600}>0.
\tag{SW28}
\]
They follow from \(\zeta(-n)=-B_{n+1}/(n+1)\), \(B_{21}=0\), and \(B_{20}=-174611/330\), also obtainable from SW3. Continuity therefore gives at least one real zero in \((-20,-19)\). Define \(\alpha\) to be the least such real zero. This is well-defined: the endpoint values exclude neighborhoods of the two endpoints, and a nonzero holomorphic function has only finitely many zeros in the remaining compact interval. Write \(m\ge1\) for its exact multiplicity, and put \(\beta=1-\alpha\in(20,21)\).

Since \(F_1(\sigma)=\sum_{n\ge2}n^{-\sigma}>0\) for real \(\sigma>1\), \(\beta\) is not a zero of \(F_1\). The divisor of \(H_1\), however, has both \(\alpha\) and \(\beta\), each with multiplicity \(m\). Define
\[
h(s)=(s-\alpha)^m(s-\beta)^m,\qquad
W(s)=e^{(s-1/2)^2}\frac{H_1(s)}{h(s)}.
\tag{SW29}
\]
The quotient is entire, \(W(\alpha),W(\beta)\ne0\), and \(W^\#=W\). Indeed reflection exchanges the two factors of \(h\) with total sign \((-1)^{2m}=1\), and all the coefficients are real. SW3 proves that \(W\) and every fixed derivative are bounded by a polynomial times \(e^{-(\Im s)^2}\) on each fixed vertical strip; away from a bounded region the denominator is a polynomial bounded below by a positive constant times \(|\Im s|^{2m}\), and inside that region removability gives boundedness.

For arbitrary prescribed \(z_\alpha,z_\beta\in\mathbb C\), take the degree-at-most-one polynomial
\[
q(s)=\frac{z_\alpha}{W(\alpha)}\frac{s-\beta}{\alpha-\beta}
+\frac{z_\beta}{W(\beta)}\frac{s-\alpha}{\beta-\alpha},
\qquad f=qW,\quad A=f^\#f.
\tag{SW30}
\]
Then \(f(\alpha)=z_\alpha\) and \(f(\beta)=z_\beta\). At every other zero of \(H_1\), \(W\) vanishes at least to the full multiplicity. Therefore \(A\) annihilates all of those zero terms. Take the strip \(-21<\Re s<22\). Its native and symmetric zero functionals are exactly
\[
Z_{1,22}(A)=m\overline{z_\beta}z_\alpha,
\qquad
Z_{H_1}(A)=m(\overline{z_\beta}z_\alpha+\overline{z_\alpha}z_\beta).
\tag{SW31}
\]
No other zero contributes, including a multiple zero or a zero with large imaginary part, because of the preceding vanishing orders.

For \((z_\alpha,z_\beta)=(1,-1)\), this gives
\[
\boxed{Z_{1,22}(f^\#f)=-m<0,\qquad Z_{H_1}(f^\#f)=-2m<0.}
\tag{SW32}
\]
For \((z_\alpha,z_\beta)=(1,i)\), it gives
\[
\boxed{Z_{1,22}(f^\#f)=-im,}
\tag{SW33}
\]
which is not real. Thus the original shifted divisor pairing is not Hermitian, and the exact symmetric lift has a genuine negative direction. Nonnegativity of \(H_1\) as a function on the critical line, proved in SW8, does not imply nonnegativity of its zero pairing.

Here are the promised contour checks for the actual tests. Since
\[
\frac{H_1'}{H_1}A
=q^\#q\,e^{2(s-1/2)^2}\frac{H_1'H_1}{h^2},
\tag{SW34}
\]
the only possible nonremovable poles are at \(\alpha,\beta\). Every other zero is canceled as an identity of meromorphic functions. SW3 and its differentiated estimate bound the numerator polynomially on each strip, so the horizontal edges tend to zero with Gaussian speed. Likewise, using \(H_1=G_1G_1(1-s)\), each occurrence of \(F_1'/F_1\) or its reflected counterpart multiplied by \(A\) cancels a factor of \(F_1\) in \(H_1^2\). The same assertion holds for \(A(1-s)\), since its denominator is the same reflection-invariant \(h^2\). The remaining digamma factors have finitely many poles in this strip and at most polynomial growth on high horizontal edges, by the digamma recurrence and its convergent right-half-plane series. Consequently SW17–SW21 apply with no unproved horizontal zero-avoidance estimate.

At \(t=1,c=22\), the absolute logarithm expansion required in SW18 holds. For instance
\[
\sum_{n\ge2}\left(\frac2{n+1}\right)^{22}
\le\left(\frac23\right)^{22}
+\int_3^\infty\left(\frac2x\right)^{22}dx
=\left(\frac23\right)^{22}\left(1+\frac3{21}\right)<1.
\tag{SW35}
\]
Thus the corrected explicit formula evaluated on the negative test is the exact equality
\[
\boxed{
-m=A(1)+\sum_{j=0}^{10}A(-2j)
+\frac1{2\pi}\int_{\mathbb R}|f(1/2+iu)|^2w_\infty(u)du
-\mathcal L_1(k)-\mathcal D_{1,22}(A).
}
\tag{SW36}
\]
Every term is defined in SW15 and SW19–SW20, and every series and integral converges by the estimates above. This is a concrete positivity analysis of the actual non-Eulerian separated sheet, including its retained completion and reflection terms. It does not insert an arbitrary Euler factor for the supported-zero prime.

The tested divisor is the full shifted divisor in the strip \(-21<\Re s<22\), and its selected real zero lies outside the classical critical strip. Thus SW32 does not establish nonpositivity for a separately defined pairing restricted to \(0<\Re s<1\). Nor does it rule out a different boundary subtraction or a selected positivity cone. Such an operation must specify its map and retain the component it removes. The exact maps for this detected component are given next.

## SW10. The retained two-point object and its positive and negative projections

Keep the actual function \(W\) of SW29 and define the vector space
\[
V=W\mathbb C[s],\qquad
E:V\longrightarrow\mathbb C^2,\quad E(f)=(f(\alpha),f(\beta)).
\tag{SW37}
\]
Let \(j:\mathbb C^2\to V\) be the interpolation formula SW30. Direct evaluation proves \(Ej=\operatorname{id}\). Since \(W(\alpha),W(\beta)\ne0\), a polynomial multiple \(qW\) lies in \(\ker E\) precisely when \(q\) is divisible by both distinct linear factors. Hence
\[
K:=\ker E=W(s-\alpha)(s-\beta)\mathbb C[s],\qquad
V=j(\mathbb C^2)\oplus K.
\tag{SW38}
\]
The decomposition is explicit: \(f=jE(f)+(f-jE(f))\), and its second term lies in \(K\). An element of the intersection has evaluation both equal to its coefficient vector and zero, proving directness.

For \(z=E(f)\) and \(w=E(g)\), the native and reflected pairings factor through these maps as
\[
B_{\mathrm{nat}}(f,g)=m\overline{z_\beta}w_\alpha,\qquad
B_{\mathrm{sym}}(f,g)=m(\overline{z_\beta}w_\alpha+\overline{z_\alpha}w_\beta).
\tag{SW39}
\]
The same cancellation used in SW31 proves this for arbitrary \(f,g\in V\). Both forms vanish when either input lies in \(K\). The descended matrix of \(B_{\mathrm{sym}}\) is \(m\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), which is invertible, so its full radical is exactly \(K\). Also \(B_{\mathrm{sym}}=B_{\mathrm{nat}}+B_{\mathrm{nat}}^{*}\), where \(B^*(f,g)=\overline{B(g,f)}\); this is the exact passage to the Hermitian part, including its factor of two.

Define
\[
\Pi_+=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
\Pi_-=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
P_\pm=j\Pi_\pm E,\quad P_K=1-jE.
\tag{SW40}
\]
Multiplication gives \(\Pi_\pm^2=\Pi_\pm\), \(\Pi_+\Pi_-=0\), and \(\Pi_++\Pi_-=1\). Using \(Ej=1\) proves that \(P_+,P_-,P_K\) are mutually annihilating idempotents summing to \(1_V\). Their images are respectively \(j\mathbb C(1,1)\), \(j\mathbb C(1,-1)\), and \(K\). These three summands are orthogonal for \(B_{\mathrm{sym}}\). To verify all signs and the orthogonality, write
\[
c_+(f)=\frac{f(\alpha)+f(\beta)}2,\qquad
c_-(f)=\frac{f(\alpha)-f(\beta)}2.
\]
Substitution in SW39 gives
\[
B_{\mathrm{sym}}(f,g)=2m\overline{c_+(f)}c_+(g)
-2m\overline{c_-(f)}c_-(g).
\tag{SW41}
\]
Thus the nonnegative cone is exactly \(\{|c_-|\le|c_+|\}\), with the radical directions retained, and \(j\mathbb C(1,1)\oplus K\) is a maximal nonnegative linear subspace. Indeed any vector outside it has \(c_-\ne0\); subtracting its positive component, already in this subspace, gives a negative vector by SW41, so it cannot be adjoined while preserving nonnegativity.

A particular boundary subtraction can now be defined, rather than left implicit:
\[
B_+(f,g):=B_{\mathrm{sym}}(f,g)+2m\overline{c_-(f)}c_-(g)
=B_{\mathrm{sym}}(P_+f,P_+g)=2m\overline{c_+(f)}c_+(g).
\tag{SW42}
\]
It is positive semidefinite, and its removed negative direction is exactly the recorded image of \(P_-\). Equations SW37–SW42 identify the defect object, its quotient, section, radical, orthogonal summands, and one exact corrected form. They do not claim that this particular subtraction is the arithmetic or prismatic choice required elsewhere in the programme; they provide the complete finite object such a comparison would have to map.

## SW11. Consequences for the programme's vanishing-infinitesimal question

The exact distinctions now have proved maps. The quotient-size construction SW1 maps to the interpolation SW2; its first-order base change is SW5; its completed divisor is measured by SW16; its failure of reflection is the meromorphic function SW13; and its reflected Hermitian lift is the norm map SW27. The first-order endpoint residue variation of the logarithmic derivative is zero, while the first-order function, logarithmic derivative, and moving zero cluster are respectively SW5, SW6, and SW23 and need not vanish. SW24 proves nonvanishing of the displacement at every simple nontrivial classical zero.

The previously derived prime-weight formula TN21 concerns a different function, a holomorphic-unit multiple of classical \(\zeta\) in \(\Re s>0\). Its unchanged zero divisor and corrected archimedean term cannot be transferred to \(F_1=\zeta-1\). The actual map from this interpolation to a symmetric divisor is SW27, which adds the reflected divisor and exposes SW32. A prismatic or deformation comparison must carry these explicit objects and the reflection defect through its maps; nilpotence of a parameter or vanishing of an endpoint residue does not erase them.

\clearpage

# Reconstruction over the full support lattice

This calculation starts from the programme's actual support-amplitude semiring. It proves the precise comparison with the earlier scalar calculations, identifies information lost by all separate Boolean branch maps after linearization, and constructs a support-valued extension of the finite Weil packet form. It does not assert that a zeta zero off the critical line exists, or that positivity for the classical Weil distribution has been proved.

The source definition and the existing spectrum theorem are in *Split Support Geometry: Universal Zero Fibres, Arithmetic Curves, and Frobenius-Perfect Quantization*, The Clankers, June 2026, Version 11. The file read for this derivation is `split_support_geometry_arithmetic_curve_v11910.tex`, SHA256 `8443cc0401b18d373939d992f0a2f5384ee2fa1130f059753d5f3972eec5052d`, Definition `def:lattice-split`, Theorems `thm:lattice-normal-form`, `thm:birkhoff-support-coordinates`, `thm:lattice-prime-classification`, `thm:spectral-ordinal-sum`, and `thm:support-base-change`, source lines1180–1871. Those results are prior programme mathematics. The different file `split_support_geometry_arithmetic_curve_v11.tex`, SHA256 `5fa6a55aa9d1a2e57599e206087d3d2466b25dd99fa1a90d5f86367aafab1b4d`, has the explicit branch-spectrum theorem at lines1925–1985. The editions are not treated as byte-identical.

## 1. The base and its split comparison maps

Let R be a nonzero commutative unital ring and L a nontrivial bounded distributive lattice. Write its bounds as 0_L and 1_L. Set
\[
S_L=G_L(R)=\{z_\lambda=(0,\lambda):\lambda\in L\}
\cup\{\widehat r=(r,1_L):r\in R\},
\quad z_{1_L}=\widehat0=e_L,\quad z_{0_L}=\tau_L.
\tag{FSR1}
\]
The overlap in this union consists of the one element e_L. The operations are
\[
(r,\lambda)+(s,\mu)=(r+s,\lambda\vee\mu),\qquad
(r,\lambda)(s,\mu)=(rs,\lambda\wedge\mu).
\tag{FSR2}
\]
In particular, \(\widehat r+z_\lambda=\widehat r\) and \(\widehat r z_\lambda=z_\lambda\), including r=0. Closure follows because every nonzero amplitude has top support. The semiring laws follow from those of R and the distributive lattice law. Its zero is tau_L and its unit is widehat1.

Put S=G_B(R), with B={0,1}. The endpoint inclusion and each Boolean branch give maps
\[
\iota:S\longrightarrow S_L,\quad \tau\mapsto\tau_L,\quad r\mapsto\widehat r,
\qquad
\beta_\epsilon:S_L\longrightarrow S,\quad
z_\lambda\mapsto z_{\epsilon(\lambda)},\quad \widehat r\mapsto r,
\qquad \beta_\epsilon\iota=\mathrm{id}_S.
\tag{FSR3}
\]
Here epsilon:L→B preserves the bounds, joins, and meets. Both maps preserve every operation in FSR2: on the zero fibre this is the lattice-map identity; on two supported amplitudes it is the identity of R; on a mixed pair it follows from the two identities after FSR2. Thus iota is injective and every beta_epsilon is surjective. The kernel congruence of beta_epsilon identifies exactly the zero-fibre elements with the same epsilon value, and no two distinct nonzero amplitudes. Its inverse image of the actual scalar zero is
\[
\beta_\epsilon^{-1}(\tau)=\{z_\lambda:\epsilon(\lambda)=0\}.
\tag{FSR4}
\]
Its inverse image of the supported scalar zero is the complementary set of zero-fibre elements. This is the exact distinction between a zero ideal and a congruence in this comparison.

The amplitude projection p_L:S_L→R has zero fibre Z_L={z_lambda}. Every homomorphism to a ring kills Z_L: the equality e_L+z_lambda=e_L implies this by additive cancellation in the target. The restriction to the supported copy then gives a unique ring homomorphism R→A. This proves the universal property of p_L, without identifying e_L with tau_L in S_L.

For a domain R, the supported zero is a prime element in the divisibility sense:
\[
e_L S_L=Z_L,
\qquad e_L\mid xy\ \Longleftrightarrow\ p_L(x)p_L(y)=0
\ \Longleftrightarrow\ e_L\mid x\ \text{or}\ e_L\mid y.
\tag{FSR5}
\]
The first equality follows from e_L z_lambda=z_lambda and e_L widehat r=e_L. The next equivalence follows from the first equality and the multiplication law. The last uses precisely the absence of zero divisors in R. The ideal Z_L is proper because widehat1 is outside it. The element e_L is not a unit, since every product with it has amplitude zero. It is reducible, since e_L=e_L e_L with two nonunits. Its primality and its multiplicative idempotence are simultaneous facts.

For completeness the entire semiring-prime comparison can be obtained directly. If an ideal contains a supported amplitude, multiplication by e_L puts e_L in it, hence puts all of Z_L in it. Its supported amplitudes form a ring ideal J. An ideal containing no supported amplitude is Z_a for a proper lattice ideal a: joins follow from addition and downward closure follows from z_mu z_lambda=z_mu when mu≤lambda. Thus all ideals are Z_a and
\[
Q_J=Z_L\cup\{\widehat r:r\in J\}.
\tag{FSR6}
\]
Testing FSR2 shows that Z_a is prime exactly when a is a prime lattice ideal, and Q_J is prime exactly when J is a ring prime. Every support prime is strictly below every arithmetic prime. For R=Z this includes
\[
Z_{\mathfrak a}\subsetneq Z_L=(e_L)=Q_{(0)}\subsetneq Q_{(p)}.
\tag{FSR7}
\]
The basic opens are D(z_lambda)={Z_a:lambda∉a} and D(widehat r)=Spec_lat(L) union D_R(r). These formulas prove the topological ordinal sum, including its topology. Contraction along beta_epsilon sends the scalar prime {tau} to Z_(epsilon inverse0) and Q_q to Q_q. Contraction along iota sends every Z_a to {tau} and Q_q to Q_q. Consequently the scalar spectrum is a retract with an explicitly chosen section; it is not the entire support spectrum.

## 2. Joint reconstruction before linearization

Now assume L finite and let J(L) be its nonzero join-irreducible elements. For j∈J(L) put theta_j(lambda)=1 if j≤lambda and 0 otherwise. A join-irreducible is join-prime: if j≤lambda∨mu, distributivity gives j=(j∧lambda)∨(j∧mu), so one term equals j. Therefore theta_j is a bounded lattice homomorphism. Every nonzero element is the join of the join-irreducibles below it, by induction in the finite partially ordered set. Hence these characters jointly distinguish elements of L.

Conversely, a Boolean branch has a prime filter whose least element j is the meet of its elements. If j=x∨y with neither x nor y equal to j, the primality of the filter contradicts the minimality of j. Thus j is join-irreducible, and the branch is theta_j. This proves the entire branch list.

The product of all branch maps is the injective semiring map
\[
\Beta:S_L\longrightarrow\prod_{j\in J(L)}S,\qquad
\Beta(x)=(\beta_j(x))_j.
\tag{FSR8}
\]
Its image is exactly the following set. All coordinate amplitudes have a common value r. If r≠0, all coordinates are the same supported element r. If r=0, each coordinate is tau or e, and the set of coordinates equal to e is an order ideal in J(L). Indeed it is {j:j≤lambda} for the source z_lambda. Conversely, an order ideal A gives lambda=join A; join-primality shows that {j:j≤lambda}=A. This proves both surjectivity onto the displayed image and injectivity.

For L=B^d the poset J(L) is an antichain of d atoms. Every subset is an order ideal, so FSR8 becomes an isomorphism
\[
G_{B^d}(R)\ \cong\ \underbrace{G(R)\times_R\cdots\times_R G(R)}_{d\text{ factors}},
\tag{FSR9}
\]
where the maps to R are amplitude projections. This is different from the product of independent amplitude coordinates: the common-amplitude condition is part of the isomorphism, not an omitted restriction.

For a general finite distributive L, FSR8 is the subsemiring of that fibre product whose zero-amplitude masks satisfy the stated order-ideal relations. The additive and multiplicative laws remain FSR2. All earlier scalar identities pull back along each beta_j. Conversely, if two S_L-valued expressions have equal images under every beta_j, FSR8 proves equality in S_L. This last conclusion concerns semiring-valued expressions; it does not yet concern their free additive envelopes.

## 3. The exact extra kernel created by linearization

For a commutative coefficient ring k define the contracted meet algebra
\[
C_L=k[(L,\wedge)]/([0_L]).
\tag{FSR10}
\]
It is free as a k-module on u_lambda=[lambda] for lambda≠0_L, with u_0=0, unit u_1, and u_lambda u_mu=u_(lambda∧mu). It retains multiplication from support and introduces its own additive linear combinations. In particular u_(lambda∨mu) is not defined to be u_lambda+u_mu.

For every nonzero a∈L, whether join-irreducible or not, define
\[
\eta_a(u_\lambda)=\mathbf1_{\{a\leq\lambda\}}.
\tag{FSR11}
\]
This is a unital k-algebra homomorphism: a≤lambda∧mu holds exactly when both inequalities hold. With any linear extension of the order, its matrix has entries 1_(a≤lambda), is triangular with diagonal1, and is invertible over the integers. Consequently
\[
\eta:C_L\xrightarrow{\sim}\prod_{a\in L\setminus\{0\}}k.
\tag{FSR12}
\]
No division in k is used.

An explicit inverse uses the Möbius function of the finite order. Define mu(a,a)=1 and, for a<b, mu(a,b)=-sum_(a≤c<b)mu(a,c). The upper triangular incidence matrix Z_(ab)=1_(a≤b) has inverse with these entries: the recurrence proves MZ=I, and finite triangular matrices then also satisfy ZM=I. Define
\[
E_a=\sum_{\lambda\leq a}\mu(\lambda,a)u_\lambda.
\tag{FSR13}
\]
Then eta_b(E_a)=sum_(b≤lambda≤a)mu(lambda,a)=delta_(ab). The term lambda=0 contributes zero. Thus
\[
E_aE_b=\delta_{ab}E_a,\qquad
\sum_{a\neq0}E_a=u_1,\qquad
u_\lambda=\sum_{0<a\leq\lambda}E_a.
\tag{FSR14}
\]
These identities follow by applying the isomorphism FSR12, so hold over every coefficient ring.

The linearized Boolean branch theta_j is precisely eta_j. Write
\[
K_L=\bigcap_{j\in J(L)}\ker\eta_j
=\bigoplus_{a\in L\setminus(\{0\}\cup J(L))}kE_a.
\tag{FSR15}
\]
This proves the full kernel, not only its dimension. Over a field its dimension is |L|−1−|J(L)|. It is a direct product of copies of k, with multiplicatively idempotent coordinate projectors. It is zero exactly when every nonzero lattice element is join-irreducible, equivalently when L is a chain. To verify the last equivalence, a chain has that property. If L is not a chain, choose incomparable a,b; then a∨b is nonzero and join-reducible.

For L=B^2={0,a,b,1}, with a∧b=0 and a∨b=1,
\[
E_a=u_a,\qquad E_b=u_b,\qquad
w=E_1=u_1-u_a-u_b,
\quad w^2=w\neq0,
\quad\eta_a(w)=\eta_b(w)=0.
\tag{FSR16}
\]
Indeed the three terms are distinct basis vectors, proving nonzero, and direct expansion gives
\((u_1-u_a-u_b)^2=u_1+u_a+u_b-2u_a-2u_b=u_1-u_a-u_b\).
Thus the semiring branch maps in FSR8 distinguish every support element, but their separately linearized maps omit w. This is a proved failure of linearized reconstruction from separate branches. Its retained object is K_L with inclusion, coordinate projectors, and quotient given in FSR15.

The nonzero a that are not join-irreducible give genuine mixed observables. For a with join-irreducible decomposition a=join_(j≤a)j,
\[
\eta_a(u_\lambda)=\prod_{j\leq a}\theta_j(\lambda).
\tag{FSR17}
\]
Both sides are1 exactly when every j≤a lies below lambda, equivalently when a≤lambda. Thus a joint product of branch tests restores this missing coordinate. Separate branch expectations do not determine expectations of these products. FSR12 gives the complete recovery map using all these joint tests.

## 4. Contracted multiplicative coefficients and the scalar retract

Let Gamma_L=k[(S_L, multiplication)]/([tau_L]). Put E=[e_L] and F=1−E. Multiplication by E sends [z_lambda] to itself and [widehat r] to [e_L]. Thus E Gamma_L is C_L, embedded by u_lambda↦[z_lambda]. The complementary factor F Gamma_L has basis
\[
v_r=[\widehat r]-[e_L],\qquad r\in R\setminus\{0\},
\tag{FSR18}
\]
and v_0=0. Their multiplication is v_r v_s=v_(rs), with zero when rs=0. Indeed expansion gives [widehat(rs)]−[e_L]−[e_L]+[e_L]. The two sets {[z_lambda]:lambda≠0} and {v_r:r≠0} form a basis: each original nonzero supported basis element is v_r+[e_L], and comparison of the distinct [widehat r] coefficients proves linear independence. Hence
\[
\Gamma_L\cong C_L\times D_R,
\qquad D_R=k[(R,\times)]/([0_R]).
\tag{FSR19}
\]
The formulas prove this for rings with zero divisors as well as domains. For R=Z the second factor is
\[
D_{\mathbb Z}\cong k[t,X_p:p\text{ rational prime}]/(t^2-1),
\quad v_{-1}\mapsto t,\quad v_p\mapsto X_p.
\tag{FSR20}
\]
Unique prime factorization of every nonzero integer proves a bijection of the displayed monomial bases and compatibility with multiplication.

For scalar support the same construction is Gamma_B=k×D_R. Under FSR19 each branch and the scalar inclusion become
\[
\Gamma(\beta_j):(c,d)\longmapsto(\eta_j(c),d),
\qquad
\Gamma(\iota):(a,d)\longmapsto(a\,u_1,d).
\tag{FSR21}
\]
These formulas follow on z_lambda and widehat r, which generate the algebras. The composite is the identity. The intersection of all branch kernels is exactly K_L×0. Thus the earlier arithmetic prime-label algebra D_R is preserved as an actual direct factor, and the missing support coefficient object is explicitly identified. This is stronger than saying that earlier work might survive.

The evaluation map Gamma_L→R when k=Z sends [widehat r] to r and every [z_lambda] to0. For R=Z, FSR19–20 identify its kernel as
\[
C_L\times (t+1,\ X_p-p\text{ for every prime }p)\subset C_L\times D_{\mathbb Z}.
\tag{FSR22}
\]
The quotient of D_Z by the displayed ideal is Z: every polynomial reduces to its integer evaluation, and that evaluation is the inverse of the resulting inclusion of Z. This proves equality of the kernel ideal. In particular all of C_L, including K_L, is killed by arithmetic addition. It remains present before that quotient. The inclusion and quotient in FSR19 and FSR22 give its exact relation to the arithmetic factor.

## 5. Extension of complexes, operators, and all primary jets

Take k=C for this section. Let (V^bullet,d) be any specified complex of complex vector spaces, with its original differentials. Its full support extension is
\[
V_L^\bullet=C_L\otimes_{\mathbb C}V^\bullet
=\bigoplus_{a\neq0}E_a\otimes V^\bullet,
\qquad d_L(E_a\otimes v)=E_a\otimes dv.
\tag{FSR23}
\]
This is a defined construction, not an identification with a prismatic complex. Decomposition FSR14 proves directly
\[
\ker d_L=\bigoplus_a E_a\otimes\ker d,
\qquad\operatorname{im}d_L=\bigoplus_a E_a\otimes\operatorname{im}d,
\qquad H^q(V_L)=\bigoplus_a E_a\otimes H^q(V).
\tag{FSR24}
\]
The first two equalities follow by equating the coefficients of the independent E_a. The third is their quotient. Thus a nonzero cohomology class of a specified old complex remains nonzero in every individual support sector. For every linear chain map T, the map 1⊗T preserves all sectors. A homotopy dH+Hd=T−T' extends to 1⊗H and satisfies the identical formula. The maps eta_j⊗id are chain maps, with joint kernel K_L⊗V^bullet. The scalar inclusion v↦u_1⊗v is split by every eta_j⊗id. These formulas specify exactly which part of this statement is functorial and which prismatic comparison still requires identifying the actual input complex.

For the finite packet take the four distinct points
\[
\alpha_1=\rho,\qquad\alpha_2=1-\overline\rho,\qquad
\alpha_3=\overline\rho,\qquad\alpha_4=1-\rho,
\]
where \(\rho=1/2+\delta+i\gamma\), \(0<\delta<1/2\) and \(\gamma>2\). Put \(d(s)=\prod_{i=1}^4(s-\alpha_i)\), \(h=d^m\) with \(m\ge1\), and \(A_h=\mathbb C[s]/(h)\). These parameters define a finite algebra for every such \(\rho\); they do not assert that \(\rho\) is a zeta zero. Pairwise coprimality gives the isomorphism to the four rings \(\mathbb C[t_i]/(t_i^m)\) by Taylor coefficients. To see its inverse explicitly, take \(h_i=h/(s-\alpha_i)^m\) and multiply \(h_i\) by the degree-\((m-1)\) Taylor polynomial of \(1/h_i\) at \(\alpha_i\). The resulting class \(e_i\) is 1 modulo \((s-\alpha_i)^m\) and 0 modulo each other primary power. Then
\[
\sum_{i=1}^4\sum_{b=0}^{m-1}c_{i,b}e_i(s-\alpha_i)^b
\tag{FSR25}
\]
is the inverse image of the four Taylor polynomials. Injectivity follows because a polynomial vanishing to order m at all four points is divisible by h. This proves the complete primary decomposition and retains every jet.

Evaluation \(\operatorname{ev}:A_h\to\mathbb C^4\) is surjective with kernel \(J_h=(d)/(d^m)\), of dimension \(4m-4\). Surjectivity follows from the \(e_i\). The kernel statement follows by divisibility by the four distinct linear factors. Choose any specified unit \(u\in A_h\) and write \(U=M_u\). Its four constant Taylor coefficients are nonzero; conversely that condition makes it a unit by the finite inverse of each truncated Taylor series. Then \(a_h=\operatorname{ev}U\) is onto with kernel \(J_h\). The old programme choice \(u=j_h(g/h)\), wherever that entire quotient defines a unit, is retained exactly by this construction; it is not substituted by 1.

Extend \(A_h,J_h,U\) and \(a_h\) coefficientwise as in FSR23. If \(u_{i,b}\) denotes its Taylor coefficient, the full operator remains
\[
U_L\bigl((x_{a,i,b})_{a,i,b}\bigr)_{a,i,b}
=\sum_{c=0}^{b}u_{i,c}x_{a,i,b-c}.
\tag{FSR26}
\]
Thus no amplitude derivative, multiplicity, or support sector is omitted. Multiplication by \(s\) still acts on each basis element by \(\alpha_i\) times that element plus the next jet, with the last next jet zero. The kernel of the extended \(a_h\) is \(C_L\otimes J_h\), while the joint kernel of all branch maps on the entire algebra is \(K_L\otimes A_h\). These are distinct explicitly defined subspaces.

## 6. The complete support-valued finite Weil pairing

Let \(\sigma\) exchange 1 with 2 and 3 with 4. On \(\mathbb C^4\) set
\[
b(c,c')=m\sum_{i=1}^4\overline{c_{\sigma i}}c'_i,
\qquad B_h(x,y)=b(a_hx,a_hy).
\tag{FSR27}
\]
Complex conjugation and reindexing by \(\sigma\) prove Hermitian symmetry. The matrix of \(b\) is the sum of two blocks \(m\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), which is nonsingular and has one positive and one negative direction per block. Since \(a_h\) is onto with kernel \(J_h\), the radical of \(B_h\) is \(J_h\) and its inertia is \((2,2,4m-4)\). A full diagonal basis is
\[
\frac{U^{-1}(e_1+e_2)}{\sqrt{2m}},\quad
\frac{U^{-1}(e_1-e_2)}{\sqrt{2m}},\quad
\frac{U^{-1}(e_3+e_4)}{\sqrt{2m}},\quad
\frac{U^{-1}(e_3-e_4)}{\sqrt{2m}},
\]
together with \(U^{-1}e_i(s-\alpha_i)^b\) for \(1\le i\le4\) and \(1\le b<m\). Direct evaluation gives squared values \(+1,-1\) and 0 as stated. This proves the finite result independently of any analytic zeta assertion.

Give \(C_L\) the involution conjugating coefficients and fixing each \(E_a\). For \(x=\sum_a E_a\otimes x_a\) and \(y=\sum_a E_a\otimes y_a\) define
\[
\mathbb B_L(x,y)=\sum_{a\neq0}E_a B_h(x_a,y_a).
\tag{FSR28}
\]
The definition is unambiguous by FSR14. It is \(C_L\)-Hermitian and sesquilinear by the scalar identities and orthogonality of the \(E_a\). Its radical is exactly \(C_L\otimes J_h\): if its values against all \(y\) vanish, choosing \(y\) supported on one sector shows that the corresponding \(x_a\) lies in the scalar radical. For every branch \(j\),
\[
\eta_j\bigl(\mathbb B_L(x,y)\bigr)
=B_h((\eta_j\otimes\mathrm{id})x,(\eta_j\otimes\mathrm{id})y).
\tag{FSR29}
\]
This is the proved comparison with the earlier scalar packet form.

The intrinsic positive cone of the finite product algebra \(C_L\) is
\[
C_L^+=\left\{\sum_a c_a E_a:c_a\in\mathbb R_{\ge0}\right\}.
\tag{FSR30}
\]
It equals \(\{v^*v:v\in C_L\}\), since each coordinate is an absolute square, and conversely each nonnegative coordinate has its nonnegative real square root. The regular-representation trace is \(\operatorname{tr}_{\rm reg}(\sum_a c_a E_a)=\sum_a c_a\): multiplication by \(E_a\) is the projection onto its one-dimensional coordinate. Consequently \(\operatorname{tr}_{\rm reg}\mathbb B_L\) has inertia
\[
\bigl(2(|L|-1),\ 2(|L|-1),\ (4m-4)(|L|-1)\bigr).
\tag{FSR31}
\]
This follows from the direct sum of the explicit diagonal bases after FSR27. No claim identifies this finite trace with the adelic trace without the corresponding analytic map.

Retaining only the sum of Boolean-branch traces means using \(\sum_{j\in J(L)}\eta_j\). The radical of that form is
\[
\left(\bigoplus_{j\in J(L)}E_j\otimes J_h\right)
\oplus\left(K_L\otimes A_h\right),
\tag{FSR32}
\]
and its inertia is
\[
\left(2|J(L)|,\ 2|J(L)|,\ (4m-4)|J(L)|+4m(|L|-1-|J(L)|)\right).
\tag{FSR33}
\]
Each observed sector has exactly the scalar radical and each unobserved sector has its entire \(4m\)-dimensional space in the radical; this proves both formulas.

For \(B^2\) let \(w\) be FSR16 and choose the fully specified element
\[
x=w\otimes U^{-1}(e_1-e_2).
\tag{FSR34}
\]
Both branch images of \(x\) vanish, but
\[
\mathbb B_{B^2}(x,x)=-2m\,w\neq0.
\tag{FSR35}
\]
The equality follows from FSR27 and \(w^2=w\). Thus zero results from all separate branch observations do not make the full support-valued form zero or positive. Replacing the minus by a plus in FSR34 gives \(+2m w\), so the omitted space carries both signs in this finite packet model. This is a concrete comparison result about the defined form. It is not a counterexample to RH: the arbitrary \(\rho\) in FSR25 has not been asserted to be a zeta zero.

Finally the scalar inclusion \(x\mapsto u_1\otimes x\) obeys
\[
\mathbb B_L(u_1\otimes x,u_1\otimes y)=u_1 B_h(x,y).
\tag{FSR36}
\]
It therefore preserves the old calculation as a diagonal subspace. Full support adds exact sectors and additional observations; it does not by itself repair a negative scalar value. This specifies the part of the old Weil construction that survives and the additional calculation required for an actual full-support adelic realization.

\clearpage

# The localized Weil packet: values, jets, and the observation multiplier

This paper computes the finite Hermitian form specified by the zero side of the Weil pairing on the programme's entire functions. It keeps the polynomial coordinate change, all primary jets, and the actual multiplier \(U=M_{j_h(v_h)}\). The form has a four-dimensional nondegenerate quotient and a fully described nilpotent radical. Every jet remains present in the source algebra and in the multiplier, although the zero-side pairing evaluates only the zeroth jets.

The definitions of the quartet, \(E_h\), the Taylor remainder \(j_h\), the unit \(U\), and the primary basis are those of the programme's OPG1 and OPG10–OPG11 in *Full observation proofs*. They are restated and proved to the extent needed here. The starting suggestion is Proposition 3 in the supplied *Split-Zero programme: orientation and new angles*, 22 September 2026. The formula there changes from the Fourier coordinate to the \(s\)-coordinate without changing the polynomial's name. Equations (WP5)–(WP11) below give the exact coordinate maps.

No analytic explicit-formula identity, Fourier inversion assertion, or positivity theorem is assumed in the finite calculation. Section 10 specifies the precise zero-side identity proved here and its analytic scope.

## 1. The complete-order quartet and the two polynomial coordinates

Retain the programme's hypotheses
\[
\rho=\frac12+\delta+i\gamma,
\qquad 0<\delta<\frac12,\quad \gamma>2,\quad m\in\mathbb Z_{\ge1}.
\tag{WP1}
\]
Order its four distinct points as
\[
\alpha_1=\rho,\quad
\alpha_2=1-\overline\rho,\quad
\alpha_3=\overline\rho,\quad
\alpha_4=1-\rho,
\qquad \mathcal R=\{\alpha_1,\alpha_2,\alpha_3,\alpha_4\}.
\tag{WP2}
\]
The real parts distinguish points with the same imaginary part because \(\delta>0\), and the imaginary parts distinguish the upper and lower pairs because \(\gamma>0\). Let \(g=2\xi\) have a zero of exact order \(m\) at each \(\alpha\in\mathcal R\). Put
\[
d(s)=\prod_{\alpha\in\mathcal R}(s-\alpha),\qquad
h(s)=d(s)^m,\qquad n=4m,\qquad v_h(s)=\frac{g(s)}{h(s)}.
\tag{WP3}
\]
Here \(s\) is the original zeta coordinate. At each \(\alpha\), write
\(g(s)=(s-\alpha)^m b_\alpha(s)\), where \(b_\alpha\) is holomorphic and \(b_\alpha(\alpha)\ne0\). If
\(h_\alpha(s)=h(s)/(s-\alpha)^m\), then \(h_\alpha(\alpha)\ne0\), and
\[
v_h(s)=\frac{b_\alpha(s)}{h_\alpha(s)}\quad\hbox{near }\alpha,
\qquad
v_h(\alpha)=\frac{g^{(m)}(\alpha)}{m!\,h_\alpha(\alpha)}\ne0.
\tag{WP4}
\]
Thus all the apparent singularities of \(g/h\) are removable and \(v_h\) is entire. At every zero \(\rho'\notin\mathcal R\) of \(g\), it vanishes because \(h(\rho')\ne0\).

Define the Fourier coordinate and its inverse by
\[
\theta(s)=\frac{s-1/2}{i},\qquad \iota(z)=\frac12+iz,
\qquad \theta\iota=\mathrm{id}_{\mathbb C},\quad
\iota\theta=\mathrm{id}_{\mathbb C}.
\tag{WP5}
\]
For \(P\in\mathbb C[z]\), the associated \(s\)-polynomial is
\[
q_P(s)=P(\theta(s)),
\qquad F_P(z)=P(z)v_h(\iota(z)).
\tag{WP6}
\]
In particular \(F_P(\theta(s))=q_P(s)v_h(s)\). The two polynomials \(P\) and \(q_P\) have the same degree, but their coefficients and variables differ by (WP5). A factor \(P(1-\overline\alpha)\) is therefore not the value obtained from \(F_P\) unless \(P\) has first been replaced by \(q_P\).

Put \(\beta_\alpha=\theta(\alpha)\). In the order (WP2),
\[
(\beta_{\alpha_1},\beta_{\alpha_2},\beta_{\alpha_3},\beta_{\alpha_4})
=(\gamma-i\delta,\gamma+i\delta,-\gamma-i\delta,-\gamma+i\delta).
\tag{WP7}
\]
Let \(\sigma\alpha=1-\overline\alpha\). This involution interchanges \(\alpha_1,\alpha_2\) and \(\alpha_3,\alpha_4\). Direct substitution gives
\[
\overline{\theta(\alpha)}=\theta(\sigma\alpha),
\qquad \iota(\overline{\beta_\alpha})=\sigma\alpha.
\tag{WP8}
\]

Define
\[
H(z)=\prod_{\alpha\in\mathcal R}(z-\beta_\alpha)^m
=i^{-n}h(\iota(z)),
\qquad E_z=\mathbb C[z]/(H),\quad E_h=\mathbb C[s]/(h).
\tag{WP9}
\]
Here \(n=4m\), so \(i^{-n}=1\); the scalar is displayed to record how the defining polynomials transform. The maps
\[
\mathcal C:E_z\longrightarrow E_h,
\quad [P]\longmapsto[P\circ\theta],
\qquad
\mathcal C^{-1}:E_h\longrightarrow E_z,
\quad[q]\longmapsto[q\circ\iota]
\tag{WP10}
\]
are inverse algebra isomorphisms. Indeed substitution sends \(H\) to \(i^{-n}h\) and \(h\) to \(i^nH\), so the maps descend to the quotients. Their two composites fix every polynomial by (WP5). They also retain the multiplication operators exactly:
\[
\mathcal C M_z=M_{\theta(s)}\mathcal C,
\qquad
\mathcal C M_{\iota(z)}=M_s\mathcal C.
\tag{WP11}
\]

## 2. All the jets and the entire-function remainder

For each \(\alpha\in\mathcal R\), introduce an independent nilpotent coordinate \(t_\alpha\) and the algebra
\[
A_\alpha=\mathbb C[t_\alpha]/(t_\alpha^m).
\tag{WP12}
\]
There is an algebra isomorphism
\[
\mathcal J:E_h\longrightarrow\prod_{\alpha\in\mathcal R}A_\alpha,
\qquad
[q]\longmapsto\left(
\sum_{a=0}^{m-1}\frac{q^{(a)}(\alpha)}{a!}t_\alpha^a
\right)_{\alpha\in\mathcal R}.
\tag{WP13}
\]
Every derivative in this formula is part of the specified map.

Here is a direct proof including its inverse. Define
\[
T_\alpha(s)=\sum_{a=0}^{m-1}
\frac{(1/h_\alpha)^{(a)}(\alpha)}{a!}(s-\alpha)^a,
\qquad e_\alpha=[h_\alpha T_\alpha]\in E_h.
\tag{WP14}
\]
Modulo \((s-\alpha)^m\), the product \(h_\alpha T_\alpha\) equals \(1\), by multiplication of the Taylor expansion and its truncated inverse. Modulo \((s-\eta)^m\) for \(\eta\ne\alpha\), it equals \(0\), because \(h_\alpha\) is divisible by that factor. Thus \(\mathcal J(e_\alpha)\) is \(1\) in the \(\alpha\)-factor and \(0\) elsewhere. The inverse of (WP13) is
\[
\mathcal J^{-1}\left(\left(\sum_{a=0}^{m-1}c_{\alpha,a}t_\alpha^a\right)_\alpha\right)
=\sum_{\alpha\in\mathcal R}\sum_{a=0}^{m-1}
c_{\alpha,a}e_\alpha(s-\alpha)^a.
\tag{WP15}
\]
This proves surjectivity. For injectivity, a polynomial in the kernel has a zero of order at least \(m\) at each of the four distinct points. Successive division by their linear factors shows it is divisible by their product \(h\). The kernel is therefore zero in \(E_h\). Taylor multiplication modulo \(t_\alpha^m\) proves multiplicativity. Equations (WP13)–(WP15) also prove
\[
e_\alpha e_\eta=0\ (\alpha\ne\eta),\qquad
e_\alpha^2=e_\alpha,\qquad\sum_\alpha e_\alpha=1,
\tag{WP16}
\]
and give the basis \(e_\alpha(s-\alpha)^a\), \(0\le a<m\), of \(E_h\).

For an entire function \(f\), define its finite Taylor remainder by
\[
j_h(f)=\mathcal J^{-1}\left(\left(
\sum_{a=0}^{m-1}\frac{f^{(a)}(\alpha)}{a!}t_\alpha^a
\right)_\alpha\right)\in E_h.
\tag{WP17}
\]
This is an algebra homomorphism: addition and scalar multiplication follow coefficient by coefficient, and the Leibniz rule gives multiplication of the truncated Taylor series. It agrees with the quotient map on polynomials. The class \(j_h(f)\) has a unique representative of degree less than \(n\), by division by the monic polynomial \(h\).

In the programme notation \(j_hv_h\), the symbol \(j_h\) denotes this map applied to \(v_h\). It is not a second scalar function multiplied by \(v_h\). Put
\[
u_h=j_h(v_h),\qquad U=M_{u_h}:E_h\longrightarrow E_h.
\tag{WP18}
\]
In the \(\alpha\)-factor of (WP13), set
\[
v_{\alpha,a}=\frac{v_h^{(a)}(\alpha)}{a!},
\qquad u_\alpha(t_\alpha)=\sum_{a=0}^{m-1}v_{\alpha,a}t_\alpha^a.
\tag{WP19}
\]
All constants \(v_{\alpha,0}\) are nonzero by (WP4). Write
\(u_\alpha=v_{\alpha,0}(1+b_\alpha)\), with \(b_\alpha\in(t_\alpha)\). Since \(b_\alpha^m=0\), its inverse is
\[
u_\alpha^{-1}=v_{\alpha,0}^{-1}
\sum_{r=0}^{m-1}(-b_\alpha)^r.
\tag{WP20}
\]
Multiplication of this finite series by \(u_\alpha\) gives \(1-(-b_\alpha)^m=1\). Hence \(u_h\) is a unit and \(U\) an automorphism. In full jet coordinates its formula is
\[
(Ux)_{\alpha,a}=\sum_{b=0}^a v_{\alpha,b}x_{\alpha,a-b}
\qquad(0\le a<m).
\tag{WP21}
\]
It therefore keeps every derivative of the amplitude through order \(m-1\). The determinant in the primary basis is
\(\prod_{\alpha\in\mathcal R}v_h(\alpha)^m\ne0\), because each block in (WP21) is triangular with that constant diagonal.

## 3. The zeroth-jet quotient and its exact multiplier map

Let \(V_{\mathcal R}=\mathbb C^{\mathcal R}\), with coordinatewise multiplication, and define
\[
e:E_h\longrightarrow V_{\mathcal R},\qquad
e([q])=(q(\alpha))_{\alpha\in\mathcal R}.
\tag{WP22}
\]
This is a surjective algebra homomorphism: it is the constant-term map in each factor of (WP13), and (WP15) lifts any tuple by \(\sum c_\alpha e_\alpha\). Its kernel is
\[
J=\ker e=(d)/(d^m)\subset E_h,
\qquad\dim_{\mathbb C}J=4m-4.
\tag{WP23}
\]
Indeed a polynomial has value zero at every \(\alpha\) precisely when it is divisible by \(d\). In the primary coordinates, \(J\) is \(\prod_\alpha(t_\alpha)\); it has basis \(e_\alpha(s-\alpha)^a\), \(1\le a<m\), and the asserted dimension follows. Every element of \(J\) has its \(m\)-th power zero. Conversely, a nilpotent element must have value zero in each complex coordinate, since a complex number with a vanishing positive power is zero. Thus \(J\) is exactly the nilradical of \(E_h\).

Write
\[
V_h:V_{\mathcal R}\longrightarrow V_{\mathcal R},\qquad
(c_\alpha)_\alpha\longmapsto(v_h(\alpha)c_\alpha)_\alpha,
\quad
a_h=eU:E_h\longrightarrow V_{\mathcal R}.
\tag{WP24}
\]
Then
\[
eU=V_he,\qquad \ker a_h=J,
\qquad a_h\text{ is surjective}.
\tag{WP25}
\]
The identity follows either from evaluation of a product or from the \(a=0\) case of (WP21). The map \(V_h\) is invertible because its four diagonal entries are nonzero, so the kernel and surjectivity assertions follow from (WP22)–(WP23). Thus the exact comparison with the programme's multiplier is the commuting diagram of typed maps
\[
\begin{array}{ccc}
E_h&\xrightarrow{\ U\ }&E_h\\
e\downarrow&&\downarrow e\\
V_{\mathcal R}&\xrightarrow{\ V_h\ }&V_{\mathcal R}.
\end{array}
\tag{WP26}
\]
The left and right vertical maps retain the same kernel \(J\); the horizontal map on the upper row retains all the additional coefficients (WP21).

The entire-function family is a further, distinct vector space
\[
\mathcal F_h=\{F_P:P\in\mathbb C[z]\}.
\tag{WP26a}
\]
The map \(P\mapsto F_P\) is a linear isomorphism onto this family. Surjectivity is its definition. For injectivity, \(v_h\) is nonzero at a packet root, hence nonzero on a neighborhood of that root. If \(F_P\) vanishes identically, \(P\) vanishes on the corresponding open set in the \(z\)-coordinate. A nonzero polynomial has only finitely many roots, so \(P=0\).

The full-jet map from this entire-function family is
\[
\begin{aligned}
\mathcal T_h:\mathcal F_h&\longrightarrow E_h,
&\mathcal T_h(F)&=j_h(F\circ\theta),\\
\mathcal T_h(F_P)&=U\mathcal C[P],
&(\mathcal J\mathcal T_h(F))_{\alpha,a}
&=i^{-a}\frac{F^{(a)}(\beta_\alpha)}{a!}.
\end{aligned}
\tag{WP26b}
\]
The first identity on the second line follows from (WP6), (WP17), and (WP18). The second follows by differentiating the affine change of variable \(\theta\) exactly \(a\) times; its derivative is \(1/i\). Thus the factor \(i^{-a}\) is retained in every jet coordinate.

The map \(\mathcal T_h\) is onto and its kernel is
\[
\ker\mathcal T_h=\{F_{HQ}:Q\in\mathbb C[z]\}.
\tag{WP26c}
\]
Indeed \(U\) and \(\mathcal C\) are isomorphisms, so \(\mathcal T_h(F_P)=0\) exactly when \(P\) is divisible by \(H\). There is a separate surjection
\[
e\mathcal T_h:\mathcal F_h\longrightarrow V_{\mathcal R},
\quad F\longmapsto(F(\beta_\alpha))_\alpha,
\qquad
\ker(e\mathcal T_h)=\{F_{D_zQ}:Q\in\mathbb C[z]\},
\quad D_z(z)=\prod_\alpha(z-\beta_\alpha).
\tag{WP26d}
\]
The coordinate formula follows from (WP26b) at \(a=0\). It is onto by (WP25). Since \(v_h(\alpha)\ne0\), its value at \(F_P\) is zero exactly when \(P\) vanishes at all the distinct \(\beta_\alpha\), which is equivalent to divisibility by \(D_z\). Thus the entire functions themselves are not identified with their finite jets or with their values: (WP26b)–(WP26d) give the actual surjections and both exact kernels.

## 4. The finite Hermitian form and its radical

Use the convention that a Hermitian form is conjugate-linear in its first argument and linear in its second. On \(V_{\mathcal R}\), define
\[
b_{\mathcal R}(c,c')=m\sum_{\alpha\in\mathcal R}
\overline{c_{\sigma\alpha}}c'_\alpha.
\tag{WP27}
\]
It is Hermitian: the conjugate of \(b_{\mathcal R}(c',c)\), after replacing the summation index \(\alpha\) by \(\sigma\alpha\), is exactly (WP27). It is nondegenerate. If it vanishes against every \(c'\), selecting \(c'\) with a single nonzero coordinate at \(\alpha\) gives \(m\overline{c_{\sigma\alpha}}=0\), hence every coordinate of \(c\) is zero.

Define the packet form on the full algebra by the pullback
\[
B_h(x,y)=b_{\mathcal R}(a_hx,a_hy)
=m\sum_{\alpha\in\mathcal R}
\overline{v_h(\sigma\alpha)x(\sigma\alpha)}
v_h(\alpha)y(\alpha),
\qquad x,y\in E_h.
\tag{WP28}
\]
Evaluation is independent of polynomial representatives by (WP22), so the formula is well defined. It is Hermitian because (WP27) is. Let \(\operatorname{rad}B_h\) mean the set of \(x\) with \(B_h(x,y)=0\) for every \(y\in E_h\).

**Theorem WP1 (exact radical and quotient).** There is an exact sequence
\[
0\longrightarrow J\longrightarrow E_h
\xrightarrow{\ a_h\ }V_{\mathcal R}\longrightarrow0,
\qquad \operatorname{rad}B_h=J.
\tag{WP29}
\]
The induced map \(\overline a_h:E_h/J\to V_{\mathcal R}\) is an algebra-multiplier comparison and a linear isometry from the descended Hermitian form to \(b_{\mathcal R}\). More precisely, \(e:E_h/J\to V_{\mathcal R}\) is an algebra isomorphism, and \(\overline a_h=V_h\overline e\) is a linear isomorphism; \(\overline a_h\) need not preserve the unit or multiplication.

**Proof.** Exactness is (WP25). If \(x\in J\), then \(a_hx=0\), so (WP28) vanishes for every \(y\). Conversely, if (WP28) vanishes for every \(y\), surjectivity of \(a_h\) implies that \(b_{\mathcal R}(a_hx,c')=0\) for every \(c'\). Nondegeneracy of (WP27) gives \(a_hx=0\), hence \(x\in J\). The quotient map is an isomorphism by exactness. Formula (WP28) proves the isometry identity. The distinction between \(\overline e\) and \(\overline a_h\) follows from (WP24): multiplying all coordinates by a fixed nonconstant unit is a linear automorphism, and is not in general an algebra homomorphism. \(\square\)

This theorem does not remove the nilpotent directions from the original packet. It identifies the precise quotient seen by this particular Hermitian form, and identifies every omitted direction as an element of the specified ideal \(J\).

## 5. Complete inertia and explicit negative representatives

In the order (WP2), write \(c=(a,b,c_3,c_4)\). Then
\[
b_{\mathcal R}(c,c')
=m\bigl(\overline b a'+\overline a b'
+\overline{c_4}c_3'+\overline{c_3}c_4'\bigr).
\tag{WP30}
\]
The matrix is the direct sum of two blocks \(m\begin{pmatrix}0&1\\1&0\end{pmatrix}\). In each pair the two vectors \((1,1)/\sqrt{2m}\) and \((1,-1)/\sqrt{2m}\) have squared values \(+1\) and \(-1\), and their mutual pairing is zero. They form a basis of that two-dimensional pair. Consequently
\[
\operatorname{inertia}(b_{\mathcal R})=(2,2,0),
\qquad
\operatorname{inertia}(B_h)=(2,2,4m-4),
\tag{WP31}
\]
where inertia lists positive, negative, and radical dimensions in that order. This is inertia under congruence of Hermitian forms, rather than an assertion that an arbitrary coefficient-frame matrix of \(B_h\) has eigenvalues \(\pm m\).

For a complete diagonal basis of the original packet, use
\[
x_1^{\pm}=\frac1{\sqrt{2m}}U^{-1}(e_{\alpha_1}\pm e_{\alpha_2}),
\qquad
x_2^{\pm}=\frac1{\sqrt{2m}}U^{-1}(e_{\alpha_3}\pm e_{\alpha_4}),
\tag{WP32}
\]
together with
\[
x_{\alpha,a}=U^{-1}\bigl(e_\alpha(s-\alpha)^a\bigr),
\quad \alpha\in\mathcal R,\quad 1\le a<m.
\tag{WP33}
\]
These form a basis because the original primary vectors do, the two changes of basis at order zero are invertible, and \(U\) is invertible. The last \(4m-4\) vectors lie in \(J\). Formula (WP28) gives \(B_h(x_j^+,x_j^+)=1\), \(B_h(x_j^-,x_j^-)=-1\), all pairings between distinct displayed positive or negative vectors zero, and all pairings with (WP33) zero. This proves (WP31) on the entire vector space, including all primary multiplicities.

These representatives are explicit finite Taylor expressions. For example
\[
U^{-1}e_\alpha
=e_\alpha\sum_{a=0}^{m-1}
\frac{(1/v_h)^{(a)}(\alpha)}{a!}(s-\alpha)^a.
\tag{WP34}
\]
The reciprocal is taken only in a neighborhood of \(\alpha\), where it is holomorphic by (WP4). Taylor multiplication proves (WP34), as also follows from (WP20). Formula (WP34) prescribes the full jet of a representative whose amplitude has constant primary jet \(1\) at one root and zero at the others.

There are also degree-three representatives, without imposing any condition on their higher amplitude jets. Define the Lagrange polynomials
\[
\ell_\alpha(s)=\prod_{\eta\in\mathcal R\setminus\{\alpha\}}
\frac{s-\eta}{\alpha-\eta}.
\tag{WP35}
\]
Their denominators are nonzero, and \(\ell_\alpha(\eta)=\delta_{\alpha\eta}\). Put
\[
q_-(s)=\frac{\ell_{\alpha_1}(s)}{v_h(\alpha_1)}
-\frac{\ell_{\alpha_2}(s)}{v_h(\alpha_2)},
\qquad P_-(z)=q_-(1/2+iz).
\tag{WP36}
\]
Then \(a_h[q_-]=(1,-1,0,0)\), so
\[
B_h([q_-],[q_-])=-2m.
\tag{WP37}
\]
Dividing either polynomial in (WP36) by \(\sqrt{2m}\) gives value \(-1\); dividing by \(\sqrt m\) gives value \(-2\). The second negative direction is obtained with \(\alpha_3,\alpha_4\). This formula includes the exact Fourier-coordinate representative \(P_-\).

For \(m>1\), the class \([q_-]\) in (WP36) and the full-jet representative \(U^{-1}(e_{\alpha_1}-e_{\alpha_2})\) need not agree. Their difference lies in \(J\), because their images under \(a_h\) agree and \(\ker a_h=J\). Thus the two explicit choices have the same pairings with every packet class, with their difference retained as a specified nilpotent class.

## 6. The surviving jet filtration and multiplication operators

The radical has the finite filtration
\[
E_h=J^0\supset J^1\supset\cdots\supset J^{m-1}\supset J^m=0,
\qquad J^r=(d^r)/(d^m).
\tag{WP38}
\]
In primary coordinates, \(J^r=\prod_\alpha(t_\alpha^r)\). To verify this from \(d\), write \(d(s)=(s-\alpha)c_\alpha(s)\), with \(c_\alpha(\alpha)\ne0\). The factor \(c_\alpha\) is a unit in \(A_\alpha\), so the ideal generated by \(d^r\) in that primary factor is exactly \((t_\alpha^r)\). The isomorphism (WP13) then proves (WP38) for every \(r\).

For \(0\le r<m\), the exact layer map is
\[
\lambda_r:J^r/J^{r+1}\longrightarrow V_{\mathcal R},
\qquad [x]\longmapsto
\left(\frac{x^{(r)}(\alpha)}{r!}\right)_\alpha.
\tag{WP39}
\]
For \(r=0\), this means the map \(e\) on \(E_h/J\). A polynomial representative of an element of \(J^r\) has all derivatives of orders less than \(r\) zero at each root. Changing it by a multiple of \(h\) changes none of the derivatives in (WP39), since \(r<m\). Changing its class by \(J^{r+1}\) also leaves those coefficients unchanged. Formula (WP13) shows that the kernel is exactly \(J^{r+1}\), and that the elements \(e_\alpha(s-\alpha)^r\) map to the coordinate basis. Hence (WP39) is an isomorphism and every layer has dimension \(4\).

All these layers are preserved by \(U\), its inverse, and \(A_h=M_s\). Their induced operators are
\[
\lambda_r\,\operatorname{gr}_r(U)=V_h\lambda_r,
\qquad
\lambda_r\,\operatorname{gr}_r(A_h)
=\operatorname{diag}(\alpha)\lambda_r.
\tag{WP40}
\]
For the first equality, use (WP21): the coefficient of order \(r\) in a product with an element whose lower coefficients are zero is \(v_{\alpha,0}x_{\alpha,r}\). For the second, multiply its Taylor series by \(\alpha+t_\alpha\); the extra term only enters the next layer. Before passage to a layer, the complete formulas remain (WP21) and
\[
A_h\bigl(e_\alpha(s-\alpha)^a\bigr)
=\alpha e_\alpha(s-\alpha)^a+e_\alpha(s-\alpha)^{a+1},
\tag{WP41}
\]
where the last term is zero for \(a=m-1\). Thus the original Jordan chains and the amplitude derivatives survive in the source and its filtered maps. The form (WP28) reads only the layer \(r=0\); this follows from its evaluated formula and does not assert that higher derivatives are unavailable to the observation map.

## 7. The exact adjoint relation for every polynomial multiplier

For \(q\in\mathbb C[s]\), define
\[
q^\#(s)=\overline{q(1-\overline s)}.
\tag{WP42}
\]
This is a polynomial: if \(q(s)=\sum_k c_ks^k\), then
\(q^\#(s)=\sum_k\overline{c_k}(1-s)^k\). It is an antilinear, multiplicative involution. Since \(\sigma\) permutes \(\mathcal R\),
\[
h^\#(s)=\prod_{\alpha\in\mathcal R}(1-s-\overline\alpha)^m
=(-1)^{4m}\prod_{\alpha\in\mathcal R}(s-\sigma\alpha)^m=h(s).
\tag{WP43}
\]
It therefore descends to an antilinear algebra involution on \(E_h\). Its action on all the jets is
\[
(x^\#)_{\alpha,a}=(-1)^a\overline{x_{\sigma\alpha,a}}.
\tag{WP44}
\]
Indeed, substitute \(s=\alpha+t\) into (WP42), expand \(q\) at \(\sigma\alpha\), and conjugate its expansion at the increment \(-\overline t\). This gives the displayed coefficient, including its sign.

For the original completed zeta function, its functional identities are \(g(1-s)=g(s)\) and \(g(\overline s)=\overline{g(s)}\). They imply \(g^\#=g\). The quartet polynomial has exactly the same two identities: conjugation permutes its four factors, and replacing \(s\) by \(1-s\) gives the sign \((-1)^{4m}=1\) and the permutation \(\alpha\mapsto1-\alpha\). Therefore
\[
v_h^\#=v_h,\qquad v_h(\sigma\alpha)=\overline{v_h(\alpha)},
\qquad (j_hv_h)^\#=j_hv_h.
\tag{WP44a}
\]
The first identity follows by division off the finite zero set of \(h\) and then by continuity at the removable points (WP4). The second is its evaluation, and the third follows from the signed jet formula (WP44). No scalar factor accompanies these identities for the monic degree-\(4m\) polynomial in (WP3).

**Theorem WP2 (multiplier adjoints).** For every \(q,x,y\in E_h\),
\[
B_h(M_qx,y)=B_h(x,M_{q^\#}y).
\tag{WP45}
\]
In particular, if \(Y_h=(A_h-\frac12I)/i=M_{\theta(s)}\), then
\[
B_h(A_hx,y)=B_h(x,(I-A_h)y),
\qquad B_h(Y_hx,y)=B_h(x,Y_hy).
\tag{WP46}
\]

**Proof.** At each root \(\alpha\), \(q^\#(\alpha)=\overline{q(\sigma\alpha)}\). Inserting a factor \(q(\sigma\alpha)\) in the conjugated first entry of (WP28) therefore has exactly the same effect as inserting \(q^\#(\alpha)\) in its second entry. This proves (WP45) term by term. For the coordinate polynomial, \(s^\#=1-s\). For \(\theta(s)=-i(s-1/2)\), antilinearity and this equality give
\(\theta^\#(s)=i((1-s)-1/2)=-i(s-1/2)=\theta(s)\). These substitutions prove both assertions in (WP46). \(\square\)

The operator \(Y_h\) is consequently self-adjoint with respect to the specified Hermitian form. Its induced eigenvalues on \(E_h/J\) are exactly (WP7), since (WP40) gives the diagonal multiplier \((\alpha-1/2)/i\). The nonreal values \(\gamma\pm i\delta,-\gamma\pm i\delta\) are paired by the two hyperbolic blocks (WP30). There is no claim that self-adjointness for this indefinite form makes those values real. Equations (WP40), (WP44), and (WP46) give the exact relation between the full primary operator and its value quotient.

In particular the original amplitude unit is itself self-adjoint for this form, by (WP44a) and (WP45). For polynomial inputs, the entire function
\[
\mathcal A_{P,Q}(s)=q_P^\#(s)q_Q(s)v_h(s)^2
\tag{WP46a}
\]
has the packet values
\[
\mathcal A_{P,Q}(\alpha)
=\overline{q_P(\sigma\alpha)v_h(\sigma\alpha)}
q_Q(\alpha)v_h(\alpha).
\tag{WP46b}
\]
This follows from \(q_P^\#(\alpha)=\overline{q_P(\sigma\alpha)}\) and (WP44a). On the complement of the zeros of \(g\), the exact logarithmic-derivative identity is
\[
\frac{\xi'(s)}{\xi(s)}\mathcal A_{P,Q}(s)
=q_P^\#(s)q_Q(s)\frac{g'(s)g(s)}{h(s)^2}.
\tag{WP46c}
\]
Here \(g=2\xi\), so \(\xi'/\xi=g'/g\); multiplication by \((g/h)^2\) proves the formula with no additional factor of two. At a zero of \(g\) outside the packet, the right side is holomorphic because \(h\) does not vanish there. At \(\alpha\in\mathcal R\), writing \(g=(s-\alpha)^mb_\alpha\) and \(h=(s-\alpha)^mh_\alpha\) shows that \(g'g/h^2\) has the Laurent term
\(m v_h(\alpha)^2/(s-\alpha)\). Thus its residue after multiplication by \(q_P^\#q_Q\) is exactly \(m\mathcal A_{P,Q}(\alpha)\). These are local meromorphic identities; no contour estimate or prime-side identity is used to prove them.

## 8. The original period observation and what each map reads

The map \(a_h=eU\) applies the same full-jet unit as the original observation and then takes values. To make the relation to the period stage explicit, let \(\Pi:E_h\to\mathbb C^n\) be the programme's OPG4 linear map, defined on the unique degree-less-than-\(n\) representative by its prescribed convergent period integrals. Retain its actual contours, exponential weight, and basis; none is changed here. Put
\[
\mathbf b_{\alpha,a}=\Pi\bigl(e_\alpha(s-\alpha)^a\bigr).
\tag{WP47}
\]
For every \(x\in E_h\), linearity and (WP21) give the identity of vectors in \(\mathbb C^n\)
\[
\Pi Ux=
\sum_{\alpha\in\mathcal R}\sum_{a=0}^{m-1}
\mathbf b_{\alpha,a}
\sum_{b=0}^a v_{\alpha,b}x_{\alpha,a-b}.
\tag{WP48}
\]
This proof uses a finite sum of the original primary classes; it does not assign a period integral to an arbitrary entire function. The value map, with the same coefficients before projection, is
\[
a_hx=(v_{\alpha,0}x_{\alpha,0})_\alpha.
\tag{WP49}
\]
Thus (WP48) and (WP49) are two exact maps out of the same source after the same multiplication. In particular, for \(x=j_h(f)\), the ring-homomorphism property (WP17) gives
\[
Uj_h(f)=j_h(v_hf),\qquad
\Pi Uj_h(f)=\Pi j_h(v_hf),\qquad
a_hj_h(f)=(v_h(\alpha)f(\alpha))_\alpha.
\tag{WP50}
\]
The middle formula evaluates \(\Pi\) on a finite Taylor remainder, exactly as in OPG11. It is not the integral of the unreduced entire function unless a separate equality proves that assertion.

There is also a precise test for whether any proposed observation \(T:E_h\to W\), to a complex vector space \(W\), factors through the value map \(a_h\). The factorization exists exactly when \(T(J)=0\); when it exists its only possible formula is
\[
\overline T(c)=T\left(U^{-1}\sum_{\alpha\in\mathcal R}c_\alpha e_\alpha\right).
\tag{WP51}
\]
To prove this, the expression in parentheses has \(a_h\)-image \(c\) by (WP15) and (WP24). If \(T(J)=0\), any two lifts with that image differ by (WP29) in \(J\), so their \(T\)-images agree, and (WP51) gives a well-defined linear factorization. Surjectivity of \(a_h\) forces uniqueness. Conversely a factorization through \(a_h\) kills its kernel \(J\). This computes the exact space of factorizing maps as the injective image
\[
\operatorname{Hom}_{\mathbb C}(V_{\mathcal R},W)
\xrightarrow{\ a_h^*\ }
\operatorname{Hom}_{\mathbb C}(E_h,W),
\quad \overline T\longmapsto\overline T a_h,
\quad
\operatorname{im}(a_h^*)=\{T:T(J)=0\}.
\tag{WP52}
\]
It does not presume that the period map, or the later cyclic tensor observation, lies in that subspace.

## 9. Why the off-line and on-line cases have different packet algebras

The hypotheses (WP1) guarantee four distinct roots. Substituting \(\delta=0\) into a formula which assumes four distinct roots merges \(\alpha_1\) with \(\alpha_2\) and \(\alpha_3\) with \(\alpha_4\). If one retains the product of four factors literally, their orders double. Exact zero order \(m\) would then no longer justify dividing \(g\) by that new polynomial. The on-line packet must instead be defined from its distinct roots and their actual orders.

For completeness, the general finite value calculation is as follows. Let \(\mathcal A\) be a finite set of distinct complex points stable under \(\sigma\alpha=1-\overline\alpha\). Assign positive integer orders \(m_\alpha\), with \(m_{\sigma\alpha}=m_\alpha\), and suppose an entire \(g\) has these exact orders there. Set
\[
h_{\mathcal A}(s)=\prod_{\alpha\in\mathcal A}(s-\alpha)^{m_\alpha},
\qquad v_{\mathcal A}=g/h_{\mathcal A}.
\tag{WP53}
\]
With the corresponding jet algebra, remainder multiplier, and amplitude-value map, define
\[
B_{\mathcal A}(x,y)=
\sum_{\alpha\in\mathcal A}m_\alpha
\overline{v_{\mathcal A}(\sigma\alpha)x(\sigma\alpha)}
v_{\mathcal A}(\alpha)y(\alpha).
\tag{WP54}
\]
Let \(f\) be the number of fixed points of \(\sigma\) in \(\mathcal A\), and let \(p\) be the number of its two-element orbits. Then
\[
\operatorname{inertia}(B_{\mathcal A})
=\left(f+p,\ p,\ \sum_{\alpha\in\mathcal A}(m_\alpha-1)\right).
\tag{WP55}
\]
To prove this directly, use the local rings \(\mathbb C[t_\alpha]/t_\alpha^{m_\alpha}\). The interpolation proof (WP14)–(WP15) applies with the individual order in each factor, because the other factors are still units at that root. Evaluation has kernel \(\prod_\alpha(t_\alpha)\) of the stated dimension, and amplitude multiplication is invertible because its constants are nonzero. On its value quotient, a fixed point contributes the positive form \(m_\alpha|c_\alpha|^2\). A two-element orbit contributes the block \(m_\alpha\begin{pmatrix}0&1\\1&0\end{pmatrix}\), with one positive and one negative direction. Distinct orbits are orthogonal since their coordinates never occur together in (WP54). This proves the radical and all three entries of (WP55).

In particular, a packet supported entirely on the critical line has \(p=0\), and (WP54) is positive semidefinite. Its radical still contains all higher jet directions. A distinct off-line quartet has \(f=0,p=2\), giving (WP31). Both assertions concern the respective actual packet algebras and the exact orders in (WP53).

## 10. The exact zero-side localization and analytic scope

Index the distinct nontrivial zeros of \(\xi\) by \(\rho'\), and let \(m_{\rho'}\) be their multiplicities. For the entire functions (WP6), form the discrete zero pairing
\[
\mathscr W_0(F_P,F_Q)
=\sum_{\rho'}m_{\rho'}
\overline{F_P(\overline{\theta(\rho')})}
F_Q(\theta(\rho')).
\tag{WP56}
\]
This particular sum has only four potentially nonzero summands. Indeed, when \(\rho'\notin\mathcal R\), (WP4) gives
\(F_Q(\theta(\rho'))=q_Q(\rho')v_h(\rho')=0\). Thus no issue of summation order remains in (WP56). At the quartet, the multiplicities equal \(m\), and (WP8) gives the exact identity
\[
\begin{aligned}
\mathscr W_0(F_P,F_Q)
&=m\sum_{\alpha\in\mathcal R}
\overline{q_P(\sigma\alpha)v_h(\sigma\alpha)}
q_Q(\alpha)v_h(\alpha)\\
&=B_h(\mathcal C[P],\mathcal C[Q]).
\end{aligned}
\tag{WP57}
\]
The bracketed arguments on the second line are classes in \(E_z\), mapped into \(E_h\) by (WP10). If a polynomial is changed by a multiple of \(H\), its amplitude has all its first \(m\) jets zero at each Fourier root. Therefore (WP57) descends to \(E_z\) exactly as claimed. In fact the form already factors through the smaller value quotient \(\mathbb C[z]/\prod_\alpha(z-\beta_\alpha)\); the explicit kernel of the map from \(E_z\) to that quotient is \(\mathcal C^{-1}J\).

For \(m>1\), the multiplicity in (WP56) multiplies a value. It does not differentiate \(F_P\) or \(F_Q\). This is why the correct inertia on the full \(4m\)-dimensional packet is (WP31), and why the higher jet directions appear as its precisely computed radical. Their maps remain (WP21), (WP38)–(WP44), and (WP48).

The proof above does not identify (WP56) with pole, Gamma, and prime terms for this test family. Such an identity involves its analytic test class and convergence statements; none follows from the finite quotient alone. The finite algebra supplies a complete target for that calculation: the Hermitian form (WP28), with the explicit negative representatives (WP32) or (WP36), the complete radical (WP23), and the exact relation to the native amplitude multiplier (WP26). No assertion here establishes positivity of the prime-side expression or a conclusion about the existence of an off-line zero of \(\xi\).

\clearpage

# The explicit formula on the original entire-function packet

This note proves the analytic identity needed to connect the [finite packet](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/WEIL_PACKET_DERIVATION.md) to the arithmetic side of Weil's explicit formula. It uses the programme's actual multiplier, retains both polynomial coordinates, and proves convergence of every term. The result is an identity, not a proof of positivity or of the Riemann hypothesis.

The classical source for the formula and the Fourier/Mellin conventions is Alain Connes and Caterina Consani, [*Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771v1](https://arxiv.org/abs/2006.13771v1), original author source `weil-compo.tex`, Appendix A, “Fourier versus Mellin transforms” (`appenmellinapp`), and Appendix B, “Explicit formula” (`appendix2`), source lines 2011–2070. In particular `bombieriexplicit`, `bombieriexplicit1`, and `burnolexplicit1` fix the pole terms, prime terms, and archimedean sign. That source states its formula for compactly supported functions. The proof below establishes the required extension directly for the present functions; it does not infer admissibility from a numerical residual.

## WA1. Objects, involutions, and the exact integrand

Let
\[
g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{WA1}
\]
Use the entire continuation of this classical function, with
\(g(1-s)=g(s)\), \(\overline{g(\bar s)}=g(s)\), and \(g(0)=g(1)=1\).
Retain the programme's counterfactual quartet
\[
\rho=\tfrac12+\delta+i\gamma,\quad
0<\delta<\tfrac12,\quad \gamma>2,\qquad
\mathcal R=(\rho,1-\bar\rho,\bar\rho,1-\rho).
\]
Each of these four distinct points is a zero of exact order \(m\ge1\) of \(g\). This is the original counterfactual input, not an assertion that such a zero has been found. Put
\[
h(s)=\prod_{\alpha\in\mathcal R}(s-\alpha)^m,
\quad v(s)=g(s)/h(s),\quad
\theta(s)=(s-\tfrac12)/i,\quad \iota(z)=\tfrac12+iz.
\tag{WA2}
\]
All apparent singularities of \(v\) are removable. At each packet point,
\[
v(\alpha)=\frac{g^{(m)}(\alpha)}{m!\prod_{\eta\in\mathcal R\setminus\{\alpha\}}(\alpha-\eta)^m}\ne0.
\]
For polynomials \(P,Q\in\mathbb C[z]\), define
\[
q_P=P\circ\theta,\quad q_Q=Q\circ\theta,\qquad
F_P(z)=P(z)v(\iota(z)),\quad F_Q(z)=Q(z)v(\iota(z)).
\]
For an entire function \(a\) in the \(s\)-coordinate, write
\(a^\#(s)=\overline{a(1-\bar s)}\). Conjugation followed by coefficient conjugation makes this entire, and the operation respects products. Reflection and conjugation permute the four factors of \(h\); the reflection contributes the sign \((-1)^{4m}=1\). Thus \(h^\#=h\) and \(v^\#=v\). The exact pairing integrand is
\[
A(s)=q_P^\#(s)q_Q(s)v(s)^2.
\tag{WA3}
\]
It is entire. On the critical line,
\[
K(t):=A(\tfrac12+it)=\overline{F_P(t)}F_Q(t),\qquad t\in\mathbb R.
\tag{WA4}
\]
At a packet point it is
\[
A(\alpha)=\overline{q_P(1-\bar\alpha)v(1-\bar\alpha)}\,q_Q(\alpha)v(\alpha).
\tag{WA5}
\]
These identities follow by substitution in the displayed involution. They do not replace \(q_P\) by \(P\).

## WA2. Uniform decay in every fixed vertical strip

Here is a decay proof that needs no zero-free horizontal line or estimate of \(\zeta'/\zeta\) inside the critical strip.

For \(\Re s>1\), integration of the absolutely convergent series for \(\zeta\) gives
\[
\zeta(s)=s\int_1^\infty\lfloor x\rfloor x^{-s-1}\,dx
=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.
\tag{WA6}
\]
For the first equality, write \(\lfloor x\rfloor=\sum_{n\ge1}1_{[n,\infty)}(x)\), exchange the absolutely convergent sum and integral, and integrate each term. The last integral is holomorphic for \(\Re s>0\), by uniform domination on compact subsets there. It therefore gives the meromorphic continuation to this half-plane and the bound
\[
|\zeta(s)|\le |s/(s-1)|+|s|/(\Re s).
\tag{WA7}
\]
In particular it is bounded by a constant times \(1+|\Im s|\) when the real part ranges in a fixed compact interval contained in \((0,\infty)\) and \(|\Im s|\ge2\).

For \(z=\sigma+it\), \(\sigma>0\), rotate the Euler integral for \(\Gamma(z)\) through the angle \(\vartheta\operatorname{sgn}(t)\), where \(0<\vartheta<\pi/2\). The integral on the small circular arc tends to zero because \(\sigma>0\); the large arc tends to zero because the real part of its ray is positive. Cauchy's theorem gives
\[
\Gamma(z)=e^{i\vartheta\operatorname{sgn}(t)z}
\int_0^\infty e^{-r e^{i\vartheta\operatorname{sgn}(t)}}r^{z-1}\,dr,
\qquad
|\Gamma(\sigma+it)|\le e^{-\vartheta|t|}
\frac{\Gamma(\sigma)}{(\cos\vartheta)^\sigma}.
\tag{WA8}
\]
The bound is uniform for \(\sigma\) in any positive compact interval. Apply it with \(\vartheta=\pi/3\) to \(\Gamma(s/2)\). Equations WA1 and WA7 show, uniformly in every fixed interval \(1/2\le\Re s\le B\),
\[
|g(s)|\le C_B(1+|\Im s|)^3 e^{-\pi|\Im s|/6}
\quad(|\Im s|\ge2).
\tag{WA9}
\]
Reflection \(g(s)=g(1-s)\) gives the same type of estimate on every fixed vertical strip, including negative real parts. The constant may depend on that strip. Applying Cauchy's derivative formula on circles of radius \(1/4\), inside a slightly larger strip, gives the same estimate with an adjusted constant for every fixed derivative of \(g\). The exponential changes on such a circle by at most a constant factor.

For \(|\Im s|\) larger than twice the largest modulus of a packet point plus the strip width, every factor of \(h\) has modulus bounded below by a fixed positive multiple of \(1+|\Im s|\). Division by this polynomial and multiplication by the finite polynomials \(q_P^\#,q_Q\) therefore give
\[
|A^{(j)}(s)|\le C_{B,P,Q,j}(1+|\Im s|)^{D_j}e^{-\pi|\Im s|/3}
\tag{WA10}
\]
on each fixed vertical strip, for each fixed derivative order \(j\). On its bounded remaining part, entireness supplies a finite maximum. The same argument gives exponential strip decay of \(F_P,F_Q\) and every fixed derivative, with exponent \(\pi/6\). These are estimates on the actual functions, not assertions of uniform constants as the packet or the polynomials vary.

## WA3. The inverse transform, convolution, and prime-tail convergence

Define
\[
f_P(u)=\frac1{2\pi}\int_{\mathbb R}F_P(t)e^{itu}\,dt,
\quad f_Q(u)=\frac1{2\pi}\int_{\mathbb R}F_Q(t)e^{itu}\,dt,
\quad k(u)=\frac1{2\pi}\int_{\mathbb R}K(t)e^{itu}\,dt.
\tag{WA11}
\]
Exponential decay and its derivative estimates show that these inverse transforms are Schwartz functions. More explicitly, differentiate under the integral for derivatives in \(u\), and integrate by parts any number of times for powers of \(u\). All boundary terms vanish by WA10, and all resulting integrals converge absolutely. Fourier inversion on Schwartz functions gives \(\widehat f_P=F_P\), \(\widehat f_Q=F_Q\) with the convention \(\widehat f(t)=\int f(u)e^{-iut}du\).

For any real \(R>0\), shift the \(t\)-contour in the last integral of WA11 to \(\Im t=R\) for \(u\ge0\), and to \(\Im t=-R\) for \(u<0\). The vertical connecting pieces tend to zero by WA10; multiplication by \(e^{itu}\) is bounded on each connecting segment for fixed \(u\). Thus
\[
|k(u)|\le C_R e^{-R|u|},\qquad
C_R=\frac1{2\pi}\max_{\epsilon=\pm1}
\int_{\mathbb R}|A(\tfrac12-\epsilon R+it)|\,dt<\infty.
\tag{WA12}
\]
The same proof applies to \(f_P,f_Q\), and to their derivatives after inserting powers of the integration variable. Fubini's theorem on Schwartz functions gives the exact convolution
\[
k=\widetilde f_P*f_Q,\qquad \widetilde f_P(u)=\overline{f_P(-u)}.
\tag{WA13}
\]
Its Fourier transform is \(\overline{F_P(t)}F_Q(t)=K(t)\), which proves the equality by Fourier inversion.

Let \(\Lambda_{\rm ar}(n)=\log \ell\) when \(n=\ell^r\) for a prime \(\ell\) and \(r\ge1\), and zero otherwise. This is the arithmetic von Mangoldt function, not the observation map. Since \(0\le\Lambda_{\rm ar}(n)\le\log n\), taking any \(R>1/2\) in WA12 proves absolute convergence of
\[
\sum_{n\ge2}\frac{\Lambda_{\rm ar}(n)}{\sqrt n}
\bigl(k(\log n)+k(-\log n)\bigr).
\tag{WA14}
\]
There is also the explicit bound for every integer \(N\ge2\):
\[
\sum_{n>N}\frac{\Lambda_{\rm ar}(n)}{\sqrt n}
\bigl(|k(\log n)|+|k(-\log n)|\bigr)
\le 2C_R\sum_{n>N}\frac{\log n}{n^{R+1/2}}.
\tag{WA15}
\]
For example, with \(R=2\), the right side is at most
\[
2C_2N^{-3/2}\left(\frac23\log N+\frac49\right).
\tag{WA16}
\]
Indeed \((\log x)x^{-5/2}\) is decreasing for \(x\ge2\), so its sum beyond \(N\) is bounded by its integral from \(N\) to infinity; integration by parts gives the displayed expression. A numerical error certificate would additionally require a certified numerical bound for \(C_2\); the existence proof alone is not such a certificate.

## WA4. Cancellation of every unwanted zero

Set
\[
L(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)=\frac{g(s)}{s(s-1)},
\qquad \ell(s)=L'(s)/L(s).
\tag{WA17}
\]
This meromorphic completed function has simple poles at \(0,1\), is invariant under \(s\mapsto1-s\), and otherwise has exactly the nontrivial zeta zeros with their multiplicities. These assertions also follow from WA1 and the stated entire continuation of \(g\). As a meromorphic identity,
\[
\ell(s)A(s)=q_P^\#(s)q_Q(s)\frac{g'(s)g(s)}{h(s)^2}
-\frac{A(s)}s-\frac{A(s)}{s-1}.
\tag{WA18}
\]
Away from the roots of \(g\), this is the logarithmic derivative identity and cancellation of one factor of \(g\). Both sides then have the same meromorphic continuation.

At a zero outside \(\mathcal R\), the first term in WA18 is holomorphic: its denominator does not vanish there. At \(\alpha\in\mathcal R\), the logarithmic derivative of \(g\) has residue \(m\); multiplication by the entire function \(A\) gives residue \(mA(\alpha)\), also when that residue is zero. At \(0,1\), the residues are respectively \(-A(0),-A(1)\). These are the only possible poles. This proves exact cancellation at every other zero, regardless of its location or multiplicity.

Choose a rectangle with vertical sides \(\Re s=3/2\) and \(\Re s=-1/2\), and horizontal sides \(\Im s=\pm T\), for \(T>\gamma+1\). There are no poles on its boundary after the removable singularities in WA18 have been filled. Equations WA9–WA10 bound its horizontal integrals by a polynomial in \(T\) times \(e^{-\pi T/3}\). They therefore tend to zero for all sufficiently large \(T\), without selecting a sequence avoiding other zeta zeros. The residue theorem and \(\ell(1-s)=-\ell(s)\) give
\[
m\sum_{\alpha\in\mathcal R}A(\alpha)-A(0)-A(1)
=\frac1{2\pi i}\int_{\Re s=3/2}
\ell(s)\bigl(A(s)+A(1-s)\bigr)\,ds.
\tag{WA19}
\]
The integral is oriented upwards. To verify the sign, the positively oriented left edge is downward. Writing it as minus an upward integral and substituting \(w=1-s\) changes \(\ell(1-w)\) to \(-\ell(w)\); its total contribution is therefore the plus \(A(1-s)\) term in WA19.

## WA5. The arithmetic integral and its exact signs

On \(\Re s=3/2\), the absolutely convergent Euler product gives
\[
\ell(s)=-\tfrac12\log\pi+\tfrac12\psi(s/2)
-\sum_{n\ge2}\Lambda_{\rm ar}(n)n^{-s},
\qquad \psi=\Gamma'/\Gamma.
\tag{WA20}
\]
For completeness, absolute convergence follows from \(\sum_{n\ge2}(\log n)n^{-3/2}<\infty\). Expanding each Euler factor as a geometric series gives \(\zeta\); expanding its logarithm and differentiating on any strictly smaller closed half-plane gives the last series with the displayed coefficients. Uniform convergence justifies that differentiation and shows the product is nonzero there.

The gamma factor in WA20 is holomorphic between real parts \(1/2\) and \(3/2\). Its growth is at most polynomial, which is sufficient here. One direct bound uses
\[
\psi(z)=-\gamma_E+\sum_{j=0}^\infty
\left(\frac1{j+1}-\frac1{j+z}\right),\qquad \Re z>0.
\tag{WA21}
\]
This expansion follows by logarithmic differentiation of Euler's gamma product, uniformly on compact subsets of this half-plane. For \(\Re z\ge a>0\), its summand has modulus at most
\(|z-1|/((j+1)(j+a))\), so the series gives \(|\psi(z)|\le C_a(1+|z|)\). Gamma conjugation gives \(\psi(\bar z)=\overline{\psi(z)}\). Shift the gamma integral in WA19 to \(\Re s=1/2\); the horizontal pieces vanish by this bound and WA10. Then substitute \(s=1/2+it\), and in the term with \(A(1-s)\) replace \(t\) by \(-t\). The result is
\[
\frac1{2\pi}\int_{\mathbb R}K(t)
\left(\Re\psi(\tfrac14+\tfrac{it}2)-\log\pi\right)dt.
\tag{WA22}
\]
All these integrals are absolutely convergent.

For the Dirichlet series part, WA10 and its absolute convergence on \(\Re s=3/2\) permit termwise integration by absolute domination. For each fixed \(n\), shift the entire integrand \(n^{-s}(A(s)+A(1-s))\) to the critical line. WA11 then gives
\[
\frac1{2\pi i}\int_{\Re s=3/2}n^{-s}
\bigl(A(s)+A(1-s)\bigr)ds
=\frac{k(-\log n)+k(\log n)}{\sqrt n}.
\tag{WA23}
\]
The first sign comes from \(n^{-it}=e^{-it\log n}\); reflection changes it for the second term. Thus the prime contribution is exactly minus WA14. Its convergence can be justified either before the shift by the absolutely convergent Dirichlet series or afterwards by WA12–WA15.

Combining WA19, WA22 and WA23 proves the complete identity
\[
\boxed{\begin{aligned}
m\sum_{\alpha\in\mathcal R}
\overline{q_P(1-\bar\alpha)v(1-\bar\alpha)}\,q_Q(\alpha)v(\alpha)
={}&A(0)+A(1)\\
&+\frac1{2\pi}\int_{\mathbb R}\overline{F_P(t)}F_Q(t)
\left(\Re\psi(\tfrac14+\tfrac{it}2)-\log\pi\right)dt\\
&-\sum_{n\ge2}\frac{\Lambda_{\rm ar}(n)}{\sqrt n}
\bigl(k(\log n)+k(-\log n)\bigr).
\end{aligned}}
\tag{WA24}
\]
It holds for every pair of polynomials and every packet satisfying the retained original hypotheses. No assumption of Weil positivity enters its proof.

## WA6. Exact comparison with the published multiplicative convention

Define a function on \(\mathbb R_{>0}\) by
\[
b_A(x)=x^{-1/2}k(-\log x).
\tag{WA25}
\]
It has decay sufficient for all the following integrals by WA12. Substituting \(x=e^u\) in its Mellin transform gives
\[
\int_0^\infty b_A(x)x^{s-1}dx
=\int_{\mathbb R}k(-u)e^{(s-1/2)u}du=A(s).
\tag{WA26}
\]
On the critical line this is Fourier inversion, and on the whole plane it follows by the same absolutely convergent transform and analytic continuation. Its involution satisfies
\[
b_A^\sharp(x)=x^{-1}b_A(x^{-1})=x^{-1/2}k(\log x).
\tag{WA27}
\]
Consequently the two pole integrals in `bombieriexplicit` are precisely \(A(1),A(0)\); for the second integral use the substitution \(y=x^{-1}\). At a prime power \(x=\ell^r\), its two finite-place terms are exactly \(\ell^{-r/2}(k(-r\log\ell)+k(r\log\ell))\). The opposite of the archimedean distribution in `burnolexplicit1` is the integral in WA24. Equations WA25–WA27 prove the complete change of conventions, including its inverse \(k(u)=e^{-u/2}b_A(e^{-u})\). The function is not asserted compactly supported; WA19–WA24 provide the required analytic extension.

## WA7. Consequence for the programme's finite form, with the radical retained

Let \(E_h=\mathbb C[s]/(h)\), let \(U=M_{j_h(v)}\) be the literal finite Taylor-remainder multiplier, and let \(e:E_h\to\mathbb C^{\mathcal R}\) evaluate the zeroth jets. The finite proofs WP13–WP25 give its complete jet formula and establish
\[
a_h=eU,\qquad a_h([q])=(q(\alpha)v(\alpha))_\alpha,\qquad
\ker a_h=(d)/(d^m),\quad d=\prod_{\alpha\in\mathcal R}(s-\alpha).
\tag{WA28}
\]
The elementary proof of the kernel is that all \(v(\alpha)\) are nonzero and a polynomial vanishes at the four distinct points exactly when divisible by \(d\). Surjectivity follows from interpolation at those points. The actual multiplier retains the higher jets, as specified in WP21; WA28 takes their stated quotient.

In the displayed order of \(\mathcal R\), the left side of WA24 is the pullback under \(a_h\) of
\[
b(c,d)=m(\bar c_2d_1+\bar c_1d_2+\bar c_4d_3+\bar c_3d_4).
\tag{WA29}
\]
Each pair has matrix \(m\begin{pmatrix}0&1\\1&0\end{pmatrix}\), with eigenvectors \((1,1)\), \((1,-1)\) and eigenvalues \(m,-m\). Hence this form has inertia \((2,2)\), and its pullback has inertia \((2,2,4m-4)\) and radical exactly WA28. The degree-three polynomial
\[
q_-(s)=\frac{\prod_{\eta\ne\alpha_1}(s-\eta)}
{v(\alpha_1)\prod_{\eta\ne\alpha_1}(\alpha_1-\eta)}
-\frac{\prod_{\eta\ne\alpha_2}(s-\eta)}
{v(\alpha_2)\prod_{\eta\ne\alpha_2}(\alpha_2-\eta)}
\tag{WA30}
\]
has amplitude values \((1,-1,0,0)\). Taking \(P_-=q_-\circ\iota\), and \(P=Q=P_-\) in WA24, proves that its full arithmetic right side is exactly \(-2m\). This is the arithmetic identity associated with the assumed off-line packet. It is not a constructed off-line zero and does not establish that the arithmetic right side is nonnegative for zeta.

The analytic identity closes the admissibility question for these noncompact test functions. The remaining RH question is an actual sign statement for the right side of WA24 on this programme family. Neither positive source norms nor the nonzero divided-power classes alone prove that sign. Their comparison must supply a proved map and an inequality before any RH conclusion can be drawn.

\clearpage

# Tau residue norms and the exact change in the Weil formula

The original semiring is \(S=G(\mathbb Z)=\{\tau\}\sqcup\mathbb Z\), with the original integer operations, \(\tau+x=x\), and \(\tau x=\tau\). Write \(e=0_{\mathbb Z}\), retaining \(e\ne\tau\). This calculation starts from its residue and support maps. It does not replace a chosen residue norm by a different one without recording the map.

The originating programme's `globalization_note.tex`, ideal/congruence/zeta sections, proves the original arithmetic ideal norm and its zeta function. Its prime spectrum is two-dimensional. The companion TAU_PRIME_SPECTRUM_DERIVATION.md checks that classification, its localizations and the coefficient maps in full. Here the calculation continues from the different residue constructions to their exact prime distributions and Weil forms.

## TN1. Three numerical constructions, with their quotient maps

For \(n\ge1\), reduction of supported integers defines the support-preserving semiring map
\[
\pi_n:S\longrightarrow G(\mathbb Z/n\mathbb Z),\qquad
\tau\longmapsto\tau_n,\quad a\longmapsto(a\bmod n)^\bullet.
\tag{TN1}
\]
It is onto and preserves both operations by their definitions. Its equivalence classes keep \(\tau\) separate from every integer. Its global-zero fibre is only \(\{\tau\}\). Arithmetic projection gives a second surjection
\[
G(\mathbb Z/n\mathbb Z)\longrightarrow\mathbb Z/n\mathbb Z,
\quad\tau_n\longmapsto0,\quad b^\bullet\longmapsto b.
\tag{TN2}
\]
The composite has zero fibre \(I_n=\{\tau\}\cup n\mathbb Z\). The two target cardinalities are \(n+1\) and \(n\), respectively. At \(n=1\) the first target is the two-element Boolean semiring and the second is the one-element ring; this case is retained.

The usual ideal product is \(I_mI_n=I_{mn}\). Every finite sum of products of multiples of \(m,n\) is a multiple of \(mn\), and every multiple of \(mn\) is itself such a product; the adjoined identity \(\tau\) causes no further integer values. Hence the second cardinality is multiplicative, whereas the first has the exact defect
\[
(m+1)(n+1)-(mn+1)=m+n.
\tag{TN3}
\]
Consequently the two actual ideal sums on \(I_n\), for \(\Re s>1\), are
\[
Z_{\rm ar}(s)=\sum_{n\ge1}n^{-s}=\zeta(s),\qquad
Z_{\rm card}(s)=\sum_{n\ge1}(n+1)^{-s}=\zeta(s)-1.
\tag{TN4}
\]
The second equality is an index change in an absolutely convergent series. It does not have the prime Euler product obtained by replacing every \(p\) by \(p+1\).

There is also a precisely defined multiplicative prime weight
\[
N_{\rm pr}(n)=\prod_{p\mid n}(p+1)^{v_p(n)},\qquad N_{\rm pr}(1)=1.
\tag{TN5}
\]
This agrees with the first residue cardinality at prime integers, but not at general integers or at \(1\). Unique factorization gives its separate Euler product
\[
E_{\rm pr}(s)=\sum_{n\ge1}N_{\rm pr}(n)^{-s}
=\prod_p\frac1{1-(p+1)^{-s}},\qquad \Re s>1.
\tag{TN6}
\]
Absolute convergence follows from \(N_{\rm pr}(n)\ge n\); expanding finite products and then passing to the absolutely convergent limit proves the identity. Thus all three functions in TN4 and TN6 are defined, and none is substituted for another.

## TN2. The exact mixed-support reason for TN3

For commutative rings \(R,T\), let \(\chi_R:G(R)\to\mathbb B\) send \(\tau\) to \(0\) and every supported element to \(1\); similarly for \(T\). There is a semiring isomorphism
\[
G(R\times T)\xrightarrow{\sim}
G(R)\times_{\mathbb B}G(T),
\quad \tau\longmapsto(\tau_R,\tau_T),\quad
(r,t)^\bullet\longmapsto(r^\bullet,t^\bullet).
\tag{TN7}
\]
The fibre product contains exactly the displayed two types, because equality of support means either both entries are absent or both are supported. The map is a bijection. Addition and multiplication on two supported entries are the ring product operations; entries involving the absent pair obey the external identity and absorber laws. These checks prove preservation of both operations, both identities, and the inverse laws. They also prove the pullback universal property: a pair of semiring maps with equal support takes values in exactly this subset, and therefore factors uniquely through it.

If \(m,n\) are coprime, choose integers \(u,v\) with \(um+vn=1\). The usual reduction map \(\mathbb Z/mn\to\mathbb Z/m\times\mathbb Z/n\) is injective because divisibility by both coprime integers implies divisibility by their product; it is surjective because \(bvn+cum\) has residues \(b,c\). Applying TN7 gives
\[
G(\mathbb Z/mn)\cong
G(\mathbb Z/m)\times_{\mathbb B}G(\mathbb Z/n).
\tag{TN8}
\]
Its embedding into the full product omits precisely
\[
(\mathbb Z/m)^\bullet\times\{\tau_n\},\qquad
\{\tau_m\}\times(\mathbb Z/n)^\bullet.
\tag{TN9}
\]
These disjoint mixed-support subsets have sizes \(m,n\). TN3 is therefore the count of explicitly identified subsets. No supported cancellation is renamed as absence. In support-separated counts the vector is \((1,n)\); fibre-product multiplication is componentwise, \((1,m)(1,n)=(1,mn)\). Forgetting the labels by summing coordinates gives \(n+1\), and TN3 measures exactly the failure of that sum map to be multiplicative.

## TN3. Exact analytic comparison for the prime weight

On \(\Re s>0\), use the branch
\[
\log(1-x^{-s})=-\sum_{j\ge1}\frac{x^{-js}}j,\qquad x\ge2,
\]
and define
\[
L_\tau(s)=\sum_p\bigl(\log(1-p^{-s})-\log(1-(p+1)^{-s})\bigr),
\quad R_\tau(s)=e^{L_\tau(s)}.
\tag{TN10}
\]
This definition has no branch ambiguity because \(|x^{-s}|<1\). To prove convergence, differentiate the summand with respect to the real variable \(x\):
\[
\log(1-p^{-s})-\log(1-(p+1)^{-s})
=-s\int_p^{p+1}\frac{x^{-s-1}}{1-x^{-s}}\,dx.
\tag{TN11}
\]
Fix \(a>0\), and put \(d_a=1-2^{-a}>0\). On \(\Re s\ge a\), the absolute value of the integrand without \(s\) is at most \(x^{-a-1}/d_a\). The prime intervals are disjoint subsets of \([2,\infty)\), so
\[
|L_\tau(s)|\le \frac{|s|2^{-a}}{a d_a}.
\tag{TN12}
\]
The same domination proves local uniform convergence of the series on the open half-plane. It therefore defines a holomorphic function, and its exponential is holomorphic and nowhere zero. On \(\Re s>1\), the absolutely convergent Euler products give
\[
E_{\rm pr}(s)=\zeta(s)R_\tau(s).
\tag{TN13}
\]
This supplies a meromorphic continuation of the particular function TN6 to \(\Re s>0\). Its zero and pole divisor there equals that of \(\zeta\), with multiplicities, because \(R_\tau\) is a holomorphic unit. This is a statement about TN6 with TN5, not about TN4's function \(\zeta-1\), and not about an isomorphism of spectra or trace spaces.

The retained logarithmic-derivative correction is
\[
r_\tau(s)=\frac{R_\tau'(s)}{R_\tau(s)}
=\sum_p\left(\frac{\log p}{p^s-1}
-\frac{\log(p+1)}{(p+1)^s-1}\right).
\tag{TN14}
\]
One may differentiate locally uniformly in TN10 by holomorphy and Cauchy's formula on slightly larger compact sets. A direct formula, including a vertical bound, is
\[
r_\tau(s)=\sum_p\int_p^{p+1}x^{-s-1}
\left(\frac{s\log x}{(1-x^{-s})^2}-\frac1{1-x^{-s}}\right)dx,
\tag{TN15}
\]
\[
|r_\tau(s)|\le
\frac{2^{-a}}{a d_a}
+\frac{\displaystyle |s|2^{-a}\left(\frac{\log2}{a}+\frac1{a^2}\right)}{d_a^2},
\qquad \Re s\ge a.
\tag{TN16}
\]
For TN15, differentiate \((\log x)/(x^s-1)\) in \(x\) and integrate its negative derivative from \(p\) to \(p+1\). The estimates use \(\int_2^\infty x^{-a-1}dx=2^{-a}/a\) and \(\int_2^\infty(\log x)x^{-a-1}dx=2^{-a}(\log2/a+1/a^2)\). They prove absolute local uniform convergence, and show that \(r_\tau\) has at most linear vertical growth in every fixed strip inside this half-plane. All quantities in TN10–TN16 are retained; equality of a zero divisor does not remove this nonzero correction.

## TN4. The corresponding prime distributions

Use the programme's actual entire test functions from WEIL_PACKET_ANALYTIC_DERIVATION.md:
\[
A(s)=q_P^\#(s)q_Q(s)v(s)^2,\quad
K(t)=A(\tfrac12+it)=\overline{F_P(t)}F_Q(t),\quad
k(u)=\frac1{2\pi}\int_{\mathbb R}K(t)e^{itu}dt.
\tag{TN17}
\]
Its proof WA2–WA3 establishes exponential decay of \(A\) in every fixed vertical strip and \(|k(u)|\le C_R e^{-R|u|}\) for every fixed \(R>0\). Define the two explicit prime functionals
\[
\begin{aligned}
\mathcal P(k)&=\sum_p\sum_{j\ge1}(\log p)p^{-j/2}
\bigl(k(j\log p)+k(-j\log p)\bigr),\\
\mathcal P_\tau(k)&=\sum_p\sum_{j\ge1}\log(p+1)(p+1)^{-j/2}
\bigl(k(j\log(p+1))+k(-j\log(p+1))\bigr).
\end{aligned}
\tag{TN18}
\]
Both sums converge absolutely: for \(R=2\), each is dominated by a constant times \(\sum_p(\log(p+1))(p+1)^{-5/2}/(1-(p+1)^{-5/2})\), or the analogous expression with \(p\); each is bounded by a convergent sum over all integers.

The exact difference is
\[
\boxed{\mathcal P(k)-\mathcal P_\tau(k)
=\frac1{2\pi}\int_{\mathbb R}K(t)
\,2\Re r_\tau(\tfrac12+it)\,dt.}
\tag{TN19}
\]
To prove it, start with
\[
\frac1{2\pi i}\int_{\Re s=3/2}
r_\tau(s)\bigl(A(s)+A(1-s)\bigr)ds.
\]
On this line, expand both terms in TN14 as absolutely convergent geometric series and integrate term by term. Fourier inversion and an entire contour shift give exactly the difference in TN18, with the factors \(p^{-j/2}\) and \((p+1)^{-j/2}\). Alternatively shift the integral itself to \(\Re s=1/2\). No poles are crossed because \(r_\tau\) is holomorphic for positive real part; its vertical bound TN16 and the strip decay of \(A\) make the horizontal integrals tend to zero. Reflect \(t\mapsto-t\) in the second summand. Since TN10 has real coefficients under conjugation, \(r_\tau(\bar s)=\overline{r_\tau(s)}\). This gives TN19, including its sign and factor \(2\).

## TN5. Weil's condition with the full tau correction

Let
\[
w_\infty(t)=\Re\psi(\tfrac14+\tfrac{it}2)-\log\pi,
\qquad
w_{\infty,\tau}(t)=w_\infty(t)-2\Re r_\tau(\tfrac12+it).
\tag{TN20}
\]
The complete analytic identity WA24 and TN19 give
\[
\boxed{B_h([q_P],[q_Q])
=A(0)+A(1)
+\frac1{2\pi}\int_{\mathbb R}\overline{F_P(t)}F_Q(t)
w_{\infty,\tau}(t)dt
-\mathcal P_\tau(k).}
\tag{TN21}
\]
Here \(B_h\) is the literal full-jet packet form with its exact radical, as constructed in WP28–WP29. To check the sign directly, TN19 says \(\mathcal P=\mathcal P_\tau+D\), where \(D\) is the integral of \(2\Re r_\tau\). Substitution into the original term \(-\mathcal P\) subtracts this integral, giving TN20. Thus altering the prime norms alone while keeping the previous infinite-place term does not produce the same form; TN20 is its required exact correction.

For \(P=Q\), the right side of TN21 is real. Its nonnegativity is exactly the original packet's Weil positivity condition, since TN21 is an equality of forms. This calculation does not prove that condition. It supplies a full new expression of the condition through the separately defined prime-residue weight, preserving the support cardinality defect and the correcting distribution. In particular the degree-three negative representative WP36 of an assumed off-line packet still gives the exact value \(-2m\) in TN21.

## TN6. What this does and does not identify

There are exact maps from the original tau semiring to two different residue targets, an exact support fibre product explaining the failure of scalar count multiplicativity, and a complete analytic comparison from one specified prime-residue Euler product to its Weil functional. These statements use the original addition and keep its supported zero. They do not replace the two-dimensional semiring spectrum by the one-dimensional arithmetic spectrum, or identify either with Connes's adele-class orbit space.

The further Connes calculation must retain the supported coordinate-zero hyperplanes, their stabilizers and transverse additive fields, and the new absence strata. Those are the objects entering Section VI, equations (5)–(15), of Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, arXiv:math/9811068v1](https://arxiv.org/abs/math/9811068v1). The independent endpoint and adelic comparison continues in TAU_CONNES_ENDPOINT_DERIVATION.md and TAU_PRIME_SPECTRUM_DERIVATION.md. No equality of their Hilbert-space traces is assumed from the scalar function identity TN13.

\clearpage

# Sources, exact proof locations, and reading scope

This addition develops the established tau/split-zero base, the original escaping inverse fibre, and the actual quotient-size interpolation. Every new algebraic and analytic calculation appears in full in the eight accompanying proof files. The exact operator input retains its earlier public definitions and proofs; those are linked below. This is not a historical novelty claim or a proof of the Riemann hypothesis.

## Earlier programme proofs

- The supported-zero prime and chain are prior programme results. Paper 1 is *An Algebraic Structure Incorporating a Z/1Z-Symmetric Element Adjoined to the Integers: Construction, Analysis, and Generalizations*, original `11.tex`, [complete public source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/ac168d55cbb400a6c8926a00d67909ba65646ac5/workbenches/splitzero-tandem/branches/identity-absorber-square/sources/17555345_11.tex), labels `thm:prime_ideals_S`, `thm:krull_dim_S`, `eq:maximal_chain`. The source was read completely, 1–1833. The user attributes this result to Gemini Pro 2.5; this is received attribution, not an inferred author field. The present proof of the full-support statement is [FSR1–FSR7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/FULL_SUPPORT_RECONSTRUCTION_DERIVATION.md).
- *Split Support Geometry: Universal Zero Fibres, Arithmetic Curves, and Frobenius-Perfect Quantization*, The Clankers, June 2026, version `split_support_geometry_arithmetic_curve_v11910.tex`, SHA256 `8443cc0401b18d373939d992f0a2f5384ee2fa1130f059753d5f3972eec5052d`. Root reading covers 1–1910; used definitions and proofs are 1180–1871. This is the received full-lattice foundation. The complete receiving proof, including all needed definitions, is [FSR1–FSR36](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/FULL_SUPPORT_RECONSTRUCTION_DERIVATION.md), not an assertion that the entire source was read.
- The actual escaping map and heat constants are in [Source mechanism transfer](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/ac168d55cbb400a6c8926a00d67909ba65646ac5/satellites/23_source_mechanism_transfer.tex), labels `eq:retained-node-map`, `eq:retained-arithmetic-extension`, and [Incompressible fibre heat](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/ac168d55cbb400a6c8926a00d67909ba65646ac5/satellites/26_incompressible_fibre_heat.tex), labels `eq:ifh-original`, `eq:ifh-chart`, `eq:ifh-target-flow`, `eq:ifh-triple`. Both local source versions were read completely; EFI records their exact hashes. The new derivation [EFI1–EFI68](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/ESCAPING_FIBRE_INFINITESIMAL_DERIVATION.md) proves every received polynomial identity it uses.
- The original metric and observation are in [Observed current plane](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/OBSERVED_CURRENT_PLANE.tex#L90), OCP1 and OCP5–OCP7. Read coverage is 35–169. The published exact incoming family and support maps are [Observed deformation and current](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/OBSERVED_DEFORMATION_AND_CURRENT.md#L22), DF1–DF16, and [Support spectrum and terminal mass](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/SUPPORT_SPECTRUM_AND_TERMINAL_MASS.md), ST1–ST20, both read completely and byte-matched to their public sources.
- The subsequent complete incoming proofs are [Observed collision](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_COLLISION.md), OC1–OC17; [Observed support propagation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_SUPPORT_PROPAGATION.md), OSP1–OSP51; and [Observed cotangent and Frobenius](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_COTANGENT_FROBENIUS.md), OCF1–OCF23 and OIF1–OIF36. ISP and EFI give the new exact trace/current and escaping-family comparisons.

## Supplied original LaTeX on separated zeta interpolation

The source-reading ledger is keyed to canonical IDs from the existing disk index. Its search results were used for routing; they were not counted as reading.

| Source | Exact version and root reading | Result used here |
|---|---|---|
| *Secondary Note on Split-Zero Globalization*, The Clankers; PUBUNIT-B1A260A5E731EA568C353AA4 | `split_zero_secondary_note.tex`, SHA256 `8e1aa2f934c49fc21e7a3d946ac6a465bc1a68896ec184afcb3d989cc9f8b364`; complete 1–1997 | `def:hurwitz-specialization`, `thm:universal-taylor-deformation`, `thm:arithmetic-kernels-riemann`, `cor:first-log-jet-explicit`; [NL1–NL18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/NON_EULERIAN_LENGTH_DERIVATION.md), [SW1–SW42](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SHIFTED_WEIL_POSITIVITY_DERIVATION.md) give the complete receiving proofs. |
| *Split-Zero Support Repair*, source author field “The Clankers / prepared in continuation”; PUBUNIT-C4735C0E0B05FF5D811C3F89 | `some considerrations.tex`, SHA256 `3f98c8eab35f87996a594d0afa7d77ba561cbc28b632fa33e16d2d6228416702`; 1473–1739 | Conservative ideal/zeta side and shifted deformation. The multiplicative ideal-norm hypothesis is retained explicitly in NL. |
| Split-zero defect preprint, blank source author field; PUBUNIT-6C3FFDFC49FDF75FE8EB43E3 | `split_zero_defect_preprint (1).tex`, SHA256 `1d5f15f9999b402356d6ba46286f2473ee6c857f55e091c836c905ca15b4695e`; 480–854 | Endpoint residues and the invariant/anti-invariant decomposition. SW distinguishes function residues from logarithmic-derivative multiplicities and derives the reflection defect. |
| Primitive defect preprint; PUBUNIT-2B18D475F69385B03F1E2B30 | `primitive_defect_preprint.tex`, SHA256 `2f3289f6a04105d3f15fe5f7c36dde286515e61f465caf1582f9808e19f3d2f7`; 1–385; the two supplied copies are identical | Retained augmentation kernel; not used as a positivity theorem. |
| Primitive support defects; PUBUNIT-E4607F9536B56699EB520E23 | `primitive_support_defects_preprint.tex`, SHA256 `f12f2c1c36effbf89740e308733d8434989e69cc088a0fc1c686281a157b42c5`; 1–440 | Source comparison for signed support defects. |
| Split-zero moonshine repair; PUBUNIT-396B23CD772DEC7617B4A2A5 | `split_zero_moonshine_repair.tex`, SHA256 `7e672f7f1c21ae8dca327a65d8395d1a8b201bbddebb4d0317a96ab9e2382538`; complete 1–826 | Character-coefficient positivity and retained negative polar data were read; no moonshine theorem is applied to infer Weil positivity. |

These received manuscripts are identified as programme sources. The independently written complete receiving proofs are included here. No private correspondence is reproduced.

## Human sources

- Alain Connes and Caterina Consani, [*Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771v1](https://arxiv.org/abs/2006.13771v1); [original author source archive](https://arxiv.org/src/2006.13771v1), `weil-compo.tex`, Appendix A “Fourier versus Mellin transforms” (`appenmellinapp`) and Appendix B “Explicit formula” (`appendix2`), 2011–2070. This exact source block was read. Labels `bombieriexplicit`, `bombieriexplicit1`, `burnolexplicit1` fix the signs and conventions. The original archive is retained privately unchanged. [WA1–WA30](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/WEIL_PACKET_ANALYTIC_DERIVATION.md) proves the extension to the actual entire test functions, with convergence.
- Terence Tao, [*A digestion of the Jacobian conjecture counterexample*, 21 July 2026](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/), displayed original polynomial map; David Speyer, [*The new counterexample to the Jacobian conjecture*, 20 July 2026](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/), marked-factor discussion, as cited by the programme's source. The first displayed map was checked live. Reading those posts does not claim a fresh audit of every original counterexample argument. EFI1–EFI3 and its exact check script verify the polynomial map and its inverse chart directly.
- [NIST DLMF, §25.11](https://dlmf.nist.gov/25.11), definitions, recurrence, special values and parameter derivative, equations 25.11.1, 25.11.3, 25.11.13, 25.11.14, 25.11.17, were checked in the primary HTML. Equation-TeX downloads returned HTTP 403 and the browser extractor rejected the TeX content type; no source download is claimed, and no PDF was substituted. SW3–SW8 supplies the needed continuation and derivative proofs independently.

The historical cotangent and prism foundations remain Luc Illusie's regular-immersion and transitivity theorems and Bhatt–Scholze's prism definitions, at the exact original-source locators retained in the linked OCF/OIF paper. This addition proves the specified polynomial and coefficient maps; it does not assert an unproved equality between complex Weil pairings and prismatic cohomology.
