# Independent verification of finite-dilation homotopies and tensor signs

Status: completed algebraic sign/support review, 2026-09-13. This file is the reviewer's durable work record and proof file. It changes no shared master and performs no remote action. The session's verbatim user input is retained by the owning task in `work/tau_f1_transcript_audit_20260913/USER_INPUTS.md`; this review uses that existing provenance record.

## Assignment, verbatim

> Independently verify finite-dilation cochain homotopy/support-transport and tensor signs, read primary source as needed. Main formulas c_t=integral_0^t U_(e^(t-r))phi_* ell e^(rA)dr, delta=Theta c. C=[V⊕V --Theta(v-Fw)--> B] deg0,1. E[-1] deg1, R section. h+=(c,0), h-=(0,-Fc); differences are degree0 cycles. Tensor top homotopy candidate H^(k)=sum_j (-1)^(j-1) f^⊗(j-1)⊗h⊗g^⊗(k-j) where f=U_a R, g=R a^A degree1 outputs; dH=f^⊗k-g^⊗k. General tensor morphism sign governed input degrees. Establish whether transport-natural homotopy exists across + and - faces (expect obstruction by cycle, exact scope), and explicit two-leg quasi-isom roof retaining H0. Do not duplicate topology or dx pairing. Write review only under work/tau_f1_transcript_audit_20260913/theta_scaling_cocycle/review_homotopy_signs.md and send findings. No browser/Lean/master/publication.

## Sources read and conventions

The complete primary source `output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md`, SHA256 `d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3`, was read. In particular, its equations (15), (19), (21), (22), (32)--(35), and (46)--(48) fix the support transports, cohomological degrees, Fourier sign, unequal two-leg action, and tensor differential used below. The complete retained `output/tau_f1_transcript_audit_2026-09-13/sources/arithmetic_input.tex`, SHA256 `a50b0fb587b644c4ea94dba45b2b423d038f2bfbe7fef188543939ba850e58d2`, was also read; its (A1)--(A13) give the actual packet section and source extension used below. These are source pins for this review, not a claim to have independently audited unrelated later analytic sections.

Use the original spaces

\[
V=\{\phi\in\mathcal S(\mathbb R):\phi(-x)=\phi(x),\ \phi(0)=0,\ \int_{\mathbb R}\phi(x)\,dx=0\},
\]
\[
\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):\sup_{x>0}x^b|D^kF(x)|<\infty\text{ for all }b\in\mathbb Z,\ k\geq0\},\qquad D=-x\partial_x.
\]

The original operators are

\[
\mathcal F\phi(\xi)=\int_{\mathbb R}\phi(x)e^{-2\pi ix\xi}\,dx,
\quad \Theta\phi(x)=2\sum_{n\geq1}\phi(nx),
\quad U_aF(x)=F(x/a).
\]

On even functions \(\mathcal F^2=1\). The source proves that \(\Theta\) is injective and continuous, that \(D\Theta=\Theta D\), and that

\[
\mathcal F D=(1-D)\mathcal F,
\qquad \mathcal F U_a=aU_{1/a}\mathcal F.
\]

Write

\[
S_t=U_{e^t}|_V,\qquad G_t=U_{e^t}|_{\mathscr B},\qquad T_t=e^tU_{e^{-t}}|_V.
\]

Their generators are \(D,D,1-D\), respectively, and

\[
\Theta S_t=G_t\Theta,\qquad \mathcal F T_t=S_t\mathcal F.
\]

Let \(Z\) be the original nonempty finite actual zero packet, retaining each full multiplicity, and put

\[
h(X)=\prod_{\rho\in Z}(X-\rho)^{m_\rho},\quad d=\deg h,\quad E=\mathbb C[X]/(h),\quad A=M_X.
\]

Here \(X\) is the polynomial indeterminate; the real variable \(t\) below is the logarithm of a dilation. The fixed source section is denoted \(R=R_{\rm ref}:E\to\mathscr B\). With the source's polynomial representative \(R_Z(u)\),

