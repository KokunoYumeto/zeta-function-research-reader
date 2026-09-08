# Independent derivation of the first separated-edge electric covariance

8 September 2026. This calculation independently verifies the coefficient
in first_separated_electric_covariance.md. It also proves the exact domain
of its graph identity: the identity with the square of the edge adjacency
matrix is correct for distinct edges sharing no face. The unrestricted
matrix identity has additional incidence-degree terms, calculated below.
All statements use the original finite open box and actual vacuum.

## 1. Original operators, coordinates, and analytic vacuum coefficients

Fix an integer \(L\ge2\). The original vertex set is
\(\mathsf V_L=\{-L,\ldots,L\}^3\). A physical edge \(e=(n,i)\)
is positively directed from \(n\) to \(n+\mathbf e_i\), with both
endpoints in this set. The elementary face \(p=(n;i,j)\), \(i<j\),
has the oriented edge word
\[
(n,i)^+(n+\mathbf e_i,j)^+(n+\mathbf e_j,i)^-(n,j)^-.
\tag{1.1}
\]
Write \(\partial p\) for its underlying set of four physical edges.
No negative traversal is a new physical edge. The complete open sets
are denoted \(\mathsf E_L,\mathsf P_L\), with
\[
N=3(2L)(2L+1)^2,\qquad M=3(2L)^2(2L+1).
\tag{1.2}
\]
The three spatial directions and every contained boundary face are retained.

Each edge carries \(U_e\in SU(2)\). With product Haar probability
measure, use the conjugate-linear-first inner product on
\(\mathcal H=L^2(SU(2)^N,dU)\). Put
\[
\begin{split}
T_a&=-i\sigma_a/2,\qquad
X_{e,a}F=\left.\frac{d}{dt}
 F(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},\\
E_e&=-\sum_{a=1}^3X_{e,a}^2,\qquad H_0=\sum_eE_e,\\
W_p(U)&=\operatorname{tr}
 \bigl(U_i(n)U_j(n+\mathbf e_i)
       U_i(n+\mathbf e_j)^{-1}U_j(n)^{-1}\bigr),
\qquad S=\sum_{p\in\mathsf P_L}W_p,\\
H&=\kappa H_0+b\sum_{p\in\mathsf P_L}(2-W_p)
   =\kappa K_\xi+2bMI,\qquad K_\xi=H_0-\xi S,\\
\kappa&=\frac{2g^2}{a},\qquad b=\frac1{2g^2a},\qquad
\xi=\frac b\kappa=\frac1{4g^4},\qquad a>0,\ g>0.
\end{split}
\tag{1.3}
\]
The Casimir on spin \(j\) is \(j(j+1)\); in particular it is \(3/4\)
on a fundamental edge and 2 on a spin-one edge. The original metric
\(c(A,B)=-\operatorname{tr}(AB)/2\) has orthonormal frame \(2T_a\),
so \(-\Delta_e^c=4E_e\) and the electric term in that metric is
\((\kappa/4)\sum_e(-\Delta_e^c)\). This exact factor of four and
the full Wilson scalar \(2bM\) are retained.

Gauge transformations act by
\(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\). Their unitary action has an
orthogonal Haar-average projection onto the physical subspace
\(\mathcal H_{\rm phys}\). Every \(E_e\), \(W_p\), and \(H\)
commutes with this action: the edge Casimir is bi-invariant and the
holonomy transforms by conjugation at its base vertex. Thus all vacuum
coefficients and link-Casimir vectors used below obey the original Gauss
constraint. Integrating a shared link also preserves gauge invariance,
by invariance of its Haar measure under both endpoint actions.

The full operator is self-adjoint on \(H^2(SU(2)^N)\), has form domain
\(H^1\), and has compact resolvent. On the physical space the domains
are their intersections with \(\mathcal H_{\rm phys}\). The potential
is real, smooth, and bounded. The compact connected configuration
manifold gives a ground-state form minimizer; its modulus also minimizes
the form. Elliptic regularity and the strong maximum principle give a
smooth strictly positive ground vector. For that vector \(\psi\),
with \(H\psi=\mathcal E\psi\), product-rule integration by parts yields
\[
\mathfrak q_{H-\mathcal E}[\psi F]
 =\kappa\sum_{e,a}\int\psi^2|X_{e,a}F|^2dU.
\tag{1.4}
\]
Any other ground vector divided by \(\psi\) has zero right side and is
constant, proving uniqueness. Gauge transformations preserve the positive
unit vector, so the ground vector belongs to \(\mathcal H_{\rm phys}\).
Write that original unit vector as \(\psi_\xi\), and write
\(\mathcal E(\xi)=2bM+\kappa e(\xi)\).

The finite-volume expansions below are actual analytic derivatives, not
an assumed formal vacuum. Indeed the full free operator has simple
eigenvalue zero and first nonzero eigenvalue \(3/4\), from product
Peter--Weyl decomposition. On \(|z|=3/8\),
\[
\|(z-H_0)^{-1}\|\le\frac83,
\qquad \|S\|=2M.
\tag{1.5}
\]
The second equality follows from \(|W_p|\le2\), equality at the
all-identity configuration, and its positive-Haar-measure neighborhoods.
The resolvent Neumann series converges for
\(|\xi|<3/(16M)\). Its contour integral gives an analytic rank-one
projection near zero, hence an analytic eigenline and eigenvalue. On
the real axis choose positive overlap with the free constant vector
and the original unit norm; these choices give a real analytic
\(\psi_\xi\). This fixes its scalar coefficient rather than deleting it.

Analyticity holds in every fixed Sobolev space as well. If it holds in
\(H^s\), use the exact eigen-equation in the form
\[
\psi_\xi=(I+H_0)^{-1}
              [(1+e(\xi)+\xi S)\psi_\xi].
\tag{1.6}
\]
Multiplication by the smooth \(S\) is bounded on \(H^s\), and the
elliptic inverse maps \(H^s\) boundedly to \(H^{s+2}\). Starting at
\(s=0\), induction proves the assertion. In particular all operator
products and coefficient pairings below are legitimate on smooth
vectors; their Taylor errors are at fixed \(L\) and are not asserted
to be uniform in volume.

## 2. Derivation of the complete first and second vacuum coefficients

Write the actual fixed-volume expansion
\[
\psi_\xi=1+\xi A_1+\xi^2A_2+O_{H^k,L}(\xi^3),
\qquad
e(\xi)=e_1\xi+e_2\xi^2+O_L(\xi^3).
\tag{2.1}
\]
For every face, \(\int W_p=0\) and \(H_0W_p=3W_p\). For distinct
faces a physical link in only one boundary makes their product odd under
\(U_e\mapsto-U_e\), so
\(\langle W_p,W_q\rangle=0\). A single face holonomy has Haar law;
fundamental character orthogonality gives \(\|W_p\|^2=1\).
Consequently \(\|S\|_{L^2}^2=M\).

