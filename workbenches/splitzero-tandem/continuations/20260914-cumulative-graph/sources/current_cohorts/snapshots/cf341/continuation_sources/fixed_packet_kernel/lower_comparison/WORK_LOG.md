# Fixed original quotient: denominator-weight comparison

The parent task owns the full user-input transcript at
`work/rh_counterfactual_20260913/shared_thread_audit/THIS_SESSION_USER_INPUTS_VERBATIM.md`
and the cumulative log at `work/rh_counterfactual_20260913/WORK_LOG.md`.
The existing records were confirmed locally. This bounded lane records only its
assigned calculation and decisions; it does not replace those records.

Parent assignment, verbatim:

> Bounded independent math subtask: fixed actual χ(S), original line S=c+iu (c=k/2 fixed), full quotient Gram determinant V_N(w) for polynomials degree≤N modulo monic χ in original remainder frame. We seek log V_N for lower weight σ(u)/(1+u²)^M with σ=|Γ(1/4+iu/2)|²/(2π), fixed integerM. Parent deriving exact full confluent kernel σ asympt: log V_N^σ=−Σλ mλ|Reλ−c| logN −Σcritical mλ² loglogN+O(1). Need prove lower weight has SAME leading logN coefficient (loglog specifics optional) using exact polynomial multiplication/Schur/finite jet extension, no new auxiliary arithmetic χ. Division by (1+u²)^M corresponds |d(S)|² with d(S)=(S−(c+1))^M up to phase on line; a fixed weight denominator comparison. May use fixed divisor of weight with fully stated comparison purpose, not replace actual χ. Write precise proof in own fixed_packet_kernel/lower_comparison subdir. Check if q bound broad errors can sharpen. Root functions sibling tail provides sandwich actual m with these weights. Do not assume unproved asymptotic theorem; exploit algebra. Send decisive formula early.

Decisive calculation sent before drafting: for every fixed r>1, a positive
constant b_(r,M) gives b_(r,M) sigma(r u) <= sigma(u)/(1+u^2)^M <= sigma(u).
The exact polynomial pullback f(S)=p(c+(S-c)/r) transfers the SAME original
jet constraints to evaluation locations c+r(lambda-c), with every derivative
factor r^j retained. The arithmetic polynomial chi, original line, quotient,
and remainder frame remain fixed in the theorem.

Parent authorized this epsilon-dilation comparison and confirmed V_N means
the determinant of the quotient Gram matrix, not its square root. This lane
does not introduce an alternative convention.

The full Gamma envelope and its elementary Binet-remainder proof were read
from `../../arithmetic_tail/tilt_audit/gamma_bound_review.md`, equations G1--G22.
The exact Binet identity was independently checked at NIST DLMF 5.9.E10_2.
No numerical evidence is used in place of a proof.

Independent `comparison_check` lane checks the complete finite-dimensional
coordinate identity, determinant factors, order passage to quotient minima,
and the squeeze limit. It confirms the affine determinant factor r^(-q^2)
when both original and transported remainder frames are displayed.

The comparison proof uses the parent lane's full fixed-Gamma confluent kernel
theorem as a preceding result, not an assumption about the actual arithmetic
weight. The final arithmetic consequence uses the already proved two-sided
weight envelope from the arithmetic-tail lane.

No Lean, Lake, Elan, publication, upload, or unrelated filesystem edits.

Completed `lower_comparison.tex`, equations LC.1--27. The direct jet matrix
identity LC.14 and determinant identity LC.15 are exact. LC.22 proves the
lower-weight limit, LC.26 proves the actual-weight limit using the established
arithmetic-tail envelope. LC.23 and LC.27 preserve the full log-log term with
bounded error when every original root lies on the line. The comparison does
not prove such a bounded error for packets with off-line roots and does not
assert uniformity in growing arithmetic packets or growing k.

Independent review accepted all constants, determinant factors, quotient
order inequalities, and the limiting argument. Its full derivation is at
`../../../fixed_weight_comparison_review/INDEPENDENT_REVIEW.md` relative to
this directory. Parent theorem reference is
`thm:fpk-full-jet-asymptotic` in `fixed_gamma_full_jet_asymptotic.tex`.

Parent completed its own full read, accepted the mathematics, and compiled
the combined FPK-plus-LC wrapper to ten pages. The only reported issue was a
1.4-point overfull LC.4 display. It was corrected by placing the envelope and
its constants on separate display lines. Final TeX SHA256 after that layout
repair is `7DC16DDE0739D2FAC3F9C7780DF1F3ADDFC2DEB08B1CBF3B37697FC072D155FB`.
