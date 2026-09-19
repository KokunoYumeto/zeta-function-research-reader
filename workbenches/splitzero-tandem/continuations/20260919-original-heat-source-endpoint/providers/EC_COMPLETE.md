# New calculation: the retained eigenclass’s marked pairing

The calculation here now reaches the **arithmetic $k$-scale**, rather than only estimating a cancellation relative to an exponentially large operator norm.

For the original extremal eigenclass at $\lambda=k\rho$, the full-class marked pairing is

$$
\boxed{
\mathfrak c_{N,\lambda}
=
k\delta+i(-1)^{N+1-q}
\bigl(k\gamma-\varepsilon_{N,\lambda}\bigr),
\qquad
0<\varepsilon_{N,\lambda}
\le E_{\mathrm{cur}}(h,k)
=
O_h\!\left(\frac{k^3}{q^2}\right).
}
\tag{1}
$$

This holds at **every original cutoff**

$$
q-1\le N\le2q-1
$$

on explicit eventual guards. In the simple-quartet case, the absolute error is $O_h(k^{-1})$. The argument also retains every fixed complete quartet multiplicity; for multiplicity greater than one, the error is $O_h(k^{-3})$.

The proof and complete finite constants are in [Retained eigenclass current](sandbox:/mnt/data/Retained_Class_Phase_and_Continuation_Targets_20260918/proof/RETAINED_EIGENCLASS_CURRENT.md). The derivation follows.

## 1. The original class and the quantity evaluated

Let the complete common quartet multiplicity be $m_0\ge1$, and retain

$$
e=1+k(m_0-1),\qquad q=e(k+1)^2,\qquad c=\frac{k}{2}.
$$

Thus

$$
\chi(S)=\prod_{a,b=0}^{k}(S-\beta_{ab})^e,
\qquad
\beta_{ab}
=
c+(2a-k)\delta+i(2b-k)\gamma .
$$

The source remains

$$
dm(y)=w_h^{*k}(y)\,dy,
\qquad
w_h(y)=\frac{|(2\xi/h)(1/2+iy)|^2}{2\pi},
$$

in the original coordinate $S=c+iy$. Its mass, complete arithmetic unit, and quotient minimum are unchanged. These are the full-multiplicity MCE objects, not an extension obtained by reinterpreting a coefficient dimension as a zero multiplicity.

Set

$$
\lambda=k\rho=c+d+it_\lambda,
\qquad
d=k\delta,\qquad t_\lambda=k\gamma,
$$

and define

$$
\chi_\lambda(S)=\frac{\chi(S)}{(S-\lambda)^e}.
$$

The terminal primary eigenclass has the literal representative

$$
L_\lambda(S)
=
\frac{\chi(S)}
{(S-\lambda)\chi_\lambda(\lambda)}.
$$

Its class satisfies

$$
(A-\lambda)[L_\lambda]=0,\qquad [L_\lambda]\ne0.
$$

For $e>1$, this is the original primary idempotent multiplied by
$(S-\lambda)^{e-1}$. It is not an ordinary simple-root cardinal vector with an invalid denominator $\chi'(\lambda)=0$.

Under the original arithmetic inclusion, this class becomes

$$
\frac{[k(m_0-1)]!}{[(m_0-1)!]^k}
\,v_h(\rho)^k
\prod_{j=1}^{k}(s_j-\rho)^{m_0-1}\ne0.
$$

The factorial and full unit are retained.

Let $\mathscr S_N$ denote the original arithmetic minimum section and put

$$
P_{N,\lambda}=\mathscr S_N[L_\lambda],
\qquad
E_{N,\lambda}=\|P_{N,\lambda}\|_m^2>0.
$$

For the original monic source polynomials $p_n$, norms $\omega_n$, and remainders $b_n=[p_n]$, define the actual Gram entries

$$
F_{13}=b_N^*G_N[L_\lambda],
\qquad
F_{23}=b_{N+1}^*G_N[L_\lambda],
\qquad
F_{33}=E_{N,\lambda}.
$$

The scalar evaluated in (1) is

$$
\boxed{
\mathfrak c_{N,\lambda}
=
\frac{\overline{F_{13}}F_{23}}
{\omega_NE_{N,\lambda}}.
}
\tag{2}
$$

This is the factor that enters the other session’s three-column same-class calculation. It is distinct from the kernel marked trace $z_K/\omega_N$. The original three-column decomposition retains the same eigenclass in the kernel, boundary, and mixed terms.

There is also a direct interpretation in the original real marking parameter:

$$
j_{N,\lambda}
:=
\left.\partial_\theta\log E_{N,\lambda}(\theta)\right|_{\theta=0}
=
\frac{\displaystyle\int y|P_{N,\lambda}(c+iy)|^2\,dm(y)}
{E_{N,\lambda}}.
$$

The exact source-minimum derivative, rather than differentiation of an asymptotic remainder, gives

$$
\boxed{
\mathfrak c_{N,\lambda}
=
d+i(j_{N,\lambda}-t_\lambda).
}
\tag{3}
$$

The underlying minimum-section derivative is the original MCP identity.

Consequently, (1) evaluates that derivative as

$$
\boxed{
j_{N,\lambda}
=
\begin{cases}
2k\gamma-\varepsilon_{N,\lambda},
&N+1-q\ \text{even},\\[2mm]
\varepsilon_{N,\lambda},
&N+1-q\ \text{odd}.
\end{cases}
}
\tag{4}
$$

These are individual complex-eigenclass norms. Their behaviour does not contradict evenness of a kernel determinant on a real-period locus.

## 2. The exact source operator retains the nonnormal term

Work on the actual minimum-section space

$$
\mathcal V_N
=
\mathcal P_N\ominus\chi\mathcal P_{N-q}.
$$

Let

$$
\mathsf J_N=\Pi_{\mathcal V_N}M_y|_{\mathcal V_N}.
$$

This is a finite Hermitian compression of the original source multiplication operator.

The exact minimum-section identity gives

$$
\mathscr S_NA\mathscr S_N^{-1}
=
cI+i\mathsf J_N
+
\frac{\widehat b_{N+1}\widehat b_N^*}{\omega_N},
\qquad
\widehat b_j=\mathscr S_Nb_j.
\tag{5}
$$

The rank-one term is retained. Equation (5) does not replace $A$ by a self-adjoint operator.

At the untilted source, the two vectors have opposite parities. They are both nonzero, since otherwise (5) could not possess the retained eigenvalue $c+d+it_\lambda$ with $d>0$. Normalize them only as coordinates in this explicitly specified source space:

$$
e_N=\frac{\widehat b_N}{\|\widehat b_N\|},
\qquad
f_N=\frac{\widehat b_{N+1}}{\|\widehat b_{N+1}\|},
\qquad e_N^*f_N=0.
$$

