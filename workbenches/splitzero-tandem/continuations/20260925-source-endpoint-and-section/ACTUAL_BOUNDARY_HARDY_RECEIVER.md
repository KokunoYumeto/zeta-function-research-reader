# The actual specialization boundary in Noor's Hardy receiver

25 September 2026. Complete derivation ABH0–ABH8. Working source pending independent review.

## ABH0. Original objects and construction stage

All coefficient operations below follow the programme's complete-history arithmetic reconstruction. The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). No addition, numerical origin, coordinate or metric is assigned to it. Branch histories and their counters are not pooled. The current correction chains, particularly 4, 7–8, 14–15 and 18–23, have been reread.

Retain the original entire strip source \(\mathcal B\), with
\[
q_{A,N}(F)=\sup_{|\Re s|\le A}(1+|\Im s|)^N|F(s)|,\quad A>0,\ N\ge0,
\]
its full nontrivial-zero ideal \(I\), and \(Q=\mathcal B/I\). The actual specialization quotient is \(R=Q/N_O\), where
\[
N_O=\{[F]:F(\rho)=0\text{ at every actual off-line nontrivial zero}\}.
\tag{ABH0.1}
\]
Every higher jet remains upstream in \(Q\) and in the specified kernel of this value quotient. Write \(\rho^\#=1-\bar\rho\), with original multiplicities \(m_{\rho^\#}=m_\rho\), and
\[
H=\ell^2(\mathscr Z,m),\quad (JF)_\rho=F_{\rho^\#},\quad
d_r(\rho)=e^{-i\Im\rho\log r}(r^{\Re\rho}-r^{1-\Re\rho}),\quad r>1.
\]
The actual boundary is \(\beta_r=D_r^*JE:Q\to H\), where \(EF=(F(\rho))_\rho\). Its kernel is \(N_O\), and its image is dense in the full off-line subspace, by the original global isolators. These are the GDE0–2 and ADM source maps, not newly chosen boundary conditions.

Let \(H_-\) denote the closed Hilbert subspace supported at \(\Re\rho<1/2\), and \(\mathscr Z_+=\{\lambda:\Re\lambda>1/2\}\). Reflection is a multiplicity-preserving bijection between their coordinate sets. The line subspace and the other half remain present in \(H\); restriction here specifies the domain of one receiving map.

The entire source multiplier is retained with its original factors:
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
F_0(0)=F_0(1)=\frac18,\quad F_0(-1)=F_0(2)=\frac\pi{24},
\]
\[
F_0(-2a)=\frac{a(2a+1)(-1)^a\pi^a}{2a!}\zeta'(-2a)\quad(a\ge1).
\tag{ABH0.2}
\]
This does not replace original \(\zeta\). In particular the original pairing used below is
\[
\langle h_k,g_s\rangle=(1-k^{1-s})\zeta(s)/s.
\tag{ABH0.3}
\]
No pole, endpoint or Gamma correction is omitted from the comparison.

## ABH1. Original Hardy kernels and covers

Use inner products linear in the first variable. Noor's Hardy kernel for \(1/2<\Re s<1\) is
\[
g_s(z)=\sum_{j\ge0}\overline{\phi_j(s)}z^j,\qquad
\phi_0(s)=-1/s,\quad
\phi_j(s)=\frac{j^{1-s}-(j+1)^{1-s}}s\quad(j\ge1).
\tag{ABH1.1}
\]
Its norm satisfies
\[
\|g_s\|_{H^2}^2
=\sum_{j\ge0}|\phi_j(s)|^2\le\frac1{2\Re s-1}.
\tag{ABH1.2}
\]
The exact argument is the step-function projection of \(x^{\bar s-1}\) on the intervals \((1/(j+1),1/j]\), whose lengths are \(1/[j(j+1)]\). Integrating on each interval gives the weighted sequence
\(j(j+1)(j^{-\bar s}-(j+1)^{-\bar s})/\bar s\).
Noor's isometry \(\Phi=T^{-1}\Psi\), \(Tf=((1-z)f)'/(1-z)\), sends it to (ABH1.1), as direct coefficient differentiation verifies. Orthogonal projection decreases the squared \(L^2(0,1)\) norm, which is exactly \(1/(2\Re s-1)\). This proves (ABH1.2) with its original norm and constant.

