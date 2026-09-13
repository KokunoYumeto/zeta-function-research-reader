(* Independent evaluation of actual theta Gram data. Not interval arithmetic.
   Evaluate with Get["check_theta_norms.wl"] in a Wolfram Language kernel.
   The returned association is the result; no filesystem or network writes.
   The omitted-integer-tail PROOF is in RESEARCH_NOTE.md, not supplied by
   agreement of high-precision floating-point outputs. *)
Module[{z, p, q, pc, qc, gram, c, moments, left, right, leftJ, rightJ,
  normsq, tail, n = 8, digits = 65, cap = 3000},
 p = NestList[Expand[2 z (# - D[#, z])] &, 4 z^2 - 6 z, 3];
 q = Table[Expand[Sum[(-1)^k Binomial[j, k] p[[k + 1]], {k, 0, j}]], {j, 0, 3}];
 pc = Table[Coefficient[p[[j]], z, r], {j, 1, 4}, {r, 0, 5}];
 qc = Table[Coefficient[q[[j]], z, r], {j, 1, 4}, {r, 0, 5}];
 gram = ConstantArray[0, {4, 4}];
 Do[
  c = N[Pi (a^2 + b^2), digits];
  moments = Table[Gamma[k + 1/2, c]/(2 c^(k + 1/2)), {k, 0, 10}];
  moments = Table[moments[[r + s + 1]], {r, 0, 5}, {s, 0, 5}];
  left = pc . DiagonalMatrix[Table[N[Pi a^2, digits]^r, {r, 0, 5}]];
  right = pc . DiagonalMatrix[Table[N[Pi b^2, digits]^r, {r, 0, 5}]];
  leftJ = qc . DiagonalMatrix[Table[N[Pi a^2, digits]^r, {r, 0, 5}]];
  rightJ = qc . DiagonalMatrix[Table[N[Pi b^2, digits]^r, {r, 0, 5}]];
  gram += 4 (left . moments . Transpose[right] + leftJ . moments . Transpose[rightJ]),
  {a, 1, n}, {b, 1, n}];
 normsq = Table[Det[gram[[1 ;; k, 1 ;; k]]]/
   If[k == 1, 1, Det[gram[[1 ;; k - 1, 1 ;; k - 1]]]], {k, 1, 4}];
 tail = 16 cap^2 Pi^10/(2 Pi ((n+1)^2+1)-20) *
   (n+1)^10 Exp[-Pi (n+1)^2]/(1-((n+2)/(n+1))^10 Exp[-Pi (2n+3)]) *
   Exp[-Pi]/(1-2^10 Exp[-3Pi]);
 <|"norm_squares" -> N[normsq, 30],
   "tail_expression_evaluation" -> N[tail, 30],
   "coefficient_cap_verified" -> And @@ Thread[(Total[Abs[#]] & /@ Join[pc, qc]) <= cap],
   "rational_steps_for_conservative_tail_bound" ->
     {Sum[3^k/k!, {k, 0, 8}] > 20, 2^81 > 10^24,
      16 cap^2 4^10 < 2*10^14, 9^10 < 10^10, 2^10/20^3 < 1/2},
   "interpretation" -> "Numerical values; written omitted-integer-tail proof is separate; no validated rounding or Schur error bound"|>
]
