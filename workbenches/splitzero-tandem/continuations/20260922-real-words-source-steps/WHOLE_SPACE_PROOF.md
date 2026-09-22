# Whole-space polynomial signs, exact source mixing, and original arithmetic evolution

22 September 2026. Continuation on the original scalar-source quotient and its actual observation. GitHub input cut: `fa55542372f01ba3a35ea20fa6eda1030404688f`; terminal-response mathematical cut: `40a766ed3a8e0eadd9947f591803255b6eecf184`; current/effective-cutoff proof: `5c69161ca70ee187f41df0bfe786e8b6eebed422`.

This note derives finite whole-space sign results, rather than inferring the current of a marked eigenclass from the determinant of a positive energy. All adjoints, source minima, observation lifts, and zero factors are specified. It also identifies an incorrect equality in RD15 of the input: its first coefficient formula is retained and its identification with twice the kernel-volume constant is corrected in Section 8.

## 0. Input statements and scope

The literal scalar source is a positive measure `mu` on the real line with all used moments finite and with positive definite polynomial Grams. The relation `Q` is real monic of degree `q` and `Q(y)>0` for mu-almost every y. The original simple-quartet polynomial has this property: it is the product of its complete conjugate pairs, none on the real line. Repeated conjugate primary factors have the same property; simplicity is not used in Sections 1–6.

Set `E=C[y]/Q`, `M[p]=[yp]`, and let `J_N:P_N -> E` be the original polynomial remainder map, for `N>=q-1`. Its attained metric is `G_N`, with source-minimum section `R_N=J_N^dagger`. Thus
\[
 J_NR_N=I_E,\qquad R_N^\dagger R_N=I_E,\qquad
 R_NJ_N=P_{(Q\mathcal P_{N-q})^\perp}\quad\hbox{on }\mathcal P_N.
 \tag{WS1}
\]
For `N=q-1` the relation subspace is zero. This dictionary retains the full original source mass. A coefficient change `S:E' -> E` transports `G` to `S^*GS`, `M` to `S^{-1}MS`, `Lambda` to `Lambda S`, and every class to its inverse image. Each form below then changes by that displayed congruence. In particular the physical arithmetic unit may be inserted by its actual multiplication map, with its entire inverse and Gram, rather than deleted.

Let `p_j` denote real monic orthogonal polynomials for mu and `omega_j=||p_j||_mu^2`, including `omega_0=mu(R)`. Put `phi_j=p_j/sqrt(omega_j)`. The orthogonal polynomial recurrence is the full real recurrence, with its positive norm ratios; no probability normalization is imposed. Orthogonality gives the usual polynomial bandwidth directly: `<phi_i,y^d phi_j>=0` for `i>j+d` or `j>i+d`. DLMF 18.2 records the recurrence and positive-moment conventions; the specific quotient calculations below are derived explicitly.

For a real polynomial `p` define the Hermitian current endomorphism and form
\[
 W_p=i[p(M)-p(M)^{\dagger_G}],\qquad
 \mathfrak W_p=GW_p=i[Gp(M)-p(M)^*G].
 \tag{WS2}
\]
Their inertia is the inertia of `G^(1/2) W_p G^(-1/2)`, equivalently of the coefficient form `mathfrak W_p`. For the original physical action `mathscr A=kI/2+iM`, exactly
\[
 \mathscr A^*G+G\mathscr A-kG=\mathfrak W_y.
 \tag{WS3}
\]
For higher real polynomial tests no new weight is assigned to `p(M)`. They are related to the original linear current by the exact noncommutative telescoping identity
\[
 W_p=\sum_{j\ge1}a_j\sum_{h=0}^{j-1}(M^\dagger)^h W_yM^{j-1-h},
 \qquad p(y)=\sum_j a_jy^j.
 \tag{WS4}
\]
Subtract consecutive powers to verify it; no factors of M and its adjoint are interchanged.

The quantitative native applications use the input RC22–27/OCP5–7 statements, on their written fixed-packet and fixed-period domains:
\[
 M=C+\epsilon f e^\dagger,\quad C=C^\dagger,\quad e\perp f,
 \quad\|e\|=\|f\|=1,\quad
 \|C\|\le2(N+1)\sqrt{u_k/\ell_k},
 \tag{WS5}
\]
\[
 \log\epsilon=q\psi(t_N)+O_{h,\varpi}(k\log(q+2)),\quad
 t_N=(N+1-q)/q,\quad
 \log(u_k/\ell_k)=O_h(k+\log(q+2)).
 \tag{WS6}
\]
The last ratio is applied at every actual extra degree used below; the source FW7 states the bound for arbitrary finite degree. The input does not need a new source cutoff to represent an outgoing class: its entire degree-N minimum is used.

The observed two-column estimates already established in OCP and RC are
\[
 U_B=[Q_B^{1/2}\Lambda e,Q_B^{1/2}\Lambda f],\quad
 0\prec U_B^*U_B\preceq I_2,\quad\det(U_B^*U_B)\ge\Theta_N>0,
 \tag{WS7}
\]
\[
 -\log\Theta_N=O(k\log q),\qquad
 \alpha_N:=\|(I-L\Lambda)e\|_G^2
 \le e^{-2q\psi(t_N)+O(k\log q)}.
 \tag{WS8}
\]
The actual conductor margin in OCP19–23 includes its complex off-diagonal determinant product. Nothing in this note substitutes individual column norm bounds for WS7. The source's terminal-class norm guard is stronger and is not needed for the whole-space results.

## 1. Every real polynomial word up to half the packet degree

Let `p` be any real polynomial of degree `d`, `1<=d<=q/2`, with leading coefficient `a_d!=0`. It may have arbitrary lower coefficients. Define the incoming and outgoing maps, with their original source scalars,
\[
 I_d=[J_N\phi_{N-d+1},\ldots,J_N\phi_N],\qquad
 O_d=[[\phi_{N+1}],\ldots,[\phi_{N+d}]],
 \tag{WS9}
\]
where every outgoing class is evaluated in `G_N`, not in `G_(N+d)`. Define the real d-by-d matrix
\[
 B_p[r,s]=\langle\phi_{N+r},p(y)\phi_{N-d+s}\rangle_\mu,
 \qquad 1\le r,s\le d.
 \tag{WS10}
\]
Degree proves `B_p[r,s]=0` for r>s. Its complete diagonal is
\[
 B_p[s,s]=a_d\sqrt{\omega_{N+s}/\omega_{N-d+s}}\ne0.
 \tag{WS11}
\]
Thus B_p is invertible.

For an actual class x, multiply its complete minimum representative R_Nx by p. Its part in P_N compresses to the selfadjoint operator
`C_p=R_N^dagger P_(P_N) p(y) R_N`. The outgoing part uses only the last d source coordinates, and the exact adjoint identity in WS1 gives
\[
 p(M)=C_p+O_dB_pI_d^{\dagger_G},\qquad C_p=C_p^\dagger.
 \tag{WS12}
\]
Set
\[
 Z_p=[I_d,O_dB_p],\qquad
 J_d=\begin{pmatrix}0&-iI_d\\iI_d&0\end{pmatrix}.
\]
Then
\[
 \boxed{W_p=Z_pJ_dZ_p^{\dagger_G}.}
 \tag{WS13}
\]
This contains every source multiplication cross term of WS4 in one exact boundary matrix.

### 1.1 The boundary map is injective, including repeated primaries

