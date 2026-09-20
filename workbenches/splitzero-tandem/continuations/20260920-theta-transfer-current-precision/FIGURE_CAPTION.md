# From arithmetic moments to the original complex current

![Exact precision transfer](figures/moment_current_transfer.png)

Read the six numbered panels in order. They display the actual map of error bounds, not a hypothetical numerical evaluation. In the original simple-quartet application, `k ≡ 1 (mod 4)`, `k ≥ 77`, `q=(k+1)²`, and `N ≥ q−1`.

1. The actual positive arithmetic measure gives the parity moment matrix H. Its proved density floor on [1,2] is d_nu. The interval Gram is `(L_t)ij=(2^(i+j+1)−1)/(i+j+1)` and `g_t=det(L_t)/tr(L_t)^t`. The original mass stays in `h=d_nu min(g_t)` and the explicit diagonal-moment upper sum U. No mass is set to one.
2. If each scalar moment has absolute error at most epsilon, the largest parity block size d gives `||H−Hhat||≤d epsilon`. Set `theta=d epsilon/h≤1/4` and use the outward lower matrix `Hlo=Hhat−d epsilon I`, not an assumed positive midpoint.
3. Positivity is proved: `(h/2)I≤Hlo≤H≤U I`, and `(1−2theta)H≤Hlo`. All inverses consequently have an explicit positive margin.
4. The original quotient map J retains the full physical unit and the complex triangular coordinate map. With `W=(JJ*)^−1`, the same fibres give `G0=(JHlo^−1J*)^−1`, `G=(JH^−1J*)^−1` and `(h/2)W≤G0≤G≤(1−2theta)^−1G0`. J is not replaced by the observation map Lambda J.
5. P and P0 project onto the same fixed kernel `K=ker Lambda`, orthogonally for G and G0 respectively. The complete block/projection calculation bounds the changes in the original pairings `z=<Px,A(I−P)x>_G` and `w=<(I−P)x,APx>_G`; z0,w0 use P0,G0. The original action `A=M_S` and class x are fixed. Put `Mbar=2 sqrt(U/h)||A||_W` and `C=Mbar U||x||_W²`. Then `|z−z0|,|w−w0|≤6C theta` and `|z0|,|w0|≤C/2`.
6. Expanding the product keeps all three errors, including the product of the two errors: `conj(z)w−conj(z0)w0=conj(z−z0)w0+conj(z0)(w−w0)+conj(z−z0)(w−w0)`. Hence its absolute value is at most `6C²theta+36C²theta²≤15C²theta`. For target error t*, choose `theta≤min(1/4,t*/(15C²))` when C>0, and `epsilon≤theta h/d`. When C=0 the product is zero.

Complete proofs: [native precision](NATIVE_MOMENT_PRECISION.tex), [projection calculation](PROJECTION_PHASE_RETURN.tex) PD4–19, [independent complete composition](NATIVE_MOMENT_PHASE_COMPOSITION.tex) MC1–16, and [root complete composition](MOMENT_TO_COMPLEX_CURRENT.tex) MC1–13. The one-factor-to-convolution moment tolerance, absent from the drawing to preserve legibility, is fully proved in the two composition sources.

Human provenance: the finite-resolvent enclosure route uses Jörn Zimmerling, Vladimir Druskin and Valeria Simoncini, [arXiv:2407.21505v3](https://arxiv.org/abs/2407.21505v3); the earlier parity receiver uses A. I. Aptekarev, G. López Lagomasino and A. Martínez-Finkelshtein, [arXiv:1410.1261v1](https://arxiv.org/abs/1410.1261v1). Their original TeX was read in full. The new receiving calculations and exact matrix inequalities are proved in the linked programme sources; they are not attributed to those papers as already stated theorems about this particular arithmetic measure.
