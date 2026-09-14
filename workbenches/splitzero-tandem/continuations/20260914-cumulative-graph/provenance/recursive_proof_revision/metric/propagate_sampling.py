exec(compile(open(r"workspace:\work\backpropagation_20260913\metric\propagate_metric.py", encoding="utf-8").read(),
             "propagate_metric.py", "exec"))
BASE=ROOT/"output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue"

sampling=r"""For $D=2q+2$, all four endpoint degrees and both generator raises
remain among these actual restrictions. The common space for the
four determinant terms themselves is $\mathcal H=\mathcal P_{2q}$.
Let $I_N:\mathcal P_N\hookrightarrow\mathcal H$ and
$I_{2q,D}:\mathcal H\hookrightarrow\mathcal P_D$ be the literal
coefficient inclusions. Restriction gives
\[
 M^{(0)}=I_{2q,D}^*M_DI_{2q,D}=M_{2q},\qquad
 M^{(1)}=I_{2q,D}^*M_D(L,J)I_{2q,D}=M_{2q}(L,J).
 \tag{PSA24a}
\]
Set $\alpha=1-\eta_{\rm per}-\eta_{\rm tail}>0$ and
$\beta=1+\eta_{\rm per}$. These two forms satisfy
$\alpha M^{(0)}\preceq M^{(1)}\preceq\beta M^{(0)}$ by
(PSA23). In this paragraph let $x\in[0,1]$ be a metric path
parameter, distinct from the physical $x_i$, and retain
\[
 M(x)=(1-x)M^{(0)}+xM^{(1)},\quad
 D_{L,J}=(M^{(0)})^{-1}M^{(1)},\quad
 C(x)=M(x)^{-1}(M^{(1)}-M^{(0)}).
 \tag{PSA24b}
\]
These are the original and actual sampled forms, rather than a
Gamma comparison. The finite algebra of the AW and SP calculations
applies through the identity of this coefficient space, with their
endpoint forms replaced by exactly $M^{(0)},M^{(1)}$.
We prove that algebra for this source here.

For $N\in\{q-1,q,2q-1,2q\}$ put
$B_N=\times\chi:\mathcal P_{N-q}\to\mathcal P_N$ and define
\[
 \begin{aligned}
 P_N(x)&=I_N(I_N^*M(x)I_N)^{-1}I_N^*M(x),\\
 Q_N(x)&=I_NB_N(B_N^*I_N^*M(x)I_NB_N)^{-1}
                             B_N^*I_N^*M(x),\\
 U(x)&=Q_{2q-1}+Q_{2q}-Q_q,\qquad Q_{q-1}=0,\\
 W(x)&=(P_{2q-1}-P_{q-1})+(P_{2q}-P_q).
 \end{aligned}
 \tag{PSA24c}
\]
Every inverse is on the displayed actual domain. For $N=q-1$
the relation domain is zero and its determinant is one.
Multiplication verifies that these are the orthogonal projections
onto the specified polynomial and relation subspaces in $M(x)$.
The degree-less-than-$q$ remainder section $s_N$ and the monic
relation columns give a frame $[s_N,B_N]$ of determinant one:
its high-degree block is triangular with diagonal one.
Block elimination in its Gram therefore gives
\[
 V_N(x)=\frac{\det(I_N^*M(x)I_N)}
                  {\det(B_N^*I_N^*M(x)I_NB_N)},\quad
 \frac{d}{dx}\log V_N(x)=\operatorname{Tr}((P_N-Q_N)C(x)).
 \tag{PSA24d}
\]
This determinant is the same quotient determinant as (PSA17)--(PSA18),
since its Schur complement is the minimum Gram over the same
remainder fibres. The derivative follows by the finite determinant
derivative and cyclicity of trace. In the relation-first orientation,
the unchanged frame has determinant $(-1)^{q(N-q+1)}$ and its
squared modulus is one, so no orientation factor has been removed.
Consequently the four original signs give
$\mathcal B'(x)=\operatorname{Tr}((U-W)C(x))$.

The flags of relation subspaces have dimensions $1,q,q+1$, and
the polynomial flag has dimensions $q,q+1,2q,2q+1$.
Nested projections act as identity or zero on successive
orthogonal pieces. Hence each of $U,W$ has eigenvalues
$0$ of multiplicity $q$, $1$ of multiplicity $2$, and $2$
of multiplicity $q-1$. Thus each has rank $q+1$, trace $2q$
and trace of the square $\operatorname{Tr}U^2=\operatorname{Tr}W^2=4q-2$.
The eigenvalue-two multiplicity is zero at $q=1$.
Let $s(x)=\dim(\operatorname{ran}U\cap\operatorname{ran}W)\ge1$,
and write $c_1(x)\le\cdots\le c_n(x)$ for the eigenvalues of
$C(x)$, $n=2q+1$, and $d(x)=c_n(x)-c_1(x)$. Define
\[
 \begin{aligned}
 S_{\rm AW}^{L,J}(x)&=c_{q+2}(x)-c_q(x)
       +2\sum_{j=1}^{q-1}(c_{2q+2-j}(x)-c_j(x)),\\
 S_{\rm SP}^{L,J}(x)&=\frac{d(x)}2\min\left\{
      4q-2s(x),\sqrt{(2q+1)(8q-4-2\operatorname{Tr}(UW))}\right\},\\
 \mathcal J_{L,J}&=\int_0^1
            \min\{S_{\rm AW}^{L,J}(x),S_{\rm SP}^{L,J}(x)\}\,dx.
 \end{aligned}
 \tag{PSA24e}
\]
For an orthogonal projection $P$ of rank $r$, its diagonal entries
in a $C(x)$-eigenbasis lie in $[0,1]$ and sum to $r$.
Moving a fixed diagonal mass from a smaller eigenvalue to a larger
one increases its trace pairing; hence
$\sum_{j=1}^rc_j\le\operatorname{Tr}(PC)
\le\sum_{j=n-r+1}^nc_j$.
Each of $U,W$ is the sum of a rank-$q+1$ range projection and a
rank-$q-1$ eigenvalue-two projection. Applying these bounds and
subtracting their full extrema yields
$|\operatorname{Tr}((U-W)C)|\le S_{\rm AW}^{L,J}$.

Let $E_L$ be the projection onto the actual intersection of the
two ranges. The positive operators $U-E_L,W-E_L$ both have trace
$2q-s(x)$, because each of $U,W$ dominates its range projection.
Thus $\|U-W\|_1\le4q-2s(x)$. Also
$\operatorname{Tr}(U-W)=0$ and
$\operatorname{Tr}((U-W)^2)=8q-4-2\operatorname{Tr}(UW)$.
Cauchy--Schwarz on its $n$ real eigenvalues gives the other
trace-norm estimate in (PSA24e).
Subtracting $(c_1+c_n)I/2$ from $C$ leaves the trace pairing
unchanged and bounds its absolute value by $d(x)\|U-W\|_1/2$,
as is seen in an orthonormal eigenbasis of $U-W$.
This proves the SP bound on the same signed derivative, and
therefore its pointwise minimum with the AW bound.
Smooth positive forms give bounded projector matrices and
continuous eigenvalues; rank strata are defined by matrix minors,
so $s(x)$ is Borel. The minimum is integrable, and integration
with its original signs gives the first bound below.

Let $b_1\le\cdots\le b_n$ be all eigenvalues of $D_{L,J}$.
The form comparison gives $\alpha\le b_j\le\beta$.
Factoring $M(x)=M^{(0)}((1-x)I+xD_{L,J})$ proves
$c_j(x)=(b_j-1)/(1-x+xb_j)$; the order follows from derivative
$(1-x+xb_j)^{-2}>0$ with respect to $b_j$.
Its integral is $\log b_j$. Therefore the full strengthened
finite-circle error, with every original source constant, is
\[
 \begin{aligned}
 |\mathcal B_{h,k}(L,J)-\mathcal B_{h,k}|
 &\le\mathcal J_{L,J}\\
 &\le\log\frac{b_{q+2}}{b_q}
       +2\sum_{j=1}^{q-1}\log\frac{b_{2q+2-j}}{b_j}\\
 &\le(2q-1)\log\frac{1+\eta_{\rm per}}
                         {1-\eta_{\rm per}-\eta_{\rm tail}}.
 \end{aligned}
 \tag{PSA25}
\]
The first quantity is also at most $\int_0^1S_{\rm SP}^{L,J}(x)\,dx$.
Each logarithmic ratio in the middle expression is at most
$\log(\beta/\alpha)$ and its coefficient total is $2q-1$.
This proves the last inequality, including the empty sum at $q=1$.
It is at most $(2q-1)\log((1+\eta)/(1-\eta))$ for
$\eta=\eta_{\rm per}+\eta_{\rm tail}$. The older bound with
coefficient $2q$ follows from this stronger estimate; the
asymmetric omitted-tail allowance is unchanged.
Fixed positive budgets still give an $O(q_k)$ error, whose
ratio to $q_k\log k$ tends to zero. No bound on the growth of
the original $\kappa_{a,D}$ or $\lambda_{p,D}$ is inserted.
The sampled values remain the exact analytic values with every
zero mode, Fourier factor and tensor source coefficient retained.
"""
source=BASE/"tex/periodized_source_intake_proofs.tex"
text=source.read_text(encoding="utf-8")
start=text.index("For $D=2q+2$, all four endpoint degrees")
end=text.index(r"\subsubsection{The finite observation map and both Laplacian boundary terms}")
text=text[:start]+sampling+"\n\n"+text[end:]
text=text.replace("PSA23--PSA25 record its source\nand determinant steps", "PSA23--PSA25 record its source\nand determinant steps, with the later AW/SP spectral and actual-overlap\ncontrol propagated through the same original and sampled coefficient maps")
save(source,Path("tex/periodized_source_intake_proofs.tex"),text,
     ["PSA24a–e exact restriction/typed projector/signed trace and full AW/SP proof", "PSA25 coefficient 2q→2q−1 and full actual minimum"])