Consider a source polynomial F in the span of the 2d consecutive phi's in WS9 whose class is zero. It equals Qh, with
`deg h<=N+d-q<=N-d`. On the other hand F is orthogonal to P_(N-d). Therefore
\[
 0=\langle h,F\rangle_\mu=\int Q(y)|h(y)|^2d\mu(y).
 \tag{WS14}
\]
Positivity of Q on the measure and positive polynomial Grams imply h=0. Independence of the source phi's gives F=0. Hence `[I_d,O_d]`, and therefore Z_p, has full column rank 2d. This proof uses no separation or simplicity of the roots of Q.

Put `R_p=Z_p^*GZ_p>0` and `V_p=Z_pR_p^{-1/2}`. Then `V_p^dagger V_p=I_(2d)`, and on its image
\[
 V_p^\dagger W_pV_p=R_p^{1/2}J_dR_p^{1/2}.
\]
The orthogonal complement is the full radical. Congruence with the invertible `R_p^(1/2)` proves
\[
 \boxed{\operatorname{In}(W_p)=(d,d,q-2d).}
 \tag{WS15}
\]
In particular the actual native q is even, so the explicitly specified word `p(y)=y^(q/2)` has inertia `(q/2,q/2,0)` at every original canonical cutoff. It has no hidden zero-current direction. This higher word is related to the original linear action by WS4; it is not identified with that linear action. These are numbers of positive, negative and zero eigenvalues on the complete original E. They do not depend on period orientation, on the lower coefficients of p, or on cutoff N within the stated domain.

### 1.2 All vectors and all maximal isotropic subspaces

For x in E set `t=Z_p^dagger x=(a,b)`, and
\[
 c_+=(a-ib)/\sqrt2,\qquad c_-=(a+ib)/\sqrt2.
\]
Every t occurs: the exact right inverse is `x=Z_pR_p^{-1}t`. Every x has the unique decomposition
\[
 x=Z_pR_p^{-1}t+x_0,\qquad x_0\in\ker Z_p^\dagger,
\]
with squared norm `t^*R_p^{-1}t+||x_0||_G^2`. Direct multiplication proves the entire sign formula
\[
 \boxed{\langle x,W_px\rangle_G
 =2\Im(a^*b)=\|c_+\|^2-\|c_-\|^2.}
 \tag{WS16}
\]
Thus the positive, negative and null sets are exactly the corresponding norm comparisons in these specified coordinates. The radical is `a=b=0`; an isotropic vector need not lie there.

Let
`S=2^{-1/2}[[I,I],[iI,-iI]]`, so `t=S(c_+,c_-)` and `S^*J_dS=diag(I,-I)`. Every maximal totally isotropic complex subspace is exactly
\[
 \{Z_pR_p^{-1}S(h,Uh)+x_0:
      h\in\mathbb C^d,\ x_0\in\ker Z_p^\dagger\},\qquad U^*U=I_d.
 \tag{WS17}
\]
It has dimension q-d. To prove completeness, a maximal isotropic space contains the radical. In the remaining signature-(d,d) space its projection onto the positive coordinates is injective, so its dimension is at most d; at dimension d it is the graph of a norm-preserving, hence unitary, map U. WS17 restores the exact source metric and inverse coordinate map.

Since Q, mu and p are real, coefficient conjugation preserves G and sends W_p to -W_p. Thus its nonzero eigenvalues are paired exactly as `+sigma_j,-sigma_j`. Conjugation is transported by the actual physical-unit map under a coefficient change; it is not presumed to be entrywise conjugation in an unrelated physical frame.

### 1.3 Observations and all their zero cases

For any given onto Lambda use its actual minimum L, metric Q_B, and isometry J_B. Then
\[
 W_{p,B}=J_B^\dagger W_pJ_B=Z_BJ_dZ_B^*,\qquad
 Z_B=Q_B^{1/2}\Lambda Z_p.
 \tag{WS18}
\]
Let `C_B=Z_B^*Z_B`, including its full nullspace. On its positive range `V=Z_B C_B^{+1/2}` is an isometry, and
\[
 W_{p,B}=V[C_B^{1/2}J_dC_B^{1/2}]V^*.
 \tag{WS19}
\]
Its other directions are zero. This is a complete matrix of order at most 2d for the whole observed sign problem, with no replacement of a zero block by an inverse. The original observed vector b has form value `(Z_B^*Q_B^(1/2)b)^*J_d(Z_B^*Q_B^(1/2)b)`.

Restriction min–max gives the explicit count bounds
\[
 (d-m)_+\le n_\pm(W_{p,B})\le d,\qquad m=\dim\ker\Lambda.
 \tag{WS20}
\]
In particular, at every native degree `m<d<=q/2`, both observed signs are present for every original observation of that rank. At the native half-degree word, the lower bound is exactly `q/2-m=(k-3)(k-11)/2`, positive for every admitted k>=17. Thus its original observed current has at least that many directions of each sign, independently of the period orientation. For d=1 the stronger exact `(1,1,dim B-2)` count is already the source OCP theorem on its full conductor-area domain. It is not claimed again as a new two-column estimate.

The observed word in WS18 is the measured full word `Lambda p(M)L`. The exact difference from applying p to the intrinsic compressed generator is retained. For d>=2, with `M_B=Lambda M L` and `Qp=I-L Lambda`,
\[
 \Lambda M^dL-M_B^d
 =\sum_{j=0}^{d-2}M_B^j\Lambda M Qp M^{d-1-j}L.
 \tag{WS20a}
\]
Insert `I=L Lambda+Qp` after the first M and iterate to prove this identity. Each right-hand factor retains all subsequent hidden excursions. Thus no nonlinear observation/action interchange is used in the sign calculation.

For a complex polynomial p=u+iv, u,v real, the exact relation is
\[
 W_p=W_u-[v(M)+v(M)^\dagger].
 \tag{WS21}
\]
The second term is retained. WS15 is a real-polynomial theorem; WS21 is the precise additional term for a nonreal pivot word.

### 1.4 Real rational words: full sign classification through denominator maps

Let `r(y)=p(y)/s(y)` have real coefficients, with `gcd(s,Q)=1`. Cancel the actual polynomial gcd of p,s first. Denote the reduced numerator and denominator again by p,s and put `d=max(deg p,deg s)`. For `1<=d<=q/2`, the entire rational action
\[
 T_r=p(M)s(M)^{-1}
\]
is well-defined on the original quotient, with all primary multiplicities. The denominator may have real or repeated poles; no rational function is integrated against the source measure in this proof. Only polynomial source inner products and the invertible quotient multiplication map s(M) are used.

Define the real symmetric Bezout coefficient matrix B by the exact polynomial identity
\[
 \frac{s(x)p(y)-p(x)s(y)}{y-x}
 =\sum_{i,j=0}^{d-1}B_{ij}x^iy^j.
 \tag{WS21a}
\]
It is invertible for the reduced pair. A proof retaining repeated roots is as follows. Arrange, by swapping p,s and reversing the sign if necessary, that deg s=d. In the quotient algebra C[x]/s, multiplication by p is invertible by the Euclidean polynomial identity. Put `c_s(x,y)=(s(y)-s(x))/(y-x)`. Modulo s(x), WS21a is exactly `-p(x)c_s(x,y)`: multiply the proposed identity by the monic polynomial y-x in the ring `(C[x]/s)[y]`, where that multiplication is injective by its leading coefficient one. The coefficient matrix of c_s is anti-triangular with the nonzero leading coefficient of s on its anti-diagonal. Thus B is the product of an invertible quotient multiplication matrix and this invertible coefficient matrix. No simple-root interpolation is used.

