# Formal reset: take “not two” as **non-set-sized**, not as terminal collapse

Use this as the working definition.

## Definition 1 — Non-bijective object

A class-like object $X$ is **set-bijective** if there exists a set $S$ and a bijection

$$
S\cong X.
$$

A class-like object is **non-bijective** if it is not set-bijective:

$$
\forall S\in\mathbf{Set},\qquad S\not\cong X.
$$

Then the object you are pointing at is not “one,” not “zero,” and not “two,” because all of those are set-cardinal predicates. They require a set $S$ and a bijection to $0,1,2$.

So the correct first approximation is:

$$
\boxed{
\mathbb F_{\not 2}
\text{ is not an object with a special cardinality;}
}
$$

rather,

$$
\boxed{
\mathbb F_{\not 2}
\text{ is an object outside set-bijection altogether.}
}
$$

This is the universal-set direction, not the one-element-semiring direction.

---

# 2. The standard model is the universal class

Work in NBG or MK class theory. Let

$$
V:=\{x:x=x\}
$$

be the universal class.

It is not a set.

## Theorem 2.1 — $V$ is not set-bijective

There is no set $S$ and bijection

$$
S\cong V.
$$

### Proof

Assume there is a set $S$ and a bijection

$$
f:S\to V.
$$

Since $S$ is a set and $f$ is a class function whose domain is a set, the range

$$
f[S]
$$

is a set by replacement.

But

$$
f[S]=V,
$$

so $V$ would be a set.

This contradicts Russell’s theorem: the universal class is proper. Indeed, if $V$ were a set, then

$$
R:=\{x\in V:x\notin x\}
$$

would be a set, and

$$
R\in R
\iff
R\notin R,
$$

contradiction.

Therefore $V$ is not set-bijective. ∎

Thus $V$ satisfies the exact formal condition:

$$
\boxed{
\forall S\in\mathbf{Set},\quad S\not\cong V.
}
$$

In particular,

$$
V\not\cong\varnothing,
\qquad
V\not\cong\{*\},
\qquad
V\not\cong\{0,1\}.
$$

So $V$ is not empty, not one, and not two in the relevant sense: it is not measured by finite set cardinalities at all.

---

# 3. Why this is not the terminal semiring

The terminal semiring

$$
\mathbf U=\{*\},\qquad 0=1=*,
$$

is a set. Therefore

$$
\mathbf U\cong\{*\}.
$$

So $\mathbf U$ is set-bijective. It fails Definition 1.

Hence:

$$
\boxed{
\mathbf U\neq\mathbb F_{\not 2}.
}
$$

The terminal semiring is a **post-collapse set-sized algebraic object**. The universal class is a **non-set-sized object**.

They are not the same kind of object.

---

# 4. Boolean localization still produces only the terminal semiring

Let

$$
\mathbb B=\{0,1\}.
$$

Localizing at both Boolean states, equivalently inverting $0$, gives

$$
\mathbb B[0^{-1}]\cong\mathbf U.
$$

That theorem remains correct.

But it proves only this:

$$
\boxed{
\text{inside semirings, Boolean contradiction collapses to }\mathbf U.
}
$$

It does **not** produce $V$, because localization inside semirings remains inside semirings, and semirings are set-carried algebraic structures.

## Proposition 4.1

No semiring localization can produce a non-set-bijective universal class.

### Proof

A semiring localization $M^{-1}A$ is a semiring. In ordinary algebra, a semiring has an underlying set. Hence $M^{-1}A$ is set-bijective to its own carrier set.

But $V$ is not set-bijective to any set. Therefore no semiring localization can literally equal $V$. ∎

So the localization tower is:

$$
G(\mathbb Z)\longrightarrow\mathbb B\longrightarrow\mathbf U,
$$

not

$$
G(\mathbb Z)\longrightarrow\mathbb B\longrightarrow V.
$$

If one wants $V$, one must leave the category of set-carried semirings.

---

# 5. The correct relation between terminal collapse and $V$