With $\mu=d+it_\lambda$ and

$$
R_\mu=(\mu I-i\mathsf J_N)^{-1},
$$

the eigenvalue equation supplies both the resolvent representation of the same class and its secular identity. Their combination yields

$$
\mathfrak c_{N,\lambda}
=
\frac{f_N^*R_\mu f_N}{\|R_\mu f_N\|^2}.
\tag{6}
$$

Reflection anticommutes with $\mathsf J_N$, and $f_N$ has definite parity. Its spectral measure is therefore even. For a pair of spectral points $\pm t$, the resolvent-weighted mean is exactly

$$
\frac{
t\bigl([d^2+(t_\lambda-t)^2]^{-1}
-[d^2+(t_\lambda+t)^2]^{-1}\bigr)
}{
[d^2+(t_\lambda-t)^2]^{-1}
+[d^2+(t_\lambda+t)^2]^{-1}
}
=
\frac{2t_\lambda t^2}{d^2+t_\lambda^2+t^2}.
$$

It follows that

$$
\boxed{
0<j_{N,\lambda}<2t_\lambda,
\qquad
|\mathfrak c_{N,\lambda}|
\le\sqrt{d^2+t_\lambda^2}.
}
\tag{7}
$$

This establishes the sign of the eventual error in (1): it is one positive scalar, not two unrelated absolute-error choices.

## 3. The original relation measure forces a quantitative zero gap

Put

$$
\widehat\chi(y)=i^{-q}\chi(c+iy),
\qquad
dW(y)=\widehat\chi(y)^2\,dm(y).
$$

The polynomial $\widehat\chi$ is real and even. All its roots, with their complete multiplicities, have modulus at most

$$
R=k\sqrt{\delta^2+\gamma^2}.
$$

Use the original GRA full-polynomial comparison through degree $2q$:

$$
\ell_k\|P\|_\sigma^2
\le\|P\|_m^2
\le u_k\|P\|_\sigma^2,
\qquad
\mathscr L_k=\log(u_k/\ell_k)
=O_h(k+\log q).
$$

This comparison applies before the same affine minimum is taken. It preserves the full arithmetic source; it does not identify its density with the Gamma density.

Take

$$
Y=2^{-16}q,\qquad
B_\chi=\frac{qR^2}{Y^2-R^2},
$$

and define

$$
\eta_0=
\frac{\sqrt{2\pi}}{c_\Gamma}
\frac{(2q+1)(4q+1)\sqrt{1+2q}}q\,16^{-q},
$$

$$
\eta=
e^{\mathscr L_k+B_\chi}
\frac{\eta_0}{1-\eta_0}.
$$

On the explicit guards

$$
q\ge100,\qquad R\le Y/4,\qquad \eta\le1/4,
$$

the following holds for **every polynomial of degree at most $q$**:

$$
\boxed{
\int_{|y|\le Y}|P(y)|^2\,dW(y)
\le
\eta\int_{\mathbb R}|P(y)|^2\,dW(y).
}
\tag{8}
$$

The proof retains the central integral. Outside it, opposite root pairs give

$$
e^{-B_\chi}|y|^{2q}
\le\widehat\chi(y)^2
\le e^{B_\chi}|y|^{2q}.
$$

Inside it, a complete Legendre expansion on $[q,2q]$, the original Gamma lower bound on that interval, and the full Gamma mass bound the central contribution by $\eta_0$ times the reference power norm. The GRA inequalities then return this estimate to the original arithmetic norm. For fixed $h$,

$$
\eta=\exp[-q\log16+O_h(k+\log q)].
$$

Let $U_j$ be the real monic orthogonal polynomials for $dW$, with squared norms $\nu_j$. Passing separately to the even and odd polynomials in $y^2$, (8) bounds the corresponding finite Jacobi Rayleigh quotients below by $Y^2(1-\eta)$. Therefore every nonzero zero of every $U_j$, $j\le q$, has modulus at least

$$
g=Y\sqrt{1-\eta}.
\tag{9}
$$

The odd polynomial’s zero at the origin remains. The real-zero, finite-Jacobi, and consecutive-interlacing facts used here are the standard orthogonal-polynomial results recorded by the National Institute of Standards and Technology (n.d., §18.2(vi)).

## 4. Consecutive Cauchy transforms determine the class phase

Set

$$
z=\frac{\lambda-c}{i}=t_\lambda-id
$$

and retain the original Cauchy transforms

$$
\mathscr C_j(z)=
\int_{\mathbb R}\frac{U_j(y)}{z-y}\,dW(y).
$$

Orthogonality gives the exact identity

$$
U_j(z)\mathscr C_j(z)
=
I_j(z)
:=
\int_{\mathbb R}\frac{U_j(y)^2}{z-y}\,dW(y).
\tag{10}
$$

Only on the exterior region define

$$
M_j=\int_{|y|>Y}\frac{U_j(y)^2}{y^2}\,dW(y).
$$

There is no use of a potentially divergent full inverse moment at zero.

The original multiplication estimate supplies

$$
C_*=C_{\mathrm{mult}}(h)
\bigl(4q+\lfloor k/3\rfloor\bigr),
$$

and Cauchy–Schwarz gives

$$
M_j\ge\frac{(1-\eta)^2\nu_j}{C_*^2}.
$$

The required multiplication bound is on the original convolution source and retains its total-degree output face.

Pairing the exterior points $y$ and $-y$, and retaining the central integral as an error, gives

$$
I_j(z)=-zM_j(1+\epsilon_j),
\qquad
|\epsilon_j|\le\theta_I,
$$

where

$$
\theta_I=
\frac{R^2}{Y^2-R^2}
+
\frac{\eta C_*^2}{dR(1-\eta)^2}.
\tag{11}
$$

The decisive additional estimate is the consecutive-zero comparison. Interlacing makes the cumulative signed count of the positive squared zeros of $U_{r-1}$ and $U_r$ at most one in absolute value. Integrating against
$\log(1-z^2/t)$ therefore gives

$$
\left|\log(\text{consecutive root-product ratio})\right|
\le
-\log(1-R^2/g^2).
\tag{12}
$$

There is **no multiplying factor $r$** in this estimate.

Combining (10)–(12), with the zero at the origin retained according to parity, proves

$$
-i\,\frac{\mathscr C_r(z)}{\mathscr C_{r-1}(z)}
=
B_r\bigl(d+i(-1)^rt_\lambda\bigr)(1+\epsilon_r),
\qquad B_r>0,
$$

with

$$
|\epsilon_r|\le
a_*:=
\frac1{(1-R^2/g^2)(1-\theta_I)^2}-1.
\tag{13}
$$

The map back to the original class is exact. Expanding its minimum representative against the complete relation basis gives

