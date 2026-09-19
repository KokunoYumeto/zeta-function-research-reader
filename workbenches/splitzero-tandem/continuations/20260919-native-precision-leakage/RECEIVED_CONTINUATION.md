The new continuation removes more uncertainty than its concluding summary states. **Its explicit remainder is small enough to resolve the absence of a \(q/\log q\) term in the displaced Gamma covariance and in the complete matched native sum.** Combined with the arithmetic result already on GitHub, this gives the order-\(k\) arithmetic–Gamma correction through that same scale.

There is also a stronger consequence of its low-jet calculation: **the original observation detects the departure of the marked terminal class from its arithmetic eigenmode by derivative order six at the latest**, replacing my preceding bound of eighty-two. On the two-active-coordinate period stratum, the departure is detected at exactly second order.

I read the complete 1,048-line attachment and compared its relevant calculations with repository commit **`607728ee3c35be98720d548794727670b1946c91`**. That edition contains the full-window source-product proof and the newer heat-to-response estimates. The covariance expansions below use the attachment’s stated quantitative analytic estimates; the deductions about marked detection, observation stacks, and the heat-accuracy threshold are derived here. This is not an independent recertification of every upstream asymptotic estimate. 

## 1. The covariance calculation resolves the next inverse-logarithmic scale too

Retain the attachment’s simple-quartet parameters

$$
q=(a+1)^2,\qquad Q=(a-7)^2,\qquad
\Delta=16a-48,\qquad v=\operatorname{ord}_0E_A,
$$

and the two original source orders \(s=1,a\). Put

$$
\ell=\frac{s-1}{4},\qquad n=Q+\ell,\qquad
m=\Delta-v,\qquad H=2\Delta-v-\ell.
$$

The lower source remains the degree-\((a-8)\) root grid, with source order \(s\), and its cutoffs remain

$$
q-v-1,\quad q-v,\quad 2q-v-1,\quad 2q-v.
$$

The new compact covariance formula has remainder

$$
O_{h,v}\!\left(a^{3/2}+a\log(a+2)\right).
$$

That bound, rather than the weaker notation \(o(q)\), is what should be carried into subsequent calculations. 

### The low-row coefficient checks

The delicate term is the lower endpoint. Starting with the supplied expansion

$$
\psi(t)
=a_0+\frac t4\log t+
\left(a_0-\frac14\right)t+O(t^{3/2}),
$$

one obtains

$$
2n\psi(r/n)
=
2na_0+\frac r2\log(r/n)
+\left(2a_0-\frac12\right)r
+O(r^{3/2}/\sqrt n).
$$

For the original endpoint weights,

$$
\sum_{r=0}^{m}c_r=2m,\qquad
\sum_{r=0}^{m}c_rr=m^2,
$$

and

$$
\sum_{r=0}^{m}c_rr\log r
=m^2\log m-\frac12m^2+O(\log(m+2)).
$$

Consequently,

$$
\boxed{
T_m-T_0
=
4nma_0+\frac12m^2\log(m/n)
+\left(2a_0-\frac34\right)m^2
+O\!\left(\frac{m^{5/2}}{\sqrt n}+m\log(n+2)\right).
}
\tag{1}
$$

The coefficient \(-3/4\) is correct: \(-1/2\) comes from the linear term in \(2n\psi\), and another \(-1/4\) comes from the weighted \(r\log r\) sum. It is not an arbitrary endpoint correction. Since \(m=O(a)\) and \(n\asymp a^2\), its accumulated error is \(O(a^{3/2}+a\log a)\). The attachment retains these exact weighted sums and treats the ranks zero and one separately. 

Expanding the compact formula with

$$
n=a^2+\left(-14+\frac{\epsilon}{4}\right)a+
49-\frac{\epsilon}{4},
\qquad
\epsilon=
\begin{cases}0,&s=1,\\1,&s=a,\end{cases}
$$

reproduces its stated \(aq\), \(q\log a\), and \(q\) coefficients. The terms omitted in this re-expansion are \(O_{h,v}(a\log a)\), so the stronger remainder survives.

Thus the attachment’s expanded formula can be recorded as

