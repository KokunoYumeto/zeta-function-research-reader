# The full signed twistor action: degree, cohomology, boundary and coefficients

24 September 2026. Independent mathematical derivation. Private working note. Proof locators TD1–TD12.

## Source and exact scope

The source is Alain Connes and Caterina Consani, *The Absolute Twistor Line and the Geometry of the compactification of Spec Z*, arXiv:2609.00299v1. Original author source: `literature/lorscheid_sources_20260923/papers/06_new_user_intake/2609.00299/tex/CC.tex`. This derivation read source lines 492–620, 772–903, 961–1194 and 1197–1226, together with W1–W10 of `work/stacked_zero_intake_20260924/deligne_visual/WINDING_PARITY_AND_INTEGER_SPECTRUM.md`. These are actual reading ranges, not a claim of complete reading. Source sections 3–4 supply the signed stalk and its two branches; source Theorem `thm:twistor_space_scheme` supplies the quotient real structure; source Proposition `prop:twistor_frobenius` supplies the distinguished odd power maps. The public author edition is [arXiv:2609.00299v1](https://arxiv.org/html/2609.00299v1).

The calculations below concern the actual complex points, the retained signed maps, and explicitly constructed coefficient objects. They do not assign an arithmetic operation, vector, coordinate or distance to the supporting point. In particular, the coordinate below is the actual value of the source section \(T\) under a complex character. It is not a coordinate of the user's proposed support \(\tau\).

The source quotient of complex points and the source equivariant topos are different objects connected by evaluation. This note computes the cohomology of the former and explicit coefficient constructions on it. It makes no identification of that cohomology with the cohomology of the entire absolute arithmetic topos.

## TD1. Full maps before and after taking the geometric quotient

Retain the source group and involution

\[
G=\langle T,J,\epsilon\mid J^2=\epsilon,\ \epsilon^2=1,\ TJ=JT\rangle,
\quad A(T)=\epsilon T^{-1},\quad A(J)=J^{-1},\quad A(\epsilon)=\epsilon.
\]

Here \(T\) is invertible, \(J\) has exact order four and \(\epsilon=J^2\) has exact order two. A full signed map preserving \(\epsilon\) and commuting with \(A\) is

\[
f_{n,c,b}(T)=T^nJ^c,\qquad f_{n,c,b}(J)=J^b,
\qquad n\in2\mathbb Z+1,\ c\in\mathbb Z/4\mathbb Z,\ b\in\{1,3\}.
\tag{TD1.1}
\]

For completeness, every finite-order element of \(G\cong\mathbb Z\times\mathbb Z/4\mathbb Z\) belongs to \(\langle J\rangle\), so the image of \(J\) is \(J^b\). The equation \(f(J^2)=\epsilon\) is \(2b=2\pmod4\). The image of \(T\) is \(T^nJ^c\). On \(J\) commutation with \(A\) is automatic; on \(T\) it says

\[
f(A(T))=\epsilon T^{-n}J^{-c}
=A(f(T))=\epsilon^nT^{-n}J^{-c}.
\]

Thus \(n\) is odd, and the displayed conditions are also sufficient on both generators. In particular \(n\ne0\). Nothing has been removed from the \(J\)-branch or the sign.

A generic complex character is

\[
\chi_{z,j}(T)=z,\quad \chi_{z,j}(J)=j,\quad
\chi_{z,j}(\epsilon)=-1,
\qquad z\in\mathbb C^\times,\quad j\in\{i,-i\}.
\]

Precomposition gives the full point map

\[
g_{n,c,b}(z,j)=(j^c z^n,j^b).
\tag{TD1.2}
\]

On the unquotiented pair of spheres

\[
Y=\mathbb P^1(\mathbb C)_{i}\ \sqcup\
\mathbb P^1(\mathbb C)_{-i},
\]

the map extends by the same rational formula on each component. For \(n>0\), the component map sends \(0\mapsto0\), \(\infty\mapsto\infty\); for \(n<0\), it sends \(0\mapsto\infty\), \(\infty\mapsto0\). The target branch remains \(j^b\).

The source geometric involution is

\[
\alpha(z,j)=(-z^{-1},-j),
\tag{TD1.3}
\]

including its endpoint exchange. Its square is the identity. For \(z\ne0,\infty\),

\[
g\alpha(z,j)=\bigl((-j)^c(-z^{-1})^n,(-j)^b\bigr)
=\bigl((-1)^{c+1}j^cz^{-n},-j^b\bigr),
\]

whereas

\[
\alpha g(z,j)=(-j^{-c}z^{-n},-j^b).
\]

The two first entries agree because \(j^{2c}=(-1)^c\). They agree at the endpoints by the already stated extension. Thus \(g\) descends to \(Y/\langle\alpha\rangle\).

Identify the quotient with the \(j=i\) sphere by the exact quotient map

\[
\pi(z,i)=z,\qquad \pi(z,-i)=-z^{-1}.
\tag{TD1.4}
\]

This is a homeomorphism on each component, and every \(\alpha\)-orbit meets the \(i\) component exactly once. Consequently the induced map of the quotient sphere is

\[
F_{n,c,b}(z)=
\begin{cases}
i^c z^n,&b=1,\\[2mm]
-i^{-c}z^{-n},&b=3.
\end{cases}
\tag{TD1.5}
\]

Both formulas retain the branch choice, its coefficient and its exponent. To state calculations common to the two formulas, write

\[
(a,d)=
\begin{cases}(i^c,n),&b=1,\\(-i^{-c},-n),&b=3.
\end{cases}
\tag{TD1.6}
\]

Thus \(F(z)=az^d\), where \(d\) is a nonzero odd integer and \(a\overline a=1\). Equations TD1.5–TD1.6 are retained whenever this notation is used; they are not a replacement that forgets the signed data.

The source power map is \(n>0\) odd, \(c=0\), \(b\equiv n\pmod4\). Equation TD1.5 then gives exactly \(z^n\) for \(n\equiv1\pmod4\), and \(-1/z^n\) for \(n\equiv3\pmod4\).

## TD2. Holomorphic degree and the antiholomorphic involution

Use homogeneous coordinates \([X:Y]\), with \(z=X/Y\). If \(d>0\), the map is

\[
[X:Y]\longmapsto[aX^d:Y^d].
\tag{TD2.1}
\]

If \(d<0\), set \(e=-d>0\); the map is

\[
[X:Y]\longmapsto[aY^e:X^e].
\tag{TD2.2}
\]

In each expression the two homogeneous polynomials have the same degree, have no common zero on projective space, and have degree \(N=|d|=|n|\). The map is therefore holomorphic at both endpoints as well as on \(\mathbb C^\times\).

Its topological degree, with the complex orientation on both spheres, is \(N\). Indeed choose a target value \(w\ne0,\infty\). For \(d>0\), its inverse images are the \(d\) distinct roots of \(z^d=w/a\); the derivative \(ad z^{d-1}\) is nonzero at every such root. For \(d<0\), they are the \(e\) distinct roots of \(z^e=a/w\); the derivative \(ad z^{d-1}\) is again nonzero there. A nonzero complex derivative has real determinant equal to its squared complex modulus, which is positive. Every inverse image consequently contributes \(+1\) to the oriented degree. This proves

\[
\deg F_{n,c,b}=|n|.
\tag{TD2.3}
\]

In particular the reciprocal branch does not introduce a negative sphere degree: the holomorphic transformation \(z\mapsto-1/z\) has degree \(+1\).

Ordinary conjugation on \(Y\) is \((z,j)\mapsto(\bar z,-j)\). Equation TD1.4 gives on the quotient

\[
\sigma(z)=-\frac1{\bar z},\qquad
\sigma(0)=\infty,\quad\sigma(\infty)=0.
\tag{TD2.4}
\]

For finite nonzero \(z\), use \(d\) odd and \(a\bar a=1\) to compute

\[
F\sigma(z)=a\left(-\frac1{\bar z}\right)^d
=-a\bar z^{-d},
\]

\[
\sigma F(z)=-\frac1{\bar a\bar z^{d}}
=-a\bar z^{-d}.
\tag{TD2.5}
\]

The two maps agree at \(0,\infty\) by their endpoint formulas. Thus every full signed map TD1.1 commutes with the actual twistor real structure. No condition on \(c\) beyond its original value modulo four is needed.

The involution \(\sigma\) is fixed-point-free: a finite nonzero fixed point would give \(z\bar z=-1\), and the endpoints are exchanged. It has topological degree \(-1\): conjugation reverses the complex orientation, while \(-1/z\) is holomorphic of degree \(+1\).

## TD3. Exact ordinary cohomology and pairing on the sphere

Let \(S=\mathbb P^1(\mathbb C)\) and use integral singular cohomology. The usual cell decomposition of the sphere consists of one zero-dimensional cell and one two-dimensional cell, with no one-dimensional cell. Its cellular cochain groups are therefore \(\mathbb Z,0,\mathbb Z\) in degrees \(0,1,2\), and all differentials are zero. Hence

\[
H^0(S;\mathbb Z)=\mathbb Z\,1,\quad
H^1(S;\mathbb Z)=0,\quad
H^2(S;\mathbb Z)=\mathbb Z\,h.
\tag{TD3.1}
\]

Choose the orientation class \(h\) by \(\langle h,[S]\rangle=1\). This specifies an integral generator; it does not rescale a source map or remove one of its factors. The full cohomology ring is

\[
H^*(S;\mathbb Z)=\mathbb Z[h]/(h^2),\qquad |h|=2.
\tag{TD3.2}
\]

The relation \(h^2=0\) follows because the sphere has no cohomology in degree four. Pullback preserves constant functions, and TD2.3 gives the action on orientation. Thus

\[
F^*1=1,\qquad F^*h=|n|h;
\qquad
\sigma^*1=1,\qquad\sigma^*h=-h.
\tag{TD3.3}
\]

There is no degree-one group on which an additional eigenvalue could act. After extension to \(\mathbb Q,\mathbb R\) or \(\mathbb C\), the eigenvalues in degrees zero and two remain \(1\) and \(|n|\).

The exact Poincaré pairing is

\[
H^0(S;\mathbb Z)\times H^2(S;\mathbb Z)\longrightarrow\mathbb Z,
\qquad (r\,1,s\,h)\longmapsto rs.
\tag{TD3.4}
\]

It is perfect because its matrix in these bases is \((1)\). The reversed pairing has the same sign because the degree product is \(0\cdot2=0\). For arbitrary classes \(x,y\) whose degrees sum to two,

\[
\langle F^*x\smile F^*y,[S]\rangle
=|n|\langle x\smile y,[S]\rangle.
\tag{TD3.5}
\]

This follows either from TD3.3–TD3.4 or from naturality and \(F_*[S]=|n|[S]\). The corresponding multiplier for \(\sigma\) is \(-1\). The sphere pairing therefore pairs the eigenvalue \(1\) with the eigenvalue \(|n|\); it does not produce a degree-one self-pairing.

In the conventional Hodge grading, \(1\) has type \((0,0)\), and \(h\) has type \((1,1)\). The first assertion holds because constants are degree-zero functions. For the second, complex dimension one gives \(H^{2,0}=H^{0,2}=0\), so the nonzero degree-two class has type \((1,1)\). Their Hodge weights are respectively \(0\) and \(2\). The eigenvalue \(1\) on constants belongs to weight zero. It is not a counterexample to a weight-one eigenvalue assertion.

## TD4. Both components and the source branches remain visible in cohomology

Order the components of \(Y\) as \(i,-i\). Let \(P_b\) be the two-by-two identity for \(b=1\), and the matrix exchanging the two coordinates for \(b=3\). On \(H^0(Y;\mathbb Z)=\mathbb Z^2\), pullback by \(g\) is \(P_b\). On \(H^2(Y;\mathbb Z)=\mathbb Z^2\), it is \(|n|P_b\). Indeed component pullback selects the target component, and the degree on each component is \(|n|\). The coefficient \(j^c\) is multiplication by a nonzero complex number, which is holomorphic of degree one, so it contributes no further integer to this cohomological degree. Its full point-map value is still TD1.2.

The action of \(\alpha^*\) is the exchanging matrix in both degrees zero and two: its component interchange is accompanied by the holomorphic map \(-1/z\) of degree one. Conjugation on \(Y\) has the exchanging matrix in degree zero and its negative in degree two. The map

\[
\pi^*:H^0(S;\mathbb Z)\longrightarrow H^0(Y;\mathbb Z),
\quad r\longmapsto(r,r),
\]

and the same formula in degree two identify the quotient groups with the \(\alpha^*\)-invariants. This holds integrally here because \(Y\) is a disjoint union of two copies each mapped homeomorphically to \(S\), rather than by invoking an averaging operation that would divide by two. Applying the stated matrices to these diagonal vectors recovers every action in TD3.3.

## TD5. The retained generic open has a different degree-one sector

Let \(U=S\setminus\{0,\infty\}=\mathbb C^\times\) and \(D=\{0,\infty\}\). The inclusion is \(j:U\hookrightarrow S\). The homotopy

\[
H_t(z)=|z|^{-t}z\qquad(0\le t\le1)
\]

retracts \(U\) onto the unit circle. This formula concerns the complex character value \(z\); it makes no statement about a metric at the support. The circle has a cell decomposition with one vertex and one oriented edge whose two endpoints coincide, so its cellular cochain differential is zero. Consequently

\[
H^0(U;\mathbb Z)=\mathbb Z,
\quad H^1(U;\mathbb Z)=\mathbb Z\,u,
\quad H^k(U;\mathbb Z)=0\quad(k\ge2).
\tag{TD5.1}
\]

Specify \(u\) by its value \(1\) on the positively oriented loop \(\gamma(t)=e^{2\pi i t}\), \(0\le t\le1\). Under \(F(z)=az^d\), this loop winds \(d\) times, with the sign of \(d\) retained. Therefore

\[
F^*u=d\,u=
\begin{cases}n\,u,&b=1,\\-n\,u,&b=3.
\end{cases}
\tag{TD5.2}
\]

Multiplication by the coefficient \(a\) does not change the winding number: a path of nonzero constants from \(1\) to \(a\) gives a homotopy between the two circle maps. This statement records its exact topological effect; it does not change TD1.5.

On that loop, \(\sigma(e^{2\pi it})=-e^{2\pi it}\). Thus

\[
\sigma^*u=u.
\tag{TD5.3}
\]

The distinction from TD3.3 is forced by the domains: an antiholomorphic map can reverse the orientation of the sphere while preserving the winding of the punctured sphere because it also exchanges its two punctures.

The differential form \(\omega=dz/z\) satisfies

\[
F^*\omega=d\,\frac{dz}{z},\qquad
\int_\gamma\omega=2\pi i,
\qquad [\omega]=2\pi i\,u_{\mathbb C}.
\tag{TD5.4}
\]

At \(0\) its residue is \(+1\). At \(\infty\), using \(w=1/z\), it is \(-dw/w\) and its residue is \(-1\). Both residues and the factor \(2\pi i\) are retained.

The unfolded punctured space has two copies of \(U\). In their respective \(z\)-coordinates, \(g^*=nP_b\) on degree one, while \(\alpha^*=-P_3\). The quotient pullback is \(u\mapsto(u,-u)\), because \(\pi\) on the second branch is \(-1/z\). Applying \(nP_b\) to this anti-diagonal vector gives the eigenvalue \(d\) in TD5.2. This is the full branch calculation relating the punctured and unpunctured actions.

## TD6. Boundary sequence, compact support and the exact degree-one pairing

The long exact sequence of the pair \((S,D)\), using TD3.1 and the two-point cohomology of \(D\), gives

\[
0\longrightarrow\mathbb Z
\xrightarrow{r\mapsto(r,r)}\mathbb Z^2
\longrightarrow H^1(S,D;\mathbb Z)
\longrightarrow0,
\tag{TD6.1}
\]

and

\[
H^2(S,D;\mathbb Z)\xrightarrow{\sim}H^2(S;\mathbb Z).
\tag{TD6.2}
\]

For the open complement of a closed subset in the compact sphere, relative cohomology is compactly supported cohomology of the complement. This identification follows by extending a cochain with compact support in \(U\) by zero and taking a decreasing family of neighborhoods of \(D\); equivalently, both compute reduced cohomology of the quotient obtained by collapsing \(D\) to its point at infinity. Thus

\[
H^0_c(U;\mathbb Z)=0,\quad
H^1_c(U;\mathbb Z)=\mathbb Z^2/\mathbb Z(1,1),\quad
H^2_c(U;\mathbb Z)=\mathbb Z.
\tag{TD6.3}
\]

The map \(F\) is proper on \(U\). To see this, the inverse image of a compact subset of \(\mathbb C^\times\) has \(|z|^d\) bounded above and away from zero, hence \(|z|\) bounded above and away from zero; it is closed and bounded in \(\mathbb C\). Its endpoint action fixes \(0,\infty\) for \(d>0\) and exchanges them for \(d<0\). On \(\mathbb Z^2/\mathbb Z(1,1)\), the exchanging map acts by \(-1\), because the class of \((0,1)\) equals the negative of the class of \((1,0)\). Naturality of TD6.1–TD6.2 therefore proves

\[
F^*|_{H^1_c(U)}=\operatorname{sgn}(d),
\qquad F^*|_{H^2_c(U)}=|n|.
\tag{TD6.4}
\]

Likewise \(\sigma^*=-1\) on both compactly supported groups: its endpoint action exchanges the two entries, and its sphere degree is \(-1\).

The pairing

\[
H^1(U;\mathbb Z)\times H^1_c(U;\mathbb Z)
\longrightarrow H^2_c(U;\mathbb Z)\xrightarrow{\int_U}\mathbb Z
\tag{TD6.5}
\]

is perfect. Here is an explicit integral generator, orientation and factor check. Write \(z=e^{r+i\theta}\), so the complex orientation is \(dr\wedge d\theta\). The real class \(u_{\mathbb R}\) is represented by \(d\theta/(2\pi)\). Choose a smooth compactly supported function \(\rho(r)\) with \(\int_{\mathbb R}\rho(r)dr=1\), and put \(\chi(r)=\int_r^\infty\rho(s)ds\). This function is one near the endpoint \(0\) and zero near the endpoint \(\infty\). Its derivative is \(d\chi=-\rho(r)dr\). The connecting map in TD6.1 sends the integral endpoint class \((1,0)\) to a generator \(v\), whose de Rham representative is \(d\chi\): this is the definition of the connecting map, obtained by extending the endpoint data and differentiating the extension. Consequently the representative \(-\rho(r)dr\) is the image of an integral class, and its pairing is

\[
\int_U\frac{d\theta}{2\pi}\wedge\bigl(-\rho(r)dr\bigr)
=\frac1{2\pi}\left(\int_{\mathbb R}\rho(r)dr\right)
\left(\int_0^{2\pi}d\theta\right)=1.
\tag{TD6.6}
\]

Since both integral groups are infinite cyclic and their specified integral generators pair to one, their pairing is perfect. Reversing the order in the cup product introduces the degree-one sign: \(\int_Uv\smile u=-1\). For the unreduced logarithmic form, the first pairing in TD6.6 is instead

\[
\int_U\frac{dz}{z}\wedge\bigl(-\rho(r)dr\bigr)=2\pi i.
\tag{TD6.7}
\]

The eigenvalue identity on this pairing is exactly

\[
d\,\operatorname{sgn}(d)=|d|=|n|.
\tag{TD6.8}
\]

For \(\sigma\), the two degree-one actions multiply to \(1\cdot(-1)=-1\), its action on the top compactly supported group. No equality of the two degree-one eigenvalue moduli has been assumed or obtained.

## TD7. The weight of this actual punctured degree-one class

The local boundary calculation gives a second exact sequence

\[
0\longrightarrow H^1(U;\mathbb Q)
\xrightarrow{\operatorname{res}}
H^0(D;\mathbb Q)(-1)
\xrightarrow{\operatorname{sum}}
H^2(S;\mathbb Q)
\longrightarrow0.
\tag{TD7.1}
\]

At the topological level, the first arrow records the integrals over small positively oriented loops about the two punctures. Those loops satisfy their single relation \(\gamma_0+\gamma_\infty=0\) in the sphere with punctures. Therefore the image is the kernel of the sum map, the subgroup of pairs \((r,-r)\). It is one-dimensional by TD5.1, so the sequence is exact. At the de Rham level, the exact vector is \((1,-1)\) for \(\omega=dz/z\), with integral comparison \([\omega]=2\pi i u_{\mathbb C}\) as in TD5.4. The Tate symbol \((-1)\) keeps this codimension-one orientation and its comparison factor; it does not remove it.

The logarithmic Hodge filtration can be computed here without an unknown cohomology group. Use the algebraic structure sheaf and algebraic differential forms on the complex projective line. On \(S\), logarithmic one-forms with poles only along \(D\) form \(\Omega^1_S(\log D)\). A global such form has only simple poles at \(0,\infty\); writing it as \(f(z)dz\), the conditions force \(f(z)=c/z\). Thus its global section space is exactly \(\mathbb C\,dz/z\). There are no degree-two forms. Also \(H^1(S,\mathcal O_S)=0\): on the cover by the two affine lines, every Laurent polynomial on their intersection is a sum of a polynomial in \(z\) and a polynomial in \(z^{-1}\), so the Čech cokernel is zero. The logarithmic de Rham calculation therefore gives \(F^1H^1(U;\mathbb C)=H^1(U;\mathbb C)\), \(F^2=0\).

For the weight filtration in this logarithmic complex, the possible weight-one part is the image of the compactification cohomology \(H^1(S;\mathbb Q)\). That group is zero by TD3.1. The residue quotient embeds in \(H^0(D;\mathbb Q)(-1)\), whose two classes have Hodge type \((1,1)\) and weight two: each is the oriented class of a complex normal disk to a point. Equation TD7.1 proves that every nonzero class of \(H^1(U;\mathbb Q)\) belongs to this weight-two part. Equivalently its complete Hodge structure is \(\mathbb Q(-1)\), with the explicit \(2\pi i\) comparison retained above.

The compactly supported class \(v\) comes from the quotient of \(H^0(D;\mathbb Q)\) by the constants in TD6.1. Both numerator and constants have type \((0,0)\), so \(H_c^1(U;\mathbb Q)\) has type \((0,0)\) and weight zero. Its pairing with the weight-two class \(u\) lands in the weight-two top compactly supported class. This proves why TD6.8 pairs moduli \(|n|\) and \(1\), rather than two moduli \(\sqrt{|n|}\).

Thus the actual sphere has weights zero and two and no degree-one ordinary cohomology; its actual punctured generic open has a degree-one boundary class of weight two and a compactly supported degree-one class of weight zero. These are determinations of these coefficient sectors, not a claim that weight-one coefficients cannot occur in further constructions.

## TD8. A precise finite-characteristic bridge for the distinguished odd powers

Let \(p\) be an odd rational prime. The distinguished map of the source, using \(n=p,c=0,b\equiv p\pmod4\), has coefficients \(1,-1\), so its exact formulas define a map on \(\mathbb P^1\) over \(\mathbb F_p\) as well as over \(\mathbb C\):

\[
F_p(z)=
\begin{cases}z^p,&p\equiv1\pmod4,\\-1/z^p,&p\equiv3\pmod4.
\end{cases}
\tag{TD8.1}
\]

Its \(r\)-fold composite is the source map \(F_{p^r}\). This follows already from precomposition by the source power map \(g\mapsto g^p\); alternatively two reciprocal branches compose as

\[
-\frac1{(-1/z^p)^p}=z^{p^2},
\]

because \(p\) is odd, and induction retains precisely the parity of \(r\).

Put \(q=p^r\). When \(q\equiv1\pmod4\), the fixed points satisfy \(z^q=z\) together with the fixed point \(\infty\). In characteristic \(p\), the polynomial \(z^q-z\) has derivative \(-1\), so it has exactly \(q\) distinct roots over the algebraic closure. Thus there are \(q+1\) fixed points. When \(q\equiv3\pmod4\), neither endpoint is fixed and the equation is \(z^{q+1}=-1\). Its roots are all nonzero and its derivative is \(z^q\) in characteristic \(p\), so it has exactly \(q+1\) distinct roots. Consequently

\[
\#\operatorname{Fix}(F_p^r)=1+p^r
\quad(r\ge1).
\tag{TD8.2}
\]

The associated formal fixed-point generating function is therefore exactly

\[
Z(F_p,t)=\exp\left(\sum_{r\ge1}\frac{1+p^r}{r}t^r\right)
=\frac1{(1-t)(1-pt)}.
\tag{TD8.3}
\]

The equality follows by the formal identity \(-\log(1-x)=\sum_{r\ge1}x^r/r\), applied separately to \(x=t\) and \(x=pt\). Both denominator factors are retained. There is no degree-one numerator factor in this calculation, precisely as TD3 predicts. This is an explicit bridge of the source action to a finite-characteristic sphere calculation. It is not an equality with the original Riemann zeta function or its zero-detecting sector. In particular it has not supplied an arithmetic weight-one object merely by relabeling \(H^0\) or the punctured boundary class.

## TD9. All local systems on the sphere, and actual local systems on the generic open

Every finite-rank local system of vector spaces on \(S\) is constant. Indeed \(S\) is simply connected: it is the union of two open disks whose connected overlap retracts onto a circle, and the overlap generator becomes null-homotopic in each disk; van Kampen gives the trivial fundamental group. Parallel transport from a fixed basepoint is consequently independent of the chosen path. It identifies a local system with the constant system with that fiber. Its cellular cochain complex is the complex of TD3 tensored with the fiber, so its degree-one cohomology is zero. Thus merely choosing a nonsingular local system on this sphere cannot create its missing degree-one sector.

The situation on \(U\) is explicit. A finite-dimensional complex local system is determined by an invertible matrix \(M:V\to V\), its monodromy along \(\gamma\). Use the covering \(u\mapsto e^u\) from \(\mathbb C\) to \(U\), and the relation

\[
(u+2\pi i,v)\sim(u,Mv).
\tag{TD9.1}
\]

This constructs the system and verifies its monodromy. The cellular cochain complex of the circle with these coefficients is

\[
V\xrightarrow{M-I}V
\tag{TD9.2}
\]

in degrees zero and one: the two ends of the lifted edge differ by one deck translation, which is \(M\). It follows exactly that

\[
H^0(U;\mathcal L_M)=\ker(M-I),
\qquad
H^1(U;\mathcal L_M)=\operatorname{coker}(M-I).
\tag{TD9.3}
\]

Pullback by \(F(z)=az^d\) gives monodromy \(M^d\). To see the constant as well as the exponent, choose a logarithm \(\ell\) of the actual coefficient \(a\) in TD1.6. A lift of \(F\) is \(u\mapsto du+\ell\). Increasing \(u\) by \(2\pi i\) increases its image by \(2\pi i d\), giving the claimed monodromy. Changing \(\ell\) by \(2\pi i k\) changes the fiber identification by \(M^k\). Thus this identification retains its basepath choice; it is not canonical without that choice.

With this identification, the induced cellular map from the \(M\)-complex to the \(M^d\)-complex is the identity in degree zero and

\[
S_d(M)=
\begin{cases}
\displaystyle\sum_{k=0}^{d-1}M^k,&d>0,\\[2mm]
\displaystyle-\sum_{k=d}^{-1}M^k,&d<0
\end{cases}
\tag{TD9.4}
\]

in degree one. Each summand is the transport along one traversed edge; for negative \(d\), the edges have the opposite orientation. The chain identity is the exact telescoping equality

\[
S_d(M)(M-I)=M^d-I.
\tag{TD9.5}
\]

For \(d<0\), expanding the sum gives \(-\sum_{k=d}^{-1}(M^{k+1}-M^k)=M^d-I\), including every negative-power term. Therefore this gives an actual pullback map

\[
\operatorname{coker}(M-I)\longrightarrow\operatorname{coker}(M^d-I).
\tag{TD9.6}
\]

It is a map between the stated coefficient systems. An endomorphism of one fixed coefficient system requires a chosen coefficient identification in addition; no such identification or spectral purity is supplied by TD9.6 itself. This is an exact domain statement, not an assumed extra cohomology group.

There is a precise relation between the source winding lattice \(L=G/\langle J\rangle\) and these loops. Characters form the torus \(\operatorname{Hom}(L,\mathbb C^\times)\), and a loop \(\gamma\) gives the homomorphism

\[
L\longrightarrow\mathbb Z,
\qquad \ell\longmapsto\operatorname{wind}\bigl(\gamma(\ell)\bigr).
\tag{TD9.7}
\]

For the source generator \(t=q(T)\), the loop \(\gamma(t)=e^{2\pi it_{\rm loop}}\) gives \(t^m\mapsto m\). Thus the fundamental-group lattice is the integral dual \(\operatorname{Hom}(L,\mathbb Z)\), with its explicit evaluation pairing, rather than an unproved identification of a monomial and a loop. The branch-return map \(-1/z\) reverses this loop generator; equation TD5.2 records the resulting sign after quotienting.

## TD10. The actual sign local system and its order-four real lift

The nontrivial order-two local system on \(U\) is obtained from the double cover

\[
q_2:\mathbb C^\times\longrightarrow\mathbb C^\times,
\qquad q_2(y)=y^2,
\tag{TD10.1}
\]

using the sign representation of its deck group \(\{1,-1\}\). Its monodromy is \(M=-I\). In rank one over \(\mathbb Q\) or \(\mathbb C\), equation TD9.2 is multiplication by \(-2\), an invertible scalar. Therefore

\[
H^0(U;\mathcal L_{-1})=H^1(U;\mathcal L_{-1})=0.
\tag{TD10.2}
\]

Over the integral sign system, multiplication by \(-2\) has zero kernel and cokernel \(\mathbb Z/2\mathbb Z\); thus \(H^1\) is precisely that torsion group. This distinguishes the rational cohomology statement from the integral one.

The relation to the retained parity is exact. Equation W2 gives \(\delta(t^m)=\epsilon^m\). Under the loop-monomial pairing TD9.7, reduction modulo two is unchanged by replacing \(t\) by \(t^{-1}\). Since an infinite cyclic lattice modulo two has a unique nonzero element, its dual has a unique nonzero character to \(\mathbb Z/2\mathbb Z\). This supplies the monodromy \(m\mapsto(-1)^m\), without selecting an orientation on the parity quotient. The source's odd \(d\) preserves this character because \((-1)^{dm}=(-1)^m\).

More explicitly, \(F(z)=az^d\) lifts to

\[
\widetilde F(y)=\kappa y^d,\qquad \kappa^2=a.
\tag{TD10.3}
\]

There are exactly two choices of \(\kappa\), differing by the deck involution. Squaring TD10.3 gives \(a(y^2)^d\), as required. Since \(d\) is odd, \(\widetilde F(-y)=-\widetilde F(y)\); hence each choice induces the requisite sign-coefficient identification, with its twofold choice retained.

The source twistor involution has precisely the two lifts

\[
\widetilde\sigma_{\pm}(y)=\frac{\pm i}{\bar y}.
\tag{TD10.4}
\]

Indeed their squares as complex numbers are \(-1/\bar y^2\), giving \(\sigma(q_2(y))\). Conversely a lift has \(\widetilde\sigma(y)\bar y\) taking values in \(\{i,-i\}\); by continuity on connected \(\mathbb C^\times\), that sign is constant. Their composites satisfy

\[
\widetilde\sigma_{\pm}^{\,2}(y)
=\frac{\pm i}{\overline{(\pm i)/\bar y}}
=\frac{\pm i}{\mp i/y}=-y.
\tag{TD10.5}
\]

Thus their square is the nontrivial deck transformation, and their fourth power is the identity. On the associated sign line, use the relation \([-y,v]=[y,-v]\). The induced conjugate-linear lift is \([y,v]\mapsto[\widetilde\sigma_\pm(y),\bar v]\); its square sends \([y,v]\) to \([-y,v]=[y,-v]\), so its square is \(-I\). This is an actual order-four lift of the order-two twistor involution, constructed from the same punctured source geometry. It retains a parity defect and an exact coefficient object; by TD10.2, it does not itself manufacture a rational degree-one cohomology sector.

The full relation between the lifted arithmetic map and this lifted real structure also retains a sign. Put \(\lambda=\pm i\) and choose \(\kappa\) from TD10.3; since \(a\bar a=1\), one has \(\kappa\bar\kappa=1\). Direct substitution gives

\[
\widetilde F\widetilde\sigma_\lambda(y)
=\kappa\lambda^d\bar y^{-d},
\qquad
\widetilde\sigma_\lambda\widetilde F(y)
=\lambda\bar\kappa^{-1}\bar y^{-d}
=\lambda\kappa\bar y^{-d}.
\]

Thus the ratio is the exact deck sign

\[
\widetilde F\widetilde\sigma_\lambda
=(-1)^{(d-1)/2}\,
\widetilde\sigma_\lambda\widetilde F.
\tag{TD10.6}
\]

The two lifts commute precisely when \(d\equiv1\pmod4\), which, using both branches in TD1.6, is equivalent to \(b\equiv n\pmod4\). In particular every distinguished source power map has this property: for \(n\equiv1\pmod4\), \(d=n\equiv1\), and for \(n\equiv3\pmod4\), \(d=-n\equiv1\). Consequently the source power maps preserve this actual order-four lifted real structure. General full signed maps still commute with \(\sigma\) on the base by TD2.5, but TD10.6 records the precise extra deck sign on this coefficient construction.

## TD11. Weight-one twistor bundles exist even though the base sphere has no \(H^1\)

Ordinary cohomology of the parameter sphere is not the same object as a twistor structure carried by a bundle on that sphere. The following concrete construction supplies the comparison.

The tautological line bundle \(\mathcal O_S(-1)\) has fiber over \([X:Y]\) equal to the line \(\mathbb C(X,Y)\subset\mathbb C^2\). Define the conjugate-linear transformation

\[
Q(X,Y)=(-\bar Y,\bar X).
\tag{TD11.1}
\]

It sends the line over \([X:Y]\) to the line over \([-\bar Y:\bar X]\), which is exactly \(\sigma([X:Y])\). It therefore lifts \(\sigma\) to the tautological bundle. Its square is

\[
Q^2(X,Y)=(-X,-Y).
\tag{TD11.2}
\]

Thus the bundle lift squares to \(-I\), while its projectivization squares to the identity. The induced conjugate-linear lift on the dual bundle \(\mathcal O_S(1)\) also squares to \(-I\), because the dual of scalar multiplication by \(-1\) is multiplication by \(-1\). Tensor powers give square \((-1)^k I\) on \(\mathcal O_S(k)\), including negative powers by duality.

There is also a real lift squaring to \(+I\) on the rank-two bundle

\[
E=\mathcal O_S(1)\otimes_{\mathbb C}\mathbb C^2.
\tag{TD11.3}
\]

Give the second factor the conjugate-linear map \(R(v_1,v_2)=(-\bar v_2,\bar v_1)\), whose square is \(-I\). The tensor map formed from the two conjugate-linear lifts is well-defined: moving a scalar from one tensor factor to the other gives its complex conjugate on both sides. It is conjugate-linear on the tensor product, and its square is \((-I)\otimes(-I)=+I\). This proves the asserted real structure. The bundle in TD11.3 is a direct sum of two copies of \(\mathcal O_S(1)\); in the conventional twistor-bundle terminology it is pure of weight one. This terminology concerns the bundle degree, not \(H^1(S;\mathbb Q)\). Thus TD3 does not rule out this exact weight-one object.

The relation of these bundles to the source base maps is also exact:

\[
F^*\mathcal O_S(k)\cong\mathcal O_S(|n|k).
\tag{TD11.4}
\]

For \(k=1\), take a nonzero linear form on the target homogeneous coordinates. Its pullback through TD2.1 or TD2.2 is a homogeneous polynomial of degree \(|n|\), whose zero divisor has total multiplicity \(|n|\). The corresponding line bundle is \(\mathcal O_S(|n|)\). Tensor powers and duality give every integer \(k\). Equivalently, the two homogeneous expressions TD2.1–TD2.2 construct the pullback line bundle directly with that transition exponent.

For the explicit rank-two bundle \(E\), its degree is two, while the degree of \(F^*E\) is \(2|n|\). If \(|n|>1\), these degrees are unequal, so no holomorphic bundle isomorphism \(F^*E\cong E\) exists: an isomorphism identifies determinant bundles and hence their zero-divisor degrees. Therefore an arithmetic endomorphism acting on coefficients over a fixed twistor parameter cannot be silently identified with a pullback isomorphism along the nontrivial source map of that parameter. The two operations have the proved connecting formula TD11.4, including its precise failure to preserve degree.

This calculation constructs an actual weight-one twistor bundle and its real structure. It does not equip it with an arithmetic Frobenius spectrum or prove a purity statement for that spectrum. Such a spectrum is additional mathematical content, not a consequence of the terminology “weight one.”

## TD12. Exact location of the remaining sector

All maps and groups calculated here are explicit:

1. The full signed source action gives the quotient maps TD1.5, commuting with the actual antiholomorphic involution by TD2.5.
2. Their sphere cohomology is \(H^0=\mathbb Q\), \(H^1=0\), \(H^2=\mathbb Q(-1)\), with actions \(1,|n|\) and pairing multiplier \(|n|\).
3. The retained generic open has \(H^1(U)=\mathbb Q(-1)\) with action \(d\), and \(H^1_c(U)=\mathbb Q(0)\) with action \(\operatorname{sgn}(d)\). The residue sequence and compactification maps prove their relationship to the sphere and to both boundary points.
4. Every nonsingular local system on the sphere is constant. On the actual generic open, all local systems and their pullbacks have the explicit complexes TD9.2–TD9.6. The actual sign system has no rational cohomology but carries the order-four lift TD10.4–TD10.5.
5. A weight-one real twistor bundle does exist by TD11.3, and its pullback under the source map changes degree as TD11.4 specifies.

These calculations isolate a precise target for a further arithmetic construction: a nonzero coefficient or global gluing sector whose arithmetic operator is defined on that sector and whose weight-one pairing can be proved there. Neither the constants nor the two-puncture boundary class is that sector. The source's global amalgam is a proposed place to construct it, but the amalgam definition alone is not a computation of its derived coefficient cohomology. No nonzero \(H^1\), polarization, Frobenius eigenvalue bound or zero-detection map is asserted for that uncomputed global object here.

This is not an impossibility theorem about the programme. The proved connecting objects are the quotient and pullback maps, the compactification/residue sequences, the coefficient complexes, the parity cover and its real lift, and the explicit weight-one bundle. They retain the actual signed winding data while locating exactly which computed sectors have weights zero and two and which constructed bundle has twistor weight one.
