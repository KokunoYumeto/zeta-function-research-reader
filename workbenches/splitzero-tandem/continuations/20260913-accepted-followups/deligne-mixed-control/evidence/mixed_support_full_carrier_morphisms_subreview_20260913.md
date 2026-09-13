# Full mixed support: exact carriers and synchronization maps

2026-09-13. This is the corrected scope after the user's clarification that the question concerns mixed support. The earlier `split_support_original_definition_subreview_20260913.md` audits the two-leg theta NOTE only and is not a complete answer to this question.

Source V5: `corpus:research-library/Chatnotes/split_zero_projective_monads_surcomplex/split_support_absolute_arithmetic_curve_v5.tex`.

Source ML: `workspace:math/output/split_zero_rh_tandem_2026-09-12/sources/Split_Support_Adelic_Weights_2026-09-11/sources/mixed_support_ledger.tex`.

The proofs below retain the independent faces, their full amplitudes, and the original multiplication. No upper analytic estimate is deduced from this algebraic audit.

## 1. Independent products and their full fibres

For nonzero commutative rings (R_i), indexed by a nonempty finite set (I), the independent carrier is
\[
P_I=\prod_{i\in I}G(R_i).
\]
Its operations are coordinatewise. Its support morphism is
\[
s:P_I\longrightarrow\mathcal P(I),\qquad
s(x)=\{i:x_i\ne\tau_i\},
\]
where the target has addition union and multiplication intersection. Indeed a sum at coordinate (i) is absent exactly when both summands are absent, and a product is absent exactly when at least one factor is absent. Thus the exact fibre at a mask (A\subseteq I) is
\[
s^{-1}(A)=\prod_{i\in A}R_i\times\prod_{i\notin A}\{\tau_i\}.
\]
Every proper nonempty face retains all of its supported amplitudes, including its supported zero. The empty face is the singleton all-absent tuple. The amplitude morphism
\[
p:P_I\to\prod_iR_i
\]
replaces absent coordinates by their typed ring zeros. For an amplitude (r), let (J(r)=\{i:r_i\ne0_{R_i}\}\). Its exact fibre is indexed by all masks (A\) containing (J(r)); each mask specifies a unique lift of (r). Hence the zero fibre has (2^{|I|}) distinct elements and the combined map ((p,s)) is injective, with image \(\{(r,A):J(r)\subseteq A\}\). This proves the full higher-face formula without collapsing to one Boolean bit.

For two factors this is exactly V5 lines 591–659. Those lines also prove the synchronized inclusion
\[
j:G\Bigl(\prod_iR_i\Bigr)\hookrightarrow P_I,
\quad j(\tau)=(\tau_i)_i,
\quad j(r^\bullet)=(r_i^\bullet)_i.
\]
It is a unital semiring morphism by the coordinate operations. Its image contains precisely the empty and full masks. Equivalently it is the pullback of the diagonal \(\mathbb B\to\mathbb B^I\) along all coordinate support characters. This is the exact relationship between synchronized and independent support.

There is no amplitude-preserving semiring map (q:P_{\{1,2\}}\to G(R_1\times R_2)) which sends every nonempty face to a supported amplitude. For (x=(1_{R_1}^\bullet,\tau_2)) and (y=(\tau_1,1_{R_2}^\bullet)), the original product is the all-absent zero. The specified images would have amplitudes ((1,0)) and ((0,1)) and their product would be the supported zero of (G(R_1\times R_2)), contradicting preservation of the all-absent zero. The surviving exact maps are the synchronized inclusion (j), the full support (s), and the ordinary amplitude (p), with (p\circ j=p_{\prod R_i}). This is a calculation of a particular impossible collapse, not a claim of unrelated objects.

## 2. The mixed quadratic double and its different synchronization quotient

