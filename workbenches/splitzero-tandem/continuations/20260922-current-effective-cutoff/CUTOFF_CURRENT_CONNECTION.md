# The original kernel increments, observed arithmetic current, and hidden evolution

22 September 2026. Result SZ-20260922-026. This continuation incorporates both the effective-cutoff manuscript and the subsequent observed-current manuscript. Their complete proofs and all earlier accepted sources accompany this edition. The calculations below connect their two scalar profiles exactly, improve the finite source-window estimates, and carry the stronger original source comparison into the current and evolution. Throughout, a stipulated simple quartet and its admitted original period, branch and arithmetic unit are fixed; these calculations neither construct such a zero nor establish RH.

## 1. Original objects and the completed finite estimate

Retain the entire original polynomial and physical coordinate
\[
q=(k+1)^2,\quad q_0=(k-7)^2,\quad \Delta=16k-48,\quad m=8k-16,
\quad k\ge17,\quad k\equiv1\pmod4,
\]
\[
Q_k(y)=\prod_{a,b=0}^{k}\bigl[y-(2b-k)\gamma+i(2a-k)\delta\bigr],
\quad 0<\delta<1/2,\quad\gamma>2,\quad s=k/2+iy.
\tag{RC1}
\]
Let \(G_N\) be the complete minimum of the original source norm on \(E=\mathbb C[y]/Q_k\), \(\Lambda:E\to B\) the complete observation, and \(I_K\) the unchanged frame of \(K=\ker\Lambda\). Put \(H_{K,N}=I_K^*G_NI_K\). All indices
\[
N_j=q-1+j,\quad t_j=j/q,\quad 0\le j\le q+1,
\qquad \mathcal R f=f_{N_0}+f_{N_1}-f_{N_q}-f_{N_{q+1}}
\tag{RC2}
\]
are retained. In particular, the two members of either endpoint pair are distinct.

The independent full Gamma proof EG23 improves the incoming finite scalar error to \(83+3\log(q+2)\) on \(0\le M\le\lfloor1.1q\rfloor\). Its complete coefficient covariance and simultaneous right inverse are EG28–35. Inserting that bound into the proved full-kernel localization LX27–33 gives the explicit scalar
\[
e_k=\frac{mE_{\rm loc}+c_{\rm loc}(24q+\log\kappa_k)}{mq},
\quad c_{\rm loc}=\min(m,v_0+N_R),\quad\kappa_k=u_k/\ell_k,
\tag{RC3}
\]
where the exact finite circle, band, source constants and guards are LX10, LX17, LX19, LX23–24, LX27–28. Every term is specified there. The contour includes all symbol poles, the source comparison includes both real regions, and the codimension loss is a compression of the actual invariant kernel. It follows that
\[
F_k(t_j):=\frac1{mq}\log\frac{\det H_{K,N_0}}{\det H_{K,N_j}},
\qquad |F_k(t_j)-J(t_j)|\le e_k.
\tag{RC4}
\]
The choice LX34 satisfies all the finite guards eventually and gives \(e_k\to0\). No numerical value of a native period is required or asserted.

