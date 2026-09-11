# Actual adelic comparison: supported sheaves, theta image, and spectral jets

Research continuation, 11 September 2026. This appendix replaces the uniform shifted-L-function example as the starting comparison: its input is the supported arithmetic module sheaf, followed by the actual adelic restriction-and-trace map. It does not assert a completed RH proof, a novelty determination, or an identification of unspecified topological cokernels.

## 1. The arithmetic object and its support

Retain one scalar construction `G(R)=R ⨿ {tau}`, with external additive zero `tau` and supported zero `e_R=0_R`. For an R-module L, use the supported module `L^tau`: supported scalar zero sends a supported vector to `0_L`, while scalar tau sends it to external absence.

For an adele a=(a_f,a_infinity), define

\[
L_a=\{r\in\mathbb Q:a_fr\in\widehat{\mathbb Z}\},\qquad
\xi_a(r)=a_fr,\qquad h_a(r)=a_\infty r.
\]

Here h_a is the map denoted tau_a in Connes–Consani, *On the Jacobian of Spec Z*, arXiv:2602.15941v1; it is not the split scalar tau. The source identifies the framed-divisor objects with the adele-class presentation.

For a nonempty arithmetic open U, use the explicit localized module

\[
L_a(U)=\{r\in\mathbb Q:a_pr\in\mathbb Z_p\text{ for every finite }p\in U\}.
\]

For a finite pointed set X, define supported sections by

\[
\widetilde{\mathcal O}(a)(U)(X)=
\{(r_x)\in(L_a(U)^\tau)^{X\setminus\{*\}}:
\infty\in U\Rightarrow\sum_{x\ne *}|h_a(p(r_x))|\le1\}.
\]

Use the terminal object on the empty open. Pointed-set maps sum over fibres with the split addition. The triangle inequality preserves the bound, and scalar multiplication is compatible because

\[
\sum_{x,y}|h_a(p(b_y r_x))|
=(\sum_y|p(b_y)|)(\sum_x|h_a(p(r_x))|).
\]

Restrictions enlarge the localized coefficient modules. Compatible supported tuples glue. This gives the supported arithmetic module sheaf and its arithmetic projection.

For q in Q^times,

\[
L_{qa}=q^{-1}L_a,\qquad\psi_q:L_{qa}\to L_a,\quad r\mapsto qr,
\]

and

\[
\xi_a\psi_q=\xi_{qa},\qquad h_a\psi_q=h_{qa}.
\]

Extending psi_q by tau -> tau gives the supported sheaf isomorphism. The principal-action groupoid, including its arrows, is retained.

On the earlier extended base i:Y -> Y^+=Y ⨿ {sigma}, with sigma=P_tau, this module sheaf extends with Boolean support stalk and support restriction maps. The arithmetic realization is the typed map

\[
i^{-1}\widetilde{\mathcal O}^{+}(a)\longrightarrow\mathcal O(a).
\]

This is not a claim of a continuous map sending the added generic support point to the zero adele. The support observation and the arithmetic realization are retained together.

## 2. The actual restriction-and-trace comparison

For x in C_Q=A_Q^times/Q^times, set H_x=ell^2(p^{-1}(x)), on its orbit of representatives. For a finite crossed-product sum

\[
a=\sum_{q\in\mathbb Q^\times}f_qU_q,\qquad
U_qfU_q^{-1}(y)=f(q^{-1}y),
\]

define

\[
(\rho_x(a)v)(y)=\sum_q f_q(y)v(q^{-1}y).
\]

Substituting twice proves the representation law. A Bruhat–Schwartz coefficient restricted to this orbit is absolutely summable: the finite-adelic support confines the rational parameter to a fractional lattice, and real Schwartz decay makes the sum converge. Each summand is a trace-class diagonal operator times a permutation. Hence

\[
\boxed{\operatorname{Tr}\rho_x(a)=\sum_{y\in p^{-1}(x)}f_1(y).}
\]

For a multiplication coefficient Phi, this is

\[
\Theta\Phi([g])=\sum_{q\in\mathbb Q^\times}\Phi(qg).
\]

This is the actual degree-zero restriction-and-trace map. Theta is linear; it is not asserted to preserve pointwise multiplication. Its full cyclic extension is a source construction, not newly proved here.

