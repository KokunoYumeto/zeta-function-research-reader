from pathlib import Path
import hashlib, json, re

ROOT = Path(r'workspace:')
BASE = ROOT / 'output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue'
OUT = ROOT / 'work/backpropagation_20260913/metric/baseline_patch'
WORK = OUT.parent
OUT.mkdir(parents=True, exist_ok=True)

metric = r'''
\subsubsection{The signed metric control at these same four endpoints}
\label{endpoint:metric-backprop}
The AW calculation supplies the full-spectrum estimate and its
condition-number consequence. The SP calculation supplies the additional
actual-overlap refinement. Their exact comparison ACM.1--13 proves that
they act on the same source. We carry both calculations into the budget
(8), rather than replacing its four signed terms by four separate errors.
Here the integration coordinate remains the original $u$ in $S=k/2+iu$;
the coordinate called $y$ in ACM is exactly this $u$. The new variable
$x\in[0,1]$ is only the metric interpolation parameter.

Put $\mathcal P_N=\mathbb C[S]_{\le N}$ and $\mathcal H=\mathcal P_{2q}$ in its original ordered monomials,
$v(u)=(1,S,\ldots,S^{2q})$, and retain the full arithmetic density
$m_1(u)=w_h^{*k}(u)$. The original Gamma comparison has the literal density
and mass
\[
 \begin{gathered}
 r_a(u)=\frac{|\Gamma(a+iu/2)|^2}{2\pi},\qquad
 c_a=2^{1-2a}\Gamma(2a),\\
 m_0(u)=\frac{c_{1/4}^{k}}{c_{k/4}}r_{k/4}(u),\qquad
 c_{1/4}=\sqrt{2\pi},\qquad
 \int_{\mathbb R}m_0(u)\,du=(\sqrt{2\pi})^k.
 \end{gathered}\tag{FV.M1}\label{fvmetric:density}
\]
The complete Gamma convolution proof retained in this reader gives
$m_0=r_{1/4}^{*k}$. Thus (FV.M1) uses its original mass; the arithmetic
mass is still $\mu_h^k$. Define
\[
 m_x=(1-x)m_0+xm_1,\qquad
 M_x=\int_{\mathbb R}v(u)^*v(u)m_x(u)\,du,
 \qquad C_x=M_x^{-1}(M_1-M_0).
 \tag{FV.M2}\label{fvmetric:path}
\]
Both endpoint densities are positive almost everywhere and have all
moments, so every $M_x$ is positive: a nonzero polynomial has only finitely
many zeros on the integration line. No matrix or density is divided by
its mass.

Let $I_N:\mathbb C[S]_{\le N}\hookrightarrow\mathcal H$ be coefficient
inclusion and $B_N:\mathbb C[S]_{\le N-q}\to\mathbb C[S]_{\le N}$ be
multiplication by the original monic $\chi$. Negative-degree spaces are
zero. Put $H_N(x)=I_N^*M_xI_N$, and use the original remainder $J_N$ to set
$G_N(x)=(J_NH_N(x)^{-1}J_N^*)^{-1}$ and $V_N(x)=\det G_N(x)$.
The maps to the common source and their orthogonal projections are exactly
\[
 \begin{aligned}
 \widetilde B_N&=I_N B_N,&
 P_N&=I_N H_N(x)^{-1}I_N^*M_x,\\
 Q_N&=\widetilde B_N
       (\widetilde B_N^*M_x\widetilde B_N)^{-1}
                          \widetilde B_N^*M_x,& Q_{q-1}&=0.
 \end{aligned}\tag{FV.M3}\label{fvmetric:maps}
\]
The formula for $Q_{q-1}$ uses the zero relation domain, with empty
determinant one. For each other $N$, injectivity of multiplication by
monic $\chi$ proves invertibility of its relation Gram. Direct
multiplication proves $P_N^2=P_N$, $Q_N^2=Q_N$ and self-adjointness in
$M_x$, with ranges $\mathcal P_N$ and $\chi\mathcal P_{N-q}$.
These formulas are also the exact typed identities
$\widetilde B_N=B_N^{\rm SP}=I_N B_N^{\rm AW}$.

The coefficient matrix
$[1,S,\ldots,S^{q-1},\chi,S\chi,\ldots,S^{N-q}\chi]$ is triangular
with diagonal one. Its Gram has determinant $\det H_N(x)$.
Eliminating the relation block leaves its Schur complement $G_N(x)$:
indeed for a fixed remainder $z$, minimizing over the relation
coefficients solves the relation normal equations and gives precisely
$z^*G_N(x)z$. Consequently
\[
 \det G_N(x)=\frac{\det H_N(x)}{\det(B_N^*H_N(x)B_N)},\qquad
 \frac{d}{dx}\log V_N(x)=\operatorname{Tr}((P_N-Q_N)C_x).
 \tag{FV.M4}\label{fvmetric:derivative}
\]
For the derivative, multilinearity of determinant gives
$d\log\det H=\operatorname{Tr}(H^{-1}dH)$.
Insert $dH_N=I_N^*(M_1-M_0)I_N$ in the numerator and
$B_N^*dH_NB_N$ in the denominator. Cyclicity of the finite trace
and $M_xC_x=M_1-M_0$ give the two terms in (FV.M4).

Define the original signed function and its two projection sums by
\[
 \begin{aligned}
 F(x)&=\log\frac{V_{q-1}(x)V_q(x)}{V_{2q-1}(x)V_{2q}(x)},\\
 U_x&=Q_{2q-1}+Q_{2q}-Q_q,\\
 W_x&=(P_{2q-1}-P_{q-1})+(P_{2q}-P_q),\qquad A_x=U_x-W_x.
 \end{aligned}\tag{FV.M5}\label{fvmetric:signed}
\]
Keeping the signs of all four terms in (FV.M4) gives
\[
 \begin{aligned}
 F'(x)&=\operatorname{Tr}(A_xC_x)
       =\int_{\mathbb R}(m_1(u)-m_0(u))
                        v(u)A_xM_x^{-1}v(u)^*\,du,\\
 \mathcal B_{h,k}&=F(1)=\mathcal B^\Gamma_{h,k}+\Delta_{h,k},
 \qquad \mathcal B^\Gamma_{h,k}=F(0),\quad
 \Delta_{h,k}=\int_0^1 F'(x)\,dx.
 \end{aligned}\tag{FV.M6}\label{fvmetric:identity}
\]
The scalar density uses the full inverse $M_x^{-1}$, not an ordinary
Euclidean projection kernel. The integral identity follows by substituting
$M_1-M_0=\int v^*v(m_1-m_0)$ in the finite trace; its entries are
integrable moments. The density is real because
$A_xM_x^{-1}$ is Hermitian. It is signed, and its $m_x$ integral
equals $\operatorname{Tr}A_x=0$, as proved next.

The relation subspaces for $q,2q-1,2q$ are nested, of dimensions
$1,q,q+1$. Hence $U_x$ has eigenvalue two on
$\chi\mathcal P_{q-1}\ominus\chi\mathcal P_0$ (dimension $q-1$),
eigenvalue one on $\chi\mathcal P_0$ and
$\chi\mathcal P_q\ominus\chi\mathcal P_{q-1}$ (one dimension each),
and eigenvalue zero on its $q$-dimensional complement.
The degree flag decomposes $W_x$ identically: its two summands have
overlap $\mathcal P_{2q-1}\ominus\mathcal P_q$ of dimension $q-1$,
and two one-dimensional end pieces. Thus both $U_x,W_x$ have rank
$q+1$, trace $2q$ and trace of the square $4q-2$. These statements include
$q=1$, when the overlap dimension $q-1$ is zero.

Let $c_1(x)\le\cdots\le c_{2q+1}(x)$ be the eigenvalues of $C_x$
in $M_x$, let $d_x=c_{2q+1}(x)-c_1(x)$, and put
$s_x=\dim(\operatorname{ran}U_x\cap\operatorname{ran}W_x)$.
Retain both exact pointwise expressions
\[
 \begin{aligned}
 S_{\rm AW}(x)&=c_{q+2}(x)-c_q(x)
       +2\sum_{j=1}^{q-1}(c_{2q+2-j}(x)-c_j(x)),\\
 S_{\rm SP}(x)&=\frac{d_x}{2}\min\left\{4q-2s_x,
 \sqrt{(2q+1)(8q-4-2\operatorname{Tr}(U_xW_x))}\right\},\\
 \mathfrak I_{h,k}&=\int_0^1\min\{S_{\rm AW}(x),S_{\rm SP}(x)\}\,dx.
 \end{aligned}\tag{FV.M7}\label{fvmetric:control}
\]
Here is the full finite proof of their applicability at this earlier
endpoint. For a rank-$r$ orthogonal projection $E$, its diagonal in an
orthonormal eigenbasis of $C_x$ lies in $[0,1]$ and sums to $r$.
Moving this diagonal mass to the lowest or highest eigenvalues gives
$\sum_{j=1}^r c_j\le\operatorname{Tr}(EC_x)
\le\sum_{j=2q+2-r}^{2q+1}c_j$.
Each of $U_x,W_x$ is its range projection, of rank $q+1$, plus its
eigenvalue-two projection, of rank $q-1$. Applying the two inequalities
to these two summands and subtracting the resulting extrema gives
$|F'(x)|\le S_{\rm AW}(x)$, with the multiplicities displayed in
(FV.M7).

Dimension gives $s_x\ge1$. Let $E_x$ be the $M_x$-orthogonal
projection onto the actual intersection of the two ranges. Each of
$U_x,W_x$ dominates its own range projection, which dominates $E_x$;
therefore $U_x-E_x$ and $W_x-E_x$ are positive and each has trace
$2q-s_x$. The triangle inequality for their trace norms gives
$\|A_x\|_1\le4q-2s_x$.
The full spectra just proved also give
\[
 \operatorname{Tr}A_x=0,\qquad
 \operatorname{Tr}A_x^2=8q-4-2\operatorname{Tr}(U_xW_x),\qquad
 \|A_x\|_1^2\le(2q+1)\operatorname{Tr}A_x^2.
 \tag{FV.M8}\label{fvmetric:overlap}
\]
The last inequality is Cauchy--Schwarz on all $2q+1$ real
eigenvalues. Subtract $(c_1+c_{2q+1})I/2$ from $C_x$ in the trace;
the first identity leaves $F'$ unchanged. In an eigenbasis of $A_x$,
each diagonal entry of the centered $C_x$ has absolute value at most
$d_x/2$. Thus $|F'(x)|\le d_x\|A_x\|_1/2\le S_{\rm SP}(x)$.
Both estimates hold at every $x$ on the same original metric. Their
pointwise minimum is integrable: all Grams and inverse Grams are smooth,
all ordered eigenvalues are continuous, and $s_x$ is Borel since its
level sets are determined by vanishing and nonvanishing matrix minors.
Consequently (FV.M6) gives the finite two-sided enclosure
\[
 \boxed{\mathcal B^\Gamma_{h,k}-\mathfrak I_{h,k}
       \le\mathcal B_{h,k}\le
        \mathcal B^\Gamma_{h,k}+\mathfrak I_{h,k}.}
 \tag{FV.M9}\label{fvmetric:budget}
\]

For the positive original relative endomorphism $D=M_0^{-1}M_1$
on $(\mathcal H,M_0)$, let $b_1\le\cdots\le b_{2q+1}$ be all
its eigenvalues. Direct factorization
$M_x=M_0((1-x)I+xD)$ gives
$C_x=((1-x)I+xD)^{-1}(D-I)$ and hence
\[
 \begin{gathered}
 c_j(x)=\frac{b_j-1}{1-x+xb_j},\qquad
 \int_0^1c_j(x)\,dx=\log b_j,\\
 \mathfrak I_{h,k}\le
 \min\left\{\log\frac{b_{q+2}}{b_q}
     +2\sum_{j=1}^{q-1}\log\frac{b_{2q+2-j}}{b_j},\quad
                    \int_0^1S_{\rm SP}(x)\,dx\right\}
 \le(2q-1)\log\frac{b_{2q+1}}{b_1}.
 \end{gathered}\tag{FV.M10}\label{fvmetric:eigenvalues}
\]
The scalar fraction is increasing in $b$ with derivative
$(1-x+xb)^{-2}$, proving the stated eigenvalue order throughout the
path. Integrating its logarithmic derivative proves the integral.
For the last bound use $s_x\ge1$ in (FV.M7) and integrate $d_x$.
The common consequence is the earlier AW bound; the pointwise minimum
retains both its spectral refinement and the additional SP overlap.

Finally let the two unchanged arithmetic endpoint losses be
$E_0=\log(V_{q-1}/V_q)$ and $E_1=\log(V_{2q-1}/V_{2q})$.
Equation (8), with (FV.M6), gives the literal central identity and bounds
\[
 \begin{gathered}
 2C_k=\mathcal B^\Gamma_{h,k}+\Delta_{h,k}-E_0-E_1,\\
 \max\left\{0,\frac{\mathcal B^\Gamma_{h,k}-\mathfrak I_{h,k}-E_0-E_1}{2}\right\}
 \le C_k\le
 \frac{\mathcal B^\Gamma_{h,k}+\mathfrak I_{h,k}-E_0-E_1}{2},\\
 4(q-1)\log\frac{L_{h,k}}{C_h^{\rm bal}q}+E_0+E_1
 \le\mathcal B_{h,k}\le\mathcal B^\Gamma_{h,k}+\mathfrak I_{h,k}.
 \end{gathered}\tag{FV.M11}\label{fvmetric:central}
\]
The first line is substitution in (8); the second uses (FV.M9) and
$C_k\ge0$; the third uses the first inequality in (7) without
discarding either endpoint loss. All expressions retain the original
full packet $h$, its exact $\chi$, and the constants in (1)--(4).
This gives an actual finite control for the old four-volume expression.
It supplies no uniform estimate of $\mathfrak I_{h,k}$ as the packet
order grows, so the original lower-growth conclusion (9) remains intact.

The comparison is induced by identity polynomial maps on every
$\mathcal P_N$ and the identity on $\mathbb C[S]/(\chi)$.
For the original source realization
$\mathcal V P=P(\sum D_i)F_h^{\otimes k}$ and complete unit map
$\eta[P]=[g/h]_h^{\otimes k}P(\sum s_i)$, these identities commute
exactly with $\eta J_N$; the values and every raw derivative of each
polynomial are unchanged. The least lift at $x$ is
$R_N(x)=H_N(x)^{-1}J_N^*G_N(x)$, so
$J_N(R_N(x)-R_N(1))=0$. Monic division gives a unique coefficient
map $\kappa_N(x)$ with
$R_N(x)-R_N(1)=B_N\kappa_N(x)$.
Retain the original fixed-order tensor division
$\chi(\sum s_i)=\sum_i h(s_i)Q_i(\mathbf s)$. On a quotient vector
$z$, the complete original theta primitive of this difference is
\[
 \sum_{i=1}^k(-1)^{i-1}Q_i(\mathbf D)
       (\kappa_N(x)z)(\textstyle\sum_jD_j)
 \bigl(F_h^{\otimes(i-1)}\otimes\phi_0
                       \otimes F_h^{\otimes(k-i)}\bigr).
 \tag{FV.M12}\label{fvmetric:primitive}
\]
The tensor differential contributes the second sign $(-1)^{i-1}$
and $h(D_i)F_h=\Theta\phi_0$, so its boundary is exactly
$\mathcal V(R_N(x)-R_N(1))z$. Thus the Gram comparison is attached
to an explicit original source map and primitive; it does not identify
the interpolated norm with the original arithmetic norm. For each
unchanged outer label and independent coefficient face, retain the actual
declared subcomplex $C_\lambda^\bullet\subseteq C_{\rm full}^\bullet$
and its degree-$(k-1)$ source $C_\lambda^{k-1}$. Write $\Xi$ for
the primitive in (FV.M12). Whenever $d\Xi$ belongs to $C_\lambda^k$,
its exact residual is $[d\Xi]\in C_\lambda^k/d(C_\lambda^{k-1})$.
The full top-degree comparison has the exact kernel
\[
 \ker\bigl[H^k(C_\lambda^\bullet)\longrightarrow
                 H^k(C_{\rm full}^\bullet)\bigr]
 =\frac{d(C_{\rm full}^{k-1})\cap C_\lambda^k}
             {d(C_\lambda^{k-1})}.
 \tag{FV.M13}\label{fvmetric:proper-source}
\]
Here both complexes have top degree $k$, so all degree-$k$ elements
are cycles. A class $[z]$ maps to zero precisely when $z=d\Xi$ for
some $\Xi\in C_{\rm full}^{k-1}$; it is already zero in the declared
source precisely when $z=d\Xi_\lambda$ for a declared primitive.
This proves (FV.M13), including its injective inclusion into
$H^k(C_\lambda^\bullet)$. Equivalently the primitive map has domain
$\{\Xi\in C_{\rm full}^{k-1}:d\Xi\in C_\lambda^k\}$ and kernel
$C_\lambda^{k-1}+\ker d$, so quotienting by this exact kernel gives
the same residual space. This retains possible cancellations among
tensor slots. For one leg with unchanged top source $\mathscr B$
and injective $\Theta:V\to\mathscr B$, it becomes the exact sequence
\[
 0\longrightarrow V/W\xrightarrow{[v]\mapsto[\Theta v]}
 \mathscr B/\Theta W\longrightarrow\mathscr B/\Theta V
 \longrightarrow0.
 \tag{FV.M14}\label{fvmetric:one-leg-residual}
\]
The first map is injective because $\Theta v\in\Theta W$ forces
$v\in W$; its image is the kernel of the quotient map, which is
surjective by definition. Thus a relation with primitive in the
declared source maps to its supported zero. A general full-source
primitive retains the exact residual (FV.M13) on every coefficient
face, rather than declaring its proper-source class zero. Identity
polynomial maps retain the outer labels; external $\tau$ still maps
to $\tau$ and an empty coefficient face retains its outer label.

'''

