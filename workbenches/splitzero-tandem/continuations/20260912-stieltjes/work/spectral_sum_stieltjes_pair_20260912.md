# Symmetric spectral-sum Stieltjes continuation — 12 September 2026

Status: completed full proof fragment, independently reviewed, ready for parent integration. The entire theorem/proof source is copied below.

The new fragment is **output/split_zero_rh_tandem_2026-09-12/tex/spectral_sum_stieltjes_pair.tex**, label **sec:spectral-sum-stieltjes-pair**, SHA256 **54fcf2d61bb2fdd70f3c76ac3b5cf6450d225b9b5bd7991a3c84b29c33c50844**.

## Exact source provenance

Read the complete PR17 **Spectral-sum descent with the relative arithmetic fibre retained**, all seven sections: pushforward resolution, invariant relation algebra, matrix weight, source metric congruences, full local ladders, and the explicitly separate Gaussian calibration.

The exact witness is **output/split_zero_rh_tandem_2026-09-12/sources/web_pr17_spectral_sum/workbenches/tau-spectral-sum/RESEARCH_NOTE.md**. Its revision is **33b29f706008124886614ba4bd55bffc489df9e2**, while its file SHA256 is **551e3fe89b4409d5ed1eeacfaac4cb7d9c1291978127de1b4f989b272bd24a47**. Both distinct identifiers match its PROVENANCE.json. The file has 12,739 bytes.

The one-factor source is the complete **theta_stieltjes_pair.tex**, separately audited at SHA256 **3695e48f9aa13b9197548ab845998ddb69a4299dbebcf23947f20e211369ac4c**. That full review is **work/theta_stieltjes_pair_review_20260912.md**.

Parent requested the full symmetric-square Stieltjes continuation, retaining \(x=-Z^2\), the factor \(x\) in the even relation ideal and in \(\alpha\), unequal parity dimensions, every relative direction, original source constants, full units and nilpotents, and exact minimum/weight congruences. Parent additionally requested both defects be identified with the original \(A_H\), including the \(V^2\) unit action. These tasks are completed in the proof source below. No earlier or frozen mathematical source or PDF was edited.

## Full result inventory

There are three complete theorem proofs, plus the fully written Hilbert, coordinate, unit, primitive and support calculations. Tags are SSP.1–SSP.37 and SSP.15a.

