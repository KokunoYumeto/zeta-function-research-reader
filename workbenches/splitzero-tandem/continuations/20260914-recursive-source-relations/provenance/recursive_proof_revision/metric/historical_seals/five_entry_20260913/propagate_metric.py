from pathlib import Path
import hashlib, json, difflib

ROOT = Path(r"workspace:")
OUT = ROOT / "work/backpropagation_20260913/metric"
STAGE = ROOT / "work/cumulative_next_edition_staging_20260913_v19/reader"
rows = []

def replace_once(text, old, new):
    assert text.count(old) == 1, (old[:100], text.count(old))
    return text.replace(old, new, 1)

def save(source, relative, new, claims):
    old = source.read_bytes()
    original = OUT / "originals" / relative
    revised = OUT / "staged" / relative
    original.parent.mkdir(parents=True, exist_ok=True)
    revised.parent.mkdir(parents=True, exist_ok=True)
    original.write_bytes(old)
    revised.write_text(new, encoding="utf-8", newline="\n")
    patch = OUT / "patches" / (str(relative).replace("/", "__") + ".patch")
    patch.parent.mkdir(parents=True, exist_ok=True)
    patch.write_text("".join(difflib.unified_diff(old.decode().splitlines(True), new.splitlines(True),
                        fromfile=str(source), tofile=str(revised))), encoding="utf-8")
    rows.append(dict(source=str(source), original_copy=str(original), revised=str(revised),
                     original_sha256=hashlib.sha256(old).hexdigest(),
                     revised_sha256=hashlib.sha256(revised.read_bytes()).hexdigest(),
                     patch=str(patch), claims=claims))

comparison = r"""
The reference density in (AT4) is exactly the density denoted
$r_{1/4}^{*k}$ in SP: with the retained convolution constant
$c_a=2^{1-2a}\Gamma(2a)$ one has
\[
 c_{1/4}=\sqrt{2\pi},\qquad
 r_{1/4}^{*k}(u)=\frac{c_{1/4}^{\,k}}{c_{k/4}}
       \frac{|\Gamma(k/4+iu/2)|^2}{2\pi}=m_0(u).
 \tag{AT4a}
\]
The original Gamma convolution identity therefore identifies all
moments and the mass $(2\pi)^{k/2}$, without a mass adjustment.
Writing $x=t$ and $y=u$, the precise coefficient arrow to the
common-source notation of SP is
$B_N^{\rm SP}=I_NB_N^{\rm AT}$, from $\cP_{N-q}$ to $H=\cP_{2q}$.
Consequently
\[
 (B_N^{\rm SP})^*M_*B_N^{\rm SP}=B_N^*M_NB_N,\qquad
 Q_N^{\rm SP}=I_NB_NH_N^{-1}B_N^*I_N^*M_*=Q_N.
 \tag{AT4b}
\]
These identities follow from $M_N=I_N^*M_*I_N$. They include the
zero relation domain, where all compositions are zero.
"""

