# Actual mixed-double synchronization: a formal bridge to the Rees workbench

This is a **non-duplicating continuation of Zeta PR #4**, based on commit
`9c47f76b4e3336ee065b691344271b2d150d75ff`. It keeps that PR's original core,
reflection, fibre modules, ideal classification, coordinate maps and presentation
proofs unchanged. The new module is `SplitZeroSynchronization.lean`.

The source is section 2.1 of `workbenches/split-support-rees-trace/RESEARCH_NOTE.md`
in pending PR #3, inspected at commit
`37b2cc9b9baee3ffe25a7649314adb025302509f`. The source already contains the paper
argument. This contribution formalizes its actual maps; it does not claim a new
discovery, assume the main conclusion, or import its later analytic assertions.

## Objects and result

Let A be any commutative ring, S = G(A), and e the supported arithmetic zero.
The structural zero of S is tau. The source's mixed carrier and multiplication are

    D = S × S,
    (a,b) ⋆ (c,d) = (ac + ofR(-1)bd, ad + bc).

Set E=(1,e). The implemented synchronization is

    r(a,b) = (a + eb, b + ea).

The code proves `r(x)=E⋆x`, `E⋆E=E`, and `r(r(x))=r(x)` for this explicit
operation. These are not hypotheses of the strictness theorem.

The amplitude target is the actual quotient algebra

    B = A[t]/(t²+1),

implemented using Mathlib's `AdjoinRoot`. With p:G(A)->A the collapse map,

    p_D(a,b) = p(a) + t p(b).

The code proves `p_D(r(x))=p_D(x)`. For **every subset F of B**, it then proves

    r(p_D⁻¹(F)) = image(r) ∩ p_D⁻¹(F).

The exported theorem `mul_E_strict` states the same equality using the literal
multiplication-by-E function. Hence every level of an amplitude-pullback
filtration satisfies this exact image equality, without any finiteness,
characteristic-zero, or continuity assumption. The source's filtered vector-space
setting is a specialization.

## Complete proof

There are four support cases. The absent pair `(tau,tau)` is fixed. A pair of
supported elements `(ofR(a),ofR(b))` is fixed because e times a supported element
is e and adding e to a supported element changes no amplitude. The mixed pair
`(tau,ofR(b))` is sent to `(e,ofR(b))`, and `(ofR(a),tau)` to `(ofR(a),e)`.
Both resulting pairs are supported and therefore fixed. This proves idempotence.

Expanding E⋆x gives the displayed synchronization formula because
`ofR(-1)*e=e`. Applying p to either coordinate of r gives
`p(a)+p(e)p(b)=p(a)`, respectively `p(b)+p(e)p(a)=p(b)`, since p(e)=0.
Substitution into the literal quotient-algebra amplitude gives amplitude
preservation.

If x lies in the amplitude-pullback set, amplitude preservation shows r(x) lies
there too, and r(x) is in image(r). Conversely, if y belongs to image(r) and the
pullback set, idempotence gives r(y)=y. The element y itself is then a preimage
inside the pullback set. This proves both inclusions and therefore equality.
No section of p_D is chosen.

## Boundaries

This proves strictness of this particular synchronization operation. It does not
prove strictness of an arbitrary cohomological comparison, construct a Rees
module, verify the full mixed-double semiring axioms, establish the tensor or
symmetric-power defect formulas, or certify a completed zeta/trace claim. The
source's conclusion about zero amplitude Rees defect requires the separate Rees
construction and its strictness-to-vanishing identification; those are not
silently counted as Lean theorems here.

The original structural results in PR #4 are credited to that existing
contribution. A parallel foundation experiment at
`codex/splitzero-lean-foundations-20260912` overlaps them and is not a second
library proposed for integration. The recommended implementation path is the
PR #4 package plus this additive synchronization module.

## Reproduction

Use the existing Lean 4.31.0 / Mathlib `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`
workspace in this directory. The additional workflow verifies the unchanged
original-core blob, builds all original modules and the new module, checks the
new source with `--trust=0 -DwarningAsError=true`, and checks every named new
source declaration's transitive axiom report against only
`propext`, `Classical.choice`, `Quot.sound`. It also reruns the original selected
28-declaration audit and its checker tests.

```sh
python3 prepare.py
python3 -m unittest -v test_synchronization_checker.py
python3 check_synchronization.py --prepare
lake update
lake exe cache get
lake -KmaxJobs=1 build
lake env lean --trust=0 -DwarningAsError=true SplitZeroSynchronization.lean
lake env lean --trust=0 -DwarningAsError=true AuditSynchronization.lean > AuditSynchronization.log
python3 check_synchronization.py --log AuditSynchronization.log
```

The additional source-name scanner covers the declaration syntax used by this
single module, not arbitrary Lean syntax or all generated constants. Missing,
duplicate, and nonstandard reports fail. The six synthetic tests exercise the
checker rather than proving the mathematics. Execution status is commit-specific
and is recorded in the PR's exact workflow link, not inferred from this note.
