# The full Gram projection and its resonance return

25 September 2026. Complete derivation FGR0–FGR7. This calculation concerns the complex receiving coefficients of the original programme. It introduces no addition, counting, parity or numerical weight on primitive \(Z_1/\tau\). The original \(Z_0,Z_1,Z_2\) distinctions and the retraction of the tau self-sum remain in force.

## FGR0. Source, purpose, and exact scope

Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, math/9811068v1](https://arxiv.org/abs/math/9811068v1), §VIII, Lemma 3 and equation (29), obtains harmonic measures as cutoff traces of zero constraints. The original author TeX, [math_9811068v1_author.tex](https://arxiv.org/abs/math/9811068v1), lines 2687–2715, sketches the finite constraint calculation. The sentence asserting asymptotic orthogonality of the individual exponential vectors requires correction: distinct exponents on the same side generally have nonzero limiting inner product. The full Gram inverse, including its off-diagonal entries, repairs that step. The harmonic-measure conclusion survives this correction.

We prove the continuous-window calculation, with all zero multiplicities, for any finite subset of the actual nontrivial zeros of the original \(\zeta\). No off-critical zero is asserted to exist. Every operator below is defined before its trace is taken. This result identifies the exact finite-constraint limit; it does not identify these finite projections with the original full adelic cutoff. In particular, we do not interchange an exhaustion of all zeros with the window limit.

The programme's original objects are \(A,J=\Sigma S,Q=A/J\), and

\[
 M_0b(s)=\int_0^\infty b(u)u^s\frac{du}{u}.
\]

Here \(S\) is the even Schwartz space with \(h(0)=\int h=0\), \(\Sigma h(u)=2\sum_{n\geq1}h(nu)\), and \(A\) consists of smooth functions decreasing with all Euler derivatives faster than every power at both endpoints. The original Mellin image of \(J\) is the ideal of all full nontrivial-zero jets. These previously proved objects remain the inputs. FGR1–FGR6 do not replace \(\zeta\) by a completed function.

## FGR1. Window, original Mellin jets, and complete projection

Let \(\Omega\) be a finite set of distinct actual nontrivial zeros \(\rho=\beta+i\gamma\), each with its full multiplicity \(m_\rho\). Put \(z_\rho=\rho-1/2\) only as a displayed coordinate difference; every formula retains \(\rho\) as the original zero. Set \(M=\sum_{\rho\in\Omega}m_\rho\).

For \(T>0\), let \(\mathscr H_T=L^2([-T,T],dx)\), included in \(L^2(\mathbb R,dx)\) by extension by zero. The exact change of variables

\[
 \xi(x)=e^{x/2}b(e^x),\qquad
 M_0b(s)=\int_{\mathbb R}\xi(x)e^{(s-1/2)x}\,dx
\tag{FGR1.1}
\]

retains the original Mellin parameter and multiplier. The sharp window belongs to a larger measurable receiving space: its inverse is \(b(u)=u^{-1/2}\xi(\log u)\), supported in \([e^{-T},e^T]\). Such a function is not asserted to belong to the original smooth \(A\). Its compactly supported Mellin integral is entire by Cauchy–Schwarz on the finite interval, which supplies the operation prerequisites. For window functions its \(j\)-th Mellin derivative at \(\rho\) is

\[
 \ell_{\rho,j,T}(\xi)=\int_{-T}^T \xi(x)x^j e^{z_\rho x}\,dx,
 \qquad 0\leq j<m_\rho.
\tag{FGR1.2}
\]

Use the inner product conjugate linear in the first argument. The Riesz vector is

Publication source credit: Hilbert duality is the classical Riesz representation theorem. See Terence Tao, [245B, Notes5, Theorem1 and Remark2](https://terrytao.wordpress.com/2009/01/17/254a-notes-5-hilbert-spaces/) (17 January2009); the theorem and its proof were checked. The present argument retains its stated conjugation and inner-product conventions.

\[
 v_{\rho,j,T}(x)=1_{[-T,T]}(x)x^j e^{\overline{z_\rho}x}.
\]

Let \(V_T:\mathbb C^M\to L^2(\mathbb R)\) have precisely these columns, and let \(G_T=V_T^*V_T\). Its entries are the full integrals

\[
 (G_T)_{(\rho,i),(\eta,j)}
 =\int_{-T}^T x^{i+j}e^{(z_\rho+\overline{z_\eta})x}\,dx.
\tag{FGR1.3}
\]

These columns are independent. Indeed, a vanishing linear combination is an exponential polynomial vanishing on an interval, hence everywhere by analyticity. Applying the constant-coefficient differential operators \(\prod_{\eta\ne\rho}(\partial_x-\overline{z_\eta})^{m_\eta}\) isolates a polynomial times \(e^{\overline{z_\rho}x}\). On polynomials the remaining factors \(\partial_x+\overline{z_\rho}-\overline{z_\eta}\) are invertible because their nonzero constant terms make their matrices triangular with nonzero diagonal. Thus each isolated polynomial vanishes, and so do all coefficients.

Consequently \(G_T\) is positive definite and

\[
 P_{\Omega,T}=V_TG_T^{-1}V_T^*
\tag{FGR1.4}
\]

is the orthogonal projection onto the full constraint space. It has rank \(M\). Its orthogonal complement in \(\mathscr H_T\) is exactly the joint kernel of (FGR1.2). This follows directly by multiplication of the matrices in (FGR1.4): the result is self-adjoint, idempotent, identity on the range of \(V_T\), and zero on its orthogonal complement.

Let \((V(t)\xi)(x)=\xi(x-t)\). This is unitary on \(L^2(\mathbb R)\), although its compression to a fixed window need not be. The finite-rank trace is exactly

\[
 \operatorname{Tr}(P_{\Omega,T}V(t))
 =\operatorname{tr}_{\mathbb C^M}
 \left(G_T^{-1}V_T^*V(t)V_T\right).
\tag{FGR1.5}
\]

The capital trace is an operator trace and the lower-case trace is a finite matrix trace. Their equality follows by writing both finite-rank products as sums of rank-one operators. Every Gram cross term remains present.

## FGR2. The right endpoint and its nonorthogonal limit

For \(\beta>1/2\), replace the column basis, within exactly the same span, by

\[
 w^+_{\rho,j,T}(x)=1_{[-T,T]}(x)(T-x)^j
                         e^{-\overline{z_\rho}(T-x)}.
\tag{FGR2.1}
\]

Expansion of \((T-x)^j\) gives a triangular change of basis with diagonal \((-1)^j e^{-\overline{z_\rho}T}\ne0\). Under \(y=T-x\), these are truncations to \([0,2T]\) of

\[
 w^+_{\rho,j}(y)=y^j e^{-\overline{z_\rho}y},\quad y\geq0.
\]

They converge in \(L^2(\mathbb R_+)\). The full limiting Gram matrix is

\[
 G^+_{(\rho,i),(\eta,j)}
 =\frac{(i+j)!}{(z_\rho+\overline{z_\eta})^{i+j+1}}.
\tag{FGR2.2}
\]

The identity follows by \(i+j\) integrations by parts in the exponential integral; its boundary terms vanish since both real parts are positive. The same independence proof as FGR1 makes \(G^+\) positive definite.

For distinct simple exponents, the unit-vector inner product tends to

\[
 \frac{2\sqrt{(\beta_\rho-1/2)(\beta_\eta-1/2)}}
 {z_\rho+\overline{z_\eta}},
\tag{FGR2.3}
\]

which is nonzero. Thus individual asymptotic orthogonality is not the reason the trace becomes a sum.

For comparison with the discrete statement in Connes, take the two abstract exponents \(z=2,w=3\), not proposed zeta zeros. The unit vectors proportional to \(2^n,3^n\), \(-N\leq n\leq N\), have limiting inner product \(\sqrt{(4-1)(9-1)}/(6-1)=\sqrt{24}/5\). This follows by summing the three geometric series. It directly tests the finite-exponential assertion, without changing any programme source object.

## FGR3. The left endpoint and the critical blocks

For \(\beta<1/2\), use

\[
 w^-_{\rho,j,T}(x)=1_{[-T,T]}(x)(T+x)^j
                              e^{\overline{z_\rho}(T+x)}.
\tag{FGR3.1}
\]

This is another invertible triangular change of the original jet columns. In \(y=T+x\), its limit is \(y^je^{\overline{z_\rho}y}\). The complete positive-definite Gram matrix is

\[
 G^-_{(\rho,i),(\eta,j)}
 =\frac{(i+j)!}{(-z_\rho-\overline{z_\eta})^{i+j+1}}.
\tag{FGR3.2}
\]

For each \(\beta=1/2\), choose real orthonormal polynomials \(p_j\), of degree \(j\), for the measure \(dr/2\) on \([-1,1]\). Their existence follows by Gram–Schmidt on \(1,r,r^2,\ldots\); positivity follows because a nonzero polynomial cannot vanish on an interval. Replace the jet basis for that \(\gamma\) by

\[
 w^0_{\gamma,j,T}(x)=(2T)^{-1/2}1_{[-T,T]}(x)
                                  p_j(x/T)e^{-i\gamma x}.
\tag{FGR3.3}
\]

Again the span is unchanged. The Gram matrix for equal \(\gamma\) is identity. For unequal \(\gamma,\gamma'\), integration by parts in
\(\tfrac12\int_{-1}^1p_i(r)p_j(r)e^{i(\gamma-\gamma')Tr}dr\)
gives \(O(T^{-1})\).

All other mixed Gram entries vanish in the limit. For a right-end vector and a critical vector, the absolute value is at most \(C T^{-1/2}\int_0^{2T}y^j e^{-(\beta-1/2)y}dy\), since the fixed polynomial in (FGR3.3) is bounded on its interval. This is \(O(T^{-1/2})\); the left-end proof is identical. For opposite endpoints, write \(y_++y_-=2T\). Their product is bounded by a polynomial in \(T\) times \(e^{-2T\min(\beta_+-1/2,1/2-\beta_-)}\), and integration adds only another factor \(2T\).

Thus in the displayed, invertibly changed basis the full Gram matrix tends to

\[
 G^+\oplus G^-\oplus\bigoplus_{\rho:\,\beta=1/2} I_{m_\rho}.
\tag{FGR3.4}
\]

Every block is invertible. Its inverse is the limit of the inverse Gram matrices: the identity \(G_T^{-1}-G^{-1}=G_T^{-1}(G-G_T)G^{-1}\), together with the positive smallest eigenvalue of the finite limiting matrix, proves this directly.

## FGR4. Full trace limit, including every nilpotent order

In right-end coordinates, the compression of \(V(t)\) for \(t\geq0\) is the half-line operator \((W(t)w)(y)=w(y+t)\). On the limiting span it acts exactly by

\[
 W(t)w^+_{\rho,j}
 =e^{-\overline{z_\rho}t}
   \sum_{r=0}^j\binom jr t^{j-r}w^+_{\rho,r}.
\tag{FGR4.1}
\]

This invariant subspace is finite dimensional, and its trace is
\(\sum_{\beta>1/2}m_\rho e^{-\overline{z_\rho}t}\).
The complete triangular matrix is retained in (FGR4.1); the nilpotent terms have zero trace by direct inspection of its diagonal. They were not deleted from the space.

For \(t<0\), the compression is the adjoint of \(W(-t)\); its trace is the conjugate trace. The full right-end result is therefore
\(\sum_{\beta>1/2}m_\rho e^{-(\beta-1/2)|t|}e^{i\gamma t}\).
The left-end compression is the backward half-line operator for \(t\leq0\) and its adjoint for \(t>0\), giving
\(\sum_{\beta<1/2}m_\rho e^{-(1/2-\beta)|t|}e^{i\gamma t}\).

These are limits of the exact finite-window matrices, not only formal half-line computations. After translation to an endpoint, the column vectors converge in \(L^2(\mathbb R)\) by extension by zero. Each \(V(t)\) is bounded. Hence all matrix coefficients converge. The Gram inverses converge by FGR3. Opposite-end and critical/end mixed coefficients vanish by the same estimates as FGR3, with a fixed shift of at most \(|t|\).

For each critical column, translation changes the polynomial argument by \(t/T\). On the shared window its squared norm error is \(O(t^2/T^2)\); the lost endpoint intervals contribute \(O(|t|/T)\). Thus

\[
 \|V(t)w^0_{\gamma,j,T}-e^{i\gamma t}w^0_{\gamma,j,T}\|_2\longrightarrow0.
\]

Using (FGR1.5) and the limiting blocks gives the full result

\[
 \boxed{\lim_{T\to\infty}\operatorname{Tr}(P_{\Omega,T}V(t))
 =\sum_{\rho\in\Omega}m_\rho
 e^{-|\beta-1/2|\,|t|}e^{i\gamma t}.}
\tag{FGR4.2}
\]

This proof keeps the complete Gram cross terms and all derivative constraints. It does not require distinct same-side vectors to become orthogonal.

## FGR5. Original arithmetic test, harmonic measure, positivity

For \(b\in A\), define the explicit receiving test

\[
 a_b(t)=e^{t/2}b(e^t),\qquad
 V(a_b)=\int_{\mathbb R}a_b(t)V(t)\,dt.
\tag{FGR5.1}
\]

The function \(a_b\) and every derivative decay faster than every exponential at both ends. In particular the operator integral exists in the strong sense and has norm at most \(\|a_b\|_1\). Since \(P_{\Omega,T}\) has rank \(M\),
\(|\operatorname{Tr}(P_{\Omega,T}V(t))|\leq M\).
Dominated convergence in (FGR4.2) proves

\[
 \lim_{T\to\infty}\operatorname{Tr}(P_{\Omega,T}V(a_b))
 =\sum_{\rho\in\Omega}m_\rho
   \int_{\mathbb R}e^{t/2}b(e^t)
              e^{-|\beta-1/2|\,|t|}e^{i\gamma t}\,dt.
\tag{FGR5.2}
\]

For \(d>0\), elementary contour integration, closing the contour above for \(t>0\) and below for \(t<0\), gives

\[
 \int_{\mathbb R}\frac{d}{\pi(d^2+(y-\gamma)^2)}e^{iyt}\,dy
 =e^{-d|t|}e^{i\gamma t}.
\tag{FGR5.3}
\]

Indeed the upper pole is \(\gamma+id\) and its residue, including the factor \(2\pi i\), is \(e^{i\gamma t-dt}\); the lower pole and clockwise orientation give \(e^{i\gamma t+dt}\). At \(t=0\) direct integration gives 1. Fubini is justified by \(\|a_b\|_1\) and the probability mass of the kernel. Hence each off-critical summand in (FGR5.2) equals

\[
 m_\rho\int_{\mathbb R} M_0b(1/2+iy)
       \frac{|\beta-1/2|}{\pi((\beta-1/2)^2+(y-\gamma)^2)}\,dy.
\tag{FGR5.4}
\]

For \(\beta=1/2\), the term is exactly \(m_\rho M_0b(\rho)\). Every original variable, multiplicity, \(1/2\) factor and Haar conversion is displayed. The shifted coordinate was not substituted for the original zeta function.

For any \(a\in L^1(\mathbb R)\), put \(a^*(t)=\overline{a(-t)}\). The equality \(V(a*a^*)=V(a)V(a)^*\) follows from Fubini and the group law. Its compression has nonnegative finite trace. Thus all the finite-window distributions above are positive on convolution squares. The limiting positive distribution replaces an off-critical Mellin evaluation by (FGR5.4). Proving that it equals the original arithmetic distribution requires checking that exact replacement on the full original source.

## FGR6. How much data the replacement changes

The original contribution of the same zero is

\[
 m_\rho M_0b(\rho)
 =m_\rho\int_{\mathbb R}e^{t/2}b(e^t)
                  e^{(\beta-1/2)t}e^{i\gamma t}\,dt.
\tag{FGR6.1}
\]

Subtracting (FGR5.2) retains the exact finite discrepancy

\[
 \sum_{\rho\in\Omega}m_\rho\int_{\mathbb R}e^{t/2}b(e^t)e^{i\gamma t}
 \left[e^{(\beta-1/2)t}-e^{-|\beta-1/2|\,|t|}\right]dt.
\tag{FGR6.2}
\]

If \(\Omega\) includes the reflected pair \(\beta+i\gamma\), \(1-\beta+i\gamma\), with common multiplicity \(m\) and \(d=|\beta-1/2|>0\), its exact integrand difference is

\[
 2m\,e^{t/2}b(e^t)e^{i\gamma t}\sinh(d|t|).
\tag{FGR6.3}
\]

This follows by retaining both exponential contributions: \(e^{dt}+e^{-dt}-2e^{-d|t|}=2\sinh(d|t|)\). No parity, amount, or numerical scaling is attributed to primitive tau. The change occurs in the receiving trace kernel. The global, absolutely convergent version and its original-ideal test are developed in the accompanying harmonic-sweep calculation.

## FGR7. What this construction allows next

The endpoint concentration is now a calculated operation, including the nonorthogonal Gram entries. All finite original zero-jet constraints produce the positive harmonic trace. The raw arithmetic trace has the additional exact term (FGR6.2). This establishes where the positive cutoff model can change the full source comparison; it does not establish that the change vanishes.

Following the user's instruction to use this finding together with the whole programme, the next calculation is to evaluate the discrepancy on an actual element of \(J=\Sigma S\). Such an element is zero in the original quotient before any Hilbert closure. The companion global derivation uses the already constructed generator \(M_0b_0(s)=(s-1)\zeta(s)e^{s^2}\) and its full reflected convolution square. This is a concrete original-source test of descent, rather than an assumption that cutoff positivity supplies the missing Deligne weight separation.

The result does not settle the active tau lifting theorem. All source endpoint and extra coefficient spaces remain those in the full sheaf comparison; this finite Hilbert calculation neither replaces that sheaf nor removes an arithmetic source point.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