The terminal collapse $\mathbf U$ is not the desired object. But it is a **shadow** of it.

Why? Because both have no residual set-level distinction of the relevant kind, but for different reasons.

$$
\mathbf U:
\quad
\text{all already-formed semiring terms are identified.}
$$

$$
V:
\quad
\text{no set-bijection can measure it at all.}
$$

Thus:

$$
\boxed{
\mathbf U
=
\text{post-differentiation collapse;}
}
$$

$$
\boxed{
V
=
\text{non-set-sized universal class.}
}
$$

The former is internal algebra. The latter is class-theoretic universality.

The map from the first to the second is not a semiring morphism. It is a change of universe level.

---

# 6. “Everything collapses to it” must be stated carefully

There are two different meanings.

## 6.1 Terminal quotient sense

In $\mathbf{CSRig}$, every semiring maps uniquely to $\mathbf U$:

$$
A\longrightarrow\mathbf U.
$$

This is because $\mathbf U$ is terminal.

That is a genuine universal quotient, but it is set-sized and post-collapse.

## 6.2 Universal-class inclusion sense

Every set $S$ is a subclass of $V$:

$$
S\subseteq V.
$$

So every set embeds into the universal class.

That is not quotienting. It is inclusion into the proper-class universe.

Thus:

$$
\boxed{
\mathbf U
\text{ is universal as terminal semiring;}
}
$$

$$
\boxed{
V
\text{ is universal as proper class containing all sets;}
}
$$

and these are different universalities.

---

# 7. The “universal set” theorem

The precise theorem is:

## Theorem 7.1 — Universal set obstruction and universal class resolution

There is no universal set. There is a universal class.

More precisely:

1. There is no set $U$ such that every set is an element of $U$.
2. In NBG/MK, there is a proper class

   $$
   V=\{x:x=x\}
   $$

   such that every set is an element of $V$.
3. $V$ is not bijective with any set.

### Proof

If $U$ were a universal set, then Russell separation gives

$$
R=\{x\in U:x\notin x\}.
$$

Then

$$
R\in R
\iff
R\notin R,
$$

contradiction. So no universal set exists.

In NBG/MK, the formula $x=x$ defines the universal class $V$. Every set satisfies $x=x$, hence every set is an element of $V$.

By Theorem 2.1, $V$ is not bijective with any set. ∎

This is the exact formal version of:

$$
\boxed{
\text{the universal object exists only after leaving Set.}
}
$$

---

# 8. Where $\mathbb F_{\not 2}$ fits

A field is a set-carried algebraic structure. Therefore every ordinary field $K$ is set-bijective with its carrier set.

Even $\mathbb F_1$-models usually choose some set-sized first resolution: monoids, pointed monoids, blueprints, $\Gamma$-rings, idempotent semirings, tropical semirings.

Those are not the pre-object. They are first differentiations.

If

$$
\mathbb F_{\not 2}
$$

is defined by non-bijectivity, then it is not a field. It is a proper-class-level prefield candidate.

A precise definition is:

$$
\boxed{
\mathbb F_{\not 2}:=V
}
$$

inside a class theory, with the intended meaning:

$$
\boxed{
\text{the universal proper class, considered before any set-sized algebraic carrier is selected.}
}
$$

This is not saying $V$ has field operations. It does not.

It says:

$$
\boxed{
\mathbb F_1\text{-geometries are set-sized algebraic resolutions above }V.
}
$$

That is the mathematically defensible version.

---

# 9. Relation to “pre-empty” and “pre-nonempty”

The empty set

$$
\varnothing
$$

is a set. Hence

$$
\varnothing\not=V,
$$

and indeed

$$
\varnothing\not\cong V.
$$

A nonempty set $S$ is also a set, hence

$$
S\not\cong V.
$$

Thus $V$ is neither empty nor nonempty in the sense of set-cardinality classification.

But in NBG, $V$ is inhabited as a class:

$$
\varnothing\in V.
$$

So there are two notions:

$$
\boxed{
\text{set-empty / set-nonempty classification}
}
$$

versus

