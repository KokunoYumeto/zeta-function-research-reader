---
title: "Identity Absorber Square: a Split-Zero coefficient branch"
date: "21 September 2026"
---

# 1. The object and the name

The starting coefficient object is exactly
\[
S=G(\mathbb Z)=\mathbb Z\sqcup\{\tau\},\qquad
\tau+x=x,\qquad \tau x=\tau\quad(x\in S).
\]
Its supported integer zero is \(e=0_{\mathbb Z}\), with \(e\ne\tau\) and \(n+(-n)=e\).
The original integer sums and products are retained. The construction is the one in the originating programme source [1], not a replacement of its unsupported element by integer zero.

For an operation, an identity leaves its other argument unchanged; an absorber makes the output equal to itself. Choosing independently for addition and multiplication gives the four defining roles:

| Distinguished element | Addition | Multiplication |
|---|---|---|
| \(\tau\) | \(\tau+x=x\) | \(\tau x=\tau\) |
| \(\varepsilon\) | \(\varepsilon+x=x\) | \(\varepsilon x=x\) |
| \(u\) | \(u+x=u\) | \(ux=x\) |
| \(\Omega\) | \(\Omega+x=\Omega\) | \(\Omega x=\Omega\) |

The domains of \(x\), preservation of old identities, and forced quotients are part of each construction; Theorem Z1 of [3] states them in full. For example, literal \(\Omega\) adjoined to \(S\) satisfies \(\tau\Omega=\Omega\), so \(\tau\) is not a global multiplicative absorber in that larger algebra.

The name chosen for this branch is **Identity Absorber Square**. In standard algebraic language, the work studies adjunctions of identity and absorbing elements to algebras with two commutative monoid operations and distributive multiplication. The literal \(\Omega\)-extension need not satisfy the global zero-annihilation axiom in the usual definition of a semiring. The name **absolute element square** can designate this particular research construction; no claim is made that it is an established technical term or that “absolute” identifies it with absolute prismatic cohomology.

# 2. The precise coefficient relation

Let \(N=\mathbb Z\setminus\{0\}\) with integer multiplication, and let \(\Lambda=\mathbb Z[N]\). Theorem Z7 of [3] proves, with explicit inverses,
\[
\Gamma(S)=\mathbb Z[S]/([\tau])
\cong\mathbb Z\times\Lambda,\qquad
[e]\longmapsto(1,0),\quad
[n]\longmapsto(1,[n])\ (n\ne0).
\tag{C1}
\]
The first projection is induced by the original support character
\(\chi(\tau)=0,\chi(n)=1\); the second is induced by the arithmetic monoid map
\(a(\tau)=e,\ a(n)=n\). Its codomain before base extension is the multiplicative integer monoid whose absorber is \(e\). Thus the second factor is the formal monoid ring \(\Lambda\), not yet the ordinary arithmetic ring.

Evaluation
\[
\operatorname{ev}:\Lambda\longrightarrow\mathbb Z,\qquad
\sum a_n[n]\longmapsto\sum a_nn
\]
is a unital ring homomorphism. The quotient which imposes every original additive relation is
\[
\mathbb Z\times\Lambda\longrightarrow\mathbb Z,\qquad
(k,v)\longmapsto\operatorname{ev}(v).
\tag{C2}
\]
Its kernel is \(\mathbb Z\times\ker(\operatorname{ev})\), exactly as proved in (Z49). In particular, the relation \(e+e=e\) kills the idempotent \([e]=(1,0)\). This is a statement about the specified quotient; it does not identify \(e\) and \(\tau\) in \(S\).

Fix a prime \(p\), write \(\widehat\Lambda=\varprojlim_r\Lambda/p^r\Lambda\), and let
\[
B_S=\mathbb Z_p\times\widehat\Lambda,\qquad
E=(1,0),\qquad F=1-E=(0,1).
\tag{C3}
\]
The prismatic comparison [4] constructs the canonical Frobenius on this ring and a second explicit Frobenius compatible with (C2). Both fix \(E,F\); the simultaneous conjugate family in Theorem P5 does so as well. The next statement records exactly what the retained idempotents do to coefficient complexes.

