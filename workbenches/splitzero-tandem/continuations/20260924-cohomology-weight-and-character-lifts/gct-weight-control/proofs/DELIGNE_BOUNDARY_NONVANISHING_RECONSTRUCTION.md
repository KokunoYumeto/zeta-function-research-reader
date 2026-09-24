# Deligne's boundary nonvanishing argument and its exact original-zeta specialization

24 September 2026. Bounded reconstruction of *La conjecture de Weil. II*, §§2.1–2.2, printed pp. 187–196. This is a mathematical derivation from the current French transcription, not original author LaTeX and not a new edition of Deligne's text. No PDF was opened.

## DB0. Source identity, scope, and corrected witness formulas

The read source is `output/Deligne_Weil_II_S20_LaTeX/typed_latex/S20_FR_record_export.tex`, lines 1553–1928, read in full. It is the current S20 editable French page-record export. Its SHA-256 is `d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351`. Human mathematical source: Pierre Deligne, *La conjecture de Weil. II*, Publications mathématiques de l'IHÉS 52 (1980), pp. 137–252, §§2.1–2.2. The routed canonical source IDs are `PUBUNIT-3D90B487DBD1CC3A259C6455` and `PUBUNIT-574B0214207BBB2BDABCFFF9`. This file reports the mathematical content reconstructed from that transcription and identifies corrections forced by its definitions. It does not attribute transcription errors to Deligne's original printing.

Three formulas require explicit control:

1. With \(\omega_s(g)=q^{-s\deg g}\), its period in \(s\) is \(2\pi i/\log q\), not \(2\pi i\log q\).
2. A representation of real part \(b\), with this character convention, has associated sheaf weight \(-2b\), not \(+2b\). The derivation below retains the sign through the original weight \(\beta\).
3. The concentration proof of §2.1.7 needs its outside-neighborhood contribution. The guaranteed lower bound is \([(1-e_1)(1-e_2)-e_2]\dim(\tau)M\); choosing \(e_1+2e_2<e\) gives the stated lemma.

The original-zeta specialization begins only after the whole arithmetic and its prime spectrum have been recovered. It uses all primes and all positive prime powers, and does not pool counters of distinct branches. No arithmetic on τ is introduced. A boundary result is proved on its actual domain; no new RH conclusion is drawn.

## DB1. The representation family and its sign convention (§2.1.1)

Let

\[
 1\longrightarrow K\longrightarrow G\longrightarrow\Gamma\longrightarrow0
 \tag{DB1.1}
\]

be an extension of a group \(\Gamma\) isomorphic to \(\mathbb Z\) or \(\mathbb R\) by a compact group \(K\). All finite-dimensional representations are continuous complex representations. The assumed structure is a direct-product extension for \(\Gamma\simeq\mathbb R\), and, for \(\Gamma\simeq\mathbb Z\), a central element whose nonzero degree generates a subgroup of finite index. Fix a nontrivial positive real character \(\omega_1\) of \(\Gamma\) and put \(\omega_s=\exp(s\log\omega_1)\). For indexed conjugacy classes \(x_v\), let

\[
 N_v=\omega_{-1}(x_v)>1.
 \tag{DB1.2}
\]

The discrete convention is the unique choice of \(q>1\) and degree isomorphism with

\[
 \omega_s(g)=\exp(-s\deg(g)\log q),\quad
 N_v=q^{\deg v},\quad
 \omega_{s+2\pi i/\log q}=\omega_s.
 \tag{DB1.3}
\]

Let \(z\) be central with nonzero image in \(\Gamma\). The quotient \(G/\langle z\rangle\) is compact. A representation on which \(z\) is unitary has an invariant positive Hermitian form: first choose a \(z\)-invariant form and then average its translates over this compact quotient. The averaged form is well defined because the initial form is invariant under \(z\). Conversely a unitary representation has a unitary \(z\)-action.

For an irreducible representation \(\tau\), Schur's lemma makes \(\tau(z)\) scalar. There is a unique real number \(b\) with \(|\tau(z)|=\omega_b(z)\); then \(\tau\omega_{-b}\) is unitarizable by the preceding averaging. Define \(\operatorname{Re}(\tau)=b\). In particular

\[
 \operatorname{Re}(\tau\omega_s)=b+\operatorname{Re}s,
 \qquad
 |\lambda(\tau(x_v))|=N_v^{-b}
 \tag{DB1.4}
\]

for each eigenvalue after the unitary twist. The last equality retains the negative exponent fixed by \(\omega_1\).

The twisting orbits \(\{\tau\omega_s:s\in\mathbb C\}\) form the components of the source's representation Riemann surface \(\widetilde G\). In the discrete case any twisting stabilizer is discrete: if \(d=\dim\tau\) and \(\tau\omega_s\simeq\tau\), determinants give \(\omega_{ds}=1\), hence \(s\in(2\pi i/(d\log q))\mathbb Z\). In the real case the same determinant identity forces \(s=0\). Thus the components are complex lines or their indicated discrete imaginary quotients. The locus of unitary irreducibles is denoted \(\widehat G\).

The source's continuous example §2.1.2 keeps an arbitrary compact factor \(K\), with each class written \((x_v^0,x_v^\Gamma)\); its positive norm is still exactly \(N_v=\omega_{-1}(x_v^\Gamma)\). Its curve example §2.1.3 takes the Weil extension of the geometric fundamental group, all closed points as \(\Sigma\), and their geometric Frobenius classes, so \(N_v=q^{\deg v}\). The full Weil extension need not satisfy the central-degree condition. The source explicitly notes this limitation. The positivity and residue proofs DB2–DB6 use the unitary representations and their twists, so do not themselves use that central-degree condition; the discrete translated-measure assertion DB8 does use a central element. The algebraic compact monodromy construction in the curve argument below supplies it on its stated receiver. No central element in an arbitrary full Weil group is inferred.

## DB2. Euler products and the entire prime-power measure (§§2.1.1–2.1.4)

Assume the source's convergence condition

\[
 \prod_v(1-N_v^{-s})^{-1}
 \quad\hbox{converges absolutely for }\operatorname{Re}s>1.
 \tag{DB2.1}
\]

In the discrete case this is equivalent to the source's bound on the entire degree counts \(A_n=\#\{v:\deg v=n\}\): for every \(\epsilon>0\), there is a finite \(C_\epsilon\) with \(A_n\leq C_\epsilon q^{(1+\epsilon)n}\). Indeed, the logarithm of the Euler product converges exactly when \(\sum_n A_nq^{-\sigma n}\) does, since \(q^{-\sigma n}\leq q^{-\sigma}<1\) and \(x\leq-\log(1-x)\leq x/(1-q^{-\sigma})\). Convergence at \(\sigma=1+\epsilon\) bounds each term by the full sum. Conversely the count bound with \(0<\epsilon<\sigma-1\) dominates the sum by a convergent geometric series. Every local degree and its multiplicity remain in \(A_n\).

For an irreducible \(\tau\) with \(\operatorname{Re}\tau>1\), define

\[
 L(\tau)=\prod_v\det(1-\tau(x_v))^{-1},\qquad
 L(\tau,s)=L(\tau\omega_s).
 \tag{DB2.2}
\]

Each local eigenvalue has modulus \(N_v^{-\operatorname{Re}\tau}<1\). The identity \(-\log\det(1-M)=\sum_{n\geq1}\operatorname{Tr}(M^n)/n\), proved by summing \(-\log(1-\lambda)\) over eigenvalues, and the bound \(|\operatorname{Tr}\tau(x_v^n)|\leq(\dim\tau)N_v^{-n\operatorname{Re}\tau}\) give locally uniform convergence of the logarithm. Thus \(L\) is holomorphic and nonzero in the asserted open half-plane. The same construction extends multiplicatively to direct sums and by quotients to virtual representations.

For a unitary virtual representation \(\rho\), its character is a finite integral linear combination of characters of unitary representations. It is bounded. Differentiation gives the full formula

