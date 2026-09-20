# New results — 20 September 2026

## SZ-20260920-053 — The original determinant retains the large and small singular values

The programme's original multiplication matrix is M=C_N+r_N ell_N in its attained arithmetic metric G_N. C_N is selfadjoint; the rank-one boundary term has norm kappa_N. The completed Gaussian result052 described the spectral distribution at scale q. This continuation calculates information that a fixed-time Gaussian trace cannot retain.

**SD5 is an exact determinant formula.** For every original cutoff and a>0, put D_a=C_N²+a²I, A_a=r_N†D_a^-1r_N and B_a=ell_ND_a^-1ell_N†. Then

\[
\det(M^\dagger M+a^2I)=|Q(ia)|^2+a^2|\det(iaI-C_N)|^2A_aB_a.
\]

The first term contains every original root and multiplicity. The second contains both actual boundary resolvent energies. SD13 returns this determinant to the already established complete action J, with its original window weights. After retaining the explicit boundary-energy correction, SD14 bounds the total remaining logarithmic error by O(1/q). The boundary-energy correction itself is only bounded by O(q), and has not been removed from an order-q calculation.

**SD21–22 force small singular values in the original metric.** There is an explicit finite bound using the full Q(0) and the eigenvalue count of C_N. It implies, uniformly over q−1<=N<=2q−1, s_min(M;G_N)/q<=q^-A eventually for every fixed A>0. Meanwhile every algebraic eigenvalue has modulus at least sqrt(delta²+gamma²). The proof uses the exact determinant at zero and the proved Gaussian bulk; it never applies weak convergence to the singular function log(x). No effective numerical threshold in k is claimed.

**SD15–19 evaluate the original root product and logarithmic loss.** The root-product constant is

\[
g=\tfrac12\log(\delta^2+\gamma^2)-\tfrac32+
\tfrac12[(\delta/\gamma)\arctan(\gamma/\delta)+(\gamma/\delta)\arctan(\delta/\gamma)].
\]

The exact product has log|Q(0)|=q log k+qg+O(q log k/k). If D_N is the sum of the negative parts of log(s_j²/q²), SD19 computes D_N using kappa_N, this full root product and the bounded positive-log integral b(s) of the already proved density. The original weighted return is

\[
\sum_Nw_ND_N=4q^2\log(q/k)+q^2[C_B-4g+2\int_0^1b(s)\,ds]+o(q^2).
\]

The integral is specified by the exact proved one-dimensional density; no numerical value for that remaining quadrature is invented.

**SD26–28 integrate the useful new metric handoff.** The all-time 1/e heat bound was already proved in published EM29 and is credited there. The additional logarithmic-determinant bound has constant1 against the scalar-invariant trace norm of the log metric ratio. The handoff's sharp whole-bracket radius is the sum of the largest floor(q/2) logarithmic generalized eigenvalues. This radius applies directly to the original regularized determinant; it avoids the false inference that the two endpoint heat values enclose every interior metric.

All complete proofs and their original programme providers are included, with human citations at use. The root checker passed 405 checks and six deliberate-failure controls. The illustrated reader includes the complete NG and GM proofs from 052. These results do not assign the seven original absolute allocations or the individual projected-current signs. The exact conductor/current complement is a separate bounded derivation now awaiting root acceptance.