erj = r'''
The signed metric control now bounds these same two return losses before
the scalar envelope is taken. Use $\mathcal B^\Gamma_{h,k}$ and
$\mathfrak I_{h,k}$ as defined and completely proved in
(FV.M1)--(FV.M10), Section~\ref{endpoint:metric-backprop}. Its common
monomial source $H_N(1)$ is exactly the original $H_N$ in (ERJ.3): both
have entries $\int\overline{(c+iu)^a}(c+iu)^bm_k(u)\,du$.
Its quotient $J_N$ is monic remainder by this same $\chi$. If $T_N$
is the monic triangular coefficient matrix of $p_0,\ldots,p_N$, then
$O_N=T_N^*H_NT_N$, $B_N^{\rm ERJ}=J_NT_N$, and direct substitution
gives $B_N^{\rm ERJ}O_N^{-1}(B_N^{\rm ERJ})^*=J_NH_N^{-1}J_N^*$.
Hence no change of quotient coordinates occurs in the comparison.
In particular the literal refinement of (ERJ.32) is
\[
 \max\{0,\mathcal B^\Gamma_{h,k}-\mathfrak I_{h,k}\}
 \le\mathcal B_{h,k}\le
 \min\{q\log C_{2q-1}+q\log C_{2q},\,
                   \mathcal B^\Gamma_{h,k}+\mathfrak I_{h,k}\}.
 \tag{ERJ.32a}\label{erj:metric-budget}
\]
The lower bound combines nonnegativity of the two original return losses
with (FV.M9); the upper bound combines that equation with (ERJ.32).
Each rational trace certificate in (ERJ.25) is retained as well: the two
upper endpoints can be summed and included as a further entry in the
minimum. The source and relation errors in (ERJ.26)--(ERJ.31) continue
to be computed for those original matrices.

This also controls the earlier inverse-power observations, not merely
their determinant. Let $g_{a,j}$, $a=0,1$, $1\le j\le q$, be all
eigenvalues of the two original returns, and let
\[
 U_{h,k}^{\rm joint}:=
 \min\{q\log C_{2q-1}+q\log C_{2q},\,
                   \mathcal B^\Gamma_{h,k}+\mathfrak I_{h,k}\}.
\]
They lie in $(0,1]$, and (ERJ.5) gives the exact identity
$\sum_{a,j}-\log g_{a,j}=\mathcal B_{h,k}$.
For every real $s>0$, put $z_{a,j}=g_{a,j}^{-s}-1\ge0$.
The expansion of $\prod(1+z_{a,j})$ contains $1+\sum z_{a,j}$
and only further nonnegative terms. Consequently
\[
 \begin{gathered}
 \operatorname{Tr}U_{q-1,2q-1}^{-s}
       +\operatorname{Tr}U_{q,2q}^{-s}
 \le 2q-1+e^{s\mathcal B_{h,k}}
 \le 2q-1+e^{sU_{h,k}^{\rm joint}},\\
 g_{a,j}\ge e^{-\mathcal B_{h,k}}\ge e^{-U_{h,k}^{\rm joint}}.
 \end{gathered}\tag{ERJ.32b}\label{erj:metric-powers}
\]
The individual lower bound follows because each nonnegative
$-\log g_{a,j}$ is at most their full sum. All powers are of the
typed return endomorphisms in (ERJ.4), so (ERJ.11a) identifies them
with the inverse singular-value observations of the original restricted
lifts. Their action defect and theta primitive remain (ERJ.6)--(ERJ.8).
This finite bound is compatible with the central lower estimates below;
it does not assign an order-uniform bound to $U_{h,k}^{\rm joint}$.

'''

