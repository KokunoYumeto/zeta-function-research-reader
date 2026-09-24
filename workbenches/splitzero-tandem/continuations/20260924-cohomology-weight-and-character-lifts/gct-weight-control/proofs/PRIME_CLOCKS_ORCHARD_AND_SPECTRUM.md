# Prime clocks, orchard visibility, and faithful prime observations

24 September 2026. Private continuation. Proofs P1–P14. This receives the user's proposal that prime spectral appearances should recover all other counts. The word torsion in that proposal means retained winding. Finite-order groups below are identified explicitly. No arithmetic operation, coordinate or distance is assigned to tau. No RH conclusion or identification of these character values with arithmetic Frobenius eigenvalues is asserted.

## P1. Integer winding from the actual oriented-ray covering

Connes–Consani, arXiv:2606.06604v1, Corollary luriearch, gives the actual covering
\[
P=\mathbb C^\times/\mathbb R_{>0}\longrightarrow B=\mathbb C^\times/\mathbb R^\times.
\]
Original FF.tex lines 1521–1580 were reread for this calculation. The source complex scalar origin is not identified with the user's tau, and the reference line chosen below is not the generic point eta of the other source paper.

Write a nonzero complex number as r exp(i theta), with r>0. The two quotient maps identify respectively angles differing by 2pi and by pi. Thus the maps
\[
\mathbb R\longrightarrow P,\quad\theta\longmapsto[e^{i\theta}]_+,
\qquad
\mathbb R\longrightarrow B,\quad\theta\longmapsto[e^{i\theta}]_{\mathbb R^\times}
\]
retain periods 2pi and pi respectively. These are coordinates on the source's ray and line spaces, not coordinates of tau. Intervals of length less than pi project injectively to B; their translates by integer multiples of pi give its covering charts.

Fix the reference line ell_0=[1]. A continuous loop in B based there has a unique continuous real angle lift starting at zero. To construct it, subdivide the compact parameter interval so each successive piece lies in one covering chart and choose the next branch to match the preceding endpoint; branch uniqueness follows because two lifts differ by an integer multiple of pi, locally constant and zero initially. The endpoint is m pi for a unique integer m. A based homotopy preserves m: lift the homotopy by the same overlapping-chart construction on a finite rectangular subdivision of its compact parameter square; the lifted terminal value is continuous and lies in the discrete set pi Z, so it is constant.

Every m is attained by the loop u->exp(i m pi u) modulo real scaling. Two lifted loops with the same endpoints are homotopic relative endpoints by linear interpolation of their real angle lifts; projecting gives a based homotopy. Concatenation adds endpoint angle displacements. Therefore
\[
\pi_1(B,\ell_0)\cong\mathbb Z,\qquad[\gamma]\longmapsto\frac{\widetilde\gamma(1)}{\pi}.
\]
The displayed division retains the original pi period. Lifting further to P shows that the ray returns to itself precisely for even m; for odd m it returns to the opposite ray. Thus the actual covering's monodromy is m->m mod 2. A full turn has angle 2pi and count two; it is not identified with zero count.

This derives integer winding from the source covering geometry rather than only naming a stalk T^Z. It still uses that covering geometry; its existence is not derived from a bare point alone. Reflection of source angles theta->-theta reverses m and preserves its parity.

In the other source, arXiv:2609.00299v1, keep the full generic group
\[
G=\langle T,J\mid TJ=JT,\ J^4=1\rangle,quad\epsilon=J^2,
\quad A(T)=\epsilon T^{-1},\quad A(J)=J^{-1}.
\]
Keep its finite-order subgroup H=<J> and the map q:G->L=G/H. Set t=q(T). The map from the just-computed fundamental group to L sends a loop of lifted angle m pi to t^m. It is a group isomorphism by the two explicit infinite cyclic descriptions. It sends ray-return parity to the source-derived observation delta(t^m)=epsilon^m. It also intertwines angle reflection with the induced action t^m->t^(-m). On G itself the sign epsilon^m remains in A(T^m); the isomorphism to L does not remove the full extension from the construction. Reversing the chosen winding orientation replaces both generators by their inverses.

## P2. The prime clocks and the exact meaning of irreducible

For each n>=1, form C_n=L/[n]L, where [n](ell)=ell^n and [n]L is the subgroup of n-th powers. These are finite winding-state groups at the same supporting point eta. Choosing t writes the n distinct states as the classes of 1,t,...,t^(n-1). The step S_n multiplies by the class of t. It visits all n states and has period n.

Every subgroup of L is <t^d> for a unique d>=0, where d=0 denotes the trivial subgroup. For a nontrivial subgroup, choose the least positive exponent d present. Division with remainder shows every exponent in the subgroup is divisible by d; conversely all multiples of d occur. Hence the subgroups of C_n are precisely
\[
\langle t^d\rangle/\langle t^n\rangle,\qquad d\mid n,
\]
with n/d elements, and quotient C_d. For n>=2 this proves
\[
 n\text{ prime}\ \Longleftrightarrow\ C_n\text{ is a nontrivial simple cyclic group}
 \ \Longleftrightarrow\ C_n\text{ has no quotient with size strictly between }1\text{ and }n.
\]
This is the precise irreducibility condition. Transitivity alone does not detect primes, since every C_n is transitive under S_n.

