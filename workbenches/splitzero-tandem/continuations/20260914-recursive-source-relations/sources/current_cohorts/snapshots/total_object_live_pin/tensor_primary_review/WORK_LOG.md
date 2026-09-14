# Ordered tensor primary boundary audit

Assignment, verbatim:

> New independent review/derivation task: ordered k-fold tensor complex boundary on same u of stable SP. N=m+1,c=−(−rho)^N/N. Original basis product s_i^b. Pi_k=e^{kc/u} W^⊗k (D(u))^⊗k P^⊗k. Character indices l_i=1..N−1, sum L, cycle M diag zeta^L. Invariant projector P0 and dimension d0=((N−1)^k+(N−1)(−1)^k)/N. Original arithmetic A_k=k rho I+Σ N_ar,i; period image k rho I+u^{1/N} Ktot, M Ktot M^-1=zeta Ktot (orientation as SP). Compute exact projector commutator, compressedA vs invariantness, exp(log a Ntot) compression includes only powers divisibleN but nilpotencycutoffk(m−1). Need prove possible power terms not vacuous, including degree/path/truncation exact matrix. Parent root task asks these, I independently derive local main. Own total_object/tensor_primary_review/ no edits main. Please full proof/review tags TPR, check k=1, m=1, N=2 and k2 etc. Message immediately any overlooked distinction of projector in period vs marked basis and fullunit coefficients.

Source: independently reviewed stable SP.1–36, complex-core SHA256 B68000AC12F65176F112C42AF282656CEE9640BD472F0705D43613BC053E5F52, with ordered monomial bases and contours retained.

Delegated independent audits: power_audit.md for exact return paths and edge cases; unit_audit.md for full original Taylor coefficients, projector commutator, and inverse compression.

Sent parent immediately: period versus marked projectors differ by the exact constant Pascal conjugation; source-weighted jet coordinates require the additional conjugation U_k Q_s U_k^-1. No assumption that the complete unit preserves the graded invariant plane is permitted.

Computed exact degree criterion: the return power qN is nonzero precisely when d_min+qN≤k(m−1), with d_min the least residue of −k modulo N. The largest possible return is k−2 ceil(k/N) when the invariant plane is nonzero. Invariantness under the arithmetic nilpotent fails exactly for m≥2 and k≥2, even in the cases with no return power.

Completed independent TPR.1–35, six-page clean draftmode compile. Both independent reviewers passed their full specified ranges. Stable hashes in REVIEW_RECEIPT.md.

Continuation assignment, verbatim:

> Core main now exists total_object/tensor_primary_boundary_control.tex TP.1–29. Please read and review independently; it includes Koszul free remainder, full original contour/product constants, projectors, exact powers/dilation and full source unit projector. I am adding TP.30+ terminal MAI class (N|k subsequence with c_h0,k retained) and a direct exact leakage rank proof via J†=F, F y^b=b(m−b)y^(b−1), H=2b−(m−1), weights w_b=b!(m−1)!/(m−1−b)!. Tensor identity ||Jx||²−||Fx||²=(K−2d)||x||² gives injectivity below middle and adjoint surjectivity above; ranks min(h_d,h_d+1). This auxiliary form proves algebraic rank only, does not replace original G. Please flag issues promptly.

Read entire main TP.1–29. No mathematical error found. Reported two stray commas in superscripts, and one reminder to keep the nonzero-space convention explicit in the later unit subsection. Independently verified the proposed rank argument's signs, basis weights, and middle-degree surjectivity. Awaiting the actual appended text for final bounded review.

Read MAI1–MAI8 in mixed_amplification_identity.tex to verify the pending terminal attachment. Sent parent the exact additional source scalar: MAI6a gives q=c_(h0,k)v_top in normalized theta-jet coordinates, so the sole-primary source period map Pi_k U_k^-1 uses x=c_(h0,k)a0^(-k)v_top. This does not change the character condition N|k, but the scalar must be present when claiming to observe the actual MAI cohomology class. Merely applying Pi_k to the unweighted marked vector is a different specified map.

Read appended TP.30–40 fully at main snapshot 913DFD191FF7EB1A826EECAF0F3C668B8C8A7FA7B0527B72CCD8585F873F00B9. Source scalar correctly incorporated; terminal periods, invariant subsequence, discrepancy, exact rank argument, and alternating k2 kernel passed. Requested explicit preservation of the original MAI counterfactual/quartet hypotheses and an unambiguous written adjoint identity. Corrected the power review receipt's scope/hash chronology without changing mathematical content.

Read all final precision edits: original MAI branch hypotheses/quartet now explicit, adjoint image-kernel equality written exactly, V0≠0 repeated in unit subsection, and both superscript commas removed. Latest reviewed main TP.1–40 SHA256 89BD831A817FD4882BB627DBF819B5F644EC19F69890AE1E62561C6A3B206868. All reported issues resolved; detailed receipt updated.