at_new = r"""\subsection{The full spectral and actual-overlap bound for the correction}

Let $n=2q+1$ and let $b_1\le\cdots\le b_n$ be all eigenvalues of
$D_*=M_*(0)^{-1}M_*(1)$ in its original $M_*(0)$ inner product.
This operator is positive because
$v^*M_*(0)D_*v=v^*M_*(1)v>0$ for $v\ne0$.
Retain $\kappa_*=b_n/b_1$ and put
\[
 \begin{aligned}
 c_j(t)&=\frac{b_j-1}{1-t+tb_j},&
 d(t)&=c_n(t)-c_1(t),\\
 \mathcal L_q(D_*)&=\log\frac{b_{q+2}}{b_q}
       +2\sum_{j=1}^{q-1}\log\frac{b_{2q+2-j}}{b_j},\\
 S_{\rm AW}(t)&=c_{q+2}(t)-c_q(t)
       +2\sum_{j=1}^{q-1}(c_{2q+2-j}(t)-c_j(t)),\\
 s(t)&=\dim(\operatorname{ran}U(t)\cap\operatorname{ran}W(t)),\\
 S_{\rm SP}(t)&=\frac{d(t)}2\min\left\{
       4q-2s(t),\sqrt{(2q+1)(8q-4-2\Tr(U(t)W(t)))}\right\},\\
 \mathcal J_{h,k}&=\int_0^1\min\{S_{\rm AW}(t),S_{\rm SP}(t)\}\,dt.
 \end{aligned}
 \tag{AT18a}
\]
An empty sum for $q=1$ is zero. Every quantity uses the unchanged
common source $H=\cP_{2q}$ and the actual relation maps in (AT11).
The complete spectra and $\mathcal L_q$ bound were proved in
AW7 and AW13--AW16; the actual overlap terms were proved in
SP8--SP10. Their full proofs are propagated here to the original
endpoint estimate, so neither calculation is replaced by a reference.

\begin{theorem}
The exact correction on the original finite source satisfies
\[
 \boxed{|\Delta\mathcal B|\le\mathcal J_{h,k}
       \le\mathcal L_q(D_*)\le(2q-1)\log\kappa_*.}
 \tag{AT18}
\]
Moreover $\mathcal J_{h,k}\le\int_0^1S_{\rm SP}(t)\,dt$. The
original Gamma and arithmetic endpoint quantities consequently obey
\[
 \mathcal B^\Ga_{h,k}-\mathcal J_{h,k}
 \le\mathcal B^\ar_{h,k}
 \le\mathcal B^\Ga_{h,k}+\mathcal J_{h,k}.
 \tag{AT19}
\]
\end{theorem}
\begin{proof}
The relation flag
$\chi\cP_0\subset\chi\cP_{q-1}\subset\chi\cP_q\subset H$
has dimensions $1,q,q+1,2q+1$. On its successive orthogonal
pieces the operator $U=Q_{2q-1}+Q_{2q}-Q_q$ has values
$1,2,1,0$ with multiplicities $1,q-1,1,q$.
On the orthogonal pieces of
$\cP_{q-1}\subset\cP_q\subset\cP_{2q-1}\subset H$,
$W$ has values $0,1,2,1$ with multiplicities $q,1,q-1,1$.
Nested orthogonal projections act as identity or zero on these
pieces, which proves the assertions including $q=1$. In particular
\[
 \begin{gathered}
 \operatorname{rank}U=\operatorname{rank}W=q+1,\quad
 \Tr U=\Tr W=2q,\quad \Tr U^2=\Tr W^2=4q-2,\\
 A=U-W,\qquad \Tr A=0,\qquad
 \Tr A^2=8q-4-2\Tr(UW).
 \end{gathered}
 \tag{AT20a}
\]
Thus the equal mass $2q$ is an operator trace, and its multiplicity-two
subspace of dimension $q-1$ is retained in each rank calculation.

The identity $M_*C=\Delta M_*=\Delta M_*^*$ proves that $C$ is
self-adjoint in $M_*(t)$. The exact factorization
$M_*(t)=M_*(0)((1-t)I+tD_*)$ gives
$C=((1-t)I+tD_*)^{-1}(D_*-I)$. A basis of $M_*(0)$-orthonormal
eigenvectors of $D_*$ remains orthogonal in $M_*(t)$, with positive
squared lengths $1-t+tb_j$, proving that the displayed $c_j(t)$
are its eigenvalues. Differentiation in $b_j$ gives
$(1-t+tb_j)^{-2}>0$, so they retain their order.

For any $M_*(t)$-orthogonal projection $P$ of rank $r$, choose an
orthonormal eigenbasis $e_j$ of $C$. Its diagonal values
$a_j=\langle e_j,Pe_j\rangle$ lie in $[0,1]$ and sum to $r$.
Thus $\Tr(PC)=\sum_jc_ja_j$ lies between the sum of the smallest
$r$ and the sum of the largest $r$ eigenvalues: moving a fixed
amount of mass from a smaller coefficient to a larger coefficient
increases the sum, until these two extrema are obtained. This also
proves the assertion when there are ties. Either $Z=U$ or $Z=W$
is the sum of its range projection of rank $q+1$ and its
eigenvalue-two projection of rank $q-1$. Applying the just-proved
inequality gives
\[
 \sum_{j=1}^{q+1}c_j+\sum_{j=1}^{q-1}c_j
 \le\Tr(ZC)\le
 \sum_{j=q+1}^{2q+1}c_j+\sum_{j=q+3}^{2q+1}c_j.
 \tag{AT20b}
\]
Subtracting the extrema for the two original operators, retaining
both sums before their common middle term cancels, proves
$|\Tr(AC)|\le S_{\rm AW}(t)$.

Both ranges have dimension $q+1$ in dimension $2q+1$; hence
$s(t)\ge1$. Let $E_L$ be the orthogonal projection onto their
intersection. Each of $U,W$ dominates its range projection, since
its nonzero eigenvalues are $1,2$; that projection dominates $E_L$.
Therefore $U-E_L,W-E_L$ are positive, of trace $2q-s(t)$, and
\[
 \|A\|_1\le4q-2s(t),\qquad
 \|A\|_1\le\sqrt{(2q+1)\Tr A^2}.
 \tag{AT20c}
\]
The first inequality is the trace-norm triangle inequality applied
to their difference. The second is Cauchy--Schwarz on all $2q+1$
real eigenvalues of $A$. Subtracting the midpoint
$a=(c_1+c_n)/2$ from $C$ leaves $\Tr(AC)$ unchanged by $\Tr A=0$.
In an orthonormal eigenbasis $f_j$ of $A$ with eigenvalues $\alpha_j$,
$|\Tr(A(C-aI))|\le\sum_j|\alpha_j|
|\langle f_j,(C-aI)f_j\rangle|\le d(t)\|A\|_1/2$.
Together with (AT20a)--(AT20c), this proves the full pointwise bound
\[
 |\Tr((U-W)C)|\le\min\{S_{\rm AW}(t),S_{\rm SP}(t)\}.
 \tag{AT20}
\]
No pairwise commutation of $U,W,C$ has been used.
The Gram inverses and projectors are smooth on the compact
interval; their ranks and intersection dimensions are Borel,
since ranks are specified by vanishing and nonvanishing minors.
All terms are bounded, hence the displayed minimum is integrable.
Integrating (AT20) in (AT15) gives the first assertion of (AT18).

For each retained relative eigenvalue,
\[
 \int_0^1 c_j(t)\,dt=\log b_j,\qquad
 \int_0^1d(t)\,dt=\log(b_n/b_1)=\log\kappa_*.
 \tag{AT21}
\]
This follows by differentiating $\log(1-t+tb_j)$; it includes
$b_j=1$, whose integrand is zero. Thus
$\int S_{\rm AW}=\mathcal L_q(D_*)$ and
$\mathcal J_{h,k}\le\int S_{\rm SP}$. Each ratio in
$\mathcal L_q$ is at most $\kappa_*$; the retained total
coefficient is $1+2(q-1)=2q-1$. This proves all inequalities.
Finally (AT19) follows by applying the two signs of the first
bound to the exact equality
$\mathcal B^\ar_{h,k}=\mathcal B^\Ga_{h,k}+\Delta\mathcal B$.
\end{proof}

When $M_*(1)=cM_*(0)$, every $b_j=c$, so $d=0$ and
$\mathcal J_{h,k}=0$. The original quotient determinants are
$(1-t+tc)^qV_N(0)$, whose four factors cancel exactly in (AT14).
This retains both original masses. For an invertible coefficient
arrow $F:H'\to H$, let $M_*'=F^*M_*F$ and transport every subspace
by $F^{-1}$. The projector formula gives
$P_N'=F^{-1}P_NF$, $Q_N'=F^{-1}Q_NF$,
$D_*'=F^{-1}D_*F$, and $C'=F^{-1}CF$.
Their spectra, intersection dimensions, $\Tr(UW)$, the signed
trace and $\mathcal J_{h,k}$ consequently agree under this exact map.

For the original reflection-stable quartet with displacement
$\delta>0$ and multiplicity $m$, retain
$q=[1+k(m-1)](k+1)^2$. Its supplied Gamma theorem gives
$\mathcal B^\Ga_{h,k}\ge4q\log(\delta k/(2\sqrt5))$.
Applying (AT19) with its actual sign proves
\[
 \begin{aligned}
 \mathcal B^\ar_{h,k}
 &\ge4q\log\!\left(\frac{\delta k}{2\sqrt5}\right)
                     -\mathcal J_{h,k}\\
 &\ge4q\log\!\left(\frac{\delta k}{2\sqrt5}\right)
                     -\mathcal L_q(D_*)\\
 &\ge4q\log\!\left(\frac{\delta k}{2\sqrt5}\right)
                     -(2q-1)\log\kappa_*,\\
 \log\kappa_*&\ge
  \frac{4q\log(\delta k/(2\sqrt5))-\mathcal B^\ar_{h,k}}{2q-1}.
 \end{aligned}
 \tag{AT22}
\]
The last denominator is positive for every $q\ge1$. This is the
same actual packet application, with its earlier necessary
condition updated to the stronger proved finite control.
No existence of such a quartet or uniform growth bound is assumed.
The full signed formulas (AT15)--(AT17), all source primitives and
the retained cohomology observations remain the objects whose
moments and actual overlaps enter the bound.

"""

