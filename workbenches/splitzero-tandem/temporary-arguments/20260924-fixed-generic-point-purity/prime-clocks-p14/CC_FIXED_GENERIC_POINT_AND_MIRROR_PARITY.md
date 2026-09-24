# The fixed generic point and the parity exchanged by the mirror

24 September 2026. Reading and derivation from the original author TeX of Alain Connes and Caterina Consani, *The Absolute Twistor Line and the Geometry of the compactification of Spec Z*, arXiv:2609.00299v1. This note uses the paper's actual topological space and sheaf action. It does not replace the user's tau by a midpoint, vector, complex coordinate or numerical distance. It does not assume a torsion construction or a purity conclusion.

## CC1. The source space and why its generic point is fixed

The source's Section 3, original CC.tex lines 499–541, specifies

\[
X=\{+, -,\eta\},\qquad
\mathcal T=\{\varnothing,\{\eta\},\{+,\eta\},\{-,\eta\},X\}.
\]

The two affine opens correspond to the two orderings of the integer group. Their intersection is the generic open and corresponds to the group without a selected ordering. The paper's Section 4 exchanges the closed points by its geometric automorphism alpha.

Here is a derivation of fixedness from this source topology, rather than an extra axiom attached to a candidate pivot. The closed subsets are the complements of the displayed opens:

\[
\varnothing,\quad\{+\},\quad\{-\},\quad\{+,-\},\quad X.
\]

The only closed set containing eta is X. Thus the closure of {eta} is X. The singleton {+} is closed, and so is {-}; neither is dense. Therefore eta is the unique point whose singleton is dense. A homeomorphism sends the closure of a set to the closure of its image: continuity gives inclusion in one direction, and continuity of the inverse gives the reverse inclusion. Hence every homeomorphism of X fixes eta. In particular the source automorphism alpha does. Since alpha exchanges + and -, they are not fixed. Consequently

\[
\operatorname{Fix}_X(\alpha)=\{\eta\},\qquad
\alpha(+)= -,\qquad\alpha(-)= +.
\]

This proves uniqueness and fixedness using the actual source, without affine coordinates. It agrees with the displayed formula in Definition def:alpha_symmetry, CC.tex lines 773–798.

## CC2. The exact parity statement follows, rather than being added

Keep the user's Z2 notation for the two orientation labels exchanged by the mirror. In this calculation their target is the two-element set

\[
Q_2=\{\mathrm{even},\mathrm{odd}\},\qquad
r(\mathrm{even})=\mathrm{odd},\quad
r(\mathrm{odd})=\mathrm{even}.
\]

The use of the names even and odd labels this two-state orientation observation. It does not identify the source chart inversion with addition of one to every integer, nor erase the full integer coefficients.

An assignment of these labels that respects the mirror has to satisfy

\[
p(\alpha x)=r(p(x))
\]

where the assignment is defined. This equation states that the label changes when the two mirror states are exchanged; it is not a numerical operation involving the user's tau.

On the exchanged pair {+,-}, there are exactly two such assignments: choose either label at +, and the equation forces the other label at -. Both satisfy the equation at both points.

Neither extends to eta. Indeed CC1 has proved alpha(eta)=eta. Extension would require

\[
p(\eta)=p(\alpha\eta)=r(p(\eta)).
\]

But neither of the two values of Q2 is fixed by r. This is a contradiction. Thus the point's lack of a mirror-exchanged Z2 label is a consequence of the topology and symmetry already in the paper. It has not been inserted as a new axiom.

This is specifically the orientation label exchanged by this mirror. A fixed point can still support nontrivial symmetry data; CC3 computes that data. An invariant label on a representation is a different observation from the free two-state label just specified.

## CC3. The point is fixed while its retained data transform

The full generic stalk in the enriched source is

\[
\mathcal O(\{\eta\})
=\mathbf F_{1^2}[T^{\mathbb Z},J]/(J^2=\epsilon),
\qquad \epsilon^2=1.
\]

The imaginary generator and the sign are retained. The source involution satisfies

\[
\alpha^*(T)=\epsilon T^{-1},\qquad
\alpha^*(J)=\epsilon J,\qquad
\alpha^*(\epsilon)=\epsilon.
\]

These are the source's equations, not operations assigned to the user's tau.

At the underlying pointed-monoid level, every nonabsorbing element has a unique multiplicative expression

\[
\epsilon^a T^m J^b,
\quad a,b\in\{0,1\},\quad m\in\mathbb Z.
\]

For completeness, uniqueness follows by using J^2=epsilon to identify the nonabsorbing group with Z times Z/4Z: the expression is sent to (m,2a+b mod 4). The inverse sends (m,k) to T^m J^k. Every k mod 4 has a unique form 2a+b with a,b in {0,1}. This is an exact description of the source multiplicative relations, retaining the full integer m, sign and imaginary branch; it is not a quotient discarding them. The absorbing zero is a separate monoid element.

Multiplicativity gives the complete action

\[
\alpha^*(\epsilon^a T^m J^b)
=\epsilon^a(\epsilon T^{-1})^m(\epsilon J)^b
=\epsilon^{a+m+b}T^{-m}J^b.
\]

Negative m are allowed because T and epsilon are units. Applying the same formula a second time gives epsilon exponent a+m+b-m+b=a+2b, integer exponent m, and branch exponent b. Since epsilon^2=1, the original element is recovered. No sign or exponent is suppressed from this check.