\[
 \Lambda_\sigma(\rho):=-\frac{L'}{L}(\omega_\sigma\rho)
  =\sum_{v}\sum_{n=1}^{\infty}
       (\log N_v)N_v^{-n\sigma}\chi_\rho(x_v^n),\qquad\sigma>1.
 \tag{DB2.3}
\]

There is no omitted prime-power term and no factor \(1/n\) remaining: differentiating \(N_v^{-ns}/n\) supplies \(-\log N_v\). To justify derivative convergence, choose \(1<\sigma_0<\sigma\). The inequality
\((\log N_v)e^{-n(\sigma-\sigma_0)\log N_v}\leq C/n\)
reduces the absolute derivative sum to the convergent logarithm in (DB2.1) at \(\sigma_0\). The same argument works locally uniformly.

Define the positive finite measure on conjugacy classes

\[
 \mu_\sigma=
 \sum_v\sum_{n=1}^{\infty}
      (\log N_v)N_v^{-n\sigma}\delta_{[x_v^n]}.
 \tag{DB2.4}
\]

Its total mass is the convergent scalar sum obtained above. Equation (DB2.3) is exactly

\[
 \Lambda_\sigma(\rho)=\int\chi_\rho\,d\mu_\sigma.
 \tag{DB2.5}
\]

For every unitary virtual \(\rho\), the conjugate representation has character \(\overline{\chi_\rho}\), so

\[
 \Lambda_\sigma(\rho\otimes\overline\rho)
       =\int|\chi_\rho(g)|^2\,d\mu_\sigma(g)\geq0.
 \tag{DB2.6}
\]

The representation may be virtual: its character is still a function, and its product with its complex conjugate is still the displayed nonnegative square. More generally any virtual character which is real and pointwise nonnegative has nonnegative integral. These are different statements from requiring every virtual representation to have a nonnegative character.

## DB3. Boundary residues (§§2.1.4–2.1.5)

The analytic input of Deligne's theorem is: \(L\) is meromorphic on a neighborhood of \(\operatorname{Re}\tau\geq1\), is holomorphic there except for a simple pole at \(\omega_1\), and has no other poles in that region. Zeros on the boundary have not been excluded as an input.

For \(\tau\in\widehat G\), define the integer

\[
 \nu(\tau)=\operatorname{ord}_{\text{pole},\,s=1}L(\tau\omega_s).
 \tag{DB3.1}
\]

A zero of multiplicity \(m\) has \(\nu=-m\). Writing
\(L(\tau\omega_s)=(s-1)^{-\nu(\tau)}u(s)\)
with \(u\) holomorphic and nonzero proves

\[
 -\frac{L'}L(\tau\omega_s)
  =\frac{\nu(\tau)}{s-1}-\frac{u'(s)}{u(s)},\qquad
 \nu(\tau)=\lim_{\sigma\downarrow1}(\sigma-1)\Lambda_\sigma(\tau).
 \tag{DB3.2}
\]

The analytic hypotheses give \(\nu(1)=1\) and \(\nu(\tau)\leq0\) for \(\tau\ne1\). Conjugation of the convergent product gives
\(\overline{L(\tau\omega_s)}=L(\overline\tau\omega_{\overline s})\);
meromorphic continuation then yields \(\nu(\overline\tau)=\nu(\tau)\). Extending \(\nu\) additively to virtual representations and taking the limit in the finite sum of (DB2.6) gives

\[
 \nu(\rho\otimes\overline\rho)\geq0
 \tag{DB3.3}
\]

for every unitary virtual \(\rho\), and hence for every genuine unitary \(\rho\). The limit multiplies by the positive number \(\sigma-1\); no sign is reversed.

## DB4. Reduction to a compact group (§§2.1.5–2.1.6)

Map \(G\) into the product of the unitary groups \(U(V_\tau)\) of its finite-dimensional unitary representations, and let \(K_B\) be the closure of its image. Each unitary-group factor is compact, so \(K_B\) is compact. An individual representation image need not itself be closed, which is why the ambient unitary groups and the closure are specified. Every unitary representation of \(G\) extends through its coordinate projection to \(K_B\). Conversely restriction of a continuous representation of \(K_B\) to the dense image of \(G\) preserves invariant subspaces and intertwiners: the relevant equations are closed conditions, so equations on a dense subset hold on the closure. It therefore preserves irreducibility and all multiplicities. Every irreducible representation of \(K_B\) restricts to a finite-dimensional unitary representation of \(G\), and uniqueness of extension follows from density. Thus the finite-dimensional unitary representation categories, their conjugation, and their tensor products agree for the purpose of (DB3.3). This comparison is not an assertion about nonunitarizable representations of \(G\).

The remaining proof may consequently be made on a compact group \(K_B\), denoted \(K_c\) below. Haar measure \(dg\) has total mass one. For characters, use the explicit convention

\[
 [\eta:\tau]=\int_{K_c}\chi_\eta(g)\overline{\chi_\tau(g)}\,dg.
 \tag{DB4.1}
\]

For genuine representations this is the integer multiplicity, by character orthogonality; for virtual representations it is the corresponding integer coefficient. Its complex conjugate is the same real integer, which explains the alternative ordering seen in the source. Complex conjugation must not simply be deleted for a general complex integrand.

## DB5. Complete concentration lemma (§2.1.7)

Let \(T\) be a finite set of irreducible representations of \(K_c\), and \(0<e<1\). We construct a genuine representation \(\rho\) satisfying

\[
 [\rho\otimes\overline\rho:\tau]
 \geq(1-e)\dim\tau\,[\rho\otimes\overline\rho:1]
 \quad(\tau\in T).
 \tag{DB5.1}
\]

For \(e\geq1\) any nonzero genuine representation already suffices, so this covers the substantive range. Choose \(e_1=e_2=e/4\). Continuity of the finitely many characters at the identity supplies an open, conjugation-invariant, inversion-invariant neighborhood \(V\) such that

\[
 |\chi_\tau(g)-d_\tau|<e_1d_\tau
 \quad(g\in V,\ \tau\in T),\qquad d_\tau=\dim\tau.
 \tag{DB5.2}
\]

This can be obtained directly by intersecting the sets defined by these character inequalities and their inverses. Choose a nonzero nonnegative continuous central inversion-invariant function \(b\) supported in \(V\). Existence follows by choosing a smaller such neighborhood with closure in \(V\), a continuous bump function there, and averaging over conjugation and inversion; its value at the identity can be kept positive. Add a sufficiently small positive constant \(\delta\). The function \(b+\delta\) is strictly positive and has arbitrarily small fraction of its squared mass outside \(V\), since the numerator there is at most \(\delta^2\), while its total squared mass tends to the positive number \(\int b^2\).

Finite complex linear combinations of irreducible characters are uniformly dense in the continuous central functions of a compact group. Applying that character-density theorem and then taking the real part and averaging under inversion gives a finite character combination \(f\) which is real, inversion-invariant, uniformly arbitrarily close to \(b+\delta\), and hence strictly positive. Both strict positivity and the desired strict mass inequality persist under sufficiently small uniform perturbation. Choose the approximations with enough room that

\[
 M:=\int_{K_c}|f|^2dg>0,\qquad
 \int_{K_c\setminus V}|f|^2dg\leq e_2M.
 \tag{DB5.3}
\]

The density theorem used here is the central-function consequence of the Peter–Weyl theorem; it is a standard compact-representation dependency, not an arithmetic positivity hypothesis.

Write \(f=\sum_\chi c_\chi\chi\) over its finite support. Each coefficient is real. Indeed by (DB4.1), reality and inversion invariance give

\[
 \overline{c_\chi}=\int f(g)\chi(g)\,dg
  =\int f(g^{-1})\chi(g^{-1})\,dg
  =\int f(g)\overline{\chi(g)}\,dg=c_\chi.
 \tag{DB5.4}
\]

Reality also gives \(c_{\overline\chi}=c_\chi\). Approximate the finitely many coefficients by rationals, taking the same rational for conjugate pairs. This preserves reality and inversion invariance. By choosing the approximation close enough, strict positivity and (DB5.3) remain true. Multiplication by a common positive denominator now gives an integral virtual character

\[
 \rho_0=\sum_\chi n_\chi\chi=\rho^+-\rho^-,\qquad
 \rho^+=\sum_{n_\chi>0}n_\chi\chi,\quad
 \rho^-=\sum_{n_\chi<0}(-n_\chi)\chi.
 \tag{DB5.5}
\]

Both \(\rho^+\) and \(\rho^-\) are genuine representations; their irreducible supports are disjoint. The common multiplication rescales both integrals in (DB5.3) by the same square, so the relative estimate persists. Set \(\rho=\rho^++\rho^-\), a genuine representation. The exact tensor identity is

\[
 \rho\otimes\overline\rho
  =\rho_0\otimes\overline{\rho_0}
   +2\bigl(\rho^+\otimes\overline{\rho^-}
                +\rho^-\otimes\overline{\rho^+}\bigr).
 \tag{DB5.6}
\]

The added representations have nonnegative multiplicities. Their trivial multiplicities are zero because the two irreducible supports are disjoint. Therefore

\[
 [\rho\overline\rho:\tau]\geq[\rho_0\overline{\rho_0}:\tau],
 \qquad
 [\rho\overline\rho:1]=[\rho_0\overline{\rho_0}:1]=M.
 \tag{DB5.7}
\]

Here the notation \(\rho\overline\rho\) means the displayed tensor product, and \(M\) is now the squared mass of the scaled \(\rho_0\).

The remaining bound must include the outside integral. The inner product is a real integer; taking its real part gives

\[
\begin{aligned}
 [\rho_0\overline{\rho_0}:\tau]
 &=\operatorname{Re}\int_{K_c}|\rho_0(g)|^2
                         \overline{\chi_\tau(g)}\,dg\\
 &\geq (1-e_1)d_\tau\int_V|\rho_0|^2dg
       -d_\tau\int_{K_c\setminus V}|\rho_0|^2dg\\
 &\geq d_\tau\bigl[(1-e_1)(1-e_2)-e_2\bigr]M\\
 &=d_\tau(1-e_1-2e_2+e_1e_2)M
 \geq(1-e)d_\tau M.
\end{aligned}
 \tag{DB5.8}
\]

The bound outside \(V\) uses \(\operatorname{Re}\overline{\chi_\tau(g)}\geq-d_\tau\), valid because every eigenvalue is on the unit circle. For the chosen constants, \(e_1+2e_2-e_1e_2=3e/4-e^2/16<e\). Together with (DB5.7), this proves (DB5.1) with all real/virtual-character and error terms accounted for.

## DB6. The exceptional quadratic character (§§2.1.5–2.1.8)

Let \(T\subset\widehat G\setminus\{1\}\) be finite, and apply DB5. All multiplicities omitted from \(T\cup\{1\}\) multiply nonpositive values of \(\nu\). Positivity therefore gives

\[
\begin{aligned}
0&\leq\nu(\rho\overline\rho)
 =\sum_\sigma[\rho\overline\rho:\sigma]\nu(\sigma)\\
&\leq M+\sum_{\tau\in T}[\rho\overline\rho:\tau]\nu(\tau)\\
&\leq M\left(1+(1-e)\sum_{\tau\in T}d_\tau\nu(\tau)\right).
\end{aligned}
 \tag{DB6.1}
\]

The final inequality reverses the multiplicity lower bound when multiplying by \(\nu(\tau)\leq0\); that sign is essential. Since \(M>0\), division and \(e\downarrow0\) prove, for every finite \(T\),

\[
 \sum_{\tau\in T}d_\tau(-\nu(\tau))\leq1.
 \tag{DB6.2}
\]

Every summand is a nonnegative integer. Thus at most one nontrivial irreducible can have negative \(\nu\), and then it must have dimension one and \(\nu=-1\). Conjugation symmetry forces that character \(\varepsilon\) to equal \(\overline\varepsilon\). A unitary one-dimensional character satisfies \(\overline\varepsilon=\varepsilon^{-1}\), so \(\varepsilon^2=1\); as it is nontrivial, its order is exactly two.

Consequently the original analytic family has no boundary zero except possibly a single simple zero at \(\omega_1\varepsilon\) for one nontrivial quadratic character. This proves the source's theorem §2.1.4 from its stated analytic hypotheses, including the entire exceptional case.

## DB7. The discrete limiting measure and its pole cancellation (§§2.1.10–2.1.11)

For this section \(\Gamma=\mathbb Z\) and the quadratic exception has been excluded by whatever arithmetic input verifies source condition (C): \(L\) has the specified simple pole and no boundary zero. This condition will be proved for the curve application below; it is not silently inferred for an unrelated representation family.

Retain the source measures

\[
 \mu^{\natural}=\sum_v\sum_{n\geq1}
      \deg(v)q^{-n\deg(v)}\delta_{[x_v^n]},
 \qquad
 \mu_0=\mathbf1_{\deg>0}\,dg,
 \tag{DB7.1}
\]

where Haar measure \(dg\) on \(G\) gives its degree-zero compact subgroup mass one, and \(\mu_0^\natural\) is the pushforward to conjugacy classes. Each positive degree component has \(\mu_0\)-mass one. The weighted measure \(\mu^\natural\) is locally finite: only divisors of a fixed positive degree enter a fixed component, and (DB2.1) makes every fixed degree contain finitely many \(v\).

For \(\operatorname{Re}\tau>0\), (DB2.3) gives exactly

\[
 \widehat\mu^{\natural}(\tau)
 =-\frac1{\log q}\frac{L'}L(\omega_1\tau).
 \tag{DB7.2}
\]

The factor \(1/\log q\) is necessary because \(\log N_v=\deg(v)\log q\). Averaging an irreducible representation over the compact kernel is its projection onto the kernel invariants. That subspace is \(G\)-stable because the kernel is normal. Irreducibility makes it either zero or the whole representation; in the latter case the representation factors through \(\mathbb Z\) and is one-dimensional. Therefore the transform of \(\mu_0^\natural\) vanishes on all other irreducibles, while

\[
 \widehat\mu_0^{\natural}(\omega_s)
   =\sum_{m=1}^{\infty}q^{-ms}
   =\frac{q^{-s}}{1-q^{-s}}.
 \tag{DB7.3}
\]

On the representation surface both transforms have just the pole at the trivial character on \(\operatorname{Re}\tau\geq0\), with residue \(1/\log q\): the first follows from DB3 and the original simple pole, and the second follows from \(1-q^{-s}=s\log q+O(s^2)\). They cancel exactly. Hence the Fourier–Laplace transform of \(\mu^\natural-\mu_0^\natural\) is holomorphic on a neighborhood of that closed half-plane.

## DB8. Equidistribution with its convergence proof (§§2.1.12–2.1.13)

For a fixed unitary representation \(\tau\), define

\[
 a_m=\int_{G_m^\natural}\chi_\tau(g)
                    \,d(\mu^\natural-\mu_0^\natural)(g),\qquad m>0.
 \tag{DB8.1}
\]

There is no additional Haar factor multiplying this measure integral. Its transform at \(\tau\omega_s\) is

\[
 \sum_{m\geq1}a_mq^{-ms}.
 \tag{DB8.2}
\]

Put \(t=q^{-s}\), retaining its exact original scale \(\log q\). The period from (DB1.3) makes this a single-valued holomorphic function of \(t\) on a neighborhood of the punctured closed unit disk; the power series supplies the value at zero. Compactness of the unit circle gives a common open annulus across it, hence a disk \(|t|<R\) for some \(R>1\). For \(1<r<R\), Cauchy's coefficient formula yields

\[
 |a_m|\leq \max_{|t|=r}\left|\sum_{j\geq1}a_jt^j\right|r^{-m}.
 \tag{DB8.3}
\]

Thus each character integral tends to zero, with a constant and decay radius allowed to depend on \(\tau\). No uniform spectral gap over all representations is inferred.

Choose a central \(z\) of positive degree \(d\). Translate the degree \(i+nd\) slice to the fixed compact conjugacy slice of degree \(i\) by multiplication by \(z^{-n}\), for \(0\leq i<d\). The compact quotient \(G/\langle z\rangle\) contains this slice, and its characters uniformly span the continuous class functions on it: extend a continuous class function by zero on the other finitely many degree classes and apply the same central character-density theorem used in DB5. Their pullbacks are unitary representations of \(G\) trivial on \(z\), so the translated character integral differences tend to zero by (DB8.3).

The total masses of the positive translated measures tend to one, by applying (DB8.3) to the trivial representation, while the comparison measure has mass one. Uniform approximation of any continuous class function \(f\) by a finite character combination \(P\) gives an error bounded by \(\|f-P\|_\infty\) times the sum of those two masses. First make this error small, then use the finite character convergence. This proves vague convergence of the translated measures asserted in §2.1.12. It also supplies the approximation argument underlying §2.1.13.

## DB9. Exact specialization to the original Riemann zeta (§2.1.9)

This specialization is made after the full arithmetic has been reconstructed. Let \(G=\Gamma=(\mathbb R,+)\), let the compact kernel be \(K=\{0\}\), and set

\[
 \omega_s(x)=e^{-sx},\qquad
 \Sigma=\{\hbox{all primes of the recovered integers}\},\qquad
 x_p=\log p,\qquad N_p=p.
 \tag{DB9.1}
\]

No finite set of selected primes is used to establish any of these data. All irreducible finite-dimensional unitary representations of \(\mathbb R\) are the characters \(x\mapsto e^{-itx}\): commuting unitary matrices can be simultaneously diagonalized, and an irreducible common eigenspace has dimension one. A continuous character of \(\mathbb R\) has the displayed form by lifting near zero to its argument and using additivity.

For \(\operatorname{Re}s>1\), the original function is

\[
 \zeta(s)=\sum_{m=1}^{\infty}m^{-s}
         =\prod_{p}(1-p^{-s})^{-1}.
 \tag{DB9.2}
\]

The equality follows from the recovered integer factorization: a finite product expands over integers supported on those primes, and absolute convergence lets the finite prime sets increase to all primes. Each integer eventually occurs, with coefficient one. Thus the complete representation family is exactly \(L(\omega_s)=\zeta(s)\), not a completed or rescaled zeta function.

Differentiating the absolutely convergent full product as in DB2 gives

\[
 -\frac{\zeta'(\sigma+it)}{\zeta(\sigma+it)}
  =\sum_{p}\sum_{n=1}^{\infty}
        (\log p)p^{-n\sigma}e^{-itn\log p}
  =\int_{\mathbb R}e^{-itx}\,d\mu_\sigma(x),
 \tag{DB9.3}
\]

with exactly the measure

\[
 \mu_\sigma=\sum_{p}\sum_{n=1}^{\infty}
       (\log p)p^{-n\sigma}\delta_{n\log p},\qquad\sigma>1.
 \tag{DB9.4}
\]

Every prime-power location, weight, and multiplicity is retained. For any real \(t_1,\ldots,t_k\) and complex \(c_1,\ldots,c_k\), its positive-definiteness is the exact identity

\[
 \sum_{j,l}c_j\overline{c_l}
  \left(-\frac{\zeta'(\sigma+i(t_j-t_l))}
                  {\zeta(\sigma+i(t_j-t_l))}\right)
   =\int\left|\sum_jc_je^{-it_jx}\right|^2d\mu_\sigma(x)\geq0.
 \tag{DB9.5}
\]

No zero-location assumption enters this positivity.

The analytic hypothesis on the closed boundary follows directly from the original Dirichlet series identity

\[
 \zeta(s)=\frac{s}{s-1}
           -s\int_1^\infty\{x\}x^{-s-1}dx,
            \qquad\operatorname{Re}s>0,
 \tag{DB9.6}
\]

initially proved for \(\operatorname{Re}s>1\) by integration against \(\lfloor x\rfloor\) and then continued by the locally uniformly convergent integral. It proves holomorphy on this half-plane except at the simple pole \(s=1\), whose residue is one. In particular the assumptions of DB3 are verified for every representation of this \(G\), rather than imported from a larger unconstructed representation family.

There is no nontrivial continuous quadratic character \(\mathbb R\to\{\pm1\}\), because the image of a connected space is connected and must contain the identity. The exceptional case of DB6 is therefore absent. It follows that the original \(\zeta(s)\) has no zero on \(\operatorname{Re}s=1\). The point \(s=1\) is its already calculated pole.

The source's exact numerical coefficients also have a direct proof. With \(\Lambda_\sigma(t)=-\zeta'(\sigma+it)/\zeta(\sigma+it)\),

\[
\begin{aligned}
 3\operatorname{Re}\Lambda_\sigma(0)
 +4\operatorname{Re}\Lambda_\sigma(t)
 +2\operatorname{Re}\Lambda_\sigma(2t)
 &=\int\bigl(3+4\cos(tx)+2\cos(2tx)\bigr)d\mu_\sigma(x)\\
 &=\int(1+2\cos(tx))^2d\mu_\sigma(x)\geq0.
\end{aligned}
 \tag{DB9.7}
\]

For \(t\ne0\), put \(m_t\) and \(m_{2t}\) equal to the actual zero multiplicities at \(1+it\) and \(1+2it\), with value zero at a nonzero function value. Multiplication by \(\sigma-1\) and (DB3.2) gives

\[
 0\leq3-4m_t-2m_{2t}.
 \tag{DB9.8}
\]

Any positive integer \(m_t\) contradicts this inequality. This is a second complete proof of the same boundary result, preserving the source's coefficients \(3,4,2\). It uses the entire measure, not values at any numerical prime shortcut.

This specialization has trivial compact kernel and \(\Gamma=\mathbb R\). It does not supply a nontrivial compact geometric monodromy group, a curve over a finite field, or the cohomological determinant formula used in §2.2. Those structures and their hypotheses must be provided by an actual receiving construction; they do not follow from the prime-power measure alone. Equations (DB9.3)–(DB9.8) concern \(\operatorname{Re}s=1\), with no shift of the original zeta function to a different working function.

## DB10. Dependency boundary for the compact-form and curve argument

The remaining reconstruction follows §2.2 and uses its explicitly stated geometric inputs: an algebraic monodromy extension, dense geometric fundamental-group image, a sufficiently faithful mixed sheaf, the determinant and semisimplicity results of §§1.3–1.5, compact complexification theory, and the cohomological trace formula with duality. These are named source dependencies, not assumptions silently supplied to the original-zeta specialization. The full compact-form calculation, all weight factors, the curve simple-pole argument, the exceptional double cover, and the strict bound follow below.

## DBC1. Source, provenance, and exact scope

Human source: Pierre Deligne, *La conjecture de Weil. II*, Publications Mathématiques de l’IHÉS **52** (1980), 137–252, §§2.2.1–2.2.10, printed pp. 192–196. The reading witness is the French transcription export at `output/Deligne_Weil_II_S20_LaTeX/typed_latex/S20_FR_record_export.tex`, lines 1784–1927, SHA256 `d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351`. This is a local transcription, not original author TeX. No PDF was opened, no source file was changed, and no public upload was made.

The existing literature-routing ledger identifies the work by `PUBUNIT-3D90B487DBD1CC3A259C6455` and `PUBUNIT-574B0214207BBB2BDABCFFF9`; those routing records are not substitutes for reading. This subtask read all of the assigned lines and additionally the exact local dependencies listed below. Root’s existing `USER_INPUTS_VERBATIM.md` and `DELIGNE_FULL_READING_LOG.md` retain the wider user provenance and reading history.

Task received: independently reconstruct compact-form conjugacy, representation equivalence, the mixed-to-pure input, and the strict compactly supported first-cohomology bound; keep every twist factor; check the sign in §2.2.8, cancellation, and the quadratic-cover exception. The parent handles the upstream determinant-weight and real-sheaf-purity derivations; DB3–DB6 above supply the complete proof of §§2.1.4–2.1.8. This file supplies the receiving calculations and does not claim to have reproved all upstream theorems.

Read dependencies and their roles:

| Source location | Local lines | Role |
|---|---:|---|
| §§1.1.12–1.1.14 | 448–473 | Weil representations, degree, and cohomological Frobenius |
| §§1.2.1–1.2.7 | 479–528 | Pointwise weights, mixedness, and exact twist factors |
| §§1.3.5–1.3.12 | 630–710 | Monodromy extension, semisimple geometric identity component, central degree, determinant weights |
| §1.3.14 | 722–730 | Finite-image rank-one Weil characters are étale |
| §§1.4.1–1.4.7 | 745–813 | Invariants, coinvariants, Tate factor, trace formula, Euler convergence |
| §§1.8.1–1.8.2 | 1210–1234 | Earlier non-strict bound and boundary purity |
| §§1.8.10–1.8.12 | 1315–1329 | A mixed irreducible lisse sheaf on a normal scheme is pointwise pure |
| §§2.1.1–2.1.8 | 1559–1724 | Sign convention and analytic nonvanishing theorem; detailed proof belongs to the parent’s reconstruction |
| §2.1.10 | 1736–1740 | Exact statement of condition (C) |

The following foundational inputs remain named inputs: the correspondence between lisse Weil sheaves and Weil-group representations; Grothendieck’s trace formula and Poincaré duality in §§1.4.1–1.4.5; the geometric monodromy theorem in §1.3.9 and central determinant criterion in §1.3.12; compact real forms of complex reductive groups, conjugacy of maximal compact subgroups, and extension of continuous finite-dimensional representations of a compact real form to algebraic representations of its complexification. These are not conclusions manufactured by the calculation below.

## DBC2. Original degree and weight conventions

Let \(q=p^f>1\), let \(\ell\ne p\), and fix the field isomorphism
\[
\iota:\overline{\mathbf Q}_\ell\longrightarrow\mathbf C.
\]
For \(\alpha\ne0\),
\[
w_q(\alpha)=2\log_q|\iota\alpha|.
\tag{DBC.2.1}
\]
If \(v\) is a closed point of degree \(d_v=[k(v):\mathbf F_q]\), geometric Frobenius \(F_v\) has degree \(d_v\), and
\[
\omega_s(g)=q^{-s\deg(g)},\qquad
\omega_s(F_v)=q^{-s d_v}.
\tag{DBC.2.2}
\]
In particular the actual period in \(s\) is \(2\pi i/\log q\).

For an irreducible complex representation \(\tau\) of the group in §3, its real part \(\sigma=\Re(\tau)\) is defined by
\[
|\tau(z)|=\omega_\sigma(z)=q^{-\sigma m}
\tag{DBC.2.3}
\]
for a central element \(z\) of positive degree \(m\). Here \(\tau(z)\) is scalar by Schur’s lemma. The representation \(\tau\omega_{-\sigma}\) is unitarizable: choose a Hermitian form invariant under the scalar of modulus one acting as \(z\); average its translates over the compact group \(G_{\mathbf R}/\langle z\rangle\). Translation by \(z\) does not change the integrand, so the average is defined and \(G_{\mathbf R}\)-invariant.

Therefore, for an element \(g\in G_{\mathbf R}\) of degree \(d\), every eigenvalue of \(\tau(g)\) has modulus \(q^{-\sigma d}\). Consequently the corresponding sheaf has pointwise weight
\[
\boxed{-2\Re(\tau)}.
\tag{DBC.2.4}
\]
This is also forced by the test representation \(\tau=\omega_s\), whose degree-one scalar is \(q^{-s}\). The plus sign in the local witness at line 1871 is inconsistent with its own definitions. This is a demonstrated discrepancy in the transcription witness, not an assertion about an uninspected printed page.

## DBC3. The compact form and conjugacy

Let
\[
1\longrightarrow G_{\mathbf C}^{0}\longrightarrow G_{\mathbf C}
 \xrightarrow{\deg}\mathbf Z\longrightarrow0
\tag{DBC.3.1}
\]
be the complex group scheme of §2.2.1. The algebraic group \(G_{\mathbf C}^{0}\) may be disconnected; its identity component is semisimple. Let \(Z_{\mathbf C}\) be the center of the full group. By §1.3.10, its degree image has finite index in \(\mathbf Z\). Its degree-zero kernel is finite, because it lies in the center of the algebraic group with semisimple identity component. Thus
\[
H=G_{\mathbf C}/Z_{\mathbf C}
\]
is a finite-type reductive algebraic group. Choose a maximal compact subgroup \(U\subset H(\mathbf C)\) and set
\[
G_{\mathbf R}=\pi^{-1}(U),\qquad
K^0=G_{\mathbf R}\cap G_{\mathbf C}^{0}.
\tag{DBC.3.2}
\]
The group \(K^0\) is a maximal compact subgroup of \(G_{\mathbf C}^{0}\), and every connected component of the quotient is met by \(U\). Hence degree maps \(G_{\mathbf R}\) onto \(\mathbf Z\), with kernel \(K^0\).

Choose \(z\in Z_{\mathbf C}\) of degree \(m>0\). It belongs to \(G_{\mathbf R}\), since its image in \(H\) is the identity. Put
\[
A=G_{\mathbf C}/\langle z\rangle,
\qquad K=G_{\mathbf R}/\langle z\rangle.
\tag{DBC.3.3}
\]
These are a finite-type complex reductive group and a maximal compact real form. Indeed, \(Z_{\mathbf C}/\langle z\rangle\) is finite, so \(A\to H\) is a finite central map, and \(K\) is the inverse image of \(U\). Alternatively, compactness follows directly because \(K\) has only \(m\) degree classes, each represented by a translate of the compact group \(K^0\).

Suppose \(a,b\in G_{\mathbf R}\) are conjugate in \(G_{\mathbf C}\). Their images in \(K\) are conjugate in \(A\). Every irreducible continuous character of \(K\) extends to an algebraic character of \(A\), so those characters take the same values on the two images. Characters separate conjugacy classes in a compact group: the algebra spanned by characters is dense in the continuous central functions, which separate disjoint compact conjugacy classes. Thus their images are conjugate in \(K\). Lift a conjugating element to \(u\in G_{\mathbf R}\). For some integer \(j\),
\[
uau^{-1}=b z^j.
\]
Conjugacy preserves degree, so \(\deg(a)=\deg(b)\), while the displayed identity gives \(\deg(a)=\deg(b)+jm\). Thus \(j=0\). This proves the full conjugacy assertion of §2.2.2, including the central degree coordinate.

The local witness of §1.3.10(iv), line 688, says “finite subgroup” where its proof and the corollary with finite cokernel require “subgroup of finite index.” The argument here uses the latter statement, exactly as proved by the nonzero-degree central element in lines 692–698.

For completeness, the Jordan decomposition in §2.2.3 keeps the central coordinate as follows. Given \(g\in G_{\mathbf C}\), write its image \(\pi(g)\in H\) as the commuting product \(h_s h_u\). The unipotent element \(h_u\) lies in the identity component of \(H\), which is the image of the identity component of \(G_{\mathbf C}^{0}\) under a finite central map. It has a unique unipotent lift \(u\) to \(G_{\mathbf C}^{0}\). To verify this, take any lift in the identity component and its ordinary Jordan decomposition: its unipotent part maps to \(h_u\), while its semisimple part maps to the identity and is finite central. Two unipotent lifts differ by a finite central element, which would be the semisimple part of their quotient expression, so that element must be the identity. Conjugation by \(g\) preserves \(u\), by uniqueness and because \(\pi(g)\) commutes with \(h_u\). Therefore
\[
g_u=u,\qquad g_s=g u^{-1},\qquad g=g_sg_u=g_ug_s.
\tag{DBC.3.4}
\]
The image of \(g_s\) in \(H\) is semisimple and its degree is the full original degree of \(g\). Any other such decomposition would give another unipotent lift of \(h_u\), so (DBC.3.4) is unique.

## DBC4. Representation equivalence, including nonsemisimple representations

Scalar transport along the field isomorphism \(\iota\) gives an equivalence
\[
\operatorname{Rep}_{\overline{\mathbf Q}_\ell}(G)
\longrightarrow\operatorname{Rep}_{\mathbf C}(G_{\mathbf C}).
\tag{DBC.4.1}
\]
The target and source are finite-dimensional algebraic representations of the group schemes; algebraicity is required on the finite-type degree-zero group.

For restriction to \(G_{\mathbf R}\), choose \(u\in G_{\mathbf R}\) of degree one. Every element of \(G_{\mathbf R}\) has a unique expression \(h u^n\), \(h\in K^0\), and every element of \(G_{\mathbf C}\) has the corresponding expression with \(h\in G_{\mathbf C}^{0}\). Let \(r\) be any finite-dimensional continuous representation of \(G_{\mathbf R}\). Its restriction to \(K^0\) has a unique algebraic extension \(r_0\) to \(G_{\mathbf C}^{0}\). Set \(T=r(u)\). On \(K^0\),
\[
T r_0(h)T^{-1}=r_0(u h u^{-1}).
\]
Both sides are algebraic in \(h\); the compact real form \(K^0\) is Zariski dense in \(G_{\mathbf C}^{0}\). Therefore this identity holds on \(G_{\mathbf C}^{0}\). The formula
\[
\widetilde r(h u^n)=r_0(h)T^n
\tag{DBC.4.2}
\]
is consequently an algebraic representation of \(G_{\mathbf C}\), restricting to \(r\). Uniqueness follows from the same density and the value on \(u\). An intertwiner on the real group intertwines \(r_0\) by density and intertwines \(T\), so it intertwines (DBC.4.2). Restriction is therefore fully faithful and essentially surjective.

No diagonalizability of \(T\) was assumed. In particular, these equivalences include extensions and Jordan blocks in the degree action. One cannot assert that every group element called semisimple in §2.2.3 has semisimple image under an arbitrary representation: for \(G=\mathbf Z\), a generator may act by a nontrivial Jordan block. The finite-type quotient used in the next section is exactly where the usual preservation of Jordan decomposition is valid.

## DBC5. Mixed input, all twist factors, and compact Frobenius classes

Assume §§2.2.4(a)–(c): a degree-preserving morphism
\[
W(X_0,\bar x)\longrightarrow G,
\]
with \(X_0\) normal and geometrically connected; continuous geometric image in some finite extension of \(\mathbf Q_\ell\), Zariski dense in \(G^0\); and a representation \(V\) with finite kernel on \(G^0\), whose lisse sheaf is \(\iota\)-mixed.

Every irreducible \(G\)-constituent \(V_a\) is an irreducible Weil representation. To see this, the Weil image is Zariski dense in each degree component, since its degree-zero image is dense and it meets every degree. The stabilizer of any vector subspace is Zariski closed. Thus Weil-stable subspaces and \(G\)-stable subspaces coincide.

The sheaf of \(V_a\) is mixed by stability under subquotients. The implication from mixed to pointwise pure uses §1.8.11, not mixedness without a lisse argument. On a sufficiently small dense open the mixed filtration is lisse; irreducibility on that open follows from normality, so only one weight occurs there. Section 1.8.10 extends that purity over \(X_0\). Denote its weight by \(\beta_a\).

Choose the central element \(z\) of degree \(m>0\) from §3, now over \(\overline{\mathbf Q}_\ell\), and write its action on \(V_a\) as \(\lambda_a\). The determinant-weight criterion §1.3.12 yields
\[
|\iota\lambda_a|=q^{m\beta_a/2}.
\tag{DBC.5.1}
\]
Choose \(c_a\in\overline{\mathbf Q}_\ell^*\) with
\[
c_a^m=\lambda_a^{-1}.
\tag{DBC.5.2}
\]
Let \(L_{c_a}\) be the rank-one Weil sheaf pulled back from \(\operatorname{Spec}\mathbf F_q\), with degree-one geometric Frobenius scalar \(c_a\). Define an auxiliary representation
\[
V'_a=V_a\otimes L_{c_a},\qquad
V_a\cong V'_a\otimes L_{c_a^{-1}}.
\tag{DBC.5.3}
\]
The latter isomorphism comes from evaluation \(L_{c_a}\otimes L_{c_a^{-1}}\to\mathbf1\). It preserves the original representation with its full degree factor. At a degree-\(d_v\) point, and on every cohomology group, the exact formulas are
\[
F_v|V'_a=c_a^{d_v}(F_v|V_a),\qquad
F|H_c^i(X,V'_a)=c_a(F|H_c^i(X,V_a)),
\tag{DBC.5.4}
\]
under the geometric-fibre identifications. Thus every original local eigenvalue \(\alpha\) becomes \(c_a^{d_v}\alpha\), and is recovered as \(c_a^{-d_v}(c_a^{d_v}\alpha)\). Every original cohomological eigenvalue \(\gamma\) becomes \(c_a\gamma\) and is recovered by the inverse scalar.

More explicitly, choose a nonzero geometric fibre vector \(e_a\) for \(L_{c_a}\). The tensor map \(v\mapsto v\otimes e_a\) identifies underlying geometric fibres, and the projection formula identifies \(H_c^i(X,\mathcal F_a\otimes L_{c_a})\) with \(H_c^i(X,\mathcal F_a)\otimes L_{c_a,\bar{\mathbf F}_q}\). Frobenius on this tensor product is \(F\otimes c_a\), which proves (DBC.5.4). These are geometric identifications with the displayed changed Frobenius action, not an assertion that \(\mathcal F_a\) and \(\mathcal F_a\otimes L_{c_a}\) are isomorphic as Weil sheaves.

The source’s twist over \(\mathbf F_p\) is identical after choosing \(b_a\) with \(b_a^f=c_a\): its closed-point factor is
\[
b_a^{[k(v):\mathbf F_p]}=b_a^{f d_v}=c_a^{d_v},
\tag{DBC.5.5}
\]
and its degree-one cohomological factor is \(b_a^f=c_a\). All base-field exponents are retained.

Equations (DBC.5.1)–(DBC.5.2) give \(|\iota c_a|=q^{-\beta_a/2}\), so the auxiliary local eigenvalues have modulus one. Also \(z\) acts on \(V'_a\) by \(\lambda_a c_a^m=1\). Therefore
\[
V'=\bigoplus_a V'_a
\]
factors through the finite-type quotient \(G/\langle z\rangle\). Its restriction to \(G^0\) still has finite kernel: the twists are geometrically trivial; restriction of the original representation to reductive \(G^0\) is semisimple; and its restriction is the direct sum of the restrictions of its \(G\)-constituents. The kernel of the representation on the quotient is then finite, since that quotient has finitely many components, and a kernel’s intersection with any one component is either empty or a translate of its finite intersection with the degree-zero subgroup.

Let \(g=\iota F_v\), and let \(g_s\) be its semisimple part in the sense of §2.2.3. In the finite-type quotient just constructed, Jordan decomposition is respected by the representation. Hence the image of \(g_s\) acts diagonally with all eigenvalues of modulus one. The closure of its integer powers in \(\mathrm{GL}(V')\) is compact. A homomorphism of complex algebraic groups with finite kernel is finite onto its closed image, and its map of complex points is proper. Therefore the powers of the image of \(g_s\) in \(G_{\mathbf C}/\langle z\rangle\) have compact closure. Their further image in \(G_{\mathbf C}/Z_{\mathbf C}\) has compact closure as well. Every compact subgroup lies in a maximal compact subgroup; all maximal compact subgroups of this reductive group are conjugate. It follows that \(g_s\) is conjugate into \(G_{\mathbf R}\). Section 3 proves uniqueness of its \(G_{\mathbf R}\)-conjugacy class.

The use of \(V'_a\) here establishes existence of a compact Frobenius representative. It neither replaces the original sheaves in the strict-bound calculation nor discards \(c_a^{d_v}\) or \(c_a\).

Now let \(\tau\) be any irreducible representation of \(G_{\mathbf R}\). The compact representative of \(g_s\) and (DBC.2.3) give local eigenvalue modulus \(q^{-\Re(\tau)d_v}\). The unipotent part of \(g\) acts unipotently, commutes with its semisimple part, and does not change the multiset of eigenvalues of their product: on each generalized eigenspace of the first commuting operator, the product has that operator’s eigenvalue multiplied by the sole eigenvalue one of the second. Thus the sheaf for \(\tau\) has weight \(-2\Re(\tau)\). An arbitrary representation has a finite composition series, so its associated sheaf is mixed. This order of proof avoids using purity of all representations to prove the initial compactness assertion.

## DBC6. The complete L-function identity

Write \(\mathcal F_0(\tau_\ell)\) for the sheaf corresponding to \(\tau\). At a closed point, conjugation and removal of the commuting unipotent part preserve the characteristic polynomial. Consequently
\[
\begin{aligned}
L(\tau,s)
&=\prod_{v\in|X_0|}
 \det(1-\tau(x_v)q^{-s d_v})^{-1}\\
&=\left.\iota Z(\mathcal F_0(\tau_\ell),t)\right|_{t=q^{-s}}.
\end{aligned}
\tag{DBC.6.1}
\]
For a smooth geometrically connected curve, put
\[
P_i(t)=\iota\det(1-tF\mid H_c^i(X,\mathcal F)).
\]
The trace formula gives the unreduced rational expression
\[
\boxed{L(\tau,s)=\frac{P_1(q^{-s})}
 {P_0(q^{-s})P_2(q^{-s})}.}
\tag{DBC.6.2}
\]
If \(V\) is the geometric fibre and \(\Pi=\pi_1(X,\bar x)\), then
\[
H_c^0(X,\mathcal F)=
\begin{cases}V^\Pi&X\text{ proper},\\0&X\text{ not proper},\end{cases}
\qquad
H_c^2(X,\mathcal F)=V_\Pi(-1).
\tag{DBC.6.3}
\]
Geometric Frobenius acts on \(\overline{\mathbf Q}_\ell(-1)\) by \(q\). This factor is retained in every denominator below.

Section 2.2.7 also treats a normal geometrically connected scheme of dimension \(N\ge1\). Keep precisely the same character \(\omega_1(g)=q^{-\deg(g)}\). The point-count estimate in §1.4.6 gives a constant \(C\) with
\[
\#\{v:\deg v=d\}\le Cq^{Nd}.
\]
For an irreducible representation \(\rho\) of dimension \(r\), write \(\sigma=\Re(\rho)\). Every eigenvalue of \(\rho(x_v)\) has modulus \(q^{-\sigma d_v}\). If \(\sigma>N\), the full logarithmic Euler series is absolutely bounded by
\[
\begin{aligned}
\sum_v\sum_{k\ge1}\frac{|\operatorname{Tr}(\rho(x_v)^k)|}{k}
&\le Cr\sum_{d\ge1}q^{Nd}\sum_{k\ge1}\frac{q^{-\sigma dk}}{k}\\
&\le\frac{Cr}{1-q^{-\sigma}}\sum_{d\ge1}q^{-(\sigma-N)d}<\infty.
\end{aligned}
\tag{DBC.6.4}
\]
Therefore \(L(\rho)\) converges and is nonzero for \(\Re(\rho)>N\). For a fixed original representation \(\tau\) of weight \(\beta=-2\Re(\tau)\), the exact region is
\[
\Re(s)>N+\frac\beta2
\quad\text{for }L(\tau,s)=L(\tau\omega_s).
\tag{DBC.6.5}
\]
In particular a unitary \(\tau\) gives \(\Re(s)>N\). The character has not been changed to \(q^{-N\deg(g)}\); the original degree, the original parameter \(s\), and the dimension \(N\) all remain visible.

## DBC7. Curve zeta poles without a noncancellation assumption

We first prove the simple pole of the zeta function at \(t=q^{-1}\) using (DBC.6.2), rather than invoking equidistribution whose hypotheses already include that pole.

For the constant sheaf on a smooth geometrically connected curve,
\[
Z(X_0,t)=\frac{P_1(t)}{(1-t)^\delta(1-qt)},
\qquad \delta=\begin{cases}1&X_0\text{ proper},\\0&X_0\text{ not proper}.\end{cases}
\tag{DBC.7.1}
\]
Suppose \(P_1(q^{-1})=0\). Remove one occurrence of the factor \(1-qt\) from this polynomial, and write the remaining polynomial as \(\prod_{j=1}^r(1-a_jt)\), with every multiplicity retained. Logarithmic differentiation of the resulting identity gives, for every \(n\ge1\),
\[
\#X_0(\mathbf F_{q^n})=\delta-\sum_{j=1}^r a_j^n.
\tag{DBC.7.2}
\]
If \(R=\max_j|a_j|>1\), the phases \(a_j/R\) for the indices of modulus \(R\) lie on a finite-dimensional compact torus. There exist arbitrarily large positive integers \(n\) for which all those phases to the \(n\)-th power are as close to one as prescribed. Indeed, among powers of any point of a compact group, two arbitrarily widely separated powers occur arbitrarily close: choose a convergent subsequence and take differences of sufficiently separated indices. Their quotient tends to the identity. Along these integers the real part of the sum of the modulus-\(R\) terms is at least \(r_R R^n/2\), where \(r_R\ge1\) is their number. The remaining terms are bounded in modulus by \((r-r_R)R_1^n\), for some \(R_1<R\). Thus (DBC.7.2) becomes negative for sufficiently large members of that sequence, contradicting the nonnegative point count.

It follows that all \(|a_j|\le1\), in which case (DBC.7.2) gives \(\#X_0(\mathbf F_{q^n})\le\delta+r\) for all \(n\). This is also impossible: a nonempty curve has infinitely many geometric closed points, and every finite selection of such points is defined over one common finite extension. Hence its point counts over finite extensions are unbounded. The contradiction proves
\[
P_1(q^{-1})\ne0.
\tag{DBC.7.3}
\]
The factor \(1-qt\) in (DBC.7.1) is simple, and \(1-q^{-1}\ne0\); the pole is therefore exactly simple.

For a smooth connected curve \(Y_0\) whose field of constants is \(\mathbf F_{q^d}\), view the same scheme as a geometrically connected curve \(Y_*\) over \(\mathbf F_{q^d}\). Its local degrees satisfy \(\deg_{\mathbf F_q}(y)=d\deg_{\mathbf F_{q^d}}(y)\), hence
\[
Z(Y_0,t)=Z(Y_*,t^d).
\tag{DBC.7.4}
\]
The latter expression has top denominator \(1-q^d t^d\), and its numerator is nonzero at \(t=q^{-1}\) by the preceding argument over \(\mathbf F_{q^d}\). The derivative of that denominator there is \(-d q\ne0\). Thus the pole at \(t=q^{-1}\) is still simple, even though \(Y_0\) has \(d\) geometric components. The parameter change \(t=q^{-s}\) has derivative \(-\log(q)q^{-s}\ne0\), so pole order one is also preserved at \(s=1\).

## DBC8. The quadratic exception and condition (C)

For an irreducible unitary \(\tau\) that is nontrivial on \(G_{\mathbf R}^0\), its invariant and coinvariant spaces under \(G^0\) vanish. Indeed, \(V^{G^0}\) is \(G\)-stable; irreducibility makes it zero or all of \(V\), and the latter is excluded. Reductivity of \(G^0\) makes invariants and coinvariants isomorphic as representations of the degree action, so both vanish. Zariski density gives the same conclusion for \(\Pi\). Therefore \(P_0=P_2=1\), and \(L(\tau,s)\) is the polynomial \(P_1(q^{-s})\), holomorphic everywhere in \(s\).

An irreducible representation trivial on \(G^0\) factors through \(\mathbf Z\) and is one-dimensional. In the unitary case it is \(\omega_{it}\) for some real \(t\). Its L-function is a translate of the curve zeta function. Equations (DBC.7.1)–(DBC.7.3) show that in the representation half-plane \(\Re(\rho)\ge1\), the only pole is a simple pole at \(\rho=\omega_1\). (Distinct values of \(s\) representing the same character are the same point of this representation parameter space.) Euler convergence holds for \(\Re(\rho)>1\).

The analytic theorem §2.1.4 therefore applies. It states that on \(\Re(\rho)=1\) there can be at most one exceptional zero, necessarily at \(\rho=\omega_1\varepsilon\), where \(\varepsilon\) is a nontrivial character of exact order two.

The finite-image Weil character \(\varepsilon\) defines an étale rank-one sheaf, hence an étale double cover \(f:Y_0\to X_0\). For example, étaleness follows from the rank-one criterion and its proof in §1.3.14, since all its scalars are roots of unity and therefore \(\ell\)-adic units. Its pullback to the Weil group is still nontrivial: the character extends algebraically to \(G\), and the Weil image is Zariski dense in every component. The cover is connected over \(\mathbf F_q\): the character is nontrivial, so the arithmetic monodromy acts transitively on its two-element fibre. There are exactly two geometric cases:

1. If \(\varepsilon|_\Pi\ne1\), the geometric image is the full group of order two, so \(Y_0\) is geometrically connected, with constant-field degree one.
2. If \(\varepsilon|_\Pi=1\), then \(\varepsilon(g)=(-1)^{\deg g}\). The cover is \(X_0\times_{\mathbf F_q}\mathbf F_{q^2}\), connected over \(\mathbf F_q\) and with two geometric components. Its constant-field degree is two.

The deck involution on \(f_*\overline{\mathbf Q}_\ell\) has projectors \((1+\sigma)/2\) and \((1-\sigma)/2\). These are valid also when \(\ell=2\), because the coefficient field has characteristic zero. They give
\[
f_*\overline{\mathbf Q}_\ell\cong
\overline{\mathbf Q}_\ell\oplus\mathcal L_\varepsilon.
\tag{DBC.8.1}
\]
Thus every local factor, with all degrees retained, yields
\[
\zeta_{Y_0}(s)=\zeta_{X_0}(s)L(\varepsilon,s).
\tag{DBC.8.2}
\]
Explicitly, at a point of degree \(d\), a split fibre contributes \((1-t^d)^{-2}\), equal to \((1-t^d)^{-1}(1-t^d)^{-1}\); an inert fibre contributes \((1-t^{2d})^{-1}\), equal to \((1-t^d)^{-1}(1+t^d)^{-1}\). These are respectively \(\varepsilon(F_v)=1\) and \(-1\).

Section 7 shows that both zeta functions in (DBC.8.2) have a simple pole at \(s=1\), in both geometric cases. Therefore their quotient \(L(\varepsilon,s)\) has order zero at \(s=1\), and its value there is finite and nonzero. This excludes the exceptional zero. In the constant-field case the unreduced top factor is \(1-q^2t^2=(1-qt)(1+qt)\); the extra factor is nonzero at \(t=q^{-1}\), which displays the same conclusion directly at the denominator level.

We have obtained condition (C): \(L(\rho)\) is meromorphic for \(\Re(\rho)\ge1\), has exactly the permitted simple pole at \(\omega_1\), and has no zeros on the boundary. Its Euler product supplies nonvanishing in the interior \(\Re(\rho)>1\).

## DBC9. Strict bound with the original weight \(\beta\)

Let \(X_0\) be a smooth geometrically connected curve, and let the original lisse sheaf \(\mathcal F_0\ne0\) be irreducible and pointwise \(\iota\)-pure of weight \(\beta\). The restriction of its Weil representation to the geometric fundamental group is semisimple: choose a nonzero simple geometric submodule; the sum of all simple geometric submodules is nonzero and invariant under the Weil group because the geometric group is normal. Irreducibility makes that sum the whole representation. Therefore §2.2.5 applies to the monodromy group of this original sheaf.

Let \(\tau\) be its complex representation. By (DBC.2.4),
\[
\Re(\tau)=-\frac\beta2,
\qquad
\Re(\tau\omega_s)=\Re(s)-\frac\beta2.
\tag{DBC.9.1}
\]
Condition (C) therefore controls the original L-function in the original variable \(s\) on
\[
\Re(s)\ge1+\frac\beta2.
\tag{DBC.9.2}
\]
No sheaf of weight zero is substituted here. The corresponding closed disc in \(t=q^{-s}\) is
\[
|t|\le q^{-1-\beta/2}.
\tag{DBC.9.3}
\]
Euler convergence controls its interior. Condition (C) controls its boundary, with the exceptional pole only when \(\tau\omega_s=\omega_1\).

**Case 1: the original representation is nontrivial geometrically.** Equations (DBC.6.2)–(DBC.6.3) give
\[
L(\tau,s)=P_1(q^{-s}),\qquad P_0=P_2=1.
\]
There is no pole of the permitted type, since twisting by degree never changes the geometric restriction. Thus \(P_1(t)\ne0\) throughout (DBC.9.3), including the boundary.

**Case 2: the original representation is geometrically trivial.** Irreducibility forces rank one. Let its degree-one Frobenius scalar be \(c\in\overline{\mathbf Q}_\ell^*\), and put \(a=\iota c\). Its original weight gives
\[
|a|=q^{\beta/2}.
\tag{DBC.9.4}
\]
Keep both cohomological factors:
\[
L(\tau,s)=
\frac{P_1(q^{-s})}
 {(1-aq^{-s})^\delta(1-qa q^{-s})}.
\tag{DBC.9.5}
\]
The \(H_c^0\) root \(a^{-1}\), when \(\delta=1\), has radius \(q^{-\beta/2}\), strictly outside (DBC.9.3). The \(H_c^2\) root
\[
t_*=(qa)^{-1}
\tag{DBC.9.6}
\]
lies on the boundary. It is the exact parameter \(\tau\omega_s=\omega_1\). At \(t_*\),
\[
1-a t_*=1-q^{-1}\ne0,
\qquad
\operatorname{ord}_{t_*}(1-qa t)=1.
\]
Condition (C) says that the L-function has a pole of order exactly one there. Therefore
\[
\operatorname{ord}_{t_*}P_1
=\operatorname{ord}_{t_*}L
 +\delta\operatorname{ord}_{t_*}(1-at)
 +\operatorname{ord}_{t_*}(1-qa t)
=-1+0+1=0.
\tag{DBC.9.7}
\]
This proves \(P_1(t_*)\ne0\); no eigenvalue has been hidden by cancellation. At every other point of (DBC.9.3), the denominator is nonzero and the L-function is nonzero, so \(P_1\ne0\) there as well.

Now every Frobenius eigenvalue \(\alpha\) on the original \(H_c^1(X,\mathcal F)\) contributes the zero \(t=(\iota\alpha)^{-1}\) to \(P_1\), with its full algebraic multiplicity. The absence of such zeros in (DBC.9.3) gives
\[
|\iota\alpha|<q^{1+\beta/2},
\qquad
\boxed{w_q(\alpha)<\beta+2}.
\tag{DBC.9.8}
\]
The strict inequality comes from the boundary nonvanishing and the exact pole-order calculation (DBC.9.7), in addition to Euler convergence in the interior.

## DBC10. Exact passage to a general pure lisse sheaf and smooth curve

For an exact sequence of lisse Weil sheaves
\[
0\longrightarrow\mathcal F'_0\longrightarrow\mathcal F_0
\longrightarrow\mathcal F''_0\longrightarrow0
\]
whose middle sheaf has pointwise weight \(\beta\), both nonzero outer sheaves have the same pointwise weight: every local Frobenius matrix is block triangular, so its characteristic polynomial is the product of the two outer characteristic polynomials. The long exact sequence gives
\[
H_c^1(X,\mathcal F')\xrightarrow{u}H_c^1(X,\mathcal F)
\xrightarrow{v}H_c^1(X,\mathcal F''),\qquad\ker v=\operatorname{im}u.
\]
Both maps commute with Frobenius. The middle vector space is an extension of \(\operatorname{im}u\), a quotient of the first group, by \(\operatorname{im}v\), a subspace of the third group. Its Frobenius eigenvalues, with multiplicities, are the union of those of those two images and therefore occur among the outer groups’ eigenvalues. A finite composition series and (DBC.9.8) prove the same strict bound for the original \(\mathcal F_0\), including nonsplit extensions. The zero sheaf has empty spectrum.

Finally, a smooth curve of finite type may have several geometric connected components. Choose \(n>0\) so that \(F^n\) fixes each such component and it is defined as a geometrically connected curve over \(\mathbf F_{q^n}\). Compactly supported cohomology decomposes as the direct sum over these open-and-closed components, with projection and inclusion maps induced by the corresponding inclusions. On each component the previous argument gives
\[
2\log_{q^n}|\iota(\alpha^n)|<\beta+2
\]
for every eigenvalue of \(F^n\) arising from an eigenvalue \(\alpha\) of the original \(F\). The original and extended-field weights agree exactly:
\[
2\log_{q^n}|\iota(\alpha^n)|
=\frac{2n\log|\iota\alpha|}{n\log q}
=w_q(\alpha).
\tag{DBC.10.1}
\]
The pullback sheaf retains pointwise weight \(\beta\): if a closed point of original degree \(d\) has a point above it of degree \(d'=d/\gcd(d,n)\) over \(\mathbf F_{q^n}\), its Frobenius is the power \(n/\gcd(d,n)\) of the original local Frobenius, and the absolute-value equality becomes
\[
(q^{d\beta/2})^{n/\gcd(d,n)}
=(q^n)^{d'\beta/2}.
\tag{DBC.10.2}
\]
Equations (DBC.10.1)–(DBC.10.2), together with the direct-sum maps, prove Deligne’s strict bound for the original smooth curve and original sheaf in full generality as stated in §2.2.10.

The optional covering step mentioned in source line 1925 also has an exact map. For a finite étale cover \(f:Y_0\to X_0\) of constant degree \(e>0\), the adjunction and trace maps are
\[
\mathcal F_0\xrightarrow{\eta}f_*f^*\mathcal F_0
\xrightarrow{\operatorname{Tr}_f}\mathcal F_0,
\qquad\operatorname{Tr}_f\eta=e\,\operatorname{id}_{\mathcal F_0}.
\tag{DBC.10.3}
\]
On an étale-trivializing neighbourhood the first map is the diagonal into \(e\) copies and the second is their sum, proving the formula. Because \(f\) is finite, compactly supported cohomology identifies the middle sheaf’s cohomology with \(H_c^i(Y,f^*\mathcal F)\). Consequently \(f^*\) is an injective Frobenius-equivariant map on cohomology, with left inverse \(e^{-1}\operatorname{Tr}_f\). The integer \(e\) is invertible in \(\overline{\mathbf Q}_\ell\), including when \(\ell\mid e\).

For the group in §3, the subgroup \(G^{00}\langle z\rangle\) has finite index and is isomorphic to \(G^{00}\times\mathbf Z\), with the second generator mapping to the original degree \(m\), not degree one in the original \(\mathbf Z\). Its preimage in the Weil group corresponds to a finite étale cover, with an accompanying finite constant-field extension if needed to make the new degree map surjective. This justifies the optional direct-product presentation while recording its cohomological injection and its changed degree generator. The proof of (DBC.9.8) above already works in the original extension and does not require this optional step.

## DBC11. Review record

Completed calculations: compact conjugacy with the central degree coordinate; categorical extension with arbitrary degree Jordan blocks; exact mixed-to-pure dependency through §1.8.11; finite-kernel compactness proof with all auxiliary twist factors and inverses; the negative sign of the representation weight; the complete trace denominator; a noncircular proof of the simple curve-zeta pole; both geometric types of connected quadratic cover; and the original-\(\beta\) strict bound with exact cancellation orders, extensions, and field-change factors.

The parent’s upstream derivations supply §1.3; DB3–DB6 above prove the analytic theorem §2.1.4. The compact-form and strict-bound derivation has not used the later stronger bound \(w_q(\alpha)\le\beta+1\) or the Riemann hypothesis for curves. DB9 contains the separate exact original-zeta boundary calculation. Source-reading coverage is the bounded coverage in DB0 and DBC1; source discovery, PDF reading, rendering, and publication were outside this subtask.
