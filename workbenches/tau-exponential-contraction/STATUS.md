# Verification and handoff — 16 September 2026

## Mathematical status

This is a written analytic theorem on the explicitly retained AMT density envelopes and canonical source/relation identities. The full two-band Jensen argument is in RESEARCH_NOTE.md. It strengthens the submitted O_h(1+k(m-1)) contraction-penalty estimate to an exponential one, uniformly on every original row q<=n<=2q, and gives a lower bound on the MINIMUM canonical allowance on q-1<=N<=2q-1. A final section proves the analogous qualitative conclusion for each fixed proportional cutoff Cq, with constants depending on C.

The theorem does not assume the desired exterior upper bound or use a claimed quantile asymptotic. It does not evaluate the next arithmetic total-volume coefficient, the individual mixed allocations, or an actual off-critical packet. It does not claim a failure of RH or of the entire tau programme. Its conclusion restricts this particular canonical small-allowance route on bounded-proportion degree windows.

No new Lean executable was available. No independent second-reader approval, actual-period arithmetic computation, full cumulative source replay, or new GitHub Actions result is claimed.

## Exact input pin

Main: 1efd53337561d8f67cf0ac1d119acdaa222644c3.

AMT1--6 were fetched directly from the original arithmetic mixed-transfer source, blob b6cfec2ac9517acc378aa02686ada6e7923ef381. The complete 540-line uploaded recurrence/action note and relevant full new transcript were read. The source-order EOR estimate remains separately scoped and is not needed for the new exponential bound. Raw GitHub downloads failed DNS; this did not prevent the connector AMT read.

## Observed local execution

The final check_bound.py has 7,482 bytes, SHA-256:

`26422a41ec9f3572aa703fbb237123a552244e207478709ce1b478c6c2b451a4`

Its expected Git blob is `9fe463722ad987f82295d7b8a8f12de8e2ced3e6`.

Both commands completed successfully:

```sh
python check_bound.py > CHECKS.json
python -O check_bound.py > CHECKS_OPTIMIZED.json
cmp CHECKS.json CHECKS_OPTIMIZED.json
```

The JSON outputs are byte-identical (2,268 bytes), SHA-256:

`87286429f0e29d693a5f0677d35ce2eaa09be0886403cd6336abacbe7d21b93e`

Their reported categories are:

- 6 exact universal-constant checks, including an outward rational-series interval for log(50000/45927).
- 79 exact Gamma norm, pairing and generating-ODE checks.
- 99 exact block partitions and 792 top-degree-face inequality checks.
- 13 exact canonical radius rows and 3 complete weighted-action products, with nonreduced and quartet reference polynomials.
- 17 separately labelled 180-digit exponential-weight monic-minimum diagnostics and 31 Gamma-window diagnostics. These are not interval arithmetic.

These categories are finite regression counts, not discoveries. Reference moment computations use literal mass seven. They are not asserted zeta-zero samples.

The four controls below each failed with its intended ArithmeticError in normal and optimized Python:

```sh
python check_bound.py --negative ratio
python check_bound.py --negative penalty_count
python check_bound.py --negative factor
python check_bound.py --negative constant
# Repeat each with python -O.
```

They respectively reverse the monic norm ratio, change the endpoint coefficient count from 4q-1 to 4q, omit an actual contraction factor, and alter the exact rate denominator. The final checker bytes were replayed for all eight controls. A first combined shell batch timed out during control execution; it was not counted as completed and was replaced by the recorded separate executions.

## Review priorities

1. Verify the probability density and entropy in the two-band lemma, the square-map Jensen argument, and the direction omega_n/h_(n-q)^chi.
2. Check the original-root radius guard q>=7R_k and every retained AMT constant in U_ctr.
3. Check total parity at the original action site; do not set the kernel and boundary pairings separately to zero.
4. Check the first admissible endpoint separately and keep the exact penalty count 4q-1.
5. Apply the result to the original complete action identity, not to a cancelled allocation with its correlated budget frozen.

The finite algebra is a focused next Lean target: original determinant-ratio interface, penalty summation and minimum-allowance implication. The analytic Jensen and density estimates must not be counted as kernel-checked merely because their finite consequences are formalized.