**Theorem C1 (modules, differentials and Frobenius preserve the two factors).**
The maps
\[
M\longrightarrow EM\times FM,\quad m\longmapsto(Em,Fm),
\qquad
EM\times FM\longrightarrow M,\quad(x,y)\longmapsto x+y
\tag{C4}
\]
are inverse natural isomorphisms for every unital \(B_S\)-module \(M\).
They give an equivalence of categories
\[
B_S\text{-}\mathrm{Mod}\ \cong\
\mathbb Z_p\text{-}\mathrm{Mod}\times
\widehat\Lambda\text{-}\mathrm{Mod}.
\tag{C5}
\]
For every cochain complex \(K^\bullet\) of \(B_S\)-modules, with no boundedness assumption, these maps are an isomorphism of complexes and induce
\[
H^i(K^\bullet)\cong
H^i(EK^\bullet)\times H^i(FK^\bullet)
\quad(i\in\mathbb Z).
\tag{C6}
\]
If \(\Phi:M\to M\) is semilinear for either of the two specified Frobenius lifts, then \(\Phi\) preserves both factors.

**Proof.** Direct multiplication gives \(E^2=E\), \(F^2=F\), \(EF=FE=0\) and \(E+F=1\). Hence the second map in (C4) composed with the first is \(m\mapsto(E+F)m=m\). Conversely \(E(x+y)=x\) and \(F(x+y)=y\) for \(x\in EM,y\in FM\), proving the other composite is the identity. The action on \(EM\) factors through \(B_SE\cong\mathbb Z_p\), and that on \(FM\) through \(B_SF\cong\widehat\Lambda\). Given modules \(U,V\) over these two rings, coordinatewise action makes \(U\times V\) a \(B_S\)-module with factors \(U,V\). A \(B_S\)-linear map commutes with \(E,F\); conversely a pair of maps on the factors gives a unique \(B_S\)-linear map. These constructions prove the category equivalence including morphisms.

Every differential is \(B_S\)-linear, so it commutes with \(E,F\), and (C4) is an isomorphism of complexes. In each degree, its kernel is the product of the two kernels, and its image is the product of the two images: for the latter, any pair \(d_E x,d_F y\) is the differential of \((x,y)\). The quotient of these kernels by these images is the product of the two quotients, proving (C6). Finally
\(\Phi(Em)=\phi(E)\Phi(m)=E\Phi(m)\), and the identical calculation holds for \(F\). This proves the last assertion. \(\square\)

For the literal extension \(H=S\sqcup\{\Omega\}\), Theorem Z7 gives
\(B_H=\mathbb Z_p\times\mathbb Z_p\times\widehat\Lambda\).
Its orthogonal idempotents are, in the original basis,
\[
[\tau],\qquad [e]-[\tau],\qquad [1]-[e].
\tag{C7}
\]
Their coordinates are respectively \((1,0,0),(0,1,0),(0,0,1)\); thus they are orthogonal, sum to \(1\), and are fixed by the two stated Frobenius lifts. Repeating the explicit maps (C4) with three coordinates proves the corresponding three-factor equivalence and cohomology decomposition. The proof requires no identification of \(\tau\) with \(e\).

Theorem C1 concerns complexes over the constructed monoid rings. It does not assert an equivalence between those modules and the original Split-Zero semimodules, nor does it identify an existing programme complex with absolute prismatic cohomology. Its content is a proved coefficient decomposition and its exact behavior under differentials and Frobenius.

# 3. Why multiplication cannot select the original addition

**Theorem C2 (two additions with the same specified multiplication).**
There are two ring additions on the set \(\mathbb Z\), with the same integer multiplication, the same \(0,1,-1\), and the same multiplicative support information, for which the sum of \(1\) with itself is respectively \(2\) and \(3\). Each extends to a Split-Zero structure on the same set \(S\), with the same multiplication and the same unsupported element \(\tau\).

**Proof.** Every nonzero integer has a unique expression
\(n=2^r3^s m\), where \(r,s\ge0\) and \(m\) is an integer divisible by neither \(2\) nor \(3\). Existence follows by repeatedly dividing by \(2\) and \(3\), which strictly decreases the positive absolute value until the process stops. Uniqueness follows by cancellation and the fact that \(2\) does not divide an odd integer and \(3\) does not divide a product of integers not divisible by \(3\); the latter fact follows directly from the two nonzero residue classes modulo \(3\).
Define
\[
f(0)=0,\qquad f(2^r3^s m)=2^s3^r m.
\]
Then \(f^2=\mathrm{id}\). Exponents add on products, and the product of two remaining factors is still divisible by neither \(2\) nor \(3\). Hence \(f(xy)=f(x)f(y)\) for nonzero \(x,y\); the zero cases follow from \(f(0)=0\). Also \(f(1)=1\) and \(f(-1)=-1\).

