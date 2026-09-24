# All continuous positive transfer forms on the original full-jet quotient

25 September 2026. Independent derivation CFP0–CFP12 and the proved analytic lemma CFPA. The inner product convention is linear in the first variable.

## CFP0. The actual source and the statement

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). All numbers, coefficient spaces, arithmetic labels and operations in this proof occur after the complete arithmetic reconstruction. No coefficient value, addition, parity, coordinate or metric is assigned to \(\tau\). The original two branch records remain distinct.

Retain the source from RD1, RTT0 and PTQ6:
\[
\mathcal B=\left\{F\text{ entire}:b_{A,M}(F)=
\sup_{|\Re s|\le A}(1+|\Im s|)^M|F(s)|<\infty
\quad(A,M\in\mathbb Z_{\ge0})\right\},
\]
\[
\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\text{ for every nontrivial zero }\rho\text{ of original }\zeta,
\ 0\le j<m_\rho\},\qquad
\mathcal Q=\mathcal B/\mathcal I.
\tag{CFP0.1}
\]
The topology is this Fréchet quotient topology. Every multiplicity \(m_\rho\) is retained. Write \(q:\mathcal B\to\mathcal Q\), and retain
\[
T_aq(F)=q(a^sF(s)),\quad Lq(F)=q(sF(s)),\quad a>0;
\qquad \mathsf U_n=nT_{1/n}\quad(n\ge1).
\tag{CFP0.2}
\]
The integer \(n\) in the transfer is the already constructed cover degree. Its coefficient inverse is not a cover of fractional degree.

**Classification.** All jointly continuous positive semidefinite Hermitian forms \(B\) on \(\mathcal Q\) satisfying
\[
B(T_nF,G)=B(F,\mathsf U_nG)
\quad\text{for every recovered integer }n\ge1
\tag{CFP0.3}
\]
are exactly
\[
\boxed{B(F,G)=\sum_{\substack{\rho\in\mathscr Z\\\Re\rho=1/2}}
m_\rho c_\rho F(\rho)\overline{G(\rho)},\qquad
0\le c_\rho\le C(1+|\Im\rho|)^d}
\tag{CFP0.4}
\]
for some finite \(C,d\ge0\) depending on the form. The weights are unique. Here and below \(F(\rho)\) means evaluation of any source representative of its class.

The proof does not assume RH, simplicity, boundedness of \(B\) for the previous value Hilbert norm, or density of the finite-support subspace in \(\mathcal Q\). In particular it extends PTQ4 beyond bounded forms on that Hilbert space. The full source, its higher jets, and all actual off-line zeros, if present, remain in the domain; the theorem determines their image in every continuous positive transfer receiver.

## CFP1. Source continuity and the positive completion

Multiplication by \(e^{ts}\) preserves \(\mathcal B\), \(\mathcal I\) and the full vanishing-jet conditions. Its action on an actual jet is multiplication by the complete jet of \(e^{ts}\), rather than the identity. Moreover,
\[
b_{A,M}(e^{ts}F)\le e^{A|t|}b_{A,M}(F),\qquad
b_{A,M}(sF)\le(A+1)b_{A,M+1}(F).
\tag{CFP1.1}
\]
For real \(t\), the identity
\(e^{hs}-1=hs\int_0^1e^{uhs}\,du\) proves continuity of \(t\mapsto e^{ts}F\) in every seminorm. The analogous second-order integral remainder proves its derivative is \(se^{ts}F\) in \(\mathcal B\). Repetition gives all derivatives. These facts pass through the quotient.

Joint continuity of \(B(qF,qG)\), positivity and Cauchy–Schwarz give integers \(A,M\) and a constant \(C_B\) such that
\[
B(qF,qF)\le C_B b_{A,M}(F)^2.
\tag{CFP1.2}
\]
Indeed continuity at the origin first bounds the form by a finite maximum of seminorms in each variable; the increasing family \(b_{A,M}\) absorbs that finite maximum. Alternatively continuity of the quadratic form supplies the same bound by scaling. Cauchy–Schwarz follows directly by applying positivity to \(x+zy\) and minimizing over \(z\in\mathbb C\).

Let \(\mathcal N_B=\{F:B(F,F)=0\}\). Cauchy–Schwarz identifies it with the full radical. Complete \(\mathcal Q/\mathcal N_B\) for the specified inner product \(B\), obtaining a Hilbert space \(H_B\). The canonical map
\[
\pi:\mathcal Q\longrightarrow H_B
\quad\text{has dense image, and}\quad
\langle\pi F,\pi G\rangle=B(F,G).
\tag{CFP1.3}
\]
The map \(\pi q\) is continuous by (CFP1.2), hence \(\pi\) is continuous by the quotient topology. This construction does not identify the original Fréchet topology with the new Hilbert norm.

## CFP2. Every integer relation gives the full continuous unitary action

