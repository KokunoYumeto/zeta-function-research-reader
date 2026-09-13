# Exact join: determinant losses and spectral coupling

This short continuation joins two already written identities on the same
finite arithmetic packet and its original least-norm metric. It does not
replace that metric or claim an asymptotic estimate. It is a direct algebraic
consequence of the supplied Toda note (28) and the frozen companion reader's
exterior equality calculation (E8); no novelty claim or Lean execution.

## Original objects and notation

Fix the existing nonempty packet, its tensor degree k, cyclic algebra
C = C[S]/chi, q = deg chi, A = M_S, and an admitted degree N >= q.
All quantities below are at the original observation theta = 0. Retain
G_N, the least-norm quotient Gram, and the adjoint A^sharp = G_N^-1 A* G_N.
Write H_N = A^sharp + A - k I. Its eigenvalues are +epsilon_N,
-epsilon_N, and zero, with the multiplicities from the rank-two calculation.

Let V_+ be the full generalized right-half-plane spectral subspace of A,
and P_N its G_N-orthogonal projector. Its positive excess is

L = sum_(Re lambda > k/2) ell_lambda (2 Re lambda - k).

Consider the nonempty V_+ case, so L > 0 and epsilon_N > 0 by the proved
exterior trace bound. Let u_+, u_- be G_N-unit eigenvectors of H_N at
+epsilon_N and -epsilon_N. The coordinate injection
E_N : C^2 -> C sends (z_+, z_-) to z_+ u_+ + z_- u_-.
Set M_N = E_N^sharp P_N E_N. Thus 0 <= M_N <= I_2.
These eigen-coordinates describe a compression only; they do not replace
the arithmetic metric.

Use C_N = P_N A (1-P_N) : V_+^perp -> V_+ for the actual off-diagonal
coupling. The symbol C_N is used here to avoid confusing this coupling
with the Toda note's operator T = (A-k I/2)/i. Every Hilbert-Schmidt norm
below uses the original restricted G_N metrics.

For the scalar quantities retain

V_N = det G_N = D_(N+1)/B_(N-q+1),
v_N = log(V_(N-1)/V_N),
s_N = (v_N + v_(N+1))/2,
t_N = (v_(N+1) - v_N)/2,
a_(N+1) = omega_(N+1)/omega_N,
phi_N = sigma - partial_theta log V_N |_(theta=0),
sigma = Tr((A-k I/2)/i).

Here D and B are exactly the source and relation Hankel determinant
sequences in the supplied note, not alternative free sequences.

## Complete loss identity

The Toda identity gives

a_(N+1) sinh(s_N)^2 - epsilon_N^2
  = a_(N+1) (exp(t_N)-cosh(s_N))^2 + phi_N^2.

The companion's E8 gives, on the same original metric,

epsilon_N^2 - L^2
  = ||C_N||_(HS,G_N)^2
    + epsilon_N^2 (det M_N + det(I_2-M_N)).

Adding these equalities cancels precisely epsilon_N^2 and proves

**a_(N+1) sinh(s_N)^2 - L^2
  = a_(N+1) (exp(t_N)-cosh(s_N))^2
    + phi_N^2
    + ||C_N||_(HS,G_N)^2
    + epsilon_N^2 (det M_N + det(I_2-M_N)).**

All four terms on the right are nonnegative. The first two are the
successive-volume imbalance and the retained phase. The last two are
the original spectral-subspace coupling and the compression remainder.
There is no cancellation between them.

The exact Sylvester morphism is also retained. In the G_N-orthogonal
decomposition C = V_+ plus V_+^perp, write
A = [[B_N, C_N], [0, D_N^op]], and the CRT spectral idempotent as
Q = [[I, X_N], [0, 0]]. The identity AQ = QA is exactly

B_N X_N - X_N D_N^op = C_N.

Its inverse is integral_(0,infinity) exp(-t B_N) Y exp(t D_N^op) dt;
the strict real spectral separation and the complete finite nilpotent
polynomial factors give convergence. Consequently the coupling term
controls ||Q-P_N|| by the actual smallest singular value of this
Sylvester map, as in E14-E18. No uniform bound for that singular value
is inserted here.

## What this adds to the two-step inequality

Let R_N = V_(N-1)/V_(N+1) = exp(2s_N). Dropping only the imbalance
square and the nonnegative compression remainder gives the stronger
finite inequality

a_(N+1) (R_N-1)^2/(4 R_N)
  >= L^2 + phi_N^2 + ||C_N||_(HS,G_N)^2.

Since s_N >= 0, this is equivalently

log R_N >= 2 arsinh(
  sqrt(L^2 + phi_N^2 + ||C_N||_(HS,G_N)^2) / sqrt(a_(N+1))).

For a full quartet at zero tilt, the supplied symmetry proves phi_N = 0;
the coupling term is still present. If that coupling is nonzero, the
original lower bound with L alone is strictly sharpened at that N.
Nothing here supplies uniform strictness or large-k decay. The retained
endpoint N = q-1 uses the source note's separate endpoint formula rather
than these preceding-volume ratios.

The empty selected subspace has L = 0 and should use the Toda identity
directly; no positive-eigenline construction is asserted when epsilon_N = 0.

## Evidence and reading scope

The parent read the complete supplied NOTE.tex, including its sections
1-10, references and explicit first-degree calculation, directly from
Tau_Toda_Volume_Control_2026-09-12.zip (SHA-256
80b365233ba5ebaf1b52aeea369a7771d74bf774dbb4416f10a56503321b8f41).
The companion E8/E14-E18 source is pinned by GitHub commit
161089942cce70a09fbe441d08ba4d36c1fd810c, under
workbenches/splitzero-tandem/continuations/20260912-cyclic/tex/
exterior_trace_equality_continuation.tex.
The displayed join was checked by literal addition of the two equalities.
The independent delivery/checker review is separate in toda_review/.

Primary-source context checked in this turn: DLMF 5.11.9 for gamma
vertical-strip decay, and DLMF 18.2(ix), especially 18.2.30 and the following
numerical-conditioning warning. The supplied 1997 Toda paper was verified
at publisher abstract/metadata scope; its full proof was not fetched.
These references identify the classical ingredients, not a prior source
for this arithmetic specialization.
