# Independent raw-derivative, Gamma-factor and supported-sign check

24 September 2026. Exact independent verification OEC0–OEC5 of ORE5.5–ORE5.8 and ORE8.8–ORE8.10 against the original Mellin lifts MCL. The formulas checked here are valid with their stated character twist and cochain convention. No change to ORE is made by this note.

## OEC0. Objects and scope actually checked

[ORIGINAL_RESTRICTION_EXTENSION_AND_DELIGNE_CROSS.md](ORIGINAL_RESTRICTION_EXTENSION_AND_DELIGNE_CROSS.md), ORE0–ORE10, was read completely. This bounded check concerns the specified residue transport and supported degree-two formulas. ORE4's separate source-jet independence argument was corrected before integration using the full proof [MCL4](ORIGINAL_MELLIN_CHARACTER_LIFTING.md); this note neither edits that file nor uses its earlier independence argument.

The controlling source remains the user's \(Z_0,Z_1/\tau,Z_2\), the supplied source operations B1–B5, and the retraction of \(\tau\) addition, with complete corpus references in MCL0. All calculations here occur in the already constructed complex receiving spaces after the retained arithmetic reconstruction. The original \(\zeta\), the factor2 in the Connes–Consani summation, all raw derivative factorials, the reflected variable, Gamma factors, orientation signs and source-faithful closed terms are retained.

Human-source provenance is Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), for the original restrictions and Fourier geometry, and Pierre Deligne, [*La conjecture de Weil. II*, §3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/), for the target lifting mechanism. The new ORE formulas are programme derivations, not formulas attributed to either human source. The full original continuous maps and their prerequisites were proved in MCL1–MCL10, GZR and UOS; no new literature equivalence is presumed here.

Fix an actual nontrivial original zero \(\rho\) of multiplicity \(m\), put
\[
 b=1-\rho,\qquad r\ge1,\qquad
 q(X)=(X-b)^r,\qquad d=\min(m,r).
\]
The actual operator on the twisted duals is
\[
 G=1-K,\qquad K=L^t,\qquad
 N=G-b=-(K-\rho).
 \tag{OEC0.1}
\]
The ordinary transpose has character \(a^\rho\); the contragredient followed by \(\chi_{\rm dil}(a)=a\) has character \(a^{1-\rho}=a^b\). Thus the original raw derivatives
\[
 A_n=\partial_z^nM_{A,z}|_\rho,\qquad
 S_n=\partial_z^nM_{S,z}|_\rho
\]
satisfy
\[
 (K-\rho)A_n=nA_{n-1},\qquad
 NA_n=-nA_{n-1},
 \tag{OEC0.2}
\]
and the identical formulas on \(S_n\). Every sign below uses the second equation for ORE's chosen representation.

## OEC1. The lift and the residue inverse with all maps typed

Retain the exact original expansions
\[
 \zeta(\rho+t)=t^m u_\rho(t),\qquad
 u_\rho(0)=\frac{\zeta^{(m)}(\rho)}{m!},\qquad
 \frac1{2u_\rho(t)}=\sum_{k\ge0}v_kt^k.
 \tag{OEC1.1}
\]
MCL5 proves that ORE's raw lift is exactly
\[
 \alpha_j
 =j!\sum_{k=0}^j\frac{v_k}{(m+j-k)!}A_{m+j-k},
 \qquad\Sigma'\alpha_j=S_j.
 \tag{OEC1.2}
\]
Indeed \(v_k=v_\rho^{(k)}(0)/k!\) in MCL5.7; replacing its index \(k\) by \(j-k\) gives (OEC1.2) with the full factorials unchanged.

