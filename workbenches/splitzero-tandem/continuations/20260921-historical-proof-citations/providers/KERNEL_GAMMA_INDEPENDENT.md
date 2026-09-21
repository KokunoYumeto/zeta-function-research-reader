# Independent derivation of the complete Gamma reduction for the original kernel

Date: 2026-09-20. Checked source: `JOINT_MINIMUM_RECEIVERS.tex`, JM21–JM28,
in this directory. All constants and all displayed inequalities in those
equations are accepted. The only textual correction is the reference to
P5: P5 is the tail estimate, whereas the multiplier estimate used here is
the Gamma multiplication estimate in its proof, written explicitly as C4
in `COERCIVITY_INDEPENDENT.md`.

The result retains the actual fixed kernel of the original observation.
Its dimension `m_K=8k-16` and the simple-packet formula `q=(k+1)^2` are
used on their original five-orbit domain. No kernel frame is selected or
altered in this derivation. The asymptotic limit is along that domain with
`k congruent to 1 modulo 4`.

## 1. Exact convolution density and its mass

Keep
\[
\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi},\quad
w_h(y)=\frac{|(2\xi/h)(1/2+iy)|^2}{2\pi},\quad
M_\sigma=\sqrt{2\pi}.
\]
Neither measure is divided by its mass. To check every convolution
constant, use the Fourier convention
\[
\widehat f(t)=\int_{\mathbb R}e^{-ity}f(y)\,dy.
\]
For any a>0 the beta integral gives
\[
\frac{\Gamma(a+ix)\Gamma(a-ix)}{\Gamma(2a)}
=\int_{-\infty}^{\infty}e^{ixv}(2\cosh(v/2))^{-2a}\,dv.
\tag{KG1}
\]
For completeness, multiply the two Euler integrals for Gamma and set
`r=u+v`, `theta=u/(u+v)` in the positive quadrant. The Jacobian is r;
the r integral is Gamma(2a), and the remaining integral is
`integral_0^1 theta^{a+ix-1}(1-theta)^{a-ix-1} dtheta`.
Then set `z=log(theta/(1-theta))`, whose derivative is
`dtheta/dz=theta(1-theta)`. The resulting integrand is precisely the
right side of KG1. Absolute convergence is ensured by a>0.

The function `(2cosh(v/2))^{-2a}` and its first two derivatives are
integrable. Its Fourier transform is therefore integrable: on a bounded
interval it is bounded by the L1 norm, and outside that interval two
integrations by parts give a constant times |x|^{-2}. Fourier inversion
thus applies to KG1 as an ordinary absolutely convergent integral.
After the exact substitution y=2x it gives
\[
\int_{\mathbb R}e^{-ity}
\frac{|\Gamma(a+iy/2)|^2}{2\pi}\,dy
=\frac{2\Gamma(2a)}{(2\cosh t)^{2a}}.
\tag{KG2}
\]
In particular
\[
\widehat\sigma(t)=M_\sigma(\cosh t)^{-1/2},\qquad
\int\sigma=M_\sigma.
\]
For the k-fold convolution, multiplication of Fourier transforms and KG2
with a=k/4 give
\[
\sigma^{*k}(y)=
\frac{M_\sigma^k2^{k/2-1}}{\Gamma(k/2)}
\frac{|\Gamma(k/4+iy/2)|^2}{2\pi}.
\tag{KG3}
\]
Both sides are integrable, and their Fourier transforms agree; uniqueness
of the Fourier transform proves the equality. Integrating either side
shows that the mass is exactly `M_sigma^k=(2pi)^{k/2}`.

Now put `ell=(k-1)/4`. The Gamma recurrence gives
\[
|\Gamma(1/4+\ell+iy/2)|^2
=4^{-\ell}\prod_{j=0}^{\ell-1}
 \left[y^2+(2j+1/2)^2\right]|\Gamma(1/4+iy/2)|^2.
\]
Since `2^{k/2-1}4^{-ell}=2^{-1/2}`, KG3 becomes
\[
\boxed{\sigma^{*k}(y)=c_k\prod_{j<\ell}(y^2+b_j^2)\sigma(y),
\quad b_j=2j+\tfrac12,\quad
c_k=\frac{(2\pi)^{k/2}}{\sqrt2\,\Gamma(k/2)}.}
\tag{KG4}
\]
This proves the exact JM21 constant. When k=1, ell=0 and c_1=1;
empty products therefore reproduce the original measure.

