# Independent review of the leading-coefficient transport proof

Date: 2026-09-13. Scope: all of the complete proof fragment
arithmetic_endpoint_leading_line_transport_20260913.tex, including AL.1--11,
the endpoint diagram, the source metrics, and the empty-packet paragraph.

Final reviewed source: 9,080 bytes, 200 lines, SHA-256
ae87f325b66c3e07830eb0362657cad0825d84d23dd38b5c7500f1deda154962.
I read this complete final file after the source author incorporated the
supported-domain expansion. The earlier reviewed source had SHA-256
35a2a57f25b01527a2af06c5a8d69bcd776badfee27449e586d9bfe159f6d12e;
the only intervening addition gives the finite and full polynomial fibre
domains and proves their kernel intersection by degree.

The mathematical claims in AL.1--11 are correct. The restriction $n\ge q$ on
the graded isomorphism is exact, and its endpoint replacement is the zero map
from a zero-dimensional relation degree to a one-dimensional leading line.
The norm and the adjoint in AL.8 use the original quotient weights and have
the correct ratio and orientation. The sign in AL.10 is correct.

The final supported-map paragraph explicitly states that its finite
polynomial fibre is $\mathcal P_n$, identifies its kernel with the image
in AL.3, states the full-polynomial kernel $\chi\mathbb C[S]$, and proves
the compatible intersection with $\mathcal P_n$. Section 6 below gives
the complete independent calculation of the same maps. The domain
annotation is incorporated and no correction remains outstanding.

This review performed no compiler, mathematical checker, or Lean run and made
no change to the reviewed TeX. The original density and source intertwining
map are the supplied programme inputs. The integrability and positivity
claims are also verified from the analytic facts proved in the separate
arithmetic endpoint review. The following is an independent calculation of
every new finite-dimensional assertion in this fragment.

## 1. Original form and the leading-coefficient quotient

Fix the original $h,k$, the coordinate $S=k/2+iu$, and

\[
\langle P,Q\rangle_{h,k}
=\int_{\mathbb R}\overline{P(k/2+iu)}Q(k/2+iu)m_{h,k}(u)\,du,
\quad m_{h,k}=w_h^{*k},\qquad
w_h(t)=\frac{|((2\xi)/h)(1/2+it)|^2}{2\pi}.
\]

The convention is conjugate-linear in $P$ and linear in $Q$. The entire
quotient defining $w_h$ is nonzero and has a discrete zero set on the line;
its exponential tail makes all its polynomial moments finite. Thus $w_h$ is
positive almost everywhere, bounded, and integrable with mass $\mu_h>0$.
For each $k\ge2$, the nonnegative convolution integrand is positive almost
everywhere in its integration variables, so $m_{h,k}$ is positive at every
real argument. Its moments are finite by the retained two-sided exponential
moments. Nonnegative Fubini gives its mass exactly $\mu_h^k$.

If $P$ is a nonzero polynomial, then $P(k/2+iu)$ vanishes at finitely many
real $u$. Its squared modulus times $m_{h,k}$ is positive almost everywhere
outside those points, so its integral is strictly positive. Hence the form
is positive definite on each finite-dimensional $\mathcal P_a$.

Set $\mathcal P_a=\mathbb C[S]_{\le a}$ for $a\ge0$ and $\mathcal P_a=0$
for $a<0$. Let $\Pi_{a-1}:\mathcal P_a\to\mathcal P_{a-1}$ denote the
orthogonal projection for this actual form, with $\Pi_{-1}=0$.
Then

\[
p_a=S^a-\Pi_{a-1}S^a
\]

has leading coefficient one and is orthogonal to $\mathcal P_{a-1}$.
Every other monic polynomial of degree $a$ has the form $p_a+v$ with
$v\in\mathcal P_{a-1}$. Consequently

\[
\|p_a+v\|_{h,k}^2=\|p_a\|_{h,k}^2+\|v\|_{h,k}^2.
\]

This proves existence and uniqueness of the monic minimizer and gives
$\omega_a=\|p_a\|_{h,k}^2>0$. Let
$\ell_a:\mathcal P_a\to\mathcal L_a=\mathcal P_a/\mathcal P_{a-1}$
be the degree quotient map. The exact identities are

\[
[p_a]=[S^a],\qquad
\|\ell_a(zp_a)\|_{\mathcal L_a}^2=|z|^2\omega_a.
\]

Indeed every representative of $z[p_a]$ is $zp_a+v$ and its norm squared is
$|z|^2\omega_a+\|v\|^2$. This proves AL.2 directly from the quotient-norm
definition. The isometric section is

\[
s_a:\mathcal L_a\longrightarrow\mathcal P_a,\qquad
s_a(z[p_a])=zp_a.
\]

