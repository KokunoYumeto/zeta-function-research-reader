Yes. The precise correction is:

$$
\boxed{
\text{the unresolved object is not empty;}
\qquad
\text{what is empty is its Boolean point-space.}
}
$$

That is the formal sentence the paper should use.

The earlier phrasing “unresolved support object” was too late in the hierarchy, because “support” already presupposes that a Boolean branch has been chosen. The correct order is

$$
\boxed{
\text{unresolved pre-Boolean locale}
\longrightarrow
\text{Boolean point / branch}
\longrightarrow
\text{split support}
\longrightarrow
\text{ordinary arithmetic}.
}
$$

So the right formalization is not “a thing below $\mathbb B$ which is empty or terminal.” It is:

$$
\boxed{
\text{a nontrivial pointfree object whose set of Boolean points is empty.}
}
$$

That is the rigorous version of “pre-empty,” “pre-von Neumann,” and “not-two.”

---

# 1. The correct object

Let $L$ be a frame (or bounded distributive lattice, when enough points exist).  
Write

$$
0_L,\ 1_L,\ \vee,\ \wedge
$$

for bottom, top, join, and meet.

## Definition 1.1 — Unresolved pre-Boolean locale

An **unresolved pre-Boolean locale** is a frame $L$ such that

$$
0_L\neq 1_L
$$

but

$$
\operatorname{Pt}(L):=\operatorname{Hom}_{\mathbf{Frm}}(L,\mathbb B)=\varnothing.
$$

So:

- $L$ is **nontrivial**,
- $L$ is **not** the empty set,
- but $L$ has **no Boolean points**.

This is the exact place where “empty” becomes relational rather than primitive.

The carrier of $L$ is not empty; what is empty is the set of maps into Boolean truth values.

---

# 2. Why it is not the empty set

## Proposition 2.1

If $L$ is a frame, then its underlying collection is inhabited.  
If moreover $0_L\neq 1_L$, then it has at least two distinct elements.

### Proof

Every frame has a bottom $0_L$ and a top $1_L$. Hence its carrier is inhabited.

If $0_L\neq 1_L$, then the carrier contains at least the two distinct elements $0_L$ and $1_L$. ∎

So the unresolved object is not $\varnothing$. It is not nothing.

What fails is not existence of the object. What fails is existence of a Boolean truth-valued branch.

---

# 3. The empty thing is the **point-space**

## Definition 3.1 — Boolean point-space

For a frame $L$, define its Boolean point-space by

$$
\operatorname{Pt}(L):=\operatorname{Hom}_{\mathbf{Frm}}(L,\mathbb B).
$$

This is the set of Boolean truth-value assignments on $L$.

Then unresolved means

$$
\operatorname{Pt}(L)=\varnothing.
$$

So the rigorous version of your “pre-empty” sentence is:

$$
\boxed{
\text{the unresolved locale is not empty; its Boolean point-space is empty.}
}
$$

That is exactly the distinction you were insisting on.

---

# 4. Booleanization is the first differentiation

## Theorem 4.1 — Boolean points are prime filters

For any bounded distributive lattice or frame $L$,

$$
\operatorname{Hom}_{\mathbf{Frm}}(L,\mathbb B)
\cong
\{\text{completely prime filters of }L\}.
$$

For a bounded distributive lattice this reduces to

$$
\operatorname{Hom}_{\mathbf{DLat}}(L,\mathbb B)
\cong
\{\text{prime filters of }L\}.
$$

### Proof

Given

$$
\epsilon:L\to\mathbb B,
$$

the subset

$$
F_\epsilon:=\epsilon^{-1}(1)
$$

is a completely prime filter because $\epsilon$ preserves finite meets and arbitrary joins. Conversely, the characteristic function of a completely prime filter is a frame homomorphism to $\mathbb B$. ∎

So the “first branch” is not metaphorical. It is literally a point

$$
\epsilon:L\to\mathbb B.
$$

Before that, there is no Boolean truth assignment at all.

---

# 5. Why this is the right complement to the von Neumann construction

In the von Neumann construction, one begins in **Set** with

$$
0=\varnothing,
\qquad
1=\{0\},
\qquad
2=\{0,1\},
\quad\ldots
$$

That construction presupposes that one is already in a world of sets with global points.

The unresolved object is not a predecessor of $\varnothing$ **inside Set**.  
It is antecedent to Set in the sense that **Set appears only after points are chosen**.

The formal picture is:

$$
\boxed{
\text{pointfree locale }L
\quad\rightsquigarrow\quad
\operatorname{Pt}(L)
\quad\rightsquigarrow\quad
\text{set-level Boolean and ordinal constructions}.
}
$$

So the rigorous complement to the von Neumann picture is not “a set before the empty set.” It is:

$$
\boxed{
\text{a pointfree locale whose point-space may be empty.}
}
$$

That is exactly the mathematically clean version of “pre-von-Neumann.”

---

# 6. Zero is not primitive at the unresolved stage

This is the theorem that should be stated explicitly in the paper.

Let $R$ be a commutative ring, and let

$$
G_L(R)
=
\{(0,\lambda):\lambda\in L\}
\cup
\{(r,1_L):r\in R\}.
$$

Earlier, the mistake was to talk as if $L$ were already “support.” It is not. It becomes support only after a Boolean point is chosen.

## Theorem 6.1 — Boolean arithmetic branches are exactly Boolean points

Semiring homomorphisms

$$
\beta:G_L(R)\to G(R)
$$