fc=r"""For the four original endpoints, retain the same degree $D=2q+2$
used to control their two generator raises. Its literal coefficient
inclusion $I_{2q,D}:\mathcal P_{2q}\hookrightarrow\mathcal P_D$
restricts the two original forms to
$M^{(0)}=M_{2q}$ and $M^{(1)}=M_{2q}(L,J)$.
The complete signed determinant proof (PSA24a)--(PSA25) applies
through these exact restrictions and the unchanged remainder maps.
In particular it is an original/sampled comparison, with no
replacement by the Gamma density. Write $b_1\le\cdots\le b_{2q+1}$
for the eigenvalues of $D_{L,J}=(M^{(0)})^{-1}M^{(1)}$.
They lie in $[\alpha,\beta]$ by (FC5). The common-source projection
formulas in (PSA24c) use $I_NB_N:\mathcal P_{N-q}\to\mathcal P_{2q}$,
where $B_N$ itself has codomain $\mathcal P_N$; substituting
$M_N=I_N^*M(x)I_N$ proves the equality of their relation Grams.
The actual trace identity (PSA24d), full flag spectra, and retained
cross-pairings prove
\[
 \begin{aligned}
 |\mathcal B(L,J)-\mathcal B|
 &\le\mathcal J_{L,J}\\
 &\le\log\frac{b_{q+2}}{b_q}
       +2\sum_{j=1}^{q-1}\log\frac{b_{2q+2-j}}{b_j}
 \le(2q-1)\log(\beta/\alpha).
 \end{aligned}
 \tag{FC13a}
\]
Here $\mathcal J_{L,J}$ is the integral of the exact pointwise
minimum in (PSA24e). The formula and complete proof there retain
all four signs; (FC13a) substitutes the same forms and bounds
each relative ratio by $\beta/\alpha$ with total coefficient
$1+2(q-1)=2q-1$. The residue coefficient inequality (FC13) stays
dimension-free: its operator is on the quotient $E$, while
(FC13a) concerns the full source $\mathcal P_{2q}$.
The exact map between them is the minimum section
$C_N=M_N^{-1}J_N^*G_N$ from (FC7), satisfying
$J_NC_N=I_E$ and $C_N^*M_NC_N=G_N$. It therefore retains the
quotient norm and its original relation-valued sampling difference;
no equality of these two different trace functionals is assumed."""
source=BASE/"tex/periodized_curvature_control_bridge.tex"
text=source.read_text(encoding="utf-8")
text=replace_once(text,"For four original endpoints, (FC7) similarly gives the fully finite\nbound $|\\mathcal B(L,J)-\\mathcal B|\\le2q\\log(\\beta/\\alpha)$.",fc)
save(source,Path("tex/periodized_curvature_control_bridge.tex"),text,
     ["FC13a full original-sampling minimum propagated from complete PSA proof", "typed quotient/source map retains distinct commutator/residue controls"])