Comparing order one in \((H_0-\xi S)\psi_\xi=e(\xi)\psi_\xi\)
and integrating gives \(e_1=0\), and then
\(H_0A_1=S\). The unit-vector condition forces
\(\langle1,A_1\rangle=0\); the first coefficient is real, so its
constant part vanishes. Therefore
\[
A_1=\frac S3.
\tag{2.2}
\]
At order two,
\(H_0A_2=SA_1+e_2\). Its Haar integral gives
\(e_2=-M/3\), and the order-two unit-vector equation gives
\(2\langle1,A_2\rangle+\|A_1\|^2=0\). Thus, retaining the constant,
\[
H_0A_2=\frac{S^2-M}{3},\qquad
\langle1,A_2\rangle=-\frac M{18}.
\tag{2.3}
\]

We resolve every component of \(S^2-M\). For a repeated face,
\[
Y_p=W_p^2-1=\chi_1(U_p),\qquad
H_0Y_p=8Y_p,\qquad \|Y_p\|^2=1.
\tag{2.4}
\]
The character identity follows from
\(\frac12\otimes\frac12=0\oplus1\), and the four spin-one edges
contribute \(4\cdot2=8\). Character orthogonality gives the norm.
For distinct faces with disjoint physical-edge boundaries, the product
\(W_pW_q\) has fundamental spin on eight edges, hence free energy
\(8\cdot3/4=6\) and squared norm one. The norm follows by independent
Haar integrations of the two face holonomies, and remains valid when
their vertex sets intersect.

For distinct faces sharing an edge \(g_0\), let
\[
Z_{pq,0}=\int_{SU(2)}W_pW_q\,dU_{g_0},
\qquad Z_{pq,1}=W_pW_q-Z_{pq,0}.
\tag{2.5}
\]
The subscript \(g_0\) distinguishes this physical edge from the original
coupling \(g\). Two distinct elementary squares share at most one edge:
coplanar squares can share only one side, and perpendicular coordinate
squares intersect in at most one unit coordinate segment. Thus the two
faces in (2.5) have exactly six other physical edges, all distinct.

An \(SU(2)\) trace equals the trace of its inverse. Reverse one face
traversal if necessary and cyclically rotate its trace to write the two
factors as \(\operatorname{tr}(U_{g_0}B)\) and
\(\operatorname{tr}(U_{g_0}^{-1}D)\), where \(B,D\) are their actual
three-edge outer words. The fundamental Haar identity
\(\int U_{ij}\overline U_{k\ell}\,dU=\delta_{ik}\delta_{j\ell}/2\)
gives the exact projection map
\[
\boxed{Z_{pq,0}=\frac12\operatorname{tr}(BD).}
\tag{2.6}
\]
The factor \(1/2\) is retained. No replacement by a unit-norm six-edge
trace is made. The two fundamental factors on the shared edge decompose
into shared spin zero and one. Hence the complete channel data are
\[
\begin{array}{c|c|c|c|c}
\text{vector}&E_{g_0}&E_e\ (e\text{ outer})&H_0&\text{squared norm}\\ \hline
Z_{pq,0}&0&3/4&9/2&1/4\\
Z_{pq,1}&2&3/4&13/2&3/4.
\end{array}
\tag{2.7}
\]
For the first norm, the six-edge trace in (2.6) has squared norm one.
The total product has squared norm one: conditional on \(U_{g_0}\),
the two outer words are independent Haar elements, so the integral of
each squared fundamental trace is one. Link Haar averaging is an
orthogonal projection, so Pythagoras gives the second norm \(1-1/4=3/4\).
Both channels are gauge invariant, as already established in Section 1.

There are no omitted cross terms between different unordered pairs.
The odd central-link support of either channel associated with
\(\{p,q\}\) is \(\partial p\mathbin\triangle\partial q\).
For a shared edge both spins in (2.7) are integral and therefore even;
the six outer fundamental edges are odd. For an edge-disjoint pair all
eight boundary edges are odd. Suppose two different unordered pairs
had equal odd support. Their symmetric face difference would be a
nonempty mod-two closed collection of at most four elementary squares.
Each edge of any selected face in this collection would need another
selected face to cancel its boundary parity. Since two elementary
squares share at most one edge, its four edges would require four
distinct other squares. The collection would contain at least five
squares, a contradiction. Thus at least one physical link has different
central parity, and integration on that link kills the mixed inner product.

Every \(Y_p\) has even link parity everywhere, and is orthogonal to
the distinct-pair terms. Different \(Y_p,Y_q\) have unequal joint
link-spin assignments, because one face has a link absent from the
other, and are orthogonal by the corresponding link Peter--Weyl
decomposition. The two channels of one adjacent pair are orthogonal
by shared spin zero versus one. Constants are orthogonal to every
nonconstant displayed channel. Finally every \(E_e\) preserves
these link parities and joint spin subspaces. The same orthogonality
therefore holds after any link-Casimir products used here.

The identity
\[
S^2-M=\sum_pY_p+2\sum_{\{p,q\},\ p\ne q}W_pW_q
\tag{2.8}
\]
has unordered distinct-pair summation. Invert \(H_0\) on each
nonconstant channel in (2.3), retaining the factor two in (2.8), and
retain the constant fixed by (2.3). This proves the entire coefficient
\[
\boxed{\begin{split}
A_2={}&-\frac M{18}+\sum_p\frac{Y_p}{24}
 +\sum_{\{p,q\}\text{ edge-disjoint}}\frac{W_pW_q}{9}\\
 &+\sum_{\{p,q\}\text{ adjacent}}
       \left(\frac4{27}Z_{pq,0}+\frac4{39}Z_{pq,1}\right).
\end{split}}
\tag{2.9}
\]
For example the two adjacent multipliers are
\((2/3)/(9/2)=4/27\) and \((2/3)/(13/2)=4/39\), with the distinct
norms in (2.7). All original faces and adjacent pairs occur in (2.9),
including at the open boundary. This was derived by differentiating
the full Hamiltonian, not by selecting a two-face Hamiltonian.

## 3. The no-common-face condition and the connected fourth coefficient

Fix distinct physical edges \(e,f\) such that no original elementary
face contains both. Let
\[
r_e=\#\{p\in\mathsf P_L:e\in\partial p\},\qquad
\gamma_e=\langle\psi_\xi,E_e\psi_\xi\rangle,
\qquad v_e=(E_e-\gamma_e)\psi_\xi.
\tag{3.1}
\]
Since \(\psi_\xi\) is smooth and the different edge Casimirs commute,
the exact covariance is
\[
C_{ef}=\langle v_e,v_f\rangle
 =\langle E_e\psi_\xi,E_f\psi_\xi\rangle-\gamma_e\gamma_f
 =\langle\psi_\xi,E_eE_f\psi_\xi\rangle-\gamma_e\gamma_f.
\tag{3.2}
\]
For an original edge \((n,i)\), with transverse directions \(j,k\),
the exact boundary-dependent number is
\[
r_{(n,i)}=\delta_L(n_j)+\delta_L(n_k),\qquad
\delta_L(t)=\begin{cases}1,&t=-L\text{ or }L,\\2,&-L<t<L.
\end{cases}
\tag{3.3}
\]
Each transverse direction permits one inward incident face at a boundary
and two in the interior. Thus \(2\le r_e\le4\), with the actual
value (3.3) used in every subtraction.

