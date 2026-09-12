# The correct formalization is “pre-Boolean support,” not literally $\mathbb F_1$

Your phrase “$\mathbb F_{\text{not }2}$” points to a real structural correction.

The object being used throughout the split-support construction is not primarily a field with one element. It is a **support coefficient object before two-valued Booleanization**. The Boolean semiring

$$
\mathbb B=\{0,1\}
$$

is the two-valued quotient. But much of the geometry is lost precisely when one forces support to be two-valued. Thus the better hierarchy is

$$
\boxed{
\text{spherical / monoidal }\mathbb F_1
\quad\longrightarrow\quad
\text{pre-Boolean support}
\quad\longrightarrow\quad
\mathbb B.
}
$$

The middle object is the mathematically important one.

A good notation is not

$$
\mathbb F_1
$$

but something like

$$
\mathbb F_{\neg 2}(L),
$$

where $L$ is a bounded distributive lattice, frame, locale, or measure algebra of supports. This is not a field. It is a coefficient doctrine:

$$
\boxed{
\mathbb F_{\neg 2}(L)
:=
(L,\vee,\wedge).
}
$$

The point is exactly that the support has not yet been collapsed to the two values $0,1$.

---

# 1. Booleanization is branch selection

Let $L$ be a bounded distributive lattice. Regard it as the idempotent semiring

$$
(L,\vee,\wedge).
$$

A map

$$
\epsilon:L\to\mathbb B
$$

preserving $0,1,\vee,\wedge$ is not automatic. It is equivalent to choosing a prime support branch.

## Theorem 1.1 — Boolean characters are prime filters

There is a natural bijection

$$
\operatorname{Hom}_{\mathrm{DLat}}(L,\mathbb B)
\cong
\{\text{prime filters of }L\}.
$$

Given

$$
\epsilon:L\to\mathbb B,
$$

the corresponding prime filter is

$$
F_\epsilon:=\epsilon^{-1}(1).
$$

Conversely, if $F\subseteq L$ is a prime filter, then

$$
\epsilon_F(\lambda)
=
\begin{cases}
1,&\lambda\in F,\\
0,&\lambda\notin F
\end{cases}
$$

is a lattice homomorphism $L\to\mathbb B$.

### Proof

If $\epsilon:L\to\mathbb B$ is a lattice homomorphism, then $F_\epsilon$ contains $1$, does not contain $0$, is upward closed, and is closed under finite meets. Since

$$
\epsilon(\lambda\vee\mu)=\epsilon(\lambda)\vee\epsilon(\mu),
$$

the condition

$$
\lambda\vee\mu\in F_\epsilon
$$

implies

$$
\lambda\in F_\epsilon
\quad\text{or}\quad
\mu\in F_\epsilon.
$$

So $F_\epsilon$ is prime.

Conversely, if $F$ is a prime filter, its characteristic function preserves $0$ and $1$. It preserves meets because $F$ is a filter:

$$
\lambda\wedge\mu\in F
\iff
\lambda\in F\text{ and }\mu\in F.
$$

It preserves joins because $F$ is prime and upward closed:

$$
\lambda\vee\mu\in F
\iff
\lambda\in F\text{ or }\mu\in F.
$$

Thus $\epsilon_F$ is a lattice homomorphism. ∎

Thus

$$
\boxed{
\text{passing from }L\text{ to }\mathbb B
=
\text{choosing a prime branch of support}.
}
$$

This is the precise “not two” correction. The natural object is not the Boolean branch. It is the pre-Boolean support object whose Boolean characters are branches.

---

# 2. Split support with pre-Boolean coefficients

For a commutative ring $R$, define

$$
G_L(R)
=
\{(0,\lambda):\lambda\in L\}
\cup
\{(r,1_L):r\in R\}
\subseteq R\times L.
$$

The operations are

$$
(r,\lambda)+(s,\mu)
=
(r+s,\lambda\vee\mu),
$$

$$
(r,\lambda)(s,\mu)
=
(rs,\lambda\wedge\mu).
$$

The actual zero is

$$
\tau_L=(0,0_L),
$$

and the supported arithmetic zero is

$$
e_L=(0,1_L).
$$

