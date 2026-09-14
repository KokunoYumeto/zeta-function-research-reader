# Arithmetic source-metric transfer inside the original SplitZero quotient

13 September 2026. Starting main: `aea6471ac6cf36f7c5e660d8698dce6b0606196e`. The published reader and its original sources remain unchanged. This contribution continues the original arithmetic calculation, not a verdict about the programme based on an auxiliary example.

## 1. Recovery, attribution, and retained source

The unfinished branch `astra/residue-rigidity-source-20260913` at `eed01119290bcac2f1c690be56ad20a71d929c35` contained eleven unmerged files. Its monic-residue and constituent modules had passed individual strict compilation, but its source-detection module stopped at evaluation of multiplication in `Module.End`. We retain all eleven files and their ancestry, supplying the missing definitional reduction without changing the theorem. The old branch and main are not rewritten.

The written source-path formulas and log-volume slopes below overlap AV1--AV7 in the recovered `../tau-residue-rigidity/ARITHMETIC_VARIATION.md`. Its `ADAPTIVE_VARIATION.md` gives a complementary slope-partition certificate and the residue-coupling derivative. Those contributions are retained with attribution. The new formal contribution consists of exact canonical secants, their source-pencil gap and original quotient transport, and an adaptive SIGNED trace-power certificate. The recovered residue/source proof is completed and checked jointly. General Schur-complement concavity is classical, not a claimed new matrix principle.

The arithmetic source stays

\[
g=2\xi,\quad Q=\mathscr B/\Theta V,\quad
\mathcal MF_h=g/h,\quad
\mathcal V_{h,k}P=P(D_1+\cdots+D_k)F_h^{\otimes k}.
\]

The full Taylor unit and every selected zero order remain in the arithmetic observation. At fixed k,N, the source presentation is

\[
0\longrightarrow\mathcal P_{N-q}\xrightarrow{\times\chi}
\mathcal P_N\xrightarrow{J}E\longrightarrow0.
\]

The source coordinates are the original S=k/2+ix. Its arithmetic and Gamma measures give two positive Gram matrices on this SAME presentation. Gamma is a comparison norm, not a replacement zero packet. Original theta primitives are required when a polynomial relation is taken into the analytic source; equality of finite jets on an arbitrary larger space is not substituted for a primitive.

## 2. Completed residue rigidity and actual source detection

For a monic polynomial h over a field, of degree q>0, E is the literal `AdjoinRoot h`. Define ell as the coefficient of S^(q-1) in the unique monic remainder. For x nonzero, let p be its nonzero remainder, of degree d<q. Then n=q-1-d satisfies 0<=n<q, and S^n p has degree q-1, with unchanged nonzero leading coefficient. Therefore

\[
\ell(S^n x)\ne0.
\]

In particular, the bilinear map beta(x,y)=ell(yx) is nondegenerate: if every beta(x,y) vanishes, the displayed monomial contradicts x nonzero. Finite dimensionality gives the actual isomorphism E -> E^dual. No root enumeration, squarefreeness or discriminant inverse occurs.

Let F be nonzero, proper, and stable under S. Polynomial induction makes it stable under every multiplier in E. It cannot contain 1, because the powers of S generate E. Nor can ell vanish on F: otherwise ell(yx)=0 for every y and x in F, contrary to the proved perfectness. The original insertion R(x)=ell(x)1 therefore has transverse map

\[
\pi_F R\iota_F=(\pi_F1)\otimes\ell_F,
\quad\operatorname{im}=K\pi_F1,
\quad\ker=\ker\ell_F.
\]

Both factors are nonzero; a normalized residue-one vector constructs every scalar in the image. Its rank is exactly one and its kernel has dimension dim(F)-1. Nilpotent and repeated-root directions are retained.

On an original support fibre let B be the original boundary family, J its finite observation and r a section, with Jr=1 and J(B)=0. Then q_B r is injective: equality of two classes puts their representative difference in B; applying J recovers equality of their original packet vectors. No equality B=ker J is assumed.

