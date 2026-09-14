# Independent nonscalar fourth-jet check of RCX28 and RCX30–32

The new companion's noncommutative fourth trace-log formula and period-derivative ordering agree with a separately computed period solution on the exact three-dimensional fixture below. The constituent has dimension two, its Gram is nonscalar, its derivative matrices do not commute, and its pure fourth logarithmic derivative has nonzero real and imaginary parts. All forty-one exact checks passed in one normal process and one `-O` process. No failure or correction occurred.

## Reviewed version and execution record

The source was `workspace:/work/residue_constituent_extension_20260913.tex`, specifically RCX25–32. The exact version read is retained in `reviewed_companion_snapshot.tex`, SHA-256 `449d2107fb97369eeb27dfcc0151012da831222a25432cc5b3e1894ff06defc0`. Later parent integration may change the live companion; this receipt identifies the version actually checked.

The complete new checker is `check_additional_fourth_jet.py`, SHA-256 `af8daa6b279414e7182d424069cad63308ebe5d1760dfaf85a23b36a1a41574b`. Its recorder is `run_additional_check.py`, SHA-256 `07088cae7e5ff0e82668f449a4f4039f6e7f9ee66f6e221b565f461b5b13fcb5`. Both are local to `workspace:/work/residue_constituent_additional_jet_check_20260913`. They import no previous checker. The checker uses explicit exceptions, with zero Python `assert` statements. Every input matrix, all Taylor coefficients through degree four, all Q polynomials through Q4, all D matrices, and every pure and mixed scalar logarithm coefficient through total degree four appear in both complete stdout records.

The actual argument arrays are:

```text
["runtime:research-python/python.exe", "workspace:/work/residue_constituent_additional_jet_check_20260913/check_additional_fourth_jet.py"]
["runtime:research-python/python.exe", "-O", "workspace:/work/residue_constituent_additional_jet_check_20260913/check_additional_fourth_jet.py"]
```

Native Windows separators are preserved in `execution_receipt.json`. Both processes used Python 3.13.9 and SymPy 1.14.0, imported from `workspace:/work/kernel_layer_replay_dependencies_20260912/sympy/__init__.py`. `PYTHONPATH` was that dependency directory and `PYTHONDONTWRITEBYTECODE=1`.

| Mode | Started UTC, 2026-09-13 | Runtime seconds | Exit | Exact checks |
| --- | --- | ---: | ---: | ---: |
| normal | 04:47:57.132319 | 1.0847873000020627 | 0 | 41 |
| optimized | 04:47:58.219598 | 1.1299177999899257 | 0 | 41 |

Both complete stderr files are empty. The normal and optimized JSON records agree in every field except the correctly reported optimization level 0 versus 1. These are forty-one checks on one fixture, not forty-one independent fixtures or unittest methods. Exactly two checker processes were executed. No earlier supplied or predecessor suite was rerun, and no Lean, Lake, or Elan process was launched. The previously sealed supplied-replay directory was not edited.

## The fixed original objects

Work in `E=C[S]/(S³+2S)`, with the ordered coefficient basis `(1,S,S²)`, and use the actual invariant ideal `F=(S)=span(S,S²)`. Its inclusion and quotient are

\[
I=\begin{pmatrix}0&0\\1&0\\0&1\end{pmatrix},\qquad
\pi=\begin{pmatrix}1&0&0\end{pmatrix}.
\]

The multiplication, unit, residue, and restricted multiplication are exactly

\[
A=\begin{pmatrix}0&0&0\\1&0&-2\\0&1&0\end{pmatrix},\quad
e=\begin{pmatrix}1\\0\\0\end{pmatrix},\quad
\ell=\begin{pmatrix}0&0&1\end{pmatrix},\quad
R=e\ell=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix},\quad
A_F=\begin{pmatrix}0&-2\\1&0\end{pmatrix}.
\]

Direct multiplication gives `AI=IA_F`, `pi I=0`, and `ell I=(0,1)`. The columns of I are independent, pi is onto, and `0<dim F=2<dim E=3`.

Retain `u=3/2` and the initial period matrix

