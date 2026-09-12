# KL.11–KL.20: new exact continuation calibrations

The complete current `tex/kernel_layer_continuation.tex` was read before writing
the new checker. This lane added
`output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_continuation.py`.
It did not edit the TeX, cumulative paper, or delivered archive members.

The checker imports a byte-identical isolated copy of the completely read
`check_kernel_layer.py`, SHA-256
`bc603e2ebda6104e10e5b48b0de56a7430a0c3276aa2023b2603040eee1cc410`.
The original dependency's bytes are checked before copying and again after the
run. No source checker is executed through its `main`; its exact polynomial
fixture functions are loaded as a module. The newly authored checks use explicit
`unittest` failures and do not rely on Python `assert` statements.

## Execution

Python 3.13.9 and the isolated SymPy 1.14.0 pin were used. The four fresh JSON
receipts are under `checks/kernel_layer_continuation/`.

| Mode | Methods | Explicit assertion evaluations | Failures | Errors | Exit |
|---|---:|---:|---:|---:|---:|
| ordinary | 4 | 929 | 0 | 0 | 0 |
| optimized `-O` | 4 | 929 | 0 | 0 | 0 |
| ordinary, incorrect homogeneous-shell control | 5 | 929 plus control | 1 | 0 | 1 |
| optimized, same incorrect substitution | 5 | 929 plus control | 1 | 0 | 1 |

The sole negative failure is `0 != 1` in
`IncorrectHomogeneousSubstitution.runTest`. All 929 positive assertions pass in
both negative executions as well. These are calibration counts, not theorem
counts. A first development invocation found an unmatched parenthesis in the new
checker; that syntax error was corrected before these four completed executions.
There was no mathematical calibration failure requiring a formula change.

## Incidence, ordered division, and the complete cokernel

For every `k=1,2,3,4` and `n=0,1,2,3,4`, the program constructs the actual
incidence matrix in the lexicographically ordered homogeneous monomial bases.
It divides every target monomial by the original ordered last-variable divisor
`z[k-1] + sum(z[:k-1])` and records both quotient and remainder matrices. It
checks the signed substitution `z[k-1] = -sum(z[:k-1])`, the complete polynomial
identity, and both matrix inverse identities for

\[
(q,r)\longmapsto\ell q+\iota r,
\qquad f\longmapsto(\operatorname{quotient}(f),\rho f).
\]

Thus the finite cases verify the injection and the complete cokernel map,
including the `k=1` zero-dimensional complementary space. No raw Mellin-variable
shell is substituted for the homogeneous **coefficient** space in KL.12.

## Actual derivative rank, full kernel, and full unused-layer quotient

Ten finite-measure fixtures were checked. They include one- and two-variable
packets, a twofold root, asymmetric positive weights, and combinations of the
last two. The fixture measure uses the original finite heights and positive
weights from the hash-pinned delivery; all complex signs, local-unit jet columns,
monic norms and original matrices are retained.

Each case verifies the complete actual source matrix identity

\[
C_N=(I-P_{\mathcal L_N})B_N
 =\mathscr E_N\mathsf T_N\mathsf D_N^{-1}\mathsf A_N^*G_N.
\]

The checker tests equality of the two ranks and represents the entire kernel
by the explicit columns `K * basis(ker(A_top.H))`. It checks the kernel image is
annihilated and has the full required dimension. It also checks the actual
projection-loss rank and KL.15's refined weight-form rank bound.

For the quotient, put `Z=D_top^{-1} A_top.H`. The program constructs a
complex-linear annihilator matrix `Qz` with kernel exactly `im(Z)`, using the
ordinary transpose for these coordinate functionals. It retains a specified
right inverse `Sz`. Together with the exact ordered-division matrices this gives

\[
Q=\begin{pmatrix}Q_z\,\mathrm{quotient}\\\rho\end{pmatrix},
\qquad S=(\mathsf T_NS_z\mid\iota).
\]

It verifies `Q*S=I`, `Q*T*Z=0`, the exact quotient dimension, and that every
column of `S*Q-I` lies in `im(T*Z)`. It then verifies that the corresponding
**actual test-function** difference `E*(S*Q-I)` lies in `im(C)`. These are finite
coordinate checks of both quotient inverse maps, including both summands of
KL.18; a dimension agreement alone is not used as the isomorphism test.

The nontrivial records include:

| k,N | Fixture | rank A_top = rank C | Layer dimension | Jet-deficit quotient | Incidence complement |
|---|---|---:|---:|---:|---:|
| 2,2 | distinct, symmetric | 2 | 4 | 1 | 1 |
| 2,3 | distinct, symmetric | 2 | 5 | 2 | 1 |
| 2,2 | repeated, symmetric | 2 | 4 | 1 | 1 |
| 2,3 | repeated, symmetric | 2 | 5 | 2 | 1 |
| 2,2 | distinct, asymmetric | 3 | 4 | 0 | 1 |
| 2,3 | repeated, asymmetric | 3 | 5 | 1 | 1 |

All ten full records are in each mode's JSON, without suppressing the different
next-jet and weight ranks.

## Consecutive quotients from original polynomial columns

Six pairs of consecutive levels are tested: two one-variable pairs and four
two-variable pairs. They cover repeated and asymmetric cases separately and
together. The program constructs each actual polynomial

\[
e_\beta=p_\beta-\sum_{|\alpha|\le N}
p_\alpha\frac{a_\alpha^*G_Na_\beta}{\kappa_\alpha}
\]

and checks its values against the original source-function columns, including
the unchanged product multiplier `v`. It then constructs and retains

\[
\Delta_\beta=(s_1+\cdots+s_k)e_\beta
-\sum_i e^{(N+1)}_{\beta+\mathbf e_i}.
\]

For each full difference it checks the degree bound, every complete remainder,
the fixed-order division into `h(s_i) Q_i`, the degree bounds of the primitives,
and both occurrences of every Koszul sign. It compares the resulting original
test-function matrix with `D*E - E_next*T_next` and checks it belongs to the
old admitted relation space. It checks that the derivative of every old relation
basis column is also in that receiving relation space. Finally it verifies the
projected derivative matrix, its injectivity, and its entire incidence cokernel.

The retained difference is nonzero in every tested pair: its rank is one for
the one-variable pairs and four for all two-variable pairs. The checker therefore
does **not** replace equality in the quotient by equality of original functions.

## Requested shell-substitution negative control

Retain `h(s)=s-1/2`, `k=2`, `N=1`, `v=1`, the three nodes
`1/2-i, 1/2, 1/2+i`, and all three weights equal to one. The product measure has
nine atoms. The exact monic polynomials and squared norms are

\[
p_0=1,\quad\kappa_0=3;\qquad
p_1=s-\tfrac12,\quad\kappa_1=2;\qquad
p_2=(s-\tfrac12)^2+\tfrac23,\quad\kappa_2=\tfrac23.
\]

The actual degree-one top jets are `[0,0]`, whereas the raw homogeneous jets are
`[1/2,1/2]`. The original representative is `R_1 u=u`, its metric is `G_1=9`, and
the packet generator is `A=1`. Thus the unprojected boundary is

\[
B_1u=(s_1+s_2-1)u\in\mathcal L_1,
\qquad C_1=(I-P_{\mathcal L_1})B_1=0.
\]

It follows that `rank(B_1)=1`, `rank(C_1)=rank(actual top)=0`, but
`rank(raw homogeneous top)=1`. The normal test checks all these exact values.
The negative flag deliberately asserts the incorrect last rank equality and must
exit with status one.

The exact raw-to-orthogonal-shell map is retained as well. For
`f=a s_1+b s_2`, it is

\[
f\longmapsto f-R_1Jf
=a(s_1-\tfrac12)+b(s_2-\tfrac12),
\]

with inverse adding `(a+b)/2`. This changes the evaluated full jet while
preserving the full degree-one leading class. The independent companion
`work/kernel_layer_shell_negative_20260912.py` constructs this map, the original
Gram matrices and the wrongly substituted map explicitly. Its proof report and
separate runtime record are in
`work/kernel_layer_shell_negative_20260912.md` and
`work/kernel_layer_shell_negative_20260912_receipt.json`.

## Reproduction and scope

From the math workspace, use the task-local SymPy pin already prepared by the
delivery replay, or install it into that isolated target:

```powershell
python -m pip install --disable-pip-version-check --target 'work/kernel_layer_replay_dependencies_20260912' 'sympy==1.14.0'
$env:PYTHONPATH = (Resolve-Path -LiteralPath 'work/kernel_layer_replay_dependencies_20260912').Path
python -B output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_continuation.py --json output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_continuation/normal.json
python -B -O output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_continuation.py --json output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_continuation/optimized.json
python -B output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_continuation.py --self-test-failure --json output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_continuation/negative_normal.json
python -B -O output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_continuation.py --self-test-failure --json output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_continuation/negative_optimized.json
```

The last two commands are supposed to fail. JSON receipts retain every labeled
positive assertion and every matrix-rank record. These finite calibrations
supplement the written KL proofs. They are not arithmetic-moment enclosures,
actual zeta-zero computations, general analytic proofs, or Lean certificates.
