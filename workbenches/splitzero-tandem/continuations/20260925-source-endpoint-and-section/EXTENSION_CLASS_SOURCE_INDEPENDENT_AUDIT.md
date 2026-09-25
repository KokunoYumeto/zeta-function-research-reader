# Independent audit of the extension-class source and residue maps

24 September 2026. Mathematical review only. No audited proof file was edited.

The complete ECR0–ECR7 proof was checked at SHA256 0da1815f474c5279012a94be8f65fdb8dbf3a178f56e97ff7b543a2d04c82bbd. No required correction was found. The conclusions concern the actual complete arithmetic receiver. They assign no arithmetic, coordinate, metric, midpoint, or parity to the support, and make no cyclic-group identification of the user's information layers.

## Reading coverage and exact versions

The following programme proofs were read over their entire indicated ranges. Their more remote GMS, SSI, GTR and SDT dependencies were received through these complete proofs; no new independent audit of every remote theorem or new complete human-source reading is claimed.

| File | Coverage | SHA256 |
|---|---|---|
| ../tau_weight_cohomology_20260924/CC_FULL_SOURCE_OBSTRUCTION_DECOMPOSITION.md | FOD0–FOD8 | 0f16829aa955a3af1bd8b16d70851df5467040b9685d607a7a1b8aa3a0cae0a3 |
| ../tau_weight_cohomology_20260924/CC_NORMAL_EXTENSION_ANNIHILATOR.md | NEA0–NEA10 | 817455b79efe7a3cdbb5310f760cfef86f5a9bc02a2498a116df0253c8f3172b |
| RESIDUE_TRACE_TRANSFER_INDEPENDENT.md | RTT0–RTT11 | 6a83d81039b4eb3e49c4054b4ff157896709647d6a5546751362b05a21de25b2 |
| GEOMETRIC_TRANSFER_POSITIVE_ADJOINT_DEFECT.md | GTAH0–GTAH7 | dd27d0022c6cc0b82fc0cabcc5d43aed84d18fe762f382ba3be16e2fa50dc739 |
| GLOBAL_SEPARATOR_TO_RESIDUE_COMPARISON.md | GSR0–GSR4 | 8abc2cbe84006219c2a49a38c625a9462ba3afd93d87fae65fd39e4b6be1e8a5 |
| GLOBAL_INFINITESIMAL_QUOTIENT.md | GIQ9, including the full-source extension and convolution estimates | 7c6dc699f7b028767d468bbe8e40bc4b83629b5da4d5cb0be685aad05371050e |

The FOD and NEA hashes agree with ECR0. Their annihilator proofs use entire-function cancellation and a nowhere-zero Gaussian test; they require neither a principal-ideal assertion nor arbitrary infinite interpolation. FOD3–FOD5 prove the low-component pushout and cyclic-module isomorphism used in ECR6.

## Embeddings, local jets, and the actual source

For \(t>0\), \(g_t(s)=e^{ts^2}\) belongs to \(\mathcal B\), and \(g_tM\subset\mathcal B\). The maps in ECR1.3 are well defined and \(M\)-linear. The first has kernel \(\mathcal B\cap\mathfrak a=\mathcal I\). The second is injective because \(g_t\) is a unit in each local holomorphic ring at an actual zero. Their composites are multiplication by \(g_t\), exactly as stated.

Both properness proofs hold on the complete actual divisor. An image of \(e_0\) under \(j\) would give a rapid-strip function with value one at every zero. An image of \([g_{t/2}]\) under \(b_t\) would give a function in \(M\) with values \(e^{-t\rho^2/2}\), of modulus \(e^{t(\gamma^2-\sigma^2)/2}\). The former contradicts rapid decay, and the latter contradicts polynomial growth on the fixed zero strip along the unbounded actual zero heights. These necessary value conditions use no interpolation assertion. The same argument proves that \([g_t]\) is not a unit of \(M/\mathfrak a\).

Expanding \(e^{t\rho^2}e^{2t\rho z}e^{tz^2}\) gives ECR2.1, including all factorials and summands. On a length-\(m\) block the matrix is lower triangular with diagonal \(e^{t\rho^2}\), hence determinant \(e^{mt\rho^2}\). Its inverse retains the complete Taylor jet of \(e^{-t\rho^2}e^{-2t\rho z}e^{-tz^2}\). This finite local inverse asserts no global division in \(M\). The parameter identity \(b_u=m_{g_{u-t}}b_t\) has the stated domain \(u>t>0\).

The source estimate in ECR3.2 can also be checked directly. For \(F(s)=e^{ts^2}h(s)\), shifting from the line \(1/2\) to any fixed real \(c\) gives
\[
a_{t,h}(u)=\frac{u^{-c}}\pi\int_{\mathbb R}F(c+iy)u^{-iy}\,dy.
\tag{ECRA1}
\]
The horizontal integrals tend to zero because the integrand on the intervening strip is bounded by a polynomial in the height times \(e^{-ty^2}\), for fixed \(u>0\). Differentiation under the absolutely convergent integral gives, for \(D=u\partial_u\),
\[
|D^j a_{t,h}(u)|\le\frac{u^{-c}}\pi
\int_{\mathbb R}|c+iy|^j|F(c+iy)|\,dy.
\tag{ECRA2}
\]
For a source seminorm of exponent \(N\), choose \(c=N+1\) on \(u\ge1\) and \(c=-N-1\) on \(0<u\le1\). The integrals are finite, and \((u^N+u^{-N})|D^j a_{t,h}(u)|\) is bounded. This proves every actual source seminorm. Fourier inversion retains the coefficient \(1/\pi\) and the original half-Mellin factor \(1/2\).