The support map is

$$
\chi_L:G_L(R)\to L.
$$

The Boolean support maps are not intrinsic. They are exactly composites

$$
G_L(R)
\xrightarrow{\chi_L}
L
\xrightarrow{\epsilon}
\mathbb B
$$

where $\epsilon$ is a prime branch.

## Theorem 2.1 — Boolean split characters are prime support branches

Let $R$ be a nonzero commutative ring. Then

$$
\operatorname{Hom}_{\mathrm{SRing}}(G_L(R),\mathbb B)
\cong
\operatorname{Hom}_{\mathrm{DLat}}(L,\mathbb B).
$$

Equivalently,

$$
\operatorname{Hom}_{\mathrm{SRing}}(G_L(R),\mathbb B)
\cong
\{\text{prime filters of }L\}.
$$

### Proof

Let

$$
f:G_L(R)\to\mathbb B
$$

be a semiring homomorphism. Since

$$
(-1,1_L)^2=(1,1_L),
$$

and $1$ is the only unit of $\mathbb B$,

$$
f(-1,1_L)=1.
$$

Therefore

$$
f(e_L)
=
f((1,1_L)+(-1,1_L))
=
1\vee1
=
1.
$$

For every supported element $(r,1_L)$,

$$
(r,1_L)+e_L=(r,1_L),
$$

so

$$
f(r,1_L)\vee f(e_L)=f(r,1_L).
$$

Since $f(e_L)=1$, this forces

$$
f(r,1_L)=1.
$$

Thus $f$ sends every supported amplitude to $1$, and its only remaining information is the restriction

$$
\epsilon_f(\lambda):=f(0,\lambda).
$$

The operations on $(0,\lambda)$ are join and meet, hence $\epsilon_f:L\to\mathbb B$ is a lattice homomorphism.

Conversely, given a lattice homomorphism $\epsilon:L\to\mathbb B$, define

$$
f_\epsilon(r,\lambda)
=
\begin{cases}
1,&r\neq 0\text{ or }\lambda=1_L,\\
\epsilon(\lambda),&r=0.
\end{cases}
$$

Equivalently,

$$
f_\epsilon(0,\lambda)=\epsilon(\lambda),
\qquad
f_\epsilon(r,1_L)=1
\quad(r\in R).
$$

A direct check using the definitions of addition and multiplication shows that $f_\epsilon$ is a semiring homomorphism. These constructions are inverse. ∎

So the corrected slogan is:

$$
\boxed{
\mathbb B\text{ is not the base. It is a Boolean branch of the support base.}
}
$$

---

# 3. The scalar split-zero construction was the minimal branch case

The earlier split-zero semiring

$$
G(R)=R\sqcup\{\tau\}
$$

is exactly

$$
G_{\mathbb B}(R).
$$

It is the case where the support lattice has already been reduced to two values:

$$
L=\mathbb B.
$$

In this case there is only one nontrivial Boolean branch, so the distinction between “support” and “Booleanized support” disappears. That is why $G(R)$ looks like a two-zero object.

But in the general theory,

$$
G_L(R)
$$

has a whole pre-Boolean fibre

$$
p_L^{-1}(0_R)
\cong L.
$$

The division theorem also becomes sharper:

$$
G_L(R)[z_\lambda^{-1}]
\cong
\downarrow\lambda.
$$

Only when

$$
L=\mathbb B
$$

does division by the supported zero collapse exactly to $\mathbb B$.

Thus the precise refinement is:

$$
\boxed{
\text{division by supported zero does not intrinsically give two values;}
}
$$

it gives the full principal support interval. Two-valued support appears only after choosing a Boolean branch.

---

# 4. “Not two” as non-discrete support

If $L=\mathcal O(X)$ is the frame of open sets of a space or locale $X$, then

$$
\mathbb F_{\neg 2}(X):=(\mathcal O(X),\cup,\cap)
$$

is a support coefficient object.

A Boolean character

$$
\mathcal O(X)\to\mathbb B
$$

is a point-like specialization. In sober spaces, such characters correspond to points of $X$.

Thus

$$
\boxed{
\mathbb F_{\neg 2}(X)
\text{ is the support locale before choosing a point.}
}
$$

