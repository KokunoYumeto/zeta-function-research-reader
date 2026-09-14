# Exact PR32 source and verification scope

Checked implementation: 8e78bc7c240b04d297ade6afdadfd863e0c6db7b.
Final supplied head: 9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6.
PR: https://github.com/KokunoYumeto/zeta-function-research-reader/pull/32
Run: https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34891954305

The complete four new Lean modules and full written research note follow.
The module imports resolve in the linked repository at the exact commit;
this flat reading file does not claim to be a standalone Lean checkout.
Files02/03/09/10/14 provide the complete written mathematical proof closure.
The analytic estimates and the polynomial-gcd dimension corollary are
outside this Lean certificate. Root independently read all four modules,
the full research note and runner, observed both successful CI jobs and
verified that the checked-to-final comparison changes no Lean or test file.


## workbenches/tau-observation-kernel-formal/RESEARCH_NOTE.md

SHA256: 7ab72341f8cb05b98959e75d89ea9bfe8047e0c228178a8bf961607ab73aa9f9

# Original observation: corrected kernel norms and complete iterated detection

14 September 2026. This is a complementary research/formalization continuation, not a replacement for the concurrent analytic source. The source baseline is main `5a2fa7d6fc2db3133601dccbeed77785792be5d4`; the full OPG1–26 and OPR1–5 addendum and NEXT_RECEIVING_INTERFACE were read at that immutable revision. Their body blobs are respectively `e719d7666011b94eb5b653fd04689c98b6d4cf7e` and `20456dcb5c5a3a0a6cfbdbfd90186bf683ef7726`. The branch also retains the complete PR31 head `b4060b25c21f1a49a5e7730e9aff76d4c93c820d` and its PR30 ancestry. Actual execution is recorded separately in STATUS; writing a proof here does not make it a Lean certificate.

## 1. What the new source supplies

The uploaded check-in report ends before the current Original Volumes source cut. Current main reports the original baseline and quantitative Gamma return completed at their stated scales, including the nonzero m=1 centre and its nonvanishing limsup radius. This note does not independently re-prove that equilibrium/Hankel asymptotic analysis or relabel its written proof as a kernel check. The source-only OPG/OPR addendum is separate from the fixed 75-page PDF. The canonical source orders remain s=1 and s=k.

We use its actual observation

    Lambda:E -> B=im(P_k Pi^(tensor k) U^(tensor k) iota),
    E=C[S]/chi,  A=M_S,  Y=(A-kI/2)/i.

The full unit U=M_(j_h(2xi/h)), all primary jets, original periods and orientations, tensor inclusion and finite cyclic average remain in Lambda. No freely chosen replacement row is used in an arithmetic application. The infinite theta quotient remains upstream of E. An observation kernel inside E is not identified with the original theta boundary.

OPG supplies the normalized polynomial classes e_d, observed columns lambda_d=Lambda e_d, covariance M_D=sum_(d<D)lambda_d lambda_d*, and their complete coupled recurrence with the fixed-section kernel coordinates. OPR supplies the correction from those coordinates to the actual minimum-section residual. These are the two finite interfaces formalized here.

## 2. The minimum observation section and the whole residual Gram

Let G be the original positive Gram on E, K=G^(-1), Lambda:E->B the stated surjection onto its actual image, and

    Q=(Lambda K Lambda*)^(-1),   S_G=K Lambda* Q.

The new Data.sectionMap is exactly the inherited Restriction.representative constructor with source G and observation Lambda. It gives

    Lambda S_G=1,   S_G* G=Q Lambda,   S_G* G S_G=Q.

For any rectangular family X of coefficient vectors, put Z=Lambda X and R=X-S_G Z. Then

    Lambda R=0,
    R* G S_G=0,
    R* G R=X* G X-Z* Q Z.                                  (OK1)

Proof. The first equation uses Lambda S_G=1. The second follows by adjoint from G S_G=Lambda*Q and Lambda R=0. Expanding the full Gram, the two cross terms and the section Gram are each Z*QZ. The expansion leaves exactly the right side of OK1. In particular it is positive semidefinite by congruence of the positive original G. This is a matrix identity, including all off-diagonal mixed entries, not only a list of scalar norms. For any competing lift S_G Z+R' with Lambda R'=0, its Gram is Z*QZ+R'*GR'; positivity also proves the unique minimum property. Empty B gives S_G=0 and R=X.

Retain the source's fixed section S_* and actual kernel maps I:Kern(Lambda)->E, kappa:E->Kern(Lambda), with

    I kappa=1-S_* Lambda.

Then the exact relation to the metric section is

    R=I(kappa X-kappa S_G Lambda X).                        (OK2)

Indeed I kappa S_G=S_G-S_*, and expansion cancels the two occurrences of S_*Lambda X. For D=q+j and X=e_D, this is precisely OPR2, not the generally false formula R=I kappa e_D. If theta=kappa e_D-kappa S_G lambda_D and H^K=I*GI, then

    theta* H^K theta=e_D*G e_D-lambda_D*Q lambda_D=t_j-xi_j.

Consequently OPR's ordered factors are

    1+xi_j,   1+(t_j-xi_j)/(1+xi_j),

and their product is exactly 1+t_j. The denominator, old degree D-1 and elimination order remain. Nothing assigns one factor the asymptotic coefficient of their combined product.

## 3. A raw observation kernel need not carry the arithmetic action

For a linear observation L:V->W and action A:V->V define

    K_inf=intersection_(n>=0) ker(L A^n),
    O_q(x)=(Lx,LAx,...,LA^(q-1)x).

K_inf is A-stable and lies in ker L. Conversely every A-stable submodule P contained in ker L lies in K_inf: all A^n x remain in P. Thus K_inf is the largest invariant submodule inside the literal one-step kernel, rather than an assumption that the one-step kernel was invariant.

If the original polynomial supplies

    A^q=sum_(j<q)c_j A^j,

strong induction proves that the first q observations determine every later one. For n>=q, multiply this same relation by A^(n-q); all resulting powers j+n-q are strictly smaller than n. Hence

    ker O_q=K_inf.                                         (OK3)

This includes a typed q=0 case: the supplied relation then forces id=0. The arithmetic monic polynomial has q>0. Its original coefficients, not inferred eigenvalues, provide the recurrence. The quotient action on V/K_inf is constructed from proved stability. The standard first-isomorphism map to im O_q is intertwining; its concrete target shift has the original coefficients c_j in its last component. The general quotient action and finite determination are Lean targets here. The explicit companion-shift realization and its inverse are written consequences and exact regression targets, not additional claimed Lean declarations.

In OPG the action Y is an invertible affine transform of A. The spans of 1,A,...,A^(q-1) and 1,Y,...,Y^(q-1) agree by their triangular binomial coefficient change with nonzero diagonal. Therefore both yield the same finite and infinite invisible kernel. This fact retains the centre k/2 and factor i; neither is assigned a different value.

## 4. Additional result: calculate the invisible kernel by the existing residue pairing

This section is an additional deduction joining OPG23 to the previously verified monic residue duality; it is not attributed as a new claim in OPG.

Let chi be monic of degree q>0 over a field and E=K[S]/chi. Retain

    ell(x)=[S^(q-1)] rem_chi(x).

The inherited MonicResidue.residueEquiv proves that x -> (y -> ell(yx)) is an actual linear equivalence E -> E*. It uses the literal AdjoinRoot quotient and the leading-coefficient monomial detection argument, including repeated factors.

Choose the specified coordinate rows lambda_mu of the actual observation Lambda. Define, using that proved inverse,

    a_mu=residueEquiv^(-1)(lambda_mu),
    lambda_mu(x)=ell(x a_mu).                              (OK4)

Then

    K_inf={x : a_mu x=0 for every mu}.                      (OK5)

Proof. If all these products vanish, every lambda_mu(A^n x)=ell(S^n x a_mu) vanishes. Conversely, if one product a_mu x is nonzero, the existing monomial detection theorem supplies n<q with ell(S^n a_mu x) nonzero. The corresponding one of the first q observations is nonzero. This proves both OK5 and concrete finite determination without assuming a separate recurrence or diagonalization.