Choose the exact rank-two linear-current factor `W_y=Z_1J_1Z_1^dagger` from WS13. Define
\[
 \mathcal Z_d=[Z_1,M^\dagger Z_1,\ldots,(M^\dagger)^{d-1}Z_1].
\]
WS4 for y^d gives
\[
 W_{y^d}=\mathcal Z_d(R_d\otimes J_1)\mathcal Z_d^\dagger,
\]
where R_d is the d-by-d anti-diagonal permutation matrix. WS15 already proves rank `2d` for the left side; consequently `mathcal Z_d` has rank 2d. This proves the needed complete Krylov independence without a new genericity assumption.

Multiply the actual rational current form by its denominator on both sides. The exact identity is
\[
 \begin{aligned}
 s(M)^*\mathfrak W_r s(M)
 &=i[s(M)^*Gp(M)-p(M)^*Gs(M)]\\
 &=G\mathcal Z_d(B\otimes J_1)\mathcal Z_d^{\dagger_G}.
 \end{aligned}
 \tag{WS21b}
\]
To verify the second line, multiply WS21a by y-x and substitute each monomial `x^iy^j` by `(M^*)^i G M^j`. Left and right multiplication are the explicitly commuting operations on the middle coefficient matrix; M and G themselves are not assumed to commute. The middle difference y-x supplies exactly `i(GM-M^*G)`.

The denominator congruence is invertible. Equivalently, with
\[
 Z_r=(s(M)^{\dagger_G})^{-1}\mathcal Z_d,
 \qquad W_r=Z_r(B\otimes J_1)Z_r^\dagger,
 \tag{WS21c}
\]
the column map Z_r has rank 2d. Every nonzero real eigenvalue of B contributes one positive and one negative eigenvalue when tensored with J_1. Therefore
\[
 \boxed{\operatorname{In}i(T_r-T_r^\dagger)=(d,d,q-2d).}
 \tag{WS21d}
\]
A real constant rational word has the zero current. Every nonconstant real rational word of the stated reduced degree has this complete whole-space signature. Repeated poles, collisions among denominator poles, and arbitrary real lower coefficients do not change it. An actual common numerator/denominator factor lowers the reduced degree by its full degree; it contributes the corresponding additional zero directions. Invertibility of s(M) is never retained across a common factor with Q by deleting that primary.

This includes the programme's original inverse powers: `r(y)=y^{-d}` is defined because the original Q_k(0) is nonzero, and its current has exactly d signs of each kind for d<=q/2. The exact connection is
`W_(M^(-d))=-M^(-d dagger) W_(M^d) M^(-d)`. At d=q/2, every one of the q directions is nondegenerate for both words.

All sign witnesses and null spaces can be recovered from WS21c by its full positive Gram and a real orthogonal diagonalization of B, followed by the fixed two-by-two eigen-isometry of J_1. For each negative B eigenvalue interchange its two signs. This constructs the same hyperbolic coordinates as WS16–17 through specified invertible matrices, with the full rational denominator retained.

At the full-rank endpoint q=2d there is also an exact determinant identity:
\[
 \boxed{
 \det W_r=
 \frac{(\det B)^2}{|\det s(M)|^2}\det W_{y^d}.
 }
 \tag{WS21e}
\]
Indeed `mathcal Z_d` is square invertible; its complete metric Gram cancels between the two determinant factorizations, while the denominator contributes `|det s(M)|^(-2)`. The factor `det s(M)=Res(Q,s)` retains every original primary multiplicity; the equality follows by triangularizing the quotient multiplication on its full primary blocks, whose diagonal values are s at those roots. Thus for a fixed rational word at this rank, its full four-cutoff logarithmic determinant return equals that for M^d exactly. No uncomputed asymptotic coefficient for that high-degree return is assigned by the equality.

## 2. Real divisor words of every degree

Factor the same real positive relation as `Q=D O`, with real monic D,O. Put `d_D=deg D`, `r=deg O`, so q=d_D+r. No coprimality is required. For the actual word `T=D(M)`, exact polynomial cancellation gives
\[
 \ker T=O\mathcal P_{d_D-1},\qquad
 \operatorname{im}T=D\mathcal P_{r-1},\qquad\operatorname{rank}T=r.
 \tag{WS22}
\]
When d_D<=r, WS15 applies directly. Consider d_D>=r. Suppose `[D b]` is orthogonal to `ker T`, and let `F=D b+Qh=Dg` be its entire degree-N minimum. It is orthogonal to the full relation space. Together with the assumed kernel orthogonality, this makes F orthogonal to
\[
 O\mathcal P_{d_D-1}+Q\mathcal P_{N-q}
 =O\mathcal P_{N-r}.
\]
The equality follows by division by the monic D. Here `deg g<=N-d_D<=N-r`, so `Og` is one of those actual source polynomials. Therefore
\[
 0=\langle Og,Dg\rangle_\mu=\int Q|g|^2d\mu,
\]
forcing g=0. Thus
\[
 \operatorname{im}T\cap(\ker T)^{\perp_G}=0.
 \tag{WS23}
\]
In the exact orthogonal splitting `ker T plus its complement`, write
`T=[[0,B],[0,A]]`. The complement has dimension r. WS23 proves that B is injective. On `ran B plus (ker T)^perp`, the current has the complete form
\[
 \begin{pmatrix}0&iB\\-iB^\dagger&i(A-A^\dagger)\end{pmatrix}.
\]
The off-diagonal block has rank r. A triangular congruence removes the last diagonal block and then an invertible change by B gives `r` hyperbolic pairs; all `q-2r` orthogonal kernel directions are zero. Hence the complete result, covering both degree orders, is
\[
 \boxed{\operatorname{In}i(D(M)-D(M)^\dagger)
 =(s,s,q-2s),\qquad s=\min(\deg D,\deg O).}
 \tag{WS24}
\]
A degree-zero real factor gives the zero current, as does D=Q; these are the s=0 cases of WS24. The formula includes shared primary factors and repeated conjugate roots. For a complex pivot factor use WS21; it is not made real by changing its label. For example `Q=y^2+1`, the Gaussian source on P_1 with G=I, and `D=y-i` give one positive current and one zero. The explicit difference is `W_D=W_y+2I`, verifying why the real-factor domain matters.

## 3. The complete boundary Gram and the evaluated signed volume

Continue with the real degree-d word, `2d<=q`. Let U_j be the real monic orthogonal polynomial for the full measure `Q^2 dmu`, and `nu_j=||QU_j||_mu^2`. Its normalized relation columns are
`r_n=Q U_(n-q)/sqrt(nu_(n-q))`, for n>=q. In the high source rows `phi_(N-d+1),...,phi_(N+d)`, the only contributing relation columns are the last at most d old ones and the d new ones. Their entire coefficient matrix is
\[
 R_H=\begin{pmatrix}X&Y\\0&Z_0\end{pmatrix},\quad
 (Z_0)_{rs}=\langle\phi_{N+r},r_{N+s}\rangle_\mu,
 \quad (Z_0)_{ss}=\sqrt{\omega_{N+s}/\nu_{N+s-q}}.
 \tag{WS25}
\]
Z_0 is upper triangular and invertible. X can have fewer than d columns at the first cutoffs; the formula uses its actual width.

