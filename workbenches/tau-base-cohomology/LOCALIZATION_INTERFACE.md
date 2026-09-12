# The global localization complex and its geometric comparison

Continuation of `FINITE_OPERATOR_COMPARISON.md`, Sections 7.1–7.2. These are written deductions in the specified analytic module category, not new Lean-certified declarations.

## 1. Extract the full arithmetic divisor without choosing a finite packet

On the analytic strip \(\mathscr S=\{0<\Re s<1\}\), retain

\[
\mathcal M_Q=\mathcal O\otimes_{\mathbb C[t]}Q,
\qquad \beta:\mathcal M_Q\longrightarrow\mathcal D_g=\mathcal O/(g),
\qquad g=2\xi.
\]

The computed decomposition in the main note is

\[
\mathcal M_Q\cong\mathcal D_g\oplus\mathcal N,
\qquad \mathcal N=\ker\beta,
\qquad \mathcal K\otimes_{\mathcal O}\mathcal N\cong\mathcal N.
\]

The section of beta is the inverse of beta on the intrinsic torsion subsheaf. It therefore commutes with the retained scaling and convolution actions, which are \(\mathcal O\)-linear on this realization. No list of zero locations is input to that section.

Define the explicit localization complex

\[
L_g(\mathcal M_Q)
=[\mathcal M_Q\xrightarrow{\ell_g}\mathcal M_Q[1/g]],
\qquad \ell_g(m)=m/1,
\]

in degrees zero and one. This is the usual principal-ideal, module-theoretic local-cohomology complex over the locally Noetherian analytic coefficient ring. Its terms and cohomology can also be calculated directly from the displayed decomposition, without invoking that general identification.

The first summand is killed by g. Multiplication by g is invertible on the second, since that summand is a module over meromorphic functions. Thus

\[
\mathcal M_Q[1/g]\cong\mathcal N,
\qquad \ell_g(d,n)=n.
\]

The actual chain map

\[
(\beta,0):L_g(\mathcal M_Q)\longrightarrow\mathcal D_g[0]
\]

is consequently a quasi-isomorphism:

\[
\boxed{H^0L_g(\mathcal M_Q)\cong\mathcal O/(2\xi),\qquad
H^1L_g(\mathcal M_Q)=0.}
\]

This is a cohomological extraction from the actual balanced arithmetic quotient. The defining map is localization at the unchanged theta multiplier g, not deletion of a selected spectral packet.

## 2. Propagate the original support through localization

At each retained support label \(\lambda\), reconstruct

\[
\widetilde\ell_g(\lambda,m)=(\lambda,m/1),
\qquad
z_L(\lambda,m)=(\lambda,0).
\]

External tau remains the global zero of the reconstruction. The internal cycles are the equalizer of \(\widetilde\ell_g\) and \(z_L\). Their \(\lambda\)-fibre is the actual torsion module \(\mathcal D_g\). The internal cokernel is the support skeleton because the ordinary localization map is surjective. Its labelled zeros are not all replaced by external tau.

The maps to the ordinary amplitude complex are exactly the source reconstruction/projection maps. For any nonzero bottom fibre required by a later diagram, the same formulas retain that module at bottom. The assertion here about a single external absent element is the original zero-bottom specialization, not an assumption about every possible opposite-index diagram.

The parent coefficient square \(G(\mathbb Z)\to G(\mathbb C)\) over \(\mathbb Z\to\mathbb C\) remains attached. Inverting the analytic function g is not inverting the scalar e. These two operations are related by the maps from the original supported localization complex to its coefficient amplitudes, not identified with one another.

## 3. The exact comparison to geometric support

Let \(j:U=\mathscr S\setminus V(g)\hookrightarrow\mathscr S\) be the open inclusion. There is a canonical derived morphism

\[
u_g:\mathcal M_Q[1/g]\longrightarrow Rj_*j^*\mathcal M_Q.
\]

It is obtained from the adjunction unit of the localized module and the identity
\(j^*(\mathcal M_Q[1/g])\cong j^*\mathcal M_Q\). Its composite with \(\ell_g\) is the adjunction unit of \(\mathcal M_Q\).

Thus there is the exact typed comparison

\[
\begin{array}{ccc}
\mathcal M_Q&\xrightarrow{\ell_g}&\mathcal M_Q[1/g]\\
\Vert&&\downarrow u_g\\
\mathcal M_Q&\longrightarrow&Rj_*j^*\mathcal M_Q.
\end{array}
\]

Taking fibres gives

\[
L_g(\mathcal M_Q)\longrightarrow
\operatorname{Fib}(\mathcal M_Q\to Rj_*j^*\mathcal M_Q).
\]

In particular the module-theoretic extraction and the geometric-support object are connected by an actual morphism. Their possible difference is

\[
\boxed{\operatorname{Cone}\bigl(
L_g(\mathcal M_Q)\to
\operatorname{Fib}(\mathcal M_Q\to Rj_*j^*\mathcal M_Q)
\bigr)
\cong\operatorname{Cone}(u_g)[-1].}
\]

No isomorphism between those two support functors has been assumed. The difference cone, with its inherited arithmetic action, is the specified object for the next geometric comparison. A module over meromorphic functions can have nontrivial extension behaviour as a sheaf on a punctured analytic neighbourhood; the explicit arrow u_g retains that issue instead of inferring geometric acyclicity from invertibility of g alone.

## 4. The endomorphism-ring lift used by the finite projectors

The main note uses the notation \(G(\operatorname{End}_{\mathbb C}Q)\). For precision, this is the following explicit extension of the same formula to an associative, possibly noncommutative, ring B:

\[
G_{\mathrm{ass}}(B)=\{\tau\}\sqcup B^\bullet,
\quad b^\bullet\oplus c^\bullet=(b+c)^\bullet,
\quad b^\bullet c^\bullet=(bc)^\bullet,
\]

with tau the additive identity and multiplicative absorber. Associativity and distributivity follow by the same supported/absent case calculations; multiplicative commutativity is not asserted. For commutative B it is the original G(B).

For B=End(Q), define

\[
\mathcal L:G_{\mathrm{ass}}(B)\to
\operatorname{End}_{G(\mathbb C)}(Q^\tau),
\]

by \(\mathcal L(f^\bullet)(v^\bullet)=f(v)^\bullet\),
\(\mathcal L(f^\bullet)(\tau)=\tau\), and \(\mathcal L(\tau)\) the constant-tau map. Direct evaluation proves preservation of addition, composition, identity, and the external zero. In particular

\[
\mathcal L(0_B^\bullet)=\varepsilon,
\qquad\varepsilon(v^\bullet)=0_Q^\bullet,
\qquad\mathcal L(\tau)(v^\bullet)=\tau.
\]

For disjoint finite packets, \(\Pi_Z\Pi_W=0_B\), so the original supported lifts compose to epsilon. This is the precise associative-semiring interface used there; it is not a claim that the commutative-ring-only source functor already had noncommutative objects in its declared domain.
