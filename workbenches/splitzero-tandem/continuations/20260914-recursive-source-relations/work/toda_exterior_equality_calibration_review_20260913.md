# Independent exact review of the Toda/exterior equality calibration

The final TC.1–13 source is approved after a complete equation-by-equation read and an independent reconstruction from the original monomial source Gram, literal quotient map and multiplication matrix. No mathematical sign or constant correction was required. The source author installed the coordinate, determinant, parity and projector-kernel clarifications identified below.

Reviewed source: `toda_exterior_equality_calibration_20260913.tex`, SHA256 `772e2cd7efef88cd9591d1918b6a1fbcacbede51cbef50d109b33b246a79238f`.

Checker: `toda_exterior_equality_calibration_check_20260913.py`, SHA256 `01e7b815a376ba01ddb10f1969bbf6518cd7afed21e8e714e743e18d1b41b94b`.

The original measure is
\[
d\nu(u)=\frac{\mu}{\sqrt{2\pi}\sigma}e^{-u^2/(2\sigma^2)}du,
\quad \mu,\sigma>0,\quad c=\frac12,\quad S=c+iu,
\quad x=S-c,\quad \chi=x^2-\sigma^2.
\]
The quotient roots are declared coefficients of this calibration. Neither the proof nor the checker identifies them as arithmetic zeros. All calculations retain the full mass \(\mu\), variance \(\sigma^2\), vertical phases and quotient basis changes. No numerical quadrature, selected-zero data, asymptotic bound or Lean execution enters the review.

## TC.1–4: source pairing and coordinate maps

Let \(C=\mathbb C[S]/(\chi)\). In the original quotient basis \((1,S)\), reduction of \(1,x,S,S^2\) gives
\[
L_{\rm coord}=\begin{pmatrix}1&-c\\0&1\end{pmatrix},
\quad A_S=\begin{pmatrix}0&\sigma^2-c^2\\1&2c\end{pmatrix}.
\]
The map \(L_{\rm coord}:\mathbb C^2_{(1,x)}\to\mathbb C^2_{(1,S)}\) sends the coefficient column of each quotient element to the column of the same element. Direct multiplication gives
\[
L_{\rm coord}^{-1}A_SL_{\rm coord}
=A_x=\begin{pmatrix}c&\sigma^2\\1&c\end{pmatrix}.
\]
Thus \(A_x\) represents multiplication by \(S\) in the \((1,x)\) basis. Multiplication by \(x\) is \(A_x-cI\), whose square is \(\sigma^2I\). Every displayed matrix retains the same quotient and generator. The determinant of the coordinate map is one.

Gaussian integration by parts gives \(m_0=\mu\), \(m_{2r+1}=0\) and
\[
m_{2r}=(2r-1)\sigma^2m_{2r-2},
\qquad(m_2,m_4,m_6)=(\mu\sigma^2,3\mu\sigma^4,15\mu\sigma^6).
\]
The boundary term vanishes because every polynomial times the Gaussian tends to zero at both ends of the real line. Applying the original pairing to monic source powers gives
\[
p_0=1,\quad p_1=x,\quad p_2=x^2+\sigma^2,
\quad p_3=x^3+3\sigma^2x.
\]
In particular
\[
p_1(c+iu)=iu,\quad p_2(c+iu)=-(u^2-\sigma^2),
\quad p_3(c+iu)=-i(u^3-3\sigma^2u).
\]
The two potentially nonzero off-diagonal pairings are
\[
\langle1,p_2\rangle=-m_2+\sigma^2m_0=0,
\quad\langle p_1,p_3\rangle=-m_4+3\sigma^2m_2=0;
\]
every other off-diagonal pairing vanishes by odd parity. The squared norms are
\[
\omega_0=\mu,\quad\omega_1=\mu\sigma^2,
\quad\omega_2=m_4-2\sigma^2m_2+\sigma^4m_0=2\mu\sigma^4,
\]
\[
\omega_3=m_6-6\sigma^2m_4+9\sigma^4m_2=6\mu\sigma^6.
\]
Reduction by the original relation \(x^2=\sigma^2\) gives exactly
\[
b_0=(1,0)^{\mathsf T},\quad b_1=(0,1)^{\mathsf T},
\quad b_2=(2\sigma^2,0)^{\mathsf T},\quad b_3=(0,4\sigma^2)^{\mathsf T}.
\]