For \(h=1\), the integral is exactly
\(\sqrt{\pi/t}\exp(-(\log u-t)^2/(4t))\). Multiplying by the original \(u^{-1/2}e^{t/4}/\pi\) gives ECR3.3 with all factors and signs retained. This source need not lie in \(J\).

## Residue, arithmetic, and the value kernel

RTT5 applies to \(g_th,g_tk\in\mathcal B\). The product is exactly
\[
g_t(\rho)\overline{g_t(\rho^\#)}
=e^{t\rho^2}e^{t(1-\rho)^2},
\qquad \rho^\#=1-\overline\rho.
\tag{ECRA3}
\]
Its modulus is \(e^{t\{\sigma^2+(1-\sigma)^2-2\gamma^2\}}\). This Gaussian bound, polynomial multiplier growth, and the full zero-count estimate prove absolute convergence. Exchanging \(\rho\) and \(\rho^\#\), with equal multiplicities, proves Hermitian symmetry. Replacing the product by \(|g_t(\rho)|^2\) would change the original Weil form; ECR does not do that.

The kernel of \(\mathsf S_t\) and of the positive value form is exactly \(\mathfrak a_{\rm val}/\mathfrak a\), because all Gaussian values are nonzero. ECR correctly avoids identifying this with the global nilradical. Its exact criterion is
\[
\sqrt{\mathfrak a}/\mathfrak a
=\{[h]:\exists n\ge1\ \forall\rho,\
 n\operatorname{ord}_{\rho}h\ge m_\rho\}.
\tag{ECRA4}
\]
Indeed \([h]^n=0\) is equivalent to \(h^n\in\mathfrak a\), and then to the displayed inequalities. Value vanishing requires only \(\operatorname{ord}_{\rho}h\ge1\); it does not furnish a single exponent valid at all zeros. No uniform multiplicity bound is assumed.

The entire \(A_{t,h,k}\) is a product of the specified rapid-strip transforms. GIQ9's reflection and convolution estimates therefore place its inverse in the complete logarithmic test space. ECR4.6–ECR4.7 retain the endpoints, \(1/(2\pi)\), digamma argument \(1/4+iy/2\), \(-\log\pi\), and every prime-power coefficient. Substitution at \(0,1,-2r\) checks every term of ECR4.8. The trivial-divisor sum is finite as stated.

An additional constant check, for the actual generator in both slots, is
\[
v_{t,1,1}(v_0)=
\frac{e^{t/2}}{\sqrt{8\pi t}}
\exp\!\left(-\frac{v_0^2}{8t}\right).
\tag{ECRA5}
\]
Its Fourier transform is \(e^{t/2}e^{-2ty^2}\), exactly \(A_{t,1,1}(1/2+iy)\). Its two endpoint Laplace values are \(e^t\). This checks the constants against the original arithmetic receiver.

## Positive defect and the source separator

The auxiliary positive form has weight \(|g_t(\rho)|^2=e^{2t(\sigma^2-\gamma^2)}\). Squaring the modulus of GTAH's exact multiplier \(e^{-i\gamma\log a}(a^\sigma-a^{1-\sigma})\) gives ECR5.4. The Weil transfer identity follows from \(\overline{a^{1-\rho^\#}}=a^\rho\); \(U_aT_a=aI\) holds on the complete class module, including its jets.

For \(a>1,t>0\), every term in ECR5.5 is nonnegative and has a strictly positive Gaussian weight. Its vanishing consequently tests every actual zero at once. This is detection, not a proof of vanishing. What further calculation is available from this result and GTAH5? Retaining the full original-source weight gives
\[
\mathcal E(a,2t)
\le\mathfrak d_{a,t}(e_0,e_0)
\le e^{2t}\mathcal E(a,2t).
\tag{ECRA6}
\]
Proof: multiply the nonnegative summands of GTAH5.2 by the retained factor \(e^{2t\sigma^2}\), and use \(1\le e^{2t\sigma^2}\le e^{2t}\) on the established strip. Every sum converges, so the inequalities hold for the complete sums. This calculates the comparison between the earlier global weighted trace and the actual extension generator.

Finally, FOD's identity \(ce_0=e_0\) gives \(cx=x\) on the full module \(M e_0\), proving ECR6.1. FOD3's pushout and FOD4's equal annihilators give the exact connection to the low source-extension component, retaining its intersection kernel. The normal action still has \(a^{s+1}\); no extra factor is erased and no postcomposition action is replaced by conjugation on a derived morphism. The separate involution derivation is outside this audit.

The audit approves the stated maps and identities. It does not assert purity, place an unspecified topology on Ext, replace a source quotient by an unrestricted infinite jet product, or replace original zeta and its complete factors.
