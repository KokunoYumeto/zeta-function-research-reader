The finite propagation and the two comparable-window budgets are consistent with the shared threshold-four result. Two bounded corrections remain at the reviewed source:

1. In `RESEARCH_NOTE.md` section 3, replace “positive generalized eigenvalues” with “nonnegative generalized eigenvalues, counted with all q multiplicities including zeros.” Since Omega is positive definite and F*G_iF is only positive semidefinite, strict positivity requires an additional full-rank premise that is false even in the intended quartet family. At theta=0 the quartet source is even. For even k, q_k is odd; its full-order cyclic polynomial in u is odd, and quotient reduction preserves parity. The first block Q_q,...,Q_(2q-1) has (q+1)/2 odd columns in an odd quotient subspace of dimension (q-1)/2. Hence F is singular. The original S=k/2+iu map and i^j factors preserve rank. The zero eigenvalue must stay in the q-fold product and mean; every 1+lambda_a remains positive, so all displayed determinant, AM-GM and threshold conclusions survive.

   An exact Gaussian calibration modulo u^3+u gives remainder columns (0,-4,0), (3,0,-7), (0,26,0), source Gram [[1,0,1],[0,1,0],[1,0,3]], and Omega=diag(6,24,120). Its complete generalized spectrum is [0,19/4,83/10], with determinant ratio 2139/40 and kernel vector (13,0,2). This is a regression fixture, not arithmetic zero data. A local proposed eighth method verifies those identities with exact fractions and retains the zero multiplicity in the AM-GM comparison; it passes normally and under optimization with expected-failure controls.

2. In `.github/workflows/splitzero-consecutive-window.yml`, add `main` to the push branches and `formal/splitzero/AuditConsecutiveWindow.lean` to the pull-request paths. The minimal diff is:

```diff
-    branches: [astra/consecutive-window-norm-20260913]
+    branches: [main, astra/consecutive-window-norm-20260913]
   pull_request:
     paths:
+      - 'formal/splitzero/AuditConsecutiveWindow.lean'
```

This preserves the entire strict job body, dependency pins and current source-checker replay. It permits the same strict checks after a main merge and on an audit-only PR update. No theorem, phase, source mass or arithmetic hypothesis needs changing for these corrections.

The branch is actively advancing, so this is review feedback, not authority to overwrite its head. The successful predecessor at a02db96da0faff1aae32409c2719aab395a4aae9 certifies nine declarations. The successor at 66fac5e7885a40cd4873e74b754907320f05b067 adds canonical_norm_volume; its two completed window runs 34728377778 and 34728375048 each have ten exact selected standard-axiom reports and successful finite-checker steps. Other inherited workflows were still running at the observation. The original failed development checks are not successful certificates.