\[
\ell(u)=[X^{d-1}]R_Z(u),\qquad
\phi_*=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},
\]
\[
DR-RA=\Theta\phi_*\ell,\qquad J_ZR=1,\qquad J_Z\Theta=0.
\tag{1}
\]

All complexes are cochain complexes. The shift convention is \((C[n])^i=C^{i+n}\), \(d_{C[n]}=(-1)^nd_C\); hence \(E[-1]\) has \(E\) in degree one. Tensor products of homogeneous maps use the Koszul convention

\[
(u\otimes v)(x\otimes y)=(-1)^{|v||x|}u(x)\otimes v(y).
\tag{2}
\]

## 1. The finite-dilation boundary and its cocycle identity

Define the actual source map

\[
c_t=\int_0^tS_{t-r}\phi_*\ell e^{rA}\,dr:E\longrightarrow V,
\tag{3}
\]

with oriented integration when \(t<0\). This is an integral in the original Schwartz space: the dilation orbit of the fixed Schwartz function is smooth, every Schwartz seminorm is bounded on each compact dilation interval, and \(e^{rA}\) acts in the finite-dimensional space \(E\). The integral retains evenness and both zero moments. Detailed continuity and quantitative estimates belong to the separate topology lane; the integral's algebraic identities are established here.

Differentiate \(G_{t-r}Re^{rA}\) in \(r\). Equation (1), with all signs retained, gives

\[
\frac{d}{dr}(G_{t-r}Re^{rA})
=-G_{t-r}(DR-RA)e^{rA}
=-\Theta S_{t-r}\phi_*\ell e^{rA}.
\]

Integration from \(0\) to \(t\) therefore yields

\[
\delta_t:=G_tR-Re^{tA}=\Theta c_t.
\tag{4}
\]

For all real \(s,t\), expansion of the left side proves

\[
\delta_{s+t}=G_s\delta_t+\delta_s e^{tA}.
\]

Substitute (4), use \(G_s\Theta=\Theta S_s\), and use injectivity of \(\Theta\). This proves the exact cocycle law

\[
c_{s+t}=S_sc_t+c_s e^{tA},\qquad c_0=0,
\quad c_{-t}=-S_{-t}c_t e^{-tA}.
\tag{5}
\]

No nilpotent part of \(A\) was discarded: every occurrence of \(e^{tA}\) is its full matrix exponential.

The operator \(c_t\) is nonzero for every \(t\ne0\). To prove this, first prove that a nontrivial dilation \(G_t\) has no nonzero finite-dimensional invariant subspace in \(\mathscr B\). If \(W\) were such a subspace, \(G_t|_W\) would be injective and hence invertible. Over \(\mathbb C\) it would have an eigenvector \(F\ne0\) of eigenvalue \(\lambda\ne0\). By replacing \(t\) with \(-t\) on \(W\), take \(a=e^t>1\). Choose \(x_0>0\) with \(F(x_0)\ne0\). Then

\[
F(a^nx_0)=\lambda^{-n}F(x_0)\quad(n\geq0).
\]

Choose an integer \(b\) with \(a^b>|\lambda|\). The values

\[
(a^nx_0)^b|F(a^nx_0)|
=x_0^b|F(x_0)|(a^b/|\lambda|)^n
\]

are unbounded, contradicting the defining seminorm of \(\mathscr B\). Now \(c_t=0\) would imply \(G_tR=Re^{tA}\). Since \(J_ZR=1\), the space \(R(E)\) is nonzero and finite-dimensional, and this identity would make it invariant. This is impossible. The proved assertion is \(c_t\ne0\) as a linear map; no claim that it is injective is needed or made.

## 2. Both singleton homotopies and the exact support obstruction

The three nonempty support complexes, in degrees zero and one, are

\[
C_+=[V\xrightarrow{\Theta}\mathscr B],\qquad
C_-=[V\xrightarrow{-\Theta\mathcal F}\mathscr B],
\]
\[
C_{+-}=[V\oplus V\xrightarrow{d}\mathscr B],\qquad
d(v,w)=\Theta(v-\mathcal Fw).
\tag{6}
\]