The high-source Gram at the larger minimum G_(N+d) is `I-R_H R_H^*`, by projection against all orthonormal relation columns. The complete covariance update is
`G_(N+d)^(-1)=G_N^(-1)+O_dO_d^*`. Apply the matrix inversion identity to this full update. If V denotes `I_d^*G_NO_d` and D denotes `O_d^*G_NO_d`, the new lower block is `D(I+D)^(-1)=I-Z_0Z_0^*`; thus `(I+D)^(-1)=Z_0Z_0^*`. The new cross block is `V(I+D)^(-1)=-YZ_0^*`, so `V=-YZ_0^(-1)`. Returning the upper block gives the exact old-cutoff Gram
\[
 \boxed{
 [I_d,O_d]^*G_N[I_d,O_d]=
 \begin{pmatrix}
 I-XX^*&-YZ_0^{-1}\\
 -Z_0^{-*}Y^*&(Z_0Z_0^*)^{-1}-I
 \end{pmatrix}.}
 \tag{WS26}
\]
All old and new source relations and all cross terms are included. The larger cutoff has been used only in this exact algebraic identity; the final metric in WS26 is G_N.

In the balanced fixed-cutoff frame
\[
 F=[I_d,O_dZ_0],\qquad
 K_0=F^*G_NF=
 \begin{pmatrix}I-XX^*&-Y\\-Y^*&I-Z_0^*Z_0\end{pmatrix}>0,
\]
put `D_p=Z_0^(-1)B_p`. The current becomes
\[
 W_p=F\begin{pmatrix}0&-iD_p^*\\iD_p&0\end{pmatrix}F^{\dagger_G}.
 \tag{WS27}
\]
These formulas specify the exact balancing map and metric; F is not declared orthonormal.

If `delta=max(||X||,||Y||,||Z_0||)` and `rho=delta+delta^2<1`, the complete Gram obeys
`(1-rho)I<=K_0<=(1+rho)I`. Generalized min–max, on the positive and negative spectral subspaces of the numerator in WS27, gives
\[
 (1-\rho)\sigma_j(D_p)\le\lambda_j^+(W_p),\ -\lambda_j^-(W_p)
 \le(1+\rho)\sigma_j(D_p),\quad 1\le j\le d.
 \tag{WS28}
\]
The same factor can bound both signs because the denominator is positive. The entire nonzero determinant is even more explicit and needs no small-rho condition:
\[
 \boxed{
 \operatorname{pdet}W_p=(-1)^d|a_d|^{2d}
 \left[\prod_{s=1}^d\frac{\nu_{N+s-q}}{\omega_{N-d+s}}\right]
 \det K_0.
 }
 \tag{WS29}
\]
Indeed the determinant of the small numerator is `(-1)^d |det D_p|^2`; multiplication by the entire positive Gram contributes det K_0. WS11 and WS25 cancel exactly the intermediate norms `omega_(N+s)`. Thus the product of all positive eigenvalues, squared, is the right side's absolute value. It depends on the lower coefficients of p only through **none of its factors**. For fixed leading coefficient, changing any real lower coefficient changes neither this full signed product nor the inertia. It can change individual eigenvalues; those are not identified by their product.

### 3.1 A finite native Gram guard

The finite guard in WS28 can be bounded without an unevaluated angle matrix. Use the original complete source comparison at degree `2q+d+1`, with ratio `kappa_k=u_k/ell_k`. The source FW7 has this degree explicitly available. Put
\[
 R_*=\max\{1,k\sqrt{\delta^2+\gamma^2},2(N+d+1)\sqrt{\kappa_k}\},
 \quad B_*=2(N+d)R_*,
\]
\[
 \zeta_*=\max_{\max(q,N-d+1)\le n\le N+d}
 \sqrt{\omega_n/\nu_{n-q}},\qquad
 \delta_* =d\sqrt{\kappa_k} B_*^{2d}\zeta_*.
 \tag{WS30}
\]
This is a finite bound `delta<=delta_*` for all the actual blocks in WS25. Here is its proof. Compressed real multiplication places every root of the used p_n and U_j inside the multiplication norm bound in R_*; the latter measure is Q^2 dmu, so its Rayleigh quotient is the ratio of the actual norms of yQP and QP. The source comparison and Gamma multiplication bound apply through their actual degrees. The roots of Q are also bounded by R_*.

Consequently, a coefficient h positions below the leading coefficient of either monic polynomial is bounded by `(n R_*)^h`. In the expansion `Q U_(n-q)=sum_i c_(i,n)p_i`, triangular elimination gives `|c_(n-h,n)|<=(2n R_*)^h`: induct on h using the bound `1+sum_(j<h)2^j=2^h`. A normalized relation coefficient is
`c_(i,n) sqrt(omega_i/omega_n) sqrt(omega_n/nu_(n-q))`.
The indices differ by at most 2d; the same Gamma source comparison gives `sqrt(omega_i/omega_n)<=sqrt(kappa_k)` in this high-index range. The matrix norm is at most d times its maximum entry. This proves WS30, with no omission of an off-diagonal block.

For the admitted native simple quartet, use RC22–24's full monic estimate at every actual n in WS30:
\[
 \log\frac{\nu_{n-q}^\sigma}{h_n}
 =2q\psi((n-q)/q)+O_h(\log(q+2)),\qquad
 h_n=\sqrt{2\pi}\,n!(1/2)_n.
\]
The original arithmetic norm comparison restores omega_n and nu_(n-q) with logarithmic error `O_h(k+log(q+d+2))`. The profile's endpoint derivative bound gives a shift error `O_h(d log(q+2))`. Therefore
\[
 \log\delta_*
 \le-q\psi(t_N)+O_h\{k\log(q+2)+d[k+\log(q+2)]\}.
 \tag{WS31}
\]
For every integer sequence `d=o(k)`, this is negative by order q, uniformly over the original N window, because the stated profile has positive minimum there. The complete Gram K_0 therefore approaches I in this explicit balanced frame; the original G_N is not set to I.

Combining WS29, the exact Gamma factorial ratios, and the same finite source comparisons proves
\[
 \boxed{
 \sum_{j=1}^{d}\log\sigma_j(W_p)
 =d\log|a_d|+dq\psi(t_N)
 +O_h\{dk\log(q+2)+d^2\log(q+2)\}.
 }
 \tag{WS32}
\]
Here the sigma_j are the d positive eigenvalues, with the negative eigenvalues exactly their opposites. The error is uniform in all real lower coefficients, even when they vary: their cancellation is the exact identity WS29. The leading coefficient may depend on k but is the same at every cutoff.

Taking the original four signs, whose parameters are exactly `0,1/q,1,1+1/q`, yields
\[
 \boxed{
 \mathcal R\sum_{j=1}^{d}\log\sigma_j(W_p)
 =2d[\psi(0)-\psi(1)]q
 +O_h\{dk\log(q+2)+d^2\log(q+2)\}.
 }
 \tag{WS33}
\]
The endpoint error is obtained by integrating the logarithmic bound for psi' near zero and its bounded derivative near one. No adjacent source degree is merged without its error. After division by dq the error tends to zero throughout d=o(k).

For any fixed real polynomial p, WS28 and the triangular matrices give the individual laws `log sigma_j=q psi(t_N)+O_(h,p,d)(k log q)`. One verification bounds B_p by the full multiplication norm of p(y), bounds its diagonal below with WS11, and uses the finite upper-triangular inverse recursion. The same recursion for Z_0, whose diagonal logarithms are `-q psi+O(k log q)`, bounds its scaled matrix and inverse by `exp[O_(h,d)(k log q)]`. These estimates are not uniform in arbitrarily large lower coefficients; WS32–33 are uniform because of their exact determinant cancellation.

