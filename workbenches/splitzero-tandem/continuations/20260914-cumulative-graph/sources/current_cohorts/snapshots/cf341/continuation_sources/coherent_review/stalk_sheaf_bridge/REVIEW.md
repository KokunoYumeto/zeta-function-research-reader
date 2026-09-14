# Exact local Ext and point-supported sheaf bridge

This independent audit concerns all algebraic modules over the analytic local ring and all sheaves of modules over the analytic structure sheaf. No coherence or finite-presentation hypothesis is inserted. The original nonzero germ g is retained without replacing it by a power of a local coordinate.

## 1. Original local ring and exact telescope

Fix the original complex coordinate t and a point s. Put z=t-s, retaining the inverse t=s+z. Let

\[
R=\mathcal O_{\mathbb C,s}=\mathbb C\{z\},\quad
\Omega=\Omega^1_{\mathbb C,s}=R\,dt,\quad
F=\operatorname{Frac}(R)=R[z^{-1}],\quad
\widehat\Omega=\mathbb C[[z]]\,dt.
\]

The equality F=R[z^{-1}] follows because every nonzero germ has a finite vanishing order and a remaining convergent unit. It changes no original germ or multiplicity.

Let P_0 and P_1 be countable free R-modules with bases e_n and f_n, n>=0. Define

\[
d(f_n)=e_n-z e_{n+1},\qquad
\epsilon(e_n)=z^{-n}.
\]

Then

\[
0\longrightarrow P_1\xrightarrow{d}P_0\xrightarrow{\epsilon}F\longrightarrow0
\tag{S1}
\]

is exact. Surjectivity follows from F=R[z^{-1}]. For injectivity of d, a finite sum with final nonzero coefficient a_N has coefficient -z a_N on e_{N+1}; this cannot vanish in the domain R. Finally, modulo the d(f_n), any finite sum sum_{n=0}^N a_n e_n equals (sum_{n=0}^N a_n z^{N-n})e_N. If its epsilon image is zero, this parenthesized coefficient is zero because R is a domain. Thus ker epsilon=im d.

Applying Hom_R(-,Omega) gives the exact two-term complex

\[
\prod_{n\ge0}\Omega\xrightarrow{D}\prod_{n\ge0}\Omega,
\qquad (Da)_n=a_n-z a_{n+1}.
\tag{S2}
\]

If Da=0, then a_0=z^n a_n for every n. A nonzero convergent germ has finite vanishing order, so intersection_{n>=0} z^n Omega=0; hence a_0=0 and all a_n=0. Therefore

\[
\operatorname{Hom}_R(F,\Omega)=0.
\tag{S3}
\]

Define the R-linear map

\[
S:\prod_{n\ge0}\Omega\longrightarrow\widehat\Omega,
\qquad S(b)=\sum_{n\ge0}z^n b_n.
\]

The series is well-defined in the z-adic completion, because each coefficient receives only finitely many contributions. Its value on Da is a_0 by telescoping: the Nth partial sum is a_0-z^{N+1}a_{N+1}, and the last term tends to zero z-adically. Therefore S descends to coker D -> Omegahat/Omega.

This induced map is surjective: for any formal differential sum c_n z^n dt, take b_n=c_n dt. For injectivity, suppose S(b)=a_0 is convergent. Define

\[
a_n=z^{-n}\left(a_0-\sum_{j=0}^{n-1}z^j b_j\right),\qquad n\ge1.
\]

The numerator is a convergent germ whose first n Taylor coefficients vanish, so division by z^n stays in Omega. Direct subtraction gives a_n-z a_{n+1}=b_n, including n=0. Thus b is in im D. Consequently

\[
\boxed{\operatorname{Ext}^1_R(F,\Omega)\simeq\widehat\Omega/\Omega,
\quad \operatorname{Hom}_R(F,\Omega)=0,
\quad \operatorname{Ext}^{j}_R(F,\Omega)=0\ (j\ge2).}
\tag{S4}
\]

All three assertions follow from the explicit free resolution (S1).

The quotient Omegahat/Omega is naturally an F-vector space. Multiplication by z is injective because zH convergent implies H convergent; it is surjective because H is congruent modulo Omega to H-H(0), which is divisible by z. Every convergent unit is invertible on the quotient. This agrees with the F-action on Ext induced by precomposition with multiplication on F. For z in particular, multiplication on the source lifts to z times the identity on (S1); applying Hom therefore acts by z on every b_n and on its formal sum. Inverses and all fractions follow uniquely.

