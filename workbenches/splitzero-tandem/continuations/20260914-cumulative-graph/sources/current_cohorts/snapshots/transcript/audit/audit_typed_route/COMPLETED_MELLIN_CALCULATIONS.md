# Completed Mellin-realization calculations on the original theta source

These calculations close two finite algebraic gaps identified by the fully read transcript section U0029–U0040. They use the original theta source, its Fourier convention, its differentiated Gaussian, its complete two-leg support, and the original generator g=2ξ. They do not replace that source by an arbitrary polynomial family. They concern Mellin realization, not the separately assigned homotopy fibre of restriction to σ.

## 1. Retained objects and source equations

Let E=ℂ and retain
\[
V=\{\phi\in\mathcal S(\mathbb R):\phi(-x)=\phi(x),\
\phi(0)=0,\ \widehat\phi(0)=0\},\qquad
\widehat\phi(\xi)=\int_{\mathbb R}\phi(x)e^{-2\pi i x\xi}\,dx,
\]
\[
\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):
\sup_{x>0}x^b|(-x\partial_x)^kF(x)|<\infty
\text{ for every }b\in\mathbb Z,\ k\ge0\}.
\]
Set
\[
D=-x\partial_x,\quad
\Theta\phi(x)=\sum_{n\in\mathbb Z\setminus\{0\}}\phi(nx),\quad
JF(x)=x^{-1}F(1/x),
\quad
\mathcal MF(s)=\int_0^\infty F(x)x^s\,\frac{dx}{x}.
\]
The primary Tau Base NOTE.md equations (10)–(14),(21)–(22),(38) and the actual comparison source retain the identities
\[
J\Theta=\Theta\mathcal F,\quad
\mathcal F D=(1-D)\mathcal F,\quad
\Theta D=D\Theta,\quad
\mathcal M(DF)=s\mathcal MF.
\]
The fixed source function is
\[
\phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\qquad
\widehat{\phi_*}=\phi_*,
\]
and
\[
b_*=\Theta\phi_*,\qquad
\mathcal Mb_*=g,\qquad
g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
The entire function g is not zero. For example, the retained theta-boundary calculation gives g(0)=1. The arithmetic quotient is Q=𝔅/ΘV. The original two-leg complex is
\[
C^\bullet=[V\oplus V\xrightarrow{\Theta\phi-J\Theta\psi}\mathscr B],
\qquad C^0=V\oplus V,\quad C^1=\mathscr B.
\]
Its H⁰ is the actual Fourier graph V and its H¹ is Q. A single-leg complex has H⁰=0; it is not the same complex.

All sheaf arguments below are stalkwise over R=𝒪_{ℂ,s₀}, with its original coordinate s, and hence glue. This local analytic ring is an integral domain. A nonzero entire function has a nonzero germ at every point by the identity theorem, even if its value at that point is zero.

## 2. The raw two-leg syzygy at every source order

For each integer m≥1, retain the actual functions
\[
b_{+,m}=\Theta D^m\phi_*=D^m b_*,
\qquad
b_{-,m}=J\Theta D^m\phi_*=(1-D)^m b_*.
\]
Their Mellin transforms are exactly
\[
\mathcal Mb_{+,m}=s^m g,\qquad
\mathcal Mb_{-,m}=(1-s)^m g.
\]
Thus the same source input D^mφ* on the two original charts gives these two images. No independent spectral function has been chosen.

Put a_m(s)=s^m and v_m(s)=(1-s)^m. Define
\[
\delta_m:R^2\longrightarrow R\otimes_E\mathscr B,\qquad
(f,h)\longmapsto f\otimes b_{+,m}-h\otimes b_{-,m},
\]
\[
\beta:R\otimes_E\mathscr B\longrightarrow R,\qquad
f\otimes F\longmapsto f\,\mathcal MF.
\]
These give the literal commutative comparison
\[
\begin{array}{ccc}
R^2&\xrightarrow{\delta_m}&R\otimes_E\mathscr B\\
1\downarrow&&\downarrow\beta\\
R^2&\xrightarrow{(f,h)\mapsto g(a_mf-v_mh)}&R.
\end{array}
\]

First, b₊,ₘ and b₋,ₘ are E-linearly independent. A relation c b₊,ₘ+d b₋,ₘ=0 gives
g(s)(c s^m+d(1-s)^m)=0. On the nonempty open set on which g does not vanish the polynomial factor vanishes, so that polynomial is identically zero. Evaluation at s=0 gives d=0; evaluation at s=1 gives c=0. Tensoring this two-dimensional E-subspace with R is injective because vector spaces split over E. Therefore δₘ is injective.

Here are the exact polynomial coefficients used for its composite:
\[
A_m(s)=\sum_{k=0}^{m-1}\binom{m+k-1}{k}s^k,\qquad
B_m(s)=\frac{1-A_m(s)(1-s)^m}{s^m}.
\]
The power series (1-s)⁻ᵐ has coefficients binom(m+k−1,k), so its truncation Aₘ gives a numerator divisible by sᵐ. Thus Bₘ is a polynomial and
\[
B_m a_m+A_m v_m=1.
\]
The germ g is a non-zero-divisor. Consequently βδₘ(f,h)=0 is equivalent to aₘ f=vₘ h. Set
r=Bₘ h+Aₘ f. Then
\[
v_mr=B_mv_mh+A_mv_mf
     =B_ma_mf+A_mv_mf=f,
\]
\[
a_mr=B_ma_mh+A_ma_mf
     =B_ma_mh+A_mv_mh=h.
\]
Conversely (f,h)=(vₘr,aₘr) has aₘf−vₘh=0. The parametrization is injective because its two coefficients generate the unit ideal. Hence
\[
\boxed{\ker\delta_m=0,\qquad
\ker(\beta\delta_m)=R\,(v_m,a_m).}
\]
In particular
\[
\boxed{z_m=v_m\otimes b_{+,m}-a_m\otimes b_{-,m}\ne0,
\qquad \beta z_m=0.}
\]
This proves the exact all-order extension of A1361's m=1 witness.

Its support is not optional. Let L=𝒫({+,−}), with empty mask corresponding to external absence. On the + face δₘ is f↦f⊗b₊,ₘ; on the − face it is h↦−h⊗b₋,ₘ; on the joint face it is the map above. All maps retain their masks. The raw maps on either singleton face, and their Mellin composites, are injective because b±,ₘ and gaₘ,gvₘ respectively are nonzero. The new syzygy occurs only in the joint face. Its lifted image is
\[
(\{+,-\},z_m)\longmapsto(\{+,-\},0),
\]
not τ. At m=0 the two source images coincide, and the raw map already has kernel R(1,1); thus m=0 is not falsely included in the new-relation assertion.

This result excludes a quasi-isomorphism of these particular raw complexes: the first H⁰ is zero while the second H⁰ is R. It says nothing by itself about nonvanishing of the full realized H¹ kernel; that different calculation follows in §4.

## 3. Operator balancing removes the raw tensor relation, and retains honest joint cycles

Let A=E[t]. On 𝔅 let t act by D, and on R let t act by multiplication by s. The quotient map
\[
\pi_{\rm bal}:R\otimes_E\mathscr B\longrightarrow R\otimes_A\mathscr B
\]
imposes the R-linear span of the actual relations
\[
sh\otimes F-h\otimes DF.
\]
These are Mellin-null because M(DF)=s MF.

For every j≥1, the exact telescoping identity is
\[
h\otimes D^j b_*-hs^j\otimes b_*
=\sum_{k=0}^{j-1}
\left(hs^k\otimes D^{j-k}b_*
      -hs^{k+1}\otimes D^{j-k-1}b_*\right).
\]
Each summand is the negative of a displayed elementary balancing relation. Applying this identity to all coefficients of the original polynomials tᵐ and (1−t)ᵐ proves
\[
\pi_{\rm bal}(h\otimes P(D)b_*)=hP(s)\otimes b_*
\quad(P\in E[t]).
\]
It follows without removing any sign that
\[
\pi_{\rm bal}(z_m)
=v_ma_m\otimes b_*-a_mv_m\otimes b_*=0.
\]
More explicitly, with
Δ_P=1⊗P(D)b*−P(s)⊗b*,
\[
z_m=v_m\Delta_{t^m}-a_m\Delta_{(1-t)^m}.
\]
The coefficients of (1−t)ᵐ remain (−1)ʲ binom(m,j).

Balancing is not a reason to erase genuine degree-zero cycles in the original two-leg source. The exact saturated source calculation makes this precise. On the plus leg let t act by D; on the minus leg let t act by 1−D. These are the infinitesimal actions induced by primary (34), since the minus scaling is aU₁/ₐ. Define
\[
i_{+,m}:A\longrightarrow V,\quad
P\longmapsto P(D)D^m\phi_*,
\]
\[
i_{-,m}:A\longrightarrow V,\quad
Q\longmapsto Q(1-D)D^m\phi_*.
\]
They are injections. Indeed, Θ applied to the first has Mellin transform P(s)sᵐg; JΘ applied to the second has transform Q(s)(1−s)ᵐg, and polynomial multiplication by either nonzero entire function is injective. Let A b* be the cyclic A-submodule of 𝔅 generated by b*. It too is free rank one because P(D)b*=0 implies P(s)g(s)=0 and therefore P=0.

The original two-leg differential restricted to these saturated subspaces is therefore exactly
\[
C_m^{\rm cyc}
=\left[A^2\xrightarrow{(P,Q)\mapsto
(t^mP-(1-t)^mQ)b_*}A b_*\right].
\]
Fourier supplies the minus term:
\[
J\Theta\bigl(Q(1-D)D^m\phi_*\bigr)
=Q(D)(1-D)^m b_*.
\]
The same Bezout polynomials show the differential is onto and that its kernel is
A((1−t)ᵐ,tᵐ). Hence
\[
\boxed{H^0(C_m^{\rm cyc})=A((1-t)^m,t^m),\qquad
H^1(C_m^{\rm cyc})=0.}
\]
This cycle is an actual Fourier-compatible two-leg cycle before Mellin realization. It is not a spurious raw tensor relation.

The A-module R is torsion-free: multiplication by a nonzero polynomial P(s) is injective in the analytic domain R. A torsion-free module over a PID is flat. One direct proof writes it as the directed union of its finitely generated submodules; those submodules are finitely generated torsion-free modules over a PID and hence free, and tensoring commutes with directed colimits. A filtered colimit of exact sequences of modules is exact. Thus R is flat, and tensoring the displayed exact cyclic sequence gives
\[
H^0(R\otimes_A C_m^{\rm cyc})
=R((1-s)^m,s^m),\qquad H^1=0.
\]
No joint H⁰ has been lost.

For completeness, its analytic comparison has β_cyc(h⊗b*)=hg and identity in degree zero:
\[
[R^2\xrightarrow{a_m f-v_mh}R b_*]
\longrightarrow
[R^2\xrightarrow{g(a_m f-v_mh)}R].
\]
The degree-one map ×g is injective with cokernel R/(g), and the degree-zero map is identity. Hence there is an exact sequence of these cochain complexes whose quotient is R/(g) concentrated in degree one. The induced map on H⁰ is identity on the displayed R-syzygy; the analytic target has H¹=R/(g). This calculation locates precisely what changes for this saturated cyclic subcomplex.

The cyclic subcomplex is not the full theta complex. Its inclusion is the literal pair (i₊,ₘ,i₋,ₘ) in degree zero and A b*↪𝔅 in degree one, and its differential is the restriction just proved. Extending these maps to the corresponding supported faces retains all masks. No equality with the full balanced kernel has been inferred.

## 4. An explicit free submodule in the raw realization kernel

This makes A1427's nonvanishing statement constructive with the actual finite-jet maps.

Let Z be any finite set of actual zeros of g, with their actual positive multiplicities mρ. Retain the complete jet space
\[
A_Z=\bigoplus_{\rho\in Z}E[z_\rho]/(z_\rho^{m_\rho}),
\qquad z_\rho=s-\rho,
\]
and the primary map
\[
J_Z:Q\longrightarrow A_Z,\qquad
[F]\longmapsto
\left(\sum_{j<m_\rho}
\frac{(\mathcal MF)^{(j)}(\rho)}{j!}z_\rho^j\right)_\rho.
\]
The source's smooth compactly supported right inverse can be written in its original measure. Fix 0<R'<R₀, let
\[
\eta(y)=
\begin{cases}\exp(-1/(R'^2-y^2)),&|y|<R',\\0,&|y|\ge R',\end{cases}
\]
and for α=(ρ,j) put
\[
r_\alpha(x)=x^{\bar\rho-1}\frac{(\log x)^j}{j!},
\]
\[
B_{\alpha\beta}=
\frac1{j!k!}\int_{-R'}^{R'}
\eta(y)e^{(\rho+\bar\sigma-1)y}y^{j+k}\,dy
\quad(\beta=(\sigma,k)).
\]
For a coefficient vector c,
\[
c^*Bc=
\int_{-R'}^{R'}\eta(y)e^{-y}
\left|\sum_\alpha\bar c_\alpha
e^{\rho y}\frac{y^j}{j!}\right|^2dy.
\]
The exponential polynomials with distinct exponents and all orders below the retained multiplicities are linearly independent on every open interval. To verify this, a vanishing sum is an entire function of y and vanishes identically. For a selected exponent ρ, applying ∏_{σ≠ρ}(∂ᵧ−σ)^{mσ} kills the other blocks. On e^{ρy}Pρ(y), each factor becomes (∂ᵧ+ρ−σ)^{mσ} on the polynomial Pρ; its constant term is nonzero, and in the degree-ordered polynomial basis its matrix is triangular with nonzero diagonal. Its product is therefore invertible. Thus Pρ=0 for each ρ. Since η is positive on the interval, c*Bc=0 forces c=0. Hence B is positive definite and invertible.

For v∈A_Z define
\[
F_v(x)=\eta(\log x)\sum_\beta(B^{-1}v)_\beta r_\beta(x).
\]
It lies in C_c^∞((e^{-R₀},e^{R₀}))⊂𝔅. Substituting x=eʸ in each Mellin derivative gives J_Z[F_v]=v, with exactly the displayed factorials and exponent −1. Thus
\[
s_Z:A_Z\longrightarrow Q,\qquad v\longmapsto[F_v]
\]
is an explicit E-linear section of J_Z. It is not asserted to be equivariant under scaling; that additional property is neither needed nor inferred.

At each analytic stalk retain
\[
\bar\beta:R\otimes_E Q\longrightarrow R/(g),\qquad
h\otimes[F]\longmapsto[h\,\mathcal MF],
\qquad K_{\rm raw}=\ker\bar\beta.
\]
Define
\[
\boxed{\iota_Z:R\otimes_E A_Z\longrightarrow K_{\rm raw},\qquad
h\otimes v\longmapsto gh\otimes s_Z(v).}
\]
The image is in the kernel because its Mellin evaluation is a multiple of g. If ι_Z(w)=0, applying 1⊗J_Z gives gw=0 in R⊗A_Z. This latter module is free of rank ∑ρmρ, and g is a non-zero-divisor. Thus w=0. Therefore ι_Z is an injective R-linear map.

This gives an explicit free rank-∑ρmρ submodule of the raw kernel for every nonempty retained packet Z. The map is natural under stalk restriction for the fixed smooth section. Every derivative direction below each actual multiplicity appears in its domain. In particular the proof does not merely cite existence of a Hamel basis for Q or reduce the packet to its values.

At each original nonempty support mask L, lift the map as
\[
(L,w)\longmapsto(L,\iota_Zw),
\]
with τ↦τ. It remains injective, retains its labelled zero, and commutes with the identity transports among the primary nonempty H¹ fibres. The target is the all-support realization-kernel fibre, not an identification with external absence.

Neither this free raw submodule nor the balancing calculation proves that the global balanced kernel is nonzero or zero. They prove the exact raw obstruction and the exact repair of its exhibited operator relation. The surviving full map is
\[
\mathcal O\otimes_{E[t]}Q\longrightarrow\mathcal O/(g),
\]
together with its actual kernel and the original strong-Schwartz/quotient topology. It must be connected through the original Aτ and Kτ; the present calculations have made no replacement of those objects.

## 5. Source pins and transcript locators

The complete primary source was read: Tau_Base_Cohomology_2026-09-12/NOTE.md, SHA-256 d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3. The canonical route was read completely, SHA-256 a8cdd18817a2c3596778c60a04ef9d76125a03ae5404759835a2bc2b18fa4c74.

The all-order calculation answers A1361 (node c9e551ee-298f-438b-9bdc-2e23c2c0613a), §1, and A1427 (node d7e752ce-cb39-4130-b089-b20333037990), §4, while retaining A1304's actual two-leg source. The smooth section retains A1167 (node 157eecdf-7f96-4ec5-96bd-6dd376276ea6), §5, with its original measure, factorials, and full jet orders. These are exact transcript UUID locators; line endings of the readable extraction were repaired during the audit without changing message text.

These are written proofs. No Lean session, remote write, numerical zero computation, or independently rerun historical checker is claimed.

