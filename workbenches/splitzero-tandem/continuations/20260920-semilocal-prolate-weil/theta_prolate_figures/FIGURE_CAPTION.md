# Exact constants and the complete finite theta-transfer bound

The top panel shows the literal source maps proved in PT1–7 of
THETA_PROLATE_SOURCE_RECEIVER.tex. The seed in Connes–Consani–Moscovici,
*Zeta Spectral Triples*, [arXiv:2511.22755v1](https://arxiv.org/abs/2511.22755v1),
equations ku, emap, and xih, is named \(H\) to distinguish it from
the programme's zero-divisor polynomial \(h\). The original seed is
\(\phi_*=4H\), the original theta map is \(\Theta\phi=2\sum_{n\ge1}\phi(nx)\),
and the original source is \(f_0=8\sum H(nx)\). Consequently
\(K=Uf_0/8\) and its literal transform is \(\Xi/4\).
The unitary \(U:L^2(du)\to L^2(du/u)\) retains the factor \(1/64\) in
the squared source norm and the exact generator centre and phase.
Connes–Consani, [arXiv:2207.10419v1](https://arxiv.org/abs/2207.10419v1),
Lemma propmapE(ii) and Proposition propmapE1, supply human provenance
for the factor-two theta trace. PT4–7 give the complete direct calculations.

The lower-left panel plots the *proved upper bound*, not the transform error,
for the explicitly chosen truncated Hermite input
\(A_\lambda=H|_{[-\lambda,\lambda]}\), extended by zero, on the entire strip
\(|\Im z|\le1/4\). Its defined interior discrepancy is exactly zero.
It is not identified with a prolate eigenfunction or a minimum Weil
eigenvector. The remaining two contributions are the omitted Gaussian lattice
tail and the two endpoints of the multiplicative Fourier integral.
PT8–12 prove their sum bounds
\(\sup|\widehat K_\lambda-\Xi/4|\) for every cutoff.
The lattice curve starts immediately after \(\lambda=1\) because its value
there is zero and cannot be shown on a logarithmic axis.
The plot uses floating-point evaluations of explicit incomplete-gamma and
erfc expressions; the samples are not interval-certified numerical results.

The lower-right panel retains all three terms for the actual prolate input,
including its actual, unevaluated discrepancy norm \(d_\lambda\).
The proof also supplies the exact original-divisor interpolation and jet
maps in PT13–18. A quotient jet below multiplicity \(m\) retains the input
derivatives through order \(2m-1\). The figure makes no claim of spectral convergence, native
growing-degree moment control, or RH.

Reproduction: run make_theta_prolate_receiver_figure.py in the parent
folder with NumPy, SciPy and Matplotlib. The SVG, PNG and explicitly labelled
sample JSON are generated together. This is a two-dimensional exact-map and
bound illustration; no geometric identification or three-dimensional model
is implied.