The exact identities \(\mathsf U_nT_n=nI\) and (CFP0.3) give
\[
B(T_nF,T_nG)=nB(F,G).
\tag{CFP2.1}
\]
Conversely (CFP2.1), with \(G\) replaced by \(T_n^{-1}G\), gives (CFP0.3). Invertibility of \(T_n\) also proves
\(B(T_{1/n}F,T_{1/n}G)=n^{-1}B(F,G)\). Composition therefore gives
\[
B(T_aF,T_aG)=aB(F,G)\qquad(a\in\mathbb Q_{>0}).
\tag{CFP2.2}
\]
For arbitrary real \(a>0\), choose positive rationals tending to \(a\). The source continuity in CFP1 and the continuity of \(B\) give exactly the same identity. This uses the entire already recovered arithmetic family and its coefficient operations; it makes no assertion that a finite set of prime labels initiates the arithmetic reconstruction.

For every real \(t\), define the auxiliary Hilbert action on the dense source image by
\[
V_t\pi F=e^{-t/2}\pi T_{e^t}F.
\tag{CFP2.3}
\]
The radical is invariant, and (CFP2.2) shows that this is an isometry with inverse \(V_{-t}\). It extends uniquely to a unitary on \(H_B\). Source continuity proves strong continuity on the dense image; the unitary norm bound and approximation by that image prove it on all of \(H_B\). The group law follows on the dense image and hence everywhere.

The exact original action is still
\[
\boxed{\pi T_{e^t}=e^{t/2}V_t\pi.}
\tag{CFP2.4}
\]
Thus its degree is not removed or replaced. The auxiliary unitary group is the specified comparison of the original action with the positive degree character. In particular, for every source \(H\in\mathcal B\),
\[
\left.\frac d{dt}\right|_{t=0}V_t\pi q(H)
=\pi q((s-1/2)H).
\tag{CFP2.5}
\]
The derivative exists in the Hilbert norm because it already exists in the stronger source topology.

## CFP3. The complete original-zeta source integral

Retain the original even Schwartz vector and the complete summation map:
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
\Sigma f(u)=2\sum_{n\ge1}f(nu),\qquad
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u}.
\tag{CFP3.1}
\]
The two source conditions are \(f_0(0)=0\) and \(\int_{\mathbb R}f_0=0\). The second follows from
\(\int v^2e^{-\pi v^2}dv=1/(2\pi)\) and
\(\int v^4e^{-\pi v^2}dv=3/(4\pi^2)\).

For the Fourier convention \(\widehat f(y)=\int f(v)e^{-2\pi ivy}dv\), differentiation of the Gaussian transform gives
\[
\widehat{v^2e^{-\pi v^2}}(y)
=(1/(2\pi)-y^2)e^{-\pi y^2},
\]
\[
\widehat{v^4e^{-\pi v^2}}(y)
=(y^4-3y^2/\pi+3/(4\pi^2))e^{-\pi y^2}.
\tag{CFP3.2}
\]
Substitution of the two original coefficients proves \(\widehat f_0=f_0\), including cancellation of the constant coefficient. Poisson summation on this Schwartz vector, with both zero terms zero, yields
\[
\Sigma f_0(u)=u^{-1}\Sigma f_0(u^{-1}).
\tag{CFP3.3}
\]
Here the Poisson identity itself follows by periodizing a Schwartz function, computing its Fourier coefficients by termwise integration, and evaluating its absolutely convergent Fourier series at zero. Thus no unsupported zero term has been silently discarded.

Put
\[
\boxed{k(t)=\frac12e^{t/2}\Sigma f_0(e^t)
=e^{t/2}\sum_{n\ge1}
\frac\pi2 n^2e^{2t}(2\pi n^2e^{2t}-3)
e^{-\pi n^2e^{2t}}.}
\tag{CFP3.4}
\]
Equation (CFP3.3) gives \(k(-t)=k(t)\). For \(t\ge0\), the absolute value of the summand is bounded by \(C n^4e^{(9/2)t}e^{-\pi n^2e^{2t}}\). Since \(n^2x\ge(n^2+x)/2\) for \(n\ge1\), \(x\ge1\),
\[
|k(t)|\le C_0\exp\bigl((9/2)|t|-(\pi/2)e^{2|t|}\bigr).
\tag{CFP3.5}
\]
The constant \(C_0\) includes the finite sum \(\sum n^4e^{-\pi n^2/2}\) and the original two polynomial coefficients. This bound proves integrability against \(|t|^j e^{R|t|}\) for every finite \(j,R\).

The exact source transform, with original \(\zeta\) explicit, is
\[
\begin{aligned}
\int_{\mathbb R}k(t)e^{(s-1/2)t}\,dt
&=\frac12\int_0^\infty\Sigma f_0(u)u^s\frac{du}{u}\\
&=\zeta(s)\int_0^\infty f_0(v)v^s\frac{dv}{v}\\
&=\boxed{\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s)=F_0(s)}.
\end{aligned}
\tag{CFP3.6}
\]
The second identity first holds on \(\Re s>1\) by absolute convergence. The Mellin integral there is
\[
\frac12\pi^{-s/2}\Gamma((s+4)/2)
-\frac34\pi^{-s/2}\Gamma((s+2)/2)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
\tag{CFP3.7}
\]
This records both Gaussian summands before their exact Gamma recursion. The left side of (CFP3.6) is entire by (CFP3.5), so the equality continues through every exceptional point. No completed zeta is used as a replacement for original \(\zeta\); \(F_0\) is this proved source multiplier.

