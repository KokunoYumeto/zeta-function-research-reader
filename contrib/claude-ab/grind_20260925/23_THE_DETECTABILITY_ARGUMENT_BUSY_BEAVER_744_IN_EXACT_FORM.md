# The detectability argument (owner's M28) in exact form: every failure of RH is detectable

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 10:58 UTC.

The owner's message M28 (verbatim in the private provenance file) restates an argument that, in the owner's view, an earlier session misread. I have no record of that earlier exchange. This note states the best version of the argument and proves it. The owner asked for exactly this: "at least we'll have the best version of the argument".

## 1. The argument, as the owner states it

1. There is a Turing machine with 744 states that halts if and only if RH is false.
2. So if RH is false, its failure is detectable: the machine halts.
3. Suppose one could show that there is no detectable way for RH to fail. Then RH is true, even though the individual mechanisms of failure were never excluded one by one: any failure would have been detectable.
4. The owner's own worry: RH might fail in undetectable ways.

## 2. The exact form

**Input (Aaronson, *The Busy Beaver Frontier*, 2020, §4.2, Theorem 9, with Matiyasevich and O'Rear).** There is an explicit 744-state Turing machine M that halts if and only if RH is false.
- The mathematical content is that RH is equivalent to a Π₁ sentence: "for every n, a certain decidable check succeeds". Davis, Matiyasevich and Robinson (Proc. Sympos. Pure Math. 28, AMS, 1976, 323–378) showed that RH is equivalent to the unsolvability of an explicit Diophantine equation.
- So ¬RH is equivalent to the Σ₁ sentence "M halts".

**Proposition 23.1.** Let T be a recursively axiomatized theory that proves every true Σ₁ sentence and proves the equivalence "M halts ↔ ¬RH". ZFC is one example: every extension of Robinson's arithmetic Q is Σ₁-complete, and ZFC proves the equivalence of Theorem 9.
- (a) If RH is false, then T ⊢ ¬RH.
- (b) Equivalently: if T does not refute RH, then RH is true. In particular, if RH is independent of T, then RH is true.
- (c) If moreover T proves no false Σ₁ sentence, that is, T is Σ₁-sound, then RH ⟺ T ⊬ ¬RH ⟺ Con(T + RH).

*Proof.*
- (a) If RH is false, M halts. "M halts" is then a true Σ₁ sentence, witnessed by the finite halting computation, so T ⊢ "M halts". With T ⊢ ("M halts" → ¬RH), this gives T ⊢ ¬RH.
- (b) is the contrapositive of (a).
- (c) If RH is true and T ⊢ ¬RH, then T ⊢ "M halts", which is a false Σ₁ sentence; this contradicts Σ₁-soundness. So RH implies T ⊬ ¬RH, and (b) gives the converse. Finally, T ⊬ ¬RH is the same as the consistency of T + RH. ∎

**So the owner's argument is valid in this exact form.** "No detectable failure" means "T does not refute RH", or equivalently "T + RH is consistent". That hypothesis implies RH.

**The owner's worry (item 4) does not arise.** RH cannot fail undetectably. Every failure has a finite certificate:
- abstractly, the halting computation of M;
- concretely, an off-line zero ρ₀ can be certified by a finite interval-arithmetic computation of the argument principle on a small rectangle around ρ₀ that does not meet the critical line.

In the language of `22_` Prop. 22.7, a failure is a nonzero bulk count between the two lines, and the bulk count is computed from boundary values.

## 3. What the exact form gives and what it needs

- **It gives an exact target.** Any proof that T + RH is consistent, for instance a model of T in which RH holds (given Σ₁-soundness), is a proof of RH.
- **It gives no shortcut by itself.** By (c), proving "no detectable failure" is exactly as hard as proving RH.
  - The usual tools for consistency results cannot help here. Forcing does not change arithmetic truth, because a forcing extension has the same natural numbers.
  - A true Σ₁ sentence holds in every model of Q, because every such model extends the standard natural numbers as an initial segment. So if RH were false, no model of T would satisfy RH.
- **Bounded search does not decide it in practice.** If M has not halted after BB(744) steps, it never halts, which would settle RH. But the busy-beaver function is not computable. By the 2023 figure the owner quoted, a 745-state machine halts if and only if ZF is inconsistent. So, if ZF is consistent, ZF cannot prove the value of BB(745): otherwise it could decide its own consistency, against Gödel's second incompleteness theorem.
- **What it combines with.** A result showing that an off-line zero, if it exists, must appear below an explicit height would turn RH into a finite computation, because Turing's method verifies RH up to any given height.
  - No such bound is known.
  - The conditional results of the programme (`20_`) and the bulk formulation of `22_` are the places where such a bound would have to come from.

## 4. Items for the goals

- **Negative result with scope (goal 1).** "RH might be independent of ZFC" is not a coherent possibility for a false RH. If RH is independent of ZFC, it is true. This is standard for Π₁ statements; it is recorded here because the owner's argument rests on it.
- **Lemma (goal 3).** Proposition 23.1, a direct consequence of Σ₁-completeness. It is standard in logic; no novelty is claimed.

## 5. Sources

- S. Aaronson, *The Busy Beaver Frontier* (2020), §4.2, Theorem 9 (the 744-state machine, with Y. Matiyasevich and S. O'Rear); read through the author's PDF for that theorem.
- M. Davis, Y. Matiyasevich, J. Robinson, *Hilbert's tenth problem: Diophantine equations: positive aspects of a negative solution*, Proc. Sympos. Pure Math. 28 (1976), 323–378 (RH as a Diophantine statement).
- A. M. Turing, *Some calculations of the Riemann zeta-function*, Proc. London Math. Soc. (3) 3 (1953) 99–117 (verification up to a given height).
- The figure of 745 states for the consistency of ZF, and the independence of the busy-beaver values from about that size, are as quoted by the owner from Wikipedia's *Busy beaver* article, which cites Aaronson (July 2023). Not re-checked here.