The same product evaluates an unavoidable whole-space correction cost. For a nonnegative scalar correction to the Hermitian current, the least value is `b_opt=max_j sigma_j(W_p)`. WS29 gives the finite bound
\[
 b_{\rm opt}\ge |a_d|\left[
 \det K_0\prod_{s=1}^d\frac{\nu_{N+s-q}}{\omega_{N-d+s}}
 \right]^{1/(2d)}.
\]
Thus every monic real word with d=o(k), without any lower-coefficient restriction, has
`log b_opt>=q psi(t_N)-O_h(k log q+d log q)` in the native family. A fixed polynomial scalar allowance cannot dominate this canonical whole-space form. For a general positive operator correction Z, the least possible trace is `sum_j sigma_j`, attained by the negative spectral part of W_p; the least possible rank is d. Indeed restrict `W_p+Z>=0` to its entire negative spectral subspace and take its trace, and then use rank-nullity on that same subspace. These are correction costs for this specified Hermitian form in G_N, not an assertion that an arbitrary source enlargement realizes the minimizing correction.

### 3.2 The full physical Hermitian part and all exterior powers

For p=y, the full current is exactly `epsilon J_1` on its two-dimensional active plane. Thus its nonzero eigenvalues are +epsilon and -epsilon. The full uncentered physical form is `G(kI+W_y)` and has eigenvalues `k+epsilon,k-epsilon,k` in the actual metric. On the explicit finite guard epsilon>k its inertia is `(q-1,1,0)`. The native estimates WS6 make this guard hold eventually, uniformly over the source window. The observed form has the same count `(dim B-1,1,0)` on the already-proved guard `epsilon Theta_N>k`. These are values of the displayed uncentered forms, not the sign of a separately marked vector.

Let `mathscr A^[r]` be the actual derivation action on the r-th exterior power, not the multiplicative matrix `wedge^r mathscr A`. The induced metric is `wedge^r G`, and
\[
 (\mathscr A^{[r]})^*\wedge^rG+(\wedge^rG)\mathscr A^{[r]}-rk\wedge^rG
 =(\wedge^rG) W_y^{[r]}.
 \tag{WS34}
\]
The exact original orthonormal eigen-isometry of W_y induces its exterior isometry. Selecting +epsilon without -epsilon gives `binom(q-2,r-1)` positive eigenvalues +epsilon; selecting the negative alone gives the same number -epsilon. Selecting both or neither gives zero. Hence
\[
 \boxed{\operatorname{In}W_y^{[r]}=
 \left(\binom{q-2}{r-1},\binom{q-2}{r-1},
 \binom{q-2}{r}+\binom{q-2}{r-2}\right).}
 \tag{WS35}
\]
Use binomial zero outside its usual range. The uncentered form is `rkI+W_y^[r]`; on epsilon>rk its negative count is `binom(q-2,r-1)` and every other direction is positive. This guard holds eventually simultaneously for 1<=r<q, since epsilon grows exponentially and rk<=qk. At r=q the centered current is zero and the uncentered form is positive.

### 3.3 Every block of the original linear Hermitian current

In the exact observed/kernel isometries let `U_B=[Pe,Pf]` and `U_K=[Qp e,Qp f]`, retaining their actual codomains. Their Grams are
\[
 C_B=\begin{pmatrix}a&r\\\bar r&b\end{pmatrix},\qquad
 C_K=I_2-C_B.
\]
The observed eigenvalues are the existing OCP values
`epsilon[-Im r +- sqrt(ab-(Re r)^2)]`. On the entire original kernel the complete list, before zero padding, is
\[
 \epsilon\left[\Im r\ \mathord\pm
 \sqrt{(1-a)(1-b)-(\Re r)^2}\right].
 \tag{WS35a}
\]
It follows by multiplying the full matrices `J_1 C_K`, including the complex off-diagonal entries. At `det C_K>0` there is one sign of each kind; at determinant zero the possible remaining eigenvalue is `2epsilon Im r`, including its actual zero case. When `C_K=0`, the whole hidden current vanishes.

The mixed **Hermitian** current is the off-diagonal block operator built from `H=epsilon U_B J_1 U_K^dagger`. It has eigenvalues `+sigma_j(H),-sigma_j(H)` and the full remaining zeros. Their squares are the nonzero eigenvalues of
\[
 \epsilon^2 C_B^{1/2}J_1C_KJ_1C_B^{1/2}\succeq0.
 \tag{WS35b}
\]
On the established native area domain `C_B>0`, its rank is `rank C_K`. Thus the mixed Hermitian current has inertia `(rank C_K,rank C_K,q-2rank C_K)`. These are exact classifications of all three blocks; they do not add their signatures to obtain the signature of their sum, since the retained mixed blocks couple the two subspaces.

## 4. Complete whole-space signs of the mixed quartic

Keep the original orthogonal projection P=L Lambda and Qp=I-P. In the actual isometries of B and K define the two full arithmetic mixed blocks
\[
 C=Qp M|_{K^\perp}:K^\perp\to K,\qquad
 D=P M|_K:K\to K^\perp.
 \tag{WS36}
\]
For x=k+b with k in K and b in K-perp, the physical cross pairings are
\[
 z(x)=\langle k,\mathscr A b\rangle_G=i\langle k,Cb\rangle_G,\qquad
 w(x)=\langle b,\mathscr A k\rangle_G=i\langle b,Dk\rangle_G.
\]
The scalar centre cancels by orthogonality. Define the actual quartic `chi(x)=Re(conj(z(x))w(x))`.

The exact G-unitary map `U_theta=P+exp(i theta)Qp` changes the pair as
\[
 z(U_\theta x)=e^{-i\theta}z(x),\quad
 w(U_\theta x)=e^{i\theta}w(x),\quad
 \boxed{\chi(U_\theta x)=\Re(e^{2i\theta}\overline{z(x)}w(x)).}
 \tag{WS37}
\]
It also satisfies `Lambda U_theta=Lambda`: the observed value, both component norms, and both pure observed/hidden currents are preserved. Every nonzero product orbit therefore attains both signs, with extrema `+|zw|` and `-|zw|` and with exact intervening zeros.

The complete degeneracy classification is: chi is identically zero exactly when C=0 or D=0. One direction is immediate. For the other, C and D^dagger are nonzero linear maps on K-perp, so their two proper kernels cannot cover that complex vector space. Select b outside both; then select k outside the two proper orthogonality hyperplanes to Cb and D^dagger b. This constructs z and w both nonzero. All such choices can be made by a finite pencil b1+t b2, then k1+s k2, avoiding the at most two roots of each pair of linear functionals.

On the original bounded-observation domain, write `K_j=intersection_(h=0)^j ker(Lambda M^h)`. The source proves `dim K_8<=128` and the decreasing layer ranks. Thus
\[
 \operatorname{rank}D=\operatorname{rank}(\Lambda MI_K)
 \ge(m-128)/8=k-18.
\]
Also
`C-D^dagger=Qp(M-M^dagger)P` has rank at most two by WS5. Therefore for every admitted `k>=21`, both C and D are nonzero. WS37 proves that the actual whole-space mixed quartic takes positive, negative and zero values at every cutoff on that domain. This is not a proposed sign for a fixed eigenclass.