source=STAGE/"tex/next_edition/AT_complete.tex"
text=source.read_text(encoding="utf-8")
text=replace_once(text, r"\subsection{Canonical sections, determinant lines and full variations}",
                  comparison+"\n"+r"\subsection{Canonical sections, determinant lines and full variations}")
start=text.index(r"\subsection{An exact finite-source bound for the correction}")
end=text.index(r"\subsection{Source dependencies and precise status}")
text=text[:start]+at_new+text[end:]
save(source, Path("tex/next_edition/AT_complete.tex"), text,
     ["AT4a–b exact density and typed relation inclusion", "AT18–22 complete strengthened proof and quartet consequence"])

aw_insert=r"""
Retain also the actual polynomial-space overlap. At each $t$, let
$s(t)=\dim(\operatorname{ran}U\cap\operatorname{ran}W)$ and
$d(t)=c_n(t)-c_1(t)$. With the actual $c_j(t)$ of (AW17), set
\[
 \begin{aligned}
 S_{\rm AW}(t)&=c_{q+2}-c_q+
          2\sum_{j=1}^{q-1}(c_{2q+2-j}-c_j),\\
 S_{\rm SP}(t)&=\frac{d(t)}2\min\left\{4q-2s(t),
       \sqrt{(2q+1)(8q-4-2\Tr(UW))}\right\},\\
 \mathcal J_{h,k}&=\int_0^1\min\{S_{\rm AW}(t),S_{\rm SP}(t)\}\,dt.
 \end{aligned}
 \tag{AW13a}
\]
The overlap refinement from SP8--SP10 is transported to this
earlier calculation by the exact arrows
$x=t$, $y=u$, $B_N^{\rm SP}=I_NB_N^{\rm AW}$.
Indeed $M_N=I_N^*MI_N$ gives
$(B_N^{\rm SP})^*MB_N^{\rm SP}=B_N^*M_NB_N$, so its projectors
are precisely (AW4), and $(\mathcal R^{\rm SP},\mathcal P^{\rm SP},
T^{\rm SP})=(U,W,C)$. The original Gamma densities agree because
$r_{1/4}^{*k}=c_{1/4}^{\,k}r_{k/4}/c_{k/4}$ with
$c_{1/4}=\sqrt{2\pi}$, exactly (AW3). The arithmetic densities
already coincide as $w_h^{*k}$. Thus this comparison preserves
the moments, masses, polynomial coefficients and all four endpoint signs.
"""
aw_proof=r"""
The range dimensions in (AW7) give $s(t)\ge1$. Let $E_L$ be the
orthogonal projector onto their intersection. Each $Z=U,W$ is
at least its range projection, since its nonzero eigenvalues are
$1,2$, and therefore $Z-E_L$ is positive of trace $2q-s(t)$.
Writing $A=U-W=(U-E_L)-(W-E_L)$ proves
\[
 \|A\|_1\le4q-2s(t),\quad
 \Tr A=0,\quad
 \Tr A^2=8q-4-2\Tr(UW),\quad
 \|A\|_1\le\sqrt{(2q+1)\Tr A^2}.
 \tag{AW16a}
\]
The square identity uses $\Tr U^2=\Tr W^2=4q-2$ and cyclicity.
The last inequality is Cauchy--Schwarz on every real eigenvalue of
the self-adjoint $A$. Subtracting $(c_1+c_n)I/2$ from $C$
does not change its trace pairing with $A$. In an orthonormal
eigenbasis of $A$, that pairing is bounded in absolute value by
$d(t)\|A\|_1/2$. This proves
$|\Tr((U-W)C)|\le S_{\rm SP}(t)$ in addition to (AW16),
and hence bounds it by their pointwise minimum. Smooth positive
Grams give bounded continuous eigenvalues and overlaps;
$s(t)$ is Borel because its rank strata are specified by matrix
minors. Therefore the minimum is integrable. The signed identity
(AW6) now proves $|\Delta\mathcal B|\le\mathcal J_{h,k}$ and
$\mathcal J_{h,k}\le\int S_{\rm SP}$.
"""
source=STAGE/"tex/next_edition/AW_complete.tex"
text=source.read_text(encoding="utf-8")
text=replace_once(text,r"\begin{theorem}"+ "\nOn the unchanged arithmetic source,",aw_insert+"\n"+r"\begin{theorem}"+"\nOn the unchanged arithmetic source,")
text=replace_once(text,r"|\Delta\mathcal B|\le\mathcal L_q(D)",r"|\Delta\mathcal B|\le\mathcal J_{h,k}\le\mathcal L_q(D)")
text=replace_once(text,"In particular the coefficient $2q$ in AT18 can be improved to\n$2q-1$, while the first bound retains the full relative spectrum.",
                  "The previously proved coefficient $2q-1$ and full relative-spectrum\nbound are retained. The pointwise minimum additionally preserves the\nactual polynomial-space overlap, and is at most $\\int_0^1S_{\\rm SP}(t)\\,dt$.")