ML lines 182–220 define (S=G(A)), (u=(-1_A)^\bullet), and
\[
D_A=S\oplus S,
\qquad(a,b)\star(c,d)=(ac+ubd,ad+bc).
\]
The unit is (X_1=(1_A^\bullet,\tau)). The four faces are
\[
\mathbf0=(\tau,\tau),\quad
X_a=(a^\bullet,\tau),\quad
Y_b=(\tau,b^\bullet),\quad
Z_{a+tb}=(a^\bullet,b^\bullet),
\]
with (B=A[t]/(t^2+1)). Since the polynomial is monic of degree two, every (z\in B) has a unique pair of coordinates (a,b\in A); no invertibility of 2 or field assumption is used. The multiplication retains all faces:
\[
X_aX_c=X_{ac},\quad X_aY_d=Y_{ad},\quad Y_bY_d=X_{-bd},
\]
\[
X_aZ_z=Z_{az},\quad Y_bZ_z=Z_{tbz},\quad Z_zZ_w=Z_{zw}.
\]
This is quadratic convolution, whereas the independent Cartesian product in §1 had coordinatewise multiplication. The exact support semiring here is \(\mathbb B[C_2]\), not the lattice semiring with intersection multiplication:
\[
\Chi(a,b)=(\chi(a),\chi(b)),\qquad
(p,q)(r,s)=(pr\vee qs,ps\vee qr).
\]
This is ML lines 323–338, and follows by applying the support character to each original summand. The four support values and all their fibres remain visible.

There is a unital synchronization quotient for this quadratic double:
\[
q_D:D_A\twoheadrightarrow G(B),\qquad
q_D(\mathbf0)=\tau,\quad q_D(X_a)=a^\bullet,
\quad q_D(Y_b)=(tb)^\bullet,\quad q_D(Z_z)=z^\bullet.
\]
To prove it, any sum or product involving \(\mathbf0\) satisfies the zero laws. A sum of two nonempty faces remains nonempty and its amplitude is the sum in (B). The displayed face table shows that a product of two nonempty faces also remains nonempty and has exactly the product amplitude in (B), including products with zero amplitude. The unit (X_1) maps to (1_B^\bullet). These facts prove every semiring law required of (q_D).

Its fibres are exact:
\[
q_D^{-1}(\tau)=\{\mathbf0\},\qquad
q_D^{-1}(e_B)=\{X_0,Y_0,Z_0\}.
\]
For \(a\ne0\) and \(b\ne0\), the fibre over ((a+tb)^\bullet) is \(\{Z_{a+tb}\}\). For (a\ne0) and (b=0), it is \(\{X_a,Z_a\}\); for (a=0) and (b\ne0), it is \(\{Y_b,Z_{tb}\}\). The uniqueness of the degree-two coordinates proves exhaustiveness. Its entire kernel congruence is generated by (X_0\sim Y_0): adding either side shows (Z_0\sim X_0\sim Y_0), then adding (X_a) gives (X_a\sim Z_a), and adding (Y_b) gives (Y_b\sim Z_{tb}). These are exactly the fibres just listed, and the quotient map proves no other identifications follow.

The synchronized-face section
\[
\iota:G(B)\longrightarrow D_A,
\quad\iota(\tau)=\mathbf0,\quad\iota(z^\bullet)=Z_z
\]
preserves addition, multiplication, and zero and satisfies (q_D\iota=\mathrm{id}). Its value at the unit is (Z_1=(1_A^\bullet,0_A^\bullet)\ne X_1), so its precise category is semirings with zero-preserving maps not required to preserve the unit. The composite \(\iota q_D\) fills all missing coordinates of a nonempty face with supported zero.

There is no unital semiring section of (q_D). Suppose (s) were such a section. In (G(B)), (1+e_B=1), so (X_1+s(e_B)=X_1). Among the three possible lifts (X_0,Y_0,Z_0), only (X_0) has this property. Hence (s(e_B)=X_0). The element (t^\bullet) has only the lifts (Y_1,Z_t). But (e_Bt^\bullet=e_B), while (X_0Y_1=Y_0\ne X_0) and (X_0Z_t=Z_0\ne X_0). Both lifts contradict multiplicativity. This proves the exact obstruction while retaining the explicit nonunital section.

ML supplies substantially more geometry than a two-element support skeleton: all ideals are \(\{\mathbf0\},M_H,I_{J,H}\), with (H\triangleleft B), (J\triangleleft A), and (JB\subseteq H) (lines 223–258). The prime families are (P_\tau,M,Q_{\mathfrak q},T_{\mathfrak p}); (M) is incomparable with every (Q_{\mathfrak q}), and \(Q_{\mathfrak q}\subseteq T_{\mathfrak p}\) iff \(\mathfrak q\cap A\subseteq\mathfrak p\) (lines 260–291). The supplied full proof gives \(\dim D_A=\dim A+2\) for finite-dimensional (A) (lines 294–309). These prime branches are part of the original mixed-support machinery to be retained by any downstream arithmetic model.