All endpoint and trivial-zero values remain in that comparison:
\[
F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0\quad(r\ge1).
\tag{CFP3.8}
\]
At zero use \(\Gamma(s/2)=2/s+O(1)\) and \(\zeta(0)=-1/2\); at one use the original zeta residue one. At \(-2r\), use the Gamma residue \(2(-1)^r/r!\) and the original simple trivial zero. Its nonzero derivative follows directly from the original functional equation
\[
\zeta(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s).
\tag{CFP3.9}
\]
Differentiating its simple sine zero supplies the derivative in (CFP3.8); reflection of the full product supplies the displayed value at \(1+2r\). On the open critical strip, every multiplier in (CFP3.6) is a holomorphic unit. Consequently the zeros of \(F_0\) are exactly the original nontrivial zeta zeros with their unchanged multiplicities.

To retain all derivative terms as well, write only as an auxiliary notation
\(M_0(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/8\). On every nonexceptional germ,
\[
F_0^{(r)}(s)=\sum_{j=0}^r\binom rj M_0^{(j)}(s)\zeta^{(r-j)}(s),
\]
\[
M_0^{(j)}(s)=\sum_{j_0+j_1+j_2=j}
\frac{j!}{j_0!j_1!j_2!}
\left(\frac{s(s-1)}8\right)^{(j_0)}
\left(-\frac{\log\pi}2\right)^{j_1}\pi^{-s/2}
2^{-j_2}\Gamma^{(j_2)}(s/2).
\tag{CFP3.10}
\]
The entire continuation at exceptional points is given by the integral, whose exact derivatives are \(\int t^rk(t)e^{(s-1/2)t}dt\). No Gamma, endpoint or scale derivative is replaced by a constant.

## CFP4. The source annihilator is an actual convergent group integral

For each \(F\in\mathcal B\),
\[
b_{A,M}(k(t)e^{t(s-1/2)}F)
\le |k(t)|e^{(A+1/2)|t|}b_{A,M}(F).
\tag{CFP4.1}
\]
This bound is integrable by (CFP3.5). Integrating on finite intervals and passing to the limit in every seminorm therefore defines an integral in the complete Fréchet space \(\mathcal B\). Point evaluation is continuous, so (CFP3.6) identifies that integral exactly:
\[
\int_{\mathbb R} k(t)e^{t(s-1/2)}F(s)\,dt
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s)F(s).
\tag{CFP4.2}
\]
This product belongs to \(\mathcal I\), since every required zero order occurs in the full \(F_0\) factor. It follows, after the continuous maps \(q\) and \(\pi\), that
\[
\int_{\mathbb R}k(t)V_t\pi q(F)\,dt=0.
\tag{CFP4.3}
\]
As \(k\in L^1(\mathbb R)\) and \(V_t\) is unitary, its Hilbert integral is a bounded operator of norm at most \(\|k\|_1\). Equation (CFP4.3) holds on a dense image, hence
\[
\boxed{\int_{\mathbb R}k(t)V_t\,dt=0\quad\text{on all of }H_B.}
\tag{CFP4.4}
\]
This is an annihilation of the completed receiver by the original source vector. It neither identifies \(F_0\) with original \(\zeta\) nor declares that the original source quotient is a quotient by the principal ideal \(F_0\mathcal B\). Only the proved inclusion \(F_0\mathcal B\subset\mathcal I\) has been used.

## CFP5. Spectral support and the complete atomic decomposition

The analytic lemma CFPA below is proved for any strongly continuous unitary group and any \(L^1\) annihilating kernel. Applying it to (CFP4.4) gives spectral support in
\[
\Gamma=\{\gamma\in\mathbb R:
\frac{(1/2+i\gamma)(-1/2+i\gamma)}8
\pi^{-(1/2+i\gamma)/2}
\Gamma((1/2+i\gamma)/2)\zeta(1/2+i\gamma)=0\}.
\tag{CFP5.1}
\]
All factors outside \(\zeta\) in this formula are nonzero and finite. Thus \(\Gamma\) is exactly the set of ordinates of actual critical-line zeros of original \(\zeta\). It is discrete and countable; it has finitely many elements in every compact interval because the entire nonzero source function \(F_0\) has isolated zeros.

There are mutually orthogonal projections \(P_\gamma\) with
\[
V_tP_\gamma=e^{it\gamma}P_\gamma,
\qquad x=\sum_{\gamma\in\Gamma}P_\gamma x,
\qquad \|x\|^2=\sum_{\gamma\in\Gamma}\|P_\gamma x\|^2.
\tag{CFP5.2}
\]
The series converges in norm, and every zero projection is permitted. Explicitly,
\[
P_\gamma x=\lim_{R\to\infty}\frac1{2R}
\int_{-R}^{R}e^{-it\gamma}V_tx\,dt.
\tag{CFP5.3}
\]
The proof in CFPA uses the full source integral and scalar positive measures, not any assumed density of finite original jets. The original degree action on this fibre remains
\[
\pi T_{e^t}=e^{t/2}V_t\pi,
\qquad T_{n,\gamma}=n^{1/2+i\gamma},
\qquad \mathsf U_{n,\gamma}=n^{1/2-i\gamma}.
\tag{CFP5.4}
\]

