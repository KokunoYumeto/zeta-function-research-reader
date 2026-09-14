# Original non-even Gaussian fixture for CM.3–5 and CM.9–12

The complete CM.1–19 source was read. The source SHA256 used for this
calibration is
`7f58291e609995d05f99249a19d8835d2e12c7c7c182b1890b9a4d158511bb3c`.
This report proves the stated identities for the explicit amplitude below.
The arithmetic-packet theorem remains a separate statement in its original
source; no identification of this fixture with that packet is made.

The calculation uses, for every real \(t\), the original amplitude
\[
a(t)=(t+1)e^{-t^2/2},\qquad
a'(t)=(1-t-t^2)e^{-t^2/2},\qquad
w(t)=(t+1)^2e^{-t^2}.
\]
It is real, smooth, and rapidly decreasing, with its original mass
\(\mu_0=3\sqrt\pi/2\). The exact difference
\(w(t)-w(-t)=4te^{-t^2}\) proves non-evenness. Every polynomial moment
and every real exponential integral used below is finite because of the
Gaussian factor. No amplitude or mass is rescaled.

## Original one-factor and product moments

Retain the definitions
\[
\mu_j=\int_{\mathbb R}t^ja(t)^2dt,\qquad
\nu_j=\int_{\mathbb R}t^ja'(t)^2dt,\qquad
\theta_j=\int_{\mathbb R}t^ja(t)a'(t)dt.
\]
For \(n\ge0\), direct integration of the Gaussian gives
\[
\int_{\mathbb R}t^{2n}e^{-t^2}dt
=\sqrt\pi\frac{(2n)!}{4^n n!},\qquad
\int_{\mathbb R}t^{2n+1}e^{-t^2}dt=0.
\]
The positive base integral has square
\(\int_{\mathbb R^2}e^{-x^2-y^2}dxdy
=2\pi\int_0^\infty re^{-r^2}dr=\pi\), so it equals \(\sqrt\pi\).
Integration by parts gives \(I_{2n}=(2n-1)I_{2n-2}/2\), proving the
even formula; reflection of the integrand proves the odd formula.
Multiplying the original polynomials before integration
therefore gives the following arrays, in order \(j=0,1,2,3,4\):
\[
(\mu_j)=\sqrt\pi\,(3/2,1,5/4,3/2,21/8),
\]
\[
(\nu_j)=\sqrt\pi\,(5/4,1/2,13/8,9/4,87/16),
\]
\[
(\theta_j)=\sqrt\pi\,(0,-3/4,-1,-15/8,-3).
\]
Here the subscripts \(\theta_j\) denote the CM.3 mixed moments, while
the unsubscripted real number \(\theta\) below is the exponential tilt.
Since \(aa'=w'/2\), integration by parts gives
\(\theta_0=0\) and \(\theta_j=-j\mu_{j-1}/2\) for every \(j\ge1\),
with all Gaussian boundary terms zero. Thus these arrays instantiate CM.3
without imposing evenness.

For \(k=2\), retain \(u=t_1+t_2\) and the original coefficient variable
\(S=1+iu\). Write
\[
P=(t_1+1)(t_2+1),\qquad
E_0=e^{-(t_1^2+t_2^2)/2},\qquad \Psi=P E_0.
\]
At fixed relative coordinate \(y=(t_1-t_2)/2\),
\(\partial_u=(\partial_{t_1}+\partial_{t_2})/2\). Thus
\[
\partial_u\Psi=R E_0,\qquad
R=\frac{(1-t_1-t_1^2)(t_2+1)+(t_1+1)(1-t_2-t_2^2)}2.
\]
This is direct differentiation of the original amplitude. In the same
order \(j=0,1,2,3,4\), polynomial expansion and the displayed Gaussian
moments give
\[
\left(\int u^jP^2E_0^2dt_1dt_2\right)
=\pi\,(9/4,3,23/4,12,117/4),
\]
\[
\left(\int u^jR^2E_0^2dt_1dt_2\right)
=\pi\,(15/16,1,49/16,33/4,423/16).
\]
The two factors in the product can also be integrated separately, giving
the exact identities
\[
M_{j,2}=\sum_{r=0}^j\binom jr\mu_r\mu_{j-r},
\]
\[
B_{j,2}=\frac12\sum_{r=0}^j\binom jr\nu_r\mu_{j-r}
+\frac12\sum_{r=0}^j\binom jr\theta_r\theta_{j-r}.
\]
In the second formula, the first sum comes from the two square terms in
\(R^2\), each retaining its factor \(1/4\). The second sum comes
from the two distinct-index terms, each retaining the same factor.
Substituting the proved mixed-moment identity gives zero for that second
sum when \(j<2\), and gives \(j(j-1)M_{j-2,2}/8\) when \(j\ge2\).
This is exactly CM.4 for this fixture, including the distinct-index term.