An equivariant clock map f:C_m->C_n satisfies f(S_m x)=S_n f(x). Consequently f(t^k)=t^k f(1). It is well defined exactly when t^m=1 in C_n, that is n divides m. When this holds every choice of f(1) gives one map; all are surjective, and exactly one preserves the initial state. Thus a pointed clock isomorphism C_m->C_n exists exactly when m=n. In particular the prime clocks yield pairwise non-isomorphic objects over the same eta, but composites also yield distinguishable objects. Simplicity, not distinguishability alone, separates primes.

The original sign and branch data remain in G. The full quotient map G->C_n has kernel
\[
K_n=\langle T^n,J\rangle,
\qquad 1\to K_n\to G\to C_n\to1.
\]
Both J and epsilon are retained in that exact sequence. Taking this clock observation does not replace the full source by its quotient.

## P3. Prime degree as indecomposable winding scale

The map [n]:L->L has image [n]L and index n. Every group endomorphism of L is one of the power maps [a], because its image on t determines its values on every element. The composition law is [a][b]=[ab]. Therefore a positive degree n>1 is prime precisely when [n] cannot factor as [a][b] with a,b>1.

On the character circle Hom(L,S^1), precomposition by [n] sends z=chi(t) to z^n. It is an n-sheeted cover: every point has n distinct roots and a sufficiently short target arc has n disjoint continuous root branches. Any factorization into connected finite covers of degrees a,b has n=ab by counting the inverse images of one point. Conversely n=ab supplies the explicit factorization z->z^b->z^(ab). This proves the same prime criterion for covering degree. Degree one is invertible and degree zero is a constant map, not a finite-sheeted cover.

Scaling [n] and unit winding S are different source maps: [n](t^m)=t^(nm), whereas S(t^m)=t^(m+1). Their relation to the count is explicit and neither is an operation on eta or tau.

## P4. Euclid's orchard and the exact clock observation

The orchard uses the arithmetic count lattice Z^2. Its lattice zero is not tau; its coordinates are counts already recovered in P1. A nonzero pair (a,b) is visible when no lattice point lies on the open segment from the lattice zero to (a,b).

Put d=gcd(|a|,|b|). If d>1 then (a/d,b/d) is an interior lattice point. If d=1, Bezout gives integers r,s with ra+sb=1. Any interior lattice point lambda(a,b), 0<lambda<1, would satisfy lambda=r(lambda a)+s(lambda b), hence lambda would be an integer, a contradiction. Thus visibility is equivalent to gcd(|a|,|b|)=1.

In C_n the state t^a has order n/gcd(a,n): writing a=da',n=dn' with coprime a',n', the return condition n divides ka is equivalent to n' divides k. Therefore, for 1<=a<n,
\[
(a,n)\text{ visible}\ \Longleftrightarrow\ t^a\text{ generates }C_n
\ \Longleftrightarrow\ \text{step }a\text{ visits all }n\text{ states}.
\]
The number of such a is phi(n). Every interior point of row n is visible exactly when n is prime: for a prime all 1<=a<n are coprime; for a composite n a divisor 1<d<n yields an invisible (d,n). A single visible vector need not represent a prime: (1,4) is visible. The complete-row property is the prime detector.

## P5. Reconstructing positive integers from prime divisors

Every integer n>1 has a prime divisor: its least divisor greater than one is prime, since any nontrivial factor of it would be a smaller divisor. Repeated division terminates because the positive quotient strictly decreases. Thus n is a finite product of primes. If a prime p divides ab and does not divide a, Bezout gives ua+vp=1 and multiplication by b proves p divides b. Applying this fact repeatedly to two prime factorizations matches a prime from one with a prime from the other, cancels them, and proves uniqueness by induction on the total number of factors.

Consequently the valuation map is an isomorphism of multiplicative monoids
\[
\mathbb Z_{>0}\longrightarrow\bigoplus_{p\text{ prime}}\mathbb Z_{\ge0},
\qquad n\longmapsto(v_p(n))_p,
\qquad n=\prod_p p^{v_p(n)},
\]
where multiplication on the left corresponds to componentwise addition on the right. The finite product retains every multiplicity. Integer one corresponds to the empty product. Integer zero is not represented by a finite prime product; negative integers require the additional sign. Nothing here identifies any of these with eta or tau.

Observing only the support {p:p divides n} loses multiplicities, as 2 and 4 demonstrate. Observing the full valuations does not. The full integer ring recovered as End(L) also retains addition. Prime factorization alone describes its positive multiplicative monoid and must not silently substitute for the ring structure.

Geometrically, Spec End(L) has one closed point for each positive prime and also the generic zero prime. Composite n is not a new prime point; its arithmetic is retained in the quotient End(L)/n End(L), whose prime-power factors and nilpotent elements are not discarded. This uses the ring and prime-ideal classification already proved in W3–W4, rather than declaring every distinct clock a new prime.

## P6. All prime-clock readings distinguish every winding count

There is a second, stronger meaning of prime observation than just divisor support. Define
\[
\mathcal R:L\longrightarrow\prod_{p\text{ prime}} C_p,
\qquad\mathcal R(\ell)=(\ell\bmod[p]L)_p.
\]
This homomorphism is injective. If two states t^m and t^n have equal images, every prime divides m-n. A nonzero integer has only finitely many positive divisors, whereas there are infinitely many primes: given any finite list, a prime divisor of their product plus one is absent from the list. Hence m-n=0.

For a finite set P of primes the corresponding kernel is [N]L with N=product over p in P of p. Indeed divisibility by the pairwise coprime primes is equivalent to divisibility by their product, by the Bezout argument above. Thus finite prime observations leave exactly the stated ambiguity; the all-prime map separates all integer states. The proof retains prime 2.