The implementation constructs a_mu by the actual residue equivalence and proves both implications. It also proves injectivity of O_q from a literal Bezout witness sum b_mu a_mu=1 in E. This witness is a required arithmetic input, not a field set to true by purity terminology.

### Written polynomial and primary calculation

For a finite row family, take its unique monic-remainder representatives a_mu(S), and put

    d=gcd(chi,a_1,...,a_r),  monic.

The ideal generated by the a_mu in E is (d)/(chi). Therefore

    K_inf=(chi/d)/(chi),
    E/K_inf = K[S]/(chi/d),
    dim K_inf=deg d,   rank O_q=q-deg d.                    (OK6)

To verify the annihilator formula directly, write chi=d b. Then d x=0 modulo chi precisely when d b divides d x in the polynomial domain, equivalently b divides x. This proves the stated ideal and the explicit quotient map; its kernel is exactly K_inf. For no observation rows the convention d=chi gives K_inf=E and zero observed quotient. There is no artificial nonempty observation.

At a root alpha of chi with multiplicity m_alpha, let

    nu_alpha=min(m_alpha, min_mu ord_alpha(a_mu)).

Its invisible submodule is the actual ideal (z^(m_alpha-nu_alpha)) inside K[z]/z^m_alpha; it has dimension nu_alpha. Its observed quotient has length m_alpha-nu_alpha. Thus no nilpotent jet is removed without a displayed kernel.

A particularly useful complete criterion is

    O_q is injective
      iff Lambda(e_alpha (S-alpha)^(m_alpha-1)) != 0
          for every primary alpha.                       (OK7)

Indeed the top primary class has nonzero residue. Multiplying it by a_mu leaves precisely a_mu(alpha) times that class. So its observation is nonzero exactly when at least one a_mu is a unit in that primary factor, equivalently nu_alpha=0. Each alpha may use a different detecting row. It is not necessary that one boundary row be faithful on the full packet.

A one-step-zero vector may be seen later; for example ell(1)=0 in K[z]/z^4, but ell(A^3 1)=1. Conversely, when every row kills a primary socle class, all of its iterates remain killed, because A acts scalarly on that class. Delayed observation cannot resurrect that permanently invisible direction.

OK6--7 and their CRT/gcd dimension interpretation are complete written consequences, with exact repeated-root regressions. They are not additional general polynomial-gcd declarations in the present Lean audit. No claim is made that the actual transcendental period/unit rows already satisfy d=1. Their certification needs their actual values or rigorous nonvanishing estimates.

## 5. Explicit reconstruction and the original metric, without selecting a new one

Suppose a literal Bezout identity in E is supplied:

    sum_mu b_mu a_mu=1.

Then for every x,y in E,

    ell(yx)=sum_mu lambda_mu(b_mu y x).                     (OK8)

Reduce b_mu y in the original power basis. Each term on the right becomes an explicit combination of the first q observed iterates of x. Applying the inverse residue equivalence reconstructs x itself. Equation OK8 supplies a written left inverse of the stack O_q, not just a rank count. Its coefficients include the actual row polynomials and Bezout coefficients; no condition-number bound is inferred from existence of that inverse.

For positive W on the original observation image, the finite Gram

    H_obs=sum_(r<q) (A^r)* Lambda* W Lambda A^r

has kernel K_inf: its quadratic form is a sum of nonnegative squared observed norms. It is positive definite on the resulting quotient. This is an additional observation of the original data, not a substitute for G. If O_q is injective with actual left inverse T, transport the specified G through T on im O_q. That is the isometric transported metric. The independently specified product metric W on the observed outputs need not equal it. Estimates comparing these metrics remain explicit quantitative obligations.

The metric residual OK1 and the dynamical kernel OK5 also remain different objects. The former subtracts the current G-minimum section from one source vector; the latter retains vectors undetectable under all operator iterates. Neither construction sets the mixed kernel/boundary pairing to zero except where the displayed canonical orthogonality actually proves it.

## 6. Original SplitZero integration

The original scalar G(R)={tau} disjoint-union R^bullet, e=0^bullet, arithmetic coefficient square and infinite theta quotient remain unchanged. For original coefficient diagrams D,E, a natural observation obs and natural action A, the new invisibleRelations has fibre K_inf,i and uses the old transports. Equivariance transports every observed power, proving stability without assuming injective support maps.

The existing Relations.quotientDiagram constructs D/K_inf. The new actionHom, observationHom and forgetIterates prove the total G(R)-linear squares

    actionHom q_inf = q_inf A,
    observationHom q_inf = obs,
    forgetIterates q_inf = q_raw.

Here q_raw is the separate quotient by ker(obs). The source class of x not in K_inf but with obs(x)=0 remains nonzero in D/K_inf and maps to the zero of its receiving support fibre. At nonbottom support this is not global absence. The existing present-empty-face theorem is reused; it is not replaced by an empty-sum convention.

These quotients are additional observations of the already marked coefficient object. No theorem here says a vector in ker(obs) has an original theta primitive. The original full/restricted boundary comparison of PR31 remains imported and is audited in the combined environment alongside the canonical signed trace and boundary-socle modules.

## 7. Handoff and scope

The concrete next evaluation is on the original OPG lambda_d and their full unit/period data: use OPR's section-corrected vector for the kernel cost, and use OK4--7 to identify exactly which primary jets any proposed observed-iterate realization retains. A simultaneous family of further observations intersects their invisible kernels by adjoining its rows; this does not license deleting the residual intersection.

The independent analytic baseline, Gamma asymptotics, actual period integration, cochain primitives and uniform arithmetic upper estimates retain their own proof scopes. The new result is finite algebra and metric bookkeeping on those actual maps, plus the explicit residue-annihilator criterion. It is neither an RH proof nor a categorical impossibility statement. Current verification, source hashes, negative controls and development failures are reported separately.


## workbenches/tau-observation-kernel-formal/LATEST_INTAKE.md

SHA256: 4cf3b018e693305dee3050710cd126396172b0bbfbbd4927ddfd82ac7ff62c0b

# Concurrent original-kernel continuation and exact source join

14 September 2026. While the new finite proofs were being checked, main advanced from `5a2fa7d6fc2db3133601dccbeed77785792be5d4` to `8fd2157e8b41783224b42781699432d824ec0c15`. The complete commit comparison was read. It modifies six publication/index files and adds the flat `20260914-original-kernel-web` source package; it does not alter an inherited Lean source or workflow. The branch integration preserves those exact changes and both parent histories. It does not merge this contribution into main.

## Reading scope

At the earlier main revision, the complete OPG1–26 and OPR1–5 bodies and NEXT_RECEIVING_INTERFACE were read. At the new main revision, the complete `00_CONTINUE_HERE.md`, all 771 lines of `04_CYCLIC_SECTORS.tex`, and `12_VALIDATION.md` were read. Their Git blobs are respectively `b89cd22db659923f5ef1312e437cb3030a99695c`, `a467c6180cd65ddfc19e40a4eb69805bafd06b47`, and `4a364c0e54b12b55426dde17927128bc58275949`. The other newly mirrored full TeX bodies are preserved, but this is not a claim to have independently audited their entire analytic proofs, source-only builds or reported validation.

The current handoff says the remaining analytic target is the absolute common original-kernel contribution `F_K^(1)/(kq)`, after the stated baseline, Gamma and source-difference results. In particular this continuation does not continue to advertise those earlier source differences as the current unsolved step. Their complete arithmetic verification remains with the analytic source lane.

## The new finite code applies to the precise OCS matrices

OCS17–19 construct the literal observation matrix

    mathfrakA_(nu;(a,b,D)) = i^D D! c_(nu;abD),
    L H = F_0 mathfrakA,

where H is the original primary basis map and F_0 is the injective unscaled zero-charge tensor-coordinate map. The full period matrix, arithmetic unit, symmetrization multiplicities, i^D and D! remain in these entries. No orthonormality of the Fourier frame is asserted: its Gram is N(I+11*), as calculated in OCS4.

OCS37–39 retain the original action J through YH=HJ and form

    mathfrakO = [mathfrakA; mathfrakA J; ...; mathfrakA J^(q-1)].

The already supplied OCS39 identifies `K_inf=H ker(mathfrakO)`. Our ObservedIterates module formalizes this finite-kernel and invariant-quotient mechanism, including its support maps. It does not claim to originate the observed-iterate construction.

