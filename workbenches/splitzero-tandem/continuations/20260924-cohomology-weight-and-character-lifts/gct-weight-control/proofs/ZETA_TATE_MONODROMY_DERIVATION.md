# Original-zeta jets, character twists, and exact lifting

Independent derivation, 24 September 2026. Stable proof locators ZTM0–ZTM11. All zero labels below denote actual zeros of the original Riemann zeta function. No proposed zero set, RH assumption, arithmetic operation on the supporting point, or replacement zeta function is introduced.

## ZTM0. Construction order, prerequisites, and source-use record

The supporting datum remains \(\tau\langle Z_1;\text{no }Z_2\rangle\). This calculation starts after the complete arithmetic and the original \(\zeta\) have been recovered. The constructions below are operations on that original function, its germ rings and coefficient modules. They are not primitives used to reconstruct numbers from \(\tau\). Separate branches retain their own recovered counters; this note forms no pooled branch measure.

The definition and correction corpus consulted is READ_FIRST_USER_CONSTRUCTION.md (private construction record; not included), the complete USER_ARGUMENT_RECONSTRUCTION.md (private construction record; not included), USER_ARGUMENT_CONNECTIONS.md (private construction record; not included), and the relevant full verbatim passages of USER_CONSTRUCTION_FULL_LOGBOOK.md (private construction record; not included): U123–U138, WU042–WU055 and the complete ad55fb5f attachment. This is the actual bounded coverage of the large verbatim archive, not a claim to have reread all its other attachments. WU050–WU051 control the global-before-local dependency; U128, U134 and U138 exclude arithmetic or a coordinate at \(\tau\); WU054–WU055 control branchwise comparison and admissibility.