This map retains the full residue at each prime, not merely whether that residue is zero. It therefore can distinguish powers such as 2 and 4 even without separately reporting their valuations. No surjectivity onto the infinite product is asserted, and no completion is identified with L.

## P7. Prime character values fill the circle densely without exhausting it

The character group of C_p has the values
\[
\mu_p=\{\exp(2\pi i a/p):a=0,\ldots,p-1\}.
\]
Indeed a character is determined by its value on t, and that value must have p-th power one. Conversely every such value defines a character by t^m->exp(2pi i am/p). The full 2pi factor and the residues a are retained.

Let Gamma be the union of mu_p over all primes. It is countable, being a countable union of finite sets. It is dense in S^1: the p-th roots divide the angle into p arcs of length 2pi/p, and unbounded primes make that mesh smaller than the length of any specified open arc. It is proper: i has order four, which does not divide any prime, so i is absent. For distinct primes p,q the intersection mu_p intersect mu_q is {1}; an element in both has order dividing gcd(p,q)=1.

Thus each prime adds p-1 new character values. This is a circle of character values, not an assertion that a prime is itself a complex point or that every visible orchard ray is prime. One arbitrarily chosen point per prime would be a different construction: the choices exp(2pi i/p) accumulate only at one and do not give this dense family.

## P8. Preserve the full signed source under prime observation

Gamma alone is not invariant under all original source maps. In particular A sends the spatial character coordinate z to -z^(-1), which can have order 2p. Arbitrary sign-preserving commuting source lifts send (z,j) to (z^n j^c,j^b), with n odd, c modulo four, and b odd. The quartic branch cannot be dropped.

For every prime p retain the finite quotient
\[
G_p^{\rm full}=G/\langle T^{4p}\rangle,
\qquad |G_p^{\rm full}|=16p,
\]
with its original J, epsilon and A. The subgroup is invariant under A since A(T^(4p))=T^(-4p), and under every source lift f_(n,c,b) since f(T^(4p))=T^(4pn)J^(4pc)=T^(4pn). Prime 2 is retained, including this quotient's order-eight spatial factor. The exponent 4p is a uniform choice; no claim of minimality for p=2 is made.

Its signed characters are exactly (z,j) with z^(4p)=1 and j in {i,-i}, because epsilon must evaluate to -1 and J^2=epsilon. Define the full domain
\[
\mathcal D=\bigcup_{p\text{ prime}}\{(z,j):z^{4p}=1,\ j\in\{i,-i\}\}.
\]
For g=T^mJ^k retain the evaluation
\[
E_{\mathcal D}(g)(z,j)=z^m j^k,
\qquad E_{\mathcal D}(0)=0.
\]
It preserves multiplication and the absorbing element. Every nonabsorbing value has modulus one: both z and j are roots of unity. To prove injectivity suppose the functions for (m,k) and (m',k') agree. Taking z=1 and j=i gives k=k' modulo four. If d=m-m' is nonzero, choose a prime p not dividing d and set z=exp(2pi i/p), which belongs to mu_(4p). Then z^d is not one, a contradiction. Hence m=m', and the zero function is distinguished from each nonabsorbing function. All full source data are therefore retained.

The original source mirror acts on D by (z,j)->(-z^(-1),-j). It stays in the same p-level since (-z^(-1))^(4p)=1. Each original commuting signed lift acts by (z,j)->(z^n j^c,j^b); its spatial coordinate has 4p-th power one and its branch remains in {i,-i}. Exact equivariance is
\[
E_{\mathcal D}(f(g))(\chi)=\chi(f(g))=E_{\mathcal D}(g)(\chi\circ f).
\]
No sign, branch, or source factor was suppressed in this comparison.

The spatial values union_p mu_(4p) are still countable and dense, since they contain Gamma. They are not the full circle: a primitive ninth root has order nine, and 9 does not divide 4p for any prime p. Thus the full signed construction preserves the user's dense-but-not-exhaustive circle picture while retaining all source symmetries and still separating every integer count.

The common modulus is proved for characters of these actual finite quotients. Deligne purity concerns arithmetic Frobenius eigenvalues and retains the factor N(x)^(w/2), as derived in D1–D5 of DELIGNE_COMMON_MODULUS_AND_WINDING.md. No map identifying those eigenvalues with E_D is established here. The faithful prime-character construction is an exact result on the source data, not an RH conclusion.

## Provenance and scope

Human sources: Alain Connes and Caterina Consani, arXiv:2606.06604v1, original FF.tex Corollary luriearch, lines 1521–1580; and arXiv:2609.00299v1, original CC.tex Sections 3–4, with the exact generic group and sheaf action read in W1–W10. The prime-clock, divisor, orchard, residue and character arguments are completely derived above; no novelty claim is made. An independent mathematical agent derived P2–P4 and reviewed the all-prime separation and character construction. The first paper's original parameter tau=i log(p)/(2pi) is its modular parameter, not the user's tau; it is not used to identify a metric on the user's object.

The controlling user definitions and corrections are retained verbatim in ../TAU_DEFINITIONS_AND_CORRECTIONS_VERBATIM.md. These results do not show that existence of a point forces the source covering or Laurent direction. They derive the integers from the actual oriented-ray covering and then prove precisely which observations characterize primes and recover integer counts.


## P9. Sequential first appearances: the exact absorption sieve

This is the user's revised observation: a composite need not produce a new line. The observer records a channel at its first activation and sees later returns in that same channel. The earlier comparison of the divisor supports of 2 and 4 did not refute this proposed first-appearance observation; it concerned a different observation of an individual number.