## CFP6. Division forces rank one and detects every killed jet

Fix \(\gamma\in\Gamma\), put \(\rho=1/2+i\gamma\), and retain the entire Gaussian
\[
g_\rho(s)=e^{(s-\rho)^2},\qquad g_\rho(\rho)=1.
\tag{CFP6.1}
\]
It belongs to \(\mathcal B\). For arbitrary \(F\in\mathcal B\), define
\[
H_{F,\rho}(s)=\frac{F(s)-F(\rho)g_\rho(s)}{s-\rho}.
\tag{CFP6.2}
\]
The singularity at \(\rho\) is removable. This division remains in \(\mathcal B\): outside a disk about \(\rho\), the denominator is bounded below; inside that disk, the holomorphic quotient is bounded by its value on a larger boundary circle, and each polynomial weight is bounded there. Applying this argument on every strip, with a slightly enlarged strip for that circle, proves all defining seminorms finite. No infinite interpolation assertion is needed.

Differentiate the eigenprojection identity \(P_\gamma V_t=e^{it\gamma}P_\gamma\) on the actual smooth vector \(\pi q(H_{F,\rho})\). By (CFP2.5),
\[
P_\gamma\pi q((s-1/2)H_{F,\rho})
=i\gamma P_\gamma\pi q(H_{F,\rho}).
\]
Therefore
\[
\boxed{P_\gamma\pi q(F)
=F(\rho)v_\rho,\qquad
v_\rho=P_\gamma\pi q(g_\rho).}
\tag{CFP6.3}
\]
Since \(\pi q(\mathcal B)\) is dense, the range of \(P_\gamma\) is the closure of its image on that dense set. Formula (CFP6.3) proves
\[
\operatorname{Ran}P_\gamma=\mathbb C v_\rho;
\quad\dim\operatorname{Ran}P_\gamma\in\{0,1\}.
\tag{CFP6.4}
\]
The possible zero dimension is retained. This is the required multiplicity statement for the positive receiver, not a simplicity assertion about zeta.

The original source still has its full local algebra \(\mathbb C[z]/(z^{m_\rho})\). The exact globally realized block map is
\[
\sum_{j=0}^{m_\rho-1}a_jz^j\longmapsto
\begin{cases}a_0v_\rho,&\Re\rho=1/2,\\0,&\Re\rho\ne1/2.\end{cases}
\tag{CFP6.5}
\]
To verify it globally, use the RD1 isolator \(e_{\rho,j}\), whose required jets vanish at every other actual zero. Equation (CFP6.3) and the complete decomposition (CFP5.2) give (CFP6.5). In particular the kernel on a block with \(v_\rho\ne0\) consists of all \(m_\rho-1\) higher-jet directions; when \(v_\rho=0\) or the zero is off-line, it is the entire original \(m_\rho\)-dimensional block. No source class is declared zero in \(\mathcal Q\) merely because this map kills it.

## CFP7. The exact weights and their necessary growth

By (CFP5.2) and (CFP6.3), for arbitrary original classes,
\[
B(F,G)=\sum_{\rho\in\mathscr Z_{\rm line}}
w_\rho F(\rho)\overline{G(\rho)},
\qquad w_\rho=\|v_\rho\|^2\ge0.
\tag{CFP7.1}
\]
The sum is absolutely convergent by Cauchy–Schwarz applied to the two norm-convergent orthogonal expansions. Retain the original multiplicity by defining
\[
c_\rho=w_\rho/m_\rho.
\tag{CFP7.2}
\]
This gives exactly (CFP0.4). The weights are unique: testing on the original isolator \(e_{\rho,0}\) gives \(B(e_{\rho,0},e_{\rho,0})=w_\rho\). The multiplicity has not been replaced by one; \(w_\rho\) is the total scalar mass of this receiver, while \(c_\rho\) is its coefficient relative to the original multiplicity trace.