The additional ResidueObservation result computes that kernel by the original perfect residue pairing. Use the actual coordinate rows of `mathfrakA H^(-1)` as the lambda_mu in OK4 (equivalently, choose coordinates on im(L) and compose Lambda). Composing with the explicit injective F_0 does not change any of the iterated kernels. The action A and Y=(A-kI/2)/i have the same finite observed-iterate kernel by their invertible triangular binomial change. Thus OK5–7 apply to these exact OCS rows. They reduce the permanently invisible part to the common annihilator, and, in the written polynomial corollary, to `gcd(chi,a_mu)`. The raw kernel and the invariant kernel remain distinct even when a later source calculates the raw kernel's dimension.

This identifies a finite test of which original primary socle lines the actual observation sees. It does not assert that the actual period rows pass that test, bound a reconstruction condition number, or evaluate the common original-kernel volume. The new observation-norm identity retains OPR's corrected kernel vector and the actual source metric for that next analytic calculation.

## Preservation and certification

The observed successful implementation `8e78bc7c240b04d297ade6afdadfd863e0c6db7b` predates this documentation/source-intake reconciliation. The reconciliation changes none of its Lean, runner, finite-checker, workflow or used dependency blobs. Its certificate is stated at that exact implementation; a later run is not claimed before observation. The mirrored analytic source has its own written-proof and validation scope, not inherited Lean certification.


## workbenches/tau-observation-kernel-formal/STATUS.md

SHA256: d8eafed05397ff5514915fa6a0b4cbb187a4bcd70c46782a906e7cef781e4d1b

# Observed strict original-observation verification

14 September 2026. The successful checked implementation is **`8e78bc7c240b04d297ade6afdadfd863e0c6db7b`**. GitHub Actions [run 34891954305](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34891954305) completed with both jobs successful: [verify 104136565071](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34891954305/job/104136565071) and [finite 104136565573](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34891954305/job/104136565573). Both complete terminal logs were read after completion. The verify job completed at approximately 20:22:02 UTC.

This later status/README and concurrent-main source reconciliation changes none of the checked Lean sources, workflow, runner, finite tests or used formal dependencies. No subsequent unobserved run is claimed.

## Exact certificate

The runner individually compiled **33 local Lean modules**, including all four new modules and the complete used local dependency closure, with `--trust=0 -DwarningAsError=true`. The four new modules are:

- `SplitZeroObservationMetric`
- `SplitZeroObservedIterates`
- `SplitZeroObservedIteratesSupport`
- `SplitZeroResidueObservation`

The joint audit imported all four together with the inherited canonical signed-resolvent, boundary-socle and conormal modules. **All 56 selected transitive targets passed: 51 in the four new modules and five inherited proper-boundary/signed-trace targets.** Their axiom sets were subsets of `propext`, `Classical.choice` and `Quot.sound`. Counts include definitions and interface lemmas, not discoveries. This is not a new run of every historical audit.

The exact 33-source order, every dependency SHA-256, all 56 target names and each transitive axiom set are emitted in the public verification log and `.observation-kernel-logs/receipt.json`.

## Unchanged pins and source hashes

Lean **4.31.0**, compiler `68218e876d2a38b1985b8590fff244a83c321783`; Mathlib **`fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`**. Original scalar Git blob **`ff991f7383922e71cdf0e4a3bc85e89e18f808ef`**, 7,366 bytes, SHA-256 `09f8ddf866687f93f384fd234975d1012dffdd6903782095901916607f042f48`. The new source hashes from the actual runner are:

| Source | SHA-256 |
|---|---|
| SplitZeroObservationMetric | `a1ef5765c3c0eebe9cbbb37a3a1812808d3025045b7bf99a0e4f4cc7e61222a8` |
| SplitZeroObservedIterates | `9587a9c6001bb3737756f811f1ed6bc231bac1bac3bc5fdaf011080c4a66251f` |
| SplitZeroObservedIteratesSupport | `d884a2773a44034b4ec4181ff74b36500cdf21bc3ce32c6e765cea6c362a83ed` |
| SplitZeroResidueObservation | `0145aac9efb60ff2288c97015fe46e35a6c165d1935cb690962a975dbac161b3` |

The separate Lean negative control was rejected at the actual equality `SplitZero.e = SplitZero.tau`: `rfl` failed because these original constructors differ. The workflow excludes missing-import, unknown-identifier and instance failures from that control's acceptance.

## Exact finite execution

The new **nine-method** suite passed normally and under `python -O`, with byte-identical success JSON. It constructs the original constrained sections for declared positive, non-diagonal complex matrix fixtures, retains all mixed Gram entries, tests the fixed-section correction and ordered denominator, preserves an explicit mass scaling, and includes the empty boundary image. Its polynomial fixtures include repeated factors, nontrivial observation annihilators, no observation rows, the original companion shift and a vector seen only after a later nilpotent iterate.

Five false formulas were rejected in each mode, with precisely the expected named JSON records: `omit-section-correction`, `diagonal-only`, `omit-denominator`, `one-step-closed`, and `always-faithful`. A generic crash was not accepted instead. The unchanged PR31 ten-method signed suite passed in both modes and its JSON records matched. The unchanged 24 derived/synchronization/tau-recovery checker unittests passed in each mode.

These are exact finite polynomial/matrix calibrations, not evaluations of actual zeta-zero packets, transcendental period coefficients, arithmetic moment intervals or a tensor-uniform estimate. No unchanged analytic delivery archive was independently extracted or rerun in this turn.

## Failures are retained

The two inspected failed candidates and their full-log diagnoses are documented in DEVELOPMENT.md. The first needed the scoped complex positive-order interface and explicit complete Gram rearrangements; the second needed the implicit source vector and membership-proof binders separated in the natural kernel diagram. The intervening residue-only push retained the first uncorrected metric error and is not presented as a distinct mathematical obstruction. All repairs keep the original statements, full cross terms and strict gates.

## Reproduction

From the checked implementation, with the unchanged toolchain installed:

```bash
cd formal/splitzero
python3 prepare.py
lake update
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = fabf563a7c95a166b8d7b6efca11c8b4dc9d911f
lake exe cache get
python3 ../../workbenches/tau-observation-kernel-formal/run_observation.py
```

The committed workflow gives the exact finite replays and negative-control commands. Its GitHub token permissions are read-only, credentials are not persisted, and the action/toolchain pins are unchanged.

## Mathematical scope

Checked: the constructed minimum observation section, full residual Gram and positivity, correction from a fixed section, the ordered scalar factors, the largest invariant observation kernel, finite determination from the original polynomial, its original SplitZero diagram/quotient actions, the concrete monic-residue annihilator characterization, and the conditional injectivity theorem from a literal Bezout witness.

Written, not additional Lean declarations here: the polynomial-gcd and primary-socle corollaries; explicit Bezout reconstruction coordinates; comparison of the resulting observation norm with the original metric; identification with the latest OCS coefficient matrices; the complete analytic construction of those period matrices. No actual-row injectivity, purity transfer, period integration or absolute common-kernel `kq` asymptotic is inferred from the finite certificate.

The branch preserves the complete checked PR31/PR30 ancestry and the current analytic main source without modifying their branch refs. LATEST_INTAKE.md records the concurrent main update and precise reading scope. No main merge was performed.


## workbenches/tau-observation-kernel-formal/run_observation.py

SHA256: a8135ac2c7c5d9a253cf6a478ae90b4b5346b00bb5398ea034681ec3f9bf2258