For the ACTUAL source generator P satisfying JP=S J, induction gives J(P^n r x)=S^n x. The source operation r R J applied to that vector has residue response r(ell(S^n x)1). Its class modulo B is nonzero for some n<q by the preceding detector. A nonbottom support also excludes external absence. This completes the formerly blocked `actual_source_residue_detects` theorem and makes the detecting family live on the original source, not independent coefficient representatives.

This algebraic detection is not an assertion that the detecting scalar lines carry a pure Frobenius action. Its established role is to prevent undetected original packet directions and to supply nonvanishing for the previously written constituent-period curvature calculation.

## 3. Exact canonical section secants in the unchanged relation columns

Let C contain fixed lifts of a quotient basis and B the original relation columns. For a positive Hermitian source form M_a define

\[
H_a=(B^*M_aB)^{-1},\quad Z_a=H_aB^*M_aC,
\quad R_a=C-BZ_a,\quad G_a=R_a^*M_aR_a.
\]

The zero-dimensional relation space is allowed at N=q-1. No earlier inadmissible inverse is introduced. The inherited weighted residual theorem gives B* M_a R_a=0. Hence every J with JB=0 has JR_a=JC. The section difference is the specified old relation

\[
D_{01}=R_1-R_0=B(Z_0-Z_1).
\]

Orthogonality and its conjugate give the full Pythagoras identity

\[
(R_a+BZ)^*M_a(R_a+BZ)=G_a+(BZ)^*M_a(BZ).
\]

Insert the other canonical section into this identity and expand M_1=M_0+(M_1-M_0). This proves both exact secants:

\[
G_1-G_0=R_0^*(M_1-M_0)R_0-D_{01}^*M_1D_{01},
\]
\[
G_1-G_0=R_1^*(M_1-M_0)R_1+D_{01}^*M_0D_{01}.
\]

The opposite signs are essential. Positivity gives two positive-semidefinite remainders but requires no ordering of the two source forms. Freezing the section and dropping its boundary Gram does not give equality.

More generally, if M_t=aM_0+bM_1 and R_t is its canonical section, the same Pythagoras calculation gives

\[
G_t-aG_0-bG_1
=a(R_t-R_0)^*M_0(R_t-R_0)
+b(R_t-R_1)^*M_1(R_t-R_1).
\]

For a,b>=0 this proves a positive-semidefinite gap, hence concavity when a+b=1. The exact identity does not need that normalization. All these finite identities and positivity consequences are in `SplitZeroMetricVariation` and reuse `WeightedQuotientVolume.residual`.

## 4. The source path and its signed density pairing (written scope)

The parameter s in this section is new: it is not the period parameter t, the representative coordinate z, or the Laplace tilt theta. Keep the original endpoint measures and put

\[
m_s=(1-s)m^\Gamma+s m^{\rm ar},\quad
M_s=M_0+sE,\quad E=M_1-M_0,\quad 0\le s\le1.
\]

The intermediate measure is only an explicit comparison path. It is not claimed to be a k-fold convolution of an interpolated one-factor amplitude. Positivity makes the finite matrix functions smooth along this compact path.

Differentiate JR_s=1. Exactness of the original polynomial sequence puts R_s' in im B. Differentiate B* M_s R_s=0 and solve its invertible relation Gram:

\[
R_s'=-B(B^*M_sB)^{-1}B^*ER_s.
\]

Thus the derivative is an original relation with a specified primitive. Orthogonality kills both cross terms in the first Gram derivative:

\[
G_s'=R_s^*ER_s.
\]

Pairing the differentiated normal equation with the coefficient of R_s' gives R_s'^* E R_s=-R_s'^* M_s R_s'. Its adjoint supplies the other term, so

\[
G_s''=-2R_s'^*M_sR_s'\preceq0.
\]