$$
\boxed{
\frac{F_{23}}{F_{13}}
=
-i\,\frac{\nu_{r-1}}{\omega_N}
\frac{\mathscr C_r(z)}{\mathscr C_{r-1}(z)},
\qquad r=N+1-q\ge1.
}
\tag{14}
$$

All factors outside the Cauchy ratio are positive real or the explicitly displayed original phase. Both Gram entries are nonzero.

Finally, $\operatorname{Re}\mathfrak c=d$ is exact. Thus the positive scale in (13) is fixed by the original eigenclass identity, rather than by choosing a new normalization. Under

$$
\theta_I<1,\qquad Ra_*\le d/2,
$$

the phase error is bounded by

$$
E_{\mathrm{phase}}=\frac{2R^2a_*}{d}.
$$

The first cutoff, $r=0$, is handled directly from its original cardinal representative, with

$$
E_{\mathrm{first}}
=
2t_\lambda
\left[
\frac{R^2}{Y^2}
+
\frac{\eta(R^2+C_*^2)}{d^2}
\right].
$$

Consequently one may take

$$
\boxed{
E_{\mathrm{cur}}
=
\max\{E_{\mathrm{phase}},E_{\mathrm{first}}\}
=
O_h(k^3/q^2).
}
\tag{15}
$$

This proves (1)–(4), including the original first endpoint. The proof does not require a simple-packet LRC asymptotic to be extended to higher multiplicity: the full-multiplicity conclusion follows directly from the retained source comparison, central estimate, and consecutive-zero argument.

## 5. The receiving formula on the same projected class

Return to the actual three-column Gram calculation:

$$
W=[b_N,b_{N+1},[L_\lambda]],
\qquad F=W^*G_NW,
$$

$$
K=
W^*G_NI(I^*G_NI)^{-1}I^*G_NW,
\qquad B=F-K.
$$

The original projected pairings are

$$
\Phi_K=\frac2{\omega_N}\Re(\overline{K_{13}}K_{23}),
$$

$$
\Phi_B=\frac2{\omega_N}\Re(\overline{B_{13}}B_{23}),
$$

$$
\Phi_\times=
\frac2{\omega_N}
\Re(\overline{K_{23}}B_{13}
+\overline{K_{13}}B_{23}).
$$

These formulas preserve the actual class and the complete mixed term.

Since the preceding calculation proves $F_{13}F_{23}\ne0$, define the actual response ratios

$$
U=\frac{K_{13}}{F_{13}},
\qquad
V=\frac{K_{23}}{F_{23}},
$$

and

$$
P_K=\bar U V,\qquad
P_B=(1-\bar U)(1-V),
$$

$$
P_\times=\bar U+V-2\bar U V.
$$

Their exact sum is one.

The new evaluated receiver is

$$
\boxed{
\frac{\Phi_X}{2E_{N,\lambda}}
=
k\left[
\delta\Re P_X-(-1)^r\gamma\Im P_X
\right]
+
(-1)^r\varepsilon_{N,\lambda}\Im P_X,
\qquad X=K,B,\times.
}
\tag{16}
$$

There is **one shared positive remainder**

$$
0<\varepsilon_{N,\lambda}\le E_{\mathrm{cur}}.
$$

Because $\sum_X\Im P_X=0$, its three contributions cancel exactly in the full same-class sum:

$$
\Phi_K+\Phi_B+\Phi_\times
=
2k\delta\,E_{N,\lambda}.
$$

Equation (16) is stronger than the previous exponentially scaled cancellation estimate: the full-class complex coefficient has been calculated with an absolute $O_h(k^{-1})$ error in the simple lane. It also identifies precisely what must still be evaluated. The individual projected error is

$$
2E_{N,\lambda}E_{\mathrm{cur}}|\Im P_X|,
$$

not automatically $O_h(k^{-1})E_{N,\lambda}$. The response ratios can amplify the scalar error.

For each component, (16) already gives a directed interval by using the same $\varepsilon_{N,\lambda}\in(0,E_{\mathrm{cur}}]$. What remains is the original period-dependent $U,V$, or sufficiently strong estimates for their correlated combinations. Those are the terminal quantities assigned to the directional session—not another inverse certificate for them.

The separate leakage expressions also remain:

$$
\frac{2\Re(u^*A_{BK}^*Q_Nb)}{2E}
=
d(1-\theta_K)-\Re(\mathfrak c P_B),
$$

$$
\frac{2\Re(u^*H_NA_{KB}b)}{2E}
=
d\theta_K-\Re(\mathfrak c P_K),
\qquad
\theta_K=\frac{K_{33}}E.
$$

Thus the evaluated phase enters both original leakage directions without equating their sum with $\Lambda AI$ alone.

## Resulting state

The completed calculation is the full extremal terminal eigenclass’s marked pairing, uniformly across the original window and with complete fixed multiplicity retained. Its leading complex coefficient and the sign of its scalar error are evaluated.

The separate projected signs, native angular allocations, independent proper-source standard return, and signed arithmetic–Gamma coefficient remain distinct unfinished targets. The two prompts require those sessions to finish those quantities at their relevant scales. This continuation does not infer the full positive-primary exterior trace by summing independently normalized eigenline pairings, and it does not claim programme closure.

The package includes the full proof, both prompts, exact provider extracts, the two latest session notes, and the frozen preceding coordinator delivery. Its verifier passes **92 exact symbolic and rational/Gaussian-rational diagnostics** both normally and under Python `-O`, with identical receipts. Those fixtures check the phase conventions, full-multiplicity terminal classes, minimum-section identities, Cauchy-transform relations, and coupled projected formulas; they are not numerical evaluations of hypothetical xi zeros or their periods.

[Full continuation package](sandbox:/mnt/data/Retained_Class_Phase_and_Continuation_Targets_20260918.zip) · [Mathematical proof](sandbox:/mnt/data/Retained_Class_Phase_and_Continuation_Targets_20260918/proof/RETAINED_EIGENCLASS_CURRENT.md)





RETAINED_EIGENCLASS_CURRENT.md
The retained eigenclass current at polynomial accuracy

Research-programme continuation, 18 September 2026.
Result and exact scope

For the programme's original positive extremal eigenclass, the phase-sensitive scalar multiplying the three same-class projected pairings can be evaluated at the arithmetic scale. The result is

[
\boxed{\mathfrak c_{N,\rho}
=k{\delta+i(-1)^r\gamma}
+O_h(k^3/q^2),\qquad r=N+1-q,\quad q-1\le N\le2q-1.}
\tag{EC1}
]

This is uniform in the original cutoff. It includes the first cutoff. Here the original complete quartet multiplicity is an arbitrary fixed integer (m_0\ge1),

[
e=1+k(m_0-1),\qquad q=e(k+1)^2,\qquad k\equiv1\pmod4.
]

