# Independent exact incidence audit of AP.19–AP.20

Date: 2026-09-12. Scope: Gaussian calibration with variance `1/16`, tensor degrees `k=1, M=4,5,6` and `k=2, M=2,3,4`.

Verdict: AP.19 and AP.20 pass this independent audit. Every matrix below is exact. The domination has an explicit positive factorization, so no numerical eigenvalue or numerical PSD decision is involved. This calibration does not certify any assertion about actual zeta zeros.

## Task provenance and retained objects

The delegated task, verbatim:

> Independently audit incidence inequality AP.19–AP.20 in package:/tex/arithmetic_frontier_parity.tex. Task only: derive exact Gaussian variance1/16 incidence matrices L for k=1 M4,5,6 and k=2 M2,3,4; verify row sum Gamma and PSD domination by rational arithmetic / structural factor proof. Write standalone brief report workspace:/work/frontier_incidence_independent_review_20260912.md. Do not edit TeX or main checker. Send any errors immediately. Preserve monic original s=1/2+it coordinates; q recurrence a_j=j/16. No actual-zeta certification, no numerical PSD.

Keep the original coordinate `s=1/2+it` and original monic polynomials, defined by

\[
q_0(s)=1,\qquad q_1(s)=s-\tfrac12,\qquad
q_{j+1}(s)=(s-\tfrac12)q_j(s)+\frac{j}{16}q_{j-1}(s).
\]

Thus `s q_j=q_{j+1}+(1/2)q_j−(j/16)q_{j−1}` with the original negative lowering sign. Let `m=κ_0>0` denote the unchanged Gaussian measure mass. Its norms are

\[
\kappa_j=m\frac{j!}{16^j},\qquad a_j=\frac{j}{16},\qquad a_0=0.
\]

Indeed the given recurrence ratio `κ_j/κ_{j−1}=j/16` iterates to this formula from the retained mass. No polynomial or measure is divided by its norm. A probability Gaussian is the specialization `m=1`.

For tensor multi-indices retain `κ_α=∏_j κ_{α_j}`, `Ω_M=diag(κ_α)_{|α|=M}`, `Ω=diag(κ_β)_{|β|=M+1}`. The original incidence map is

\[
L:\mathbb C^{\{|\beta|=M+1\}}\longrightarrow
\mathbb C^{\{|\alpha|=M\}},\qquad
L_{\alpha\beta}=\sum_{j:\beta-e_j=\alpha}\frac{\beta_j}{16}.
\]

Writing `Z=[z_α]_{|α|=M}`, this definition proves `E_+=ZL` by equality of every column. The row-sum matrix and domination difference are

\[
N=\Omega_M L\Omega^{-1}L^*,\qquad
H=\Gamma_{k,M}\Omega_M^{-1}-L\Omega^{-1}L^*.
\]

## The three k=1 matrices

There is one degree-`M` index `(M)` and one degree-`M+1` index `(M+1)`. Consequently

\[
\Omega_M=[mM!/16^M],\quad
\Omega=[m(M+1)!/16^{M+1}],\quad
L=[(M+1)/16].
\]

Multiplication gives `N=[(M+1)/16]` and `H=[0]`. Explicitly:

| `(k,M)` | `L` | `N` | `Γ_{k,M}` | `H` |
|---|---|---|---|---|
| `(1,4)` | `[5/16]` | `[5/16]` | `5/16` | `[0]` |
| `(1,5)` | `[6/16]` | `[6/16]` | `6/16` | `[0]` |
| `(1,6)` | `[7/16]` | `[7/16]` | `7/16` | `[0]` |

This proves equality in the first incidence domination before applying `Z`, for all three one-factor cases.

## The three k=2 matrices

Order the lower indices as `α_i=(i,M−i)`, `0≤i≤M`, and upper indices as `β_r=(r,M+1−r)`, `0≤r≤M+1`. Then

\[
(\Omega_M)_{ii}=m^2\frac{i!(M-i)!}{16^M},\qquad
\Omega_{rr}=m^2\frac{r!(M+1-r)!}{16^{M+1}}.
\]

The two possible incidences give, with the stated row and column domains,

\[
L_{i,i}=\frac{M+1-i}{16},\qquad
L_{i,i+1}=\frac{i+1}{16},
\]

and all other entries are zero. These are respectively addition of `e_2` and `e_1` to `α_i`. Explicitly,

\[
L_{2,2}=\frac1{16}
\begin{pmatrix}3&1&0&0\\0&2&2&0\\0&0&1&3\end{pmatrix},
\quad
L_{2,3}=\frac1{16}
\begin{pmatrix}4&1&0&0&0\\0&3&2&0&0\\0&0&2&3&0\\0&0&0&1&4\end{pmatrix},
\]
\[
L_{2,4}=\frac1{16}
\begin{pmatrix}
5&1&0&0&0&0\\
0&4&2&0&0&0\\
0&0&3&3&0&0\\
0&0&0&2&4&0\\
0&0&0&0&1&5
\end{pmatrix}.
\]

For every contributing frontier `β=α+e_j`, the exact identity

\[
\frac{\kappa_\alpha a_{\beta_j}}{\kappa_\beta}=1
\]