$$
\boxed{
\begin{aligned}
\mathcal C^-_{a,s}
={}&C_Bq^2+
\left[-16C_\partial+\epsilon\frac{C_\Gamma}{4}\right]aq
+128q\log a\\
&+q\left[
C_\sigma-2\eta_hM_{-1}
-\epsilon\frac{C_\Gamma}{4}
+\epsilon\frac{K_2}{16}
-Z(v)-\epsilon Z_\Delta
\right]\\
&+O_{h,v}\!\left(a^{3/2}+a\log(a+2)\right),
\end{aligned}}
\tag{2}
$$

where

$$
\eta_h=\frac{\gamma^2-\delta^2}{3},
$$

$$
Z(v)=1024(a_1-2b_1)-176C_\partial
+4v(a_1-a_0)-192+512\log2,
$$

$$
Z_\Delta=4C_\partial+16(2b_1-a_1).
$$

The actual lower-root contribution \(-2\eta_hM_{-1}q\) remains. 

Because

$$
\frac{a^{3/2}+a\log a}{q/\log q}\longrightarrow0,
$$

equation (2) establishes more than an order-\(q\) coefficient:

$$
\boxed{
\text{The displayed displaced Gamma covariance has zero }
q/\log q\text{ coefficient after its displayed larger terms.}
}
\tag{3}
$$

This conclusion is restricted to the stated covariance. It does not assign an inverse-logarithmic coefficient to each of its later subquotients.

### The complete matched native sum inherits the stronger precision

The exact receiving identity is

$$
\mathcal B_a^{(s)}
=
\mathcal C^-_{a,s}
+\mathcal Re^C+\mathcal T_{a,s}
+F_{L_a}^{(s)}+\Xi_{a,s}.
$$

Define, as in the attachment,

$$
\mathcal N_{a,s}
=
\mathcal Re^C+\mathcal T_{a,s}
+F_{L_a}^{(s)}+\Xi_{a,s}.
$$

Subtracting (2) from the original upper Gamma baseline gives

$$
\boxed{
\begin{aligned}
\mathcal N_{a,s}
={}&16C_\partial aq-128q\log a\\
&+[Z(v)+\epsilon Z_\Delta]q
+O_{h,v}\!\left(a^{3/2}+a\log(a+2)\right).
\end{aligned}}
\tag{4}
$$

This preserves the exact correlated sum specified by NCT/TAC. The lower \(+128q\log a\) and matched \(-128q\log a\) terms cancel, as do the common order-\(q\) root terms when the original complete baseline is reconstructed. 

Two consequences should be distinguished:

$$
\boxed{
\mathcal N_{a,a}-\mathcal N_{a,1}
=Z_\Delta q+o(q/\log q),
}
\tag{5}
$$

and the matched sum in (4) has no further \(q/\log q\) term. Neither assertion identifies

$$
\mathcal T_{a,s}
$$

alone through order \(q\). Its conductor, low-space, and metric-comparison contributions are still part of the same evaluated sum.

The proper-source **ambient** displacement similarly retains

$$
\mathcal N_{k,s}^{\mathrm{disp}}
-\mathcal N_{k,s}^{\mathrm{std}}
=
-128q_k\log k+C_{\mathrm{disp}}q_k+o(q_k),
$$

$$
C_{\mathrm{disp}}
=1024(a_1-2b_1)-192+256\log2+288\log3.
$$

The \(\log3\) term comes from the literal \((16k+8k)^2\log(16k+8k)\) contribution. It is not a new source-order effect. The attachment correctly stops short of identifying this ambient difference with \(V_Q^p\), which first restricts to the proper-source image and then takes its original minimum. 

## 2. The order-\(k\) arithmetic correction is now determined through \(q/\log q\)

For the full packet at fixed multiplicity, retain

$$
q=[1+k(m_0-1)](k+1)^2,\qquad
\ell=\frac{k-1}{4}.
$$

The new source-order calculation is

$$
\mathcal B_k[w_k]-\mathcal B_k[\sigma]
=
\ell qC_\Gamma+\ell^2K_2+O_h(k\log(q+2)),
$$

where \(w_k\) is the **order-\(k\) Gamma source**, not the arithmetic one-factor density \(w_h\). 