## The full original derivative Gram in \(1,S,S^2\)

For \(c_0=1,c_1=S,c_2=S^2\), the coefficient derivatives are
\(c_0'=0,c_1'=i,c_2'=2iS\). The original derivative of each complete
amplitude is
\[
\partial_u(\Psi c_j)=E_0(Rc_j+Pc_j').
\]
Set \(F_j=\Psi c_j\), with the convention
\(H^0_{ij}=\int\overline{F_i}F_j\) and
\(H^\partial_{ij}=\int\overline{\partial_uF_i}\partial_uF_j\).
Direct multiplication of the displayed polynomials gives
\[
H^0=\pi\begin{pmatrix}
9/4&9/4+3i&-7/2+6i\\
9/4-3i&8&8+15i\\
-7/2-6i&8-15i&43
\end{pmatrix},
\]
\[
H^\partial=\pi\begin{pmatrix}
15/16&15/16+i&1/8+2i\\
15/16-i&4&25/4+25i/4\\
1/8-2i&25/4-25i/4&53/2
\end{pmatrix}.
\]
The complete four-term calculation in CM.5 is retained separately:
\(H^\partial=H_B+H_P+C_1+C_2\), where
\[
H_B=\pi\begin{pmatrix}
15/16&15/16+i&-17/8+2i\\
15/16-i&4&4+37i/4\\
-17/8-2i&4-37i/4&67/2
\end{pmatrix},
\]
\[
H_P=\pi\begin{pmatrix}
0&0&0\\0&9/4&9/2+6i\\0&9/2-6i&32
\end{pmatrix},
\]
\[
C_1=\pi\begin{pmatrix}
0&0&9/4\\0&-9/8&-6i\\0&-9/4+3i&-39/2-6i
\end{pmatrix},
\qquad
C_2=\pi\begin{pmatrix}
0&0&0\\0&-9/8&-9/4-3i\\9/4&6i&-39/2+6i
\end{pmatrix}.
\]
Here
\[
(H_B)_{ij}=\int R^2\overline{c_i}c_jE_0^2dt_1dt_2,
\quad
(H_P)_{ij}=\int P^2\overline{c_i'}c_j'E_0^2dt_1dt_2,
\]
\[
(C_1)_{ij}=\int PR\overline{c_i}c_j'E_0^2dt_1dt_2,
\quad
(C_2)_{ij}=\int PR\overline{c_i'}c_jE_0^2dt_1dt_2.
\]
Both cross matrices are nonzero, and \(C_2=C_1^*\). Fibre integration
gives \(\int\Psi\Psi'\,dy=m_2'/2\), so a second calculation of
each cross matrix is
\[
(C_1)_{ij}=-\frac12\int(\overline{c_i}c_j')'m_2\,du,
\qquad
(C_2)_{ij}=-\frac12\int(\overline{c_i'}c_j)'m_2\,du.
\]
The original moment arrays reproduce the same two displayed matrices.
Thus the direct derivative Gram and both CM.5 cross terms agree separately.

## Real tilt with the full original masses

For every real \(\theta\), define the actual integrals
\[
M(\theta)=\int_{\mathbb R}e^{\theta t}a(t)^2dt,\qquad
N(\theta)=\int_{\mathbb R}e^{\theta t}a'(t)^2dt.
\]
Put \(Z(\theta)=\sqrt\pi e^{\theta^2/4}\). Completing the Gaussian
square, or differentiating its integral, gives
\[
M(\theta)=Z(\theta)\frac{\theta^2+4\theta+6}{4},
\qquad
N(\theta)=Z(\theta)
\frac{\theta^4+4\theta^3+8\theta^2+8\theta+20}{16}.
\]
For completeness, the moments used in this evaluation are obtained from
\(g_0=1,g_1=\theta/2\) and
\(g_{n+1}=\theta g_n/2+ng_{n-1}/2\), with the exact identity
\(\int t^ne^{-t^2+\theta t}dt=Z(\theta)g_n(\theta)\).
It follows by integrating the derivative of
\(t^ne^{-t^2+\theta t}\). The factor \(Z\) is restored in every
integral and is never assigned the value one.

The exact mixed integral is
\[
J(\theta)=\int e^{\theta t}aa'\,dt=-\frac\theta2M(\theta).
\]
Expanding the directly differentiated product \(R E_0\) before
integrating gives
\[
\int e^{\theta u}|\Psi'|^2dt_1dt_2
=\frac12NM+\frac12J^2
=\frac12NM+\frac{\theta^2}{8}M^2,
\]
\[
\int e^{\theta u}\Psi\Psi'\,dt_1dt_2=MJ=-\frac\theta2M^2.
\]
The weighted multiplier has the exact typed inverse
\[
L^2(e^{\theta t}dt)\longrightarrow L^2(dt),\quad
f\longmapsto e^{\theta t/2}f,
\qquad q\longmapsto e^{-\theta t/2}q.
\]
Its norm equality follows by squaring the displayed multiplier under the
integral. Direct differentiation, including the two mixed terms, yields
\[
\|(e^{\theta t/2}a)'\|^2
=N+\theta J+\frac{\theta^2}4M
=N-\frac{\theta^2}4M
=Z(\theta)\frac{\theta^2+4\theta+10}{8}>0.
\]
The last positivity follows from
\(\theta^2+4\theta+10=(\theta+2)^2+6\). In the product,
\(\Psi_\theta=e^{\theta u/2}\Psi\) exactly, so
\[
\|\partial_u\Psi_\theta\|^2
=\frac12NM+\frac{\theta^2}{8}M^2
-\frac{\theta^2}{2}M^2+\frac{\theta^2}{4}M^2
=\frac12M\left(N-\frac{\theta^2}{4}M\right).
\]
The negative adjustment is the contribution of the actual derivative
cross term. It is present in this non-even fixture.

At the concrete tilt \(\theta=1\), the complete values are
\[
M=\frac{11}{4}\sqrt\pi e^{1/4},\quad
N=\frac{41}{16}\sqrt\pi e^{1/4},\quad
N-\frac14M=\frac{15}{8}\sqrt\pi e^{1/4},
\]
\[
M^2=\frac{121}{16}\pi e^{1/2},\quad
\int e^u|\Psi'|^2=\frac{143}{32}\pi e^{1/2},\quad
\|\Psi_1'\|^2=\frac{165}{64}\pi e^{1/2}.
\]

## Direct fibre verification of the full information identity

The original change of variables is
\[
t_1=u/2+y,\quad t_2=u/2-y,\qquad
\det\frac{\partial(t_1,t_2)}{\partial(u,y)}=-1.
\]
Thus its Lebesgue Jacobian is exactly one. Retain
\[
b=1+u/2,\quad Q=b^2-y^2,\quad
\Psi=Qe^{-u^2/4-y^2},\quad
\Psi'=(b-uQ/2)e^{-u^2/4-y^2}.
\]
Set \(C=\sqrt{\pi/2}\) and
\[
F=b^4-b^2/2+3/16=(b^2-1/4)^2+1/8>0.
\]
Gaussian integration in \(y\), retaining its moments
\(\int y^2e^{-2y^2}dy=C/4\) and
\(\int y^4e^{-2y^2}dy=3C/16\), gives
\[
m_2=C e^{-u^2/2}F,
\qquad
\|\Psi'\|_{L^2(dy)}^2=C e^{-u^2/2}G,
\]
\[
G=b^2-ub(b^2-1/4)+\frac{u^2}{4}F,
\quad
\langle\Psi,\Psi'\rangle
=\frac{C e^{-u^2/2}}2(F'-uF)=\frac12m_2'.
\]
The actual line projection in \(L^2(dy)\) is
\(\Pi_0f=\Psi\langle\Psi,f\rangle/m_2\). Therefore the full
relative normal vector \(n=(I-\Pi_0)\Psi'\) satisfies
\[
\|n(u)\|^2=C e^{-u^2/2}
\left(G-\frac{(F'-uF)^2}{4F}\right)
=C e^{-u^2/2}\frac{b^2}{8F}.
\]
For the last equality, remove the component \(-u\Psi/2\) before
projecting. The remaining derivative is \(b e^{-u^2/4-y^2}\), whose
squared residual is
\(C e^{-u^2/2}b^2[1-(b^2-1/4)^2/F]\);
the difference \(F-(b^2-1/4)^2=1/8\) gives the formula. This is an
exact orthogonal decomposition of the original derivative. In particular,
\(\|n(0)\|^2=2\sqrt{\pi/2}/11\), and the normal energy is positive
for every real \(u\ne-2\). Its weighted integral is strictly positive
for every real tilt.

The complete left side of CM.12 can now be checked before integration:
\[
e^{\theta u}\frac{(m_2'+\theta m_2)^2}{m_2}
+4e^{\theta u}\|n(u)\|^2
\]
\[
=C e^{-u^2/2+\theta u}
\left(\frac{[F'+(\theta-u)F]^2}{F}+\frac{b^2}{2F}\right)
\]
\[
=4C e^{-u^2/2+\theta u}
\left(G+\frac\theta2(F'-uF)+\frac{\theta^2}{4}F\right).
\]
The first equality substitutes the full density and full normal residual;
the second uses the proved residual identity. The final bracket, multiplied
by \(C\), is also obtained independently by integrating
\((b-uQ/2+\theta Q/2)^2e^{-2y^2}\) in the fibre. Consequently the
complete displayed pointwise expression integrates to four times the
directly differentiated tilted product energy proved above.
Both original terms are integrable: \(F\ge1/8\), so they are bounded
by a polynomial times \(e^{-u^2/2+\theta u}\). Consequently
\[
\int e^{\theta u}\frac{(m_2'+\theta m_2)^2}{m_2}\,du
+4\int e^{\theta u}\|n(u)\|^2du
=2M(\theta)\left(N(\theta)-\frac{\theta^2}{4}M(\theta)\right).
\]
At \(\theta=1\), this full value is
\(165\pi e^{1/2}/16\). The Fisher term and the positive normal term
are both retained; no vanishing normal residual is used to obtain the value.

## Validation and provenance

The script `cyclic_metric_connection_tilt_fixture_20260912.py` has SHA256
`af51d618d65f031134ac90ab645e681f989601ac4d2961c7702139b93622226d`.
Normal and optimized Python each passed 21 compact exact checks. The checks
compare direct product differentiation with the moment formulas, retain both
complex derivative cross matrices, and compare the direct original fibre
integral with the complete tilted information identity. A separate agent
independently reproduced the one-factor tilt functions, the product energies,
the moment table, and both complete Gram matrices before reading this report.
The parent independently reproduced the same tilt functions and values.
The independent review found no mathematical defect. Its two exposition
requests are incorporated: every original integral and amplitude symbol is
defined explicitly, and the final pointwise information expression is
identified as four times the tilted derivative energy.
The replay script pins the source hash actually audited and has no private
source-path dependency; all fixture calculations are defined in the script.
No CM source, cumulative reader, frozen edition, or publication-stage file
was edited by this task.