Let \(T=E_eE_f\) on the smooth vectors in question. Then
\[
T1=0,\qquad TA_1=0.
\tag{3.4}
\]
The second identity holds term by term in \(A_1=S/3\): a single
face trace depends on at most one of these two link variables. For the
analytic vacuum series \(\sum_{j\ge0}\xi^jA_j\), with \(A_0=1\),
every coefficient of degree less than four in \(\langle\psi,T\psi\rangle\)
therefore vanishes. At degree four, any pair \(i+j=4\) except
\((i,j)=(2,2)\) has \(i\le1\) or \(j\le1\). Moving \(T\)
between smooth factors by self-adjointness and (3.4) makes those terms
zero. Hence
\[
[\xi^4]\langle\psi_\xi,E_eE_f\psi_\xi\rangle
                 =\langle A_2,E_eE_fA_2\rangle.
\tag{3.5}
\]
No unknown third or fourth vacuum derivative is required for this
coefficient; its disappearance is the proved annihilation (3.4).
The first term of \(\gamma_e\) is likewise
\[
[\xi^2]\gamma_e=\langle A_1,E_eA_1\rangle
 =\frac1{9}\sum_{p:e\in\partial p}\frac34=\frac{r_e}{12}.
\tag{3.6}
\]

Define the two-face channel count exactly as in the source:
\[
a_{ef}=\#\{(p,q)\in\mathsf P_L^2:
 e\in\partial p,\ f\in\partial q,
 |\partial p\cap\partial q|=1\}.
\tag{3.7}
\]
There are \(r_er_f\) face pairs obtained by choosing a face incident
to each edge. They are distinct faces, and their assignment to \(e,f\)
is unique. Indeed equality of the faces, or containment of \(e\) in
the face assigned to \(f\), would give a common face, contrary to the
hypothesis. Thus these ordered-by-containment pairs correspond
bijectively to the relevant unordered distinct-face terms of (2.9).
Exactly \(a_{ef}\) are adjacent and \(r_er_f-a_{ef}\) are edge-disjoint.

The constant and every repeated-face term in (2.9) are killed by \(T\).
For the remaining terms, if the union of the two faces omits either
\(e\) or \(f\), the corresponding derivative kills the term. If both
occur in the union, the no-common-face hypothesis assigns one to each
face as above. In an adjacent pair its shared edge \(g_0\) cannot
be \(e\): otherwise the face containing \(f\) would also contain
\(e\). The same argument excludes \(g_0=f\). Therefore both
\(e,f\) are outer fundamental links in both channels of (2.7).
This proves the complete support assertion for (3.5), including the
shared-edge exclusions; no contributing term has been dropped.

The orthogonality proved after (2.7), preserved by \(T\), now evaluates
(3.5) exactly. Each edge-disjoint pair contributes
\[
\left(\frac19\right)^2
 \left(\frac34\right)^2\|W_pW_q\|^2=\frac1{144}.
\tag{3.8}
\]
Each adjacent pair contributes, retaining the two norms and the two
inverse-energy factors separately,
\[
\begin{split}
\left(\frac34\right)^2
 \left[\left(\frac4{27}\right)^2\frac14
          +\left(\frac4{39}\right)^2\frac34\right]
 &=\frac1{324}+\frac3{676}.
\end{split}
\tag{3.9}
\]
Thus the uncentered and disconnected degree-four terms are respectively
\[
\begin{split}
[\xi^4]\langle\psi,E_eE_f\psi\rangle
 &=\frac{r_er_f-a_{ef}}{144}
              +a_{ef}\left(\frac1{324}+\frac3{676}\right),\\
[\xi^4](\gamma_e\gamma_f)&=\frac{r_er_f}{144}.
\end{split}
\tag{3.10}
\]
In particular the disconnected subtraction retains every product of
the actual incidence counts, including their boundary values. The
edge-disjoint contribution cancels exactly against its portion of this
product; an adjacent channel leaves
\[
\frac1{324}+\frac3{676}-\frac1{144}
 =\frac{676+972-1521}{219024}
 =\frac{127}{219024}>0.
\tag{3.11}
\]

To obtain the stated next order, define the full central-link involution
\[
(\mathcal ZF)(U)=F((z_i(n)U_{(n,i)})_{(n,i)}),
\qquad z_i(n)=(-1)^{\sum_{j<i}n_j}I.
\tag{3.12}
\]
It is a real Haar unitary, commutes with every Casimir and with the
gauge action, and sends every \(W_p\) to \(-W_p\). To check the
last assertion for a face \(ij\), \(i<j\), the two \(i\)-link
exponents agree while the \(j\)-link exponent at \(n+\mathbf e_i\)
exceeds that at \(n\) by one. The face word (1.1) consequently gets
one minus sign, also on the inverse traversals since \((-I)^{-1}=-I\).
Therefore \(\mathcal ZK_\xi\mathcal Z=K_{-\xi}\). Positivity and
uniqueness give \(\psi_{-\xi}=\mathcal Z\psi_\xi\), for real small
\(\xi\). All expectations in (3.2) and (3.6) are even real analytic
functions. Their expansions consequently obey
\[
\gamma_e=\frac{r_e}{12}\xi^2+O_L(\xi^4),\qquad
\boxed{C_{ef}=\frac{127}{219024}\,a_{ef}\xi^4+O_L(\xi^6)}
\quad(e,f\text{ share no face}).
\tag{3.13}
\]
For a fixed finite box the implicit constants can be taken uniformly
over its finitely many edge pairs. No uniformity in \(L\) is claimed.
If \(a_{ef}>0\), (3.13) implies \(C_{ef}>0\) for sufficiently small
positive \(\xi\): divide by \(\xi^4\) and use its positive limit.

## 4. Independent proof of the graph identity and its full incidence map

Define the original unsigned edge-face incidence map, including all
boundary rows and columns,
\[
\mathsf I:\mathbb C^{\mathsf P_L}\longrightarrow\mathbb C^{\mathsf E_L},
\qquad (\mathsf Ix)_e=\sum_{p:e\in\partial p}x_p,
\qquad \mathsf I_{ep}=\mathbf1_{\{e\in\partial p\}}.
\tag{4.1}
\]
Its adjoint for the original counting inner products is its transpose.
Let \(\mathsf R=\operatorname{diag}(r_e)\), let \(\mathsf A\) be
the simple face adjacency from shared physical edges, and let
\(\mathsf B\) be the simple edge adjacency defined by
\[
\mathsf B_{ef}=\mathbf1_{\{e\ne f,\ \exists p:
                       e,f\in\partial p\}}.
\tag{4.2}
\]
The following geometry proves why a binary adjacency is sufficient in
(4.2), instead of presuming that multiplicities are absent.