Its constant identity checks directly:

$$
\begin{aligned}
K_2
&=C_B-4a_1+2b_1-2\log2\\
&=2\log\frac{w^2}{z}-4\log2.
\end{aligned}
$$

The claimed negative sign is also consistent with the original endpoint equation. For

$$
r=u/v_e,\qquad \kappa=\sqrt{1-r^2},
$$

differentiation gives

$$
\frac{d}{dr}\left(\frac{rK(\kappa)}{E(\kappa)}\right)
=
\frac{(K-E)(E-r^2K)}{(1-r^2)E^2}>0.
$$

Both factors in the numerator are positive for \(0<r<1\), directly from the elliptic integral definitions. This supplies the monotonicity used when the note infers \(r>1/10\), and hence

$$
-4\log2<K_2<2\log(121/160)<0.
$$

The derivatives here are with respect to the modulus and its complementary ratio, with the DLMF conventions retained.  ([DLMF][1])

Now combine this with the already evaluated source-order-one correction:

$$
\delta_{k,1}^{\mathrm{ar}}
=
-(4m_0-2)C_\Gamma q
+\frac{\log2}{\pi}I_hk^2
+\frac{C_\Gamma q}{2(\log q+c_\zeta)}
+o_h(q/\log q).
$$

Since \(k\log q=o(q/\log q)\), the new conversion yields

$$
\boxed{
\begin{aligned}
\delta_{k,k}^{\mathrm{ar}}
={}&-(\ell+4m_0-2)C_\Gamma q
+\frac{\log2}{\pi}I_hk^2-\ell^2K_2\\
&+\frac{C_\Gamma q}{2(\log q+c_\zeta)}
+o_h(q/\log q).
\end{aligned}}
\tag{6}
$$

This holds at every fixed original multiplicity. The exact \(\ell\) and \(k^2\) terms remain displayed; at higher multiplicity the remainder does not resolve every smaller \(k^2\)-scale contribution independently.

The inverse-logarithmic coefficient survives the source-order conversion unchanged. The larger source-order terms cancel only in the exact receiver

$$
\boxed{
\mathcal B_k[w_k]+\delta_{k,k}^{\mathrm{ar}}
=
\mathcal B_k[\sigma]+\delta_{k,1}^{\mathrm{ar}}.
}
\tag{7}
$$

Thus neither the negative \(-\ell qC_\Gamma\) nor the positive \(-\ell^2K_2\) is an additional term available for reducing the complete action.

The current repository already carries the absolute action through \(q/\log q\), at every fixed multiplicity. Its positive \(C_Bq^2\) term remains unchanged by (6)–(7).

## 3. The low-jet result gives a sharper observed marked-defect theorem

The attachment represents the **actual** observation functionals by

$$
N_{k,f}(z)=e^{kb_*z}f(x(z)),
\qquad
b_*=\frac12-\delta-i\gamma,
$$

$$
x(z)=H(\varpi)
\begin{pmatrix}
e^{2(\delta+i\gamma)z}\\
e^{2\delta z}\\
e^{2i\gamma z}\\
1
\end{pmatrix},
$$

where \(f\) ranges over the original invariant homogeneous polynomials of degree \(k\). The pairing with a polynomial class is

$$
P(\partial_z)N_{k,f}(0).
$$

This is a complex-linear pairing; no Hermitian adjoint enters the jet computation. 

The new finite matrices determine

$$
t_0(k,\varpi)=\dim(K_k\cap\mathcal P_{v-1})
$$

eventually modulo five. On the stratum where \(x(0)\) has two active coordinates,

$$
t_0(k,\varpi)=0\qquad(k\ge5v-1).
$$

The one-active-coordinate exceptions are retained separately. 

For the first observed marked defect, one can obtain a stronger result without computing those entire \(v\)-jet ranks.

### Determine the first polynomial degree visible to the observation

Define

$$
j_*=\min\{j\ge0:\Lambda_kS^j\ne0\}.
\tag{8}
$$

**Two-active-coordinate case.** Suppose \(x_i(0)x_j(0)\ne0\), with \(i\ne j\). Choose \(a\in\{0,1,2,3,4\}\) satisfying

