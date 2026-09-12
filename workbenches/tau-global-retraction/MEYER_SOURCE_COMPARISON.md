# The theta quotient in Meyer's spectral construction

This source comparison was added on 12 September 2026. It supplements, without rewriting, the original note's account of which literature its author consulted.

Ralf Meyer, [*A spectral interpretation for the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/0412277), defines the zeta operator in section 3 by

$$Z\phi(x)=\sum_{n\geq1}\phi(nx).$$

His source $H_\cap$ is the space of even Schwartz functions with $\phi(0)=\widehat\phi(0)=0$. His target $H_-$ is the intersection, over all real $s$, of the multiplicative Schwartz spaces weighted by $x^{-s}$. The precise identifications with [the present note](RESEARCH_NOTE.md) are

$$V=H_\cap,\qquad \mathscr B=H_-,\qquad \Theta=2Z|_V.$$

The factor 2 comes from pairing the positive and negative terms in the theta sum on even functions. The Fourier kernels with signs $+2\pi i x\xi$ and $-2\pi i x\xi$ agree on these even inputs. Meyer's local Euler operator $x\partial_x$ is the negative of the present $D=-x\partial_x$.

The target topologies also agree, not just their underlying functions. In logarithmic coordinates $x=e^y$, polynomial factors in $y$ are controlled by slightly stronger exponential weights. Conversely every real weight is bounded by neighboring integer weights. The weighted logarithmic Schwartz seminorms and the present integer-weight Euler-derivative seminorms therefore define the same Fréchet space.

Meyer's theorem following the Poisson formula in section 3 (source label `the:Zeta_estimate`) proves that $Z:H_+\to H_\cup$ is a topological embedding with closed range, and $Z\phi\in H_-$ exactly when $\phi\in H_\cap$. Its proof uses the continuous Möbius inverse on the exterior weighted space (label `pro:Z_invertible`), Poisson summation and simultaneous estimates of a function and its Fourier transform. Thus the closed-range assertion for $\Theta:V\to\mathscr B$ is already covered by this literature under the displayed maps.

The present note additionally writes an explicit continuous left inverse $\Lambda:\mathscr B\to V$ and the projection $K=1-\Theta\Lambda$, retaining their scaling defect. Closed range alone does not give that particular projection. This source comparison makes no priority claim about the projection or the later literature.

Source version checked: arXiv TeX `math_0412277.tex`, SHA-256 `ab9bc31f3c105a64fdc6f3b65ad16701dd8bf218fc90df98fe8d7f3c7c58c00e`; definitions at lines 240–279, zeta operator and inverse at 445–503, Poisson/source space and complete closed-range proof at 514–571. The source body and proof, not merely its abstract, were read for this comparison. No source-paper bulk text is reproduced here.
