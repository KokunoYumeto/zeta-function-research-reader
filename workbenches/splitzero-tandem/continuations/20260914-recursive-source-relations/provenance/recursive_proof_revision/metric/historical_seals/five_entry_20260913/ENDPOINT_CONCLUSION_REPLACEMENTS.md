# Literal replacements at earlier endpoint conclusion sites

Baseline SHA-256: cec03014398811e5fa4788cb7b6f4816123c026d673a1a9a0398b7fded360e3b

Root owns the conclusion file. These are isolated literal old/new blocks; each preserves the old result and substitutes the propagated control at its original paragraph. No conclusion file was edited. JSON start_line is inclusive and end_line is exclusive.

## R44 endpoint costs: original lines 1436–1439

Old:
```latex
Both additional logarithms are nonnegative by minimization over
nested lift spaces. Substitution of $L_{h,k}/q_k\ge\delta k/2$,
division by $q_k\log k$, and $(q_k-1)/q_k\to1$ prove the
necessary four-volume lower limit $4$ in (EP.50e).

```

Replacement:
```latex
Both additional logarithms are nonnegative by minimization over
nested lift spaces. Substitution of $L_{h,k}/q_k\ge\delta k/2$,
division by $q_k\log k$, and $(q_k-1)/q_k\to1$ prove the
necessary four-volume lower limit $4$ in (EP.50e).
The new signed control is now substituted into this same identity.
Write $q=q_k$ and retain the arithmetic endpoint losses
$E_0=\log(V_{q-1}/V_q)$, $E_1=\log(V_{2q-1}/V_{2q})$, and put
$\mathcal B_{h,k}=2C_k+E_0+E_1$. On the original Gamma-to-arithmetic
moment path, (FV.M1)--(FV.M18) proves the exact identity
$\mathcal B_{h,k}=\mathcal B^\Gamma_{h,k}+\Delta_{h,k}$ and
$|\Delta_{h,k}|\le\mathfrak J_{h,k}$, where
\[
 \mathfrak J_{h,k}=\int_0^1
 \min\{S_{\rm AW}(x),T_q(x),S_{\rm SP}(x),S_{\rm HS}(x),
             (2q-1)\sqrt{1-e^{-F(x)/(2q-1)}}\,d_x\}\,dx.
\]
Here $F(x)$ is the unchanged four-volume function and $d_x$ the
full original relative spectral diameter. The full formulas for
$S_{\rm AW},S_{\rm SP}$, their exact source correspondence and
the nonlinear coordinate are proved at that original endpoint site.
Equation (FV.M15a) retains
$T_q=d_x\|U_x-W_x\|_1/2$ and
$S_{\rm HS}=\sqrt{\Sigma_x\operatorname{Tr}((U_x-W_x)^2)}$, where
$\Sigma_x=\operatorname{Tr}(C_x^2)-(\operatorname{Tr}C_x)^2/(2q+1)$,
and proves both bounds on the original metric by midpoint centering
and centered Hilbert--Schmidt Cauchy--Schwarz. The last minimum entry
is the actual-moment specialization of RMT11. Every entry is retained,
including the exact $T_q$ and its majorant $S_{\rm SP}$.
Let $a=2q-1$, $H_0=2\operatorname{arcosh}
(e^{\mathcal B^\Gamma_{h,k}/(2a)})$, and retain the complete
$\mathfrak I_{h,k}^{\rm nl}$ of (FV.M15). The simultaneous endpoints are
\[
 \begin{aligned}
 \mathcal B_{h,k}^{\rm lo}
 &=\max\left\{0,\mathcal B^\Gamma_{h,k}-\mathfrak J_{h,k},
 2a\log\cosh\left(\frac{\max\{0,H_0-\mathfrak I_{h,k}^{\rm nl}\}}2\right)\right\},\\
 \mathcal B_{h,k}^{\rm hi}
 &=\min\left\{\mathcal B^\Gamma_{h,k}+\mathfrak J_{h,k},
 2a\log\cosh\left(\frac{H_0+\mathfrak I_{h,k}^{\rm nl}}2\right)\right\}.
 \end{aligned}
\]
Monotonicity of the exact inverse coordinate in (FV.M16)--(FV.M18)
and the signed bound give
\[
 \begin{gathered}
 \mathcal B_{h,k}^{\rm lo}\le\mathcal B_{h,k}
                  \le\mathcal B_{h,k}^{\rm hi},\\
 4(q-1)\log\frac{L_{h,k}}{C_h^{\rm bal}q}+E_0+E_1
       \le\mathcal B_{h,k}^{\rm hi},\qquad
 C_k\le\frac{\mathcal B_{h,k}^{\rm hi}-E_0-E_1}{2}.
 \end{gathered}
\]
The last two inequalities substitute the retained central lower bound
and the exact four-volume identity; neither arithmetic endpoint loss
is omitted. The proper-source primitive residual is the exact tensor
intersection quotient (FV.M13), with the one-leg $V/W$ map proved in
(FV.M14), so this metric comparison does not erase any proper-source
class.


```

## R45 upper gap: original lines 1483–1489

Old:
```latex
All constants and the literal source mass are retained. For
$\mathcal L_k=2(q_k-1)\log(\delta k/(2C_h^{\rm bal}))$,
(AU.32) computes every term of $\mathcal U_k-\mathcal L_k$,
and (AU.33) proves that its quotient by $q_k^2$ tends to
$\alpha D+\log256>0$. This upper estimate leaves the stated
gap to the quartet lower estimate.


```