\[
B=\begin{pmatrix}
1&(1+i)/2&(2-i)/3\\
0&1&(1+2i)/3\\
0&0&1
\end{pmatrix}.
\]

Its determinant is one. Hence the original complex-rational Hermitian matrix

\[
H_0=B^*B=
\begin{pmatrix}
1&(1+i)/2&(2-i)/3\\
(1-i)/2&3/2&(3+i)/6\\
(2+i)/3&(3-i)/6&19/9
\end{pmatrix}
\]

is strictly positive: for every nonzero vector v, `v* H0 v=||Bv||²>0`. This proves positivity without replacing H0 by a scalar or diagonal metric. The constituent Gram and its determinant are

\[
H_F=I^*H_0I=\begin{pmatrix}3/2&(3+i)/6\\(3-i)/6&19/9\end{pmatrix},
\qquad \det H_F=26/9.
\]

Both H0 and HF have nonzero nonreal off-diagonal entries and are nonscalar.

## Independent period solution and the order of Q

Write the original equation as `Pi'(t)=−Pi(t)(A+tR)/u`, with `Pi(0)=B`, and expand `Pi(t)=sum B_n t^n`. Matching coefficients, with `B_{−1}=0`, gives the ordered recurrence

\[
(n+1)B_{n+1}=-\frac{B_nA+B_{n-1}R}{u}.
\]

This recurrence determines every coefficient uniquely and was the route used for the actual period Taylor solution in the checker. Its products remain on the right of B_n. Independently, differentiation of `Pi^(n)=Pi Q_n` gives