Their transports \(i_+:C_+\to C_{+-}\) and \(i_-:C_-\to C_{+-}\) are \(v\mapsto(v,0)\), \(w\mapsto(0,w)\) in degree zero and identity in degree one. The actions are \(S_t,T_t,S_t\oplus T_t\) in degree zero and \(G_t\) in degree one.

For each complex, \(f_t,g_t:E[-1]\to C_A\) are the degree-zero cochain maps whose degree-one components are \(G_tR\), \(Re^{tA}\). A homotopy from \(g_t\) to \(f_t\) has degree \(-1\), and its equation is \(f_t-g_t=dH_t+H_td_{E[-1]}=dH_t\). By (4), the unique singleton choices are

\[
H_{+,t}=c_t:E\to V,\qquad H_{-,t}=-\mathcal Fc_t:E\to V.
\tag{7}
\]

The second sign is forced:

\[
(-\Theta\mathcal F)(-\mathcal Fc_t)=\Theta c_t=\delta_t.
\]

Transport to the joint support gives

\[
h_{+,t}=(c_t,0),\qquad h_{-,t}=(0,-\mathcal Fc_t),
\tag{8}
\]

and hence

\[
h_{+,t}-h_{-,t}=(c_t,\mathcal Fc_t).
\tag{9}
\]

The entire space of joint degree-zero cycles is

\[
\ker d=\{(\mathcal Fw,w):w\in V\},
\tag{10}
\]

because \(\Theta\) is injective. Equation (9) is exactly the cycle (10) with \(w=\mathcal Fc_t\). For \(t\ne0\), it is nonzero as a map from \(E\). It cannot be a degree-zero boundary because \(C_{+-}^{-1}=0\). Equivalently, the difference is a nonzero class in

\[
H^{-1}\operatorname{Hom}(E[-1],C_{+-})
\cong\operatorname{Hom}(E,H^0(C_{+-})).
\tag{11}
\]

There is no degree \(-2\) homotopy between these homotopies: \(\operatorname{Hom}^{-2}(E[-1],C_{+-})=0\).

Every joint solution of \(dH_t=\delta_t\) has the form

\[
H_t=(c_t+\mathcal Fb_t,b_t),\qquad b_t:E\to V.
\tag{12}
\]

Indeed its two components satisfy \(v-\mathcal Fw=c_t\), again by injectivity. Naturality with the plus inclusion forces \(b_t=0\), whereas naturality with the minus inclusion forces \(b_t=-\mathcal Fc_t\). Thus, for each \(t\ne0\), **there is no homotopy for these fixed maps on the constant packet support diagram that commutes strictly with both singleton-to-joint transports**. At \(t=0\), both are zero and the obstruction vanishes.

This statement concerns the fixed original quotient packet maps and support arrows, with their actual source complexes. It does not rule out the equivariant roof in the next section, does not remove any cohomology, and is not a purity obstruction. In the split lift, each amplitude in (8)--(12) has its original support mask; an amplitude zero is that mask's supported zero, never \(\tau\).

## 3. A complete equivariant roof retaining the joint degree-zero cohomology

Let

\[
\mathscr B_Z=\Theta V+R(E)\subseteq\mathscr B.
\]

Its source sequence is exact:

\[
0\longrightarrow V\xrightarrow{\Theta}\mathscr B_Z\xrightarrow{J_Z}E\longrightarrow0.
\tag{13}
\]

For completeness, if \(b=\Theta v+Ru\), then \(J_Zb=u\), so the kernel is \(\Theta V\), the quotient is \(E\), and the sum is a direct sum of complex vector spaces. Formula (4) proves that \(\mathscr B_Z\) is stable under every \(G_t\); formula (1) proves stability under \(D\). The restriction of \(J_Z\) intertwines these operators with \(e^{tA}\) and \(A\), respectively.

Put

