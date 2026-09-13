# SGA trace and exact period determinant: formalization handoff

This is an add-only analytic continuation of the exponential and logarithmic-constituent workbenches. Keep their existing quotient implementation, original theta source, coefficient pin, and dependency pins. No remote files were changed here.

## Mathematical output

The supplied SGA 5 III (6.8.5) is applied to the exact finite free algebra E_t=R[t,S]/(chi(S)-t). Its residue functional is the top coefficient of the monic remainder. The polynomial divided difference C_H(X,Y)=(H(X)-H(Y))/(X-Y) is its coevaluation tensor. Multiplication sends C_H to chi'. The resulting trace is lambda_t(chi'P), including repeated-root multiplicities. The trace-form radical is ann(chi'), with the perfect residue pairing retained.

The full diagonal admits the alternating multiplication resolution with X-Y and C_H. Tensoring by the diagonal gives alternating maps 0 and chi', and hence the positive Hochschild groups recorded in NOTE §§4–5. The source action is multiplication by X throughout. These homology degrees are not an asserted identification with the separately indexed nullity ladder.

For the previous exponential family D=u d/dS+(chi-t), the quantum coefficient matrices C_a differ from the classical A(t)^(a+1) by a strictly upper-triangular matrix. Their traces are identical. Define F=Tr(M_(Phi-tS)) on E_t. Its coefficient gradients yield

    det Pi = det Pi_mon exp(F/u),
    det(Pi* Pi) = (2 pi |u|)^q exp(2 Re(F/u)).

All phases are retained in the original ray matrix, not reconstructed from the squared formula. The rank-one upward contour is the negative of Gamma_1 in the common ray ordering; the orientation map is explicit in §9.

The first q coefficient derivatives of the determinant recover Tr(A^r) and the exact original chi-t through Newton recursion. This recovery uses cyclicity; it does not claim trace classification for a general noncyclic module.

## Bounded finite targets

1. Monic remainder top-coefficient pairing, its antidiagonal determinant, and coefficient base change.
2. Casimir/diagonal identities, coevaluation inverse, and lambda(chi'P)=Tr(M_P).
3. Trace-pairing radical via the composite beta-flat o M_chi'.
4. Alternating annihilator identities over B=T/((X-Y)C_H), with monic non-zero-divisor proofs over the actual coefficient ring.
5. Strict triangularity of quantum reduction minus classical reduction in the increasing-power basis; trace equality for powers 1 through q.
6. Polynomial identities for gradients of Tr(Phi_t(A(t))). A direct universal-polynomial proof can replace the analytic simple-root density argument in the written note, without changing the statement.
7. Newton recursion recovering the companion characteristic polynomial with all integer factors.
8. Original metric transport Gtilde=Pi^{-*}G Pi^{-1}, endpoint determinant cancellation, and the differentiated control congruence.
9. Invariant-subspace period minor: P_F'=−P_F A_F/u at t=0; its logarithmic Gram derivative yields the original aggregate trace defect. The first normal derivative is zero and the second is the explicit rank-one R correction.

The existing scalar reconstruction lifts these coefficient maps at their stated support labels. A vanished relation lands at its receiving fibre's zero; tau is only the external absence case. Do not define another scalar adjunction for each diagonal homology degree.

## Analytic proof scope

The arbitrary-degree period determinant proof uses convergent ray integrals, differentiation on compact coefficient sets, a scalar determinant ODE, and the exact monomial initial matrix. Those are written analytic proofs, not new Lean certificates. The complex-to-finite-field comparison remains a span from a specified finitely generated coefficient ring; there is no field map C to F_Q and no Frobenius-to-A intertwiner supplied by these determinant formulas.

## Quantitative target retained

For the full period determinant, the t-direction sees total Tr A, whose real part is already kq/2 in a reflection-stable packet. The relevant nontrivial target is the determinant norm of the rectangular period map Pi I_F for an actual invariant constituent, with its original theta-source Gram in the denominator. Section 10.1 computes its derivative and normal acceleration. Section 11 carries forward the exact original subquotient-coupling upper certificate. No uniform upper estimate contradicting the quartet threshold four is established.

## Replays supplied

Eighteen new finite exact test methods pass in both normal and optimized Python; all three false controls are rejected in both. The predecessor manifests (51 and 38 entries) and suites (22 and 16 methods) were independently replayed. Separate small-degree ray quadratures are numerical, not interval certificates. See CHECKS.md and machine-readable logs. No source corpus, font files, or private transcript is redistributed.
