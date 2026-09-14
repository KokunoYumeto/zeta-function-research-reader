# Exact actual-program amplification match

Complete proofs: purity_amplification_match.tex, PAM.1--27 and PSC.1--64.
All statements below refer to those full proofs and the same original
actual packet, source, measures, full units, and supported maps.

- The amplified nonzero arithmetic class is explicit:
  v_k=e_(k rho)(S-k rho)^(d_k-1), d_k=1+k(m-1), with nonzero
  observation sigma_h^(tensor k) eta_k v_k. Its eigenvalue is k rho.
  The whole nilpotent primary block is retained (PAM.1--5).
- The critical-line phase generator is D_(L,theta)=-partial_r+k/2.
  Its exact connection to the arithmetic quotient is
  D R-R A=B, with the literal original theta primitive and signs
  (PAM.8--11). On the full primary block:
  R=sum_(j=0)^(d_k-1)(D-k rho)^(-j-1)B N_k^j (PAM.15).
- The offending eigenclass has the exact boundary ratio
  ||B v_k||^2/||R v_k||^2=k^2 delta^2 plus the original weighted
  frequency dispersion. Thus no phase or degree choice turns this
  actual generator error into o(k) (PAM.12--20).
- The original gluing comparison can have BOTH its lift difference
  and the difference between its two generator boundaries <=1/(k+1),
  using the explicit period in PSC.42. Nevertheless each full
  generator boundary retains a positive multiple of k q_k in the
  same metric (PSC.43--49). The exact relation maps and all cross
  terms connecting those statements are proved in PSC.16--41.
- At the first admissible degree, gluing is exactly zero. The actual
  generator boundary is (phase image of chi) tensor the original
  residue functional ell (PSC.50--55). Its exact squared operator
  and Hilbert--Schmidt norm is
  epsilon^2+(Im alpha)^2+omega_q/omega_(q-1)>epsilon^2>=L_h,k^2
  (PSC.56--60). The full-jet eigenvector has the explicit moment
  ratio in PSC.61--64.
- The strengthened actual HC12 estimate retains
  J_N^D-k^2 q_k/4, with all terms and signs proved. Its computed
  source-moment upper expression still has positive lower growth
  after division by k q_k (PSC.1--8).
- QT's class-preserving repair changes the generator boundary by
  exactly D H-H A and has Gram 2G-GG_low^(-1)G. VR's closest
  class-preserving unitary fixes the actual minimum lift and its
  boundary pointwise (PAM.24--27). Their variation error cannot be
  substituted for the generator error: on the constant actual-metric
  path it is zero while the original generator boundary persists.

The nonzero amplification and an exactly critical-line Hilbert generator
are both present in the programme. Their computed connecting morphism
includes the explicitly nonzero boundary above. None of the reviewed
proved estimates supplies an o(k) exclusion for that amplified
arithmetic class. No verdict about RH or the impossibility of a new
arithmetic estimate is asserted.

Final proof SHA256:
E8250C3F4F55517A2987A2D3C932CA83ABA035A3D8232B29B18E865CF32092C9.
Sixteen-page draft compile clean; full independent review and source
provenance in PURITY_MATCH_LOG.md and phase_scaling_audit/.
