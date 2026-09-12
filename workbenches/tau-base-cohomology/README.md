# Tau-base arithmetic cohomology

This is an additive research workbench in the owner's SplitZero programme. The branch is stacked on PR #6, commit `5f6ee6575550d8a20c6fc3990359cb4f67855f80`, without changing its Lean modules or the frozen reader. It also uses the actual theta comparison from PR #3. Nothing is merged automatically.

## Read in this order

1. [The tau-base model](TAU_BASE_MODEL.md): the original split coefficients and infinite arithmetic quotient, the characteristic-zero theta chart, its cohomology, right-adjoint calculation, arithmetic action, and tensor maps.
2. [Exact finite operator comparison](FINITE_OPERATOR_COMPARISON.md): differential inverses on the actual test spaces, complete finite operator kernels and quotients, spectral projectors on the original cohomology, the analytic torsion-subsheaf theorem, and the residue/trace comparison.
3. [Localization interface](LOCALIZATION_INTERFACE.md): the full arithmetic divisor extracted by the actual localization complex, its split lift, and the precise comparison cone to geometric support.
4. [Validation record](VALIDATION.json): what was checked and what was not.

The baseline is a publication edition of the preceding authored note, not a claim that its bytes reproduce every earlier conversational response. It retains the same four-point chart, operators, projective resolution, right adjoint, and original scalar quotient, and records the new formalization's nonzero-bottom-fibre interface explicitly. The prior checker retains its historical `NOTE.md` docstring; the corresponding publication note is now `TAU_BASE_MODEL.md`.

## The principal calculation

Let `Q = B / Theta V` be the actual degree-one tau-base theta cohomology, and let `t` act by `D = -x d/dx`. For a finite test polynomial `h` with roots anywhere in the open critical strip, write `E_h = C[t]/(h)` and let `g_h` be the complete Taylor residue of `g = 2 xi`. The new derivation computes

- `C_theta tensor^L E_h` as the actual complex `[E_h --g_h--> E_h]`;
- `Q[h(D)]` as `ker(g_h)` and `Q/h(D)Q` as `coker(g_h)`;
- the exact finite kernel-to-quotient map and its local unit;
- finite equivariant spectral projectors on Q with their explicit source-function representatives;
- the intrinsic analytic torsion part of `O tensor_C[t] Q` as `O/(2 xi)`;
- its complementary kernel as a module over meromorphic functions;
- the localization complex extracting that torsion, while retaining the meromorphic module and the separate cone to geometric support;
- the finite-rank arithmetic trace on the original Q and the complete tensor action.

The original supported lift is applied to every relation and projector. For disjoint finite packets, the composition of the lifted projectors is the internal-zero map `(label,v) -> (label,0)`, not the externally absent operator. The infinite arithmetic quotient `G(Z) -> Z` remains in the structural coefficient square.

This is written mathematics submitted for review. It is not a proof of positivity, purity, RH or GRH, and is not Lean certification of the analytic claims. The remaining global geometric-support comparison has its explicit cone in `LOCALIZATION_INTERFACE.md`; it is not assumed acyclic. The meromorphic kernel is not assumed to vanish.

## Existing checked interfaces reused

The implementation is the owner's existing library, not a competing copy:

- `formal/splitzero/SplitZeroReconstruction.lean` and `SplitZeroRecovery.lean`: original total semimodule and recovery, including a possibly nonzero bottom module.
- `SplitZeroInternalQuotient.lean`: original internal coequalizer against arbitrary split-linear targets.
- `SplitZeroHomology.lean` and `SplitZeroComplex.lean`: actual homology maps, transported-class kernels, and compatible kernel actions.
- `SplitZeroFiniteJets.lean`: quotient tensor base change, exact balancing relation, and the full split/reflection square.

The note supplied with PR #6 records the exact mathematical scope. Its successful GitHub Actions run `34672542080` at the pinned head was read in this session. That run is previous Lean evidence; Lean was not rerun here, and it does not certify the new analytic arguments.

## Reproduce the finite regressions

The authoring run used Python 3.13.5 and SymPy 1.14.0. Install SymPy in the environment, then run:

```sh
python check_tau_base.py --output base.json
python -O check_tau_base.py --output base-optimized.json
python check_finite_operator.py --output finite.json
python -O check_finite_operator.py --output finite-optimized.json
cmp base.json base-optimized.json
cmp finite.json finite-optimized.json
```

The baseline reports 79 named records in six suites. The new checker runs ten unittest methods, including parametrized finite algebra examples. These numbers are not theorem counts or analytic proof certificates. Both scripts' `--negative-control` runs must fail, both normally and under `python -O`.

No bare Python assert statement is used to enforce a check. Local copies of both published checker blobs were compared byte-for-byte through their Git object identities and rerun in both modes. The validation record includes the detected and repaired whitespace-only transfer difference.

## Provenance and publication

The SplitZero construction and research direction are the owner's. The new analytic/algebraic derivations are AI-assisted contributions under that direction; no global historical-priority claim is made. Prior spectral realizations of zeta zeros, including Meyer's, are cited in the main note rather than counted as discoveries of this session.

Only authored mathematical exposition, test code and provenance records are included. No private transcripts, source-literature corpus, credentials, or font files are published. This workbench adds files only. Existing licenses, formal sources, dependency pins, source books, accepted statements and other branches remain unchanged.