Define
\[
x\boxplus y=f^{-1}(f(x)+f(y)).
\tag{C8}
\]
For associativity, applying the injective map \(f\) to either parenthesized three-term sum gives \(f(x)+f(y)+f(z)\). Commutativity follows in the same way. Zero is the identity, and the inverse of \(x\) is \(f^{-1}(-f(x))\). To verify distributivity, apply \(f\):
\[
f\bigl(x(y\boxplus z)\bigr)
=f(x)(f(y)+f(z))
=f(xy)+f(xz)
=f(xy\boxplus xz).
\]
The other distributive law follows by commutativity of multiplication. The original unit \(1\) is unchanged. These checks prove the ring axioms with the unchanged multiplication. But \(1\boxplus1=f^{-1}(2)=3\), whereas \(1+1=2\).

Extend \(f\) by \(f(\tau)=\tau\) and extend \(\boxplus\) by making \(\tau\) its identity. This is transport of the whole original Split-Zero structure under the multiplicative bijection \(f\), so all its identities and distributive laws follow from the corresponding identities already checked, including cases involving \(\tau\). Both structures have the same multiplication and the same support character. Thus those data alone do not select which displayed element is the sum \(1+1\). \(\square\)

The two rings are isomorphic through \(f\); the theorem proves a failure of *canonical recovery on the specified underlying multiplicative object*. It does not claim that the two rings are unrelated. The corrected Frobenius in [4] imports the chosen integer values into its coefficients. This explains why it is a valid positive bridge but not a construction of integer addition from multiplication alone.

# 4. Position in the programme

This is an algebraic branch of Split Zero: its starting object, support map and arithmetic projection are the programme's original ones. The four-corner and order calculations determine which arithmetic and support data survive each adjoining construction. The monoid-ring calculations then connect those exact objects to familiar coefficient rings and bounded crystalline prisms. The user proposed the four-role framing and suggested investigating the prismatic connection; the local derivations supply the stated proofs. Historical novelty is not asserted.

The prismatic literature does not define a prism by multiplication alone. Its \(\delta\)-ring already includes addition, and the absolute site varies bounded prisms without a fixed base prism. Theorems P1–P5 of [4] calculate objects and maps in that setting. They neither solve a stated open problem in absolute prismatic cohomology nor establish an equivalence with the programme's analytic cohomology.

# References and complete proof sources

[1] HI-AI, *An Algebraic Structure Incorporating a Z/1Z-Symmetric Element Adjoined to the Integers: Construction, Analysis, and Generalizations*, Zenodo 17555345, original 11.tex, Section 3 and the arbitrary-ring construction. See the preserved original [source](sources/17555345_11.tex), lines 578–749 and 1524–1577.

[2] HI-AI, *An Examination of Semiring Structures Derived from the Integers by Sequential Adjunction of Identity and Absorbing Elements*, Zenodo 17547186, original 5.tex, literal \(\Omega\) construction. See the preserved original [source](sources/17547186_5.tex), lines 1288–1360.

[3] [Four corners over the integers](FOUR_CORNERS_OVER_Z.md), Theorems Z1–Z8. All definitions, receiver maps, comparisons and product coordinates used above are fully proved there.

[4] [Prismatic comparison](PRISMATIC_COMPARISON.md), with original human sources and the full local construction.


## Retained cohomology and Frobenius

The [chain comparison](CHAIN_COMPARISON.md), Theorems Q1–Q4, propagates these coefficient maps to supported cohomology and calculates the additive-relation kernel. The [homotopy-defect construction](HOMOTOPY_DEFECT.md) proves the exact retained summand for a contractible input and its coefficient extensions. In the integer example the [Frobenius cross-effect](FROBENIUS_CROSS_EFFECT.md), Theorems F1–F3, is the mixed Laurent ideal: it has a specified Frobenius-semilinear map, a completely calculated linearization cokernel, and a delta-stable ideal defining an actual quotient of crystalline prisms. Thus these later proofs construct additional maps on the retained classes themselves.