## TC.5–6: direct source and relation Grams

For each \(N=1,2,3\), the checker first constructs the original source Gram
\[
M_N=(\langle S^r,S^s\rangle)_{0\le r,s\le N}
\]
and the actual quotient map
\[
B_{N,S}:\mathbb C^{N+1}\to\mathbb C^2_{(1,S)},
\qquad z\longmapsto\left[\sum_{j=0}^Nz_jS^j\right]_{\chi}.
\]
It then calculates, without using the claimed answer,
\[
K_{N,S}=B_{N,S}M_N^{-1}B_{N,S}^*,\quad G_{N,S}=K_{N,S}^{-1},
\quad R_{N,S}=M_N^{-1}B_{N,S}^*G_{N,S}.
\]
The first two quotient columns are independent, so \(B_{N,S}\) is onto. The source Gram is positive definite: a nonzero polynomial cannot vanish on a set of positive Gaussian measure on the vertical line. Consequently all inverses displayed here exist. Matrix multiplication proves
\[
B_{N,S}R_{N,S}=I,\qquad R_{N,S}^*M_NR_{N,S}=G_{N,S}.
\]
For \(z\in\ker B_{N,S}\),
\(z^*M_NR_{N,S}=z^*B_{N,S}^*G_{N,S}=0\).
Therefore the displayed right inverse gives the unique minimum source representative by the original Pythagorean identity.

Changing only coefficient columns gives
\[
G_{N,x}=L_{\rm coord}^*G_{N,S}L_{\rm coord},
\qquad K_{N,S}=L_{\rm coord}K_{N,x}L_{\rm coord}^*.
\]
The independent reconstruction agrees with the orthogonal-polynomial sum \(K_{N,x}=\sum_{j\le N}b_jb_j^*/\omega_j\). Its three values are
\[
K_{1,x}=\operatorname{diag}(1/\mu,1/(\mu\sigma^2)),
\quad K_{2,x}=\operatorname{diag}(3/\mu,1/(\mu\sigma^2)),
\]
\[
K_{3,x}=\operatorname{diag}(3/\mu,11/(3\mu\sigma^2)).
\]
Their inverses and determinants prove TC.5 with
\[
(V_1,V_2,V_3)=\mu^2\sigma^2(1,1/3,1/11).
\]
The checker retains every entry of each original \(M_N,B_{N,S},R_{N,S},K_{N,S},G_{N,S}\) in its result JSON.

The original relation on the vertical line is \(\chi(c+iu)=-(u^2+\sigma^2)\). Thus
\[
\nu_0=m_4+2\sigma^2m_2+\sigma^4m_0=6\mu\sigma^4,
\]
\[
\nu_1=m_6+2\sigma^2m_4+\sigma^4m_2=22\mu\sigma^6.
\]
The pairing of \(\chi\) with \(\chi x\) is zero by odd parity. The original relation basis \((\chi,\chi S)\) is obtained from \((\chi,\chi x)\) through the coefficient matrix
\[
T=\begin{pmatrix}1&c\\0&1\end{pmatrix}.
\]
Its full Gram is \(T^*\operatorname{diag}(\nu_0,\nu_1)T\), so the relation determinant remains \(\nu_0\nu_1\). Direct source determinants are
\[
\mathfrak D_2=\mu^2\sigma^2,
\quad\mathfrak D_3=2\mu^3\sigma^6,
\quad\mathfrak D_4=12\mu^4\sigma^{12}.
\]
Division by \(1,\nu_0,\nu_0\nu_1\), respectively, gives the three values of \(V_N\). The empty determinant at \(N=1\) is exactly one. The checker also verifies that the coefficient columns of every relation \(\chi S^j\), \(0\le j\le N-2\), lie in the quotient kernel and are orthogonal to the minimum source image. These columns span the entire kernel by polynomial division and their distinct degrees.

## TC.7 and the zero-tilt phase