au = r'''
The signed endpoint calculation now improves this earlier central
estimate on the same original source. Retain its definitions
$\mathcal B^\Gamma_{h,k}$, $\mathfrak I_{h,k}$ and the arithmetic
endpoint terms $E_0=\log(V_{q-1}/V_q)$,
$E_1=\log(V_{2q-1}/V_{2q})$ from (FV.M1)--(FV.M11),
Section~\ref{endpoint:metric-backprop}. The exact coefficient map
$\Psi$ in (AU.2) carries its $S$ source to this $u$ source. Its
quotient coefficient map $\mathsf T_{q-1}$ sends $[P(S)]$ to
$[P(c+iu)]$; because $\Psi(\chi Q)=i^q\psi\Psi(Q)$, it has
the exact remainder identity
$J_N^u\mathsf T_N=\mathsf T_{q-1}J_N^S$.
Thus $K_N^u=\mathsf T_{q-1}K_N^S\mathsf T_{q-1}^*$ and
$V_N^u=|\det\mathsf T_{q-1}|^{-2}V_N^S=V_N^S$.
The identity is valid at both densities of the interpolation; their
literal masses, the factor $i^q$ in relation multiplication and every
raw-derivative factor $i^d$ are retained. Define
\[
 \mathcal U_k^{\rm signed}
 =\frac{\mathcal B^\Gamma_{h,k}+\mathfrak I_{h,k}-E_0-E_1}{2}.
 \tag{AU.31a}\label{au:signed-upper}
\]
Equations (AU.9) and (FV.M11) now prove $0\le C_k\le
\mathcal U_k^{\rm signed}$ by substitution, with no endpoint term
discarded. Together with the existing proved bounds this gives
\[
 \begin{aligned}
 0\le C_k\le\widehat{\mathcal U}_k:=\min\bigg\{&
 \log\det\mathsf K_{2q-1}^{\nu}-\log\det\mathsf K_q,\quad
 q\log\mathcal C_{k,q},\ \mathcal U_k,\quad
 \mathcal U_k^{\rm signed},\\
 &q\log\left(M_k\sum_{j=0}^q\tau_j\right)
  +\log\det\mathsf K_{2q-1}^{\nu}-\log\det\mathsf A_q(\tau)
 \bigg\},\qquad \tau_j>0.
 \end{aligned}\tag{AU.31b}\label{au:combined-upper}
\]
Each entry is an upper bound for the same $C_k$, respectively by
(AU.14), (AU.25), (AU.31), (FV.M11), and (AU.19).
Their minimum is therefore an upper bound; (AU.23) still gives each
interval-kernel variant with its full $T$ powers. The new signed entry
uses the actual original source moments through degree $4q$, the
relative eigenvalues and the actual projection overlap in (FV.M7).
The lower-degree arithmetic cutoff of (AU.14) is unchanged for its
own entry; it is not asserted for the new signed entry.

'''