\[
\Pi^{(n+1)}=\Pi'Q_n+\Pi Q_n'
=\Pi\left(Q_n'-\frac{A+tR}{u}Q_n\right).
\]

Starting at `Q0=I3`, this proves RCX30 by induction, with the factor `A+tR` on the left of Q_n. The first higher polynomials, without commuting A and R, are

\[
\begin{aligned}
Q_1&=-A_t/u,\\
Q_2&=A_t^2/u^2-R/u,\\
Q_3&=-A_t^3/u^3+(RA_t+2A_tR)/u^2,\\
Q_4&=A_t^4/u^4-
 (RA_t^2+2A_tRA_t+3A_t^2R)/u^3+3R^2/u^2,
\qquad A_t=A+tR.
\end{aligned}
\]

To obtain Q4, differentiate the three ordered factors in `A_t³` separately. Differentiating `RA_t+2A_tR` gives `3R²`. The additional left multiplication of Q3 by `−A_t/u` contributes `−A_tRA_t/u³−2A_t²R/u³` to the derivative's coefficients `−RA_t²/u³−A_tRA_t/u³−A_t²R/u³`, yielding the displayed multiplicities 1,2,3. No exchange of matrix factors occurs.

On the fixed fixture, the exact matrices `T_n=Q_n(0)` for n=1,...,4 are

\[
\begin{gathered}
T_1=\begin{pmatrix}0&0&0\\-2/3&0&4/3\\0&-2/3&0\end{pmatrix},\qquad
T_2=\begin{pmatrix}0&0&-2/3\\0&-8/9&0\\4/9&0&-8/9\end{pmatrix},\\
T_3=\begin{pmatrix}0&4/9&0\\16/27&0&-8/27\\0&16/27&0\end{pmatrix},\qquad
T_4=\begin{pmatrix}-8/27&0&16/27\\0&16/81&0\\-32/81&0&-8/81\end{pmatrix}.
\end{gathered}
\]

The independently computed right-recurrence coefficients satisfy the full matrix equations `n! B_n=B T_n` for every n=0,...,4. Thus the actual fourth Taylor truncation is exactly

\[
\Pi(t)=B\left(I_3+T_1t+T_2t^2/2+T_3t^3/6+T_4t^4/24\right)+O(t^5).
\]

The full polynomial Q3 was also checked against RCX31 for symbolic t. Reversing its two order multiplicities produces, at zero, the nonzero residual

\[
\frac{RA-AR}{u^2}
=\begin{pmatrix}0&4/9&0\\0&0&-4/9\\0&0&0\end{pmatrix}.
\]

The ordering check is therefore substantive on this fixture.

## The noncommutative trace-log coefficient

Define, as in RCX32,

\[
D_n=H_F^{-1}I^*H_0Q_n(0)I,\qquad 1\le n\le4.
\]

For `K(t)=I* B* Pi(t) I`, its initial value is HF and
`HF^−1 K(t)=I2+D1 t+D2 t²/2+D3 t³/6+D4 t⁴/24+O(t⁵)`.
The constant `log det HF` is retained; only its positive-order derivatives vanish. Put `Z=D1 t+D2 t²/2+D3 t³/6+D4 t⁴/24`. The fourth coefficient of the convergent trace-log series uses the following ordered products:

\[
\begin{array}{c|l}
\text{term}&24[t^4]\text{ term}\hline
\operatorname{Tr}Z&\operatorname{Tr}D_4\\
-\tfrac12\operatorname{Tr}Z^2&
\operatorname{Tr}\bigl(-2D_1D_3-2D_3D_1-3D_2^2\bigr)\\
\tfrac13\operatorname{Tr}Z^3&
4\operatorname{Tr}\bigl(D_1^2D_2+D_1D_2D_1+D_2D_1^2\bigr)\\
-\tfrac14\operatorname{Tr}Z^4&-6\operatorname{Tr}D_1^4.
\end{array}
\]

Terms with five or more factors have degree at least five. Cyclic trace equates the two quadratic cross terms and the three cubic terms, proving precisely

\[
\phi^{(4)}(0)=\operatorname{Tr}
\left(D_4-4D_1D_3-3D_2^2+12D_1^2D_2-6D_1^4\right).
\]

This is an identity under trace; it does not assert that the matrices commute. In fact the executed fixture gives

\[
D_1D_2-D_2D_1=
\begin{pmatrix}
-14/117+8i/39&-10/39-10i/39\\
-5/39-5i/39&14/117-8i/39
\end{pmatrix}\ne0.
\]

Direct substitution of the recorded D matrices in RCX32 gives

\[
\phi^{(4)}(0)=\frac{164}{117}+\frac{295}{1014}i.
\]

## Independent scalar determinant calculations retaining all pure jets

The checker computed the scalar determinants directly from the actual period coefficients obtained by the right recurrence, before using RCX32. The two exact degree-four determinant expansions are

\[
\begin{aligned}
\det\bigl(I^*B^*\Pi(t)I\bigr)
&=\frac{26}{9}-\frac{5+5i}{18}t^2
  +\frac{-28+48i}{243}t^3
  +\frac{41+15i}{243}t^4+O(t^5),\\
\det\bigl(I^*\Pi(x)^*\Pi(x)I\bigr)
&=\frac{26}{9}-\frac59x^2-\frac{56}{243}x^3
  +\frac{109}{243}x^4+O(x^5),\qquad x\in\mathbb R.
\end{aligned}
\]

For either determinant `d(z)=sum d_n z^n`, write its scalar logarithm as `ell(z)=log(d0)+sum_{n>=1} ell_n z^n`. The identity `d'=d ell'` gives

\[
\ell_n=\frac{n d_n-\sum_{k=1}^{n-1}k\ell_k d_{n-k}}{n d_0}.
\]

This scalar derivative recurrence supplied a calculation independent of the noncommutative matrix expression. In the present fixture `d1=0`, so `ell2=d2/d0`, `ell3=d3/d0`, and `ell4=d4/d0−d2²/(2d0²)`. Therefore

\[
\begin{aligned}
\phi(t)&=\log(26/9)
 -\frac{5+5i}{52}t^2
 +\left(-\frac{14}{351}+\frac{8i}{117}\right)t^3
 +\left(\frac{41}{702}+\frac{295i}{24336}\right)t^4+O(t^5),\\
\psi(x)&=\log(26/9)
 -\frac5{26}x^2-\frac{28}{351}x^3
 +\frac{4993}{36504}x^4+O(x^5).
\end{aligned}
\]

All pure coefficients remain present. In particular `24[t⁴]phi=164/117+295i/1014`, agreeing with RCX32, while the real fourth derivative computed directly from the real Gram is `24[x⁴]psi=4993/1521`.

## Exact mixed coefficient and the sixfold contribution

The original metric quotient cost and residue dual cost are

\[
q_{H_0,F}([e])
=e^*H_0\left(I_3-IH_F^{-1}I^*H_0\right)e=\frac9{26},
\qquad
(\ell I)H_F^{-1}(\ell I)^*=\frac{27}{52}.
\]

For the first value, the Schur complement of HF in H0 equals `det H0/det HF=1/(26/9)=9/26`; for the second, the lower right entry of `HF^−1` is `(3/2)/(26/9)=27/52`. Hence

\[
\mathfrak c_F(H_0)=\frac{243}{1352},\qquad
\frac{\mathfrak c_F(H_0)}{|u|^2}=\frac{27}{338}.
\]

A separate bivariate computation uses `t,w` as independent variables and the exact Gram `sum_{a,b} (B_a I)* (B_b I) w^a t^b`, retaining every term of total degree at most four. Multiplication does not decrease degree, so neither an omitted degree-five period jet nor a discarded higher-degree term can change these coefficients. Taking its two-by-two determinant and the scalar logarithm through fourth order gives

\[
\begin{aligned}
\psi(t,w)=\log(26/9)
&+a_2t^2+\bar a_2w^2+a_3t^3+\bar a_3w^3\\
&+a_4t^4+\bar a_4w^4+\frac{27}{1352}t^2w^2
+O_{\rm total}(5),
\end{aligned}
\]

where the three exact pure coefficients `a2,a3,a4` are those displayed in phi above. The coefficients at `(1,1)`, `(2,1)`, `(1,2)`, `(3,1)`, and `(1,3)` vanish, and the two pure first coefficients vanish. Thus every bidegree through four is specified. Differentiating `t²w²` multiplies its coefficient by `2!2!=4`, giving `27/338`, exactly the mixed derivative predicted by RCX26.

Along the real axis `t=w=x`, the full fourth derivative is consequently

\[
\begin{aligned}
\psi^{(4)}_{\mathbb R}(0)
&=24\left(a_4+\bar a_4+\frac{27}{1352}\right)\\
&=2\operatorname{Re}\phi^{(4)}(0)
  +6\frac{\mathfrak c_F(H_0)}{|u|^2}\\
&=\frac{328}{117}+\frac{81}{169}
 =\boxed{\frac{4993}{1521}}.
\end{aligned}
\]

The coefficient six is the binomial factor `4!/(2!2!)`. The pure contribution `328/117` is nonzero and is required for agreement with the directly expanded real Gram. The second derivative similarly equals `−5/13=2 Re(−(5+5i)/26)`, confirming the real second-derivative identity in RCX28 as well.

## Evidence and conclusion

`normal.stdout.json` and `optimized.stdout.json` contain the complete forty-one-check inventory, exact fixture, original coefficient and metric matrices, Taylor and Q matrices, D matrices, noncommutativity witnesses, all pure and real determinant coefficients, all logarithmic coefficients and derivatives, and the zero residual of RCX28. `execution_receipt.json` binds the actual argv, times, exit codes, output paths and hashes, environment, and source/code pins. The independent read-only derivation of RCX30–32 is in `order_and_trace_proof.md`; it performed no extra checker execution.

There is no discrepancy in the audited companion formulas. This is one exact independent nonscalar finite verification, with its full calculation and execution evidence. Its findings can be integrated without changing or rerunning the previously sealed supplied replay.

The complete independent order-and-trace proof has SHA-256 `e587868ecb457c2b6d643c6fdc7bd592227cecfa54a674cd75e760dfdd3e453a`. Its hand-derived fourth derivative agrees exactly with the two executed results. A final read-only hash check confirms that all thirty-seven artifacts in the earlier supplied-replay seal remain unchanged; its manifest hash remains `d11ccc2a0ba181cbd0d11efaa960f620f98894cc3941d4c7b251e74663ce9f72`. That metadata verification is recorded in `prior_replay_immutability.json` and did not execute any earlier checker.
