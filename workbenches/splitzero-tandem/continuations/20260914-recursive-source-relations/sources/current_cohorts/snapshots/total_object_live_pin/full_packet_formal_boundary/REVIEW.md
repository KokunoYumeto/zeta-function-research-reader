# Independent review: full-packet formal boundary

Reviewer: `/root/full_packet_formal_boundary/formal_boundary_review`.

Scope: the exact formal global-to-local comparison for the original polynomial
twisted de Rham complex, its phase-coordinate matrices, and the induced
u-connection. The standalone parent TeX will receive a separate final read
when available. This file records independent derivations rather than an RH
endpoint or a claim that formal data determine analytic Stokes matrices.

## Topology, cohomology, and explicit inverse

The global ring is C[s][[u]], not C[[u]][s]. Its coefficient polynomials may
have unbounded s-degree as the u-degree grows. The local ring at rho is
C[[y]][[u]], with y=s-rho. The coefficientwise Taylor map is well defined
and commutes with u partial_s+h. It need not be surjective as a ring map.

For a local h=y^m a(y), a(0) nonzero, use the exact splitting of a coefficient
f as h q+r, where r is its Taylor polynomial of degree below m and
q=(f-r)/h. Given p=sum u^n p_n, set q_{-1}=0 and recursively divide
p_n-partial_y q_{n-1}=h q_n+r_n. This gives uniquely p=Lq+r. The same
construction with ordinary polynomial division gives the global splitting
with remainder degree below d. Injectivity of L follows at the first
nonzero u-coefficient. Hence H^0=0 and H^1 is free of rank m locally and
d globally over C[[u]]. Every recursion uses only finitely many earlier
u-coefficients and is continuous for the stated topology.

Write A and B for these global and summed local complexes; let I be the
Taylor/phase map. Let R_A,R_B denote remainder retractions, i_A,i_B the
degree-one remainder inclusions, and H_A,H_B division-quotient homotopies.
Then dH+Hd=1-iR. The induced matrix is T=R_B I i_A and satisfies
R_B I=T R_A. Since T_0 is invertible, T^{-1} is obtained coefficient by
coefficient: S_0=T_0^{-1} and
S_n=-T_0^{-1} sum_{j=1}^n T_j S_{n-j}.
The reverse chain map is J^0=0, J^1=i_A T^{-1}R_B. Exactly JI=i_A R_A,
and H_A contracts 1-JI. On B, H'_B=H_B(1-IJ) satisfies
dH'_B+H'_Bd=1-IJ because R_B IJ=R_B. Thus the comparison has explicit
chain maps and homotopies, not merely matching ranks.

## Phase coordinate and Jacobian

Put N=m+1, c=Phi(rho), and
a(y)=N(Phi(rho+y)-c)/y^N. Choose b with b^N=a(0) and retain that choice.
Then w=y a(y)^(1/N), with the root whose constant term is b, is a formal
coordinate. Its inverse is y=psi(w). The degree-zero map is substitution;
the degree-one map contains the indispensable Jacobian:
f(s) ds maps to f(rho+psi(w)) psi'(w) dw. The differential becomes
u partial_w+w^m, while the phase constant remains c.

For the unchanged ascending global monomial columns and ordered local rows,
the matrix T_0 is the Hermite/CRT matrix followed by the local triangular
one-form coordinate changes. The diagonal of the latter block is
b^{-(a+1)}, 0<=a<m. Consequently

det T_0 = product_rho b_rho^{-m_rho(m_rho+1)/2}
          product_{rho<sigma}(sigma-rho)^{m_rho m_sigma}.

The inverse sends q(w) dw to q(w(y)) w'(y) dy modulo y^m and applies the
full Hermite/CRT inverse. No jet or Jacobian is omitted.

## Complete remainder and matrix coefficients

In the standard local complex, the exact reduction is
R(w^{a+qN})=(-u)^q product_{ell=0}^{q-1}(a+1+ell N) w^a
for 0<=a<m. The residue class m modulo N has zero remainder. This follows
from R(w^j)=-u(j-m)R(w^{j-N}) for j>=m, including j=m.

Formal residue substitution gives a useful closed coefficient formula:

[w^j] f(rho+psi(w))psi'(w)
  = [y^j] f(rho+y)a(y)^{-(j+1)/N}.

Indeed both are the residue of f(rho+y)w(y)^(-j-1)dy. Therefore the
(rho,a),b matrix entry is the complete series

sum_{q>=0} (-u)^q product_{ell<q}(a+1+ell N)
  [y^{a+qN}](rho+y)^b a(y)^{-(a+qN+1)/N}.

Each u coefficient is a finite Taylor coefficient computation retaining
all original phase coefficients. There is no convergence assertion.

