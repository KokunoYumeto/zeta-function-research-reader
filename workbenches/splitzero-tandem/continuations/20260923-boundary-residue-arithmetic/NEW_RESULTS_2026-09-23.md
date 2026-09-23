# New mathematical results — 23 September 2026

Read [the complete sixteen-page derivation](BOUNDARY_RESIDUE_ARITHMETIC_RECEIVERS.pdf), with [standalone LaTeX](BOUNDARY_RESIDUE_ARITHMETIC_RECEIVERS.tex). The supplied boundary paper, exact rational witness and companion manuscript are preserved unchanged. Earlier sealed editions remain available at their stated scope.

## SZ-20260923-130 — The collision defect in arithmetic tests

For labelled roots with the generalized reciprocal and the entire analytic unit \(U\), the full equation is

\[
F_t+F_{zz}=UD+FB,\qquad \frac{D}{P}=\sum_\ell\frac{m_\ell(m_\ell-1)}{(z-c_\ell)^2}.
\]

The coefficient \(B\) retains all unit and external-root terms; BT3 evaluates it explicitly. The contact class can be nonzero while its ordinary multiplication trace pairing vanishes. Its derivative receiver, proved in BT8–18, is

\[
\delta_{\rm contact}\dot Z(A)=\frac14\sum_\ell m_\ell(m_\ell-1)A''(\rho_\ell).
\]

On reflected tests vanishing at a real critical collision, its contribution is \(-m(m-1)\overline{F'(\rho)}G'(\rho)/2\). This cancels the positive first-jet contribution of the genuine heat equation. BT19–20 and WR12–14 give its complete matrices in the original Cauchy and Laurent tests. This computes the change introduced by the added contact dynamics; the unmodified arithmetic flow keeps its original equation.

## SZ-20260923-131 — The next unit coefficient reaches the earlier determinant

Set \(A_n=\mathbb C[x]/(x^n)\) and \(\lambda_n(f)=\operatorname{Res}_{x=0} f\,dx/(x^nu(x))\). The full marked residue pairing determines exactly \(u\bmod x^n\). Under these perfect pairings, the quotient \(A_N\to A_n\) has transpose \(f\mapsto x^{N-n}\widetilde f\). The proofs retain every kernel and support label.

Write \(A=L_1/L_0\) and \(B=L_2/L_0\). The original unit coefficients are \(c=-A\), \(d=A^2-B\), and \(b=A^2-2B\). RJ20 and RJ24 insert these into the full earlier fixed-test correction HR4 and determinant correction HR14. Order two is necessary and sufficient for the full layer-zero correction. Order three is necessary and sufficient for every positive-index flag and for the determinant when \(m\ge2\); actual polynomial heat families prove necessity. For a double zero, changing the new datum by \(\Delta B\) changes the layer-one \(t^2\) coefficient by \(-4\Delta B\,\overline{f_1}g_1\), and the relative determinant correction by \(-4\Delta B\). The new \(A_3\) is an analytic thickening; the multiplicity remains two.

## SZ-20260923-132 — Independent reproduction of the supplied rational witness

The coefficients are \(c_i=1000^in_i/10^{120}\), \(0\le i\le18\), exactly as in `rational_witness.json`. Complete theta integration, with directed intervals and explicit quadrature and tail errors, gives:

| Original time | Complete root-trace value |
|---|---|
| \(-2\) | \([-2.385,-2.383]\times10^{-46}\) |
| \(0\) | \([0.00081442298606666852,0.00081442298606666854]\) |

The derivative is positive at both times. These signs reproduce the supplied calculation. Every root enters the moment identities; no selected-root remainder is omitted. The implementation does not certify the companion manuscript's separate 32-dimensional inertia claims. WR12–14 map the contact defect into this exact test space.

## Sources and reproduction

The human heat source is Brad Rodgers and Terence Tao, [*The de Bruijn–Newman constant is non-negative*, original author version 5](https://arxiv.org/abs/1801.05914v5), equations `hoz`, `sas`, `phidef`, and `htdef`. Classical entire-function factorization is credited to Jacques Hadamard, [1893 paper](https://www.numdam.org/item/JMPA_1893_4_9__171_0/). The earlier residue/trace conventions are [HH23–28 in the pinned public proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/3c022a0adde0a6aa3d8fc8e43ef42795d88e44b0/workbenches/splitzero-tandem/continuations/20260923-supported-zero-collision-holonomy/HEAT_COLLISION_HOLONOMY.tex). `SOURCE_AND_RESULT_INDEX.json` records files, versions, reading coverage, receiving formulas and hashes. Original supplied papers retain their citations.

The incoming checker passed 1848 finite checks and 11 negative controls. The new contact checker passed 276 checks; the residue receiver passed 650 checks in ordinary and optimized Python. Full analytic proofs accompany these checks. All 16 new PDF pages and both diagrams were rendered and inspected.

Run in a working copy with Python, SymPy, mpmath and LuaLaTeX installed:

```text
python check_boundary.py
python check_contact_trace.py
python check_residue_jet_fixed_tests.py
python reproduce_rational_witness.py
lualatex -interaction=nonstopmode -halt-on-error BOUNDARY_RESIDUE_ARITHMETIC_RECEIVERS.tex
```

Run LaTeX twice for the contents and cross-references. The numerical proof uses directed `mpmath.iv` arithmetic; formal verification of that library is not claimed. Exact binary endpoints and analytic remainder bounds are included. The whole RH programme remains unfinished.
