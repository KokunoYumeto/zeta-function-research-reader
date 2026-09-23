# The full integral collision at the prime 3

This calculation retains the finite collision algebra, its original root coordinate, and the signed coordinate. All coefficient maps fix \(O=\mathbb Z_3\). Put
\[
B=O[R,T]/((R-1)^2(R+2),\ T^2-3R^2+3),\qquad x=R-1.
\tag{P3-1}
\]
The substitution is an isomorphism of the displayed presentations, with inverse \(R=x+1\). Thus
\[
B=O[x,T]/(f,g),\quad f=x^2(x+3),\quad
g=T^2-3x(x+2),\quad D=O[T]/T^2,
\quad\pi:B\longrightarrow D,\quad(x,T)\longmapsto(0,T).
\tag{P3-2}
\]
The reflection is \(\sigma(x)=x,\ \sigma(T)=-T\), on both rings. Every calculation below takes place over \(O\); in particular, no root projector involving \(1/3\) is used to define an integral map.

The incoming coordinate identities are [EIGHT_STATE_HEAT_COMPARISON.md, ESH58–72](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/d5c9d198a8432e3ede468b280162a99c00e3f4f7/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/EIGHT_STATE_HEAT_COMPARISON.md). Those statements were read directly together with the relevant entries in SOURCE_READING_AND_USE.md. The Frobenius/delta definition used here is Bhargav Bhatt and Peter Scholze, *Prisms and Prismatic Cohomology*, [arXiv:1905.08229v4, original author source](https://arxiv.org/src/1905.08229v4), `prisms.tex` lines 484–541, in particular `def:deltaring` and `FrobLiftTheta`, read directly for this calculation. The cotangent foundation is Luc Illusie, *Complexe cotangent et déformations I*, III, 3.2.2–3.2.4, in the [retained edition](https://zenodo.org/records/22884471); the diplomatic TeX lines 23386–23779, including the proof of 3.2.4, were read directly. That edition is a transcription of the historical work, not original author TeX. Its source identity and the original Bhatt–Scholze archive hashes remain those recorded in SOURCE_READING_AND_USE.md. All specialized maps, lattices, kernel computations, and cohomology groups below are derived explicitly here.

## 1. The retained algebra is local and free

**P3.1.** The ordered list
\[
\mathcal E=(1,x,x^2,T,xT,x^2T)
\tag{P3-3}
\]
is an \(O\)-basis of \(B\). The ring \(B\) is complete, has no 3-torsion, and is local with maximal ideal \((3,x,T)\). In particular, it admits no nontrivial decomposition as a product of rings over \(O\).

**Proof.** Division by the monic polynomial \(f\) gives the free rank-three ring \(K=O[x]/f\). Division by the monic polynomial \(T^2-3x(x+2)\) then gives \(B=K\oplus TK\), proving the asserted basis and absence of 3-torsion. A finite free module over the complete ring \(O\) is complete. Reduction modulo 3 is
\[
B/3B=\mathbb F_3[x,T]/(x^3,T^2),
\tag{P3-4}
\]
which has the unique maximal ideal \((x,T)\). Because \(B\) is finite and integral over \(O\), every maximal ideal of \(B\) contracts to \((3)\); consequently (P3-4) identifies its unique maximal ideal. An idempotent in a local ring is 0 or 1: one of \(e\) and \(1-e\) is a unit, and \(e(1-e)=0\) then forces the other to vanish. A nontrivial product would supply a different idempotent. This proves the last assertion. \(\square\)

## 2. The integral nilradical, its powers, and the reduced order

Retain exactly the three generators from the incoming collision calculation:
\[
n_1=x(x+3),\qquad n_2=T(x+3),\qquad n_3=Tx(x+3).
\tag{P3-5}
\]

**P3.2.** The nilradical and all its nonzero powers are
\[
\begin{aligned}
N&=On_1\oplus On_2\oplus On_3,\\
N^2&=18On_1\oplus3On_3,\\
N^3&=54On_3,\qquad N^4=0.
\end{aligned}
\tag{P3-6}
\]
The complete multiplication and the actions of the algebra generators are
\[
\begin{gathered}
n_1^2=n_1n_3=n_2n_3=n_3^2=0,\qquad
n_2^2=18n_1,\qquad n_1n_2=3n_3,\\
xn_1=xn_3=0,\quad xn_2=n_3,\qquad
Tn_1=n_3,\quad Tn_2=6n_1,\quad Tn_3=0.
\end{gathered}
\tag{P3-7}
\]

**Proof.** The defining equations give \(x^3=-3x^2\), \(x^4=9x^2\), and \(T^2=3x(x+2)\). Hence
\[
n_1^2=x^2(x+3)^2=f(x+3)=0,\qquad
xn_1=f=0,
\]
and
\[
Tn_2=3x(x+2)(x+3)=3(x+2)n_1=6n_1.
\]
Multiplication of these identities by \(T\), together with \(xn_2=n_3\), proves the second row of (P3-7). The remaining products are
\[
n_2^2=(x+3)Tn_2=6(x+3)n_1=18n_1,
\quad n_1n_2=(x+3)Tn_1=3n_3,
\]
and the zero products follow from \(xn_1=0\), \(n_1^2=0\), and \(Tn_3=0\). Thus their span is an ideal of fourth power zero. Its three displayed generators are independent in (P3-3).

There are three \(O\)-algebra maps to \(O\), with values on \((x,T)\) equal to
\[
(0,0),\qquad(-3,3),\qquad(-3,-3).
\tag{P3-8}
\]
For \(p,q\in O[x]\) of degree at most two, their simultaneous vanishing on \(p+Tq\) means
\[
p(0)=0,\qquad p(-3)+3q(-3)=0,\qquad
p(-3)-3q(-3)=0.
\]
Since 2 and 3 are nonzero divisors in \(O\), this is equivalent to \(p(0)=p(-3)=q(-3)=0\). Writing coefficients explicitly gives \(p=a(x^2+3x)\) and
\(q=b(x+3)+c(x^2+3x)\), with \(a,b,c\in O\). Therefore the common kernel of (P3-8) is exactly the stated span. Every nilpotent must vanish under (P3-8), because \(O\) has no nonzero nilpotents. The span already has fourth power zero, so it is the entire nilradical.

The nonzero entries of the multiplication table generate \(N^2\). Multiplying these by \(N\) gives only multiples of \(54n_3\), with \((18n_1)n_2=54n_3\); multiplying once more gives zero. Independence of \(n_1,n_3\) proves that the sums and powers in (P3-6) are exact. \(\square\)

**P3.3.** Evaluation in (P3-8) induces
\[
B/N\ \simeq\ \{(a,b,c)\in O^3:a\equiv b\equiv c\pmod3\}.
\tag{P3-9}
\]
The integral closure of this reduced order in \(\mathbb Q_3^3\) is \(O^3\); its conductor is \(3O^3\), and
\[
O^3/(B/N)\simeq (O/3O)^2.
\tag{P3-10}
\]

**Proof.** Modulo \(N\), the basis can be reduced to \(1,x,T\), using
\[
x^2=-3x,\quad xT=-3T,\quad x^2T=9T,\quad T^2=-3x.
\]
The images of these three basis vectors under (P3-8) are \((1,1,1)\), \((0,-3,-3)\), and \((0,3,-3)\). Their span lies in the right side of (P3-9). Conversely a triple there has coefficients
\[
a\cdot1+\frac{2a-b-c}{6}x+\frac{b-c}{6}T.
\]
Both quotients belong to \(O\), since their numerators lie in \(3O\) and 2 is a unit; the formula asserts divisibility within \(O\), not inversion of 3 in the algebra. This proves (P3-9). The two independent differences modulo 3 give (P3-10).

The ring \(O^3\) is integral over \(B/N\), because it is generated by the coordinate idempotents and each satisfies \(z^2-z=0\). It is integrally closed in \(\mathbb Q_3^3\): a rational 3-adic coordinate integral over \(O\) has nonnegative valuation. Conversely an element of \(\mathbb Q_3^3\) integral over \(B/N\) is integral over \(O\) by transitivity, because \(B/N\) is finite over \(O\). Thus every coordinate belongs to \(O\), proving the integral-closure assertion. An element \(z\in O^3\) lies in the conductor exactly when each \(ze_i\) lies in (P3-9), where \(e_i\) are the coordinate idempotents. This is equivalent to all three coordinates of \(z\) belonging to \(3O\). \(\square\)

## 3. Exact defects of the marked-root map

**P3.4.** The map \(\pi:B\to D\) is onto, with kernel \(xB\). Its restriction to the nilradical satisfies
\[
\pi(n_1)=\pi(n_3)=0,\qquad\pi(n_2)=3T,
\tag{P3-11}
\]
and consequently there is an exact sequence of \(O\)-modules
\[
0\longrightarrow On_1\oplus On_3\longrightarrow N
\xrightarrow{\ \pi\ }OT\longrightarrow (O/3O)T\longrightarrow0.
\tag{P3-12}
\]
The comparison with the square of the nilradical is
\[
\begin{aligned}
\ker(\pi|_N)/N^2&\simeq (O/9O)n_1\oplus(O/3O)n_3,\\
N/N^2&\simeq On_2\oplus(O/9O)n_1\oplus(O/3O)n_3,\\
N^2/N^3&\simeq O(18n_1)\oplus(O/9O)(3n_3).
\end{aligned}
\tag{P3-13}
\]
All these maps preserve reflection; \(n_1\) has sign \(+1\), and \(n_2,n_3,T\) have sign \(-1\).

**Proof.** Setting \(x=0\) in the presentation leaves exactly \(O[T]/T^2\), proving the first assertion. Substitution proves (P3-11). Independence of the generators proves the kernel and image in (P3-12), and (P3-6) gives every quotient in (P3-13), using that 18 generates the ideal \(9O\) and 54 generates \(27O\). The reflection signs follow directly from (P3-5). \(\square\)

**P3.5.** The square-zero elements of \(B\) are exactly \(On_1\oplus On_3\). Every \(O\)-algebra map \(j:D\to B\) therefore satisfies \(\pi j(T)=0\). In particular \(\pi\) has no algebra section.

**Proof.** A square-zero element is nilpotent, so it has a unique expression \(v=an_1+bn_2+cn_3\). The table gives
\[
v^2=18b^2n_1+6abn_3.
\tag{P3-14}
\]
This is zero exactly when \(b=0\), because \(O\) is a domain and the generators are independent. The image of \(T\) under \(j\) must be square-zero; (P3-11) proves its zero marked-root image. \(\square\)

For an additional exact comparison, retain the integral double-root algebra
\[
C=O[\epsilon,T]/(\epsilon^2,T^2-6\epsilon).
\tag{P3-15}
\]

**P3.6.** The coordinate-preserving map
\[
\iota:B\longrightarrow C\times O\times O,
\quad x\longmapsto(\epsilon,-3,-3),\quad
T\longmapsto(T,3,-3)
\tag{P3-16}
\]
is injective, and its cokernel as an \(O\)-module is
\[
\operatorname{coker}\iota\simeq O/9O\oplus O/27O.
\tag{P3-17}
\]

**Proof.** Both defining equations vanish after the indicated substitutions. In the ordered basis \(1,\epsilon,T,\epsilon T\) of \(C\), an element of the target is written \((a+b\epsilon+cT+d\epsilon T,e,f)\). It lies in the image if and only if
\[
\frac{e+f}{2}-a+3b\in9O,\qquad
\frac{e-f}{2}-3c+9d\in27O.
\tag{P3-18}
\]
Indeed a source element \(p_0+p_1x+p_2x^2+T(q_0+q_1x+q_2x^2)\) has \(a=p_0,b=p_1,c=q_0,d=q_1\); the two expressions in (P3-18) equal \(9p_2\) and \(27q_2\). Conversely membership in the respective ideals determines unique \(p_2,q_2\in O\), and these produce the proposed target. This also proves injectivity. Reduction of the two expressions modulo their indicated ideals is onto \(O/9O\oplus O/27O\), since the coordinates \(e,f\) allow arbitrary sum and difference after division by the unit 2. Its kernel is exactly the image just computed, proving (P3-17). \(\square\)

## 4. Every coefficient-preserving Frobenius lift

Here a Frobenius lift means an \(O\)-algebra endomorphism whose reduction modulo 3 is the absolute Frobenius of (P3-4).

**P3.7.** Every such endomorphism is exactly one of the following:
\[
\begin{array}{ll}
\Phi_+:&(x,T)\longmapsto(-3,3),\\
\Phi_-:&(x,T)\longmapsto(-3,-3),\\
\Phi_v:&x\longmapsto\dfrac32v^2,\quad T\longmapsto3v,
\qquad v\in N.
\end{array}
\tag{P3-19}
\]
The parameter \(v\) in the third family is unique. For \(v=an_1+bn_2+cn_3\), its coordinates are
\[
\Phi_v(x)=27b^2n_1+9abn_3,\qquad
\Phi_v(T)=3an_1+3bn_2+3cn_3.
\tag{P3-20}
\]

**Proof.** In (P3-4), \(x^3=T^3=0\), so every Frobenius lift has images \(X=3u,Y=3v\), for unique \(u,v\in B\). Substituting these into the defining equations and cancelling powers of the nonzero divisor 3 gives the equivalent conditions
\[
u^2(u+1)=0,\qquad v^2=u(3u+2).
\tag{P3-21}
\]
Because \(B\) is local, either \(u\) is a unit or \(u+1\) is a unit. In the first case (P3-21) implies \(u=-1\), then \(v^2=1\). Since \((v-1)(v+1)=0\) and their difference is the unit 2, one factor is a unit and the other is zero. Thus \(v=1\) or \(v=-1\), producing the first two maps.

If \(u\) is not a unit, then \(u+1\) is a unit, so \(u^2=0\). The other equation gives \(v^2=2u\), hence \(v^4=0\) and \(v\in N\). It follows that \(u=v^2/2\), yielding the third family. Conversely each \(v\in N\) has fourth power zero by (P3-6); therefore \(u=v^2/2\) satisfies both equations in (P3-21). All listed images are divisible by 3, so they lift Frobenius. Uniqueness follows from \(\Phi_v(T)=3v\) and the absence of 3-torsion. Formula (P3-20) is (P3-14) substituted into (P3-19). \(\square\)

**P3.8.** The delta structures belonging to these lifts have the exact generator values
\[
\begin{aligned}
\delta_v(x)&=x^2+\frac12v^2,&
\delta_v(T)&=v-Tx(x+2),\\
\delta_\pm(x)&=x^2-1,&
\delta_\pm(T)&=\pm1-Tx(x+2),\\
\delta(c)&=(c-c^3)/3&& (c\in O).
\end{aligned}
\tag{P3-22}
\]
In particular the augmentation \(\Phi_0(x)=\Phi_0(T)=0\) is a reflection-equivariant Frobenius lift on the whole unsplit algebra, with
\[
\delta_0(x)=x^2,\qquad \delta_0(T)=-Tx(x+2).
\tag{P3-23}
\]

**Proof.** The differences \(\Phi(z)-z^3\) lie in \(3B\) by the Frobenius condition, and division by 3 is unique because \(B\) has no 3-torsion. Expanding \(\Phi(a+b)=\Phi(a)+\Phi(b)\) and \(\Phi(ab)=\Phi(a)\Phi(b)\) gives directly
\[
\delta(a+b)=\delta(a)+\delta(b)-a^2b-ab^2,
\quad
\delta(ab)=a^3\delta(b)+b^3\delta(a)+3\delta(a)\delta(b),
\]
with \(\delta(0)=\delta(1)=0\). Thus these are delta structures. Now \(x^3=-3x^2\) and \(T^3=3Tx(x+2)\), proving (P3-22). Augmentation and reflection commute on both generators, and (P3-23) is the case \(v=0\). \(\square\)

**P3.9.** The Frobenius lifts commuting with reflection are exactly
\[
\Phi_{bn_2+cn_3}\qquad(b,c\in O).
\tag{P3-24}
\]
The maps in (P3-19) that induce a Frobenius lift on \(D\) through \(\pi\) are exactly the family \(\Phi_v\); their induced maps are
\[
\Phi_D(T)=9bT,\qquad\delta_D(T)=3bT
\quad\text{for }v=an_1+bn_2+cn_3.
\tag{P3-25}
\]
Every coefficient-preserving Frobenius lift on \(D\) has the form \(T\mapsto3cT\), \(c\in O\), and it comes from a lift on \(B\) if and only if \(c\in3O\).

**Proof.** For \(\Phi_v\), commuting on \(T\) is equivalent to \(\sigma(v)=-v\). In the independent basis (P3-5), this is precisely \(2a=0\), hence \(a=0\). When it holds, \(v^2\) is fixed by reflection, so commuting on \(x\) also holds. The constant maps \(\Phi_\pm\) cannot commute on \(T\), since they send it to a nonzero fixed constant. This proves (P3-24).

The kernel of \(\pi\) is \(xB\). For \(\Phi_v\), equations (P3-11) and (P3-14) show that \(\pi\Phi_v(x)=0\); the induced value of \(T\) is \(3\pi(v)=9bT\). In contrast \(\pi\Phi_\pm(x)=-3\ne0\), so the kernel is not preserved. Since both rings have no 3-torsion, a commuting Frobenius square also commutes with the associated delta maps, proving (P3-25).

If an endomorphism of \(D\) sends \(T\) to \(a+bT\), its square-zero condition gives \(a^2=0\), so \(a=0\). Its reduction is Frobenius exactly when \(b\in3O\). By (P3-25), liftability through \(\pi\) requires \(b\in9O\), and every value \(b=9d\) is attained by choosing \(v=dn_2\). \(\square\)

## 5. The entire cotangent presentation

**P3.10.** The relative cotangent complex is the following two-term complex, in cohomological degrees \(-1,0\):
\[
L_{B/O}\simeq
\left[B e_f\oplus B e_g
\xrightarrow{J}B\,dx\oplus B\,dT\right],
\qquad
J=\begin{pmatrix}
3x(x+2)&-6(x+1)\\0&2T
\end{pmatrix}
=\begin{pmatrix}T^2&-6R\\0&2T\end{pmatrix}.
\tag{P3-26}
\]
It has no cohomology outside those degrees. Its degree \(-1\) cohomology is free over \(O\) on
\[
u_1=(n_1,0),\qquad u_2=(n_3,0),\qquad
u_3=(n_2,n_3).
\tag{P3-27}
\]
There is an explicit isomorphism of \(B\)-modules
\[
N\xrightarrow{\sim}H^{-1}(L_{B/O}),
\qquad n_1\mapsto u_1,\quad n_3\mapsto u_2,\quad n_2\mapsto u_3.
\tag{P3-28}
\]

**Proof.** In \(P=O[x,T]\), \(f\) is a nonzero divisor. The ring \(P/(f)\) is \(K[T]\), and \(g\) is monic in \(T\), so multiplication by \(g\) is injective: the leading coefficient of a nonzero polynomial remains the leading coefficient of its product with \(g\). Thus \((f,g)\) is a regular sequence. For this regular immersion, the conormal module is free on \(e_f,e_g\) and the regular-immersion cotangent description, together with the polynomial base, gives the two-term complex. Differentiation gives exactly (P3-26).

For completeness, the needed annihilators can be solved in the free basis. In \(K\),
\[
x(a+bx+cx^2)=ax+(b-3c)x^2,
\]
so \(\operatorname{ann}_K(x)=On_1\). The element \(x+2\) is a unit because its residue is 2 in the residue field; therefore \(\operatorname{ann}_K(3x(x+2))=On_1\). Writing an element of \(B\) as \(p+Tq\), the equation \(T(p+Tq)=0\) first forces \(p=0\) and then \(q\in On_1\). Consequently
\[
\operatorname{ann}_B(T)=On_3,\qquad
\operatorname{ann}_B(T^2)=On_1\oplus On_3.
\tag{P3-29}
\]
If \(J(a,b)=0\), its second coordinate gives \(b=cn_3\) for a unique \(c\in O\). Since \(Rn_3=n_3\) and \(T^2n_2=6n_3\), the first coordinate becomes \(T^2(a-cn_2)=0\). Equation (P3-29) now gives the unique expression
\[
(a,b)=Au_1+Cu_2+cu_3\qquad(A,C,c\in O).
\]
This proves (P3-27). The actions on this basis are
\[
xu_1=xu_2=0,\quad xu_3=u_2,\qquad
Tu_1=u_2,\quad Tu_2=0,\quad Tu_3=6u_1.
\]
They agree term by term with (P3-7) under the correspondence in (P3-28), proving that it is \(B\)-linear. \(\square\)

**P3.11.** The degree-zero cotangent cohomology has the following exact decomposition as an \(O\)-module:
\[
\Omega^1_{B/O}
=Oa_0\oplus Ob_0\oplus Ob_1
\oplus(O/3O)a_1\oplus(O/3O)a_2
\oplus(O/3O)a_4\oplus(O/3O)a_5
\oplus(O/3O)b_2\oplus(O/3O)c,
\tag{P3-30}
\]
where every symbol denotes the following actual form:
\[
\begin{gathered}
a_0=dx,\quad a_1=x\,dx,\quad a_2=x^2\,dx,\quad
a_3=T\,dx,\quad a_4=xT\,dx,\quad a_5=x^2T\,dx,\\
b_0=dT,\quad b_1=x\,dT,\quad b_2=x^2\,dT,\quad
c=a_3-2b_1=T\,dx-2x\,dT.
\end{gathered}
\tag{P3-31}
\]
In particular \(\Omega^1_{B/O}\simeq O^3\oplus(O/3O)^6\).

**Proof.** Before imposing relations, also put \(b_3=T\,dT\), \(b_4=xT\,dT\), \(b_5=x^2T\,dT\). Multiply \(df\) by the six basis elements (P3-3). The resulting relations are equivalent to
\[
3a_1=3a_2=3a_4=3a_5=0:
\]
the even ones are \(6a_1+3a_2=0\), \(-3a_2=0\), \(9a_2=0\); the odd ones are \(6a_4+3a_5=0\), \(-3a_5=0\), \(9a_5=0\). These equivalences use only division by the unit 2.

Multiplication of \(dg=-6(x+1)dx+2T\,dT\) by \(1,x,x^2\) then eliminates, with coefficient 1, the three symbols
\[
b_3=3(a_0+a_1),\qquad
b_4=3(a_1+a_2)=0,\qquad b_5=-6a_2=0.
\]
Its products by \(T,xT,x^2T\) give respectively
\[
3(-a_3-a_4+2b_1+b_2)=0,\quad
3(a_4+a_5+b_2)=0,\quad
6a_5+9b_2=0.
\]
With the already derived relations these are equivalent to \(3b_2=0\) and \(3(a_3-2b_1)=0\). Every generator of the original relation module has been included, and every elimination used an invertible coefficient. Replacing \(a_3\) by \(c+2b_1\) therefore gives precisely (P3-30), with no additional relations. \(\square\)

## 6. Ordinary de Rham cohomology, with representatives

Here the complex is the ordinary relative Kähler de Rham complex \(\Omega^\bullet_{B/O}\). Its calculation does not identify this complex with crystalline or prismatic cohomology.

**P3.12.** Its terms in degree at least two are
\[
\Omega^2_{B/O}=\mathbb F_3[x]/(x^3)\,w,
\qquad w=dx\wedge dT,\qquad \Omega^j_{B/O}=0\quad(j\ge3).
\tag{P3-32}
\]
The entire ordinary de Rham cohomology is
\[
\begin{aligned}
H^0_{\mathrm{dR}}(B/O)&=O\cdot1\oplus O\cdot(3x^2)
\oplus O\cdot(3x^2T),\\
H^1_{\mathrm{dR}}(B/O)&=(O/3O)[x^2dx]
\oplus(O/3O)[3x\,dT],\\
H^j_{\mathrm{dR}}(B/O)&=0\qquad(j\ge2).
\end{aligned}
\tag{P3-33}
\]
Both displayed degree-one classes are nonzero and have exact order 3.

**Proof.** Wedge the two relations in (P3-26) with \(dx,dT\). Their coefficient ideal on \(w\) is \((T^2,6R,2T)\). The elements 2 and \(R=x+1\) are units, so this ideal is \((3,T)\). Taking the quotient in (P3-4) gives (P3-32). Exterior powers of a module generated by two elements vanish in degrees at least three.

Using the direct decomposition (P3-30), the differential from the six basis vectors of \(B\) is
\[
\begin{array}{c|rrrrrr}
z&1&x&x^2&T&xT&x^2T\\ \hline
dz&0&a_0&2a_1&b_0&c+3b_1&2a_4+b_2.
\end{array}
\tag{P3-34}
\]
For \(z=p_0+p_1x+p_2x^2+q_0T+q_1xT+q_2x^2T\), the free coordinates of \(dz\) force \(p_1=q_0=q_1=0\). Its remaining torsion coordinates vanish exactly when \(p_2,q_2\in3O\), proving the first line of (P3-33).

The next differential, on the generators of (P3-30), is
\[
\begin{gathered}
da_0=db_0=da_1=da_2=dc=0,\qquad db_1=w,\\
da_4=-xw,\quad da_5=-x^2w,\quad db_2=2xw.
\end{gathered}
\tag{P3-35}
\]
For instance \(dc=d(Tdx)-2d(xdT)=-3w=0\). These formulas reach all three basis vectors \(w,xw,x^2w\) of (P3-32), proving \(H^2=0\).

Put \(u=2a_4+b_2\). Since \(w,xw,x^2w\) are independent over \(\mathbb F_3\), (P3-35) gives the full degree-one kernel as
\[
Oa_0\oplus Ob_0\oplus O(3b_1)
\oplus(O/3O)a_1\oplus(O/3O)a_2
\oplus(O/3O)c\oplus(O/3O)u.
\tag{P3-36}
\]
Indeed the coefficient of \(b_1\) must be divisible by 3; the coefficient of \(a_5\) must vanish; and the relation between the coefficients of \(a_4,b_2\) is exactly their being a multiple of \((2,1)\). Now (P3-34) says that the image from degree zero is generated by
\[
a_0,\quad b_0,\quad 2a_1,\quad c+3b_1,\quad u.
\]
After quotienting, \(a_2\) remains an independent order-three generator. If \(s=3b_1\), the other remaining summand is
\[
(Os\oplus(O/3O)c)/(s+c)\simeq(O/3O)s.
\]
This proves the second line of (P3-33), including nonvanishing and exact orders. Higher vanishing follows from (P3-32). \(\square\)

The closed degree-zero elements form an explicit order. With \(A=3x^2\) and \(E=3x^2T\), their multiplication is
\[
A^2=27A,\qquad AE=27E,\qquad E^2=243A.
\tag{P3-37}
\]
Indeed \(x^4=9x^2\) gives the first two identities, while \(x^4T^2=81x^2\) gives the last. Under the three evaluations (P3-8), \(A\) has values \((0,27,27)\) and \(E\) has values \((0,81,-81)\). Thus the degree-zero calculation keeps the original integral constants and their exact indices.

## 7. The cotangent and de Rham maps to the dual numbers

**P3.13.** The cotangent map induced by \(\pi\) is represented, in the displayed polynomial presentations, by
\[
\begin{array}{rcl}
B e_f\oplus B e_g&\longrightarrow&D e_{T^2},
\qquad(a,b)\longmapsto\pi(b)e_{T^2},\\
B\,dx\oplus B\,dT&\longrightarrow&D\,dT,
\qquad a\,dx+b\,dT\longmapsto\pi(b)\,dT,
\end{array}
\tag{P3-38}
\]
where \(L_{D/O}=[D e_{T^2}\xrightarrow{2T}D\,dT]\). It induces the zero map on \(H^{-1}\). On degree zero it sends \(b_0\mapsto dT\) and every other generator in (P3-30) to zero. The ordinary de Rham map is augmentation on \(H^0\), and both classes of \(H^1_{\mathrm{dR}}(B/O)\) have zero image.

**Proof.** The map of polynomial rings sends \(f\mapsto0\) and \(g\mapsto T^2\). Therefore its map on conormal generators is \(e_f\mapsto0,e_g\mapsto e_{T^2}\); the map on differentials is \(dx\mapsto0,dT\mapsto dT\). This proves (P3-38) and also verifies the chain-map identity directly with (P3-26). Each cycle in (P3-27) has second coordinate either 0 or \(n_3\), whose image is zero by (P3-11), proving the \(H^{-1}\) assertion. Substitution gives the claimed images in degree zero.

For \(D\), the relation is \(2T\,dT=0\). Since 2 is a unit, \(\Omega^1_{D/O}=O\,dT\), and the derivative \(a+bT\mapsto b\,dT\) is onto with kernel \(O\). Hence \(H^0_{\mathrm{dR}}(D/O)=O\) and \(H^j_{\mathrm{dR}}(D/O)=0\) for \(j>0\). Applying \(x\mapsto0\) to (P3-33) proves all de Rham assertions. \(\square\)

**P3.14.** Every Frobenius lift in (P3-19) acts as zero on \(H^1_{\mathrm{dR}}(B/O)\). For \(\Phi_v\), its action on \(H^0\) is augmentation; the actions of \(\Phi_\pm\) on the basis \(1,A,E\) of (P3-37) are
\[
(1,A,E)\longmapsto(1,27,\pm81).
\tag{P3-39}
\]

**Proof.** For \(\Phi_v\), put \(X=3v^2/2,Y=3v\). Then \(X^2=0\), so \(\Phi_v(A)=\Phi_v(E)=0\). On the two degree-one representatives its pullback gives
\[
x^2dx\longmapsto X^2dX=0,\qquad
3x\,dT\longmapsto3X\,dY
=\frac{27}{2}v^2dv=\frac92d(v^3).
\]
The last expression is exact over \(O\), since \(9/2\in O\). The constant maps kill every positive-degree differential and have the values (P3-39) by direct substitution. \(\square\)

The results above distinguish three explicit maps on the retained infinitesimal: \(N\to OT\) has image \(3OT\); the induced map on degree \(-1\) cotangent cohomology is zero; and the two nonzero ordinary de Rham classes in (P3-33) map to zero. Equations (P3-11), (P3-27), and (P3-38) prove each connecting map in the original coordinates.