Two distinct physical edges lie in at most one elementary square.
If their directions agree, they must be opposite sides of a square;
their positive bases must differ by \(\pm\mathbf e_j\) for exactly
one transverse direction \(j\). That nonzero difference determines
the other plane direction and the canonical base, uniquely. If their
directions \(i,j\) differ, they must be adjacent sides and must meet
at a vertex \(x\). Their other endpoints can be written uniquely as
\(x+s_i\mathbf e_i\) and \(x+s_j\mathbf e_j\), with
\(s_i,s_j\in\{-1,1\}\). The fourth vertex of a containing elementary
square must then be \(x+s_i\mathbf e_i+s_j\mathbf e_j\), and its
canonical base is
\(x+\min(s_i,0)\mathbf e_i+\min(s_j,0)\mathbf e_j\).
This determines the face uniquely. Nonincident perpendicular edges
cannot be the perpendicular sides of one square. These statements are
about physical edges with their actual endpoints; there is no periodic
identification. Restricting to contained faces cannot increase the count.

Consequently the two exact incidence Gram identities are
\[
\mathsf I\mathsf I^T=\mathsf R+\mathsf B,
\qquad \mathsf I^T\mathsf I=4I+\mathsf A.
\tag{4.3}
\]
The first diagonal counts incident faces and the first off-diagonal
counts the zero or one face just proved; the second diagonal counts
the four edges of a face, while its off-diagonal is zero or one by
the face intersection fact proved before (2.6).

Extend the ordered two-face count to all edge pairs by defining
\[
\mathsf T=\mathsf I\mathsf A\mathsf I^T,
\quad
\mathsf T_{ef}=\sum_{p,q}\mathsf I_{ep}\mathsf A_{pq}\mathsf I_{fq}.
\tag{4.4}
\]
For the distinct no-common-face pairs in (3.7),
\(\mathsf T_{ef}=a_{ef}\) exactly. Unlike that restricted definition,
(4.4) also assigns a value to common-face pairs and to diagonal pairs.
Associativity of these explicitly defined finite linear maps and (4.3)
give the full identity
\[
\boxed{\begin{split}
\mathsf T
 &=\mathsf I(\mathsf I^T\mathsf I-4I)\mathsf I^T
   =(\mathsf I\mathsf I^T)^2-4\mathsf I\mathsf I^T\\
 &=\mathsf B^2+\mathsf B\mathsf R+\mathsf R\mathsf B-4\mathsf B
                          +\mathsf R^2-4\mathsf R,\\
\mathsf T_{ef}
 &=(\mathsf B^2)_{ef}+(r_e+r_f-4)\mathsf B_{ef}
                         +(r_e^2-4r_e)\delta_{ef}.
\end{split}}
\tag{4.5}
\]
Thus the source's specified no-common-face hypothesis makes both extra
terms zero, and proves precisely
\[
\boxed{a_{ef}=(\mathsf B^2)_{ef}\qquad
        (e\ne f,\ e,f\text{ share no face}).}
\tag{4.6}
\]
In general \(\mathsf T\ne\mathsf B^2\); the exact correction, rather
than only a nonidentity assertion, is (4.5). For example interior edges
\(e=((0,0,0),1)\), \(f=((0,0,0),2)\) have \(r_e=r_f=4\)
and \(\mathsf B_{ef}=1\), so their two matrix entries differ by 4.
At a diagonal entry, \(\mathsf T_{ee}=r_e(r_e-1)\), while
\((\mathsf B^2)_{ee}=3r_e\): each incident face supplies three
distinct other edges, with no repetition by the uniqueness proof above.
Their difference \(r_e(r_e-4)\) records the nontrivial open-boundary
correction when \(r_e=2\) or 3.

There is also an exact channel bijection verifying (4.6) independently
of matrix multiplication. Send each pair \((p,q)\) counted in (3.7)
to its unique shared edge \(g_0\). That edge is different from \(e,f\)
by the argument preceding (3.8), and is adjacent in \(\mathsf B\)
to both. Conversely, if \(g_0\) is a common \(\mathsf B\)-neighbor
of \(e,f\), the proved two-edge uniqueness supplies exactly one
contained face \(p\) with \(e,g_0\) and one \(q\) with \(g_0,f\).
They are distinct because \(e,f\) share no face. They share \(g_0\)
and no second edge by the face uniqueness property. Hence they form a
pair counted in (3.7). These constructions are inverses, so the number
of such pairs is exactly the number of common edge-graph neighbors,
namely \((\mathsf B^2)_{ef}\).

For these no-common-face pairs, graph distance is two exactly when
\(a_{ef}>0\). Combining (3.13) and (4.6), the degree-four connected
coefficient has exactly that support. Beyond graph distance two the
coefficient is zero, giving \(C_{ef}=O_L(\xi^6)\); this makes no
all-orders finite-range assertion. There are actual positive channels
in every original box with \(L\ge2\):
\[
e=((0,0,0),1),\qquad f=((0,2,0),1),\qquad
p=((0,0,0);1,2),\qquad q=((0,1,0);1,2)
\tag{4.7}
\]
give shared edge \(g_0=((0,1,0),1)\). The links \(e,f\) share no
face since their parallel bases differ by \(2\mathbf e_2\).
Every vertex of both faces belongs to the box, including at \(L=2\).
This already proves \(a_{ef}\ge1\) without omitting boundary vertices.

## 5. Relation to the exact local energy matrix and original physical scales

Define, with the same actual interacting vacuum and original Hamiltonian,
\[
\mathcal A_\xi=H-\mathcal E(\xi)I,\qquad
\mathcal N_{ef}=\langle v_e,\mathcal A_\xi v_f\rangle.
\tag{5.1}
\]
All vectors are smooth. The Casimirs commute, and the functions and
operators preserve the real subspace. Expanding the double commutator
and using \(H\psi=\mathcal E\psi\) gives
\[
\begin{split}
\langle\psi,[E_e,[H,E_f]]\psi\rangle
={}&\langle E_e\psi,HE_f\psi\rangle
 +\langle E_f\psi,HE_e\psi\rangle
 -2\mathcal E\langle E_e\psi,E_f\psi\rangle\\
={}&2\langle v_e,(H-\mathcal E)v_f\rangle.
\end{split}
\tag{5.2}
\]
For the second line, self-adjointness and reality make the first two
terms equal, and all centered ground-vector terms vanish under
\(H-\mathcal E\). This proves
\[
\mathcal N_{ef}
 =\frac12\langle\psi,[E_e,[H,E_f]]\psi\rangle
 =\frac b2\sum_{p:e,f\in\partial p}
       \langle\psi,[E_e,[2-W_p,E_f]]\psi\rangle.
\tag{5.3}
\]
The second equality has two exact reasons. First \(E_e,E_f\) commute
with the whole electric sum, so its coefficient \(\kappa\) multiplies
an identically zero commutator. Second, the product rule gives a zero
\([2-W_p,E_f]\) if \(f\notin\partial p\). When \(f\in\partial p\),
that commutator consists of multiplication and first derivatives in
the \(f\) variable, with coefficients depending only on the face's
link variables. It therefore commutes with \(E_e\) if
\(e\notin\partial p\). This proves every support exclusion in (5.3),
including its derivative terms. In particular
\[
\boxed{\mathcal N_{ef}=0\quad\text{exactly for every positive coupling
 whenever }e,f\text{ share no face}.}
\tag{5.4}
\]