It satisfies $\ell_as_a=I_{\mathcal L_a}$ and
$s_a\ell_a=I_{\mathcal P_a}-\Pi_{a-1}$.
At degree zero, $p_0=1$ and $\omega_0=\mu_h^k$; no mass factor has been
assigned another value.

## 2. The exact relation sequence and its graded square

Let $\chi$ be monic of degree $q\ge1$ and $E=\mathbb C[S]/(\chi)$.
For $n\ge q-1$ the source map in AL.3 is

\[
m_{\chi,n}:\mathcal P_{n-q}\longrightarrow\mathcal P_n,\qquad
Q\longmapsto\chi Q.
\]

It is injective because $\mathbb C[S]$ is an integral domain. Every nonzero
image has degree $q+\deg Q\le n$. Conversely, if $P\in\mathcal P_n$ has
zero residue modulo $\chi$, then $P=\chi Q$ for a unique polynomial $Q$,
and the same degree identity gives $Q\in\mathcal P_{n-q}$.
The kernel of $\pi_\chi|_{\mathcal P_n}$ is therefore exactly its image.

Division by the monic polynomial gives a unique remainder of degree below
$q$ for every residue. Every such remainder belongs to $\mathcal P_n$ when
$n\ge q-1$, so the reduction map is surjective in that range. This proves
all three exactness assertions in AL.3.

For $n\ge q$, both degrees $n$ and $n-q$ are nonnegative. For $a\ge0$,

\[
0\longrightarrow\mathcal P_{a-1}\longrightarrow\mathcal P_a
\xrightarrow{\operatorname{lc}_a}\mathbb C\longrightarrow0
\]

is exact: its kernel is precisely the lower-degree space, and $zS^a$
has leading coefficient $z$. The left vertical multiplication in AL.4 is
well-defined because
$\deg(\chi Q)\le q+(n-q-1)=n-1$ for a nonzero input. The middle vertical
multiplication has the target already established. For every
$Q\in\mathcal P_{n-q}$, including lower-degree and zero inputs,

\[
\operatorname{lc}_n(\chi Q)=\operatorname{lc}_{n-q}(Q),
\]

because the coefficient of $S^q$ in $\chi$ is one. Thus the right square
commutes with the literal identity on $\mathbb C$. The left square commutes
because both paths take $Q$ to the same polynomial $\chi Q$.

The induced map is

\[
T=\overline m_\chi:\mathcal L_{n-q}\longrightarrow\mathcal L_n,
\qquad [Q]\longmapsto[\chi Q].
\]

Changing $Q$ by an element of $\mathcal P_{n-q-1}$ changes its product by
an element of $\mathcal P_{n-1}$, proving well-definedness. The
leading-coefficient identifications of both quotient lines with $\mathbb C$
identify $T$ with the identity. Its inverse is exactly

\[
z[S^n]\longmapsto z[S^{n-q}].
\]

This proves AL.4--6, including all maps at $n=q$, where the top row is
$0\to0\to\mathcal P_0\to\mathbb C\to0$.

## 3. The endpoint $n=q-1$

At this endpoint, $\mathcal P_{n-q}=\mathcal P_{-1}=0$.
Reduction $\mathcal P_{q-1}\to E$ is a bijection: surjectivity follows from
division, and a polynomial of degree below $q$ cannot be a nonzero multiple
of $\chi$. Thus AL.3 is still exact.

Its relation degree quotient is the zero vector space
$\mathcal P_{-1}/\mathcal P_{-2}=0/0=0$. This statement does not require
extending the previously defined symbol $\mathcal L_a$ to negative $a$.
The target degree quotient
$\mathcal L_{q-1}=\mathcal P_{q-1}/\mathcal P_{q-2}$ has basis
$[S^{q-1}]$ and dimension one. Multiplication from the zero relation source,
followed by this quotient, is therefore the unique map

\[
0\longrightarrow\mathcal L_{q-1}.
\]

The top row of AL.7 is the all-zero exact row. Its downward maps are the
unique zero maps into the bottom exact leading-coefficient row, so both
squares commute. The same proof includes $q=1$: the bottom row becomes
$0\to0\to\mathcal P_0\xrightarrow{\operatorname{lc}_0}\mathbb C\to0$.
Its leading line has squared norm $\mu_h^k$ on the coefficient-one vector.
This proves both the endpoint diagram and the sharp restriction $n\ge q$
for the isomorphism in AL.5.

## 4. Original norm, adjoint, and full multiplied representative

Continue with $n\ge q$. Write $e=[p_{n-q}]$ and $f=[p_n]$ for the actual
quotient-line bases. Both $\chi p_{n-q}$ and $p_n$ are monic of degree $n$.
Their difference

