**The next step strengthens the amplification: an off-line quartet would force the same canonical control constant to grow at least cubically in tensor degree.** The proof uses an exterior-power map on the existing arithmetic cohomology, with its original representatives and metric.

The key improvement is

$$
\boxed{
\sum_{\Re\lambda>k/2}
\ell_\lambda(2\Re\lambda-k)
\;\leq\;
\epsilon_{h,k,N}^{\mathrm{cyc}}.
}
$$

Previously, testing one eigenvector bounded the largest individual real-part defect. This bounds **their entire positive sum**, with all generalized-eigenspace multiplicities retained.

For a full nonreal quartet

$$
\tfrac12\pm\delta\pm i\gamma,
\qquad \delta>0,\quad\gamma>0,
$$

of common multiplicity \(m\), the calculation gives

$$
\boxed{
\epsilon_{h,k,N}^{\mathrm{cyc}}
\ge
2\delta[1+k(m-1)](k+1)
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor.
}
$$

For simple roots, that is asymptotic to \(\delta k^3/2\). Thus a **subcubic** upper estimate on the specified arithmetic family would suffice for this contradiction argument; the earlier single-eigenvector argument sought a sublinear estimate. The new lower bound and the exterior comparison are proved below. The subcubic arithmetic upper estimate is not yet proved.

[**Full derivation in the HTML reader**](sandbox:/mnt/data/Tau_Exterior_Trace_Amplification/index.html) · [**LaTeX**](sandbox:/mnt/data/Tau_Exterior_Trace_Amplification/NOTE.tex) · [**Formalization handoff**](sandbox:/mnt/data/Tau_Exterior_Trace_Amplification/HANDOFF.md) · [**Complete package**](sandbox:/mnt/data/Tau_Exterior_Trace_Amplification_2026-09-12.zip)

## 1. The genuine GitHub correction is integrated

I checked the repository at pinned revision
`a4494fba4968db837a8af6fcb952c8688cd5d1da`.

The current sum-connection note makes the empty-packet case explicit. For \(h=1\),

$$
I=(h(s_1),\ldots,h(s_k))
=\mathbb C[s_1,\ldots,s_k],
$$

so every quotient by \(I^r\) is the zero coefficient module. Its split lift still has \(e\) and \(\tau\). The analytic amplitude \(g=2\xi\) and its nonzero mass remain, but they do not create a nonzero finite spectral packet in this case. Every Gram inverse below therefore has an explicitly nonempty packet as its domain.

I also retained the current formalization’s restriction on inverse compression. It proves that operation with its actual inclusion, extraction, self-adjoint projection, and commutation hypotheses. For the spectral subspace used below, I construct its compressed Gram directly rather than assuming those hypotheses for an oblique spectral projector.

The newer conormal and relative-connection results remain inputs. This continuation does not duplicate their dual-number map or claim a new Lean certificate.

## 2. Start with the original canonical arithmetic control

The base remains \(\mathfrak b_\tau\), carrying

$$
\boxed{
\begin{array}{ccc}
G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C.
\end{array}
}
$$

The target of \(p_{\mathbb Z}\) is still infinite. The coefficient maps preserve the supported scalar \(e=0^\bullet\) and external absence \(\tau\) separately before applying the arithmetic quotient.

Keep

$$
C_+=[V\xrightarrow{\Theta}\mathscr B],
\qquad
Q=\mathscr B/\Theta V,
\qquad
D=-x\partial_x,
\qquad
g=2\xi.
$$

For the full finite packet polynomial \(h\), the preceding construction gives

$$
C=C_{h,k}
=
\mathbb C[S]/(\chi_{h,k}),
\qquad
A=M_S,
$$

where \(S=s_1+\cdots+s_k\), and

$$
\chi_{h,k}(S)
=
\prod_\lambda(S-\lambda)^{\ell_\lambda}.
$$

Its actual arithmetic inclusion remains

$$
\eta_{h,k}[P]
=
\upsilon_h^{\otimes k}P(A_k)1,
\qquad
\upsilon_h=j_h(g/h).
$$

For each admitted polynomial degree \(N\), retain the canonical representative

$$
R_N:C\longrightarrow\mathscr B^{\widehat\otimes k},
$$

with

$$
J^{(k)}R_N=\eta_{h,k},
\qquad
q^{(k)}R_N=\sigma_h^{\otimes k}\eta_{h,k},
\qquad
G_N=R_N^*R_N.
$$