Its failure to preserve that eigenclass is an explicit arithmetic defect:
\[
 \boxed{MU_\theta-U_\theta M
 =(e^{i\theta}-1)(PMQp-QpMP).}
 \tag{WS38}
\]
Thus rotating k cannot be used to change a prescribed terminal eigenclass while claiming it is the same input.

For a complete Hermitian realization of the quartic, let `S=Pi_Sym2(B) (C^dagger tensor D) Pi_Sym2(K)`. With the actual induced symmetric-square metrics,
\[
 \chi(k+b)=\Re\langle b\otimes b,S(k\otimes k)\rangle.
\]
The block Hermitian operator on `Sym^2 K plus (K tensor B) plus Sym^2 B`, with only off-diagonal blocks `S/2,S^dagger/2`, has inertia `(rank S,rank S,dim Sym^2 E-2rank S)`. Its restriction to the actual pure-square image is exactly the original chi; WS37 proves both signs on that image itself, rather than inferring them from arbitrary symmetric tensors.

## 5. Original source activation has an affine sign pencil

Let the actual covariance, including its original complete normal-source correction, be
\[
 C_\alpha=G_\alpha^{-1}=(1-\alpha)C_0+\alpha C_1>0,
 \qquad 0\le\alpha\le1.
\]
Fix the original action word T and the original onto Lambda. Define the fixed-coordinate dual current
\[
 S_\alpha=i(TC_\alpha-C_\alpha T^*)
 =(1-\alpha)S_0+\alpha S_1.
 \tag{WS39}
\]
The exact full and observed congruences are
\[
 \boxed{
 C_\alpha i(G_\alpha T-T^*G_\alpha)C_\alpha=S_\alpha,
 \quad
 L_\alpha^*i(G_\alpha T-T^*G_\alpha)L_\alpha
 =Q_{B,\alpha}\Lambda S_\alpha\Lambda^*Q_{B,\alpha}.
 }
 \tag{WS40}
\]
Here `L_alpha=C_alpha Lambda^* Q_B,alpha` and the quotient metric is formed from that same covariance. No section is frozen. The actual maps taking a dual vector to its original primal sign witness are `x=C_alpha z` in E and `b=Q_B,alpha^{-1}z` in B.

For any finite collection of source covariances, the same proof makes the dual current an affine Hermitian function of all weights. Thus its positive-semidefinite region is exactly the intersection of the parameter domain with that affine matrix inequality. On a covariance polytope, positivity on the entire whole space is equivalent to positivity at every vertex: a convex combination of positive forms is positive, and the converse includes each vertex. A fixed marked class has value `b^*Q_B,alpha (Lambda S_alpha Lambda^*)Q_B,alpha b`; its dual coordinate moves. This formula is the exact reason the whole-space vertex statement does not validate vertex sampling of an unrelated marked scalar.

### 5.1 A finite reduction that keeps a singular joint current

For a real polynomial word of degree d<=q/2, the canonical dual current has the factor `S_0=U J_d U^*`, where U=Z_p in E or U=Lambda Z_p in B. The latter can be rank deficient; the following formula allows that.

For alpha>0 put `t=(1-alpha)/alpha`. The inertia to compute is that of `H(t)=S_1+t UJ_dU^*`. Use an actual unitary split of the fixed coefficient space into `ran S_1 plus ker S_1`:
\[
 S_1=\operatorname{diag}(D,0_z),\quad D=D^*\text{ invertible},
 \qquad U=\binom{U_1}{U_0},\quad C=U_1^*D^{-1}U_1.
\]
Put `s=rank U_0`. Choose an isometry onto ran U_0, so `U_0` has its s nonzero rows `V` and `z-s` zero rows. Let N be an isometry from `C^(2d-s)` onto ker V. The whole inertia is
\[
 \boxed{
 \operatorname{In}H(t)
 =\operatorname{In}D
 +\operatorname{In}[-N^*(J_d+tC)N]
 +(s,s,z-s)-(d,d,0).
 }
 \tag{WS41}
\]
The additions and subtraction are componentwise; the formula as a whole has nonnegative entries and total original dimension. The reduced Hermitian pencil has order at most 2d.

For a full proof, border H(t) before eliminating anything:
\[
 \mathcal B_t=\begin{pmatrix}
 D&0&U_1\\0&0&U_0\\U_1^*&U_0^*&-J_d/t
 \end{pmatrix}.
\]
Eliminating the invertible final block gives `In B_t=In H(t)+(d,d,0)`. Eliminating D instead gives D and the block `[0,U_0;U_0^*,-J_d/t-C]`. Remove only the explicit `z-s` zero rows, and use the positive congruence `diag(t^(-1/2)I_s,t^(1/2)I_(2d))`. This leaves `[0,V;V^*,-J_d-tC]`. Split its last space into ran V^* and ker V. The paired block `[0,V_r;V_r^*,F]` has inertia `(s,s,0)` and its inverse has zero lower-right block. Therefore its Schur correction to the remaining N-block is exactly zero, and the latter block is `-N^*(J_d+tC)N`. This proves WS41 and accounts for every radical, including persistent zeros.

### 5.2 The original linear current has at most two interior transition parameters

For d=1 there are three exhaustive cases:

* s=2: the reduced pencil is empty and `In H(t)=In D+(1,1,z-2)` for all t>0.
* s=1: the reduced pencil is the real scalar `-n^*J_1n-t n^*Cn`. Its sign has at most one zero; when both coefficients vanish it is an explicitly retained permanent zero.
* s=0: the reduced matrix is `-J_1-tC`. Its determinant is the real quadratic
\[
 \det(J_1+tC)=-1+t\operatorname{tr}(\operatorname{adj}(J_1)C)+t^2\det C.
 \tag{WS42}
\]
Its constant coefficient is -1, so it is not the zero polynomial. There are at most two positive roots. Between them the complete signs follow from its determinant and trace; at each root the zero multiplicity is retained. The signs at alpha=0 and alpha=1 are the actual endpoint inertias, not a limit with zeros discarded.

Thus an entire full-rank covariance activation has at most two interior sign-transition parameters for the canonical linear-current family. The native joint endpoint's coefficients in WS41 are actual matrices; no numerical inertia for that endpoint is assigned merely from its positive covariance.

### 5.3 A same-map positive-source example attaining two transitions

On C^4 use
\[
 M=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix},\quad
 \Lambda=[I_2,0],\quad
 D_0=\operatorname{diag}(1/2,-1/2),\quad
 D_1=\operatorname{diag}(-1/2,3/4),
\]
\[
 C_0=\begin{pmatrix}I_2&iD_0\\-iD_0&I_2\end{pmatrix},\qquad
 C_1=\begin{pmatrix}3I_2&iD_1\\-iD_1&3I_2\end{pmatrix}.
 \tag{WS43}
\]
Both covariances and their difference are positive definite. Their exact two-by-two blocks have eigenvalues `1+-1/2`, `3+-1/2`, `3+-3/4`, and `2+-1`, `2+-5/4`, respectively. Thus the interpolation is a genuine positive added source covariance on the same M and Lambda.

The actual quotient metric is `Q_B,alpha=(1+2alpha)^(-1)I`, and
\[
 \Lambda S_\alpha\Lambda^*
 =\operatorname{diag}(1-2\alpha,-1+5\alpha/2).
 \tag{WS44}
\]
The complete observed signatures are `(1,1,0)` before alpha=2/5, `(1,0,1)` at 2/5, `(2,0,0)` between 2/5 and 1/2, `(1,0,1)` at 1/2, and `(1,1,0)` afterwards. Both endpoints are indefinite and an interior interval is positive definite. This example evaluates actual source-minimum matrices and has a rank-two observed endpoint current, the exact hypothesis of the finite update reduction. It is not claimed to be the native scalar-source endpoint or a native-period evaluation.