The exact relation to the nonzero covariance (3.13) is a matrix of
spectral measures, not an assertion that the two matrices are unrelated.
Let \(P_{\mathcal A_\xi}(B)\) be the physical spectral projection
for a Borel set \(B\subset\mathbb R\). Define
\[
\Sigma_{ef}(B)=\langle v_e,P_{\mathcal A_\xi}(B)v_f\rangle.
\tag{5.5}
\]
For complex coefficients \(w_e\), the matrix quadratic form is
\[
\sum_{e,f}\overline w_e\Sigma_{ef}(B)w_f
 =\left\|P_{\mathcal A_\xi}(B)\sum_e w_ev_e\right\|^2\ge0.
\tag{5.6}
\]
Every entry is a finite measure; the finite total variation follows
by Cauchy--Schwarz on spectral projections of any finite disjoint
partition, bounded by \(\|v_e\|\|v_f\|\). Reality of the operator
and vectors makes each entry real. Smoothness gives the first moment,
and spectral calculus gives the exact maps
\[
C_{ef}=\int d\Sigma_{ef}(\omega),\qquad
\mathcal N_{ef}=\int\omega\,d\Sigma_{ef}(\omega).
\tag{5.7}
\]
In particular the off-diagonal measure need not be nonnegative.
For a separated pair with \(a_{ef}>0\), it has positive total mass
at sufficiently small positive \(\xi\), by (3.13), and zero first
moment by (5.4). It has no atom at zero because both \(v_e,v_f\)
are ground-state orthogonal. At each fixed box the compact resolvent
and simple ground state give a strictly positive first excited energy.
If this off-diagonal measure were nonnegative, its first moment would
be at least that energy times its positive total mass, contradicting
(5.4). Thus its positive and negative parts are both nonzero in this
case. Equations (5.5)--(5.7) give the exact spectral correspondence
permitting a nonzero zeroth moment and a zero first moment. This is
a finite-box statement, with no assumed infinite-volume mass gap.

Finally, returning the original coupling explicitly,
\[
\frac{127}{219024}\,a_{ef}\xi^4
 =\frac{127a_{ef}}{219024\cdot256\,g^{16}}
 =\frac{127a_{ef}}{56070144\,g^{16}}.
\tag{5.8}
\]
The covariance (3.2) is of the dimensionless Casimirs \(E_e,E_f\),
so there is no additional energy factor in (5.8). The covariance of
the original physical electric energies \(\kappa E_e,\kappa E_f\)
is exactly \(\kappa^2C_{ef}\), and their centered energy matrix is
\(\kappa^2\mathcal N_{ef}\). The eigenvalue of a link electric
operator in the original metric is the same physical operator because
\((\kappa/4)(-\Delta_e^c)=\kappa E_e\). The scalar \(2bM\) remains
in \(H\) and \(\mathcal E\), canceling only in their displayed
difference. No nonlinear plaquette interaction has been discarded:
the full \(S^2\), all its channels, and the actual vacuum equation
were used to obtain the coefficient.

## 6. Independent check of the fourth spectral functional and physical time

The root source was extended during this review to resolve the fourth
coefficient against functions of energy. This section verifies that
extension from the retained vacuum coefficients and actual band transport.
Use the dimensionless excitation operator
\[
\widehat{\mathcal A}_\xi=(H-\mathcal E)/\kappa=K_\xi-e(\xi)I.
\tag{6.1}
\]
The notation distinguishes it from the physical-energy operator
\(\mathcal A_\xi=H-\mathcal E\) in (5.1).

First, the free physical energy-three space is exactly
\(\mathcal P=\operatorname{span}\{W_p\}\), with the next physical
energy at \(9/2\). Here is the isolation argument used in the
transport. Project product Peter--Weyl coefficients by the vertex Haar
action; their invariant contractions span the physical space. A nonzero
link spin at a degree-one support vertex has no invariant vector, so
a nonconstant physical support has no such vertex. Any nonempty finite
graph of minimum degree at least two contains a cycle. The cubic lattice
is simple and bipartite, so a cycle has at least four links, each costing
at least \(3/4\). Below energy \(9/2\), at most five links can have
nonzero spin. A four-cycle in this lattice is one elementary square;
a fifth edge cannot be an isolated component without a degree-one vertex,
cannot extend outward from the cycle without a degree-one endpoint,
and cannot be a chord between its same-bipartition opposite vertices.
Thus only that square is supported. The invariant contraction at each
degree-two vertex requires equal spins on its two incident edges, by
Schur's lemma, so every square edge has the same spin. Only spin \(1/2\)
then has total energy below \(9/2\), producing its unique trace \(W_p\)
at energy 3. Conversely a six-edge rectangular fundamental loop exists
in every \(L\ge2\) box and has energy \(9/2\). This proves the claim.

Let \(P\) be the orthogonal projection onto \(\mathcal P\) in the
physical space, and set
\[
R_3=(I-P)\bigl((H_0-3)|_{\mathcal P^\perp}\bigr)^{-1}(I-P).
\tag{6.2}
\]
The inverse is bounded by the proved isolation, and its constant-state
multiplier is \(-1/3\). The contour \(|z-3|=3/4\) defines the
actual spectral projection \(P_\xi\) of \(K_\xi\). For
\(|\xi|\le3/(64M)\), the free resolvent bound \(4/3\) and
\(\|S\|=2M\) give Neumann factor at most \(1/8\). Integrating
the resolvent difference gives
\(\|P_\xi-P\|\le(3/4)(4/3)^2(2M\cdot3/(64M))/(1-1/8)=1/7\).
For real \(\xi\), the exact map
\[
V_\xi=P_\xi P(PP_\xi P|_{\mathcal P})^{-1/2}
 :\mathcal P\longrightarrow\operatorname{ran}P_\xi
\tag{6.3}
\]
is an isometry onto this range. The inverse square root is the binomial
series at the identity, justified by the bound \(1/7\); using
\(P_\xi^2=P_\xi=P_\xi^*\) verifies \(V_\xi^*V_\xi=I\).
For \(|\xi|\le3/(128M)\), bounded perturbation of the isolated
free spectral clusters makes this range orthogonal to the actual vacuum.
The contour expression and the eigen-equation give smooth finite-rank
ranges and analytic derivatives in each fixed Sobolev norm.