## 3. Higher zero fibres, their maps to the independent cube, and retained depth

V5 lines 1316–1481 define, for a bounded distributive lattice (L),
\[
G_L(R)=\{(0_R,\lambda):\lambda\in L\}
\cup\{(r,1_L):r\in R\}\subseteq R\times L,
\]
with sum ((r+s,\lambda\vee\mu)) and product ((rs,\lambda\wedge\mu)). Its full amplitude-zero fibre is exactly (L); its support projection is a semiring map; and localization at (z_\lambda=(0_R,\lambda)) is exactly \(\downarrow\lambda\). The latter map before localization is explicitly
\[
(r,\mu)\longmapsto\lambda\wedge\mu.
\]
Its unit has image \(\lambda\), the unit of the interval; multiplication by (z_\lambda) proves its universal localization property because an invertible idempotent must become the unit. Its fibres are all the original pairs with \(\lambda\wedge\mu=\nu\); in particular all original amplitudes at top map to \(\lambda\), not to absent support.

For (L=\mathcal P(I)) and (R=\prod_iR_i), there is a precise injective unital semiring morphism
\[
J:G_{\mathcal P(I)}\Bigl(\prod_iR_i\Bigr)\hookrightarrow P_I.
\]
It sends ((r,I)) to the fully supported tuple of amplitudes (r_i), and ((0,A)) to the zero-amplitude tuple supported exactly on (A). The definitions agree at ((0,I)). The coordinate sum and product immediately give join and meet for the zero faces, and multiplying a full tuple by a zero face gives that same zero face. These verify the morphism; recovery of amplitude and mask proves injectivity. Its image is exactly all full-support tuples together with all zero-amplitude faces. Proper faces with nonzero amplitude lie in the larger independent product described in §1. This exact inclusion explains what the higher-zero scalar does and does not retain.

For (C_n=\{0<1<\cdots<n\}), the ring-zero fibre has (n+1) strata. The original subzeros are \(\tau_i=(0,n-i)\), with
\[
\tau_i+\tau_j=\tau_{\min(i,j)},\qquad
\tau_i\tau_j=\tau_{\max(i,j)}.
\]
For each (1\le k\le n), the threshold map \(\alpha_k(j)=0\) for (j<k) and (1\) for (j\ge k\) preserves bottom, top, join, and meet. It therefore induces the exact unital morphism
\[
G_{C_n}(R)\to G(R),
\quad(r,n)\mapsto r^\bullet,
\quad(0,j)\mapsto
\begin{cases}\tau&j<k,\\e_R&j\ge k.\end{cases}
\]
The absent fibre consists of the (k) original strata below (k), while the supported-zero fibre consists of the (n-k+1) strata at or above (k). This records explicitly the depth lost in any such binary observation.

V5 lines 1483–1527 identify this chain with all (n+1) ideals (I_a=p^a(\mathbb Z/p^n)\) or (J_a=\epsilon^a k[\epsilon]/(\epsilon^n)\), by (j\mapsto I_{n-j}\) or (J_{n-j}\), using sum and intersection. Lines 1529–1556 retain the separate ideal-product operation (I_aI_b=I_{\min(n,a+b)}\), the full truncated valuation degree. This is an explicit common carrier with two completely specified multiplications; no nilpotent order is replaced by a single support bit.

## Bounded audit conclusion

The user's mixed-support object has original independent faces, a quadratic-convolution double, distinct mixed prime branches, higher distributive-lattice zero fibres, and iterated nilpotent/valuation degrees. The exact maps above show how a synchronized or binary model can lose those faces and degrees. A discussion restricted to (\tau\) versus (e), or to a single globally supported packet, does not establish that this full machinery has been carried into the arithmetic control construction. That downstream comparison must retain these explicitly typed maps and fibres. This audit does not decide what analytic upper estimate exists in later files; that is the parent's parallel source audit.