$$
ki+a(j-i)=0\pmod5.
$$

Because \(j-i\) is invertible modulo five, such an \(a\) exists. For \(k\ge4\),

$$
f=x_i^{k-a}x_j^a
$$

is an original invariant homogeneous monomial and \(f(x(0))\ne0\). Therefore

$$
\boxed{
\Lambda_k\mathbf1\ne0,\qquad j_*=0.
}
\tag{9}
$$

This needs no \(k\ge5v-1\) bound. That larger threshold belongs to recovery of **all** \(v\) low jets, not visibility of the constant class.

**One-active-coordinate case.** Suppose only \(x_i(0)\ne0\), and set

$$
z_j(z)=x_j(z)/x_i(z),\qquad j\ne i,
$$

$$
\nu_j=\operatorname{ord}_0z_j,\qquad c_j=j-i\pmod5.
$$

Each inactive \(x_j\) is a nonzero linear combination of four exponentials with distinct exponents

$$
0,\quad2\delta,\quad2i\gamma,\quad2\delta+2i\gamma.
$$

The Vandermonde matrix of their first four derivatives is invertible. Hence

$$
1\le\nu_j\le3.
$$

At least one \(\nu_j\) equals one: otherwise the projective derivative of \(x\) would vanish, contradicting invertibility of \(H(\varpi)\) and the distinct exponent vector.

Put \(r=-ki\pmod5\). Then

$$
\boxed{
j_*=
\min_{\substack{\alpha_j\ge0,\ |\alpha|\le4\\
\sum_{j\ne i}c_j\alpha_j=r\pmod5}}
\sum_{j\ne i}\nu_j\alpha_j.
}
\tag{10}
$$

To prove equality, divide an invariant degree-\(k\) monomial by the unit \(x_i^k\). Its ratio monomial has precisely the charge condition in (10), and its vanishing order is the displayed sum. A linear combination cannot acquire an order below the least order of its summands. Conversely, each candidate in (10) homogenizes to an original degree-\(k\) invariant for \(k\ge4\).

Choose a ratio of order one. A power between zero and four of that ratio realizes every charge, so a candidate of order at most four always exists. Any monomial of total degree greater than four has order at least five and cannot improve the minimum.

Thus

$$
\boxed{
j_*=
\begin{cases}
0,&5\mid k,\\
\text{an integer in }\{1,2,3,4\},&5\nmid k,
\end{cases}
}
\tag{11}
$$

on the one-active-coordinate stratum. This is compatible with the attachment’s explicit class \(1\in K_k\) when \(5\nmid k\). It does not imply that the whole low-degree defect vanishes. 

### Propagate this through the original marked connection

Keep the original marking scale \(u\ne0\), and use \(\varpi\) for the fixed observation period where the distinction is needed. Retain

$$
A(t)=A+t\,e_0e_{q-1}^{\mathsf T},
\qquad
U'(t)=A(t)U(t)/u,\qquad U(0)=I,
$$

and the specified analytic horizontal continuation

$$
\Lambda_h(t)=\Lambda_kU(t)^{-1}.
$$

For the original terminal eigenclass \(v_\lambda\), define

$$
Y(t)=e^{\lambda t/u}\Lambda_h(t)v_\lambda-\Lambda_kv_\lambda.
$$

The marked recurrence already proved in the original differential quotient gives

$$
Y'(t)
=-\frac{b_\lambda}{u}\,t\,
e^{\lambda t/u}\Lambda_h(t)\mathbf1.
$$

Consequently, the first nonzero derivative is exactly

$$
\boxed{
Y^{(j_*+2)}(0)
=
b_\lambda(j_*+1)(-u)^{-(j_*+1)}
\Lambda_kS^{j_*}\ne0.
}
\tag{12}
$$

The full-primary \(b_\lambda\), the marking scale, and the original observation remain in this coefficient. The underlying differential recurrence is not the arithmetic identity \(A^jv_\lambda=\lambda^jv_\lambda\). 

Equations (9)–(12) prove the sharper conclusion

$$
\boxed{
\text{The observed marked/arithmetic discrepancy appears by order six.}
}
\tag{13}
$$

