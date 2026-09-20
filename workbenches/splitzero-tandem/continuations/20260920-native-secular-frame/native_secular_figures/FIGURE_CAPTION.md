# The outgoing relation, the secular determinant and the original allowance

This is a diagram of exact maps proved in **NATIVE_SECULAR_RECEIVER.tex, NS1–37**, not a numerical picture of zeta zeros.

The source is the original positive arithmetic convolution measure
\(m=w_h^{*k}\), where \(w_h(t)=|(g/h)(1/2+it)|^2/(2\pi)\),
\(g=2\xi\), and \(h\) retains each selected actual zero with its complete order.
The packet is closed under conjugation and reflection. Its mass remains
\(\int m=\mu_h^k\). No replacement probability measure is used.

The quotient is \(C=\mathbb C[S]/(\chi)\), with the exact tensor cyclic
annihilator of NS4; \(S=k/2+iu\) is the displayed coordinate map.
At degree \(L\geq\deg\chi-1\), \(E\) reduces the original orthonormal
polynomial source to this quotient, \(G=(EE^*)^{-1}\), and \(R=E^*G\)
is its unique least-norm section. The finite symmetric Jacobi matrix
\(J_L\) records multiplication by \(u\) followed by orthogonal projection
back into that admitted source.

NS6 proves the entire correction, including its sign and phase:
\[
A=EJ_LR=M+Q,\quad M=(M_S-kI/2)/i,\qquad
Q=r\ell=\frac{i}{\omega_L}b_{L+1}b_L^*G.
\]
Here \(b_n=[p_n]_\chi\) and \(\omega_n\) is the full monic source norm.
The correction is the outgoing highest-degree multiplication term.
The attained matrix satisfies \(A^*G=GA\). The actual reflection
involution of NS7–8 proves \(b_L^*Gb_{L+1}=0\), hence \(Q^2=0\);
this is not an assertion that \(M\) and \(A\) have the same eigenvalues.

NS11–21 prove the polynomial identity at every old root:
\[
d=\det(zI-A)=\chi_u(1-f),\qquad
f=\ell(zI-M)^{-1}r=P_f/D_f,\qquad
d=(\chi_u/D_f)(D_f-P_f).
\]
The displayed reduced denominator is monic and retains the precise
pole orders \(p_\alpha\). The local coefficients are
\(c_{\alpha,j}=\ell(M-\alpha I)^j\Pi_\alpha r\), using the complete
Chinese-remainder projector in NS14. The active factor \(D_f-P_f\)
has simple real roots; the other factor remains part of the full
characteristic polynomial and can share a root with it.
For every original nonreal root, \(p_\alpha=e_\alpha\): the full pole
is cancelled in the construction of the new determinant \(d\).
The original polynomial \(\chi_u\) is unchanged.

NS35–37 identify the original control with this same term:
\[
\mathcal C=-i(Q-Q^{\dagger_G}),\qquad
\epsilon_L=\|\mathcal C\|_G=\|Q\|_G,\qquad
|2\Re\kappa-k|\leq\epsilon_L.
\]
The complete two-column Gram determinant in NS36 retains its
cross term, which vanishes here by the proved reflection symmetry.
The physical map is
\(\eta[P]=j_h(g/h)^{\otimes k}P(\sum s_j)\);
NS30–32 retain all its unit derivatives, factorials and multiplicities.
The diagram does not assert decay of \(\epsilon_L\), convergence of
spectra or the Riemann hypothesis.

Human provenance: **Alain Connes, Caterina Consani and Henri Moscovici,
Zeta Spectral Triples, arXiv:2511.22755v1**, Lemma key and equation
eq:detDp, provide the finite rank-one determinant comparison:
[original paper](https://arxiv.org/abs/2511.22755v1).
The complete native specialization is proved in NS1–37, extending
the programme's source calculation SZ-20260920-031.
Reproduce the vector SVG and PNG with make_native_secular_figure.py.