source=BASE/"tex/research_conclusion.tex"
text=source.read_text(encoding="utf-8")
start=text.index(r"\paragraph{Result R58:")
end=text.index(r"\paragraph{Result R59:")
old=text[start:end]
new=old.replace(r"""Their exact error is
\[
 \left|\mathcal B_{h,k}(L,J)-\mathcal B_{h,k}\right|
      \le2q\log(\beta/\alpha).
\]""",r"""On the literal common source
$\mathcal H=\mathcal P_{2q}$, restrict those degree-$D$ forms to
$M^{(0)}=M_{2q}$ and $M^{(1)}=M_{2q}(L,J)$.
The full signed derivation (PSA24a)--(PSA25) now gives the
propagated error at the original claim site:
\[
 \begin{aligned}
 \left|\mathcal B_{h,k}(L,J)-\mathcal B_{h,k}\right|
 &\le\mathcal J_{L,J}\\
 &\le\log\frac{b_{q+2}}{b_q}
       +2\sum_{j=1}^{q-1}\log\frac{b_{2q+2-j}}{b_j}
 \le(2q-1)\log(\beta/\alpha).
 \end{aligned}
\]
Here $b_1\le\cdots\le b_{2q+1}$ are the eigenvalues of
$D_{L,J}=(M^{(0)})^{-1}M^{(1)}$, all in $[\alpha,\beta]$.
For $M(x)=(1-x)M^{(0)}+xM^{(1)}$, let $P_N,Q_N$ be its
orthogonal projections onto $\mathcal P_N$ and
$\chi\mathcal P_{N-q}$ inside $\mathcal H$, and put
$U=Q_{2q-1}+Q_{2q}-Q_q$,
$W=P_{2q-1}-P_{q-1}+P_{2q}-P_q$.
Then the actual signed derivative is
$\operatorname{Tr}((U-W)M(x)^{-1}(M^{(1)}-M^{(0)}))$.
Writing $c_j(x)=(b_j-1)/(1-x+xb_j)$,
$d(x)=c_{2q+1}(x)-c_1(x)$ and
$s(x)=\dim(\operatorname{ran}U\cap\operatorname{ran}W)$,
the retained full control is
\[
 \begin{aligned}
 \mathcal J_{L,J}
 =\int_0^1\min\Bigl\{&
 c_{q+2}-c_q+2\sum_{j=1}^{q-1}(c_{2q+2-j}-c_j),\\
 &\frac{d(x)}2
   \min\{4q-2s(x),\sqrt{(2q+1)(8q-4-2\operatorname{Tr}(UW))}\}
                         \Bigr\}\,dx.
 \end{aligned}
\]
The complete proof at (PSA24a)--(PSA25) establishes these source
maps, ranks $q+1$, traces $2q$, and the exact metric comparison,
including the common-range and cross-trace terms. Its endpoint
substitution is also made in (FC13a). The two generator raises
still use the original degree $D=2q+2$.""")
assert new!=old
out=OUT/"conclusion_replacements"
out.mkdir(exist_ok=True)
(out/"R58_OLD.tex").write_text(old,encoding="utf-8")
(out/"R58_NEW.tex").write_text(new,encoding="utf-8")
(out/"R58_MAP.json").write_text(json.dumps(dict(source=str(source),
    source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    start_line=text[:start].count("\n")+1,end_line=text[:end].count("\n"),
    old_sha256=hashlib.sha256((out/"R58_OLD.tex").read_bytes()).hexdigest(),
    new_sha256=hashlib.sha256((out/"R58_NEW.tex").read_bytes()).hexdigest(),
    proof_dependencies=["PSA24a–PSA25","FC13a"]),indent=2),encoding="utf-8")
(OUT/"PATCH_MANIFEST.json").write_text(json.dumps(dict(schema="metric-backpropagation-v2",
    isolated_staging=True, original_sources_unchanged=True, rows=rows),indent=2),encoding="utf-8")
print("Completed five proof-site patches and complete R58 replacement.")