## Connection and coincident critical values

Use the source convention from marked_product_boundary_connection:
G=-C_h/u^2+B_h/u on the original basis. On the local phase basis the
connection matrix is D with entries -c_rho/u^2+(a+1)/(N_rho u).
The exact compatibility equation is T'+D T=T G. Since both traces equal
-sum m_rho c_rho/u^2+d/(2u), the identity also gives
det T(u)=det T_0 over C[[u]]. This is stronger than invertibility modulo u.

An independent exact observation handles equal critical values without
forgetting their distinct root labels. If rho is different from sigma
but Phi(rho)=Phi(sigma)=c, then Q_sigma B_h Q_rho=0. To prove this, choose
the degree-below-d representative f supported at rho. Its division is
Phi f=h q+c f, since all other primary jets vanish. At sigma, Phi-c has
order at least m_sigma+1 and f has order at least m_sigma; hence q has
order at least m_sigma+1 and q' is zero modulo (s-sigma)^m_sigma. The
definition of B_h as the derivative of this quotient proves the claim.

The formal projectors are T^{-1} E_rho T. They reduce to the original
CRT projectors and are horizontal for the formal connection. This does
not identify analytic sectorial gluing or supply a finite-field/complex
Frobenius comparison.

## Multiplication and source-type check

Multiplication by an arbitrary f(s) is not a chain endomorphism of the
deformed complex: f Lq=L(fq)-u f' q. Therefore the fixed marked arithmetic
matrix A_h, or the full Taylor-unit matrix U_h, extended in the original
monomial basis, must be transported as T A_h T^{-1} and T U_h T^{-1}.
They are not automatically identified with multiplication on the local
twisted cohomology. At u=0 these maps are the full Jacobian-weighted jet
conjugations. The same rule applies to original coefficient/source masks
and projectors. All conclusions must preserve this map type.

## Independent exact check

`review_exact_check.py` and `review_exact_check.json` test the stated
coefficient, connection, and determinant identities over exact rationals
for h=s^2(s+1), with multiplicities 2 and 1 and retained phase roots b=1.
This is an identity test, not an actual RH packet or a substitute object.

The resulting T_0 is [[1,0,0],[-1/2,1,0],[1,-1,1]]. The determinant is 1.
With T calculated through u^4, T'+D T-T G is zero through Laurent powers
-2,-1,0,1,2; det T is 1 through u^4; the trace equality holds exactly.
All checks passed. This finite check supplements the proofs above and
does not replace their all-orders statements.

Current status: intended identities PASS; final parent-source audit pending.

## Exact analytic comparison that limits a formal-monodromy claim

The original global contours provide more than a warning about missing Stokes
data. They compute the ordinary u-loop monodromy directly. Keep the displayed
ordered rays ell_j at arguments (arg u+pi)/(d+1)+2pi j/(d+1) and the cycles
Gamma_j=-ell_0+ell_j, 1<=j<=d. Along a positive loop of u, every ray moves
continuously through a decaying leading-term sector and ends at ell_{j+1}
(indices modulo d+1). Absolute convergence is uniform locally along the
loop: the leading term is negative of order r^(d+1), while all lower terms
have order at most r^d. The integrand is entire in s and single valued in u.
Thus analytic continuation ends with exactly

Gamma_j -> Gamma_{j+1}-Gamma_1 for j<d,
Gamma_d -> -Gamma_1.

The resulting constant row matrix M is the reduced cyclic permutation
representation of d+1 rays. Its eigenvalues are all nontrivial (d+1)-st
roots of unity, each once, and its characteristic polynomial is
(z^(d+1)-1)/(z-1). The nonzero full period determinant already proved in
the original boundary-connection source identifies these cycles with the
entire period basis. There is no invariant vector and the representation
has order d+1, for every retained lower coefficient of h.

This is ordinary analytic period monodromy, while the diagonal phase
connection supplies formal monodromy. They must not be conjugated merely
because the formal lattice map is invertible over C[[u]]. For an exact
illustration, h=s^2-1 has two simple critical points: each formal block has
the period monodromy eigenvalue -1, but the ordinary global ray matrix has
the two nontrivial cube roots. Actual Stokes gluing accounts for the
difference. This example verifies the map type, not an RH obstruction.

On the actual ordered k-fold period tensor, ordinary analytic monodromy is
M tensor ... tensor M. A basis eigenvector is indexed by (a_1,...,a_k) with
1<=a_i<=d and eigenvalue exp(2pi i sum a_i/(d+1)). Root-of-unity filtering
gives invariant dimension (d^k+d(-1)^k)/(d+1). This statement concerns the
full global ray representation and must not be confused with the sum of
the labelled formal primary-block invariant dimensions.