```python
#!/usr/bin/env python3
"""Compile the real local import closure and audit exact selected declarations."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / 'formal/splitzero'
LOGS = FORMAL / '.observation-kernel-logs'
MODULES = ['SplitZeroObservationMetric', 'SplitZeroObservedIterates',
           'SplitZeroObservedIteratesSupport', 'SplitZeroResidueObservation',
           'SplitZeroCanonicalSignedResolvent', 'SplitZeroBoundarySocleSupport',
           'SplitZeroConormalTower']
TARGETS = {
 'SplitZero.ObservationMetric.Data': ['sectionMap', 'section_observation',
   'section_adjoint', 'section_gram', 'metric_section', 'residual',
   'residual_observation', 'kernel_section_orthogonal', 'residual_gram',
   'residual_difference_positive', 'fixed_section_correction', 'corrected_kernel_gram'],
 'SplitZero.ObservationMetric': ['ordered_factors'],
 'SplitZero.ObservedIterates': ['invisible', 'window', 'observe', 'mem_invisible',
   'mem_window', 'observe_apply', 'ker_observe', 'invisible_le_kernel', 'invariant',
   'largest_invariant', 'all_iterates_of_window', 'finite_determination',
   'quotientAction', 'quotient_action_mk', 'powers_intertwine', 'window_injective_iff',
   'rawRelations', 'invisibleRelations', 'actionHom', 'observationHom',
   'forgetIterates', 'action_square', 'observation_square', 'forget_square',
   'transient_kernel_retained', 'observed_zero_iff', 'observed_output_not_absent',
   'present_empty_face'],
 'SplitZero.ResidueObservation': ['rootAction', 'root_pow_apply', 'observation',
   'rowCoefficient', 'row_formula', 'annihilator_kills_iterate', 'finite_kernel_iff',
   'invisible_kernel_iff', 'original_finite_determination', 'injective_of_bezout'],
 'SplitZero.RestrictedBoundary': ['original_square', 'range_iff_supported_zero', 'proper_residual'],
 'SplitZero.SignedTraceEnclosure': ['weighted_schwarz', 'signed_interval'],
}
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def run(args: list[str], name: str) -> str:
    print('RUN', ' '.join(args), flush=True)
    proc = subprocess.run(args, cwd=FORMAL, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, timeout=420)
    (LOGS / (name + '.log')).write_text(proc.stdout, encoding='utf-8')
    print(proc.stdout, flush=True)
    if proc.returncode:
        raise RuntimeError(f'{name}: exit {proc.returncode}')
    return proc.stdout


def main() -> None:
    LOGS.mkdir(exist_ok=True)
    inherited = ROOT / 'workbenches/tau-signed-resolvent-formal/run_signed.py'
    spec = importlib.util.spec_from_file_location('inherited_screen', inherited)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load the unchanged source-token screen')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    order: list[str] = []
    active: set[str] = set()
    seen: set[str] = set()
    def visit(name: str) -> None:
        if name in seen:
            return
        if name in active:
            raise ValueError('Import cycle: ' + name)
        active.add(name)
        code = mod.code_only((FORMAL / (name + '.lean')).read_text(encoding='utf-8'))
        if re.search(r'\b(sorry|admit|axiom|native_decide)\b', code):
            raise ValueError('Forbidden proof shortcut: ' + name)
        for line in code.splitlines():
            if line.startswith('import '):
                for dep in line.split()[1:]:
                    if (FORMAL / (dep + '.lean')).exists():
                        visit(dep)
        active.remove(name)
        seen.add(name)
        order.append(name)
    for name in MODULES:
        visit(name)
    output = FORMAL / '.lake/build/lib/lean'
    output.mkdir(parents=True, exist_ok=True)
    failures = []
    for name in order:
        try:
            run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                 '-o', str(output / (name + '.olean')), name + '.lean'], name)
        except RuntimeError as exc:
            failures.append(str(exc))
    if failures:
        raise RuntimeError('; '.join(failures))
    targets = [ns + '.' + t for ns, ts in TARGETS.items() for t in ts]
    if len(targets) != len(set(targets)):
        raise ValueError('Duplicate audit target')
    audit = '\n'.join(['import ' + m for m in MODULES] +
                      ['#print axioms ' + t for t in targets]) + '\n'
    (FORMAL / 'AuditObservationKernel.lean').write_text(audit, encoding='utf-8')
    text = run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                'AuditObservationKernel.lean'], 'audit')
    matches = re.findall(r"'([^']+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)", text, re.S)
    if len(matches) != len(targets) or {x[0] for x in matches} != set(targets):
        raise ValueError('Incomplete or unexpected audit coverage')
    axioms = {n: sorted(filter(None, re.split(r'[\s,]+', a.strip()))) for n, a in matches}
    for name, values in axioms.items():
        if not set(values) <= ALLOWED:
            raise ValueError(f'Unapproved axioms for {name}: {values}')
    receipt = {
      'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
      'strict_modules': order, 'selected_targets': len(targets), 'axioms': axioms,
      'sha256': {m: hashlib.sha256((FORMAL / (m + '.lean')).read_bytes()).hexdigest() for m in order},
      'scope': 'Constructed canonical observation section, full corrected kernel Gram, '
               'finite observed-iterate kernel, largest invariant submodule, residue '
               'annihilator detection and original support quotient maps. No arithmetic '
               'periods, moment quadrature or tensor-uniform spectral estimate.'}
    (LOGS / 'receipt.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(json.dumps(receipt, indent=2, sort_keys=True), flush=True)

if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, ValueError, OSError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)

```

## workbenches/tau-observation-kernel-formal/check_exact.py

SHA256: bb7474c67599b8b62a1d4fd85c4b949ff77236099ca185da7b64afdf8d0d8171