text=replace_once(text,"No mutual commutation of $U,W,C$ is used.","No mutual commutation of $U,W,C$ is used.\n"+aw_proof)
text=replace_once(text,"Integrating (AW16) in the exact signed identity (AW6) proves\nthe first inequality of (AW14).",
                  "Integrating (AW16) proves $\\mathcal J_{h,k}\\le\\mathcal L_q(D)$;\nthe preceding pointwise-minimum argument proves the first inequality\nof (AW14).")
text=replace_once(text,r"-\mathcal L_q(D)."+"\n"+r" \tag{AW18}",r"-\mathcal J_{h,k}."+"\n"+r" \tag{AW18}")
text=replace_once(text,"This is substitution of the complete supplied Gamma theorem\ninto the proved first inequality of (AW14).",
                  "This is substitution of the complete supplied Gamma theorem\ninto the proved first inequality of (AW14). It retains the stronger\nactual overlap bound, and also implies the earlier lower bounds with\n$-\\mathcal L_q(D)$ and $-(2q-1)\\log\\kappa(D)$ respectively.")
save(source,Path("tex/next_edition/AW_complete.tex"),text,
     ["AW13a density/codomain comparison and overlap definition", "AW14/AW16a complete pointwise-minimum proof", "AW18 strengthened quartet endpoint"])

