## Precise reformulation of the KMS bridge

I will state the result in the only form that is mathematically correct.

There are three separate levels.

1. The **abstract operator-algebraic level**: KMS simplices, extremal KMS states, symmetry action, barycentric decomposition.
2. The **proved arithmetic realizations**: the BC system over $\mathbf Q$ and the CM system over an imaginary quadratic field $K$.
3. The **general BCM formalism**: unconditional construction of low-temperature extremal KMS states attached to invertible points $y\in Y_{D,L}^{\times}$, together with a conditional completion statement requiring a full KMS classification.

The first two are unconditional theorems. The third is unconditional only on the “branch side”; the exact unresolved/branch identification is conditional on the missing classification theorem. If, in a particular arithmetic BCM model, that classification is equivalent to RH or GRH, then the completed bridge is correspondingly RH- or GRH-conditional. That implication is formal.

I now write this out in theorem-lemma-proof form.

---

# 1. Abstract KMS geometry

Let $(A,\sigma)$ be a unital $C^*$-dynamical system, with
$$
\sigma:\mathbf R\to \operatorname{Aut}(A),\qquad t\mapsto \sigma_t.
$$

For $0<\beta<\infty$, let $\Sigma_\beta$ denote the compact convex set of KMS$_\beta$-states on $A$, and let $E_\beta\subseteq \Sigma_\beta$ be its set of extreme points. For $\beta=\infty$, let $\Sigma_\infty$ be the weak-* compact convex set of weak limits of KMS$_\beta$-states as $\beta\to\infty$, and let $E_\infty\subseteq\Sigma_\infty$ be its set of extreme points. In the CM papers, this is exactly the convention adopted in Definitions 2.1-2.2 and the following discussion. `CMR1.pdf` `CMR1.pdf`

We also fix a compact group $G$ acting by automorphisms of the dynamical system:
$$
\alpha:G\to \operatorname{Aut}(A,\sigma),
\qquad
\alpha_g\circ \sigma_t=\sigma_t\circ \alpha_g.
$$
The KMS condition implies that inner automorphisms act trivially on KMS states, so such a symmetry action induces an action on each $\Sigma_\beta$ and each $E_\beta$. This is explicitly stated in the CM discussion of symmetry breaking and KMS actions. `CMR1.pdf` `cmr0.pdf`

---

## Definition 1.1 - unresolved state and branch space

For a fixed inverse temperature $\beta$, define:

1. the **branch space**
   $$
   \mathcal B_\beta:=E_\beta;
   $$
2. the **unresolved state** (if it exists) to be a $G$-fixed point of $\Sigma_\beta$.

When $\Sigma_\beta$ is a singleton, its unique element will be called the **canonical unresolved state** at temperature $\beta^{-1}$.

This is the mathematically precise version of the unresolved/branch language.

---

## Lemma 1.2 - extremality of the unique KMS state

Assume that $\Sigma_\beta$ is a singleton:
$$
\Sigma_\beta=\{\varphi_\beta\}.
$$
Then $\varphi_\beta$ is an extreme point of $\Sigma_\beta$, hence a factor state.

### Proof

A singleton compact convex set has its unique point as an extreme point by definition. The general structure theorem for KMS simplices states that the extreme points of $\Sigma_\beta$ are precisely the factor states. This is Proposition 3.2.5 in the BCM text and is also stated in the CM papers. `Bost-Connes-Marcolli systems.pdf` `CMR1.pdf` Thus $\varphi_\beta$ is a factor state. ∎

---

## Lemma 1.3 - invariance of the unique KMS state

Assume that $\Sigma_\beta=\{\varphi_\beta\}$. Then $\varphi_\beta$ is $G$-invariant.

### Proof

For each $g\in G$, the induced action sends $\Sigma_\beta$ to itself. Since $\Sigma_\beta$ contains only one point, necessarily
$$
g\cdot \varphi_\beta=\varphi_\beta.
$$
∎

---

## Lemma 1.4 - unique invariant barycenter of a transitive branch space

Let $E$ be a compact Hausdorff space carrying a continuous transitive action of a compact group $G$. Then there exists a unique $G$-invariant Borel probability measure on $E$. Consequently, for every continuous affine embedding
$$
E\hookrightarrow K
$$
into a compact convex set $K$, there is a canonically defined $G$-invariant barycenter
$$
\operatorname{bar}_G(E)\in K.
$$

### Proof