The same estimate reaches every fixed complete restriction or attained quotient: the original isometric compression LX30 has at most \(c_{\rm loc}\) upper and \(c_{\rm loc}\) lower exceptions; their total logarithmic deviation is at most \(c_{\rm loc}(24q+\log\kappa_k)\). This proves RC4 and its subquotient versions directly, with their actual ranks, rather than assigning a coefficient from the rank of the full space. Earlier [IR6–10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/INTEGRATED_PROFILE_AND_RECEIVERS.md#L50) therefore receive a specified finite error.

## 2. Exact map between the two retained profiles

Use B. C. Carlson's complete elliptic integral conventions, with modulus as argument. Their original equation sources [DLMF19.5.1–2](https://dlmf.nist.gov/19.5) and [19.8.12a–b](https://dlmf.nist.gov/19.8.E12) were read and retained. Their derivation and exact branch are also given in the preceding [EP1–11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/ELLIPTIC_PROFILE_PROOF.md#L5). Put
\[
F(z)=\frac2\pi K(\sqrt z)=\sum_{n\ge0}\frac{\binom{2n}{n}^2}{16^n}z^n,
\quad t=4zF'(z)/F(z),\quad z=z_t\in(0,1).
\tag{RC5}
\]
The map is strictly increasing and onto: its logarithmic derivative is four times the positive variance of the displayed series distribution; at one every finite initial part of that distribution has vanishing mass. The exact cutoff profile is
\[
J(t)=2\log F(z_t)-\frac t2\log z_t,\quad J(0)=0,
\qquad J'(t)=-\frac12\log z_t.
\tag{RC6}
\]
The original arithmetic-current profile uses
\[
r=\frac{1-\sqrt z}{1+\sqrt z},\quad
\kappa=\frac{2z^{1/4}}{1+\sqrt z},\quad
1+t=\frac{E(\kappa)}{rK(\kappa)},\quad
\psi(t)=t\log\frac{\kappa}{E(\kappa)}+
\log\frac{1+r}{E(\kappa)}.
\tag{RC7}
\]
Here \(r\) and \(z\) are scalar elliptic coordinates only; the physical coordinate and source matrices in RC1–4 are unchanged. The Landen formulas give
\[
E(\kappa)=\frac\pi2(1+t)(1-\sqrt z)F(z),
\quad
\psi(t)=(1+t)L(t)+\frac t4\log z_t,
\]
\[
L(t)=\log\frac4{\pi(1+t)(1-z_t)F(z_t)}.
\tag{RC8}
\]
These equalities follow by direct substitution in both terms of RC7: \(\kappa/E=4z^{1/4}/[\pi(1+t)(1-z)F]\) and \((1+r)/E=4/[\pi(1+t)(1-z)F]\).

The coefficient recurrence in RC5 gives
\[
4z(1-z)t'(z)=4z(t+1)-(1-z)t^2.
\tag{RC9}
\]
For clarity, differentiating RC8 yields
\[
L'(t)=-\frac1{1+t}+\frac{z_t'}{1-z_t}
-\frac{t z_t'}{4z_t},
\quad (1+t)L'(t)+\frac{t z_t'}{4z_t}=0;
\]
the second equality is exactly RC9 after multiplication by \(4z_t/z_t'\). Hence \(\psi'=L+\tfrac14\log z\). Subtracting gives the exact differential and integral maps
\[
\boxed{J'=2\psi-2(1+t)\psi',\qquad
\psi''=-\frac{J''}{2(1+t)},}
\tag{RC10}
\]
\[
\boxed{\psi(t)=(1+t)\left[
a_0-\frac12\int_0^t\frac{J'(s)}{(1+s)^2}\,ds\right],
\qquad a_0=\log(4/\pi).}
\tag{RC11}
\]
Indeed differentiate \(\psi/(1+t)\) and integrate; RC8 gives its value \(a_0\) at zero. Since \(J'(s)=-\tfrac12\log s+O(s)\), the integral converges at zero. Conversely integration of RC10, with \(J(0)=0\), proves
\[
J(t)=4\int_0^t\psi(s)\,ds-2(1+t)\psi(t)+2a_0.
\tag{RC12}
\]
Thus these profiles determine each other together with their specified endpoint value. This supplies an exact connection between the already evaluated kernel-volume profile and the arithmetic-current growth profile.

## 3. Reconstruction from the actual source increments

Let \(b_N\) and \(\rho_N\) denote the two original nonnegative rank-one source and kernel leverages in the determinant update, with precisely the conventions of incoming ME2 and preceding IR14–16. The complete covariance update and the matrix determinant lemma give
\[
A_{i,k}:=\log\frac{\det H_{K,N_i}}{\det H_{K,N_{i+1}}}
=\log\frac{1+\rho_{N_i}}{1+b_{N_i}}\ge0,
\quad F_k(t_j)=\frac1{mq}\sum_{i<j}A_{i,k}.
\tag{RC13}
\]
For an explicit verification of the determinant step, a positive covariance \(C\) updated to \(C+vv^*\) has inverse \(C^{-1}-C^{-1}vv^*C^{-1}/(1+v^*C^{-1}v)\). Restrict this inverse to the unchanged kernel frame and apply \(\det(H-ww^*/d)=\det H(1-w^*H^{-1}w/d)\). The resulting ratio is exactly the source quotient in RC13, with the complete original minimizing sections. This is the update used by the cited receiver, not a replacement set of columns. The nonnegative sign also follows directly from nesting of the full source fibres.

Define the finite observable
\[
\widehat\psi_k(t_j)=(1+t_j)\left[a_0-
\frac1{2mq}\sum_{i=0}^{j-1}\frac{A_{i,k}}{(1+t_{i+1})^2}\right].
\tag{RC14}
\]
It uses every actual increment up to the indicated cutoff. For every \(0\le j\le q+1\),
\[
\boxed{|\widehat\psi_k(t_j)-\psi(t_j)|
\le\frac{1+t_j}{2}\left[e_k+\frac{2J(t_j)}q\right].}
\tag{RC15}
\]
To prove it put \(w_i=(1+t_i)^{-2}\), \(D_i=F_k(t_i)-J(t_i)\). Discrete integration by parts gives
\[
\sum_{i<j}w_{i+1}(D_{i+1}-D_i)
=w_jD_j+\sum_{i=1}^{j-1}(w_i-w_{i+1})D_i,
\]
since \(D_0=0\). Its absolute value is at most \(e_kw_1\le e_k\). On each mesh interval the variation of \((1+t)^{-2}\) is at most \(2/q\). Because \(dJ\) is positive, replacing its weight by the right-endpoint value costs at most \(2J(t_j)/q\). Apply RC11 to prove RC15. No bound for an individual microscopic leverage is inferred from a cumulative error.

## 4. Stronger shrinking-window and curvature bounds

Fix \(0<a<1\). On \([a,1]\) let
\[
v_a=\frac{9a}{80(1+a)},\quad
M_3=1280\left(\frac{1+a}{a}\right)^3,
\quad M_4=150\left(\frac{80(1+a)}{9a}\right)^5.
\tag{RC16}
\]
We prove \(|J'''|\le M_3\), \(|J''''|\le M_4\). In the probability \(p_n=a_nz^n/F(z)\), put \(V=\operatorname{Var}n\) and let \(\kappa_3,\kappa_4\) be its third and fourth cumulants. Termwise differentiation on compact disks gives
\[
J''=-\frac1{8V},\quad
J'''=\frac{\kappa_3}{32V^3},\quad
J''''=\frac{\kappa_4V-3\kappa_3^2}{128V^5}.
\tag{RC17}
\]
The rational series certificate EG19 implies \(z<11/20\) for \(t\le1.1\). Also \(z\ge t/(1+t)\), \(F\le(1-z)^{-1/2}\), so
\(V\ge p_0p_1=z/(4F^2)\ge v_a\). Bounding \(a_n/F\le1\) in the raw moments and summing the differentiated geometric series at \(z=11/20\) gives
\[
\mathbb E n^2<10,\quad\mathbb E n^3<47,\quad
\mathbb E n^4<315,\quad\mathbb E n=t/4\le11/40.
\]
Thus \(V<10\), \(|\kappa_3|<47+3(11/40)10+2(11/40)^3<56\). The slightly tighter original values \(\mathbb E n^2\le6820/729\), \(\mathbb E n^3\le102740/2187\) give \(|\kappa_3|<55\). Moreover the fourth central moment is at most \(315+6(11/40)^2\,10<320\), since its other nonconstant terms are negative; hence \(|\kappa_4|<620<1000\). These inequalities in RC17 prove RC16: \(55/(32v_a^3)<M_3\) and \((1000\cdot10+3\cdot55^2)/(128v_a^5)<M_4\).

Choose an integer \(L\ge1\), \(h=L/q\), with \(a\le t_j-h<t_j+h\le1\), and take the complete actual product
\[
G^c_{j,L}=\left[\prod_{i=j-L}^{j+L-1}
\frac{1+b_{N_i}}{1+\rho_{N_i}}\right]^{1/(2mL)}.
\]
RC4 and RC13, followed by the centered Taylor formula for \(J\), prove
\[
\boxed{\left|\log\frac{G^c_{j,L}}{\sqrt{z_{t_j}}}\right|
\le\frac{e_k}{h}+\frac{M_3h^2}{6}.}
\tag{RC18}
\]
Indeed \(\log G^c=-[F_k(t_j+h)-F_k(t_j-h)]/(2h)\), and the two endpoint errors total at most \(e_k/h\); the centered average of \(J'\) differs from \(J'(t_j)\) by at most \(M_3h^2/6\). The opposite sign agrees exactly with \(\log\sqrt z=-J'\).

At \(h_0=(3e_k/M_3)^{1/3}\) and \(L=\lceil qh_0\rceil\), whenever the displayed interval guard holds, the bound is
\[
\frac{3^{2/3}}2 M_3^{1/3}e_k^{2/3}
+\frac{M_3h_0}{3q}+\frac{M_3}{6q^2}.
\tag{RC19}
\]
This proves a smaller error than the one-sided shrinking window, using its exact original integer cutoffs.

For the second centered difference, the triangular integral of \(J''\) cancels the odd term of its Taylor expansion. Since \(\int_{-1}^1u^2(1-|u|)du=1/6\),
\[
\boxed{\left|\frac{F_k(t_j+h)-2F_k(t_j)+F_k(t_j-h)}{h^2}
-J''(t_j)\right|\le\frac{4e_k}{h^2}+\frac{M_4h^2}{12}.}
\tag{RC20}
\]
At \(h_0=(48e_k/M_4)^{1/4}\), \(L=\lceil qh_0\rceil\), its bound becomes
\[
2\sqrt{M_4e_k/3}+\frac{M_4(2h_0/q+q^{-2})}{12}.
\tag{RC21}
\]
In particular the actual centered difference is negative as soon as this bound is below \(1/80\), because \(J''=-1/(8V)<-1/80\). This is a finite guard with an explicit eventual realization from LX34; it is not an assumption of the desired sign.

## 5. Stronger original source cost and the actual current

The retained [FW7 full-source comparison](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L120043) states for every finite polynomial degree \(n\)
\[
\ell=\frac{a_k}{[1+4(n+M)^2]^M},\quad u=A_k,\quad M=21+4m_0,
\quad \log(A_k/a_k)=O_h(k+\log k).
\tag{RC22}
\]
Here \(M\) is a fixed source exponent, not the multiplication operator. Use exactly its stated \(n=2q+2\); then
\(\log(u/\ell)=O_h(k+\log q)\), retaining both absolute constants and every source degree needed by the final raising column. The underlying polynomial proof uses the full weighted source inequality and successive Gamma multiplication bounds through degree \(n+M\), followed by Cauchy–Schwarz between the reciprocal weights. This is the same source, not an assumed metric equivalence.

The retained [LRS11 monic theorem](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L83769), or its stated receiver [FW47–49](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L120720), gives on the fixed-data domain
\[
\log(\nu^{(b),\sigma}_j/h_{Q_b+j})
=2Q_b\psi(j/Q_b)+O_h(\log q),
\quad0\le j\le2Q_b,\quad b=k,k-8.
\tag{RC23}
\]
All lower indices in OCP20 are at most \(q_0+O(k)\), and therefore lie in this proved interval eventually. For the remaining finite-index formulation OCP30 gives an explicit recurrence bound; no original cutoff is dropped. Integrating the logarithmic endpoint derivative bound from RC8–10 shows uniformly for \(0\le r\le q+1\)
\[
q_0\psi((r+\Delta-v_0)/q_0)-q\psi(r/q)=O_h(k\log q).
\tag{RC24}
\]
To verify this estimate, the argument displacement is \(O(k/q)\). The integral of \(1+|\log t|\) on an interval of that length is \(O((k/q)\log q)\); multiplying by \(q_0\) and including \(q-q_0=O(k)\) proves it.

Retain the original current notation of the supplied complete TeX OCP1–28: \(e_N,f_N\) are its orthonormal consecutive source classes, \(\epsilon_N=\sqrt{E_NF_N}/\omega_N\), \(\mathcal C_N\) is their full observed two-column Gram, \(\Theta_N\) its exact area certificate OCP22, and \(\alpha_N=\|P_{K,N}e_N\|^2\). The conductor proof there keeps the exact finite determinant
\(|\det Y|\ge|\kappa_N\kappa_{N+1}|A_DB_D[(1-x_N)(1-y_N)-z_N]\), including its cross term. Its two source comparisons and RC23–24 now prove
\[
\boxed{\begin{gathered}
\log\epsilon_N=q\psi(t_j)+O_h(k\log(q+2)),\qquad
0\le-\log\Theta_N=O_{h,\varpi}(k\log(q+2)),\\
\alpha_N\le e^{-2q\psi(t_j)+O_{h,\varpi}(k\log(q+2))},\qquad
\log\|C_N\|^+=O_h(k+\log q).
\end{gathered}}
\tag{RC25}
\]
Here \(C_N\) is the selfadjoint part of original multiplication; the last bound means \(\log\max(1,\|C_N\|)\). Its finite bound is \(2(N+1)\sqrt{u/\ell}\). To check each other error, the finite conductor norm \(\mathcal F_N\) is polynomial in \(N\) with fixed exponents, and \(L_N\) in OCP20 has bounded positive logarithm. The logarithms of \(d_N,e_N^\circ\) are \(-2q\psi(t_j)+O(k\log q)\) by RC23–24. Thus OCP19 and OCP25 hold eventually; their margin \(\zeta_N\ge1/2\) has bounded logarithm. The ratio \(\xi_N/e_N^\circ\) in the area certificate is compared before taking its bound: its logarithm is the difference in RC24 with error \(O(\log q)\). Substitution into OCP22 and OCP26 proves the area and leakage estimates in RC25. The exact monic difference formulas OCP5–7, with exponentially small subtraction ratios, prove its first estimate. This accounts for every possible growing error, without discarding either source column.

Write \(\mathcal C_N=\left(\begin{smallmatrix}a&r\\\bar r&d\end{smallmatrix}\right)\). The observed centered Hermitian current has exact nonzero eigenvalues
\[
\lambda_\pm=\epsilon_N[-\Im r\pm\sqrt{ad-(\Re r)^2}],
\quad\lambda_+\lambda_-=-\epsilon_N^2\det\mathcal C_N.
\tag{RC26}
\]
Indeed it is \(i\epsilon_N(vu^*-uv^*)\), with \([u,v]^*[u,v]=\mathcal C_N\); multiplication of its two-by-two characteristic polynomial proves RC26. The full isometry of the actual quotient is CE2–3. Its finite area bound and \(\mathcal C_N\preceq I\) give \(\epsilon_N\Theta_N\le\lambda_+,-\lambda_-\le\epsilon_N\). Thus RC25 improves all OCP38–48 logarithmic errors to \(O_{h,\varpi}(k\log q)\). In particular
\[
\log\lambda_+=\log(-\lambda_-)=q\psi(t_j)+O_{h,\varpi}(k\log q),
\quad \|\mathscr W_{K,N}\|+|\operatorname{tr}\mathscr W_{B,N}|
\le e^{O_{h,\varpi}(k\log q)}.
\tag{RC27}
\]
The operator has inertia \((1,1,\dim B-2)\); the two specified original source superpositions in OCP41–45 have opposite signed currents. No sign for a different vector follows from this signature.

## 6. Full first-order evolution and its hidden source

Let \(Q_B=(\Lambda G_N^{-1}\Lambda^*)^{-1}\), \(L_N=G_N^{-1}\Lambda^*Q_B\). The independent CE9–19 proof retains the full noncommuting Duhamel integral and both signed times. Its two operators are
\[
U_N(T)=\Lambda e^{iTM}L_N,\qquad
V_N(T)=e^{iT\Lambda ML_N},\qquad T=e^{-bq},\quad b>a_0/2.
\tag{RC28}
\]
Their norms are taken in the original \(Q_B\) metric. CE20a lists the complete finite cost. Equation RC25 bounds it by \(O(k\log q)\), so CE21–23 give
\[
\log\|U_N(T)\|=q(\psi(t_j)-b)_++O(k\log q),
\]
\[
\log\sigma_{\max}V_N(T)=-\log\sigma_{\min}V_N(T)
=q(\psi(t_j)-b)_++O(k\log q).
\tag{RC29}
\]
The equality here denotes the shared leading term with the stated errors. The smallest singular value follows from the exact intrinsic inverse \(V_N(T)^{-1}=V_N(-T)\); the full observed operator has the different inverse defect CE26. At \(b=1/8\), retaining all four signs,
\[
\boxed{\mathcal R\log\operatorname{cond}_{Q_{B,N}}V_N(e^{-q/8})
=[4\log(4/\pi)-1/2]q+O_{h,\varpi}(k\log q).}
\tag{RC30}
\]
The scalar \(e^{kT/2}\) for the original physical action cancels exactly in this condition number and in the four-cutoff norm return. The coefficient in RC30 is approximately \(0.4662579010819617787641475663\); its certificate is twice the independently replayed outgoing-norm coefficient. Combining RC15 with the 1-Lipschitz function \(x\mapsto(x-b)_+\) supplies actual-increment approximations to each leading exponent in RC29, with additional error at most \((1+t_j)(qe_k+2J(t_j))/2\), and twice that for the condition number.

In the actual quotient isometry \(J_N=L_NQ_B^{-1/2}\), put \(P=J_NJ_N^\dagger\). The full connecting defect is
\[
\mathcal D_N=J_N^\dagger M(I-P)MJ_N.
\tag{RC31}
\]
CE24–29 prove its complete Volterra equation and the exact rank-one cancellation
\(J_N^\dagger R(I-P)RJ_N=-z_NR_B\), because \(R^2=0\) before observation and \(R_B^2=z_NR_B\) after observation. This retains all mixed and hidden source terms. RC25 strengthens its full bound to \(\|\mathcal D_N\|\le\exp[q\psi(t_j)+O(k\log q)]\), and the entire hidden current remains bounded as in RC27. These are quantitative controls on the actual defect and its maps.

## 7. The prescribed eigenclass has an exact receiving map

Let \(x\) be any original eigenclass \(Mx=\omega x\), let \(y=Px\), and keep its hidden part \(x_K=(I-P)x\). The full action is \(M=C+\epsilon fe^\dagger\), with \(\|C\|\le c\), \(e\perp f\), and \(\alpha=\|(I-P)e\|^2\). The eigenvalue equation implies
\[
\epsilon|\langle e,x\rangle|\le(|\omega|+c)\|x\|.
\]
Since \(\langle e,y\rangle=\langle e,x\rangle-
\langle(I-P)e,x_K\rangle\), the exact current pairing and its bound are
\[
\Phi_N(\Lambda x)=i[\langle y,My\rangle-\langle My,y\rangle]
=-2\Im\omega\,\|y\|^2+2\Im\langle y,Mx_K\rangle,
\tag{RC32}
\]
\[
\boxed{|\Phi_N(\Lambda x)|\le
2[(|\omega|+c)\|x\|+\epsilon\sqrt\alpha\|x_K\|],\|y\|.}
\tag{RC33}
\]
For the bound, the selfadjoint part contributes zero and
\(|\Phi_N|\le2\epsilon|\langle e,y\rangle||\langle f,y\rangle|\), with the last factor at most \(\|y\|\). This proves RC33 and retains the complex interference term in RC32. By RC25 and \(|\omega|\le k\sqrt{\delta^2+\gamma^2}\), its coefficient is \(e^{O(k\log q)}\). If \(\Lambda x=0\), both sides vanish. Otherwise division by \(\|y\|^2\) still retains the actual ratio \(\|x\|/\|Px\|\). No individual projected sign or bound on that ratio is supplied by the operator signature. RC32–33 provide the exact return to that outstanding original vector calculation, strengthening the earlier complete residual identity NE13 without changing its observation.

## 8. Earlier heat receivers and verification scope

The new complete positive-word band LX42 has explicit error \(e_{\rm word}\) for every positive energy. Insert this error into the preceding [PH34–35](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/PHASE_HEAT_PROOFS.md#L641). If \(L_*=1/J'(1)\), its complete measured heat error is bounded by
\[
\alpha_k^{\rm angle}+L_*\frac{e_{\rm word}}q+
\frac1q+\frac{L_*(1+e^{-1})}q.
\tag{RC34}
\]
Here \(\alpha_k^{\rm angle}\) is the same complete projection-angle defect as PH35. To verify the scalar part, a Gumbel variable \(G\) represents the heat smoothing, and \(\mathbb E|G|\le1+e^{-1}\). The limiting cutoff distribution is \(L_*\)-Lipschitz, so a center displacement \(e_{\rm word}/q\) and the random displacement \(G/q\) cost at most the two displayed terms; the discrete cutoff measure costs \(1/q\). The original angle comparison is added before this scalar comparison. Thus the effective arrival improves the word error while preserving the earlier sharper \(O(1/q)\) smoothing term.

The auxiliary exact and interval checks accompanying this proof test the rational differential maps, source-window constants, complete finite maps and incoming scalar enclosures. They supplement the analytic proofs. They do not report evaluations of actual zeta zeros or period-dependent native matrices. Human provenance for the Gamma and orthogonal-polynomial inputs remains R. A. Askey and R. Roy, and T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw with W. P. Reinhardt, respectively: [DLMF5.7.6](https://dlmf.nist.gov/5.7.E6), [18.22.8](https://dlmf.nist.gov/18.22.E8), [18.23.7](https://dlmf.nist.gov/18.23.E7). Complete author equation TeX and reading locators are preserved. The elliptic source is Carlson as cited above; the programme-specific maps and error estimates are proved here and in the accompanying EG, LX, OCP and CE proofs.


## 9. The earlier terminal-class bound completes another receiver

The earlier [OB1–15 conductor and reverse-lift proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L127618) already controls the norm ratio occurring in RC33. We now apply it at its exact proved period domain. This is an integration of an established estimate, not a newly assumed bound.

Keep its prescribed terminal cardinal
\[
v_+(S)=\frac{\chi_k(S)}{(S-k\rho)\chi'_k(k\rho)},
\quad \rho=\tfrac12+\delta+i\gamma,
\quad \omega=k\gamma-ik\delta.
\tag{RC35}
\]
Then \(Mv_+=\omega v_+\) in the unchanged physical coordinate \(S=k/2+iy\).
Let \(j_-=k-8\), \(Q_0=Q_{j_-}\), \(v_-\) its corresponding terminal cardinal, and \(v_A\) the same first nonzero conductor order denoted \(v_0\) above. Evaluation at every lower-grid root proves
\[
C_Av_+=a_{88}v_-,\qquad K\subset\ker C_A.
\tag{RC36}
\]
Only the original \((8,8)\) shift reaches the upper terminal root. Every other evaluation is zero. Thus this is the original coefficient, with its phase, and not a freely chosen scalar.

Here is the explicit period domain proved in [OC50–74](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L127917). Retain \(\gamma\ge1000\delta\), the original five-orbit requirement and the admitted radius \(R_{\rm adm}\). Write
\[
\tau=(\gamma^2-\delta^2)/3,\quad d_h=2\delta\gamma,\quad
x=\delta+i\gamma,\quad h_c(w)=w^4+6\tau w^2+(\delta^2+\gamma^2)^2,
\]
\[
m_{\rm corner}=\frac{23\tau^2d_h}{500|h_c'(x)|^2},
\quad
R_{\rm corner}=\max\{R_{\rm adm},1,2\mathcal M_2/m_{\rm corner}\}.
\tag{RC37}
\]
The finite constant \(\mathcal M_2=18432\kappa_V^2 M_*^8\) retains OC67–69:
\[
\begin{gathered}
\rho_0=|x|,\quad
\kappa_V=\rho_0^2(1+\rho_0+\rho_0^2+\rho_0^3)/d_h,\\
A_2=(|\beta|/3)5^{3/5}2^{2/5},\quad
B_2=|\eta|5^{1/5}2^{4/5},\\
K_2=\tfrac25(12/5)^{3/2}A_2^{5/2}
+\tfrac45(4/5)^{1/4}B_2^{5/4},\\
M_*=\max_{\substack{1\le b\le4\\0\le r\le3}}
5^{(r+1-b)/5}2^{b/5}
\frac{\Gamma((r+1)/5)}{\Gamma(b/5)}e^{K_2},
\quad \beta=6\tau,\quad\eta=\rho_0^4.
\end{gathered}
\tag{RC38}
\]
These are fixed functions of the original quartet. The complete source proof bounds the exact original period conjugation entries by \(\mathcal M_2\) on \(|z|=2\), and their values at zero below by \(m_{\rm corner}\). Cauchy's coefficients give variation at most \(\mathcal M_2/|\varpi|\) at the actual \(z=\varpi^{-1}\). Extremal coefficients of the four-factor original biform are products of the four corresponding entries. Therefore, on \(|\varpi|\ge R_{\rm corner}\),
\[
|a_{88}|\ge(m_{\rm corner}/2)^4>0.
\tag{RC39}
\]
The algebraic estimate at zero keeps every original unit phase: OC59–60 bounds the squared-modulus difference of its two quadratic brackets, before taking their difference. The complete proof and coefficients are in the unchanged source bank at the precise locator above. No extension of RC39 to an exceptional period is made.

For completeness, the full finite terminal norm comparison used below is
\[
\frac{\|P_Nv_+\|_{G_N}^2}{\|v_+\|_{G_N}^2}
\ge\mathfrak l_{k,N}:=
\frac{\ell_k}{u_k}
\frac{|a_{88}|^2|D_k(k\rho)|^2g_{k,N}^{\Delta-v_A}}
{\mathfrak C_{A,N}^2\mathcal T_{N-\Delta}(z_0)^2
[2(N+1)+R]^{2\Delta}}>0,
\tag{RC40}
\]
where every original quantity is
\[
\begin{gathered}
D_k(S)=\chi_k(S)/\chi_{k-8}(S-8\rho),\quad
R=k\sqrt{\delta^2+\gamma^2},\quad z_0=-8\gamma+8i\delta,\\
B_-=2q_0/\delta+2+\pi/2,\quad
R_-=(k-8)\sqrt{\delta^2+\gamma^2},\\
g_{k,N}=\{1+B_-^2[R_-^2+4(N-v_A+3)^2]\}^{-1},\\
\mathcal T_n(z)=e(n+1)(2n+1)^{(|z|+1)/2},\\
\mathfrak C_{A,N}=\sum_{u,w=0}^8|a_{uw}|
\mathcal T_N((2w-8)\gamma-i(2u-8)\delta).
\end{gathered}
\tag{RC41}
\]
The values \(\ell_k,u_k\) are the original complete source constants through degree \(2q+2\).

Here is the entire receiving argument for RC40. The lower terminal cardinal minimum equals
\[
\mathcal E_-^\sigma(q_0-1+r)
=\frac{H_r}{|Q_0'((k-8)\gamma-i(k-8)\delta)|^2},
\quad
H_r=\min_{\deg p<r}\int\left|\frac1{z_--y}-p(y)\right|^2Q_0(y)^2d\sigma.
\]
The complete Jacobi resolvent gives
\(H_{r+1}/H_r=a_{r+1}^2 L/(1+a_{r+1}^2L)\), where
\(L=\|(z_--J^{(r+1)})^{-1}e_0\|^2\).
Its spectral measure has second moment \(a_{r+2}^2\), so Jensen gives
\(L\ge(R_-^2+a_{r+2}^2)^{-1}\).
Integration by parts using the digamma bound in OCP30 gives
\(a_{r+1}\ge(r+1)/B_-\), and the full Gamma multiplication bound gives
\(a_{r+2}\le2(q_0+r+2)\).
Thus each of the \(\Delta-v_A\) required original steps has ratio at least \(g_{k,N}\).

The exact reverse lift is
\[
v_+(S)=D_k(S)v_-(S-8\rho)/D_k(k\rho).
\]
It maps every lower representative of degree \(N-\Delta\) to an upper representative of degree \(N\), with all free relations intact. Translation has norm at most \(\mathcal T_{N-\Delta}(z_0)\): the Gamma generating function multiplies by \(e^{z_0\arctan t}\); Cauchy's formula at \(t=n/(n+1)\) and summation of all its weighted coefficient diagonals give exactly \(\mathcal T_n\). Successive multiplication by all \(\Delta\) factors of \(D_k\) costs \([2(N+1)+R]^\Delta\). Conversely RC36 forces every lift of the observed terminal class to have lower conductor class \(a_{88}v_-\), whose full minimum is bounded below by its lower cardinal norm divided by \(\mathfrak C_{A,N}^2\). Apply both source comparisons and the consecutive-minimum bound. Their quotient is RC40, with every determinant factor retained.

Every factor of \(D_k(k\rho)\) has modulus at least \(2(k-7)\delta\); there are \(\Delta=O(k)\) such factors. The finite formulas give
\[
0\le-\log\mathfrak l_{k,N}=O_{h,\varpi}(k\log q)
\tag{RC42}
\]
uniformly on the original window. Its lower sign follows because RC40 compares with an actual norm ratio at most one. Its upper order follows from \(-\log g=O(\log q)\), \(\log(u/\ell)=O(k+\log q)\), and fixed exponents in the translation constants. Consequently RC33 has the new normalized receiver
\[
\boxed{
\frac{|\Phi_N(\Lambda v_+)|}{\|\Lambda v_+\|_{Q_{B,N}}^2}
\le
2\mathfrak l_{k,N}^{-1/2}
\bigl[|\omega|+c_N+\epsilon_N\sqrt{\alpha_N}\bigr]
=\exp[O_{h,\varpi}(k\log q)].
}
\tag{RC43}
\]
This closes the norm-ratio step on its proved period domain. The same explicit obstruction at other admitted periods remains governed by their actual conductor columns and RC32; no nonvanishing is assigned there.

There is a further exact consequence in the observed current's sign eigenspaces. Let \(w_\pm\) be unit eigenvectors for RC26 in the actual observation metric, put
\[
b=\Lambda v_+/\|\Lambda v_+\|_{Q_B},\qquad
p_\pm=|\langle w_\pm,b\rangle_{Q_B}|^2,
\quad j_N=\Phi_N(\Lambda v_+)/\|\Lambda v_+\|_{Q_B}^2.
\]
The spectral theorem, with all zero directions retained, gives
\(j_N=\lambda_+p_++\lambda_-p_-\). Therefore
\[
\boxed{
|p_+-p_-|
\le\frac{|j_N|}{-\lambda_-}
+\left|\frac{\lambda_+}{-\lambda_-}-1\right|p_+
\le\exp[-q\psi(t_j)+O_{h,\varpi}(k\log q)].
}
\tag{RC44}
\]
The last inequality is RC25–27, RC43 and the exact trace bound
\(|\lambda_++\lambda_-|\le2\epsilon\sqrt\alpha\).
It proves exponentially balanced weights of the original terminal class in the two sign sectors. It does not infer its residual sign: that still belongs to the complex pairing in RC32. The result now uses the earlier conductor comparison rather than sending that completed calculation back out as missing work.