sp_prefix=r"""
The precise arrow to the earlier AW source keeps $H$ and every
coefficient fixed, sends $t_{\rm AW}$ to $x$ and $u_{\rm AW}$ to $y$,
and sends the relation map by
$B_N^{\rm SP}=I_NB_N^{\rm AW}:\mathcal P_{N-q}\to H$.
The Gamma convolution constant is
$c_a=2^{1-2a}\Gamma(2a)$, so
\[
 r_{1/4}^{*k}(y)
 =\frac{c_{1/4}^{\,k}}{c_{k/4}}
             \frac{|\Gamma(k/4+iy/2)|^2}{2\pi},\qquad
 c_{1/4}=\sqrt{2\pi}.
 \tag{SP1a}
\]
This is exactly AW3, including its mass $(2\pi)^{k/2}$; both
arithmetic densities are $w_h^{*k}$ with mass $\mu_h^k$.
Thus $M_x=M_{\rm AW}(x)$, and
$(B_N^{\rm SP})^*M_xB_N^{\rm SP}=(B_N^{\rm AW})^*M_NB_N^{\rm AW}$
with $M_N=I_N^*M_xI_N$.
"""
sp_full=r"""
The complete earlier AW13--AW16 bound applies to this same
source through $(U,W,C)=(\mathcal R_x,\mathcal P_x,T_x)$.
Write $c_1(x)\le\cdots\le c_{2q+1}(x)$ for all eigenvalues of
$T_x$ in $M_x$ and define
\[
 S_{\rm AW}(x)=c_{q+2}(x)-c_q(x)
       +2\sum_{j=1}^{q-1}(c_{2q+2-j}(x)-c_j(x)),\qquad
 S_{\rm SP}(x)=\text{the right-hand side of (SP10)}.
 \tag{SP10a}
\]
Here is the complete retained spectral proof. For an orthogonal
projection $P$ of rank $r$, its diagonal values $a_j$ in an
orthonormal eigenbasis of $T_x$ satisfy $0\le a_j\le1$ and
$\sum_j a_j=r$. Thus $\operatorname{Tr}(PT_x)=\sum_jc_ja_j$
is at least the sum of the smallest $r$ and at most the sum of
the largest $r$ eigenvalues: moving a fixed diagonal mass from
a smaller coefficient to a larger one increases this sum.
Either $Z=\mathcal R_x$ or $Z=\mathcal P_x$ equals its range
projection, of rank $q+1$, plus its eigenvalue-two projection,
of rank $q-1$. Therefore
\[
 \sum_{j=1}^{q+1}c_j+\sum_{j=1}^{q-1}c_j
 \le\operatorname{Tr}(ZT_x)\le
 \sum_{j=q+1}^{2q+1}c_j+\sum_{j=q+3}^{2q+1}c_j.
 \tag{SP10b}
\]
Subtracting the two extrema with their exact multiplicities gives
$|F'(x)|\le S_{\rm AW}(x)$. Combining this bound with SP10 before
integration proves
\[
 |F'(x)|\le\min\{S_{\rm AW}(x),S_{\rm SP}(x)\}.
 \tag{SP10c}
\]
Positive smooth Gram matrices make the eigenvalues and overlaps
bounded on $[0,1]$; $s_x$ is Borel since its rank strata are
given by matrix minors. Hence the right side is integrable.
The original source isometry of AW10 also yields the exact
commutator identity
$F'=\operatorname{Tr}(W(T^{\rm iso})^{-1}[C,T^{\rm iso}])$.
It follows from $U=T^{\rm iso}W(T^{\rm iso})^{-1}$ and cyclicity,
with $T^{\rm iso}$ the explicit isometry and $C=T_x$ the metric
derivative. Its full original observation remains
$\mathcal O=\sigma_h^{\otimes k}\eta J_{2q}$ and has exact defect
$\mathcal OT^{\rm iso}-\mathcal O
=\sigma_h^{\otimes k}\eta J_{2q}(T^{\rm iso}-I)$ and kernel
$\ker(\mathcal OT^{\rm iso})=(T^{\rm iso})^{-1}(\chi\mathcal P_q)$.
The defect follows by expansion and the kernel follows from
injectivity of $\sigma_h^{\otimes k}\eta$ and
$\ker J_{2q}=\chi\mathcal P_q$. Thus no additional
cohomology-intertwining property of the metric isometry is used.
"""
source=ROOT/"work/tau_signed_projection_control_20260913.tex"
text=source.read_text(encoding="utf-8")
text=replace_once(text,"self-adjoint in the \\(M_x\\) inner product. It is not asserted positive.",
                  r"""self-adjoint in the \(M_x\) inner product. Its exact relation to
the positive \(M_0\)-self-adjoint operator \(R=M_0^{-1}M_1\) is
\(T_x=(I+x(R-I))^{-1}(R-I)\), obtained by factoring
\(M_x=M_0(I+x(R-I))\). Thus its eigenvalues are
\((r-1)/(1+x(r-1))\) for the positive eigenvalues \(r\) of \(R\),
with their actual signs retained."""+"\n"+sp_prefix)
text=replace_once(text,r"\subsection{Ranks, multiplicities and the retained overlap}",
                  r"""\subsection{Ranks, multiplicities and the retained overlap}
The following complete spectra and the final condition-number
coefficient were already established in AW7 and AW14. They are
retained here with the exact source correspondence above; the
actual cross-trace and intersection terms supply the added refinement.
""")
text=replace_once(text,"There is a closed integrated bound.",sp_full+"\nThere is a closed integrated bound.")
start=text.index("Combining SP7--SP12 proves")
end=text.index("SP1--SP13 give finite two-sided control")
text=text[:start]+r"""Write \(r_1\le\cdots\le r_{2q+1}\) for all positive eigenvalues
of \(R\), and retain
\[
 \mathcal L_q(R)=\log\frac{r_{q+2}}{r_q}
       +2\sum_{j=1}^{q-1}\log\frac{r_{2q+2-j}}{r_j}.
\]
The ordered form of SP11 gives
\(c_j(x)=(r_j-1)/(1+x(r_j-1))\) and
\(\int_0^1c_j(x)\,dx=\log r_j\). Therefore SP7--SP12 and the
full spectral proof above give both original-source controls
\[
 \begin{gathered}
 \boxed{|\Delta_{h,k}|
 \le\int_0^1\min\{S_{\rm AW}(x),S_{\rm SP}(x)\}\,dx
 \le\mathcal L_q(R)
 \le(2q-1)\log\frac{r_{\max}}{r_{\min}},}\\
 |\Delta_{h,k}|
 \le\frac12\int_0^1d_x\|\mathcal R_x-\mathcal P_x\|_1\,dx
 \le(2q-1)\log\frac{r_{\max}}{r_{\min}}.
 \end{gathered}
 \tag{SP13}
\]
The first integral is also at most \(\int_0^1S_{\rm SP}(x)\,dx\).
Every logarithmic ratio in \(\mathcal L_q\) is bounded by
\(\log(r_{\max}/r_{\min})\), with coefficient total
\(1+2(q-1)=2q-1\); this proves the last inequality explicitly.
The two displayed integral bounds each remain available: no
ordering between the exact trace norm and the spectral refinement
is assumed. When the Grams are proportional, every \(c_j\) agrees,
both bounds are zero, and the correction is exactly zero without
rescaling their original masses.

""" +text[end:]
save(source,Path("tex/tau_signed_projection_control.tex"),text,
     ["SP1 exact positive-relative-operator morphism", "SP1a Gamma/B_N source map", "SP8 AW priority", "SP10a–c complete spectral/commutator proof", "SP13 pointwise-minimum endpoint"])

(OUT/"PATCH_MANIFEST.json").write_text(json.dumps(dict(schema="metric-backpropagation-v1",
    isolated_staging=True, original_sources_unchanged=True, rows=rows), indent=2), encoding="utf-8")
print(json.dumps(rows,indent=2))