\[
C_{Z,+-}=[V\oplus V\xrightarrow{\Theta(v-\mathcal Fw)}\mathscr B_Z].
\]

The explicit chain isomorphism

\[
\Psi:C_{Z,+-}\xrightarrow{\sim}C_{Z,+}\oplus V_T[0],
\quad\Psi^0(v,w)=(v-\mathcal Fw,w),\quad\Psi^1=1,
\tag{14}
\]

has inverse \((u,w)\mapsto(u+\mathcal Fw,w)\), where \(C_{Z,+}=[V\xrightarrow{\Theta}\mathscr B_Z]\). It is a chain map since the first component has differential \(\Theta\). It is equivariant since

\[
S_tv-\mathcal FT_tw=S_t(v-\mathcal Fw).
\]

Here \(V_T\) means the original second-leg representation with action \(T_t=e^tU_{e^{-t}}\), not a replacement by \(S_t\).

Define

\[
p:C_{Z,+-}\longrightarrow V_T[0]\oplus E[-1],\qquad
p^0(v,w)=w,\quad p^1(b)=J_Zb.
\tag{15}
\]

It is a chain map because \(J_Z\Theta=0\). It is equivariant by the displayed actions. On degree-zero cohomology it is \((\mathcal Fw,w)\mapsto w\), an isomorphism, and on degree-one cohomology it is the isomorphism supplied by (13). Hence the requested two-leg roof is

\[
V_T[0]\oplus E[-1]\ \xleftarrow[\simeq]{\ p\ }\ C_{Z,+-}\
\xrightarrow{\ \mathrm{incl}\ } C_{+-}.
\tag{16}
\]

Every arrow is an actual equivariant cochain map, and the left arrow is a proved quasi-isomorphism. The right arrow induces the identity on the full \(V_T\) in degree zero and the source packet inclusion \(\sigma=qR:E\to Q\) in degree one. No section \(E\to\mathscr B\) commuting with scaling was assumed.

### The support transports in this roof carry a nonzero extension component

This calculation fixes the additional sign that is easily missed when replacing the roof by its cohomology objects. Work in the category of \(\mathbb C[X]\)-modules, with \(X=D\) on \(\mathscr B_Z\), \(X=A\) on \(E\), and \(X=1-D\) on \(V_T\). Set \(r(X)=R_Z(1)\). The actual section satisfies

\[
h(D)R(1)=\Theta\bigl(r(D)\phi_*\bigr).
\tag{17}
\]

The source proves that the class of \(r(D)\phi_*\) in \(V/h(D)V\) is the unit
\(\varepsilon=j_h(h/g)\ne0\), under the exact source jet isomorphism. Thus this class is nonzero.

For the minus complex the extension injection is \(i_-=-\Theta\mathcal F\). The class of the extension

\[
0\to V_T\xrightarrow{-\Theta\mathcal F}\mathscr B_Z\xrightarrow{J_Z}E\to0
\]

is represented, in the projective-resolution convention \(h(D)R(1)=i_-(w)\), by

\[
w=-\mathcal F r(D)\phi_*
\quad\text{in }V/h(1-D)V.
\tag{18}
\]

The component of the transported minus arrow in the **\(V_T[0]\) summand of (16)** is the negative of that connecting class. This is a shift sign, not a new Fourier sign. To verify it without an unstated triangle convention, use the free resolution of \(E\), in degrees \(-1,0\), with differential \(h\). After shifting by \(-1\), its degrees are \(0,1\) and its differential is \(-h\). The degree-one lift to \(C_{Z,-}\) sends \(1\) to \(R(1)\), extended \(\mathbb C[X]\)-linearly. Its degree-zero lift must send \(1\) to \(-w\), because

\[
i_-(-w)=-h(D)R(1).
\]

The projection from \(C_{Z,-}\) to \(V_T[0]\) is identity in degree zero. Consequently the induced derived map

\[
E[-1]\longrightarrow V_T[0]
\]

is the class