Consequently the error is (O_h(k^{-1})) for a simple quartet and (O_h(k^{-3})) for every fixed (m_0\ge2). An explicit finite error and all its guards are given below.

Equivalently, for the original fixed eigenclass and its actual arithmetic minimum norm (E_{N,\rho}(\theta)), the marking derivative satisfies

[
j_{N,\rho}:=\left.\partial_\theta\log E_{N,\rho}(\theta)\right|_0
=\begin{cases}
2k\gamma+O_h(k^3/q^2),&r\text{ even},\
O_h(k^3/q^2),&r\text{ odd}.
\end{cases}
\tag{EC2}
]

In fact (0<j_{N,\rho}<2k\gamma). Thus both errors in (EC2) have specified directions. There is one actual scalar (\varepsilon_{N,\rho}>0), bounded by the explicit radius below, for which

[
\boxed{\mathfrak c_{N,\rho}
=k\delta+i(-1)^r\bigl(k\gamma-\varepsilon_{N,\rho}\bigr).}
\tag{EC3}
]

The result concerns the fixed eigenclass's norm, not a kernel determinant and not the arithmetic--Gamma interpolation. It does not assert that the marking derivative of a kernel determinant equals the marking derivative of an individual complex eigenclass. It does not evaluate the period-dependent projected response coefficients appearing in Section 9. In particular it is not a proof of the remaining projected signs or a claim of an actual off-critical zero.

Unlike DBS's coarse directional estimate, this proof needs neither CRV's simple-packet asymptotic nor an exceptional-cutoff argument. Its analytic inputs are the original full-multiplicity GRA/AMT polynomial comparison and CAI multiplication estimate. Their supplied proofs and constants are retained as inputs; this note does not re-audit the preceding theta/convolution lower-envelope construction.
1. The same complete arithmetic class

Fix the stipulated actual quartet

[
\rho=\tfrac12+\delta+i\gamma,\qquad
0<\delta<\tfrac12,\quad\gamma>2,
]

with complete common multiplicity (m_0). Retain

[
h(s)=\prod_{\alpha\in{\rho,\bar\rho,1-\rho,1-\bar\rho}}(s-\alpha)^{m_0},
\qquad v_h=2\xi/h,
]

[
dm(y)=w_h^{*k}(y),dy,
\qquad w_h(y)=\frac{|v_h(1/2+iy)|^2}{2\pi},
\qquad S=c+iy,\quad c=k/2.
]

The measure is the original unscaled arithmetic measure. Its complete mass remains in every norm below. It is even, positive almost everywhere, and has the polynomial moments used here by the original source estimates.

The original algebra is

[
E=\mathbb C[S]/(\chi),\quad A=M_S,\quad
\chi(S)=\prod_{a,b=0}^k(S-\beta_{ab})^e,
]

[
\beta_{ab}=c+(2a-k)\delta+i(2b-k)\gamma,
\qquad e=1+k(m_0-1),\quad q=e(k+1)^2.
]

Let (\lambda=k\rho=c+d+iv), where

[
d=k\delta>0,\quad t_\lambda=k\gamma>0,\quad
R=k\sqrt{\delta^2+\gamma^2}=\sqrt{d^2+t_\lambda^2}.
\tag{EC4}
]

Write (\chi_\lambda=\chi/(S-\lambda)^e). The terminal eigenclass in the original primary block has the degree-below-(q) representative

[
L_\lambda(S)=\frac{\chi(S)}{(S-\lambda)\chi_\lambda(\lambda)}.
\tag{EC5}
]