Fix $x_0\in E$. Since the action is transitive, the orbit map
$$
\pi_{x_0}:G\to E,\qquad g\mapsto g\cdot x_0
$$
is surjective and continuous. Push forward normalized Haar measure $dg$ on $G$ to obtain a probability measure
$$
\mu_E:=(\pi_{x_0})_*(dg).
$$
Left-invariance of Haar measure implies $G$-invariance of $\mu_E$.

To prove uniqueness, let $\nu$ be another $G$-invariant probability measure on $E$. For any continuous $f\in C(E)$, define
$$
F(g):=f(g\cdot x_0).
$$
Then
$$
\int_E f\,d\nu
=
\int_G f(g\cdot x_0)\,dg
=
\int_E f\,d\mu_E,
$$
because the $G$-invariance of $\nu$ identifies $\int_E f\,d\nu$ with the Haar average of $f$ along the orbit of $x_0$. Hence $\nu=\mu_E$.

If $E\hookrightarrow K$ is an affine embedding into a compact convex set, the barycenter of $\mu_E$ gives an element $\operatorname{bar}_G(E)\in K$, and by $G$-invariance of $\mu_E$ this barycenter is $G$-fixed. ∎

---

## Theorem 1.5 - exact KMS realization of unresolved/branch geometry

Let $(A,\sigma)$ be a $C^*$-dynamical system with compact symmetry group $G$.

Assume that for some $\beta_c>0$ the following hold.

1. For every $0<\beta\le \beta_c$, $\Sigma_\beta$ is a singleton.
2. For every $\beta>\beta_c$, the branch space $E_\beta$ is a compact homogeneous $G$-space.
3. Every state in $\Sigma_\beta$ lies in the closed convex hull of $E_\beta$. In particular, this holds whenever $\Sigma_\beta$ is a Choquet simplex.

Then:

1. for $0<\beta\le \beta_c$, the unresolved state is exactly the unique KMS$_\beta$-state;
2. for $\beta>\beta_c$, the branches are exactly the extreme KMS$_\beta$-states;
3. for $\beta>\beta_c$, there is a canonically defined $G$-invariant unresolved state
   $$
   \bar\varphi_\beta:=\operatorname{bar}_G(E_\beta),
   $$
   obtained by Haar averaging the branch orbit.

### Proof

The first assertion is Lemmas 1.2 and 1.3.

The second assertion is tautological from the definition $\mathcal B_\beta=E_\beta$.

For the third, Lemma 1.4 gives a unique $G$-invariant probability measure $\mu_\beta$ on $E_\beta$. Since $\Sigma_\beta$ is compact convex and contains the closed convex hull of $E_\beta$, the barycenter
$$
\bar\varphi_\beta:=\int_{E_\beta}\psi\,d\mu_\beta(\psi)
$$
is a well-defined state in $\Sigma_\beta$, and it is $G$-invariant. ∎

This theorem is the exact bridge. There is no analogy left once the hypotheses are verified.

---

# 2. The BC system over $\mathbf Q$

We now specialize to the BC system $ (A_1,\sigma_t) $. The relevant facts proved in the Connes-Marcolli account are the following.

1. The partition function is $\zeta(\beta)$. `CMR1.pdf`
2. For $0<\beta\le 1$, the set of extremal KMS$_\beta$-states is a singleton. `cmr0.pdf`
3. For $1<\beta\le \infty$, the extremal KMS$_\beta$-states are indexed by invertible $\mathbf Q$-lattices, equivalently by
   $$
   \widehat{\mathbf Z}^{\times}
   \cong
   \mathrm{GL}_1(\widehat{\mathbf Z}),
   $$
   with a free and transitive action of $\widehat{\mathbf Z}^{\times}$. `cmr0.pdf`
4. The extremal KMS$_\infty$-states evaluated on the rational arithmetic subalgebra $A_{1,\mathbf Q}$ take values in $\mathbf Q^{\mathrm{cycl}}$, and the class field theory isomorphism
   $$
   \theta:\operatorname{Gal}(\mathbf Q^{\mathrm{cycl}}/\mathbf Q)\xrightarrow{\sim}\widehat{\mathbf Z}^{\times}
   $$
   intertwines Galois action and symmetry action. `cmr0.pdf`

These are precisely the ingredients needed to invoke Theorem 1.5.

---

## Theorem 2.1 - BC exactness theorem

For the BC system $(A_1,\sigma_t)$, let
$$
G:=\widehat{\mathbf Z}^{\times}.
$$

Then:

1. for every $0<\beta\le 1$, the unresolved state is exactly the unique KMS$_\beta$-state;
2. for every $1<\beta<\infty$, the branch space is exactly the $G$-torsor $E_\beta\cong G$;
3. for every $1<\beta<\infty$, the unresolved state at inverse temperature $\beta$ is exactly the Haar barycenter of the branch space:
   $$
   \bar\varphi_\beta(a)
   =
   \int_G \varphi_{\beta,g}(a)\,dg;
   $$
4. at $\beta=\infty$, the branch space is still $E_\infty\cong G$, and evaluation on the arithmetic subalgebra produces $\mathbf Q^{\mathrm{cycl}}$ with symmetry action intertwined with Galois action.

### Proof

By Proposition 3.2.5 of the BCM text, KMS state spaces are compact convex simplices whose extreme points are factor states. `Bost-Connes-Marcolli systems.pdf`

By the BC classification theorem recorded in CMR Part II, $E_\beta$ is a singleton for $0<\beta\le1$, while for $1<\beta\le\infty$ it is parameterized by invertible $\mathbf Q$-lattices, equivalently by $\widehat{\mathbf Z}^{\times}$, and the action of $\widehat{\mathbf Z}^{\times}$ is free and transitive. `cmr0.pdf`

Hence assertions (1)-(3) follow from Theorem 1.5, since $\widehat{\mathbf Z}^{\times}$ is compact profinite.

Assertion (4) is exactly the fabulous-states statement: the extremal KMS$_\infty$-states take values in $\mathbf Q^{\mathrm{cycl}}$ on $A_{1,\mathbf Q}$, and the class field theory isomorphism intertwines Galois and symmetry actions. `cmr0.pdf` ∎

---

## Corollary 2.2 - The BC bridge is not an analogy

In the BC system, the unresolved/branch distinction is literally the KMS phase structure:

$$
\begin{array}{c|c}
0<\beta\le1 & \text{unique unresolved state},\\[1ex]
1<\beta\le\infty & \text{resolved cyclotomic branches}.
\end{array}
$$

The zero-temperature branches are arithmetic points in the sense that their values on $A_{1,\mathbf Q}$ generate $\mathbf Q^{\mathrm{cycl}}$ and carry the class field theoretic Galois action. ∎

---

# 3. The CM system over an imaginary quadratic field

Now let $K$ be an imaginary quadratic field and consider the CM system $(A_K,\sigma_t)$.

The relevant proven facts are:

1. For $0<\beta\le1$, there is a unique KMS$_\beta$-state. `cmr0.pdf` `CMR1.pdf`
2. For $\beta>1$, the extremal KMS$_\beta$-states are parameterized by invertible $K$-lattices
   $$
   E_\beta\cong A_{K,f}^{\times}/K^\times,
   $$
   and the symmetry group
   $$
   C_K/D_K \cong A_{K,f}^{\times}/K^\times
   $$
   acts freely and transitively. `cmr0.pdf` `cmr0.pdf`
3. The branch space $A_{K,f}^{\times}/K^\times$ is compact. This is explicitly recorded in the comparison table of CMR Part II, which lists the CM symmetry group as compact. `CMR1.pdf`
4. The extremal KMS$_\infty$-states evaluated on the arithmetic subalgebra $A_{K,0}$ or $A_{K,\mathbf Q}$ generate $K^{ab}$, and the class field theory isomorphism intertwines the symmetry action with $\operatorname{Gal}(K^{ab}/K)$. `cmr0.pdf` `cmr0.pdf`

---

## Theorem 3.1 - CM exactness theorem

For the CM system $(A_K,\sigma_t)$, let
$$
G:=C_K/D_K\cong A_{K,f}^{\times}/K^\times.
$$

Then:

1. for every $0<\beta\le1$, the unresolved state is exactly the unique KMS$_\beta$-state;
2. for every $1<\beta<\infty$, the branch space is exactly the compact homogeneous $G$-space $E_\beta\cong G$;
3. for every $1<\beta<\infty$, the unresolved state at inverse temperature $\beta$ is exactly the Haar barycenter of the branch space:
   $$
   \bar\varphi_\beta(a)=\int_G \varphi_{\beta,g}(a)\,dg;
   $$
4. at $\beta=\infty$, the branch space remains $E_\infty\cong G$, and evaluation on the arithmetic subalgebra generates $K^{ab}$ with symmetry action intertwined with $\operatorname{Gal}(K^{ab}/K)$.

### Proof

The general simplex statement again comes from Proposition 3.2.5 of the BCM text. `Bost-Connes-Marcolli systems.pdf`

