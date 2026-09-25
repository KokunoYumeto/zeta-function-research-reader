# Involutions of the actual extension-class modules and their original-zeta residue maps

24 September 2026. Complete independent derivation ECI0–ECI13.

## ECI0. The constructed objects and the next calculation

The support remains \(\tau\langle Z_1;\text{no }Z_2\rangle\). All scalars, functions, modules and dual operations below occur after complete-history arithmetic reconstruction. The two branch counters remain separate. Addition at \(\tau\) remains retracted, and no numerical coordinate, midpoint, metric or parity is assigned to it. The current corpus-and-operation rule and `READ_FIRST_USER_CONSTRUCTION.md` were read again before selecting these operations. The amended forward-step rule asks for an actual next calculation using all established findings. Here that calculation is the involution and duality of the actual cyclic extension modules just constructed, followed by their map to the existing residue receiver.

The complete FOD0–FOD8 and NEA0–NEA10 proofs were read, together with the already checked GMS, GSR, RTT and GTAH comparisons. Their exact annihilator statements are used, not an assumption that the full normal ideal has a quotient's spectrum. Write
\[
M=\{h\text{ entire}:\text{on each bounded real strip, }h
\text{ has at most polynomial vertical growth}\},
\]
\[
\mathcal B=\{F\text{ entire}:b_{A,N}(F)=
\sup_{|\Re s|\le A}(1+|\Im s|)^N|F(s)|<\infty
\text{ for every }A,N\}.
\tag{ECI0.1}
\]
For every actual original nontrivial zero \(\rho\) of \(\zeta\), retain its full multiplicity \(m_\rho\). The ideals are
\[
\mathfrak a=\{h\in M:\operatorname{ord}_\rho h\ge m_\rho\ \forall\rho\},
\quad
\mathfrak a_+=\{h\in M:\operatorname{ord}_{\rho+1}h\ge m_\rho\ \forall\rho\},
\]
\[
\mathcal I=\mathcal B\cap\mathfrak a,
\quad\mathcal I_+=\mathcal B\cap\mathfrak a_+,
\quad\mathcal Q=\mathcal B/\mathcal I,
\quad\mathcal Q_+=\mathcal B/\mathcal I_+,
\]
\[
\mathscr C=M/\mathfrak a,
\qquad\mathscr C_+=M/\mathfrak a_+.
\tag{ECI0.2}
\]
FOD and NEA prove the identifications
\[
\mathscr C\simeq M e_0\simeq M e_{\rm low},\qquad
\mathscr C_+\simeq M e_+\simeq M e_{\rm high}\simeq M\delta.
\tag{ECI0.3}
\]
Each sends \([h]\) to the displayed actual class multiplied by \(h\). The generator \(e_0\) is the original source row, \(e_+\) is the actual normal source row, and \(\delta\) is the actual localization boundary with the shifts retained in FOD7 and NEA10. These are isomorphisms of the cyclic images only, not of full Ext groups or full source ideals. No unproved locally convex topology is assigned to \(M\), \(\mathscr C\), or \(\mathscr C_+\). Their embeddings of \(\mathcal Q\) and \(\mathcal Q_+\) remain the injective maps induced by \(\mathcal B\subset M\).

## ECI1. Conjugation, reflection, and the two distinct Weil involutions