The adjoint used throughout is the actual weighted adjoint \(A_x^\sharp=G_{N,x}^{-1}A_x^*G_{N,x}\). At the first two degrees it gives
\[
H_1=\begin{pmatrix}0&2\sigma^2\\2&0\end{pmatrix},
\qquad H_2=\begin{pmatrix}0&4\sigma^2\\4/3&0\end{pmatrix}.
\]
Both satisfy \(G_{N,x}H_N=H_N^*G_{N,x}\); their squares are \(4\sigma^2I\) and \((16\sigma^2/3)I\). In a positive metric, a self-adjoint operator whose square is \(aI\), \(a>0\), has squared norm \(a\): directly \(\|H_Nv\|_G^2=\langle v,H_N^2v\rangle_G=a\|v\|_G^2\) for every vector. This proves the exact radii without any change of metric. Since the two eigenvalues of \(A_x\) are \(c\pm\sigma\), the retained right-half-plane spectral aggregate is \(L_{\rm spec}=2\sigma\).

For the original tilt \(e^{\theta u}d\nu\), completing the square gives the full moment generating function
\[
M(\theta)=\mu e^{\sigma^2\theta^2/2}.
\]
It is finite for every real \(\theta\). Its derivatives give every tilted moment; differentiation under the integral follows by Gaussian domination on each bounded \(\theta\)-interval. The real-coordinate source and relation moment matrices are
\[
H_{rs}(\theta)=M^{(r+s)}(\theta),
\qquad H^\chi_{rs}(\theta)=M^{(r+s+4)}(\theta)
+2\sigma^2M^{(r+s+2)}(\theta)+\sigma^4M^{(r+s)}(\theta).
\]
Reflection \(u\mapsto-u\) proves the diagonal parity congruences stated in the final source. The exact monomial matrix is
\[
C_{rj}=\binom jr c^{j-r}i^r\quad(r\le j),
\qquad S^j=\sum_r C_{rj}u^r.
\]
Thus the source Gram in original \(S\) coordinates is \(C^*H(\theta)C\), and the relation Gram is given by the same congruence in its own dimension. The triangular determinant has modulus one. This proves evenness of both determinants and hence \(\ell_N'(0)=0\). The checker also computes the same derivatives directly as
\[
\operatorname{Tr}(M_N^{-1}M_N')
-\operatorname{Tr}((M_N^{\rm rel})^{-1}(M_N^{\rm rel})'),
\]
with the second summand zero in dimension zero. Each individual trace vanishes. Finally \(\sigma_T=\operatorname{Tr}((A_x-cI)/i)=0\); therefore the complete phase square \((\sigma_T-\ell_N'(0))^2\) is zero. The original rank-two cross pairing \(b_N^*G_{N,x}b_{N+1}/\omega_N\) is also computed directly and vanishes for \(N=1,2\).

## TC.8–10: the exact Toda loss

The original ratios give
\[
\delta_2=\frac13,\quad\delta_3=\frac3{11},\quad
a_3=3\sigma^2,\quad\mathcal R_2=\frac{V_1}{V_3}=11.
\]
Their exact Toda contribution and upper expression are
\[
3\sigma^2\left(1-\frac13\right)\left(\frac{11}3-1\right)
=\frac{16\sigma^2}{3}=\epsilon_2^2,
\]
\[
3\sigma^2\frac{(11-1)^2}{4\cdot11}=\frac{75\sigma^2}{11}.
\]
For the stated positive ratios,
\[
e^t=\sqrt{\delta_2/\delta_3}=\frac{\sqrt{11}}3,
\quad \cosh s=\frac{\sqrt{\mathcal R_2}+1/\sqrt{\mathcal R_2}}2
=\frac6{\sqrt{11}}.
\]
Consequently
\[
a_3(e^t-\cosh s)^2
=3\sigma^2\left(-\frac7{3\sqrt{11}}\right)^2
=\frac{49\sigma^2}{33},
\]
and
\[
\frac{75\sigma^2}{11}-\frac{49\sigma^2}{33}
=\frac{16\sigma^2}{3}.
\]
This checks the sign and every constant in TC.9–10 against the radius reconstructed from the original source Gram.

## TC.11–13: both projectors and the full adjoint products

Let \(G=G_{2,x}\) and \(v_\pm=(\pm\sigma,1)^{\mathsf T}\). Direct multiplication gives \(A_xv_\pm=(c\pm\sigma)v_\pm\),
\[
v_+^*G_{1,x}v_-=0,
\qquad v_+^*Gv_-=\frac{2\mu\sigma^2}{3},
\qquad v_+^*Gv_+=\frac{4\mu\sigma^2}{3}.
\]
Both maps \(P,Q:C\to C\) in TC.12 therefore have image \(\mathbb Cv_+\). The original orthogonal complement is spanned by \(w=(-3\sigma,1)^{\mathsf T}\), since \(v_+^*Gw=0\). Direct multiplication gives \(Pw=0\), \(Qv_-=0\), \(Pv_+=Qv_+=v_+\), and \(Pv_-=v_+/2\). This proves the two exact kernels and all asserted projector properties.

For \(X=Q-P\), the full original adjoint and products are
\[
X=\begin{pmatrix}1/4&-\sigma/4\\1/(4\sigma)&-1/4\end{pmatrix},
\qquad
X^\sharp=G^{-1}X^*G
=\begin{pmatrix}1/4&3\sigma/4\\-1/(12\sigma)&-1/4\end{pmatrix},
\]
\[
X^\sharp X=
\begin{pmatrix}1/4&-\sigma/4\\-1/(12\sigma)&1/12\end{pmatrix}
=\frac13(I-P),
\]
\[
XX^\sharp=
\begin{pmatrix}1/12&\sigma/4\\1/(12\sigma)&1/4\end{pmatrix}
=\frac13P.
\]
Their trace proves \(\|X\|_{\rm HS,G}^2=1/3\). Conjugating \(P,Q,X\) by \(L_{\rm coord}\) and transporting \(G\) by the stated inverse congruence preserves this trace, by cancellation of adjacent inverse matrices. The checker verifies this using the independently reconstructed original \(G_{2,S}\). Hence
\[
\epsilon_2^2-L_{\rm spec}^2
=\frac{16\sigma^2}3-4\sigma^2
=\frac{4\sigma^2}3
=L_{\rm spec}^2\|Q-P\|_{\rm HS,G}^2.
\]
The exterior projector discrepancy and the Toda imbalance retain their separate, explicitly calculated maps and values. Neither is replaced by the other.

## Independent execution and deliberate controls

All 161 exact comparisons pass normally and under optimized Python 3.13.9 with SymPy 1.13.1. For each pair, the complete result records agree after removing only the optimization flag.

Each of three deliberate-fault modes runs the same 161 comparisons and fails exactly one comparison, with exit status one, under both normal and optimized Python:

- `wrong-phase-sign`: replaces \(p_2(c+iu)=-(u^2-\sigma^2)\) by the positive expression. The nonzero residual is \(-2u^2+2\sigma^2\).
- `wrong-boundary-factor`: divides the original degree-two rank-two boundary by an additional factor two. The independently computed kernel identity rejects the changed factor.
- `wrong-toda-loss-sign`: adds the imbalance square to the upper expression instead of subtracting it. The residual is \(-98\sigma^2/33\).

Each fault is a single injected formula error. The full baseline computations continue unchanged, so the failure count records detection of that exact error, and the other 160 comparisons continue to pass. The checker uses explicit recorded comparisons and return codes; Python assertions do not control validation.

The eight result files, actual tool execution records and replay manifest accompany this review. Results support this finite symbolic calibration and supplement the full written proof above. No statement about arithmetic zero locations or growing-degree bounds follows from these checks.

## Revision and scope record

The initial read covered TC.1–10. A second independent algebra review read those equations and the complete earlier E chapter, and independently derived the same metric, radius, Toda loss and projector matrices. During this review the author distinguished the coordinate matrix from the spectral scalar, explicitly defined the determinants/logarithm and volume ratio, stated which operator \(A_x\) represents, supplied the exact real-to-original parity congruence, and added TC.11–13 with the exact two projector kernels. This final review reread the complete amended source and all thirteen equation groups at the pinned hash above. The reviewer changed no mathematical source, published stage or frozen edition.