## 2. The whole polynomial comparison

Set `n=2q`, `a=a_{h,n}`, and `b=b_{h,n}`, with exactly the constants
proved in P1–P2 and C16–C19 of `COERCIVITY_INDEPENDENT.md`. The finite
positive form inequality on one-factor degree at most n is
\[
a\|Q\|_\sigma^2\le\|Q\|_{w_h}^2\le b\|Q\|_\sigma^2.
\]
Tensor products of positive matrices preserve this order, with factors
a^k and b^k. For a scalar polynomial P of degree at most n, retain the
physical total variable
\[
S=s_1+\cdots+s_k=k/2+i(y_1+\cdots+y_k)=c+iy,
\qquad c=k/2.
\]
The polynomial `P(s_1+...+s_k)` has separate degree at most n. Its tensor
norm is exactly its scalar convolution norm. Thus
\[
a^k\|P(c+i\,\cdot)\|_{\sigma^{*k}}^2
\le\|P(c+i\,\cdot)\|_{w_h^{*k}}^2
\le b^k\|P(c+i\,\cdot)\|_{\sigma^{*k}}^2.
\tag{KG5}
\]
This retains the complete form, including cross terms between every
pair of coefficients and every relation candidate.

The monic Gamma basis has norms and recurrence
\[
\gamma_j=M_\sigma j!(1/2)_j,\qquad
p_0=1,\quad p_1=y,\quad
p_{j+1}=yp_j-j(j-1/2)p_{j-1}.
\tag{KG6}
\]
These formulas were checked from DLMF 18.19.8–9 and 18.23.7 in C1–C3
of `COERCIVITY_INDEPENDENT.md`, with the original measure retained.
The two off-diagonal coefficients in its orthonormal basis are
`sqrt(j(j-1/2))`. Consequently a polynomial Q of degree at most m satisfies
\[
\|yQ\|_\sigma\le2(m+1)\|Q\|_\sigma.
\tag{KG7}
\]
Indeed each of the two shifted coefficient vectors has norm at most
`sqrt((m+1)(m+1/2))||Q||` or `sqrt(m(m-1/2))||Q||`; their sum is at
most `2(m+1)||Q||`.

For `u_j=2(n+j+1)+b_j`, KG7 and the triangle inequality give
\[
\|(y+ib_j)Q\|_\sigma\le u_j\|Q\|_\sigma
\quad\text{when }\deg Q\le n+j.
\]
After j preceding factors, the degree is at most n+j. Iteration therefore
gives exactly
\[
\left\|\prod_{j<\ell}(y+ib_j)P(c+iy)\right\|_\sigma^2
\le\left(\prod_{j<\ell}u_j^2\right)
\|P(c+i\,\cdot)\|_\sigma^2.
\tag{KG8}
\]
The matching lower bound uses the pointwise inequality
`prod(y^2+b_j^2)>=prod b_j^2`. Combining KG4, KG5, and KG8 proves
\[
\boxed{\alpha_k\|P(c+i\,\cdot)\|_\sigma^2
\le\|P(c+i\,\cdot)\|_{w_h^{*k}}^2
\le\beta_k\|P(c+i\,\cdot)\|_\sigma^2,}
\tag{KG9}
\]
\[
\alpha_k=a^kc_k\prod_{j<\ell}b_j^2,\qquad
\beta_k=b^kc_k\prod_{j<\ell}u_j^2.
\]
This is JM22. The source measure on the right and left of KG9 is the
order-one Gamma measure in the variable y, while the physical scalar
coordinate remains S=c+iy throughout.

The finite logarithmic width is therefore
\[
L_k^{\rm form}=\log(\beta_k/\alpha_k)
=k\log(b/a)+2\sum_{j<\ell}\log(u_j/b_j)\ge0.
\tag{KG10}
\]
The scalar c_k cancels in this ratio; it was included in both bounds
before the cancellation. There is also an explicit upper bound for the
second term. Since
\[
\frac{u_j}{b_j}=2+\frac{2n+3/2}{2j+1/2}\le4n+5,
\]
one has
\[
0\le L_k^{\rm form}\le k\log(b/a)+2\ell\log(4n+5)
=O_h(k\log^2(q+2)).
\tag{KG11}
\]
This verifies JM23, with no hidden scalar mass and no root-gap estimate.

