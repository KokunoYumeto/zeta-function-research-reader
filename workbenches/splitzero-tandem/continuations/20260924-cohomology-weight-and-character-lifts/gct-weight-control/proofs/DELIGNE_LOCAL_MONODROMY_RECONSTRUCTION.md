# Deligne, Weil II §§1.6–1.9: local monodromy and exact weight control

Independent reconstruction, 24 September 2026. Result labels in this file are DLM1–DLM15. This file reconstructs the specified part of Deligne's argument; it does not assign a sheaf, Frobenius, nilpotent operator, weight, distance, or vector to the programme's `τ〈Z1; no Z2〉`.

## Source identity, reading coverage, and transcription corrections

The work is Pierre Deligne, *La conjecture de Weil. II*, Publications mathématiques de l'IHÉS **52** (1980), 137–252. The source used here is the current French page-record export:

`S20_FR_record_export.tex`

Its SHA256 is `d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351`. It is a transcription with explicit page records, not author-supplied TeX. The historical English math-mode file was used to compare ambiguous formulas, not to override the French witness. No PDF was read for this reconstruction.

Reading completed: every line of §§1.6–1.9, current export lines 874–1421, printed pages 165–181; the §1.9 heading begins on page 179. Dependencies actually read: conventions (0.6)–(0.11), printed page 145; §1.2, printed pages 153–155; §1.4, printed pages 162–163. The reconstruction uses Grothendieck's trace formula, quasi-unipotence, Abhyankar's lemma, and basic étale sheaf/cohomology results as the external inputs identified by Deligne. It does not claim a new proof of those foundations.

The witness is preserved unchanged. The following corrections are independently forced by the formulas and definitions; they are not accusations about Deligne's printed original:

1. In (1.6.7), the exception in `Ne_i=e_{i-2}` must be `i≠−d`, with `Ne_{−d}=0`; the witness writes `i≠d`.
2. In (1.6.13)'s uniqueness proof the witness contains the impossible inequality `k−2i−2≥k`. The necessary and true inequality is `k−2i−2≥2j−k` when `k≥i+1` and `j≤0`. DLM4 proves it with the arbitrary top weight retained.
3. In (1.6.14.3), both witnesses display a positive twist `(i+j)/2`. With the explicitly stated convention `N:V(1)→V`, the required formula is
   \[
   \operatorname{Gr}_i^M V\cong
   \bigoplus_{j\ge |i|,\ j\equiv i\ (2)}P_{-j}\left(-\frac{i+j}{2}\right).
   \tag{DLM-C1}
   \]
   Indeed `N^r:Gr_i V(r)→P_{−j}` with `r=(i+j)/2` is the relevant isomorphism on the indicated summand. Its inverse supplies the negative twist. The witness's next assertion that both sides have equal weights independently requires this sign. DLM3 proves the formula, and DLM10 uses it without changing β.
4. In (1.7.5), the weight filtration is the **direct sum over `j≤i`** of generalized eigenspaces of weight `j`. The witness's `product over j<i` cannot have graded piece of weight `i`.
5. For geometric Frobenius `F` and `N:V(1)→V`, `FNF^{-1}=Q^{-1}N`. Consequently the conjugation coefficient in the proof of (1.7.5), if `F''^n=exp(λN)F'^n`, is `μ=λ/(1−Q^{-n})`. The witness displays `1−q^n`. DLM6 includes the direct multiplication that checks this correction.
6. The denominator in (1.8.1.1) is `H_c^2`, as in the current French text. The historical English `H^0` is not used. DLM8 retains all three compact-support degrees before proving the degree-zero factor is 1 in the auxiliary affine curve.

## DLM1. The monodromy filtration and its primitive pieces

**Source:** (1.6.1)–(1.6.7), printed pages 165–166.

Let `V` be an object of an abelian category and let `N:V→V` be nilpotent. There is a unique finite increasing filtration `M` satisfying

\[
NM_i\subseteq M_{i-2},\qquad
N^k:\operatorname{Gr}_k^M V\xrightarrow{\sim}\operatorname{Gr}_{-k}^M V
\quad(k\ge0).
\tag{DLM1.1}
\]

Here a finite filtration is exhaustive and zero in sufficiently low degree. The subscript `0` is a filtration index. It is not a base point of the scheme, nor the centre of a geometric circle.

**Existence and uniqueness.** Induct on an integer `d≥0` for which `N^{d+1}=0`. For `d=0`, the conditions force `M_{−1}=0,M_0=V`. For `d>0`, the extreme pieces must be

\[
M_d=V,\quad M_{d-1}=\ker N^d,\quad
M_{-d}=\operatorname{im}N^d,\quad M_{-d-1}=0.
\tag{DLM1.2}
\]

To see that they are forced, (DLM1.1) and `N^{d+1}=0` imply `Gr_k=0` for `k>d`; symmetry gives the same for `k<−d`. On the remaining top graded piece, `N^d` is an isomorphism to the bottom graded piece. Its kernel in `V` is therefore `M_{d−1}`, and its image is `M_{−d}`. On

\[
\ker N^d/\operatorname{im}N^d
\]

the induced `N^d` is zero. Its monodromy filtration is already constructed uniquely by induction. Pull its pieces back into `ker N^d`, and attach (DLM1.2). The lowering condition and the isomorphisms follow on the middle graded pieces by induction and on the extreme pieces from the image/coimage isomorphism for `N^d`. This proves both assertions.

Set

\[
P_i(V)=\ker\bigl(N:\operatorname{Gr}_i^M V\longrightarrow
\operatorname{Gr}_{i-2}^M V\bigr).
\tag{DLM1.3}
\]

For `i>0`, `N` is injective on `Gr_i`, because its composite with `N^{i−1}` is the isomorphism `N^i`; hence `P_i=0`. For `j≥0`, the composite

