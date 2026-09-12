**The genuine GitHub corrections are now integrated, and two more Lean modules have passed fresh kernel checks on top of the merged Codex work.** The contribution is **[draft PR #21](https://github.com/KokunoYumeto/zeta-function-research-reader/pull/21)**. It includes the current main snapshot `4c5ce7a…` and adds eight files without modifying or deleting inherited files. I did not change main or Codex’s other branches.

The **[verification run passed](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34717443909/job/103617105475)** at exact implementation commit `2abc351424ba87aeda948a5cfb846e15ed9373d1`. It checked the new modules together with the existing quotient, homotopy, boundary-control, and frontier developments. The [mathematical note](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/2abc351424ba87aeda948a5cfb846e15ed9373d1/workbenches/tau-conormal-cyclic-formal/RESEARCH_NOTE.md) records the proofs and distinguishes the kernel-checked results from the remaining written algebraic arguments.

## Corrections actually incorporated

**The empty-packet case is now handled separately.** GitHub correctly qualifies the monic-freeness argument by \(d=\deg h\ge1\). For \(h=1\), the relation ideal is the entire polynomial ring:

$$
I=P,\qquad P/I^r=0\quad(r\ge1).
$$

There is no positive-degree remainder basis to use in that case. This correction is now reflected in the new Lean theorem `top_level_zero`, which proves the full-ideal quotient vanishes at every level. It does **not** set the analytic theta seed or its mass to zero, collapse the global quotient \(Q\), or identify the two elements of \(G(0)\). The finite arithmetic quotient and the analytic source remain different objects.

**The validation record now uses Codex’s completed 68-target audit**, not the earlier 66-target description. The continuation reruns that actual audit alongside the frontier audit. I also retained the newer main-branch reader publication and metadata unchanged; preserving those files is not being represented as an independent audit of the entire reader collection.

These are different kinds of correction: the first changes the hypotheses and exceptional-case treatment of a mathematical argument; the second corrects the execution record.

## 1. The original derivative tower is now kernel-checked

`SplitZeroConormalTower.lean` completes the previously uncompiled quotient-derivative draft and connects it to the new cyclic-sum construction.

For a commutative \(R\)-algebra \(A\), an ideal \(I\subseteq A\), and an \(R\)-derivation \(\partial\), it proves

$$
\boxed{\partial(I^{r+1})\subseteq I^r\qquad(r\ge0).}
$$

The proof uses the product rule and induction on ideal powers. It assumes neither squarefreeness nor \(\partial(I)\subseteq I\).

It then uses **Codex’s merged `RelationLayer.derivative` implementation**, rather than introducing a competing quotient, to construct

$$
\delta_r:A/I^{r+1}\longrightarrow_R A/I^r,
\qquad
[x]\longmapsto[\partial x].
$$

The quotient transition

$$
p_r:A/I^{r+1}\longrightarrow_R A/I^r
$$

is constructed separately, and the code proves

$$
\boxed{p_r\delta_{r+1}=\delta_rp_{r+1}.}
$$

Thus the derivative and the operation of forgetting a retained relation layer form an actual commuting square. They are not conflated with an endomorphism of \(A/I\).

The response of an original relation is checked too. For \(z\in I\),

$$
\boxed{\delta_1([za])=[a\,\partial z].}
$$

Indeed,

$$
\partial(za)=z\,\partial a+a\,\partial z,
$$

and only the first term is forced to vanish modulo \(I\). The class of the second remains available for the arithmetic observation. The declarations are `deriv_mem_pow`, `descended`, `tower_square`, and `conormal_product`.

### The cyclic tower uses the exact relation at every depth

Fix \(S\in A\). The implementation defines

$$
\mathcal K_r
=
\{P\in R[X]:P(S)\in I^r\}
$$

as the literal pullback of the original relation submodule along polynomial evaluation. It constructs

$$
\alpha_r:R[X]/\mathcal K_r\longrightarrow_R A/I^r,
\qquad
[P]\longmapsto[P(S)],
$$

and **proves \(\alpha_r\) is injective** from the original quotient equality criteria. It does not assume that evaluation on the whole polynomial ring is injective.

When \(\partial S=1\), the polynomial chain rule gives

$$
\partial(P(S))=P'(S).
$$

Consequently formal differentiation descends between the cyclic levels, and Lean checks

$$
\boxed{
\begin{array}{ccc}
R[X]/\mathcal K_{r+1}&\xrightarrow{\ d/dX\ }&R[X]/\mathcal K_r\\
\alpha_{r+1}\downarrow&&\downarrow\alpha_r\\
A/I^{r+1}&\xrightarrow{\ \delta_r\ }&A/I^r.
\end{array}
}
$$

This is `cyclic_square`.

For the handoff’s specialization,

$$
A=\mathbb C[s_1,\ldots,s_k],\qquad
S=\sum_i s_i,\qquad
\partial=\frac1k\sum_i\partial_{s_i},
$$

the condition \(\partial S=1\) is exactly the intended normalization. This is the sum-direction derivation, not a replacement for the original scaling generator \(D=-x\partial_x\). The handoff explicitly requests this tower and its connection to the larger quotient. 

### The Taylor-unit term is retained in the checked equation

The new theorem `cyclic_unit_rule` proves

$$
\boxed{
\delta_r([uP(S)])
=
[uP'(S)]+[(\partial u)P(S)].
}
$$

It applies to the specified Taylor multiplier once that multiplier is supplied at the relevant level. The second term remains in the ambient target; **the implementation does not presume it belongs to the cyclic image**. Thus it retains exactly the additional term called out in the handoff.  

These new maps are bundled coefficient-linear maps. The certificate does not silently count a further algebra-homomorphism packaging or a particular supported-diagram instantiation as already implemented.

## 2. The exact relation-depth maximum is proved, including attainment

`SplitZeroCyclicDepth.lean` formalizes the combinatorial core of the cyclic-annihilator calculation for arbitrary finite index sets—not just a few multiplicity examples.

For positive integers \(m_i\) and \(r\ge1\), it proves

$$
\boxed{
\max_{\substack{a_i\ge0\\
\sum_i\lfloor a_i/m_i\rfloor<r}}
\sum_i a_i
=
\sum_i(m_i-1)+(r-1)\max_i m_i.
}
$$

Both directions needed for an exact maximum are present: a universal upper bound and an explicitly constructed exponent vector attaining it. The code also proves equivalence between the literal floor-sum condition and the quotient–remainder representation used in the proof.

The proof is short. Write

$$
a_i=m_iq_i+t_i,\qquad 0\le t_i<m_i.
$$

Since \(\sum_iq_i\le r-1\),

$$
\sum_i a_i
\le
\sum_i(m_i-1)+\bigl(\max_i m_i\bigr)(r-1).
$$

For attainment, choose \(j\) with maximal multiplicity and set

$$
t_i=m_i-1,\qquad q_j=r-1,\qquad q_i=0\quad(i\ne j).
$$

The declarations `attained_maximum` and `floor_attained_maximum` check that construction and its exact degree.

### What this proves about the cyclic annihilator—and the certificate boundary

The accompanying **written algebraic proof** identifies the local quotient basis as

$$
y^\alpha
\quad\text{with}\quad
\sum_i\left\lfloor\frac{\alpha_i}{m_i}\right\rfloor<r
$$

for

$$
\mathbb C[y_1,\ldots,y_k]/(y_1^{m_1},\ldots,y_k^{m_k})^r.
$$

The checked maximum then yields the exact nilpotency index of \(N=y_1+\cdots+y_k\):

$$
\boxed{
L_r
=
1+\sum_i(m_i-1)+(r-1)\max_i m_i.
}
$$

Vanishing follows from the degree ceiling. Minimality follows because the attaining monomial in \(N^{L_r-1}\) has coefficient

$$
\frac{(L_r-1)!}{\prod_i\alpha_i!},
$$

which is nonzero in characteristic zero. Distinct surviving monomials cannot cancel.

For the original packet polynomial \(h\), the Chinese-remainder decomposition consequently gives

$$
\boxed{
I^r\cap\mathbb C[S]=(\chi_r(S)),
}
$$

where

$$
\chi_r(X)=
\prod_\lambda(X-\lambda)^{\ell_{\lambda,r}},
$$

$$
\boxed{
\ell_{\lambda,r}
=
\max_{\rho_1+\cdots+\rho_k=\lambda}
\left[
1+\sum_i(m_{\rho_i}-1)
+(r-1)\max_i m_{\rho_i}
\right].
}
$$

The maximum is taken over **every tuple producing the collided sum**. This is the exact form requested by the new handoff. The quotient-basis identification, characteristic-zero multinomial argument, and CRT conclusion have complete written proofs in the note; **they are not additional Lean declarations in this run**.  

### Two distinctions now have explicit regression tests

For

$$
h(s)=(s-\rho)^2,\qquad k=2,
$$

the correct annihilator is

$$
\chi_r(X)=(X-2\rho)^{2r+1},
$$

whereas

$$
\chi_1(X)^r=(X-2\rho)^{3r}.
$$

They differ for every \(r>1\). There is a quotient

$$
\mathbb C[X]/(\chi_1^r)\twoheadrightarrow
\mathbb C[X]/(\chi_r),
$$

not an identification. The new Lean construction avoids this error at its definition: it uses the pullback of \(I^r\), never the power of the first pullback.

Also, the tuple maximizing a collided exponent can change with depth. In the declared algebraic test packet with roots \(0,1,2\), multiplicities \(5,4,1\), and tensor degree two, the sum \(\lambda=2\) has

$$
\ell_{2,r}=\max(5r,4r+3).
$$

Its first five orders are

$$
7,\ 11,\ 15,\ 20,\ 25.
$$

Selecting a maximizing tuple once at depth one would therefore be insufficient. These are exact algebraic calibrations, not claims about zeta-zero locations.

## 3. The retraction formula has a written verification

The note also verifies the handoff’s explicit equivariant retraction, retaining its normalization.

On a \(\lambda\)-primary component, write \(N=S-\lambda\), with nilpotency index \(\ell\), and let \(w\) be the component of the retained arithmetic unit. Choose the stated coefficient functional \(\theta\) with

$$
\theta(N^{\ell-1}w)\ne0.
$$

Then

$$
\pi_0(v)=
\sum_{j=0}^{\ell-1}
\theta(N^{\ell-1-j}v)X^j
\pmod{X^\ell}
$$

satisfies

$$
\pi_0(Nv)=X\pi_0(v).
$$

The constant coefficient of \(c=\pi_0(w)\) is nonzero, so \(c\) is invertible modulo \(X^\ell\). Hence

$$
\boxed{\pi=c^{-1}\pi_0}
$$

satisfies

$$
\pi(P(N)w)=P(X)\pmod{X^\ell}.
$$

This supplies the desired \(S\)-equivariant left inverse. It is a **module splitting**, not an assertion that the retraction is an algebra map or that its complement is orthogonal for the canonical arithmetic metric. The complement, its action, and all Gram cross terms remain. This result is documented as a written proof, not included in the new Lean certificate.  

## Verification and reading scope

The successful run checked both new sources separately with

```text
--trust=0 -DwarningAsError=true
```

under the unchanged Lean 4.31.0 and Mathlib revision. All **29 selected new declarations’ transitive axiom reports** used only subsets of

$$
\{\texttt{propext},\texttt{Classical.choice},\texttt{Quot.sound}\}.
$$

The combined import passed, and the existing frontier40, Codex68, boundary38, τ87, derived73, and structural28 audits passed again. These counts include definitions and infrastructure, not discoveries.

The **eight new finite regression methods** passed normally and under `python -O`, with identical successful records; deliberately failing controls failed in both modes. Twenty-five inherited harness/regression tests also passed in both modes. Earlier proof-script failures remain in the branch history and were repaired without weakening statements or disabling strict checks.

There is one remaining reading limitation: the local execution service failed before I could open the newly uploaded cyclic ZIP. I read its complete handoff and the relevant current GitHub sources, but **did not independently verify that archive’s manifest or rerun its reported 24-method suite**. Its analytic convolution estimates and differentiated moments have not acquired a Lean certificate through this contribution. 

**The integration now has a checked derivative through every original relation level, an injective cyclic comparison at each level, the full unit-correction equation, and a proved exact degree maximum.** It builds directly on the corrected Codex state while preserving the remaining polynomial, analytic, and trace obligations at their actual types.