- SSP.1–SSP.10 prove the original substitutions, coefficient sums with every power \(4^{-j}\), invariant algebra, both coefficient ideals, their full multiplication, and dimensions \(D(D+1),D^2\).
- SSP.11–SSP.15 prove both module exact sequences with the original \(A_H\). Injectivity of \(\alpha\) is proved without inverting \(x\) in either quotient. The coprimality needed for the kernel map is proved from finite dimension of \(B_o\), using univariate annihilators of both variables. The complete kernel and cokernel of multiplication by \(S-1\) are also specified.
- SSP.15a gives the full inherited ideal product under the module identification: \(q\star t=2(-1)^D x_hH'(x_h)qt\bmod H\). The proof retains the full \(Q_\Delta=\Delta A_1\) before multiplying; premature coefficient evaluation is explicitly excluded by the proved map.
- SSP.16–SSP.22 retain every double Taylor coefficient of the original product unit, prove its \(V(x_h)^2\) action on both defects, and give explicit unscaled orbit-coordinate matrices with every diagonal orbit factor one or two retained.
- SSP.23–SSP.30 prove the actual matrix pushforward with both \(1/(2\pi)\) factors, the real Jacobian \(1/2\), all signs from \(\Delta=-v^2\), the half-line Jacobian, the full vector-valued inverse and unbounded multiplication domain, and both degree bounds for every relative direction.
- SSP.31–SSP.35 specify source Grams and full-jet kernel columns, prove positivity and surjectivity at \(M=4D-2\), identify the original minimum and its full determinant/generator congruences, and prove the rectangular weight formula. Its forced and additional zero multiplicities are \(D+2(D^2-p)\).
- SSP.36 retains the original symmetric repeated eigenline and its exact factor \(4|\Re\rho-1/2|\).
- SSP.37 and its proof retain both original cochain primitives, their signs, and their degree bounds by monic ordered division and swap averaging. The final paragraph gives algebra lifts and fixed-label linear lifts with their distinct exact types and receiving supported zeros.

Every one of these mathematical claims is fully articulated and proved in the copied source below. No numerical fixture replaces the actual arithmetic source and no location or multiplicity of an actual zero is assumed.

## Independent audit and executable checks

Two independent lanes read the entire source. The full primary review is **work/spectral_sum_stieltjes_pair_independent_review_20260912.md**. The second full algebra/source/checker audit is **work/symmetric_parity_formula_audit_20260912.md**, SHA256 **969ce848145b8581c0ef2942aaecc8f8e6b7799a01e705fae23427488e451a12**; its final review covers the source hash above, all SSP.1–37 and SSP.15a, SP dependencies, and the final norm wording and primitive proof changes. Both report no outstanding mathematical correction.

The separate checker lane owns **scripts/check_spectral_sum_stieltjes_pair.py** and **checks/spectral_sum_stieltjes_pair_report.md** under the cumulative output directory. Its final reported result is 644 successful records: 583 exact checks and 61 expected mathematical negative controls. Normal and optimized Python runs produce identical record arrays. The injected harness negative fails its 645th record in both modes, with the four process exits \(0,0,1,1\). All four receipts identify the final source hash above. The proof audit also inspected that checker and its receipts.

Those fixtures cover exact unscaled Sym² coordinates, full polynomial quotient carriers, repeated/simple/central examples, the exact \(A_H\) maps and \(V^2\) action, inherited product, source primitives, and the declared Gaussian matrix-weight calibration. Their stated scope remains calibration and implementation verification; the analytic proof is the actual-source proof below.

## Isolated compiler and visual review

A separate XeLaTeX wrapper with the current cumulative preamble renders the fragment to eight pages under **work/spectral_sum_stieltjes_review_20260912**. Compilation succeeds. It reports zero overfull boxes, missing characters, or undefined references.

The isolated wrapper supplies a display-only prerequisite reference to SP. Its absent hyperlink target produces one expected hyperref warning; the cumulative document includes the real SP section. One underfull paragraph warning has no visible overlap or clipping. These isolated wrapper details are recorded rather than concealed.

All eight final Poppler pages at 105 DPI were viewed through the image tool. The shortened title fits, the two exact sequences and unequal blocks fit, and no overlapping text, clipped formula, missing glyph or equation-tag collision was found. The compiler/visual receipt is **work/spectral_sum_stieltjes_review_20260912/verification_receipt.json**. Parent owns the combined paper's subsequent compilation and visual QA.

## Full proof source

The following fenced text copies the complete final fragment, including every theorem and proof.
```tex
\section{The symmetric spectral sum and its unequal Stieltjes pair}
\label{sec:spectral-sum-stieltjes-pair}

The complete PR~17 note, \emph{Spectral-sum descent with the relative
arithmetic fibre retained}, supplies the invariant relation ideal and
the original matrix weight used below.  We prove their further
reflection decomposition, its full paired-packet defect, and the
minimum-metric and weight formulas.  The coordinate \(x\) in this
section belongs to the spectral sum.  We write \(x_h\) for the
one-factor coordinate of Section~\ref{sec:theta-stieltjes-pair};
their exact relation on the defect will be proved.

\subsection{Original polynomial coordinates and the reflection ideals}

Keep \(g=2\xi\), the same nonempty quartet-closed packet \(h\) with
every full order, \(d=2D\), and
\[
 h(s)=(-1)^D H(-(s-\tfrac12)^2),\qquad
 A_H=\mathbb C[x_h]/(H),\qquad v_h=g/h,\qquad
 \upsilon=j_hv_h.
 \tag{SSP.1}
\]
In particular \(D\ge1\) and \(H(0)\ne0\), as proved in (SP.1)--(SP.3).
Write
\[
 \begin{gathered}
 S=s_1+s_2,\quad r=s_1-s_2,\quad \Delta=r^2,\quad
 Z=S-1,\quad x=-Z^2,\\
 s_1=\tfrac12+(Z+r)/2,\qquad s_2=\tfrac12+(Z-r)/2.
 \end{gathered}                                                    \tag{SSP.2}
\]
The swap fixes \(S\) and negates \(r\).  Thus substitution gives a
filtered algebra isomorphism
\(\mathbb C[S,\Delta]\to\mathbb C[s_1,s_2]^{S_2}\), with
\(\deg S=1,\deg\Delta=2\): expansion in \(r\) keeps precisely its
even powers, and the inverse coordinate map in (SSP.2) keeps
the factors \(1/2\).

Write \(h(1/2+y)=\sum_{j=0}^D b_jy^{2j}\), with \(b_D=1\).
Define the following entire finite polynomials:
\[
 \begin{aligned}
 A_0(x,\Delta)
 &=\sum_{j=0}^D b_j4^{-j}
       \sum_{\ell=0}^j\binom{2j}{2\ell}(-x)^{j-\ell}\Delta^\ell,\\
 A_1(x,\Delta)
 &=\sum_{j=1}^D b_j4^{-j}
       \sum_{\ell=0}^{j-1}\binom{2j}{2\ell+1}
                         (-x)^{j-\ell-1}\Delta^\ell,\qquad
 Q_\Delta=\Delta A_1.
 \end{aligned}                                                    \tag{SSP.3}
\]
Binomial expansion, with \(x=-Z^2\), proves exactly
\[
 \begin{aligned}
 h(s_1)&=A_0+rZA_1,& h(s_2)&=A_0-rZA_1,\\
 A_0(0,\Delta)&=(-1)^DH(-\Delta/4),&
 A_1(0,\Delta)&=\frac{(-1)^{D+1}}2H'(-\Delta/4).
 \end{aligned}                                                    \tag{SSP.4}
\]
For the last identity one can also differentiate the difference
\(h(1/2+(Z+r)/2)-h(1/2+(Z-r)/2)\) at \(Z=0\), and divide
by \(2r\); both sides are polynomials, so the identity includes
\(r=0\).  The polynomial \(A_0(0,\Delta)\) has degree \(D\)
and leading coefficient \(4^{-D}\).  No localization at \(r\),
\(\Delta\), \(Z\), or \(x\) has been made.

\begin{theorem}[The original symmetric algebra with both parity modules]
Let \(\mathcal E=(E_h\otimes E_h)^{S_2}\), \(E_h=\mathbb C[s]/(h)\).
There is an exact algebra isomorphism
\[
 \mathcal E\cong
 \mathbb C[x,Z,\Delta]/(Z^2+x,A_0,ZQ_\Delta).
 \tag{SSP.5}
\]
Put
\[
 B_e=\mathbb C[x,\Delta]/(A_0,xQ_\Delta),\qquad
 B_o=\mathbb C[x,\Delta]/(A_0,Q_\Delta).
 \tag{SSP.6}
\]
The underlying module of (SSP.5) is \(B_e\oplus ZB_o\).
The two maps and the product are
\[
 \begin{gathered}
 \beta:B_e\to B_o,\quad[a]\mapsto[a],\qquad
 \alpha:B_o\to B_e,\quad[b]\mapsto[xb],\\
 (a,b)(c,e)=\bigl(ac-\alpha(be),\,\beta(a)e+\beta(c)b\bigr),\\
 \alpha\beta=xI_{B_e},\qquad \beta\alpha=xI_{B_o}.
 \end{gathered}                                                    \tag{SSP.7}
\]
The map \(\beta\) is a unital algebra homomorphism; \(\alpha\) is
a homomorphism of \(\mathbb C[x,\Delta]\)-modules.  Its full
multiplicative relation is
\(\alpha(b)\alpha(c)=x\alpha(bc)\), and \(\alpha(1)=x\).
Reflection in both original variables acts as \((a,b)\mapsto(a,-b)\).
The dimensions are
\[
 \dim B_e=D(D+1),\qquad \dim B_o=D^2.
 \tag{SSP.8}
\]
\end{theorem}
\begin{proof}
In the polynomial algebra \(\mathbb C[S,r]\), the original ideal
\((h(s_1),h(s_2))\) is \((H_0,rH_1)\), where
\(H_0=A_0(-Z^2,\Delta)\) and \(H_1=ZA_1(-Z^2,\Delta)\).
The factors \(1/2\) in the sum and difference of the original
generators give both ideal containments.  An invariant polynomial
in this ideal can be written \(H_0a+rH_1b\).
Average this expression under \(r\mapsto-r\).  The result is
\(H_0a_e+\Delta H_1b_o\), where
\(a_e\) and \(b_o\) are polynomials in \(S,\Delta\);
the odd part of \(b\) is \(rb_o\).
Conversely both invariant generators lie in the original ideal.
Every invariant class in the quotient has an invariant lift by
this same averaging.  Therefore
\[
 \mathcal E\cong\mathbb C[S,\Delta]/(H_0,\Delta H_1).
 \tag{SSP.9}
\]
Replace \(S\) by \(1+Z\) and adjoin \(x=-Z^2\); this proves (SSP.5)
with inverse given by the original substitutions.

Before imposing \(A_0,ZQ_\Delta\), division by \(Z^2+x\)
gives the free module \(\mathbb C[x,\Delta]\oplus
Z\mathbb C[x,\Delta]\).  Multiplying the two remaining generators
by arbitrary elements gives
\[
 A_0(a+Zb)+ZQ_\Delta(c+Ze)
   =A_0a-xQ_\Delta e+Z(A_0b+Q_\Delta c).
 \tag{SSP.10}
\]
Its even and odd coefficient ideals are precisely those in
(SSP.6).  This proves the module decomposition, including both
directions of its defining relations.  Multiplication by \(Z\)
is \((a,b)\mapsto(-\alpha b,\beta a)\), so direct multiplication
proves (SSP.7) and the two compositions.  All operations are
well-defined by the displayed ideals.

Reflection sends \(Z,r\) to \(-Z,-r\), and fixes \(x,\Delta\).
The one-factor decomposition (SP.4) has reflection spaces
of dimensions \(D,D\).  On the invariant tensor square the
positive space is the sum of their two symmetric squares,
with dimension \(2D(D+1)/2\).  The negative space consists
of their mixed symmetrized tensors, with dimension \(D^2\).
They are exactly the even and odd coefficient modules in
(SSP.10), proving (SSP.8), including \(D=1\).
\end{proof}

\subsection{The entire defect is the original paired packet}

\begin{theorem}[Two exact sequences with every original local order]
The map \(\alpha\) is injective and \(\beta\) is surjective.
Regard \(A_H\) as a \(\mathbb C[x,\Delta]\)-module through
\(x\mapsto0,\ \Delta\mapsto-4x_h\).  The two exact sequences
of modules are
\[
 \begin{aligned}
 0&\longrightarrow B_o\xrightarrow{\alpha}B_e
      \xrightarrow{\rho_0}A_H\longrightarrow0,
 &\rho_0[a]&=[a(0,-4x_h)],\\
 0&\longrightarrow A_H\xrightarrow{\iota_0}B_e
      \xrightarrow{\beta}B_o\longrightarrow0,
 &\iota_0[q]&=[Q_\Delta q(-\Delta/4)].
 \end{aligned}                                                    \tag{SSP.11}
\]
In particular both defects retain the original polynomial \(H\)
and every order in it.  On the full algebra \(\mathcal E\),
multiplication by the original sum is
\[
 A_S=I+\begin{pmatrix}0&-\alpha\\\beta&0\end{pmatrix}.
 \tag{SSP.12}
\]
Its full kernel and cokernel at \(S=1\) are
\[
 \ker(A_S-I)=\{(\iota_0q,0):q\in A_H\},\qquad
 \operatorname{coker}(A_S-I)\cong A_H,\quad
 [(a,b)]\mapsto\rho_0a .
 \tag{SSP.13}
\]
\end{theorem}
\begin{proof}
Let \(\mathcal R=\mathbb C[x,\Delta]\).
Since \(A_0(0,\Delta)\ne0\), the prime polynomial \(x\)
does not divide \(A_0\).  If \(xb=A_0c+xQ_\Delta e\),
then \(x(b-Q_\Delta e)=A_0c\) forces \(c=xc_1\), whence
\(b=A_0c_1+Q_\Delta e\).
This proves injectivity of \(\alpha\) without dividing by
\(x\) in either quotient.  Surjectivity of \(\beta\) follows
from its quotient definition.
The image of \(\alpha\) is \(xB_e\), because every polynomial
representative of an even class is also an odd coefficient
representative.  Therefore
\[
 \operatorname{coker}\alpha
 \cong\mathcal R/(A_0,x)
 \cong\mathbb C[\Delta]/((-1)^DH(-\Delta/4))
 \cong A_H .
 \tag{SSP.14}
\]
The last isomorphism sends \(\Delta\) to \(-4x_h\);
its inverse sends \(x_h\) to \(-\Delta/4\).
This proves the first sequence, with all constants.

We justify the cancellation required for the second sequence.
The quotient \(\mathcal R/(A_0,Q_\Delta)=B_o\) has finite
dimension \(D^2\), already proved in (SSP.8).
If a nonconstant irreducible polynomial divided both
\(A_0,Q_\Delta\), then it would divide every polynomial
annihilator of \(x\) and every polynomial annihilator of
\(\Delta\) in this quotient.  Such nonzero univariate
annihilators exist by linear dependence of the powers in
the finite vector space.  Over \(\mathbb C\), a common
irreducible divisor of a nonzero polynomial in \(x\) alone
and one in \(\Delta\) alone is impossible: their irreducible
factors are respectively \(x-a\) and \(\Delta-b\).
Thus \(\gcd(A_0,Q_\Delta)=1\) in \(\mathcal R\).

The kernel of \(\beta\) consists exactly of the classes
\([Q_\Delta p]\) in \(B_e\).
Multiplication by \(Q_\Delta\) gives a surjection
\[
 \mathcal R/(A_0,x)\longrightarrow\ker\beta,\qquad
 [p]\longmapsto[Q_\Delta p].
 \tag{SSP.15}
\]
It is well-defined since \(A_0Q_\Delta=xQ_\Delta=0\)
in \(B_e\).  If \(Q_\Delta p=A_0c+xQ_\Delta e\), the
coprimality just proved forces \(A_0\mid p-xe\).
Hence \([p]=0\) in \(\mathcal R/(A_0,x)\), proving
injectivity.  Compose (SSP.15) with the inverse last map of
(SSP.14) to obtain exactly \(\iota_0\) in (SSP.11).
Finally multiplication by \(Z\) is the off-diagonal part
of (SSP.12).  Its kernel has odd component zero by
injectivity of \(\alpha\), and even component \(\ker\beta\).
Its cokernel has zero odd quotient by surjectivity of
\(\beta\), and even quotient \(\operatorname{coker}\alpha\).
This proves (SSP.13).
\end{proof}

The full multiplication on the second defect is also explicit.
Put
\[
 \mathfrak c_H=2(-1)^D x_hH'(x_h)\pmod H .
\]
Then, for every \(q,t\in A_H\),
\[
 \iota_0(q)\iota_0(t)=\iota_0(\mathfrak c_Hqt).
 \tag{SSP.15a}
\]
Indeed \(xQ_\Delta=0\) gives
\(Q_\Delta^2=Q_\Delta Q_\Delta(0,\Delta)\) in \(B_e\).
Equation (SSP.4), followed by \(\Delta=-4x_h\), identifies
\(Q_\Delta(0,-4x_h)\) with \(\mathfrak c_H\).
Substitution in the two products proves (SSP.15a).
Thus the module isomorphism \(\iota_0\) transports the
inherited ideal multiplication to \(q\star t=\mathfrak c_Hqt\),
retaining the derivative and its nilpotent values.

The generator in (SSP.11) is the full class \(Q_\Delta=\Delta A_1\)
modulo \((A_0,xQ_\Delta)\).  Reducing its coefficient at \(x=0\)
before forming this class would change the map.  In particular
(SSP.4) can vanish on repeated local fibres through \(H'\);
the proved injective map \(\iota_0\) still retains those fibres.
Equation (SSP.15) specifies the complete mixed nilpotent class
that carries them.

\subsection{The original unit and all coordinate factorials}

The original full unit on \(\mathcal E\) is
\[
 \upsilon^{(2)}=[v_h(s_1)v_h(s_2)]\in\mathcal E^\times .
 \tag{SSP.16}
\]
This bracket denotes its complete double Taylor class modulo
\((h(s_1),h(s_2))\), followed by the invariant identification;
the values of all admitted derivatives are retained.
Since \(d=2D\), \(v_h(1-s)=v_h(s)\).
Thus this unit has the form \((u_e,0)\) under (SSP.5), and
its two multiplication maps are
\[
 U_e=M_{u_e}:B_e\to B_e,\qquad
 U_o=M_{\beta(u_e)}:B_o\to B_o .
 \tag{SSP.17}
\]
Both are invertible, by multiplication with the components of
the original inverse unit.  Their exact intertwiners and defect
actions are
\[
 \begin{gathered}
 U_e\alpha=\alpha U_o,\qquad \beta U_e=U_o\beta,\qquad
 \rho_0U_e=M_{V(x_h)^2}\rho_0,\\
 U_e\iota_0=\iota_0M_{V(x_h)^2},
 \qquad V(x_h)=(-1)^D\Phi(x_h)/H(x_h).
 \end{gathered}                                                    \tag{SSP.18}
\]
Indeed the first two equations are the module multiplication laws
in (SSP.7).  The algebra homomorphism \(\mathcal E\to A_H\)
given by \((a,b)\mapsto\rho_0a\) is the original specialization
\(s_2=1-s_1\), followed by its even quotient:
\(Z=0\), \(\Delta=4(s_1-1/2)^2=-4x_h\).
It sends (SSP.16) to
\(v_h(s_1)v_h(1-s_1)=V(x_h)^2\), proving the third
equation with all jets.  For the last equation,
\(xQ_\Delta=0\) implies
\[
 u_eQ_\Delta q(-\Delta/4)
   =Q_\Delta u_e(0,\Delta)q(-\Delta/4).
 \tag{SSP.19}
\]
The same specialization proves (SSP.18).
In particular the factor \(g=2\xi\) occurs in each original
unit factor and is present in the squared defect unit.

Here are explicit finite coordinate maps to the unscaled symmetric
basis used earlier.  Let \(T:E_h\to A_H\oplus z_hA_H\)
be the exact matrix (SP.6), with \(z_h=s-1/2\).
Use the bases \(a_i=x_h^i\) and \(b_i=z_hx_h^i\),
\(0\le i<D\), in that target.  The new symmetric basis is
ordered in these three groups:
\[
 \begin{gathered}
 a_i\odot a_j\ (i\le j),\qquad
 b_i\odot b_j\ (i\le j),\qquad
 a_i\odot b_j\ (0\le i,j<D),\\
 u\odot v=u\otimes v+v\otimes u\quad(u\ne v),\qquad
 u\odot u=u\otimes u .
 \end{gathered}                                                    \tag{SSP.20}
\]
The first two groups are the basis of \(B_e\), and the last,
after removal of its displayed \(Z\), is the basis of \(B_o\).
These identifications follow by the inverse substitutions in
(SSP.2) and (SP.4): swap invariance leaves even powers of \(r\),
and reflection leaves even powers of \(Z\) in the first two groups
and odd powers in the last.  Replace \(Z^{2j}r^{2a}\) by
\((-x)^j\Delta^a\), and \(Z^{2j+1}r^{2a}\) by
\(Z(-x)^j\Delta^a\).  This finite coefficient prescription gives
each basis polynomial explicitly, without choosing values at roots.

Let \(I_{\rm old}\) and \(I_{\rm new}\) insert the literal orbit
sums in, respectively, the original monomial tensor basis and
the basis (SSP.20) before passage to its invariant space.
Put
\[
 \begin{gathered}
 D_{\rm old}=I_{\rm old}^*I_{\rm old},\quad
 L_{\rm old}=D_{\rm old}^{-1}I_{\rm old}^*,\\
 D_{\rm new}=I_{\rm new}^*I_{\rm new},\quad
 L_{\rm new}=D_{\rm new}^{-1}I_{\rm new}^*,\\
 T_s=L_{\rm new}(T\otimes T)I_{\rm old},\qquad
 T_s^{-1}=L_{\rm old}(T^{-1}\otimes T^{-1})I_{\rm new}.
 \end{gathered}                                                    \tag{SSP.21}
\]
Each diagonal entry of \(D_{\rm old},D_{\rm new}\) is one for
a repeated basis vector and two for two distinct vectors.
These are the original orbit cardinalities.  The products \(IL\)
are both the permutation average \((I+\mathrm{swap})/2\);
it commutes with \(T\otimes T\).  Hence the two displayed
matrices compose to identity.  This proves all factors in the
coordinate maps.  Moreover
\[
 |\det T_s|=|\det T|^{d+1}=1.
 \tag{SSP.22}
\]
To verify the exponent, triangularize \(T\) over \(\mathbb C\);
on symmetric tensors its diagonal entries are the products of
its diagonal entries indexed by \(i\le j\).  Each original
diagonal entry occurs \(d+1\) times.  The similarity inducing
that triangularization and the final permutation into (SSP.20)
do not change the absolute determinant.  Equation (SP.7)
then proves (SSP.22).  No tensor basis vector has been divided
by its length.

\subsection{The actual matrix weight and its positive half-line pair}

Retain the original density
\[
 w_h(t)=|v_h(1/2+it)|^2/(2\pi).
 \tag{SSP.23}
\]
It is even and has the exponential and polynomial integrability
proved for the theta source.  For a fixed source degree \(M\),
put \(L_M=\lfloor M/2\rfloor\) and keep every relative direction
\(0\le a\le L_M\).  The PR~17 matrix weight is exactly
\[
 \mathsf W_{ac}(u)=\frac{(-1)^{a+c}}2
   \int_{\mathbb R}v^{2(a+c)}
       w_h((u+v)/2)w_h((u-v)/2)\,dv .
 \tag{SSP.24}
\]
For each \(u\), this finite matrix is real Hermitian and strictly
positive.  Indeed its quadratic form on a nonzero vector \(c\)
is one half of the integral of
\(\left|\sum_a c_a(-v^2)^a\right|^2\) against the two positive
densities.  Their zeros are discrete, while that polynomial is
nonzero, proving strict positivity.  The actual decay gives
finite integrals.  Evenness of \(w_h\) gives
\(\mathsf W(-u)=\mathsf W(u)\), with every matrix entry retained.

For a symmetric original numerator
\[
 P(S,\Delta)=\sum_{a=0}^{L_M}\Delta^af_a(S),\qquad
 \deg f_a\le M-2a,
\]
the original coordinate change
\(u=t_1+t_2,\ v=t_1-t_2\) has
\(dt_1dt_2=du\,dv/2\), and \(S=1+iu,\Delta=-v^2\).
Expansion and Fubini, justified by the actual moment bounds, give
\[
 \|\mathcal T_h^{(2)}P\|^2
   =\int_{\mathbb R}f(1+iu)^*\mathsf W(u)f(1+iu)\,du .
 \tag{SSP.25}
\]
Here \(\mathcal T_h^{(2)}P=
P(D_1+D_2,(D_1-D_2)^2)F_h^{\otimes2}\); its Mellin
multiplier is \(P(S,\Delta)v_h(s_1)v_h(s_2)\).
Thus (SSP.25) includes both factors \(1/(2\pi)\), the real
Jacobian \(1/2\), and every relative-coordinate sign.

Define the matrix-valued measure on \(x>0\) by
\[
 d\Lambda(x)=\mathsf W(\sqrt x)\frac{dx}{\sqrt x}.
 \tag{SSP.26}
\]
For a matrix measure \(d\Lambda=W_\Lambda dx\), its squared \(L^2\)
norm is \(\int f^*W_\Lambda f\,dx\); every component has the
declared dimension \(L_M+1\).
The full unitary map and inverse are
\[
 \begin{aligned}
 \mathcal U_\Sigma:
 L^2(\Lambda)\oplus L^2(x\Lambda)
 &\longrightarrow L^2(\mathbb R,\mathsf W(u)\,du),\\
 (A,B)&\longmapsto f(1+iu)=A(u^2)+iuB(u^2),\\
 A(x)&=\frac{f(1+i\sqrt x)+f(1-i\sqrt x)}2,\\
 B(x)&=\frac{f(1+i\sqrt x)-f(1-i\sqrt x)}{2i\sqrt x}.
 \end{aligned}                                                    \tag{SSP.27}
\]
To prove the norm identity, add the two quadratic forms at
\(u\) and \(-u\).  The cross terms cancel and give
\(2A^*\mathsf W A+2u^2B^*\mathsf W B\).
The substitution \(x=u^2\) proves the direct-sum norm with
exactly (SSP.26).  The same calculation on the parity parts
of an arbitrary \(f\) proves that the displayed inverse belongs
to both asserted spaces.  There is no atom at zero, so the
almost-everywhere inverse requires no value there.
Multiplication by \(S=1+iu\) is
\[
 (A,B)\longmapsto(A-xB,A+B),
 \quad
 \begin{cases}
 A\in L^2(\Lambda)\cap L^2(x\Lambda),\\
 B\in L^2(x\Lambda)\cap L^2(x^2\Lambda).
 \end{cases}                                                       \tag{SSP.28}
\]
Its exact domain follows by adding \(\|uf\|^2\) to
\(\|f\|^2\), since \(|1+iu|^2=1+u^2\); the same parity
calculation gives the two additional weighted norms.

The finite source image in (SSP.27) is precisely
\[
 \deg A_a\le\left\lfloor\frac{M-2a}{2}\right\rfloor,\qquad
 \deg B_a\le\left\lfloor\frac{M-2a-1}{2}\right\rfloor
 \quad(0\le a\le L_M).
 \tag{SSP.29}
\]
A negative degree bound means the zero polynomial.
In particular the last odd relative direction can have a zero
allowed polynomial space while its ambient Hilbert component
is still retained.  The exact coefficient maps are obtained by
expanding each original \(S^j=(1+Z)^j\):
\[
 (1+Z)^j=
 \sum_{2\ell\le j}\binom j{2\ell}(-x)^\ell+
 Z\sum_{2\ell+1\le j}\binom j{2\ell+1}(-x)^\ell.
 \tag{SSP.30}
\]
The inverse replaces \(x\) by \(-(S-1)^2\), \(Z\) by \(S-1\)
in \(\sum_a\Delta^a(A_a(x)+ZB_a(x))\).
This proves both (SSP.29) and preservation of the original
weighted total-degree filtration.

\subsection{Full-jet kernels for the actual constrained minimum}

Fix \(M\ge2(d-1)=4D-2\).
Let \(\mathcal I_e=\{(a,j)\in\mathbb N^2:2a+2j\le M\}\),
and \(\mathcal I_o=\{(a,j)\in\mathbb N^2:2a+2j+1\le M\}\).
The positive source Gram matrices and full residue columns are
\[
 \begin{aligned}
 (M_e)_{(a,j),(c,\ell)}
     &=\int_0^\infty x^{j+\ell}\,d\Lambda_{ac}(x),
 &F_{a,j}&=u_e[\Delta^ax^j]_{B_e},\\
 (M_o)_{(a,j),(c,\ell)}
     &=\int_0^\infty x^{j+\ell+1}\,d\Lambda_{ac}(x),
 &E_{a,j}&=\beta(u_e)[\Delta^ax^j]_{B_o}.
 \end{aligned}                                                    \tag{SSP.31}
\]
Use the exact bases (SSP.20) for these columns and let \(J_e,J_o\)
be the corresponding column matrices.  Each Gram is strictly
positive: a nonzero coefficient vector gives a nonzero polynomial
vector in (SSP.29), whose squared norm is positive for the
strictly positive matrix density.  All its moments are finite by
(SSP.24)--(SSP.26).

The two jet maps are onto at the stated degree.  Indeed the
original symmetric orbit basis \(s_1^is_2^j+s_1^js_2^i\)
for \(i<j<d\), and the diagonal basis \(s_1^is_2^i\), has
degree at most \(2(d-1)\).  Its full residue map is onto
\(\mathcal E\), and multiplication by the actual unit is
invertible.  Reflection preserves the degree filtration and
this unit, so parity projection proves surjectivity onto
each of \(B_e,B_o\) separately.  Equivalently the concrete
basis (SSP.20) has maximum degrees \(4D-4\), \(4D-2\),
and \(4D-3\) in its three groups.  This verifies the
endpoint \(M=4D-2\), including \(D=1,M=2\).

Define the actual kernels and their inverse metrics by
\[
 K_e=J_eM_e^{-1}J_e^*,\quad K_o=J_oM_o^{-1}J_o^*,\qquad
 G_e=K_e^{-1}>0,\quad G_o=K_o^{-1}>0.
 \tag{SSP.32}
\]
All columns here are full polynomial remainders with the full
unit.  In particular their matrix sizes are
\(D(D+1)\) and \(D^2\), respectively.

\begin{theorem}[The same original minimum and its unequal relative blocks]
Let \(R_M^s\) be the original symmetric canonical representative
in the unscaled monomial orbit coordinates, \(G_M^s=(R_M^s)^*R_M^s\),
and \(A_M^s\) its original sum generator.
Then
\[
 \begin{gathered}
 T_s^{-*}G_M^sT_s^{-1}=\operatorname{diag}(G_e,G_o),\qquad
 \det G_M^s=\det G_e\det G_o,\\
 T_sA_M^sT_s^{-1}
      =I+\begin{pmatrix}0&-\alpha\\\beta&0\end{pmatrix}.
 \end{gathered}                                                    \tag{SSP.33}
\]
The original weight and its exact allowance satisfy
\[
 \begin{gathered}
 W_M^s=(A_M^s)^*G_M^s+G_M^sA_M^s-2G_M^s,\\
 T_s^{-*}W_M^sT_s^{-1}
   =\begin{pmatrix}
     0&\beta^*G_o-G_e\alpha\\
     G_o\beta-\alpha^*G_e&0
    \end{pmatrix},\\
 \boxed{\epsilon_M^s
   =\left\|G_e^{-1/2}(\beta^*G_o-G_e\alpha)G_o^{-1/2}\right\|_{\rm op}.}
 \end{gathered}                                                    \tag{SSP.34}
\]
If the displayed rectangular block has rank \(p\), the relative
weight has \(p\) positive and \(p\) negative eigenvalues,
given by its positive singular values and their negatives.
Its zero multiplicity is
\[
 D(D+1)+D^2-2p=D+2(D^2-p).
 \tag{SSP.35}
\]
Thus the dimension difference, all additional zero directions,
and all nonzero multiplicities are retained.
\end{theorem}
\begin{proof}
The actual product source has the permutation-invariant Hilbert
norm and full invariant jet map specified before (SSP.25).
For a symmetric target, apply swap to its unique full minimum.
The image and norm are unchanged, so uniqueness makes that
minimum symmetric.  Therefore minimizing over precisely the
invariant degree-\(M\) polynomials gives the original
\(R_M^s\), not a new family of positive forms.

The exact coefficient transformation (SSP.30) has source Gram
\(\operatorname{diag}(M_e,M_o)\); mixed terms vanish by the
proved parity isometry.  Its full jet map in coordinates
(SSP.21) is \(\operatorname{diag}(J_e,J_o)\).
For a positive source Gram \(M\) and surjective map \(J\),
the vector
\[
 M^{-1}J^*(JM^{-1}J^*)^{-1}y
\]
has image \(y\) and is \(M\)-orthogonal to \(\ker J\).
Every other preimage differs by a kernel vector, and its
squared norm is the squared norm of this vector plus the
positive squared norm of that difference.  Thus its minimum
metric is exactly \((JM^{-1}J^*)^{-1}\).
Apply this calculation to the two declared blocks to prove
the metric congruence in (SSP.33).  The coordinate representative
is \(R_M^sT_s^{-1}\), and its two source coefficient blocks
are explicitly \(M_e^{-1}J_e^*G_e\) and
\(M_o^{-1}J_o^*G_o\).  Hence both its source function and
full jets agree with the original minimum.
Equation (SSP.22) proves the determinant equality.
Equation (SSP.12) proves the generator similarity.

Multiplying the two generator blocks with the metric in
(SSP.33) cancels the two identity terms against \(2G_M^s\).
This gives exactly the middle line of (SSP.34).
The relative congruence by
\(\operatorname{diag}(G_e^{-1/2},G_o^{-1/2})\) has the form
\(\left(\begin{smallmatrix}0&B\\B^*&0\end{smallmatrix}\right)\)
with the rectangular block displayed there.
For each positive singular value \(\sigma\) and corresponding
unit singular vectors \(u,v\), its vectors \((u,v)\) and
\((u,-v)\) have eigenvalues \(\sigma,-\sigma\).
The remaining kernel is \(\ker B^*\oplus\ker B\),
with dimensions \(D(D+1)-p\) and \(D^2-p\).
This proves its norm, all signs, and (SSP.35).
The coordinate map
\[
 \operatorname{diag}(G_e^{1/2},G_o^{1/2})
             T_s(G_M^s)^{-1/2}
\]
is unitary by (SSP.33) and intertwines the two relative
Hermitian matrices.  Thus these are the complete relative
eigenvalues of the original arithmetic weight.
No inverse of \(\alpha,\beta,B\), or either frontier rank
has been used.
\end{proof}

In particular zero allowance is exactly the finite equation
\(\beta^*G_o=G_e\alpha\), with both rectangular maps retained.
It does not follow from positivity of the two source Gram
matrices.  The map from those positive matrices to this
equation is the fully proved difference block (SSP.34).
Every original zero \(\rho\), of any order \(m_\rho\), has
an eigenvector represented in its local factor by
\((s-\rho)^{m_\rho-1}\).  Its square tensor is symmetric,
nonzero, and has sum eigenvalue \(2\rho\).
Its original Rayleigh quotient is therefore
\[
 \frac{u^*W_M^su}{u^*G_M^su}=4\operatorname{Re}\rho-2,
 \qquad
 4\left|\operatorname{Re}\rho-\tfrac12\right|
       \le\epsilon_M^s .
 \tag{SSP.36}
\]
This retains the exact tensor factor and every original local
direction in the full metric; it makes no assumption about
the limiting size of that metric difference.

\subsection{Original primitives and supported maps}

For any invariant relation written
\(H_0A+\Delta H_1B\), the original identity is
\[
 H_0A+\Delta H_1B
  =h(s_1)\frac{A+rB}{2}
       +h(s_2)\frac{A-rB}{2}.
 \tag{SSP.37}
\]
The two original cochain primitives apply the first coefficient
to \(\phi_*\otimes F_h\) and the negative of the second
coefficient to \(F_h\otimes\phi_*\).
The second tensor differential contributes its own minus sign,
so their total boundary is precisely (SSP.37).
For an even relation \(A_0a+xQ_\Delta b\), take
\(A=a,\ B=-Zb\); for an odd relation
\(Z(A_0a+Q_\Delta b)\), take \(A=Za,\ B=b\).
Substitution of \(Z^2=-x\) proves both assertions with their
full signs.  Thus the two coefficient ideals in (SSP.6)
have the original theta primitives, including the factor
\(xQ_\Delta\) in the even ideal.  At a finite admitted
degree the polynomial identity is the same original relation.
For completeness, divide a relation \(P\) of total degree at most
\(M\) first by the monic \(h(s_1)\), then divide its remainder
by the monic \(h(s_2)\).  The final remainder is zero because
\(P\) lies in the original ideal.  This gives
\(P=h(s_1)C_1+h(s_2)C_2\), with
\(\deg C_1,\deg C_2\le M-d\).
Average under swap and put
\(B_1=(C_1+\mathrm{swap}(C_2))/2\), \(B_2=\mathrm{swap}(B_1)\).
Then \(A=B_1+B_2\) is even in \(r\), and
\(B=(B_1-B_2)/r\) is a polynomial even in \(r\).
Their degrees satisfy \(\deg A\le M-d\) and
\(\deg B\le M-d-1\), and their coefficients in (SSP.37)
are exactly \(B_1,B_2\).
This proves the original finite-degree primitive bounds,
including a zero coefficient when its degree bound is negative.

Every algebra isomorphism in (SSP.5), (SSP.9), and (SSP.14)
has the exact \(G\)-lift: it fixes external \(\tau\) and
sends a supported amplitude to its supported algebra image.
The algebra-homomorphism laws and the absorbing rule for
\(\tau\) prove the semiring laws; the inverse is the lift
of the displayed inverse.  The algebra maps \(\beta,\rho_0\)
have the same functorial lift.
The module maps \(\alpha,\iota_0\) and all Hilbert, jet,
kernel and representative maps above have their fixed-label
linear lifts \((\lambda,v)\mapsto(\lambda,Tv)\), fixing
external absence.  Their exact module actions are the ones
proved in (SSP.7), (SSP.11), and (SSP.18).
A class killed in either exact sequence goes to the zero
in its receiving supported fibre; the represented kernel
and cokernel \(A_H\) retain every local order and the
unit \(V^2\).  The direct sum in (SSP.6) is equipped with
the multiplication (SSP.7); its parity components have not
been assigned independent external supports by this map.

```