For the continuity bound (CFP1.2), the Gaussian satisfies
\[
|g_\rho(\sigma+iy)|=e^{(\sigma-1/2)^2-(y-\gamma)^2},
\]
\[
b_{A,M}(g_\rho)\le
e^{(A+1/2)^2}(1+|\gamma|)^M
\sup_{u\in\mathbb R}(1+|u|)^M e^{-u^2}.
\tag{CFP7.3}
\]
The last supremum is finite. Since \(P_\gamma\) is an orthogonal projection,
\[
0\le m_\rho c_\rho=w_\rho
\le\|\pi q(g_\rho)\|^2
\le C'(1+|\gamma|)^{2M}.
\tag{CFP7.4}
\]
As \(m_\rho\ge1\), this proves the necessary polynomial bound on \(c_\rho\). It also proves the stronger polynomial bound on its actual atomic mass \(m_\rho c_\rho\). No uniform lower bound for zero spacing, isolator coefficients, or \(\zeta'(\rho)\) is involved.

## CFP8. Every indicated polynomial family gives a continuous form

Human-source attribution: the unconditional count used here is the classical Riemann–von Mangoldt theorem. The inspected witness already documented at PTQ8 is Alain Connes, [*The Riemann Hypothesis: Past, Present and a Letter Through Time*](https://arxiv.org/abs/2602.04022v1), the Hardy–Littlewood discussion preceding “Zero-free regions and zero-density estimates.” Its asymptotic implies the bound below; this is not a new zero-counting theorem.

Conversely suppose \(0\le c_\rho\le C(1+|\gamma|)^d\). The actual zero count with multiplicities is
\[
N(R)=\sum_{\rho\in\mathscr Z,\ |\Im\rho|\le R}m_\rho
=O(R\log(R+2)).
\tag{CFP8.1}
\]
This unconditional count is one of the original divisor estimates already used in RTT1. It does not impose RH. By grouping zeros into dyadic height intervals, it implies
\(\sum_\rho m_\rho(1+|\Im\rho|)^{-q}<\infty\) for every \(q>1\).
Choose an integer \(M\) with \(2M-d>2\). Then
\[
\sum_{\rho\in\mathscr Z_{\rm line}}
m_\rho c_\rho |F(\rho)|^2
\le C b_{1,M}(F)^2
\sum_{\rho\in\mathscr Z}m_\rho(1+|\Im\rho|)^{d-2M}<\infty.
\tag{CFP8.2}
\]
Cauchy–Schwarz proves absolute convergence of the two-variable form and joint continuity on \(\mathcal B\). It annihilates \(\mathcal I\) in either argument and hence gives a jointly continuous form on the quotient: take the infimum of the displayed seminorm bound over representatives in each argument. Its positivity is termwise.

For every \(n\ge1\), on a retained coordinate \(\overline\rho=1-\rho\), so
\[
\overline{n^{1-\rho}}=n^\rho.
\]
Substitution in the absolutely convergent sums gives exactly
\(B(T_nF,G)=B(F,nT_{1/n}G)\). This proves sufficiency and completes the classification.

## CFP9. Universal source kernel, without a value-norm hypothesis

For a particular weight family define
\[
\mathscr Z_c=\{\rho\in\mathscr Z_{\rm line}:c_\rho>0\},
\qquad
\mathcal K_c=\{[F]\in\mathcal Q:F(\rho)=0\text{ for every }\rho\in\mathscr Z_c\}.
\tag{CFP9.1}
\]
Equation (CFP0.4) proves that this is exactly the radical. The completion is canonically
\[
\overline{\mathcal Q/\mathcal K_c}^{,B}
\simeq\ell^2(\mathscr Z_c,m_\rho c_\rho),
\tag{CFP9.2}
\]
with map \([F]\mapsto(F(\rho))_{\rho\in\mathscr Z_c}\). The norm identity follows from the formula. Every finite sequence occurs, by the actual full-jet isolators, and finite sequences are dense in the displayed weighted Hilbert space. This proves surjectivity of the map on completions without any claim about finite-jet density in the original topology.

The intersection of radicals of **all** continuous positive forms satisfying the original transfer identities is therefore exactly
\[
\boxed{\mathcal K_{\rm all}
=\{[F]:F(\rho)=0\quad(\rho\in\mathscr Z_{\rm line})\}
=\mathcal I_{\mathscr Z_{\rm line}}^{\rm val}/\mathcal I.}
\tag{CFP9.3}
\]
Every classified form kills this space. Conversely the choice \(c_\rho=1\) is permitted by CFP8 and detects every class outside it. Thus this common kernel is proved in the actual Fréchet category, rather than inferred from boundedness in PTQ's auxiliary value norm.

At an individual original nontrivial zero, the scalar relation responsible for this kernel can also be checked directly: \(B(T_nx,T_nx)=nB(x,x)\) forces a pure eigenvector of exponent \(\rho\) to have zero norm when \(n^{2\Re\rho}\ne n\). The global argument above additionally proves that no continuous residual sector escapes this finite-coordinate calculation and that all higher jets are killed. That global assertion is precisely what finite-support computations alone do not supply.

## CFP10. Every continuous positive Hilbert receiver factors through the classified kernel

Let \(X:\mathcal Q\to K\) be a continuous linear map into a Hilbert space, with bounded receiving operators \(A_n,C_n\) such that
\[
XT_n=A_nX,\quad X\mathsf U_n=C_nX,\quad C_n=A_n^*.
\tag{CFP10.1}
\]
Its pulled-back form \(B_X(F,G)=\langle XF,XG\rangle\) is jointly continuous, positive, and satisfies (CFP0.3). Consequently
\[
X\mathcal K_{\rm all}=0,
\quad X:\mathcal Q\longrightarrow\mathcal Q/\mathcal K_{\rm all}
\longrightarrow K
\tag{CFP10.2}
\]
is a unique continuous factorization in the quotient topology. The classification supplies its exact nonnegative polynomial weights and identifies the completion of its image with (CFP9.2). The original degree relation is retained: on the closed span of \(X\mathcal Q\), the identities imply \(A_n^*A_n=nI\), since it holds on the dense image.

Thus allowing arbitrary continuous Hilbert receivers from the source creates additional polynomial weights, but creates no additional supported zero, off-line value, or nonconstant jet direction compatible with a positive adjoint. This is an exact comparison with PTQ: bounded forms on its specified \(H\) correspond to the subfamily with bounded \(c_\rho\); continuity on the stronger source permits the polynomially growing families of (CFP0.4).

## CFP11. The original Weil form and all arithmetic contributions remain

Retain the original source Weil form and its exact zero observation:
\[
W(F,G)=\sum_{\rho\in\mathscr Z}m_\rho
F(\rho)\overline{G(1-\overline\rho)}.
\tag{CFP11.1}
\]
RTT1 and the count (CFP8.1) prove joint continuity; substitution proves the original transfer identity. At a line zero its contribution is the \(c_\rho=1\) contribution in (CFP0.4). For an off-line reflected orbit, retain both actual terms
\[
m_\rho\bigl(F(\rho)\overline{G(\rho^\#)}
+F(\rho^\#)\overline{G(\rho)}\bigr),
\qquad \rho^\#=1-\overline\rho.
\tag{CFP11.2}
\]
The globally realized difference \(e_{\rho,0}-e_{\rho^\#,0}\) has value \(-2m_\rho\) under \(W\). The sum has value \(+2m_\rho\). Both statements follow by direct substitution with all other values zero. The classification therefore does not make this original form positive by a change of source topology: it identifies exactly the space that every positive transfer form would have to kill.

For completeness retain the actual arithmetic receiver from RTT9. Put
\[
A_{F,G}(s)=F(s)\overline{G(1-\overline s)},\qquad
A_{F,G}(s)=\int_{\mathbb R}h(v)e^{-(s-1/2)v}dv,
\quad\widehat h(t)=\int_{\mathbb R}h(v)e^{-itv}dv.
\]
Then the unchanged full formula is
\[
W(F,G)=A_{F,G}(0)+A_{F,G}(1)+A_\infty(h)-P_{\rm hist}(h),
\]
\[
A_\infty(h)=\frac1{2\pi}\int_{\mathbb R}\widehat h(t)
\left(\Re\frac{\Gamma'(1/4+it/2)}{\Gamma(1/4+it/2)}-\log\pi\right)dt,
\]
\[
P_{\rm hist}(h)=\sum_{n\ge2}
\frac{\log L_n-\log L_{n-1}}{\sqrt n}
\bigl(h(\log n)+h(-\log n)\bigr),\quad
L_n=\operatorname{lcm}(1,\ldots,n).
\tag{CFP11.3}
\]
The coefficient is the original \(\Lambda(n)\), with every prime-power repetition. At each finite trivial-zero cutoff \(R\), retain also
\[
V_{\zeta,R}=W(F,G)+\sum_{r=1}^RA_{F,G}(-2r)-A_{F,G}(1),
\]
\[
G_R=A_\infty(h)+A_{F,G}(0)+\sum_{r=1}^RA_{F,G}(-2r),
\qquad V_{\zeta,R}=G_R-P_{\rm hist}(h).
\tag{CFP11.4}
\]
These are the original proved RTT/GIQ identities, retained here without a divergent infinite trivial-zero sum. No weighted form with arbitrary \(c_\rho\), and no compression removing (CFP11.2), is asserted to equal their right side. The original supported endpoints and their coefficient labels remain those in that established source formula.

## CFP12. The next calculation performed: the exact source-topology kernel

The issue left by PTQ was whether its value-Hilbert boundedness excluded other continuous positive source forms carrying hidden higher jets or off-line data. CFP1–CFP10 answer that question by the full source integral, the actual unitary completion and exact Gaussian division: no such additional continuous directions exist, and the complete additional freedom is the polynomial family of weights.

This does not prove that \(\mathcal K_{\rm all}\) consists only of the original higher-jet radical. Their precise difference is retained:
\[
\mathcal N_0=\{[F]:F(\rho)=0\ \forall\rho\in\mathscr Z\}
\subset\mathcal K_{\rm all},
\qquad
\mathcal K_{\rm all}/\mathcal N_0
\cong\frac{\mathcal I_{\mathscr Z_{\rm line}}^{\rm val}}
{\mathcal I_{\mathscr Z}^{\rm val}}.
\tag{CFP12.1}
\]
The displayed isomorphism is induced by the identity on representatives; its kernel and surjectivity follow directly from the two quotients. It retains the actual off-line value data. The existing off-line value observation injects this quotient into \(H_{\rm off}\), with dense image by the full original isolators. Thus the exact obstruction exposed by extending PTQ is the same source-topological off-line observation, rather than an unknown class of unbounded positive forms. The receiver of the remaining geometric comparison is now fixed without a value-norm hypothesis.

One further exact consequence records what a faithful positive form would mean. A classified form is positive definite on the **full** \(\mathcal Q\) exactly when every actual zero lies on the line, every multiplicity is one, and every \(c_\rho\) is strictly positive. Necessity follows respectively from an off-line isolator, a higher-jet isolator, or a value isolator at a zero-weight coordinate. Sufficiency follows because a nonzero full-jet class then has a nonzero retained value. This statement is not used to demand simplicity for ordinary Weil positivity: the original Weil form is allowed its precisely identified higher-jet radical.

## CFPA. Proof of the unitary annihilator lemma used above

Human-source attribution added for publication: the positive Fourier-measure representation is Bochner’s classical theorem; see Terence Tao, [245C Notes 2, Theorem 57](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/). The proof below supplies this special case with its displayed Fourier convention and all constants; no novelty is claimed for that theorem.

Here is a proof of exactly the spectral facts used in CFP5. It is included to avoid leaving a new spectral assertion implicit. Basic Fourier inversion for integrable functions, Gaussian Fourier integration, the Riesz representation theorem for finite measures, and Hilbert completion are used with their usual stated domains.

For the classical Fourier inversion theorem, see Tao, [245C Notes 2, equation (11)](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/); the Fourier convention and constants below are retained. The weak-star compactness used below is Banach--Alaoglu; see Tao, [245B Notes 11, Theorem 3](https://terrytao.wordpress.com/2009/02/21/245b-notes-11-the-strong-and-weak-topologies/).

Let \((V_t)_{t\in\mathbb R}\) be a strongly continuous unitary group on a Hilbert space \(H\). For \(x\in H\) set
\[
f_x(t)=\langle V_tx,x\rangle.
\tag{CFPA.1}
\]
This function is continuous, bounded by \(\|x\|^2\), and positive definite: for finite coefficients,
\[
\sum_{i,j}a_i\overline{a_j}f_x(t_i-t_j)
=\left\|\sum_i a_iV_{t_i}x\right\|^2\ge0.
\tag{CFPA.2}
\]

First prove the positive Fourier-measure representation needed here. If \(f\) is continuous positive definite, then \(f(0)\ge0\), \(f(-t)=\overline{f(t)}\), and \(|f(t)|\le f(0)\), by the two-point positive matrix. For \(\varepsilon>0\), put \(f_\varepsilon(t)=f(t)e^{-\varepsilon t^2}\). The Gaussian is a positive mixture of characters, so integrating (CFPA.2) after multiplying the coefficients by those characters proves that \(f_\varepsilon\) is positive definite. It is also integrable.

Define
\[
p_\varepsilon(\lambda)=\frac1{2\pi}
\int_{\mathbb R}f_\varepsilon(t)e^{-it\lambda}dt.
\tag{CFPA.3}
\]
This is continuous and nonnegative. To prove the sign, positive definiteness, approximation of integrals by finite sums, and the interval function \(e^{-i\lambda t}1_{[-R,R]}(t)\) show
\[
0\le\frac1{2R}\int_{-R}^R\int_{-R}^R
f_\varepsilon(t-u)e^{-i\lambda(t-u)}dt\,du
=\int_{-2R}^{2R}
\left(1-\frac{|v|}{2R}\right)
f_\varepsilon(v)e^{-i\lambda v}dv.
\]
Dominated convergence as \(R\to\infty\) proves (CFPA.3) is nonnegative. It is real because of the conjugate symmetry.

For \(\delta>0\), Fourier integration and Fubini give
\[
\int_{\mathbb R}e^{-\delta\lambda^2}p_\varepsilon(\lambda)d\lambda
=\frac1{2\sqrt{\pi\delta}}
\int_{\mathbb R}e^{-t^2/(4\delta)}f_\varepsilon(t)dt
\longrightarrow f(0)
\quad(\delta\downarrow0).
\tag{CFPA.4}
\]
Monotone convergence on the nonnegative left side proves \(\int p_\varepsilon=f(0)\). Fourier inversion, now with both transforms integrable, gives
\(f_\varepsilon(t)=\int e^{it\lambda}p_\varepsilon(\lambda)d\lambda\).

The measure-representation step uses the classical Riesz representation theorem for positive functionals, not Hilbert-space Riesz representation; see Terence Tao, [245B Notes 12, Theorem 24](https://terrytao.wordpress.com/2009/03/02/245b-notes-12-continuous-functions-on-locally-compact-hausdorff-spaces/). The mass and tightness calculation in this application follows explicitly.

The finite positive measures \(\mu_\varepsilon=p_\varepsilon d\lambda\), of this fixed total mass, have a weakly convergent subnet as functionals on \(C_0(\mathbb R)\), by weak-star compactness. There is no loss of mass at infinity as \(\varepsilon\downarrow0\): for \(a>0\),
\[
\int\left(1-\frac{\sin(a\lambda)}{a\lambda}\right)d\mu_\varepsilon
=f(0)-\frac1{2a}\int_{-a}^a f_\varepsilon(t)dt.
\tag{CFPA.5}
\]
The right side tends uniformly to zero when \(a\downarrow0\) and \(0<\varepsilon\le1\), by continuity of \(f\) at zero. The integrand is at least \(1/2\) when \(|\lambda|\ge2/a\). Thus the measures are uniformly tight. Riesz representation gives a finite positive limiting measure \(\mu\), with total mass \(f(0)\). Tightness allows the convergence to be tested against the bounded character \(e^{it\lambda}\), by a compact cutoff and a uniformly small tail. It follows that
\[
f(t)=\int_{\mathbb R}e^{it\lambda}d\mu(\lambda),
\qquad \mu(\mathbb R)=f(0).
\tag{CFPA.6}
\]
Uniqueness follows from Gaussian smoothing: a finite complex measure with identically zero Fourier transform has zero convolution with every Gaussian, by Fubini and the Gaussian inversion formula; those Gaussian convolutions approximate the measure against every continuous compactly supported test, so the measure is zero. This proves the required representation without an unproved spectral decomposition.

Apply this result to \(f_x\), obtaining \(\mu_x\) with total mass \(\|x\|^2\). For \(h\in L^1(\mathbb R)\), the Bochner integral \(V(h)x=\int h(t)V_tx\,dt\) exists and satisfies
\[
\|V(h)x\|^2
=\int_{\mathbb R}\left|\int_{\mathbb R}h(t)e^{it\lambda}dt\right|^2d\mu_x(\lambda).
\tag{CFPA.7}
\]
Indeed expand its squared norm as a double integral with integrand \(h(t)\overline{h(u)}f_x(t-u)\), then use (CFPA.6) and Fubini. The bound \(|f_x|\le\|x\|^2\) supplies absolute integrability.

If \(V(k)=0\), (CFPA.7) proves that \(\mu_x\) is supported on the zero set of \(\varphi(\lambda)=\int k(t)e^{it\lambda}dt\). More explicitly, its complement is the union of the measurable sets \(\{|\varphi|\ge1/j\}\), each of zero measure. Suppose this zero set is a discrete countable set \(\Gamma\), as it is in (CFP5.1).

For each \(\gamma\in\Gamma\) take
\[
h_{R,\gamma}(t)=\frac1{2R}e^{-it\gamma}1_{[-R,R]}(t),
\qquad
\int h_{R,\gamma}(t)e^{it\lambda}dt
=\frac{\sin(R(\lambda-\gamma))}{R(\lambda-\gamma)},
\tag{CFPA.8}
\]
with value one at \(\lambda=\gamma\). These multipliers converge pointwise to the indicator of \(\{\gamma\}\) and are bounded by one. Formula (CFPA.7), applied to differences of the \(h_{R,\gamma}\), and dominated convergence show that \(V(h_{R,\gamma})x\) is Cauchy. Call its limit \(P_\gamma x\). Its norm is
\[
\|P_\gamma x\|^2=\mu_x(\{\gamma\}).
\tag{CFPA.9}
\]
Changing the interval of integration by a fixed translation changes its average in norm by at most \(|a|\|x\|/R\). Hence
\(V_aP_\gamma x=e^{ia\gamma}P_\gamma x\). Conversely if \(y\) is an eigenvector with this character, then \(V(h_{R,\gamma})y=y\). If \(x\) is orthogonal to all such eigenvectors, each average remains orthogonal to them, by unitarity and their eigenvector property; so its limit is zero. These facts prove that \(P_\gamma\) is exactly the orthogonal projection onto that eigenspace.

Different frequencies have orthogonal eigenspaces, because invariance of an inner product multiplies it by \(e^{it(\gamma-\eta)}\) for every \(t\). Finally (CFPA.9), countable additivity, and the support assertion give
\[
\sum_{\gamma\in\Gamma}\|P_\gamma x\|^2
=\mu_x(\Gamma)=\mu_x(\mathbb R)=\|x\|^2.
\tag{CFPA.10}
\]
Orthogonality now proves \(x=\sum P_\gamma x\) in norm. This proves every spectral statement used in CFP5, including possible zero fibres and completeness. In particular there is no undeclared continuous spectral remainder.

## Proof sources and reading scope

The full PTQ0–PTQ11 proof was read for the earlier bounded category. The relevant RTT0–RTT2, RTT5–RTT11 and RD1–RD5 were read for the actual Fréchet quotient, exact isolators, full residue and degree maps. PGF5.1–PGF5.8 and the exact Gaussian formula were read for the original Schwartz source; the preceding derivation recomputes its Fourier and Mellin constants. PSC0–PSC2 were read for the precise source kernel and quotient topology. The arithmetic identity in CFP11 is the retained proved RTT9/GIQ9 identity, not a new independent derivation of the explicit formula.

Original derivation reading record, retained as provenance: the private canonical-index title query for spectral-theorem, unitary-group and positive-definite-function sources returned no relevant exact original source for the unitary-measure argument; unrelated routing hits were not counted as reading. CFPA supplies the needed proof directly. At that derivation stage no newly located human paper was cited as read, and no novelty claim was made for that classical analytic lemma. The Bochner attribution above was added for this publication edition; it does not retrospectively expand the derivation’s source-reading claim.