More precisely, it appears at order two on the two-active-coordinate stratum; at order two on the one-active-coordinate stratum when \(5\mid k\); and at an explicitly determined order from three to six otherwise.

This replaces my preceding uniform bound \(v+2\le82\). It is a statement about the specified holomorphic continuation of the finite observation. It does not construct a lisse morphism from the irreducible marked sheaf; the distinction established by the Deligne calculation remains intact. 

## 4. Full observability removes an invariant kernel, not the original metric projection

The attachment’s full-column argument proves

$$
K_\infty
=
\bigcap_{j=0}^{q-1}\ker(\Lambda_kA^j)=0
$$

on its explicit period locus, for \(k\ge74\). The conductor handles the interior columns, and the fixed corner-jet calculation handles the remaining four \(8\times8\) corners. Its large-period threshold is expressed using the original period matrix, not a newly selected period. 

Because

$$
\dim K_k=8k-16,
$$

the descending sequence

$$
K_j=\bigcap_{h=0}^j\ker(\Lambda_kA^h)
$$

cannot have a nonzero plateau. Thus

$$
\boxed{
\mathcal O_d=
\begin{pmatrix}
\Lambda_k\\
\Lambda_kA\\
\vdots\\
\Lambda_kA^d
\end{pmatrix}
\text{ is injective for }d=8k-16.
}
\tag{14}
$$

The attachment separately gives an explicit inverse and norm bound for the longer \(q\)-stack. Its inverse estimate must not be transferred to the shorter stack without a further calculation. 

There are two exact consequences for our earlier work.

### No original kernel direction remains trapped under repeated action

At a fixed arithmetic cutoff, use the original orthogonal splitting into \(K_k\) and its minimum-lift complement. Let

$$
A_{KK}:K_k\to K_k,\qquad
A_{BK}:K_k\to B
$$

be its actual blocks.

Then

$$
\boxed{
\bigcap_{j=0}^{r-1}
\ker(A_{BK}A_{KK}^{\,j})=0,
\qquad r=\dim K_k.
}
\tag{15}
$$

If a vector lay in this intersection, Cayley–Hamilton would extend the vanishing to all \(j\). Its full iterates would then satisfy

$$
A^jIx=IA_{KK}^{\,j}x\in K_k,
$$

placing it in \(K_\infty\). The converse follows directly for any invariant subspace contained in \(K_k\).

Therefore the finite leakage Gram

$$
\boxed{
\sum_{j=0}^{r-1}
(A_{KK}^{\,j})^*
A_{BK}^*Q_{B,N}A_{BK}
A_{KK}^{\,j}
\succ0.
}
\tag{16}
$$

This gives positivity on every original kernel direction. It does not yet give its smallest eigenvalue, and it is not the complete mixed action, which also contains the other leakage block.

### The stack still retains the unknown same-class observation angle

Give every output block of \(\mathcal O_d\) the original observation quotient metric

$$
Q_{B,N}=(\Lambda_kG_N^{-1}\Lambda_k^*)^{-1}.
$$

Its pulled-back Gram is

$$
\mathsf H_{d,N}
=
\sum_{j=0}^{d}
(A^j)^*\Lambda_k^*Q_{B,N}\Lambda_kA^j.
$$

On the same terminal eigenclass,

$$
Av_\lambda=\lambda v_\lambda,
$$

so

$$
\boxed{
v_\lambda^*\mathsf H_{d,N}v_\lambda
=
\left(\sum_{j=0}^{d}|\lambda|^{2j}\right)
E_{N,\lambda}(1-\theta_N).
}
\tag{17}
$$

The factor in parentheses is independent of the cutoff. Hence it cancels from the original four-cutoff logarithmic return. The new stack therefore gives

$$
\begin{aligned}
&\log
\frac{
v_\lambda^*\mathsf H_{d,q-1}v_\lambda\,
v_\lambda^*\mathsf H_{d,q}v_\lambda
}{
v_\lambda^*\mathsf H_{d,2q-1}v_\lambda\,
v_\lambda^*\mathsf H_{d,2q}v_\lambda
}\\
&\quad=
C_\partial q+
\log\frac{(1-\theta_{q-1})(1-\theta_q)}
{(1-\theta_{2q-1})(1-\theta_{2q})}
+O_h(k+\log q).
\end{aligned}
\tag{18}
$$