```python
#!/usr/bin/env python3
"""Exact finite calibrations; no zeta-zero or arithmetic-integral assertions."""
from __future__ import annotations
import argparse
import json
import sympy as S

x = S.Symbol('x')
I = S.I

def need(value: bool, reason: str) -> None:
    if not value:
        raise AssertionError(reason)

def zero(M: S.Matrix) -> bool:
    return all(S.simplify(a) == 0 for a in M)

def fixture():
    R = S.Matrix([[1,I,1,0],[0,2,1,I],[0,0,1,1],[1,0,0,2]])
    G = R.H * R + S.diag(1,2,3,4)
    K = G.inv()
    L = S.Matrix([[1,0,1,I],[0,1,I,1]])
    Q = (L*K*L.H).inv()
    section = K*L.H*Q
    fixed = L.H*(L*L.H).inv()
    inc = S.Matrix.hstack(*L.nullspace())
    kap = S.Matrix.hstack(inc, fixed).inv()[:inc.cols,:]
    X = S.Matrix([[1,2],[I,1],[2,1-I],[1+I,3]])
    lam = L*X
    residual = X-section*lam
    return G,K,L,Q,section,fixed,inc,kap,X,lam,residual

def metric_section():
    G,K,L,Q,A,_,_,_,_,_,_ = fixture()
    need(zero(L*A-S.eye(2)), 'section observation')
    need(zero(A.H*G-Q*L), 'source dual')
    need(zero(A.H*G*A-Q), 'section Gram')
    need(zero(G*K-S.eye(4)), 'original inverse')

def mixed_residual():
    G,_,L,Q,A,_,_,_,X,lam,r = fixture()
    need(zero(L*r), 'kernel membership')
    need(zero(r.H*G*A), 'kernel-section orthogonality')
    E = X.H*G*X-lam.H*Q*lam
    need(zero(r.H*G*r-E), 'complete residual Gram')
    need(S.simplify(E[0,1]) != 0, 'fixture must have mixed covariance')

def section_correction():
    G,_,L,_,A,T,J,kap,X,lam,r = fixture()
    need(zero(J*kap-(S.eye(4)-T*L)), 'fixed splitting')
    v = kap*X-kap*A*lam
    need(zero(J*v-r), 'OPR section correction')
    need(zero(v.H*(J.H*G*J)*v-r.H*G*r), 'original kernel Gram')
    need(not zero(J*kap*X-r), 'uncorrected section must differ')

def ordered_factors():
    G,_,_,Q,_,_,_,_,X,lam,r = fixture()
    t = S.simplify((X.H*G*X)[0,0])
    xi = S.simplify((lam.H*Q*lam)[0,0])
    a = S.simplify((r.H*G*r)[0,0])
    need(xi > 0 and a > 0 and t == xi+a, 'positive retained costs')
    need(S.simplify((1+xi)*(1+a/(1+xi))-(1+t)) == 0, 'ordered factors')

def mass_scaling():
    G,K,L,Q,A,_,_,_,_,_,_ = fixture()
    scale = S.Rational(7)
    K2 = (scale*G).inv()
    Q2 = (L*K2*L.H).inv()
    need(zero(Q2-scale*Q), 'quotient mass')
    need(zero(K2*L.H*Q2-A), 'section mass invariance')

def empty_boundary():
    G = S.Matrix([[3,1],[1,2]])
    L = S.zeros(0,2)
    Q = S.zeros(0,0)
    A = G.inv()*L.H*Q
    X = S.eye(2)
    r = X-A*L*X
    need(A.shape == (2,0) and zero(r-X), 'empty section convention')
    need(zero(r.H*G*r-G), 'empty boundary leaves whole kernel')

def algebra(chi, rows):
    chi = S.Poly(chi, x, domain=S.QQ).monic()
    q = chi.degree()
    def vector(p):
        r = S.rem(S.Poly(p, x, domain=S.QQ), chi)
        return S.Matrix([r.nth(j) for j in range(q)])
    A = S.Matrix.hstack(*(vector(x**(j+1)) for j in range(q)))
    L = S.zeros(len(rows),q)
    for k,a in enumerate(rows):
        for j in range(q):
            L[k,j] = vector(a*x**j)[q-1]
    O = S.Matrix.vstack(*(L*A**j for j in range(q)))
    d = chi
    for a in rows:
        d = S.gcd(d, S.Poly(a,x,domain=S.QQ))
    d = d.monic()
    need(O.rank() == q-d.degree(), 'residue gcd rank')
    if d.degree():
        p = S.exquo(chi,d).as_expr()
        Z = S.Matrix.hstack(*(vector(p*x**j) for j in range(d.degree())))
    else:
        Z = S.zeros(q,0)
    need(zero(O*Z), 'explicit invisible ideal')
    need(Z.rank() == q-O.rank(), 'entire invisible kernel')
    need(zero(O*A*Z), 'invariance of retained kernel')
    return chi,A,L,O,Z

def residue_rank_cases():
    chi = (x-S.Rational(3,4))**3*(x-S.Rational(1,4))**2
    for rows in [[1],[x-S.Rational(3,4)],
                 [(x-S.Rational(3,4))**2,(x-S.Rational(3,4))*(x-S.Rational(1,4))],[]]:
        algebra(chi,rows)
    algebra((x-1)**4,[(x-1)**2])

def original_shift():
    chi,A,L,O,_ = algebra((x-1)**3*(x+2)**2,[1,x-1])
    q,r = A.rows,L.rows
    T = S.zeros(q*r,q*r)
    for j in range(q-1):
        T[j*r:(j+1)*r,(j+1)*r:(j+2)*r] = S.eye(r)
    for j in range(q):
        T[(q-1)*r:q*r,j*r:(j+1)*r] = -chi.nth(j)*S.eye(r)
    need(zero(O*A-T*O),'original coefficient shift')
    need(zero(O[:r,:]-L),'first component is original observation')

def transient_kernel():
    _,A,L,O,_ = algebra(x**4,[1])
    z = S.Matrix([1,0,0,0])
    need(zero(L*z) and not zero(O*z), 'one-step zero remains observable later')
    need(not zero(L*A**3*z), 'full nilpotent iterate is retained')
    _,_,_,O2,Z2 = algebra(x**4,[x])
    need(O2.rank() == 3 and Z2.cols == 1, 'socle failure is not silently removed')

TESTS = [metric_section,mixed_residual,section_correction,ordered_factors,
         mass_scaling,empty_boundary,residue_rank_cases,original_shift,transient_kernel]

def negative():
    G,_,L,Q,A,_,J,kap,X,lam,r = fixture()
    gram = r.H*G*r
    t = S.simplify((X.H*G*X)[0,0]); xi = S.simplify((lam.H*Q*lam)[0,0])
    _,N,obs,O,_ = algebra(x**4,[1])
    _,_,_,O2,_ = algebra(x**4,[x])
    wrong = {
      'omit-section-correction': zero(r-J*kap*X),
      'diagonal-only': zero(gram-S.diag(*gram.diagonal())),
      'omit-denominator': S.simplify((1+xi)*(1+t-xi)-(1+t)) == 0,
      'one-step-closed': zero(obs*N**3*S.Matrix([1,0,0,0])),
      'always-faithful': O2.rank() == 4,
    }
    for name,value in wrong.items():
        print(json.dumps({'control':name,'false_claim_accepted':bool(value)},sort_keys=True))
    return 1 if all(not value for value in wrong.values()) else 0

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--negative',action='store_true')
    args=parser.parse_args()
    if args.negative:
        raise SystemExit(negative())
    for test in TESTS:
        test()
    print(json.dumps({'status':'pass','methods':len(TESTS),
      'tests':[t.__name__ for t in TESTS],
      'scope':'Exact declared polynomial and matrix fixtures; no arithmetic zero or integral certificate.'},sort_keys=True))

if __name__ == '__main__':
    main()

```

## formal/splitzero/SplitZeroObservationMetric.lean

SHA256: a1ef5765c3c0eebe9cbbb37a3a1812808d3025045b7bf99a0e4f4cc7e61222a8

