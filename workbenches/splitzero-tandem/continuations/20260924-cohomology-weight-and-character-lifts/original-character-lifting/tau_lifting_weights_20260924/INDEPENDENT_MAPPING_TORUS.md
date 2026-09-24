# The mapping-torus lifting obstruction and the retained prime jets

Independent derivation, 24 September 2026. This calculation concerns the explicit Connes–Consani prime fiber and its finite compact quotients. It does not identify their full adelic cohomology with the cohomology of these quotients.

The active target is the user's formulation: “Deligne proves that an obstruction to lifting vanishes by separating its weights from those of the classes being lifted.” Sections MT5–MT7 below construct the actual connecting homomorphism and calculate its vanishing or nonvanishing. The preceding Fourier and holonomy calculations fix its signs and the precise receiver.

## Sources and notation

**[CCJ]** Alain Connes and Caterina Consani, *On the Jacobian of \(\overline{\operatorname{Spec}\mathbb Z}\)*, [arXiv:2602.15941](https://arxiv.org/abs/2602.15941). Original source inspected:

`Jacobian.tex`, original author source retained under `sources/`.

The displayed mapping torus is at lines 255–261. The group-fiber calculation is in subsection fibers, lines 1852–1912. The conventions for scaling and its inverse are at lines 2539–2542 and 2587–2593. The local denominator \(1/|1-u|\) appears in subsection geomtrace, lines 2544–2575. This derivation reads these portions, not the entire paper.

**[DII]** Pierre Deligne, *La conjecture de Weil. II*, Publications mathématiques de l'IHÉS **52** (1980), 137–252, [publication record and DOI](https://www.numdam.org/item/PMIHES_1980__52__137_0/). The exact argument being compared is §3.6, Theorem 3.6.1 and Lemmas 3.6.2–3.6.3, pp. 213–214. The local French transcription inspected is:

../deligne_quotient_weight_20260924/sources/S20_FR_record_export.tex,

lines 2467–2553. It is a transcription, not Deligne's original author TeX. Its status must remain explicit.

The user’s current \(Z_1/\tau\) has presence without parity and has no stipulated addition. Nothing below assigns addition to \(\tau\), sends \(\tau\) to an integer, or identifies it with a zero vector. Every vector space, matrix, scalar \(1\), and addition below belongs to the already constructed complex arithmetic receiver. Any retained support index is carried unchanged as an external index; the proofs do not identify distinct support labels.

Fix a rational prime \(p\), and write
\[
 L=\log p>0,\qquad K=K^{(p)}=\prod_{\ell\ne p}\mathbb Z_\ell^\times.
\tag{MT0.1}
\]
Translation \(u\mapsto pu\) is a homeomorphism of \(K\). It is not a group homomorphism of \(K\): it sends its identity to \(p\). Its mapping torus, with the exact source orientation, is
\[
 \mathcal T_p=(K\times\mathbb R)/D^{\mathbb Z},\qquad
 D(u,t)=(pu,t+L).
\tag{MT0.2}
\]
In particular,
\[
 [u,t+L]=[p^{-1}u,t].
\tag{MT0.3}
\]
The source's deck action is multiplication by \(p\); the return of the positive \(t\)-flow on the section \(t=0\) is multiplication by \(p^{-1}\). These are inverse maps, not a change of the source convention.

For a finite quotient \(H=K/U\) by an open subgroup, let \(N=|H|\), let \(\bar p\) denote the image of \(p\), and let \(d=\operatorname{ord}_H(\bar p)\). Then
\[
 \mathcal T_{p,H}=(H\times\mathbb R)/
 ((u,t)\sim(\bar p u,t+L)).
\tag{MT0.4}
\]
Every orbit of \(\bar p\) has \(d\) elements, so this space is a disjoint union of \(N/d\) circles, each of period \(dL\). This follows by following \(t\) from \(0\) to \(dL\): the section label becomes \(\bar p^{-d}u=u\), and \(d\) is the least positive return index.

## MT1. Complete characters, measure, and signs

Equip \(K\) with Haar measure \(\nu\), retain its arbitrary positive total mass \(v_K=\nu(K)>0\), and retain \(dt\) without dividing it by \(L\). On a fundamental domain,
\[
 \int_{\mathcal T_p} f\,d\mu
  =\int_K\int_0^L f([u,t])\,dt\,d\nu(u),
 \qquad \mu(\mathcal T_p)=v_KL.
\tag{MT1.1}
\]
At finite level, each \(u\in H\) has measure \(v_K/N\). Each of the \(N/d\) circles consequently has measure \(v_KdL/N\). The total measure remains \(v_KL\). The endpoints \(0\) and \(L\) are identified by (MT0.3); they are not two independent boundary components.

For a continuous character \(\chi:K\to S^1\), choose a real number \(\theta_\chi\) with
\[
 \chi(p)=e^{i\theta_\chi}.
\tag{MT1.2}
\]
For \(n\in\mathbb Z\), put
\[
 \lambda_{\chi,n}=\frac{2\pi n-\theta_\chi}{L},\qquad
 \Phi_{\chi,n}([u,t])
   =\chi(u)\exp(i\lambda_{\chi,n}t).
\tag{MT1.3}
\]
The function is well-defined because
\[
 \Phi_{\chi,n}(pu,t+L)
  =\chi(p)\exp(i\lambda_{\chi,n}L)\Phi_{\chi,n}(u,t)
  =\Phi_{\chi,n}(u,t).
\tag{MT1.4}
\]
Replacing \(\theta_\chi\) by \(\theta_\chi+2\pi j\) relabels \(n\) by \(n-j\); it does not change the set of functions.

These are precisely all continuous group characters of \(\mathcal T_p\). Indeed, a character lifted to \(K\times\mathbb R\) restricts to some \(\chi\) on \(K\) and to \(t\mapsto e^{i\lambda t}\) on \(\mathbb R\); being trivial on \((p,L)\) gives \(\chi(p)e^{i\lambda L}=1\), which is (MT1.3).

The functions \((v_KL)^{-1/2}\Phi_{\chi,n}\) form an orthonormal basis in \(L^2(\mathcal T_p,\mu)\). For different \(\chi\), orthogonality follows by integrating over \(K\); for fixed \(\chi\), the \(t\)-integral gives the ordinary Fourier orthogonality on \([0,L]\). For completeness, expand a function on the fundamental domain in characters of \(K\); in the \(\chi\)-coefficient, multiplication by \(\exp(i\theta_\chi t/L)\) turns the boundary condition into periodicity of period \(L\). Ordinary Fourier series on that interval then give every \(n\). The character expansion on \(K\) can be obtained by finite quotient averaging: continuous characters factor through finite quotients, and finite-cylinder functions are dense in \(L^2(K)\). For the factorization claim, continuity puts the image of some open subgroup in a sufficiently short arc about \(1\); that arc contains no nontrivial subgroup of \(S^1\), so this open subgroup lies in the kernel.

Define the positive-flow pullback and the inverse-flow action separately:
\[
 U_a f([u,t])=f([u,t+a]),\qquad V_a=U_{-a}.
\tag{MT1.5}
\]
Both are unitary for the positive Haar inner product, since translation preserves (MT1.1). On the displayed basis,
\[
 U_a\Phi_{\chi,n}=e^{i\lambda_{\chi,n}a}\Phi_{\chi,n},
 \qquad
 V_a\Phi_{\chi,n}=e^{-i\lambda_{\chi,n}a}\Phi_{\chi,n}.
\tag{MT1.6}
\]
The self-adjoint operator \(-i\partial_t\), with the boundary conditions above, has eigenvalues \(\lambda_{\chi,n}\). The infinitesimal generator of \(V_a\) is \(-\partial_t\). Thus the source scaling convention \(\vartheta(u)\xi(x)=\xi(u^{-1}x)\) must not be silently replaced by the opposite flow.

## MT2. The full finite-level return distribution

For \(h\in C_c^\infty(\mathbb R)\), the operator \(U(h)=\int h(a)U_a\,da\) is trace class at finite level. Its eigenvalues decay faster than any power of \(n\), by integration by parts in the integral \(\int h(a)e^{i\lambda_{\chi,n}a}\,da\). Since there are \(N\) characters, their absolute sum converges. The trace is
\[
 \operatorname{Tr}U(h)
 =\sum_{\chi\in\widehat H}\sum_{n\in\mathbb Z}
    \int_{\mathbb R}h(a)e^{i\lambda_{\chi,n}a}\,da
 =L\sum_{\chi\in\widehat H}\sum_{r\in\mathbb Z}
      \chi(\bar p)^{-r}h(rL).
\tag{MT2.1}
\]
The last equality is the Fourier series identity for the periodic delta distribution:
\[
 \sum_{n\in\mathbb Z}e^{i(2\pi n-\theta)a/L}
   =L\sum_{r\in\mathbb Z}e^{-ir\theta}\delta(a-rL).
\tag{MT2.2}
\]
There is no pointwise convergence assertion in (MT2.2). Pairing with \(h\) gives the equality used in (MT2.1).

Finite character orthogonality gives
\[
 \sum_{\chi\in\widehat H}\chi(\bar p)^{-r}
   =\begin{cases}N,&d\mid r,\\0,&d\nmid r,\end{cases}
\]
hence
\[
 \operatorname{Tr}U(h)=NL\sum_{j\in\mathbb Z}h(jdL).
\tag{MT2.3}
\]
The Haar mass \(v_K\) cancels from the trace because the basis has norm factor \((v_KL)^{-1/2}\) on each side of the inner product; the Hilbert space still uses the original measure. Every remaining factor is retained: \(N\) is the character count, \(L=\log p\), \(dL\) is the orbit period, and \(j=0\) is the identity-time contribution. For \(V(h)\), the unsummed character coefficient is \(\chi(\bar p)^r\), and the fully summed expression (MT2.3) is unchanged because \(j\) runs through all integers.

For the trivial character alone, positive return times contribute
\[
 (\log p)\sum_{r\ge1}h(r\log p).
\tag{MT2.4}
\]
Restricting to positive times means taking \(h\) supported in \((0,\infty)\); it is not a deletion of the identity-time or negative-time terms from (MT2.1).

This is a trace calculation on the compact fiber. It does **not** contain the transverse local-field factor \(1/|1-u|\) in [CCJ, subsection geomtrace]. That factor comes from a different, explicitly stated transverse scaling kernel. Consequently (MT2.1) is not being represented as the complete Weil explicit formula.

## MT3. A bundle retaining the complete actual prime jet

For \(\rho\in\mathbb C\) and an integer \(m\ge1\), let
\[
 A_{\rho,m}=\mathbb C[T]/(T^m),\qquad
 H_p=p^\rho\exp((\log p)T),\qquad
 p^\rho=\exp(\rho\log p).
\tag{MT3.1}
\]
Here \(T\) acts by multiplication, and the exponential is the exact finite sum
\[
 \exp((\log p)T)=\sum_{j=0}^{m-1}
       \frac{(\log p)^j}{j!}T^j.
\tag{MT3.2}
\]
For an actual zero \(\rho\) of the original zeta function, this is the retained primary jet from the programme. The definition of this receiver makes sense for every \(\rho\); its existence for a value of \(\rho\) is not evidence that \(\zeta(\rho)=0\).

Define the flat bundle over the source-oriented mapping torus by
\[
 E_{\rho,m}
 =(K\times\mathbb R\times A_{\rho,m})/
 \bigl((u,t,v)\sim(pu,t+L,H_p^{-1}v)\bigr).
\tag{MT3.3}
\]
The inverse in the gluing is essential. Positive horizontal transport from \([u,0]\) to \([p^{-1}u,0]\) has fiber map \(H_p\), because
\[
 (u,L,v)\sim(p^{-1}u,0,H_pv).
\tag{MT3.4}
\]
At finite level its holonomy around a full positive circle of length \(dL\) is
\[
 H_p^d=p^{d\rho}\exp(d(\log p)T).
\tag{MT3.5}
\]
Thus no power, logarithm, or nilpotent part has been dropped.

A section is represented by a function \(F\) satisfying
\[
 F(pu,t+L)=H_p^{-1}F(u,t).
\tag{MT3.6}
\]
In the character sector \(F(u,t)=\chi(u)f(t)\), this becomes
\[
 f(t+L)=(\chi(p)H_p)^{-1}f(t).
\tag{MT3.7}
\]
Writing \(f(t)=e^{-t(\rho I+T)}e^{-i\theta_\chi t/L}g(t)\), where \(g(t+L)=g(t)\), gives the exact generator blocks
\[
 \partial_t\big|_{\chi,n}
   =\left(-\rho+\frac{i(2\pi n-\theta_\chi)}{L}\right)I-T.
\tag{MT3.8}
\]
In particular, positive Haar measure on the base does not remove the real part \(-\Re\rho\) or the nilpotent term \(-T\) from this coefficient action.

For completeness, the coefficient trace at finite level is
\[
 \operatorname{Tr}U_{E_{\rho,m}}(h)
  =L\sum_{\chi\in\widehat H}\sum_{r\in\mathbb Z}
       \chi(\bar p)^{-r}\operatorname{Tr}(H_p^{-r})h(rL)
  =mL\sum_{\chi,r}\chi(\bar p)^{-r}p^{-r\rho}h(rL).
\tag{MT3.9}
\]
The proof is (MT2.2) applied to (MT3.8), with
\(\operatorname{Tr}\exp(-rLT)=m\). The inverse-flow convention instead has coefficient
\[
 L\,\chi(\bar p)^r\operatorname{Tr}(H_p^r)
       =mL\,\chi(\bar p)^r p^{r\rho}.
\tag{MT3.10}
\]
All nilpotent terms remain in the bundle and generator; the trace annihilates their strictly triangular parts. Equations (MT3.9)–(MT3.10) therefore do not justify replacing the jet by its semisimplification in a lifting problem.

The formula (MT3.9) may be justified without using a nonorthogonal spectral basis. The invertible smooth gauge in (MT4.1) below changes sections into periodic functions on each finite circle. Its conjugated generator is a constant finite-dimensional matrix plus the periodic derivative. Integration against compactly supported \(h\) gives matrix Fourier coefficients with rapid decay in \(n\), including the finitely many polynomial factors from \(T\). The operator is trace class; trace is invariant under this bounded invertible gauge on the compact circle.

## MT4. Exact triviality and the limit of the positive-metric argument

Put \(A=\rho I+T\), so \(H_p=e^{LA}\). There is an explicit smooth bundle isomorphism to the product vector bundle:
\[
 [(u,t,v)]\longmapsto
       ([u,t],e^{tA}v).
\tag{MT4.1}
\]
It is well-defined because \(e^{(t+L)A}H_p^{-1}=e^{tA}\). Under this map the flat connection becomes
\[
 \nabla=d-A\,dt.
\tag{MT4.2}
\]
The connection term is retained: (MT4.1) is generally not a flat trivialization. Its inverse sends \(w\) to \(e^{-tA}w\).

At finite level, \(E_{\rho,m}\) is flat-trivial precisely when \(H_p^d=I\). Necessity follows by transporting a global flat frame around a circle. For sufficiency, choose a frame at one vertex in each of the \(N/d\) circles and extend it by horizontal transport; \(H_p^d=I\) is exactly the condition that the frame returns to its original value.

For the jet (MT3.1), this condition is exactly
\[
 m=1,\qquad e^{dL\rho}=1,
\quad\text{equivalently}\quad
 m=1,\quad \Re\rho=0,\quad dL\,\Im\rho\in2\pi\mathbb Z.
\tag{MT4.3}
\]
To prove the restriction on \(m\), equality \(H_p^d=I\) first forces its scalar eigenvalue to be \(1\). The coefficient of \(T\) in \(\exp(dLT)-I\) is \(dL\ne0\). Thus the exponential cannot equal \(I\) when \(T\ne0\), which is exactly \(m>1\).

Two bundles of this form over the same finite mapping torus are isomorphic as flat bundles over the identity of the base precisely when
\[
 m=m',\qquad e^{dL\rho}=e^{dL\rho'}.
\tag{MT4.4}
\]
Flat isomorphism implies similarity of the two circle holonomies and hence equal rank and scalar eigenvalue. Conversely, under these equalities the two holonomy matrices in their specified \(T\)-bases are equal. Choose the identity map at one vertex of each circle and extend by the two parallel transports. Equality of the complete loop maps makes this extension well-defined. This proves sufficiency, including the complete nilpotent part.