The raw cover and its adjoint are
\[
W_nf(z)=(1+z+\cdots+z^{n-1})f(z^n),\qquad
(W_n^*f)_j=\sum_{a=0}^{n-1}f_{nj+a}.
\tag{ABH1.3}
\]
They obey \(W_n^*W_n=nI\) and \(W_nW_n^*=nP_n\), where \(P_n\) averages each consecutive coefficient block of length \(n\). Telescoping (ABH1.1), including its first coefficient, gives
\[
W_n^*g_s=n^{1-\bar s}g_s.
\tag{ABH1.4}
\]
The retained constant term of
\(h_k=(1-z)^{-1}\log((1+\cdots+z^{k-1})/k)\)
is essential in (ABH0.3). At each actual right-off-line zero \(\lambda\), that identity proves \(g_\lambda\in\mathcal N^\perp\), where
\(\mathcal N=\operatorname{span}\{h_k:k\ge2\}\).

## ABH2. A full-source uniqueness lemma

This section proves the injectivity needed later; no completeness of the finite Hardy jet family is assumed. It also records the endpoint correction before any quotient.

For \(t>0\) put \(g_t(s)=e^{ts^2}\) and
\[
\psi_j(s)=\phi_j(s)+8F_0(s)/s,\qquad F_{t,j}=g_t\psi_j.
\tag{ABH2.1}
\]
The residue at zero cancels exactly because \(8F_0(0)=1\). Thus \(\psi_j\) is entire, with polynomial strip growth, and \(F_{t,j}\in\mathcal B\). On each fixed strip its source seminorm is bounded by \(C_{A,N,t}(j+1)^{A+3}\): outside a disk divide the explicit numerator by \(s\), and inside use the maximum principle for the entire quotient on a larger disk. The Gaussian controls every vertical polynomial. Hence, for every continuous \(\Lambda\in\mathcal B'\),
\[
\mathcal H_t\Lambda(z)=\sum_{j\ge0}\overline{\Lambda(F_{t,j})}z^j
\tag{ABH2.2}
\]
converges on the unit disk. It is continuous from the strong dual to the compact-open holomorphic space: for each \(a<1\), the classes of
\(\sum_jF_{t,j}\bar z^j\), \(|z|\le a\), form a bounded source set by the stated seminorm bound.

Suppose \(\mathcal H_t\Lambda=0\). Summing its first \(n\) zero coefficients gives
\[
\Lambda\!\left[g_t(s)\frac{n^{1-s}-8nF_0(s)}s\right]=0
\quad(n\ge1).
\tag{ABH2.3}
\]
Define the entire scalar function
\[
L(w)=\Lambda\!\left[g_t(s)
\frac{e^{(1-s)w}-8e^wF_0(s)}s\right].
\tag{ABH2.4}
\]
The numerator again vanishes at \(s=0\). It depends holomorphically on \(w\) in every source seminorm. Indeed on \(|\Re s|\le A\), the nonconstant exponential times the Gaussian is bounded by
\[
e^{tA^2+(1+A)|\Re w|}
e^{-t(\Im s)^2+(\Im s)\Im w}.
\]
Completing the square bounds every vertical polynomial by a constant times
\((1+|\Im w|)^N e^{(\Im w)^2/(4t)}\).
The removable division on a fixed disk is controlled by a surrounding circle; the fixed \(F_0\) term has the same required source bounds. Continuity of \(\Lambda\) therefore gives
\(|L(w)|\le C\exp(C(1+|w|^2))\).

Equation (ABH2.3) says \(L(\log n)=0\) for every \(n\ge1\). If \(L\) were nonzero, choose a point \(w_0\) with \(L(w_0)\ne0\). Jensen's identity on the disk of radius \(2R\) about \(w_0\) gives
\[
\#\{\text{zeros in }|w-w_0|\le R\}\log2
\le \log\max_{|w-w_0|\le2R}|L(w)|-\log|L(w_0)|=O(R^2).
\]
The distinct points \(\log n\), \(n\le e^{R/2}\), contradict that bound for all sufficiently large \(R\). Thus \(L=0\).

Differentiating the complete numerator gives the exact cancellation
\[
(\partial_w-1)L(w)=-\Lambda(g_te^{(1-s)w}).
\tag{ABH2.5}
\]
Consequently \(\Lambda(g_te^{vs})=0\) for every complex \(v\).

To reach every original \(F\in\mathcal B\), fix real \(u>t\) and set \(h=e^{(u-t)s^2}F\in\mathcal B\). Its original inverse half-Mellin transform \(a=\Theta^{-1}h\) gives
\[
g_t(s)h(s)=\frac12\int_{\mathbb R}a(e^v)g_t(s)e^{sv}\,dv.
\tag{ABH2.6}
\]
The integral converges in every original source seminorm: \(a(e^v)\) decreases faster than every exponential, while
\(q_{A,N}(g_te^{vs})\le C_{A,N,t}e^{A|v|}\) for real \(v\).
Therefore \(\Lambda(e^{us^2}F)=0\) for every \(u>t\).
For fixed \(F\), this scalar function of \(u\) is holomorphic on \(\Re u>0\), by uniform Gaussian domination in every source seminorm on compact subsets. The identity theorem extends its vanishing to that half-plane. Finally
\[
q_{A,N}((e^{us^2}-1)F)
\le u e^{A^2}(A^2+1)q_{A,N+2}(F)\quad(0<u\le1)
\]
by the integral remainder of the exponential. Letting \(u\downarrow0\) gives \(\Lambda(F)=0\).

We have proved \(\ker\mathcal H_t=0\) already on \(\mathcal B'_\beta\), and hence on \(Q'_\beta\) and \(R'_\beta\) through their transpose inclusions. No vanishing on \(I\) was used in this uniqueness proof. NHD7–9 supplies the same corrected tests and cover identity; the independently developed full-dual continuation supplies a separate check of this lemma.

## ABH3. The actual boundary gives a trace-class Hardy map

For \(x\in H_-\) define
\[
\lambda_x([F])=\langle\beta_r[F],x\rangle_H.
\tag{ABH3.1}
\]
This is a continuous linear functional of \([F]\), conjugate-linear in \(x\), and annihilates \(N_O\), so it descends to \(R\). The map \(\bar H_-\to R'_\beta\) is continuous: the image under \(\beta_r\) of every source-bounded set is Hilbert-norm bounded. Its kernel is zero because the image of \(\beta_r\) is dense in the whole off-line Hilbert space. A single \(\lambda_x\) may have a larger kernel. The joint kernel over this restricted \(H_-\) is exactly the classes whose values vanish at all right-off-line zeros; the full \(N_O\) imposes both halves.

Compose it with ABH2:
\[
\boxed{\mathcal L_{r,t}x=\mathcal H_t\lambda_x
=-\sum_{\lambda\in\mathscr Z_+}
m_\lambda d_r(\lambda)\overline{g_t(\lambda)}
x_{\lambda^\#}g_\lambda.}
\tag{ABH3.2}
\]
For finite coordinate vectors this follows by reindexing \(\rho=\lambda^\#\), using \(d_r(\lambda^\#)=-d_r(\lambda)\), and observing that \(F_0/s\) vanishes to the full original order at every nontrivial zero. The two conjugate-linear operations give a linear map in \(x\).

The series converges absolutely in \(H^2\) for every \(x\in H_-\). To prove this, put \(\sigma=\Re\lambda>1/2\). Differentiation gives
\[
0<\Delta_r(\sigma)=r^\sigma-r^{1-\sigma}
\le (r+1)\log r\,(\sigma-\tfrac12).
\]
Together with ABH1.2 this implies
\[
|\Delta_r(\sigma)|^2\|g_\lambda\|^2
\le\frac{(r+1)^2(\log r)^2}{4},
\tag{ABH3.3}
\]
since \(0<\sigma-\tfrac12<\tfrac12\). In particular no lower bound on \(\sigma-\tfrac12\) is required.

Define the finite number
\[
C_{r,t}=\sum_{\lambda\in\mathscr Z_+}
m_\lambda|\Delta_r(\Re\lambda)|^2
e^{2t((\Re\lambda)^2-(\Im\lambda)^2)}\|g_\lambda\|^2.
\tag{ABH3.4}
\]
The original multiplicity-counting bound makes
\[
C_{r,t}\le
\frac{(r+1)^2(\log r)^2}{4}e^{2t}
\sum_{\lambda\in\mathscr Z_+}m_\lambda e^{-2t(\Im\lambda)^2}<\infty.
\]
Cauchy–Schwarz bounds the sum of the norms in (ABH3.2) by
\(\|x\|_H C_{r,t}^{1/2}\).
Thus \(\mathcal L_{r,t}:H_-\to H^2\) is bounded. On the orthonormal input basis \(u_{\lambda^\#}=e_{\lambda^\#}/\sqrt{m_\lambda}\), the sum of squared output norms is exactly \(C_{r,t}\); hence it is Hilbert–Schmidt. In fact the stronger sum converges:
\[
\sum_{\lambda\in\mathscr Z_+}\|\mathcal L_{r,t}u_{\lambda^\#}\|
\le\frac{(r+1)\log r}{2}e^t
\sum_{\lambda\in\mathscr Z_+}\sqrt{m_\lambda}e^{-t(\Im\lambda)^2}<\infty.
\tag{ABH3.6}
\]
Each summand in the basis expansion is the rank-one operator
\(x\mapsto\langle x,u_{\lambda^\#}\rangle\mathcal L_{r,t}u_{\lambda^\#}\),
whose trace norm is exactly the displayed output norm. Their sum therefore converges in trace norm and agrees with (ABH3.2) on every basis vector and, by continuity, on all of \(H_-\). This proves that \(\mathcal L_{r,t}\) is trace class between its two specified Hilbert spaces. It does not assign an ordinary scalar trace to an operator with different domain and codomain. The limit agrees with the analytic receiver in (ABH3.2) by compact-open continuity on the strong dual.

ABH2 and injectivity of \(x\mapsto\lambda_x\) now prove
\[
\ker\mathcal L_{r,t}=0,\qquad
\mathcal L_{r,t}(H_-)\subset\mathcal N^\perp.
\tag{ABH3.5}
\]
The second inclusion follows first from original \(\zeta\)'s exact pairing (ABH0.3), then from the closedness of \(\mathcal N^\perp\). This is a faithful positive Hilbert receiver of the specified actual boundary sector. It is not a positive-adjoint identity on the original \(Q\).

## ABH4. Exact comparison with the GDE energy

Let \(B_{r,t}=D_r^*JG_t\) be the original GDE operator. Define
\[
\mathcal D(C_+)=
\{y\in H_+:\sum_{\lambda\in\mathscr Z_+}
m_\lambda|y_\lambda|\|g_\lambda\|<\infty\},\qquad
C_+y=\sum_\lambda m_\lambda y_\lambda g_\lambda.
\tag{ABH4.1}
\]
This specified domain contains every finite coordinate vector. It is not asserted to be all of \(H_+\). Direct evaluation gives
\[
(B_{r,t}^*x)_\lambda
=-\overline{g_t(\lambda)}d_r(\lambda)x_{\lambda^\#}
\quad(x\in H_-).
\]
The same Cauchy–Schwarz estimate as ABH3 proves \(B_{r,t}^*(H_-)\subset\mathcal D(C_+)\). Consequently the exact factorization is
\[
\boxed{\mathcal L_{r,t}=C_+B_{r,t}^*|_{H_-}.}
\tag{ABH4.2}
\]
The GDE squared norm at this stage is \(\|B_{r,t}^*x\|_H^2=\langle B_{r,t}B_{r,t}^*x,x\rangle\), retaining the reflected Gaussian. The Hardy squared norm is \(\|C_+B_{r,t}^*x\|^2\). They are related by this map with its proved domain, not declared equal.

In full coordinates, put \(K(\lambda,\mu)=\langle g_\lambda,g_\mu\rangle
=\sum_{j\ge0}\overline{\phi_j(\lambda)}\phi_j(\mu)\). Then
\[
\|\mathcal L_{r,t}x\|^2=
\sum_{\lambda,\mu\in\mathscr Z_+}
m_\lambda m_\mu d_r(\lambda)\overline{d_r(\mu)}
\overline{g_t(\lambda)}g_t(\mu)
x_{\lambda^\#}\overline{x_{\mu^\#}}K(\lambda,\mu).
\tag{ABH4.3}
\]
This double series converges absolutely by the absolute vector series in ABH3 and Cauchy–Schwarz for \(K\). It retains all off-diagonal terms; replacing it by the diagonal GDE energy would change the pairing.

## ABH5. The exact raw-cover defect

On \(H_-\) retain \((T_nx)_\rho=n^\rho x_\rho\), for each recovered integer \(n\ge1\). Every \(T_n\) and its inverse is bounded for fixed \(n\). From ABH1.4 and \(\lambda^\#=1-\bar\lambda\), the absolutely convergent expansion gives
\[
\boxed{W_n^*\mathcal L_{r,t}=\mathcal L_{r,t}T_n.}
\tag{ABH5.1}
\]
This is also the NHD full-source identity applied through
\(\beta_r U_n=T_n^*\beta_r\), with the original source companion \(U_nF=n^{1-s}F\).

Put \(K_{r,t}=\mathcal L_{r,t}^*\mathcal L_{r,t}\). It is positive trace class, has kernel zero, and its trace is \(C_{r,t}\). Taking the adjoint and product of ABH5.1, with all maps bounded, yields
\[
\boxed{nK_{r,t}-T_n^*K_{r,t}T_n
=n\mathcal L_{r,t}^*(I-P_n)\mathcal L_{r,t}.}
\tag{ABH5.2}
\]
The right side is a computed positive operator. It need not be discarded to obtain positivity of the receiver. It records precisely the part lost by replacing the unilateral reverse composition \(W_nW_n^*=nP_n\) with \(nI\).

For the original normalized coordinate vector \(u_{\lambda^\#}=e_{\lambda^\#}/\sqrt{m_\lambda}\), ABH5.2 has the exact scalar value
\[
\bigl(n-n^{2(1-\Re\lambda)}\bigr)
m_\lambda|\Delta_r(\Re\lambda)|^2
e^{2t((\Re\lambda)^2-(\Im\lambda)^2)}\|g_\lambda\|^2.
\tag{ABH5.3}
\]
Every factor is positive for an actual right-off-line coordinate and \(n>1\). Existence of such a coordinate is not assumed. The sign differs from GDE7.6 because the input is the reflected boundary coordinate and the receiving norm is (ABH4.3); the exact comparison is ABH4.2.

## ABH6. Every scale of the cover defect recovers the full Hardy norm

Fix a recovered integer \(n\ge2\). Iterating ABH5.2 gives, for every \(J\ge1\),
\[
K_{r,t}=
\sum_{j=0}^{J-1}n^{-j}(T_n^*)^j
\mathcal L_{r,t}^*(I-P_n)\mathcal L_{r,t}T_n^j
+n^{-J}(T_n^*)^JK_{r,t}T_n^J.
\tag{ABH6.1}
\]
This is a finite exact telescoping identity; no cover operator has been rescaled or replaced. The final positive operator tends strongly to zero. Its quadratic form is at most
\[
\|\mathcal L_{r,t}\|^2
\sum_{\rho\in\mathscr Z_-}m_\rho|x_\rho|^2n^{J(2\Re\rho-1)},
\]
which tends to zero by dominated convergence, since every retained coordinate has \(\Re\rho<1/2\) and the factors are at most one. Uniform boundedness and positivity convert convergence of these quadratic forms to strong convergence, using
\(\|R_Jx\|^2\le\|R_J\|\langle R_Jx,x\rangle\).
Thus
\[
\boxed{\|\mathcal L_{r,t}x\|^2
=\sum_{j=0}^\infty n^{-j}
\|(I-P_n)\mathcal L_{r,t}T_n^jx\|^2.}
\tag{ABH6.2}
\]
This is a global all-scale identity. In particular simultaneous vanishing of every displayed observation forces \(x=0\), by ABH3.5.

There is also exact vector reconstruction. The operators
\(n^{-j}W_n^j(I-P_n)(W_n^*)^j\) are orthogonal projections onto mutually orthogonal subspaces: \(W_n^*W_n=nI\) proves their idempotence and \((I-P_n)W_n=0\) proves orthogonality for distinct indices. The finite sum equals
\(I-n^{-J}W_n^J(W_n^*)^J\).
The remainder projects onto sequences constant in blocks of length \(n^J\). Their decreasing intersection is zero, since a square-summable sequence constant on every such block must be constant everywhere and hence zero. To verify strong convergence, these nested orthogonal projections have Cauchy projected vectors by the Pythagorean identity, and their limit lies in their intersection. Therefore
\[
\mathcal L_{r,t}x=
\sum_{j=0}^\infty n^{-j}W_n^j(I-P_n)\mathcal L_{r,t}T_n^jx
\quad\text{in }H^2.
\tag{ABH6.3}
\]
This is the elementary unilateral isometry decomposition, fully proved here for the actual unrescaled cover. The application to the programme boundary uses ABH3–5. No novelty claim is made for the underlying Hilbert-space decomposition.

## ABH7. What the adjoint-domain test now says on the whole boundary sector

Noor's unconditional theorem is
\(\mathcal N^\perp\cap\mathcal D_{\delta_1}=\{0\}\),
where \(\mathcal D_{\delta_1}=\operatorname{ran}(I-S^*)=\operatorname{dom}(I-S)^{-*}\).
Its proof uses the unconditional density of \((I-S)\mathcal N\) and the surjectivity of the inverse of \(I-S\). This is the exact theorem read in the author TeX, not an assertion of RH.

ABH3.5 now gives the full-domain conclusion
\[
\boxed{\{x\in H_-:\mathcal L_{r,t}x\in\mathcal D_{\delta_1}\}=\{0\}.}
\tag{ABH7.1}
\]
Indeed membership puts \(\mathcal L_{r,t}x\) in both spaces of Noor's theorem, hence makes it zero; injectivity makes \(x=0\). The reverse inclusion is immediate. This strengthens the finite-jet domain test for this particular actual-boundary Hilbert receiver.

The positive norm and its all-scale reconstruction have therefore been obtained without silently adding the adjoint regularity that would annihilate it. To advance the original target one must calculate an additional geometric map or relation on the actual source that controls this boundary regularity or the complete cover defect. ABH5–6 calculate the attempted use of the cover relation itself: the retained projection term recovers the entire received norm, rather than vanishing by cyclicity.

The complementary original Weil pairing, the first specialization boundary and the full derived extension are retained. A positive norm on the injective Hardy image is not an assertion that those original pairings agree with it. The exact map from the GDE boundary is ABH4.2, and its non-diagonal Gram matrix is ABH4.3.

## ABH8. Reading and proof provenance

Programme sources fully read for this continuation: GDE0–13; NHD0–10; NHR0–6 (the subsequent NHR7 finite map is also explicitly restated and checked in NHD); CTS0–6; FST0–7; QTI0–7; ACC0–8 as a working draft, without importing its unreviewed claims into this proof. Earlier GAP/ADM complete reading remains in its own source ledger. The full-dual uniqueness argument in ABH2 was developed jointly with an independent derivation and is proved here in full.

Human source: S. Waleed Noor, [A Hardy space analysis of the Báez-Duarte criterion for the RH, arXiv:1809.09577v4](https://arxiv.org/abs/1809.09577v4), author TeX SHA256 bc3075483547782dce36bf55a6349899a26766fcfc8ae9f265079ec74601f2d3. Newly read original TeX coverage: lines 114–159 and 263–387, including the exact cover, unconditional density proof and adjoint-domain proof. The isometry's external book reference is not newly read; NHR's coefficient verification and the displayed norm argument supply the receiving comparison. Source routing uses canonical unit PUBUNIT-803463A3EF787AE3E69C519B; routing is recorded separately from reading.

The earlier geometric origins remain Connes–Consani, [arXiv:0903.2024v3 §5](https://arxiv.org/abs/0903.2024v3), and the target remains Deligne, [Weil II §3.6](https://numdam.org/item/PMIHES_1980__52__137_0/). No new whole-paper reading of either is claimed. Nothing in ABH asserts original weight-separated lifting vanishing or an RH resolution.