The existing control identity is

$$
\boxed{
W_N=A^*G_N+G_NA-kG_N
=
G_N
\frac{b_{N+1}b_N^*+b_Nb_{N+1}^*}{\omega_N}
G_N.
}
$$

Here \(b_j=[p_j]_{\chi_{h,k}}\), and \(\omega_j\) is the actual squared norm of the monic orthogonal polynomial \(p_j\) for the convolution measure. In particular,

$$
\omega_0=\mu_h^k,
$$

not \(1\).

The original inverse-kernel comparison remains

$$
v=G_N^{-1}\lambda.
$$

It carries both metric and control Rayleigh quotients exactly, with the representative map attached. 

### Turn that particular form into an operator

Define the Gram adjoint and control endomorphism by the explicit composites

$$
A^{\sharp_{G_N}}=G_N^{-1}A^*G_N,
$$

$$
\boxed{
\mathsf H_N
=
G_N^{-1}W_N
=
A^{\sharp_{G_N}}+A-kI_C.
}
$$

This is an endomorphism of the same \(C\). It is self-adjoint for \(G_N\), has rank at most two, and

$$
\operatorname{Tr}\mathsf H_N
=
2\Re\operatorname{Tr}A-k\dim C=0,
$$

because reflection pairs \(\lambda\) with \(k-\bar\lambda\), with equal lengths.

Consequently its nonzero spectrum is

$$
\boxed{\{+\epsilon_N,-\epsilon_N\}.}
$$

The exact number is the preceding two-row quantity:

$$
\boxed{
\epsilon_N
=
\frac{\sqrt{a_Nd_N-|c_N|^2}}{\omega_N},
}
$$

where

$$
a_N=b_N^*G_Nb_N,\qquad
d_N=b_{N+1}^*G_Nb_{N+1},\qquad
c_N=b_N^*G_Nb_{N+1}.
$$

Nothing about the arithmetic metric has been changed.

## 3. Exterior powers retain the same allowance, rather than multiplying it

For \(1\le p\le\dim C\), define the **additive exterior generator**

$$
A^{[p]}(v_1\wedge\cdots\wedge v_p)
=
\sum_{j=1}^p
v_1\wedge\cdots\wedge Av_j\wedge\cdots\wedge v_p.
$$

Its relationship to the multiplicative exterior action is

$$
\boxed{
A^{[p]}
=
\left.\frac{d}{dt}\right|_{t=0}
\bigwedge\nolimits^p(e^{tA}),
\qquad
\bigwedge\nolimits^p(e^{tA})
=
e^{tA^{[p]}}.
}
$$

In the unscaled wedge basis, let

$$
(G_N^{[p]})_{I,J}
=
\det(G_N)_{I,J}.
$$

The exact control identity is

$$
\boxed{
(A^{[p]})^*G_N^{[p]}
+
G_N^{[p]}A^{[p]}
-kpG_N^{[p]}
=
G_N^{[p]}\mathsf H_N^{[p]}.
}
$$

**The new estimate is**

$$
\boxed{
-\epsilon_NG_N^{[p]}
\preceq
(A^{[p]})^*G_N^{[p]}
+
G_N^{[p]}A^{[p]}
-kpG_N^{[p]}
\preceq
\epsilon_NG_N^{[p]}.
}
$$

There is no factor \(p\) multiplying \(\epsilon_N\).

### Proof

For \(\epsilon_N>0\), retain the Gram-orthogonal eigenspace decomposition

$$
C=L_+\oplus Z_0\oplus L_-,
$$

where

$$
\mathsf H_N|_{L_+}=\epsilon_N,\qquad
\mathsf H_N|_{Z_0}=0,\qquad
\mathsf H_N|_{L_-}=-\epsilon_N,
$$

and both \(L_+\) and \(L_-\) are one-dimensional.

The exterior space decomposes through the actual wedge maps into

$$
\begin{aligned}
\bigwedge\nolimits^p C
={}&
\bigwedge\nolimits^p Z_0\\
&\oplus
\left(L_+\wedge\bigwedge\nolimits^{p-1}Z_0\right)\\
&\oplus
\left(L_-\wedge\bigwedge\nolimits^{p-1}Z_0\right)\\
&\oplus
\left(L_+\wedge L_-\wedge
\bigwedge\nolimits^{p-2}Z_0\right).
\end{aligned}
$$

