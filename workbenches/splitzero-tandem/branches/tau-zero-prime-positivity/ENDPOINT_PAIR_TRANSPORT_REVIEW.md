# Independent mathematical review of the endpoint-pair transport

This review covers EPM1–47 in `ENDPOINT_PAIR_TRANSPORT_AND_WEIL_MATRIX.md`, the complete incoming ER1–40a in `endpoint_receiver_intake_20260923/ENDPOINT_RESONANCE_AND_PRIME_CLASS.tex`, and ERD1–39 in `ENDPOINT_RESONANT_ZERO_DETECTION.md`. The already reviewed OZG20–27 supplies a comparison for the finite-cutoff Gamma calculation, which is also checked directly here. AP's enclosure \(50<q_c<64\) is retained at its quoted source scope. This review does not rerun or claim an independent numerical audit of AP.

The transport, quotient, entire-matrix and index arguments check. Two receiving details were reported to the author: the Taylor translation kernel uses the negative source shifts, as proved below; and the curvature/endpoint sums in EPM43 must display multiplicity weights under EPM's convention that \(\rho\) denotes distinct zeros. The latter restores the literal formula from ERD, where the zeros were already counted with multiplicity. Both repairs were made by the author and verified directly in the controlling source, SHA256 `09e7f87f60b85dc976d6771f2349e6bfcf87a2d9adf25adab689a966d08b0cdb`. Neither changes the bound or the proposed receiver. The reviewed scope is EPM1–47; later additions require their own reading.

## 1. Gaussian and endpoint identities

