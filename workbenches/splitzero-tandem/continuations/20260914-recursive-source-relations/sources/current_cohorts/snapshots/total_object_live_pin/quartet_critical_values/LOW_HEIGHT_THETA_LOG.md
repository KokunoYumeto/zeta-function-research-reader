# Low-height theta calculation

Task from `/root/quartet_critical_values`: prove from the actual unscaled theta programme that `g(s)=2xi(s)` has no zero for `0 <= Re s <= 1`, `|Im s| <= 2`. No child agents spawned.

Source read: `total_object/certified_hankel_attachment.tex`, HCA.1--HCA.2. The original source is `f0=Theta(phi*)`, with the original even positive `psi(y)=exp(y/2) f0(exp(y))`. This calculation does not modify another source or any sealed edition.

New exact proof in `low_height_theta.tex`:

- Differentiate the original Gaussian theta function to obtain `f0=(x^2 theta'(x))'`. Differentiate the original theta functional equation to obtain the endpoint limits. This proves the exact original mass `g(1)=1`.
- `M0 >= 1 - g''(1)/8` follows by integrating `cosh(z)-1 <= z^2 cosh(z)/2`.
- Bound the actual positive integral for `g''(1)` by the complete theta sum of polynomial-exponential integrals. Use `log x <= x-1`, `(1+v)^2 >= 1+2v`, exact factorial integrals, and `pi > 3`.
- The remaining five rational coefficients sum to `230/27`. The complete theta sum is `<1/19` because `exp(3)>89641/4480>20`, so `g''(1)<230/513`.
- The original Fourier--Laplace integral gives `Re g(1/2+a+it) >= M0-t^2 g''(1)/2`. Hence throughout the stated closed rectangle, `Re g > 97/2052 > 0`.
- The local ring map is explicit: multiplication by `g` is invertible there with inverse multiplication by the holomorphic germ `1/g`, bounded on the rectangle by `2052/97`. Thus the corresponding local quotient modules vanish, with no deletion of proper-source kernels.

`check_low_height_theta.py` verifies the rational arithmetic exactly with `Fraction`; it is not used as a substitute for the analytic proof or as a numerical zero verification. Full tails are bounded analytically in the proof.

Self-review: confirmed the factor `16 pi^2` in the upper bound, the original integration measure `dx/x` before evaluation at `s=1`, the even-kernel factors of two, and the constants `1/8`, `17/8`, `230/513`, `97/2052`. Corrected a typesetting-only single line-break escape and moved LHT.18 into a display. No mathematical normalization or extra hypothesis was introduced.