\[
\operatorname{Gr}_{j+2}^M V
\xrightarrow{N^{j+1}}\operatorname{Gr}_{-j}^M V
\xrightarrow{N}\operatorname{Gr}_{-j-2}^M V
\]

is an isomorphism. Therefore

\[
\operatorname{Gr}_{-j}^M V
=P_{-j}\oplus N^{j+1}\operatorname{Gr}_{j+2}^M V.
\tag{DLM1.4}
\]

Iterating this direct sum, then using `N^i:Gr_i→Gr_{−i}`, yields, for a chosen actual endomorphism `N`,

\[
\operatorname{Gr}_i^M V\cong
\bigoplus_{j\ge |i|,\ j\equiv i\ (2)}P_{-j}.
\tag{DLM1.5}
\]

The map `N:(V,M)→(V,M shifted by 2)` is strict:

\[
N(M_{i+2})=\operatorname{im}N\cap M_i.
\tag{DLM1.6}
\]

If `i<0`, its associated graded onto `M_i` is surjective by (DLM1.5), and finite filtrations imply surjectivity. If `i+2>0`, the induced map `V/M_{i+2}→V/M_i` is injective on associated gradeds, hence injective. These cases cover every integer `i`. Thus kernels commute with passage to the associated graded:

\[
\operatorname{Gr}_i^M(\ker N)\cong P_i.
\tag{DLM1.7}
\]

For finite-dimensional vector spaces, a Jordan string of length `d+1` has vectors

\[
e_d,e_{d-2},\ldots,e_{-d},\qquad
Ne_i=e_{i-2}\ (i> -d),\quad Ne_{-d}=0.
\]

Its filtration is `M_i=span{e_j:j≤i}`. Direct sums of these strings give the entire filtration. The string's primitive vector is its **lowest** vector `e_{−d}`. This specifies the sign of every primitive index above.

## DLM2. The SL(2) construction, tensor products, and duals

**Source:** (1.6.8)–(1.6.12), printed pages 167–168.

Now work over a characteristic-zero field. On a string of length `d+1`, put `e_r=e_{−d+2r}` for `0≤r≤d`. Define

\[
H e_r=(-d+2r)e_r,\qquad
F e_r=e_{r-1},\qquad
E e_r=(d-r)(r+1)e_{r+1},
\tag{DLM2.1}
\]

with the out-of-range vectors zero. Then `F=N`, and direct substitution gives

\[
[H,E]=2E,\qquad[H,F]=-2F,\qquad[E,F]=H.
\]

This is the irreducible `SL(2)` representation `S_d=Sym^d(k^2)` in a rescaled basis. On the associated graded, the grading itself prescribes `H`, and the primitive decomposition prescribes these strings. Thus one obtains the `SL(2)` representation of (1.6.10), with the diagonal matrix `diag(λ,λ^{-1})` acting by `λ^i` on `Gr_i^M V`. This representation is on the associated graded; no choice of a splitting of `V` is being declared canonical.

For `(V',N')` and `(V'',N'')`, use exactly

\[
V=V'\otimes V'',\qquad N=N'\otimes1+1\otimes N''.
\tag{DLM2.2}
\]

On the tensor product `SL(2)` representation, diagonal weights add and the lowering generator is precisely (DLM2.2). Its increasing weight filtration therefore satisfies (DLM1.1); uniqueness gives

