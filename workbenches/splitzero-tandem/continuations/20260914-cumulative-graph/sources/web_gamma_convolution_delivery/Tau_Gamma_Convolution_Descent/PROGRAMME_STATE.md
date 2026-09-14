# Programme state after gamma convolution descent

## Preserved

The original split scalar G, e/tau distinction, infinite arithmetic quotient,
absolute pointed base, theta complex, full packet orders, cyclic injection with
its Taylor unit, canonical source constraints, exterior trace bound, and Toda
source/relation determinant ratio remain unchanged.

## Newly calculated

- The exact gamma reference is closed under the literal spectral sum at every k,
  with mass c_lambda^k and convolution factor c_lambda^k/c_(k lambda).
- The sum projection of every product gamma polynomial and its entire normal
  component have explicit maps and squared norms.
- The actual arithmetic sum-density multiplier has coefficients
  `[z^n](sum (2lambda)_j c_j z^j)^k/(2k lambda)_n`.
- A degree-N arithmetic source and relation Gram need only the first 2N
  one-factor coefficients, with exact finite-moment equality.
- A full quartet has a bounded multiplier relative to the original lambda=1/4
  reference. This gives a proved source/quotient upper comparison and explicit
  tail bounds for all polynomial moments.
- The actual recurrence and quotient-volume change factor into a fully explicit
  gamma term and specified arithmetic source/boundary determinant corrections.

## Exact remaining estimate

At theta=0, retain X_n=D_n/Dgamma_n, Y_n=B_n/Bgamma_n,
T_N=X_(N+1)/Y_(N-q+1), and Q_N=X_(N+2)X_N/X_(N+1)^2.
The actual upper bound uses

  sqrt((N+1)(N+2k lambda) Q_N)
  * (Rgamma_N T_(N-1)/T_(N+1)-1)
  / (2 sqrt(Rgamma_N T_(N-1)/T_(N+1))).

The known one-sided bound T_N<=C_h^(kq) does not control its consecutive ratio.
The phase and volume-imbalance squares in the inherited exact identity remain
available. No subcubic or other uniform small-control estimate is inferred here.

## Collaboration

Read directly from GitHub main fa4be32... and PR22 811210d.... The latter's
inspected status was still in progress. Do not change that session's source or
claim its unfinished workflow as a success. This delivery includes an add-only
patch, but no remote write was made by this session.