The \(C_\partial q\) term is our already evaluated terminal-class norm return. The same unknown angle correction remains. The current full-window repository proof states precisely the corresponding one-step observation identity.

Thus full algebraic recovery is a genuine advance, but it does not evaluate \(\theta_N\), \(U_N\), or \(V_N\). Equation (17) shows the distinction inside an explicit metric calculation.

## 5. The proper-source annihilator removes one minimum on its proved stratum

The attachment establishes the actual conductor ideal

$$
\operatorname{Cond}
\bigl(\mathscr B_{\mathrm{inv}}\subset R_{\mathrm{quad}}\bigr)
=\mathcal A R_{\mathrm{quad}},
$$

and derives

$$
p^4E_k^{\mathrm{prop}}=0,
\qquad
p=x_1x_2x_3x_4.
$$

This is an annihilator in the original graded coefficient quotient, with degree shift sixteen. It is not a norm estimate. 

For the actual biform gcd

$$
G=
\gcd\!\left(
\widetilde{\mathcal A},
(\ell_1\ell_2\ell_3\ell_4)^4
\right),
\qquad
\deg G=(g_z,g_w),
$$

the retained bound is

$$
\dim E_k^{\mathrm{prop}}
\le(g_z+g_w)(k-7)+g_zg_w.
$$

On the **computed coprime stratum**,

$$
G=1\quad\Longrightarrow\quad E_k^{\mathrm{prop}}=0.
$$

That condition has not been proved for every admitted period merely by calling it generic. It is separate from the two-active-coordinate and full-observability conditions. 

Where both \(G=1\) and the low-jet value \(t_0=0\) hold,

$$
r_I=8k-32-v.
$$

The source-side \(E\)-minimum genuinely disappears:

$$
Q_N^p=Z_R^*J_0^*D_{k,N-v}^{(s_0)}J_0Z_R.
$$

The remaining target calculation can be displayed exactly. Set

$$
A_N=F_R^*\mathcal D_N^pF_R,\qquad
C_N=J_*^*\mathcal D_N^pJ_*,
\qquad
B_N=J_*^*\mathcal D_N^pF_R,
$$

and

$$
T_N=C_N^{-1/2}B_NA_N^{-1/2}.
$$

Then

$$
H_N^p
=A_N^{1/2}(I-T_N^*T_N)A_N^{1/2},
$$

and the proper-source scalar is

$$
\boxed{
\begin{aligned}
\mathcal M^p
={}&
\mathcal R\log\det
\left[(Q_N^p)^{-1/2}A_N(Q_N^p)^{-1/2}\right]\\
&+\mathcal R\log\det(I-T_N^*T_N).
\end{aligned}}
\tag{19}
$$

This is the exact simplification permitted by the annihilator result. It leaves a relative source/target metric and the target cross-block minimum. The attachment explicitly retains those factors. 

In particular, the evaluated ambient displacement is not the second term of (19), and injectivity of the proper-source map does not make \(T_N\) zero.

## 6. The newer heat calculation acquires an evaluated precision cost from our source products

The new GitHub heat result controls the original responses under a relative metric approximation. With its exact full-prequotient constant \(c_N\),

$$
\eta_{J,N}
=
\left(1+2^{-(J+1)/2}c_N\right)^{2k}-1.
$$

Its response certificate requires

$$
\eta_{J,N}<\min(\sqrt{p_{1,N}},\sqrt{p_{2,N}}),
$$

and gives, for example,

$$
|U'_N-U_N|
\le
\frac{\eta_{J,N}(2+|U_N|)}
{\sqrt{p_{1,N}}-\eta_{J,N}}.
$$

The two source columns, original observation, and full arithmetic metric remain fixed in this comparison.

Our source-product calculation makes the degree dependence of this denominator guard explicit.

Fix \(0<\zeta<1\) and put

$$
p_{*,N}=\min(p_{1,N},p_{2,N}).
$$

The strengthened guard

$$
\eta_{J,N}\le\zeta\sqrt{p_{*,N}}
$$