\[
-[w]=[\mathcal F r(D)\phi_*]\ \in\
\operatorname{Ext}^1_{\mathbb C[X]}(E,V_T)
\cong V/h(1-D)V.
\tag{19}
\]

The last isomorphism follows directly by applying \(\operatorname{Hom}_{\mathbb C[X]}(-,V_T)\) to the same two-term free resolution: its cokernel is the stated quotient. Fourier is an isomorphism from \(V/h(D)V\) to \(V/h(1-D)V\), since \(\mathcal F D=(1-D)\mathcal F\). Hence (19) is nonzero by (17). Its \(E[-1]\) component is identity. The plus support arrow has zero \(V_T[0]\) component and identity \(E[-1]\) component.

Thus the two transported singleton roofs do not both become the naive inclusion of the \(E[-1]\) summand in the equivariant derived category. Their exact difference includes (19), the original arithmetic extension class. In the ordinary derived category of complex vector spaces this Ext group vanishes; forgetting the action explains that weaker collapse, but does not make it an equivariant collapse. At cochain level the original \(C_{Z,A}\), with their coordinate transports, form a strict equivariant support diagram throughout.

## 4. Tensor homotopy: evaluated formula versus tensor of graded maps

Fix \(t\), one of the joint homotopies \(h=h_{+,t}\) or \(h=h_{-,t}\), and write \(f=f_t\), \(g=g_t\), \(X=E[-1]\). The cochain maps \(f,g:X\to C_{+-}\) have **map degree zero**, even though their nonzero outputs are in cochain degree one. The homotopy \(h\) has map degree \(-1\).

With the Koszul tensor convention (2), the degree \(-1\) tensor homotopy is

\[
\mathcal H^{(k)}=\sum_{j=1}^k
f^{\otimes(j-1)}\otimes h\otimes g^{\otimes(k-j)}.
\tag{20}
\]

There is **no additional coefficient \((-1)^{j-1}\) in (20)**. That sign is already included by applying the tensor of graded maps to inputs of degree one. Written as an explicit formula on the actual elements \(u_i\in E=X^1\), it is

\[
\mathcal H^{(k)}(u_1\otimes\cdots\otimes u_k)
=\sum_{j=1}^k(-1)^{j-1}
f(u_1)\otimes\cdots\otimes f(u_{j-1})\otimes h(u_j)
\otimes g(u_{j+1})\otimes\cdots\otimes g(u_k).
\tag{21}
\]

Indeed the only odd map in the tensor is \(h\), and its degree \(-1\) crosses the \(j-1\) preceding inputs, all of degree one. For general homogeneous inputs the sign is \((-1)^{\sum_{i<j}|u_i|}\), not a fixed count independent of their degrees.

On each summand of (21), all factors except \(h(u_j)\) are closed degree-one elements, and \(h(u_j)\) has degree zero. The tensor differential contributes \((-1)^{j-1}\) when it reaches the \(j\)-th factor. This cancels the displayed coefficient and gives

\[
d\mathcal H^{(k)}(u_1\otimes\cdots\otimes u_k)
=\sum_{j=1}^k f(u_1)\otimes\cdots\otimes f(u_{j-1})
\otimes(f-g)(u_j)\otimes g(u_{j+1})\otimes\cdots\otimes g(u_k).
\]

Adjacent terms cancel after expanding \(f-g\): the negative term at position \(j+1\) equals the positive term at position \(j\), except for the two endpoints. Therefore

\[
d\mathcal H^{(k)}=f^{\otimes k}-g^{\otimes k}.
\tag{22}
\]

The domain differential is zero. In the general Hom-complex notation the identity is \(d_C\mathcal H^{(k)}+\mathcal H^{(k)}d_{X^{\otimes k}}=f^{\otimes k}-g^{\otimes k}\), since the homotopy has degree \(-1\).

For \(k=2\), the sign is completely visible:

\[
\mathcal H^{(2)}(u\otimes v)=h(u)\otimes g(v)-f(u)\otimes h(v),
\]
\[
d\mathcal H^{(2)}=(f-g)\otimes g+f\otimes(f-g)
=f\otimes f-g\otimes g.
\]