For an idele a, put c_a=product_p p^{-v_p(a_p)}. Then L_a=c_a Z and lambda_a=|a_infinity|c_a=|a|_A. The arithmetic bounded-section count is

\[
N_a(r)=1+2\lfloor r/\lambda_a\rfloor.
\]

Its weighted count is

\[
\int_{(0,\infty)}e^{-\pi u r^2}\,d(N_a(r)-1)
=\sum_{v\in L_a\setminus\{0\}}e^{-\pi u|h_a(v)|^2}.
\]

Thus the theta test is an explicit weighted section-count operation on the arithmetic realization of the supported sheaf. The support lift remains above this observation.

## 3. Both endpoint maps and the test-function topology

Let

\[
V=\{\varphi\in\mathcal S(\mathbb R):\varphi(-x)=\varphi(x),\ 
\varphi(0)=0,\ \int_{\mathbb R}\varphi=0\}.
\]

Use Fourier transform with kernel exp(-2 pi i xy). The two endpoint maps are phi -> (phi(0),hat phi(0)). Embed phi into the adelic coefficients as

\[
\Phi_\varphi(x_f,x_\infty)=\mathbf1_{\widehat{\mathbb Z}}(x_f)\varphi(x_\infty).
\]

At g_t=(1_f,t),

\[
\boxed{\Theta\varphi(t)=\sum_{n\in\mathbb Z\setminus\{0\}}\varphi(nt).}
\]

Before imposing the endpoints, Poisson summation reads

\[
\Theta\varphi(t)=t^{-1}\Theta\widehat\varphi(t^{-1})
+t^{-1}\widehat\varphi(0)-\varphi(0).
\]

Both final terms vanish for phi in V. Define the strong-Schwartz Frechet space T by the seminorms

\[
p_{N,j}(F)=\sup_{t>0}(t^N+t^{-N})|(t\partial_t)^jF(t)|,
\quad N,j\ge0.
\]

Theta:V -> T is continuous. At infinity, differentiate and bound the Schwartz sums; at zero use the displayed Poisson identity for hat phi, which satisfies the same two endpoint equations. Mellin transformation

\[
\mathcal MF(s)=\int_0^\infty F(t)t^s\frac{dt}{t}
\]

is entire and continuous into locally uniform convergence with derivatives. Choose N greater than the spectral real parts on each compact set; additional powers of |log t| control derivatives.

## 4. The actual analytic image is computed

For Re(s)>1, absolute convergence gives

\[
\mathcal M\Theta\varphi(s)=2\zeta(s)M_+\varphi(s),\quad
M_+\varphi(s)=\int_0^\infty\varphi(t)t^s\frac{dt}{t}.
\]

Retain

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad
H_\varphi(s)=\frac{2\pi^{s/2}M_+\varphi(s)}{s(s-1)\Gamma(s/2)}.
\]

**Theorem.** H_phi is entire, and M Theta phi = 2 xi H_phi.

**Proof.** Taylor subtraction continues M_+ phi with possible simple poles at negative even integers. The value condition removes the pole at zero. Reciprocal Gamma cancels the negative-even poles; its simple zero at s=0 cancels the explicit denominator s. The integral condition gives M_+phi(1)=0 and cancels s-1. There are no other possible poles. Analytic continuation extends the identity from Re(s)>1. No division by xi at a zero was assumed.

Set D=x d/dx and

\[
\boxed{\varphi_*=D(D+1)e^{-\pi x^2}
=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}.}
\]

Integration by parts proves phi_* in V and

