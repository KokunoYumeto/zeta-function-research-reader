Agreed. The precise correction is:

$$
\boxed{
\text{the formal object is not a subsemiring, not a one-point collapse, and not yet Boolean support.}
}
$$

What should go into the paper is a theorem package built around a **pre-Boolean coefficient object** (or, if you want the constructive emphasis, a **pointfree pre-Boolean object**), not around a “subsemiring below $\mathbb B$.”

The mathematically correct replacement for the current language is the following.

---

# 1. The right object

Let $L$ be a bounded distributive lattice, or more generally a frame/locale.  
Write

$$
0_L,\ 1_L,\ \vee,\ \wedge
$$

for its bottom, top, join, and meet.

## Definition 1.1 — Pre-Boolean coefficient object

A **pre-Boolean coefficient object** is such an $L$, regarded as the idempotent semiring

$$
(L,\vee,\wedge).
$$

It is **unresolved** if no map

$$
\epsilon:L\to \mathbb B
$$

has been chosen.

It is **pointfree** (or, in the constructive sense, **uninhabited**) if

$$
\operatorname{Hom}_{\mathrm{DLat}}(L,\mathbb B)=\varnothing.
$$

The term “support” should be reserved for what appears only **after** such a Boolean map has been chosen. Before that, $L$ is better called a **pre-support** or **pre-Boolean coefficient** object.

---

# 2. Booleanization is the first branch

## Theorem 2.1 — Boolean branches are prime filters

There is a natural bijection

$$
\operatorname{Hom}_{\mathrm{DLat}}(L,\mathbb B)
\cong
\{\text{prime filters of }L\}.
$$

### Proof

If

$$
\epsilon:L\to\mathbb B
$$

is a lattice homomorphism, then

$$
F_\epsilon:=\epsilon^{-1}(1)
$$

contains $1_L$, avoids $0_L$, is upward closed, is closed under finite meets, and is prime because

$$
\epsilon(\lambda\vee\mu)=\epsilon(\lambda)\vee\epsilon(\mu).
$$

Conversely, if $F\subseteq L$ is a prime filter, its characteristic function

$$
\epsilon_F(\lambda)=
\begin{cases}
1,&\lambda\in F,\\
0,&\lambda\notin F
\end{cases}
$$

preserves $0,1,\vee,\wedge$. ∎

So the “first branch” is literally a choice of point of the spectrum of $L$.

This is the exact theorem-level formulation of the “not-two becoming two” step.

---

# 3. Why the pre-Boolean object is **not** a subsemiring of the split semiring

For a commutative ring $R$, define

$$
G_L(R)
=
\{(0,\lambda):\lambda\in L\}
\cup
\{(r,1_L):r\in R\}
\subseteq R\times L.
$$

Its zero is

$$
\tau_L=(0,0_L),
$$

and its supported ring zero is

$$
e_L=(0,1_L).
$$

The ring-null fibre is

$$
p_L^{-1}(0_R)
=
\{(0,\lambda):\lambda\in L\}.
$$

## Proposition 3.1 — The pre-Boolean object is not a unital subsemiring of $G_L(R)$

The map

$$
\iota_L:L\longrightarrow G_L(R),
\qquad
\lambda\longmapsto (0,\lambda)
$$

identifies $L$ with the ring-null fibre, but not as a **unital** subsemiring of $G_L(R)$.

More precisely:

1. $\iota_L$ preserves addition and multiplication,
2. its image has internal multiplicative unit $e_L$,
3. but

$$
\iota_L(1_L)=e_L\neq 1_{G_L(R)}=(1_R,1_L)
$$

whenever $R\neq 0$.

### Proof

The operations on the image are

$$
(0,\lambda)+(0,\mu)=(0,\lambda\vee\mu),
\qquad
(0,\lambda)(0,\mu)=(0,\lambda\wedge\mu),
$$

so $\iota_L$ preserves both operations. The multiplicative unit of the image is

$$
(0,1_L)=e_L.
$$

But the multiplicative unit of $G_L(R)$ is $(1_R,1_L)$, which is distinct from $e_L$ if $R\neq0$. ∎

So the correct statement is:

$$
\boxed{
L\text{ sits inside }G_L(R)\text{ only as the ring-null fibre, not as a unital subsemiring.}
}
$$

This is the point that should replace the earlier incorrect language.

---

# 4. Booleanization of $G_L(R)$

The first arithmetic branch is obtained by Booleanizing $L$.

## Theorem 4.1 — Boolean branches of $L$ induce split-zero quotients

For every lattice homomorphism