Take the source winding progression from the chosen ordering, with one elementary step S(t^n)=t^(n+1). The state at zero winding is the initial identity in L, not eta or the absorbing monoid zero. Applying one step n times visits every state with count 0,1,...,n in order. A composite instruction S^r abbreviates those r successive steps; it does not delete their intermediate states. Each fixed finite prime is reached after finitely many steps, while there is no finite step at which all primes have been reached.

The periodic channel labelled d>=2 is the quotient clock C_d. At time n its state is t^n modulo <t^d>, and it returns to its initial state exactly when d divides n. Thus an earlier count covers a later count through this divisibility relation, not through earlier occurrence alone: 2 covers 4, but 3 does not cover 4.

Define the sequential sieve without presupposing the list of primes. Initially there are no active channels. At each integer time n>=2, let B_n be the set of previously activated d with d dividing n. If B_n is nonempty, create no new channel. If B_n is empty, activate channel n; it registers its initial return now and every subsequent multiple. This rule refers only to the retained progression and its quotient-clock return tests.

The activated counts are exactly the primes. Prove this by induction on n. At n=2 there is no earlier channel and 2 is prime. Suppose the activated counts below n are precisely the primes below n. If n is prime, it has no proper divisor d with 2<=d<n, so B_n is empty and it activates. If n is composite, its least divisor p>1 is prime and satisfies p<n; by the induction hypothesis its channel is already active, and p divides n, so n is covered and does not activate. This proves the assertion at every finite time.

Equivalently the exact first-arrival indicator is
\[
A(n)=\prod_{\substack{p<n\\p\ \mathrm{prime}}}
\left(1-\mathbf 1_{p\mid n}\right),\qquad n\ge2.
\]
The product is finite and retains all overlapping channels. It equals one precisely for a prime, and zero for a composite. The recurrence preceding the formula computes the same active set without requiring primes as prior input.

For example the successive events are: 2 activates; 3 activates; 4 is covered by 2; 5 activates; 6 is covered by both 2 and 3; 7 activates; 8 is covered by 2; 9 is covered by 3. Integer 1 is the multiplicative unit, with a one-state quotient clock and no nontrivial prime channel. It is not identified with the supporting point eta or tau.

This proves why first appearances detect exactly primes and why suppressing repeated appearances does not delete the underlying composite counts. Reconstructing composites retains the channel-composition operation and its multiplicities, as proved in P5; the activation list alone is not asserted to be a record of every state at every time. The proposition derives prime events from the source winding progression and periodic return maps. It does not yet derive that progression from an unstructured absence/presence datum, or identify this binary sieve with the analytic absorption spectrum in Connes's trace formula.

The companion interactive incidence diagram implements this recurrence for counts 1 through 48. Its equal-height channel marks mean that a channel is present; they assert no spectral weight, geometric radius from tau, or purity theorem. A finite display illustrates the proved all-n statement and is not evidence substituting for its induction proof.


## P10. Finite histories and the inductive whole

The user further proposes that ordered winding history is essential and that the whole collection of counts is obtained only through indefinite continuation. The exact construction retains the finite stages rather than positing a last infinite-time event.

In the actual source winding group take L_+={1,t,t^2,...}, selected by the chosen ordering and generated by one positive winding step. For each finite n let H_n={1,t,...,t^n}, with the order inherited from their exponents and inclusion H_n->H_(n+1). The distinctness of these states follows from P1's winding calculation, not from assigning new labels to the same parity value. Every finite history is a prefix of every later history of the same deterministic run.

The union H_infinity=union_(n>=0) H_n is exactly L_+. It has the following universal property. Given maps f_n:H_n->Y agreeing on successive overlaps, define f(t^k)=f_n(t^k) for any n>=k. Compatibility makes this independent of the chosen n, and this defines the unique map extending all f_n. Thus H_infinity is the direct limit of the finite histories. The already proved exponent correspondence identifies it with N including zero. Each individual count k belongs to H_k; no count first appears at an additional infinite-time stage. There is no largest finite H_n, since t^(n+1) is absent from H_n.

The winding step maps each history state to its successor. A composed instruction S^r represents r such steps; its mathematical prefixes remain S,S^2,...,S^r. Sequential generation does not require a storage device to retain a separate copy of every frame: the initial state, known transition rule and full count uniquely determine those prefixes. It does require retaining enough information to distinguish t^n from t^(n+2); parity alone cannot do that.

The sieve states of P9 are compatible under these same inclusions. At stage n every count from 2 through n has either activated a prime channel or returned through one already active. The union of all prime channels covers exactly the positive integers >=2: each has a least prime divisor, while the unit 1 has none. Every individual count is processed at a finite stage, and every individual prime activates at a finite stage. No finite stage contains all primes, by Euclid's proof in P6.

This gives a precise sense of internal sequential order. It does not identify the step parameter with physical time, posit a Hamiltonian, or establish that no other faithful representation of these histories exists. P6 and P8 explicitly construct other faithful encodings of the same count. The present theorem describes the generation by one winding step and its compatible finite observations.


## P11. The exact uniform infinite-observation statement

Use the full prime-clock readings, not only the binary sieve-event indicator. For a finite nonempty prime set P put M_P=product_(p in P)p. P6 proves that the fiber over the readings of an integer n is n+M_P Z. It is infinite. No finite set of those readings isolates n among all integers. Every infinite set of distinct primes does isolate it, since a nonzero difference has finitely many prime divisors. Thus the minimum cardinality of a family of prime residue observations isolating any given n is aleph_0, the same for all n.