recursive=(WORK/'recursive_endpoint_specialization.tex').read_text(encoding='utf-8')
metric=metric.replace('Finally let the two unchanged arithmetic endpoint losses be',recursive+'\nFinally let the two unchanged arithmetic endpoint losses be',1)
metric=metric.replace(r'\max\left\{0,\frac{\mathcal B^\Gamma_{h,k}-\mathfrak I_{h,k}-E_0-E_1}{2}\right\}',r'\max\left\{0,\frac{\mathcal B_{h,k}^{\rm lo}-E_0-E_1}{2}\right\}')
metric=metric.replace(r'\frac{\mathcal B^\Gamma_{h,k}+\mathfrak I_{h,k}-E_0-E_1}{2}',r'\frac{\mathcal B_{h,k}^{\rm hi}-E_0-E_1}{2}')
metric=metric.replace(r'\le\mathcal B_{h,k}\le\mathcal B^\Gamma_{h,k}+\mathfrak I_{h,k}.',r'\le\mathcal B_{h,k}\le\mathcal B_{h,k}^{\rm hi}.')
metric=metric.replace('the second uses (FV.M9) and','the second uses (FV.M18) and')
erj=erj.replace(r'$\mathfrak I_{h,k}$ as defined and completely proved in',r'$\mathfrak I_{h,k}$ and the recursively refined endpoints $\mathcal B_{h,k}^{\rm lo},\mathcal B_{h,k}^{\rm hi}$, as defined and proved in')
erj=erj.replace('(FV.M1)--(FV.M10)', '(FV.M1)--(FV.M18)')
erj=erj.replace(r'\max\{0,\mathcal B^\Gamma_{h,k}-\mathfrak I_{h,k}\}',r'\mathcal B_{h,k}^{\rm lo}')
erj=erj.replace(r'\mathcal B^\Gamma_{h,k}+\mathfrak I_{h,k}',r'\mathcal B_{h,k}^{\rm hi}')
erj=erj.replace('(FV.M9); the upper bound', '(FV.M18); the upper bound')
au=au.replace(r'$\mathcal B^\Gamma_{h,k}$, $\mathfrak I_{h,k}$ and the arithmetic',r'$\mathcal B^\Gamma_{h,k}$, $\mathfrak I_{h,k}$, the recursively refined upper endpoint $\mathcal B_{h,k}^{\rm hi}$, and the arithmetic')
au=au.replace('(FV.M1)--(FV.M11)', '(FV.M1)--(FV.M18)')
au=au.replace(r'\mathcal B^\Gamma_{h,k}+\mathfrak I_{h,k}-E_0-E_1',r'\mathcal B_{h,k}^{\rm hi}-E_0-E_1')
au=au.replace('The new signed entry\nuses', 'The new signed entry includes the actual-moment full-angle refinement and\nits nonlinear transport in (FV.M15)--(FV.M18). It uses')

