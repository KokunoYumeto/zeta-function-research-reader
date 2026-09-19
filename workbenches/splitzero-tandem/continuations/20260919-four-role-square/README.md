# Four ways to combine identity and absorber

The originating question is to adjoin an element by specifying what it does under addition and multiplication. The complete square is:

| Addition ↓ / Multiplication → | Identity | Absorber |
|---|---|---|
| **Identity** | **ε:** (x+\varepsilon=x,;x\varepsilon=x) | **𝒯:** (x+\mathcal T=x,;x\mathcal T=\mathcal T) |
| **Absorber** | **u:** (x+u=u,;xu=x) | **Ω:** (x+\Omega=\Omega,;x\Omega=\Omega) |

Boolean zero and one realize the 𝒯 and u roles with addition OR and multiplication AND. The other diagonal also exists: on a power set, use union for both operations. The empty set is then an identity for both, and the whole underlying set is an absorber for both. These are exact realizations of the role equations.

The original idea was an adjoined “trivial number,” subsequently denoted 𝒯: addition leaves the other number unchanged, while multiplication returns the adjoined element. The originating manuscript has recorded publication date **12 July 2025**. Its original title and terminology are retained in the [origin record](https://zenodo.org/records/17555345). The Ω construction is actually present in [an earlier deposited version of the same work](https://zenodo.org/records/17547186), specifically `5.tex`, Sections 9–10. The first step of this continuation was to recover those definitions and check their actual rules.

## What the four adjunctions preserve

Start with a nonzero commutative ring (R), its ordinary zero (e=0_R), and (S_R=R\sqcup\{\mathcal T\}).

| Role adjoined | Exact result for the original arithmetic |
|---|---|
| **𝒯** | (R) embeds with all its old sums and products. Its old zero remains the local additive identity of the ring component; 𝒯 is the new global additive identity and multiplicative absorber. |
| **Ω** | (S_R) embeds with all its old sums and products. Ω absorbs both operations globally, so (\mathcal T\Omega=\Omega). The old multiplicative absorption by 𝒯 holds on (S_R). The full structure satisfies commutativity, associativity, distributivity and both identity laws. |
| **u** | Allowing the old multiplicative identity to become local, the universal receiving algebra is the chain (t<c<u), with maximum as addition and minimum as multiplication. 𝒯 maps to (t); every ring element maps to (c). Distributivity forces that merger of ring amplitudes. Keeping the old unit global further identifies (c=u), giving exactly Boolean support. |
| **ε** | Allowing both old identities to become local, the universal receiving algebra has two elements (\varepsilon<c), with maximum for both operations. The whole old (S_R) maps to (c). The two operations share the new identity ε. |

The phrase “local identity” has an explicit meaning here: the old operation equations still hold on the old subcarrier. A global identity must act on every element of the enlarged carrier. Uniqueness of identities and absorbers means four distinct elements cannot satisfy the entire square globally for one pair of operations; the square generates four precisely posed adjunction problems.

## What is retained by the original Ω extension

Let (H_R=R\sqcup\{\mathcal T,\Omega\}), with the original Ω rules. There are two exact observations:


| State | Arithmetic observation (q) | Three-state observation (\sigma) |
|---|---|---|
| (r\in R) | (r) | (1) |
| (\mathcal T) | (0_R) | (0) |
| (\Omega) | (\bot) | (\infty) |


The arithmetic codomain is (R\sqcup\{\bot\}), with ⊥ absorbing both operations. The three-state codomain extends the Boolean algebra by a global absorber ∞, including (0\infty=\infty). Both observations preserve addition, multiplication, zero and unit in the explicitly specified category. Their pair is injective. The fibre of (\sigma=1) recovers the original ring, including its zero and additive inverses.

Identifying 𝒯 with (e) gives exactly the absorbing extension (R\sqcup\{\bot\}). That is the (+,\cdot,0,1) part of Bergstra and Tucker's construction (\mathsf{Enl}_{\bot}(R)), defined in [Section 2.1 of *On the Axioms of Common Meadows*](https://doi.org/10.1093/comjnl/bxac026). The proof here supplies the exact quotient and the retained extra state. It does not infer division, a real-line topology, or an RH estimate from the symbol “infinity.”

The extension also preserves every ring homomorphism exactly: (R\mapsto H_R) is fully faithful in its stated category. Its congruences are classified by two copies of the ring-ideal lattice and the universal congruence. Under the original nonempty-ideal convention, its spectrum contains the old spectrum as a closed subspace and has one further open dense point. For (R=\mathbb Z), its prime chain has length three:

\[
\{\Omega\}\subsetneq\{\mathcal T,\Omega\}
\subsetneq\{e,\mathcal T,\Omega\}
\subsetneq p\mathbb Z\cup\{\mathcal T,\Omega\}.
\]

These establish precisely what the third state retains. They recover and extend the original exploration; they are not claims that adjoining a formal absorber is historically new.

## Complete proofs and date codes

- **SZ-20260919-011:** the complete role square, examples and common-identity universal receiver — [FOUR_ROLE_SQUARE.tex](FOUR_ROLE_SQUARE.tex).
- **SZ-20260919-012:** the exact u-adjunction and Boolean specialization — [ADDITIVE_ABSORBER_MULTIPLICATIVE_IDENTITY.tex](ADDITIVE_ABSORBER_MULTIPLICATIVE_IDENTITY.tex).
- **SZ-20260919-013:** the recovered literal Ω construction, universal property, all congruences and full faithfulness — [INDEPENDENT_OMEGA_EXTENSION.tex](INDEPENDENT_OMEGA_EXTENSION.tex).
- **SZ-20260919-014:** the arithmetic/support pair, common-meadow comparison and exact spectral receiver — [OMEGA_OBSERVERS_AND_SPECTRUM.tex](OMEGA_OBSERVERS_AND_SPECTRUM.tex).

The sources contain complete proofs. [The finite checker](check_finite_models.py) also exhausts the algebra laws on examples over ℤ/2ℤ, ℤ/3ℤ and ℤ/4ℤ, checks the paired observation, and enumerates all congruences in those examples. The [receipt](FINITE_MODEL_CHECKS.json) records their scope. These finite checks supplement the general proofs.

This note records a user-directed foundational investigation. The existing RH estimates and unfinished analytic calculations retain their prior status. The earlier request for a clear mathematical programme overview, and the work of understanding the wider preceding corpus, remain outstanding.
