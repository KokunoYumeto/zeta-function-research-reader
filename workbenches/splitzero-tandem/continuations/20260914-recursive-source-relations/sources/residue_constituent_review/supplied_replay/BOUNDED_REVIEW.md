# Independent bounded replay: residue-driven constituent curvature

This review records the completed local execution of the new twelve-method finite suite in the delivered `Tau_Residue_Constituent_Curvature` packet. Both normal and optimized runs passed all twelve methods. Each mode also rejected all three deliberately false formulas through the intended mathematical check. There were no execution errors, missing methods, manifest mismatches, or source modifications.

## Exact source and execution provenance

The raw packet is at `workspace:/output/split_zero_rh_tandem_2026-09-12/sources/web_residue_constituent_delivery/Tau_Residue_Constituent_Curvature`. The replay is at `workspace:/work/residue_constituent_replay_20260913`.

All thirty rows in the delivered manifest have the declared byte count and SHA-256 hash. The source tree contains thirty-one files: the thirty listed files and `MANIFEST.json` itself. There are no other unlisted files. The full before-and-after snapshots agree for every file, including the manifest. The validator rejects duplicated rows and any row that escapes the source directory. The complete per-row results are in `manifest_validation.json`; the unchanged source tree is independently recorded by `raw_snapshot_before.json` and `raw_snapshot_after.json`.

The following source hashes were measured before execution and again retained in the completed receipt:

| Source file | SHA-256 |
| --- | --- |
| MANIFEST.json | `0bf699e3db7bc784d31eeed9c90934716b1cbdb69d77147e24604bd1b81cfae9` |
| check_residue_curvature.py | `bd0b42ee4db1d6825b69742fe22b300ae7c74481aeebe9f92a3496c4d4962b04` |
| run_checks.py | `5d0c9ca003133cfa3d4906415d7f724da395b84d6ad0e884de0489cd0f4c5509` |

The requested replay directory was absent when work began. Only the two execution scripts were copied to its fresh `executable` subdirectory. Their copies have the same hashes as the source files. The delivered runner writes its receipts under that copy's `executable/checks` directory. It does not write into the raw packet or replace any supplied historical receipt.

The actual interpreter is `runtime:research-python/python.exe`, version `3.13.9 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 19:09:58) [MSC v.1929 64 bit (AMD64)]`. The imported SymPy version is exactly `1.14.0`; its module file is `workspace:/work/kernel_layer_replay_dependencies_20260912/sympy/__init__.py`. `PYTHONPATH` names that dependency directory and `PYTHONDONTWRITEBYTECODE=1`. The delivered historical executions report Python 3.13.5; the local receipt records the actual 3.13.9 runtime and does not relabel historical results as local results.

The enclosing replay began at `2026-09-13T04:35:26.380444+00:00` and completed at `2026-09-13T04:36:01.893002+00:00`. `runtime.json`, `batch_receipts.json`, and `replay_receipt.json` preserve the interpreter, module location, environment settings, exact argument vectors, working directory, timestamps, return codes, elapsed times, and all child receipt paths.

## Code audit before execution

The entire checker, runner, handoff, manifest, checks summary, and README were read before any checker execution. The checker imports the Python standard library and SymPy. It performs finite exact polynomial and complex rational matrix calculations; it has no remote calls, predecessor imports, Lean entrypoints, file mutation, or numerical quadrature. Its `algebra` helper makes the polynomial monic, but every supplied fixture is already monic, so this does not alter any fixture coefficient. Exact equalities are evaluated by SymPy, while positivity is accepted only when its exact symbolic predicate is explicitly true.

AST inspection confirms exactly twelve `test_` methods and zero Python `assert` statements. The helper `require` explicitly raises `AssertionError` when its Boolean input is false; `eq` calls `require` after testing the exact difference. These are executed function calls and exceptions, so Python's `-O` flag does not remove them. The delivered runner uses `subprocess.run` with a forty-second timeout for each child. It launches exactly four children in each mode: one suite and the three negative formula controls. The local enclosing driver preserves the supplied script bytes and checks both the actual child arguments and their outputs.