The additive control eigenvalues on these four parts are respectively

$$
0,\quad\epsilon_N,\quad-\epsilon_N,\quad0.
$$

A nonzero wedge cannot contain the one-dimensional positive control direction twice. That proves the bound. At top exterior degree the control is zero; when \(\epsilon_N=0\), the conclusion follows directly.

The underlying extremal-trace principle is classical Ky Fan theory. The use here is on the programme’s particular source-generated rank-two control, with its original arithmetic metric. ([SIAM][1])

## 4. The exterior operation carries the original theta boundaries

Use the unscaled alternating map

$$
\operatorname{Alt}_p:
\bigwedge\nolimits^p C\hookrightarrow C^{\otimes p},
$$

$$
v_1\wedge\cdots\wedge v_p
\longmapsto
\sum_{\pi\in S_p}\operatorname{sgn}(\pi)
v_{\pi(1)}\otimes\cdots\otimes v_{\pi(p)}.
$$

Its composite with the exterior quotient is \(p!I\).

The actual source representative is

$$
\boxed{
R_{N,p}
=
R_N^{\otimes p}\operatorname{Alt}_p:
\bigwedge\nolimits^pC
\longrightarrow
\mathscr B^{\widehat\otimes kp}.
}
$$

It satisfies

$$
\boxed{R_{N,p}^*R_{N,p}=p!G_N^{[p]},}
$$

and

$$
J^{(kp)}R_{N,p}
=
\eta_{h,k}^{\otimes p}\operatorname{Alt}_p,
$$

$$
q^{(kp)}R_{N,p}
=
(\sigma_h^{\otimes k}\eta_{h,k})^{\otimes p}
\operatorname{Alt}_p.
$$

The factorial is retained in the source Gram and control form. The relative allowance is unchanged because both are multiplied by that same explicitly displayed factor.

### Both cochain signs remain

Each block has cohomological degree \(k\). If \(T_\pi\) is the actual Koszul permutation of the \(p\) blocks, its top-degree action is

$$
T_\pi=(\operatorname{sgn}\pi)^kP_\pi.
$$

The chain idempotent selecting the ordinary exterior top-degree part is therefore

$$
\boxed{
\mathsf A_{p,k}
=
\frac1{p!}
\sum_{\pi\in S_p}
(\operatorname{sgn}\pi)^{k+1}T_\pi.
}
$$

The two top-degree signs multiply to \(\operatorname{sgn}\pi\). The complementary idempotent remains in the complex. These are the standard tensor-complex signs, applied to the actual degree \(k\), not to an ungraded substitute. ([The Stacks Project][2])

Now take the already-constructed primitive

$$
D^{(k)}R_N-R_NA=dK_N^{\mathrm{prim}}.
$$

The exterior primitive is

$$
\boxed{
K_{N,p}^{\mathrm{prim}}
=
\sum_{j=1}^p(-1)^{k(j-1)}
R_N^{\otimes(j-1)}
\otimes K_N^{\mathrm{prim}}
\otimes R_N^{\otimes(p-j)}
\operatorname{Alt}_p.
}
$$

The tensor differential supplies the second occurrence of
\((-1)^{k(j-1)}\), giving

$$
\boxed{
D^{(kp)}R_{N,p}
-
R_{N,p}A^{[p]}
=
dK_{N,p}^{\mathrm{prim}}.
}
$$

**This is the original relation being sent to its supported zero.** The lifted maps retain the product support labels; sums of differently located primitives use their actual join. External absence remains \(\tau\). The internal quotient is still the source’s quotient by boundaries within each fibre.  

The note also connects this representative to the full \(kp\)-factor minimum. With the explicit jet inclusion \(I_{k,p}\), their difference \(\Delta\) is an original theta boundary, and

$$
\boxed{
p!G_N^{[p]}
=
I_{k,p}^*G_{kp,M}^{\mathrm{full}}I_{k,p}
+
\Delta^*\Delta.
}
$$

Its complete control correction is retained. The two metrics are not declared identical.

## 5. A determinant line now measures all positive defects together

Let

$$
C_{>}
=
\bigoplus_{\Re\lambda>k/2}C_\lambda
\subseteq C,
\qquad
p=\dim C_{>},
$$

