# Root-owned TO/CAU: exact support propagation proposals

These are proposals for the root's complete derived TO/CAU files. This lane
does not write either live or derived competing whole file. Existing 341 TO
already includes the independent carriers and `C_U -> C_Omega -> C_+`, so those
valid statements are retained. These are the remaining local use-site edits.

## TO: after the paragraph ending “no colimit over the face-filling arrows is taken.”

```tex
At the empty packet $h=1$, retain $E_1=0$ and the unique zero
section, action and primitive maps on that amplitude space. The
named original source function is nevertheless $F_1=\Theta\phi_*$:
$1(D)$ is the identity, so its defining equation forces that value,
and Mellin gives $\mathcal M F_1=g$. Thus for $1\mid H$ the
actual divisor equation is $H(D)F_H=F_1$; the zero maps on $E_1$
do not replace this nonzero theta boundary. These endpoint equations
are now used at the definitions and divisor identities in AG, MCF
and CFA, with their complete proofs.
The empty coefficient face at a retained outer label is the element
$(W,S;\varnothing,0)$, distinct from global external $\tau_{\rm out}$.
The other zero faces $(W,S;A,0)$ retain their own masks as well.
This is the literal disjoint labelled carrier in (MCF35); the zero
amplitude complexes at these labels do not identify their labels.
```

## TO.8: after “The complete unit $g/h$ is retained in (TO.8).”

```tex
For the empty family of prescribed jets, take $h=1$ and $P=0$;
then the representative in (TO.8) is $F_\alpha=0$ and its class
is zero. This representative is distinct from the named seed inverse
$F_1=\Theta\phi_*$ above. They have different defining inputs:
$S_1\Theta(0(D)\phi_*)=0$, whereas $S_1\Theta\phi_*=\Theta\phi_*$.
This verifies the empty case of the inverse without a unit inverse
in the zero amplitude space.
```

## CAU: after the coefficient paragraph ending “independent carrier $G(E)^n$.”

```tex
At the empty coefficient mask the amplitude complex is zero at its
retained outer label $(W,S)$; the carrier element
$(W,S;\varnothing,0)$ is distinct from global external
$\tau_{\rm out}$. More explicitly, for $X=U,\Omega$ retain
$Q_{W,X}=\mathscr B_X/\Theta W$ and the same present source legs
as in (CAU.28), with central term $\mathscr B_X$. In each active
coordinate the exact original kernel sequence is
\[
 0\to(V/W)^A\xrightarrow{[v_i]\mapsto[\Theta v_i]_W}
 Q_{W,X}^A\to(T_XQ)^A\to0.
\]
Injectivity follows from that of $\Theta$, the last kernel consists
exactly of the classes of these theta functions, and the last arrow
is onto by $\mathscr B_X=q^{-1}(T_XQ)$. The inclusion
$\mathscr B_U\subseteq\mathscr B_\Omega$ gives
\[
 0\to Q_{W,U}^A\to Q_{W,\Omega}^A\to(T_LQ)^A\to0.
\]
Its quotient is $\mathscr B_\Omega/\mathscr B_U$; the full Bezout
decomposition in (MCF41b)--(MCF41f) identifies it with $T_LQ$.
The source denominator is unchanged, so no proper-source kernel is
removed by this inclusion. Balancing preserves all these sequences
by the same stalkwise flatness as (CAU.28), and every coefficient
insertion commutes coordinatewise. This proves the full source-chain
comparison on the earlier anchored support diagram itself.
```

## CAU: after the final finite packet comparison to AG6--13

```tex
On a nonempty packet the original function section and the strict
polynomial-linear map remain related by (AG8a)--(AG8b):
$\kappa_h^0(P)=P(D)e_h(D)\phi_*$ and
$\kappa_h^1(P)=P(D)e_h(D)F_h$, with
$e_h=r_h(j_h(g/h)^{-1})$. Their cochain equation is
$\kappa_h^1(hP)=\Theta\kappa_h^0(P)$, and their difference from
the finite section is the original theta boundary of the polynomial
$(Pe_h-r_h(\varepsilon_h[P]_h))/h$ applied at $D$ to $\phi_*$.
Thus the balanced arrow used here is $O\otimes_A\kappa_h$;
its cohomology is the same packet injection. No balancing of the
non-$A$-linear function section is asserted. The full divisor maps,
their composition homotopies, and the compatibility between those
homotopies are (CFA.22a)--(CFA.22d), and all coefficient faces retain
these exact maps independently.
```

Notation compatibility: CAU uses `A=C[t]` with `t` acting by `D`; the
`A_sp=C[s]` in AG8a is related by the stated variable-renaming isomorphism.
The root should either retain the CAU `t` glyph in these formulas or insert
that isomorphism explicitly. No spectral variable is identified with the
negacyclic coefficient coordinate.