\[
r_n=\chi p_{n-q}-p_n
\]

belongs to $\mathcal P_{n-1}$, hence $Te=f$. The exact inner products are

\[
\langle ze,we\rangle_{\mathcal L_{n-q}}
=\overline z\,w\,\omega_{n-q},\qquad
\langle zf,wf\rangle_{\mathcal L_n}
=\overline z\,w\,\omega_n.
\]

Therefore, for any nonzero $z$,

\[
\frac{\|T(ze)\|^2}{\|ze\|^2}=\frac{\omega_n}{\omega_{n-q}},
\qquad
\|T\|^2=\frac{\omega_n}{\omega_{n-q}}.
\]

The defining adjoint identity for the conjugate-linear-first convention is
$\langle Tx,y\rangle_{\mathcal L_n}
=\langle x,T^*y\rangle_{\mathcal L_{n-q}}$.
For arbitrary $x=ze,y=wf$, its left side is $\overline z\,w\,\omega_n$.
The right side equals this for all $z,w$ exactly when

\[
T^*(wf)=w\frac{\omega_n}{\omega_{n-q}}e.
\]

This verifies the factor, orientation, and absence of a misplaced complex
conjugation in AL.8. It also gives

\[
T^*T=\frac{\omega_n}{\omega_{n-q}}I_{\mathcal L_{n-q}},
\quad
TT^*=\frac{\omega_n}{\omega_{n-q}}I_{\mathcal L_n},
\quad
\|T^{-1}\|^2=\frac{\omega_{n-q}}{\omega_n}.
\]

These are statements about the exact source quotient metrics on the lines.
Their relation to the original multiplied source polynomial is the following
orthogonal decomposition, with every map specified:

\[
T=\ell_n m_{\chi,n}s_{n-q},\qquad
A=m_{\chi,n}s_{n-q}:\mathcal L_{n-q}\longrightarrow\mathcal P_n.
\]

Since $\Pi_{n-1}p_n=0$ and $r_n\in\mathcal P_{n-1}$, put

\[
K=\Pi_{n-1}A,\qquad K(ze)=zr_n.
\]

Then

\[
A=s_nT+K,\qquad
(s_nT)(ze)=zp_n,\qquad
\operatorname{ran}(s_nT)\perp\operatorname{ran}K.
\]

In particular $r_n=\Pi_{n-1}(\chi p_{n-q})$. Pythagoras gives the literal
source norm

\[
\|\mathcal V_{h,k}(\chi p_{n-q})\|^2
=\omega_n+\|\mathcal V_{h,k}r_n\|^2,
\]

because AL.1 is precisely the given source norm. Equivalently,

\[
A^*A=T^*T+K^*K,\qquad
\|A\|^2=\frac{\omega_n+\|r_n\|_{h,k}^2}{\omega_{n-q}}.
\]

This explicitly carries the multiplied representative to its leading-line
minimum and retains the lower-degree correction. At the first admitted
degree $n=q$, it reads $p_{n-q}=p_0=1$,
$r_q=\chi-p_q$, and $\|T\|^2=\omega_q/\mu_h^k$.

Reducing the defining equality for $r_n$ modulo $\chi$ gives

\[
\pi_\chi(r_n)=-\pi_\chi(p_n),\qquad
\pi_\chi(\chi p_{n-q})=0.
\]

Thus the correction need not itself be an arithmetic relation; its residue
is exactly the displayed negative residue, so their sum is the original
relation. This verifies every sign and representative in AL.9--10.

## 5. Why the arithmetic image uses the retained representative

For $q\ge1,n\ge q$, the arithmetic reduction
$\pi_\chi:\mathcal P_n\to E$ does not descend through the degree quotient
$\ell_n:\mathcal P_n\to\mathcal L_n$. Indeed $1\in\mathcal P_{n-1}$ has
$\ell_n(1)=0$ and $\pi_\chi(1)\ne0$, so such a descended map would have
to send the zero degree class to a nonzero residue.

The complete morphism relating the two constructions is nevertheless
explicit. The original multiplication lift $A$ from Section 4 has zero
arithmetic image:

\[
\pi_\chi A=0.
\]

With its orthogonal decomposition $A=s_nT+K$, this becomes the exact
identity of maps $\mathcal L_{n-q}\to E$,

\[
\pi_\chi s_nT=-\pi_\chi K.
\]

On $e=[p_{n-q}]$ it is precisely
$\pi_\chi(p_n)=-\pi_\chi(r_n)$. Thus the degree-line isomorphism has a
specified relation lift whose correction cancels the residue of its monic
minimum. This proves the exact relationship, without claiming an arithmetic
map on degree classes that would be undefined.

