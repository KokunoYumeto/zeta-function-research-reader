# Exact calibration of the branch connection and its derivative domain

This calibration accompanies FC.1–20 in `tex/sum_connection_stieltjes.tex`. It retains both original spectral branches, the original coefficient functions, their derivatives, every matrix weight and normal component, and the half-line Jacobian. Its finite frames and Gaussian-polynomial amplitude are explicitly specified below. They supply exact independent checks of the displayed transport identities. They do not identify these finite frames or this amplitude with the arithmetic theta source, and they make no asymptotic or RH claim.

The final checker records 847 successful comparisons in ordinary Python and in `python -O`: 829 exact equalities or sign tests and 18 controls that detect deliberately omitted terms or false claims. The failure-injection runs add a false signed-branch equality as record 848 and both exit with status 1. Successful runs exit with status 0. The complete records retain every fixture name. The record arrays agree in both Python modes. The implementation uses SymPy 1.13.1 and explicit exceptions, without Python `assert`, floating-point arithmetic, quadrature, or Lean.

## Original finite frame

The non-even frame is the linear injection from `C²` into `C⁴`

\[
j(u)=\begin{pmatrix}
1&0\\0&1\\1+u&1+u\\1+u^2&2(1+u^2)
\end{pmatrix}.
\]

Its first two rows give `j(u)c=0 ⇒ c=0` at every real `u`. With the usual Hermitian forms, its original weight is

\[
W(u)=I_2+(1+u)^2\begin{pmatrix}1&1\\1&1\end{pmatrix}
 +(1+u^2)^2\begin{pmatrix}1&2\\2&4\end{pmatrix}>0.
\]

The two rank-one matrices have nonzero commutator, and their coefficients at `u=0` and `u=2` are not proportional; the checker directly verifies `[W(0),W(2)]≠0`. The weight is not even. The original frame has `B=j* j'=W'/2` because every variable row is a real scalar function times a constant row. The checker computes `Γ=W⁻¹B`, `Π=jW⁻¹j*`, and `N=(I−Π)j'` directly from the original frame at each branch point. For `u≠0`, `j'(u)` has independent bottom rows and zero top rows. Thus `N(u)c=0` implies `j'(u)c=j(u)d`; comparison of the top rows gives `d=0`, and the bottom rows then give `c=0`. Consequently the full normal Gram is positive at every nonzero sample radius. Its positivity is checked by its original leading principal minor and determinant.

The independent original coefficient vector is

\[
f(S)=\binom{2+(1+i)S-3S^2+S^4}{1-i+2S^2-iS^3+S^5},\qquad
c(u)=f(k/2+iu).
\]

The centers are `k/2=1/2,3/2,2`; the positive branch radii are `1/3,1/2,1,3/2,2`. Each original derivative is calculated directly as

\[
\frac d{du}(j(u)c(u))=j'(u)c(u)+j(u)c'(u).
\]

The paired polynomials are independently assembled from the full binomial formula FC.13 and are checked against the original `f(S)` through its exact inverse. Both their degree bounds and every center coefficient are retained. At every sample, the checker compares the directly differentiated original branch norm, divided by `2v`, with the complete right-hand density of FC.15. It also compares the undifferentiated original density, the signed chain rule on each branch, the separate normal Gram congruence, the multiplication by `S`, and the derivative and constant coefficients of `[J∇ₓ,S]=iI`.

The metric and frame checks explicitly include

\[
M^{-1}M'=\operatorname{diag}(0,(2x)^{-1}I),\qquad
J^*HJ=4xH,\qquad A^*H+HA=H'+H/(2x).
\]

The positive Jacobian `1/(2v)` occurs on both norm branches. The coefficient derivative on the negative branch has the signed factor `−2v`. Controls detect omission of that sign, the density drift, the moving-basis derivative, and the full normal energy.

## Even frame and variable complex frame

The even frame replaces the two variable row multipliers by `1+u²` and `1+u⁴`, retaining their distinct constant row directions and the top identity block. The checker directly computes its original derivatives before comparing them with every block in FC.19 and its full even energy formula. Its weights at `u=0` and `u=2` also fail to commute. Thus the even checks do not silently commute matrix coefficients.

The separate variable frame is

\[
C(u)=\begin{pmatrix}1&u+i\\0&1\end{pmatrix},\qquad j^C(u)=j(u)C(u).
\]