follows from the factorial norm formula. The diagonal entry of `N` therefore sums `(i+1)/16` and `(M−i+1)/16`. The frontier `(i+1,M−i)` contributes the off-diagonal entry `(M−i)/16` in column `i+1`; the frontier `(i,M−i+1)` contributes `i/16` in column `i−1`. Hence

\[
N_{ii}=\frac{M+2}{16},\quad
N_{i,i-1}=\frac{i}{16}\ (i\ge1),\quad
N_{i,i+1}=\frac{M-i}{16}\ (i<M).
\]

In the endpoint rows the absent term has coefficient zero. Every row sum is exactly

\[
\frac{M+2+i+(M-i)}{16}=\frac{2M+2}{16}
=\Gamma_{2,M}.
\]

This equals AP.19 because its two summands are `a_{i+1}+a_{M−i}` and `a_{M−i+1}+a_i`. The actual matrices are

\[
N_{2,2}=\frac1{16}
\begin{pmatrix}4&2&0\\1&4&1\\0&2&4\end{pmatrix},
\qquad \Gamma_{2,2}=\frac6{16},
\]
\[
N_{2,3}=\frac1{16}
\begin{pmatrix}5&3&0&0\\1&5&2&0\\0&2&5&1\\0&0&3&5\end{pmatrix},
\qquad \Gamma_{2,3}=\frac8{16},
\]
\[
N_{2,4}=\frac1{16}
\begin{pmatrix}
6&4&0&0&0\\1&6&3&0&0\\0&2&6&2&0\\0&0&3&6&1\\0&0&0&4&6
\end{pmatrix},
\qquad \Gamma_{2,4}=\frac{10}{16}.
\]

## Exact positive factorization and the complete AP.20 implication

Set `d_i=16^M/(m² i!(M−i)!)`, the original reciprocal norm, and let `e_i` be the standard basis vector of the lower-index space. Define positive rational multiples of the retained mass by

\[
w_i=\frac{16^{M-1}}{m^2 i!(M-i-1)!},\qquad 0\le i<M.
\]

The exact factorization is

\[
\boxed{
H=\sum_{i=0}^{M-1}w_i(e_i-e_{i+1})(e_i-e_{i+1})^*.
}
\]

To prove it entry by entry, `H=diag(d_i)(ΓI−N)`. Its superdiagonal is `−d_i(M−i)/16=−w_i`, and its subdiagonal is `−d_{i+1}(i+1)/16=−w_i`. Its diagonal is `Md_i/16`. Taking `w_{−1}=w_M=0`, the factorial definitions give `w_{i−1}=id_i/16` and `w_i=(M−i)d_i/16` whenever the corresponding edge exists; at the endpoints the omitted term is zero. The factorization's diagonal is therefore `w_{i−1}+w_i=Md_i/16`, proving every entry. For each `x∈C^{M+1}` this yields

\[
x^*Hx=\sum_{i=0}^{M-1}w_i|x_i-x_{i+1}|^2\ge0.
\]

The exact edge weights for the requested matrices are

\[
\begin{array}{c|c}
M&(w_0,\ldots,w_{M-1})\\\hline
2&(16/m^2)(1,1)\\
3&(128/m^2)(1,2,1)\\
4&(2048/(3m^2))(1,3,3,1)
\end{array}
\]

The kernel is exactly the constant-coordinate line, since every `w_i>0` and all successive differences vanish precisely there. Thus this incidence bound is attained on its declared lower-index space.

For any original jet matrix `Z`, multiplication gives the exact identity

\[
\Gamma Z\Omega_M^{-1}Z^*-E_+\Omega^{-1}E_+^*=ZHZ^*\succeq0.
\]

This implication preserves every original jet and polynomial coordinate: for any target vector `y`, its quadratic form is `(Z^*y)^*H(Z^*y)≥0`. For `k=1` this difference is zero. For `k=2` it is explicitly the sum of the positive rank-one matrices `w_i(Z e_i−Z e_{i+1})(Z e_i−Z e_{i+1})^*`.

Finally AP.3 gives, without omitting lower degrees,

\[
\mathcal C_M-Z\Omega_M^{-1}Z^*
=\sum_{|\alpha|<M}\frac{z_\alpha z_\alpha^*}{\kappa_\alpha}\succeq0.
\]

Consequently `E_+Ω^{-1}E_+^*≼ΓZΩ_M^{-1}Z^*≼ΓC_M`. With the stated invertible original minimum metric `G_M=C_M^{-1}` and the declared map `V=G_M^{1/2}E_+Ω^{-1/2}`, congruence gives `VV^*≼ΓG_M^{1/2}C_M G_M^{1/2}=ΓI`. This proves the entire AP.20 chain for all six stated calibrations.

## Audit status

The source AP.19–AP.20 was read in full and the incidence matrices were independently derived from the factorial norms and original recurrence. A separate Python `fractions.Fraction` calculation built every incidence directly from the multi-indices, multiplied the original diagonal norm matrices, and asserted equality with every displayed entry formula, every exact row sum, and the full factorization `H=∑w_i(e_i−e_{i+1})(e_i−e_{i+1})^*`. All six cases passed at both `m=1` and `m=7/3` (12 exact checks); the proof above retains arbitrary positive `m`. No floating-point arithmetic was used.

No error was found in those two equations. This report edits neither the TeX source nor the main checker. No Lean process was started, and no assertion concerning actual-zeta certification is made.