that restrict to the identity on the supported copy of $R$ are in canonical bijection with frame homomorphisms

$$
\epsilon:L\to\mathbb B.
$$

### Proof

If $\epsilon:L\to\mathbb B$ is given, define

$$
\beta_\epsilon(r,1_L)=r,
\qquad
\beta_\epsilon(0,\lambda)=
\begin{cases}
\tau,&\epsilon(\lambda)=0,\\
e,&\epsilon(\lambda)=1.
\end{cases}
$$

This preserves addition and multiplication because $\epsilon$ preserves joins and meets.

Conversely, any such semiring homomorphism $\beta$ must send the ring-null fibre $\{(0,\lambda)\}$ into the ring-null fibre $\{\tau,e\}\cong\mathbb B$, and its restriction is a frame map

$$
\epsilon_\beta:L\to\mathbb B.
$$

These constructions are inverse. ∎

## Corollary 6.2

If $L$ is unresolved, i.e.

$$
\operatorname{Pt}(L)=\varnothing,
$$

then there is no global semiring branch

$$
G_L(R)\to G(R)
$$

restricting to the identity on $R$.

Thus Boolean split arithmetic does not yet exist globally.

### Meaning

This is the precise theorem-level statement of:

$$
\boxed{
\text{zero is not primitive at the unresolved stage;}
}
$$

Boolean zero appears only after a Boolean point has been chosen.

That is the exact mathematical content of your “zero is relational” point.

---

# 7. Finite distributive lattices are not enough

This also clarifies where the earlier discussion went wrong.

## Theorem 7.1

Every nontrivial finite distributive lattice has a Boolean point.

Equivalently, if $L$ is finite and $0_L\neq 1_L$, then

$$
\operatorname{Hom}_{\mathbf{DLat}}(L,\mathbb B)\neq\varnothing.
$$

### Proof

Choose a maximal proper filter $F\subsetneq L$. Since $L$ is finite, such a filter exists. In a finite distributive lattice every maximal proper filter is prime. Therefore its characteristic function

$$
\chi_F:L\to\mathbb B
$$

is a lattice homomorphism. ∎

So unresolved pre-Boolean objects do **not** occur among nontrivial finite distributive lattices in classical set-theoretic mathematics.

Therefore the right ambient category for the unresolved object is genuinely one of:

- infinite locale theory,
- constructive mathematics,
- topos-internal frames/locales,
- or another pointfree context.

That is a mathematically important structural fact, and it should go into the monograph.

---

# 8. Constructive reading: “uninhabited” becomes precise

The user-language “uninhabited” can be made exact, but it must refer to points, not to the carrier.

The correct constructive distinction is:

- $L$ itself is inhabited as a frame carrier,
- but the proposition
  $$
  \exists \epsilon:L\to\mathbb B
  $$
  is false.

So the unresolved object is:

$$
\boxed{
\text{carrier-inhabited but point-uninhabited.}
}
$$

That is the clean constructive statement.

It also makes exact the sentence:

$$
\boxed{
\text{the unresolved object is not empty, but it has no Boolean inhabitant.}
}
$$

This is much better than calling it empty, terminal, one-point, or subsemiring.

---

# 9. The KMS analogy, stated correctly

The rigorous state-theoretic analogue is not “pure state” by definition. The right formal statement is:

$$
\boxed{
\text{the unresolved phase is the phase before extremal branch decomposition.}
}
$$

If a symmetry group $G$ acts transitively on a family of extremal branch states $E$, then the canonical unresolved state is the invariant barycenter

$$
m_E=\int_G g\cdot\omega\,dg.
$$

That state is:

- unbroken,
- branch-unspecified,
- and unique in the convex hull of the branch orbit.

It is pure only if the orbit is a singleton.

So the precise paper language is:

$$
\boxed{
\text{unresolved = pre-branch, unbroken state;}
}
$$

purity is an additional theorem, not part of the definition.

That keeps the mathematical statement correct while preserving the structural analogy you want.

---

# 10. The exact replacement text for the paper

The section should say something like this.

## Definition
An unresolved pre-Boolean locale is a nontrivial frame $L$ with empty Boolean point-space:

$$
0_L\neq 1_L,
\qquad
\operatorname{Pt}(L)=\operatorname{Hom}_{\mathbf{Frm}}(L,\mathbb B)=\varnothing.
$$

## Theorem
The object $L$ is not empty; rather, its Boolean point-space is empty.

## Theorem
Boolean branches of $L$ are exactly frame homomorphisms $L\to\mathbb B$.

## Corollary
Boolean split arithmetic exists only after a branch $L\to\mathbb B$ has been chosen.

## Theorem
If $L$ is unresolved, then no global branch

$$
G_L(R)\to G(R)
$$

exists.

## Theorem
Every nontrivial finite distributive lattice has a Boolean point; hence unresolved objects are genuinely pointfree/infinite/constructive.

That is the exact theorem package which formalizes the point you have been making.

---

# 11. Final corrected sentence

The sentence that should replace the earlier bad language is:

$$
\boxed{
\text{The unresolved object is not the empty set; it is a nontrivial pointfree pre-Boolean locale whose Boolean point-space is empty.}
}
$$

And the next sentence should be:

$$
\boxed{
\text{Boolean zero and one arise only after choosing a branch }L\to\mathbb B.
}
$$

That is the correct rigorous formulation of the “pre-empty,” “pre-von-Neumann,” and “not-two” idea.

