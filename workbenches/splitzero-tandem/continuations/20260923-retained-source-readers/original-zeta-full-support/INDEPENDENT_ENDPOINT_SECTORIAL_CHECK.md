# Independent verification of the endpoint sectorial heat extension

Date: 2026-09-23. Read all of ENDPOINT_SECTORIAL_HEAT_EXTENSION.tex, ESH1–16, including the domain and scope statements. This check preserves the original coordinate \(s=\frac12+\frac{iZ}{2}\), every original multiplier, and physical time \(t\).

## ESC1. The original density

Set \(A(s)=\pi^{-s/2}\Gamma(s/2)\), \(\psi(x)=\sum_{n\ge1}e^{-\pi n^2x}\). The full theta formula is
\[
A(s)\zeta(s)=\frac1{s-1}-\frac1s+
\int_1^\infty\psi(x)[x^{s/2-1}+x^{-(s+1)/2}]\,dx.
\]
Under \(x=e^{4u}\), the two integrands become \(4e^{2su}\psi(e^{4u})\) and \(4e^{(2-2s)u}\psi(e^{4u})\). Their sum is \(8e^u\psi(e^{4u})\cos(Zu)\). Also
\[
\frac1{s-1}-\frac1s=\frac1{s(s-1)}=-\frac4{1+Z^2}.
\tag{ESC1}
\]
For \(|\Im Z|<1\), \(\int_0^\infty e^{-u}\cos(Zu)\,du=(1+Z^2)^{-1}\). Thus the full density is exactly
\[
\rho(u)=8e^u\psi(e^{4u})-4e^{-u},\qquad
A(s)\zeta(s)=\int_0^\infty\rho(u)\cos(Zu)\,du.
\tag{ESC2}
\]

The theta term and all its derivatives decay faster than every Gaussian at positive infinity. Its derivatives add powers of \(n\) and \(e^u\), dominated by \(e^{-\pi n^2e^{4u}}\). The other term is the original endpoint \(e^{-u}\). Hence
\[
I_t(Z)=\int_0^\infty e^{tu^2}\rho(u)\cos(Zu)\,du
\tag{ESC3}
\]
converges, with all parameter derivatives locally uniformly, on \(\Re t<0,\ Z\in\mathbb C\). At real \(t>0,Z=0\), its endpoint contribution diverges negatively like \(-4e^{tu^2-u}\), while the theta part remains integrable. Thus continuation is necessary. No positive-time value of the same improper integral is established. At \(\Re t=0\) some additional strip convergence is possible; ESH uses an open convergence domain rather than claiming it is maximal.

## ESC2. The erfc sheets and their oriented jump

For real \(q>0\), completing the square proves
\[
F(q,a)=\int_0^\infty e^{-qu^2-au}\,du
=\frac{\sqrt\pi}{2\sqrt q}e^{a^2/(4q)}
\operatorname{erfc}\!\left(\frac a{2\sqrt q}\right).
\tag{ESC4}
\]
First take real \(a\); then both sides are entire in \(a\), by Gaussian domination for the integral and the entire erfc primitive for the other side. This proves the formula for complex \(a\). The square root positive at positive \(q\) defines the stated slit-plane branch. The entire primitive gives \(\operatorname{erfc}(z)+\operatorname{erfc}(-z)=2\).

At \(q=-t\), \(t>0\), approached respectively from above and below, \(\sqrt q=i\sqrt t\) and \(-i\sqrt t\). With \(z=a/(2i\sqrt t)\), the values are
\[
F_+=-\frac{i\sqrt\pi}{2\sqrt t}e^{-a^2/(4t)}\operatorname{erfc}(z),
\quad
F_-=\frac{i\sqrt\pi}{2\sqrt t}e^{-a^2/(4t)}\operatorname{erfc}(-z).
\]
Therefore
\[
F_+-F_-=-i\sqrt{\pi/t}\,e^{-a^2/(4t)}.
\tag{ESC5}
\]
The cosine endpoint is \(\frac12[F(q,1-iZ)+F(q,1+iZ)]\). Expanding the squares gives
\[
B_+-B_-=-i\sqrt{\pi/t}\,e^{(Z^2-1)/(4t)}\cos(Z/(2t)).
\tag{ESC6}
\]
The full endpoint coefficient is \(-4\), so
\[
I_+-I_-=4i\sqrt{\pi/t}\,e^{(Z^2-1)/(4t)}\cos(Z/(2t)).
\tag{ESC7}
\]
All factors and the upper-minus-lower \(q\)-plane orientation in ESH3–6 are correct.

The theta part \(L_t\) is jointly entire by its double-exponential majorant. The erfc formulas define local analytic branches at every nonzero continued time, with entire \(Z\)-dependence. Differentiating ESC3 gives \(\partial_tI=-\partial_Z^2I\) in \(\Re t<0\), and analytic continuation proves the same identity on each branch. This does not assert positive-time improper convergence.