where \(C_\lambda\) is the **full generalized eigenspace**, of dimension \(\ell_\lambda\).

There is an actual injection

$$
\boxed{
\det C_{>}
\longrightarrow
\bigwedge\nolimits^pC
\xrightarrow{R_{N,p}}
\mathscr B^{\widehat\otimes kp}.
}
$$

The additive generator on this determinant line is

$$
\zeta_{>}
=
\operatorname{Tr}(A|_{C_{>}})
=
\sum_{\Re\lambda>k/2}\ell_\lambda\lambda.
$$

For a wedge of a basis, every off-diagonal replacement repeats a basis vector and vanishes. The surviving coefficient is precisely the trace. This proves the determinant-line action while retaining the original nilpotent spaces upstream.

Its real weight excess is

$$
\boxed{
L_{h,k}
=
2\Re\zeta_{>}-kp
=
\sum_{\Re\lambda>k/2}
\ell_\lambda(2\Re\lambda-k).
}
$$

Apply the exterior control inequality to its nonzero determinant vector:

$$
\boxed{L_{h,k}\le\epsilon_{h,k,N}^{\mathrm{cyc}}.}
$$

This also has an exact volume formulation. If \(B_{>}\) is the column map of an unscaled basis and

$$
G_{>}=B_{>}^*G_NB_{>},
$$

then

$$
\boxed{
\det\!\left(U_{>}(a)^*G_{>}U_{>}(a)\right)
=
a^{kp+L_{h,k}}\det G_{>},
}
$$

where \(U_{>}(a)=a^{A|_{C_{>}}}\).

The source determinant vector has squared norm

$$
p!\det G_{>}.
$$

The exterior estimate bounds its growth between
\(a^{kp-\epsilon_N}\) and \(a^{kp+\epsilon_N}\), with that same norm retained.

### The spectral projection and metric projection are explicitly connected

Let

$$
Q_{>}=e_{>}(A)
$$

be the CRT idempotent selecting these full spectral blocks. Its metric-orthogonal counterpart is

$$
\boxed{
P_{>}
=
B_{>}(B_{>}^*G_NB_{>})^{-1}B_{>}^*G_N.
}
$$

Their exact relationships are

$$
Q_{>}P_{>}=P_{>},\qquad
P_{>}Q_{>}=Q_{>},\qquad
(P_{>}-Q_{>})^2=0.
$$

They give

$$
\operatorname{Tr}(P_{>}A)
=
\operatorname{Tr}(Q_{>}A)
=
\zeta_{>},
$$

and

$$
\boxed{\operatorname{Tr}(P_{>}\mathsf H_N)=L_{h,k}.}
$$

For \(\epsilon_N>0\), the actual rank-one control projections are

$$
F_\pm
=
\frac{\mathsf H_N^2\pm\epsilon_N\mathsf H_N}
{2\epsilon_N^2}.
$$

The full slack is calculated:

$$
\boxed{
L_{h,k}
=
\epsilon_N\left[
1-
\|(1-P_{>})F_+\|_{\mathrm{HS},G_N}^2
-
\|P_{>}F_-\|_{\mathrm{HS},G_N}^2
\right].
}
$$

The complement is retained through

$$
\operatorname{Tr}f(A)
=
\operatorname{Tr}(Q_{>}f(A))
+
\operatorname{Tr}((1-Q_{>})f(A)).
$$

Thus the new trace estimate does not obtain positivity by deleting an unwanted block.

## 6. The quartet gives a cubic, explicitly counted amplification

Take an actual nonreal off-line zero with displacement \(\delta>0\) and height \(\gamma>0\). The functional equation and complex conjugation give

$$
\rho_{\varepsilon,\eta}
=
\tfrac12+\varepsilon\delta+i\eta\gamma,
\qquad
\varepsilon,\eta\in\{+1,-1\},
$$

with common multiplicity \(m\). This uses the original \(\xi\)-symmetry; \(g\) remains \(2\xi\). ([DLMF][3])

The distinct \(k\)-fold sums are exactly

$$
\boxed{
\lambda_{a,b}
=
\frac k2+\delta(2a-k)+i\gamma(2b-k),
\qquad
0\le a,b\le k.
}
$$

There is no genericity assumption about zero ordinates here.

To construct the sum with margins \(a,b\), choose any integer