\[
M_i(V'\otimes V'')=\sum_{a+b=i}M_aV'\otimes M_bV''.
\tag{DLM2.3}
\]

The dual operator is `−N^t`, not `N^t`: differentiation of the contragredient action introduces the minus sign. Diagonal weights negate, so

\[
M_i(V^*)=(M_{-i-1}V)^\perp.
\tag{DLM2.4}
\]

For finite filtrations, choosing splittings verifies the natural isomorphisms

\[
\operatorname{Gr}(V'\otimes V'')\cong\operatorname{Gr}V'\otimes\operatorname{Gr}V'',
\qquad
\operatorname{Gr}_i(V^*)\cong(\operatorname{Gr}_{-i}V)^*;
\]

the maps themselves are induced by classes and pairings and do not depend on the splittings used to verify bijectivity.

Choose a nonzero lowest-weight vector in each `S_d`, and choose the Clebsch–Gordan isomorphisms

\[
S_{d'}\otimes S_{d''}\cong
\bigoplus_{j\in P(d',d'')}S_j,
\quad
P(d',d'')=\{j:|d'-d''|\le j\le d'+d'',\ j\equiv d'+d''\pmod2\}.
\tag{DLM2.5}
\]

These decompositions follow by multiplying the characters
`z^d+z^{d−2}+⋯+z^{−d}` and subtracting successively the highest character. Every listed summand occurs once. Complete reducibility in characteristic zero makes this a direct sum of representations. The isomorphisms involve the stated choices; the source does not assert a unique scalar for every Clebsch–Gordan component.

The lowest-weight inclusion gives

\[
\operatorname{Gr}^M V\cong\bigoplus_{j\ge0}S_j\otimes P_{-j},
\quad
P_{-j}\cong\operatorname{Hom}_{SL(2)}(S_j,\operatorname{Gr}^M V).
\tag{DLM2.6}
\]

Applying (DLM2.5) to (DLM2.6) gives the primitive tensor decomposition. Twists must be restored when `N` belongs to a nontrivial line, as follows.

## DLM3. The monodromy line and every Tate twist

**Source:** (1.6.14), printed pages 169–170.

Let `𝔑` be a one-dimensional vector space acting nilpotently on `V`, and write `V(k)=V⊗𝔑^{⊗k}`; negative `k` uses the dual line. The action is a map `N:V(1)→V`. Choosing a basis in `𝔑` turns it into an endomorphism. Changing that basis multiplies the endomorphism by a nonzero scalar, leaving `M` and `P_i` unchanged. Iterated action is the basis-independent map

\[
N^k:\operatorname{Gr}_{a+k}^M\operatorname{Gr}_a^W V(k)
\longrightarrow\operatorname{Gr}_{a-k}^M\operatorname{Gr}_a^W V.
\tag{DLM3.1}
\]

The primitive decomposition, tensor primitive decomposition and dual primitive decomposition are

\[
\operatorname{Gr}_i^M V\cong
\bigoplus_{j\ge|i|,\ j\equiv i\ (2)}P_{-j}\left(-\frac{i+j}{2}\right),
\tag{DLM3.2}
\]

\[
P_{-j}(V'\otimes V'')\cong
\bigoplus_{j\in P(j',j'')}
P_{-j'}(V')\otimes P_{-j''}(V'')
\left(\frac{j-j'-j''}{2}\right),
\tag{DLM3.3}
\]

\[
P_{-j}(V^*)\cong P_{-j}(V)^*(j).
\tag{DLM3.4}
\]

To check (DLM3.2), let `r=(i+j)/2`. The `j`-string in degree `i` maps isomorphically to its lowest vector by `N^r` after tensoring the source with `𝔑^{⊗r}`. Solving for the source gives twist `−r`. To check (DLM3.3), the component of length `j` arises from the two strings by `r=(j'+j''−j)/2` contractions; under rescaling `N`, its comparison with the chosen primitive vectors has exactly `r` inverse powers of the monodromy-line basis. This gives twist `−r`. Equivalently, retain the strings as `S_j` with the monodromy-line grading: the primitive degree `−j` is obtained from degree `−j'−j''` by raising `2r`, and each raising contributes `𝔑^{-1}`. For the dual, the lowest vector comes from the dual of the highest vector, which by (DLM3.2) is the dual of `P_{−j}(-j)`; this is `P_{−j}^*(j)`.

In the geometric application, `𝔑=\overline{\mathbf Q}_\ell(1)`, geometric Frobenius acts on it by `Q^{-1}`, and its weight is `−2`. The weight checks on (DLM3.2)–(DLM3.4) are then respectively

\[
-j-2\left(-\frac{i+j}{2}\right)=i,
\quad
-j'-j''-2\left(\frac{j-j'-j''}{2}\right)=-j,
\quad j-2j=-j.
\]

These checks do not replace the maps; they verify the twists in the maps just constructed.

## DLM4. Uniqueness of relative monodromy, with arbitrary top weight retained

**Source:** (1.6.13), printed pages 168–169.

Let `W` be a finite increasing filtration on `V`, preserved by `N`. There is at most one finite increasing `M` with

\[
NM_i\subseteq M_{i-2},\qquad
N^k:\operatorname{Gr}_{a+k}^M\operatorname{Gr}_a^W V
\xrightarrow{\sim}\operatorname{Gr}_{a-k}^M\operatorname{Gr}_a^W V
\quad(a\in\mathbf Z,\ k\ge0).
\tag{DLM4.1}
\]

This is a uniqueness assertion; existence for a mixed sheaf is proved in DLM11 and DLM14, not inserted here as an assumption about arbitrary filtered objects.

Induct on the length of `W`. Let `a` be its top nonzero degree, so `W_a=V`. The restriction to `W_{a−1}` is unique by induction; on `Gr_a^W V`, the filtration is the absolute monodromy filtration centred at `a`. Let its range be contained in `[a−c,a+c]`. For `r≥0`, a putative filtration satisfies

\[
\begin{aligned}
M_{a-r}&=M_{a-r}(W_{a-1}) &&(r>c),\\
M_{a-r}&=M_{a-r}(W_{a-1})+N^rM_{a+r},\\
M_{a+r}&=\ker\left(N^{r+1}:V\longrightarrow V/M_{a-r-2}\right).
\end{aligned}
\tag{DLM4.2}
\]

The first formula says that the quotient has no degree that low. For the second, the lowering condition gives inclusion of the right side into the left, while the induced `N^r` maps the quotient's `M_{a+r}` onto its `M_{a−r}`, as one sees on each string centred at `a`. For the third, one inclusion follows from lowering. On `G=Gr_j^W V`, `j≤a`, the reverse inclusion follows because

\[
N^{r+1}:G/M_{a+r}G\longrightarrow G/M_{a-r-2}G
\]

is injective. On a degree `k>a+r`, the central isomorphism runs from `k` to `2j−k`. The shorter iterate by `r+1` remains injective since

\[
k-2r-2\ge 2j-k,
\]

which follows from `k≥a+r+1` and `j≤a`. Passage to `Gr^W` of a kernel injects into the corresponding kernel; finite filtrations then give the required inclusion in `V`. Starting in sufficiently large `r` and descending, the three formulas determine alternately `M_{a+r}` and `M_{a-r}`. This proves uniqueness without replacing `a` by zero.

## DLM5. Local inertia and its logarithm

**Source:** (1.7.1)–(1.7.3), printed pages 170–171.

Let `R` be a henselian discrete valuation ring, with fraction field `K`, residue field `k`, and compatible algebraic closures. The exact sequence and tame quotient are

\[
1\to I\to\operatorname{Gal}(\bar K/K)\to\operatorname{Gal}(\bar k/k)\to1,
\]
\[
1\to P\to I\xrightarrow{t}\prod_{\ell'\ne p}\mathbf Z_{\ell'}(1)\to1.
\tag{DLM5.1}
\]

Here `p` is the residue characteristic exponent and `P` is pro-`p`. Fix `ℓ≠p`; the `ℓ`-component is `t_ℓ:I→Z_ℓ(1)`.

For a quasi-unipotent `ℓ`-adic representation `ρ` of `I`, there is a unique nilpotent line action

\[
N:V(1)\longrightarrow V
\quad\text{with}\quad
\rho(\sigma)=\exp(Nt_\ell(\sigma))
\tag{DLM5.2}
\]

on a sufficiently small finite-index subgroup of `I`. The exponential and logarithm are finite polynomials on nilpotent/unipotent matrices. The prime-to-`ℓ` kernel cannot have a nontrivial image in a sufficiently small torsion-free pro-`ℓ` unipotent group. Thus this restriction factors through `Z_ℓ(1)`. Taking the logarithm and dividing by a nonzero element of an open subgroup determines the unique linear action of `Q̄_ℓ(1)`. This also shows independence of the finite-index subgroup.

If `k` is finite with `Q` elements, the local Weil group is the inverse image of the integer powers of geometric Frobenius. Its representations satisfy quasi-unipotence, the theorem of Grothendieck cited by Deligne. The Frobenius conjugation explains the finite-order semisimple part: after removing the finite wild and prime-to-`ℓ` images, a tame generator has its eigenvalue multiset preserved by the `Q`-power map. Each eigenvalue consequently has finite multiplicative order; a common positive power is unipotent. This is compatible with (DLM5.2), whose coordinate-free `N` is Weil-equivariant.

Choosing a basis for the Tate line displays that equivariance as

\[
FNF^{-1}=Q^{-1}N.
\tag{DLM5.3}
\]

The nilpotent operator is not an involution. Except for the zero operator, a nilpotent operator cannot square to the identity. Its exponential is the unipotent part of monodromy, and all its tensor and dual operations have been specified above.

## DLM6. Independence of Frobenius lift and the local weight filtration

**Source:** (1.7.4)–(1.7.7), printed pages 171–172.

If `F'` and `F''` are lifts of the same residue Frobenius, their eigenvalues differ by roots of unity. One can pass to semisimplification for this eigenvalue assertion. There the inertia image is finite: an irreducible constituent's `ker N` is nonzero and Weil-stable by (DLM5.3), so it is the whole constituent and `N=0`. In a representation with finite inertia image, choose a power of Frobenius that centralizes that finite image, then a further power killing the finite discrepancy between the two lifts. The resulting powers of `F'` and `F''` agree. Their eigenvalues before powering therefore differ by roots of unity.

Thus

\[
w_Q(\alpha)=2\log_Q|\iota\alpha|
\]

is independent of the lift. Suppose these weights are integers. For a chosen lift, let `V_j'` be the sum of its generalized eigenspaces of weight `j` and set

\[
M_i'=\bigoplus_{j\le i}V_j'.
\tag{DLM6.1}
\]

The operator `N` takes `V_j'` to `V_{j−2}'` by (DLM5.3). For two lifts, choose `n>0` for which their powers differ by unipotent inertia:

\[
F''^n=\exp(\lambda N)F'^n.
\]

All powers of `N` commute. Direct multiplication gives

\[
\begin{aligned}
\exp(\mu N)F'^n\exp(-\mu N)
&=\exp(\mu N)\exp(-\mu Q^{-n}N)F'^n\\
&=\exp(\mu(1-Q^{-n})N)F'^n.
\end{aligned}
\tag{DLM6.2}
\]

Take `μ=λ/(1−Q^{−n})`. Passing from `F'` to `F'^n` does not change the partition into weights, because `w_{Q^n}(α^n)=w_Q(α)`. The operator `exp(μN)` preserves each `M_i'`; therefore the filtrations obtained from the two lifts coincide. Conjugating a lift by any Weil-group element gives another lift, so `M` is Weil-stable. Uniqueness follows from the decomposition into generalized eigenspaces: a filtration with pure graded weights must place the generalized weight-`j` summand in degree `j`.

In particular `NM_i(1)⊂M_{i−2}`. A locally pure representation has a single weight, so `N=0` and inertia has finite image. This does **not** say that the local representation at the boundary of a pointwise pure sheaf is pure. DLM10 calculates its several weights `β+i`; nonzero local monodromy is exactly compatible with those shifts.

Without the integral-weight restriction, grouping eigenvalues modulo `Q^Z` times roots of unity gives the canonical decomposition in (1.7.7). The same conjugation proof works: multiplication of an eigenvalue by `Q^{-1}` keeps its class, so `N` preserves each class and the exponential comparisons preserve the decomposition. Each class can be twisted by a rank-one character to obtain integral weights. This last comparison retains the twisting scalar; it is not a replacement of the original representation in DLM10.

## DLM7. The tame normal-crossing specialization functor and its exact compatibility

**Source:** (1.7.8)–(1.7.12), printed pages 172–174.

Let `X` be regular, let `D=⋃_{i∈I}D_i` be a normal-crossing divisor with smooth transverse components, and put `E=⋂D_i`. Locally choose equations `t_i=0`. For `n` invertible on `X`, form

\[
X_n=X[T_i:i\in I]/(T_i^n-t_i:i\in I).
\tag{DLM7.1}
\]

Over `X−D` this is an étale cover, with `μ_n^I` acting by `T_i↦r_iT_i`. Above `E` the reduced section is `T_i=0`. For a locally constant finite sheaf tamely ramified through primes in `L`, Abhyankar's lemma supplies such an `n` after which the pullback extends locally constantly over `X_n`. Restrict that extension to the section over `E`; its inherited `μ_n^I` action defines `𝓕[E]`. Passing through compatible finite levels gives the `ℓ`-adic construction and an action of

\[
\mathbf Z_L(1)^I=\left(\prod_{\ell'\in L}\mathbf Z_{\ell'}(1)\right)^I.
\]

This functor is exact on the stated locally constant sheaves: after a common cover trivializes a finite-level sequence, extension and restriction are exact operations on the corresponding constant modules. The same argument with compatible lattices gives the `Q̄_ℓ` functor. Tensor products and duals are likewise preserved. The commuting unipotent logarithms are

\[
N_i:\mathcal F[E](1)\to\mathcal F[E],\qquad
\rho(\sigma)=\exp\left(\sum_i N_i\sigma_i\right)
\tag{DLM7.2}
\]

on an open subgroup.

For `J⊂I`, define

\[
D_J=\bigcap_{j\in J}D_j,\quad
X_J=X\setminus\bigcup_{i\notin J}D_i,\quad
D_J^*=D_J\cap X_J.
\]

For `K⊂I−J`, restriction of a common Kummer extension first to the `J`-stratum and then to the `J∪K`-stratum equals direct restriction. Hence there is an actual isomorphism

\[
\mathcal F[D_J^*][D_{J\cup K}^*]
\xrightarrow{\sim}\mathcal F[D_{J\cup K}^*]
\tag{DLM7.3}
\]

preserving every inertia coordinate in `J∪K`. For three nested strata the two composites agree because both are restriction of the same sheaf on the same Kummer cover. This transitivity will be used, not merely an equality of dimensions.

The equation-dependent construction has an intrinsic version on the normal bundle of `E` with its component hyperplanes removed. A choice of the `t_i` gives a section of that bundle; its pullback recovers `𝓕[E]`. The construction commutes with smooth base change. This retains the dependence on a transverse direction instead of deleting it.

In a henselian local neighborhood, the tame fundamental group is an extension of the residue Galois group by `Z_L(1)^I`. Choosing compatible roots of the `t_i` splits it: use the lifts fixing those roots. The functor above is precisely restriction along this splitting together with the retained inertia action. Over a finite residue field, the arguments of DLM5–DLM6 apply with commuting `N_i` and show quasi-unipotence, independence of weights from the lift, and existence of the local weight filtration. In (DLM6.2), one replaces `λN` and `μN` by sums of the commuting `N_i`, with the same factor `1−Q^{−n}` in every coordinate.

## DLM8. Boundary weights from the full trace formula and all tensor powers

**Source:** (1.8.1), printed page 175, using (1.4.1)–(1.4.7), printed pages 162–163.

Let `X_0` be a smooth absolutely irreducible curve over `F_q`, `j:U_0↪X_0` the complement of a finite set `S_0`, and `𝓕_0` lisse and pointwise `ι`-pure of weight `β` on `U_0`. At a closed point `x`, put `N(x)=q^{deg x}`. For every eigenvalue `α` of `F_x` on `(j_*𝓕_0)_{\bar x}`,

\[
|\iota\alpha|\le N(x)^{\beta/2}.
\tag{DLM8.1}
\]

Here is the complete amplification argument. For the local assertion at the finitely many points in `S_0`, one can delete an additional point from `U_0` to work on an affine open of `X_0`. This auxiliary passage leaves the sheaf and the boundary stalks being asserted unchanged; it is not a deletion of a boundary factor. On that affine curve, the full trace formula is

\[
\begin{aligned}
&\prod_{x\in|U_0|}\iota\det(1-F_xt^{\deg x},\mathcal F_{0,\bar x})^{-1}
\prod_{x\in|S_0|}\iota\det(1-F_xt^{\deg x},(j_*\mathcal F_0)_{\bar x})^{-1}\\
&\hspace{1cm}=
\frac{\iota\det(1-Ft,H_c^1(X,j_*\mathcal F))}
{\iota\det(1-Ft,H_c^0(X,j_*\mathcal F))\,
 \iota\det(1-Ft,H_c^2(X,j_*\mathcal F))}.
\end{aligned}
\tag{DLM8.2}
\]

The degree-zero compact-support space vanishes: any such section is zero on a nonempty open of the connected affine curve, and a section of `j_*𝓕` injects into its generic fiber. Its determinant factor is consequently exactly `1`. The degree-two space is

\[
H_c^2(X,j_*\mathcal F)
\cong H_c^2(U,\mathcal F)
\cong V_{\pi_1(U)}(-1),
\tag{DLM8.3}
\]

where geometric coinvariants are used. The geometrically constant quotient of the pure sheaf is pure of weight `β`; the displayed `(-1)` raises the weight by `2`. Thus every denominator eigenvalue in degree two has modulus `q^{(β+2)/2}`. There is no pole of the right side in

\[
|t|<q^{-(\beta+2)/2}.
\tag{DLM8.4}
\]

The first Euler product on the left is analytic and nonzero there. Indeed the number of degree-`n` closed points is at most `Cq^n`; the rank is finite; and each local eigenvalue has modulus `q^{nβ/2}`. The logarithmic expansion is absolutely convergent when `q^{1+β/2}|t|<1`, by comparison with the geometric series, including the higher powers in the logarithm. Each boundary reciprocal determinant can only have poles, not zeros. Since neither the first Euler product nor another boundary reciprocal polynomial can cancel a boundary pole, (DLM8.2)–(DLM8.4) give

\[
|\iota\alpha|\le N(x)^{(\beta+2)/2}.
\tag{DLM8.5}
\]

For every positive integer `r`, the actual stalk inclusion is

\[
(V^I)^{\otimes r}\hookrightarrow (V^{\otimes r})^I,
\quad\text{equivalently}\quad
(j_*\mathcal F_0)^{\otimes r}\hookrightarrow j_*(\mathcal F_0^{\otimes r}).
\tag{DLM8.6}
\]

It is generally not surjective, and no such surjectivity is used. The tensor-power sheaf has pointwise weight `rβ`. If `α` occurs in `V^I`, an eigenvector tensor power shows that `α^r` occurs in the left side of (DLM8.6), hence also in the right side. Applying the weak estimate to this sheaf gives

\[
|\iota\alpha|^r\le N(x)^{(r\beta+2)/2},
\qquad
w_{N(x)}(\alpha)\le\beta+\frac2r.
\tag{DLM8.7}
\]

This holds for every `r`. If the weight exceeded `β` by `ε>0`, an integer `r>2/ε` would contradict (DLM8.7). This proves (DLM8.1) exactly, with no finite tensor cutoff and no change of the original `β`.

## DLM9. The auxiliary degree-one bound

**Source:** (1.8.2), printed page 175.

In (DLM8.4) the left side of the trace formula has no zeros. Its degree-two denominator is nonzero there. Consequently the numerator cannot vanish there. Every eigenvalue `α` on `H_c^1(X,j_*𝓕)` therefore satisfies

\[
|\iota\alpha|\le q^{(\beta+2)/2}.
\tag{DLM9.1}
\]

This is the auxiliary bound stated at this stage, not the later sharp curve theorem. Its exact role here is distinct from the local tensor-power argument, which already removed the `+2` at boundary stalks.

## DLM10. Local purity: tensor square and duality force the exact modulus

**Source:** theorem (1.8.4), printed pages 175–176; primitive maps (1.6.14.2), (1.6.14.4), (1.6.14.5).

Choose `s∈S_0` with residue field of cardinality **`Q=N(s)`**, a geometric point over it, and the geometric generic point of its strict henselization. Put `V=𝓕_{0,\bar η}` and let `M` be its local monodromy filtration. For every integer `i`,

\[
\operatorname{Gr}_i^M V\text{ is }\iota\text{-pure of weight }\beta+i
\quad\text{relative to }Q.
\tag{DLM10.1}
\]

A finite cover makes inertia unipotent. This comparison preserves all relevant weights: a residue extension of degree `f` replaces `Q` by `Q^f` and an eigenvalue by its `f`th power, up to the finite inertia factors; the logarithmic weight is unchanged. A ramification index `e` replaces `N` by `eN`; the monodromy filtration and its primitive subspaces are unchanged because `e≠0` in the characteristic-zero coefficient field. Thus it suffices to prove the assertion on this cover, with the field cardinality, weight `β`, and scaling of `N` retained in the comparison. No twist to weight zero is used below.

For unipotent inertia,

\[
V^I=\ker N=(j_*\mathcal F_0)_{\bar s}.
\]

By DLM8 every Frobenius eigenvalue on this space has modulus at most `Q^{β/2}`. Since `P_{−j}=Gr_{−j}^M(ker N)`, the same bound initially holds for `α` on `P_{−j}`.

Now apply the statement to `𝓕_0⊗𝓕_0`, whose weight is **`2β`**. The primitive tensor map (DLM3.3), with `j'=j''=j` and target index zero, includes the direct summand

\[
P_{-j}(V)\otimes P_{-j}(V)(-j)
\hookrightarrow P_0(V\otimes V).
\tag{DLM10.2}
\]

The eigenvalue on the tensor square is `α²`; the `(-j)` twist multiplies it by `Q^j`. The boundary estimate for weight `2β` therefore gives

\[
|\iota(\alpha^2Q^j)|\le Q^{\beta},
\qquad
|\iota\alpha|\le Q^{(\beta-j)/2}.
\tag{DLM10.3}
\]

Next apply that same established upper bound to the **dual sheaf of weight `−β`**. By the actual dual primitive isomorphism (DLM3.4), the corresponding eigenvalue is

\[
\alpha^{-1}Q^{-j}\quad\text{on }P_{-j}(V^*).
\]

Its upper bound is `Q^{(−β−j)/2}`. Hence

\[
|\iota\alpha|^{-1}Q^{-j}\le Q^{(-\beta-j)/2},
\qquad
|\iota\alpha|\ge Q^{(\beta-j)/2}.
\tag{DLM10.4}
\]

Together (DLM10.3) and (DLM10.4) force

\[
\boxed{|\iota\alpha|=Q^{(\beta-j)/2}\quad\text{on }P_{-j}.}
\tag{DLM10.5}
\]

Finally the degree-`i` summand in (DLM3.2) carries the multiplier `Q^{(i+j)/2}`. Thus each of its eigenvalues has modulus

\[
Q^{(\beta-j)/2}Q^{(i+j)/2}=Q^{(\beta+i)/2}.
\tag{DLM10.6}
\]

This proves (DLM10.1). The centre of this weight statement is the retained number `β`; it is obtained through exact eigenvalue multipliers and the two opposite inequalities, not by choosing a spatial origin.

## DLM11. Mixed relative monodromy and the smooth-divisor case

**Source:** (1.8.5)–(1.8.8), printed pages 176–177.

Suppose a lisse sheaf has a finite increasing filtration `W` by lisse subsheaves, with `Gr_a^W𝓕_0` pointwise pure of weight `a`. Its local representation has integral weights: apply DLM10 to every graded quotient and then combine their eigenvalue multisets. DLM6 therefore gives an actual local weight filtration `M`. The operator `N` lowers it by two. On each `Gr_a^W V`, DLM10 says its monodromy filtration shifted by `a` is exactly this weight filtration. Consequently

\[
N^b:\bigl(\operatorname{Gr}_{a+b}^M\operatorname{Gr}_a^W V\bigr)(b)
\xrightarrow{\sim}\operatorname{Gr}_{a-b}^M\operatorname{Gr}_a^W V.
\tag{DLM11.1}
\]

The use of `Gr^W` here is compatible with the weight filtration: a Frobenius-equivariant linear map preserves generalized weight spaces, and taking their direct sums is exact. Thus the graded object in (DLM11.1) is the same whether one first passes to `Gr^W` or first takes the weight filtration. DLM4 proves uniqueness. This proves existence and identification of the relative monodromy filtration, rather than assuming it.

For a smooth divisor `D_0` in a smooth finite-field scheme `X_0`, assume tame ramification and the same lisse filtration `W` on the complement. The sheaf `𝓕_0[D_0]` and `N` are furnished by DLM7. At each closed point of `D_0`, choose an étale transverse curve. Its local representation is exactly the corresponding fiber of `𝓕_0[D_0]` with its tame logarithm. DLM11.1 supplies the fiber filtration; uniqueness makes it invariant under parallel transport and therefore a lisse filtration. Its degree-`a` graded sheaf is pointwise pure of weight `a`.

For a pointwise pure sheaf of weight `β`, the actual boundary sheaf is obtained by taking the invariants of the finite residual inertia action on `ker N`. Since its order is invertible in `Q̄_ℓ`, averaging makes the invariants functor exact. The filtration therefore descends, with

\[
\operatorname{Gr}_i^M(j_*\mathcal F_0)_{\bar s}
\text{ pure of weight }\beta+i,\qquad i\le0,
\]

and zero for `i>0`. The same assertion holds along a smooth divisor. With mixed input, the resulting boundary filtration has its degree-`a` quotient pure of weight `a`.

## DLM12. Extension across an open immersion and propagation of purity

**Source:** (1.8.9)–(1.8.13), printed pages 177–178.

For any finite-type `F_q` scheme and open immersion `j:U_0↪X_0`, an `ι`-mixed sheaf of pointwise weights `≤β` has `j_*𝓕_0` of the same weight bound. Integral weights remain integral.

The source's reduction is induction on `dim U_0`, with the following exact maps retained:

* For an extension `0→𝓕'→𝓕→𝓕''→0`, left exactness gives `0→j_*𝓕'→j_*𝓕→j_*𝓕''`; the quotient of the middle by the first is a subsheaf of the last. Bounds and integrality pass to these subquotients.
* A locally closed support `i:V_0↪U_0` with `𝓕↪i_*i^*𝓕` reduces the assertion to the closure of `V_0` and `i^*𝓕`.
* For a finite surjection `ε:X'_0→X_0`, adjunction and the nonempty geometric fibers give `j_*𝓕↪ε_*j'_*ε^*𝓕`. Finite pullback and pushforward preserve the weight condition. For pushforward, the Frobenius blocks correspond to residue extensions, and taking the appropriate power converts eigenvalues to those of the original closed-point fiber; `w_{q^f}(α^f)=w_q(α)` verifies the unchanged weights.
* If `𝓕` is lisse and `k:V_0↪U_0` is dense, `j_*𝓕↪(jk)_*k^*𝓕`. One can shrink until the complement in a normal ambient scheme is a divisor and the sheaf has constant rank and pure weight.
* If `X_0` is normal, let `i:F_0=X_0−U_0↪X_0` and choose a dense open `k:V_0↪F_0`. Then `i^*j_*𝓕↪k_*k^*i^*j_*𝓕`. At a geometric point `x` of the boundary, choose successive generalizations `x→y→z` into `V_0` and `U_0`. The strict-local complement is connected by normality, so the boundary stalk injects into the generic lisse stalk. This injection factors through the stalk of `k_*k^*i^*j_*𝓕`, proving the claimed injectivity.

Stratification and the first two steps reduce to pure lisse input; normalization and a finite cover remove wild ramification at the finitely many generic boundary divisors. Shrinking around these generic points gives the smooth-divisor situation of DLM11. The remaining boundary has smaller dimension, so the last injection and the induction hypothesis extend the bound to it. This is (1.8.9); the finite-cover and constructibility inputs are those cited by Deligne, not new assumptions about the programme's base.

For a lisse sheaf on `X_0` that is pure of weight `β` on a dense open, the injections of the sheaf and of its dual into their open direct images give respectively weights `≤β` and `≥β`. Thus it is pure everywhere. On a normal connected scheme an irreducible lisse sheaf stays irreducible on every nonempty open; a mixed such sheaf is therefore pure after shrinking, and hence everywhere. Taking a composition series proves that a mixed lisse sheaf on a normal scheme has lisse pure successive quotients.

If a mixed lisse sheaf on a connected scheme is pure at one point, normalization shows purity of that same weight on every irreducible component through that point. Repeating across components makes the pure locus both open and closed; connectedness forces it to be the entire scheme. These arguments preserve integral weights when the input weights are integral, and hold for all embeddings `ι` when the input is pure rather than merely `ι`-pure.

The Hodge-theoretic text (1.8.14)–(1.8.15), printed pages 178–179, formulates an **open problem in that text** about good mixed Hodge variations on a punctured disk, relative monodromy, and nilpotent orbits. It is not an additional proved theorem in these sections. The requested relative filtration is precisely the displayed formula (DLM11.1) without the finite-field Tate-line notation, and the suggested nilpotent-orbit comparison uses `exp(−uN)` on the Hodge filtration. No solution of that historical problem is imported into this reconstruction.

## DLM13. Positive combinations of tame logarithms are realized by actual curves

**Source:** (1.9.1), (1.9.3), printed pages 179–181.

Let `X` be smooth over `F_q`, `D=⋃D_i` a normal-crossing divisor as in DLM7, and `𝓕` lisse and tame on `X−D`. Assume its given filtration `W` has pointwise pure degree-`a` quotients of weight `a`. Put `G=𝓕[E]` and keep all maps `N_i:G(1)→G`.

For each family of **positive integers** `c_i`, set

\[
N_c=\sum_{i\in I}c_iN_i.
\tag{DLM13.1}
\]

This operator is not chosen on grounds of numerical positivity. It is obtained from a concrete pullback. At a closed point `x∈E`, make a finite extension of the ground field so that `x` is rational, retaining the Frobenius-power comparison. Complete the equations `t_i` to étale local coordinates `(t_i,u_j)`. Map an affine line with parameter `t` to the coordinate affine space by

\[
t\longmapsto(t_i=t^{c_i},\ u_j=0).
\tag{DLM13.2}
\]

The fiber product with the chosen étale neighborhood of `X` is a smooth curve near the selected point: its projection to the affine line is étale by base change. On the punctured curve, its generic stalk is `G_{\bar x}`. Pulling back a Kummer root of `t_i` gives a root of `t^{c_i}`. Thus a tame loop in the curve maps to `c_i` times that loop in the `i`th inertia coordinate. Taking logarithms in (DLM7.2) gives **exactly** (DLM13.1), including every coefficient.

DLM11 applied to this actual curve proves that `N_c` has relative monodromy filtration on `G_{\bar x}`, whose degree-`a` piece is pure of weight `a`. The uniqueness from DLM4 makes the fiber filtration invariant under the lisse parallel-transport action, so it forms a filtration by lisse subsheaves of `G`. At every closed point it is characterized as the filtration by Frobenius weights. It therefore does not depend on the chosen positive integers `c_i`.

For positive rational `c_i`, multiply all coefficients by one positive integer `m` to make them integral. Replacing `N_c` by `mN_c` changes the `b`th iterated map by the nonzero scalar `m^b` and hence changes neither the filtration nor any assertion that the map is an isomorphism. This proves the same result for all positive rational coefficient vectors. No assertion about arbitrary real, negative, or vanishing coefficients follows from this argument.

## DLM14. The complete system of relative filtrations on all strata

**Source:** theorem (1.9.2), proof (1.9.4), printed pages 180–181.

For filtrations `W',W''` on a sheaf and a family `N_α`, Deligne's condition `L(W',W'',(N_α))` means:

1. every `N_α` preserves `W'`;
2. `N_αW''_a(1)⊂W''_{a−2}`;
3. for every family of positive rational `c_α` and every `b≥0`,

\[
\left(\sum_\alpha c_\alpha N_\alpha\right)^b:
\left(\operatorname{Gr}_{a+b}^{W''}\operatorname{Gr}_a^{W'}G\right)(b)
\xrightarrow{\sim}
\operatorname{Gr}_{a-b}^{W''}\operatorname{Gr}_a^{W'}G.
\tag{DLM14.1}
\]

There exists a unique system `W(J)`, indexed by **every** subset `J⊂I`, on `G=𝓕[E]`, stable under the full `Z_L(1)^I` action, such that

\[
W(\varnothing)=W[E],\qquad
L\bigl(W(J),W(K),(N_k)_{k\in K-J}\bigr)
\quad(J\subsetneq K).
\tag{DLM14.2}
\]

Furthermore `Gr_a^{W(I)}G` is pointwise pure of weight `a`.

**Construction.** Apply DLM13 on `X_J` along the components indexed by `J`. It gives a weight filtration on `𝓕[D_J^*]`, call it `W(J)`, relative to the original `W` and to all positive combinations of `N_j`, `j∈J`. For `J⊂K`, apply DLM13 again on `D_J` along the additional components `K−J`, now with input filtration `W(J)`. It gives a weight filtration on

\[
\mathcal F[D_J^*][D_K^*].
\]

The exact specialization isomorphism (DLM7.3) identifies this sheaf, its Frobenius and each inertia operator with `𝓕[D_K^*]`. The filtration just constructed and the filtration obtained directly for `K` are both its Frobenius weight filtration, so DLM6 identifies them. This proves (DLM14.1) on the `K`-stratum. Specialize once more to `E`, using exactness of the functor to preserve the graded isomorphisms. Define the resulting filtration on `G` to be `W(J)`. This proves every compatibility in (DLM14.2), and transitivity of (DLM7.3) proves independence of the sequence of strata.

**Uniqueness.** The relative-monodromy condition for `∅⊂J`, with one positive coefficient vector, already forces `W(J)` by DLM4. Thus two systems agree subset by subset. Invariance under the remaining inertia operators also follows from uniqueness: they preserve the original filtration and commute with the chosen logarithm, so they take its relative filtration to another one with the same defining properties.

The construction treats all allowed positive combinations simultaneously. It does not derive a universal positivity form on an arbitrary space from the existence of a fixed supporting point.

## DLM15. What §1.9's final remarks establish, and the exact mechanism received here

**Source:** (1.9.5)–(1.9.6), printed page 181.

Deligne announces a fiberwise variant for a smooth family `X→S` over a finite-type `Z` scheme with a **relative** normal-crossing divisor and a tame lisse sheaf. The text says this is checked on fibers using (1.9.2); it does not state a complete separate list of filtration hypotheses and conclusions. This reconstruction does not manufacture a stronger global theorem from that remark. The same paragraph explicitly distinguishes the case of a normal-crossing divisor in a regular arithmetic scheme, including `Spec Z[1/ℓ]`, as inaccessible to that argument. The distinction is part of the original source, not a verdict about the programme.

The added-in-proof remark attributes to Cattani and Kaplan the corresponding **pure** Hodge-variation statement on `(D*)^I`, where positive real coefficients are permitted. Their proof is not reproduced in §§1.6–1.9 and has not been read for this file; no claim of that further reconstruction is made.

The exact weight-control mechanism now reconstructed is the following chain of actual maps and conclusions:

\[
\begin{array}{c}
\text{full curve trace formula, including }H_c^0,H_c^1,H_c^2
\\\Downarrow\quad\text{all tensor powers through }(V^I)^{\otimes r}\hookrightarrow(V^{\otimes r})^I
\\ |\iota\alpha|\le Q^{\beta/2}\text{ on boundary invariants}
\\\Downarrow\quad P_{-j}^{\otimes2}(-j)\hookrightarrow P_0(V^{\otimes2})
\\ |\iota\alpha|\le Q^{(\beta-j)/2}
\\\Downarrow\quad P_{-j}(V^*)\cong P_{-j}(V)^*(j)
\\ |\iota\alpha|\ge Q^{(\beta-j)/2}
\\\Downarrow\quad\operatorname{Gr}_i V\cong\bigoplus_jP_{-j}(-(i+j)/2)
\\ |\iota\lambda|=Q^{(\beta+i)/2}\text{ on every degree-}i\text{ graded piece}.
\end{array}
\tag{DLM15.1}
\]

For mixed tame input, the independently constructed curves `t_i=t^{c_i}` realize all positive rational combinations of logarithms. Weight-filtration uniqueness and the exact specialization isomorphisms then identify their relative filtrations. Those are the objects and maps that have actually been calculated here. In particular, this local theorem neither chooses an origin called zero nor obtains its radius by replacing a zero with another supporting point.
