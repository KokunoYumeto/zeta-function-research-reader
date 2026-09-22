# The original kernel pencil, canonical section maps, and the coupled physical current

Independent derivation, 22 September 2026. This proof receives Section 3, KP1–KP13, of the supplied Arithmetic Probe Mass Integration package. The chain construction, filtration indices and projective splitting repeat established 021 BD4–7; they are proved here for completeness and are not claimed as new. The new connecting results are PEN5–PEN6 and PEN9–PEN13: canonical section maps with the original physical action, the exact distinction between two short-sector metrics, and the complete coupled current after their respective minima.

## PEN1. Original source, observation and established finite bounds

Retain \(k\equiv1\pmod4\), \(k\ge17\), \(q=(k+1)^2\), \(m=8k-16\), \(n=q-m\), and
\[
\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta,\qquad
0<\delta<1/2,\quad\gamma>2,
\]
\[
Q_k(y)=\prod_{a,b=0}^k(y-\omega_{ab}),\quad
E=\mathbb C[y]/Q_k,\quad M[p]=[yp],\quad
\mathscr A=kI/2+iM.
\]
The original \(\Lambda:E\to B\) is onto, \(K=\ker\Lambda\) has dimension \(m\), and \(I_K:\mathbb C^m\to E\) is its given frame. The roots are distinct and nonzero, by their separate real and imaginary coordinates and odd \(k\). Thus \(M\) is invertible. At each original cutoff, \(G_N>0\) is the complete attained source metric. Write
\[
H_{K,N}=I_K^*G_NI_K,\quad
Q_N=(\Lambda G_N^{-1}\Lambda^*)^{-1},\quad
L_N=G_N^{-1}\Lambda^*Q_N,\quad
\mathcal R f=f_{q-1}+f_q-f_{2q-1}-f_{2q}.
\]

The original period remains in the established size-five orbit and corner domain OC71–73, \(|\varpi|\ge R_{\rm corner}^{\rm explicit}\). The complete coefficient product and all phases are retained. The original finite-height condition used there is \(\gamma\ge1000\delta\), valid for an actual hypothetical offcritical zeta quartet by the retained Platt–Trudgian theorem. The complete original conductor has at most 81 supported distinct shifts and factors through \(\Lambda\); 021 BD2–3 prove
\[
K_j=\bigcap_{r=0}^j\ker(\Lambda M^r),\quad
K_d=0\text{ for some }d\le80,\qquad t_8:=\dim K_8\le128. \tag{PEN1}
\]
We take \(d\) to be the least such index, rather than requiring it to equal the possibly larger support bound \(J-1\).

The needed full-source inequality has a completed proof in 021 BD11, independently of the received \(Z_{k,1}\) expression:
\[
e^{-E_k}G_{q-1}\preceq G_N\preceq G_{q-1},\qquad q-1\le N\le2q,\qquad E_k=O_h(q). \tag{PEN2}
\]
Its finite constants are
\[
R=k\sqrt{\delta^2+\gamma^2},\quad r=R/q,\quad t=\max(1,r),\quad
C_L=\frac{\pi}{\Gamma(3/4)^2},\quad M_\sigma=\sqrt{2\pi},
\]
\[
K_q=\frac{(2q+1)11^{2q}e^{\pi q}}{\sqrt{C_Lq}},\quad
D_q=1+(q+1)[4t(1+r)]^q,\quad
C_{\rm rem}=\sqrt{M_\sigma}\,2^qD_qK_q,
\]
\[
E_k=2\log C_{\rm rem}+\log(u_k/\ell_k).
\]
Here \(\ell_k,u_k\) are the unchanged native source bounds through degree \(2q\). The proof uses the literal full polynomial remainder, every original root, and the original Gamma mass. Thus the metric bound used below is a proved inherited result, not an extra assumed missing theorem. Full source nesting also gives \(G_{N+1}\preceq G_N\).

## PEN2. Full pencil rank and the exact filtration algorithm

Define
\[
\mathcal P(u,v)=uI_K-vMI_K:\mathbb C^m\longrightarrow E.
\]
It has rank \(m\) at every \([u:v]\in\mathbb P^1\). At \(v=0\) this is injectivity of \(I_K\). If \(v\ne0\), a nonzero null vector would give \(x\in K\setminus0\) with \(Mx=(u/v)x\), and every \(\Lambda M^j x\) would vanish, contradicting \(K_d=0\). This also handles \(u=0\).