Let \(w=s-1/2\), \(P(w)=w^2-1/4\), and retain the full product
\(\mathcal Q(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\).
The original formula has factor \(16\), so \(H_0(z)=\mathcal Q(1/2+iz/2)/16\). Gaussian integration, with both exponentials of the original cosine, gives
\[
\int_{\mathbb R}e^{-x^2/(4t)-wx}\cos(ux)\,dx
=2\sqrt{\pi t}\,e^{tw^2-tu^2}\cos(2twu).
\tag{EPR1}
\]
The \(e^{tu^2}\) in the original source cancels the displayed \(e^{-tu^2}\) only within this exact integral identity. The theta density has every positive Gaussian moment, and the outer Gaussian controls \(e^{|\Re w||x|}\), proving Fubini on each compact set of \(w\). Thus the unmodulated transform is \(2\sqrt{\pi t}e^{tw^2}H_0(2tw)\).

For \(h_+=h_c+ih_s=e^{-x^2/(4t)+ix/(2t)}H_t\), replace \(w\) by \(w-i/(2t)\); for \(h_-=h_c-ih_s\), use \(w+i/(2t)\). Consequently
\[
\begin{split}
M_c+iM_s&=\frac{\sqrt{\pi t}}8
e^{tw^2-1/(4t)-iw}\mathcal Q(1+itw),\\
M_c-iM_s&=\frac{\sqrt{\pi t}}8
e^{tw^2-1/(4t)+iw}\mathcal Q(itw).
\end{split}\tag{EPR2}
\]
This independently fixes both endpoint arguments, both signs of \(iw\), and the factor \(1/8\). Averaging the two rows recovers the incoming ER cosine formula with factor \(1/16\).

The product \(\mathcal Q\) is entire and has precisely the original nontrivial zeros, with multiplicities. At a trivial zero its Gamma pole multiplies the original simple zero through the complete unit of EPM3; at 1 the full factors in EPM4 give the value 1; at 0 the value is also 1. The boundary zero-free argument EPM5 keeps the original pole at 1 and proves strict strip containment. Hence simultaneous vanishing in (EPR2) would place \(itw\) and \(1+itw\) in the same open strip of width one, impossible. The two unfiltered transforms have no common zero. After multiplying by the retained polynomial \(P\), their common zero set is exactly \(\{0,1\}\), with minimum multiplicity one at each point. This proves EPM8–9 on the whole complex plane for every fixed \(t>0\).

The source recovery EPM10 follows by the pointwise identity \(\cos^2+\sin^2=1\) and is an inverse on the specified image. Multiplication by the growing Gaussian is not asserted to be continuous on arbitrary Schwartz pairs. The independent filter inverse is \(-e^{-|x|/2}*f\): its derivative jump is \(+1\), so its image under \(D^2-1/4\) is \(\delta_0\). Moving derivatives to a Schwartz input and using all polynomially weighted \(L^1\) moments of the exponential kernel proves continuity on Schwartz space. The homogeneous solutions have no nonzero Schwartz member. Thus EPM11 is a genuine two-sided inverse on that domain.

## 2. Every sign in the coupled transport

Write \(g_\pm=e^{a_\pm}\), with
\(a_\pm=-x^2/(4t)\pm ix/(2t)\). The original integral gives \(\partial_tH_t=-\partial_x^2H_t\). For \(h_\pm=g_\pm H_t\), the product rule yields
\[
\partial_th_\pm=-h_{\pm,xx}+2a_{\pm,x}h_{\pm,x}
 +(a_{\pm,t}+a_{\pm,xx}-a_{\pm,x}^2)h_\pm,
\tag{EPR3}
\]
where
\[
2a_{\pm,x}=-x/t\pm i/t,\qquad
a_{\pm,t}+a_{\pm,xx}-a_{\pm,x}^2
=1/(4t^2)-1/(2t).
\tag{EPR4}
\]
The mixed imaginary terms cancel in the scalar coefficient. Under \((h_c,h_s)\mapsto h_c+ih_s\), the specified matrix
\(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\)
acts as multiplication by \(i\). Thus the cross term in the real vector PDE is **\(+J\partial_x/t\)**, exactly EPM14. In coordinates its first component is \(-h_{s,x}/t\), its second \(+h_{c,x}/t\). Each has the required parity.

For the bilateral transform, integration by parts and differentiation under the integral give
\(M(Dh)=wM\) and \(M(xDh)=-M-wM_w\). The drift contributes \(+M/t+(w/t)M_w\), converting the scalar coefficient \(-1/(2t)\) to \(+1/(2t)\). Therefore
\[
\partial_t\mathbf M=\frac wt\mathbf M_w+
\left(-w^2+\frac1{2t}+\frac1{4t^2}\right)\mathbf M
+\frac wtJ\mathbf M.
\tag{EPR5}
\]
Multiplication by \(P(w)\) gives \(P\mathbf M_w=\mathbf F_w-(P'/P)\mathbf F\). Hence the additional term in the filtered equation is
\(-wP'/(tP)=-2w^2/(t(w^2-1/4))\), with the minus sign of EPM16. At the two polynomial zeros the original identity \(\mathbf F=P\mathbf M\) supplies its exact germ; assigning a scalar inverse of \(P\) at those points would be a different, undefined operation.

Along the characteristics \(tw=t_0w_0\), the two \(\mathcal Q\) arguments in (EPR2) stay fixed. The common scalar ratio is
\[
\sqrt{t/t_0}\exp\left(tw^2-t_0w_0^2-\frac1{4t}+\frac1{4t_0}\right).
\tag{EPR6}
\]
The plus chiral component acquires \(e^{i(w_0-w)}\), the minus component its reciprocal. Recombining gives **\(R(w_0-w)\)**, rather than the reverse rotation. The scalar ratio is nowhere zero, the rotation has determinant one, and the argument scaling is invertible. Swapping \(t,t_0\) gives their explicit inverse. This proves EPM18 on \(\mathcal O(\mathbb C)^2\). Conjugating by multiplication by \(P\) proves its second statement on \(P\mathcal O(\mathbb C)^2\), with the full quotient germ at every exceptional point. The map also preserves the actual even/odd subspace: its scalar multiplier is even in \(w\), the diagonal rotation entries are even, and the off-diagonal entries odd. No unrestricted Schwartz-space transport is inferred from the entire-function isomorphism.

## 3. Exact extension of the even prime quotient

ER29 starts with the even Schwartz space. EPM20 does not insert an odd source into that old domain: it first defines \(H^{\rm all}=H^{\rm ev}\oplus H^{\rm odd}\) and its moment map \(\mu(h)=(h(0),\int h)\). Both moments vanish on the odd summand. The explicitly given even \(b_0,b_1\) have moments \((1,0),(0,1)\), so they supply the stated direct decomposition.

As algebraic \(R_0\)-modules one obtains
\[
M_0^{\rm all}=(R_0\otimes H_0^{\rm ev})\oplus
(R_0\otimes H^{\rm odd})\oplus(I\otimes\mathbb C^2),
\]
\[
IM_0^{\rm all}=(I\otimes H_0^{\rm ev})\oplus
(I\otimes H^{\rm odd})\oplus(I^2\otimes\mathbb C^2).
\tag{EPR7}
\]
Taking the quotient proves the three summands in EPM20. The even and odd projections preserve these submodules and descend, giving the asserted split inclusion and complementary projection. No topological tensor completion or additional norm enters this calculation.

The identity for \(t_{ab}-1\) and prime factorization give \(I/I^2\cong\bigoplus_p\mathbb C\ell_p\), with inverse detected by the valuations. The source moments of the cosine filter are
\[
\mu(f_c)=\left(H_t''(0)-
\left(\frac1{2t}+\frac1{4t^2}+\frac14\right)H_t(0),
-\frac{\sqrt{\pi t}}{32}e^{-1/(4t)}\right).
\tag{EPR8}
\]
The first coordinate comes from differentiating the Gaussian and cosine twice at zero, including both their second derivatives. The second is \(-1/4\) times \(M_c(t,1/2)\), since the integral of \(h_c''\) is zero. Equation (EPR2) evaluates \(M_c(t,1/2)=\sqrt{\pi t}e^{-1/(4t)}/8\). This verifies EPM21 exactly. The odd filter has both moments zero, so \(1\otimes f_s\in M_0^{\rm all}\) and \((t_p-1)\otimes f_s\in IM_0^{\rm all}\). Its constant group component remains \(f_s\ne0\) in the odd quotient summand, because \(h_s\ne0\) and the filter is injective. These are compatible, different receiving maps.

At \(t=1/32\), the scalar coefficient in the first moment is \(16+256+1/4=1089/4\), verifying the constants in EPM40 independently of AP's separate pairing enclosure.

## 4. Reflected matrix and the exact translation orientation

Real parity gives
\(\overline{F_i(1-\bar s)}=\eta_iF_i(s)\), with \(\eta_c=1\), \(\eta_s=-1\). The transformed real translate \((f_i)_a(x)=f_i(x-a)\) is \(e^{-aw}F_i(s)\), whereas reflection of that first slot contributes \(e^{aw}\eta_iF_i(s)\). Therefore the exact two-translate identity is
\[
B((f_i)_a,(f_j)_b)=K_{ij}(a-b),\qquad
K_{ij}(b-a)=B((f_i)_{-a},(f_j)_{-b}).
\tag{EPR9}
\]
This is the orientation dictionary required when passing from EPM23 to its Taylor kernel EPM37. In particular EPM35 is the Gram block for the two source shifts \(0,-a\). Using shifts \(0,a\) instead gives its block-transposed orientation \(K(-a),K(a)\). Both are valid full translation tests, related by the explicitly stated sign change of the parameter.

The reflected product is \(\eta_iF_iF_j\), so the cross sector has its retained sign and is not an absolute square off the line. Changing the summation variable first by conjugation and then by \(\rho\mapsto1-\rho\) gives
\[
K_{ij}(a)\in\mathbb R\ (a\in\mathbb R),\qquad
K_{ji}(a)=\eta_i\eta_jK_{ij}(a)=K_{ij}(-a).
\tag{EPR10}
\]
Thus the cosine-sine entry is odd, not identically zero. Only its value at zero vanishes.

The height estimate EPM24 is valid. The source sum is bounded by
\(D e^{9u}e^{-\pi e^{4u}}\); one half of the last exponential has integral at most \(e^{-\pi/2}/(2\pi)\), because \(e^{4u}\ge1+4u\). Maximizing the other factor gives the displayed \(O(b\log(b+11))\) exponent. In EPM8 this is dominated by half of the original negative Gaussian \(-t|\Im w|^2\), including the linear phase magnitude and polynomial filter. This proves EPM25 uniformly on every fixed real strip. The zero count then yields normal convergence of every entry and every translation derivative on complex compact sets.

The Laplace transform has the rank-one residue
\(m_\rho(F_c(\rho),-F_s(\rho))^{\mathsf T}(F_c(\rho),F_s(\rho))\), nonzero by joint nonvanishing. Entrywise boundedness makes the Laplace matrix holomorphic on the positive half-plane; the identity theorem excludes every right off-critical pole, and reflection excludes every left one. Conversely under RH the reflected coefficients are their usual complex conjugates, and Cauchy–Schwarz proves EPM34. A two-by-two scalar principal restriction of EPM35 bounds each matrix entry by its two diagonal values. This verifies both directions of the matrix criterion, without assuming positivity from one diagonal.

Integration by parts gives \(M_{D^jf_i/j!}=w^jF_i/j!\). Reflecting its first slot supplies \((-1)^j\), so EPM36 is the actual Gram coefficient. The entire expansion has kernel \(K(b-a)\), with the negative source shifts (EPR9); square coefficient truncations converge absolutely for every finite translation family. This justifies passage from all coefficient blocks to all required translated blocks.

For the exact index, orthogonality to both polynomial families \(F_i(\rho)P(c_\rho)\) makes the two corresponding entire exponential sums vanish. Their coefficients are absolutely summable by Cauchy–Schwarz and the Gaussian bound. Their Laplace transforms are normally meromorphic; each residue is \(m_\rho\bar u_\rho F_i(\rho)\). Since the two factors do not vanish together, every \(u_\rho\) is zero. Thus the combined polynomial range is dense in the complete original weighted value space, including every critical-line point. The involution supplies one negative direction per distinct exchanged pair, with its original multiplicity in the norm. Projection into its negative spectral subspace gives the upper bound; approximation of each finite negative orthonormal family with column error below \(1/4\) gives the lower bound, since its Gram error is below \(9/16\). Every finite list of polynomials fits in one initial block. This proves EPM39, including an infinite index, and retains the full coefficient tower rather than a single finite block.

## 5. All finite-cutoff original-zeta and Gamma signs

For the entire test \(\mathcal A_{ij,a}\), the argument principle with both lines upward gives the original trace
\[
V_{N,ij}=I_\sigma(\mathcal A j)-I_{b_N}(\mathcal A j)
=K_{ij}+\sum_{m\le N}\mathcal A(-2m)-\mathcal A(1).
\tag{EPR11}
\]
The full local units in EPM3–4 are holomorphic after extracting their signed order terms. Their products with the entire test have no local residue; they still enter the original logarithmic derivatives on both boundary lines. The finite-width separated-height contour argument is justified by EPM25, and never asserts uniformity as the left boundary tends to negative infinity.

Insert the original reflection \(j(s)+j(1-s)=-\kappa(s)-\kappa(1-s)\) on the left edge. The reflected Euler line has positive orientation after both substitutions in the differential and contour direction. Euler inversion gives \(-P_{ij}\), with both legs \(k_{ij}(a\pm\log n)\). A general cross entry is not even, so replacing those legs by a factor two would be invalid. Shifting the Gamma edge to \(1/2\) crosses residues \(-1\) at \(0,-2,\ldots,-2N\). Therefore its original left-edge value is
\[
\mathcal G_{N,ij}=A_{\infty,ij}+\mathcal A(0)+U_{N,ij},\qquad
K_{ij}=\mathcal A(0)+\mathcal A(1)+A_{\infty,ij}-P_{ij}.
\tag{EPR12}
\]
These are all signs in EPM28–30. The full completion contour separately has value \(\mathcal A(1)-U_{N,ij}\). Gaussian source tails give Gaussian convolution bounds and absolute convergence of every prime leg. The central second difference at the Gamma origin has order \(x^2\), and the unequal exponential difference order \(x\), proving local integrability with their stated denominator. These facts justify the translation derivatives too. No independent infinite sum of the raw trivial-zero entries is needed. The indexed increments and the inverse \(K=V_N-U_N+\mathcal A(1)\) preserve them exactly.

The carrier of EPM41 has nonzero amplitudes only at top support. Its linear maps fix each lower zero element, and the pairing takes the meet of input labels. A nonzero output requires two nonzero top-labelled inputs, so this lift lands in the original carrier. Additivity follows from bilinear additivity of amplitudes and distributivity of meet over join; conjugate linearity in the first complex scalar slot remains understood. No differential operator is thereby promoted to a semiring homomorphism. Vanishing endpoint amplitudes retain top label \(e\), while a lower absent input retains its own label, including \(\tau\).

## 6. The new scalar receiving claims EPM43–47

The entire ERD1–39 proof was also read for this extension. Its low-height exclusion follows from the original theta expression
\(\mathcal Q(a)=1+a(a-1)\mathcal J(a)\) and
\(|\mathcal J(a)|<2/21\) on \(0\le\Re a\le1\). When \(|\Im a|\le1\), the perturbation has magnitude below \(4/21\). Outside the strip, the original Euler product and full reflection exclude zeros. Hence every zero used in its product proof has \(|\Im\rho|>1\).

ERD15–17 also supplies a complete genus-one proof with its linear exponential retained. The theta growth and Jensen estimate give square summability. The product quotient has a holomorphic logarithm; selected circles avoiding zero moduli bound its real part by \(O(R^{5/4}\log R)\). Fourier coefficients on those circles force every coefficient of degree at least two to vanish. The derivative at zero then fixes its linear term as \(-\delta\). Thus its differentiated product is legitimate. Under EPM's convention of **distinct** zeros, its resulting exact formulas are
\[
\begin{split}
\left(\frac{\zeta'}\zeta+\frac1s+\frac1{s-1}
-\frac12\log\pi+\frac12\psi_\Gamma(s/2)\right)'
&=-\sum_\rho\frac{m_\rho}{(s-\rho)^2},\\
\sum_\rho\frac{m_\rho}{\rho(1-\rho)}&=2\delta,
\qquad \sum_\rho\frac{m_\rho}{|\Im\rho|^2}\le4\delta.
\end{split}\tag{EPR13}
\]
The literal weights are required in all three sums; ERD's notation had already included them by counting zeros with multiplicity. For \(\rho=\beta+i\gamma\), put \(b=\beta(1-\beta)\), \(x=\gamma^2>1\). Its exact real summand is
\((x+b)/((x+b)^2+x(1-4b))\ge1/(x+1)>1/(2x)\).
The first cross-multiplied difference is \(b(3x+1-b)\ge0\). Summing with the positive multiplicities proves the last estimate of (EPR13).

Consequently logarithmic curvature is bounded by \(4\delta/(1-|v|)^2\) on \(a=u+iv\), \(|v|<1\), uniformly in \(u\). The product has a holomorphic logarithm on this simply connected strip, real on the real axis. The logarithm of \(\mathcal Q(z+1)/\mathcal Q(z)\) has relative imaginary part bounded by \(4\delta |v|/(1-|v|)\), obtained by integrating the curvature first over the unit horizontal segment and then vertically. At \(z=itw\), \(|v|\le t/2\), so the relative phase of the two cosine summands is strictly below
\(1+(8/21)t/(2-t)\le\pi\) for the stated closed time interval. The strict inequality survives its upper endpoint because \(\delta<2/21\). At \(v=0\) both compared terms are positive real. This independently verifies the no-cancellation receiver in EPM43–44. It is uniform in the entire critical strip's height, not a compact-region argument with a height-dependent time.

At \(t=1/32\), this proves \(F(\rho)\ne0\) for every original nontrivial zero. The scalar residue \(m_\rho F(\rho)^2\) is then nonzero at every exponent. The preceding Laplace argument applies to this single cosine entry. Under RH the critical-line transform is real and nonzero, so all its spectral weights are positive. This proves the two directions of EPM45. The diagonal enclosure \(50<q<64\) is imported from AP exactly as stated and was not independently numerically checked here.

For the cosine source, parity gives real even \(K\), and the two original source translates satisfy
\(B(f_a,f_a)=q\),
\(B(f_a,f)=K(a)\),
\(B(f,f_a)=K(-a)=K(a)\).
Expanding the two actual squares yields EPM46, including both signs and the factors two. Hence the two-translate criterion concerns actual tests, not an unrelated scalar bound. Finally the single Gaussian-decaying, nowhere-zero-on-zeros factor \(F\) makes the scalar polynomial range dense by the same entire-transform and residue proof. This gives the scalar index statement EPM47, retaining all multiplicities. It is not a proof of the remaining uniform translation bound.

The review found a complete reconstruction of the stated endpoint transport and its matrix receivers. The literal receiving-notation correction (EPR13) and explicit orientation dictionary (EPR9) are now present in the reviewed source. The review supplies no new RH positivity assertion and no new AP numerical certificate.