\[
M_+\varphi_*(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

Consequently H_phi*=1 and M Theta phi*=2xi. Fourier conjugation D -> -(D+1) proves hat phi*=phi_*.

The Gaussian/Hermite multiplier is already in the source programme; it is not counted as a new discovery. Its consequence for the supported analytic comparison is

\[
\boxed{\mathcal I_\Theta=2\xi\mathcal O_{\mathbb C},}
\]

where I_Theta is the sheaf of ideals generated by all M Theta phi. Containment follows from the factorization; the chosen actual input proves equality. Thus

\[
0\to\mathcal O_{\mathbb C}\xrightarrow{\times2\xi}\mathcal O_{\mathbb C}
\to\mathcal D_\xi\to0,
\qquad\mathcal D_\xi=\mathcal O_{\mathbb C}/(2\xi).
\]

This is analytic sheafification of the actual image. No equality of an unspecified topological closure with an algebraic ideal is asserted.

The exact map to the existing workbench coordinates is

\[
\mathcal F_\mu\mathcal E\varphi(z)
=\tfrac12\mathcal M\Theta\varphi(\tfrac12-iz),
\quad
\mathcal E\varphi(t)=t^{1/2}\sum_{n\ge1}\varphi(nt).
\]

For phi_*, it gives xi(1/2-iz)=Xi(z), by the functional equation. Both the factor 1/2 and the Fourier exponent's sign are retained.

## 5. All support labels survive the comparison

Let L be the join-semilattice of finite-dimensional subspaces W of V, with join W+W' and bottom 0. In sheaf-valued linear diagrams on this fixed L, set

\[
\mathcal A_W=\mathcal O\otimes_{\mathbb C}W,
\qquad
\mathcal B_W=\mathcal O\ (W\ne0),\qquad\mathcal B_0=0,
\]

and

\[
\delta_W(\sum_j a_j\otimes\varphi_j)=\sum_j a_j\mathcal M\Theta\varphi_j.
\]

Use inclusion in the source and identity in the nonzero target for W subset W'. The squares commute. Define H^1_W=coker(delta_W) fibrewise. This is the degree-one cohomology sheaf of the two-term sheaf complex, not a claim that global sheaf cohomology of the arithmetic curve has already been computed.

Reconstruct the fixed-support diagram through chapter 14's equivalence. Then

\[
e\cdot(W,h)=(W,0),\qquad\tau\cdot(W,h)=(0,0).
\]

**Cofinal stabilization theorem.** Whenever W contains phi_*, its image ideal is 2xi O, and H^1_W=D_xi. Transport between two such labels is the identity on that amplitude cokernel. Every W lies in W+C phi_*, proving cofinality. The labelled origins remain distinct in the reconstructed diagram.

Dilation sends W to {phi(a dot):phi in W}; Fourier sends W to hat W. These are automorphisms of the same join-semilattice. Their amplitude intertwiners are the actual Mellin/Poisson identities, not new scalar supports.

## 6. Surjective maps from the actual topological quotient to every finite jet family

Define, using the topology in section 3,

\[
Q_\Theta=\mathscr T/\overline{\Theta V}^{\,\mathscr T}.
\]

For h in C_c^infinity(R_+), multiplicative convolution h*phi preserves V and satisfies Theta(h*phi)=h*Theta(phi), by absolute convergence. It acts continuously on T and its quotient; Mellin turns the action into multiplication by M h.

For a finite set Omega of actual zeros of xi, with multiplicities m_rho, define

\[
\boxed{
J_\Omega:Q_\Theta\to\bigoplus_{\rho\in\Omega}\mathbb C[z_\rho]/(z_\rho^{m_\rho}),
\quad
[F]\mapsto\left(\sum_{j<m_\rho}\frac{(\mathcal MF)^{(j)}(\rho)}{j!}z_\rho^j\right)_\rho.
}
\]

Continuity of Mellin jets and the factor 2xi prove that it kills the closed image.

**Theorem.** J_Omega is surjective; every finite set of jets has a representative in C_c^infinity(R_+).

**Proof.** Choose a nonnegative smooth h supported in (-delta,delta), of integral one, with exp(M delta)-1<1/2 for M=max |rho|. Then H(s)=integral h(y)exp(sy)dy satisfies |H(rho)-1|<1/2. For prescribed jets b_rho, the Chinese remainder theorem supplies a polynomial P of degree less than sum m_rho such that P(s)H(s) equals b_rho modulo (s-rho)^m_rho at every point. Use the Taylor inverse of H at each point. Set F(t)=[P(-d/dy)h(y)] at y=log t. Integration by parts gives M F=P H, with every 1/j! in the displayed Taylor map retained.

This proves finite-jet surjectivity. It does not assert unrestricted infinite-jet surjectivity or silently identify different functional-analytic cokernels.

## 7. The previous lattice calculation now has an actual arithmetic input

At an actual zero rho, set R_rho=O_{C,rho}, z_rho=s-rho and

\[
u_\rho(z_\rho)=2\xi(\rho+z_\rho)/z_\rho^{m_\rho},\quad u_\rho(0)\ne0.
\]

The inclusion is

\[
L_Q=(2\xi)R_\rho\hookrightarrow L_P=R_\rho.
\]

Its quotient is (D_xi)_rho, of length m_rho. Its comparison with the coordinate block is the square with horizontal maps times 2xi and times z_rho^m, right vertical identity, and left vertical multiplication by u_rho. The unit is an explicit isomorphism, not discarded.

With omega_rho=R_rho ds,

\[
\operatorname{Ext}^1_{R_\rho}((\mathcal D_\xi)_\rho,\omega_\rho)
\cong(2\xi)^{-1}\omega_\rho/\omega_\rho.
\]

The perfect pairing is ([f],[eta]) -> Res_rho(f eta). Bases z^i and z^{-j-1} dz give delta_ij. All higher jets are retained. The length counts the actual multiplicity; it is not renamed as a horizontal displacement from the critical line.

## 8. Dilation and the genuine arithmetic trace pairing

For a>0, lambda_a F(t)=F(at) preserves the source image and

\[
\mathcal M\lambda_aF(s)=a^{-s}\mathcal MF(s).
\]

On a rho-jet block it acts by multiplication by

\[
a^{-\rho}\sum_{j<m_\rho}\frac{(-\log a)^j}{j!}z_\rho^j.
\]

The generator for a=exp(t) is multiplication by -s.

Define iota(s)=1-bar s and f^dagger(s)=overline{f(1-bar s)}. Since xi^dagger=xi, this acts on the quotient. Its local coefficient map from the iota(rho)-block to the rho-block is

\[
\sum_j a_jz^j\longmapsto\sum_j(-1)^j\bar a_jz^j.
\]

For finite iota-stable Omega put A_Omega=direct sum R_rho/(2xi). The actual multiplication trace is

\[
\operatorname{tr}_\Omega(f)=\sum_\rho m_\rho f(\rho)
=\sum_\rho\operatorname{Res}_{s=\rho}\left(f(s)\frac{\xi'(s)}{\xi(s)}ds\right).
\]

Define Q_Omega(f,g)=tr_Omega(f^dagger g). Its radical is exactly the nilradical. Reduction retains multiplicities as the weights m_rho; the Ext pairing above retains the discarded Taylor directions. These two explicit pairings have different domains and are connected by the reduction map.

The exact identity is

\[
\boxed{\mathcal Q_\Omega(a^{-s}f,a^{-s}g)=a^{-1}\mathcal Q_\Omega(f,g).}
\]

Proof: (a^{-s})^dagger=a^{-(1-s)}, and their product is a^{-1}.

A fixed point rho=1-bar rho has reduced pairing m_rho bar x y. A two-point orbit has matrix

\[
m_\rho\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Thus the functional equation produces the weight-one duality identity on the actual divisor. Positivity is not assumed in deriving it.

For f,g in C_c^infinity(R_+), let f^sharp(t)=t^{-1}overline{f(t^{-1})}, and k=f^sharp*g with multiplicative convolution. Then

\[
\mathcal M(f^\sharp*g)=(\mathcal Mf)^\dagger\mathcal Mg.
\]

The finite trace pairing through J_Omega is precisely the corresponding finite part of the Weil spectral sum. Arbitrarily rapid vertical Mellin decay and the standard O(T log T) zero count give absolute convergence on exhaustion. The imported explicit formula, with its full terms retained, is

\[
\begin{aligned}
\sum_\rho m_\rho\mathcal Mk(\rho)
={}&\mathcal Mk(0)+\mathcal Mk(1)
-\sum_p\log p\sum_{n\ge1}(k(p^n)+p^{-n}k(p^{-n}))\\
&-(\log4\pi+\gamma)k(1)
-\int_1^\infty\frac{k(x)+x^{-1}k(x^{-1})-2x^{-1}k(1)}{x-x^{-1}}dx.
\end{aligned}
\]

The quadratic-input involution contains conjugation; the linear reflected term inside the explicit formula does not.

## 9. All primitive Dirichlet channels and the abelian Dedekind product

For a nonprincipal primitive character chi of conductor q>1 and parity chi(-1)=(-1)^epsilon, define

\[
\Phi_{\chi,\psi}(x_f,x_\infty)=\mathbf1_{\widehat{\mathbb Z}}(x_f)\chi(x_f\bmod q)\psi(x_\infty),
\]

with psi Schwartz of the indicated parity. Both adelic endpoint maps vanish: chi(0)=0 and the finite average of chi is zero. The trace is Theta_{chi,psi}(t)=sum_{n in Z}chi(n)psi(nt). Projection onto the character uses Haar measure of total mass one on hat Z^times and the factor bar chi; its conductor is retained.

For psi_chi(x)=x^epsilon exp(-pi x^2/q), direct Mellin integration gives

\[
\boxed{
\mathcal M\Theta_{\chi,\psi_\chi}(s)
=\Lambda_\chi(s)
=(q/\pi)^{(s+\varepsilon)/2}\Gamma((s+\varepsilon)/2)L(s,\chi).
}
\]

The two signs of the integer sum cancel the 1/2 of the Gaussian integral. For arbitrary parity-matching psi the multiplier is 2L(s,chi)M_+psi. Taylor continuation and reciprocal Gamma show that its quotient by Lambda_chi is entire. The chosen Gaussian makes the quotient one. Hence the full analytic image ideal is Lambda_chi O. All support-diagram, finite-jet, lattice, and residue maps above apply to these actual channels. The local Euler factor at a conductor prime is 1, by chi(p)=0; no ramified factor is silently omitted.

For a finite abelian extension K/Q use the associated primitive characters, including the principal conductor-one character. Put

\[
C_K=\prod_\chi q_\chi^{\varepsilon_\chi/2},\qquad
\Lambda_K(s)=|D_K|^{s/2}\Gamma_{\mathbb R}(s)^{r_1}\Gamma_{\mathbb C}(s)^{r_2}\zeta_K(s),
\]

where Gamma_R(s)=pi^{-s/2}Gamma(s/2) and Gamma_C(s)=2(2pi)^{-s}Gamma(s). The conductor-discriminant relation and Gamma_R(s)Gamma_R(s+1)=Gamma_C(s) give product_chi Lambda_chi=C_K Lambda_K.

Using phi_* in the principal channel and multiplicatively convolving all the theta traces gives

\[
\boxed{(2\xi(s))\prod_{\chi\ne1}\Lambda_\chi(s)=C_Ks(s-1)\Lambda_K(s).}
\]

For Q(i), C_K=2. This covers every primitive rational finite-order character and every finite abelian extension of Q; an arbitrary nonabelian extension is not asserted by replacing notation.

## 10. Relation to the purity calculation and source scope

The previous local-lattice/Ext machinery now has the actual arithmetic multiplication map as an input. The quotient-to-jet map is constructed and surjective for every finite family. The duality relation is calculated on those same arithmetic fibres. This goes beyond a family whose logarithmic derivative was chosen to reproduce zeta.

The full weight/positivity bound remains to be obtained for this arithmetic object. The Chen–Moriwaki one-place casting estimate does not itself identify its filtration with the spectral real-part filtration above. No such identification has been inserted as an assumption disguised as a definition.

Sources read: the preceding authored sheaf and Rees notes; the mounted original globalization; repository chapter 14 (fixed-support diagrams), chapter 15 (existing divisor/jet construction), chapter 17 (existing packet trace); the Connes sidebar TeX lines 1–85 (actual theta multiplier and topology qualification); supplied arXiv:2602.15941v1 `Jacobian.tex`, selected sections on arithmetic sheaves, framed divisors, and trace geometry. The Jacobian TeX was extracted directly from the supplied archive. No OCR or PDF extraction was used for these readings. Abstract/metadata checks for arXiv:math/0703392 and math/0311468 do not constitute a full reading of their TeX.

The explicit formula is the source formula in Connes–Consani–Moscovici, equations (3.1)–(3.4), with all terms displayed above. Finite-order factorization and conductor-discriminant identities are the source inputs in Cogdell. The new proofs here do not count those source theorems as novel results.

This is a draft calculation, not a merged accepted claim. The fuller conversation package includes editable LaTeX, all proofs, exact tests, and separately labelled high-precision theta diagnostics. Third-party source texts and private transcripts are not included in this PR.