$$
\max(0,a+b-k)\le t\le\min(a,b).
$$

The four occupation counts

$$
(t,\ a-t,\ b-t,\ k-a-b+t)
$$

are nonnegative and sum to \(k\). Conversely, every occupation has these margins. Since \(\delta,\gamma\) are nonzero, different margins give different sums.

Every local maximal length is

$$
\ell_k=1+k(m-1).
$$

Therefore

$$
\boxed{
\chi_{h,k}(S)
=
\prod_{a,b=0}^k(S-\lambda_{a,b})^{\ell_k},
\qquad
\dim C=\ell_k(k+1)^2.
}
$$

The positive-defect subspace has dimension

$$
p
=
\ell_k(k+1)\left\lceil\frac k2\right\rceil.
$$

Its total excess is

$$
\begin{aligned}
L_{h,k}
&=
2\delta\ell_k(k+1)
\sum_{a=\lfloor k/2\rfloor+1}^{k}(2a-k)\\
&=
\boxed{
2\delta\ell_k(k+1)
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor.
}
\end{aligned}
$$

For \(k=2n\), the inner sum is \(n(n+1)\). For \(k=2n+1\), it is \((n+1)^2\). The imaginary parts cancel in the determinant trace.

The result is the announced bound:

$$
\boxed{
2\delta[1+k(m-1)](k+1)
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor
\le
\epsilon_{h,k,N}^{\mathrm{cyc}}.
}
$$

For simple roots, the leading term is \(\delta k^3/2\). Repeated roots retain the additional factor \(1+k(m-1)\); the construction does not impose simplicity.

## 7. The next analytic target is now weaker—and remains explicit

The required arithmetic quantity is still

$$
\epsilon_{h,k,N}^{\mathrm{cyc}}
=
\frac{\sqrt{a_Nd_N-|c_N|^2}}{\omega_N}.
$$

The new amplification would exclude an actual off-line quartet from a proved estimate

$$
\boxed{
\frac{\sqrt{a_Nd_N-|c_N|^2}}
{k^3\omega_N}
\longrightarrow0,
}
$$

along an admitted choice

$$
\boxed{
N=N(k)\ge[1+k(m-1)](k+1)^2-1.
}
$$

For this contradiction argument, **the packet \(h\) can remain fixed**. Constants may depend on that packet; uniformity across every zero height is not required.

This does not supply the upper estimate. It changes what the next estimate needs to achieve. The new exterior step converts the existing rank-two control into a determinant bound on the sum of the positive defects. That follows the amplification architecture in the retained Deligne reading: carry the same spectral information into a cohomological construction and apply a further estimate there. 

The polynomial-degree cost remains. For a simple quartet it is at least quadratic in \(k\), so the earlier constant-column Fisher estimate cannot be inserted as though it controlled fixed-degree polynomials. The existing full polynomial moment formulas, their \(\mu_h^k\) mass, the derivative cross term, and the inverse interpolation matrix remain the inputs for that calculation.

### Verification and handoff

The new checker passed **22 exact finite test methods**, normally and under `python -O`, with identical successful records. Both deliberately failing controls failed as intended. The supplied cyclic-sum checker’s **24 methods** passed fresh runs in both modes, and all **42 entries** of its source manifest verified.

The tests include nonnormal companion operators, repeated jets, the exterior factorial, additive exterior action, both cochain signs, the two projector maps, determinant-line weights, quartet counting, and the retained \(e/\tau\) cases. Declared Gaussian calibrations are not represented as actual zeta packets.

No new Lean execution, arithmetic interval certificate, or remote repository change is claimed. The [handoff](sandbox:/mnt/data/Tau_Exterior_Trace_Amplification/HANDOFF.md) gives the other session bounded formal targets using its existing library.

**The completed advance is the exterior control theorem and its determinant-line application: the programme now has a proved aggregate spectral bound, an exact cubic quartet calculation, and a subcubic arithmetic target, all carried through the original theta representatives and supported relation maps.**

[1]: https://epubs.siam.org/doi/10.1137/0613006 "https://epubs.siam.org/doi/10.1137/0613006"
[2]: https://stacks.math.columbia.edu/tag/0GWN "https://stacks.math.columbia.edu/tag/0GWN"
[3]: https://dlmf.nist.gov/25.4 "https://dlmf.nist.gov/25.4"