For a covariance error and action error in fixed coefficient coordinates, the exact dual difference is
\[
 i[\delta T\,C+T\delta C+\delta T\delta C
 -\delta C\,T^*-C\delta T^*-\delta C\delta T^*].
\]
Its norm is at most
`2(||delta T||||C||+||T||||delta C||+||delta T||||delta C||)`. Observed errors additionally retain the exact left and right Lambda factors and their perturbations. This supplies a finite sign margin, rather than presuming that a nearly zero eigenvalue has a fixed sign.

## 6. The actual full evolution at every positive exponential time scale

The source CE9–23 proves its joint estimate for the full measured and intrinsic compressed propagators on `b>psi(0)/2`. The following contour calculation extends the full original propagator and its measured norm to **every fixed b>0**. It does not assign the bounded spectrum of M to its noninvariant compression.

Let, in the original finite metric,
\[
 M=C+R_0,\quad C=C^\dagger,\quad\operatorname{rank}R_0=1,\quad
 \|C\|\le c,\quad\|R_0\|=\epsilon,\quad
 \operatorname{spec}M\subset\{|z|\le r_0\}.
\]
The full original M has `r_0=k sqrt(delta^2+gamma^2)`, including its algebraic multiplicities. Put
\[
 R=4q\max(1,c,r_0).
 \tag{WS45}
\]
On `|z|=R`, factor each characteristic polynomial into its q actual eigenvalues, with multiplicity. The exact determinant lemma and the rank-one inverse formula give
\[
 (zI-M)^{-1}-(zI-C)^{-1}
 =\frac{(zI-C)^{-1}R_0(zI-C)^{-1}}
 {\det(zI-M)/\det(zI-C)}.
 \tag{WS46}
\]
Because C is selfadjoint, its resolvent norm is at most `1/(R-c)`. Also
\[
 \left|\frac{\det(zI-C)}{\det(zI-M)}\right|
 \le\left(\frac{1+1/(4q)}{1-1/(4q)}\right)^q<2.
\]
Indeed its logarithm is at most `1/4+1/[4(1-1/(4q))]<=7/12<log 2`; the last strict inequality follows, for example, from the positive series of `log 2`. Therefore
\[
 \|(zI-M)^{-1}-(zI-C)^{-1}\|\le4\epsilon/R^2.
\]
Cauchy's finite-matrix functional calculus, on the same circle enclosing both spectra, gives for every integer j>=1
\[
 \|M^j-C^j\|\le4\epsilon R^{j-1}.
 \tag{WS47}
\]
The exact j=1 difference is R_0. Sum the absolutely convergent exponential series from j=2 onwards:
\[
 \boxed{
 \|e^{itM}-e^{itC}-itR_0\|
 \le\frac{4\epsilon}{R}(e^{R|t|}-1-R|t|)
 \le2\epsilon R t^2e^{R|t|}.
 }
 \tag{WS48}
\]
For real signed t, `||e^(itC)-I||<=c|t|`, so
\[
 \boxed{
 \frac{\|e^{itM}-I-itR_0\|}{1+|t|\epsilon}
 \le c|t|+2R|t|e^{R|t|}.
 }
 \tag{WS49}
\]
No commutation of C and R_0 is used. No lower bound on root separation or diagonalizability of M is needed; the determinant factors retain repeated roots.

On the native source WS5–8, R_0 is nilpotent and `log R=O_h(k+log q)`. For `t=+-exp(-bq)` with b in a fixed compact subset of `(0,infinity)`, WS49 is exponentially small. The nilpotent rank-one shear has exact norm
\[
 S(x)=\frac{\sqrt{x^2+4}+x}{2},\qquad x=|t|\epsilon.
\]
It has one reciprocal pair of singular values, with all other singular values one. Thus the full original propagator satisfies
\[
 \boxed{
 \log\|e^{\pm i e^{-bq}M}\|_G
 =q(\psi(t_N)-b)_++O_{h,\varpi,b}(k\log q),
 }
\]
\[
 \boxed{
 \log\operatorname{cond}_G(e^{i e^{-bq}M})
 =2q(\psi(t_N)-b)_++O_{h,\varpi,b}(k\log q),\qquad b>0.
 }
 \tag{WS50}
\]
The inverse in the second formula is exactly the full exponential with negative signed time.

For the original measured propagator `U(t)=J_B^dagger e^(itM)J_B`, put
`R_B=J_B^dagger R_0J_B`, `epsilon_B=||R_B||` and `h=|tr R_B|/epsilon_B`. WS7–8 prove `epsilon_B>=epsilon sqrt(Theta_N)` and `h<=sqrt(alpha_N/Theta_N)`. Contract WS48 by the actual J_B; its relative error to `1+|t|epsilon_B` is at most
\[
 \delta_B=\Theta_N^{-1/2}[c|t|+2R|t|e^{R|t|}].
\]
An exact unitary frame in the two-dimensional range/source span puts `R_B/epsilon_B` at distance at most 2h from the nilpotent unit shear: its matrix is `[zeta,sqrt(1-|zeta|^2);0,0]`, `|zeta|=h`, after fixing the actual second-vector phase. Therefore
\[
 \left|\frac{\|U(\pm t)\|_{Q_B}}{S(|t|\epsilon_B)}-1\right|
 \le2\delta_B+2h.
 \tag{WS51}
\]
The finite guard that the right side is below one holds eventually for every fixed b>0, since both Theta_N and the leakage alpha_N retain WS8. This proves
\[
 \boxed{
 \log\|\Lambda e^{\pm i e^{-bq}M}L\|_{Q_B}
 =q(\psi(t_N)-b)_++O_{h,\varpi,b}(k\log q),\qquad b>0.
 }
 \tag{WS52}
\]
In particular its entire original four-return is
\[
 \mathcal R\log\|\Lambda e^{i e^{-bq}M}L\|_{Q_B}
 =2q[(\psi(0)-b)_+-(\psi(1)-b)_+]+O(k\log q).
 \tag{WS53}
\]
For every fixed `0<b<psi(1)`, the evaluated coefficient is `2[psi(0)-psi(1)]`, the plateau formerly outside CE's joint b-domain. The full-space condition number has twice that coefficient. For the physical action `mathscr A=kI/2+iM`, the scalar `exp(kt/2)` is kept at each cutoff and cancels exactly under the four signs and from condition numbers.

No intrinsic inverse is assigned to the measured operator. The original exact defect remains
\[
 U(-t)U(t)=I-J_B^\dagger e^{-itM}(I-P)e^{itM}J_B.
 \tag{WS54}
\]
The intrinsic operator `V(t)=exp(it Lambda M L)` retains its existing CE proof and its domain `b>psi(0)/2`. Extending WS52 to the intrinsic small-b domain would require its own spectral estimate: the determinant ratio in WS46 uses the characteristic polynomial of the full M, not that of its compression. The full hidden Volterra equation CE27 and all its cross terms remain unchanged.

## 7. Source-parameter families, exact signs, and marked classes

