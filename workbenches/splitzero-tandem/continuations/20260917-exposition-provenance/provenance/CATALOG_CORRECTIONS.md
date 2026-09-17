# Exact corrections to three recorded catalogue formulations

These findings concern the programme's catalogue wording, not errors attributed to the cited authors. Original records remain preserved. This note supplies explicit maps or counterexamples; source-sensitive sign conventions remain recorded separately.

## Mapping-torus lift

For the convention
\(M_\alpha=\{f\in C([0,1],A):f(1)=\alpha(f(0))\}\),
the path \(f(t)=(1-t)p+t\alpha(p)\) has endpoints \(p,\alpha(p)\) and satisfies the defining condition. It is a self-adjoint lift when \(p\) is a projection; it need not be a path of projections.

The recorded reversed interpolation \(g(t)=tp+(1-t)\alpha(p)\) instead has endpoints \(\alpha(p),p\). In \(A=\mathbb C^3\), let \(\alpha\) cyclically permute the coordinate projections \(e_1\mapsto e_2\mapsto e_3\mapsto e_1\), and take \(p=e_1\). Then \(g(1)=e_1\) while \(\alpha(g(0))=e_3\), so it does not belong to this mapping torus.

The exact convention map is time reversal \((\rho f)(t)=f(1-t)\). It preserves products and adjoints pointwise, satisfies \(\rho^2=1\), and sends the condition \(f(1)=\alpha(f(0))\) to \((\rho f)(0)=\alpha((\rho f)(1))\). Moreover \(\operatorname{ev}_1\rho=\operatorname{ev}_0\). This is an isomorphism to the reversed-endpoint convention. The boundary/Bott sign must still be checked against Blackadar's specified convention; the endpoint correction alone does not determine it.

## Separable versus a countable approximate identity

An equivalence between separability and existence of a countable approximate identity is false. The unital C*-algebra \(\ell^\infty(\mathbb N)\) has the constant approximate identity \(1,1,\ldots\). It is not separable: the characteristic functions of all subsets of \(\mathbb N\) form an uncountable family whose distinct members have norm distance one. Balls of radius less than one half about them are disjoint; a countable dense set would need a distinct point in each ball, which is impossible. Any cited result requiring separability must retain that hypothesis.

## Extending a general homomorphism to multipliers

A blanket extension assertion also needs hypotheses. Consider the inclusion
\(\iota:C_0((0,1])\hookrightarrow C([0,1])\) by zero extension at the left endpoint. The multiplier algebras are \(C_b((0,1])\) and \(C([0,1])\). If a *-homomorphism between them extended \(\iota\), then for every multiplier \(f\) and \(a\in C_0((0,1])\), multiplicativity would give \(\widetilde\iota(f)\,a=\iota(fa)\). Choosing \(a(t)\ne0\) at any fixed \(t>0\) forces \(\widetilde\iota(f)(t)=f(t)\). For \(f(t)=\sin(1/t)\), that is incompatible with continuity at zero. Thus no such extension exists for this inclusion. This does not disprove a separately constructed concrete multiplier map; its formula and hypotheses must be checked directly.