## 3. Quotient first, actual kernel restriction second

Let E=C[S]/(chi_k(S)) be the unchanged original scalar quotient of
dimension q. For every `q-1<=N<=2q`, let `J_N:P_{<=N}->E` be the
original remainder map. For each v in E its affine fibre is nonempty.
The complete physical minimum and Gamma minimum are
\[
v^*G_Nv=\min_{J_NP=v}\|P(c+i\,\cdot)\|_{w_h^{*k}}^2,
\qquad
v^*G_N^\sigma v=\min_{J_NP=v}\|P(c+i\,\cdot)\|_\sigma^2.
\tag{KG12}
\]
These minima exist because the spaces are finite-dimensional and their
norm matrices are positive definite. Apply KG9 to every polynomial in
the identical fibre. Taking the minima of the three forms gives
\[
\alpha_kG_N^\sigma\preceq G_N\preceq\beta_kG_N^\sigma.
\tag{KG13}
\]
No relation vector has been omitted, and no polynomial representative
has been fixed before minimizing.

Let the original fixed kernel be `K=ker Lambda_O`, and let
`I_K:C^{m_K}->E` be its actual injective frame map. Set
\[
H_{K,N}=I_K^*G_NI_K,\qquad
H_{K,N}^\sigma=I_K^*G_N^\sigma I_K.
\]
Restriction of KG13 is a congruence by that same I_K. Both restricted
matrices are positive definite. The eigenvalues of
`(H_{K,N}^sigma)^{-1/2}H_{K,N}(H_{K,N}^sigma)^{-1/2}` lie in
[alpha_k,beta_k], so the product of its m_K eigenvalues yields
\[
m_K\log\alpha_k\le e_N\le m_K\log\beta_k,\qquad
e_N=\log\det H_{K,N}-\log\det H_{K,N}^\sigma.
\tag{KG14}
\]
This is JM24. It is the restriction of the full quotient metric; it is
not obtained by retaining selected coefficient directions before the
quotient minimum.

Use the four original signs
\[
\mathcal Re=e_{q-1}+e_q-e_{2q-1}-e_{2q}.
\]
All four e_N belong to the same interval of length m_K L_k^{form}.
Pair the first term with the third and the second with the fourth.
Each difference has absolute value at most that length; hence
\[
\boxed{\left|\mathcal R\log\det H_{K,N}
-\mathcal R\log\det H_{K,N}^\sigma\right|
\le2m_KL_k^{\rm form}.}
\tag{KG15}
\]
No monotonicity of the errors e_N is assumed. This verifies the factor
2 in JM25. The common scalar `m_K log c_k` in each e_N cancels in this
four-sign expression as well.

On the actual simple-packet domain,
\[
2m_KL_k^{\rm form}=O_h(k^2\log^2(q+2)),\quad
\frac{k^2\log^2(q+2)}{kq}
=\frac{k\log^2((k+1)^2+2)}{(k+1)^2}\longrightarrow0.
\tag{KG16}
\]
Thus the error is o_h(kq), as stated, while retaining all roots and
the entire original kernel.

## 4. Exact covariance in the transported quotient

To specify the coordinate change completely, if chi_k is monic of degree
q, set
\[
Q(y)=i^{-q}\chi_k(c+iy).
\]
This is monic and retains every original root with its full multiplicity;
the root lambda is transported to `(lambda-c)/i`. The substitution
\[
T:E\longrightarrow E_y=\mathbb C[y]/(Q),\qquad
T[P]=[P(c+iy)]
\tag{KG17}
\]
is an isomorphism, with inverse substitution `y=(S-c)/i`. Its coefficient
matrix is triangular with diagonal `1,i,...,i^{q-1}`. The transported
kernel frame is `I_{K,y}=T I_K`. The matrices transform as
\[
G_{N,y}^\sigma=(T^{-1})^*G_N^\sigma T^{-1},\qquad
C_{N,y}^\sigma=T C_N^\sigma T^*.
\]
Consequently
`I_{K,y}^*G_{N,y}^sigma I_{K,y}=I_K^*G_N^sigma I_K` exactly. No
coordinate determinant or kernel-frame factor is lost.