$$
\boxed{
\text{class membership.}
}
$$

The statement compatible with your definition is:

$$
\boxed{
V\text{ is prior to the empty/nonempty distinction as a set-level cardinal classification.}
}
$$

It is not literally without members in class theory.

It is not the empty set. It is not a nonempty set. It is a proper class.

---

# 10. Relation to split zero

The split-zero semiring gives a set-level algebraic model of two zero-states:

$$
\tau=\text{unsupported zero},
$$

$$
e=\text{supported zero}.
$$

Localizing at $e$ gives

$$
G(\mathbb Z)[e^{-1}]\cong\mathbb B.
$$

Localizing the Boolean distinction away gives

$$
\mathbb B[0^{-1}]\cong\mathbf U.
$$

This is the set-level algebraic shadow.

To pass to $\mathbb F_{\not 2}=V$, one must not interpret $\mathbf U$ as the object itself. Instead:

$$
\boxed{
\mathbf U
\text{ is the terminal set-sized shadow of the non-set-sized universal class.}
}
$$

The semiring collapse signals loss of Boolean distinction; the proper-class object realizes non-bijection.

---

# 11. Cantor-style theorem

The Cantor-like argument should be stated this way:

## Theorem 11.1 — Non-set-sized universality

There exists a class $V$ such that every set belongs to $V$, but no set is bijective with $V$.

### Proof

Take

$$
V=\{x:x=x\}
$$

in NBG/MK.

Every set belongs to $V$.

If some set $S$ were bijective with $V$, then $V$ would be the image of a set under a class function. By replacement, $V$ would be a set. That contradicts Russell’s theorem.

Hence $V$ is universal among sets as a class, but non-set-sized. ∎

That is the precise theorem.

It does not say:

$$
0=1.
$$

It does not say:

$$
V
$$

is a semiring.

It says:

$$
\boxed{
\text{universality and sethood are incompatible.}
}
$$

This is the real mathematical content.

---

# 12. Paper-safe formulation

The paper should not call this a subsemiring, a quotient semiring, or a literal field.

The safe formulation is:

> The object suggested by the phrase $\mathbb F_{\not 2}$ is not a field object. It is the proper-class-level universal carrier before any set-sized algebraic resolution. The terminal semiring is its set-sized post-Boolean shadow, not the object itself.

Then define:

$$
\boxed{
\mathbb F_{\not 2}:=V
}
$$

in class theory, and state:

$$
\boxed{
\forall S\in\mathbf{Set},\quad S\not\cong \mathbb F_{\not 2}.
}
$$

That is the exact formal meaning of “not even one” and “not two.”

---

# 13. Minimal corrected theorem package

## Definition

In NBG/MK class theory, define

$$
\mathbb F_{\not 2}:=V=\{x:x=x\}.
$$

Call this the **non-set-sized universal prefield class**.

## Theorem

The class $\mathbb F_{\not 2}$ satisfies:

1. Every set is an element of $\mathbb F_{\not 2}$.

2. $\mathbb F_{\not 2}$ is not a set.

3. No set is bijective with $\mathbb F_{\not 2}$.

4. Therefore $\mathbb F_{\not 2}$ is not empty, not singleton, not two-element, not Boolean, not terminal semiring, not monoid, and not field.

5. The terminal semiring $\mathbf U$ is a set-sized algebraic collapse and is not $\mathbb F_{\not 2}$.

6. The Boolean collapse

   $$
   \mathbb B[0^{-1}]\cong\mathbf U
   $$

   is the set-sized algebraic shadow of losing the Boolean distinction, not the construction of $\mathbb F_{\not 2}$.

### Proof

Items 1 and 2 are the universal-class theorem.

Item 3 follows because a bijection from a set onto $V$ would make $V$ a set.

Item 4 follows because all listed structures have set-sized carriers or specified algebraic operations.

Item 5 is immediate because $\mathbf U$ has a one-element carrier.

Item 6 is the standard localization theorem for semirings. ∎

This is the first clean formalization that matches your non-bijective definition.