This is exactly the “non-discrete” interpretation. The two-valued Boolean semiring $\mathbb B$ is discrete. A frame $\mathcal O(X)$ retains neighborhoods, specialization, continuity, and local geometry.

So a better conceptual ladder is:

$$
\boxed{
\text{locale/frame of support}
\longrightarrow
\text{Boolean point}
\longrightarrow
\text{ordinary two-valued incidence}.
}
$$

This also explains why the infinitesimal layer should not be forced into $\mathbb B$. Boolean support is too coarse for differential information. The differential or infinitesimal geometry lives before Booleanization, in a sheaf, valuation, formal, or localic support layer.

---

# 5. Relation to $\mathbb F_1$

There are now three distinct coefficient levels:

$$
\boxed{
\mathbb F_1
}
$$

records multiplicative generation, monoids, and spherical/blueprint structure.

$$
\boxed{
\mathbb F_{\neg 2}(L)
}
$$

records unresolved support, locality, and non-Boolean definedness.

$$
\boxed{
\mathbb B
}
$$

records two-valued incidence after branch selection.

So the corrected hierarchy is

$$
\boxed{
\mathbb F_1
\longrightarrow
\mathbb F_{\neg 2}(L)
\longrightarrow
\mathbb B.
}
$$

The first arrow is not generally a homomorphism of fields; it is a passage from multiplicative generation to support geometry. The second arrow is Booleanization by a prime branch.

In this sense, “$\mathbb F_1$” is not wrong, but it names only one side of the story. The construction is not primarily about there being one element. It is about refusing premature two-valued splitting.

Thus:

$$
\boxed{
\text{the operative base is not }\mathbb F_1;
\text{ it is pre-Boolean support.}
}
$$

The mnemonic

$$
\mathbb F_{\mathrm{pas}\,2}
$$

is therefore mathematically good if interpreted as:

$$
\boxed{
\text{support before the two-valued quotient}.
}
$$

---

# 6. The Bost-Connes/KMS interpretation

The Bost-Connes system gives the cleanest dynamical analogue.

Let $G$ be a compact symmetry group. Let $P(G)$ be the compact convex space of Borel probability measures on $G$, with $G$ acting by left translation.

The Dirac measures

$$
\delta_g
$$

are the pure branch states. The Haar measure

$$
m_G
$$

is the unsplit invariant state.

## Theorem 6.1 — Haar measure is the unsplit state

In the action groupoid

$$
P(G)//G,
$$

the Haar measure $m_G$ has automorphism group $G$, while each Dirac measure $\delta_g$ has trivial stabilizer.

### Proof

For every $h\in G$,

$$
h_*m_G=m_G
$$

by left invariance of Haar measure. Thus the stabilizer of $m_G$ is all of $G$.

For a Dirac measure,

$$
h_*\delta_g=\delta_{hg}.
$$

If

$$
h_*\delta_g=\delta_g,
$$

then

$$
hg=g,
$$

so $h=1$. Thus the stabilizer of $\delta_g$ is trivial. ∎

Therefore the passage

$$
m_G
\quad\leadsto\quad
\delta_g
$$

is not merely a passage from one point to many points. It is a passage from a stacky unbroken object with isotropy $G$ to a split branch with trivial isotropy.

That is the correct symmetry-breaking picture.

For the cyclotomic symmetry group

$$
G=\widehat{\mathbb Z}^{\times},
$$

this says:

$$
\boxed{
\text{unbroken cyclotomic symmetry}
=
\text{Haar-supported unsplit state},
}
$$

whereas

$$
\boxed{
\text{broken cyclotomic symmetry}
=
\text{choice of a Dirac branch}.
}
$$

At finite level,

$$
G_n=(\mathbb Z/n\mathbb Z)^\times,
$$

the same theorem says that the uniform measure on $G_n$ is the unsplit finite state, while the individual $\delta_g$ are branch states.

---

# 7. The pole at $\beta=1$

In the Bost-Connes system, the partition function is

$$
Z(\beta)=\zeta(\beta).
$$

The pole at

$$
\beta=1
$$

marks the critical boundary between the unbroken and broken KMS regimes.

