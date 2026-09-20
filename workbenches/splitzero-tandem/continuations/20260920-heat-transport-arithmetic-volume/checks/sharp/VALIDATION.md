# Validation of the sharp rank-one metric heat bound

The complete proof is `RANK_ONE_HEAT_BOUND.tex`, Theorem 1, with the scalar integral bound in Lemma 1 and the one-sided matrix bound in Lemma 2. `SCALAR_LOG_MEASURE_PROOF.md` is a separately derived proof of the scalar and matrix lemmas. A second complete reading of the theorem by that independent worker found no mathematical flaw in the original-coordinate transport, the difference of the two one-sided gaps, the singular cases, or the prescribed-metric equality examples.

## Executed exact checks

Both commands completed successfully on 20 September 2026:

```text
python check_rank_one_heat_bound.py
python -O check_rank_one_heat_bound.py
```

Each run reported:

```json
{
  "status": "passed",
  "arithmetic": "exact SymPy; no floating point",
  "checks": 97,
  "failure_controls": 9,
  "python_version": "3.13.9",
  "sympy_version": "1.13.1"
}
```

The respective `python_optimized` fields were `false` and `true`. The checker uses explicit exceptions rather than Python assertions, so its checks remain active under `-O`.

The finite inputs retain nonreal entries in the positive original metric, the update vector, and the test matrices. Cases cover full rank, rank two, rank one with each equality direction, and rank zero. The checks establish the exact metric and adjoint transport identities, characteristic-polynomial identities, both positive-semidefinite comparisons, the rank-at-most-one condition, each common-support determinant budget, and the exact scalar equality values at kappa four. They also check the unit-vector return maps and the scalar optimizer equations. The failure controls reject rank-two updates, rank-changing updates, reversed order, an insufficient relative bound, loss of conjugation, a wrong determinant ratio, a reversed square root, and an incorrect doubled equality value.

These finite checks support the identities. The uniform inequality for every complex finite matrix and every positive heat parameter is established by the complete written proof, not by a numerical sample.

During checker development, a comparison of two unevaluated exact SymPy expressions failed even though their difference vanishes. The checker was repaired to evaluate exact scalar and matrix expressions before comparing them. Both successful runs used the repaired checker. No theorem or bound was weakened.

No discovery, indexing, rendering, or publication was performed by this worker.

## Pinned files

SHA-256 values after the successful runs and the complete independent theorem audit:

```text
RANK_ONE_HEAT_BOUND.tex
3e8c43aa1084e04d797a35e4991b800de6fe0b5803b2b4627711fbdb0ac3a5c5

check_rank_one_heat_bound.py
c6020af425496f89e396b0709b99930e0720fa581430d8f7ae9ce32d05073a79

SCALAR_LOG_MEASURE_PROOF.md
b221f526e818c10acef9342d819d8340f2e51999c231010f4ae93a04ecca43e2

CHECKS_NORMAL.json
5aecde466fcccca44b939d70a4ceac2f001c7a429f985e181fa96b3bad117553

CHECKS_OPTIMIZED.json
46ee1a11de23228b5d9fe9baccea2ac07c462c33442f93f993013c56743655de
```

The two JSON receipts preserve every field and every named check from the retained actual successful checker outputs. Their line endings were written by `apply_patch`; no replay, proof edit, or checker edit was performed during this receipt finalization.

## Independent audit of the parent degree-volume proof

The complete `../DEGREE_VOLUME_HEAT_RETURN.tex` was read. The requested mathematical checks found no gap; two punctuation transcription defects in VH11 and the VH27 proof were reported to the parent for correction.

For VH11, put `A_lambda = a a* G_lambda`. Differentiating the original adjoint gives

\[
(M^{\dagger_{G_\lambda}})'=[A_\lambda,M^{\dagger_{G_\lambda}}],
\qquad
H_\lambda'=A_\lambda H_\lambda-
M^{\dagger_{G_\lambda}}A_\lambda M.
\]

Trace differentiation and cyclicity therefore give

\[
\begin{aligned}
\Psi_s'(\lambda)
&=-s\operatorname{tr}(e^{-sH_\lambda}A_\lambda H_\lambda)
 +s\operatorname{tr}(e^{-sH_\lambda}M^{\dagger_{G_\lambda}}A_\lambda M)\\
&=s\operatorname{tr}\!\left[A_\lambda
\left(M e^{-sH_\lambda}M^{\dagger_{G_\lambda}}-
H_\lambda e^{-sH_\lambda}\right)\right]
=s a^*G_\lambda B_\lambda a.
\end{aligned}
\]

Thus its sign is positive for the displayed definition of `B_lambda`; no sign for the value of the quadratic form itself follows.

For VH19, the stated source and boundary Toda identities give

\[
\ell_N''=a_{N+1}-c_{N-q+1},\qquad
v_{N+1}''=(\ell_N-\ell_{N+1})''
=a_{N+1}-a_{N+2}-c_{N-q+1}+c_{N-q+2}.
\]

The indices and the signs in the parent file match these exact subtractions.

For VH21, the outgoing source column has coefficient
`i^{-(N+1)} b_{N+1}/sqrt(omega_N)`, and the lifted last-coordinate row is
`i^N b_N* G_N/sqrt(omega_N)`. Their product has phase `-i`. Consequently

\[
M=\mathsf A_N-\frac{i}{\omega_N}b_{N+1}b_N^*G_N,
\quad Q_N=\frac{i}{\omega_N}b_{N+1}b_N^*G_N,
\quad \operatorname{tr}Q_N=\frac{i z_N}{\omega_N}
=\ell_N'-\sigma.
\]

It follows that `z_N/omega_N = i(sigma-ell_N')`, so the mixed contraction at nonzero tilt is not dropped. Also

\[
\|Q_N\|_{\mathrm{HS},G_N}^2
=\frac{B_NC_N}{\omega_N^2},\qquad
\operatorname{tr}\left[i(Q_N^{\dagger_N}-Q_N)\right]^2
=2\frac{B_NC_N}{\omega_N^2}-2(\ell_N'-\sigma)^2.
\]

The second identity uses the reality of `tr Q_N` and `Q_N^2=(tr Q_N)Q_N`. Since the Hermitian defect has rank at most two and trace zero, its eigenvalues are opposite, giving exactly the subtraction in VH23. Thus the rank-one Hilbert--Schmidt norm and the rank-two Hermitian allowance are distinct at a general tilt.

At the first degree `N=q-1`, invertibility of the square column map gives `B_N/omega_N=1`, while

\[
\frac{C_N}{\omega_q}=e^{v_q}-1
=\frac{\nu_0}{\omega_q}-1.
\]

Therefore `||Q_{q-1}||_HS^2=(nu_0-omega_q)/omega_{q-1}`, and the same phase-square subtraction gives the displayed VH25 allowance. No preceding inadmissible degree or inverse is used.

The parent file owns its further edits and its final receipt; this worker did not edit it.