## 2. An explicit nonsplit extension

Take b_n=n! dt for n>=0 and write

\[
H=\sum_{n\ge0}n!z^n\,dt\in\widehat\Omega.
\]

This is not convergent on any neighborhood of zero: for any r>0, consecutive absolute terms have ratio (n+1)r, eventually at least two. Thus [H] is nonzero in Omegahat/Omega.

Let b:P_1->Omega send f_n to b_n and define

\[
E_b=(\Omega\oplus P_0)/\{(-b(v),d(v)):v\in P_1\}.
\tag{S5}
\]

The injection iota:Omega->E_b sends omega to [(omega,0)]. It is injective because d is injective. The map pi:E_b->F is pi([(omega,p)])=epsilon(p). It is well-defined and surjective. If epsilon(p)=0, write p=d(v); then [(omega,p)]=[(omega+b(v),0)], proving ker pi=im iota. Thus

\[
0\longrightarrow\Omega\xrightarrow{\iota}E_b\xrightarrow{\pi}F\longrightarrow0
\tag{S6}
\]

is exact. In E_b the generators obey the exact signed relations
\(e_n-z e_{n+1}=\iota(b_n)\).

If (S6) split, a section would give lifts t_n of z^{-n} with t_n-z t_{n+1}=0. Each lift can be written t_n=e_n-iota(a_n), and the relation becomes Da=b. Applying S gives H=a_0 in Omega, contradicting divergence. Conversely any a with Da=b gives such a compatible section, so the displayed obstruction is exactly the splitting obstruction, with no missing implication.

## 3. The original stalk M_s=N_s plus K_s

Retain the stipulated original direct-sum identification

\[
M_s=N_s\oplus K_s,\qquad N_s=R/(g),
\]

where g is the original nonzero analytic germ and K_s is the given nonzero F-vector space. The resolution 0->R --g--> R ->R/(g)->0 gives Hom_R(N_s,Omega)=0, Ext^1_R(N_s,Omega)=Omega/gOmega, and higher Ext zero.

There is a canonical F-linear identification

\[
\operatorname{Ext}^1_R(K_s,\Omega)
\simeq\operatorname{Hom}_F(K_s,\widehat\Omega/\Omega).
\tag{S7}
\]

Indeed for an injective resolution I^bullet of Omega, the termwise adjunction is

\[
\operatorname{Hom}_R(K_s,I^j)
\simeq\operatorname{Hom}_F\bigl(K_s,\operatorname{Hom}_R(F,I^j)\bigr),
\]

sending h to the map k |-> (f |-> h(fk)), with inverse evaluation at f=1. Since every F-vector space is free, Hom_F(K_s,-) is exact, so it commutes with cohomology. Combining with (S4) proves (S7), Hom_R(K_s,Omega)=0, and all higher Ext zero. Equivalently, after choosing an F-basis B, the Ext group is the product over B of Omegahat/Omega.

For the specified direct-sum identification one therefore has

\[
\boxed{\operatorname{Hom}_R(M_s,\Omega)=0,\qquad
\operatorname{Ext}^1_R(M_s,\Omega)
\simeq\Omega/g\Omega\oplus
\operatorname{Hom}_F(K_s,\widehat\Omega/\Omega),\qquad
\operatorname{Ext}^j_R(M_s,\Omega)=0\quad(j\ge2).}
\tag{S8}
\]

The second summand is nonzero. Explicitly, choose 0!=v in K_s, extend v to an F-basis, and let lambda:K_s->F be its coefficient functional, so lambda(v)=1. Define p:M_s->F to be zero on N_s and lambda on K_s. Pull (S6) back along p. Its pullback along the section F->M_s, f |-> (0,fv), recovers (S6). Hence the extension of M_s by Omega obtained in this way is nonsplit. The choice constructs an extension; it does not alter M_s or g.

## 4. Exact sheaf adjunction with the full germ action

Let X=C and let i_s:({s},R)->(X,O_X) be the morphism of ringed spaces induced by the identity on the stalk R. For any R-module A, the direct image is the sheaf

\[
(i_{s*}A)(U)=\begin{cases}A,&s\in U,\\0,&s\notin U,\end{cases}
\]

where O_X(U) acts through its germ map O_X(U)->R. This is the skyscraper with the entire local-ring action, not a module on which the maximal ideal is stipulated to act by zero.

The stalk functor F |-> F_s is exact: it is the filtered colimit of sections over neighborhoods, and filtered colimits of modules are exact. The functor i_{s*} is exact by its displayed section formula. For every O_X-module Fcal, the adjunction