The quantifiers are important: for every finite P there is some n_P different from n with the same readings, but there is no single n' different from n that has the same readings at every prime. This is an exact global-observation property. It does not prevent n from being specified in another representation, such as a finite successor history.

For the full signed source G and the character family D of P8, equality of observations at the finitely many p in P has kernel
\[
\{T^{4M_P r}:r\in\mathbb Z\}.
\]
Proof: equality with the identity at z=1,j=i forces k=0 modulo four. Equality for every z in mu_(4p) forces 4p to divide m for each p in P. The least common multiple of these 4p is 4M_P: every odd prime in P occurs once, and the power of two is four if 2 is absent and eight if 2 is present. Conversely divisibility by 4M_P makes all the stated evaluations one. Thus every fiber remains infinite at a finite observation stage, while the full family separates G by P8. This statement retains the source's four branch states and the extra two-adic factor in the chosen uniform family.

The equal aleph_0 value is an observation-complexity invariant relative to this family of finite clocks. It is not the definition of Deligne weight, an eigenvalue modulus, or a metric on tau. The following construction gives an actual common-modulus theorem from the global clock completion.

## P12. A compact global completion and its exact modulus theorem

For each finite nonempty prime set P retain the quotient
\[
G_P=G/\langle T^{4M_P}\rangle
\cong (\mathbb Z/(4M_P)\mathbb Z)\times(\mathbb Z/4\mathbb Z).
\]
The isomorphism sends T^mJ^k to (m modulo 4M_P,k modulo four), retaining both coordinates. For P contained in Q the transition G_Q->G_P reduces the first coordinate and leaves the second unchanged. All these finite groups have their discrete topologies. Define
\[
K=\varprojlim_P G_P
\]
as the space of compatible families, with the subspace topology from their product. The constraints of compatibility are closed, so K is a closed subspace of a product of finite compact spaces and is compact. Equivalently choose the cofinal sequence of sets of the first N primes; the diagonal subsequence argument proves compactness of the resulting countable product, and the compatibility equations retain a closed subset. Multiplication and inversion are coordinatewise and continuous.

The map i:G->K sends a source element to all its finite residue classes. It is injective by P11: all residues equal identity force k=0 modulo four and every 4M_P to divide m, hence m=0. It has dense image. A basic open condition specifies only finitely many quotient coordinates. Their union Q is a finite prime set; a compatible value in G_Q has a representative T^mJ^k in G, whose image satisfies all those conditions. Thus every nonempty basic open set meets i(G). This is a faithful embedding with retained finite observations, not an identification of G with its completion.

The cofinal sets P containing 2 give the more explicit full description
\[
K\cong(\mathbb Z/8\mathbb Z)\times
\prod_{p\ \mathrm{odd\ prime}}\mathbb Z/p\mathbb Z
\times(\mathbb Z/4\mathbb Z).
\]
To verify it, use 4M_P=8 times the product of the odd primes in P. The reduction map modulo these pairwise coprime factors is injective because an integer divisible by each is divisible by their product; it is surjective by Bezout's identity, constructing a representative for each finite list of residues. These finite isomorphisms commute with every transition, so taking compatible families gives the displayed isomorphism. The final factor remains the source J-branch. The first factor comes from the chosen uniform 4p observation family, including p=2; it is not declared a minimal completion.

All original source symmetries used above extend continuously. At a finite level, the source mirror is
\[
A_P(m,k)=(-m,2m-k),
\]
where the first coordinate is modulo 4M_P and the second modulo four. This is well defined because 4 divides 4M_P. It is a homomorphism of order two and it commutes with reductions. Hence it induces A_K on K. Each sign-preserving commuting lift has finite formula
\[
f_{n,c,b;P}(m,k)=(nm,cm+bk),
\qquad n,b\text{ odd},\quad c\pmod4,
\]
with the same respective moduli. This is well defined, continuous and compatible with transitions, so it extends to K as well. No source sign is removed by the extension.

Now let chi:K->C^times be a continuous group character. Its image is a compact subgroup of C^times because K is compact. The modulus image is therefore a compact subgroup of R_(>0). Such a subgroup is {1}: if it contains r>1 then the powers r^n are unbounded, contrary to compactness; if it contains 0<r<1 then it contains r^(-1)>1. Consequently
\[
\boxed{|\chi(x)|=1\quad\text{for every }x\in K.}
\]
This is the common-modulus theorem for the constructed global clock completion. It follows from compactness and the multiplicative character law. It neither measures a distance from eta nor assigns infinite modulus to source elements.

The continuous characters can also be classified without an extra hypothesis. Consider the open arc V={exp(i theta): |theta|<pi/3}. It contains no nontrivial subgroup of S^1. Indeed, if a nonidentity value already lies outside V it is excluded; if it is exp(i theta) with 0<|theta|<pi/3, the power with exponent ceil(pi/(3|theta|)) has an angle between pi/3 and 2pi/3 in absolute value and lies outside V. Continuity gives an identity neighborhood in K whose image lies in V. Some kernel N_P of K->G_P is contained in that neighborhood, since finite quotient conditions form a neighborhood basis. Its character image is a subgroup contained in V, hence trivial. Thus chi factors through G_P.

