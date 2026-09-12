# Partial original residues for the complete tensor section correction

This direct continuation retains the exact source of CW.1–40, SHA256 6ca142ec052ad110e3c58ece4d81bf87a33fc18c8533c41deb863bceb300715a, without changing that sealed fragment. The parent owns cumulative integration.

Let \(h(s)=\prod_{\rho\in\mathcal Z}(s-\rho)^{m_\rho}\) be the original monic nonempty finite packet of actual zeros with complete orders, \(d=\deg h\ge1\), \(g=2\xi\), \(v_h=g/h\), \(k\ge1\). Write
\[
E_h=\mathbb C[s]/(h),\quad E=E_h^{\otimes k},\quad
E_{\widehat i}=\bigotimes_{j\ne i}E_h,\quad
v_i=j_h(v_h)\text{ in the \(i\)-th factor},\quad
\gamma_i=j_h(g')\text{ in the \(i\)-th factor},\quad U=\prod_i v_i.
\]
Every \(v_i\) is the original complete invertible jet. Let \(\ell_h:E_h\to\mathbb C\) extract the coefficient of \(s^{d-1}\) from the unique one-variable monic remainder. Let \(c_i:E_{\widehat i}\to E\) insert the constant polynomial one in the \(i\)-th factor, and let \(\ell_i:E\to E_{\widehat i}\) apply \(\ell_h\) in that factor and identity in every other factor. Thus \(\ell_i\) extracts the original coefficient of \(s_i^{d-1}\), retaining every other-variable coordinate. For \(k=1\), \(E_{\widehat i}=\mathbb C\), and \(c_i\) is the unit column. Let \(M_a\) denote multiplication by the displayed element in its declared algebra.

Define the coefficient-valued partial residue map
\[
\mathcal R_i:E\longrightarrow E_{\widehat i},\qquad
\mathcal R_i(u)=
\sum_{\rho\in\mathcal Z}\operatorname{Res}_{s_i=\rho}
\frac{\widetilde u(s_1,\ldots,s_k)}{g(s_i)}\,ds_i ,
\tag{PRC.1}
\]
where the coefficients in the other original variables are taken modulo their original ideals after the indicated residue. Each residue uses the usual positively oriented complex \(s_i\)-coordinate; there is no additional \(2\pi i\) factor in this residue notation. Equivalently, each residue equals \(1/(2\pi i)\) times the corresponding positively oriented contour integral.

This map is well-defined on \(E\). A change by \(h(s_i)p\) in its own variable changes the integrand by \(p/v_h(s_i)\), which is holomorphic at every selected centre because the removed zero orders were complete. A change by \(h(s_j)p\), \(j\ne i\), produces that same factor \(h(s_j)\) in the remaining coefficient algebra, hence zero in \(E_{\widehat i}\). Linearity then covers the full original ideal. The finite sum of coefficient residues is complex-linear and \(E_{\widehat i}\)-linear.

The exact coefficient formula is
\[
\boxed{\mathcal R_i=\ell_iM_{v_i}^{-1}.}
\tag{PRC.2}
\]
To prove it, let \(p_i\) be the degree-below-\(d\) remainder in \(s_i\) of \(v_i^{-1}u\), retaining the full coefficient algebra \(E_{\widehat i}\). The residue in (PRC.1) equals the corresponding residue of \(p_i/h(s_i)\): the difference in the numerator vanishes to the complete selected orders, so division by \(h\) is locally holomorphic. Every coefficient of \(p_i/h\) has an ordinary partial-fraction expansion. The coefficient of \(s_i^{-1}\) at infinity is the sum of the finite simple-pole coefficients; higher-pole terms contribute no \(s_i^{-1}\) coefficient. Since \(h\) is monic and \(\deg_{s_i}p_i<d\), that coefficient is precisely \(\ell_i(p_i)\). This proof applies coefficientwise in the finite algebra \(E_{\widehat i}\) and gives (PRC.2) with every other-variable nilpotent coefficient retained.

Define the original partial correction endomorphisms
\[
C_i=M_{\gamma_i}c_i\mathcal R_i:E\longrightarrow E.
\tag{PRC.3}
\]
They satisfy
\[
\boxed{C_i^2=dC_i,\qquad
C_iC_j=C_jC_i,\qquad
\operatorname{rank}C_i=d^{k-1},\qquad
\operatorname{Tr}C_i=d^k.}
\tag{PRC.4}
\]
Indeed \(g'=h'v_h+hv_h'\) gives \(\gamma_i=v_ih_i'\) in the original \(i\)-th quotient, so
\[
\mathcal R_iM_{\gamma_i}c_i
=\ell_iM_{v_i}^{-1}M_{\gamma_i}c_i
=\ell_iM_{h_i'}c_i=dI_{E_{\widehat i}}.
\tag{PRC.5}
\]
The last equality uses the literal degree \(d-1\) and leading coefficient \(d\) of the original derivative \(h'\). This proves the first formula in (PRC.4). It also proves that \(M_{\gamma_i}c_i\) is injective and \(\mathcal R_i\) is onto. The factorization (PRC.3) therefore has rank \(\dim E_{\widehat i}=d^{k-1}\). Alternatively a specified right inverse for \(\mathcal R_i\) is \(a\mapsto v_i s_i^{d-1}c_i(a)\), using (PRC.2). The two rectangular factors in (PRC.3) have traces \(\operatorname{Tr}_E(AB)=\operatorname{Tr}_{E_{\widehat i}}(BA)\); apply (PRC.5) to obtain \(d\,d^{k-1}=d^k\). Operators belonging to distinct variables are tensor products of their respective one-variable maps with identity on the other factors. Their compositions therefore commute, proving the remaining identity.

These operators give precisely the correction of the original full-unit section:
\[
\boxed{\mathsf J_U=\frac1k\sum_{i=1}^k C_i.}
\tag{PRC.6}
\]
For proof, retain the complete CW thickened unit \(\widehat U\), its residue \(U=\prod_i v_i\), and its full first derivative \(\beta_h=U^{-1}\delta\widehat U\). The original source-selected operator is still
\[
\mathsf D_U=M_{\beta_h}+M_U\mathsf D_0M_U^{-1},
\qquad
[Z,\mathsf D_U]=-I_E+\mathsf J_U,\qquad
\mathsf J_U=M_U\left(\frac1k\sum_i M_{h_i'}c_i\ell_i\right)M_U^{-1}.
\tag{PRC.7}
\]
Write \(U=v_iU_{\widehat i}\), with \(U_{\widehat i}=\prod_{j\ne i}v_j\). The maps \(c_i,\ell_i\) are \(E_{\widehat i}\)-linear, so the operator \(M_{U_{\widehat i}}\) commutes through their indicated source and target actions, and its inverse then cancels with exactly that same full other-variable unit. Thus each summand in (PRC.7) is
\[
M_U M_{h_i'}c_i\ell_iM_U^{-1}
=M_{v_i h_i'}c_i\ell_iM_{v_i}^{-1}
=M_{\gamma_i}c_i\mathcal R_i=C_i.
\tag{PRC.8}
\]
This proves (PRC.6). No \(v_i\) has been replaced by one, and no unit derivative has been discarded: the term \(M_{\beta_h}\) remains in \(\mathsf D_U\) and commutes with the original multiplication operator \(Z=M_{\sum_i s_i-k/2}\), which is why it contributes zero to that specified commutator.

For completeness, retaining all \(k\) residue variables gives
\[
\mathcal R_{\mathrm{all}}:E\longrightarrow\mathbb C,\qquad
\mathcal R_{\mathrm{all}}(u)=
\sum_{\rho_1,\ldots,\rho_k\in\mathcal Z}
\operatorname{Res}_{s_k=\rho_k}\cdots
\operatorname{Res}_{s_1=\rho_1}
\frac{\widetilde u(\mathbf s)}{\prod_i g(s_i)}\,
ds_1\cdots ds_k.
\tag{PRC.9}
\]
Here the formula means the ordered iterated coefficient residues, with each original variable positively oriented. Each variable operates on a different tensor factor, so swapping their evaluation order gives the identical scalar coefficient and introduces no sign. Formula (PRC.2) in each factor proves
\[
\mathcal R_{\mathrm{all}}
=\ell_h^{\otimes k}M_U^{-1},
\qquad
\boxed{C_1\cdots C_k(u)
=\left(\prod_i\gamma_i\right)\mathcal R_{\mathrm{all}}(u).}
\tag{PRC.10}
\]
The map \(\ell_h^{\otimes k}:E_h^{\otimes k}\to\mathbb C\) is the tensor product of the original one-variable highest-coefficient functionals. Tensoring the one-variable factorization (PRC.3) proves the second equality directly, so it keeps all repeated-root and mixed nilpotent data before the final scalar functional is evaluated. The column and functional are both nonzero: their contraction is
\[
\mathcal R_{\mathrm{all}}\left(\prod_i\gamma_i\right)
=\prod_{i=1}^k
\left(\sum_{\rho\in\mathcal Z}
\operatorname{Res}_{s_i=\rho}\frac{g'(s_i)}{g(s_i)}\,ds_i\right)
=\prod_{i=1}^k\left(\sum_\rho m_\rho\right)=d^k.
\tag{PRC.11}
\]
This is the rank-one full-product correction, with its exact nonzero eigenvalue and trace \(d^k\). Its square is \(d^k\) times itself by (PRC.10)–(PRC.11). The residue of \(g'/g\) is \(m_\rho\) because \(g(s)=(s-\rho)^{m_\rho}u_\rho(s)\) with \(u_\rho(\rho)\ne0\); hence \(g'/g=m_\rho/(s-\rho)+u_\rho'/u_\rho\). This gives the complete multiplicity proof used in (PRC.11).

At \(d=1\), (PRC.5) gives \(C_i=I_E\) on the one-dimensional \(E\); consequently \(\mathsf J_U=I_E\), and (PRC.10) is the same identity. At \(k=1\), every formula reduces exactly to CW.31–33, including the original residue functional \(\mathscr R_{\mathcal Z}(1,u)\), rank one and trace \(d\). For \(h=1\), the original arithmetic quotient is zero; no formula using an inverse unit in a positive-degree packet or a degree-\(d-1\) coefficient is applied. No statement here assumes root simplicity, separation of repeated fibres, RH, a scalar-valued replacement for the original arithmetic unit, or an orthogonal metric for these algebraic maps.