Let \(i=\pi':Y=\chi_{\rm dil}Q'\to\widetilde A=\chi_{\rm dil}A'\).
For \(0\le h<m\), \(A_h/h!\) annihilates the original summation image, so the actual element on which the residue inverse acts is
\[
 \eta_h=i^{-1}(A_h/h!)\in Y.
\]
This types ORE5.5 explicitly: the functional first enters \(Y\) by the proved annihilator identification; no inverse \(D^{-1}\) on all of \(A'\) is asserted.

At the reflected zero put
\(\zeta(b+t)=t^m u_b(t)\). The formula is
\[
 \boxed{
 j_b(D^{-1}\eta_h)(t)
 =(-1)^h u_b(t)t^{m-1-h}\pmod{t^m}.
 }
 \tag{OEC1.3}
\]
Here \(D=D_\zeta\) is the original residue map with denominator \(\zeta(s)\), not the auxiliary \(F_*(s)\). To check it directly, use the actual primary representative whose germ is the right side and whose other primary germs vanish. The retained isolator theorem constructs that global representative. Its contribution against a test \(F\) is the residue at \(t=0\) of
\[
 \frac{(-1)^h u_b(t)t^{m-1-h}F(\rho-t)}
      {t^m u_b(t)}\,dt
 =(-1)^h t^{-h-1}
   \sum_{k\ge0}\frac{(-1)^kF^{(k)}(\rho)}{k!}t^k\,dt .
\]
The residue selects \(k=h\), with product of signs \((-1)^{2h}=1\), and equals \(F^{(h)}(\rho)/h!\). This verifies every sign and the raw-derivative factorial. No factor \(1/8\), Gamma multiplier, or completed denominator has entered this original residue map.

## OEC2. Transport the full connecting class and retain its Gamma germ

For \(0\le j<r\), repeated use of (OEC0.2) in (OEC1.2) gives
\[
 N^r\alpha_j
 =(-1)^rj!\!
 \sum_{\substack{0\le k\le j\\h=m+j-k-r\ge0}}
 \frac{v_k}{h!}A_h.
 \tag{OEC2.1}
\]
Every displayed \(h\) is \(<m\), since \(j<r\). Thus it is in \(iY\), and
\(\delta_q(S_j)=[i^{-1}N^r\alpha_j]\).

Apply (OEC1.3) term by term. For a retained summand its sign is
\[
 (-1)^r(-1)^h=(-1)^{m+j-k}
               =(-1)^{m+j}(-1)^k,
\]
and its exponent is
\[
 m-1-h=r-1-j+k.
\]
Consequently
\[
 (D\bmod q)^{-1}\delta_q(S_j)
 =
 \left[
 (-1)^{m+j}j!\,u_b(t)t^{r-1-j}
 \sum_{k=0}^jv_k(-t)^k
 \right]_{\mathbb C[t]/(t^d)} .
 \tag{OEC2.2}
\]
This writes all \(0\le k\le j\), including any excluded \(h<0\) terms, only after the following exact check: such an index has
\(r-1-j+k\ge m\), hence contributes zero modulo \(t^d\), since \(d\le m\). Therefore none of these terms has been removed outside the stated quotient.

For each new index \(k>j\), the exponent \(r-1-j+k\) is at least \(r\), hence at least \(d\). This proves that the finite series in (OEC2.2) may be compared with the full convergent germ modulo that exact ideal. The original functional equation gives
\[
 \zeta(s)=\chi_\zeta(s)\zeta(1-s),\qquad
 \chi_\zeta(s)=
 \pi^{s-1/2}
 \frac{\Gamma((1-s)/2)}{\Gamma(s/2)} .
\]
Substituting \(s=b+t\) retains the reflected displacement \(-t\):
\[
 u_b(t)=(-1)^m\chi_\zeta(b+t)u_\rho(-t).
 \tag{OEC2.3}
\]
The factor \((-1)^m\) comes from \((-t)^m\), and is essential. Multiplication by the full reciprocal series now gives
\[
 u_b(t)\sum_{k\ge0}v_k(-t)^k
 =\frac{(-1)^m}{2}\chi_\zeta(b+t).
\]
Substitute this identity into (OEC2.2), keeping the two separate \((-1)^m\) factors until their product is evaluated. The result is
\[
 \boxed{
 (D\bmod q)^{-1}\delta_q(S_j)
 =
 \left[
 \frac{(-1)^j j!}{2}\,
 t^{r-1-j}\,
 \pi^{b+t-1/2}
 \frac{\Gamma((1-b-t)/2)}{\Gamma((b+t)/2)}
 \right]_{\mathbb C[t]/(t^d)} .
 }
 \tag{OEC2.4}
\]
This verifies ORE5.6 and, at \(j=r-1\), ORE5.7. Every derivative of the Gamma-ratio germ of degree below \(d\) is retained, not only its value at zero.

The quotient transport \(D\bmod q\) is legitimate independently of an inverse on all \(Y\). Its surjectivity follows from polynomial divisibility of \(C_\zeta=Y/DQ\): for \(y\in Y\), solve \(q[c]=[y]\), choose a representative \(y_1\), and write \(y-qy_1=Dx\). For injectivity, \(Dx=qy\) implies \(q[y]=0\) in \(C_\zeta\), hence \(y=Dx_1\) by the same proved polynomial injectivity; then \(x=qx_1\). This is the exact quotient isomorphism used in (OEC2.2)–(OEC2.4), with no algebraic surjectivity claim for \(D\).

The function \(\chi_\zeta(b+t)\) is holomorphic with nonzero constant term on the chosen local domain inside the critical strip. Multiplication by it is therefore invertible on this finite quotient. The images of \(S_0,\ldots,S_{r-1}\) in (OEC2.4) are nonzero scalar multiples of that common unit times the monomials \(t^{r-1},\ldots,t^0\). MCL4 proves these source jets independent. Exactly the monomials of exponent \(<d\) remain, giving
\[
 \operatorname{rank}\delta_q=d,\qquad
 \ker\delta_q=
 \begin{cases}
 0,&r\le m,\\
 \operatorname{span}(S_0,\ldots,S_{r-m-1}),&r>m.
 \end{cases}
 \tag{OEC2.5}
\]
This verifies ORE5.8 with the complete kernel, not only the top class.

## OEC3. Independent derivation of the supported minus sign and half-sum

Retain UOS's actual complexes in degrees \(-1,0,1,2\):
\[
 K_\zeta=[P\xrightarrow{-d}A
 \xrightarrow{\pi'D\pi}\widetilde A
 \xrightarrow{d'}\chi_{\rm dil}P'],
\]
\[
 \mathcal L_\zeta=[P\xrightarrow{-d}A
 \xrightarrow{(\pi'D\pi,-\pi'D\pi)}\widetilde A^2
 \xrightarrow{d_Z'}\chi_{\rm dil}P'].
\]
The actual cone map \(\mathcal J:K_\zeta\to\mathcal L_\zeta\) is identity except for its degree-one anti-diagonal. The original term
\[
 H'=S'\oplus(\mathbb C^4)'\oplus V_{\rm extra}'
\]
retains all four endpoint functionals and both complete closed extra dual copies.

For the resolution \(\mathbb C[X]\xrightarrow{q}\mathbb C[X]\), the Hom cochain is
\[
 \mathscr H^n(K)=K^n\oplus K^{n-1},\qquad
 \partial(u,v)=
 (d_Ku,d_Kv-(-1)^nq(G_K)u).
 \tag{OEC3.1}
\]
This sign follows from \(d_{\rm Hom}f=d_Kf-(-1)^nf\,d_{\rm resolution}\), applied to its two components. In degree one the second component is \(d_Kv+qu\); in degree two it is \(d_Kv-qu\).

Let \(\eta\in\ker q(G_S)\). Extend it to the plus-chart Schwartz coordinate
\[
 u=((\eta,0,0),(0,0,0),0)\in\chi_{\rm dil}P'.
\]
Its endpoints, minus-chart component and complete extras are zero. Restriction to the Fourier graph is exactly \((\eta,0)\in\chi_{\rm dil}H'\), and the plus-chart action agrees with that graph coordinate, so \(qu=0\). Thus \((u,0)\) is a degree-two Hom cocycle for \(K_\zeta\).

Choose an actual \(\alpha\in\widetilde A\) with \(\Sigma'\alpha=\eta\); MCL provides the explicit choices for all \(S_j\). In the supported target put \(w=(\alpha,0)\). Its differential is
\[
 d_Z'w=(r_+'\alpha,0,0)=u.
\]
The plus restriction is \(r_+'(\alpha)=(\Sigma'\alpha,0,0)\), with its two endpoint zeros retained. Formula (OEC3.1) therefore gives
\[
 \partial^1(w,0)=(u,(q\alpha,0)).
\]
Subtracting this exact boundary from the image of \((u,0)\) leaves
\[
 \boxed{(0,(-q\alpha,0)).}
 \tag{OEC3.2}
\]
There is no further dual differential sign at this point: it has already entered (OEC3.1).

Write \(q\alpha=iy_\alpha\). Under the exact UOS identification of degree-one cohomology,
\[
 [(\lambda_+,\lambda_-)]
 \longmapsto
 \left(\left[\frac{\lambda_+-\lambda_-}{2}\right],
             \frac{\lambda_++\lambda_-}{2}\right)
 \in C_\zeta\oplus Y,
\]
the pair in (OEC3.2) is
\[
 \left([-y_\alpha/2],-y_\alpha/2\right).
 \tag{OEC3.3}
\]
Its first component vanishes only after taking the proved quotient
\(C_\zeta/qC_\zeta=0\). The second component is
\(-[y_\alpha]/2=-\delta_q(\eta)/2\) in \(Y/qY\).
Endpoint and extra functionals are direct degree-two subcomplex coordinates on both sides, and \(\mathcal J\) acts by identity there. Thus the complete induced map is
\[
 \boxed{
 H^2\operatorname{RHom}(V_q,\mathcal J)(\eta,e)
 =\left(-\frac12\delta_q(\eta),e\right).
 }
 \tag{OEC3.4}
\]
This verifies ORE8.8 and ORE8.9 on their exact degrees and complete terms.

Combining (OEC3.4) with (OEC2.4) proves
\[
 \boxed{
 (D\bmod q)^{-1}
 \big(H^2\operatorname{RHom}(V_q,\mathcal J)(S_j,0)\big)_1
 =
 \left[
 \frac{(-1)^{j+1}j!}{4}\,
 t^{r-1-j}\,
 \pi^{b+t-1/2}
 \frac{\Gamma((1-b-t)/2)}{\Gamma((b+t)/2)}
 \right]_{\mathbb C[t]/(t^d)} .
 }
 \tag{OEC3.5}
\]
The first \(1/2\) is from the original two-sign summation. The second is the supported half-sum. The extra minus sign is from subtracting the degree-one Hom boundary. These are three distinct sources, all evaluated explicitly. This verifies ORE8.10.

## OEC4. Ordinary versus twisted convention, and Fourier compatibility

If one instead uses the ordinary transpose \(K=L^t\) and relation
\((K-\rho)^r=0\), the same chosen lift \(\alpha_j\) has connecting representative
\[
 (K-\rho)^r\alpha_j=(-1)^rN^r\alpha_j.
\]
Their underlying kernel quotients have the same subspaces because multiplication by \((-1)^r\) does not change the image of the operator. Consequently the ordinary-transpose representative transported through the same underlying \(D\) has the exact formula
\[
 \left[
 \frac{(-1)^{r+j}j!}{2}
 t^{r-1-j}\chi_\zeta(b+t)
 \right]_{\mathbb C[t]/(t^d)} .
 \tag{OEC4.1}
\]
This is a comparison of specified conventions, not a correction to ORE. ORE uses \(G=1-K\) throughout, so its (OEC2.4) sign is the required one.

The original residue map intertwines
\[
 DL_Q=(1-K_Q)D,
\]
not \(DL_Q=K_QD\). Thus retaining the reflected parameter \(b=1-\rho\) is necessary in the quotient transport. The whole real action on the raw derivatives is
\[
 \mathcal U_a A_j
 =a^{1-\rho}\sum_{k=0}^j\binom jk(-\log a)^{j-k}A_k.
\]
The quotient germ \(x(t)\in\mathbb C[t]/(t^d)\) is acted on by
\[
 a^{b+t}x(t)
 =a^b\left(\sum_{n=0}^{d-1}
 \frac{(\log a)^n}{n!}t^n\right)x(t)\pmod{t^d}.
 \tag{OEC4.2}
\]
Both action formulas follow from the retained intertwiner, including the opposite signs in the reflected derivative coordinate.

The Fourier comparison in MCL8 has
\[
 \kappa(z)=\frac{\zeta(1-z)}{\zeta(z)}
 =\pi^{1/2-z}\frac{\Gamma(z/2)}{\Gamma((1-z)/2)}.
\]
Since \(b=1-\rho\),
\[
 \chi_\zeta(b+t)=\kappa(\rho-t).
 \tag{OEC4.3}
\]
Hence the Gamma germ used in ORE is precisely the full reflected Mellin Fourier multiplier, with the displacement \(-t\), not an independently chosen factor. At \(r=1,j=0\), (OEC2.4) gives \(\chi_\zeta(b)/2\), while direct raw calculation gives
\[
 D^{-1}\left(-\frac{m}{2\zeta^{(m)}(\rho)}
             i^{-1}A_{m-1}\right)
 \equiv
 \frac{(-1)^m m!}{2\zeta^{(m)}(\rho)}u_b(0)
 =\frac{\chi_\zeta(b)}2\pmod t.
\]
This independent first-order check keeps the raw factorial and confirms the sign for every multiplicity \(m\). The supported image is its negative half, \(-\chi_\zeta(b)/4\), in agreement with (OEC3.5).

There is also a direct check of every prime logarithm in the transported matrix. Put \(\ell=\log a\). Applying (OEC2.4) to the complete action on \(S_j\) gives
\[
 \begin{aligned}
 a^b\sum_{k=0}^j\binom jk(-\ell)^{j-k}
   \frac{(-1)^k k!}{2}t^{r-1-k}\chi_\zeta(b+t)
 &=
 a^b\frac{(-1)^j j!}{2}t^{r-1-j}
   \left(\sum_{h=0}^j\frac{(\ell t)^h}{h!}\right)
   \chi_\zeta(b+t)\\
 &\equiv
 a^{b+t}\frac{(-1)^j j!}{2}
   t^{r-1-j}\chi_\zeta(b+t)\pmod{t^d}.
 \end{aligned}
 \tag{OEC4.4}
\]
For the last equality, every added term \(h>j\) has total degree at least \(r\ge d\). Thus the full action agrees at every \(a>0\), in particular at every original prime, without deriving a global group assertion only from its generator. Multiplication by the additional supported scalar \(-1/2\) preserves this exact equality.

## OEC5. Verification result and exact scope

No correction to ORE5.5–ORE5.8 or ORE8.8–ORE8.10 is required. Their full factors, signs, Gamma derivatives and support placements agree with the raw Mellin lifts MCL.

Two details made explicit here are useful when carrying the formulas forward. First, the \(A_h/h!\) entering \(D^{-1}\) means its actual image \(i^{-1}(A_h/h!)\) in \(Y\), justified by annihilation of the summation image. Second, replacing the finite reciprocal sum by its full germ occurs only modulo \(t^d\), with both sets of discarded terms proved to lie in that exact ideal in OEC2.

The verified supported class is \(-\delta_q/2\), in degree two of the actual resolved cone map. The unshifted character connecting class, the contragredient twisted class, and the residue-cone quotient map remain different specified maps, with their exact comparisons displayed above. None of these formulas identifies a receiving constant with primitive \(Z_1/\tau\), removes an endpoint or extra closed copy, assigns a numerical source weight, or proves RH.