The whole-space signature WS15 holds at every positive scalar source measure in the stated moment class, including real exponential tilts within their actual moment domain. For the original tilt `exp(theta y)dmu(y)`, the source isometry is multiplication by `exp(theta y/2)` into the original L2 space, restricted to the stated polynomial fibres; it does not assert that the changed fibre remains the same unweighted polynomial subspace. Applying WS9–16 to its actual orthogonal polynomials and attained metric proves the same inertia at every tilt. WS39–44 instead treat a positive covariance addition through its exact affine current map. These two family constructions are related by the common covariance `J_N H_source^(-1)J_N^*`; no equality between a mixed covariance and an unspecified moment Gram is presumed.

On each original eigenclass `Mx=omega x`, the full linear current is exactly
\[
 \langle x,W_yx\rangle_G=-2\Im\omega\,\|x\|_G^2.
 \tag{WS55}
\]
For the stipulated terminal omega=k gamma-i k delta this is positive. It does not follow that a span of several same-half-plane eigenclasses is a positive subspace: in an eigenclass frame x_j the exact current Gram is
\[
 \langle x_i,W_yx_j\rangle_G
 =i(\omega_j-\overline{\omega_i})\langle x_i,x_j\rangle_G.
 \tag{WS56}
\]
All off-diagonal source Grams remain. The exact auxiliary Gaussian quotient `Q=(y^2+1)(y^2+4)`, `N=3`, has positive individual current values on the -i and -2i eigenlines but a signature-(1,1) current on their span. The checker constructs the actual eigenvectors and verifies that statement. This is consistent with, and illustrates the necessity of, the whole-space signature WS15.

For the prescribed observed terminal class, the original TR20 formula remains
\[
 j_N=2\epsilon\sqrt{\det C_B}\Im(\overline{c_g}c_h)
       -2\epsilon(\Im r)|c_g|^2.
 \tag{WS57}
\]
The new source proves the last term exponentially small in absolute value, with its observed-norm guard, and proves an exponentially small coherence deficit. Neither property assigns the sign of the retained imaginary product. This continuation does not rotate that marked class or replace its observation to assign a sign. It completes whole-space, polynomial-word and mixed-form classifications instead.

## 8. A necessary correction to the new denominator return

The original source profiles are different scalar functions connected by RC10–12. Retain exactly
\[
 a_0=\psi(0)=\log(4/\pi),\qquad
 a_1=\psi(1)=\log\frac{\kappa_1(1+r_1)}{E(\kappa_1)^2},\quad E(\kappa_1)=2r_1K(\kappa_1),
\]
\[
 J(t)=4\int_0^t\psi(s)ds-2(1+t)\psi(t)+2a_0,
 \qquad C_\partial=2J(1).
 \tag{WS58}
\]
RD10–14 correctly give `log alpha_resp=2q psi(t_N)+O(k log q)`. Its first equality in RD15 therefore correctly yields
\[
 \boxed{\mathcal R\log\alpha_{\rm resp}=4(a_0-a_1)q+O(k\log q).}
 \tag{WS59}
\]
Read as a new local definition, RD15 assigns its symbol C_boundary a different number; that local label cannot be propagated into the existing CK/PT kernel receivers. Keeping the established global `C_boundary=2J(1)`, the following equality to `2C_boundary q` in RD15 is false. Indeed WS58 gives
\[
 2C_\partial-4(a_0-a_1)
 =16\int_0^1\psi(s)ds-12a_1+4a_0
 \ge4(a_0+a_1)>0,
 \tag{WS60}
\]
because the stated psi is positive decreasing. This is an exact derivation of the discrepancy, independent of a numerical resemblance. OCP46–47 already give the correct half-size linear-current coefficient `2(a_0-a_1)`.

The companion outward integer checker certifies
\[
 0.35009104650043305003462290080515
 <2(a_0-a_1)
 <0.35009104650043305003462290080516,
\]
\[
 \boxed{
 0.70018209300086610006924580161031
 <4(a_0-a_1)
 <0.70018209300086610006924580161032.
 }
 \tag{WS61}
\]
In contrast `2C_boundary` lies between `2.70856397565058426576797955030769` and `2.70856397565058426576797955030770`. The intervals are disjoint. The current profile, the valid denominator pointwise bounds, and the earlier kernel-volume coefficient are unchanged; only RD15's identification of two constants is corrected.

The checker uses denominator 10^80, outward integer addition/multiplication/division and square roots, a Machin enclosure of pi, 4096 normalized elliptic-series terms with geometric tails, 125 certified bisection decisions, and a 160-term logarithm series with its full remainder. Its numerical scope is the universal scalar constants, not a native period or an off-line zero.

## 9. Verification and limits of the result

`check_whole_space_identities.py` tests the full source minima, every polynomial boundary factor, exact signatures, positive/negative/isotropic witnesses, real repeated-primary relations, real divisor words, the full relation Gram with its off-diagonal blocks, signed nonzero products, actual exterior metrics and additive actions, same-map source activation, singular endpoint-current radicals, and original mixed phase orbits. Its negative controls retain the precise failures of a real-root sign-changing relation, a complex divisor word, inference of positive subspaces from eigenline signs, and omission of the eigenclass defect under a hidden-phase rotation. Counts and executed modes are recorded by the package verification manifest, not asserted from the proof alone.

`check_rational_currents.py` verifies the full denominator congruence, the Bezout/Krylov factor, gcd cancellation, and the exact sign counts with repeated primaries and real or repeated denominator poles. `check_reduced_pencils.py` verifies the complete singular-base inertia formula for d=1,2,3, every possible null-coupling rank, and three positive rational interpolation weights, including the retained radical. `check_evolution_diagnostics.py` is separately labeled noninterval: it tests the proved contour bound at 140-digit precision on matrices with the exact spectrum {i,-i} and very large rank-one boundary terms. Its numerical successes are not proofs of the analytic bounds.

The new finite results are WS15–24 (including the complete rational extension WS21a–e), WS26–29, WS35b–44, and WS46–54, with their scope and maps given above. The large-degree applications WS31–33 and WS50–53 use the retained source estimates RC22–27 and the actual full characteristic polynomial, not a new assumption about a native projection. The exact whole-space signs are determined; the separate marked terminal imaginary product WS57 is not numerically or asymptotically evaluated here. No claimed zero, period, or RH conclusion follows from an auxiliary sign fixture.

### Source locations and reading coverage

Read in the pinned GitHub source, with full mathematical bodies used: `OBSERVED_CURRENT_PLANE.tex` OCP1–59 (finite source/conductor/current identities and existing signed-time bound); `CUTOFF_CURRENT_CONNECTION.md` RC1–34 (profiles, finite source costs, current and evolution returns); `EVOLUTION_PROOF.md` CE1–29; `RESPONSE_DENOMINATORS.md` RD1–21; `TERMINAL_COHERENCE_PROOF.md` TR1–24 including TR12a. The last terminal-conductor domain itself is inherited through the TR/RD references, not re-proved by replacing it with a weaker period assumption. The supplied `/mnt/data/Native_Cutoff_Profile_20260922/COMPLETE_PROOFS.md` was reviewed as the earlier cutoff-profile context; its coefficient and measured-phase results are not relabeled as new in this note.

Human primary reference: NIST DLMF 18.2 for the real orthogonal-polynomial recurrence, positivity and Christoffel conventions. All finite source, inertia, mixed-current and contour formulas needed here are proved in this note. The Gamma and elliptic estimates used for native rates retain the original RC/OCP source citations; the interval checker derives its scalar series and remainders directly. A separately executed finite checker supplements rather than replaces the proofs.