## ESC3. Endpoint derivative and the full filter

Poisson summation yields
\[
\psi(x)=x^{-1/2}\psi(1/x)+(x^{-1/2}-1)/2.
\]
Its derivative at one gives
\(2\psi'(1)=-\psi(1)/2-1/4\), hence
\[
\rho'(0)=8\psi(1)+32\psi'(1)+4=0.
\tag{ESC8}
\]
Every term, including the endpoint derivative \(+4\), is needed.

For \(x=e^{4u}\),
\[
\frac{d^2}{du^2}(e^u\psi(x))
=e^u[\psi(x)+24x\psi'(x)+16x^2\psi''(x)].
\]
Since \((\partial_u^2-1)e^{-u}=0\),
\[
\frac{\rho''-\rho}{64}
=e^u[3x\psi'(x)+2x^2\psi''(x)]
=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}}
=\Phi(u).
\tag{ESC9}
\]
Thus the coefficients \(8,4,64,2,3\) all check directly.

Let \(D_t=Z-2t\partial_Z\). Its actual square is
\[
D_t^2=Z^2-2t-4tZ\partial_Z+4t^2\partial_Z^2.
\tag{ESC10}
\]
The derivative commutator supplies the \(-2t\). For \(W=e^{tu^2}\cos(Zu)\), one has \(W(0)=1,W'(0)=0\), and
\[
W''=e^{tu^2}[(2t+4t^2u^2-Z^2)\cos(Zu)-4tZu\sin(Zu)].
\]
Twice integrating by parts gives
\[
\int_0^\infty\rho''W=-\rho'(0)+\int_0^\infty\rho W''
=-\rho'(0)-D_t^2I_t.
\tag{ESC11}
\]
The boundaries at infinity vanish; the first at zero is \(-\rho'(0)\), and the second is zero because \(W'(0)=0\). Therefore
\[
\mathcal N_t=-\frac{1+D_t^2}{64},\qquad
\mathcal N_tI_t=H_t.
\tag{ESC12}
\]
This follows first by ESC8–9 in the open convergence domain and then on the two continued branches. The \(H_t\) integral itself is jointly entire.

The individual endpoint contributions can also be checked without combining them prematurely. For density \(e^{-u}\), its derivative at zero is \(-1\), so ESC11 gives
\[
(1+D_t^2)B=1,\qquad \mathcal N_tB=-1/64.
\tag{ESC13}
\]
For the theta-only density \(8e^u\psi(e^{4u})\), its derivative at zero is \(-4\), so
\[
\mathcal N_tL_t=H_t-1/16.
\tag{ESC14}
\]
Consequently
\[
\mathcal N_t(L_t-4B)=(H_t-1/16)+1/16=H_t.
\tag{ESC15}
\]
This identifies both nonzero boundary terms and their exact cancellation. Applying the density filter to \(e^{-u}\) alone does not justify dropping its integration boundary.

## ESC4. Full entire kernel and the actual cosine subspace

For fixed \(t\ne0\), write \(f=e^{Z^2/(4t)}g\). This is an invertible change of entire-function coefficients, retaining the full exponential. Direct calculation gives
\[
D_tf=-2t e^{Z^2/(4t)}g',\qquad
(1+D_t^2)f=e^{Z^2/(4t)}(g+4t^2g'').
\]
The constant-coefficient equation has exactly two entire solutions determined by \(g(0),g'(0)\), as its Taylor recursion proves. Therefore
\[
\ker\mathcal N_t=
\left\{e^{Z^2/(4t)}
(c_+e^{iZ/(2t)}+c_-e^{-iZ/(2t)}):c_\pm\in\mathbb C\right\}.
\tag{ESC16}
\]
The basis functions are independent because their ratio is nonconstant.

Both actual continued cosine integrals are even in \(Z\). Evenness of ESC16 forces \(c_+=c_-\), so on this original source
\[
\ker(\mathcal N_t|_{\text{entire even}})
=\mathbb C\,e^{Z^2/(4t)}\cos(Z/(2t)).
\tag{ESC17}
\]
The odd sine direction belongs to the larger entire-function domain. The actual jump ESC7 lies in precisely the one-dimensional even part. Thus the full two-dimensional theorem ESH12 is correct as stated, but its use for the actual cosine branches should explicitly retain this one-dimensional restriction.

The time dependence of a kernel function that is itself a heat solution is equally exact. On a connected simply connected nonzero-time domain, assume its coefficients are holomorphic and \(\partial_tf=-\partial_Z^2f\). They can be recovered holomorphically from \(f(t,0)\) and \(\partial_Zf(t,0)\). For
\(\phi_\pm=e^{Z^2/(4t)\pm iZ/(2t)}\),
\[
\partial_t\phi_\pm+\partial_Z^2\phi_\pm
=\left(\frac1{2t}-\frac1{4t^2}\right)\phi_\pm.
\]
Independence therefore forces
\[
c_\pm'=\left(-\frac1{2t}+\frac1{4t^2}\right)c_\pm,\qquad
c_\pm=C_\pm t^{-1/2}e^{-1/(4t)}.
\tag{ESC18}
\]
Thus the exact two joint kernel-and-heat modes are
\[
t^{-1/2}e^{(Z+i)^2/(4t)},\qquad
t^{-1/2}e^{(Z-i)^2/(4t)}.
\tag{ESC19}
\]
Their symmetric combination is the only joint mode in the actual even source.

## ESC5. Original coordinate, full multiplier and differential receiver

Retain \(Z=-2i(s-\frac12)\). Then
\[
Z-2t\partial_Z=-i[(2s-1)+t\partial_s],
\]
and
\[
[(2s-1)+t\partial_s]^2
=(2s-1)^2+2t+2t(2s-1)\partial_s+t^2\partial_s^2.
\]
It follows that
\[
16\mathcal N_t
=s(s-1)+t/2+\frac{t(2s-1)}2\partial_s+\frac{t^2}4\partial_s^2.
\tag{ESC20}
\]
Using the exact identities \(I_\pm=Af_\pm\) and \(z_t=16H_t/[s(s-1)A]\) now gives
\[
z_t=
\frac{[s(s-1)+t/2]Af_\pm+
\frac{t(2s-1)}2\partial_s(Af_\pm)+
\frac{t^2}4\partial_s^2(Af_\pm)}
{s(s-1)A}.
\tag{ESC21}
\]
This verifies every coefficient in ESH15. Expanding gives
\((Af)'=A'f+Af'\) and \((Af)''=A''f+2A'f'+Af''\), with
\[
A'/A=-\tfrac12\log\pi+\tfrac12\psi_\Gamma(s/2),\qquad
A''/A=\tfrac14\psi_\Gamma'(s/2)
+[-\tfrac12\log\pi+\tfrac12\psi_\Gamma(s/2)]^2.
\tag{ESC22}
\]
Thus every derivative of the original multiplier remains present.

The fixed-time basis ESC16 becomes
\(e^{1/(4t)}e^{-s^2/t}\) and
\(e^{1/(4t)}e^{-(s-1)^2/t}\);
the full common factor is displayed here. The joint heat modes ESC19 become
\(t^{-1/2}e^{-s^2/t}\) and
\(t^{-1/2}e^{-(s-1)^2/t}\).
The symmetry \(Z\mapsto-Z\) is \(s\mapsto1-s\), interchanging the modes.

Expanding the cosine in ESC7 and substituting this exact coordinate gives
\[
I_+-I_-=2i\sqrt{\pi/t}
[e^{-s^2/t}+e^{-(s-1)^2/t}].
\]
Hence
\[
f_+-f_-=2i\sqrt{\pi/t}\,
\frac{\pi^{s/2}}{\Gamma(s/2)}
[e^{-s^2/t}+e^{-(s-1)^2/t}],
\tag{ESC23}
\]
with the complete factor required for ESH14. Numerator modes and returned-function modes are related by this full multiplier.

## ESC6. Time zero and exceptional domains

On \(0<\Re s<1\), equivalently \(|\Im Z|<1\), the endpoint of ESC3 has the majorant \(Ce^{-(1-|\Im Z|)u}\) as \(t\to0^-\); on compact subsets of that strip the margin is uniform. The theta part has stronger domination. Thus \(I_t\to A\zeta\) and \(f_t\to\zeta\) locally uniformly on the strip. At zero, ESC20 becomes \(16\mathcal N_0=s(s-1)\), proving the same initial original-zeta return for \(z_t\).

At any fixed nonzero time on a continued branch, \(I_\pm\) is entire in \(s\), and \(1/A=\pi^{s/2}/\Gamma(s/2)\) is entire. Therefore \(f_\pm\) is entire. The exact differential map ESC21 can nevertheless produce the returned meromorphic \(z_t\), whose pole at \(s=1\) for real \(t\) is established by the original returned-family proof. Equality first holds away from isolated exceptional factors and extends meromorphically with their full germs retained. Entire \(f_\pm\) cannot converge locally uniformly on a neighborhood of \(s=1\) to \(\zeta\), because such a limit would be holomorphic there. This is compatible with the proved open-strip convergence.

## Verification outcome

Every displayed ESH1–16 formula checks: full density, endpoint sign, erfc orientation, derivative at zero, filter commutator, full entire kernel, original-coordinate modes, differential coefficients, Gamma derivatives, and convergence versus continuation domains.

The required scope clarification is ESC17: the full two-dimensional kernel restricts to one dimension on the actual even cosine source, and the actual lateral jump uses exactly this symmetric direction. ESC18–19 give the exact time dependence of genuine homogeneous heat modes. ESC13–15 retain the individual nonzero integration-boundary contributions before their cancellation.