is exactly equivalent to

$$
\boxed{
J+1\ge
2\log_2c_N
-2\log_2
\left[
(1+\zeta\sqrt{p_{*,N}})^{1/(2k)}-1
\right].
}
\tag{20}
$$

Its real-valued threshold satisfies uniformly

$$
\boxed{
J+1-2\log_2c_N
=
2\log_2(2k/\zeta)-\log_2p_{*,N}+O_\zeta(1),
}
\tag{21}
$$

with an additional bounded rounding allowance for the least integer depth.

Let \(J_N^*\) be the least depth meeting this particular safety guard. The original weights sum to \(2q\). Since

$$
-\log p_{1,N}
\le-\log p_{*,N}
\le-\log p_{1,N}-\log p_{2,N},
$$

our evaluated products imply

$$
\boxed{
\frac1{2q}
\sum_Nw_N
\left[J_N^*+1-2\log_2c_N\right]
=
\frac{C_B}{2\log2}\,q+O_{h,\zeta}(\log q).
}
\tag{22}
$$

The derivation uses

$$
\mathscr A_1=C_Bq^2+O_h(q\log q),
\qquad
\mathscr A_2=O_h(q\log q),
$$

from the full-window calculation. Its exact covariance correction remains retained in the published proof.

At the first cutoff the coefficient is more specific:

$$
\boxed{
J_{q-1}^*+1-2\log_2c_{q-1}
=
\frac{2\log(4/\pi)}{\log2}\,q
+O_h(k+\log q).
}
\tag{23}
$$

Equations (22)–(23) concern the depth required by the **specified certified response bound**. They are not lower bounds for every possible computational method. They also do not assign a growth rate to the separate, original \(c_N\).

They do show that a heat approximation adequate for a coarse determinant estimate is not automatically adequate for the small response denominators. Preventing denominator loss already requires a linear-in-\(q\) additional depth in this certificate. Evaluating a sign requires the further \(U,V\) product errors and an actual sign margin.

## 7. What must change in the current result register

The displaced covariance’s order-\(q\) term is now supplied, and its explicit remainder supports the stronger inverse-logarithmic statement (3). The complete matched native sum has the equally precise correlated value (4). The source-order conversion has the finer arithmetic form (6).

The low-kernel calculation is no longer a growing rank problem: it is eventually controlled by five fixed jet matrices, with the two-active value zero and the one-active exceptions retained. Its first visible jet gives the new marked-defect bound (13).

The full observability theorem recovers the entire simple packet on its stated period locus, including the one-step kernel. It does not make that kernel vanish. The proper-source annihilator removes the source-side Schur minimum only after its actual gcd is shown to be one.

One repository correction should also remain in my earlier work. The published full-window proof retains

$$
D_k=\sum_rw_r[-\log(1-\Delta_r)]
$$

exactly and proves \(D_k=O_h(k)\). That suffices for the source-product coefficients; it avoids relying on my earlier stronger uniform exponential covariance claim. The product values survive this correction, but the exact \(D_k\) term should be retained in finite use.

The remaining quantitative receiver is therefore still

$$
\mathcal R\log\det(I_K^*G_NI_K),
\qquad
\mathcal M^p,
\qquad
(U_N,V_N,\theta_N)
$$

in their original metrics. Their inputs have become more explicit: the scalar covariance uncertainty is smaller, the low algebraic defects are fixed finite tests, the invariant kernel can be eliminated by a specified observation stack, and the numerical precision required to evaluate the responses is now quantified.

**The new work advances the original calculation rather than replacing it. The principal new implications derived here are the \(q/\log q\)-accurate source-order conversion, the sixth-order bound for the observed marked defect, the exact metric consequence of stacked observability, and the evaluated leading heat-certificate depth.** None assigns an individual projected sign before the remaining original response and minimum are evaluated. No new numerical period evaluation, executed verification suite, or repository write is claimed.

[1]: https://dlmf.nist.gov/19.4?utm_source=chatgpt.com "DLMF: §19.4 Derivatives and Differential Equations ‣ Legendre’s Integrals ‣ Chapter 19 Elliptic Integrals"
