# The distinguished collision prism and its actual module specializations

Independent derivation, 23 September 2026.

The element \(3+\epsilon\) already occurring in the radical–cotangent extension defines a bounded prism on the retained four-state integral collision algebra. This proof constructs that prism, its exact map from the original unsplit algebra, and the specializations of the original nilradical and cotangent modules. It retains the given Frobenius parameter and original residue coefficients.

The source definitions are Bhargav Bhatt and Peter Scholze, [*Prisms and Prismatic Cohomology*, arXiv:1905.08229v4, original author source](https://arxiv.org/src/1905.08229v4), labels DefPrismCat, FrobLiftTheta, distinguishedDivide, prismcrit, and PrismMapTaut. The local original-source reading record is given in DP11. Every application to the programme algebras is proved below.

## DP1. Original algebras and the retained Frobenius family

Let \(O=\mathbb Z_3\), fix \(c\in O\), and retain
\[
B=O[x,T]/(x^2(x+3),T^2-3x(x+2)),\qquad
C=O[\epsilon,T]/(\epsilon^2,T^2-6\epsilon).
\tag{DP1}
\]
Successive monic division gives the free \(O\)-bases
\[
1,x,x^2,T,xT,x^2T,\qquad 1,\epsilon,T,\epsilon T.
\tag{DP2}
\]
The quotient \(q:B\to C\), \(x\mapsto\epsilon,T\mapsto T\), is onto and has kernel
\[
J=(x^2)=Ox^2\oplus Ox^2T.
\tag{DP3}
\]

Put \(n_1=x(x+3)\), \(n_2=T(x+3)\), \(n_3=Tx(x+3)\). The retained Frobenius maps fix \(O\) and have values
\[
\phi_B(x)=0,\qquad\phi_B(T)=3c\,n_3;
\]
\[
\phi_C(\epsilon)=0,\qquad\phi_C(T)=9c\,\epsilon T.
\tag{DP4}
\]
They are algebra homomorphisms: \(n_3^2=0\) and \((\epsilon T)^2=0\), so the quadratic relations map to zero, and the other relations map to zero because \(x,\epsilon\) do. Modulo 3, both maps are Frobenius. On \(B/3\), \(x^3=T^3=0\); on \(C/3\), \(\epsilon^3=T^3=0\); and constants have the usual characteristic-three Frobenius.

Both rings are 3-torsionfree, so
\[
\delta_A(f)=\frac{\phi_A(f)-f^3}{3}\quad(A=B,C)
\tag{DP5}
\]
is a well-defined integral operation. Expansion gives
\[
\delta_A(f+g)=\delta_A(f)+\delta_A(g)-fg(f+g),
\]
\[
\delta_A(fg)=f^3\delta_A(g)+g^3\delta_A(f)+3\delta_A(f)\delta_A(g),
\]
and \(\delta_A(0)=\delta_A(1)=0\), proving the delta-ring identities directly. In particular
\[
\delta_B(x)=x^2,\qquad
\delta_B(T)=c\,n_3-x(x+2)T,
\]
\[
\delta_C(\epsilon)=0,\qquad
\delta_C(T)=(3c-2)\epsilon T.
\tag{DP6}
\]
The quotient satisfies \(q\phi_B=\phi_Cq\), because \(q(n_3)=3\epsilon T\). Applying DP5 and using that \(C\) is 3-torsionfree proves \(q\delta_B=\delta_Cq\). The generator formulas DP6 also verify this equality directly.

The parameter is transported exactly: if the target family in DP4 had parameter \(c'\), compatibility on \(T\) would require \(9(c-c')\epsilon T=0\). The free basis DP2 then gives \(c=c'\). Every \(c\in O\) gives the displayed compatible pair; no reduction of that parameter is being substituted.

## DP2. The distinguished element and all of its torsion

Retain the two corresponding elements
\[
a_B=3+x,\qquad a_C=3+\epsilon.
\tag{DP7}
\]
They satisfy
\[
a_C(3-\epsilon)=9.
\tag{DP8}
\]
If \(a_C f=0\), multiplication by \(3-\epsilon\) gives \(9f=0\), so \(f=0\) by DP2. Thus \(a_C\) is a nonzerodivisor.

In \(B\), multiplication of a general coefficient polynomial gives
\[
(3+x)(p_0+p_1x+p_2x^2)
=3p_0+(p_0+3p_1)x+p_1x^2.
\]
It vanishes exactly when \(p_0=p_1=0\). The same calculation applies to the \(T\)-coefficient polynomial. Therefore
\[
\operatorname{Ann}_B(a_B)=J.
\]
For every \(r\ge1\),
\[
\operatorname{Ann}_B(a_B^r)=J.
\tag{DP9}
\]
Indeed, if \(a_B^r f=0\), applying \(q\) gives \(a_C^r q(f)=0\), so \(q(f)=0\) and \(f\in J\). Conversely \(a_B J=0\). Hence the quotient \(q\) kills exactly all \(a_B\)-power torsion, with no additional elements.

The Frobenius and delta values are
\[
\phi_B(a_B)=\phi_C(a_C)=3,
\]
\[
\delta_B(a_B)=-8-9x-2x^2,\qquad
\delta_C(a_C)=-8-9\epsilon.
\tag{DP10}
\]
For \(B\), expand \((3+x)^3\) and use \(x^3=-3x^2\); for \(C\), use \(\epsilon^2=0\). Both delta values are units, with exact inverses
\[
\delta_B(a_B)^{-1}=-\frac18+\frac9{64}x+\frac{11}{64}x^2,
\]
\[
\delta_C(a_C)^{-1}=-\frac18+\frac9{64}\epsilon.
\tag{DP11}
\]
Multiplying and reducing by \(x^3=-3x^2,x^4=9x^2\), or by \(\epsilon^2=0\), proves these formulas. All denominators are powers of 2 and are units in \(O\).

Thus both elements are distinguished, meaning their delta values are units. The pair \((B,(a_B))\) fails the Cartier-divisor condition, since the nonzero ideal \(J\) annihilates \(a_B\). The quotient \(C\) removes precisely this obstruction, by DP9.

## DP3. Complete verification of the bounded-prism axioms

A prism at 3 is a delta-ring \(A\) with a Cartier ideal \(I\), derived \((3,I)\)-complete, and satisfying \(3\in I+\phi(I)A\). It is bounded when \(A/I\) has bounded \(3\)-power torsion.

Take \(I_C=(a_C)\). It is Cartier by DP8. Since \(\phi_C(a_C)=3\),
\[
3\in\phi_C(I_C)C,
\tag{DP12}
\]
which proves the required ideal containment.

For completeness, retain the exact ideals
\[
(3,a_C)=(3,\epsilon),\qquad
(3,\epsilon)^r=(3^r,3^{r-1}\epsilon)\quad(r\ge1).
\tag{DP13}
\]
The second formula follows by expanding a product of \(r\) generators and using \(\epsilon^2=0\). These powers are cofinal with the powers of \((3)\). Since \(C\) is finite free over the complete ring \(O\), its ordinary completion for this ideal is \(C\).

There is also a direct derived-completeness calculation. Use the Koszul tower
\[
K_r=\operatorname{Kos}_C(3^r,\epsilon^r).
\]
For \(r\ge2\), one has \(\epsilon^r=0\), and \(3^r\) is regular. Thus the only cohomology groups of \(K_r\) are \(C/3^rC\) in degrees 0 and \(-1\). The transition \(K_{r+1}\to K_r\) multiplies the generator for \(3^{r+1}\) by 3 and the generator for \(\epsilon^{r+1}\) by \(\epsilon\). On degree-zero cohomology the transition is reduction; on degree-minus-one cohomology it includes multiplication by \(\epsilon\). Every two-step transition in the latter tower is therefore zero.

The degree-zero tower is surjective, so its higher inverse limit vanishes and its inverse limit is \(C\). The degree-minus-one tower is pro-zero, so both its inverse limit and higher inverse limit vanish. The inverse-limit cohomology sequence for these bounded complexes consequently gives
\[
R\!\varprojlim_r K_r\simeq C
\]
in degree zero. This proves derived \((3,\epsilon)\)-completeness, hence derived \((3,a_C)\)-completeness, with the actual transition maps specified.

The \(a_C\)-adic topology itself is also cofinal with the 3-adic topology:
\[
a_C^2=9+6\epsilon\in3C,\qquad9\in a_CC.
\tag{DP14}
\]
Indeed \(a_C^{2r}C\subset3^rC\) and \(3^{2r}C\subset a_C^rC\). No inversion of 3 or of \(a_C\) is involved.

The quotient is exactly
\[
D:=C/(a_C)\xrightarrow{\sim}(O/9O)[T]/T^2,
\qquad \epsilon\mapsto-3,\quad T\mapsto T.
\tag{DP15}
\]
To verify this, impose \(\epsilon=-3\). The relation \(\epsilon^2=0\) becomes \(9=0\), and \(T^2-6\epsilon=0\) becomes \(T^2+18=0\), which is \(T^2=0\) modulo 9. These substitutions define inverse maps. The quotient is killed by 9, and its element 1 has additive order 9. Hence its full \(3\)-power torsion has exact exponent 9.

It follows from DP8 and DP12–DP15 that
\[
\boxed{(C,(3+\epsilon))\text{ is a bounded, oriented prism}.}
\tag{DP16}
\]
This holds for every retained parameter \(c\in O\).

## DP4. The exact universal quotient and its prism form

The map \(q\) is universal among delta-maps from \(B\) for which the image of \(a_B\) is regular. Precisely, let \(f:B\to A\) be a delta-ring map and assume multiplication by \(f(a_B)\) is injective on \(A\). For \(j\in J\),
\[
f(a_B)f(j)=f(a_Bj)=0,
\]
so \(f(j)=0\). There is therefore a unique ring map \(\overline f:C=B/J\to A\) with \(\overline f q=f\). It is a delta-map: for \(b\in B\),
\[
\overline f(\delta_C(qb))
=\overline f(q\delta_Bb)
=f(\delta_Bb)
=\delta_A(fb).
\]
Surjectivity of \(q\) proves the required compatibility for every element of \(C\). This establishes the universal property with its exact domain of targets.

For prism targets there is a stronger formulation. A distinguished element \(d\) belonging to the Cartier ideal \(I\) of a prism \((A,I)\) generates \(I\), and is therefore regular. Here is the argument with its hypotheses retained. The original prism criterion supplies a faithfully flat delta-localization \(A\to A'\) on which \(IA'=(e)\), with \(e,3\) in the Jacobson radical. Write \(d=eu\) there. The delta product identity gives
\[
\delta(d)=e^3\delta(u)+u^3\delta(e)+3\delta(e)\delta(u).
\]
The left side is a unit, and the first and third terms on the right lie in the Jacobson radical. Consequently \(u^3\delta(e)\) is a unit, and hence \(u\) is a unit. Thus \(IA'=(d)\). Faithful flatness descends the ideal equality \(I=(d)\); regularity follows after the same cover, where \(d\) is a unit times the regular Cartier generator \(e\).

Apply this to a delta-map \(f:B\to A\) with \((A,I)\) a prism and \(f(a_B)\in I\). The element \(f(a_B)\) is distinguished because the unit in DP10 maps to \(\delta_A(f(a_B))\). It therefore generates \(I\) and is regular. The factorization just proved gives a unique prism morphism
\[
(C,(a_C))\longrightarrow(A,I).
\tag{DP17}
\]
Thus DP16 is the initial prism equipped with such a delta-map from the original \(B\) carrying \(a_B\) into its prism ideal. This is a property of the specified original element and specified Frobenius family. It does not assert a prism structure with ideal \((a_B)\) on \(B\).

## DP5. The actual map to the crystalline prism

The same delta-ring \(C\) also supports the bounded crystalline prism \((C,(3))\): multiplication by 3 is injective, \(C\) is derived 3-complete by its free \(O\)-basis, \(3\in(3)\), and \(C/3\) has its \(3\)-torsion killed by 3.

The Frobenius \(\phi_C\) is itself a delta-map. Indeed, in the 3-torsionfree ring \(C\), applying \(\phi_C\) to DP5 and using that it fixes 3 gives
\[
3\phi_C(\delta_C f)=\phi_C^2(f)-\phi_C(f)^3
=3\delta_C(\phi_C f).
\]
Cancelling 3 proves the assertion. Since \(\phi_C(a_C)=3\), it defines a prism morphism
\[
\phi_C:(C,(3+\epsilon))\longrightarrow(C,(3)).
\tag{DP18}
\]
The extended image of the source ideal is exactly \((3)\).

The identity ring map is a prism morphism in neither direction. One has
\(a_C\notin3C\), since its \(\epsilon\)-coefficient is 1 in the free basis. Also \(3\notin a_CC\), since 3 has nonzero image in the characteristic-nine quotient DP15.

On prism quotients, DP18 induces the exact map
\[
D=(O/9O)[T]/T^2\longrightarrow
C/3=\mathbb F_3[\epsilon,T]/(\epsilon^2,T^2),
\qquad T\mapsto0,\quad \overline z\mapsto z\bmod3.
\tag{DP19}
\]
Its image is the constants \(\mathbb F_3\), and its kernel is \((3,T)\subset D\). These formulas follow immediately from DP4, including its factor \(9c\).

## DP6. The nilradical quotient is this prism specialization

Retain
\[
N_B=On_1\oplus On_2\oplus On_3,\qquad
N_C=O\epsilon\oplus OT\oplus O\epsilon T.
\tag{DP20}
\]
These are the original nilradicals. For \(C\), the stated ideal is nilpotent and its quotient is the reduced ring \(O\). For \(B\), evaluation at \((0,0),(-3,3),(-3,-3)\) has precisely this kernel: a coefficient expression \(p(x)+Tq_0(x)\) is killed by all three maps exactly when \(p(0)=p(-3)=q_0(-3)=0\), giving the displayed three generators. Their products satisfy
\[
n_1^2=n_1n_3=n_2n_3=n_3^2=0,\quad
n_1n_2=3n_3,\quad n_2^2=18n_1,
\]
so that kernel is nilpotent. Every nilpotent must vanish in the reduced evaluation target, proving equality with the nilradical.

The actions are
\[
xn_1=xn_3=0,\quad xn_2=n_3,\qquad
Tn_1=n_3,\quad Tn_2=6n_1,\quad Tn_3=0.
\tag{DP21}
\]
In particular \(JN_B=0\), so \(N_B\) is a \(C\)-module through \(q\). The map
\[
i:N_B\xrightarrow{\sim}N_C,\qquad
n_1\mapsto\epsilon,\quad n_2\mapsto T,\quad n_3\mapsto\epsilon T
\tag{DP22}
\]
is \(C\)-linear: every generator action in DP21 agrees with multiplication by \(\epsilon,T\) on its images. Its basis map is bijective.

The actual quotient-induced map \(q_N\) is
\[
q_N(n_1)=3\epsilon,\quad
q_N(n_2)=3T+\epsilon T,\quad
q_N(n_3)=3\epsilon T.
\]
Thus
\[
\boxed{q_N=m_{a_C}\circ i.}
\tag{DP23}
\]
Multiplication by \(a_C\) is injective on \(N_C\), since it is injective on \(C\). Therefore
\[
Q_N=\operatorname{coker}q_N
=N_C/a_CN_C
\simeq N_C\otimes_C^{\mathbf L}D
\tag{DP24}
\]
with the derived tensor concentrated in degree zero. To prove the derived assertion, use the free resolution
\(0\to C\xrightarrow{a_C}C\to D\to0\). Tensoring gives the two-term map \(a_C:N_C\to N_C\), whose kernel is zero; its cokernel is exactly DP24.

There is also an injection \(N_C/a_CN_C\to C/a_CC\). If \(a_C f\in N_C\), its constant coefficient is \(3f_0\). That coefficient vanishes only when \(f_0=0\), so \(f\in N_C\). Hence \(N_C\cap a_CC=a_CN_C\), proving injection. Under DP15 its image is precisely
\[
\boxed{Q_N\xrightarrow{\sim}(3,T)\subset D,\qquad
[\epsilon]\mapsto-3,\quad[T]\mapsto T.}
\tag{DP25}
\]
The ideal \((3,T)\) is nilpotent, with
\[
(3,T)^2=(3T),\qquad(3,T)^3=0.
\]
Its quotient in \(D\) is \(\mathbb F_3\), which is reduced, so it is exactly \(\operatorname{Nil}(D)\). Thus the same \(Q_N\) is the original module specialization, the nilradical of the prism quotient, and the kernel of DP19.

In original generators \(a=[\epsilon]\), \(b=[T]\), its module presentation remains
\[
Q_N=(O/3O)a\oplus(O/9O)b,\qquad[\epsilon T]=-3b.
\tag{DP26}
\]
The sign agrees with the embedding \(\epsilon\mapsto-3\) in DP25.

## DP7. Both cotangent quotients and their exact comparison

Retain the original relative cotangent kernels
\[
H_B=H^{-1}(L_{B/O}),\qquad H_C=H^{-1}(L_{C/O}).
\]
Their free bases are
\[
u_1=(n_1,0),\quad u_2=(n_3,0),\quad u_3=(n_2,n_3);
\]
\[
v_1=(\epsilon,0),\quad v_2=(\epsilon T,0),\quad
v_3=(3T,\epsilon T).
\tag{DP27}
\]
These are kernels of the respective Jacobian matrices
\[
\begin{pmatrix}3x(x+2)&-6(x+1)\\0&2T\end{pmatrix},
\qquad
\begin{pmatrix}2\epsilon&-6\\0&2T\end{pmatrix}.
\]
For completeness, let \(A_0=O[x]/(x^2(x+3))\). Multiplication by \(x\) sends \(p_0+p_1x+p_2x^2\) to \(p_0x+(p_1-3p_2)x^2\), so its kernel is \(On_1\). Also \(x+2\) is a unit, with inverse \(1/2-x/4-x^2/4\). Writing \(B=A_0\oplus TA_0\), the equation \(T(p+Tq_0)=0\) forces \(p=0\) and \(3x(x+2)q_0=0\). Freeness permits cancellation of 3, and the unit inverse gives \(q_0\in On_1\). Thus \(\operatorname{Ann}_B(T)=On_3\) and \(\operatorname{Ann}_B(T^2)=On_1\oplus On_3\). In the first Jacobian kernel, the lower equation gives \(b=zn_3\), and the upper equation gives \(T^2a=6zn_3\), since \((x+1)n_3=n_3\). Since \(T^2n_2=6n_3\), this means \(a-zn_2\in On_1\oplus On_3\), exactly the three displayed cycles. For the second kernel, coefficient comparison in the free basis of \(C\) gives \(\operatorname{Ann}_C(T)=O\epsilon T\); the equation \(\epsilon a=3b\) then gives its stated basis. These are the original presentations, with no coordinate change.

The maps previously proved in NC18–NC19 are
\[
\kappa_B(n_1)=u_1,\quad\kappa_B(n_2)=u_3,\quad
\kappa_B(n_3)=u_2;
\]
\[
\kappa_C(\epsilon)=3v_1,\quad
\kappa_C(T)=v_3-2v_2,\quad
\kappa_C(\epsilon T)=3v_2.
\tag{DP28}
\]
The first is a \(C\)-linear isomorphism and the second a \(C\)-linear injection. Their linearity follows from the generator actions
\[
\epsilon v_1=\epsilon v_2=0,\quad\epsilon v_3=3v_2,\qquad
Tv_1=v_2,\quad Tv_2=0,\quad Tv_3=18v_1
\]
and DP21; injectivity follows from their independent displayed coefficients. Direct substitution gives
\[
q_H(u_1)=9v_1,\quad q_H(u_2)=9v_2,\quad
q_H(u_3)=3v_3-3v_2,
\]
and hence the exact factorization
\[
\boxed{q_H=\kappa_C\,m_{a_C}\,i\,\kappa_B^{-1}.}
\tag{DP29}
\]
Consequently the actual cotangent cokernel is
\[
Q_H=H_C/(a_C\kappa_C(N_C)).
\tag{DP30}
\]
This is connected to the prism specialization of the entire \(H_C\) by the surjection
\[
Q_H\longrightarrow H_C/a_CH_C.
\]
Multiplication by \(a_C\) is injective on the \(O\)-free module \(H_C\): if \(a_C h=0\), then \(9h=(3-\epsilon)a_C h=0\). Its induced map therefore identifies
\[
a_CH_C/(a_C\kappa_C(N_C))
\simeq H_C/\kappa_C(N_C).
\]
The latter is \(R=\mathbb F_3[T]/T^2\), via
\([v_1]\mapsto1,[v_2]\mapsto T,[v_3]\mapsto2T\). This yields the exact sequence
\[
0\longrightarrow R\xrightarrow{\,a_C\,}Q_H
\longrightarrow H_C/a_CH_C\longrightarrow0.
\tag{DP31}
\]
The first arrow means: lift a class from \(H_C/\kappa_C(N_C)\), multiply its lift by \(a_C\), and take its class in DP30. It is well defined and injective by the preceding cancellation proof.

The second quotient is explicitly
\[
H_C/a_CH_C\simeq\mathbb F_3\{[v_1],[v_2],[v_3]\}
\simeq R\oplus\mathbb F_3
\tag{DP32}
\]
as \(C\)-modules. Indeed \(a_Cv_1=3v_1\), \(a_Cv_2=3v_2\), and \(a_Cv_3=3v_3+3v_2\), so the quotient has exactly the three relations \(3v_j=0\). There \(\epsilon\) acts as zero, \(T[v_1]=[v_2]\), and \(T[v_2]=T[v_3]=0\), giving the displayed module decomposition. Its derived specialization is again concentrated in degree zero because \(a_C\) is injective on \(H_C\).

Thus DP30 and DP32 have both their actual presentations and their connecting maps. In particular \(Q_H\), of order \(3^5\), is not replaced by the order-\(3^3\) specialization DP32.

## DP8. The prism element in the original extension

Use the original notation
\[
Q_N=(O/3)a\oplus(O/9)b,\qquad
Q_H=(O/9)c_1\oplus(O/9)c_2\oplus(O/3)w,
\]
where \(c_1=[v_1]\), \(c_2=[v_2]\), \(w=[v_3-v_2]\). The original extension maps are
\[
\kappa(a)=3c_1,\quad\kappa(b)=w-c_2,\qquad
\psi(c_1)=1,\quad\psi(c_2)=\psi(w)=T.
\tag{DP33}
\]
The connecting map associated with the annihilator element \(a_C\) is
\[
\rho:R\to Q_N[3],\qquad
\rho(1)=a,\quad\rho(T)=-3b.
\]
It is an isomorphism by the original \(T\)-action \(Ta=-3b\). Direct multiplication gives
\[
\boxed{a_C\,\mathrm{id}_{Q_H}=\kappa\rho\psi.}
\tag{DP34}
\]
On \(c_1,c_2,w\), the two sides are respectively \(3c_1,3c_2,3c_2\), since \(3w=0\) and \(\epsilon w=3c_2\). Therefore
\[
a_C^2Q_H=0,\quad
a_CQ_H=\kappa(Q_N[3]),\quad
\ker(a_C:Q_H\to Q_H)=\kappa(Q_N).
\tag{DP35}
\]
The image has order 9 and identifies with the kernel in DP31. The kernel assertion follows from DP34 and injectivity of \(\kappa,\rho\).

Retain also the coefficient-3 map
\[
\theta:Q_H\to Q_N,\qquad
\kappa\theta=3\,\mathrm{id}_{Q_H},
\]
whose values are \(\theta(c_1)=a,\theta(c_2)=-3b,\theta(w)=0\). Then the original divided cotangent operator has the exact expression
\[
L=-\frac{5\epsilon}{8}
=\frac{5(3-a_C)}8
=\frac58\,\kappa(\theta-\rho\psi).
\tag{DP36}
\]
This is an equality of actual integral endomorphisms on \(Q_H\), not division of a torsion map by 3. It relates the coefficient-3 connecting map and the prism-element connecting map with the original coefficient 5 retained.

## DP9. The residue descends to a nonzero derivation on the prism quotient

The original integral residues are
\[
D_B(x)=0,\quad D_B(T)=-n_3/8,\qquad
D_C(\epsilon)=0,\quad D_C(T)=-3\epsilon T/8.
\tag{DP37}
\]
They preserve the defining relations by \(T^2n_1=0\) and \(\epsilon^2=0\), respectively. They commute with \(q\). For the Frobenius family DP4,
\[
D_B\phi_B=\phi_BD_B=0,\qquad
D_C\phi_C=\phi_CD_C=0.
\]
Indeed the images of the residues are the coefficient lines \(On_3\) and \(O\epsilon T\), respectively; Frobenius kills these lines, and the residue kills every Frobenius image. This is compatibility with the stated Frobenius, not an assertion of commutation with the nonlinear delta operation.

On the whole algebra \(C\), the divided operator is an integral derivation:
\[
\partial=\frac{D_C}{3},\qquad
\partial(\epsilon)=0,\quad\partial(T)=-\epsilon T/8.
\tag{DP38}
\]
Its action on \(T^2-6\epsilon\) is
\(-\epsilon T^2/4=-3\epsilon^2/2=0\), and its action on \(\epsilon^2\) is zero, proving that it descends from the polynomial algebra. It fixes \(a_C\), so it induces a derivation on DP15. Its exact formula there is
\[
\overline\partial:(O/9)[T]/T^2\longrightarrow(O/9)[T]/T^2,
\qquad
\overline\partial(z_0+z_1T)=\frac38z_1T.
\tag{DP39}
\]
It kills constants and is nonzero, since \(3T\ne0\). Its square and its triple are zero. The unscaled \(D_C=3\partial\) consequently induces the zero derivation on the prism quotient.

Under the actual nilradical identification DP25, its restriction is exactly
\[
A_N(a)=0,\qquad A_N(b)=\frac38b.
\tag{DP40}
\]
In particular its image is the ideal \((3T)=\operatorname{Nil}(D)^2\), of order 3. It is not multiplication by \(3/8\) on the whole ring \(D\), since its value at 1 is zero; multiplication by \(3/8\) describes only its restriction to the nilradical, where \(3\cdot3=0\).

The asymmetry with the source \(B\) is exact. Dividing \(D_B(T)\) by 3 would give
\[
-\frac{x^2T}{24}-\frac{xT}{8},
\]
whose \(x^2T\)-coefficient does not belong to \(O\). Thus \(D_B/3\) is not an integral algebra derivation on \(B\), although its original restriction to \(N_B\) is divisible by 3, as proved in NC36–NC43. The map to \(C\), and then the prism specialization, are the specified morphisms relating these facts.

## DP10. The exact ordinary spectra

The nilradical of \(C\) is \(N_C=(\epsilon,T)\), as proved in DP20, and \(C/N_C=O\). Every prime ideal contains the nilradical. Since \(O=\mathbb Z_3\) has exactly the prime ideals \((0)\) and \((3)\), the complete ordinary spectrum is
\[
\operatorname{Spec}(C)=\{\mathfrak n_C,\mathfrak m_C\},\qquad
\mathfrak n_C=(\epsilon,T),\quad
\mathfrak m_C=(3,\epsilon,T).
\tag{DP41}
\]
Here \(\mathfrak n_C\subset\mathfrak m_C\); the first point is generic and the second closed. The quotient rings by these ideals are respectively \(O\) and \(\mathbb F_3\), so each displayed ideal is prime and the list is exhaustive.

For the actual prism quotient, DP25 proves
\[
\operatorname{Nil}(D)=(3,T)=:\mathfrak m_D,\qquad
D/\mathfrak m_D=\mathbb F_3.
\tag{DP42}
\]
Thus \(\operatorname{Spec}(D)\) has the single prime \(\mathfrak m_D\). The quotient map \(C\to D\) pulls it back to \(\mathfrak m_C\): the three elements \(3,\epsilon,T\) map into \((3,T)\), while the residual scalar map is reduction modulo 3. Therefore the ordinary closed immersion has image
\[
\operatorname{Spec}(D)\longrightarrow\operatorname{Spec}(C),\qquad
\mathfrak m_D\longmapsto\mathfrak m_C,
\quad\operatorname{im}=V(a_C)=\{\mathfrak m_C\}.
\tag{DP43}
\]
Indeed the image of \(a_C\) in \(C/\mathfrak n_C=O\) is the nonzero scalar 3, so \(\mathfrak n_C\) does not contain \(a_C\), whereas \(\mathfrak m_C\) does. This is specialization at the prime 3 with the complete characteristic-nine nilpotent structure of \(D\) retained. In particular \(D[1/3]=0\), but \(3\) and \(T\) are both nonzero in \(D\).

## DP11. Exact source-reading and use record

Canonical source ID: PUBUNIT-3372AF0EC9F522F58C6F6CEE.

Authors: Bhargav Bhatt and Peter Scholze. Title: *Prisms and Prismatic Cohomology*. Version: arXiv:1905.08229v4, original author source archive retained locally. The existing machine-readable route sources/prismatic/prisms_index_routes.json was consulted before reading. The actual original source read is `sources/prismatic/1905.08229v4/prisms.tex`, SHA256
`f155d2051758e2805efad8513690a91d7b18c19461514abdfd3d32f1676cf38b`.

Actual bounded reading for this derivation: source lines 134–180 for introductory prism and boundedness definitions; 484–558 for delta-ring identities, Frobenius lifts, and quotient compatibility; 689–742 for distinguished-element products and division; 936–1084 for Koszul conventions, the exact prism definition DefPrismCat, prismcrit, rigidity PrismMapTaut, and the start of the bounded-prism properties. These original LaTeX portions were read directly. The rest of that paper is not claimed as newly read here.

The received mathematical uses are precise: DP1 applies the delta-ring definition directly to the retained Frobenius family; DP3 checks every prism and boundedness axiom; DP4 applies the distinguished-division argument and the source's faithfully flat delta-localization construction; DP5 uses the definition of a prism morphism. All specialised identities, torsion kernels, coefficient signs, completeness calculations, and module specializations are proved in this file.

Incoming programme proofs are [Integral eight-state collision proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5a89872598df0902b7c1393cf8e4692ca3010a95/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/research_calculations/INTEGRAL_EIGHT_STATE_COLLISION_DERIVATION.md), the original integral algebra and Frobenius calculations; [Nilradical and cotangent divided-residue proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5a89872598df0902b7c1393cf8e4692ca3010a95/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/research_calculations/NILRADICAL_COTANGENT_DIVIDED_RESIDUE_DERIVATION.md), NC1–NC43; and [Integral extension-class proof](NILRADICAL_COTANGENT_EXTENSION_CLASS_DERIVATION.md), EC1–EC48. This is a construction of a specific bounded prism and its actual module maps. It does not identify ordinary de Rham or cotangent cohomology with an uncomputed prismatic cohomology group.