An element fixed by alpha must have m=-m, hence m=0. With m=0, equality of the sign coordinate requires b=0. The fixed nonabsorbing monoid elements are therefore exactly 1 and epsilon; together with the absorbing element they form {0,1,epsilon}. This computation is at the stated multiplicative level, before any additional additive realization.

In particular alpha acts nontrivially on the retained stalk even though eta is fixed as a point. For example J and epsilon J are distinct in this source and are exchanged. The quotient therefore retains isotropy: the two group elements identity and alpha both stabilize eta. The paper records this at CC.tex lines 891–899. Lack of a freely exchanged point-label must not erase that isotropy or the stalk action.

The spatial exponent changes m to -m. Consequently m modulo 2 is unchanged under this particular exponent inversion. This exact formula retains the distinction between the exchanged chart-orientation label in CC2 and ordinary integer residue; their full comparison cannot be replaced by using the word parity for both.

## CC4. The previously established connection with the user's Wick/Cartan work

The July source modular_cartan_realform_bridge_20260719.tex, lines 226–248, uses the parameter involution

\[
\rho(\zeta)=-\overline\zeta,
\qquad \rho(t+is)=-t+is.
\]

Here zeta is that source's complex modular parameter; it is neither the Riemann zeta function nor the user's tau. The real coordinate changes sign while the imaginary coordinate is retained. This is a formula about the supplied July operator construction, not a vector structure assigned to tau.

In the first Connes–Consani source, arXiv:2606.06604v1, Corollary luriearch, the exact cover is

\[
P=\mathbb C^\times/\mathbb R_{>0}
\longrightarrow
B=\mathbb C^\times/\mathbb R^\times,
\qquad [z]_+\longmapsto[z]_{\mathbb R}.
\]

The two rays over a line are exchanged by [z]_+ to [-z]_+. The July theorem, lines 722–768, constructs the associated real rank-two bundle with relation

\[
(p,t+is)\sim(rp,-t+is).
\]

Its map to the orientation line together with the retained imaginary coordinate is

\[
[p,t+is]\longmapsto([p,t],(\pi(p),is)).
\]

It is well-defined because replacing (p,t,s) by (rp,-t,s) preserves the class [p,t], the base pi(p), and is. Conversely a pair ([p,t],(pi(p),is)) maps to [p,t+is]. Choosing the other representative replaces (p,t) by (rp,-t), exactly the defining relation, so the inverse is well-defined. The composites are the identities by substitution; in every local covering chart the maps are continuous and real-linear. This proves the earlier typed comparison with all coordinates retained. The first summand is the orientation/Möbius line, and the second is a trivial imaginary line.

The later source's descended complex-point symmetry is

\[
\sigma(z)=-1/\overline z,
\qquad \sigma(0)=\infty,\quad\sigma(\infty)=0.
\]

Let I(z)=1/z, including I(0)=infinity and I(infinity)=0. Direct substitution gives

\[
I\circ\rho=\rho\circ I=\sigma.
\]

The original inversion, minus sign and conjugation all remain present. The two-copy orbit derivation is written in CARTAN_WICK_SPLINE_COMPARISON.md C2 and MIRROR_AND_PURITY.md M3 and is checked against the original CC.tex theorem at lines 989–1033.

The fixed generic topological point eta and the formula on complex-valued points belong to the actual source at their stated levels. The complex-valued-point involution has no fixed point: a finite nonzero fixed point would give z*conjugate(z)=-1, and the two endpoints are exchanged. This fact does not remove eta from the underlying three-point topological space. The paper uses both levels.

## CC5. Receiving statement for the user's construction

The user's latest statement is that the rotation is around their Z1/tau, and that its missing mirror parity is to be derived rather than stipulated. CC1–CC2 prove the fixed-base/no-exchanged-parity mechanism on the actual Connes–Consani source. Its unique generic point is the specific source object to compare with that proposed role for tau. It is not defined by averaging two numbers and is not the numbered endpoint zero.

This note has not declared a full identification of the source's enriched generic stalk with the user's latest Z0/no-torsion and Z1/torsion-without-parity proposal. That would have to retain the sign, imaginary generator, complete exponent data and involution in CC3; naming eta tau is not that construction. The existing Wick/Cartan comparison is retained in CC4 rather than discarded.

There is no additive-tau calculation here. The parity statement is a proved consequence about the specified mirror observation, not a new axiom. The user's proposed route to purity remains the research target; no numerical distance or RH conclusion is substituted for it.

## Sources and exact reading

- Alain Connes and Caterina Consani, [The Absolute Twistor Line and the Geometry of the compactification of Spec Z, v1](https://arxiv.org/html/2609.00299v1#S3), Sections 3–5. Original author TeX used: literature/lorscheid_sources_20260923/papers/06_new_user_intake/2609.00299/tex/CC.tex. This step read lines 350–407, 415–548, 557–685, 725–913, 970–1056, 1140–1225. No claim of reading the whole paper is made.
- Alain Connes and Caterina Consani, [On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve, v1](https://arxiv.org/html/2606.06604v1#S4.SS1.SSS1), Corollary luriearch. Original FF.tex lines 1521–1587 reread in this step.
- The supplied July modular-Cartan TeX, sections headed Canonical parity splitting of the modular plane and Typed descent of time and radial directions. Original lines 202–256 and 712–783 reread in this step.

Public arXiv pages were used to verify source identity. Mathematical reading used the original local TeX. The generic-point parity derivation and the multiplicative action were independently derived by a mathematical sub-agent; no independent agent was used for file discovery or recordkeeping.