The negative-control branch does not refuse to start. Each branch first constructs the same exact two-dimensional fixture, computes the target quantity, and reaches a deliberately false rank or equality check. The recorded tracebacks reach `negative_control`, then `require` or `eq`, and end in the formula-specific `AssertionError`. All six negative stdout files are empty; the complete tracebacks are preserved. The local audit additionally rules out import or syntax failures as a negative-control explanation.

## Actual executions

The supplied runner was invoked as the exact argument array `["runtime:research-python/python.exe", "workspace:/work/residue_constituent_replay_20260913/executable/run_checks.py", MODE]`, with `MODE` respectively `normal` and `optimized`. The runner's optimized children include `-O` immediately after the interpreter. The suite children take only the checker path; each negative child appends `--negative` and its control name. Native path separators in the actual Windows argument arrays are retained in the JSON receipts.

| Mode | Child | Exit code | Elapsed seconds | Verified result |
| --- | --- | ---: | ---: | --- |
| normal | suite | 0 | 15.662 | 12 methods; PASS; no errors or failures |
| normal | rank | 1 | 0.535 | substantive rank assertion rejected |
| normal | laplacian | 1 | 0.540 | substantive omitted-forcing assertion rejected |
| normal | curvature | 1 | 0.561 | substantive omitted-parameter assertion rejected |
| optimized | suite | 0 | 16.051 | 12 methods; PASS; no errors or failures |
| optimized | rank | 1 | 0.518 | substantive rank assertion rejected |
| optimized | laplacian | 1 | 0.477 | substantive omitted-forcing assertion rejected |
| optimized | curvature | 1 | 0.484 | substantive omitted-parameter assertion rejected |

The enclosing normal batch took 17.39330510000582 seconds and the optimized batch took 17.60780050000176 seconds. Both batch runners exited zero. Their complete stdout and stderr are in the four `MODE.runner.*.txt` files. The sixteen child stdout/stderr files, both successful JSON records, and both supplied-runner execution receipts are under `executable/checks`. Every positive run's stderr is empty. The two successful JSON records agree byte for byte.

There are exactly twenty-four successful method invocations and six deliberately failing negative-control invocations. The negative controls are separate checker invocations, not additional unittest methods. The output method inventory is checked against the twelve AST-discovered method names, so a zero-exit process alone was not counted as a twelve-method pass.

## Exact finite coverage

The shared constituent fixtures are `(S²,S)`, `(S³+S,S)`, `(S³+S,S²+1)`, `((S−2)³(S+1),(S−2)²)`, and `((S−2)³(S+1),S+1)`, with inclusion given by the coefficient columns of `d S^j` and quotient given by remainder modulo `d`. The first three fixtures are used where stated below. Repeated roots are therefore present in the tested finite models.