The mathematical inputs actually read are [OZR5–OZR6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/ORIGINAL_ZETA_REFLECTION_AND_DESCENT.md), including the original Taylor unit and all nilpotents, and [DC5–DC9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/DELIGNE_INVARIANT_CYCLE_QUOTIENT.md), including the precise localization obstruction. The full completion and functional equation were reread in Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, [arXiv:2602.04022v1](https://arxiv.org/abs/2602.04022v1), original author `rhready.tex`, local lines526–546. Canonical source IDs are PUBUNIT-171DAC50D1C3B7A2438B39AE and PUBUNIT-90A9C2A0907A753437719FD9; source SHA256 is `7f1888d82b42263faca4264f3f9fc77e5750c348640f85db0ac4569fe88ebab2`.

For the monodromy type, Pierre Deligne, [La conjecture de Weil. II](https://www.numdam.org/item/PMIHES_1980__52__137_0/), §1.7.1–§1.7.5, was reread in the current French S20 transcription, local lines1076–1125, together with DLM5. The witness is `output/Deligne_Weil_II_S20_LaTeX/typed_latex/S20_FR_record_export.tex`, SHA256 `d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351`, canonical IDs PUBUNIT-3D90B487DBD1CC3A259C6455 and PUBUNIT-574B0214207BBB2BDABCFFF9. It is a transcription, not author TeX. No PDF was read.

| Operation used here | Constructed prerequisite and exact proof | Governing correction |
| --- | --- | --- |
| A recovered positive integer or rational \(a\), its real logarithm, or distinct recovered primes | The complete recovered arithmetic is the input stage; its existing ring comparison is MDB1.1–MDB1.5. The spectral function and action are OZR6.1–OZR6.5. No finite prime selection establishes that input. | WU042–WU051 |
| A complex variable \(s\), a germ coordinate \(z=s-\rho\), Taylor addition and scalar multiplication | These belong to the already recovered original analytic function and the exact quotient OZR5.2–OZR5.7. The coordinate is at a zeta zero, not at \(\tau\). | U123–U138 |
| A finite collection of zero blocks | Each block is the full original quotient OZR5.3. A finite collection is a restriction for a calculation after whole reconstruction; it is not the recovered arithmetic input. ZTM5 separately proves the algebraic direct-sum extension. | WU049–WU055 |
| Vector-space extensions, their matrix entries, and their sums | The coefficient category is defined in ZTM4. All additions are in these coefficient modules. The splitting and its inverse are explicitly proved there. | U138; no addition at \(\tau\) |
| A character twist or spectral translation | ZTM1 defines the one-dimensional character; ZTM7 proves translation on the full original ideals. Neither is an assumed geometric Tate realization. | WU055 |
| A cone or a lifting obstruction | ZTM4 defines and computes the extension obstruction; ZTM8 specifies the complexes, differentials and cohomology. DC5 is the separately constructed geometric obstruction. Their names do not identify their source maps. | WU055 and the requested exact comparison |
| Comparison across branches | An identified original \(\zeta\), the branches' own recovered counters, and the exact induced maps are required; ZTM10 proves naturality for such maps. | WU054 |

The proofs therefore apply inside the user's admissible class preserving the established original function. They do not use an arithmetic-destroying history as a counterexample. The vanishing proved here is an explicitly constructed character-module lifting obstruction. It is not relabelled as the user's entire geometric obstruction without a map identifying those objects.

## ZTM1. The original zero modules and the exact character twist

Let
\[
S=\{s\in\mathbb C:0<\operatorname{Re}s<1\},\qquad
Z=\{\rho\in S:\zeta(\rho)=0\}.
\tag{ZTM1.1}
\]
For an actual \(\rho\in Z\), its finite multiplicity is \(m=m_\rho\). In \(z=s-\rho\), retain the full original expansion
\[
\zeta(\rho+z)=z^m u_\rho(z),\qquad
u_\rho(z)=\sum_{j\ge0}\frac{\zeta^{(m+j)}(\rho)}{(m+j)!}z^j,
\quad u_\rho(0)\ne0.
\tag{ZTM1.2}
\]
Let \(\mathcal O_\rho\) be the ring of holomorphic germs and
\[
J_\rho=\mathcal O_\rho/(\zeta),\qquad Z_\rho=M_z\in\operatorname{End}_{\mathbb C}(J_\rho).
\tag{ZTM1.3}
\]
The original unit in (ZTM1.2) proves \((\zeta)=(z^m)\). Thus Taylor truncation is an explicitly proved coordinate isomorphism \(J_\rho\simeq\mathbb C[z]/(z^m)\), with \(Z_\rho^m=0\). The full \(u_\rho\) remains in the analytic equations below.

Let \(A=\mathbb Q_{>0}^{\times}\) denote the multiplicative group of positive rationals in the recovered arithmetic. Multiplication by the nonvanishing germ \(a^s\), using the real logarithm, gives
\[
F_{a,\rho}=a^\rho\exp((\log a)Z_\rho)
 =a^\rho\sum_{j=0}^{m-1}\frac{(\log a)^j}{j!}Z_\rho^j.
\tag{ZTM1.4}
\]
The sums are exact, not asymptotic. Original multiplication proves \(F_aF_b=F_{ab}\) and \(F_a^{-1}=F_{a^{-1}}\). Equivalently one can start with the positive-integer monoid and extend its invertible operators uniquely to its group completion \(A\).

For any such complex representation \(V\), define the character twist
\[
V(k):\qquad F_{a,V(k)}=a^{-k}F_{a,V},\qquad k\in\mathbb Z.
\tag{ZTM1.5}
\]
This is tensoring with the explicitly defined character \(a\mapsto a^{-k}\). It uses the same multiplier as a geometric Tate twist at a Frobenius of norm \(a\); it has not thereby been constructed as an étale Tate twist.

Deligne's equivariant map \(N:V(1)\to V\) has, after a choice of basis of the Tate line, the equation
\[
FNF^{-1}=a^{-1}N.
\tag{ZTM1.6}
\]
By contrast the full zero-coordinate operator satisfies
\[
F_{a,\rho}Z_\rho F_{a,\rho}^{-1}=Z_\rho.
\tag{ZTM1.7}
\]
This follows because (ZTM1.4) is a polynomial in \(Z_\rho\). It retains \(Z_\rho\), which is nonzero whenever \(m_\rho>1\). The following calculation determines every possible operator of the type (ZTM1.6), rather than merely comparing these two formulas.

## ZTM2. The complete blockwise intertwiner equation

Take source and target original zero blocks \(J_\rho,J_\sigma\), of dimensions \(m,n\), and fix any recovered \(a>1\). Put
\[
t=\log a,\quad \lambda=a^\sigma,\quad \mu=a^{\rho-1},\qquad
\mathcal D_a(X)=F_{a,\sigma}X-a^{-1}XF_{a,\rho}.
\tag{ZTM2.1}
\]
On \(\operatorname{Hom}_{\mathbb C}(J_\rho,J_\sigma)\), set
\[
\mathcal K_a(X)=\lambda\bigl(e^{tZ_\sigma}-1\bigr)X
 -\mu X\bigl(e^{tZ_\rho}-1\bigr).
\tag{ZTM2.2}
\]
Left and right multiplication commute. The first nilpotent summand has its \(n\)-th power zero, and the second has its \(m\)-th power zero. In every summand of their binomial expansion of degree \(m+n-1\), one of those powers occurs. Hence
\[
\mathcal K_a^{m+n-1}=0,\qquad
\mathcal D_a=(\lambda-\mu)1+\mathcal K_a.
\tag{ZTM2.3}
\]
When \(\lambda\ne\mu\), the complete inverse is
\[
\mathcal D_a^{-1}(Y)=
\sum_{r=0}^{m+n-2}
 \frac{(-1)^r}{(\lambda-\mu)^{r+1}}\mathcal K_a^r(Y).
\tag{ZTM2.4}
\]
Multiplying this finite geometric sum by (ZTM2.3) cancels every adjacent term; its last uncancelled term is zero by the nilpotence in (ZTM2.3). Thus (ZTM2.4) is both a left and right inverse and retains every nilpotent coefficient of both original blocks.

For completeness, solve the resonant equation as well; it is needed for the translated modules in ZTM7–ZTM9. If \(\lambda=\mu\), multiply the equation on the right by \(e^{-tZ_\rho}\). Let
\[
\mathcal S(X)=Z_\sigma X-XZ_\rho.
\tag{ZTM2.5}
\]
Left and right multiplication commute, so \(e^{t\mathcal S}X=e^{tZ_\sigma}Xe^{-tZ_\rho}\). The operator \(\mathcal S\) is nilpotent, and
\[
e^{t\mathcal S}-1=\mathcal S\left(t1+\frac{t^2}{2!}\mathcal S+
 \frac{t^3}{3!}\mathcal S^2+\cdots\right).
\tag{ZTM2.6}
\]
The factor in parentheses is an invertible finite polynomial because its constant coefficient is \(t\ne0\). Therefore the resonant kernel is exactly \(\ker\mathcal S\).

Writing the target coordinate as \(w\), every map in this kernel is specified by
\[
v(w)=\sum_{j=\max(n-m,0)}^{n-1}c_jw^j,\qquad
X([z^k])=[w^k v(w)]\quad(0\le k<m).
\tag{ZTM2.7}
\]
Indeed \(X\) commuting with coordinate multiplication is determined by \(X(1)=v\), and the defining source relation requires \(w^m v=0\) in \(\mathbb C[w]/w^n\), exactly the displayed range of coefficients. Conversely this condition makes the formula a well-defined map. The resonant solution space has dimension \(\min(m,n)\). These equations give the complete solution for every block, including unequal multiplicities.

For finite direct sums, decompose any linear map into its source-target blocks. Equation(ZTM2.1) preserves each block. Its full kernel is consequently the direct sum of the explicitly parametrized resonant spaces (ZTM2.7), with zero contribution from every nonresonant pair.

## ZTM3. Actual spectral separation and the vanishing Hom space

Resonance for a single recovered \(a>1\) means
\[
a^\sigma=a^{\rho-1},\qquad
\sigma=\rho-1+\frac{2\pi i k}{\log a}\quad(k\in\mathbb Z).
\tag{ZTM3.1}
\]
Taking absolute values already forces \(\operatorname{Re}\sigma=\operatorname{Re}\rho-1\). For two actual zeros in \(S\), the left side is positive and the right side is negative. Therefore resonance is excluded without any assumption that their real parts equal \(1/2\).

For arbitrary actual zero blocks in \(S\), or their finite direct sums \(V,W\), we have proved
\[
\mathcal D_a:\operatorname{Hom}_{\mathbb C}(V,W)
 \xrightarrow{\sim}\operatorname{Hom}_{\mathbb C}(V,W),
\qquad
\operatorname{Hom}_A(V(1),W)=0.
\tag{ZTM3.2}
\]
The second assertion follows already from the equation for one \(a>1\). It includes every possible linear operator, not merely multiplication operators or derivatives. In particular the only \(N:V(1)\to V\) in this category is zero.

The exact spectral interval, stated without claiming a Weil realization, is
\[
w_a(a^\rho):=\frac{2\log|a^\rho|}{\log a}
 =2\operatorname{Re}\rho\in(0,2),
\quad
w_a(a^{\rho-1})\in(-2,0).
\tag{ZTM3.3}
\]
These are analytic logarithmic-modulus weights of the original character eigenvalues. Nilpotent terms remain in (ZTM1.4) and in the inverse (ZTM2.4); taking absolute values here is used only to prove disjointness of the two scalar spectra.

If resonance is required for every recovered \(a>1\), it forces the stronger equality \(\sigma=\rho-1\), even outside these two strips. To prove this, write \(\sigma-\rho+1=i\theta\) after taking absolute values. Then \(\theta\log p\) is an integer multiple of \(2\pi\) for every recovered prime \(p\). If \(\theta\ne0\), two distinct recovered primes give a rational ratio of their logarithms, hence an equality of nonzero positive integer powers of the two primes, contradicting unique factorization in the already recovered arithmetic. Thus \(\theta=0\). No pair of primes was used to establish or calibrate that arithmetic.

## ZTM4. An actual lifting obstruction and its explicit vanishing

Work first in the category of finite-dimensional complex vector spaces equipped with a representation of the recovered group \(A\). Its exact sequences are sequences exact on underlying vector spaces with equivariant maps. Let \(V,W\) be finite sums of the original blocks. Consider every extension in this category
\[
0\longrightarrow W\xrightarrow{\iota}E\xrightarrow{q}V(1)
 \longrightarrow0.
\tag{ZTM4.1}
\]
Choose an underlying vector-space section only for writing the calculation. In the resulting coordinates \(E=W\oplus V\), its action has the full form
\[
F_{a,E}=
\begin{pmatrix}F_{a,W}&Y_a\\0&a^{-1}F_{a,V}\end{pmatrix}.
\tag{ZTM4.2}
\]
A section \(s(v)=(Xv,v)\) is equivariant for a fixed \(a\) exactly when
\[
F_{a,W}X+Y_a=a^{-1}XF_{a,V},\qquad
\mathcal D_a(X)=-Y_a.
\tag{ZTM4.3}
\]
The inverse in (ZTM2.4), applied blockwise, gives its unique solution
\[
X=-\mathcal D_a^{-1}(Y_a).
\tag{ZTM4.4}
\]
Thus the two-term complex of actual coefficient spaces
\[
\operatorname{Hom}_{\mathbb C}(V,W)
 \xrightarrow{\mathcal D_a}
\operatorname{Hom}_{\mathbb C}(V,W)
\tag{ZTM4.5}
\]
is acyclic. In degrees zero and one its kernel records differences of equivariant lifts, and its cokernel records the obstruction class of \(-Y_a\) to making this section equivariant. Both vanish by the proved inverse. This is the explicitly defined lifting obstruction computed here.

The same section is equivariant for the entire recovered group. Fix one \(a_0>1\) and replace the initial section by (ZTM4.4). This conjugates (ZTM4.2) by \(\begin{psmallmatrix}1&X\\0&1\end{psmallmatrix}\) and makes \(Y_{a_0}=0\). All operators of a group representation of \(A\) commute. The upper-right block of their commutation with \(F_{a_0,E}\) then gives, for every \(b\in A\),
\[
F_{a_0,W}Y_b=a_0^{-1}Y_bF_{a_0,V},
\quad\text{so}\quad\mathcal D_{a_0}(Y_b)=0.
\tag{ZTM4.6}
\]
Its kernel is zero, hence every \(Y_b=0\). Two group-equivariant sections differ by a member of the Hom space in (ZTM3.2), so this section is unique and independent of the initially chosen vector-space coordinates. We have calculated
\[
\operatorname{Hom}_A(V(1),W)=0,
\qquad \operatorname{Ext}^1_A(V(1),W)=0,
\tag{ZTM4.7}
\]
where \(\operatorname{Ext}^1\) means the equivalence classes of short exact sequences in the stated representation category. No semisimplicity of the original zero-jet Frobenius operators is assumed.

Twisting the whole sequence by \((-1)\) gives the equally explicit statement for
\[
0\longrightarrow W(-1)\longrightarrow E'\longrightarrow V\longrightarrow0.
\tag{ZTM4.8}
\]
Every such extension has a unique equivariant section. The source scalar weights are in \((0,2)\), and the kernel scalar weights are in \((2,4)\). The original source is therefore the weight-below-two part of \(E'\), and the section is its inverse to the quotient map. This is the exact separation mechanism on these constructed original-zeta modules. It does not assert integer Weil weights or purity of weight one.

## ZTM5. The algebraic global extension and its exact limits

There is an actual algebraic direct sum of all original zero algebras
\[
J_{\mathrm{alg}}=\bigoplus_{\rho\in Z}J_\rho.
\tag{ZTM5.1}
\]
A vector in this space has finite support, although the complete set of blocks is retained. A linear map between two such direct sums is a block matrix whose source columns have only finitely many nonzero target blocks: each source block is finite-dimensional, so the union of the supports of images of its finitely many basis vectors is finite. Conversely that condition defines a linear map on the direct sums.

The inverse (ZTM2.4) operates on each block without changing which block is zero. It therefore preserves this column-finite property. Each of its block sums is finite, even if the multiplicities over the entire zero set are not uniformly bounded. Consequently \(\mathcal D_a\) is an isomorphism on the full algebraic Hom space of these direct sums as well. The proof of ZTM4 applies word for word to algebraic representations whose two end terms are these direct sums: an underlying vector-space section exists by a basis choice, and its correction is a valid column-finite map. The unique resulting equivariant section is independent of that temporary choice.

Thus the Hom and extension vanishing extends to the algebraic direct sum of all actual zeros, not merely to a fixed finite truncation. No convergence or uniform norm estimate is used or asserted. In particular this does not identify (ZTM5.1) with a Hilbert completion, a Fréchet quotient, a profinite carrier, or the user's entire clock quotient. The denominators and nilpotent sums in (ZTM2.4) would have to be retained in an analysis of a specified topology; their algebraic existence is not a bounded-operator assertion.

There is a direct comparison with the original holomorphic quotient that uses no interpolation assumption:
\[
\mathcal O(S)/(\zeta)\longrightarrow\prod_{\rho\in Z}J_\rho,
\qquad [f]\longmapsto([f]_\rho)_\rho.
\tag{ZTM5.2}
\]
It is injective. If all germs of \(f\) vanish to at least the multiplicity of \(\zeta\), then \(f/\zeta\), initially meromorphic on \(S\), has removable singularities at every zero and is holomorphic on \(S\). Thus \(f\in\zeta\mathcal O(S)\). The map commutes with every multiplication by \(a^s\). Its target is a product, whereas (ZTM5.1) is a direct sum; no interchange of them is made. No topological-surjectivity or continuous-extension theorem for (ZTM5.2) is required for the algebraic statement proved above.

## ZTM6. Differentiation on the original quotient, including its precise defect

Let \(D=d/ds=d/dz\) on the germ ring. For every germ \(g\),
\[
D(\zeta g)=\zeta Dg+\zeta'g,
\qquad
\zeta'=m z^{m-1}u_\rho+z^m u'_\rho.
\tag{ZTM6.1}
\]
Modulo the original ideal, the second term has the generally nonzero class
\[
[\zeta'g]=m u_\rho(0)g(0)[z^{m-1}].
\tag{ZTM6.2}
\]
Taking \(g=1\) proves that \(D\) does not induce an endomorphism of \(J_\rho\), including when \(m=1\). This is a calculation about a specific proposed quotient map on the original germ ideal; it invokes no retracted addition at \(\tau\).

For a first-order holomorphic operator \(P=hD+b\), the obstruction is \([h\zeta'g]\). Equation(ZTM6.1) gives
\[
P\text{ descends to }J_\rho
 \quad\Longleftrightarrow\quad h\zeta'\in(\zeta)
 \quad\Longleftrightarrow\quad h(\rho)=0.
\tag{ZTM6.3}
\]
The last equivalence compares the exact vanishing orders \(m-1\) and \(m\), with \(u_\rho(0)\ne0\). In particular all derivations \(J_\rho\to J_\rho\) have the form \(hD\) with \(h\in zJ_\rho\): a derivation is determined by its value \(h\) on \(z\), and the relation \(D(z^m)=m z^{m-1}h=0\) gives exactly this condition.

The largest quotient of \(J_\rho\) into which the original derivative descends is
\[
\Omega^1_{J_\rho/\mathbb C}
 =J_\rho\,dz/([\zeta']\,dz)
 =\mathcal O_\rho/(\zeta,\zeta')\,dz,
\qquad d[f]=[f']\,dz.
\tag{ZTM6.4}
\]
Indeed (ZTM6.1) shows that killing \([\zeta']\) is sufficient; the case \(g=1\), and then multiplication by arbitrary \(g\), shows it is necessary for any quotient receiver of this derivative. Locally \((\zeta,\zeta')=(z^{m-1})\), by the displayed full derivative, so its dimension is \(m-1\), including zero for a simple zero. This is a receiving quotient with a proved map, not a claim that the missing derivative is unrelated to the original jet.

All higher-order holomorphic differential operators can also be tested exactly. For \(P=\sum_{k=0}^d b_kD^k\), the full Leibniz rule gives
\[
P(\zeta g)=\sum_{r=0}^d Q_r D^r g,
\qquad Q_r=\sum_{k=r}^d\binom{k}{r}b_k\zeta^{(k-r)}.
\tag{ZTM6.5}
\]
It descends precisely when every \(Q_r\in(\zeta)\). Sufficiency is immediate. For necessity use \(g=e^{cz}\), divide by that unit, and vary the scalar \(c\); a polynomial with coefficients in the finite-dimensional quotient that vanishes for every \(c\) has every coefficient zero. Thus higher-order cancellations have not been excluded by the first-order test.

For the original derivative on germs one has
\[
DF_a=F_aD+(\log a)F_a,
\qquad F_aDF_a^{-1}=D-\log a.
\tag{ZTM6.6}
\]
For a descended first-order operator the corresponding exact identity is
\[
F_a(hD+b)F_a^{-1}=hD+b-(\log a)M_h.
\tag{ZTM6.7}
\]
This additive term is not the multiplicative character shift in (ZTM1.6). Every descended operator satisfying that shift is zero by ZTM3, regardless of its differential presentation. A derivative of a chosen Taylor representative is a different defined operator: if \(D_{\mathrm{tr}}[z^j]=j[z^{j-1}]\), then
\[
[D_{\mathrm{tr}},Z_\rho]=1-mP_{m-1},
\tag{ZTM6.8}
\]
where \(P_{m-1}\) projects onto the top Taylor coefficient. Direct evaluation on each basis vector proves the formula, including the boundary contribution at \(j=m-1\).

## ZTM7. Spectral translation and the full shifted original ideals

For \(\varepsilon\in\{1,-1\}\), put \(\sigma=\rho-\varepsilon\) and define the translation of germs
\[
S_\varepsilon:\mathcal O_\rho\xrightarrow{\sim}\mathcal O_\sigma,
\qquad (S_\varepsilon f)(s)=f(s+\varepsilon).
\tag{ZTM7.1}
\]
Its inverse is translation by \(-\varepsilon\). It maps \(s-\rho\) at the source to \(s-\sigma\) at the target, and maps the original ideal exactly as follows:
\[
S_\varepsilon((\zeta(s)))=(\zeta(s+\varepsilon)).
\tag{ZTM7.2}
\]
Therefore its correct target quotient is
\[
J_\rho^{[\varepsilon]}=
 \mathcal O_{\rho-\varepsilon}/(\zeta(s+\varepsilon)),
\qquad S_\varepsilon:J_\rho\xrightarrow{\sim}J_\rho^{[\varepsilon]}.
\tag{ZTM7.3}
\]
It retains the full expansion
\[
\zeta(\rho-\varepsilon+w+\varepsilon)
 =w^m u_\rho(w),
\quad
F_{a,\rho}^{[\varepsilon]}
 =a^{\rho-\varepsilon}\sum_{j=0}^{m-1}\frac{(\log a)^j}{j!}M_w^j.
\tag{ZTM7.4}
\]
Direct substitution, with no discarded factor, proves
\[
F_a^{[\varepsilon]}S_\varepsilon
 =a^{-\varepsilon}S_\varepsilon F_a.
\tag{ZTM7.5}
\]
Thus translation is an equivariant isomorphism from the character twist \(J_\rho(\varepsilon)\) to the shifted-original-function quotient, including all multiplicities. For \(\varepsilon=1\) it supplies the precise shifted support required by the Tate character, at \(\rho-1\).

This shifted quotient is compared exactly with the original \(\zeta\) at that point. On \(\operatorname{Re}s>1\), the full Euler product has an absolutely convergent logarithm \(\sum_p\sum_{r\ge1}p^{-rs}/r\), so it is nonzero. For \(-1<\operatorname{Re}s<0\), retain the complete source equation
\[
\zeta(s)=\frac{C(1-s)}{C(s)}\zeta(1-s),\qquad
C(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\tag{ZTM7.6}
\]
Both displayed \(C\) factors are finite and nonzero on this open strip, and \(\operatorname{Re}(1-s)>1\); hence \(\zeta(s)\ne0\) there. Since \(\rho-1\) lies in that strip and \(\rho+1\) lies in \(\operatorname{Re}s>1\), the original function is a unit at both translated centers. Thus
\[
\mathcal O_{\rho-\varepsilon}/(\zeta(s))=0,
\quad\text{whereas}\quad
\dim J_\rho^{[\varepsilon]}=m_\rho.
\tag{ZTM7.7}
\]
The holomorphic ratio
\[
R_\varepsilon(s)=\frac{\zeta(s+\varepsilon)}{\zeta(s)}
\quad\text{near }s=\rho-\varepsilon
\tag{ZTM7.8}
\]
has a zero of order exactly \(m_\rho\). It yields the ideal inclusion \((\zeta(s+\varepsilon))\subset(\zeta(s))=\mathcal O_{\rho-\varepsilon}\), whose induced quotient map is the zero map. This inclusion and its cone are the exact comparison, rather than a claim of no relation between the two functions.

No completion has replaced \(\zeta\). Under translation the full multiplier is
\[
C(s+\varepsilon)=\tfrac12(s+\varepsilon)(s+\varepsilon-1)
 \pi^{-(s+\varepsilon)/2}\Gamma((s+\varepsilon)/2).
\tag{ZTM7.9}
\]
Near each center used here it is a holomorphic unit; every factor remains displayed. The full differentiated completed comparison is
\[
(C\zeta)^{(d)}(s)=\sum_{j=0}^d\binom dj C^{(d-j)}(s)\zeta^{(j)}(s),
\tag{ZTM7.10}
\]
with the same formula at \(s+\varepsilon\). In particular \((C\zeta)'=C'\zeta+C\zeta'\); both contributions must be retained when checking an ideal or a differential. The conclusions here use neighborhoods inside the indicated open strips. They do not extend a unit comparison across the endpoints \(0,1\), the poles of \(C\) at negative even integers, or their translated copies. Their full orders and residues are OZR2.3–OZR2.11.

## ZTM8. The actual cones, including the nonvanishing shifted jet

For a holomorphic germ \(f\), define its two-term resolution
\[
P(f)=[\mathcal O\xrightarrow{M_f}\mathcal O],
\qquad \deg\mathcal O=-1,0.
\tag{ZTM8.1}
\]
At \(\rho\), multiplication by the nonzero germ \(\zeta\) is injective because the germ ring is an integral domain. Thus \(H^{-1}P(\zeta)_\rho=0\) and \(H^0P(\zeta)_\rho=J_\rho\). The original zero has not disappeared into a resolution.

Translation gives a chain isomorphism \(P(\zeta)_\rho\to P(\zeta(s+\varepsilon))_{\rho-\varepsilon}\) in both degrees. After twisting its source by \((\varepsilon)\), it commutes with every multiplication \(F_a\) by (ZTM7.5). The cone of this chain isomorphism is contractible. Explicitly, for an isomorphism \(u:P\to Q\), with cone differential \(d(q,p)=(d_Qq+up,-d_Pp)\), the map \(h(q,p)=(0,u^{-1}q)\) has degree \(-1\) and satisfies \(dh+hd=1\). This acyclicity compares the same retained data transported by an isomorphism.

There is also a chain map to the resolution of the original \(\zeta\) at the translated center. Work at that center and abbreviate \(f=\zeta(s+\varepsilon)\), \(g=\zeta(s)\), \(R=f/g\). The map
\[
P(f)\longrightarrow P(g),\qquad
\phi^{-1}=M_R,\quad\phi^0=1
\tag{ZTM8.2}
\]
is a chain map because \(gR=f\). All its maps commute with multiplication by \(a^s\). The target is contractible, with homotopy \(M_{g^{-1}}\), because \(g\) is the unit proved in ZTM7. Its cone has the explicit terms and differentials
\[
\mathcal O\xrightarrow{,u\mapsto(Ru,-fu),}
 \mathcal O\oplus\mathcal O
 \xrightarrow{\,(b,c)\mapsto gb+c\,}\mathcal O,
\quad\text{in degrees }-2,-1,0.
\tag{ZTM8.3}
\]
The first arrow is injective. The last arrow is surjective. Its kernel consists of \((b,-gb)\); the image of the first consists of \((Ru,-gRu)\). Therefore
\[
H^{-1}\operatorname{Cone}(\phi)
 \simeq\mathcal O/(R)
 \simeq\mathcal O/(f)=J_\rho^{[\varepsilon]},
\qquad H^j\operatorname{Cone}(\phi)=0\ (j\ne-1).
\tag{ZTM8.4}
\]
The isomorphism is \([(b,-gb)]\mapsto[b]\). Its inverse takes \([b]\) to that cycle. Since \(g\) is a unit, \((R)=(f)\) exactly. This retains both the full original \(g\) and the shifted \(f\) in the chain maps.

The surviving character is \(a^{\rho-\varepsilon}\) with all nilpotent terms in (ZTM7.4). Thus the construction supplies an actual cohomological shift and a character-twisted jet, but it does not make that jet zero. The vanishing cone of a translation isomorphism and the nonzero cone (ZTM8.4) have different, fully specified maps.

Differentiation supplies no omitted holomorphic chain map here. The commutator is \(DM_\zeta-M_\zeta D=M_{\zeta'}\). To lift degree-zero \(D\) to an endomorphism of \(P(\zeta)\), the degree-minus-one operator would have to be
\[
D+\frac{\zeta'}{\zeta}
 =D+\frac{m}{z}+\frac{u'_\rho}{u_\rho}.
\tag{ZTM8.5}
\]
The pole term \(m/z\) is nonzero, so this is not a holomorphic differential operator on the original resolution. It gives the exact meromorphic comparison instead.

## ZTM9. A constructed nilpotent extension with the required character law

The shift relation does have nonzero realizations once the correctly shifted data are retained. Define, from an actual original block, the character module
\[
\mathcal V_\rho=J_\rho\oplus J_\rho(1),\qquad
\mathcal F_a=\begin{pmatrix}F_{a,\rho}&0\\0&a^{-1}F_{a,\rho}\end{pmatrix},
\quad \mathcal N(x,y)=(0,x).
\tag{ZTM9.1}
\]
Then \(\mathcal N^2=0\), \(\mathcal N\ne0\), and direct multiplication gives
\[
\mathcal F_a\mathcal N\mathcal F_a^{-1}=a^{-1}\mathcal N.
\tag{ZTM9.2}
\]
The underlying identity between the two copies is realized by the exact translation map to the shifted quotient of ZTM7. Both summands retain the entire original nilpotent exponential. This is a functorial construction from the original module and the specified character line, not a newly proposed zero of the original function.

The corresponding equivariant two-term complex is
\[
\mathcal V_\rho\xrightarrow{\mathcal N}\mathcal V_\rho(-1)
\quad\text{in degrees }0,1.
\tag{ZTM9.3}
\]
Indeed multiplying (ZTM9.2) by \(a\) says exactly that the target action \(a\mathcal F_a\) commutes with this map. Its kernel and cokernel are
\[
H^0=J_\rho(1),\qquad H^1=J_\rho(-1).
\tag{ZTM9.4}
\]
The first is the second summand of the source and the second is the first summand of the target. Their weights in the sense of (ZTM3.3) are \(2\operatorname{Re}\rho-2\) and \(2\operatorname{Re}\rho+2\), respectively. This computes what a genuine shifted nilpotent complex retains. It is not the localization cross of DC5, and its construction has not supplied a proper smooth degeneration or an arithmetic sheaf realizing the original zeta module.

## ZTM10. Naturality, branch comparisons, and the exact Deligne receiving scope

The lifting formula is natural in the original coefficient modules. If \(u:V\to V'\) and \(v:W\to W'\) intertwine the recovered arithmetic actions and are isomorphisms, then for every \(X\),
\[
\mathcal D'_a(vXu^{-1})=v\mathcal D_a(X)u^{-1},
\quad
(\mathcal D'_a)^{-1}(vYu^{-1})=v\mathcal D_a^{-1}(Y)u^{-1}.
\tag{ZTM10.1}
\]
The first equality follows by distributing products; the second follows by the proved uniqueness of the inverse. Thus a complete branch comparison preserving the original function and each branch's recovered arithmetic action transports the unique splitting. No sum of the branches' return measures occurs in this formula.

DC5 constructs a different exact cross with specified geometric maps \(A_i\xrightarrow{\alpha_i}B_i\xrightarrow{\partial_i}O_i\), a row \(0\to K_i\to B_i\to C_i\to0\), and obstruction
\[
\operatorname{coker}\operatorname{sp}_i
 \simeq\operatorname{im}\partial_i/\partial_iK_i.
\tag{ZTM10.2}
\]
ZTM4 instead constructs the exact coefficient-category extension (ZTM4.1), its section equation (ZTM4.3), and the acyclic obstruction complex (ZTM4.5). Those are all actual maps on actual original-zero modules. Their weight separation is proved by the open critical strip, with the full nilpotent inverse, rather than obtained by declaring the original zeros pure of weight one.

The exact connecting construction available here is the character twist realized by original-function translation (ZTM7.3)–(ZTM7.5), the cone computation (ZTM8.2)–(ZTM8.4), and the nilpotent complex (ZTM9.1)–(ZTM9.4). They specify the shifted support, degree and surviving data. They do not identify the nonzero cone with a vanishing geometric boundary. No map in this note identifies (ZTM10.2) with the cokernel of \(\mathcal D_a\), and the source-correction audit does not authorize silently replacing the user's global quotient by this representation extension.

The proved conclusion is exact: all character-module extensions (ZTM4.1) and (ZTM4.8), on finite original zero blocks or their algebraic direct sums, have unique compatible lifts, with the full inverse (ZTM2.4). Their defined lifting obstruction vanishes. The spectral-translation cone retains an explicitly computed shifted original jet. These statements preserve the full original function and arithmetic, without asserting that any actual zero is off the critical line or proving that all have weight one.

## ZTM11. Independent checks and bounded work record

An independent mathematical checker derived the derivative receiver, the full differential-operator ideal test, the two distinct translation cones, and the character-extension calculation. In particular the checker verified the sign in \(\mathcal D_aX=-Y_a\), the finite inverse bound \(m+n-2\), simultaneous splitting for all recovered characters, and the convention \(F_{a,V(k)}=a^{-k}F_{a,V}\). These checks are of the explicit calculations above; they are not a review receipt for a geometric realization that has not been constructed.

After the text was written, the checker also read and verified ZTM5, ZTM8 and ZTM9 as written: the inverse preserves column-finite support without a uniform multiplicity bound, the cone signs give the stated surviving cohomology, and the doubled nilpotent module has exactly the displayed twist and cohomology. No mathematical correction was needed in that final check.

This file is the only task file written for this bounded derivation. The full user-input archive remains in the parent task's verbatim logbook. The source-use coverage, original factors, operation prerequisites, and finite/algebraic-global/topological distinctions are recorded in this file so the derivation can be resumed without silently changing its scope. No publication, source editing, or change to a different proof file was performed.