Its determinant is one at every real `u`. At original points `−3/2,0,2/3,2`, the checker differentiates `jC` directly and verifies the complete changed weight, `B`, connection, projection, normal map and normal Gram. It rejects the generally false equality `B^C=(W^C)'/2`. The paired gauge checks use the positive radius `|u|`, with radius `1/2` for the sample `u=0`; they retain the two ordered evaluations at that radius and its negative. The density-drift identity therefore remains a positive half-line check, including at original negative-frame samples.

## Scalar amplitude with its original mass

The scalar calibration uses the entire real amplitude

\[
a(t)=t e^{-t^2/2},\quad w(t)=t^2e^{-t^2},\quad
\mu=\sqrt\pi/2,\quad I=4\int|a'|^2=3\sqrt\pi.
\]

Gaussian moments are evaluated exactly by

\[
\int_{\mathbb R}t^{2n}e^{-\beta t^2}dt
 =\Gamma(n+1/2)\beta^{-n-1/2},\qquad
\int_{\mathbb R}t^{2n+1}e^{-\beta t^2}dt=0.
\]

In the original two-factor fiber `t₁=u/2+y`, `t₂=u/2−y`, with measure `du dy`,

\[
\Psi=(u^2/4-y^2)e^{-u^2/4-y^2},\qquad
m(u)=\frac{\sqrt{\pi/2}}{16}(u^4-2u^2+3)e^{-u^2/2}.
\]

The checker differentiates this original `Ψ`, integrates its polynomial factors exactly in `y`, verifies its line/normal decomposition at five real fibers, and integrates its entire squared derivative:

\[
\int\|\partial_u\Psi\|^2du=\mu I/8=3\pi/16.
\]

The original mass factor is tested and a control rejects its omission. The original residual is zero at `u=0` and positive at the four nonzero tested fibers. For `ρ(x)=m(√x)/√x`, the checker verifies the symbolic identity

\[
2x\bigl(\rho'(x)+\rho(x)/(2x)\bigr)=m'(\sqrt x)
\]

and the equality of the entire radial Fisher density in FC.20. A separate control rejects deleting its drift term.

## The exact joining-domain witness

Use the same original non-even frame and `e=(1,0)ᵀ`, and put

\[
c(u)=\begin{cases}e^{-u}e,&u>0,\\2e^u e,&u<0.\end{cases}
\]

Both its open-branch norm and its open-branch derivative energy are finite. Direct integration of their full original polynomial factors against `e^{-2v}dv` gives

\[
\int_{\mathbb R\setminus\{0\}}\|j(u)c(u)\|^2du=27/2,\qquad
\int_{\mathbb R\setminus\{0\}}\|(j(u)c(u))'\|^2du=9.
\]

These integrals use `∫₀∞vⁿe⁻²ᵛdv=n!/2ⁿ⁺¹`; every coefficient is retained. The exact paired vector is

\[
q(x)=e^{-\sqrt x}\binom{(3/2)e}{i e/(2\sqrt x)}.
\]

The checker compares its full transported norm and derivative energy densities with the independently computed originals at four positive radii. Its two limits are exactly `e` and `2e`, so they fail FC.18. The original vector jump is

\[
j(0)(e-2e)=(-1,0,-1,-1)^T.
\]

Integration by parts against an arbitrary compactly supported smooth test function gives the ordinary open-branch derivative plus this nonzero vector times `δ₀`. A nonzero delta distribution cannot be represented by an `L²` function: for a fixed test function equal to one at zero, its rescaling to support of length `ε` has `L²` norm tending to zero while the delta pairing stays one. Thus the original joined function has no `L²` weak derivative although all paired open-domain integrals are finite. The full two-branch map consequently requires precisely the matching condition stated in FC.18.

## Reproducibility and review scope

Run `python scripts/check_sum_connection_stieltjes.py --output checks/sum_connection_stieltjes.json`; add `-O` before the script for the optimized run, or `--inject-failure` for the deliberate-failure run. The four sealed receipts are `sum_connection_stieltjes.json`, `sum_connection_stieltjes_optimized.json`, `sum_connection_stieltjes_negative.json`, and `sum_connection_stieltjes_negative_optimized.json`. The manifest pins the checker, this report, the receipts, and the independent reviewer’s file. The reviewer read FC.1–20 and the current checker; the later strict arithmetic positivity and higher-derivative claims are outside this finite calibration’s claimed scope.