Adding an extra alternating prefactor to the graded-map expression (20) would instead double-count the Koszul sign and would fail this calculation.

### The tensor support obstruction retains its lower-degree classes

Subtract the versions of (21) obtained from \(h_{+,t}\) and \(h_{-,t}\). Put \(z_t=(c_t,\mathcal Fc_t):E\to C_{+-}^0\). Their difference is

\[
\Delta\mathcal H_t^{(k)}(u_1\otimes\cdots\otimes u_k)
=\sum_{j=1}^k(-1)^{j-1}
f(u_1)\otimes\cdots\otimes f(u_{j-1})\otimes z_t(u_j)
\otimes g(u_{j+1})\otimes\cdots\otimes g(u_k).
\tag{23}
\]

It is closed, as \(dz_t=0\). Its cohomology class is nonzero for every \(t\ne0\) and every \(k\geq1\). Here is a direct verification that does not assume away a possible lower-degree boundary. Define chain maps

\[
\pi_0:C_{+-}\to V[0],\quad\pi_0^0(v,w)=w,\quad\pi_0^1=0,
\]
\[
\pi_1:C_{+-}\to Q[-1],\quad\pi_1^0=0,\quad\pi_1^1=q.
\]

For each \(j\), apply \(\pi_0\) in factor \(j\) and \(\pi_1\) in all other factors to (23). Every summand except the \(j\)-th vanishes, because its degree-zero factor is sent through \(\pi_1\). The remaining map is

\[
(-1)^{j-1}(qf)^{\otimes(j-1)}\otimes(\mathcal Fc_t)
\otimes(qg)^{\otimes(k-j)}.
\tag{24}
\]

Both \(qf\) and \(qg\) are the injective map \(\sigma e^{tA}:E\to Q\): equation (4) identifies them, and \(\overline J_Z\sigma=1\) proves injectivity. The map \(\mathcal Fc_t\) is nonzero. A tensor product of these maps over \(\mathbb C\) is nonzero: choose an input on which \(\mathcal Fc_t\) is nonzero, nonzero inputs in the other factors, and linear functionals nonzero on each resulting nonzero vector; their tensor functional evaluates the tensor to a nonzero product. Thus (24) is nonzero. Its target has zero differential, so (23) cannot be a boundary. This proves that the tensor difference cannot be removed by a higher homotopy either, including when the tensor complex has nonzero components below degree \(k-1\).

The retained classes lie in the actual summands with one \(H^0(C_{+-})=V_T\) and \(k-1\) copies of \(H^1(C_{+-})=Q\). The top tensor quotient remains the original \(Q^{\otimes k}\); this calculation exhibits the lower-degree classes that a replacement by top cohomology alone would lose.

## Verification record and integration instructions

1. Read the complete primary Tau Base note and complete retained arithmetic input; preserved the source's two-leg action, Fourier transform, support arrows, polynomial unit, nilpotent matrix exponential, and cohomological shifts.
2. Verified (3)--(5) by differentiation, endpoint integration, and theta injectivity. Proved nonvanishing of \(c_t\) as a map for every nonzero dilation parameter.
3. Computed all joint homotopies, their support mismatch, and the nonzero class that prevents strict support naturality for the fixed packet maps.
4. Constructed the actual joint roof (16), including its inverse chain-coordinate transformation and its full degree-zero action. Computed the nonzero minus-transport extension component with the shifted-resolution sign (19).
5. Checked tensor signs in both precise notations, including the explicit two-factor calculation and the nontriviality of the tensor support mismatch.

For integration, use (21) when writing an evaluated pure-tensor formula, or (20) when writing a tensor of graded morphisms. Do not use both sign conventions at once. Preserve the \(V_T[0]\) summand and the transport class (19) when passing to the roof. This review leaves quantitative Schwartz estimates, analytic boundary pairings, the full transcript audit, PDF assembly, and shared-master integration to their existing owners.