A positive definite Hermitian metric preserved by parallel transport exists exactly when
\[
 m=1,\qquad\Re\rho=0.
\tag{MT4.5}
\]
Indeed, preservation of a metric makes every loop holonomy unitary for that metric. Its eigenvalues must have modulus \(1\), giving \(p^{d\Re\rho}=1\). A unitary matrix is diagonalizable, whereas the nontrivial jet has a nontrivial Jordan block, so \(m=1\). Conversely, for \(m=1\) and \(\Re\rho=0\), multiplication by \(p^\rho\) has modulus \(1\), and the constant metric descends and is parallel.

This has a precise consequence: the positive Haar inner product in MT1 proves unitarity of scalar translation on the base. It does not prove (MT4.5) for the nonunitary coefficient system (MT3.3). A nonparallel positive metric always exists, for example the metric transported through (MT4.1); its existence does not make the flat transport unitary.

The full prime tuple
\[
 H_q=q^\rho\exp((\log q)T)\qquad(q\ \text{any prime})
\tag{MT4.6}
\]
commutes on \(A_{\rho,m}\). It defines compatible coefficient operators for every \(\rho\) and every \(m\); no condition \(\Re\rho=\tfrac12\) is used in this construction. These are coefficient maps. This statement does not assert that every \(q\) acts as multiplication by a unit on \(K^{(p)}\): when \(q\ne p\), its \(q\)-component is not a unit.

