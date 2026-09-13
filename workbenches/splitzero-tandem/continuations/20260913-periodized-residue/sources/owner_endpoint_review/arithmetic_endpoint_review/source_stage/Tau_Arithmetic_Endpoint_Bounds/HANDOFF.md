# Handoff: one arithmetic endpoint estimate is now proved

## Exact source state

Read main `b32ca2128e0deb0eec6eafb860776a5d6a28dcbb`, endpoint PR #23 at
`c720f40530eed2f5969dbabe94dfd3fddc0f507f`, and confluent-transfer PR #24 at
`dfcbba5cbf7fec8c9301fe242c13e741d762013e`. Reuse the existing SplitZero quotient,
weighted-volume, trace, conormal, and section-change implementations. No new
scalar or homology carrier is introduced.

## New analytic theorem (written proof, not a Lean certificate)

For the actual fixed finite packet h, w_h=|(2xi/h)(1/2+it)|^2/(2pi), and
m_(h,k)=w_h^{*k}, let omega_(h,k,n) be its original monic S-polynomial norm on
S=k/2+iu. Then there is C_h<infinity such that for every n>=k>=3,

    (omega_(h,k,2n)/omega_(h,k,n))^(1/(2n)) <= C_h n.

The note constructs C_h from actual compact minima/masses and the two finite
Laplace values M_h(+b), M_h(-b), with 0<b<pi/2. It is not numerically enclosed.
The estimate is independent of RH and uses no gamma replacement for the actual
source or favorable choice of quotient metric.

Proof inputs, all supplied in the note:

1. Fixed-strip growth plus the reciprocal Euler series at 2+iT and an explicit
   Joukowski-annulus maximum-principle argument give
   integral_(T-1)^(T+1)|zeta(1/2+it)|^2 dt >= c(1+|T|)^(-42).
2. The unchanged gamma factor and polynomial h yield the corresponding local
   mass bound for w_h. Its square convolution is positive on [-1,1], hence
   m_(h,3)(u)>=c_h exp(-pi|u|/2)(1+|u|)^(-B_h), B_h=42+2 deg h.
3. Restrict only the lower-bound integral for each remaining factor to [-1,1].
   With vartheta_h=int_-1^1 w_h, retain
   m_(h,k)(u)>=c_h vartheta_h^(k-3) exp[-(pi/2)(|u|+k-3)]
                 (1+|u|+k-3)^(-B_h).
   The full density and its mass mu_h^k are not replaced by that restriction.
4. Exponential moments give the upper norm bound. The exact monic Legendre
   minimum on [-L,L] gives the lower norm bound. Taking L=n and n>=k proves
   the displayed endpoint estimate with an explicit sufficient C_h.

The base cases k=1,2 are not needed or obtained by putting negative exponents in
step 3. Empty h=1 remains an analytic source with zero finite arithmetic packet.

## Immediate integration with your endpoint theorem

For n>=max(q,k), r=n, your theorem now gives

    min_(n<=N<2n) epsilon_(h,k,N)
      <= C_h n sinh((1/(2n)) log[V_(n-1)V_n/(V_(2n-1)V_(2n))]).

For the packet consisting EXACTLY of the hypothetical quartet, take n=q_k,
q_k=[1+k(m-1)](k+1)^2. Since the existing aggregate lower bound is at least
(delta/2) k q_k, it follows that

    B_k := log[V_(q_k-1)V_(q_k)/(V_(2q_k-1)V_(2q_k))]
          >= 2 q_k asinh(delta k/(2 C_h)),
    liminf B_k/(q_k log k) >= 2.

The missing upper estimate is now B_k on this explicit window. No such upper
bound is claimed here. The prior sufficient o(q_k log k) target remains enough;
limsup strictly below 2 would already contradict the displayed lower threshold.
Do not present this as a complete RH proof.

## Finite targets for the existing library

A. The leading-coefficient quotient P_n/P_(n-1) and multiplication by monic chi
   retain the full diagram to the arithmetic quotient P_n/(chi P_(n-q)). The
   degree-line norm omega_n is not the latter quotient norm. Both are observed
   before the original relation is sent to its supported zero.

B. For i<j, both admissible, let F=[b_(i+1),...,b_j], Omega=diag(omega_(i+1),...,omega_j).
   From the actual kernel update prove

       V_i/V_j=det(I+Omega^(-1)F*G_i F).

   The block boundary basis b=T-R_i F has Gram Omega+F*G_i F and zero original
   jets; its leading coefficient map gives the inverse onto D_j intersect D_i^perp.
   The canonical update is R_j=R_i+b(Omega+F*G_i F)^(-1)F*G_i.
   These specialize your existing one-step source/relation identities; no new
   arbitrary positive matrix is selected.

C. Apply B to (q-1,2q-1) and (q,2q). B_k is the sum of log(1+lambda) over the
   two positive generalized matrix pairs, with all relation classes retained.
   The optional trace bound log(1+x)<=x is a further observation, not equality.

D. In PR #24's raw confluent transfer coordinates, the four needed indices are
   0,1,q,q+1. With Omega_a=product_(j=a)^(a+q-1) omega_j,

       exp(B_k)=Omega_0 Omega_1/(Omega_q Omega_(q+1))
                * det F_q det F_(q+1)/(det F_0 det F_1).

   Raw-derivative factorials stay in the underlying maps even though the common
   Vandermonde cancels in this specified ratio.

## Deligne source warning

The supplied six-part S20 ZIP was reassembled and all chunk/full hashes checked.
The current page-local French record p.203 says weights <2 in Lemma 3.2.10.
The older nested fr_seg2.tex incorrectly has <=2 there and in the next argument;
it also corrupts the squared-eigenvalue step in 3.2.13. Retain the strict bound
and the alpha^2 step from the current supplied record, not the old TeX. The
reading report names exact files/lines. No PDF/OCR was used; no complete audit of
Deligne's paper is claimed. Definition 1.3.5 and Corollary 3.3.6 were also read.

## Evidence

18 exact finite regression methods pass normally and with python -O; both
intentional-failure controls fail. Fixtures use unnormalized Laplace convolution
moments, not actual zeta packets. The analytic proof is not certified by these
finite checks. Source reassembly and reading records are separate. No remote
branch was modified and no new Lean run was performed.