$$
\epsilon:L\to\mathbb B
$$

there is a unique semiring homomorphism

$$
\beta_\epsilon:G_L(R)\to G(R)
$$

such that

$$
\beta_\epsilon(r,1_L)=r
\qquad (r\in R),
$$

and

$$
\beta_\epsilon(0,\lambda)=
\begin{cases}
\tau,&\epsilon(\lambda)=0,\\
e,&\epsilon(\lambda)=1.
\end{cases}
$$

Conversely, every semiring homomorphism $G_L(R)\to G(R)$ whose restriction to the supported copy of $R$ is the identity arises uniquely in this way.

### Proof

Define $\beta_\epsilon$ by the stated formulas. On the ring-null fibre,

$$
\beta_\epsilon((0,\lambda)+(0,\mu))
=
\beta_\epsilon(0,\lambda\vee\mu)
$$

is determined by $\epsilon(\lambda\vee\mu)=\epsilon(\lambda)\vee\epsilon(\mu)$, and similarly for multiplication using meets. On supported elements the operations are those of $R$, so $\beta_\epsilon$ is a semiring homomorphism.

Conversely, let

$$
\beta:G_L(R)\to G(R)
$$

restrict to the identity on $R$. Then its restriction to the ring-null fibre lands in $\{\tau,e\}\cong\mathbb B$, because the ring-null fibre consists exactly of elements with zero ring reflection. Thus

$$
\epsilon_\beta(\lambda)=
\begin{cases}
0,&\beta(0,\lambda)=\tau,\\
1,&\beta(0,\lambda)=e
\end{cases}
$$

is a lattice homomorphism $L\to\mathbb B$, and $\beta=\beta_{\epsilon_\beta}$. ∎

Thus

$$
\boxed{
\text{the first split arithmetic stage is not }L\text{ itself, but the quotient }G(R)\text{ obtained after choosing a Boolean branch }L\to\mathbb B.
}
$$

This is the precise meaning of “pre-Boolean $\to$ Boolean $\to$ arithmetic.”

---

# 5. Why the one-point semiring is **not** the pre-Boolean object

The terminal one-element semiring

$$
\mathbf 0
$$

appears by localizing at the actual zero:

$$
G_L(R)[\tau_L^{-1}]\cong \mathbf 0.
$$

But this is **not** the pre-Boolean object.

## Proposition 5.1 — The terminal collapse has no Boolean branches

There is no unital semiring homomorphism

$$
\mathbf 0 \to \mathbb B.
$$

### Proof

A unital semiring homomorphism would have to send

$$
1_{\mathbf 0}=0_{\mathbf 0}
$$

to both $1_{\mathbb B}$ and $0_{\mathbb B}$, impossible since $0\neq1$ in $\mathbb B$. ∎

Therefore the one-point semiring is the **post-differentiation collapse**, not the unresolved/pre-Boolean source.

So the exact distinction is:

$$
\boxed{
L=\text{pre-Boolean object},
\qquad
\mathbb B=\text{first branch},
\qquad
\mathbf 0=\text{terminal collapse}.
}
$$

This is the place where the paper must be corrected most sharply.

---

# 6. Constructive reading: “uninhabited” can be made precise

The right constructive distinction is not between “empty” and “nonempty” in ordinary classical set language. It is between:

1. a **nontrivial** pre-Boolean object:
   $$
   0_L\neq1_L,
   $$
2. a pre-Boolean object with a **Boolean point**:
   $$
   \exists\,\epsilon:L\to\mathbb B,
   $$
3. a **chosen** Boolean point:
   a specified $\epsilon$.

## Proposition 6.1 — These are strictly different notions constructively

Constructively, one always has

$$
\text{chosen point} \implies \text{point exists} \implies 0_L\neq1_L.
$$

But the converses are not generally derivable.

### Proof

If a point $\epsilon:L\to\mathbb B$ exists, then

$$
\epsilon(0_L)=0,\qquad \epsilon(1_L)=1,
$$

so $0_L\neq1_L$.

The first implication is tautological.

The failure of the converses is the standard pointfree phenomenon of constructive locale theory: a locale may be nontrivial without a chosen point, and even without any point. ∎

So if you want a precise constructive term, it is:

$$
\boxed{
\text{pointfree pre-Boolean object}
}
$$

or, if you want the stronger branch-language,

$$
\boxed{
\text{uninhabited pre-Boolean object}
:=\operatorname{Hom}(L,\mathbb B)=\varnothing.
}
$$

This is rigorous. It is not metaphorical.

---