Differentiating the projection identity gives \(PP'_0P=0\), so
\(PV'_0=0\). Differentiating spectral intertwining then gives
\((H_0-3)V'_0=(I-P)SP\), hence
\(V'_0=R_3SP\). The second band coefficient before subtracting the
vacuum is \(-PSR_3SP\). Its constant virtual channel contributes
\(+1/3\) to every face-matrix entry, its repeated-face channel
contributes \(-1/5\) to the diagonal, each disjoint pair contributes
\(-1/3\) to its two diagonals and mutual entries, and each adjacent
pair contributes
\[
-\frac{1/4}{9/2-3}-\frac{3/4}{13/2-3}=-\frac8{21}
\tag{6.4}
\]
to that same pattern. These terms follow from (2.7) with the exact
energy denominators in (6.2), and their cross terms vanish by the
parity proof in Section 2. If \(d_p\) is the original face degree,
the diagonal sum is \(7/15-M/3-d_p/21\), while the off-diagonal
sum is \(-1/21\) for adjacent faces and zero otherwise. Subtracting
the actual vacuum coefficient \(-M/3\) from (2.3) gives
\[
V_\xi^*\widehat{\mathcal A}_\xi V_\xi
 =3I+\xi^2\mathsf F+O_L(\xi^4),\qquad
\mathsf F=\frac7{15}I-\frac1{21}
                    (\operatorname{diag}(d_p)+\mathsf A).
\tag{6.5}
\]
For the fourth-order error rather than a third-order error, the central
map (3.12) acts as \(-I\) on \(\mathcal P\), and the Gram factor in
(6.3) is even. Hence \(V_{-\xi}=-\mathcal ZV_\xi\); conjugating
the compressed matrix and using the even vacuum energy proves that
matrix is even. This supplies the stated remainder in (6.5).

To determine the higher-channel part of the electric vector, take any
fixed real link weights \(w_e\), with no constraint that they be equal,
and define the original linear maps
\[
\Gamma_w=\sum_ew_eE_e,\quad
a_p(w)=\frac14\sum_{e\in\partial p}w_e,\quad
x(w)=\sum_pa_p(w)W_p,\quad
v(w)=(\Gamma_w-\langle\Gamma_w\rangle)\psi_\xi.
\tag{6.6}
\]
Set \(y_\xi(w)=V_\xi^*v(w)\) and
\(\rho_\xi(w)=(I-P_\xi)v(w)\), an exact orthogonal spectral
decomposition. The vector \(v(w)\) transforms under \(\xi\mapsto-\xi\)
by \(\mathcal Z\). With \(V_{-\xi}=-\mathcal ZV_\xi\) it follows
that \(y_\xi(w)\) is odd. The smooth expansions therefore have form
\[
y_\xi(w)=\xi x(w)+\xi^3z(w)+O_L(\xi^5),\qquad
\rho_\xi(w)=\xi^2r(w)+O_{H^k,L}(\xi^3).
\tag{6.7}
\]
The unknown \(z(w)\) is an actual derivative of the defined finite
band coordinate; it will disappear from the final coefficient by an
exact mass identity.

Here is the full derivation of \(r(w)\). Write
\(s=a_p(w)+a_q(w)\), and let \(g_0\) be the shared edge of an
adjacent pair. The eigenvalues of \(\Gamma_w\) on a repeated face,
disjoint pair, adjacent zero channel, and adjacent one channel are
respectively
\[
8a_p,\qquad 3s,\qquad 3s-\frac32w_{g_0},\qquad
3s+\frac12w_{g_0}.
\tag{6.8}
\]
The last two subtract the twice-counted fundamental contribution of
the shared edge in \(3s\) and insert its actual spin-zero or spin-one
Casimir. Multiplying (2.9) by these actual eigenvalues gives the
\(\Gamma_w A_2\) coefficients in the table below. The first
spectral dressing \(R_3Sx(w)\) has the table's next column, from
the denominators \(8-3,6-3,9/2-3,13/2-3\). Their difference is
the high-channel coefficient of \((I-P_\xi)v(w)\): the order-two
part of \(v(w)\) is even under \(\mathcal Z\) and therefore has
zero projection on \(P\), while \(P'_0x=R_3Sx\).
\[
\begin{array}{c|c|c|c}
\text{channel}&\Gamma_w A_2& R_3Sx(w)& r(w)\\ \hline
Y_p&a_p/3&a_p/5&2a_p/15\\
W_pW_q\text{, disjoint}&s/3&s/3&0\\
Z_{pq,0}&(4s-2w_{g_0})/9&2s/3&-2(s+w_{g_0})/9\\
Z_{pq,1}&(12s+2w_{g_0})/39&2s/7&2(3s+7w_{g_0})/273.
\end{array}
\tag{6.9}
\]
The constant from centering at order two is
\(-\sum_pa_p/3\), by (3.6) summed against \(w_e\); the constant
in \(R_3Sx(w)\) is the same, using the multiplier \(-1/3\).
These constants cancel exactly, rather than being deleted from either
input. There is no disjoint residual and no other channel. Thus (6.9)
proves the complete vector
\[
\boxed{r(w)=\sum_p\frac{2a_p(w)}{15}Y_p
 +\sum_{\{p,q\}\text{ adjacent}}
 \left[-\frac{2(s+w_{g_0})}{9}Z_{pq,0}
       +\frac{2(3s+7w_{g_0})}{273}Z_{pq,1}\right].}
\tag{6.10}
\]

Use the single-link weight \(w^{(e)}_h=\delta_{eh}\) and denote its
vectors by \(x_e,z_e,r_e^{\rm vec}\), keeping the latter distinct
from the incidence integer \(r_e\). Then
\(x_e=\sum_{p\ni e}W_p/4\). For our no-common-face edges,
\(\langle x_e,x_f\rangle=0\), and the full incidence count gives
\[
\langle x_e,\mathsf Fx_f\rangle
 =-\frac1{4\cdot21\cdot4}
         \sum_{p,q}\mathsf I_{ep}\mathsf A_{pq}\mathsf I_{fq}
 =-\frac{a_{ef}}{336}.
\tag{6.11}
\]
In the cross measure of \(r_e^{\rm vec},r_f^{\rm vec}\), a
repeated-face term would require a face containing both edges, so it
vanishes. The same support proof as in Section 3 leaves precisely
the adjacent pairs counted by \(a_{ef}\). On each, both edges are
outer edges, \(w_{g_0}=0\), and \(s=1/4\) for either single-link
weight. Their two coefficients in (6.10) are therefore \(-1/18\)
and \(+1/182\), respectively. Using the norms in (2.7), the entire
free cross functional is
\[
\langle r_e^{\rm vec},h(H_0)r_f^{\rm vec}\rangle
 =a_{ef}\left[\frac1{1296}h(9/2)
                    +\frac3{132496}h(13/2)\right].
\tag{6.12}
\]
Both contributions are positive products of the equal signed amplitudes
of the two links; their different signs before taking products in
(6.10) have been retained.

The exact test-function scope in the source is sufficient: take any
bounded continuous real or complex \(h\) on \([0,\infty)\) that
is differentiable at 3. Equivalently one may take such a function on
\(\mathbb R\); its values on the negative half-line are immaterial
because \(\widehat{\mathcal A}_\xi\ge0\). To justify the out-of-band
limit, (6.7) gives \(\rho_\xi(w)/\xi^2\to r(w)\) in \(H^2\).
Also
\(\widehat{\mathcal A}_\xi-H_0=-\xi S-e(\xi)I\) has bounded
norm at most \(2M|\xi|+|e(\xi)|\), which tends to zero. The resolvent
identity yields norm resolvent convergence. The algebra generated by
resolvents is uniformly dense in continuous functions vanishing at
infinity, so functional calculus gives norm convergence for such
functions. For a general bounded continuous \(h\), multiply it by
a continuous compact cutoff and control the tail on each scaled
residual vector by
\[
\|\mathbf1_{(R,\infty)}(\widehat{\mathcal A}_\xi)
            \rho_\xi(w)/\xi^2\|^2
 \le R^{-2}\|\widehat{\mathcal A}_\xi\rho_\xi(w)/\xi^2\|^2.
\tag{6.13}
\]
The rightmost norm is uniformly bounded for small real \(\xi\), by
the \(H^2\) convergence and the bounded perturbation. Cauchy--Schwarz
controls cross tails by the corresponding two diagonal bounds. First
let \(\xi\to0\) at fixed cutoff, then \(R\to\infty\). This proves
that (6.12) is the whole fourth-order out-of-band limit for the stated
test functions. The argument retains the unbounded operator domains;
it does not infer convergence of all bounded functions from norm
resolvent convergence alone.

In the finite band, differentiability at 3 means
\(h(3+s)=h(3)+h'(3)s+o(|s|)\) as real \(s\to0\). Every
eigenvalue of the matrix (6.5) differs from 3 by \(O_L(\xi^2)\),
so its finite spectral calculus gives the operator-norm expansion
\[
h(V_\xi^*\widehat{\mathcal A}_\xi V_\xi)
 =h(3)I+\xi^2h'(3)\mathsf F+o_L(\xi^2).
\tag{6.14}
\]
No derivative at \(9/2\) or \(13/2\) is required. Since
\(\langle x_e,x_f\rangle=0\), (6.7) and (6.14) make the band
fourth coefficient
\[
h(3)(\langle x_e,z_f\rangle+\langle z_e,x_f\rangle)
                   -\frac{a_{ef}}{336}h'(3).
\tag{6.15}
\]
At \(h=1\), the exact orthogonal spectral decomposition says that
the band mass plus the out-of-band mass is the actual covariance.
Subtracting (6.12) at 1 from the proved (3.13) gives the actual
previously unspecified band-mass derivative:
\[
\langle x_e,z_f\rangle+\langle z_e,x_f\rangle
 =a_{ef}\left(\frac{127}{219024}
                      -\frac1{1296}-\frac3{132496}\right)
 =-\frac{59a_{ef}}{275184}.
\tag{6.16}
\]
Thus no assumption about \(z_e,z_f\) closes the calculation; their
needed pairing has been computed from exact mass conservation.

Combining (6.12), (6.15), and (6.16) proves independently
\[
\boxed{\begin{split}
\lim_{\xi\to0}\xi^{-4}
       \langle v_e,h(\widehat{\mathcal A}_\xi)v_f\rangle
 =a_{ef}\biggl[&-\frac{59}{275184}h(3)-\frac1{336}h'(3)\\
               &+\frac1{1296}h(9/2)
                         +\frac3{132496}h(13/2)\biggr].
\end{split}}
\tag{6.17}
\]
For merely bounded continuous \(h\) differentiable at 3, this is a
limit with an \(o_L(\xi^4)\) error for the unscaled functional.
It does not assert an analytic \(O(\xi^6)\) remainder for every
such test function.

The derivative term in (6.17) is essential and is not a finite signed
measure when \(a_{ef}>0\). To prove that exact assertion, take
\[
h_n(q)=(q-3)\max\{1-n|q-3|,0\},\qquad n=1,2,\ldots.
\tag{6.18}
\]
These admissible test functions have
\(\|h_n\|_\infty=1/(4n)\), \(h_n'(3)=1\), and zero values at
\(3,9/2,13/2\). The right side of (6.17) equals
\(-a_{ef}/336\) for every \(n\), although their supremum norms
tend to zero. Integration against a finite signed measure would tend
to zero by its total-variation bound. On smooth compact test functions
the exact coefficient can be written as the distribution
\[
a_{ef}\left[-\frac{59}{275184}\delta_3
 +\frac1{336}\delta'_3+\frac1{1296}\delta_{9/2}
                         +\frac3{132496}\delta_{13/2}\right],
\quad \delta'_3(h)=-h'(3).
\tag{6.19}
\]
This explains the sign of its derivative component and the precise
relation to the moving actual band. Every original \(\Sigma\) is
still the matrix of finite spectral measures in (5.5); its fourth
derivative is the functional (6.17), not a new positive-atom model.

The test \(h(q)=q\) is unbounded, so its first-moment check should
not be obtained by applying the bounded-test theorem without another
argument. The needed argument is already available: \(H^2\) convergence
in (6.7) gives
\[
\left\langle\frac{\rho_\xi(e)}{\xi^2},
 \widehat{\mathcal A}_\xi\frac{\rho_\xi(f)}{\xi^2}\right\rangle
 \longrightarrow\langle r_e^{\rm vec},H_0r_f^{\rm vec}\rangle.
\tag{6.20}
\]
The finite band expansion applies directly to its own matrix, so the
degree-four first-moment coefficient is consequently
\[
3\left(-\frac{59}{275184}\right)-\frac1{336}
       +\frac9{2\cdot1296}+\frac{39}{2\cdot132496}=0.
\tag{6.21}
\]
This exact rational cancellation agrees with
\(\mathcal N_{ef}/\kappa=0\) from (5.4); the two high channels and
the band-energy derivative all contribute to it.

For physical time \(t\ge0\), set \(\tau=\kappa t\). The function
\(h(q)=e^{-\tau q}\) is bounded on the nonnegative spectrum and has
derivative \(-\tau e^{-3\tau}\) at 3. If a function on all of
\(\mathbb R\) is desired, use \(e^{-\tau\max(q,0)}\), which
agrees on the entire spectrum and near 3. Applying (6.17) gives
\[
\boxed{\begin{split}
\langle v_e,e^{-t(H-\mathcal E)}v_f\rangle
 =a_{ef}\xi^4\biggl[&-\frac{59}{275184}e^{-3\kappa t}
       +\frac{\kappa t}{336}e^{-3\kappa t}\\
       &+\frac1{1296}e^{-9\kappa t/2}
       +\frac3{132496}e^{-13\kappa t/2}\biggr]
       +O_{L,t,\kappa}(\xi^6).
\end{split}}
\tag{6.22}
\]
The positive sign of \(\kappa t/336\) is the product of the
negative derivative coefficient and \(h'(3)=-\kappa t e^{-3\kappa t}\).
At \(t=0\) the bracket is \(127/219024\). Its derivative is zero
by minus \(\kappa\) times (6.21), as required by the exact energy
matrix identity.

For the stronger remainder asserted only for this analytic time family,
use the exact factorization
\[
e^{-t(H-\mathcal E)}
 =e^{\tau e(\xi)}e^{-\tau(H_0-\xi S)},\qquad \tau=\kappa t.
\tag{6.23}
\]
The ordered \(n\)-fold Duhamel integral for the second factor has norm
bounded by
\[
\frac{(2M|\xi|\tau)^n}{n!}
 =\frac{(2M|\xi|\kappa t)^n}{n!}.
\tag{6.24}
\]
Indeed every free factor \(e^{-sH_0}\), \(s\ge0\), is a contraction;
the \(n\) potential factors have norm \((2M)^n\), and the ordered
time simplex has volume \(\tau^n/n!\). This gives norm analyticity
at fixed \(\tau\). The scalar \(e^{\tau e(\xi)}\), the vacuum,
and the vectors are analytic too; the central cochain makes the whole
cross expectation even. Its established vanishing lower coefficients
and (6.17) then imply the \(O(\xi^6)\) remainder in (6.22).
For physical time the factor \(\kappa\) in (6.24) must be retained:
\((2M|\xi|t)^n/n!\) would be the bound for dimensionless time, not
for the original physical-time semigroup. The analytic scalar in
(6.23) also remains part of the exact expression.

These are fixed \(L,\tau\) estimates, or equivalently fixed
\(L,t,\kappa\) estimates. Their exact relation to a coupling path
at fixed original lattice spacing is
\[
g^2=\frac1{2\sqrt\xi},\qquad
\kappa=\frac1{a\sqrt\xi},\qquad
\tau=\frac{t}{a\sqrt\xi}\quad(\xi>0).
\tag{6.25}
\]
Thus a fixed physical \(a,t>0\) path has varying \(\tau\) as
\(\xi\to0\). The displayed map preserves that relation; a uniform
remainder along the resulting unbounded-\(\tau\) path is not supplied
by the fixed-\(\tau\) statement. No coupling, volume, time, or
continuum limit is exchanged in this review.

## 7. Review outcome and exact finite diagnostics

The coefficient, sign, disconnected subtraction, two spin channels, and
even remainder in the root source are verified. The root source's graph
claim is also verified with its explicitly stated no-common-face
hypothesis. A use of that claim as an unrestricted full-matrix identity
would be incorrect; its exact extension, retaining all original
boundary degrees, is (4.5). No correction to the stated restricted
theorem is required. The subsequently added spectral functional, its
test-function scope, its two high-channel masses, and its first-moment
cancellation are verified in Section 6. The physical-time Duhamel bound
must use \(\tau=\kappa t\) as in (6.24); that scale correction was
reported to the root author without editing the root source.

A separate standard-library exact diagnostic enumerated every original
edge, face, and physical-edge star for \(L=2,3,4\). It constructed
\(\mathsf T\) by the ordered adjacent-face sum and independently
constructed \(\mathsf B^2\) by counting common neighbors. Every
matrix entry satisfied (4.5), and every no-common-face entry satisfied
(4.6). The exact counts were
\[
\begin{array}{c|r|r|r|r}
L&\text{edges}&\text{faces}&\text{unordered adjacent face pairs}
 &\text{ordered separated pairs with }a_{ef}>0\\ \hline
2&300&240&1128&9330\\
3&882&756&3852&32070\\
4&1944&1728&9168&76458.
\end{array}
\tag{7.1}
\]
It also checked the two channel contributions and the disconnected
subtraction using exact rational arithmetic, and verified the
boundary-dependent expression (3.10) for every separated edge pair
with a nonzero counted entry. The rational arithmetic gave
\(1/324+3/676-1/144=127/219024\) and
\(219024\cdot256=56070144\). No floating point, vacuum sampling,
eigenvalue fitting, heavy job, Lean run, remote write, or new agent
was used. These finite checks supplement the all-\(L\) geometric,
operator, and analytic proofs above.

For reproducibility, the essential independent incidence check is the
following executable standard-library Python. It constructs the two
counts from different combinatorial operations and tests the full
correction, so it does not assume the disputed identity while checking it.

```python
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product

def plus(n, i):
    out = list(n)
    out[i] += 1
    return tuple(out)

def boundary(p):
    n, i, j = p
    return frozenset(((n, i), (plus(n, i), j),
                      (plus(n, j), i), (n, j)))

for L in (2, 3, 4):
    vertices = tuple(product(range(-L, L + 1), repeat=3))
    edges = tuple((n, i) for n in vertices for i in range(3) if n[i] < L)
    faces = tuple((n, i, j) for n in vertices
                  for i, j in combinations(range(3), 2)
                  if n[i] < L and n[j] < L)
    bd = {p: boundary(p) for p in faces}
    star = {e: set() for e in edges}
    for p in faces:
        for e in bd[p]:
            star[e].add(p)
    B = {e: set() for e in edges}
    for p in faces:
        for e in bd[p]:
            B[e].update(bd[p] - {e})
    assert all(len(B[e]) == 3 * len(star[e]) for e in edges)
    T = Counter()
    adjacent_count = 0
    for shared, incident in star.items():
        for p, q in combinations(incident, 2):
            assert bd[p] & bd[q] == {shared}
            adjacent_count += 1
            for e in bd[p]:
                for f in bd[q]:
                    T[e, f] += 1
                    T[f, e] += 1
    B2 = Counter()
    for e in edges:
        for shared in B[e]:
            for f in B[shared]:
                B2[e, f] += 1
    tested = (set(T) | set(B2)
              | {(e, f) for e in edges for f in B[e]}
              | {(e, e) for e in edges})
    separated_count = 0
    for e, f in tested:
        re, rf = len(star[e]), len(star[f])
        correction = ((re + rf - 4) * int(f in B[e])
                      + (re * re - 4 * re) * int(e == f))
        assert T[e, f] == B2[e, f] + correction
        if e != f and f not in B[e]:
            assert T[e, f] == B2[e, f]
            separated_count += int(T[e, f] > 0)
            adjacent = F(3, 4)**2 * (F(4, 27)**2 * F(1, 4)
                                     + F(4, 39)**2 * F(3, 4))
            disjoint = F(3, 4)**2 * F(1, 9)**2
            assert disjoint == F(1, 144)
            assert adjacent == F(1, 324) + F(3, 676)
            all_pairs = re * rf
            assert 0 <= T[e, f] <= all_pairs
            connected = ((all_pairs - T[e, f]) * disjoint
                         + T[e, f] * adjacent - F(all_pairs, 144))
            assert connected == F(127, 219024) * T[e, f]
    origin_x = ((0, 0, 0), 0)
    origin_y = ((0, 0, 0), 1)
    separated_x = ((0, 2, 0), 0)
    assert T[origin_x, separated_x] == B2[origin_x, separated_x] == 1
    assert T[origin_x, origin_y] - B2[origin_x, origin_y] == 4
    print(L, len(edges), len(faces), adjacent_count, separated_count)
assert F(1, 324) + F(3, 676) - F(1, 144) == F(127, 219024)
assert 219024 * 256 == 56070144
```

Continuity record: this reused worker read the entire specified root
source before deriving the coefficient and graph correspondence. The
earlier native-band outputs were preserved. Only this independent
derivation/review file is owned by this second calculation; the root
source and the separate all-orders volume work were not edited. The
existing root logbook and user-input provenance continue to apply.
