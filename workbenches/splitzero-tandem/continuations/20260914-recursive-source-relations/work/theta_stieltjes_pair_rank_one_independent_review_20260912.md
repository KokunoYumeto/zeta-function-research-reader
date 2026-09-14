# Independent review of the full half-line boundary, SP.32–SP.35

Review date: 2026-09-12. Scope: the appended rank-one kernel discrepancy and its derivative-cost identity. The entire current `tex/theta_stieltjes_pair.tex` was read, with the new claims checked independently against the original covariance recurrence and the actual derivative map. No TeX was edited by this reviewer.

## Exact reviewed objects

| Object | SHA-256 | Reading scope |
|---|---|---|
| `tex/theta_stieltjes_pair.tex` | `15b2b20e2da43826024585431754047548237cca0ba4b495ffc156ecd62fa21b` | Complete SP.1–SP.35; this report certifies the independent extension review SP.32–SP.35. |
| `tex/quartet_dissipation_continuation.tex` | `7f6e76ef6d6a7126eb52c4e02d0448f7d7d69b50c163f250f2a99ff096f1fea0` | QD.1–QD.12, including the definitions of the original graph layer, derivative map and Hilbert–Schmidt cost. |
| `tex/theta_gamma_reference.tex` | `008fb6b2688a8052800c04834cc810674446a3c3d4ae6ff5f8dc5cf4dbfadacf` | Previously reviewed complete TG.1–TG.28; used here only for the exact norm determinant map in the final paragraph. |

## Original finite spaces and phase conventions

The packet has degree `d=2D`; `x=−(s−1/2)²` and `h(s)=(-1)^D H(x)` retain SP's monic degree-D polynomial H. The original admitted degree is `N≥d−1`. The full invertible arithmetic jet is multiplication by `V mod H`, not its value at a centre. Thus `f_n=U_V P_n(X)c_H` and `e_n=U_V R_n(X)c_H` are columns in the entire length-D quotient, including all local nilpotents.

At `N=2n` the even inverse metric sums through n and the odd inverse metric through n−1. At `N=2n+1` both sum through n. Both metrics are positive at every admitted degree. The source monic polynomials and norms are

\[
q_{2n}=(-1)^nP_n(x),\quad q_{2n+1}=(-1)^n(s-1/2)R_n(x),\qquad
\kappa_{2n}=p_n,\quad\kappa_{2n+1}=u_n.
\]

These signs determine both boundary signs below. Neither the original coordinate nor any polynomial norm is rescaled.

## Covariance telescope and all boundary columns

Let `z_j=U_upsilon[q_j]_h` in the original residue basis and `C_N=Σ_(j=0)^N z_j z_j*/κ_j`. The original vertical-line recurrence is

\[
Az_j=z_{j+1}+b_jz_j-a_jz_{j-1},\qquad
b_j+\overline b_j=1,\quad a_j=\kappa_j/\kappa_{j-1}>0.
\]

Substituting into `A C_N+C_N A*−C_N`, all diagonal terms vanish. The coefficient of the interior pair `z_(j+1)z_j*` is `1/κ_j−a_(j+1)/κ_(j+1)=0`, and its adjoint vanishes identically. The remaining pair has its original positive sign:

\[
A C_N+C_N A^*-C_N
=\frac{z_{N+1}z_N^*+z_Nz_{N+1}^*}{\kappa_N}.
\]

This is the displayed SP proof formula because `a_(N+1)/κ_(N+1)=1/κ_N`. Transform by T and T*, using `TAT^{-1}=I/2+[[0,-X],[I,0]]` and `T C_N T*=diag(K_e,K_o)`. The upper right block is exactly `K_e−X K_o`.

For `N=2n`, the two transformed columns are `((-1)^n f_n,0)` and `(0,(-1)^n e_n)`, so the upper right block is `f_n e_n*/p_n`. For `N=2n+1`, they are `(0,(-1)^n e_n)` and `((-1)^(n+1) f_(n+1),0)`, so that block is `−f_(n+1)e_n*/u_n`. This proves both rows of SP.32 and their precise finite summation cutoffs. It also proves the identities when a boundary column is zero.

## Original weight and its entire spectrum

Multiplying the boundary identity on the left by `G_e=K_e^{-1}` and right by `G_o=K_o^{-1}` gives `G_o−G_e X`. The relative upper right block in SP.24 is therefore

\[
B_N=\begin{cases}
G_e^{1/2}f_ne_n^*G_o^{1/2}/p_n,&N=2n,\\
-G_e^{1/2}f_{n+1}e_n^*G_o^{1/2}/u_n,&N=2n+1.
\end{cases}
\]

For any two vectors a,b, `||ab*||²=(a*a)(b*b)`, including the zero-vector cases. Applying this identity proves SP.33. The full original relative weight is congruent through the proved isometries to `[[0,B_N],[B_N*,0]]`. Its nonzero eigenvalues, when they occur, are exactly `+ε` and `−ε`; all other eigenvalues are zero. This is a finite rank-one boundary identity on the full quotient, not a quotient of the packet by its nilpotent directions.

## Derivative cost and volume loss with no omitted zero cases

At one factor, QD.1 has one new column: `F=z_(N+1)`, `Ω=κ_(N+1)`, `E_+=a_(N+1)z_N`. The actual relation-layer graph has squared norm

\[
H_{\rm lay}=\kappa_{N+1}+z_{N+1}^*G_N^{\rm src}z_{N+1}.
\]

The original derivative map is `b Ω^{-1}E_+*G_N^{src}`. Since `a_(N+1)/κ_(N+1)=1/κ_N`, its relative Hilbert–Schmidt squared norm is

\[
\chi_N=H_{\rm lay}\,
\frac{z_N^*G_N^{\rm src}z_N}{\kappa_N^2}.
\]

This proves the two SP.34 cost formulas directly from the actual map. The next-column size is `λ_N=z_(N+1)*G_N^{src}z_(N+1)/κ_(N+1)`, and the matrix determinant lemma gives `π_N=(1+λ_N)^{-1}`. Hence

\[
(1-\pi_N)\chi_N
=\frac{(z_{N+1}^*G_N^{\rm src}z_{N+1})
        (z_N^*G_N^{\rm src}z_N)}{\kappa_N^2}
=\epsilon_{N-d}^2.
\]

The first equality uses only positive κ and `1+λ`, so no vanishing column has been divided out. If the new column is zero, `λ=0`, `π=1`, and ε is zero while χ can remain nonzero. If the predecessor column is zero, χ and ε are zero while λ can remain positive. Thus SP.35 retains both zero-frontier cases.

## Exact connection to the gamma determinants

TG's actual packet determinants `D_j^h` give the same unaltered norms

\[
p_n=\sqrt2\,(2n)!\,\Gamma(2n+1/2)\frac{D_{2n}^h}{D_{2n-1}^h},\qquad
u_n=\sqrt2\,(2n+1)!\,\Gamma(2n+3/2)\frac{D_{2n+1}^h}{D_{2n}^h},
\]

where `D_{−1}^h=1`. Consequently the Christoffel ratio in SP.19 is exactly

\[
-c_n=\frac{u_n}{p_n}
=(2n+1)(2n+1/2)
\frac{D_{2n+1}^hD_{2n-1}^h}{(D_{2n}^h)^2}.
\]

These are substitution identities between the two proved representations of the original measure; they impose no asymptotic assumption on the arithmetic determinants.

**Review outcome:** no mathematical correction found in SP.32–SP.35 at the exact reviewed source hash. No main or frozen paper file was modified. This report supplies an independent derivation, not an empirical claim based on a finite calibration.