Put \(K_j=0\) after the first zero level. For \(h\ge1\),
\[
MK_h\subset K_{h-1},\qquad K_h\cap MK_h=MK_{h+1}. \tag{PEN3}
\]
For the second equality, \(Mx\in K_h\) with \(x\in K_h\) means precisely that all observations through power \(h+1\) annihilate \(x\). Injectivity of \(M\) on \(K\) follows already from observability, so dimensions are preserved in these images. Choose an actual coefficient complement
\[
K_{h-1}=(K_h+MK_h)\oplus V_h
\]
in descending \(h=d,\ldots,1\). Its dimension is
\[
c_h=\dim K_{h-1}-2\dim K_h+\dim K_{h+1}.
\]
For every chosen basis vector \(x\in V_h\), retain the entire list \(x,Mx,\ldots,M^h x\). Its first \(h\) vectors lie in \(K\); the terminal one lies outside \(K\).

Here is the full basis argument. The induced map
\[
M:K_h/K_{h+1}\longrightarrow K_{h-1}/K_h
\]
is injective, since \(Mx\in K_h\) is equivalent to \(x\in K_{h+1}\). At the highest nonzero level the chosen leaders form its entire quotient. Descending induction shows that the descendants of leaders chosen at higher levels form the injected subspace \(MK_h/(MK_h\cap K_h)\) at level \(K_{h-1}/K_h\), and the new leaders \(V_h\) complete its basis. Thus every quotient in the filtration has exactly its claimed basis. Descending through all levels proves all nonterminal columns form a basis of \(K\). Their immediate-predecessor classes form a basis of \(K/K_1\). Its injective map into \(E/K\) makes the terminal columns independent modulo \(K\). Complete those terminal classes to a basis of \(E/K\) and choose actual representatives; each additional vector is a chain of length zero.

Let the complete chain columns form \(X:E_{\rm chain}\to E\), and let their lengths be \(\nu_1,\ldots,\nu_n\). Let \(E_K\) include nonterminal coordinates and \(E_B\) terminal coordinates. There is a unique invertible \(Y\) such that \(I_KY=XE_K\). Consequently
\[
X^{-1}(uI_K-vMI_K)Y=\bigoplus_{a=1}^n L_{\nu_a}(u,v),\qquad
L_\nu(u,v)e_j=ue_j-ve_{j+1}\quad(0\le j<\nu). \tag{PEN4}
\]
A length-zero block has one target row and no source column. Every identity follows from the actual columns \(Me_{a,j}=e_{a,j+1}\) for \(j<\nu_a\). No external classification theorem is needed for this pair.

This is the algorithm implemented in the independent checker. The supplied routine was also read: its concatenation of a basis of \(K_h+MK_h\) before the columns of \(K_{h-1}\), followed by pivot selection, constructs precisely these complements. Its final coordinate solve constructs \(Y\). Its rank guards do not estimate conditioning.

## PEN3. Complete lengths and the unchanged source frames

A vector remains in \(K\) for \(j\) further powers exactly when the last \(j\) nonterminal coefficients of every chain vanish. First \(\Lambda Mx\), for \(x\in K\), reads the immediate-predecessor coefficients in the independent terminal images. Their vanishing makes \(Mx\) another hidden vector. Repeat inductively. No terminal-column action is used before this vanishing has been established. Thus
\[
K_j=\operatorname{span}\{e_{a,r}:0\le r<\nu_a-j\},\qquad
\dim K_j=\sum_a(\nu_a-j)_+,\qquad \sum_a\nu_a=m. \tag{PEN5}
\]
If \(b_j=\dim K_{j-1}-\dim K_j\), then
\[
b_j=\#\{a:\nu_a\ge j\},\quad
\#\{a:\nu_a=j\}=b_j-b_{j+1},\quad
\#\{a:\nu_a=0\}=n-b_1.
\]
This determines the entire list from actual observation ranks. In particular,
\[
\max_a\nu_a=d\le80,\qquad
\sum_a(\nu_a-8)_+\le128.
\]
These repeated 021 results do not determine the actual list from those two inequalities alone.

Every coefficient change is transported in the physical metric:
\[
\widetilde G_N=X^*G_NX,\qquad
Y^*H_{K,N}Y=E_K^*\widetilde G_NE_K,\qquad
\widetilde M=X^{-1}MX.
\]
The matrix \(T_B=\Lambda XE_B\) is invertible and \(\Lambda X=T_BE_B^*\). Thus the observed chain metric is \(Q_N^c=T_B^*Q_NT_B\), and its attained section is \(X^{-1}L_NT_B\). These may be nonunitary changes; no condition number is assigned.