| Method | Exact executed scope |
| --- | --- |
| test_01_perfect_residue_and_multiplication_trace | For `S−2`, `S²`, `S³+S`, and `(S−2)³(S+1)`, checks the residue Gram determinant `(-1)^(q(q−1)/2)`, multiplication self-adjointness for that bilinear Gram, and the residue realization of multiplication traces for powers 0 through q. |
| test_02_generated_matrix_algebra | For the same four polynomials, vectorizes all `A^i R A^j`, `0≤i,j<q`, and checks rank q². |
| test_03_full_constituent_rank_and_kernel | On all five constituent fixtures, checks `pi I=0`, surjectivity of pi, A-invariance, exact rank-one factorization, nonzero restricted residue, and kernel dimension `dim F−1`. The general identification of the kernel also uses the written factorization and nonzero quotient unit. |
| test_04_source_cost_positive_with_nonorthogonal_constituents | On all five fixtures and the specified nonorthogonal positive matrix `B*B+I_q`, where `B=model(q)` and `*` denotes conjugate transpose, checks exact positivity of the product of quotient and dual costs. In source notation the matrix is `model(q).H*model(q)+s.eye(q)`. |
| test_05_exact_normal_velocity_all_parameters | On the first three fixtures, uses `u=2+i` and the three parameters `t=0,2,i` to check the complete normal-velocity identity and normal ranks 0,1,1. The method name does not mean that infinitely many parameters were executed. |
| test_06_curvature_factorization | On the first three fixtures at `t=1+i`, `u=2+i`, verifies the trace factorization and exact positive coefficient. |
| test_07_normal_acceleration_and_quartic_coefficient | Checks normal acceleration in the `(S³+S,S)` fixture at `u=2`; independently constructs the scalar bivariate log-Gram jet for `(S²,S)` and verifies four times the `x²y²` coefficient. |
| test_08_source_endpoint_determinant_enclosure | On the first three fixtures, uses the specified positive `Gj` and `Gi=Gj+diag(1,...,q)` and checks both exact determinant-ratio inequalities. |
| test_09_period_to_source_condition_enclosure | Uses `(S³+S,S²+1)`, `G=diag(2,3,4)`, `H=diag(4,12,8)`. The relative diagonal ratios are 2,4,2, giving condition number 2; checks both coefficient bounds. |
| test_10_laplacian_forcing_with_rank_one_term | Uses `(S−2)³(S+1)`, `u=2+i`, `k=3`, `t=2/3` and checks the exact corrected forcing identity; also verifies that omitting the forcing changes the matrix. |
| test_11_original_metric_laplacian_transport | Uses `S³+S`, `k=2`, and the specified positive source metric; checks the metric commutator identities and their exact period conjugations. |
| test_12_translation_preserves_curvature_not_trace | Uses `S³+S`, `d=S²+1`, `a=2+i`, `f=3+i`; checks Pascal translation, residue transport, curvature-coefficient invariance, and the full q-dimensional trace shift `2q Re(a)`. This method does not itself evaluate the p-dimensional constituent trace shift stated in the handoff. |

The supplied mathematical note and parent proof integration supply the general arguments. These executions establish the listed finite regression results, including exact repeated-root examples. They do not establish an entire-parameter analytic theorem merely from sampled parameters, an arithmetic zeta-zero packet, a contour or source integral, an asymptotic estimate, or a new Lean certificate. No predecessor check and no Lean, Lake, or Elan process was launched in this subtask.

## Independent fourth mixed-jet calculation

Use the checker's original ordered coefficient basis `(1,S)`, `chi=S²`, `d=S`, `u=2`, and `B=model(2)`. Write `e0=(1,0)^T`, `e1=(0,1)^T`, and `b=(1+i)/3`. Then

\[
A=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
R=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
\iota=e_1,\quad
B=\begin{pmatrix}1&b\\0&1\end{pmatrix}.
\]

Write the formal period coefficients as `J0=B`, `J1=−BA/u`, and `J2=−(J1 A+J0 R)/(2u)`. These are Taylor coefficients, with `J2=Pi''(0)/2!`. Since `A²=0`, `A iota=0`, and `R iota=e0`, the constituent coefficients are

\[
p_0=J_0\iota=(b,1)^T,\qquad p_1=0,\qquad
p_2=J_2\iota=-e_0/4.
\]

Let `x=t`, `y=bar(t)` be independent formal variables. Terms of holomorphic or antiholomorphic degree above two cannot affect the `x²y²` coefficient because every term in the formal logarithm has nonnegative bidegrees. The truncated Gram is exactly

\[
h(x,y)=h_0-\frac{\bar b}{4}x^2-\frac b4y^2
       +\frac1{16}x^2y^2,\qquad
h_0=1+|b|^2=\frac{11}{9}.
\]

For `Z=h/h0−1`, the only contributions to `x²y²` in `log(1+Z)` are the mixed term in `Z` and the cross product in `−Z²/2`. Thus

\[
[x^2y^2]\log h
=\frac1{16h_0}-\frac{|b|^2}{16h_0^2}
=\frac1{16h_0^2}=\frac{81}{1936}.
\]

The logarithm expansion through its fourth power used by the checker is sufficient even if linear terms were present: every monomial of `Z` has total degree at least one, so `Z^n` with `n>4` cannot contribute to total degree four. In this actual fixture `p1=0`, so the higher powers already contribute nothing to the target coefficient.