```lean
import SplitZeroRestrictionSource
import Mathlib.Analysis.Matrix.Order

/-!
# OPR1--4: the original observation section and its retained kernel

The section is the existing `Restriction.representative`, instantiated with
source metric G and observation Lambda. No independently chosen quotient
metric or orthogonality assumption replaces that construction. Rectangular
columns keep every mixed Gram entry; the boundary image may be empty.
-/
noncomputable section
namespace SplitZero.ObservationMetric
open Matrix
open scoped ComplexOrder

variable {e b : Type*} [Fintype e] [DecidableEq e]
  [Fintype b] [DecidableEq b]

/-- The actual source inverse and observed covariance inverse. -/
structure Data (e b : Type*) [Fintype e] [DecidableEq e]
    [Fintype b] [DecidableEq b] where
  G : Matrix e e ℂ
  K : Matrix e e ℂ
  obs : Matrix b e ℂ
  Q : Matrix b b ℂ
  positive : G.PosDef
  hermitianG : G.conjTranspose = G
  hermitianK : K.conjTranspose = K
  hermitianQ : Q.conjTranspose = Q
  left_inverse : K * G = 1
  right_inverse : G * K = 1
  observed_inverse : (obs * K * obs.conjTranspose) * Q = 1

namespace Data
variable (O : Data e b)

/-- The old minimum section, now for the stated boundary observation. -/
def sectionMap : Matrix e b ℂ :=
  Restriction.representative O.obs O.K O.Q

theorem section_observation : O.obs * O.sectionMap = 1 :=
  Restriction.representative_section O.obs O.K O.Q O.observed_inverse

theorem section_adjoint : O.sectionMap.conjTranspose * O.G = O.Q * O.obs :=
  Restriction.representative_adjoint O.obs O.G O.K O.Q
    O.left_inverse O.hermitianK O.hermitianQ

theorem section_gram : O.sectionMap.conjTranspose * O.G * O.sectionMap = O.Q :=
  Restriction.representative_gram O.obs O.G O.K O.Q
    O.left_inverse O.hermitianK O.hermitianQ O.observed_inverse

theorem metric_section : O.G * O.sectionMap = O.obs.conjTranspose * O.Q := by
  simp only [sectionMap, Restriction.representative, ← Matrix.mul_assoc,
    O.right_inverse, Matrix.one_mul]

/-- All columns of X remain, including their off-diagonal pairings. -/
def residual {t : Type*} (X : Matrix e t ℂ) : Matrix e t ℂ :=
  X - O.sectionMap * (O.obs * X)

theorem residual_observation {t : Type*} (X : Matrix e t ℂ) :
    O.obs * O.residual X = 0 := by
  simp only [residual, Matrix.mul_sub, ← Matrix.mul_assoc,
    O.section_observation, Matrix.one_mul, sub_self]

theorem kernel_section_orthogonal {t : Type*} (I : Matrix e t ℂ)
    (hI : O.obs * I = 0) : I.conjTranspose * O.G * O.sectionMap = 0 := by
  rw [Matrix.mul_assoc, O.metric_section, ← Matrix.mul_assoc,
    ← Matrix.conjTranspose_mul, hI, Matrix.conjTranspose_zero, Matrix.zero_mul]

/-- Exact complete mixed Gram subtraction, not merely a scalar norm identity. -/
theorem residual_gram {t : Type*} (X : Matrix e t ℂ) :
    (O.residual X).conjTranspose * O.G * O.residual X =
      X.conjTranspose * O.G * X -
        (O.obs * X).conjTranspose * O.Q * (O.obs * X) := by
  let Z := O.obs * X
  let T := O.sectionMap * Z
  have hXT : X.conjTranspose * O.G * T = Z.conjTranspose * O.Q * Z := by
    dsimp [T, Z]
    rw [Matrix.mul_assoc, ← Matrix.mul_assoc O.G, O.metric_section]
    simp only [Matrix.conjTranspose_mul, Matrix.mul_assoc]
  have hTX : T.conjTranspose * O.G * X = Z.conjTranspose * O.Q * Z := by
    calc
      _ = Z.conjTranspose * (O.sectionMap.conjTranspose * O.G) * X := by
        simp only [T, Matrix.conjTranspose_mul, Matrix.mul_assoc]
      _ = Z.conjTranspose * (O.Q * O.obs) * X := by rw [O.section_adjoint]
      _ = _ := by simp only [Z, Matrix.mul_assoc]
  have hTT : T.conjTranspose * O.G * T = Z.conjTranspose * O.Q * Z := by
    dsimp [T]
    rw [Matrix.conjTranspose_mul]
    calc
      _ = Z.conjTranspose *
          (O.sectionMap.conjTranspose * O.G * O.sectionMap) * Z := by
            simp only [Matrix.mul_assoc]
      _ = _ := by rw [O.section_gram]
  change (X - T).conjTranspose * O.G * (X - T) = _
  calc
    _ = X.conjTranspose * O.G * X - X.conjTranspose * O.G * T -
          (T.conjTranspose * O.G * X - T.conjTranspose * O.G * T) := by
        simp only [Matrix.conjTranspose_sub, Matrix.sub_mul, Matrix.mul_sub]
        abel
    _ = _ := by rw [hXT, hTX, hTT]; dsimp [Z]; abel

theorem residual_difference_positive {t : Type*} [Fintype t] (X : Matrix e t ℂ) :
    (X.conjTranspose * O.G * X -
      (O.obs * X).conjTranspose * O.Q * (O.obs * X)).PosSemidef := by
  rw [← O.residual_gram X]
  exact O.positive.posSemidef.conjTranspose_mul_mul_same _

/-- Fixed-section and metric-section kernels differ by the stated kernel lift. -/
theorem fixed_section_correction {r t : Type*} [Fintype r]
    (I : Matrix e r ℂ) (kap : Matrix r e ℂ) (S : Matrix e b ℂ)
    (hsplit : I * kap = 1 - S * O.obs) (X : Matrix e t ℂ) :
    O.residual X = I * (kap * X - kap * O.sectionMap * (O.obs * X)) := by
  have hkS : I * kap * O.sectionMap = O.sectionMap - S := by
    rw [hsplit, Matrix.sub_mul, Matrix.one_mul, Matrix.mul_assoc,
      O.section_observation, Matrix.mul_one]
  calc
    _ = (1 - S * O.obs) * X - (O.sectionMap - S) * (O.obs * X) := by
      simp only [Matrix.sub_mul, Matrix.one_mul, Matrix.mul_assoc, residual]
      abel
    _ = (I * kap) * X - (I * kap * O.sectionMap) * (O.obs * X) := by
      rw [hkS, hsplit]
    _ = _ := by simp only [Matrix.mul_sub, Matrix.mul_assoc]

/-- A further corrected kernel basis has the original restricted Gram. -/
theorem corrected_kernel_gram {r t : Type*} [Fintype r]
    (I : Matrix e r ℂ) (V : Matrix r t ℂ) (X : Matrix e t ℂ)
    (hV : O.residual X = I * V) :
    V.conjTranspose * (I.conjTranspose * O.G * I) * V =
      X.conjTranspose * O.G * X -
        (O.obs * X).conjTranspose * O.Q * (O.obs * X) := by
  rw [← O.residual_gram X, hV]
  simp only [Matrix.conjTranspose_mul, Matrix.mul_assoc]

end Data

/-- Preserve the denominator and the original boundary-first elimination order. -/
theorem ordered_factors (t xi : ℝ) (hxi : 0 ≤ xi) (hres : xi ≤ t) :
    1 + xi > 0 ∧ 1 + (t - xi) / (1 + xi) ≥ 1 ∧
      (1 + xi) * (1 + (t - xi) / (1 + xi)) = 1 + t := by
  have hp : 0 < 1 + xi := by linarith
  refine ⟨hp, ?_, ?_⟩
  · exact le_add_of_nonneg_right (div_nonneg (sub_nonneg.mpr hres) hp.le)
  · field_simp
    ring

end SplitZero.ObservationMetric

```

## formal/splitzero/SplitZeroObservedIterates.lean

SHA256: 9587a9c6001bb3737756f811f1ed6bc231bac1bac3bc5fdaf011080c4a66251f

