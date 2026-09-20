# Independent review of the complete ES coefficient extension

The complete root source `ES_COEFFICIENT_TOTAL_EXTENSION_BODY.tex`, equations ET1–39 including ET28a, was read and compared with the independent proof ETR1–31. Its final SHA-256 is `deafefa5e21f54bae521bd21c63523ee3b64ad245735849c28246b673be730ac`. The initial ET1–36 reading had SHA-256 `e8d03642510c94d7a31040ff076b255ddd01f7d8106eb3bd3d819c8e278c17b0`; the appended ET37–39 was then read and independently proved in ETR31. The exact checker records the source and independent proof hashes on every execution.

The independent derivation accepts the stated coefficient normalization, its full ring map and conductor, the rank-twenty-four signed extension and its entire cokernel, both root/sign multiplication operators and every intertwining, the three-step pole residue, the unchanged original receivers, all finite inverse singular values, every exterior degree, and the complete source-to-target inverse comparison with its original metric factors. It also checks the full coefficient Jacobian, all four maximal minors, both rank-loss loci and their eight-dimensional signed fibers.

Two distinctions were made explicit during this derivation and are present in the read root source:

- Exactly eight inverse singular values equal `|C|/5`. Another eight approach that scale and are strictly smaller at every finite point in the stated domain. ETR17–23 prove the exact quadratic formula, order, full finite bounds and every limiting constant.
- The rank-twenty-four algebra is the pullback of the full signed algebra to the normalization of its coefficient base. No assertion identifies that pullback with the integral closure of the signed cover. ETR6–7 prove its conductor directly, coefficient by coefficient.

The inverse of the actual source-to-target map is proved in ETR25–28. Its twenty-four singular values are the three explicitly computed coefficient inverse singular values multiplied by the eight original conductor inverse singular values. The complete top exterior norm is exactly

`(5|A|/(4|C|))^8 |det A_{3,s}|^(-6)`.

No original Gamma mass, center, inverse moment, root label or factor sign is deleted. The fixed original conductor remains the FC24 isomorphism. The demonstrated pole is in the specified coefficient-extension action; it is not a proved order jump of that conductor or an RH endpoint.

The additional finite estimate is ETR21–22. It supplies explicit two-sided bounds for every exterior degree throughout `A C != 0`, with an exact determinant equality in degree twenty-four. ETR31 proves its complete cross-receiver version: the baseline consists of the original eight conductor singular values multiplied separately by the exact coefficient scales `a_C, b_C, b_C`; the full exterior norm lies between the largest baseline product and that product times `(1+delta_C)^(min(j,8,24-j)/2)`. The proof checks all four entry counts per block and every possible global subset exponent, without numerical substitution or an assumption on the order of the two coefficient scales.

Immediate sources actually read for this bounded derivation:

- Received defining-prime account, all text read; the independently used ring assertions are equations (3)–(8). The later arithmetic and collision assertions in that source were not adopted wholesale.
- Cumulative original conductor source, FC21–24, FC27–30, RD18–22 and GD13–17, for the exact receiving maps, norms and determinant.
- Root extension source, complete ET1–39 including ET28a, at the final hash above.

Reproduction: run `python independent/ES_TOTAL_EXTENSION_REVIEW.py` from the calculation directory. The final execution passed 102 groups comprising 3,352 scalar entries. The symbolic checks verify the identities named in the JSON; the domain, conductor necessity, positivity, singular ordering, full tensor metric argument and limits are proved in the accompanying TeX. No rendering, publication or unrelated coordination was performed by this review.