The CM classification theorem is Theorem 3.1 of CMR Part I and Theorem 5.2 of CMR Part II. It gives precisely the unique-state statement for $0<\beta\le1$, the free transitive branch parameterization for $\beta>1$, and the arithmetic/Galois statement at $\beta=\infty$. `cmr0.pdf` `CMR1.pdf`

Since the symmetry group $G$ is compact, Theorem 1.5 applies and gives the Haar barycenter statement for $1<\beta<\infty$. The zero-temperature arithmetic statement is part of Theorem 3.1 / 5.2 itself. ∎

---

## Corollary 3.2 - The CM bridge is not an analogy

In the CM system, the unresolved/branch distinction is literally the thermodynamic phase structure, and the branch states are literally arithmetic points of the associated noncommutative pro-variety in the sense explained by Connes-Marcolli-Ramachandran. The arithmetic subalgebra is not a heuristic decoration: it is the algebra on which branch evaluation recovers $K^{ab}$ together with the correct Galois action. `CMR1.pdf` ∎

---

# 4. The general BCM formalism

Now let $(D,L)$ be a summable BCM pair, with BCM $C^*$-algebra $A(D,L)$, zeta function $\zeta_{D,L}$, and invertible locus $Y_{D,L}^{\times}$.

The general BCM text proves the following unconditional facts.

1. If $y\in Y_{D,L}^{\times}$ and $\zeta_{D,L}(\beta)$ converges, then
   $$
   \Phi_{\beta,y}(f)
   :=
   \frac{\operatorname{Tr}(\pi_y(f)e^{-\beta H_y})}{\zeta_{D,L}(\beta)}
   $$
   is a KMS$_\beta$-state. `Bost-Connes-Marcolli systems.pdf`
2. The commutant of $\pi_y(A(D,L))$ is scalar for $y\in Y_{D,L}^{\times}$. `Bost-Connes-Marcolli systems.pdf`
3. Hence $\Phi_{\beta,y}$ is an extremal type $I_\infty$ factor state. `Bost-Connes-Marcolli systems.pdf`

This yields the branch side of the story.

---

## Theorem 4.1 - Unconditional BCM branch theorem

Let $(D,L)$ be a summable BCM pair and let $\beta$ be such that $\zeta_{D,L}(\beta)$ converges.

Then the assignment
$$
y\in Y_{D,L}^{\times}\longmapsto \Phi_{\beta,y}\in \Sigma_\beta
$$
takes values in the branch space $E_\beta$, and every such state is a type $I_\infty$ factor state.

### Proof

By Lemma 6.2.1 of the BCM paper, $\Phi_{\beta,y}$ is a KMS$_\beta$-state whenever $\zeta_{D,L}(\beta)$ converges. `Bost-Connes-Marcolli systems.pdf`

By Lemma 6.2.2, the commutant $\pi_y(A(D,L))'$ is scalar for $y\in Y_{D,L}^{\times}$. Hence Proposition 6.2.3 shows that $\Phi_{\beta,y}$ is extremal of type $I_\infty$. `Bost-Connes-Marcolli systems.pdf` `Bost-Connes-Marcolli systems.pdf` ∎

---

This is unconditional. What is **not** unconditional is the converse, namely:

- that every extremal KMS$_\beta$-state arises from some $y\in Y_{D,L}^{\times}$;
- that for $0<\beta\le\beta_c$ there is a unique KMS$_\beta$-state;
- that the resulting branch space is a compact homogeneous symmetry space.

Those are classification statements, and they are exactly the content needed to turn the BCM branch theorem into a full unresolved/branch theorem.

---

## Theorem 4.2 - Conditional BCM exactness theorem

Let $(D,L)$ be a summable BCM pair. Assume the following classification hypotheses hold for some $\beta_c>0$.

1. For every $0<\beta\le\beta_c$, $\Sigma_\beta$ is a singleton.
2. For every $\beta>\beta_c$, every extremal KMS$_\beta$-state is of the form $\Phi_{\beta,y}$ for a unique class $y\in Y_{D,L}^{\times}/\!\sim$.
3. The symmetry group $G$ acts continuously, freely, and transitively on the quotient $Y_{D,L}^{\times}/\!\sim$, and this quotient is compact.

Then the unresolved/branch bridge is exact for $(D,L)$: Theorem 1.5 applies verbatim.

### Proof

Under hypothesis (2), Theorem 4.1 identifies the branch space $E_\beta$ with the compact homogeneous $G$-space $Y_{D,L}^{\times}/\!\sim$. Hypothesis (1) gives the unique unresolved state at high temperature, and compact transitivity gives the Haar barycenter at low temperature. Therefore Theorem 1.5 applies. ∎