```lean
import SplitZeroInternalQuotient
import Mathlib.LinearAlgebra.Quotient.Basic

/-!
# OPG23--24: observing iterates without assuming an invariant raw kernel

`invisible` is the largest A-invariant submodule inside ker(obs). The finite
comparison uses an explicit original polynomial recurrence, not a spectral
normality assumption. The case q=0 is also typed: its recurrence forces id=0.
-/
noncomputable section
namespace SplitZero.ObservedIterates
open scoped BigOperators

variable {R V W : Type*} [CommRing R]
  [AddCommGroup V] [Module R V] [AddCommGroup W] [Module R W]

/-- All source vectors invisible under every iterate of the SAME action. -/
def invisible (obs : V →ₗ[R] W) (A : Module.End R V) : Submodule R V :=
  ⨅ n : ℕ, LinearMap.ker (obs.comp (A ^ n))

/-- The finite window retains the complete tuple of observed vectors. -/
def window (obs : V →ₗ[R] W) (A : Module.End R V) (q : ℕ) : Submodule R V :=
  ⨅ j : Fin q, LinearMap.ker (obs.comp (A ^ j.val))

def observe (obs : V →ₗ[R] W) (A : Module.End R V) (q : ℕ) :
    V →ₗ[R] (Fin q → W) :=
  LinearMap.pi fun j => obs.comp (A ^ j.val)

@[simp] theorem mem_invisible (obs : V →ₗ[R] W) (A : Module.End R V) (x : V) :
    x ∈ invisible obs A ↔ ∀ n : ℕ, obs ((A ^ n) x) = 0 := by
  simp only [invisible, Submodule.mem_iInf, LinearMap.mem_ker, LinearMap.comp_apply]

@[simp] theorem mem_window (obs : V →ₗ[R] W) (A : Module.End R V)
    (q : ℕ) (x : V) :
    x ∈ window obs A q ↔ ∀ j : Fin q, obs ((A ^ j.val) x) = 0 := by
  simp only [window, Submodule.mem_iInf, LinearMap.mem_ker, LinearMap.comp_apply]

@[simp] theorem observe_apply (obs : V →ₗ[R] W) (A : Module.End R V)
    (q : ℕ) (x : V) (j : Fin q) :
    observe obs A q x j = obs ((A ^ j.val) x) := rfl

theorem ker_observe (obs : V →ₗ[R] W) (A : Module.End R V) (q : ℕ) :
    LinearMap.ker (observe obs A q) = window obs A q := by
  ext x
  simp only [LinearMap.mem_ker, mem_window, funext_iff, observe_apply, Pi.zero_apply]

theorem invisible_le_kernel (obs : V →ₗ[R] W) (A : Module.End R V) :
    invisible obs A ≤ LinearMap.ker obs := by
  intro x hx
  simpa using (mem_invisible obs A x).mp hx 0

theorem invariant (obs : V →ₗ[R] W) (A : Module.End R V)
    {x : V} (hx : x ∈ invisible obs A) : A x ∈ invisible obs A := by
  apply (mem_invisible obs A (A x)).mpr
  intro n
  simpa only [pow_succ, Module.End.mul_apply] using
    (mem_invisible obs A x).mp hx (n + 1)

/-- A raw observation kernel need not be stable; this constructs its largest stable part. -/
theorem largest_invariant (obs : V →ₗ[R] W) (A : Module.End R V)
    (P : Submodule R V) (hP : P ≤ LinearMap.ker obs)
    (hA : ∀ x ∈ P, A x ∈ P) : P ≤ invisible obs A := by
  intro x hx
  apply (mem_invisible obs A x).mpr
  intro n
  apply hP
  induction n with
  | zero => simpa using hx
  | succ n ih =>
      simpa only [pow_succ', Module.End.mul_apply] using hA ((A ^ n) x) ih

/-- The literal action polynomial closes all higher observation equations. -/
theorem all_iterates_of_window (obs : V →ₗ[R] W) (A : Module.End R V)
    (q : ℕ) (c : Fin q → R)
    (hpoly : A ^ q = ∑ j : Fin q, c j • A ^ j.val)
    (x : V) (hx : x ∈ window obs A q) :
    ∀ n : ℕ, obs ((A ^ n) x) = 0 := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
      by_cases hn : n < q
      · exact (mem_window obs A q x).mp hx ⟨n, hn⟩
      · have hqn : q ≤ n := Nat.le_of_not_gt hn
        have he : n = q + (n - q) := by omega
        have hr : obs ((A ^ n) x) =
            ∑ j : Fin q, c j • obs ((A ^ (j.val + (n - q))) x) := by
          conv_lhs => rw [he, pow_add, hpoly, Finset.sum_mul]
          simp only [smul_mul_assoc, ← pow_add, LinearMap.sum_apply,
            LinearMap.smul_apply, map_sum, map_smul]
        rw [hr]
        apply Finset.sum_eq_zero
        intro j _
        rw [ih (j.val + (n - q)) (by have := j.isLt; omega), smul_zero]

theorem finite_determination (obs : V →ₗ[R] W) (A : Module.End R V)
    (q : ℕ) (c : Fin q → R)
    (hpoly : A ^ q = ∑ j : Fin q, c j • A ^ j.val) :
    window obs A q = invisible obs A := by
  ext x
  constructor
  · intro hx
    exact (mem_invisible obs A x).mpr (all_iterates_of_window obs A q c hpoly x hx)
  · intro hx
    exact (mem_window obs A q x).mpr fun j => (mem_invisible obs A x).mp hx j.val

/-- The action on the genuine quotient is induced by the proved stability. -/
def quotientAction (obs : V →ₗ[R] W) (A : Module.End R V) :
    Module.End R (V ⧸ invisible obs A) :=
  (invisible obs A).mapQ (invisible obs A) A (fun _ hx => invariant obs A hx)

@[simp] theorem quotient_action_mk (obs : V →ₗ[R] W) (A : Module.End R V) (x : V) :
    quotientAction obs A ((invisible obs A).mkQ x) =
      (invisible obs A).mkQ (A x) := rfl

/-- Intertwining of arbitrary powers, with no injectivity hypothesis on transport. -/
theorem powers_intertwine {V' : Type*} [AddCommGroup V'] [Module R V']
    (T : V →ₗ[R] V') (A : Module.End R V) (A' : Module.End R V')
    (h : ∀ x, T (A x) = A' (T x)) (n : ℕ) (x : V) :
    T ((A ^ n) x) = (A' ^ n) (T x) := by
  induction n with
  | zero => rfl
  | succ n ih =>
      simp only [pow_succ', Module.End.mul_apply, h, ih]

/-- Exact faithful-observation criterion, permitting a noninjective one-step map. -/
theorem window_injective_iff (obs : V →ₗ[R] W) (A : Module.End R V)
    (q : ℕ) (c : Fin q → R)
    (hpoly : A ^ q = ∑ j : Fin q, c j • A ^ j.val) :
    Function.Injective (observe obs A q) ↔ invisible obs A = ⊥ := by
  rw [← LinearMap.ker_eq_bot, ker_observe, finite_determination obs A q c hpoly]

end SplitZero.ObservedIterates

```

## formal/splitzero/SplitZeroObservedIteratesSupport.lean

SHA256: d884a2773a44034b4ec4181ff74b36500cdf21bc3ce32c6e765cea6c362a83ed

```lean
import SplitZeroObservedIterates
import SplitZeroRestrictedBoundary

/-!
# The observed-iterate quotient on the ORIGINAL support reconstruction

The new relation is explicitly an observation kernel, not an assertion that
it equals the original theta boundary. Noninjective support transports are
allowed. Both the old one-step kernel and its action-stable submodule remain.
-/
noncomputable section
namespace SplitZero.ObservedIterates
open SplitZero.Reconstruction

universe u v
variable {R : Type u} [CommRing R] {L : Type v}
  [SemilatticeSup L] [OrderBot L]
  {D E : LinearDiagram R L}

/-- The original one-step observation kernel, with its actual transports. -/
def rawRelations (obs : Hom D E) : Relations D where
  fibre i := LinearMap.ker (obs.app i)
  stable {i j} h {x} hx := by
    change obs.app j (D.map h x) = 0
    rw [obs.naturality, hx, map_zero]

/-- All iterates are checked in each fibre before the original reconstruction. -/
def invisibleRelations (obs : Hom D E) (A : Hom D D) : Relations D where
  fibre i := invisible (obs.app i) (A.app i)
  stable {i j} h {x} hx := by
    apply (mem_invisible (obs.app j) (A.app j) (D.map h x)).mpr
    intro n
    have hp := powers_intertwine (D.map h) (A.app i) (A.app j)
      (fun y => (A.naturality h y).symm) n x
    rw [← hp, obs.naturality, (mem_invisible (obs.app i) (A.app i) x).mp hx n,
      map_zero]

/-- A new quotient action only after proving stability of the retained relation. -/
def actionHom (obs : Hom D E) (A : Hom D D) :
    Hom (invisibleRelations obs A).quotientDiagram
      (invisibleRelations obs A).quotientDiagram where
  app i := quotientAction (obs.app i) (A.app i)
  naturality h x := by
    induction x using Submodule.Quotient.induction_on with
    | _ x =>
      change (invisible (obs.app _) (A.app _)).mkQ (A.app _ (D.map h x)) =
        (invisible (obs.app _) (A.app _)).mkQ (D.map h (A.app _ x))
      rw [A.naturality]

/-- The first observation descends, without being declared injective. -/
def observationHom (obs : Hom D E) (A : Hom D D) :
    Hom (invisibleRelations obs A).quotientDiagram E where
  app i := (invisible (obs.app i) (A.app i)).liftQ (obs.app i)
    (invisible_le_kernel (obs.app i) (A.app i))
  naturality h x := by
    induction x using Submodule.Quotient.induction_on with
    | _ x => exact obs.naturality h x

/-- Forgetting the additional iterate data has its own receiving quotient. -/
def forgetIterates (obs : Hom D E) (A : Hom D D) :
    Hom (invisibleRelations obs A).quotientDiagram (rawRelations obs).quotientDiagram where
  app i := (invisible (obs.app i) (A.app i)).mapQ (LinearMap.ker (obs.app i))
    LinearMap.id (fun _ hx => invisible_le_kernel (obs.app i) (A.app i) hx)
  naturality h x := by
    induction x using Submodule.Quotient.induction_on with
    | _ x => rfl

theorem action_square (obs : Hom D E) (A : Hom D D) :
    (actionHom obs A).total.comp (invisibleRelations obs A).quotientMap.total =
      (invisibleRelations obs A).quotientMap.total.comp A.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  rfl

theorem observation_square (obs : Hom D E) (A : Hom D D) :
    (observationHom obs A).total.comp (invisibleRelations obs A).quotientMap.total =
      obs.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  rfl

theorem forget_square (obs : Hom D E) (A : Hom D D) :
    (forgetIterates obs A).total.comp (invisibleRelations obs A).quotientMap.total =
      (rawRelations obs).quotientMap.total := by
  apply LinearMap.ext
  rintro ⟨i, x⟩
  rfl

/-- A one-step-zero vector can remain nonzero once its future observations are retained. -/
theorem transient_kernel_retained (obs : Hom D E) (A : Hom D D)
    (i : L) (x : D.V i) (h0 : obs.app i x = 0)
    (hfuture : x ∉ invisible (obs.app i) (A.app i)) :
    (invisibleRelations obs A).quotientMap.total ⟨i, x⟩ ≠
        (⟨i, 0⟩ : (invisibleRelations obs A).quotientDiagram.Total) ∧
      (observationHom obs A).total
        ((invisibleRelations obs A).quotientMap.total ⟨i, x⟩) =
        (⟨i, 0⟩ : E.Total) := by
  constructor
  · intro hz
    have hq : (invisible (obs.app i) (A.app i)).mkQ x = 0 :=
      ((invisibleRelations obs A).quotientDiagram.same_label_eq i _ _).mp hz
    exact hfuture ((Submodule.Quotient.mk_eq_zero _).mp hq)
  · change (⟨i, obs.app i x⟩ : E.Total) = ⟨i, 0⟩
    rw [h0]

/-- Vanishing is tested against e in the receiving fibre, never against global absence. -/
theorem observed_zero_iff (obs : Hom D E) (A : Hom D D) (i : L) (x : D.V i) :
    (observationHom obs A).total
      ((invisibleRelations obs A).quotientMap.total ⟨i, x⟩) =
        (⟨i, 0⟩ : E.Total) ↔ obs.app i x = 0 :=
  E.same_label_eq i (obs.app i x) 0

theorem observed_output_not_absent (obs : Hom D E) (A : Hom D D)
    (i : L) (x : D.V i) (hi : i ≠ ⊥) :
    (observationHom obs A).total
      ((invisibleRelations obs A).quotientMap.total ⟨i, x⟩) ≠ 0 := by
  intro h
  exact hi (congrArg (fun y : E.Total => y.fst) h)

/-- Original mixed-support inner faces are preserved by the inherited theorem. -/
theorem present_empty_face {J : Type*} [DecidableEq J]
    (F : LinearDiagram R (L × Finset J)) (i : L) (hi : i ≠ ⊥) :
    (⟨(i, ∅), 0⟩ : F.Total) ≠ 0 :=
  RestrictedBoundary.present_empty_residual F i hi

end SplitZero.ObservedIterates

```