Conversely every character of a finite G_P pulls back to a continuous character of K. The source signed condition chi(epsilon)=-1 requires j=chi(J) in {i,-i}. Its restriction to G therefore has exactly the original formula
\[
\chi(T^mJ^k)=z^m j^k,
\qquad z^{4M_P}=1\text{ for some finite }P,
\qquad j\in\{i,-i\}.
\]
All original factors are retained. These signed characters separate K: at a finite quotient where two elements differ, their branch difference is detected with z=1,j=i when that difference is nonzero modulo four; otherwise a character z detecting the distinct first residues, with j=i, separates them. Thus the global completion and every original winding state are faithfully observable by this continuous signed character family.

This construction also identifies the exact continuity obstruction for original source characters not in this family. The original character chi_(2,i)(T^mJ^k)=2^m i^k is valid on the uncompleted G. Along a cofinal sequence P_N, the source elements T^(4M_(P_N)) converge to identity in K, because every fixed finite quotient eventually sends them to identity. Their chi_(2,i) values are 2^(4M_(P_N)), which do not converge to one. That character cannot extend continuously to K. The full original character space is retained in the record; the map of continuous characters of K into it is a proved inclusion, not a replacement obtained by rescaling values.

There are consequently two distinct proved statements: every original winding state requires infinitely many unrestricted prime-clock observations to isolate it in this observation topology; and every continuous character of the compact global clock completion has modulus one. The second follows through the explicit topology and group structure, not by renaming the first statement as purity. Deligne weight w is the arithmetic eigenvalue relation |iota alpha|=N(x)^(w/2), with its full residue-norm factor. No identification of these clock characters with the required arithmetic cohomology has been supplied by the completion theorem.


## P13. Retaining all stacked prime powers

The intermediate completion K in P12 is faithful on the original group G but is not the completion of all winding clocks. At an odd prime p its spatial factor is F_p. Multiplication by p, and multiplication by p^r for any r>=1, both have the same zero image on that factor and are invertible at every other prime factor. Their spatial image index is p in K, not p^r. Thus the intermediate observer does not preserve every covering-degree multiplicity after completion. This defect does not identify source integers, but it matters to the user's stacking operation.

Retain all finite clock quotients instead. For each positive integer N put
\[
\widetilde G_N=G/\langle T^{4N}\rangle
\cong\mathbb Z/(4N)\mathbb Z\times\mathbb Z/4\mathbb Z.
\]
For N dividing M use reduction modulo 4N in the first coordinate and retain the branch coordinate. Define
\[
\widehat G=\varprojlim_{N\mid M}\widetilde G_N.
\]
The moduli 4N are cofinal among all positive integer moduli: every modulus d divides 4d. A coherent family at moduli 4N therefore extends uniquely to all moduli by reduction, and restriction gives its inverse. Hence
\[
\boxed{\widehat G\cong\widehat{\mathbb Z}\times\mathbb Z/4\mathbb Z,
\qquad\widehat{\mathbb Z}=\varprojlim_N\mathbb Z/N\mathbb Z.}
\]
The space is compact by the same finite-product and closed-compatibility proof as P12. The source map T^mJ^k -> ((m mod N)_N,k) is injective: a nonzero integer m cannot be divisible by every positive N. Its image is dense because every basic finite compatible residue prescription reduces to one prescription modulo the least common multiple and has an integer representative. The absorbing zero is retained separately as an isolated absorbing point; it is neither the group identity nor the supporting eta.

Prime factorization and the same finite Bezout construction identify the spatial completion with product_p Z_p, where Z_p=lim_r Z/p^r Z. Every modulus involves finitely many prime powers; finite compatibility constructs its residue from those components. Conversely the residue family restricts to every prime-power chain. Thus all p^r information, including the entire prime-two chain, is retained.

The original source involution and all the classified commuting signed maps extend continuously:
\[
\widehat A(x,k)=(-x,\,2(x\bmod4)-k),
\qquad
\widehat f_{n,c,b}(x,k)=(nx,\,c(x\bmod4)+bk),
\]
with n,b odd and second coordinate modulo four. These formulas descend at every modulus 4N and commute with the transition maps, so are well defined. They restrict to the original source formulas. The earlier completion K is a quotient of this one: retain x modulo eight, x modulo each odd prime, and k modulo four. This projection records exactly which higher prime-power coordinates that intermediate observer omitted; it does not replace the full completion.

For any positive n, multiplication by n on Zhat is injective and has image equal to the kernel of reduction modulo n. Here is a direct proof without an exactness assumption about inverse limits. If nx=0, inspect its coordinate modulo nm for an arbitrary positive m. A representative a of x modulo nm satisfies nm divides na, hence m divides a. Its reduction x modulo m is zero; all coordinates are therefore zero. Conversely, if x modulo n is zero, choose a representative a of x modulo nm divisible by n, and define y modulo m to be a/n modulo m. This is independent of representative, since changing a by nm changes a/n by m. Compatibility of the x coordinates makes these y coordinates compatible. They define y in Zhat with ny=x. Thus
\[
\widehat{\mathbb Z}/n\widehat{\mathbb Z}\cong\mathbb Z/n\mathbb Z,
\qquad [\widehat{\mathbb Z}:n\widehat{\mathbb Z}]=n.
\]
In particular the degree p^r retains its exact index p^r. For a signed source lift with odd nonzero n and odd b, injectivity follows from injectivity of multiplication by n and invertibility of b modulo four. Its image has exactly the condition x in n Zhat; once the unique preimage of x is chosen, the branch equation can be solved uniquely for k. Thus its image index is |n|. The winding map at n=2 also exists and retains index two; this does not remove W5's obstruction to a sign-preserving equivariant lift of even degree on the full source.