Indeed ((S-\lambda)L_\lambda=0\pmod\chi), and at (\lambda) its full local class is ((S-\lambda)^{e-1}), while at every other centre its complete primary class vanishes. This uses (\chi_\lambda(\lambda)\ne0), not (\chi'(\lambda)), which would vanish at higher multiplicity. For (e=1) it is exactly the original cardinal idempotent.

The original inclusion (\eta) of MCE4 sends this class to

[
\eta([L_\lambda])
=\frac{[k(m_0-1)]!}{[(m_0-1)!]^k}
v_h(\rho)^k\prod_{j=1}^k(s_j-\rho)^{m_0-1}\ne0
\tag{EC6}
]

on the all-(\rho) tensor primary component. No unit is replaced by one. The surrounding algebra, quotient covariance, and polynomial relation retain every primary block and its full multiplicity. Any originally specified nonzero scalar multiple of (EC5) has the same homogeneous current below, with that scalar retained in its norm and in its three-column Gram.

Let (\mathscr S_N\to\mathcal P_N) be the original arithmetic minimum section. Its image is

[
\mathcal V_N=\mathcal P_N\ominus\chi\mathcal P_{N-q},
]

where an empty relation space at (N=q-1) is zero. Let (G_N) be its exact quotient Gram. Define

[
P_{N,\lambda}=\mathscr S_N[L_\lambda],\qquad
E_{N,\lambda}=|P_{N,\lambda}|_m^2>0.
]

For the real source tilt (e^{\theta y}dm(y)), the eigenclass itself is fixed. Differentiating the attained minimum kills the section-derivative terms by orthogonality to the full relation space. Hence

[
j_{N,\lambda}
=\frac{\int y|P_{N,\lambda}(c+iy)|^2dm(y)}{E_{N,\lambda}}.
\tag{EC7}
]

This is the same envelope identity as MCP1, applied to this particular class.
2. A bounded source compression, with the entire feedback term retained

Let (p_n(S)) be the original arithmetic monic source polynomials, (\omega_n) their norms, and (b_n=[p_n]). Set

[
F_{13}=b_N^*G_N[L_\lambda],\quad
F_{23}=b_{N+1}^*G_N[L_\lambda],\quad F_{33}=E_{N,\lambda}.
]

The scalar to be evaluated is

[
\mathfrak c_{N,\lambda}
=\frac{\overline{F_{13}}F_{23}}{\omega_NE_{N,\lambda}}.
\tag{EC8}
]

It is not the marked kernel pairing (z_K/\omega_N).

Let (\Pi_N) be the arithmetic source-orthogonal projector onto (\mathcal V_N). On that same space define

[
\mathsf J_N=\Pi_NM_y|_{\mathcal V_N}.
]

It is Hermitian. CAI25, including its total-degree output face, gives

[
|\mathsf J_N|\le C_{\rm mult}(h)(2N+\lfloor k/3\rfloor).
\tag{EC9}
]

The exact multiplication identity, equivalently MCP2 transported by the minimum section, is

[
\mathscr S_NA\mathscr S_N^{-1}
=cI+i\mathsf J_N+
\frac{\widehat b_{N+1}\widehat b_N^*}{\omega_N},
\qquad \widehat b_j=\mathscr S_Nb_j.
\tag{EC10}
]

For a direct proof, multiply a minimum representative by (S). Its degree-(N+1) coefficient is the original (p_N) coefficient. Subtract that multiple of (p_{N+1}), then project onto the minimum-section space. The remaining relation term is orthogonal to that space. The coefficient of the surviving (\widehat b_{N+1}) is (\langle\widehat b_N,P\rangle/\omega_N), giving (EC10).

Reflection preserves the minimum space, anticommutes with (\mathsf J_N), and gives opposite parities to (\widehat b_N,\widehat b_{N+1}). Thus those two vectors are orthogonal. Both are nonzero: otherwise the feedback term would vanish and (EC10) would have all its eigenvalues on (\operatorname{Re}S=c), contrary to the actual algebraic eigenclass (EC5).

Put

[
e_N=\widehat b_N/|\widehat b_N|,\quad
f_N=\widehat b_{N+1}/|\widehat b_{N+1}|,\quad
\epsilon_N=|\widehat b_N||\widehat b_{N+1}|/\omega_N.
]

These dimensionless coordinates are an explicitly stated isometric calculation; they do not change the source or the norm of the retained class. Equation (EC10) is

[
cI+i\mathsf J_N+\epsilon_N f_Ne_N^*.
]

In particular (\mathsf J_N) is not substituted for (A); the generally large, nonnormal feedback term remains.

For (\mu=d+iv) the resolvent

[
\mathcal R_\mu=(\mu I-i\mathsf J_N)^{-1}
]

exists and has norm at most (1/d). If (z_N=P_{N,\lambda}/\sqrt{E_{N,\lambda}}), (\alpha=e_N^*z_N), and (\beta=f_N^*z_N), then

[
z_N=\epsilon_N\alpha\mathcal R_\mu f_N,
\quad 1=\epsilon_Ne_N^*\mathcal R_\mu f_N,
\quad \epsilon_N^2|\alpha|^2|\mathcal R_\mu f_N|^2=1.
]

Consequently

[
\boxed{
\mathfrak c_{N,\lambda}
=\epsilon_N\bar\alpha\beta
=\frac{f_N^*\mathcal R_\mu f_N}{|\mathcal R_\mu f_N|^2}
=d+i(j_{N,\lambda}-t_\lambda).
}
\tag{EC11}
]

This also proves (F_{13}\ne0). The positive real part of the numerator proves (F_{23}\ne0).
Exact polynomial-scale bound

The spectral measure of (\mathsf J_N) at (f_N) is even, because reflection anticommutes with (\mathsf J_N) and fixes (f_N) up to sign. Pair the spectral points (t,-t). Under the resolvent squared norm, their conditional mean is exactly

[
\frac{t{[d^2+(t_\lambda-t)^2]^{-1}-[d^2+(t_\lambda+t)^2]^{-1}}}
{[d^2+(t_\lambda-t)^2]^{-1}+[d^2+(t_\lambda+t)^2]^{-1}}
=\frac{2vt^2}{d^2+t_\lambda^2+t^2}.
\tag{EC12}
]

This lies in ([0,2t_\lambda)). An atom at zero contributes zero. The measure cannot be supported only at zero, because that would give (e_N^*\mathcal R_\mu f_N=0), contradicting the displayed secular equality. Hence

[
\boxed{0<j_{N,\lambda}<2t_\lambda,\quad
\operatorname{Re}\mathfrak c_{N,\lambda}=d,\quad
|\operatorname{Im}\mathfrak c_{N,\lambda}|<t_\lambda,\quad
|\mathfrak c_{N,\lambda}|\le R.}
\tag{EC13}
]

This bound is exact at every original cutoff. It already replaces an exponentially large operator-scale bound for this particular scalar by the actual arithmetic scale (O_h(k)).
3. Explicit full-source constants and the central-region estimate

The reference measure used only for comparison is

[
d\sigma(y)=|\Gamma(1/4+iy/2)|^2dy/(2\pi),\quad
\sigma(\mathbb R)=\sqrt{2\pi},
]

[
c_\Gamma e^{-\pi|y|/2}(1+|y|)^{-1/2}
\le\sigma(y)\le
C_\Gamma e^{-\pi|y|/2}(1+|y|)^{-1/2},
]

where (c_\Gamma=\sqrt2e^{-7/6}) and
(C_\Gamma=\sqrt{2\sqrt5},e^{2/3}).

For full original multiplicity put

[
p_h=8m_0-\tfrac92,\quad B_h=42+8m_0,\quad M_h=21+4m_0,
]

[
\vartheta_h=\int_{-1}^1w_h(y)dy,\quad
M_{\pi/2}=\int e^{\pi y/2}w_h(y)dy.
]

Retain the original TW/BT constants (c_h,C_h^{\rm tilt}), and define exactly the GRA/CAI constants

[
\underline a_k=
\frac{c_h\vartheta_h^{k-3}e^{-(\pi/2)(k-3)}(k-2)^{-B_h}}
{C_\Gamma2^{B_h/2}},\qquad
\overline a_k=
\frac{C_h^{\rm tilt}}{c_\Gamma}k^{p_h+1}M_{\pi/2}^{k-1},
]

[
D_n=[1+4(n+M_h)^2]^{M_h},\quad
\ell_k=\underline a_k/D_{2q},\quad u_k=\overline a_k,
\quad \mathscr L_k=\log(u_k/\ell_k).
\tag{EC14}
]

The proved whole-polynomial comparison is

[
\ell_k|P|_\sigma^2\le|P|m^2\le u_k|P|\sigma^2,
\qquad \deg P\le2q,
\quad \mathscr L_k=O_h(k+\log(q+1)).
\tag{EC15}
]

The upper inequality also holds pointwise at the density level, which will be used on the central interval. The lower inequality is used on the complete polynomial norm, not pointwise.

For completeness the fixed multiplication constant in (EC9) is the original CAI22 value. Set

[
d_0=\pi/2-\log(5/3),\quad
C_\sigma=4/(\sqrt{15}\sqrt{2\pi}),
]

[
H_h=\frac{64C_\sigma(1+4M_h^2)^{M_h}}{d_0^2}
\max_{b=3,4,5}\frac{M_{\pi/2}^b}{\underline a_b},
]

[
T_h=\frac2{d_0}{\log16+2M_h+3+\log^+H_h},\qquad
C_{\rm mult}(h)=\sqrt{T_h^2+1}.
\tag{EC16}
]

All these constants belong to the unscaled original source.

Define

[
\widehat\chi(y)=i^{-q}\chi(c+iy),\quad
dW(y)=\widehat\chi(y)^2dm(y).
]

The polynomial (\widehat\chi) is real, monic, even, and includes the complete multiplicities. Its roots have modulus at most (R) and occur in opposite pairs, counted with multiplicity.

Set

[
\epsilon_=2^{-16},\quad Y=\epsilon_q,
\quad B_\chi=\frac{qR^2}{Y^2-R^2},
]

[
\eta_0=
\frac{\sqrt{2\pi}}{c_\Gamma}
\frac{(2q+1)(4q+1)\sqrt{1+2q}}q,16^{-q},
]

[
\boxed{\eta=
e^{\mathscr L_k+B_\chi}\frac{\eta_0}{1-\eta_0}.}
\tag{EC17}
]

Initially impose (q\ge100), (R\le Y/4), and (\eta\le1/4). Then, for every complex polynomial (P) of degree at most (q),

[
\boxed{\int_{|y|\le Y}|P(y)|^2dW(y)
\le\eta\int_{\mathbb R}|P(y)|^2dW(y).}
\tag{EC18}
]
Proof retaining the whole central interval

Put (\mathcal H_q[P]=\int|y|^{2q}|P(y)|^2d\sigma(y)). On (|y|\ge Y), pairing every opposite root, including repetitions, gives

[
e^{-B_\chi}|y|^{2q}
\le\widehat\chi(y)^2\le e^{B_\chi}|y|^{2q}.
]

On (|y|\le Y), the bound

[
\widehat\chi(y)^2\le[(9/4)\epsilon_*^2q^2]^q
]

is valid; the constant (9/4) is a deliberate enlargement of the paired-root bound.

Expand (P) in the shifted Legendre basis on ([q,2q]). The same estimate holds for all degrees at most (2q), so in particular for those required here. The transformed coordinate on ([-Y,Y]) has modulus below four. The Legendre recurrence gives (|L_j(t)|\le10^j) there by induction. Cauchy--Schwarz in the complete orthonormal expansion yields

[
|P(y)|^2\le
\frac{(2q+1)(4q+1)100^{2q}}q\int_q^{2q}|P(t)|^2dt
\qquad(|y|\le Y).
]

Meanwhile

[
\mathcal H_q[P]\ge
\frac{c_\Gamma q^{2q}e^{-\pi q}}{\sqrt{1+2q}}
\int_q^{2q}|P(t)|^2dt.
]

Use ((9/4)e^\pi10^4\epsilon_*^2<1/16) and the full mass (\sqrt{2\pi}). Both the root-weighted and power-weighted central integrals are at most (\eta_0\mathcal H_q[P]). The complete Gamma root norm is at least

[
e^{-B_\chi}(1-\eta_0)\mathcal H_q[P].
]

The polynomial (\widehat\chi P) has degree at most (2q), so (EC15) applies to its entire norm. The density upper bound applies to its central integral. Dividing those two inequalities proves (EC18). The original central contribution is bounded, not removed.
4. A gap for the relation-polynomial zeros

Let (U_j) be the real monic orthogonal polynomials for (dW), with full squared norms (\nu_j). Evenness gives (U_j(-y)=(-1)^jU_j(y)). For (j\le q), every nonzero zero of (U_j) satisfies

[
|y|\ge g,\qquad g^2=Y^2(1-\eta).
\tag{EC19}
]

Indeed the even polynomials become orthogonal polynomials in (t=y^2) for the pushforward of (W); the odd polynomials have the form (yV(t)), with the extra factor (t) in that measure. The positive zeros squared are eigenvalues of the respective finite multiplication-by-(t) compressions. For every polynomial vector in either compression, (EC18) gives

[
\frac{\int y^2|P(y)|^2dW}{\int|P(y)|^2dW}\ge Y^2(1-\eta).
]

The relevant degrees are at most (j-2), so the already proved degree range suffices. The finite Rayleigh principle proves (EC19). No claim is made that the original measure has a literal support gap; it has a quantitatively negligible central contribution on the specified polynomial space.

The positive orthogonal-polynomial recurrence also gives real simple zeros and consecutive interlacing. These standard facts follow directly from the finite real symmetric tridiagonal matrix and its positive off-diagonal entries. Interlacing here retains the zero at the origin for every odd polynomial.
5. Cauchy transforms, with a relative rather than absolute estimate

Let

[
z=\frac{\lambda-c}{i}=t_\lambda-id,\qquad |z|=R,
]

[
q_j(z)=\int\frac{U_j(y)}{z-y},dW(y),\qquad
I_j(z)=\int\frac{U_j(y)^2}{z-y},dW(y).
]

Orthogonality gives the exact identity

[
\boxed{U_j(z)q_j(z)=I_j(z).}
\tag{EC20}
]

The difference quotient ((U_j(z)-U_j(y))/(z-y)) has degree below (j) in (y), proving the equality. The imaginary part of (I_j(z)) is strictly positive because (\operatorname{Im}z<0); (U_j(z)\ne0) because its zeros are real. Thus every (q_j(z)\ne0).

Keep the outer inverse moment only on its valid domain:

[
M_j=\int_{|y|>Y}\frac{U_j(y)^2}{y^2},dW(y)>0.
]

There is no use of the generally divergent full inverse moment at zero. Put

[
C_* = C_{\rm mult}(h)(4q+\lfloor k/3\rfloor).
]

CAI25 applies to (\widehat\chi U_j), whose degree is at most (2q), and gives

[
\int y^2U_j(y)^2dW\le C_*^2\nu_j.
]

Cauchy--Schwarz on the retained outer set then gives

[
M_j\ge\frac{(1-\eta)^2\nu_j}{C_*^2}.
\tag{EC21}
]

Pairing (y,-y) in the outer integral,

[
I_{j,\mathrm{out}}(z)
=-z\int_{|y|>Y}\frac{U_j(y)^2/y^2}{1-z^2/y^2},dW(y).
]

Its relative difference from (-zM_j) is at most (R^2/(Y^2-R^2)). The full inner part is bounded in absolute value by (\eta\nu_j/d), since (|z-y|\ge d). Hence

[
I_j(z)=-zM_j(1+\epsilon_j),\qquad
|\epsilon_j|\le t_I,
]

[
\boxed{t_I=\frac{R^2}{Y^2-R^2}
+\frac{\eta C_*^2}{dR(1-\eta)^2}.}
\tag{EC22}
]

This bound is uniform through (j=q).
Interlacing avoids charging an error at every root

Let (1\le r\le q). The complete factorizations of the adjacent even and odd polynomials have the form

[
\frac{U_{r-1}(z)}{U_r(z)}
=\begin{cases}
-A_rz,\mathcal P_r(z),&r\text{ even},\
A_rz^{-1}\mathcal P_r(z),&r\text{ odd},
\end{cases}\qquad A_r>0.
\tag{EC23}
]

The factor (A_r) is the positive product of their actual nonzero squared roots, with its exact reciprocal placement. No value is assigned to it. The normalized product (\mathcal P_r) consists of all factors (1-z^2/t_j) from those roots with the appropriate numerator/denominator signs.

The signed counting function of the squared positive roots of adjacent polynomials has absolute value at most one by interlacing. Each root is at least (g^2) by (EC19). Integrate the derivative of (\log(1-z^2/t)) against this counting function, using the branch tending to zero at infinity. This proves

[
|\log\mathcal P_r(z)|\le
\int_{g^2}^\infty\frac{R^2}{t(t-R^2)}dt
=-\log(1-R^2/g^2).
\tag{EC24}
]

The count, not the number of roots, controls the bound. In particular no additional factor (r) appears. At (r=1), the normalized product is one.

Combining (EC20)--(EC24), with every positive multiplier retained, gives

[
-i\frac{q_r(z)}{q_{r-1}(z)}
=B_r{d+i(-1)^rv}(1+\varepsilon_r),\qquad B_r>0,
\quad |\varepsilon_r|\le a_*,
\tag{EC25}
]

where the completely finite radius can be written without an exponential as

[
\boxed{a_*=
\frac1{(1-R^2/g^2)(1-t_I)^2}-1.}
\tag{EC26}
]

For even (r), (iz=d+iv); for odd (r), (-i/z=(d-iv)/R^2), and that last positive (R^{-2}) is absorbed in the explicitly positive multiplier (B_r). The ratio (M_r/M_{r-1}) and the full factor (A_r) remain in (B_r). The error bound follows by taking the two logarithms of (1+\epsilon_j), whose absolute values are at most (-\log(1-t_I)), and using (EC24).
6. Exact coefficient maps back to the original minimum eigenclass

Let

[
\pi_j(S)=i^jU_j((S-c)/i),\qquad
C_j(\lambda)=\int
\frac{|\chi(c+iy)|^2\overline{\pi_j(c+iy)}}{c+iy-\lambda},dm(y).
]

All (\pi_j) are the original monic relation polynomials, with their full norms (\nu_j). The coordinate change gives, including its phase,

[
\boxed{C_j(\lambda)=i(-i)^j q_j(z).}
\tag{EC27}
]

For (r=N+1-q), the full relation projection is

[
P_{N,\lambda}(S)
=\frac{\chi(S)}{\chi_\lambda(\lambda)}
\left[
\frac1{S-\lambda}
-\sum_{j=0}^{r-1}\frac{C_j(\lambda)}{\nu_j}\pi_j(S)
\right].
\tag{EC28}
]

The first factor times the rational term is the polynomial (EC5). The sum subtracts exactly the orthogonal projection on every original relation (\chi\pi_j), (j<r). Thus this is the original minimum representative, not a new test vector.

For (r\ge1), its top coefficient gives

[
F_{13}=-\frac{\omega_N C_{r-1}(\lambda)}
{\chi_\lambda(\lambda)\nu_{r-1}}.
]

Also the original minimum representative of (b_{N+1}) is

[
\mathscr S_Nb_{N+1}=p_{N+1}-\chi\pi_r.
]

Its leading coefficient cancels, its remainder is (b_{N+1}), and it is orthogonal to every lower relation. Pairing this polynomial with (EC28) gives

[
F_{23}=-\frac{C_r(\lambda)}{\chi_\lambda(\lambda)}.
]

Hence

[
\boxed{\frac{F_{23}}{F_{13}}
=-i\frac{\nu_{r-1}}{\omega_N}\frac{q_r(z)}{q_{r-1}(z)}.}
\tag{EC29}
]

Every norm ratio and complex phase is explicit. All denominators are nonzero by (EC20). For (r=0) instead,

[
F_{13}=\omega_{q-1}/\chi_\lambda(\lambda),\qquad
F_{23}=-C_0(\lambda)/\chi_\lambda(\lambda).
]

Equations (EC8) and (EC29) show that (\mathfrak c) is a positive real multiple of the right side of (EC25). Its real part is exactly (d) by (EC11). Therefore the unknown positive multipliers cancel in determining this current's phase; they have not been discarded from either individual coefficient or norm.
7. Finite phase radius and proof of the uniform asymptotic

In addition to Section 3's guards impose

[
t_I<1,\qquad Ra_*\le d/2.
\tag{EC30}
]

Define

[
E_{\mathrm{phase}}=\frac{2R^2a_}{d},\qquad
E_{\mathrm{first}}=
2t_\lambda\left[\frac{R^2}{Y^2}
+\frac{\eta(R^2+C_^2)}{d^2}\right],
]

[
\boxed{E_{\mathrm{cur}}=
\max{E_{\mathrm{phase}},E_{\mathrm{first}}}.}
\tag{EC31}
]

For (r\ge1), write (w=(d+i(-1)^rv)(1+\varepsilon_r)) from (EC25). Its real part is at least (d-Ra_*\ge d/2). Since (\mathfrak c=d,w/\operatorname{Re}w), direct expansion gives

[
\left|\operatorname{Im}\mathfrak c-(-1)^rv\right|
\le\frac{R^2a_}{d-Ra_}
\le E_{\mathrm{phase}}.
\tag{EC32}
]

For example the numerator before division is exactly (R^2\operatorname{Im}\varepsilon_r). This is why controlling the relative Cauchy ratio, rather than its absolute size, suffices.

At (r=0), (EC28) contains no projection sum. Its norm density is the original even (W) divided by (d^2+(y-t_\lambda)^2). Pairing (y,-y) as in (EC12) gives

[
2t_\lambda-j_{q-1,\lambda}
=2t_\lambda,\mathbb E_{\mathrm{paired}}\frac{R^2}{R^2+y^2}.
]

On the outer set this fraction is at most (R^2/Y^2). The inner probability is at most (\eta(R^2+C_^2)/d^2): its unnormalized mass is at most (\eta\nu_0/d^2), while Jensen's inequality and the full second-moment bound give total mass at least (\nu_0/(R^2+C_^2)). Thus

[
0<2t_\lambda-j_{q-1,\lambda}\le E_{\mathrm{first}}.
\tag{EC33}
]

Combining (EC13), (EC32), and (EC33), the exact directed statement is

[
\boxed{
\mathfrak c_{N,\lambda}=d+i(-1)^r(t_\lambda-\varepsilon_{N,\lambda}),
\qquad 0<\varepsilon_{N,\lambda}\le E_{\mathrm{cur}},
\quad q-1\le N\le2q-1.
}
\tag{EC34}
]

Every quantity in the finite radius uses original source constants and the stated root radius. It has no unknown quotient Gram, period minor, or individual allocation in it.

For each fixed (h) and complete multiplicity, (EC15) and (EC17) give

[
\log\eta=-q\log16+O_h(k+\log q),\qquad
B_\chi=O_h(k^2/q).
]

Since (R=O_h(k)), (d\asymp_h k), (Y=\epsilon_q), and (C_=O_h(q)),

[
t_I=O_h(k^2/q^2)+O_h(\eta q^2/k^2),\qquad
a_*=O_h(k^2/q^2)+O_h(\eta q^2/k^2),
]

[
E_{\mathrm{cur}}=O_h(k^3/q^2).
\tag{EC35}
]

All guards hold eventually. Substitution of the exact (q=1+k(m_0-1)^2) proves (EC1)--(EC3) and both multiplicity-specific error orders. This is an independent full-multiplicity proof for the terminal eigenclass, not an extension of a simple-grid CRV asymptotic by notation.
8. Exact finite evaluability with the original moments

The Cauchy transforms above have an additional exact feature at the original evaluation point. Since (\widehat\chi(z)=0), polynomial division gives

[
q_j(z)=-\int U_j(y)\widehat\chi(y)
\frac{\widehat\chi(y)}{y-z},dm(y).
\tag{EC36}
]

The integrand is a polynomial; every complex coefficient is fixed by the original root polynomial. Thus the Cauchy factors can also be evaluated from the original arithmetic moments, with no new meromorphic integration or arbitrary pole data. Their asymptotic phase has nevertheless been evaluated in Sections 3--7; (EC36) is not used as a substitute for that evaluation.
9. The exact same-class projected receiver

Keep the original observation (\Lambda), its full kernel frame (I), the original arithmetic (G_N), and all attained quotient metrics. Form the same three columns

[
W=[b_N,b_{N+1},[L_\lambda]],\quad
F=W^*G_NW,
]

[
K=W^*G_NI(I^*G_NI)^{-1}I^*G_NW,\qquad B=F-K.
]

They retain the whole old kernel inverse. Put

[
U=K_{13}/F_{13},\qquad V=K_{23}/F_{23},\qquad
\theta_K=K_{33}/F_{33}.
\tag{EC37}
]

These ratios are well defined by Sections 2 and 6. They remain actual period-dependent data; no rank fraction or generic value is assigned to them.

Define

[
P_K=\bar U V,\quad
P_B=(1-\bar U)(1-V),\quad
P_\times=\bar U+V-2\bar U V.
]

They satisfy (P_K+P_B+P_\times=1). The original three projected pairings are exactly

[
\boxed{\frac{\Phi_X}{2E_{N,\lambda}}
=\operatorname{Re}(\mathfrak c_{N,\lambda}P_X),
\qquad X=K,B,\times.}
\tag{EC38}
]

No eigenvector has been changed: these are the three terms of MCE14 on its same original class. Substitution of the evaluated phase gives the directed receiver

[
\boxed{
\frac{\Phi_X}{2E_{N,\lambda}}
=k{\delta\operatorname{Re}P_X-(-1)^r\gamma\operatorname{Im}P_X}
+(-1)^r\varepsilon_{N,\lambda}\operatorname{Im}P_X,
\quad 0<\varepsilon_{N,\lambda}\le E_{\mathrm{cur}}.
}
\tag{EC39}
]

The error is one shared positive scalar, not three independent allowances. Its three signed contributions sum to zero exactly. In particular

[
\Phi_K+\Phi_B+\Phi_\times=2k\delta E_{N,\lambda}.
]

For an individual term the rigorous absolute replacement error is

[
2E_{N,\lambda}E_{\mathrm{cur}}|\operatorname{Im}P_X|.
\tag{EC40}
]

The factor (|\operatorname{Im}P_X|) remains. Its growth cannot be suppressed when deciding whether an individual approximation reaches the desired arithmetic sign scale. A sign follows from (EC39) only after the actual response is controlled relative to its explicit narrow phase interval.

The separate action leakages, with the original blocks, remain

[
\frac{\mathcal L_{BK}}{2E_{N,\lambda}}
=k\delta(1-\theta_K)-\operatorname{Re}(\mathfrak c P_B),
]

[
\frac{\mathcal L_{KB}}{2E_{N,\lambda}}
=k\delta\theta_K-\operatorname{Re}(\mathfrak c P_K),
\tag{EC41}
]

where (\mathcal L_{BK}=2\operatorname{Re}(b^*Q_N\Lambda AIu)) and
(\mathcal L_{KB}=2\operatorname{Re}(u^*H_NA_{KB}b)) for the original coordinates ([L_\lambda]=Iu+L_Nb). Their sum is (\Phi_\times). Thus the result does not replace (\Lambda AI) by the mixed weight block or drop the other leakage direction.

The full unit remains in the original arithmetic inclusion and the norm (E_{N,\lambda}). The polynomial-scale current is now evaluated. The unresolved response products in (EC39), and not an unspecified exponential radial prefactor, are the remaining directional input for the signs.
10. What this continuation finishes

The following are evaluated on the original class: the full source current's sign, its exact interval, its parity-dependent leading coefficient, an explicit uniform absolute error below the arithmetic (k) scale, and its same-class three-Gram receiver with a single correlated remainder. All cutoffs and full terminal primary multiplicity are covered under the displayed eventual guards.

The following are not claimed: values of the native angular allocation, the actual period-dependent (U,V), the independent proper-source standard return, the arithmetic--Gamma coefficient, separate projected signs, or a positive-primary exterior trace obtained by summing normalized eigenline identities. The original exterior trace uses its joint Gram and needs its own projection calculation. The proof does not declare a longstanding conjecture settled.
Source register

National Institute of Standards and Technology. (n.d.). General orthogonal polynomials, §18.2. In NIST Digital Library of Mathematical Functions. The standard real-zero, interlacing, and Jacobi-matrix facts used in Section 4 are also proved in the required finite form there and in the argument above.

Split-Zero research programme. (2026). 01_Current_Cumulative_and_Proofs.tex [Supplied cumulative manuscript]. Inputs: MCE1--6 and MCE9--14 for the full source and class, MCP1--2 for the attained source derivative, GRA3--6/AMT for the full-multiplicity source comparison, and CAI16--25 for its complete multiplication constant. Exact source ranges and hashes are in the package manifest.

Split-Zero mathematical continuation. (2026, September 18). Relative directional certificates and the three-column same-class Gram [Supplied as Pasted markdown(20260918-051153).md]. Section 9 uses its same-class response organization with all original factors; this note newly evaluates the full current multiplying those responses.

Coordinator continuation. (2026, September 18). Directional boundary spectrum and retained-class cancellation [DBS]. Its coarse-scale claims remain frozen as a predecessor. The present proof does not use DBS's exceptional-cutoff estimate to infer the new polynomial-scale result.
Verification and delivery status

The companion checker tests exact source/quotient and Cauchy-transform identities on finite even discrete-source fixtures, including a repeated-primary fixture. It also tests the directed gapped-measure phase radius and the complete three-term projected identity with a nonzero mixed term. The fixtures are not actual xi packets or period values. The analytic result is the proof above, not the finite examples. The original source providers remain imported with the stated evidential status.