## formal/splitzero/SplitZeroResidueObservation.lean

SHA256: 0145aac9efb60ff2288c97015fe46e35a6c165d1935cb690962a975dbac161b3

```lean
import SplitZeroObservedIterates
import SplitZeroMonicResidue

/-!
# Exact residue-polynomial test for the original cyclic observation

Each actual observation row is converted by the EXISTING perfect monic
residue duality into an element of AdjoinRoot h. The complete invisible
kernel is their common annihilator. No squarefreeness or injected purity
hypothesis is used. The polynomial gcd evaluation of that annihilator is
recorded separately as a written consequence, not assumed in these proofs.
-/
noncomputable section
namespace SplitZero.ResidueObservation
open Polynomial
open scoped BigOperators

variable {K J : Type*} [Field K] {h : K[X]}

/-- The original multiplication action on the literal polynomial quotient. -/
def rootAction (h : K[X]) : Module.End K (AdjoinRoot h) where
  toFun x := AdjoinRoot.root h * x
  map_add' x y := mul_add _ _ _
  map_smul' r x := by simp

@[simp] theorem root_pow_apply (h : K[X]) (n : ℕ) (x : AdjoinRoot h) :
    (rootAction h ^ n) x = AdjoinRoot.root h ^ n * x := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [pow_succ', Module.End.mul_apply]
      change AdjoinRoot.root h * ((rootAction h ^ n) x) = _
      rw [ih, pow_succ', mul_assoc]

/-- Retain the actual rows, rather than an arbitrarily chosen detecting functional. -/
def observation (rows : J → AdjoinRoot h →ₗ[K] K) :
    AdjoinRoot h →ₗ[K] (J → K) := LinearMap.pi rows

/-- A row's coefficient is constructed by the previously proved residue equivalence. -/
def rowCoefficient (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (j : J) : AdjoinRoot h :=
  (MonicResidue.residueEquiv hh hd).symm (rows j)

theorem row_formula (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (j : J) (x : AdjoinRoot h) :
    rows j x = MonicResidue.residue hh (x * rowCoefficient hh hd rows j) := by
  have he := LinearMap.congr_fun
    ((MonicResidue.residueEquiv hh hd).apply_symm_apply (rows j)) x
  exact he.symm

/-- Annihilating all actual row coefficients kills every observed iterate. -/
theorem annihilator_kills_iterate (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (x : AdjoinRoot h)
    (hx : ∀ j, rowCoefficient hh hd rows j * x = 0) (n : ℕ) :
    observation rows ((rootAction h ^ n) x) = 0 := by
  funext j
  change rows j ((rootAction h ^ n) x) = 0
  rw [root_pow_apply, row_formula hh hd rows j]
  calc
    MonicResidue.residue hh
        ((AdjoinRoot.root h ^ n * x) * rowCoefficient hh hd rows j) =
      MonicResidue.residue hh
        (AdjoinRoot.root h ^ n * (rowCoefficient hh hd rows j * x)) := by
          congr 1
          ring
    _ = 0 := by rw [hx j, mul_zero, map_zero]

/-- All of the first deg(h) observations suffice, including every repeated-root jet. -/
theorem finite_kernel_iff (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (x : AdjoinRoot h) :
    x ∈ ObservedIterates.window (observation rows) (rootAction h) h.natDegree ↔
      ∀ j, rowCoefficient hh hd rows j * x = 0 := by
  constructor
  · intro hx j
    by_contra hn
    obtain ⟨n, hnd, hdetect⟩ := MonicResidue.exists_detecting_monomial hh hd
      (rowCoefficient hh hd rows j * x) hn
    have he := congrFun
      ((ObservedIterates.mem_window _ _ _ _).mp hx ⟨n, hnd⟩) j
    change rows j ((rootAction h ^ n) x) = 0 at he
    rw [root_pow_apply, row_formula hh hd rows j] at he
    apply hdetect
    simpa only [mul_assoc, mul_comm, mul_left_comm] using he
  · intro hx
    apply (ObservedIterates.mem_window _ _ _ _).mpr
    intro n
    exact annihilator_kills_iterate hh hd rows x hx n.val

/-- The largest invisible invariant kernel is exactly the common annihilator. -/
theorem invisible_kernel_iff (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (x : AdjoinRoot h) :
    x ∈ ObservedIterates.invisible (observation rows) (rootAction h) ↔
      ∀ j, rowCoefficient hh hd rows j * x = 0 := by
  constructor
  · intro hx
    apply (finite_kernel_iff hh hd rows x).mp
    exact (ObservedIterates.mem_window _ _ _ _).mpr fun n =>
      (ObservedIterates.mem_invisible _ _ _).mp hx n.val
  · intro hx
    exact (ObservedIterates.mem_invisible _ _ _).mpr
      (annihilator_kills_iterate hh hd rows x hx)

/-- Concrete finite determination, using residue detection rather than assuming recurrence. -/
theorem original_finite_determination (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) :
    ObservedIterates.window (observation rows) (rootAction h) h.natDegree =
      ObservedIterates.invisible (observation rows) (rootAction h) := by
  ext x
  rw [finite_kernel_iff hh hd, invisible_kernel_iff hh hd]

/-- A literal Bezout certificate suffices for faithfulness; it is not automatic. -/
theorem injective_of_bezout [Fintype J] (hh : h.Monic) (hd : 0 < h.natDegree)
    (rows : J → AdjoinRoot h →ₗ[K] K) (coeff : J → AdjoinRoot h)
    (hbezout : ∑ j, coeff j * rowCoefficient hh hd rows j = 1) :
    Function.Injective
      (ObservedIterates.observe (observation rows) (rootAction h) h.natDegree) := by
  rw [← LinearMap.ker_eq_bot, ObservedIterates.ker_observe]
  apply le_antisymm ?_ bot_le
  intro x hx
  have hann := (finite_kernel_iff hh hd rows x).mp hx
  change x = 0
  calc
    x = (∑ j, coeff j * rowCoefficient hh hd rows j) * x := by rw [hbezout, one_mul]
    _ = ∑ j, coeff j * (rowCoefficient hh hd rows j * x) := by
      rw [Finset.sum_mul]
      simp only [mul_assoc]
    _ = 0 := by simp only [hann, mul_zero, Finset.sum_const_zero]

end SplitZero.ResidueObservation

```