\[
\operatorname{Hom}_{O_X}(\mathcal F,i_{s*}A)
\simeq\operatorname{Hom}_R(\mathcal F_s,A)
\tag{S9}
\]

is explicit. A sheaf morphism gives its stalk map. Conversely, an R-linear map u:Fcal_s->A acts on a section f over a neighborhood U of s by u(f_s), and acts by zero when s is absent. These operations are inverse and compatible with restrictions and the full germ action.

Since i_{s*} is right adjoint to the exact stalk functor, it takes injective R-modules to injective O_X-modules: extension of an R-linear map across the induced stalk inclusion gives extension of the adjoint sheaf map across any sheaf monomorphism. If A->I^bullet is an injective resolution, exactness of i_{s*} therefore makes i_{s*}I^bullet an injective resolution of i_{s*}A. Applying (S9) term by term proves the canonical derived adjunction

\[
\boxed{R\operatorname{Hom}_{O_X}(\mathcal M,i_{s*}A)
\simeq R\operatorname{Hom}_R(\mathcal M_s,A).}
\tag{S10}
\]

This formula uses global derived Hom complexes; it requires no coherence, finite generation, or finite presentation of Mcal.

There is also an exact internal version. Over every open U containing s, the adjunction in (S9) uses the same stalk, while over an open U not containing s the target is zero. Therefore termwise internal Hom has the sheaf identity

\[
\mathcal Hom_{O_X}(\mathcal M,i_{s*}I^j)
\simeq i_{s*}\operatorname{Hom}_R(\mathcal M_s,I^j).
\]

The direct image injectives just constructed compute internal derived Hom as well; restriction to an open set preserves injectivity because its left adjoint, extension by zero, is exact on stalks. Thus

\[
\boxed{R\mathcal Hom_{O_X}(\mathcal M,i_{s*}A)
\simeq i_{s*}R\operatorname{Hom}_R(\mathcal M_s,A),\qquad
\mathcal Ext^j_{O_X}(\mathcal M,i_{s*}A)
\simeq i_{s*}\operatorname{Ext}^j_R(\mathcal M_s,A).}
\tag{S11}
\]

In particular A=Omega makes (S8) an exact sheaf statement for this specified point-supported target.

## 5. Explicit nonsplit sheaf extension and the comparison to the original target

Let 0->Omega->E->M_s->0 be the nonsplit module extension constructed in Section 3. Applying exact i_{s*} gives an extension of i_{s*}M_s by i_{s*}Omega. The adjunction unit is the explicit germ map
\(\eta:\mathcal M\to i_{s*}\mathcal M_s\).
Define the sheaf pullback

\[
\mathcal E=\mathcal M\times_{i_{s*}M_s}i_{s*}E.
\]

Then

\[
0\longrightarrow i_{s*}\Omega\longrightarrow\mathcal E
\longrightarrow\mathcal M\longrightarrow0
\tag{S12}
\]

is exact, by the pullback of the displayed epimorphism. At s this is the original module extension because (i_{s*}E)_s=E and eta_s is the identity. Any sheaf splitting would induce a stalk splitting. Consequently (S12) is explicitly nonsplit and realizes the calculated nonzero class on the original sheaf Mcal with a fully specified point-supported target.

There is also a canonical map from the original holomorphic differential target: sending a differential on U to its germ at s, or to zero when s is absent, defines
\(\Omega_X^1\to i_{s*}\Omega\).
It induces the actual derived comparison

\[
R\mathcal Hom_{O_X}(\mathcal M,\Omega_X^1)
\longrightarrow
R\mathcal Hom_{O_X}(\mathcal M,i_{s*}\Omega)
\simeq i_{s*}R\operatorname{Hom}_R(M_s,\Omega).
\tag{S13}
\]

Likewise there is its global derived Hom version. This morphism is the proved bridge from the original differential target to the calculated point-supported target. No assertion that it is an isomorphism, or that its map on Ext classes is surjective, follows from the telescope computation.

In particular, this audit makes no general identification of
\((\mathcal Ext^j_{O_X}(\mathcal M,\Omega_X^1))_s\)
with
\(\operatorname{Ext}^j_R(M_s,\Omega)\).
Finite-presentation hypotheses that can justify stalk formulas are absent for the present source. Equations (S10)-(S13), together with the explicit nonsplit extension (S12), are the exact sheaf conclusions proved here.
