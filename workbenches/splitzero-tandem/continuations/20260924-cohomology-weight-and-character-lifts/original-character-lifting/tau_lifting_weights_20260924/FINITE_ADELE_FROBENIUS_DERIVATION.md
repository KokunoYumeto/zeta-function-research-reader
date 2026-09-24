# Finite adele support and arithmetic Frobenius in the distribution realization

Independent derivation, 24 September 2026.

This calculation restores the finite adele variables and the source's arithmetic Frobenius to the previously constructed distribution realization. The maps, residue, rational quotient action, and a finite-boundary contribution are computed explicitly. The resulting exact maps concern the stated distribution receiver; no identification with primitive \(Z_1/\tau\) or with the complete cohomology of the adelic complex lift is presumed.

## FA0. Controlling sources and prerequisite check

Alain Connes and Caterina Consani, [*The Riemann–Roch strategy: Complex lift of the Scaling Site*, arXiv:1805.10501v1](https://arxiv.org/abs/1805.10501v1), is the human source. The original author file read is

`thecurve_K.tex`; its exact local path and source identity are retained in the private source-use ledger.

The exact source locators are:

- §5.2, Lemma adelicomp1 and equations actionpq, adelicomp3, lines 1203–1224: \((x,y)\mapsto(ax+b,ay)\), \(\bar\partial=\partial_x+i\partial_y\), and \(P(\mathbb Q)\backslash\mathbb A_{\mathbb Q}^2\).
- §6.6, the paragraph before Proposition comparescalcs, lines 2381–2418: the vector fields \(y\partial_x,y\partial_y\) and their full factor \(y\).
- §7 and §7.1, lines 2532–2601: right vertical scaling, the coefficient maps \(\theta_\mu([r])=[r^\mu]\), the evaluation \(\chi_\lambda([r])=r^\lambda\), and arithmetic Frobenius \(\operatorname{Fr}^a_\mu=\theta_\mu R(\mu^{-1})\).
- §7.1, equations holom2 and Proposition functionq, lines 2602–2624: the moving Teichmüller coefficient. That function \(q\) is different from the auxiliary quotient \(q_\rho\) used below.

The preceding programme derivations used here are:

- [SDB receiver](../independent/CC_SUPPORTED_DOLBEAULT_BOUNDARY.tex), SDB18–SDB31 and SDB40–SDB57.
- [DR realization](DISTRIBUTION_REALIZATION_OF_B_INDEPENDENT.md), DR1–DR8.
- [Original auxiliary lifting calculation](TAU_LIFTING_AND_WEIGHT_SEPARATION.md), TL2–TL3.

Before deriving the comparison, the current operation rules (private construction record; not included), the complete quoted definitions U01–U18, and the complete user passages USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2, USR-6152e3bc6302258c, USR-508e136619bfced2, and USR-4322be19bff532cd in the retained user corpus were read. These passages require the whole arithmetic construction and forbid replacing the source by an invented numerical model. Every calculation below consequently takes place in a stated arithmetic receiver after the existing arithmetic reconstruction. None counts copies of \(\tau\), assigns source parity, or restores the retracted source addition. In FA7 the comparison changes because an actual finite-support contribution is restored; that result does not contradict a definition of primitive \(\tau\).

The symbols have distinct domains:
\[
 \begin{array}{c|l}
 (X_f,Y_f)&\text{finite adele coordinates}\\
 (X,Y)&\text{archimedean coordinates}\\
 x,y,t&\text{variables of the existing finite complex algebras}\\
 \lambda,\mu&\text{positive real evaluation and Frobenius parameters}\\
 q_\rho&\text{the auxiliary algebra quotient }x\mapsto t,\ y\mapsto0\\
 p&\text{a rational prime}.
 \end{array}
\]

## FA1. Exact test spaces and finite pullback

Let \(\mathbb A_f\) be the finite adeles of \(\mathbb Q\). On each \(\mathbb Q_\ell\), fix additive Haar measure with \(\mathbb Z_\ell\) of mass \(1\), and use the product measure on \(\mathbb A_f^2\). Put
\[
 \mathscr S_f=C_c^{\mathrm{lc}}(\mathbb A_f^2),\qquad
 \mathscr V_f=\mathscr S_f',
\tag{FA1.1}
\]
where the dual consists of continuous complex linear functionals on the usual Bruhat test-function space. A locally integrable function denotes its distribution relative to this measure.

For \(a\in\mathbb Q^\times,b\in\mathbb Q\), set
\[
 L_f(a,b)(X_f,Y_f)=(aX_f+b,aY_f).
\]
Its scalar-distribution pullback is
\[
 \langle P_f(a,b)v,\psi\rangle
  =|a|_f^{-2}
       \left\langle v,
         \psi\!\left(\frac{X_f-b}{a},\frac{Y_f}{a}\right)
       \right\rangle,\qquad
 |a|_f=\prod_{\ell<\infty}|a|_\ell.
\tag{FA1.2}
\]
This is a distribution because the affine map carries compact locally constant test functions to such test functions and is continuous on their test-function space. Substitution proves that it agrees with composition for functions. The support is transformed exactly by
\[
 \operatorname{supp}P_f(a,b)v
     =L_f(a,b)^{-1}\operatorname{supp}v.
\tag{FA1.3}
\]
The inclusion in one direction follows by testing away from that inverse image; the reverse inclusion follows by applying the inverse pullback. For a compact-open box,
\[
 1_{(u+U)\times(v+V)}
 \longmapsto
 1_{((u-b)/a+a^{-1}U)\times(v/a+a^{-1}V)}.
\tag{FA1.4}
\]
For a point mass,
\[
 P_f(a,b)\delta_{(u,v)}
    =|a|_f^{-2}\delta_{((u-b)/a,v/a)}.
\tag{FA1.5}
\]
These different coefficient factors must not be interchanged.

The elementary product formula in this situation is
\[
 |a|_f=|a|_\infty^{-1}.
\tag{FA1.6}
\]
Indeed write \(a=\epsilon\prod_p p^{n_p}\), with finitely many nonzero integer \(n_p\) and \(\epsilon=\pm1\). Then
\(\prod_p|a|_p=\prod_p p^{-n_p}=|a|_\infty^{-1}\).
Consequently the finite two-variable Jacobian in (FA1.2) is
\(|a|_\infty^2\). The archimedean two-variable scalar pullback
has factor \(|a|_\infty^{-2}\). Their product is exactly \(1\)
on the entire rational adelic affine map. This cancellation is
proved while retaining both original factors; it is not a choice
to omit finite support.

We will use two specific finite distributions:
\[
 h_0=1_{X_f}\otimes1_{Y_f},\qquad
 h_1=1_{X_f}\otimes\delta_0(Y_f).
\tag{FA1.7}
\]
Their pairings are respectively integration over \(\mathbb A_f^2\)
and \(\psi\mapsto\int_{\mathbb A_f}\psi(X_f,0)\,dX_f\).
Both are distributions although their supports are not compact:
the tests are compactly supported. Their exact supports and actions are
\[
 \begin{aligned}
 \operatorname{supp}h_0&=\mathbb A_f^2,&
 P_f(a,b)h_0&=h_0,\\
 \operatorname{supp}h_1&=\mathbb A_f\times\{0\},&
 P_f(a,b)h_1&=|a|_\infty h_1.
 \end{aligned}
\tag{FA1.8}
\]
For the second equality, substitute \(X_f'=(X_f-b)/a\) in
(FA1.2): its measure factor is \(|a|_f\), leaving
\(|a|_f^{-1}=|a|_\infty\). For the first, the two substitutions
cancel the full inverse determinant. The distributions are
linearly independent: a test supported away from \(Y_f=0\)
annihilates \(h_1\) but need not annihilate \(h_0\).

### FA1a. Entry from finite functions, and the exact current enlargement

Neither the existence of \(\mathscr V_f\) nor the displayed
delta current is asserted to be part of an unexamined
source sheaf. The source paper constructs its adelic quotient
and discusses \(W\)-valued functions; the distribution
receiver here is an explicitly constructed enlargement.
Its entry from the finite function space is
\[
 j_0:C_c^{\mathrm{lc}}(\mathbb A_f^2)\longrightarrow
       \mathscr V_f,\qquad
 j_0(f)(\psi)=\int_{\mathbb A_f^2}f\psi.
\tag{FA1a.1}
\]
It is injective: if a locally constant \(f\) is nonzero
at a point, choose a compact-open neighborhood where its
value is a nonzero constant and test by the indicator of
that neighborhood. It intertwines scalar pullbacks by
substitution in (FA1.2). The same formula defines the
sheaf of locally constant functions as locally integrable
distributions without a compact-support requirement;
compact test functions still make the pairing finite.

Let \(D_f=\mathbb A_f\times\{0\}\) and identify it with
\(\mathbb A_f\) using \(X_f\). Restriction of a locally
constant function to \(D_f\) is defined pointwise. Put
\[
 i_f^*f(X_f)=f(X_f,0),\qquad
 j_1(g)(\psi)=\int_{\mathbb A_f}g(X_f)\psi(X_f,0)\,dX_f.
\tag{FA1a.2}
\]
Both maps are defined on compactly supported locally
constant functions and also on the corresponding
sheaves without compact support. The map \(j_1\) is
injective by the same compact-open testing argument.
Thus the exact source-to-current map is
\[
 \Lambda_f=j_1 i_f^*,\qquad
 \Lambda_f(f)=f(X_f,0)\delta_0(Y_f).
\tag{FA1a.3}
\]
On the constant function \(1\), it gives \(h_1\).
On the genuine finite test function
\(1_{\widehat{\mathbb Z}\times\widehat{\mathbb Z}}\),
it gives \(1_{\widehat{\mathbb Z}}(X_f)\delta_0(Y_f)\).
Thus the construction is available on finite compact-open
data as well as on global constants.

This delta current is not a regular finite function.
The subset \(\{0\}\subset\mathbb A_f\) has Haar measure
zero: in a compact neighborhood it lies inside the sets
with one fixed prime component restricted to
\(\ell^n\mathbb Z_\ell\), whose measures tend to zero.
Hence \(D_f\) has product Haar measure zero locally.
A regular locally integrable distribution supported on
\(D_f\) must be zero, since its density vanishes almost
everywhere outside \(D_f\), and \(D_f\) has measure zero.
But \(j_1(g)\ne0\) for \(g\ne0\), by injectivity.
Consequently \(h_1\), and every such nonzero divisor
current, lies outside the regular-function entry (FA1a.1).

The exact affine covariance of this new entry is
\[
 \boxed{
 P_f(a,b)\Lambda_f(f)
     =|a|_\infty\,\Lambda_f(P_f(a,b)f).
 }
\tag{FA1a.4}
\]
Indeed (FA1.2) applied to (FA1a.3), followed by the
one-variable substitution in \(X_f\), gives
\[
 |a|_f^{-1}f(aX_f+b,0)\delta_0(Y_f).
\]
Use (FA1.6) to obtain (FA1a.4).
This is precisely the finite factor used later;
it is not inferred from a dimension analogy.

The map is local in the sheaf sense. For every open
subset \(U\subset\mathbb A_f^2\), the same restriction
and pairing formulas give a map from locally constant
functions on \(U\) to distributions on \(U\), and these
maps commute with restriction to smaller open subsets.
For a locally constant multiplier \(a_f\) on \(U\),
\[
 \Lambda_f(a_f f)
     =a_f\,\Lambda_f(f),\qquad
 \operatorname{supp}\Lambda_f(f)
     \subseteq\operatorname{supp}f\cap D_f.
\tag{FA1a.5}
\]
The first identity holds because multiplication of a
delta current restricts the multiplier to \(D_f\).
The support assertion follows by testing where \(f\)
vanishes or away from \(D_f\). Thus no global coefficient
projection is needed to construct this map from finite
functions.

For an exact common coefficient space on which it is
an endomorphism, define the sheaf
\[
 \mathscr V_f^{\mathrm{reg,0}}(U)
   =j_0(C^{\mathrm{lc}}(U))
       \oplus j_1(C^{\mathrm{lc}}(U\cap D_f)).
\tag{FA1a.6}
\]
The direct-sum assertion follows from the measure-zero
argument: an equality of a regular distribution and a
zero-stratum current forces both to vanish. Restrictions
preserve the two summands, and \(P_f(a,b)\) preserves
their types by (FA1a.4). Define
\[
 \widetilde\Lambda_f(j_0(f)+j_1(g))=j_1(i_f^*f).
\tag{FA1a.7}
\]
This map is well-defined by uniqueness of the
decomposition, commutes with restrictions, is linear
over the locally constant function sheaf, and kills
the zero-stratum summand. It has
\(\widetilde\Lambda_f^2=0\), and its affine covariance
is (FA1a.4) with both input types included.

It also preserves every filtration defined by
geometric support containment: if a distribution
of (FA1a.6) has support in a closed set \(Z\), both
of its regular and zero-stratum parts have support in
\(Z\), by uniqueness of the decomposition on the
open complement; (FA1a.5) then puts its image in
\(Z\). In particular it maps the whole coefficient
space into the zero-stratum support step and maps that
step to zero. Equality of supports is not claimed:
\(h_0\) has support \(\mathbb A_f^2\), while
\(\widetilde\Lambda_fh_0=h_1\) has support \(D_f\).
Any external lattice index is separate from this
geometric support change.

## FA2. Both archimedean charts and the rational action

Retain the open domain
\[
 \Omega^\times=\mathbb R\times\mathbb R^\times.
\tag{FA2.1}
\]
Its two components are indexed by \(\sigma\in\{+1,-1\}\),
with \(\sigma Y>0\). This adds the negative chart to DR
without inserting the excluded stratum \(Y=0\).
For \(\rho\in\mathbb C\), \(m\ge1\), \(\alpha=\rho+1\), define
\[
 g_{\sigma,r}(Y)
   =1_{\{\sigma Y>0\}}|Y|^\alpha
                \frac{(\log|Y|)^r}{r!},\qquad r\ge0.
\tag{FA2.2}
\]
The indicator is smooth on the disconnected open set
\(\mathbb R^\times\). For each \(c\in\mathbb Q\),
\[
 \Phi_{c,\sigma}(x^uy^j)
       =\delta^{(j)}(X-c)\otimes g_{\sigma,m-j-1-u},
 \qquad u+j<m.
\tag{FA2.3}
\]
The same test-function and logarithmic-polynomial arguments as
DR1 prove injectivity. With
\[
 \mathscr J=Y\partial_Y-\alpha,\qquad
 \mathscr N=\partial_X\mathscr J,
\]
one still has \(\mathscr J\Phi=\Phi M_x\) and
\(\mathscr N\Phi=\Phi M_y\), because
\(Y\partial_Y\log|Y|=1\) on both components.

For arbitrary nonzero real \(a\), scalar pullback satisfies
\[
 P_\infty(a,b)
   (\delta_c^{(j)}\otimes g)
   =|a|^{-1}a^{-j}
       \delta_{(c-b)/a}^{(j)}\otimes Q_ag,\qquad
 Q_ag(Y)=g(aY).
\tag{FA2.4}
\]
The factor \(a^{-j}\), including its sign, comes from the
\(j\)-th derivative of the test function; the factor \(|a|^{-1}\)
comes from the normal Jacobian. Thus, writing
\(\varepsilon=\operatorname{sgn}(a)\),
\[
 \boxed{
 P_\infty(a,b)\Phi_{c,\sigma}(x^uy^j)
  =\varepsilon^j|a|^{\rho-j}
     \sum_{k=0}^{m-j-1-u}\frac{(\log|a|)^k}{k!}
       \Phi_{(c-b)/a,\,\sigma\varepsilon}(x^{u+k}y^j).
 }
\tag{FA2.5}
\]
The formula follows by expanding
\((\log|aY|)^r/r!\) with every binomial coefficient retained.
It specializes exactly to DR2.5 for positive \(a\).

On \(\mathscr V_f\otimes\Phi(B)\) the full left rational
pullback is
\[
 \mathcal P(a,b)=P_f(a,b)\otimes P_\infty(a,b).
\tag{FA2.6}
\]
The tensor product is algebraic. It embeds injectively into
distributions on the product test space
\(\mathscr S_f\otimes C_c^\infty(\Omega^\times)\).
For injectivity, express a tensor using finitely many independent
finite distributions; test functions give enough independent
evaluations to isolate their coefficients, and then the
archimedean distribution independence applies. No completion
or unspecified infinite tensor sum is used.

The full support in (FA2.6) changes by (FA1.3) at finite places
and by \((c,\sigma)\mapsto((c-b)/a,\sigma\varepsilon)\)
at infinity. The rational pullbacks obey
\[
 \mathcal P(a,b)\mathcal P(a',b')
   =\mathcal P(a'a,a'b+b').
\tag{FA2.7}
\]
This is the exact right action, or the left action after group
inversion. Arithmetic Frobenius below commutes with this action.

## FA3. The full family complex and its residues

Let
\[
 \mathcal J_{\mathbb Q,\pm}
  =\bigoplus_{c\in\mathbb Q}\bigoplus_{\sigma=\pm1}
      \bigoplus_{j\ge0}
        \delta_c^{(j)}\otimes
        \mathcal D'(\{Y:\sigma Y>0\}).
\tag{FA3.1}
\]
Only finite sums are allowed in each element. Define
\(\mathcal J_f=\mathscr V_f\otimes\mathcal J_{\mathbb Q,\pm}\).
For \(\lambda>0\), the original character-family operators are
\[
 D_\lambda=\lambda\partial_X+i\partial_Y,\qquad
 \mathcal L_\lambda=Y D_\lambda.
\tag{FA3.2}
\]
They act identically on finite distributions and branch labels.
Their complete residues on the archimedean normal jets are
\[
 R_\lambda\!\left(\sum_j\delta_c^{(j)}\otimes g_j\right)
     =\sum_j(-i/\lambda)^j\partial_Y^jg_j,
\]
\[
 R_{Y,\lambda}\!\left(\sum_j\delta_c^{(j)}\otimes g_j\right)
     =\sum_j(-i/\lambda)^j
                         \partial_Y^j(Y^{-1}g_j).
\tag{FA3.3}
\]
They retain \(c,\sigma\) as separate target indices. The section is
\[
 E_Yh=\delta_c\otimes Yh
\tag{FA3.4}
\]
on each branch. The exact homotopy is
\[
 T_{Y,\lambda}
   \left(\sum_j\delta_c^{(j)}\otimes g_j\right)
   =\frac1\lambda\sum_{j\ge1}\sum_{k=0}^{j-1}
       (-i/\lambda)^k\delta_c^{(j-1-k)}
                   \otimes\partial_Y^k(Y^{-1}g_j).
\tag{FA3.5}
\]
All derivatives of \(Y^{-1}\) are retained by this formula;
expanding them gives
\[
\partial_Y^k(Y^{-1}g)
=\sum_{r=0}^k\binom kr(-1)^r r!
       Y^{-r-1}g^{(k-r)}.
\]

Direct differentiation and cancellation of adjacent terms give
\[
 \begin{gathered}
 R_{Y,\lambda}\mathcal L_\lambda=0,\qquad
 R_{Y,\lambda}E_Y=I,\qquad T_{Y,\lambda}E_Y=0,\\
 \mathcal L_\lambda T_{Y,\lambda}
       =I-E_YR_{Y,\lambda},\qquad
 T_{Y,\lambda}\mathcal L_\lambda=I.
 \end{gathered}
\tag{FA3.6}
\]
For clarity, before multiplying by \(Y\), the terms of
\(D_\lambda\) are
\(\lambda\delta_c^{(j+1)}\otimes g+
i\delta_c^{(j)}\otimes g'\).
In its residue their coefficients sum to
\(\lambda(-i/\lambda)^{j+1}+i(-i/\lambda)^j=0\).
In the homotopy, the same cancellation leaves only the starting
jet and its residue section. The highest normal coefficient
proves injectivity of \(D_\lambda\) because \(\lambda\ne0\);
it then proves the last identity. Multiplication by \(Y\)
and \(Y^{-1}\) in their displayed order gives (FA3.6).
Tensoring these explicit identities by the identity of
\(\mathscr V_f\) and taking finite branch sums proves them
on \(\mathcal J_f\), without an exactness assumption on a
completed tensor product.

Now form the precisely specified family spaces
\[
 \mathcal C^0_f=\prod_{\lambda>0}\mathcal J_f,\qquad
 \mathcal C^1_f=\prod_{\lambda>0}\mathcal J_f,\qquad
 \mathcal H_f=
 \prod_{\lambda>0}\left(
  \mathscr V_f\otimes
   \bigoplus_{c,\sigma}\mathcal D'(\sigma Y>0)\right).
\tag{FA3.7}
\]
Each individual component has finite tensor and branch support.
No common finite bound as \(\lambda\) varies is imposed.
The componentwise operators give the split exact sequence
\[
 0\longrightarrow\mathcal C^0_f
 \xrightarrow{\mathcal L}\mathcal C^1_f
 \xrightarrow{\mathcal R}\mathcal H_f
 \longrightarrow0,
\quad
 u\longmapsto(\mathcal Ru,\mathcal Tu),\quad
 (h,k)\longmapsto\mathcal Eh+\mathcal Lk.
\tag{FA3.8}
\]
Both compositions equal the identity by (FA3.6). This constructs
the receiver and proves its exactness.

For \(a\in\mathbb Q^\times\), the **raw** residues obey
\[
 R_\lambda P_\infty(a,b)
      =|a|^{-1}Q_aR_\lambda,\qquad
 R_{Y,\lambda}P_\infty(a,b)
      =\varepsilon Q_aR_{Y,\lambda},
\tag{FA3.9}
\]
with the indicated branch changes. The first identity follows
from \(|a|^{-1}a^{-j}\) in (FA2.4) and \(a^j\) from the
derivative of \(Q_a\). The second follows from
\(Y^{-1}P_\infty(a,b)=aP_\infty(a,b)Y^{-1}\).
The original \(D_\lambda\) cochain action has
\[
 \rho^0(a,b)=\mathcal P(a,b),\qquad
 \rho^1(a,b)=a\mathcal P(a,b),
\tag{FA3.10}
\]
since \(D_\lambda\mathcal P=a\mathcal P D_\lambda\).
For \(\mathcal L_\lambda\), both degrees carry \(\mathcal P\).
The receiver action for either cochain presentation is
\[
 v\otimes h_{c,\sigma}
   \longmapsto
 P_f(a,b)v\otimes
       \varepsilon Q_a h_{c,\sigma}
 \quad\text{at }((c-b)/a,\sigma\varepsilon).
\tag{FA3.11}
\]
The sign \(\varepsilon\) is required on the negative component.
The section and homotopy commute with these actions: on \(E_Y\),
the factors are \(|a|^{-1}\) from \(\delta\) and \(a\) from
\(Q_a(Yh)\), yielding \(\varepsilon\). The homotopy factors
cancel as in (FA3.9), giving
\(T_{Y,\lambda}\mathcal P=\mathcal P T_{Y,\lambda}\).

## FA4. Original arithmetic Frobenius on the realization

Let \(B_\mu\), \(\mu>0\), be the pullback of the right geometric map
\[
 (X_f,Y_f,X,Y)\longmapsto(X_f,Y_f,X,Y/\mu).
\tag{FA4.1}
\]
It fixes the finite coordinates. At infinity its inverse Jacobian
is \(\mu\), and its exact distribution pairing is
\[
 \langle B_\mu u,\varphi\rangle
   =\mu\langle u,\varphi(X,\mu Y)\rangle.
\tag{FA4.2}
\]
Thus
\[
 B_\mu(\delta_c^{(j)}\otimes g)
      =\delta_c^{(j)}\otimes Q_{1/\mu}g.
\tag{FA4.3}
\]
There is no normal \(X\) scaling. The rational branch \(c\),
the sign chart \(\sigma\), and all finite-adele support are
unchanged.

The coefficient algebra used explicitly by Connes–Consani here is
\[
 W_{\rm alg}=\mathbb C[\mathbb R_{>0}^{\times}],
 \qquad \theta_\mu([r])=[r^\mu],\qquad
 \chi_\lambda([r])=r^\lambda.
\tag{FA4.4}
\]
The authors' Teichmüller notation is not primitive \(Z_1/\tau\).
Evaluation gives the injective map
\[
 \operatorname{ev}:W_{\rm alg}\otimes\mathcal J_f
   \longrightarrow\mathcal C^1_f,\qquad
 \sum_{r\in F}[r]\otimes u_r
      \longmapsto\left(\sum_{r\in F}r^\lambda u_r\right)_\lambda.
\tag{FA4.5}
\]
For distinct \(r_1,\ldots,r_n\), evaluations at
\(\lambda=1,\ldots,n\) have determinant
\((\prod_k r_k)\prod_{k<l}(r_l-r_k)\ne0\).
Applying the inverse matrix to vector-valued coefficients proves
injectivity. The map is not claimed onto the product family.
This is a degreewise entry of the algebraic coefficient
space. It is not asserted to be an inclusion of a full
original \(W_{\rm alg}\)-valued complex: multiplication by
\(\lambda\) in \(\mathcal L_\lambda\) need not preserve
the finite exponential-sum image (FA4.5). The differential
and its splitting are proved on the explicitly defined
family complex (FA3.7).

The exact original arithmetic action on the algebraic coefficients is
\[
 [r]\otimes u\longmapsto[r^\mu]\otimes B_\mu u.
\tag{FA4.6}
\]
Its family action is
\[
 (\mathfrak F_\mu u)_\lambda=B_\mu u_{\lambda\mu}.
\tag{FA4.7}
\]
Evaluation of (FA4.6) gives (FA4.7) directly. On the original
operator \(\mathcal L_\lambda\),
\[
 \mathcal L_\lambda B_\mu=B_\mu\mathcal L_{\lambda\mu},
\quad
 R_{Y,\lambda}B_\mu
    =\mu^{-1}Q_{1/\mu}R_{Y,\lambda\mu},
\tag{FA4.8}
\]
\[
 T_{Y,\lambda}B_\mu=B_\mu T_{Y,\lambda\mu},\qquad
 B_\mu E_Y=E_Y(\mu^{-1}Q_{1/\mu}).
\tag{FA4.9}
\]
For the first identity,
\(\partial_YB_\mu=\mu^{-1}B_\mu\partial_Y\),
\(\partial_XB_\mu=B_\mu\partial_X\), and
\(B_\mu Y=\mu^{-1}YB_\mu\).
For the residue, each term has the complete coefficient
\[
 (-i/\lambda)^j\mu^{-j-1}
     =\mu^{-1}(-i/(\lambda\mu))^j;
\]
the factor \(\mu^{-1}\) before the \(j\) derivatives is supplied
by \(Y^{-1}Q_{1/\mu}=\mu^{-1}Q_{1/\mu}Y^{-1}\).
The same termwise calculation proves the homotopy identity.
Thus the induced action on the actual residue receiver is
\[
 (\mathfrak F_\mu^H h)_\lambda
       =\mu^{-1}Q_{1/\mu}h_{\lambda\mu},
\tag{FA4.10}
\]
with every finite coefficient and branch label retained.

The corresponding original \(D_\lambda\)-complex has arithmetic
actions \(B_\mu u_{\lambda\mu}\) in degree \(0\) and
\(\mu^{-1}B_\mu u_{\lambda\mu}\) in degree \(1\).
Indeed \(D_\lambda B_\mu=\mu^{-1}B_\mu D_{\lambda\mu}\).
Its raw residue satisfies \(R_\lambda B_\mu
=Q_{1/\mu}R_{\lambda\mu}\); after the degree-one factor it
has exactly (FA4.10). The cochain isomorphism to the
\(\mathcal L\)-complex multiplies degree \(1\) by \(Y\).
It intertwines both actions because
\(Y\mu^{-1}B_\mu=B_\mu Y\). This preserves all original
cochain factors rather than treating them as optional twists.

On the exact DR realization, (FA4.3) yields
\[
 \boxed{
 \mathfrak F_\mu\bigl([r]\otimes v_f\otimes
             \Phi_{c,\sigma}(x^uy^j)\bigr)
  =[r^\mu]\otimes v_f\otimes
    \mu^{-(\rho+1)}
       \sum_{k=0}^{m-j-1-u}
          \frac{(-\log\mu)^k}{k!}
           \Phi_{c,\sigma}(x^{u+k}y^j).
 }
\tag{FA4.11}
\]
Here \(\mathfrak F\) means the algebraic action followed by
evaluation when required. The geometric calculation is simply
\[
 g_{\sigma,r}(Y/\mu)
    =\mu^{-(\rho+1)}
      \sum_{k=0}^r\frac{(-\log\mu)^k}{k!}g_{\sigma,r-k}(Y).
\]
The source arithmetic action therefore realizes
\[
 G_\mu=\mu^{-(\rho+1)}e^{-(\log\mu)J}
\tag{FA4.12}
\]
on every \(y\)-degree, together with \([r]\mapsto[r^\mu]\).
It commutes with both \(J\) and \(N\); it does not conjugate
\(N\) by \(\mu^{-1}\). At a rational prime \(p\), the scalar
and all nilpotent coefficients are \(p^{-(\rho+1)}\) and
\((-\log p)^k/k!\), respectively.

To see the precise cohomological cancellation, let
\[
 C_{j,h}(z)=[w^h]\prod_{k=0}^{j-1}(z+w-k),\qquad
 r_0=m-j-1-u.
\]
The full residue of (FA4.5) on a monomial is
\[
 \begin{aligned}
 &\left(\mathcal R\operatorname{ev}
   ([r]\otimes v_f\otimes\Phi_{c,\sigma}(x^uy^j))
       \right)_\lambda\\
 &\quad=
 r^\lambda v_f\otimes
 \sigma^{j+1}(-i/\lambda)^j
   1_{\{\sigma Y>0\}}|Y|^{\rho-j}
   \sum_{h=0}^{\min(j,r_0)}
      C_{j,h}(\rho)
       \frac{(\log|Y|)^{r_0-h}}{(r_0-h)!}.
 \end{aligned}
\tag{FA4.13}
\]
The sign \(\sigma^{j+1}\) comes from \(Y^{-1}\) and the
\(j\) derivatives on the negative chart. Applying (FA4.10)
introduces exactly
\[
 \mu^{-1}\,\mu^{-j}\,\mu^{-\rho+j}
      =\mu^{-(\rho+1)}
\tag{FA4.14}
\]
from the degree factor, \((\lambda\mu)^{-j}\), and vertical
scaling of \(|Y|^{\rho-j}\). The logarithm becomes
\(\log|Y|-\log\mu\), with the complete coefficients in
(FA4.11). The finite support remains unchanged.
Thus the original arithmetic Frobenius does not inherit a
different scalar eigenvalue at different \(j\) merely because
left dilation did.

## FA5. Exact comparison of left primes and arithmetic primes

For positive rational \(a\), define the horizontal-and-finite
operator
\[
 \mathcal H_a
   =P_f(a,0)\otimes(X,Y\mapsto aX,Y)^*.
\tag{FA5.1}
\]
It sends finite support through the inverse finite dilation,
and sends
\[
 \delta_c^{(j)}\otimes g
       \longmapsto
       a^{-j-1}\delta_{c/a}^{(j)}\otimes g
\tag{FA5.2}
\]
at infinity. Its finite two-coordinate Jacobian is \(a^2\);
the horizontal real Jacobian is \(a^{-1}\). Formula (FA5.2)
includes the derivative factor \(a^{-j}\) as well.
At the level of geometric maps,
\[
 B_a\,\mathcal P(a,0)=\mathcal H_a.
\tag{FA5.3}
\]
Indeed vertical scaling by \(1/a\) cancels the archimedean
vertical scaling by \(a\), while the finite and horizontal
coordinates are exactly those displayed in (FA5.1).
All scalar-distribution pullback factors multiply accordingly.

On algebraic \(W\) coefficients the complete identity is
\[
 \boxed{\mathfrak F_a\,\mathcal P(a,0)
       =\theta_a\,\mathcal H_a,\qquad
       \mathcal P(a,0)=
           \theta_a\mathcal H_a\mathfrak F_a^{-1}.}
\tag{FA5.4}
\]
These operations commute in this identity: \(\theta_a\)
changes only coefficient labels, \(B_a\) only the vertical
real coordinate, and \(\mathcal H_a\) the remaining displayed
coordinates. At \([r]\) the inverse arithmetic action changes
the label to \([r^{1/a}]\); the subsequent \(\theta_a\)
returns it to \([r]\). This accounts for the coefficient map
in the second identity.

For the invariant finite distribution \(h_0\) and the unit
coefficient \([1]\), (FA5.4) has the exact scalar product
\[
 a^{-j-1}\cdot a^{\rho+1}=a^{\rho-j},
\tag{FA5.5}
\]
and the inverse arithmetic logarithmic series has
\((\log a)^k/k!\). This recovers every term of the original
left action in DR. It explains where the \(j\)-dependent
factor lies: horizontal normal derivatives and finite
coefficient action are retained; they are not part of
(FA4.12) alone.

The quotient \(q_\rho\) and section \(i_\rho\) extend by
the identity on \(W_{\rm alg}\), finite distributions, and
branch indices. They commute with \(\mathfrak F_\mu\)
because \(q_\rho J=Tq_\rho\), \(Ji_\rho=i_\rho T\),
and (FA4.12) contains no additional \(y\)-mixing. They
commute with the rational affine action by (FA2.5).
The previously computed comparison with residue remains
exact, using (FA4.13) and its explicit \(j=0\) projection.
The quotient is still not a differential or a residue kernel.

For actual zeros with \(0<\Re\rho<1\), the residue in
(FA4.13) is injective on the algebraic \(W\)-coefficient,
finite-distribution realization of all retained blocks.
To verify this, first separate branches and finite linear
coefficient spans by test functions. The exponents
\(\rho-j\) are distinct for distinct pairs \((\rho,j)\):
equality forces the real difference of two numbers in
\((0,1)\) to be the integer \(j-j'\), hence forces
\(j=j'\), then \(\rho=\rho'\). Finite exponential-polynomial
independence therefore separates these blocks.
The derivative polynomial \(\prod_{k=0}^{j-1}(\rho+\partial_s-k)\)
is invertible on the finite logarithmic-polynomial space,
because \(\rho\notin\{0,\ldots,j-1\}\).
After undoing it and the nonzero \(\lambda^{-j}\), the
remaining \(r^\lambda\) coefficients are independent by
the Vandermonde argument in (FA4.5).
This proves the assertion without suppressing a finite
support factor or an evaluation parameter.

## FA6. The complete rational quotient cochain comparison

The split sequence (FA3.8) is equivariant for the full
rational affine group and the arithmetic Frobenius.
The finite coordinates commute with all archimedean
differential operators. Left affine maps commute with
right vertical scaling, so the two group actions commute.
Thus the existing homotopy gives an exact construction
after taking rational quotient group cochains, as follows.

Let \(\Gamma=P(\mathbb Q)\), and convert the right
pullbacks to left module actions by \(g\cdot v
=\mathcal P(g^{-1})v\), with the receiver action
(FA3.11). For a left \(\Gamma\)-module \(V\), define
\[
 C^r(\Gamma,V)=\operatorname{Map}(\Gamma^r,V)
\]
and use the full differential
\[
 \begin{aligned}
 (d_\Gamma f)(g_1,\ldots,g_{r+1})
  &=g_1 f(g_2,\ldots,g_{r+1})\\
  &\quad+\sum_{k=1}^r(-1)^k
       f(g_1,\ldots,g_kg_{k+1},\ldots,g_{r+1})\\
  &\quad+(-1)^{r+1}f(g_1,\ldots,g_r).
 \end{aligned}
\tag{FA6.1}
\]
All coefficient maps in (FA3.8) extend pointwise.
Their \(\Gamma\)-equivariance proves that they commute
with every term of (FA6.1).

Form the double complex with horizontal degree \(r\)
and vertical degrees \(0,1\) from \(\mathcal C_f^\bullet\).
Its total differential on horizontal degree \(r\) is
\[
 d_{\mathrm{tot}}=d_\Gamma+(-1)^r\mathcal L.
\tag{FA6.2}
\]
Put
\[
 \mathcal H_{\mathrm{tot}}=(-1)^r\mathcal T
     \text{ on }C^r(\Gamma,\mathcal C_f^1),
 \qquad \mathcal H_{\mathrm{tot}}=0
     \text{ on }C^r(\Gamma,\mathcal C_f^0).
\tag{FA6.3}
\]
In vertical degree \(1\), the two horizontal terms
\((-1)^r d_\Gamma\mathcal T\) and
\((-1)^{r+1}\mathcal Td_\Gamma\) cancel. The vertical
term is \(\mathcal L\mathcal T=I-\mathcal E\mathcal R\).
In degree \(0\), the surviving composition is
\(\mathcal T\mathcal L=I\). Therefore
\[
 d_{\mathrm{tot}}\mathcal H_{\mathrm{tot}}
   +\mathcal H_{\mathrm{tot}}d_{\mathrm{tot}}
       =I-\mathcal E\mathcal R
\tag{FA6.4}
\]
with \(\mathcal E\mathcal R\) understood as zero on
vertical degree \(0\). The maps \(\mathcal E,\mathcal R\)
are inverse on the residue complex, and (FA6.4) proves
the homotopy equivalence, with degree \(1\) retained:
\[
 H^n(\operatorname{Tot} C^\bullet
           (\Gamma,\mathcal C_f^\bullet))
       \cong H^{n-1}(\Gamma,\mathcal H_f)
       \quad(n\ge1),\qquad H^0=0.
\tag{FA6.5}
\]
The arithmetic action commutes with this entire
homotopy by (FA4.8)–(FA4.10), so the isomorphism is
arithmetic-Frobenius equivariant.

This is an exact rational-quotient calculation for the
defined finite-adele distribution complex. Its construction
does not require the invariant or coinvariant functor to
be exact. It is not a claim that this coefficient complex
already computes every sheaf or completed cohomology
of \(P(\mathbb Q)\backslash\mathbb A_{\mathbb Q}^2\).
In particular \(Y=0\) at infinity remains excluded,
and the full character product is not identified with
an unspecified completed \(W\)-coefficient sheaf.

## FA7. A finite boundary contribution changes the weight comparison

The previous DR uniqueness theorem concerned the
archimedean rational-orbit receiver. We now calculate,
rather than discard, the new kernel maps supplied
by an actual finite-adele boundary coefficient.

Let
\[
 V_f^{(01)}=\mathbb C h_0\oplus\mathbb C h_1
      \subset\mathscr V_f
\tag{FA7.1}
\]
with \(h_0,h_1\) from (FA1.7).
It is stable under the complete rational affine
action, by (FA1.8), and fixed pointwise by right
archimedean arithmetic Frobenius.
Take all finite rational branch sums on both sign charts:
\[
 A_{\rho,\mathbb Q,\pm}
    =\bigoplus_{c,\sigma} A_{\rho,c,\sigma},\qquad
 B_{\rho,\mathbb Q,\pm}
    =\bigoplus_{c,\sigma} B_{\rho,c,\sigma}.
\]
Let \(q=I\otimes q_\rho\) and \(i=I\otimes i_\rho\)
on the tensor products with \(V_f^{(01)}\).
The full maps are also tensored with \(W_{\rm alg}\)
when those source coefficients are retained.
No primitive source operation is involved.

For \(m\ge2\), define a complex-linear map into
the exact kernel of \(q\) by
\[
 \begin{aligned}
 H(h_0\otimes f(t)_{c,\sigma})
    &=\sigma h_1\otimes
           \bigl(y f(x)\bigr)_{c,\sigma},\\
 H(h_1\otimes f(t)_{c,\sigma})&=0.
 \end{aligned}
\tag{FA7.2}
\]
The linear map \(f(t)\mapsto yf(x)\) is well-defined
modulo \(t^m\) because \(yx^m=0\) in \(B_\rho\).
It kills \(t^{m-1}\), and \(qH=0\).
It is nonzero since \(H(h_0\otimes1_{c,\sigma})
=\sigma h_1\otimes y_{c,\sigma}\ne0\).

We prove full rational equivariance with all signs.
Write \(a=\varepsilon|a|\).
On \(h_0\otimes f(t)_{c,\sigma}\), the source
action sends it to
\[
 h_0\otimes |a|^\rho
      e^{(\log|a|)t} f(t)_{(c-b)/a,\sigma\varepsilon}.
\]
Applying \(H\) gives coefficient
\(\sigma\varepsilon |a|^\rho h_1\)
times \(y e^{(\log|a|)x}f(x)\).
In the other order, the finite factor in (FA1.8)
is \(|a|\), and the \(j=1\) normal factor in
(FA2.5) is \(\varepsilon |a|^{\rho-1}\).
Their product, including the original \(\sigma\),
is exactly
\[
 \sigma\cdot|a|\cdot
       \varepsilon|a|^{\rho-1}
       =\sigma\varepsilon|a|^\rho.
\tag{FA7.3}
\]
The logarithmic polynomial is identical in both orders.
On the \(h_1\)-source summand, both compositions are
zero because that summand is stable and \(H\) is zero
there. The rational branch change is the same in both
orders. Thus \(H\) commutes with full \(P(\mathbb Q)\).

It also commutes with the exact arithmetic action.
The finite coefficients and \(\sigma\) are unchanged,
and (FA4.12) commutes with multiplication by \(y\):
\[
 e^{-(\log\mu)x}\,y f(x)
       =y e^{-(\log\mu)x}f(x).
\tag{FA7.4}
\]
The source action on \(A_\rho\) is the same
\(\mu^{-(\rho+1)}e^{-(\log\mu)t}\).
The coefficient change \([r]\mapsto[r^\mu]\)
commutes with the identity on \(W_{\rm alg}\).
This proves arithmetic-Frobenius equivariance
on every displayed coefficient space.

There is a stronger, sheaf-local version of (FA7.2).
Use the coefficient sheaf (FA1a.6) or its compactly
supported sections, and set
\[
 H_{\mathrm{loc}}(v_f\otimes f(t)_{c,\sigma})
   =\sigma\,\widetilde\Lambda_f(v_f)
            \otimes(yf(x))_{c,\sigma}.
\tag{FA7.4a}
\]
On regular input, the finite operation is exactly
restriction to \(Y_f=0\) followed by current inclusion;
on zero-stratum input it is zero. Equation (FA1a.4) supplies
the factor \(|a|\), so the full calculation (FA7.3)
proves rational equivariance for every such finite
function or current, not only for the constant
two-dimensional coefficient space. Arithmetic
Frobenius leaves this finite operation unchanged,
and (FA7.4) proves its arithmetic equivariance.
The map is compatible with multiplication by finite
locally constant functions and with restriction to
finite-adele open sets. Its geometric support can only
decrease to \(D_f\), while its rational branch and
its sign chart are retained before applying a group
action. It is nonzero on compact finite tests, for
example by applying it to
\(1_{\widehat{\mathbb Z}^2}\otimes1_{c,\sigma}\).

This supplies an exact map **from** a finite
function input **into** the defined current enlargement.
The source paper's function complex is not thereby
declared closed under delta currents. If one restricts
both domain and codomain to regular finite functions,
this particular \(H_{\mathrm{loc}}\) is not an
endomorphism, because of the proved nonmembership in
FA1a. Sheaf-locality and a filtration by support
containment do not exclude it in the current receiver:
both properties have been proved. A different,
more restrictive source category must be specified
before making a claim that its morphisms contain
or exclude this map.

Consequently, for each \(z\in\mathbb C\),
\[
 \boxed{s_z=i+zH,\qquad q s_z=I}
\tag{FA7.5}
\]
is an exact section commuting with both full
rational affine action and arithmetic Frobenius.
The sections are distinct for distinct \(z\)
when \(m\ge2\), by the nonzero value in (FA7.2).
Replacing \(H\) by \(H_{\mathrm{loc}}\) gives the same
exact section family on the sheaf (FA1a.6), with all
maps compatible with finite-adele restrictions.
No choice of an off-critical zero is needed for
this construction. It holds for any specified
\(\rho\) and retained multiplicity \(m\ge2\).
If \(m=1\), the auxiliary kernel is zero and
this additional map is zero.

For a positive prime \(p\), the compensation
can be seen directly in the scalar eigenvalues:
\[
 \underbrace{p}_{\text{finite support }\mathbb A_f\times\{0\}}
 \cdot
 \underbrace{p^{\rho-1}}_{\text{normal order }j=1}
       =p^\rho.
\tag{FA7.6}
\]
Under the source arithmetic Frobenius all of
these \(j\)-blocks already have the common
scalar \(p^{-(\rho+1)}\), as calculated in
(FA4.11)–(FA4.14).
Thus the former archimedean weight gap is
filled by a specific retained finite boundary
factor in this enlarged receiver.

This result does not say that a lift fails:
the entire family (FA7.5) consists of lifts.
It proves that uniqueness by the earlier
archimedean weight comparison does not extend
unchanged to this explicit finite-adele object.
It also does not imply a zero of \(\zeta\)
outside the critical line. The new data are
the actual finite support, its modulus, and
the resulting exact equivariant kernel map.

## FA8. What is now available to the original specialization calculation

The mathematical connection now includes both
directions needed to use the existing auxiliary object:

1. Its complete jets embed into distributions with
finite adele coefficients by (FA2.3), (FA2.6).
All prime powers and logarithmic nilpotent terms
are retained.
2. Original source arithmetic Frobenius acts by
(FA4.11), with the complete residue action
(FA4.13)–(FA4.14). The exact relation to the
left prime action is (FA5.4).
3. The auxiliary quotient is recovered from
the injective residue image by the explicit
DR spectral projection, tensored with finite
coefficients and retaining the evaluation
parameter. It is not a boundary quotient.
4. The full rational group-cochain comparison
has the explicit equivariant homotopy (FA6.4).
This keeps the nonzero residue receiver and
does not replace the problem by an acyclic
finite-torus example.
5. The finite stratum \(Y_f=0\) has an explicit
effect on the actual lifting calculation,
given by (FA7.2)–(FA7.6).

Every displayed amplitude map preserves an
additional specified support index by
\((v,\lambda_0)\mapsto(f(v),\lambda_0)\).
For the historical lattice receiver this is
well-defined because all maps send amplitude
zero to amplitude zero. No index is identified
with another after cancellation. The arithmetic
evaluation parameter \(\lambda\) and the
retained lattice index \(\lambda_0\) are
different variables.

The remaining comparison is not filled by
renaming any vector-space zero as \(Z_1/\tau\).
The user’s primitive source, the full
finite-adele support, the archimedean
\(Y=0\) stratum, and the exact specialization
map retain their stated domains. The
constructed distribution group-cochain
receiver is an explicit receiving object
with proved maps, not an asserted replacement
for all of those objects.