In E_y use the standard coefficient frame of degree below q and define
\[
v_j=\operatorname{rem}_Qp_j,
\]
where p_j and gamma_j are exactly KG6. The orthonormal source basis
is `p_j/sqrt(gamma_j)`, for all `0<=j<=N`; its remainder matrix has
columns `v_j/sqrt(gamma_j)`. Thus its complete covariance is
\[
C_{N,y}^\sigma=\sum_{j=0}^N\frac{v_jv_j^*}{\gamma_j}.
\tag{KG18}
\]
For j<q, p_j already has degree below q, so v_j=p_j. The first q
columns are triangular with diagonal one. They have full rank, proving
`C_{N,y}^sigma>0` for every N>=q-1.

For a direct proof of the minimum formula, let B be this remainder matrix
on orthonormal source coefficients. Since BB*=C>0, the coefficient
vector `B^*C^{-1}v` has value v and norm squared `v^*C^{-1}v`.
Every other coefficient vector with value v differs from it by ker B,
which is orthogonal to im B*. Its squared norm therefore equals that
minimum plus the squared norm of the difference. It follows that
\[
G_{N,y}^\sigma=(C_{N,y}^\sigma)^{-1},\qquad
\boxed{H_{K,N}^\sigma=I_{K,y}^*(C_{N,y}^\sigma)^{-1}I_{K,y}.}
\tag{KG19}
\]
These are JM26–JM27 with the coordinate transport specified. The inverse
is taken on the complete q-dimensional value space before restriction
to the actual m_K-dimensional kernel. In general
`I_K^*C^{-1}I_K` is different from `(I_K^*C I_K)^{-1}`; only the former
is proved and used here. Every column through degree N is present in
KG18, so every earlier scalar relation enters the minimum.

## 5. The actual change to the joint kernel metric

Keep the same section at all four cutoffs, as in J3–J11. The already
proved joint form enclosure and nesting give
\[
0\le\mathcal R\log\det H_{K,N}^J\le2m_KW,
\qquad W=k\log(\tau_\eta\Lambda_{h,2q}).
\tag{KG20}
\]
By definition
`Delta_{K,N}=log det H_{K,N}-log det H_{K,N}^J`. Combine KG15 with
both endpoints of KG20 to obtain
\[
\boxed{\begin{aligned}
\mathcal R\log\det H_{K,N}^\sigma-2m_K(L_k^{\rm form}+W)
&\le\mathcal R\Delta_{K,N}\\
&\le\mathcal R\log\det H_{K,N}^\sigma+2m_KL_k^{\rm form}.
\end{aligned}}
\tag{KG21}
\]
This is JM28, with its signs and asymmetric error terms unchanged.
At the declared polynomial tolerances, `W=O_h(k log^2(q+2))`; thus
both errors are o_h(kq) by KG16. More specifically, for the actual
simple one-factor divisor, `d_max=0`, `tau_eta=L_h`, and W is independent
of eta altogether. The polynomial-tolerance statement is therefore
valid, and on this simple domain the same error bound holds for every
positive eta at most one when the section is fixed across cutoffs.

The derived expression KG19 is the full finite Gamma receiver needed
for the next kernel calculation. The reduction preserves a possible
kq coefficient of its four-return, but does not assign that coefficient
without evaluating the determinant asymptotics in the actual frame.

## Reading and use record

The primary task source actually read was the displayed section of
`JOINT_MINIMUM_RECEIVERS.tex` containing JM21–JM28. The prior independent
proof `COERCIVITY_INDEPENDENT.md` supplies P2 and the exact Gamma basis
and multiplier estimates; its original DLMF TeX files and precise reading
record remain in `coercivity_sources/` and its Section 11. The convolution
identity and every new error estimate were derived above from the exact
Gamma Euler integrals and those already checked inputs. No additional
literature, numerical experiment, rendering, build, or publication is
represented as performed.
