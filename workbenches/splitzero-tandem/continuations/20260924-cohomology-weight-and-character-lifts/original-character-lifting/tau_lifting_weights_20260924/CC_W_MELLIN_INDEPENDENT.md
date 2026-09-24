# Connes–Consani coefficient scaling inside the actual Mellin quotient

24 September 2026. Independent proof of the explicit map proposed by the root task. The operation prerequisites were checked in the local AGENTS.md, CORPUS_AND_OPERATION_RULES.md, U01–U18, and B1–B5/P1–P5 of SOURCE_OPERATIONS_AND_PROOFS.md. The complete relevant user passages USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2, and USR-6152e3bc6302258c were read in the preserved user corpus. This proof uses the already reconstructed arithmetic and its original zeta function. It does not construct arithmetic by counting primitive tau, and does not assign tau a coordinate, metric, parity, or addition.

The source datum supplied by the root task is Alain Connes and Caterina Consani's coefficient group algebra
\[
W_{\mathrm{alg}}=\mathbb C[\mathbb R_{>0}^{\times}],\qquad
[x][y]=[xy],\qquad \theta_a[x]=[x^a]\quad(a>0).
\tag{CW0.1}
\]
The root task read the original 2018 author TeX at §7.1, equations `holom`, `holom1`, and Proposition `frobarith`: [Connes–Consani, The Riemann–Roch strategy, Complex lift of the Scaling Site](https://arxiv.org/abs/1805.10501v1). This independent note proves the indicated receiving construction from those explicit operations, without claiming a reading of that whole paper.

The entry into their holomorphic construction is exact. Regard \(w\in W_{\mathrm{alg}}\) as a constant W-valued function on the original adelic complex lift. Every character evaluation is constant in both archimedean coordinates, so
\[
(\lambda X+iY)\chi_\lambda(w)=0\quad(\lambda>0).
\tag{CW0.2}
\]
Right geometric scaling fixes a constant function. The source arithmetic Frobenius \(\theta_aR(a^{-1})\) therefore restricts to \(\theta_a\) on these constant coefficients. Distinct algebraic coefficients remain distinct under their complete character family: for finitely many distinct \(x_j>0\), the evaluations at \(\lambda=1,\ldots,d\) have matrix \((x_j^r)\), with determinant
\[
\left(\prod_{j=1}^d x_j\right)
\prod_{1\le i<j\le d}(x_j-x_i)\ne0.
\tag{CW0.3}
\]
This establishes the precise source entry of the scaling representation used here. It does not identify the constant-coefficient subspace with the full holomorphic sheaf.

## CW1. Domains and the complete Gaussian Mellin factor

Let \(V_+\subset W_{\mathrm{alg}}\) be the complex span of basis elements \([x]\) with \(x>1\). It is invariant under every \(\theta_a\), since \(x^a>1\) for \(a>0\). Its elements are finite linear combinations; their multiplicities and coefficients belong to this specified group algebra, not to primitive \(\tau\). The source group-algebra unit \([1]\) is not in \(V_+\). We do not extend the formulas below to it by treating zero as a positive dilation.

Use the original strong Mellin space \(\mathcal A\), with seminorms
\[
p_{N,j}(k)=\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^j k(u)|,
\qquad N,j\ge0,
\]
and original transform and action
\[
F_k(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u},\qquad
W_a k(u)=a^{1/2}k(u/a),\qquad a>0.
\tag{CW1.1}
\]
Keep the explicit vector
\[
b(u)=\exp(-(\log u)^2).
\tag{CW1.2}
\]
It belongs to \(\mathcal A\): in \(v=\log u\), every \(j\)-th derivative is a polynomial in \(v\) times \(e^{-v^2}\), and multiplication by \(e^{Nv}+e^{-Nv}\) has finite supremum for each polynomial, because the negative quadratic dominates its linear and logarithmic growth.

Its entire Mellin transform is
\[
B(s):=F_b(s)
=\int_{\mathbb R}e^{-v^2+(s-1/2)v}\,dv
=\sqrt{\pi}\exp\!\left(\frac{(s-1/2)^2}{4}\right).
\tag{CW1.3}
\]
The integral is entire by an integrable Gaussian bound on each compact \(s\)-set, including derivatives. For real \(s\), completing the square and translating the real integration variable prove the last equality. Both sides are entire, so the identity theorem proves it for every complex \(s\). In particular \(B(s)\) never vanishes. Every factor in this evaluated transform remains in the comparison.

For \(x>1\), put \(t_x=\log x>0\) and define
\[
K_b[x]=W_{t_x}b,\qquad
(K_b[x])(u)=t_x^{1/2}
\exp\!\left(-(\log u-\log t_x)^2\right).
\tag{CW1.4}
\]
Extend linearly to \(V_+\). Dilation preserves \(\mathcal A\), since
\[
p_{N,j}(W_a k)
\le a^{1/2}\max(a^N,a^{-N})p_{N,j}(k).
\]
Substitution \(u=av\) in (CW1.1) gives
\[
F_{W_a k}(s)=a^sF_k(s),
\]
and consequently the full exact formula is
\[
\boxed{F_{K_b[x]}(s)=
\sqrt{\pi}\exp\!\left(\frac{(s-1/2)^2}{4}\right)(\log x)^s.}
\tag{CW1.5}
\]
Here \((\log x)^s=\exp(s\log(\log x))\), with the real logarithm of the positive number \(\log x\). Neither this double logarithm nor the Gaussian factor is absorbed into a replacement parameter.

Since \(\log(x^a)=a\log x\) and \(W_aW_t=W_{at}\), direct substitution proves
\[
K_b\theta_a=W_aK_b\qquad(a>0).
\tag{CW1.6}
\]
This is a linear intertwiner of the complete positive-real scaling action.

## CW2. The actual original-zeta quotient and every multiplicity condition

Retain
\[
\mathcal E f(u)=u^{1/2}\sum_{n\ge1}f(nu),\quad
I=\overline{\mathcal E(S_0^{\mathrm{even}})}^{\mathcal A},\quad
Q=\mathcal A/I,
\tag{CW2.1}
\]
where \(S_0^{\mathrm{even}}\) is the even Schwartz space with \(f(0)=0\) and \(\int_{\mathbb R}f=0\). Denote the quotient map by \(\pi_Q\), and set
\[
\overline K_b=\pi_QK_b:V_+\longrightarrow Q.
\tag{CW2.2}
\]
The programme has proved that \(I\) is invariant under \(W_a\), so (CW1.6) descends to this actual quotient.

The source of every zero condition is the original identity, initially on \(\Re s>1\),
\[
F_{\mathcal E f}(s)
=\zeta(s)\int_0^\infty f(v)v^s\frac{dv}{v}.
\tag{CW2.3}
\]
Absolute convergence justifies exchanging sum and integral there. The second factor is holomorphic for \(\Re s>-2\), since evenness and \(f(0)=0\) give \(f(v)=O(v^2)\) at zero and the Schwartz property controls infinity. The product is therefore holomorphic throughout the critical strip, and its meromorphic identity continues from the half-plane. For every actual nontrivial zero \(\rho\) of \(\zeta\), with its full multiplicity \(m_\rho\),
\[
F_{\mathcal E f}^{(r)}(\rho)=0\qquad(0\le r<m_\rho).
\tag{CW2.4}
\]
Each derivative evaluation is continuous on \(\mathcal A\), by its defining integral with the factor \((\log u)^r\) and a sufficiently strong seminorm at both endpoints. Thus (CW2.4) holds for all of \(I\), not merely its generating image.

No completed zeta function replaces \(\zeta\) in this argument. The original pole and the full source endpoint restrictions remain part of (CW2.1)–(CW2.3); no assertion about omitted trivial zeros is needed for this implication.

## CW3. Injectivity through the quotient: a global zero-density proof

Take \(v=\sum_{j=1}^d c_j[x_j]\), with the \(x_j>1\) distinct and all displayed coefficients nonzero. Write
\[
t_j=\log x_j>0,\qquad \lambda_j=\log t_j\in\mathbb R,\qquad
P_v(s)=\sum_{j=1}^d c_j e^{\lambda_j s}.
\tag{CW3.1}
\]
Then
\[
F_{K_bv}(s)=B(s)P_v(s).
\tag{CW3.2}
\]
If \(\overline K_bv=0\), then \(K_bv\in I\), and CW2 implies that this product vanishes to order at least \(m_\rho\) at every actual nontrivial zero \(\rho\). Since the entire factor \(B\) is nowhere zero, \(P_v\) itself has those zeros with at least those multiplicities.

A nonzero finite exponential polynomial of the displayed kind has at most \(O(R)\) zeros in a disk of radius \(R\), counted with multiplicity. Here is the complete Jensen estimate needed for that assertion. Choose \(s_*\) with \(P_v(s_*)\ne0\), put \(H=\max_j|\lambda_j|\), and \(C=\sum_j|c_j|e^{\lambda_j\Re s_*}>0\). Then for \(|z|\le R'\),
\[
|P_v(s_*+z)|\le C e^{HR'}.
\tag{CW3.3}
\]
Apply Jensen's formula to \(P_v(s_*+z)\) at a radius \(R'\) between \(2R\) and \(2R+1\) having no boundary zeros. Each zero in \(|z|\le R\) contributes at least \(\log2\). Thus its zero count \(n_v(R)\) satisfies
\[
n_v(R)\log2
\le \frac1{2\pi}\int_0^{2\pi}
\log|P_v(s_*+R'e^{i\theta})|\,d\theta-\log|P_v(s_*)|
\le \log C+H(2R+1)-\log|P_v(s_*)|.
\tag{CW3.4}
\]
Such a radius exists because zeros are discrete when \(P_v\) is not identically zero. This proves the asserted \(O(R)\) estimate with all quantities specified.

The unconditional explicit Riemann–von Mangoldt bound of Elchin Hasanalizade, Quanli Shen, and Peng-Jie Wong, [*Counting zeros of the Riemann zeta function*, arXiv:2107.06506v1](https://arxiv.org/abs/2107.06506v1), Corollary 1.2, states for every \(T\ge e\)
\[
\left|N_\zeta(T)-\frac{T}{2\pi}\log\left(\frac{T}{2\pi e}\right)\right|
\le0.1038\log T+0.2573\log\log T+9.3675,
\tag{CW3.5}
\]
where \(N_\zeta(T)\) counts the nontrivial zeros with \(0<\Im\rho\le T\), including multiplicity. The source defines this count in original TeX lines 187–201, states the complete bound at lines 255–261 (`main-thm`, `main-bound-1`), and uses the argument principle at lines 327–337, which retains multiplicity. Those passages were read directly for this proof. All constants of the source bound are displayed; its lower estimate grows faster than every fixed multiple of \(T\). This is an established external theorem, not a new programme result or an RH assumption. The previous programme upper-count bound alone would not supply this lower estimate.

Every zero counted by \(N_\zeta(R-|s_*|-2)\) lies in the disk \(|\rho-s_*|\le R\), since \(0<\Re\rho<1\) gives \(|\rho|\le1+|\Im\rho|\). Therefore the zero multiplicity conditions above contradict (CW3.4) unless \(P_v\) is identically zero.

Finally the functions \(e^{\lambda_js}\) are linearly independent. Differentiating an identically vanishing \(P_v\) at \(s=0\), for derivative orders \(0,\ldots,d-1\), gives the matrix \((\lambda_j^r)\). Its determinant is \(\prod_{i<j}(\lambda_j-\lambda_i)\ne0\), because the \(x_j\) and therefore the \(\lambda_j\) are distinct. Thus every \(c_j=0\). We have proved
\[
\boxed{\overline K_b:V_+\longrightarrow Q\ \text{is injective}.}
\tag{CW3.6}
\]
The same argument proves that \(K_b\) is injective before quotienting; there even (CW3.2) and independence suffice. No RH, zero simplicity, bounded-height test, or selected finite prime list enters the quotient injection.

## CW4. The exact jet maps, their Gaussian unit, and finite joint surjectivity

For each actual zero define the full local algebra and the linear source observation
\[
A_\rho=\mathbb C[T_\rho]/(T_\rho^{m_\rho}),\qquad
L_\rho[x]
=(\log x)^\rho
\sum_{r=0}^{m_\rho-1}
\frac{(\log\log x)^r T_\rho^r}{r!}.
\tag{CW4.1}
\]
Every label \(\rho\) and multiplicity remains. This expression is the complete Taylor jet of \((\log x)^s\) at \(s=\rho\). For the actual quotient jet
\[
j_\rho([k])=\sum_{r=0}^{m_\rho-1}
\frac{F_k^{(r)}(\rho)}{r!}T_\rho^r,
\]
the exact commutative comparison is
\[
\boxed{j_\rho\overline K_b
=M_{B(\rho+T_\rho)}L_\rho.}
\tag{CW4.2}
\]
Here \(M\) means multiplication in the named receiving algebra, and the complete Gaussian jet factor is
\[
B(\rho+T_\rho)
=\sqrt{\pi}\exp\!\left(\frac{(\rho-1/2)^2}{4}\right)
\exp\!\left(\frac{\rho-1/2}{2}T_\rho+\frac14T_\rho^2\right).
\tag{CW4.3}
\]
All exponentials in the nilpotent variable are taken modulo \(T_\rho^{m_\rho}\); every surviving term is retained. Its inverse is
\[
\frac1{\sqrt{\pi}}\exp\!\left(-\frac{(\rho-1/2)^2}{4}\right)
\exp\!\left(-\frac{\rho-1/2}{2}T_\rho-\frac14T_\rho^2\right).
\tag{CW4.4}
\]
The derivative product rule proves (CW4.2) with its factorials. Multiplication of the finite exponentials proves the inverse formula, so the Gaussian unit has an explicit return rather than being discarded.

For any finite collection \(\mathcal S\) of distinct actual zeros, the linear map
\[
L_{\mathcal S}:V_+\longrightarrow\prod_{\rho\in\mathcal S}A_\rho
\tag{CW4.5}
\]
is onto. To prove it, let a linear functional on the finite target vanish on every \(L_{\mathcal S}[x]\). Since \(\lambda=\log\log x\) ranges over all real numbers as \(x\) ranges over \((1,\infty)\), this gives an identically vanishing function
\[
\sum_{\rho\in\mathcal S}p_\rho(\lambda)e^{\rho\lambda}=0,
\qquad \deg p_\rho<m_\rho.
\tag{CW4.6}
\]
Fix \(\rho_0\). Apply
\[
\prod_{\substack{\eta\in\mathcal S\\\eta\ne\rho_0}}
(\partial_\lambda-\eta)^{m_\eta}.
\]
It kills all other summands. After removing \(e^{\rho_0\lambda}\), it acts on \(p_{\rho_0}\) by a product of \((\partial_\lambda+\rho_0-\eta)^{m_\eta}\). On polynomials of degree below \(m_{\rho_0}\), each such factor is triangular with nonzero diagonal, hence invertible. Therefore \(p_{\rho_0}=0\); the argument applies to every member of \(\mathcal S\). The supposed target functional is zero, because its coefficients differ from those of the \(p_\rho\) only by the nonzero factorials in (CW4.1).

A proper linear subspace of a finite-dimensional vector space is annihilated by a nonzero functional: extend a basis of the subspace to a basis of the target and take one new coordinate functional. Therefore the absence of such a functional proves surjectivity in (CW4.5). This proof also applies to a single zero block. By the invertible componentwise Gaussian multiplication, \(j_{\mathcal S}\overline K_b\) is onto the same finite product.

The complete product map
\[
L:V_+\longrightarrow\prod_{\rho\in\mathcal Z}A_\rho
\tag{CW4.7}
\]
is injective, by the proof of CW3 applied directly to \(P_v\). No surjectivity onto that complete product has been inferred from finite surjectivity. In fact its constant coordinates obey an exact restriction:
\[
|P_v(\rho)|\le\sum_{j=1}^d|c_j|\max(1,t_j)
\quad\text{for every }0<\Re\rho<1.
\tag{CW4.8}
\]
Thus they are bounded uniformly over the full zero set for each fixed source element. The complete product permits, for example, constant coordinates \(|\Im\rho|\), which are unbounded along zeros by (CW3.5), so this product element is not in the image. This proves the non-surjectivity of (CW4.7), with no claim about the topology of the full quotient.

The image is nevertheless dense in the complete product when each finite local algebra has its ordinary finite-dimensional topology and the product has the product topology. A basic open neighbourhood restricts only finitely many coordinates. CW4.5 supplies an element realizing those coordinates exactly, hence meeting that neighbourhood. This density statement is about the product topology, not a Hilbert norm or an asserted purity metric.

## CW5. Exact scaling at every primary block

For every \(a>0\), Taylor expansion of \((\log x^a)^s=(a\log x)^s\) proves
\[
L_\rho\theta_a
=M_{a^\rho\exp((\log a)T_\rho)}L_\rho.
\tag{CW5.1}
\]
The exponential is again the full finite nilpotent sum, and the multiplier is the original unshifted operator. The Gaussian multiplier in CW4.2 commutes with it because both are multiplication in the same local algebra. Thus the finite-block diagrams and the complete-product diagram simultaneously preserve every positive-real dilation, in particular every prime and every prime power. The image of \(V_+\) is an actual invariant subspace of \(Q\), by the injective map (CW3.6), with finite jet maps onto all finite original-zero packets.

At no point does this identify \([x]\), \(T_\rho\), a scalar identity, or a Mellin coordinate with primitive \(\tau\). The domain is a specified part of CC's coefficient algebra after arithmetic reconstruction, with its source scaling operation retained.

## CW6. What the source multiplication does and does not preserve

These are linear intertwiners, not algebra homomorphisms for the original CC product. For \(x,y>1\), write \(t=\log x\), \(u=\log y\). Then
\[
L_\rho([x][y])=(t+u)^\rho
\exp((\log(t+u))T_\rho),
\tag{CW6.1}
\]
whereas multiplication of the two receiving values is
\[
L_\rho[x]\,L_\rho[y]=(tu)^\rho
\exp((\log t+\log u)T_\rho).
\tag{CW6.2}
\]
These retain the source product \([xy]\) and its exact image. At \(x=y=e\), the first constant is \(2^\rho\), while the second is 1; for a nontrivial zero their moduli differ because \(0<\Re\rho<1\). Thus the failure is exhibited on an actual primary receiver, rather than hidden in notation.

The full strong-space convolution comparison is also exact:
\[
K_b[x]*K_b[y]=b*K_b[\exp(tu)].
\tag{CW6.3}
\]
One can prove it directly in logarithmic coordinates, retaining all factors: convolution obeys
\((W_t b)*(W_u b)=W_{tu}(b*b)\), and \(b*W_{tu}b=W_{tu}(b*b)\), by substituting the integration variable and using the explicit square-root factors in \(W\). The original source product instead gives \(K_b[xy]=W_{t+u}b\). Formula (CW6.3) is a proved alternative convolution relation, not a replacement for the original CC algebra law.

Therefore the established comparison is an injective linear representation map for scaling, with all its exact finite and global jet observations. It does not assert a ring isomorphism, a positive metric, a lift of all infinite jet data, or Deligne purity merely from the existence of that map.

## CW7. Every support label on the exact linear comparison

For the programme's bounded distributive lattice \(L\), and any of the named complex vector spaces \(V\), retain its labelled receiving semimodule
\[
G_L(V)=\{(0,\lambda):\lambda\in L\}\cup\{(v,1_L):v\in V\}.
\]
Its receiving addition is \((v,\lambda)+(w,\mu)=(v+w,\lambda\vee\mu)\); the scalar \((c,\nu)\in G_L(\mathbb C)\) acts by \((cv,\nu\wedge\lambda)\). These are the already specified receiving operations, not operations on primitive \(\tau\). A linear map \(f:V\to V'\) induces
\[
G_L(f)(v,\lambda)=(f(v),\lambda).
\tag{CW7.1}
\]
It is well-defined because a non-top input label forces \(v=0\), and linearity gives \(f(v)=0\). Linearity and the unchanged joins and meets prove preservation of the displayed operations directly. Identity maps and compositions are preserved by substitution.

Applying this to \(\overline K_b\) gives an injective map \(G_L(V_+)\to G_L(Q)\): equality of images gives equality of labels and, by CW3.6, equality of amplitudes. Its inverse on its image sends \((\overline K_bv,\lambda)\) to \((v,\lambda)\), preserving that label as well. Every finite-jet map of CW4 lifts coordinatewise with exactly the same label, and its surjectivity lifts because a preimage exists for every top-supported amplitude while each \((0,\lambda)\) has preimage \((0,\lambda)\). This uses a common label on the finite product; independent labels on different blocks would be a different object and are not substituted for it.

In particular a scalar amplitude cancellation remains \((0,\lambda)\) under every lifted map, retaining the distinction between every supported zero and the bottom label. No \(z_\lambda=(0,\lambda)\) is identified with primitive \(\tau\). This proves the full support return for the linear intertwiners, without asserting an unconstructed equivalence of semimodule cohomology theories.

## Sources and exact reading scope

- The local operation rules, U01–U18, B1–B5/P1–P5, and the three complete user arguments listed in the opening paragraph were read before deriving the comparison. The complete-history reconstruction remains an input; this note does not construct integers from an incomplete clock.
- The actual source quotient and prime action are the already-read programme proofs *Global canonical Mellin involution*, G1–G5, and *Global infinitesimal quotient*, GIQ1–GIQ3. Their exact filenames are retained in the source ledger. The complete implications needed here are repeated in CW1–CW2 and CW4.
- Alain Connes and Caterina Consani retain authorship of the coefficient group algebra and \(\theta_a\) action in CW0.1. The root read their original 2018 TeX, `thecurve_K.tex`, lines 2564–2601, including §7.1's `holom`, `holom1` and `frobarith`, and proved the constant-function entry above. This subagent does not claim a whole-paper reading.
- The complete explicit zero-count input is Hasanalizade–Shen–Wong, arXiv:2107.06506v1, original `sources/2107.06506v1/source.tex`, lines 181–201, 221–277, and 309–359 read for this calculation. These include the count definition, full Corollary 1.2, and multiplicity convention from the argument principle. SHA256: \nolinkurl{3FAA3CB45EE34B5FCD96F84ED036DE2AF1C3DCEA75723776410E2AC359FF5021}. This is bounded original-source reading, not a claim to have reread the whole paper. CW3 uses its stated count of original-zeta zeros; it does not replace zeta by the source's completed function. Jensen's formula is the classical analytic theorem used in CW3.4, with the complete actual bound displayed.
- A bounded routing lookup located the existing canonical-index receipt, whose database is recorded as research_canonical_index.sqlite in the retained literature foundation. This was routing only, not a claim of reading its mathematical sources. No PDF was used.
- The root proposed \(K_b\). This independent proof verifies its full factor, global injectivity, every finite-jet surjection, the complete-product injection, the precise multiplication defect, and all operator identities. No additional claim of literature novelty or RH resolution is made.

## Current propagation from OMS — 24 September 2026

[The complete synthesis proof](ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md), OMS1–OMS5, proves that the original summation image is closed and that the full actual-zero jet map on Q has zero common kernel. Its image remains a proper dense subspace of the unrestricted product, carrying the stronger original quotient topology. Earlier statements leaving those two questions undetermined are superseded by that proof, not by an assumption. Every original zero multiplicity and support label remains.

OMS7A proves the exact return to AC0–AC4: the same original spaces give I0=2 E(S)=E(S), with the factor 2 retained in the periodization map and inverse. Thus D_cl=0, C_alg→Q is the identity-induced topological isomorphism, and the specific global two-extension class of the actual adelic two-term complex is zero. Both endpoint contributions at each prime and the higher derived-coinvariant groups remain unchanged. No vanishing of the entire Ext group or full tau purity is inferred.

## Global adelic lifting propagation - 24 September 2026

The complete current proofs are GLOBAL_ADELIC_LIFTING_AND_PRIME_BOUNDARY.md GAP0–GAP9 (including GAP6A–GAP6B), COMPLETE_GENERATOR_ENDPOINT_RETURN.md GER0–GER7, GLOBAL_ENDPOINT_EXTENSION_RETURN.md GEX0–GEX9, and COMPLETE_COMPARISON_TRIANGLE_FORMALITY.md CTF0–CTF8. Every original prime wedge, endpoint pair and nilpotent jet is retained. GER credits the existing RZ endpoint resolvents and gives their explicit original Schwartz return and covariance corrections. GEX proves vanishing of the entire extension groups between the whole actual Q and the stated endpoint modules, in the explicitly constructed algebraic and strict locally convex operator categories. This strengthens the earlier finite-block and particular-extension assertions without assigning that theorem to a larger unspecified category.

GAP and CTF construct the full derived adelic complex, its canonical cohomology map, the exact original CC comparison and its entire cone. The faithful coefficient copies distinguish primitive tau from integer one in both objects. All additional cone contractions and the final-arrow homotopy are explicit; no test-space section Q→A is asserted. On the separate supported-Q row the same polynomial is invertible, rather than zero. Full tau numerical purity does not follow from endpoint separation and remains unproved.
