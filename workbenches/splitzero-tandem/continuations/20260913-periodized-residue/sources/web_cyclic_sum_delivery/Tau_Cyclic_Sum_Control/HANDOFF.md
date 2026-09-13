# Handoff: sum-generated arithmetic control

## Division of work

This is an analytic/algebraic continuation, not a replacement for the parallel Lean or GitHub workflow. No remote repository was changed. The existing SplitZero scalar, reconstruction, quotient, homotopy, and topology interfaces remain inputs with their reported scope. No new formal certificate is claimed.

## Main new mathematical targets

1. **Cyclic annihilator at every relation depth.** For P=C[s_1,...,s_k], I=(h(s_i)), establish I^r intersect C[S]=(chi_r), S=sum s_i, with the exact maximum-over-collided-tuples exponent in NOTE section 7. A local monomial basis is floor-sum(alpha_i/m_i)<r. This supplies the top degree and the nonzero multinomial coefficient proving minimality. Do not replace chi_r by chi_1^r: the latter maps onto the former by an explicit quotient.
2. **Spectrum-complete cyclic injection.** alpha:C[S]/chi_1 -> (P/I)^(S_k) is an injective algebra map. eta=M_U alpha is a separate coefficient-linear injection carrying the full arithmetic unit U=product j_h(g/h). eta intertwines multiplication by S. Every k*rho is represented. At collisions do not identify every repeated pure tensor with the constructed cyclic eigenvector.
3. **Explicit equivariant retraction.** On a sum eigenspace use pi0(v)=sum_j theta(N^(ell-1-j)v) X^j, choose theta as the actual top monomial coefficient, and multiply by the retained inverse of pi0(w). Prove pi*eta=1 and S-equivariance. The complement is ker pi with its full action. Arithmetic Grams retain all cross terms under this splitting.
4. **Source and quotient.** V_k(P)=P(sum D_i)F_h^(tensor k). The full jet is eta([P]_chi). Its exact polynomial kernel is chi P_{N-q}; fixed-order division by h(s_i) supplies original theta primitives with both Koszul signs. Lift the maps using the existing original internal quotient, not a new scalar definition.
5. **Canonical cyclic metric and rank-two defect.** With the exact convolution measure w_h^(*k), retain all monic orthogonal-polynomial norms omega_j. K_N=sum b_j b_j*/omega_j, G_N=K_N^-1, A=M_S. Prove Z=A K+K A*-kK=(b_(N+1)b_N*+b_N b_(N+1)*)/omega_N. Same-metric reflection forces the cross Gram entry to be purely imaginary. The exact excess is sqrt(det Gram_G(b_N,b_(N+1)))/omega_N. No bound on this number uniform in k is claimed.
6. **Comparison with the full source minimum.** Delta=R_cyc-R_full eta is an actual old theta boundary. Therefore G_cyc=eta* G_full eta+Delta*Delta; the control difference is A*Delta*Delta+Delta*Delta A-kDelta*Delta. Do not order the control forms merely from the Gram ordering.
7. **Raw differentiated moments.** For mu_j=int t^j|a|^2 and nu_j=int t^j|a'|^2, with fixed arithmetic phase, theta_j=-j mu_(j-1)/2. Formal series yield M_(j,k)=j![z^j]M(z)^k and B_(j,k)=j![z^j](N(z)M(z)^(k-1)/k+(k-1)z^2 M(z)^k/(4k)). The cross term survives for higher moments. All masses remain. This is not a claim that a scalar Fisher estimate bounds every polynomial direction without these moments.
8. **Derivative tower with units.** C_(r+1)->C_r sends [P] to [P']; B_(r+1)->B_r sends [P] to [(1/k)sum partial_i P]. Prove their square, then carry eta via delta(U P)=U P'+(delta U)P. The second term need not be cyclic. The original relative quotient records it.
9. **Trace comparison.** Full symmetric sum multiplicities a_lambda, cyclic orders ell_lambda, and complement multiplicities a_lambda-ell_lambda all remain. The finite cyclic residue/Jacobian trace uses chi_1; full arithmetic vector pairing through eta retains U^dagger U. No replacement of g=2xi or of the original trace is licensed.

## Non-overlap and checks

The 24-method checker is an exact finite regression suite, not Lean. It checks local powers, collisions, trace complements, the constructed retraction, conormal maps, full units, canonical metrics, rank-two identities, complex reflection, raw convolution and derivative moments, and original split-zero outputs. Gaussian/polynomial fixtures are explicitly not zeta-zero certificates.

The earlier 20-method Sum Connection suite was rerun normally and under python -O. All 48 source-manifest entries verified. Successful JSON records agree between normal and optimized executions; deliberately failed controls fail in both modes. The source note and transcript reading scope is recorded in SOURCE_READING.json.

## Quantitative next object

The pending estimate is on the exact cyclic constant epsilon_(h,k,N), with N>=deg chi_(h,k)-1. The object retains every amplified exponent and has a scalar convolution norm. The Fisher contraction is available on its constant column; the complete polynomial graph moments are now explicit. The growth of N and the inverse interpolation cost remain part of the estimate.