Replacement:
```latex
All constants and the literal source mass are retained. For
$\mathcal L_k=2(q_k-1)\log(\delta k/(2C_h^{\rm bal}))$,
(AU.32) computes every term of $\mathcal U_k-\mathcal L_k$,
and (AU.33) proves that its quotient by $q_k^2$ tends to
$\alpha D+\log256>0$. This upper estimate leaves the stated
gap to the quartet lower estimate.
The propagated original-source estimate is the additional bound
\[
 C_k\le\mathcal U_k^{\rm signed}
   :=\frac{\mathcal B_{h,k}^{\rm hi}-E_0-E_1}{2}.
\]
Its complete proof (AU.31a)--(AU.31b) transports the unchanged monomial
source and original relation by $P(S)\mapsto P(k/2+iu)$, retaining
the factor $i^q$ and every raw derivative factor $i^d$. This signed
entry uses actual moments through $4q$; the original first matrix
bound continues to require actual moments only through $2q$.
Let $\widehat{\mathcal U}_k$ be the minimum of this signed entry
and all the full bounds in (AU.31b), including the original
$\mathcal U_k$ and the actual low-degree matrix entry. They bound
the same $C_k$, so
\[
 \mathcal L_k\le C_k\le\widehat{\mathcal U}_k\le\mathcal U_k,
 \qquad
 0\le\widehat{\mathcal U}_k-\mathcal L_k
       \le\mathcal U_k-\mathcal L_k.
\]
The positive limit in (AU.33) belongs to the explicitly displayed
old scalar majorant; it is not assigned to this refined minimum.
The complete angle, spectral, and overlap integrands remain the
actual quantities controlling the newly narrowed finite interval.


```

## R47 joint budget: original lines 1595–1610

Old:
```latex
The arithmetic remainder estimate is extended to every admitted
degree with its entire monic quotient formula. In the original
notation of the upper-comparison chapter, it gives
\[
 G_{q-1}\preceq C_NG_N,\qquad
 C_N=\frac{U_k(T)A_N^2B_q(r)^2}{T a_k(T)},\qquad
 N\ge q-1,
\]
with $T=Dq$, $r=kR_0/T<1$, the unchanged original density mass,
and all constants defined in the complete proof. Thus the actual
endpoint gaps $C_{2q-1}^{-1}$ and $C_{2q}^{-1}$ are proved
arithmetic inequalities. The exact ratio satisfies
$C_{2q}/C_{2q-1}\le147/5<32$, so the same construction gives
$\mathcal B_{h,k}\le2\mathcal U_k+q\log32$ with
$\mathcal U_k$ from R45.


```

Replacement:
```latex
The arithmetic remainder estimate is extended to every admitted
degree with its entire monic quotient formula. In the original
notation of the upper-comparison chapter, it gives
\[
 G_{q-1}\preceq C_NG_N,\qquad
 C_N=\frac{U_k(T)A_N^2B_q(r)^2}{T a_k(T)},\qquad
 N\ge q-1,
\]
with $T=Dq$, $r=kR_0/T<1$, the unchanged original density mass,
and all constants defined in the complete proof. Thus the actual
endpoint gaps $C_{2q-1}^{-1}$ and $C_{2q}^{-1}$ are proved
arithmetic inequalities. The exact ratio satisfies
$C_{2q}/C_{2q-1}\le147/5<32$, so the same construction gives
$\mathcal B_{h,k}\le2\mathcal U_k+q\log32$ with
$\mathcal U_k$ from R45.
The same-source metric refinement now gives the stronger literal
joint budget
\[
 \mathcal B_{h,k}^{\rm lo}\le\mathcal B_{h,k}\le
 U_{h,k}^{\rm joint}:=
 \min\{q\log C_{2q-1}+q\log C_{2q},\mathcal B_{h,k}^{\rm hi}\}.
\]
Equation (ERJ.32a) proves the required equality of the monic-source
and monomial-source quotient kernels before taking this minimum.
The complete five-estimate pointwise minimum and its nonlinear transport
therefore apply to these exact original restriction returns.
The two finite trace-certificate upper endpoints below may also be
summed and included in the same minimum; their original entry errors
and series tails remain attached to their actual matrices.


```

## R47 inverse powers: original lines 1680–1683

Old:
```latex
Indeed the central trace is one plus the inverse-power sum of its
remaining $q-1$ eigenvalues. The tangent inequality $e^y\ge1+y$
at their logarithmic mean bounds this sum from below by their
geometric mean, and the ordered comparison transfers every eigenvalue.

```

Replacement:
```latex
Indeed the central trace is one plus the inverse-power sum of its
remaining $q-1$ eigenvalues. The tangent inequality $e^y\ge1+y$
at their logarithmic mean bounds this sum from below by their
geometric mean, and the ordered comparison transfers every eigenvalue.
These same inverse observations also acquire the finite upper
control proved in (ERJ.32b):
\[
 \operatorname{Tr}U_{q-1,2q-1}^{-s}
 +\operatorname{Tr}U_{q,2q}^{-s}
 \le2q-1+e^{s\mathcal B_{h,k}}
 \le2q-1+e^{sU_{h,k}^{\rm joint}}.
\]
Indeed all $2q$ return eigenvalues $g_{a,j}$ lie in $(0,1]$ and
their negative logarithms sum exactly to $\mathcal B_{h,k}$.
Writing $z_{a,j}=g_{a,j}^{-s}-1\ge0$, expansion gives
$\prod(1+z_{a,j})\ge1+\sum z_{a,j}$, which is precisely the
displayed bound. Each individual eigenvalue also satisfies
$g_{a,j}\ge e^{-\mathcal B_{h,k}}\ge e^{-U_{h,k}^{\rm joint}}$.
The original lower bounds and central unit eigenvalues above are
retained simultaneously, with their full phase/contraction penalty.


```