Every continuous character of Ghat still has modulus one by compactness, with the complete proof in P12 applying unchanged. Every such character factors through some finite quotient, by the no-small-subgroup arc argument. The continuous signed characters restrict to the original G as
\[
\chi_{z,j}(T^mJ^k)=z^m j^k,
\qquad z\text{ any root of unity},\quad j\in\{i,-i\}.
\]
Every root of unity occurs since its finite order divides 4N for some N. Conversely the finite quotient relation forces that order condition. These signed characters separate Ghat by the finite-coordinate proof, and separate all original source elements. The character values are a dense proper subset of the unit circle, with all prime powers now retained.

This gives a compact global object carrying the entire sequence of finite clock observations, faithfully retaining original integers and preserving winding-cover degrees. Its character-modulus theorem is proved. It is not an identification of Ghat with Spec Z, nor a construction of the arithmetic cohomology whose eigenvalues enter Deligne purity.

## P14. The exact degree factor in the clock operators

### P14.1. Measure and change of variables

Write K_w=Zhat for the winding factor of the full group Ghat=Zhat x C_4 in P13. Every variable in the following integrals belongs to K_w, not to tau. Retain a finite nonzero translation-invariant Haar measure mu with arbitrary total mass h=mu(K_w)>0. Its measure on a residue class modulo M is h/M: the M classes partition K_w and translations permute them. These assignments are compatible with refinement, since each class modulo M is a disjoint union of M'/M classes modulo M' when M divides M'. They describe the measure directly on every finite clock. No choice h=1 or rescaling of operators is made.

For a positive integer n, P13 proves that multiplication phi_n(x)=nx is injective, with clopen image nK_w of index n. It is a homeomorphism from K_w onto nK_w, since a continuous bijection from a compact space to a Hausdorff space has continuous inverse. Division x/n is used only on nK_w. Each of its n cosets has measure h/n. The measures (phi_n)_*mu and n mu restricted to nK_w are translation invariant on that subgroup and both have mass h. Uniqueness of Haar measure at specified mass gives
\[
\int_{K_w}F(nx)\,d\mu(x)=n\int_{nK_w}F(y)\,d\mu(y).
\tag{P14.1}
\]
This identity holds for nonnegative measurable F and for integrable complex F. It can also be checked first on each residue-class cylinder using the class measures h/M, then extended to nonnegative measurable functions by the measure extension and monotone convergence theorems. It implies mu(nE)=mu(E)/n and mu(phi_n^{-1}(E))=n mu(E intersect nK_w). Thus both image and inverse image preserve null sets, including for the completed measure.

### P14.2. Unrescaled operators and adjoints

Let H=L^2(K_w,mu), with inner product linear in its first entry, and define
\[
(U_nf)(x)=f(nx),\qquad
(V_nf)(x)=\begin{cases}f(x/n),&x\in nK_w,\\0,&x\notin nK_w.\end{cases}
\tag{P14.2}
\]
The null-set statement proves these maps are well defined on almost-everywhere equivalence classes. Formula P14.1 gives
\[
\|U_nf\|^2=n\int_{nK_w}|f(y)|^2\,d\mu(y),\qquad
\|V_nf\|^2=\frac1n\int_{K_w}|f(y)|^2\,d\mu(y).
\tag{P14.3}
\]
In particular both operators are bounded. The second equality gives norm(V_n)=1/sqrt(n). The first gives norm(U_n)<=sqrt(n), and equality follows by taking f=1_(nK_w): its squared norm is h/n while U_nf=1_(K_w) has squared norm h. Thus every factor is retained:
\[
\|U_n\|=\sqrt n,\qquad\|V_n\|=\frac1{\sqrt n}.
\tag{P14.4}
\]
For f,g in H, change variables y=nx through P14.1 to obtain
\[
\begin{aligned}
\langle U_nf,g\rangle
&=\int_{K_w}f(nx)\overline{g(x)}\,d\mu(x)\\
&=n\int_{nK_w}f(y)\overline{g(y/n)}\,d\mu(y)
=\langle f,nV_ng\rangle.
\end{aligned}
\]
Cauchy--Schwarz and P14.3 justify these integrals. Hence U_n^*=nV_n and V_n^*=U_n/n. With P_n multiplication by the indicator of nK_w, direct evaluation yields U_nV_n=I and V_nU_n=P_n, and consequently
\[
\boxed{U_nU_n^*=nI,\quad U_n^*U_n=nP_n,\quad
V_n^*V_n=\frac1nI,\quad V_nV_n^*=\frac1nP_n.}
\tag{P14.5}
\]

### P14.3. These factors already occur in the finite clocks

