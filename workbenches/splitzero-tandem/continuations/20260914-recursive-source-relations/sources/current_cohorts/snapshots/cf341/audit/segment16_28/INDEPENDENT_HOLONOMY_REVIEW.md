# Independent review of the actual holonomy counterfactual

Reviewed module: `../segment55_67/actual_holonomy_counterfactual.tex`, current SHA-256 `74f8b45052c6f10d3d0ecd8a861336e2b66b19fd94ed26921889c22bf932c449`.

Declared source inspected directly: `output/split_zero_rh_tandem_2026-09-12/sources/web_holonomy_descent_delivery/Tau_Holonomy_Descent_Control/NOTE.tex`, SHA-256 `444f82a8fa420e6f471ef448442085f3a93acb137069e1505d155faab051b881`. The reads cover H2–H21, H24–H34, H51–H57 and the explicit original cochain degrees at H30–H31. I also read the module in full and its accompanying AUDIT.md. No original file was edited in this review.

**Verdict: the current corrected module passes this bounded mathematical review.** The bounds concern the actual arithmetic counterfactual and do not replace its source measure or divisor condition by a reference fixture. This is not an independent replay of the inherited analytic existence theorem for F_h, which the module correctly imports from its declared source.

## Required repairs found and now present in the current file

The first version read used an unsigned tensor primitive, put the other F_h factors in degree zero, and called the primitive degree minus one. That silently changed the source grading. H30–H31 retain the theta complex in degrees 0,1 and the original tensor arithmetic in degree k. The correct primitive is

\[
\sum_{i=1}^k(-1)^{i-1}Q_i(D_1,\ldots,D_k)
  (F_h^{\otimes(i-1)}\otimes\phi_h\otimes F_h^{\otimes(k-i)}),
\]

in degree k−1. The tensor differential supplies the second factor (−1)^{i−1}; its differential is the required positive polynomial sum. I reported this to the parent. A subsequent read confirms that this exact repair is now in the original module. The two `^{,2}` Hilbert–Schmidt superscripts in HT14 have also been corrected to `^{2}`.

## Constants, maps and domains checked

- **Actual divisor:** HT1 starts from an actual zero of the original g=2ξ, retains all four symmetry partners with full order m, and defines v_h=g/h. Full selected orders imply that the division is entire and j_h(v_h) is invertible. The norm is exactly the original w_h=|v_h(1/2+iu)|²/(2π), followed by k-fold convolution. No Gamma replacement occurs.
- **Amplification:** the nilpotent sum has exact index ℓ_k=1+k(m−1), by the nonzero multinomial coefficient displayed in the proof. Every independent real/imaginary sign count occurs; the distinct grid points therefore give χ with degree q=ℓ_k(k+1)². The unit prefactor in η is retained, and η is correctly called a complex-linear module injection rather than a unital algebra map.
- **Holonomy:** HT4–HT7 reproduce H9–H17 and H24 with the full relative Hilbert space, half-density exp((kr+Σz_i)/2), multiplier e^(−iθ), lattice (2πn+θ)/L, sampling factor 2π/L, and phase integration dθ/(2π). The zero mode is included. Positivity of every sampled mass is justified for k≥2, and N≥q−1 is the correct first admitted degree.
- **Rank-two identity:** the recurrence on the vertical line is Sp_j=p_{j+1}+(c+ia_j)p_j−(ω_j/ω_{j−1})p_{j−1}. The imaginary diagonal and adjacent terms cancel exactly, giving HT11 even at N=q−1. Congruence by G^{1/2} produces precisely the H of HT8. Complete-grid trace gives Tr H=0.
- **Lower constant:** the invariant positive-real-part primary subspace yields 2δℓ_k(k+1)floor((k+1)²/4). The positive integer sums are r² for k=2r−1 and r(r+1) for k=2r. The trace of an orthogonal compression of the rank-two trace-zero Hermitian matrix is at most its positive eigenvalue. Thus HT9, including L_(h,k)/q≥δk/2, has the correct constants.
- **Energy:** the twisted H¹ domain has unit-modulus boundary multiplier, so D*+D=kI. The orthogonal decomposition T=UZ+T_perp gives Tr(G^(−1)B*B)=ε²/2+||(Z−Z*)/2||²+||T_perp||². The constants L²/2 and δ²k²q²/8 follow without omitted terms. HT15 averages the proved phasewise energies; it does not interchange an inverse with an average.
- **Laplacian:** the H² domain explicitly imposes the same multiplier on the derivative. D²−kD=∂r²−c² has eigenvalues −u_n²−c². For λ=c+x+iy, the squared distance is exactly (u_n²+x²−y²)²+4x²y². The extreme actual grid eigenvalue has x=kδ,y=kγ, giving 2k²δγ. When y=0 the positive bound x²+min_n u_n² is retained.

The concluding scope is accurate: these are lower bounds on explicitly retained actual source boundaries. The small section-gluing norm concerns a different source quantity before the derivative, and the module does not silently promote it to an upper bound on these derivative energies. The reduced generic examples discussed at the end are correctly denied the status of counterexamples satisfying h|2ξ.