The source matrix is `M=B*B`, where `*` denotes conjugate transpose. Its restricted Gram on F is `h0`. The image of the quotient unit is represented by `B e0=e0`; its squared distance from the line spanned by `(b,1)^T` is `1−|b|²/h0=1/h0=9/11`. The squared dual norm of the restricted residue is likewise `1/h0=9/11`. Consequently

\[
\mathfrak c_F(B^*B)=\frac{81}{121},\qquad
\frac{\mathfrak c_F(B^*B)}{|u|^2}=\frac{81}{484}.
\]

Differentiating `x²y²` twice in each variable multiplies its coefficient by `2!2!=4`. Therefore the actual mixed derivative is `4·81/1936=81/484`, exactly the expected curvature coefficient. There is no missing factorial in method 7 or in RC27.

For the general identity RC25, write `g(t,bar(t))=c_F(H(t))/|u|²`. The given identity is `partial_t partial_bar(t) psi=t bar(t) g`. Applying one further derivative in each variable and evaluating at zero leaves precisely `g(0)`; every other Leibniz term retains a factor t or bar(t). This proves the RC27 derivative conversion and its coefficient `g(0)/4` without conflating it with a derivative along the real axis.

RC28 uses ordinary `d/dt` and must be read along real t with real positive u. Indeed at zero `P'=−P A_F/u`, so along the real axis `H_F'=−(A_F* H_F+H_F A_F)/u`; taking `Tr(H_F^−1 H_F')` gives `−2 Re Tr(A_F)/u`. A Wirtinger derivative would instead give `−Tr(A_F)/u`. This is a notation clarification, not a failing finite check.

## Independent exact negative-control calculations

All three controls retain `chi=S²`, `d=S`, the ordered basis `(1,S)`, `iota=e1`, `pi=(1,0)`, `B=I2`, `u=1`, and `t=2`. Hence `A`, `R` are the two matrices displayed above, `H_F=1`, and the orthogonal projector is `diag(0,1)`.

For the rank control, `pi R iota=(1)`, whose rank is exactly one. The control requires rank zero and therefore fails on the intended false rank formula.

For the Laplacian control, `B1=−A` and `B2=A²−R=−R`. The alleged uncorrected equality compares `B2+B1=−R−A` with `A²−A=−A`. Their difference is exactly `−R`, a nonzero rank-one matrix. The control therefore fails on the omitted-forcing formula.

For the curvature control, `Pprime=−(A+2R)iota=−2e0`. Its squared normal norm is four. Both source quotient and dual factors equal one, so the expression with the omitted `|t|²` factor equals one. The false identity differs by exactly three. This control therefore fails on the missing parameter factor.

These calculations explain the six actual failures directly. Their formula-specific tracebacks, explicit exception mechanism, and matching results under `-O` exclude a startup guard or removed-assertion explanation.

## Completion and integration handoff

The finite replay is complete. Its machine-readable entry point is `replay_receipt.json`; `batch_receipts.json` preserves verified child execution details; `code_audit.json` preserves the pre-execution audit; `manifest_validation.json` and the source snapshots prove exact local manifest agreement and immutability. The parent intake task remains responsible for full written proof integration and propagation into its cumulative artifacts. The only coverage qualifications requiring preservation there are the sampled parameter scope, the scalar nature of the fourth-jet fixture, the full-dimensional trace check in method 12, and the real-axis meaning of RC28.

An independent read-only mathematical audit is included unchanged as `fourth_jet_paper_audit.md`, SHA-256 `5f33b217d18d1ad7f0136486f31217632c832f2f3588853c5f52c350ac14517d`. It supplies the complete RC18–RC27 calculation and the additional three-dimensional normal-acceleration computation `513216/2679769`. Its original is `workspace:/work/residue_curvature_fourth_jet_paper_audit_20260913.md`. Both texts were read and their fixture calculations reconciled before handoff. The audit agent and its read-only negative-control collaborator executed no checker, so they add no test invocations to the counts above.
