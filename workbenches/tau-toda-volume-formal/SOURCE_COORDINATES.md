# The unchanged source moment matrix is an explicit formal input

`SplitZeroWeightedQuotientVolume` removes even the need for an orthonormal coordinate conversion in the quotient-volume calculation. Let M be the original source moment matrix, C the original representative columns, and B the admitted relation columns. With H=(B* M B)^(-1), the constructed residual is

    R = C - B H B* M C.

Lean checks

    B* M R=0,
    R* M R=C* M C-C* M B H B* M C,
    det [[C* M C,C* M B],[B* M C,B* M B]]
       = det(B* M B) det(R* M R).

For every supplied observation J killing those relation columns, JR=JC. The determinant-ratio form retains the nonzero relation determinant as an explicit hypothesis. These are algebraic statements on the source coordinates; they do not replace M by the identity or normalize the measure. The unweighted module remains a special useful interface, not a silent change of the arithmetic metric.

To instantiate the source's polynomial sequence, C is the coordinate inclusion of 1,S,...,S^(q-1), B is the coefficient map P -> chi P, and M is the actual degree-N moment Gram. The concatenation [C,B] has determinant one by monicity. Thus the source's analytic construction identifies this formal ratio with D_(N+1)/B_(N-q+1). The general polynomial basis proof and analytic integral identities remain separately scoped source results.

This supplement updates the earlier count in the research note: the final target manifest contains five new Lean modules. Execution status and exact source hashes are recorded by the completed workflow and PR body, not inferred from this prose.