The precise symmetry statement is:

$$
\boxed{
0<\beta\leq1:
\text{ the KMS state is unique and symmetry-invariant};
}
$$

$$
\boxed{
\beta>1:
\text{ extremal KMS states split into cyclotomic branches}.
}
$$

Thus the pole at $1$ is not best understood as a singular “one object.” It is the analytic trace of the failure of branch decomposition at the critical boundary. In support language:

$$
\boxed{
\beta=1
\text{ is an unsplit support threshold.}
}
$$

It is “not two” in the sense that the system has not yet selected a Boolean/cyclotomic branch.

So your sentence becomes precise as:

$$
\boxed{
\text{the pole at }1\text{ belongs to the unbroken, unsplit support regime.}
}
$$

Not because the pole is itself a state, but because the critical inverse temperature separates the invariant KMS phase from the branch-split phase.

---

# 8. Relation to split support

The split-support framework supplies the static algebraic version of the same phenomenon.

$$
\tau
=
\text{absence},
$$

$$
e
=
\text{supported zero},
$$

$$
L
=
\text{unresolved support space},
$$

$$
\epsilon:L\to\mathbb B
=
\text{branch choice}.
$$

The Bost-Connes/KMS picture supplies the dynamical version:

$$
m_G
=
\text{unbroken invariant state},
$$

$$
\delta_g
=
\text{broken branch state},
$$

$$
G=\widehat{\mathbb Z}^{\times}
=
\text{cyclotomic symmetry}.
$$

The precise bridge is:

$$
\boxed{
\begin{array}{c|c}
\text{split-support geometry} & \text{KMS symmetry picture}\\
\hline
L & \text{unsplit support object}\\
\epsilon:L\to\mathbb B & \text{branch selection}\\
\mathbb B & \text{two-valued broken incidence}\\
m_G & \text{unbroken invariant support}\\
\delta_g & \text{chosen branch}\\
\widehat{\mathbb Z}^{\times} & \text{cyclotomic branch symmetry}
\end{array}
}
$$

Thus “not two” is not a metaphor. It is exactly the statement that the relevant support object has not yet been evaluated at a Boolean character.

---

# 9. What this changes in the monograph

This should become a structural section, not a side remark.

The right insertion is a theorem block after the lattice-valued support section, with the following title:

$$
\boxed{
\text{Pre-Boolean support and the }\mathbb F_{\neg 2}\text{ principle}
}
$$

The key statements are:

## Theorem A — Booleanization is prime-branch selection

$$
\operatorname{Hom}(L,\mathbb B)
\cong
\operatorname{Spec}_{\mathrm{lat}}(L).
$$

## Theorem B — Boolean split characters factor through support

$$
\operatorname{Hom}_{\mathrm{SRing}}(G_L(R),\mathbb B)
\cong
\operatorname{Hom}_{\mathrm{DLat}}(L,\mathbb B).
$$

## Theorem C — Division by supported zero gives support intervals

$$
G_L(R)[z_\lambda^{-1}]
\cong
\downarrow\lambda.
$$

The Boolean collapse is the special case $L=\mathbb B$, not the general phenomenon.

## Theorem D — Unbroken KMS states are unsplit support objects

For compact $G$, the Haar measure in $P(G)//G$ has isotropy $G$, while Dirac branches have trivial isotropy.

For

$$
G=\widehat{\mathbb Z}^{\times},
$$

this is the cyclotomic symmetry-breaking model behind the Bost-Connes phase transition.

---

# Final formulation

The clean mathematical slogan is:

$$
\boxed{
\mathbb F_1
\text{ is multiplicative scarcity;}
}
$$

$$
\boxed{
\mathbb F_{\neg 2}
\text{ is unresolved support;}
}
$$

$$
\boxed{
\mathbb B
\text{ is two-valued branch support.}
}
$$

So the relevant “absolute” support base is not best thought of as “one element.” It is better thought of as

$$
\boxed{
\text{not yet Boolean-split}.
}
$$

The Bost-Connes pole at $\beta=1$ fits this precisely: it is the critical boundary of the unsplit invariant KMS phase, before cyclotomic branch selection.