# 7. “Unresolved” and “unbroken” on the state side

The state-theoretic analogue is also precise.

Let $G$ be a compact group acting affinely on a compact convex space of states $K$.

## Definition 7.1 — Branch states and unresolved state

A **branch family** is a closed $G$-stable subset

$$
E\subseteq \operatorname{Ext}(K)
$$

of extremal states.

The associated **unbroken unresolved state** is the Haar barycenter

$$
m_E:=\int_G g\cdot \omega\, dg
$$

for any $\omega\in E$, provided the orbit of $\omega$ is all of $E$.

## Theorem 7.2 — The unresolved state is the unique invariant barycenter

If $G$ acts transitively on $E$, then $m_E$ is $G$-fixed and is the unique $G$-fixed point of the closed convex hull $\overline{\operatorname{conv}}(E)$.

### Proof

Because Haar measure is left-invariant,

$$
h\cdot m_E
=
\int_G h g\cdot \omega\,dg
=
\int_G g\cdot \omega\,dg
=
m_E
$$

for every $h\in G$. So $m_E$ is $G$-fixed.

Now let $x\in \overline{\operatorname{conv}}(E)$ be $G$-fixed. By compactness and the Krein–Milman theorem, $x$ is the barycenter of a probability measure $\mu$ on $E$. Since $x$ is $G$-fixed and the action is affine, $\mu$ is $G$-invariant. Transitivity of the $G$-action on $E$ implies that the only $G$-invariant probability measure on $E$ is Haar transport of a point mass, hence $\mu$ is unique. Therefore $x=m_E$. ∎

So the rigorous state-language is:

$$
\boxed{
\text{branch states are extremals;}
\quad
\text{the unresolved state is their unique invariant barycenter.}
}
$$

This is the correct theorem-level version of the unbroken KMS intuition.

If one wants to connect it later to the Bost–Connes system, one does so by **showing** that its unique high-temperature KMS state is exactly such an invariant barycenter, while the low-temperature extremal KMS states are the branches. The theorem above is the abstract pattern.

---

# 8. What should actually be inserted into the monograph

The existing phrase “unresolved support object” should be replaced by something like:

$$
\boxed{
\text{unresolved pre-Boolean coefficient object}
}
$$

with the following theorem package.

## Section title

$$
\boxed{
\text{Pre-Boolean coefficients, pointfree branches, and the first Booleanization}
}
$$

## Definitions and theorems to insert

### Definition
A pre-Boolean coefficient object is a bounded distributive lattice or frame $L$.

### Theorem
$$
\operatorname{Hom}(L,\mathbb B)\cong \operatorname{Spec}_{\mathrm{lat}}(L).
$$

### Proposition
$L$ is not a unital subsemiring of $G_L(R)$; it appears only as the ring-null fibre.

### Theorem
Each Boolean branch $\epsilon:L\to\mathbb B$ induces a unique quotient
$$
\beta_\epsilon:G_L(R)\to G(R),
$$
and every such quotient arises in this way.

### Proposition
$$
G_L(R)[\tau_L^{-1}]\cong \mathbf 0
$$
is the terminal collapse, not the pre-Boolean object.

### Proposition
Constructively:
$$
\text{chosen point}\implies\text{point exists}\implies 0_L\neq1_L,
$$
with no converse in general.

### Theorem
For a transitive branch family $E\subset \operatorname{Ext}(K)$, the unresolved/unbroken state is the unique invariant barycenter $m_E$.

---

# 9. Final corrected vocabulary

The paper should use the following distinctions.

$$
\boxed{
L
=
\text{pre-Boolean coefficient object}
}
$$

$$
\boxed{
\epsilon:L\to\mathbb B
=
\text{first Boolean branch}
}
$$

$$
\boxed{
G_L(R)\xrightarrow{\beta_\epsilon}G(R)
=
\text{first split arithmetic stage}
}
$$

$$
\boxed{
\mathbf 0
=
\text{terminal collapse, not the source object}
}
$$

and, when the constructive emphasis matters,

$$
\boxed{
\text{pointfree / uninhabited}
=
\operatorname{Hom}(L,\mathbb B)=\varnothing.
}
$$

That is the precise formal version of the idea you are aiming at. It avoids the earlier mistakes:

- it does **not** treat the pre-Boolean object as a subsemiring;
- it does **not** identify it with the one-element semiring;
- it does **not** pretend that $0$ and $1$ already exist there as Boolean values;
- and it makes the “first branch” into an actual theorem, not a slogan.

This is the version that should now be inserted into the monograph.