targets = {}
def patch(rel, transform):
    old=(BASE/rel).read_text(encoding='utf-8')
    new=transform(old)
    assert new != old, rel
    targets[rel]=(old,new)
    path=OUT/rel
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(new,encoding='utf-8',newline='\n')

src='build/endpoint_four_volume_threshold_source.tex'
patch(src,lambda t:t.replace('Since \\(h\\) is fixed and \\(q_k\\to\\infty\\)',metric+'Since \\(h\\) is fixed and \\(q_k\\to\\infty\\)',1))
md='sources/owner_endpoint_terminal/published/workbenches/tau-arithmetic-endpoint-bounds/FOUR_VOLUME_THRESHOLD.md'
metric_md=metric.replace('\\subsubsection{The signed metric control at these same four endpoints}', '### 4a. The signed metric control at these same four endpoints')
patch(md,lambda t:t.replace('Since \\(h\\) is fixed and \\(q_k\\to\\infty\\)',metric_md+'Since \\(h\\) is fixed and \\(q_k\\to\\infty\\)',1))
md_hash=hashlib.sha256((OUT/md).read_bytes()).hexdigest()
patch('build/endpoint_four_volume_threshold_wrapper.tex',lambda t:t.replace('50cf16bc0ccd955d2dccac62b7fb8d8f08623cfe6436c4fff7374ac5ea3f3ec2',md_hash).replace('Complete owner calculation with the original arithmetic norm and volume.','Complete owner calculation with the original arithmetic norm and volume, updated at its endpoint proof by the full AW/SP signed metric control.'))
patch('tex/endpoint_restriction_join.tex',lambda t:t.replace('Set $X_0=\\max(1,M_h(b),M_h(-b))$,',erj+'Set $X_0=\\max(1,M_h(b),M_h(-b))$,',1))
patch('tex/arithmetic_volume_upper_route.tex',lambda t:t.replace('The strongest displayed\nbound retains an explicit positive matrix:', 'The original matrix\nbound retains an explicit positive matrix:',1).replace('A second\nbound uses only the supplied envelope constants and two Laplace values.', 'A second\nbound uses only the supplied envelope constants and two Laplace values.\nThe signed four-endpoint comparison is now propagated into (AU.31a)--(AU.31b);\nit retains the endpoint losses and uses actual moments through degree $4q$.',1).replace('The complete central lower estimate in the balanced-window/factor-four',au+'The complete central lower estimate in the balanced-window/factor-four',1).replace('This quantity concerns the two displayed upper and lower estimates.',r'''The propagated upper bound gives the additional actual finite gap
$0\le\widehat{\mathcal U}_k-\mathcal L_k\le
\mathcal U_k-\mathcal L_k$: the first inequality follows from
$\mathcal L_k\le C_k\le\widehat{\mathcal U}_k$, and the second from
the minimum in (AU.31b). The function in (AU.32) still concerns the
two displayed scalar upper and lower estimates.''',1))