---

## Corollary 4.3 - RH/GRH dependence, when present

Suppose that for a given arithmetic BCM datum $(D,L)$, the classification hypotheses of Theorem 4.2 are equivalent to RH or GRH for the zeta/L-function encoded by $\zeta_{D,L}$. Then the exact unresolved/branch theorem for $(D,L)$ is equivalent to that RH/GRH statement.

### Proof

Immediate from Theorem 4.2 by logical equivalence. ∎

This is the precise formulation of your interruption: in such a case the statement is not merely “true in the framework”; it is true **assuming the RH/GRH-controlled BCM classification**, because that classification is exactly what upgrades the unconditional branch construction to the full exact bridge.

---

# 5. The BC-GL$_2$-CM bridge is itself proved, not heuristic

There is a second statement one should record because you said “this has proof of bridges between coupled fields.” The relevant theorem is that the systems are linked by actual correspondences, not by verbal analogy.

The CMR text proves that the BC and GL$_2$ systems are related by a correspondence
$$
\rho_{12}:A_1\longrightarrow M(A_2)
$$
compatible with time evolutions and rational subalgebras; this is Proposition 3.10 in CMR Part II. `CMR1.pdf`

The same text also states that the CM system is realized as a subgroupoid of the GL$_2$-system and inherits its natural arithmetic subalgebra from that realization. `CMR1.pdf`

Thus there are actual arrows

$$
\mathrm{BC}\ \longrightarrow\ \mathrm{GL}_2
\quad\text{and}\quad
\mathrm{CM}\ \hookrightarrow\ \mathrm{GL}_2,
$$

compatible with time evolution and arithmetic subalgebras. These are not metaphorical bridges; they are proved functorial/correspondence statements in the cited papers. `CMR1.pdf` `CMR1.pdf`

---

## Theorem 5.1 - arithmetic KMS towers form a proved bridge diagram

There is a diagram of arithmetic quantum statistical systems

$$
\mathrm{BC}
\overset{\rho_{12}}{\longrightarrow}
\mathrm{GL}_2
\longleftarrow
\mathrm{CM},
$$

such that:

1. $\rho_{12}$ is compatible with time evolutions and rational subalgebras;
2. the CM system is realized as a subgroupoid specialization of $\mathrm{GL}_2$;
3. in each of the BC and CM systems, the extremal KMS$_\infty$-states are arithmetic points whose evaluations recover explicit class field theory.

### Proof

Item (1) is CMR Part II, Proposition 3.10. `CMR1.pdf`  
Item (2) is stated explicitly in CMR Part II in the discussion preceding the CM theorem. `CMR1.pdf`  
Item (3) is exactly the BC theorem and the CM theorem quoted above. `cmr0.pdf` `cmr0.pdf` ∎

So even before one speaks about any BCM generalization, there is already a proved bridge between the arithmetic systems relevant here.

---

# 6. Final precise statement

The correct rigorous replacement for the earlier sketch is:

## Theorem 6.1 - Exactness of the KMS bridge in the proved arithmetic cases

In the BC and CM systems, the unresolved/branch distinction is not an analogy. It is the exact thermodynamic structure of the KMS simplex.

More precisely:

1. for $0<\beta\le1$, there is a unique KMS$_\beta$-state, and this is the unresolved state;
2. for $\beta>1$, the branch space is the set of extremal KMS$_\beta$-states, with free transitive action of the arithmetic symmetry group;
3. the symmetry-fixed unresolved state for $\beta>1$ is the Haar barycenter of the branch space;
4. at $\beta=\infty$, the branch states evaluate the arithmetic subalgebra in the corresponding maximal abelian extension and carry the class-field-theoretic Galois action.

For BC the symmetry group is $\widehat{\mathbf Z}^{\times}$, and for CM it is $C_K/D_K$. `cmr0.pdf` `cmr0.pdf`

---

## Corollary 6.2 - What is unconditional and what is RH-conditional

- In BC and CM, the bridge is unconditional and fully proved.
- In abstract BCM, the existence of branch states $\Phi_{\beta,y}$ attached to invertible $y$ is unconditional. `Bost-Connes-Marcolli systems.pdf`
- The exact unresolved/branch identification for a general BCM datum is conditional on the corresponding KMS classification theorem.
- If that classification theorem is, for the datum in question, equivalent to RH or GRH, then the exact KMS bridge is correspondingly RH- or GRH-conditional.

That is the precise statement. There is no ambiguity left.