The precise relation to the auxiliary parameter in 021 is also fixed. That proof writes \(A=M/(2R)\). With the same leader, its chain vectors and the present ones obey \(e_{M,j}=(2R)^je_{A,j}\); the chain frame change is the corresponding diagonal matrix, whose congruence transports the metric. Its homogeneous parameter changes by \([u:v]\mapsto[u:2Rv]\). Thus its length list agrees with the present list while this proof keeps the literal original \(M\), \(k/2+iM\), and \((u,v)\) in every formula.

The repeated construction and splitting are cited at their actual public proof: [021 BD4–7, chain construction, complete polynomial quotient and projective endpoints](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/BOUNDED_DEGREE_PROOFS.md#L84). The original rectangular support and 128-direction theorem are [021 BD2–3](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/BOUNDED_DEGREE_PROOFS.md#L33), and the entire-source bound used in (PEN2) is [021 BD11–12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/BOUNDED_DEGREE_PROOFS.md#L241). The frozen local proof was matched by SHA256 before using these source locators.

## PEN4. Complete long sectors and their directed metric return

At depth \(s\ge0\), let \(\mathcal L_s=\{a:\nu_a>s\}\), \(\ell_s=|\mathcal L_s|\), and \(t_s=\dim K_s\). The complete long hidden and ambient dimensions are exactly
\[
h_s=\sum_{a\in\mathcal L_s}\nu_a=s\ell_s+t_s,\qquad
a_s=\sum_{a\in\mathcal L_s}(\nu_a+1)=(s+1)\ell_s+t_s. \tag{PEN6}
\]
Each summand of \(t_s\) is a positive integer, so \(\ell_s\le t_s\). Hence
\[
h_s\le(s+1)t_s,\qquad a_s\le(s+2)t_s,\qquad
h_8\le1152,\quad a_8\le1280.
\]
The bounds are sharp among lists satisfying only \(t_8\le128\): 128 lengths equal to nine attain them. This is not a claim that such a list is realized by an original period, or that every \(k\) has enough total hidden dimension. For the native \(m\), retain also \(h_8\le m\) and \(\ell_8\le\lfloor m/9\rfloor\).

Order the short hidden columns before long hidden columns. Write the full restricted metric
\[
H_N^c=\begin{pmatrix}H_{SS,N}&H_{SL,N}\\H_{LS,N}&H_{LL,N}\end{pmatrix},
\qquad
H_{S,N}^{K}=H_{SS,N}-H_{SL,N}H_{LL,N}^{-1}H_{LS,N}. \tag{PEN7}
\]
This is the minimum over long hidden coordinates with the short hidden value fixed. Exact elimination gives
\(\det H_N^c=\det H_{LL,N}\det H_{S,N}^{K}\).
Since \(Y\) is the same at all cutoffs, its determinant contribution cancels under the four signs. Restriction of (PEN2) to the fixed long frame and source nesting yield
\[
0\le\mathcal R\log\det H_{LL,N}\le2h_sE_k.
\]
Indeed pair \((q-1,2q-1)\) and \((q,2q)\). Each log determinant difference is nonnegative by source inclusion and at most \(h_sE_k\) by the complete-form enclosure. Therefore
\[
0\le \mathcal R\log\det H_{K,N}
-\mathcal R\log\det H_{S,N}^{K}
\le2h_8E_k\le2304E_k=O_h(q). \tag{PEN8}
\]
Empty determinants are one. The complete long metric and its cross term remain present.

## PEN5. Canonical sections from the original filtration

The pointwise full-rank pencil defines
\[
0\longrightarrow\mathcal O(-1)\otimes K
\xrightarrow{\,uI-vM\,}\mathcal O\otimes E
\longrightarrow\mathcal Q\longrightarrow0.
\]
The coordinates \(u,v\) are the actual pencil parameters. On a chain of length \(\nu\), the row \((v^\nu,uv^{\nu-1},\ldots,u^\nu)\) annihilates all pencil columns and is nonzero on every projective fibre. Its kernel has the same dimension as the pencil image, proving \(\mathcal Q\simeq\bigoplus_a\mathcal O(\nu_a)\). This repeats 021's splitting.

A stronger identification needs no choice of chain basis. For \(x\in K_j\), define a section \(\Phi_j(x)\) of \(\mathcal Q(-j-1)\) by
\[
\Phi_j(x)|_{u\ne0}=\left[\frac{M^{j+1}x}{u^{j+1}}\right],\qquad
\Phi_j(x)|_{v\ne0}=\left[\frac{x}{v^{j+1}}\right]. \tag{PEN9}
\]
Brackets mean the actual quotient by the pencil image in the stated trivialization. All \(M^r x\), \(0\le r\le j\), belong to \(K\). The exact telescoping identity
\[
\frac{x}{v^{j+1}}-\frac{M^{j+1}x}{u^{j+1}}
=(uI-vM)\sum_{r=0}^{j}
\frac{M^r x}{u^{r+1}v^{j+1-r}} \tag{PEN10}
\]
proves gluing, including its signs and denominators.

In a proved chain frame, for \(0\le r<\nu_a-j\), its formula is
\[
\Phi_j(e_{a,r})=u^r v^{\nu_a-j-1-r}
\]
in the \(a\)-th \(\mathcal O(\nu_a-j-1)\) summand. These are its complete monomial basis. A section of \(\mathcal O(b)\) is a pair of chart polynomials \(f(t),g(s)\) satisfying \(f(t)=t^b g(1/t)\); this forces the powers \(0,\ldots,b\) for \(b\ge0\), and zero for \(b<0\). Thus
\[
\Phi_j:K_j\xrightarrow{\ \simeq\ }H^0(\mathbb P^1,\mathcal Q(-j-1))
\]
is a proved canonical isomorphism for the fixed pair \((K\subset E,M)\) and fixed pencil coordinates. The construction, unlike its verification in a convenient chain frame, is independent of the complements.

## PEN6. Both projective variables and the original physical action

For \(x\in K_{j+1}\),
\[
\Phi_j(x)=v\,\Phi_{j+1}(x),\qquad
\Phi_j(Mx)=u\,\Phi_{j+1}(x). \tag{PEN11}
\]
The first follows from the quotient relation \([tMy]=[y]\), with \(t=v/u\) and \(y=M^{j+1}x\in K\); the second follows on the \(u\ne0\) chart. Thus the two homogeneous multiplications record the actual inclusion \(K_{j+1}\subset K_j\) and \(M:K_{j+1}\to K_j\).

Writing \(c=k/2\), the original physical operator satisfies
\[
\Phi_j(\mathscr A x)=(cv+iu)\Phi_{j+1}(x). \tag{PEN12}
\]
If \(f(S)=\sum_{r=0}^ha_rS^r\) and \(x\in K_{j+h}\), iteration proves
\[
\Phi_j(f(\mathscr A)x)
=\left[\sum_{r=0}^ha_r(cv+iu)^r v^{h-r}\right]\Phi_{j+h}(x). \tag{PEN13}
\]
No physical coordinate or source degree cutoff changes. The domain \(K_{j+h}\) states exactly when the entire word stays in the required kernel levels.

At \([1:0]\), the fibre is \(E/K\), identified with the original \(B\) by \(\Lambda\), and
\(\Phi_j(x)([1:0])=\Lambda M^{j+1}x\).
Thus the next observation is an exact endpoint evaluation. At \([0:1]\), the fibre is \(E/MK\); since \(M\) is invertible its identification with \(B\) is \(\Lambda M^{-1}\). The other endpoint is \(\Lambda M^{-1}x\), in the trivialization (PEN9), and its attained metric is
\[
Q_{\infty,N}=(\Lambda M^{-1}G_N^{-1}M^{-*}\Lambda^*)^{-1}.
\]
This is an explicit different quotient of the same complete source, not an assigned equality to \(Q_N\).

## PEN7. Current on the canonical section spaces

Give \(H^0(\mathcal Q(-j-1))\) the actual pulled-back metric
\[
\langle s,t\rangle_{j,N}
=\langle\Phi_j^{-1}s,\Phi_j^{-1}t\rangle_{G_N}.
\]
This definition retains every native mass and cross term. It is not a Fubini–Study assignment. If \(s,t\in H^0(\mathcal Q(-j-2))\), (PEN11) gives the exact centered current pairing
\[
\mathfrak J_{j,N}(s,t)
=i\{\langle vs,ut\rangle_{j,N}
-\langle us,vt\rangle_{j,N}\}. \tag{PEN14}
\]
Indeed for \(x=\Phi_{j+1}^{-1}s\), \(y=\Phi_{j+1}^{-1}t\), the right side is
\(i(x^*G_NMy-x^*M^*G_Ny)\), the restriction of
\(\mathscr A^*G_N+G_N\mathscr A-kG_N\).
Thus the section multiplication dictionary carries the actual Hermitian current, not only the arithmetic rank. It gives no sign without the source metric values.

## PEN8. What survives quotienting complete long chains

Fix the chain frame and a depth \(s\), and split its ambient coordinates as
\[
E_{\rm chain}=E_S\oplus E_L,\qquad
E_S=K_S\oplus B_S,\quad E_L=K_L\oplus B_L.
\]
Here \(K_S,K_L\) mean spans of nonterminal chain coordinates and \(B_S,B_L\) their terminal-coordinate spans; the latter are chosen coefficient lifts, not orthogonal subspaces. In particular \(\dim K_L=h_s\), \(\dim B_L=\ell_s\), and \(\dim E_L=a_s\). We suppress the fixed \(X\) transport in the displayed matrices but retain \(\widetilde G=X^*GX\) and \(\widetilde M=X^{-1}MX\).

Write
\[
\widetilde M=
\begin{pmatrix}M_{SS}&M_{SL}\\M_{LS}&M_{LL}\end{pmatrix}.
\]
For every hidden column, its next chain vector lies in the same complete ambient sector. Therefore the cross blocks vanish on the hidden parts and factor exactly through the terminal selectors:
\[
M_{SL}=C_{SL}E_{B_L}^*,\qquad
M_{LS}=C_{LS}E_{B_S}^*. \tag{PEN15}
\]
Here \(C_{SL}=M_{SL}E_{B_L}\) and \(C_{LS}=M_{LS}E_{B_S}\) are the full original terminal action columns. They are not set to zero.

Let \(\pi:E_S\oplus E_L\to E_S\) be coordinate projection. The pencil quotient is a proved commuting square:
\[
\pi(uI-v\widetilde M)|_K
=(uI_{K_S}-vM_{SS}I_{K_S})\,\pi_K,
\]
where \(\pi_K:K_S\oplus K_L\to K_S\). Indeed both \(I_{K_L}\) and \(\widetilde M I_{K_L}\) land in \(E_L\). Its kernel and target quotient retain exactly the short blocks, all of length at most \(s\). The full operator \(\widetilde M\) descends to an endomorphism of \(E/E_L\) if and only if \(C_{SL}=0\). This equivalence follows because invariance of \(E_L\) is exactly vanishing of \(M_{SL}\), and (PEN15) proves which columns can obstruct it. Thus the obstruction is the concrete map \(C_{SL}:B_L\to E_S\).

For the kernel minimum (PEN7), the attained hidden lift is
\[
L_K^S x=I_{K_S}x-I_{K_L}H_{LL}^{-1}H_{LS}x.
\]
Its correction lies in \(K_L\), so projection kills both the correction and its image under \(\widetilde M\). Therefore
\[
\pi(uI-v\widetilde M)L_K^S
=uI_{K_S}-vM_{SS}I_{K_S}. \tag{PEN16}
\]
The unchanged quotient pencil survives this moving metric lift exactly. This does not imply the complete action on \(E_S\) is closed.

## PEN9. The short hidden minimum and the short ambient minimum differ

There are two distinct, explicitly related minimization problems. The metric \(H_S^K\) minimizes only over \(K_L\) while every terminal coordinate is zero. The ambient quotient metric minimizes over \(E_L=K_L\oplus B_L\), allowing the long terminal values to vary. We now prove their exact morphism.

First eliminate \(K_L\) from the entire \(\widetilde G\), leaving coordinates \(E_S\oplus B_L\). Denote that full Schur complement by
\[
G^{(1)}=
\begin{pmatrix}A&B\\B^*&C\end{pmatrix}>0,
\]
where, with all subscripts referring to the displayed original blocks,
\[
A=G_{E_SE_S}-G_{E_SK_L}G_{K_LK_L}^{-1}G_{K_LE_S},
\]
\[
B=G_{E_SB_L}-G_{E_SK_L}G_{K_LK_L}^{-1}G_{K_LB_L},
\quad
C=G_{B_LB_L}-G_{B_LK_L}G_{K_LK_L}^{-1}G_{K_LB_L}. \tag{PEN17}
\]
Let \(I_S:K_S\to E_S\) be its coordinate inclusion and \(B_K=I_S^*B\). Then
\[
H_S^K=I_S^*AI_S,\qquad
G_S^E=A-BC^{-1}B^*,
\]
\[
\boxed{I_S^*G_S^EI_S
=H_S^K-B_KC^{-1}B_K^*.} \tag{PEN18}
\]
These follow by minimizing successively over exactly the same coordinates; alternatively direct completion of both squares gives the same formula. Thus the defect is a specified positive form of rank
\[
r_{\rm met}=\operatorname{rank}B_K\le\ell_s\le t_s,\qquad r_{\rm met}\le128\quad(s=8).
\]
The two metrics agree if and only if \(B_K=0\), since \(C>0\). This describes the exact space of source metrics for which the two quotient procedures agree, rather than inferring unrelatedness from their different domains.

The determinant ratio is also a complete \(\ell_s\)-dimensional receiver. Put
\[
C_K=C-B_K^*(H_S^K)^{-1}B_K>0.
\]
Taking the determinant of the block restriction of \(G^{(1)}\) to \(K_S\oplus B_L\) in both orders gives
\[
\frac{\det H_S^K}{\det(I_S^*G_S^EI_S)}
=\frac{\det C}{\det C_K}. \tag{PEN19}
\]
If \(K_S=0\) the ratio is one; if \(B_L=0\) all correction determinants are empty and one.

Every metric here is obtained by restriction and exact minimum from the same \(G_N\), in fixed coordinate spaces. Such operations preserve the source enclosure and monotonicity: a bound between two positive forms holds for every candidate lift, and therefore for their infima. Consequently both \(C_N\) and \(C_{K,N}\), of rank \(\ell_s\), have directed four-cutoff returns in \([0,2\ell_sE_k]\). Subtracting gives the useful two-sided estimate
\[
\left|\mathcal R\log\det H_{S,N}^K
-\mathcal R\log\det(I_S^*G_{S,N}^EI_S)\right|
\le2\ell_sE_k\le256E_k\quad(s=8). \tag{PEN20}
\]
The metric defect has a positive sign at each cutoff, but its four-cutoff return need not have one. Combining with (PEN8) yields
\[
-2\ell_sE_k\le
\mathcal R\log\det H_{K,N}
-\mathcal R\log\det(I_S^*G_{S,N}^EI_S)
\le2(h_s+\ell_s)E_k,
\]
so at depth eight the bounds are \(-256E_k\) and \(2560E_k\). The directed \(2304E_k\) theorem applies to \(H_S^K\), exactly as in (PEN8), not automatically to the ambient short restriction.

An explicit auxiliary example proves the possible negative sign. Take chain lengths \((1,2)\), depth one, and metric identity on all hidden coordinates. Couple the sole short hidden coordinate to the long terminal by \(1/2\), with all other off-diagonal entries zero. At the first two cutoffs give that long terminal diagonal one, and at the last two give it \(1/2\); all remaining diagonals are one. These are positive metrics and form a nested family. The whole hidden determinant and \(H_S^K\) are constant one. The ambient short hidden metric is \(3/4\) at the first two cutoffs and \(1/2\) at the last two. Hence the return difference between the full hidden metric and that ambient short restriction is exactly \(-2\log(3/2)<0\). This fixture establishes the sign issue for the general operation; it is not a native period evaluation.

## PEN10. Full physical action after the ambient minimum

Now order the full metric by \(E_S,E_L\):
\[
\widetilde G=\begin{pmatrix}G_{SS}&G_{SL}\\G_{LS}&G_{LL}\end{pmatrix},\quad
Z=-G_{LL}^{-1}G_{LS},\quad
H=G_{SS}-G_{SL}G_{LL}^{-1}G_{LS}=G_S^E.
\]
The original attained section of \(\pi\) is \(L_\pi=(I,Z)^{\mathsf T}\), its metric is \(H\), and its complementary projection is
\[
P_L=\begin{pmatrix}0&0\\-Z&I\end{pmatrix}.
\]
This follows by direct multiplication and orthogonality to every vector of \(E_L\). With
\[
U=\begin{pmatrix}I&0\\Z&I\end{pmatrix},
\]
the complete metric and action become
\[
U^*\widetilde G U=\begin{pmatrix}H&0\\0&G_{LL}\end{pmatrix},
\quad
U^{-1}\widetilde M U=
\begin{pmatrix}\mathcal B&\mathcal C\\\mathcal D&\mathcal E\end{pmatrix}, \tag{PEN21}
\]
where every block is
\[
\mathcal B=M_{SS}+M_{SL}Z,\qquad \mathcal C=M_{SL},
\]
\[
\mathcal D=M_{LS}+M_{LL}Z-ZM_{SS}-ZM_{SL}Z,\qquad
\mathcal E=M_{LL}-ZM_{SL}. \tag{PEN22}
\]
Multiplying the three displayed matrices proves the identities. In particular
\[
\pi\widetilde M-(\pi\widetilde M L_\pi)\pi=M_{SL}(-Z,I)
=\pi\widetilde M P_L. \tag{PEN23}
\]
This proves the received KP11 for the actual minimum projection and displays its full terminal-column factor \(C_{SL}E_{B_L}^*\). The reverse defect \(\mathcal D\) is also retained; it records how the moving attained lift fails to be invariant. A coordinate short sector and its attained short lift need not have the same invariance condition.

For the physical \(\mathscr A=cI+iM\), its full centered Hermitian current in this attained splitting is
\[
\mathfrak J=
\begin{pmatrix}
i(H\mathcal B-\mathcal B^*H)&i(H\mathcal C-\mathcal D^*G_{LL})\\
i(G_{LL}\mathcal D-\mathcal C^*H)&i(G_{LL}\mathcal E-\mathcal E^*G_{LL})
\end{pmatrix}. \tag{PEN24}
\]
Indeed its definition is \(i(\operatorname{diag}(H,G_{LL})U^{-1}\widetilde M U
-(U^{-1}\widetilde M U)^*\operatorname{diag}(H,G_{LL}))\).
For a vector with attained coordinates \((x,\ell)\), the complete scalar is
\[
x^*i(H\mathcal B-\mathcal B^*H)x
+\ell^*i(G_{LL}\mathcal E-\mathcal E^*G_{LL})\ell
+2\Re\{x^*i(H\mathcal C-\mathcal D^*G_{LL})\ell\}. \tag{PEN25}
\]
Both cross blocks and their complex phases survive.

The difference between the true short current and one formed from the raw \(M_{SS}\) is
\[
i(HM_{SL}Z-Z^*M_{SL}^*H).
\]
Its rank is at most \(2\operatorname{rank}M_{SL}\le2\ell_s\le256\) at depth eight, by (PEN15). This is an exact rank bound on a specified correction, not a bound on its magnitude or sign. The full off-diagonal current also contains \(\mathcal D\) and cannot be reconstructed from this correction alone.

## PEN11. Relation to the original observed current

The original observation in chain coordinates is \(E_B^*\), with metric \(Q^c=T_B^*QT_B\). Project its output to the short terminal coordinates, calling the result
\[
\lambda_S=(E_{B_S}^*,0):E_S\oplus E_L\to B_S.
\]
It factors through \(\pi\), so exact successive minimization gives
\[
Q_S=(E_{B_S}^*H^{-1}E_{B_S})^{-1},\quad
L_S^{\rm red}=H^{-1}E_{B_S}Q_S,\quad
L_S^{\rm full}=L_\pi L_S^{\rm red}. \tag{PEN26}
\]
The last is exactly \(\widetilde G^{-1}\lambda_S^*Q_S\): it has the required value and is orthogonal to \(\ker\lambda_S=K_S\oplus E_L\), which proves equality by uniqueness. Its centered current is
\[
\Phi_S(b_S)
=i b_S^*(L_S^{\rm red})^*
(H\mathcal B-\mathcal B^*H)L_S^{\rm red}b_S.
\]
It measures the original short observed value while allowing the original long observed value to minimize. This is not asserted equal to the full current at an arbitrary fixed long value.

The exact relation is another complete Schur splitting. Write the original observed metric and arithmetic operator as
\[
Q^c=\begin{pmatrix}Q_{SS}&Q_{SL}\\Q_{LS}&Q_{LL}\end{pmatrix},\quad
M_B^c=T_B^{-1}\Lambda ML T_B.
\]
Put \(Z_B=-Q_{LL}^{-1}Q_{LS}\) and
\(U_B=(I,0;Z_B,I)\). The short metric in (PEN26) equals
\(Q_{SS}-Q_{SL}Q_{LL}^{-1}Q_{LS}\), by the same nested minimum. For the original fixed observed vector \((b_S,b_L)\), define \(\beta_L=b_L-Z_Bb_S\). Its original attained lift splits orthogonally as
\[
X^{-1}LT_B(b_S,b_L)
=L_S^{\rm full}b_S+X^{-1}LT_B(0,\beta_L).
\]
Transport \(M_B^c\) by \(U_B\) and \(Q^c\) by congruence, using all four formulas (PEN22) with the observed blocks substituted. The full original current is then exactly the three terms of (PEN25) with \(H\) replaced by \(Q_S\), \(G_{LL}\) by \(Q_{LL}\), and \((x,\ell)\) by \((b_S,\beta_L)\). This proves the full connecting map between the shortened receiver and the original observed current, including its long-value and complex cross contributions.

## PEN12. A finite exact reconstruction recipe for both minima

The complete finite probes recovered in 021 and in the other 022 channel determine the full original \(G^{-1}\), hence \(G\), while \((M,\Lambda)\) determine the chain frame independently of \(N\). The following are finite exact operations on those actual data: construct \(X,Y,T_B\); transform \(G\); take (PEN17); compute the two short metrics and their positive correction (PEN18); form \(Z,\mathcal B,\mathcal C,\mathcal D,\mathcal E\); then apply (PEN24) and (PEN26). No approximate source identification or diagonal replacement occurs. Source uncertainty can be propagated through each minimum by the same complete-form inequalities, but a current sign requires a separate enclosure of the actual current matrix; the positive metric width alone does not determine it.

The canonical maps (PEN9)–(PEN13) use only the unchanged finite quotient and preserve every relation \(Q_kp=0\). They neither enlarge the physical source cutoff nor translate its integration axis. Their section metrics in PEN7 are the actual restrictions of the original \(G_N\), so all four endpoint returns retain the original normalization and phases.

There is a more precise link to the mixed-covariance receiver. In the chain kernel frame put \(C_N=(H_N^c)^{-1}\). The depth-\(s\) captured coordinate set contains every short hidden coordinate, and exactly the last \(s\) hidden coordinates of each long chain. This follows directly from (PEN5), because the omitted coordinates are \(K_s\). Denote the additional long coordinates by \(P_s\), so \(\dim P_s=s\ell_s\). Write the principal covariance on the captured coordinates as
\[
C_N^{\rm cap}=
\begin{pmatrix}C_{SS,N}&C_{SP,N}\\C_{PS,N}&C_{PP,N}\end{pmatrix},
\quad
W_{s,N}=C_{PP,N}-C_{PS,N}C_{SS,N}^{-1}C_{SP,N}.
\]
Its complete Schur determinant is
\(\det C_N^{\rm cap}=\det C_{SS,N}\det W_{s,N}\).
The mixed observation rows selected at depth \(s\) differ from these captured coordinate rows by a fixed invertible matrix: both vanish on exactly \(K_s\), and both have rank \(m-t_s\). This proves the exact coordinate isomorphism; its determinant cancels under the four endpoint signs. Therefore the original depth-\(s\) covariance receiver \(X_s\) satisfies
\[
X_s=-\mathcal R\log\det C_N^{\rm cap},\qquad
Y_s:=\mathcal R\log\det H_{S,N}^{K}
=-\mathcal R\log\det C_{SS,N},
\]
\[
\boxed{X_s-Y_s=-\mathcal R\log\det W_{s,N},\qquad
0\le X_s-Y_s\le2s\ell_sE_k.} \tag{PEN27}
\]
To prove the last bounds, inverses \(C_N\) increase with source cutoff. Principal restriction and Schur minimum preserve this ordering, as well as the width factor \(e^{E_k}\). Hence each of the two negative covariance log determinant differences is nonnegative and at most \(s\ell_sE_k\). Empty blocks have determinant one. Combined with the established exact depth remainder
\(0\le\mathcal R\log\det H_{K,N}-X_s\le2t_sE_k\),
this decomposes the full long-chain return into two positive pieces, with total bound
\(2(t_s+s\ell_s)E_k=2h_sE_k\), exactly (PEN8). At depth eight the second piece has bound \(16\ell_8E_k\le2048E_k\), and the omitted-depth piece has bound \(256E_k\). Both use the same original inverse kernel metric and cannot be assigned independently.

## PEN13. Scope of completion and exact checks

The independent checker constructs filtration complements on nonnormal rational and Gaussian-rational systems in nonunitary frames; verifies the whole two-parameter pencil; checks every filtration index and both canonical section multiplications; verifies physical polynomial words with their full \(c\) and \(i\); and checks both Schur procedures and their exact low-rank difference. Its coupled-terminal fixture verifies the entire current matrix and its projected defect, including nonzero cross terms. A separate nested family checks the failure of a directed sign when the wrong short metric is substituted. The combinatorial 128-length-nine fixture is labelled a sharp bound for lists, not original native data.

The proof retains the complete native metric and original coefficients. The inherited native kernel coefficient, EIQ value, and separate complex-current signs remain unevaluated. Neither the count \(1152/1280\), the bundle degree \(m\), nor the return width \(2304E_k\) assigns those values.