records=[]
for rel,(old,new) in targets.items():
    marks=[]
    for n,line in enumerate(new.splitlines(),1):
        if any(s in line for s in ['\\tag{FV.M','\\tag{AU.31a','\\tag{AU.31b','\\tag{ERJ.32a','\\tag{ERJ.32b','endpoint:metric-backprop']):
            marks.append({'line':n,'text':line})
    records.append({'path':rel,'old_sha256':hashlib.sha256((BASE/rel).read_bytes()).hexdigest(),'new_sha256':hashlib.sha256((OUT/rel).read_bytes()).hexdigest(),'old_lines':len(old.splitlines()),'new_lines':len(new.splitlines()),'locators':marks})
manifest={'baseline':str(BASE),'patch_root':str(OUT),'scope':'Earlier four-volume theorem and its restriction-return and central-volume consequences. Immutable baseline not edited.','acm_source':str(ROOT/'work/rh_counterfactual_20260913/total_object/combined_original_metric_control.tex'),'acm_sha256':hashlib.sha256((ROOT/'work/rh_counterfactual_20260913/total_object/combined_original_metric_control.tex').read_bytes()).hexdigest(),'recursive_source':str(WORK.parent/'recursive_metric_transport.tex'),'recursive_sha256':hashlib.sha256((WORK.parent/'recursive_metric_transport.tex').read_bytes()).hexdigest(),'recursive_specialization_sha256':hashlib.sha256((WORK/'recursive_endpoint_specialization.tex').read_bytes()).hexdigest(),'files':records}
manifest['signed_source']=str(WORK.parent/'incoming_pr29_metric/incoming_source_metric_control.tex')
manifest['signed_sha256']=hashlib.sha256(Path(manifest['signed_source']).read_bytes()).hexdigest()
manifest['historical_five_entry_seal']=str(WORK/'historical_seals/five_entry_20260913/BASELINE_ENDPOINT_PATCH_MANIFEST.json')
manifest['signed_propagation']='FV.M16a-c retains finite signed center and convergent residual, with L_ISM=p_N>=0. FV.M17 adds the signed lower/upper entries to the existing five-bound nonlinear interval; ERJ/AU inherit, R44 states both entries.'
(WORK/'BASELINE_ENDPOINT_PATCH_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(WORK/'BASELINE_ENDPOINT_PATCH_README.md').write_text('''# Earlier endpoint calculations updated by the combined metric control

This isolated patch changes five active source paths, never the immutable 821-page baseline. The full FV.M1–18 derivation is inserted into the earlier four-volume threshold proof after (9), including the exact proper-source residual and its one-leg map. The authoritative Markdown, generated TeX body and wrapper provenance are all updated together. ERJ.32a–b carries the same budget into both return maps and their inverse powers. AU.31a–b carries it into the original central upper estimate, retaining both endpoint losses and all old envelope alternatives. The old scalar asymptotic remains explicitly attached to its original scalar bound. The recursive wave incorporates the newest RMT1–18 proof through an exact actual-measure and coefficient correspondence: its complete five-term minimum and nonlinear simultaneous interval replace the earlier two-term estimate in every downstream application while preserving that earlier proof in full. FV.M15a proves the exact trace-norm and centered-Hilbert--Schmidt additions directly in the unchanged original metric.

The original Gamma constant, arithmetic mass, monomial phases, full relation polynomial and theta primitive remain explicit. AW supplies the existing spectral estimate; SP supplies actual overlap information; ACM proves their exact same-source comparison. This patch does not label their repeated spectra as new.

Full read scope: fresh ACM.1–13 and RMT1–18; original four-volume wrapper, complete generated body and complete authoritative Markdown; complete ERJ.1–45; complete AU.1–49. No edit is proposed for the reflected fibre-product chapter because its relation/power identities are unchanged by this endpoint metric bound. ENDPOINT_CONCLUSION_REPLACEMENTS.json and its Markdown rendering contain four exact original/replacement blocks at the root-owned R44, R45 and R47 conclusion sites; this agent does not edit that shared conclusion file.

Apply only the five files listed in BASELINE_ENDPOINT_PATCH_MANIFEST.json to a new live cumulative worktree. The manifest records both prior and resulting hashes and exact inserted formula locators. Regenerating the reader must use the updated authoritative Markdown; copying only the generated TeX would lose the source update.

The final signed wave retains the constructed finite Neumann center and its exact residual from ISM31–37 and RMT19–22. FV.M16a–c proves the original-source dictionary and carries L_ISM=p_N without altering any polynomial cutoff or physical parameter. FV.M17 intersects both earlier endpoints with B_Gamma+j_p-e_p and B_Gamma+j_p+e_p. The original five-entry version is preserved under historical_seals/five_entry_20260913. A numerical integration must carry its own integration error; these are exact finite-matrix integrals, with convergence for the fixed original source pair.
''',encoding='utf-8')
print(json.dumps({'files':len(records),'manifest':str(WORK/'BASELINE_ENDPOINT_PATCH_MANIFEST.json')},indent=2))
