# Bounded formalization handoff: full-jet kernel and original layer

## Exact starting interfaces

Source: PR #14, `3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc`, supplied archive verified in SOURCE_REVIEW_RECEIPT.json. Its matrix of full jets includes the retained unit. The existing Lean baseline is PR #15, `21970bbf4760d0bbca512a4a7996a2e38f968947`. Its new five-module receipt is not expanded by this supplement.

No original scalar, quotient, homology, dependency pin, workflow, or other-session branch has been changed. The added local patch contains authored exposition, a checker, and verification records. It does not contain a new Lean theorem or change any existing theorem's status.

## Precise next declarations

1. Inverse-metric congruence. For positive Hermitian G and K=G^{-1}, W=A*G+GA-wG, prove K W K=A K+K A*-wK. Prove both directions of the quadratic-form inequality under the actual bijection u=K lambda. The natural weight-w antidual action wI-A* has defect NEGATIVE this new form.

2. Finite orthogonal-source constructor. Input a source polynomial space P_N, a positive diagonal Gram in a specified monic basis p_alpha, a surjective full-jet map J, and its constrained minimum. Construct K=sum a_alpha a_alpha*/kappa_alpha, not a separate metric.

3. Actual relation-layer basis. For next-degree columns f_beta and their full jets a_beta, define e_beta=f_beta-R a_beta. Prove these vectors lie in the original upper relation space and are orthogonal to the old relation space. Prove independence from their leading polynomial parts and spanning by subtracting those parts. Reuse SplitZeroRelationLayer's existing quotient equivalence.

4. Derived boundary coefficients. Construct the rows F_beta=sum_i a_(beta-e_i)*/kappa_(beta-e_i). From monicity and the raw finite representative expansion, prove B-E F G lies in the old relations. Obtain C=E F G by orthogonal projection. This generalizes the finite source-expansion approach of SplitZeroKrylovStep without taking the desired endpoint formula as a hypothesis.

5. Boundary-to-kernel calculation. With H=E*E=D+U*G U and E*R=-U*G, prove Y=-E H^{-1}U*G and then W=G(U F+F*U*)G. Regroup through the OLD top-degree columns to get rank <=2 card{|alpha|=N}; do not change the larger actual dimension of the next relation layer.

6. Original univariate specialization. For N=n+deg h and k=1, prove e_(N+1) equals the existing monic theta vector u_(n+1). Its norm is kappa_(N+1)^(h)+a_(N+1)*G a_(N+1). The two norm families are different until this explicit formula relates them.

The complete statements and proofs are equations (9)–(28) in RESEARCH_NOTE.md. Concrete theta-range results, integration by parts on the test space, and existence of all-degree arithmetic moments remain analytic instantiations. No everywhere-defined unbounded derivative on L2 is introduced.

## Arithmetic estimate now retained

The same sought bound can be tested as -epsilon K <= V <= epsilon K, with K a positive full-jet sum and V its top-degree endpoint. This avoids a second matrix inversion in the certification path. Errors in both moments and arithmetic jets must be included in the enclosure of K; operator uncertainty is retained separately. No actual zeta quadrature enclosure or sublinear-in-tensor-degree estimate is supplied here.

## Independent checks

Nineteen supplied tests and eighteen new tests were rerun in normal and optimized Python. Their corresponding records agree in each suite. The negative controls fail as intended. New cases include repeated-root jets, a nonzero imaginary recurrence diagonal, explicit old-versus-new quotient classes, all ordered division signs, a nonvacuous 14-versus-16 rank-bound fixture, and the natural antidual sign. These finite fixtures are not zeta counterexamples and are not Lean certificates.