For every positive M give H_M=C^(Z/MZ) the inner product
\[
\langle F,G\rangle_M=\frac hM\sum_{a\bmod M}F(a)\overline{G(a)}.
\tag{P14.6}
\]
The pullback J_M F=F composed with reduction rho_M embeds it isometrically into H, by the measured residue classes above. Define maps with their different domains retained:
\[
u_{n,M}:H_{nM}\to H_M,\quad (u_{n,M}F)(a)=F(na),
\]
\[
v_{n,M}:H_M\to H_{nM},\quad
(v_{n,M}G)(b)=\begin{cases}G(b/n),& n\mid b,\\0,&n\nmid b.\end{cases}
\tag{P14.7}
\]
The map a mod M -> na mod nM is injective with image the residues divisible by n; its inverse there is division by n modulo M. Therefore the displayed formulas are well defined. Their adjoint calculation is
\[
\begin{aligned}
\langle u_{n,M}F,G\rangle_M
&=\frac hM\sum_{a\bmod M}F(na)\overline{G(a)}\\
&=\frac h{nM}\sum_{b\bmod nM}F(b)
\overline{n\mathbf1_{n\mid b}G(b/n)}
=\langle F,nv_{n,M}G\rangle_{nM}.
\end{aligned}
\tag{P14.8}
\]
Thus u_(n,M)^*=n v_(n,M). Also uv=I and vu is multiplication by the divisibility indicator. The completed and finite maps intertwine exactly:
\[
U_nJ_{nM}=J_Mu_{n,M},\qquad V_nJ_M=J_{nM}v_{n,M}.
\tag{P14.9}
\]
The factor n is therefore already forced by finite quotient arithmetic and the two class measures h/M and h/(nM). The construction has not inserted it by choosing an eigenvalue or changing scale.

### P14.4. Composition retains multiplication and common divisors

For positive m,n, evaluating at x gives
\[
U_mU_n=U_{mn}=U_nU_m,\qquad
V_mV_n=V_{mn}=V_nV_m.
\tag{P14.10}
\]
The first equality is f(nmx). For the second the support conditions are x in mK_w and x/m in nK_w, equivalently x in mnK_w; on that set unique division gives (x/m)/n=x/(mn).

There is a more informative mixed relation. Let d=gcd(m,n), a=m/d, b=n/d. Injectivity of multiplication by d proves mx in nK_w iff ax in bK_w. Since a,b are coprime, choose integers r,s with ra+sb=1. If ax in bK_w then x=r(ax)+s(bx) is in bK_w; the converse is immediate. On this support x=by gives mx/n=ay. Therefore
\[
\boxed{U_mV_n=V_{n/d}U_{m/d},\qquad d=\gcd(m,n).}
\tag{P14.11}
\]
The coprime case is U_mV_n=V_nU_m; the common divisor has not been discarded.

### P14.5. Operator modulus and eigenvalue modulus

P14.5 gives the exact positive operator square root
\[
|U_n|=(U_n^*U_n)^{1/2}=\sqrt n\,P_n.
\tag{P14.12}
\]
The equality follows because P_n is a self-adjoint projection, so the nonnegative operator sqrt(n) P_n squares to nP_n. For n>1, P_n and I-P_n are nonzero: their supports have positive measures h/n and h-h/n. Thus U_n^*U_n=nP_n differs from U_nU_n^*=nI, and U_n is not normal.

The same operator has the exact eigenvector
\[
U_n\mathbf1_{K_w}=\mathbf1_{K_w},\qquad
\|\mathbf1_{K_w}\|^2=h.
\tag{P14.13}
\]
For n>1 its eigenvalue 1 has modulus different from sqrt(n). Hence P14.12 is an operator-modulus result; it does not make every eigenvalue have modulus sqrt(n). This statement concerns the constructed operator on its stated full function space. It makes no assertion that another arithmetic cohomological realization or a derived sector cannot have pure weight. No such realization is constructed here. Continuous characters have squared norm h, since their pointwise modulus is one by P13.

### P14.6. The full signed source is retained

Keep the entire Ghat=K_w x C_4, with its original A and sign epsilon, rather than replacing it by K_w. Define its translation-invariant measure by
\[
\int_{\widehat G}F(x,k)\,d\widetilde\mu(x,k)
=\frac14\sum_{k\bmod4}\int_{K_w}F(x,k)\,d\mu(x).
\tag{P14.14}
\]
Its total mass remains h and every branch has mass h/4. Pullback by the winding projection pi(x,k)=x is isometric because the four terms and the factor 1/4 cancel explicitly in the squared norm. This is a retained comparison map, not an identification of the two spaces.

For a positive odd n, c modulo four, and odd b, the original source map F=f_(n,c,b) from P13 is an injective homomorphism onto nK_w x C_4 of index n. Its inverse there is explicitly
\[
F^{-1}(y,l)=\left(y/n,\ b^{-1}\bigl(l-c((y/n)\bmod4)\bigr)\right),
\tag{P14.15}
\]
where b inverse is taken modulo four. Define U_F f=f composed with F and V_F f as f composed with F inverse on its image and zero elsewhere. The same Haar argument, now on the full signed group and its index-n image, gives U_F^*=n V_F and all four relations in P14.5 with the image projection P_F. Every branch and its measure remain present. Moreover pi composed with F=[n] composed with pi, so
\[
U_F\pi^*=\pi^*U_n,\qquad V_F\pi^*=\pi^*V_n.
\tag{P14.16}
\]
These identities follow by evaluating inside and outside the image. Winding degree two retains index two on K_w; this does not assert an even-degree sign-preserving map commuting with A on Ghat, whose obstruction was proved in W5.

### P14.7. What the global construction establishes

The exact chain now proved is: finite clock residues have infinite ambiguity on integer counts (P11); their compatible completion is compact and retains all prime powers and the original signed data (P12–P13); its continuous characters have modulus one (P12–P13); and its arithmetic degree-n maps have index n and the unrescaled adjoint factor n, with operator modulus sqrt(n) on the image sector (P14). These are maps and identities of the original source-derived winding data. Neither the shared countable observation requirement nor the operator modulus is being substituted for Deligne's arithmetic Frobenius eigenvalue relation. P14 was independently derived and its complete finite and infinite computations are recorded here.
