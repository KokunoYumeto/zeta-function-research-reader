# The exact quotient triangle of the complete supported comparison

24 September 2026. Independent proof SCT0–SCT6.

## SCT0. Relation to existing proofs and source scope

[UOS5–UOS7](GLOBAL_UNIT_ORBIT_AND_SUPPORTED_COMPARISON.md) already constructs the complete map \(\mathcal J:K_\zeta\to\mathcal L_\zeta\), both cones, their cohomology and the companion mirror. [ORE8](ORIGINAL_RESTRICTION_EXTENSION_AND_DELIGNE_CROSS.md) computes the full cyclic derived-Hom map. This appendix constructs the degreewise quotient of that existing map, its exact triangle, and an explicit contraction of its cone. It then identifies the entire connecting sequence after the cyclic resolution. These are further consequences of the retained maps, not a new definition of the coefficient geometry.

The original restrictions are due to Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The exact original-space image is proved in [OMS](ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md), using the framework of Ralf Meyer, [arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3). The geometric lifting argument is Pierre Deligne, [*La conjecture de Weil. II*, §§3.6.1–3.6.3](https://www.numdam.org/item/PMIHES_1980__52__137_0/); its retained French transcription and exact reading coverage are recorded in ORE0. Its geometric weight bounds are not assumed for this receiving calculation.

The current corpus, original \(Z_0,Z_1/\tau,Z_2\) notation, and operation prerequisites remain those of ORE0–ORE1 and CORPUS_AND_OPERATION_RULES.md (private construction record; not included). No addition, parity or numerical weight is assigned to primitive \(\tau\). All calculations below take place on the constructed complex receiving coefficient spaces.

## SCT1. The degreewise quotient and original signs

Keep the original complete terms
\[
P=V_+\oplus V_-\oplus V_{\rm extra},\quad
V_\pm=S\oplus\mathbb C^2,\quad
\widetilde A=\chi_{\rm dil}\otimes A',\quad
Y=\chi_{\rm dil}\otimes Q',\quad\chi_{\rm dil}(a)=a.
\]
The spaces, topologies and transforms are ORE1's original spaces. The actual restrictions are
\[
\Sigma h(u)=2\sum_{n\ge1}h(nu),\qquad
Rb(u)=u^{-1}b(u^{-1}),\qquad
r_+(h,c)=\Sigma h,\quad r_-(h,d)=R\Sigma h=\Sigma\widehat h.
\tag{SCT1.1}
\]
Put \(d(v_+,v_-,w)=r_+v_+-r_-v_-\) and \(\Psi=\pi'D_\zeta\pi\), with the original residue map. In degrees \(-1,0,1,2\), the existing complexes are
\[
K_\zeta=[P\xrightarrow{-d}A\xrightarrow{\Psi}
\widetilde A\xrightarrow{d'}\chi_{\rm dil}P'],
\]
\[
\mathcal L_\zeta=[P\xrightarrow{-d}A\xrightarrow{(\Psi,-\Psi)}
\widetilde A^2\xrightarrow{d_Z'}\chi_{\rm dil}P'].
\tag{SCT1.2}
\]
The complete final differentials are
\[
d'\alpha=(\Sigma'\alpha,0,0,-\Sigma'R'\alpha,0,0,0_{\rm extra}),
\]
\[
d_Z'(\alpha_+,\alpha_-)
=(\Sigma'\alpha_+,0,0,\Sigma'R'\alpha_-,0,0,0_{\rm extra}).
\tag{SCT1.3}
\]
The injection \(\mathcal J\) is identity in degrees \(-1,0,2\), and \(\mathcal J^1\alpha=(\alpha,-\alpha)\).

Let \(B=\widetilde A[-1]\), meaning that \(\widetilde A\) is in cochain degree1 with zero differential. Define
\[
\nu^1(\alpha_+,\alpha_-)=\alpha_++\alpha_-,
\qquad \nu^n=0\quad(n\ne1).
\tag{SCT1.4}
\]
This is a cochain map because it kills \((\Psi b,-\Psi b)\). Its degree-one kernel is precisely the anti-diagonal, its other kernels are the complete terms, and its degree-one map is onto. Thus
\[
\boxed{0\to K_\zeta\xrightarrow{\mathcal J}\mathcal L_\zeta
\xrightarrow{\nu}\widetilde A[-1]\to0}
\tag{SCT1.5}
\]
is degreewise exact. It is continuously split as a sequence of graded vector spaces by
\[
\sigma^1\alpha=(\alpha/2,\alpha/2).
\tag{SCT1.6}
\]
This graded section is not silently declared to be a cochain section.

## SCT2. The connecting cochain and explicit contraction

The failure of \(\sigma\) to commute with the differential is the precise cochain
\[
\boxed{\theta^1\alpha
=\left(\frac{\Sigma'\alpha}{2},0,0,
\frac{\Sigma'R'\alpha}{2},0,0,0_{\rm extra}\right)
\in K_\zeta^2.}
\tag{SCT2.1}
\]
It defines \(\theta:B\to K_\zeta[1]\), and \(d_{\mathcal L}\sigma=\mathcal J\theta\). Since \(d_B=0\) and \(K^3=0\), the cochain identity into the shifted complex holds.

The exact graded decomposition \(\mathcal L_\zeta\simeq K_\zeta\oplus B\) in degree1 is
\[
(\alpha_+,\alpha_-)\longmapsto
\left(\frac{\alpha_+-\alpha_-}{2},\alpha_++\alpha_-\right).
\tag{SCT2.2}
\]
Its inverse is \((k,b)\mapsto(k+b/2,-k+b/2)\); in other degrees use identity on the \(K_\zeta\) term. Substitution in every differential gives
\[
d_{\mathcal L}(k,b)=(d_Kk+\theta b,0).
\tag{SCT2.3}
\]
Hence the actual exact triangle is
\[
\boxed{K_\zeta\xrightarrow{\mathcal J}\mathcal L_\zeta
\xrightarrow{\nu}\widetilde A[-1]\xrightarrow{\theta}K_\zeta[1].}
\tag{SCT2.4}
\]

For completeness this has a full cochain contraction. With the existing cone convention,
\[
\operatorname{Cone}(\mathcal J)^n=\mathcal L_\zeta^n\oplus K_\zeta^{n+1},
\quad d(\ell,k)=(d_{\mathcal L}\ell+\mathcal Jk,-d_Kk),
\]
define
\[
\mathfrak p(\ell,k)=\nu\ell,\qquad
\mathfrak i(b)=(\sigma b,-\theta b).
\tag{SCT2.5}
\]
Both are cochain maps and \(\mathfrak p\mathfrak i=\mathrm{id}_B\). Their signs follow directly from \(d_{\mathcal L}\sigma=\mathcal J\theta\) and \(d_K\theta=0\).
Set
\[
\mathfrak h(\ell,k)=
\left(0,\mathcal J^{-1}(\ell-\sigma\nu\ell)\right)
\in\operatorname{Cone}(\mathcal J)^{n-1}.
\tag{SCT2.6}
\]
The inverse is used only on the image of \(\mathcal J\); SCT1.5 proves that the parenthesis lies there. Write \(a=\mathcal J^{-1}(\ell-\sigma\nu\ell)\). Then
\(d_{\mathcal L}\ell=\mathcal Jd_Ka+\mathcal J\theta\nu\ell\), so
\[
d\mathfrak h(\ell,k)=(\ell-\sigma\nu\ell,-d_Ka),\qquad
\mathfrak h d(\ell,k)=(0,d_Ka+\theta\nu\ell+k).
\]
Adding gives
\[
\boxed{d\mathfrak h+\mathfrak h d
=\mathrm{id}-\mathfrak i\mathfrak p.}
\tag{SCT2.7}
\]
Every map is continuous on the original coefficient spaces. Thus the full cone of \(\mathcal J\) deformation-retracts onto \(\widetilde A[-1]\). Only the explicit identity-cone kernel is contracted; no retained \(H,H'\) or extra coefficient term was removed by assumption.

## SCT3. Complete ordinary cohomology and the original factor2

The existing cohomology is
\[
H^{-1}K_\zeta=H^{-1}\mathcal L_\zeta=H,\quad
H^0K_\zeta=H^0\mathcal L_\zeta=0,
\]
\[
H^1K_\zeta=C_\zeta,\quad H^1\mathcal L_\zeta=C_\zeta\oplus Y,
\quad H^2K_\zeta=\chi_{\rm dil}H',
\quad H^2\mathcal L_\zeta=\chi_{\rm dil}E'.
\]
Here \(H\) is the complete Fourier graph including four endpoint lines and both full extra closed copies, and \(E=\mathbb C^4\oplus V_{\rm extra}\).

UOS identifies the degree-one cycle \((\pi'\lambda_+,\pi'\lambda_-)\) with
\[
(c,\mu)=\left(
\left[\frac{\lambda_+-\lambda_-}{2}\right],
\frac{\lambda_++\lambda_-}{2}\right).
\]
Therefore
\[
\boxed{H^1\nu(c,\mu)=2\pi'\mu.}
\tag{SCT3.1}
\]
The factor2 follows from the specified half-sum, with no change of coordinates.

For \(\alpha\in H^1(B)=\widetilde A\), restrict \(\theta\alpha\) to the actual Fourier graph \(((h,c),(\widehat h,d),w)\). Its Schwartz value is
\[
\frac12(\Sigma'\alpha)(h)
+\frac12(\Sigma'R'\alpha)(\widehat h)
=\frac12\alpha(\Sigma h)+\frac12\alpha(R\Sigma\widehat h)
=\alpha(\Sigma h).
\]
The equality \(R\Sigma\widehat h=\Sigma h\) uses the original Fourier and \(R\) conventions. Thus the connecting map is
\[
\partial^1\alpha=(\Sigma'\alpha,0_{\rm endpoints},0_{\rm extra})
\in\chi_{\rm dil}H'.
\tag{SCT3.2}
\]
The entire nontrivial part of the cohomology sequence is
\[
\boxed{
0\to C_\zeta\xrightarrow{c\mapsto(c,0)}C_\zeta\oplus Y
\xrightarrow{(c,\mu)\mapsto2\pi'\mu}\widetilde A
\xrightarrow{\Sigma'\ {\rm in\ the}\ S'\ {\rm coordinate}}
\chi_{\rm dil}H'\xrightarrow{\iota'}\chi_{\rm dil}E'\to0.}
\tag{SCT3.3}
\]
The degree-\(-1\) map is identity on \(H\); degree0 is zero; all other terms vanish. Directly, \(\ker\Sigma'=\pi'Y\), its image is the complete \(S'\) coordinate, and \(\iota'\) removes that coordinate while retaining every endpoint and extra functional. This verifies exactness independently of the triangle formalism.

## SCT4. The whole sequence after the cyclic resolution

Let \(\mathcal R=\mathbb C[X]\), acting by the actual generator, and \(V_q=\mathcal R/(q)\), \(q\ne0\). Use the explicit free resolution \(\mathcal R\xrightarrow q\mathcal R\to V_q\to0\). For a complex \(K\), its Hom complex is
\[
\mathscr H^n(K)=K^n\oplus K^{n-1},\qquad
\partial^n(u,v)=(d_Ku,d_Kv-(-1)^nq(G_K)u).
\tag{SCT4.1}
\]
Applying this to SCT1.5 is degreewise exact, because each Hom term is the direct sum of two original degreewise exact rows. No analytic derived-category assertion is used.

For \(B\), the Hom complex is precisely
\[
\widetilde A\xrightarrow{+q(G_A)}\widetilde A
\quad\hbox{in degrees }1,2.
\tag{SCT4.2}
\]
The sign is positive since \(-(-1)^1=+1\). ORE3 proves \(q(G_A)\) onto on the actual continuous dual by closed polynomial division on the original test space followed by Hahn–Banach. Consequently
\[
H^1\mathscr H(B)=\ker q_A,\qquad
H^n\mathscr H(B)=0\quad(n\ne1).
\tag{SCT4.3}
\]

Using the full cohomology proved in ORE8, the resulting middle exact sequence is
\[
\boxed{
\begin{aligned}
0\longrightarrow\ker q_Y
&\xrightarrow{\,2\pi'\,}\ker q_A
\xrightarrow{\gamma\mapsto(\Sigma'\gamma,0)}
\ker(q:\chi_{\rm dil}H'\to\chi_{\rm dil}H')\\
&\xrightarrow{(\eta,e)\mapsto(-\delta_q(\eta)/2,e)}
Y/q_Y Y\oplus\ker(q:\chi_{\rm dil}E'\to\chi_{\rm dil}E')
\longrightarrow0 .
\end{aligned}}
\tag{SCT4.4}
\]
Here \(\delta_q\) is the original restriction connecting class of ORE2, and
\(\chi_{\rm dil}H'=\widetilde S\oplus\chi_{\rm dil}E'\).

Check the first two arrows directly. A \(q\)-annihilated \(y\in Y\) has representative \(((\pi'y,\pi'y),0)\) in \(\mathscr H^1(\mathcal L_\zeta)\); its quotient is \(2\pi'y\). For \(\gamma\in\ker q_A\), lift it by \((\sigma\gamma,0)\). Its differential is
\((\mathcal J\theta\gamma,q\sigma\gamma)=(\mathcal J\theta\gamma,0)\), because \(\sigma\) commutes with \(q\). Hence its connecting class is \((\theta\gamma,0)\), which restricts to \((\Sigma'\gamma,0)\) by SCT3.2. The next map is ORE8.8. Its sign can be checked anew: extending \(\eta\) on the plus chart and subtracting the Hom boundary of \(((\alpha,0),0)\), where \(\Sigma'\alpha=\eta\), leaves the degree-one cycle \((-q\alpha,0)\); its half-sum gives \(-\delta_q(\eta)/2\). The \(C_\zeta/qC_\zeta\) component is zero by the actual polynomial inverse; the \(Y/qY\) component remains.

Thus the \(S'\) part of SCT4.4 is the original exact cyclic restriction sequence, with the factors2 and \(-1/2\) required by these cone coordinates. It retains all multiplicity information in its original target \(Y/qY\).

For completeness the other degrees are identity on
\(\ker(q:H\to H)\) in degree\(-1\), identity on \(H/qH\) in degree0, and in degree3 the map
\[
(\chi_{\rm dil}H')/q(\chi_{\rm dil}H')
\xrightarrow{\iota'}
(\chi_{\rm dil}E')/q(\chi_{\rm dil}E').
\tag{SCT4.5}
\]
The latter is an isomorphism because \(q\) is onto on the complementary \(\widetilde S\) coordinate by ORE3.1. All further groups vanish. This states the complete long exact sequence, not only its finite spectral portion.

## SCT5. The original-zeta value in this single triangle

At an actual nontrivial zero \(\rho\) of its full order \(m\), set
\(b=1-\rho\), \(q=(X-b)^r\), \(t=L_Q-b\). For the raw original source Mellin derivatives \(S_j\), \(0\le j<r\), ORE4–ORE5 gives
\[
(D_\zeta\bmod q)^{-1}\delta_q(S_j)
=\left[
\frac{(-1)^j j!}{2}\,t^{r-1-j}
\pi^{b+t-1/2}
\frac{\Gamma((1-b-t)/2)}{\Gamma((b+t)/2)}
\right]_{\mathbb C[t]/(t^{\min(m,r)})}.
\tag{SCT5.1}
\]
ORE4's repaired proof establishes independence directly on compact source tests of integral zero, including that constraint before using these characters.

The fourth arrow of SCT4.4 therefore sends
\[
\boxed{
(S_j,0)\longmapsto
\left(
\left[
\frac{(-1)^{j+1}j!}{4}\,t^{r-1-j}
\pi^{b+t-1/2}
\frac{\Gamma((1-b-t)/2)}{\Gamma((b+t)/2)}
\right],0\right).}
\tag{SCT5.2}
\]
The first factor \(1/2\) is the original factor2 in \(\Sigma\); the second is the actual supported half-sum. The Gamma ratio is holomorphic and nonzero at \(b\). Every derivative below the stated quotient order is retained, and the map has rank \(\min(m,r)\) on this source character space. Neither \(\rho\), its multiplicity, the reflected parameter, the factorial, signs, powers of \(\pi\), nor Gamma arguments have been replaced by a completed arithmetic function.

## SCT6. Actions, mirror, support labels and scope

All maps commute with the original real and prime actions: every dual term carries the same uniform twist, and sum, difference, the specified scalar factors, restrictions and \(\Psi\) are equivariant. This also makes the graded section, connecting cochain and contraction equivariant. All receiving-ring actions remain, including identity components on the faithful extra closed copies.

The exact companion mirror on \(\mathcal L_\zeta^1\) is
\[
(\alpha_+,\alpha_-)\longmapsto(-R'\alpha_-,-R'\alpha_+).
\]
The full sum gives the quotient mirror \(-R'\) on \(B\). The symmetric section intertwines these mirrors, since its two transformed entries are both \(-R'\alpha/2\). The connecting cochain and contraction inherit compatibility from their displayed formulas and the existing companion cochain map. On the cyclic resolution the mirror transports \(q(X)\) to \(q(1-X)\), because it conjugates the generator to \(1-G\); the polynomial is not held fixed unless it has that symmetry. The original and reflected residue denominators remain companions; no self-mirror pairing is assumed.

Every receiving linear map has the exact existing label-preserving lift
\((v,\lambda)\mapsto(f(v),\lambda)\). A nontop input has zero amplitude and keeps its support label; a nonzero output retains top support. The linear identities, compositions and homotopy equations hold on the corresponding fixed labelled receiving fibres, including their supported zero; primitive \(\tau\) is not identified with that zero. Independently labelled factors remain separate.

This one quotient triangle makes the prior \(-\delta_q/2\) placement part of a coherent complete exact sequence. Its quotient is the entire original dual overlap space \(\chi_{\rm dil}A'\) in degree1. The ordinary cohomology has the exact factor2 map into that space, while the cyclic sequence retains the original extension in \(Y/qY\). The separate residue pushout sends its image to \(C_\zeta/qC_\zeta=0\), as [RPC and its independent check](ACTUAL_RESIDUE_PUSHOUT_INDEPENDENT_CHECK.md) prove. The two targets are not identified, and their exact quotient relation is not converted into a numerical purity claim.
