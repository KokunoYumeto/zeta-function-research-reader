# Independent proof check: RW1–20

Read the entire corrected RATIONAL_NATIVE_RECEIVER_BODY.tex.
Reviewed SHA-256: 57C0251522728ECD2437DAD8DB94336D8807A4DBC2EB9863627BFB8C59F17758.
Also read the receiving definitions and domains in FC21–24, SE5–17 and TC1–11.
Result: the corrected RW1–20 identities are accepted by the calculations below.
This receipt makes no claim that the full Weil matrix has been numerically evaluated or has a specified sign.

## Required correction, now applied

The first version of RW14 combined the source label Gram G_X with the target evaluation Gram G. That is a legitimate metric on a newly specified mixed product, but is neither SE13's original source direct sum nor its original target direct sum.

The reviewed version uses the actual target metric diag(G_Y,G) in RW14 and RW16, and separately retains the source metric diag(G_X,G_U) in RW19–20. Both changes were read and verified. No metric-identification defect remains.

## Exact coefficient receiver

With b=bar(ω)−1 and h=ω+b>0, set u=(z+b)/(ω−z). Then z=(ωu−b)/(1+u) and ω−z=h/(1+u). Substitution proves that the coefficient column of

\[
h^{-n-1/2}(1+u)^n p((\omega u-b)/(1+u))
\]

is exactly the inverse RW3, including its exponent and signs. Changing to t=ω−z and reversing the columns gives two signs (-1)^{n(n+1)/2}; they cancel. The remaining determinant is exactly h^{(n+1)^2/2}. This proves RW2–4 for every integer n≥0. The accompanying symbolic certificate checks every coefficient, both compositions and the determinant independently for n=0,...,5.

RW5 is literal translation in the original polynomial variable. Composition gives Cκ C−κ=I. RW6 follows from the actual equality T_A Φ=Ψ. The source inverse in RW18 acts on the actual quotient P_(v+3)/P_(v−1), as FC21–24 require. For other degrees the corresponding actual quotient is used, not an obsolete cutoff.

## Target native Gram

Evaluating C−κ N_j at the original S'=c_*+iy evaluates N_j at 1/2+iy. Its two linear factors are exactly d+i(y−τ) and d−i(y−τ). Thus

\[
\overline{N_i(1/2+iy)}N_j(1/2+iy)
=h(d+i(y-\tau))^{3+j-i}(d-i(y-\tau))^{3+i-j}.
\]

This proves every entry and index orientation g_(j−i) in RW8. The original measure is unchanged. Expansion yields RW10, including all odd shifted moments. The certificate recomputes all sixteen entries from RW9's unshifted moments and compares them to this expression.

The monic orthogonal norm product is

\[
\det\mathcal H
=12M_s^4\beta^3(\beta+1)^2(\beta+2),\qquad\beta=s/2>0.
\]

Together with det R=h^8 and det C−κ=1 this proves RW11. Independence of the determinant from τ does not imply a condition-number bound; RW does not claim one.

## Full Weil receiver

Exact reflected conjugation gives

\[
\overline{\varphi_i^\omega(1-\bar\rho)}\varphi_j^\omega(\rho)
=h\,\frac{(\rho+\bar\omega-1)^{j-i-1}}
 {(\omega-\rho)^{j-i+1}}.
\]

The symbolic check verifies all sixteen exponents independently. The possible poles at ω and 1−bar(ω) are outside the open critical strip because Re ω>1. Absolute convergence follows from the displayed theta growth bound and Jensen argument: the count is O(R log(R+2)), so the dyadic sum of |ρ|^-2 converges. Reflection of the actual zero multiset gives Hermitian symmetry. These steps do not assume RH or omit a zero tail.

## Two exact native metric congruences

Let

\[
F=\begin{pmatrix}I&0\\E&O\end{pmatrix},\quad A=[E\ O],\quad
S=\begin{pmatrix}I&0\\-O^{-1}E&O^{-1}B_\omega^{-1}\end{pmatrix}.
\]

Direct multiplication gives

\[
FS=\operatorname{diag}(I,B_\omega^{-1}),\qquad
AS=[0\ B_\omega^{-1}].
\]

These two identities simultaneously prove RW16 and RW20:

\[
S^*\mathbb W S=\operatorname{diag}(0,T_3),\quad
S^*\mathbb H_W S=\operatorname{diag}(G_Y,H_\omega),\quad
S^*\mathbb H_U S=\operatorname{diag}(G_X,H_{U,\omega}).
\]

All inverses exist on the stated original quartet domain: O is invertible by SE7 (SE5 computes its contributing coefficient determinant), Bω by RW4 and FC32, and the original Gamma quotient norms are positive. Source and target Grams retain their distinct meanings. Positive square-root conjugation proves the generalized eigenvalue statements. Solving the kernel equation gives precisely RW17, including any extra ker T3 directions. The visible graph is not claimed to be the whole kernel when T3 is singular.

## Receipts

verify_rational_native_receiver.py and its captured output passed all stated exact algebra checks. The general block proof above uses arbitrary invertible O,Bω and arbitrary original positive Grams; no sampled matrix substitutes for it.

The explicit source entries announced after RW20 belong to NH26 onward and are outside this bounded receipt. The defining source norm and congruence RW19–20 themselves were checked here.