A constant-fiber isomorphism intertwining every \(H_q\) for two such prime tuples forces \(m=m'\) and \(\rho=\rho'\). Rank gives the first equality. Equality of the scalar eigenvalues for \(q=2,3\) gives
\[
 (\rho-\rho')\log2=2\pi i a,\qquad
 (\rho-\rho')\log3=2\pi i b
\]
for integers \(a,b\). If \(\rho-\rho'\ne0\), both \(a,b\) are nonzero and \(\log2/\log3=a/b\). Exponentiation would give \(2^b=3^a\), impossible by unique prime factorization, including after moving negative exponents to the other side. Therefore \(\rho=\rho'\). Conversely equal \((\rho,m)\) have the identity intertwiner. Thus the full tuple distinguishes the parameter; it does not force its real part.

## MT5. The exact cochain complex and connecting map

Let \(V\) be any finite-dimensional coefficient space with invertible positive return \(H_p\). At finite level, put \(C=\operatorname{Map}(H,V)\). Positive parallel transport pushes section data forward by
\[
 (Rc)(u)=H_p\,c(\bar p u).
\tag{MT5.1}
\]
To verify the argument \(\bar p u\), a value initially at \(\bar p u\) arrives at \(u\) after positive time \(L\), and its fiber value is multiplied by \(H_p\), by (MT3.4).

The local-system cohomology is computed by the two-term complex
\[
 C\xrightarrow{\,R-I\,}C
\tag{MT5.2}
\]
in degrees \(0,1\), with no higher cohomology. One can prove this directly on each circle: subdivide it at its \(d\) vertices, use the edge flat trivializations, and write a coboundary as transported starting value minus ending value. All edge transports and orientations are invertible, and this cellular differential is (MT5.2) after the indicated identification of edge fibers with their ending fibers. Eliminating \(d-1\) successive vertices leaves the one-vertex differential \(H_p^d-I\). Its kernel is the set of global flat sections, and its cokernel is first cohomology.

Equivalently, in the \(\chi\)-sector,
\[
 C_\chi^\bullet(V):
 \quad V\xrightarrow{\,B_{\chi,V}\,}V,\qquad
 B_{\chi,V}=\chi(\bar p)H_p-I.
\tag{MT5.3}
\]
This sign agrees with the invariant-section boundary condition (MT3.7): a constant horizontal coefficient is possible exactly when \(\chi(\bar p)H_p v=v\).

Now take an exact sequence of such coefficient systems
\[
 0\longrightarrow V_A\xrightarrow{\iota}V_B
       \xrightarrow{\pi}V_C\longrightarrow0
\tag{MT5.4}
\]
whose maps commute with the specified \(H_p\). For \(c\in\ker B_{\chi,V_C}\), choose \(b\in V_B\) with \(\pi b=c\). Since
\[
 \pi B_{\chi,V_B}b
    =B_{\chi,V_C}c=0,
\]
there is a unique \(a\in V_A\) satisfying
\[
 \iota a=B_{\chi,V_B}b.
\]
The connecting homomorphism is
\[
 \boxed{\delta_\chi(c)=[a]\in
       V_A/B_{\chi,V_A}V_A.}
\tag{MT5.5}
\]
Replacing \(b\) by \(b+\iota a_0\) replaces \(a\) by
\(a+B_{\chi,V_A}a_0\), so the class is independent of the lift. Linearity follows by choosing lifts of a sum and of a scalar multiple. Finally,
\[
 \delta_\chi(c)=0
 \iff c\ \text{has a lift in }\ker B_{\chi,V_B}.
\tag{MT5.6}
\]
For the forward implication, write \(a=B_{\chi,V_A}a_0\); then \(b-\iota a_0\) is an invariant lift. The reverse implication uses the invariant lift itself, for which \(a=0\).

This gives the complete relevant portion of the long exact sequence:
\[
 \ker B_A\longrightarrow\ker B_B\longrightarrow\ker B_C
 \xrightarrow{\delta_\chi}
 \operatorname{coker}B_A\longrightarrow
 \operatorname{coker}B_B\longrightarrow
 \operatorname{coker}B_C\longrightarrow0.
\tag{MT5.7}
\]
Exactness at each term follows by the same lift calculation: a cokernel class becomes zero in the next term precisely when its representative can be adjusted by a differential to lie in the preceding subspace.

Suppose specified coefficient maps \(F_A,F_B,F_C\) commute with their \(H_p\) and with \(\iota,\pi\). They induce maps on every kernel and cokernel. Then
\[
 \delta_\chi F_C=F_A\delta_\chi.
\tag{MT5.8}
\]
Indeed \(F_Bb\) lifts \(F_Cc\), and
\[
 B_BF_Bb=F_BB_Bb=F_B\iota a=\iota F_Aa.
\]
For the actual prime jets, one can take \(F=H_q\) for every prime \(q\), since the exponentials in \(T\) commute.

## MT6. Exact spectral separation and the actual jet obstruction

Here is the finite-dimensional algebra used by the Deligne mechanism. Let \(S:U\to W\) satisfy \(SF_U=F_WS\), where \(F_U,F_W\) are invertible endomorphisms of finite-dimensional complex spaces. If their spectra are disjoint, then \(S=0\). To prove this without semisimplicity, let \(P\) and \(Q\) be their minimal polynomials. They have no common root, so there are polynomials \(a,b\) with \(aP+bQ=1\). For \(u\in U\),
\[
 Su=S\bigl(a(F_U)P(F_U)+b(F_U)Q(F_U)\bigr)u
    =b(F_W)Q(F_W)Su=0.
\tag{MT6.1}
\]
If, for a fixed real \(q>1\), all eigenvalues on \(U\) have modulus at most \(q^{i/2}\), and all on \(W\) have modulus at least \(q^{(i+1)/2}\), the spectra are disjoint and this argument applies. This last observation is an exact algebraic consequence of the displayed modulus separation; it supplies neither modulus bound for a new geometric object.

Apply the calculation now to the **actual retained jet** (MT3.1). Put
\[
 z=\chi(\bar p)p^\rho,\qquad
 B_\chi=z\,e^{LT}-I.
\tag{MT6.2}
\]
If \(z\ne1\), its complete inverse is
\[
 \boxed{
 B_\chi^{-1}=
 \sum_{j=0}^{m-1}
 \frac{(-1)^j z^j(e^{LT}-I)^j}{(z-1)^{j+1}}.
 }
\tag{MT6.3}
\]
Indeed \(e^{LT}-I\) is a multiple of \(T\), so its \(m\)-th power is zero; multiplying the finite geometric series by
\((z-1)I+z(e^{LT}-I)\) leaves \(I\). This inverse commutes with every \(H_q\). It is a contracting homotopy from degree \(1\) to degree \(0\) for (MT5.3).

For a nontrivial zero \(\rho\) of the original zeta function,
\[
 0<\Re\rho<1,\qquad |z|=p^{\Re\rho}>1.
\tag{MT6.4}
\]
Therefore \(z\ne1\), and
\[
 H^0(C_\chi^\bullet(A_{\rho,m}))
  =H^1(C_\chi^\bullet(A_{\rho,m}))=0
\tag{MT6.5}
\]
for every finite quotient and every character. This applies to zeros on and off the critical line alike. The proof has used the known open critical strip, not RH.

Consequently this particular torus receiver has no nonzero invariant class of an actual zero jet to lift. Its vanishing obstruction is the explicitly calculated acyclicity (MT6.3), **not** Deligne's nonvacuous weight separation. It cannot distinguish the critical line from the rest of the open strip.

The resonant case calculates what the jet extension itself contributes when an invariant class is present. Retain \(m=2\) and \(z=1\). There is an exact sequence, equivariant for every \(H_q\),
\[
 0\longrightarrow\mathbb C\,T
 \longrightarrow\mathbb C[T]/T^2
 \longrightarrow\mathbb C\longrightarrow0.
\tag{MT6.6}
\]
The differential on the middle space is
\[
 B_\chi=e^{LT}-I=LT;
\tag{MT6.7}
\]
on the subspace and quotient it is zero. The quotient class \(1\) has lift \(1\) in the middle space, so (MT5.5) gives
\[
 \boxed{\delta_\chi(1)=L[T]\ne0.}
\tag{MT6.8}
\]
The bracket denotes its class in the cokernel, which here is the entire line \(\mathbb C\,T\), because that line's differential is zero. Since \(L=\log p>0\), the class does not vanish. Every lift of \(1\) has the form \(1+aT\), and applying \(B_\chi\) gives \(LT\); thus no invariant lift exists.

The full prime action on the source of \(\delta_\chi\) and on its target is respectively
\[
 H_q\big|_{\mathbb C}=q^\rho I,\qquad
 H_q\big|_{\mathbb C T}=q^\rho I.
\tag{MT6.9}
\]
They have exactly the same eigenvalue, not separated weights. Their real growth index
\[
 \frac{2\log|q^\rho|}{\log q}=2\Re\rho
\tag{MT6.10}
\]
is equal on both sides. This index is a statement about these complex coefficient operators; it is not a claim that they are algebraic Weil numbers. Equation (MT6.8) proves that retaining the nilpotent extension matters, even though its strictly triangular part is invisible in (MT3.9).

The same calculation works at every retained jet length \(m\ge2\). Use
\[
 0\longrightarrow\mathbb C T^{m-1}
 \longrightarrow A_{\rho,m}
 \longrightarrow A_{\rho,m-1}\longrightarrow0.
\tag{MT6.11}
\]
At resonance,
\[
 e^{LT}-I=T\,U(T),\qquad
 U(T)=\sum_{j=1}^{m-1}\frac{L^j}{j!}T^{j-1},
\tag{MT6.12}
\]
where \(U(0)=L\ne0\), so \(U(T)\) is invertible in the truncated polynomial algebra. In \(A_{\rho,m-1}\), the kernel of this differential is exactly the line generated by \(T^{m-2}\). Lifting that generator to \(A_{\rho,m}\) gives
\[
 \boxed{\delta_\chi(T^{m-2})=L[T^{m-1}]\ne0.}
\tag{MT6.13}
\]
Indeed the degree-one term of the exponential produces \(LT^{m-1}\), and every term of higher degree produces a multiple of \(T^m=0\). Both lines have prime action \(H_q=q^\rho I\). Thus every stage of the retained jet tower has the same-eigenvalue obstruction at resonance, with the exact coefficient \(\log p\).

One concrete resonant instance is \(\rho=0\), \(\chi=1\), at every prime. It is an example internal to the defined coefficient functor, not an asserted nontrivial zeta zero, not a counterexample to RH, and not a proposed replacement of the programme's arithmetic. It demonstrates the exact same-weight lifting obstruction.

## MT7. The precise comparison with Deligne §3.6

Deligne's setting is a proper morphism \(f:X\to S\), with \(S\) the spectrum of a henselian local ring of a smooth curve, total space essentially smooth, and smooth geometric generic fiber. After reduction to a finite-field situation, the exact cross in [DII, §3.6, equation (8)] has middle and right terms
\[
 E=H^i(X_\eta),\qquad
 C=H^i(X_{\bar\eta})^I,
\]
and support target
\[
 O=H^{2N-i-1}(X_s)^\vee(-N).
\tag{MT7.1}
\]
Its horizontal row is
\[
 0\longrightarrow H^{i-1}(X_{\bar\eta})_I(-1)
 \longrightarrow E\longrightarrow C\longrightarrow0.
\tag{MT7.2}
\]
Its vertical maps have the form
\[
 H^i(X_s)\longrightarrow E\xrightarrow{b}O,
 \qquad
 \operatorname{im}(H^i(X_s)\to E)=\ker b.
\tag{MT7.3}
\]
The Tate twists \((-1)\) and \((-N)\), and the index \(2N-i-1\), are part of these maps.

The two weight calculations in Lemmas 3.6.2–3.6.3 are
\[
 \operatorname{weights}(C)\le i,\qquad
 \operatorname{weights}(O)\ge i+1.
\tag{MT7.4}
\]
Since the weight functor \(W_i\) is exact on the objects in question, (MT7.2) gives a surjection \(W_iE\to C\). The map \(b\) kills \(W_iE\) by (MT7.4), so
\[
 W_iE\subseteq\ker b
   =\operatorname{im}(H^i(X_s)\to E).
\tag{MT7.5}
\]
Every class of \(C\) therefore has a lift in \(W_iE\), and that lift has a preimage in \(H^i(X_s)\). This is the surjectivity of specialization in Theorem 3.6.1.

The elementary part of this mechanism is exactly the intertwining calculation (MT6.1), together with an exact source of bounded-weight lifts. One must retain both parts: a putative direct map from \(C\) to \(O\) is not by itself Deligne's entire cross. In particular the choice of a lift in \(E\), its possible change by the left term of (MT7.2), and the subsequent support obstruction are all present.

For the concrete mapping-torus receiver, the corresponding exact sequence is (MT5.7), and its genuine lifting obstruction is (MT5.5). The actual calculation yields:

1. For the original nontrivial zeta jets, the complex is equivariantly contractible by (MT6.3). This receiver has no invariant class available for the desired specialization argument.
2. When a jet class is resonant and does exist, the explicitly retained length-two extension has the nonzero obstruction (MT6.8), while source and obstruction have identical prime eigenvalues (MT6.9).
3. The circle cochain differential (MT5.3) carries no built-in \((-1)\) Tate twist. The occurrence of \((-1)\) in Deligne's inertia cohomology in [DII, §3.6, equations (4)–(5)] cannot be inferred from a topological circle's degree alone. In this calculated receiver the additional prime maps act on coefficients and do not rescale the circle generator.

Thus this computation provides exact connecting maps and an exact obstruction object. It does not supply the two distinct geometric weight bounds in (MT7.4), nor a comparison identifying the torus cohomology with Deligne's support group. The unchanged source \(Z_1/\tau\) does not create such a Tate factor by relabeling a vector-space zero.

## MT8. What is preserved for the global receiving calculation

The following data are ready to be used without a new interpretation of the source:

- The source-oriented prime torus, its full finite-quotient characters, periods, and Haar volume: (MT0.1)–(MT2.3).
- A flat bundle with the entire actual prime jet as positive return holonomy, and the inverse gluing required by that orientation: (MT3.1)–(MT3.8).
- Exact finite-level flat-isomorphism and flat-metric conditions, with the connection term retained under smooth trivialization: (MT4.1)–(MT4.6).
- The genuine lifting obstruction, its prime-equivariance, and the exact vanishing criterion through invariant lifts: (MT5.5)–(MT5.8).
- An explicit contracting homotopy for every actual open-strip zero jet in this receiver, and an explicit nonzero same-eigenvalue obstruction at resonance: (MT6.3)–(MT6.10).
- The exact logical position of the comparison within Deligne's cross: (MT7.1)–(MT7.5).

These statements neither discard the nilpotent jet nor identify a scalar circle trace with the full adelic trace. They also do not imply a classification of global adelic support cohomology. The nontrivial global continuation is to use the actual programme support sequence and its connecting map, rather than replacing it by the acyclic finite-torus complex calculated here.