Jacobi differentiation gives

\[
(\log\det G_s)'=\operatorname{tr}(G_s^{-1}R_s^*ER_s),
\]
\[
(\log\det G_s)''
=-2\operatorname{tr}(G_s^{-1}R_s'^*M_sR_s')
-\operatorname{tr}\bigl((G_s^{-1/2}G_s'G_s^{-1/2})^2\bigr)\le0.
\]

Both losses remain; no matrices are presumed to commute. These are the recovered AV formulas, with their full written proofs retained. They are not extra Lean calculus declarations in this push.

For e_N(x)=(1,S,...,S^N), define the actual quotient-evaluation density

\[
\ell_{N,s}(x)=e_N(x)R_sG_s^{-1}R_s^*e_N(x)^*\ge0.
\]

Finite sums and the given source moments prove

\[
\int\ell_{N,s}m_s=q,\qquad
\log T_N=\int_0^1\int(m^{\rm ar}-m^\Gamma)\ell_{N,s}\,dx\,ds,
\quad T_N=V_N^{\rm ar}/V_N^\Gamma.
\]

For i_0=q-1, i_1=q, j_0=2q-1, j_1=2q, let

\[
\kappa_s=\ell_{i_0,s}+\ell_{i_1,s}-\ell_{j_0,s}-\ell_{j_1,s}.
\]

The SIGNED correction is exactly

\[
\mathcal C=\log\frac{T_{i_0}T_{i_1}}{T_{j_0}T_{j_1}}
=\int_0^1\int(m^{\rm ar}-m^\Gamma)\kappa_s\,dx\,ds,
\qquad \int\kappa_s m_s=0.
\]

This identifies the arithmetic correlation, rather than bounding four unsigned quantities independently. Concavity of each term assigns no sign to the four-term contrast. The recovered adaptive slope-partition certificate approximates this integral with correctly oriented upper/lower slopes; its proof and explicit mesh error remain in `ADAPTIVE_VARIATION.md`.

## 5. A terminating SIGNED trace-power certificate

On the same q-dimensional space set

\[
A_N=(G_N^\Gamma)^{-1}G_N^{\rm ar},\qquad\det A_N=T_N.
\]

These operators are positive and self-adjoint in the Gamma metric, not necessarily Euclidean Hermitian. They need not be above or below the identity. Select one common c larger than all four maximal eigenvalues; for instance c=1+sum_N tr(A_N). Put H_N=I-A_N/c. Every eigenvalue of H_N is in [0,1).

The c here is a numerical certificate parameter. No source measure or mass is renormalized. For p>=1 define

\[
s_{N,p}=\operatorname{Re}\operatorname{tr}(H_N^p),\quad
P_{N,p}=\sum_{m=1}^p\frac{\operatorname{Re}\operatorname{tr}(H_N^m)}m,
\]
\[
U_{N,p}=P_{N,p}+rac{P_{N,2p}-P_{N,p}}{1-s_{N,p}}.
\]

The existing `RestrictionSpectrum` theorem proves, when s_(N,p)<1,

\[
P_{N,p}\le-\log\det(I-H_N)\le U_{N,p}.
\]

For completeness, for a scalar eigenvalue x in [0,1), write r_p(x) as the positive tail of -log(1-x). Termwise comparison gives r_(2p)(x)<=x^p r_p(x). Summing and using x_a^p<=sum_b x_b^p gives L-P_(2p)<=s_p(L-P_p). Division by 1-s_p yields the bound. At fixed finite H_N, s_p tends to zero; thus each endpoint has a finite stopping order. No bound uniform in k follows.

The determinant scale is retained first:

\[
\log T_N=q\log c+\log\det(I-H_N).
\]

The four common q log c terms cancel BEFORE the bounds are combined. With separate admitted p_N at the four endpoints this proves

\[
\boxed{P_{j_0}+P_{j_1}-U_{i_0}-U_{i_1}
\le\mathcal C\le
U_{j_0}+U_{j_1}-P_{i_0}-P_{i_1}.}
\]

The expression uses only finite matrix powers, traces, sums and divisions. It does not take a numerical matrix logarithm or require computed eigenvectors to evaluate it. The theorem uses an explicit inverse-coordinate spectral witness, and proves determinant positivity and trace transport through both inverse laws. Existence of that witness from weighted positivity is standard finite-dimensional spectral theory, not a new implemented eigensolver or a theorem about unevaluated arithmetic integrals.

Refining p gives convergent fixed-matrix enclosures. Certified arithmetic entries additionally require their error propagation and a certified positive 1-s_p. Subtracting independently upper-bounded prefixes is not licensed: approximate arithmetic should enclose the positive tail block sum_(m=p+1)^(2p) tr(H^m)/m directly and combine endpoint intervals in the displayed orientations.

## 6. The change remains in the original supported quotient

Let D,E be original diagrams over the same support semilattice and B a stable original relation family. Raw sections r_i need not be natural. The explicit sufficient condition is

\[
D(h)r_i(v)-r_j(E(h)v)\in B_j.
\]

`quotientSection` uses that witness to construct a Hom into the EXISTING `Relations.quotientDiagram`. Its total map is linear over the original G(R). A B-valued change of section preserves this condition; the two total quotient maps are equal. For the canonical metrics, the coefficient primitive Z_0-Z_1 from section 3 proves precisely that original-boundary membership after the specified source-coordinate equivalence.

A boundary maps to its own fibre zero. At a nonbottom support that image is not external absence. The infinite theta quotient and any larger finite-observation kernel stay distinct. Source sections and residue insertions are not declared natural across packets without the original two transport-error witnesses. No scalar, relation quotient, support transport, arithmetic action, or period-coordinate metric is redefined.

## 7. Execution and limitations

The final observed execution record belongs in STATUS.md and the PR. The runner compiles six modules and their complete used local SplitZero dependency closure with strict kernel flags, then prints and checks all selected transitive axioms in one import environment. It reuses the inherited fail-closed checker and pins. Counts include definitions and interface lemmas, not discoveries.

The new exact checker uses polynomial source moments in S=1/2+ix from a Gaussian of literal mass seven with weights 1,1+x^2,1+2x^2. It keeps the same quotient `(S-1/2)^2+1`, including the first admitted degree with no relation columns. It tests both secants, the pencil gap, symbolic first/second variations, log-curvature terms, actual old-relation corrections, and adaptive signed bounds in both orientations and at equality. The recovered ten-method residue and three-method slope/coupling suites are replayed unchanged. Deliberately false boundary-loss, signed-log, transverse-rank and derivative-sign formulas must fail. These are finite calibrations, not actual zero packets or arithmetic integral enclosures.

The exact next arithmetic obligation is to bound the signed density contrast or the signed certificate on the original growing packets. A generic auxiliary-purity counterexample is a useful regression, not a categorical impossibility result. Conversely, none of the present finite computations is relabelled as a uniform arithmetic upper estimate.

## References

Boyd, S., & Vandenberghe, L. (2004). *Convex optimization*. Cambridge University Press. Official author site: https://web.stanford.edu/~boyd/cvxbook/ . Standard background for the matrix-fractional and log-determinant mechanisms, not a source for the programme-specific arithmetic assumptions.

Repository sources: current main at the pinned commit; the original `SplitZeroWeightedQuotientVolume`, `SplitZeroInternalQuotient`, `SplitZeroSourcePresentation`, `SplitZeroRestrictionLogCertificate`, and `SplitZeroRestrictionSpectrum`; and the complete recovered residue-rigidity branch at its pinned original head. The user's supplied Deligne-bound audit specifies the signed arithmetic/Gamma target. None of its auxiliary Gamma polynomials is asserted to divide 2xi.