On the original coordinate define
\[
\mathsf C h(s)=\overline{h(\overline s)},\qquad
\mathsf R_1h(s)=h(1-s),\qquad
\mathsf K_1h(s)=h^{\#_1}(s)=\overline{h(1-\overline s)}.
\tag{ECI1.1}
\]
The first and third maps are anti-linear, the second is linear, and \(\mathsf K_1=\mathsf C\mathsf R_1=\mathsf R_1\mathsf C\). Taylor expansion proves that their outputs are entire. A strip of width \(A\) is carried into one of width at most \(A+1\); imaginary parts only change sign. Thus each preserves \(M\) and is continuous on \(\mathcal B\). Each is multiplicative and involutive, with the appropriate conjugation of complex scalars.

The actual original functional equation and conjugation give the multiplicity-preserving permutations \(\rho\mapsto\overline\rho\), \(\rho\mapsto1-\rho\), and \(\rho\mapsto\rho^\#=1-\overline\rho\). Hence all three maps preserve \(\mathfrak a\) and \(\mathcal I\), and induce the corresponding maps on \(\mathscr C\) and \(\mathcal Q\). In full local jets,
\[
j_\rho(\mathsf K_1h)=
\sum_{j=0}^{m_\rho-1}
\frac{(-1)^j\overline{h^{(j)}(\rho^\#)}}{j!}(s-\rho)^j.
\tag{ECI1.2}
\]
This is the complete jet map, not only its value.

In the translated normal coordinate \(\lambda\), the corresponding maps are
\[
\mathsf R_3h(\lambda)=h(3-\lambda),\qquad
\mathsf K_3h(\lambda)=h^{\#_3}(\lambda)=
\overline{h(3-\overline\lambda)}.
\tag{ECI1.3}
\]
Conjugation remains \(\mathsf C h(\lambda)=\overline{h(\overline\lambda)}\). These preserve \(\mathfrak a_+\) and \(\mathcal I_+\), since
\[
3-\overline{(\rho+1)}=\rho^\#+1.
\tag{ECI1.4}
\]
Formula (ECI1.2) holds with \(\rho,\rho^\#\) replaced by \(\rho+1,\rho^\#+1\), with exactly the same factorials and signs. In particular \(\#_1\) must not be used as the normal involution without coordinate transport. It carries the translated divisor to \(\mathscr Z-1\), since \(1-\overline{(\rho+1)}=\rho^\#-1\). Likewise \(\#_3\) carries the unshifted divisor to \(\mathscr Z+2\). These are exact maps to other translated ideals, not identifications with the original ideal.

The induced operations on the cyclic extension modules are, for example,
\[
\mathsf K_{e_0}(h e_0)=h^{\#_1}e_0,
\qquad
\mathsf K_{e_+}(h e_+)=h^{\#_3}e_+.
\tag{ECI1.5}
\]
Well-definedness is precisely invariance of the proved annihilator ideals. On the actual original row, the anti-linear semilinear maps \(\mathsf K_1\) on its kernel, middle module and quotient commute with the inclusion and quotient maps. On the normal row the analogous statement uses \(\mathsf K_3\). Consequently these are also the maps on the cyclic classes obtained by applying those explicit semilinear exact equivalences to the rows, fixing the respective generator. No homological sign is introduced by this covariant exact operation. Transport to the low and high class modules uses the exact cyclic pushout isomorphisms (ECI0.3); it does not claim that \(\mathsf K_1\) alone preserves the full intersection ideal of the joint row.

## ECI2. Translation and every scalar degree

Retain the actual maps
\[
(Vh)(\lambda)=h(\lambda-1),\qquad
(Uk)(s)=k(s+1),\qquad UV=VU=1.
\tag{ECI2.1}
\]
They preserve polynomial strip bounds and rapid strip bounds, using strips enlarged by one. They give inverse ring isomorphisms \(M_s\leftrightarrow M_\lambda\), take \(\mathfrak a\leftrightarrow\mathfrak a_+\), and induce inverse maps \(\mathscr C\leftrightarrow\mathscr C_+\), as well as the established topological maps \(\mathcal Q\leftrightarrow\mathcal Q_+\). They are semilinear for this translation of scalars:
\[
V(hx)=(Vh)(Vx).
\tag{ECI2.2}
\]
Equivalently, equip the unshifted normal module with the actual action \(h\cdot x=h(s+1)x(s)\); then \(V\) is \(M\)-linear to the normal module in the \(\lambda\)-coordinate.

Direct substitution proves
\[
\mathsf C V=V\mathsf C,
\quad\mathsf R_3V=V\mathsf R_1,
\quad\mathsf K_3V=V\mathsf K_1.
\tag{ECI2.3}
\]
Under (ECI0.3), \(h e_0\mapsto(Vh)e_+\) is the corresponding semilinear isomorphism of cyclic extension modules. At the level of the actual rows it is induced by translating the entire original source sequence, including its kernel. It is not the identity on the scalar ring's coordinate.

Write \(L[h]=[sh]\), \(L_+[k]=[\lambda k]\), \(D_a[h]=[a^s h]\), and \(D_a^+[k]=[a^\lambda k]\), for every already recovered \(a>0\). Then
\[
L_+V=V(L+1),\qquad
D_a^+V=aVD_a,\qquad
UD_a^+=aD_aU.
\tag{ECI2.4}
\]
Their involution identities are
\[
\mathsf K_1L=(1-L)\mathsf K_1,
\qquad\mathsf K_3L_+=(3-L_+)\mathsf K_3,
\]
\[
\boxed{\mathsf K_1D_a=aD_{1/a}\mathsf K_1,
\qquad\mathsf K_3D_a^+=a^3D_{1/a}^+\mathsf K_3.}
\tag{ECI2.5}
\]
Both scalar degree factors follow by substituting the full coordinate in the exponential; neither is selected from a desired weight. On a length-\(m_\rho\) block they retain
\[
D_a=a^\rho\sum_{j=0}^{m_\rho-1}
\frac{(\log a)^j}{j!}M_t^j,
\qquad
D_a^+=a^{\rho+1}\sum_{j=0}^{m_\rho-1}
\frac{(\log a)^j}{j!}M_t^j.
\tag{ECI2.6}
\]
Translation leaves the local parameter \(t\) unchanged; the reflected anti-linear jet map changes it to \(-t\) while conjugating coefficients as in (ECI1.2). These formulas retain every nilpotent term.

## ECI3. The joint class module has a componentwise involution with an explicit source representative

FOD proves \(c\in\mathfrak a_+\), \(1-c\in\mathfrak a\), and
\[
M/(\mathfrak a\cap\mathfrak a_+)\xrightarrow{\sim}
\mathscr C\oplus\mathscr C_+,
\qquad[h]\mapsto([h]_{\mathfrak a},[h]_{\mathfrak a_+}),
\tag{ECI3.1}
\]
with inverse \(([f],[g])\mapsto[cf+(1-c)g]\). The componentwise operation \((x,y)\mapsto(\mathsf K_1x,\mathsf K_3y)\) therefore induces an exact anti-linear multiplicative involution on the actual joint cyclic module. In the single quotient presentation it is
\[
[h]\longmapsto[c h^{\#_1}+(1-c)h^{\#_3}]
\quad\bmod(\mathfrak a\cap\mathfrak a_+).
\tag{ECI3.2}
\]
If a representative changes by the intersection ideal, the first component of its \(\#_1\) change vanishes in \(\mathscr C\), and the second component of its \(\#_3\) change vanishes in \(\mathscr C_+\). The separator kills the opposite components. This proves well-definedness directly. Multiplicativity and the square identity follow from (ECI3.1) on both components. In particular the two actual component idempotents represented by \(c\) and \(1-c\) are fixed.

There is an actual anti-linear continuous source representative on \(\mathcal B\):
\[
\mathsf A_cF=c\mathsf K_1F+(1-c)\mathsf K_3F.
\tag{ECI3.3}
\]
It preserves \(\mathcal K=\mathcal I\cap\mathcal I_+\), by exactly the preceding full-jet argument, and induces the componentwise involution on \(\mathcal B/\mathcal K\). Its complete square before quotient is
\[
\begin{aligned}
\mathsf A_c^2F={}&
\bigl[c c^{\#_1}+(1-c)(1-c)^{\#_3}\bigr]F\\
&+c(1-c)^{\#_1}F(s+2)
+(1-c)c^{\#_3}F(s-2).
\end{aligned}
\tag{ECI3.4}
\]
This follows by expanding the four terms and using \(\mathsf K_1\mathsf K_3F=F(s+2)\), \(\mathsf K_3\mathsf K_1F=F(s-2)\). Each cross-term multiplier vanishes to the full orders at both required divisors. The coefficient of \(F\), minus one, does as well. Thus \(\mathsf A_c^2F-F\in\mathcal K\), with the entire difference displayed. No equality \(\mathsf A_c^2=1\) on \(\mathcal B\), and no single scalar-ring involution preserving the whole original and normal row at once, has been assumed. The actual full-source extension and this explicit error remain available.

## ECI4. The dual involution on the strong residue receiver contains the functional-equation unit

Retain RTT's \(\widehat\iota:\mathcal H_{\rm res}\xrightarrow{\sim}\mathcal Q'_\beta\). The continuous anti-linear involution \(\mathsf K_1\) on \(\mathcal Q\) induces
\[
(\mathsf K_1^\vee\lambda)(F)=\overline{\lambda(\mathsf K_1F)},
\qquad\mathsf K_1^\vee:\mathcal Q'_\beta\to\mathcal Q'_\beta.
\tag{ECI4.1}
\]
The value is linear in \(F\), anti-linear in \(\lambda\), and the square is the identity. For a bounded \(B\subset\mathcal Q\), its strong seminorm is \(p_{\mathsf K_1B}(\lambda)\). Thus it is strong-continuous. Define the actual continuous involution
\[
\mathsf K_{\rm res}=\widehat\iota^{-1}\mathsf K_1^\vee\widehat\iota.
\tag{ECI4.2}
\]
This definition is on the full completion and requires no global meromorphic multiplier theorem.

Its finite-jet formula retains a nontrivial unit and sign. Original zeta has
\[
\zeta(s)=\chi(s)\zeta(1-s),\qquad
\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)
=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\tag{ECI4.3}
\]
For finite-support \(g\), conjugating its residue pairing against \(\mathsf K_1F\), using \(\overline{\zeta(\overline s)}=\zeta(s)\), and then substituting \(s=1-z\), gives
\[
\begin{aligned}
(\mathsf K_1^\vee\iota g)(F)
&=\sum_\rho\operatorname{Res}_{s=\rho}
\frac{F(1-s)(\mathsf Cg)(1-s)}{\zeta(s)}\,ds\\
&=-\sum_\rho\operatorname{Res}_{s=\rho}
\frac{F(s)(\mathsf Cg)(s)\chi(s)}{\zeta(s)}\,ds.
\end{aligned}
\tag{ECI4.4}
\]
The minus sign is the derivative of the reflection. Accordingly \(\mathsf K_{\rm res}g\) is the unique finite-support class with local jets
\[
\boxed{j_\sigma(\mathsf K_{\rm res}g)
=j_\sigma\bigl[-\chi(1-s)g^{\#_1}(s)\bigr].}
\tag{ECI4.5}
\]
Every required germ of \(\chi(1-s)\) is a holomorphic unit; RD's global finite isolators realize those jets. Their derivatives are included in the product in (ECI4.5), not replaced by the unit's value. The formula does not assert that its meromorphic expression on the entire plane preserves \(\mathcal B\). The extension to the full residue completion is instead already proved by (ECI4.1)–(ECI4.2). Locally its square is also directly one, since \(\chi(1-s)\chi(s)=1\) and the two minus signs cancel.

For reference, conjugation alone on the dual, \(\lambda\mapsto(F\mapsto\overline{\lambda(\mathsf CF)})\), corresponds on finite residue classes to \(g\mapsto\mathsf Cg\). Linear reflection on the dual corresponds to local jets \(-\chi(1-s)g(1-s)\). These follow by the same computation without one of its conjugations. Thus the source involution and its actual residue-dual representative have a proved morphism retaining their functional-equation defect; they are not silently identified.

## ECI5. Every cyclic class has a canonical original-zeta trace functional

An element \([h]\in\mathscr C\) need not be in the rapid-decay quotient \(\mathcal Q\). Nevertheless the exact expression
\[
\mathsf W_M([h])(F)
=\sum_\rho m_\rho F(\rho)\overline{h(\rho^\#)},
\qquad F\in\mathcal Q,
\tag{ECI5.1}
\]
defines a continuous complex-linear functional on \(\mathcal Q\). It is anti-linear in \([h]\). To prove the assertion with its topology, let \(w_\rho=1+|\Im\rho|\). The strip bound for this particular \(h\) gives \(|h(\rho^\#)|\le Cw_\rho^d\). For every integer \(k\ge0\),
\[
E_k:\mathcal Q\to H,\qquad (E_kF)_\rho=w_\rho^kF(\rho)
\tag{ECI5.2}
\]
is continuous: its squared norm is bounded on \(\mathcal B\) by \(b_{1,k+2}(F)^2\sum_\rho m_\rho w_\rho^{-4}\), and it kills \(\mathcal I\). Choose \(k\ge d+2\). Cauchy–Schwarz gives
\[
|\mathsf W_M([h])(F)|
\le\|E_kF\|_+
\left(\sum_\rho m_\rho w_\rho^{-2k}|h(\rho^\#)|^2\right)^{1/2}<\infty.
\tag{ECI5.3}
\]
The unconditional full zero count makes the last sum finite. This proves both absolute convergence and continuity on the actual quotient. Changing \(h\) by \(\mathfrak a\), or \(F\) by \(\mathcal I\), changes no term.

Define
\[
\boxed{\mathsf S_M=\widehat\iota^{-1}\mathsf W_M:
\mathscr C\longrightarrow\mathcal H_{\rm res}.}
\tag{ECI5.4}
\]
This is an anti-linear map from the specified algebraic module; no continuity claim is made for an unassigned topology on \(\mathscr C\). Its restriction along \(\mathcal Q\hookrightarrow\mathscr C\) is exactly the already proved continuous map \(\mathsf S\) from RTT.

There is an exact strong residue realization of every value in (ECI5.4). For finite \(E\subset\mathscr Z\), put
\[
r_E(h)=\sum_{\rho\in E}
m_\rho(-1)^{m_\rho-1}u_\rho(0)
\overline{h(\rho^\#)}e_{1-\rho,m_\rho-1},
\qquad
\zeta(\rho+t)=t^{m_\rho}u_\rho(t).
\tag{ECI5.5}
\]
Its residue functional is the finite partial sum in (ECI5.1), by RTT's exact local matrix. For a bounded \(B\subset\mathcal Q\), the tail seminorm is at most
\[
\sup_{F\in B}\|E_kF\|_+
\left(\sum_{\rho\notin E}m_\rho w_\rho^{-2k}|h(\rho^\#)|^2\right)^{1/2}
\longrightarrow0.
\tag{ECI5.6}
\]
This proves strong convergence in the entire residue receiver. No density of finite-support primal classes, chosen Gaussian window, or unproved infinite residue series is needed.

Let \(\mathfrak r=\{h\in M:h(\rho)=0\ \forall\rho\}\). Global isolators tested in (ECI5.1) give the exact kernel
\[
\ker\mathsf S_M=\mathfrak r/\mathfrak a.
\tag{ECI5.7}
\]
Locally this is the higher-jet ideal in every multiplicity block. No uniform nilpotence exponent, or equality with an algebraic nilradical when multiplicities are unbounded, is asserted globally. Each original zero value survives.

## ECI6. A full-jet primal multiplier on the cyclic module, and involution covariance

The multiplier \(H_\zeta=s^2\zeta'(1-s)\) belongs to \(M\) by RTT2's full Euler–Maclaurin estimate, and \(H_\zeta(0)=-1\). The original \(F_0\in\mathfrak a\) has \(F_0(0)=1/8\). Thus
\[
[h]\longmapsto
\left[\frac{h(s)-F_0(s)h(0)/F_0(0)}s\right]
\tag{ECI6.1}
\]
is the inverse of \(L\) on the entire \(\mathscr C\). Entire division at the one removable point preserves the polynomial strip bounds, and the same local argument preserves \(\mathfrak a\). The two inverse identities follow by multiplication, exactly as in NEA7 and RTT2. This constructs
\[
\mathsf P_M=L^{-2}M_{s^2\zeta'(1-s)}\mathsf C:
\mathscr C\to\mathscr C.
\tag{ECI6.2}
\]
Its full local germ at a zero is \(\zeta'(1-s)\overline{h(\overline s)}\). If the output zero is \(\sigma\), put \(\rho=1-\sigma\), \(m=m_\rho\). Then
\[
j_\sigma(\mathsf P_Mh)=
m(-1)^{m-1}u_\rho(0)\overline{h(\overline\sigma)}(s-\sigma)^{m-1}.
\tag{ECI6.3}
\]
The proof differentiates \(\zeta(\rho-t)=(-t)^mu_\rho(-t)\) with respect to its own argument before taking the full quotient jet, as in RTT3. The coefficient is nonzero, so the block map has rank one, with the exact kernel of all positive-order input jets. Its global kernel is again \(\mathfrak r/\mathfrak a\). The map restricts to RTT's continuous \(\mathsf P\) on \(\mathcal Q\); the target is otherwise the explicitly algebraic module \(\mathscr C\).

For any \(b,h\in M\), the full convergent trace formula proves
\[
\widehat\iota\mathsf S_M(bh)
=m_{b^{\#_1}}'\widehat\iota\mathsf S_M(h).
\tag{ECI6.4}
\]
The transpose acts on the original continuous dual; its strong continuity follows because the multiplier on \(\mathcal Q\) preserves bounded sets. This is the extended exact GSR covariance, with its scalar conjugation intact.

The involution comparison is
\[
\boxed{\mathsf S_M\mathsf K_1=\mathsf K_{\rm res}\mathsf S_M.}
\tag{ECI6.5}
\]
Indeed evaluating the right side at \(F\) gives
\(\overline{\sum m_\rho\overline{F(\rho^\#)}\overline{h(\rho^\#)}}
=\sum m_\rho F(\rho)h(\rho)\), after reindexing by \(\#\). Evaluating the left side gives the same expression. Its absolute convergence follows from (ECI5.3). Thus this is a whole-module equality, not an extension inferred from finite-support density.

The local formula (ECI4.5) agrees with (ECI6.5) through the exact differentiated functional equation
\[
\zeta'(1-s)=\frac{\chi'(s)}{\chi(s)^2}\zeta(s)
-\frac{1}{\chi(s)}\zeta'(s).
\tag{ECI6.6}
\]
The first term retains the full original multiplicity and is zero only after passage to that actual jet quotient; the second term retains the minus sign and all unit derivatives. This proves the relation between the source involution, the \(\zeta'\) trace map and the residue-dual involution, without replacing the original function by its completion or treating \(\chi\) as a global entire multiplier.

## ECI7. The normal class module maps to the same existing residue receiver

Use the actual inverse translation \(U:\mathscr C_+\to\mathscr C\). Define
\[
\mathsf S_+=\mathsf S_MU:\mathscr C_+\to\mathcal H_{\rm res}.
\tag{ECI7.1}
\]
For \(X\in\mathcal Q_+\), its precise evaluation is
\[
(\widehat\iota\mathsf S_+k)(UX)
=\sum_\rho m_\rho X(\rho+1)\overline{k(\rho^\#+1)}.
\tag{ECI7.2}
\]
Thus it is a map from the actual cyclic normal-extension or boundary module, by (ECI0.3), to the original strong residue receiver, tested through the exact coordinate map \(U\). Its kernel is
\(\mathfrak r_+/\mathfrak a_+\), where \(\mathfrak r_+=V\mathfrak r\). All zero values and all original multiplicities in the normal module are retained.

For the normal involution and arbitrary multipliers,
\[
\mathsf S_+\mathsf K_3=\mathsf K_{\rm res}\mathsf S_+,
\qquad
\widehat\iota\mathsf S_+(bk)
=m_{U(b^{\#_3})}'\widehat\iota\mathsf S_+(k).
\tag{ECI7.3}
\]
These follow from \(U\mathsf K_3=\mathsf K_1U\), \(U(bk)=(Ub)(Uk)\), and (ECI6.4). Specializing to \(b(\lambda)=a^\lambda\) retains
\[
\boxed{\mathsf S_+D_a^+=a\widehat T_a\mathsf S_+,
\qquad
\widehat\iota\mathsf S_+D_a^+
=a^2(T_{1/a})'\widehat\iota\mathsf S_+.}
\tag{ECI7.4}
\]
Here \(\widehat T_a\) is the existing residue action from GTR10, satisfying \(\widehat\iota\widehat T_a=a(T_{1/a})'\widehat\iota\). The extra factor in (ECI7.4) is the actual normal translation factor in (ECI2.4).

There is an exact translated primal map as well:
\[
\mathsf P_+=V\mathsf P_MU
=(L_+-1)^{-2}
M_{(\lambda-1)^2\zeta'(2-\lambda)}\mathsf C.
\tag{ECI7.5}
\]
The only derivative pole being removed is at \(\lambda=1\), and the multiplier's value there is \(-1\). This point is outside the actual normal divisor, so the inverse of \(L_+-1\) exists on \(\mathscr C_+\) by NEA7. Every full block formula is (ECI6.3) translated by one, with the local coordinate unchanged. No additional spectrum is inserted.

## ECI8. Normal residue duality and the distinction from geometric normal transfer

The translated residue pairing on actual finite-support normal classes is
\[
\mathcal R_+(X,Y)=\sum_{\rho}
\operatorname{Res}_{\lambda=\rho+1}
\frac{X(\lambda)Y(3-\lambda)}{\zeta(\lambda-1)}\,d\lambda.
\tag{ECI8.1}
\]
It is a coordinate transport of the original residue, not a replacement arithmetic function:
\[
\mathcal R_+(VF,VG)=\mathcal R(F,G).
\tag{ECI8.2}
\]
Proof: put \(\lambda=s+1\). The denominator becomes original \(\zeta(s)\), the second numerator becomes \(G(1-s)\), and \(d\lambda=ds\). Both multiplicities and positive local residue orientations are unchanged. The completion for its corresponding bounded-set seminorms is therefore topologically isomorphic to the existing \(\mathcal H_{\rm res}\), via the extension of \(V\); this follows because \(V,U\) on the test quotients carry bounded sets to bounded sets. No extra completion is needed in (ECI7.1).

The full normal functional equation is
\[
\zeta(\lambda-1)=\chi(\lambda-1)\zeta(2-\lambda).
\tag{ECI8.3}
\]
Consequently the normal residue-dual involution has local jets
\[
Y(\lambda)\longmapsto
-\chi(2-\lambda)Y^{\#_3}(\lambda).
\tag{ECI8.4}
\]
This is exactly (ECI4.5) translated, with its full Gamma, sine, power and derivative data from (ECI4.3). Its completed action is the same transported continuous dual involution, not an assumed entire multiplier.

The normal pairing's full dilation factor is
\[
\mathcal R_+(D_a^+X,D_a^+Y)=a^3\mathcal R_+(X,Y),
\quad
W_+(D_a^+X,Y)=W_+(X,a^3D_{1/a}^+Y),
\tag{ECI8.5}
\]
where \(W_+\) is the exact value sum in (ECI7.2). In the residue integrand the multiplier is \(a^\lambda a^{3-\lambda}=a^3\). In the value formula the equality follows from \(\overline{3-\overline\lambda}=3-\lambda\). These are whole-divisor identities.

For \(a=n\) a positive integer, GTR's actual degree-\(n\) covering has normal pullback \(aT_a\) in the original source coordinate and transfer with inverse coefficients \(T_{1/a}\). For general \(a>0\), these same expressions remain the specified coefficient operators; no covering with nonintegral degree is asserted. Transporting both coefficient operators gives
\[
V(aT_a)U=D_a^+,
\qquad V T_{1/a}U=aD_{1/a}^+.
\tag{ECI8.6}
\]
Their product remains \(aI\). Therefore the normal Weil/residue adjoint operator in (ECI8.5) is precisely \(a^2\) times the displayed normal coefficient transfer, and, for positive integer \(a=n\), precisely \(n^2\) times the actual geometric normal transfer. The three identities (ECI7.4), (ECI8.5) and (ECI8.6) agree with each other; none permits deletion of that factor. This calculation concerns the degree-shifted normal class module. It does not assign its \(a^3\) factor to the original degree-one Weil pairing, whose factor remains \(a\).

## ECI9. The separator's zero and identity actions remain different after translation

FOD and NEA prove
\[
c=0\text{ on }\mathscr C_+,
\qquad c=1\text{ on }\mathscr C,
\qquad c\delta=0.
\tag{ECI9.1}
\]
The two actions are compatible with the actual translation because
\[
(Uc)(s)=c(s+1)=1-E(s)\in\mathfrak a,
\tag{ECI9.2}
\]
whereas \(c(s)-1\in\mathfrak a\). Thus translating the annihilation equation on the normal class module gives multiplication by \(Uc\), not multiplication by \(c\), on the original module. Explicitly
\[
\mathsf S_+(ck)=\mathsf S_M((Uc)(Uk))=0,
\qquad
\mathsf S_M(ch)=\mathsf S_M(h).
\tag{ECI9.3}
\]
The first vanishes because its argument is zero in \(\mathscr C\); the second retains the entire original trace. These equations are the exact connecting map between the two assertions. They do not identify their source classes or their scalar actions. In particular the normal annihilation \(c\delta=0\), which proves the actual lift in FOD7/NEA10, does not become an annihilation of original Weil values by silently removing the coordinate translation.

## ECI10. What the extension-class residue maps do to the positive-adjoint defect

On the established value Hilbert space retain GTAH's bounded operator
\[
(D_ax)_\rho=(a^{\overline\rho}-a^{1-\rho})x_\rho,
\qquad a>1.
\tag{ECI10.1}
\]
It acts on this explicitly constructed value space, not as an asserted entire multiplier on all of \(\mathscr C\). RTT6.2 proves an injective continuous anti-linear map
\[
\mathsf A:H\to\mathcal H_{\rm res},\qquad
(\widehat\iota\mathsf Ay)(F)=\langle EF,Jy\rangle,
\qquad\mathsf S=\mathsf A E.
\tag{ECI10.2}
\]
The new extension-class map restricts to exactly this map on \(\mathcal Q\subset\mathscr C\), by (ECI5.1). Every finite value vector is attained there by the actual global isolators. Consequently this extension of the domain loses no original value direction, and
\[
\mathsf A D_a^*D_a=0\quad\Longleftrightarrow\quad D_a^*D_a=0.
\tag{ECI10.3}
\]
The reverse implication is immediate; the forward implication is injectivity applied to each vector. Positivity of the Hilbert norm then gives equivalence to \(D_a=0\), exactly as in GTAH6.7.

There is a specific full-source test for every actual zero, avoiding an unproved nonholomorphic multiplier lift. Fix \(\rho\) and let \(e_{\rho,0}\) be its global full-jet isolator, viewed in \(\mathcal Q\subset\mathscr C\). Put
\[
d_\rho^2=|a^{\overline\rho}-a^{1-\rho}|^2,
\qquad h_\rho=d_\rho^2 e_{\rho,0}\in\mathcal B\subset M.
\tag{ECI10.4}
\]
Then \(E[h_\rho]=D_a^*D_a E[e_{\rho,0}]\), and evaluation on the other actual isolator gives
\[
(\widehat\iota\mathsf S_M[h_\rho])(e_{\rho^\#,0})
=m_\rho d_\rho^2.
\tag{ECI10.5}
\]
This is nonzero precisely when the displayed scalar defect is nonzero. It quantifies over the actual divisor and does not postulate an off-line zero. Translating \(h_\rho\) to \(Vh_\rho\in\mathscr C_+\) gives the same result through \(\mathsf S_+V=\mathsf S_M\). Thus neither the extension-class involution nor this residue comparison kills a nonzero positive-adjoint defect. The statement is established by the actual maps and witnesses, not by treating an RH-equivalent criterion as an achievement.

For every actual two-point orbit, the signed test also remains \(e_{\rho,0}-e_{\rho^\#,0}\), with original Weil value \(-2m_\rho\) as calculated in GTAH6.5. Both new class-module maps restrict to that same residue value. The higher-jet kernel (ECI5.7) is the exact information they remove; it contains no nonzero isolated value vector.

## ECI11. Original factors, class actions and category scope

Every source factor used above remains
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad
F_+(\lambda)=\frac{(\lambda-1)(\lambda-2)}8
\pi^{-(\lambda-1)/2}\Gamma((\lambda-1)/2)\zeta(\lambda-1).
\tag{ECI11.1}
\]
Their endpoints are \(F_0(0)=F_0(1)=F_+(1)=F_+(2)=1/8\), and the original trivial-zero comparison is
\[
F_0(-2r)=F_+(1-2r)
=\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r),\quad r\ge1.
\tag{ECI11.2}
\]
The function in every residue denominator remains \(\zeta\) in its explicitly related coordinate. Its arithmetic is still
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},
\qquad -\frac{\zeta'}\zeta(s)=\sum_p\sum_{k\ge1}(\log p)p^{-ks},
\quad\Re s>1.
\tag{ECI11.3}
\]
On the original test subspace the new trace maps are exactly RTT's map, so RTT9's complete prime, Gamma, endpoint and finite trivial-divisor identity remains unchanged. Formula (ECI5.1) on a general polynomial-growth multiplier is proved directly as a continuous spectral functional; no extension of the prime explicit formula to an unspecified larger test class is inferred.

The class-module action above is multiplication, or central postcomposition on the actual cyclic extension classes. As FOD7 and NEA10 prove, conjugation of the equivariant boundary by dilation fixes that boundary. The scalar factors in ECI2 and ECI8 concern the specified multiplier and pairing actions; they are not reassigned as conjugation weights of \(\delta\). Likewise the semilinear involutions of ECI1 are explicit coefficient and row operations, not an unproved identification with ordinary or étale Verdier duality. The residue-dual comparison they do supply is (ECI4.1)–(ECI4.5), and its relation to the actual extension modules is (ECI6.5) and (ECI7.3).

## ECI12. Exact comparison with the Gaussian source embedding

The complete ECR0–ECR7 derivation in `EXTENSION_CLASS_TO_ORIGINAL_RESIDUE.md` was read for this comparison. It constructs, for each \(t>0\), the entire source multiplier \(g_t(s)=e^{ts^2}\) and the injective \(M\)-map
\[
b_t:\mathscr C\to\mathcal Q,\qquad[h]\mapsto[g_t h],
\quad j:\mathcal Q\hookrightarrow\mathscr C,
\quad jb_t=m_{g_t}.
\tag{ECI12.1}
\]
Its coefficient-to-source estimate retains \(|g_t(\sigma+i\gamma)|=e^{t(\sigma^2-\gamma^2)}\), so multiplying a polynomial-growth representative by \(g_t\) really lands in \(\mathcal B\). The target and purpose differ from the direct trace functional of ECI5: \(b_t\) reaches the actual source quotient and hence the positive value Hilbert space, while (ECI5.4) reaches its strong dual receiver. For example the value sequence of \([1]\in\mathscr C\) is not in \(H\), since there are infinitely many actual zeros, but (ECI5.1) at \(h=1\) is a continuous functional on every original rapid test. There is no identification of those two receiving spaces.

The exact comparison is
\[
\boxed{\mathsf S b_t=\mathsf S_M m_{g_t}:\mathscr C\to\mathcal H_{\rm res}.}
\tag{ECI12.2}
\]
Indeed \(\mathsf S_Mj=\mathsf S\) by (ECI5.1); compose this equality with \(b_t\) and use (ECI12.1). Explicitly both sides evaluated against \(F\) give
\(\sum_\rho m_\rho F(\rho)\overline{g_t(\rho^\#)h(\rho^\#)}\), with absolute and strong convergence already proved. Because \(g_t\) is a unit in each actual local ring, both maps have the same value-zero kernel \(\mathfrak r/\mathfrak a\). This is not a claim that \([g_t]\) is invertible in the global multiplier quotient; ECR1 proves it is not.

The embedding also has an exact involution factor which should be retained in any dual comparison:
\[
g_t^{\#_1}(s)=e^{t(1-s)^2}=d_t(s)g_t(s),
\qquad d_t(s)=e^{t(1-2s)},
\qquad d_t^{\#_1}=d_t^{-1}.
\tag{ECI12.3}
\]
Both \(d_t\) and its inverse are in \(M\). Consequently
\[
\mathsf K_1 b_t=m_{d_t}b_t\mathsf K_1.
\tag{ECI12.4}
\]
This is equality on full source jets: it follows from multiplication of the entire functions before quotient. No coordinate or coefficient has been normalized. Conjugation alone commutes with \(b_t\), since \(g_t\) has real Taylor coefficients; reflection alone satisfies the same \(d_t\) factor as (ECI12.4).

Write \(\mathsf S_t=\mathsf S b_t\), as in ECR4. Combining (ECI6.5), (ECI12.4), and the multiplier covariance gives the complete dual version
\[
\widehat\iota\mathsf K_{\rm res}\mathsf S_t
=m_{d_t^{-1}}'\widehat\iota\mathsf S_t\mathsf K_1.
\tag{ECI12.5}
\]
The inverse factor arises from the involution on the multiplier, not an inverse of \(g_t\). For the normal class module the transported source Gaussian is \((Vg_t)(\lambda)=e^{t(\lambda-1)^2}\), and its corresponding factor is \((Vd_t)(\lambda)=e^{t(3-2\lambda)}\). These follow directly from (ECI2.3), retaining the actual shift instead of choosing a different normal Gaussian.

For two class-module inputs, (ECI12.2) gives precisely ECR's full trace
\[
\widehat{\mathcal R}(b_th,\mathsf S_tk)
=\sum_\rho m_\rho e^{t\{\rho^2+(1-\rho)^2\}}
h(\rho)\overline{k(\rho^\#)}.
\tag{ECI12.6}
\]
The positive value receiver instead has the actual modulus weight \(e^{2t(\sigma^2-\gamma^2)}\). The two weights are not substituted for each other. ECR4 proves the former's complete original prime/Gamma/endpoint formula; ECR5 proves the latter's positive defect formula through its stated Hilbert-space map. Thus the canonical residue map here and ECR's Gaussian source embedding agree by an exact morphism while preserving their different domains and purposes.

## ECI13. Exact receiving result

The new cyclic modules now have complete involution maps, including their full jets, translation, and actual row origins. Their original and normal involutions use \(1-s\) and \(3-\lambda\), respectively, with the exact translation diagram (ECI2.3). Their residue-dual involutions retain the functional-equation units and minus signs (ECI4.5), (ECI8.4). Every polynomial-growth extension class has a canonical, explicitly convergent map to the original strong residue receiver, extending RTT without changing its kernel on original tests. Its covariance retains every factor \(a\), \(a^2\), and \(a^3\) in the different specified domains.

This calculates the proposed use of the new annihilator modules rather than merely naming their resemblance to duality. The normal boundary's annihilation and the unchanged original positive-adjoint defect coexist through the proved translation (ECI9.2). The remaining attempt toward the active goal must supply additional source information controlling that retained defect; the independent positive source-pairing calculation can now use the exact involution and degree dictionary here. No pure weight, positive original Weil form, or RH conclusion is assumed.

Proof sources actually read for this continuation: `../tau_weight_cohomology_20260924/CC_FULL_SOURCE_OBSTRUCTION_DECOMPOSITION.md`, FOD0–FOD8; `../tau_weight_cohomology_20260924/CC_NORMAL_EXTENSION_ANNIHILATOR.md`, NEA0–NEA10; `EXTENSION_CLASS_TO_ORIGINAL_RESIDUE.md`, ECR0–ECR7; current construction/prerequisite instructions; and the existing checked RTT, GSR, GTAH and GMS maps cited at their equation locators above. Human-source context remains the original Connes–Consani §5 construction and Deligne's Weil II §3.6, with their source-reading coverage recorded in those receiving proofs. This continuation makes no new complete-reading claim for those human papers and no public release claim.