## 6. Supported finite and full source maps

Let $\Lambda$ be the set of original admitted support labels. For a fixed
admitted degree $n\ge q-1$, define

\[
\widetilde{\mathcal P}_n
=\{\tau\}\sqcup\coprod_{\lambda\in\Lambda}
  \bigl(\{\lambda\}\times\mathcal P_n\bigr),
\qquad
\widetilde E
=\{\tau\}\sqcup\coprod_{\lambda\in\Lambda}
  \bigl(\{\lambda\}\times E\bigr).
\]

No extra label or scalar zero has been adjoined. The finite supported map is

\[
\widetilde\pi_{\chi,n}:\widetilde{\mathcal P}_n\longrightarrow\widetilde E,
\quad
\widetilde\pi_{\chi,n}(\tau)=\tau,\qquad
\widetilde\pi_{\chi,n}(\lambda,P)=(\lambda,\pi_\chi P).
\]

Its inverse image of the supported zero at a fixed label is exactly

\[
\widetilde\pi_{\chi,n}^{-1}\{(\lambda,0_E)\}
=\{(\lambda,\chi Q):Q\in\mathcal P_{n-q}\}.
\]

This follows from the kernel calculation in Section 2. At $n=q-1$ it is
the singleton $\{(\lambda,0)\}$, whereas the absent point has image
$\tau$, not $(\lambda,0_E)$.

On the full polynomial source, define the analogous map

\[
\widetilde\pi_\chi:
\{\tau\}\sqcup\coprod_{\lambda\in\Lambda}
(\{\lambda\}\times\mathbb C[S])\longrightarrow\widetilde E
\]

by the same formula. Its inverse image of $(\lambda,0_E)$ is
$\{(\lambda,\chi Q):Q\in\mathbb C[S]\}$. The inclusion
$\widetilde{\mathcal P}_n$ into the full source commutes with these
supported maps. Intersecting the full kernel with a finite-degree fibre
recovers exactly the kernel from AL.3, by the degree formula.
This verifies the finite/full type expansion incorporated in the final source.

Finally retain the actual programme identity

\[
J^{(k)}\mathcal V_{h,k}
=\eta_{h,k}\pi_\chi,\qquad
\eta_{h,k}[P]=\upsilon_h^{\otimes k}P(A_k)1,\qquad
\upsilon_h=j_h((2\xi)/h).
\]

Composing it with $m_{\chi,n}$ yields the zero linear map at the receiving
fibre, since $\pi_\chi m_{\chi,n}=0$. Its supported version sends each
labelled relation to the corresponding labelled zero and preserves the
external point $\tau$. Every Taylor-unit coefficient remains inside the
given map $\eta_{h,k}$. The preceding norm identity retains the exact source
norm of the relation before this composition. This checks the use of AL.11
and its support convention without replacing the supplied source map.

## 7. Empty arithmetic packet

For $\chi=1$ the degree is $q=0$ and $E=\mathbb C[S]/(1)=0$.
For every $n\ge0$, multiplication is the identity on $\mathcal P_n$,
and its induced map on $\mathcal L_n$ is the identity. Since the form in
AL.1 still has its actual positive mass, $\omega_n>0$ and

\[
\|I_{\mathcal L_n}\|^2=1=\frac{\omega_n}{\omega_n},\qquad
I_{\mathcal L_n}^*=I_{\mathcal L_n},\qquad
r_n=1\cdot p_n-p_n=0.
\]

The exact source norm decomposition becomes $\|p_n\|^2=\omega_n+0$,
and both reduction statements have value zero in $E$. The finite supported
map sends every polynomial at a fixed label to that label's supported zero,
while the external point remains $\tau$. Its finite source-fibre kernel is
all of $\mathcal P_n$, which is the image of multiplication by one.
No inverse on a positive-rank arithmetic quotient is used.

The $n=q-1$ discussion for positive $q$ is not applied to $q=0$:
the empty case is defined directly for every $n\ge0$, and no negative
degree leading-coefficient map is required. This verifies the full
empty-packet paragraph, including degree zero and the mass $\mu_h^k$.

## 8. Review conclusion

The fragment supplies the correct endpoint domain and the exact metric
transport that the raw paragraph after arithmetic equation (13) needed.
Its new finite-dimensional proof is complete, including the incorporated
supported-map domains and their exact kernel intersection. No change to the arithmetic endpoint
constant, the measure, the coordinate $S=k/2+iu$, or the source generator
follows from this review.

No statement here certifies test execution, a TeX render, or a Lean proof.
Those operations were outside this review assignment and were not run.
