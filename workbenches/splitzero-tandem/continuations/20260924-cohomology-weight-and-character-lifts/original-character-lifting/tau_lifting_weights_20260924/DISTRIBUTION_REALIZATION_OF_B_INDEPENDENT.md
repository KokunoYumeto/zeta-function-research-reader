# Exact distribution realization of the two-nilpotent object and its rational orbit

Independent mathematical derivation, 24 September 2026.

This calculation realizes the entire existing auxiliary object \(B_\rho\) inside the existing supported-distribution receiver. It computes both original Dolbeault residues, constructs the exact quotient comparison, and proves uniqueness of the equivariant lift on the entire finite rational-translation orbit, including algebraic sums over all original zero blocks. It does not identify that orbit with the complete adelic quotient.

## DR0. Source, definitions, and operation domains

Human source: Alain Connes and Caterina Consani, [*The Riemann–Roch strategy: Complex lift of the Scaling Site*, arXiv:1805.10501v1](https://arxiv.org/abs/1805.10501v1). The original author source read for this calculation is

`thecurve_K.tex`, original author source retained under `sources/`.

Section 5.2, Lemma adelicomp1 and equation actionpq, lines 1203–1224, gives the affine action and original operator. Section 6.6, the paragraph before Proposition comparescalcs, lines 2381–2418, gives the two original vector fields and their full \(Y\) factor. Section 7.1, equations holom, holombis, holom1 and Proposition frobarith, lines 2564–2601, concerns the separate arithmetic Frobenius combining a right action and coefficient change. That last arithmetic Frobenius is not identified with the raw left affine pullback calculated here.

The existing programme sources are:

- [Supported Dolbeault receiver](../independent/CC_SUPPORTED_DOLBEAULT_BOUNDARY.tex), equations SDB1–SDB31 and their proofs.
- [Existing two-nilpotent comparison](../deligne_quotient_weight_20260924/MONODROMY_JET_COMPARISON.md), MJ4.1–MJ5.4.
- [Existing equivariant lifting calculation](TAU_LIFTING_AND_WEIGHT_SEPARATION.md), TL2.1–TL3.3, in particular the quotient \(q_\rho(x_\rho)=t_\rho,\ q_\rho(y_\rho)=0_{A_\rho}\).
- User definitions U01–U18 (private construction record; not included) and operation domains (private construction record; not included), read before defining the present maps.

The present operations are in the complex arithmetic receivers already specified in those sources. In particular, \(Z_1/\tau\) remains presence without source parity or source addition. No polynomial, derivative, scalar subtraction, branch coordinate, or residue below has primitive \(\tau\) as an operand. The origin \(X=0\) here is an archimedean coordinate in Connes–Consani's explicitly stated receiver, not an identification of that coordinate with the source \(Z_1\). All statements involving an actual zero \(\rho\) use the original \(\zeta(\rho)=0\), not a replacement zeta function.

Use capital \(X,Y\) for the original archimedean coordinates, to distinguish them from the algebra variables \(x,y\) of \(B_\rho\). Write
\[
 \Omega=\mathbb R\times(0,\infty),\qquad
 D=\partial_X+i\partial_Y,\qquad D_Y=YD.
\tag{DR0.1}
\]
There is no factor \(1/2\) in \(D\). All distributions are complex scalar distributions on this open set. In particular there is no extension across \(Y=0\), and no discarded endpoint distribution.

Fix \(\rho\in\mathbb C\), an integer \(m\ge1\), and put
\[
 \alpha=\rho+1,\qquad
 A_\rho=\mathbb C[t]/t^m,\qquad
 B_\rho=\mathbb C[x,y]/(x,y)^m.
\tag{DR0.2}
\]
The existing operators and maps are
\[
 J=M_x,\quad N=M_y,\quad
 F_a=a^\rho e^{(\log a)J}D_a,\quad
 D_a(x)=x,\ D_a(y)=a^{-1}y,\quad a>0,
\tag{DR0.3}
\]
\[
 q_\rho(x)=t,\quad q_\rho(y)=0_{A_\rho},\qquad
 i_\rho(t)=x,\qquad
 K_\rho=\ker q_\rho=yB_\rho.
\tag{DR0.4}
\]
All exponentials in these finite algebras terminate. These formulas are restated from the existing receiver, not definitions of arithmetic from primitive \(\tau\).

## DR1. The distribution embedding and both nilpotents

For \(r\ge0\), define the smooth function on \(Y>0\)
\[
 g_r(Y)=Y^\alpha\frac{(\log Y)^r}{r!},
 \qquad Y^\alpha=\exp(\alpha\log Y),
 \qquad g_{-1}=0.
\tag{DR1.1}
\]
For each rational number \(c\), define
\[
 \boxed{\Phi_c(x^u y^j)
   =\delta^{(j)}(X-c)\otimes g_{m-j-1-u}(Y),
       \qquad u,j\ge0,\quad u+j<m.}
\tag{DR1.2}
\]
The tensor distribution has the full pairing
\[
 \langle\delta^{(j)}(X-c)\otimes g,\varphi\rangle
   =(-1)^j\int_0^\infty
       g(Y)\partial_X^j\varphi(c,Y)\,dY.
\tag{DR1.3}
\]
The test function is compactly supported in \(\Omega\), so the integral is finite for every \(\rho\), including near the excluded endpoint. No asymptotic integrability at \(Y=0\) or \(Y=\infty\) has been assumed.

Formula (DR1.2), extended linearly from the monomial basis of \(B_\rho\), is injective. Different \(j\) are independent normal derivatives: a test function supported near \(c\), of the form \((X-c)^j\chi(X)\psi(Y)/j!\), isolates the \(j\)-coefficient as in SDB3–SDB6. At fixed \(j\), the functions \(g_0,\ldots,g_{m-j-1}\) are linearly independent. Indeed division by the nonzero function \(Y^\alpha\), followed by \(s=\log Y\), gives a polynomial identity on all real \(s\), which forces every coefficient to vanish.

On distributions define the explicitly named operators
\[
 \mathscr J=Y\partial_Y-\alpha,\qquad
 \mathscr N=\partial_X\mathscr J.
\tag{DR1.4}
\]
The scalar \(-\alpha\) is part of the operator; it is not removed from the formulas. Differentiation gives
\[
 \mathscr Jg_r=g_{r-1},\qquad
 \mathscr N(\delta^{(j)}_c\otimes g_r)
          =\delta^{(j+1)}_c\otimes g_{r-1},
\tag{DR1.5}
\]
where \(\delta_c^{(j)}=\delta^{(j)}(X-c)\). Therefore
\[
 \mathscr J\Phi_c=\Phi_c J,\qquad
 \mathscr N\Phi_c=\Phi_c N.
\tag{DR1.6}
\]
For \(u+j=m-1\), the right sides vanish because the degree-\(m\) monomials vanish, and the left sides vanish because \(g_{-1}=0\). Thus these identities also prove the boundary cases, including \(m=1\). No order term has been lost. The operators \(\mathscr J,\mathscr N\) commute on this image because \(\partial_X\) commutes with \(Y\partial_Y-\alpha\).

This is an embedding of the specified vector space with its named operators. It is not an algebra homomorphism into an algebra of distributions: arbitrary products of the displayed Dirac derivatives are not being defined.

## DR2. Full rational affine action and all Jacobians

For \(a>0\) and \(b\in\mathbb R\), let
\[
 \ell(a,b)(X,Y)=(aX+b,aY).
\]
Scalar-distribution pullback, in the exact source convention, is
\[
 \langle P(a,b)u,\varphi\rangle
   =a^{-2}
      \left\langle u,
        \varphi\!\left(\frac{X-b}{a},\frac Ya\right)
      \right\rangle.
\tag{DR2.1}
\]
The factor \(a^{-2}\) is the inverse determinant of the two-dimensional map; it has not been absorbed into the distributions. For one variable put \(Q_ag(Y)=g(aY)\), with distributional definition
\[
 \langle Q_ag,\psi\rangle
   =a^{-1}\langle g,\psi(\cdot/a)\rangle.
\tag{DR2.2}
\]
Direct substitution into (DR1.3) gives
\[
 P(a,b)(\delta_c^{(j)}\otimes g)
   =a^{-j-1}\delta_{(c-b)/a}^{(j)}\otimes Q_ag.
\tag{DR2.3}
\]
All signs in the derivative of the delta distribution are those of (DR1.3); since \(a>0\), no sign from an absolute determinant is omitted.

The full coefficient calculation is
\[
 Q_ag_r
  =a^\alpha
       \sum_{k=0}^{r}\frac{(\log a)^k}{k!}g_{r-k},
\tag{DR2.4}
\]
because
\[
 \frac{(\log(aY))^r}{r!}
   =\sum_{k=0}^r
      \frac{(\log a)^k(\log Y)^{r-k}}{k!(r-k)!}.
\]
Combining (DR2.3) and (DR2.4), with \(r=m-j-1-u\), proves
\[
 \boxed{
 P(a,b)\Phi_c(x^u y^j)
  =a^{\rho-j}
    \sum_{k=0}^{m-j-1-u}
      \frac{(\log a)^k}{k!}
        \Phi_{(c-b)/a}(x^{u+k}y^j).
 }
\tag{DR2.5}
\]
For \(b=0,c=0\), this is exactly
\[
 P(a,0)\Phi_0=\Phi_0 F_a,
\tag{DR2.6}
\]
with the complete original \(F_a\), not its scalar part.

For \(a\in\mathbb Q_{>0}\) and \(b\in\mathbb Q\), the support \((c-b)/a\) stays rational. Define algebraic direct sums
\[
 B_{\rho,\mathbb Q}=\bigoplus_{c\in\mathbb Q}B_{\rho,c},
 \qquad A_{\rho,\mathbb Q}=\bigoplus_{c\in\mathbb Q}A_{\rho,c}.
\tag{DR2.7}
\]
Every vector has finite branch support. Define \(\mathcal P(a,b)\) on the first space by the right side of (DR2.5), with \(\Phi\) replaced by the branch basis notation. Define its action on \(A_{\rho,\mathbb Q}\) by
\[
 t_c^u\longmapsto
 a^\rho\sum_{k=0}^{m-1-u}
       \frac{(\log a)^k}{k!}t_{(c-b)/a}^{u+k}.
\tag{DR2.8}
\]
These are invertible finite sums.

Pullback is contravariant. For the source affine multiplication
\[
 (a,b)(a',b')=(aa',ab'+b),
\]
the exact composition law is
\[
 P(a,b)P(a',b')
    =P(a'a,a'b+b').
\tag{DR2.9}
\]
For instance the support changes first to \((c-b')/a'\) and then to
\((c-b'-a'b)/(a'a)\), which is the support on the right. The polynomial coefficients multiply by \(F_aF_{a'}=F_{aa'}\), giving the same law for \(\mathcal P\). Thus these are right actions of \(P^+(\mathbb Q)\), or equivalently left actions after replacing \((a,b)\) by its inverse \((a^{-1},-b/a)\). No switch of convention is hidden.

The sum
\[
 \Phi_{\mathbb Q}((b_c)_c)=\sum_c\Phi_c(b_c)
\tag{DR2.10}
\]
is an injective distribution map and intertwines these right actions. To prove injectivity, a finite support set can be separated by disjoint \(X\)-neighborhoods, so each branch is isolated by a test function; then DR1 gives injectivity within that branch. This proof uses finite branch support. It does not assert that every infinite sum on the dense set \(\mathbb Q\) defines a distribution.

The quotient and section extend componentwise:
\[
 q_{\rho,\mathbb Q}=\bigoplus_cq_{\rho,c},
 \qquad i_{\rho,\mathbb Q}=\bigoplus_ci_{\rho,c},
 \qquad K_{\rho,\mathbb Q}=\bigoplus_c yB_{\rho,c}.
\tag{DR2.11}
\]
Equations (DR2.5) and (DR2.8) prove that both maps commute with the full rational affine action: the terms with \(j>0\) remain in the kernel, and the terms with \(j=0\) have identical coefficients in both formulas. Hence
\[
 0\longrightarrow K_{\rho,\mathbb Q}
 \longrightarrow B_{\rho,\mathbb Q}
 \xrightarrow{q_{\rho,\mathbb Q}}A_{\rho,\mathbb Q}
 \longrightarrow0
\tag{DR2.12}
\]
is an equivariantly split exact sequence over the complete specified rational orbit.

## DR3. The original distribution complex on the entire rational orbit

Extend the existing SDB space to the explicitly defined algebraic direct sum
\[
 \mathcal J_{\mathbb Q}
   =\bigoplus_{c\in\mathbb Q}\bigoplus_{j\ge0}
       \delta_c^{(j)}\otimes\mathcal D'((0,\infty)).
\tag{DR3.1}
\]
Every element has finitely many branches and finitely many normal derivatives in each branch. The distribution embedding is injective by the same test-function argument as in DR2. The original \(D\) and \(D_Y\) act branchwise. Define the full, branch-retaining residues
\[
 \begin{aligned}
 (R_{\mathbb Q}u)_c
   &=\sum_j(-i)^j\partial_Y^jg_{c,j},\\
 (R_{Y,\mathbb Q}u)_c
   &=\sum_j(-i)^j\partial_Y^j(Y^{-1}g_{c,j}),
 \end{aligned}
\tag{DR3.2}
\]
for \(u=\sum_{c,j}\delta_c^{(j)}\otimes g_{c,j}\), with targets
\(\bigoplus_c\mathcal D'((0,\infty))\). These formulas retain the branch label \(c\). Taking a sum of the outputs over \(c\) would be another map and would forget branches.

SDB8–SDB31 apply to each branch by replacing \(X\) with \(X-c\). To make the exactness explicit, put
\[
 E_{\mathbb Q}(h)=\sum_c\delta_c\otimes h_c,\qquad
 E_{Y,\mathbb Q}(h)=\sum_c\delta_c\otimes Yh_c,
\]
\[
 T_{\mathbb Q}u
  =\sum_c\sum_{j\ge1}\sum_{k=0}^{j-1}
      (-i)^k\delta_c^{(j-1-k)}\otimes
            \partial_Y^kg_{c,j},\qquad
 T_{Y,\mathbb Q}=T_{\mathbb Q}M_{Y^{-1}}.
\tag{DR3.3}
\]
All sums are finite. Applying \(D\) to a term yields
\[
 D(\delta_c^{(j)}\otimes g)
      =\delta_c^{(j+1)}\otimes g
        +i\delta_c^{(j)}\otimes g',
\tag{DR3.4}
\]
so \(R_{\mathbb Q}D=0\). In \(DT_{\mathbb Q}\), consecutive terms cancel by \((-i)^k+i(-i)^{k-1}=0\), leaving
\[
 DT_{\mathbb Q}=I-E_{\mathbb Q}R_{\mathbb Q}.
\tag{DR3.5}
\]
The highest normal derivative in \(Du\) has the same nonzero coefficient as the highest derivative in \(u\), raised by one, so \(D\) is injective. Applying (DR3.5) to \(Du\) then proves \(T_{\mathbb Q}D=I\). Also \(R_{\mathbb Q}E_{\mathbb Q}=I\). It follows that
\[
 0\longrightarrow\mathcal J_{\mathbb Q}
 \xrightarrow{D}\mathcal J_{\mathbb Q}
 \xrightarrow{R_{\mathbb Q}}
       \bigoplus_{c\in\mathbb Q}\mathcal D'((0,\infty))
 \longrightarrow0
\tag{DR3.6}
\]
is exact, with the stated splitting. Multiplication by \(Y\) is invertible on this open domain. Retaining that multiplication in the order \(D_Y=M_YD\) proves the corresponding exact sequence with \(D_Y,R_{Y,\mathbb Q},E_{Y,\mathbb Q},T_{Y,\mathbb Q}\). This is precisely the branchwise version of SDB27–SDB31.

The complete affine covariance is
\[
 DP(a,b)=aP(a,b)D,\qquad
 D_YP(a,b)=P(a,b)D_Y.
\tag{DR3.7}
\]
On residues, the \(c\)-component moves to \(c'=(c-b)/a\), and
\[
 \begin{aligned}
 (R_{\mathbb Q}P(a,b)u)_{c'}
     &=a^{-1}Q_a(R_{\mathbb Q}u)_c,\\
 (R_{Y,\mathbb Q}P(a,b)u)_{c'}
     &=Q_a(R_{Y,\mathbb Q}u)_c.
 \end{aligned}
\tag{DR3.8}
\]
For the first formula, each \(j\)-term contributes
\(a^{-j-1}(-i)^j\partial_Y^jQ_ag
 =a^{-1}Q_a((-i)^jg^{(j)})\).
For the second, apply the first formula to \(Y^{-1}P(a,b)u
=aP(a,b)(Y^{-1}u)\). These derivations retain both Jacobians and every derivative.

The original cochain actions must also be retained:
\[
 \rho^0(a,b)=P(a,b),\quad
 \rho^1(a,b)=aP(a,b)\quad\text{for }D;
\tag{DR3.9}
\]
both degrees carry \(P(a,b)\) for \(D_Y\). Accordingly \(R_{\mathbb Q}\) intertwines \(\rho^1\) with \(Q_a\), whereas its raw-pullback quotient intertwines \(P(a,b)\) with \(a^{-1}Q_a\). There is no replacement of one action by the other. Formula (DR2.6) realizes \(F_a\) by **raw** \(P(a,0)\). In degree \(1\) of the original \(D\)-complex it consequently realizes the operator \(aF_a\). In the \(D_Y\)-complex it realizes \(F_a\) in both degrees.

## DR4. Every residue coefficient, and exact injectivity

For integers \(j\ge0\), define the full polynomial
\[
 P_j(z)=\prod_{k=0}^{j-1}(z-k),\qquad P_0(z)=1.
\]
Write
\[
 P_j(\alpha+z)
    =\sum_{h=0}^j C_{j,h}(\alpha)z^h,
\quad
 C_{j,h}(\alpha)
    =\sum_{\substack{S\subseteq\{0,\ldots,j-1\}\\|S|=h}}
         \prod_{k\notin S}(\alpha-k).
\tag{DR4.1}
\]
The empty product is \(1\); in particular \(C_{0,0}=1\). For \(s=\log Y\),
\[
 \partial_Y^j(Y^\alpha f(s))
  =Y^{\alpha-j}P_j(\alpha+\partial_s)f(s).
\tag{DR4.2}
\]
This follows by induction: one derivative changes the exponent from
\(\alpha-j\) to \(\alpha-j-1\) and applies
\(\alpha-j+\partial_s\) to the polynomial. Thus for the exact
\(r=m-j-1-u\),
\[
 \boxed{
 R\Phi_c(x^uy^j)
  =(-i)^jY^{\rho+1-j}
       \sum_{h=0}^{\min(j,r)}
        C_{j,h}(\rho+1)
            \frac{(\log Y)^{r-h}}{(r-h)!}.
 }
\tag{DR4.3}
\]
The notation \(R\) on the left means the \(c\)-component of
\(R_{\mathbb Q}\); the branch label is retained.
Similarly,
\[
 \boxed{
 R_Y\Phi_c(x^uy^j)
  =(-i)^jY^{\rho-j}
       \sum_{h=0}^{\min(j,r)}
        C_{j,h}(\rho)
            \frac{(\log Y)^{r-h}}{(r-h)!}.
 }
\tag{DR4.4}
\]
This is obtained by multiplying the coefficient in (DR1.2) by \(Y^{-1}\) **before** differentiating. It is not obtained by dropping a \(Y\) factor after the derivative.

Here is the full injectivity argument. At fixed \(j\), the polynomial operator
\(P_j(\alpha+\partial_s)\) on polynomials of degree at most \(m-j-1\) is triangular with diagonal coefficient \(P_j(\alpha)\). It is invertible precisely when \(P_j(\alpha)\ne0\). An exact inverse when this coefficient is nonzero is the finite operator
\[
 \sum_{n=0}^{m-j-1}
    \frac{(-1)^n}{P_j(\alpha)^{n+1}}
       \bigl(P_j(\alpha+\partial_s)-P_j(\alpha)I\bigr)^n.
\tag{DR4.5}
\]
The parenthesized operator decreases polynomial degree, so its
\((m-j)\)-th power is zero. Multiplication by \(P_j(\alpha+\partial_s)\)
telescopes to the identity, proving the inverse.

Different \(j\) give distinct exponents \(\alpha-j\). The spaces
\[
 e^{(\alpha-j)s}\,\mathbb C[s]_{\le m-j-1}
\tag{DR4.6}
\]
are linearly independent. To verify this for a finite sum, choose one index \(j\) and apply
\[
 \prod_{h\ne j}
       (\partial_s-(\alpha-h))^{m-h}.
\]
This kills every summand of index \(h\ne j\). On the \(j\)-summand it is a polynomial in \(\partial_s\) with nonzero constant term after factoring out \(e^{(\alpha-j)s}\), hence invertible on the finite polynomial space by the same finite inverse argument. The chosen summand must therefore be zero.

It follows that \(R\Phi_c\) is injective whenever
\[
 \rho+1\notin\{0,1,\ldots,m-2\}.
\tag{DR4.7}
\]
The displayed set is empty when \(m=1\). This is also a complete classification of the exceptional kernel. If \(\alpha=n\) is in that set, then for \(j>n\) exactly one factor of \(P_j(\alpha+\partial_s)\) is \(\partial_s\); all other factors are invertible on the polynomial space. Its kernel is precisely the constants. For \(j\le n\) it is invertible. Therefore
\[
 \ker(R\Phi_c)
  =\operatorname{span}
        \{x^{m-j-1}y^j:n+1\le j\le m-1\}
       \quad(\rho+1=n\in\{0,\ldots,m-2\}).
\tag{DR4.8}
\]
Outside those exceptional values the kernel is zero. The same proof
for (DR4.4) gives \(R_Y\Phi_c\) injective whenever
\[
 \rho\notin\{0,\ldots,m-2\},
\tag{DR4.9}
\]
and the corresponding kernel (DR4.8) with \(n=\rho\).

Every actual nontrivial zero of the original zeta function has
\(0<\Re\rho<1\). Both conditions (DR4.7) and (DR4.9) therefore hold,
including for zeros off the critical line. Hence both maps
\[
 B_{\rho,\mathbb Q}\xrightarrow{\Phi_{\mathbb Q}}
 \mathcal J_{\mathbb Q}
 \xrightarrow{R_{\mathbb Q}}
       \bigoplus_c\mathcal D'((0,\infty)),
\]
\[
 B_{\rho,\mathbb Q}\xrightarrow{\Phi_{\mathbb Q}}
 \mathcal J_{\mathbb Q}
 \xrightarrow{R_{Y,\mathbb Q}}
       \bigoplus_c\mathcal D'((0,\infty))
\tag{DR4.10}
\]
are injective for actual zero blocks. By (DR3.6), no nonzero vector
of this embedded \(B_{\rho,\mathbb Q}\) is a \(D\)-boundary;
the analogous assertion holds for \(D_Y\).

## DR5. The exact relation with the auxiliary quotient

The result (DR4.10) implies
\[
 \ker(R\Phi_c)=0,\qquad
 \ker q_\rho=yB_\rho
\tag{DR5.1}
\]
for actual zeros. At \(m>1\), these kernels differ. This does not end
the comparison: the exact factorization of \(q_\rho\) through the
residue image is as follows.

Let
\[
 \mathscr V_{\rho,c}=R\Phi_c(B_\rho)
    =\bigoplus_{j=0}^{m-1}
       Y^{\alpha-j}\mathbb C[\log Y]_{\le m-j-1}.
\tag{DR5.2}
\]
Equality, including surjectivity on every summand, follows from
(DR4.3) and (DR4.5). Put \(E=Y\partial_Y\) on smooth functions,
retaining the exact exponents \(\alpha-j\). For \(m>1\), define
\[
 G(z)=\prod_{j=1}^{m-1}(z-(\alpha-j))^{m-j},
\]
\[
 H(z)=\sum_{r=0}^{m-1}
      \frac1{r!}\left.
          \frac{d^r}{dw^r}\frac1{G(w)}
      \right|_{w=\alpha}
      (z-\alpha)^r,\qquad
 \Pi_0=G(E)H(E).
\tag{DR5.3}
\]
All these coefficients are defined: \(G(\alpha)=
\prod_{j=1}^{m-1}j^{m-j}\ne0\).
For \(m=1\), put \(G=H=1\), so \(\Pi_0=I\).
On the \(j=0\) summand, \((E-\alpha)^m=0\);
Taylor's formula for \(1/G\) shows that \(G(E)H(E)=I\).
On each \(j>0\) summand, \(G(E)=0\) by its explicit factor of order
\(m-j\). Thus \(\Pi_0\) is precisely the projection onto \(j=0\),
with kernel all \(j>0\) summands.

Define the isomorphism onto that zeroth summand by
\[
 \mathscr I_{\rho,c}:A_{\rho,c}\longrightarrow
    Y^\alpha\mathbb C[\log Y]_{\le m-1},\qquad
 \mathscr I_{\rho,c}(t^u)
      =Y^\alpha\frac{(\log Y)^{m-1-u}}{(m-1-u)!}.
\tag{DR5.4}
\]
It is \(R\Phi_c i_\rho\), and its inverse reads off the displayed
polynomial coefficients in reverse order, retaining each factorial.
Now put
\[
 \mathscr Q_{\rho,c}
       =\mathscr I_{\rho,c}^{-1}\Pi_0:
       \mathscr V_{\rho,c}\longrightarrow A_{\rho,c}.
\]
The complete comparison is
\[
 \boxed{
 q_\rho=\mathscr Q_{\rho,c}R\Phi_c,\qquad
 \mathscr Q_{\rho,c}\mathscr I_{\rho,c}=I.
 }
\tag{DR5.5}
\]
It follows on each basis monomial: at \(j=0\) it returns \(t^u\);
at \(j>0\) it returns zero. The maps and their kernels are therefore
proved on the whole object.

The same construction for \(R_Y\) replaces \(\alpha=\rho+1\) in
(DR5.2)–(DR5.4) by \(\rho\), giving
\[
 q_\rho=\mathscr Q_{Y,\rho,c}R_Y\Phi_c.
\tag{DR5.6}
\]
Its codomain exponent remains \(\rho\); this change is forced by
the already retained \(Y^{-1}\) in (DR4.4).

All these maps extend to the rational branch direct sums and are
equivariant. Indeed \(E\) commutes with \(Q_a\), and translations
only permute the branch labels. Therefore \(\Pi_0\) commutes with
the target action \(a^{-1}Q_a\) for raw \(R\), and with \(Q_a\)
for \(R_Y\). The maps \(\mathscr I\) intertwine those exact actions
with (DR2.8), as follows either by substituting their full
logarithm expansions or by (DR2.6), (DR3.8).

The \(j>0\) pieces are thus genuine, independent residue classes.
They disappear under the explicit spectral projection \(\Pi_0\),
not under the SDB residue or differential. The auxiliary quotient
has now been constructed as an exact map on the actual residue
image; it has not been identified with a boundary operation.

## DR6. Uniqueness of the lift on the whole rational orbit

We prove
\[
 \operatorname{Hom}_{P^+(\mathbb Q)}
       (A_{\rho,\mathbb Q},K_{\rho,\mathbb Q})=0.
\tag{DR6.1}
\]
The Hom means complex-linear maps commuting with the right actions
in DR2; it does not impose an unmentioned topology.

Let \(f\) be such a map, and restrict it to the finite-dimensional
branch \(A_{\rho,0}\). The image of a finite basis has a finite
union \(S\subset\mathbb Q\) of branch supports. Every vector of
\(f(A_{\rho,0})\) has support in \(S\). Conversely choose \(S\) as
the union of all nonzero component positions of the image, which
is still finite. Since \(A_{\rho,0}\) is preserved by every positive
rational dilation and that action is invertible, equivariance makes
the image invariant under those dilations. Formula (DR2.5) sends
branch \(c\) to \(c/a\) by an invertible coefficient operator,
so \(S/a=S\) for all \(a\in\mathbb Q_{>0}\).
If \(S\) contained a nonzero \(c\), it would contain all
\(c/2^n\), \(n\ge0\), which are distinct. Finiteness excludes this.
Thus \(S\subseteq\{0\}\).

It remains to calculate the coefficient map
\(f:A_{\rho,0}\to K_{\rho,0}\). For any prime \(p\), its source
action has only eigenvalue \(p^\rho\); its target action has
eigenvalues
\[
 p^{\rho-j},\qquad 1\le j\le m-1,
\tag{DR6.2}
\]
with full Jordan lengths \(m-j\). None equals \(p^\rho\),
because the positive real number \(p^{-j}\) is not \(1\).
An intertwiner between two finite-dimensional operators with
disjoint spectra is zero: their minimal polynomials are coprime;
a Bézout identity, evaluated on the two operators and moved across
the intertwiner, annihilates it. This argument does not assume
semisimplicity. Therefore \(f|_{A_{\rho,0}}=0\).
Finally \(P(1,-c)\) maps \(A_{\rho,0}\) isomorphically to
\(A_{\rho,c}\). Translation equivariance proves \(f=0\) on
every branch and hence on the direct sum. This proves (DR6.1).

Any two equivariant sections of \(q_{\rho,\mathbb Q}\) differ by
a map into its kernel. Equation (DR6.1), together with the existing
section (DR2.11), proves that
\[
 \boxed{i_{\rho,\mathbb Q}
       \text{ is the unique }P^+(\mathbb Q)\text{-equivariant
       section of }q_{\rho,\mathbb Q}.}
\tag{DR6.3}
\]
The conclusion includes \(m=1\), where the kernel is zero.

There is also an exact simultaneous result allowing mixing of
different original zeros. Let \(\mathscr Z\) be any set of complex
numbers with \(0<\Re\rho<1\), each with specified finite
positive integer \(m_\rho\); it may in particular be the distinct
nontrivial zeros of the original \(\zeta\), with their actual
multiplicities. Form algebraic direct sums
\[
 \mathscr A=\bigoplus_{\rho\in\mathscr Z}
       A_{\rho,\mathbb Q},\quad
 \mathscr B=\bigoplus_{\rho\in\mathscr Z}
       B_{\rho,\mathbb Q},\quad
 \mathscr K=\bigoplus_{\rho\in\mathscr Z}
       K_{\rho,\mathbb Q}.
\tag{DR6.4}
\]
Every vector has finite \(\rho\)-support and finite branch support.
Actions preserve each \(\rho\)-summand. Any equivariant map
\(f:\mathscr A\to\mathscr K\), even if it is not required to
preserve \(\rho\), is zero.

The distribution and residue maps also retain this complete
algebraic sum. For \(\Phi\), normal derivative order and branch
are first isolated by test functions. At each remaining index,
finitely many distinct \(\rho\) give independent functions
\(Y^{\rho+1}\) times polynomials in \(\log Y\), by the
differential-operator proof in DR4. For the residue images,
equality of two exponents would imply
\(\rho-j=\rho'-j'\). Taking real parts and using
\(0<\Re\rho,\Re\rho'<1\) forces the integer \(j-j'\) to be
zero, hence \(j=j'\) and \(\rho=\rho'\). Thus the residue
exponents are distinct across different \((\rho,j)\).
The same finite exponential-polynomial argument proves that
both residue maps are injective on \(\mathscr B\).
This proves actual distribution realization of the whole
specified algebraic sum, not only of each block separately.

To prove the asserted vanishing of equivariant maps, restrict to a fixed finite-dimensional
\(A_{\rho,0}\). The preceding support argument forces its image
to branch \(0\). It has components in only finitely many target
\(\rho'\)-summands because a finite basis has finite images.
Project to any one of these summands; projection commutes with
dilation. For every prime \(p\), the source eigenvalue has modulus
\[
 |p^\rho|=p^{\Re\rho}>1,
\]
whereas every target kernel eigenvalue satisfies
\[
 |p^{\rho'-j}|=p^{\Re\rho'-j}<1,\qquad j\ge1.
\tag{DR6.5}
\]
The same coprime-polynomial argument kills every component.
Translations then kill the image of every branch. Since the
domain is the algebraic direct sum, this proves
\[
 \boxed{\operatorname{Hom}_{P^+(\mathbb Q)}
               (\mathscr A,\mathscr K)=0.}
\tag{DR6.6}
\]
Consequently the direct sum of \(i_{\rho,\mathbb Q}\) is the unique
equivariant section of the direct sum quotient. This separation
uses the known open critical strip, not RH, and retains every
nilpotent block. There is no interchange of an infinite sum and
an analytic limit in the proof. No corresponding result for an
unspecified completion or product is inferred.

## DR7. Exact limits of the complex comparison

The inclusion \(\Phi_c\) realizes the two auxiliary nilpotents as
actual operators on distributions, but those named operators
are not the original Dolbeault differential. Their commutators
on the full distribution space are
\[
 [D,\mathscr J]=i\partial_Y,\qquad
 [D,\mathscr N]=i\partial_X\partial_Y.
\tag{DR7.1}
\]
The first identity follows from
\([\partial_Y,Y\partial_Y]=\partial_Y\); the second follows
because \(\partial_X\) commutes with \(D,\mathscr J\).
Thus neither is asserted to be a cochain endomorphism of
the entire \(D\)-complex using the same action in both degrees.

In particular \(\mathscr J\) need not preserve its boundaries.
From \(D\mathscr J-\mathscr JD=i\partial_Y\) and \(RD=0\),
\[
 R\mathscr JD=-i\partial_YR.
\tag{DR7.2}
\]
For example \(u=\delta_c\otimes Y\) has \(Ru=Y\), so
\(R\mathscr JDu=-i\ne0\). Likewise
\[
 R\mathscr ND=-iR\partial_X\partial_Y
             =-\partial_Y^2R,
\tag{DR7.2a}
\]
where \(R\partial_X=-i\partial_YR\) follows directly from
the residue formula. Taking \(u=\delta_c\otimes Y^2\) gives
\(R\mathscr NDu=-2\ne0\). These are smooth coefficients
defining distributions on the open domain, so no compact
support of the coefficients themselves is required. This is an
explicit domain calculation, not an assertion that the
constructions are unrelated.
On the injective finite cohomology image (DR4.10), the
\(\mathscr J,\mathscr N\) actions do transport through \(R\Phi_c\)
and \(R_Y\Phi_c\), because these maps are isomorphisms onto
their stated images. Equations DR1, DR4 and DR5 give those exact
comparison maps. They do not extend that transported action to
all cohomology without a separately defined operation.

Likewise \(\Phi_c(B_\rho)\) itself is generally not a subcomplex
for \(D\). Its complete derivative is
\[
 D\Phi_c(x^uy^j)
   =\delta_c^{(j+1)}\otimes
       Y^\alpha\frac{(\log Y)^r}{r!}
    +i\delta_c^{(j)}\otimes
       Y^{\alpha-1}
        \left(
          \alpha\frac{(\log Y)^r}{r!}
          +\frac{(\log Y)^{r-1}}{(r-1)!}
        \right),
\tag{DR7.3}
\]
where the final term is zero when \(r=0\). All terms remain
inside \(\mathcal J_{\mathbb Q}\). In the top \(y\)-degree,
the first term already has normal derivative order \(m\),
outside the image of \(B_\rho\), and is nonzero.
The \(D_Y\) formula is \(Y\) times the whole right side,
retaining that factor on both terms.

Finally, the rational orbit extension removes the earlier
restriction to the single branch \(X=0\) for the **positive
rational affine action**. It does not include finite adele
variables, the negative-\(a\) component, endpoint strata,
infinite branch completions, or the separate right-action
arithmetic Frobenius of the human source. Those are explicit
scope boundaries of this constructed receiver, not statements
that those objects cannot be related. The exact achieved
connection is (DR2.10), the exact residue comparison is
(DR5.5)–(DR5.6), and the global-within-this-receiver lifting
result is (DR6.3)–(DR6.6).

## DR8. Retained support indices

For any specified family of existing support indices \(\lambda\),
each amplitude map above has the index-preserving lift
\[
 (v,\lambda)\longmapsto(f(v),\lambda).
\tag{DR8.1}
\]
If the source is the historical lattice carrier
\(G_L(V)=\{(0,\lambda):\lambda\in L\}\cup(V\times\{\top\})\),
well-definedness follows from \(f(0)=0\): a nontop label has
zero amplitude, which remains zero. Linearity proves compatibility
with the already defined lattice receiver's operations, exactly
as in SDB34–SDB38. Injective maps remain injective because both
the amplitude and the unchanged label can be recovered.
Every composition identity retains the same label, including
when an amplitude vanishes.

This statement concerns \(z_\lambda\) in that existing receiving
carrier. It does not rename any \(z_\lambda\) as primitive
\(\tau\), and does not reinstate the retracted source addition.
The rational branch index \(c\), the zero index \(\rho\), and
any support index \(\lambda\) are distinct retained data in
these maps.
