# Programme state after canonical endpoint restriction

The original theta complex, structural tau-base, infinite G(Z)->Z quotient,
full arithmetic unit and nilpotent jets remain unchanged.

Inherited analytic input: for a fixed actual packet h and n>=k>=3,
(omega_(h,k,2n)/omega_(h,k,n))^(1/(2n))<=C_h n. Its proof is written, not
newly Lean-verified here. The four-volume target remains
B=log(V_(q-1)V_q/(V_(2q-1)V_(2q))).

New calculated objects:

* The adjoint T_(i,j)=K_i G_j of the actual identity transport
  (E,G_i)->(E,G_j), with source restriction L R_i T=P R_j.
* Its reverse composition T_(i,j)T_(j,l)=T_(i,l), original boundary
  L R_i-R_j, and complete arithmetic action commutator.
* B as minus the sum of logarithms of the squared singular values of the two
  source restrictions, with all original classes retained.
* Cauchy--Binet weights of every admitted full-jet q-tuple and their exact
  polynomial Z(z)=det(K_i+z(K_j-K_i)). Admitted zero minors remain supported.
* Convergent finite trace-moment enclosures for B, with explicitly certified
  gaps K_i>=g0 K_j. Original source integral/jet errors need their own enclosures.

The new upper interface is U0+U1. The endpoint theorem now gives
min epsilon <= C_h q sinh((U0+U1)/(2q)). The required uniform arithmetic
estimate has not been proved.

Off-line quartet consequence: at least one of the two actual restrictions must
have a squared singular value <=exp(-asinh(delta k/(2C_h))). This is a concrete
necessary source-representative phenomenon, not a new RH-disproof certificate.

No change of homotopy parameter is used to modify a fixed metric. No arbitrary
positive metric is chosen. The return maps' spectral spaces are not presumed
A-invariant; the exact commutator is retained. No second cost-free exterior step.

No remote repository change and no fresh Lean execution in this continuation.
