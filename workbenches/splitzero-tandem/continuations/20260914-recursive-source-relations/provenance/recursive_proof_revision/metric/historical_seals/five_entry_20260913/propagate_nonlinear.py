exec(compile(open(r"workspace:\work\backpropagation_20260913\metric\propagate_sampling.py", encoding="utf-8").read(),
             "propagate_sampling.py", "exec"))

def edit_row(rel,new,claim):
    global rows
    current=next(r for r in rows if Path(r["revised"])==OUT/"staged"/rel)
    rows=[r for r in rows if r is not current]
    save(Path(current["source"]),Path(rel),new,current["claims"]+[claim])

at=(OUT/"staged/tex/next_edition/AT_complete.tex").read_text()
bridge=r"""
The original-moment angle calculation supplies a further simultaneous
bound at this same claim site. Put $a_q=2q-1$ and
\[
 \begin{aligned}
 A_{h,k}(t)&=a_q\sqrt{1-e^{-\mathcal B(t)/a_q}}\,d(t),\\
 \mathcal J_{h,k}^{(3)}
   &=\int_0^1\min\{S_{\rm AW}(t),S_{\rm SP}(t),A_{h,k}(t)\}\,dt,\\
 \mathcal I_{h,k}
   &=\int_0^1\min\left\{d(t),
   \frac{S_{\rm AW}(t)}{a_q\sqrt{1-e^{-\mathcal B(t)/a_q}}},
   \frac{S_{\rm SP}(t)}{a_q\sqrt{1-e^{-\mathcal B(t)/a_q}}}\right\}\,dt .
 \end{aligned}
 \tag{AT18b}
\]
These specialize RMT1--RMT18 through $a_{\rm RMT}=a_q$, $x=t$, $C_x=C(t)$ and
$(U_x,W_x)=(U(t),W(t))$. The density and relation arrows were
proved in (AT4a)--(AT4b), so every source moment and original
cohomology map agrees. This application uses the actual moment
measures (AT4)--(AT5). It does not impose moment structure on an
arbitrary positive coefficient Gram.
"""
at=replace_once(at,r"\begin{theorem}"+"\nThe exact correction on the original finite source satisfies",bridge+"\n"+r"\begin{theorem}"+"\nThe exact correction on the original finite source satisfies")
at=replace_once(at,r"\boxed{|\Delta\mathcal B|\le\mathcal J_{h,k}",r"\boxed{|\Delta\mathcal B|\le\mathcal J_{h,k}^{(3)}\le\mathcal J_{h,k}")
at=replace_once(at,r"\mathcal B^\Ga_{h,k}-\mathcal J_{h,k}",r"\mathcal B^\Ga_{h,k}-\mathcal J_{h,k}^{(3)}")
at=replace_once(at,r"\le\mathcal B^\Ga_{h,k}+\mathcal J_{h,k}.",r"\le\mathcal B^\Ga_{h,k}+\mathcal J_{h,k}^{(3)}.")
at=replace_once(at,"Integrating (AT20) in (AT15) gives the first assertion of (AT18).",
 r"""Integrating (AT20) in (AT15) gives
$|\Delta\mathcal B|\le\mathcal J_{h,k}$ for these two positive
forms, even without moment structure. On the actual measures,
RMT11 retains the two full $q$-angle lists of the crossed pairs
$(q-1,2q)$ and $(q,2q-1)$, including the designated zero angle,
and proves $|\mathcal B'|\le A_{h,k}$.
Its strict positivity proof applies here: if $\mathcal B=0$,
the first pair has identical minimum sections, putting $1$ in
the orthogonal complement of $\chi\mathcal P_q$. The polynomial
$\chi^{\#_k}(S)=\sum_j\overline{\chi_j}(k-S)^j$ then gives
$0=\int\chi\chi^{\#_k}\,dm_t=\int|\chi|^2\,dm_t$, contradicting
the positive original Gram of $\chi$. Thus $\mathcal B(t)>0$.
RMT11 follows from its complete original angle proof and concavity
of $\sqrt{1-e^{-z}}$ on the retained $a_q$-entry scalar list.
Applying all three inequalities to this same derivative proves
$|\Delta\mathcal B|\le\mathcal J_{h,k}^{(3)}\le\mathcal J_{h,k}$.
Compactness and the positive continuous $\mathcal B$ make every
denominator in (AT18b) nonzero and bounded away from zero.""")
at=replace_once(at,r"Finally (AT19) follows by applying the two signs of the first",
 r"Finally (AT19) follows by applying the two signs of the three-bound")
at=replace_once(at,r"                     -\mathcal J_{h,k}\\",r"                     -\mathcal J_{h,k}^{(3)}\\")
nonlinear=r"""
The same actual-moment calculation also propagates to the nonlinear
endpoint coordinate. Set
$\mathscr H_{a_q}(B)=2\operatorname{arcosh}(e^{B/(2a_q)})$ and
$H_0=\mathscr H_{a_q}(\mathcal B^\Ga_{h,k})$.
Its exact derivative is
$\mathscr H_{a_q}'(B)=1/(a_q\sqrt{1-e^{-B/a_q}})$ and its continuous
inverse is $2a_q\log\cosh(z/2)$ for $z\ge0$.
The positivity just proved permits the chain rule throughout this
fixed path. Dividing the three derivative bounds by their positive
factor and integrating gives
$|\mathscr H_{a_q}(\mathcal B^\ar_{h,k})-H_0|
\le\mathcal I_{h,k}\le\log\kappa_*$.
Consequently the existing interval (AT19) has the simultaneous
strengthening
\[
 \begin{aligned}
 \mathcal B^\ar_{h,k}&\ge
 \max\left\{0,\mathcal B^\Ga_{h,k}-\mathcal J_{h,k}^{(3)},
 2a_q\log\cosh\frac{\max\{0,H_0-\mathcal I_{h,k}\}}2\right\},\\
 \mathcal B^\ar_{h,k}&\le
 \min\left\{\mathcal B^\Ga_{h,k}+\mathcal J_{h,k}^{(3)},
 2a_q\log\cosh\frac{H_0+\mathcal I_{h,k}}2\right\}.
 \end{aligned}
 \tag{AT19a}
\]
Every inverse and sign is the original RMT16--RMT18 calculation
on the forms already specified in AT; the scalar continuous value
at zero bounds an actual strictly positive endpoint.
"""
at=replace_once(at,"When $M_*(1)=cM_*(0)$,",nonlinear+"\nWhen $M_*(1)=cM_*(0)$,")
edit_row(Path("tex/next_edition/AT_complete.tex"),at,"RMT actual-moment specialization AT18b/19a and tighter AT18/19/22 at existing claims")

aw=(OUT/"staged/tex/next_edition/AW_complete.tex").read_text()
awbridge=bridge.replace("AT18b","AW13b").replace("S_{\\rm AW}(t)","S_{\\rm AW}(t)").replace("(AT4a)--(AT4b)","(AW3)--(AW4) and (AW13a)").replace("(AT4)--(AT5)","(AW3)").replace("AT","AW")
aw=replace_once(aw,r"\begin{theorem}"+"\nOn the unchanged arithmetic source,",awbridge+"\n"+r"\begin{theorem}"+"\nOn the unchanged arithmetic source,")
aw=replace_once(aw,r"|\Delta\mathcal B|\le\mathcal J_{h,k}\le\mathcal L_q(D)",r"|\Delta\mathcal B|\le\mathcal J_{h,k}^{(3)}\le\mathcal J_{h,k}\le\mathcal L_q(D)")
aw=replace_once(aw,r"$|\Delta\mathcal B|\le\mathcal J_{h,k}$ and",r"$|\Delta\mathcal B|\le\mathcal J_{h,k}$ and")
aw=replace_once(aw,r"$\mathcal J_{h,k}\le\int S_{\rm SP}$.",
 r"""$\mathcal J_{h,k}\le\int S_{\rm SP}$.
For the original moment path, the exact original-source identification
above also applies RMT11--RMT12: its full crossed angle lists give
$|\mathcal B'|\le A_{h,k}$, and $\mathcal B>0$ follows because
otherwise $1\perp\chi\mathcal P_q$ would force
$\int|\chi|^2m_t=0$ by the reflected polynomial
$\chi^{\#_k}(S)=\sum_j\overline{\chi_j}(k-S)^j$.
Taking the pointwise minimum of this additional proved inequality
with (AW16) and (AW16a) gives
$|\Delta\mathcal B|\le\mathcal J_{h,k}^{(3)}$.
The complete proof of the original angle estimate and its exact
chain-rule continuation is retained in EP and RMT; it uses
AW's earlier projection identities, not the final claim (AW14).""")
aw=replace_once(aw,r"-\mathcal J_{h,k}."+"\n"+r" \tag{AW18}",r"-\mathcal J_{h,k}^{(3)}."+"\n"+r" \tag{AW18}")
aw=replace_once(aw,"The preceding pointwise-minimum argument proves the first inequality",
                  "The preceding three-bound argument proves the first inequality") if "The preceding pointwise-minimum argument proves the first inequality" in aw else aw
aw=replace_once(aw,r"       \le\log(b_3/b_1)."+"\n"+r" \tag{AW22}",r"       \le\mathcal I_{h,k}\le\log(b_3/b_1)."+"\n"+r" \tag{AW22}")
aw=replace_once(aw,r"and $L=\tfrac12\log(b_3/b_1)$, monotonicity of",r"and $L=\mathcal I_{h,k}/2\le\tfrac12\log(b_3/b_1)$, monotonicity of")
aw=replace_once(aw,"Divide (AW21) by its positive square-root factor and\nintegrate (AW17).",
 r"""Divide (AW21) by its positive square-root factor. The two
independent inequalities (AW16) and (AW16a) can be divided by
that same factor because $q=1$ gives $a_q=1$ and $\mathcal B>0$.
Their pointwise minimum integrates to $\mathcal I_{h,k}$ in
(AW13b); integration of (AW17) bounds it by $\log(b_3/b_1)$.""")
edit_row(Path("tex/next_edition/AW_complete.tex"),aw,"RMT actual-moment AW13b, tighter AW14/AW18 and propagated q1 AW22–23")

sp=(OUT/"staged/tex/tau_signed_projection_control.tex").read_text()
spapp=r"""
On the original moment source (SP1a), the later angle calculation
propagates further at this endpoint. With $a_q=2q-1$ define
\[
 \begin{aligned}
 A(x)&=a_q\sqrt{1-e^{-F(x)/a_q}}\,d_x,\\
 J^{(3)}&=\int_0^1\min\{S_{\rm AW}(x),S_{\rm SP}(x),A(x)\}\,dx,\\
 I&=\int_0^1\min\left\{d_x,
 \frac{S_{\rm AW}(x)}{a_q\sqrt{1-e^{-F(x)/a_q}}},
 \frac{S_{\rm SP}(x)}{a_q\sqrt{1-e^{-F(x)/a_q}}}\right\}\,dx .
 \end{aligned}
 \tag{SP13a}
\]
The exact map to RMT is $a_{\rm RMT}=a_q$, $F=\mathcal B$, $T_x=C_x$ and
$(\mathcal R_x,\mathcal P_x)=(U_x,W_x)$, with the same original
moment measures by SP1a. RMT11--RMT12 proves $F>0$ and
$|F'|\le A$: its full two angle lists keep the designated zero
angle, and vanishing $F$ would imply $1\perp\chi\mathcal P_q$,
contradicting $\int|\chi|^2\,d\mu_x>0$ through
$\chi^{\#_k}(S)=\sum_j\overline{\chi_j}(k-S)^j$.
Thus the two-bound proof above remains valid for general positive
forms, while on these actual moment forms its displayed first
bound in SP13 strengthens to
\[
 |\Delta_{h,k}|\le J^{(3)}
 \le\int_0^1\min\{S_{\rm AW}(x),S_{\rm SP}(x)\}\,dx .
 \tag{SP13b}
\]
For $H_0=2\operatorname{arcosh}(e^{F(0)/(2a_q)})$, the derivative
$[2\operatorname{arcosh}(e^{B/(2a_q)})]'
=1/(a_q\sqrt{1-e^{-B/a_q}})$ and its inverse
$2a_q\log\cosh(z/2)$ give the actual endpoint interval
\[
 \begin{aligned}
 F(1)&\ge\max\left\{0,F(0)-J^{(3)},
 2a_q\log\cosh\frac{\max\{0,H_0-I\}}2\right\},\\
 F(1)&\le\min\left\{F(0)+J^{(3)},
 2a_q\log\cosh\frac{H_0+I}2\right\},
 \qquad I\le\log(r_{\max}/r_{\min}).
 \end{aligned}
 \tag{SP13c}
\]
This follows by dividing all three derivative bounds by the same
positive factor, integrating, and applying the increasing inverse;
compactness and $F>0$ justify every denominator. It is precisely
RMT13--RMT18 on the stated unchanged original source.
"""
sp=replace_once(sp,"SP1--SP13 give finite two-sided control",spapp+"\nSP1--SP13 give finite two-sided control")
edit_row(Path("tex/tau_signed_projection_control.tex"),sp,"RMT actual moment specialization SP13a–c, preserving full generic PD-Gram proof")

psa=(OUT/"staged/tex/periodized_source_intake_proofs.tex").read_text()
psabridge=r"""
The actual source in (PSA24a) has additional moment structure.
The first measure is $m_{h,k}(y)\,dy$, and the second is the
unchanged positive atomic measure
$\sum_{|n|\le J}(2\pi/L)m_{h,k}(2\pi n/L)\delta_{2\pi n/L}$,
including zero. Their degree-$2q$ Grams are exactly
$M^{(0)},M^{(1)}$ by (PSA10)--(PSA11) and (PSA21).
Positivity was proved in (PSA23). Hence the complete RMT
calculation applies with this original/sampled pair, with no
change to any atom, mass or polynomial coefficient.
For $a_q=2q-1$ put
\[
 \begin{aligned}
 A_{L,J}(x)&=a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}\,d(x),\\
 \mathcal J^{(3)}_{L,J}&=\int_0^1
 \min\{S_{\rm AW}^{L,J}(x),S_{\rm SP}^{L,J}(x),A_{L,J}(x)\}\,dx,\\
 \mathcal I_{L,J}&=\int_0^1\min\left\{d(x),
 \frac{S_{\rm AW}^{L,J}(x)}{a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}},
 \frac{S_{\rm SP}^{L,J}(x)}{a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}}\right\}\,dx.
 \end{aligned}
 \tag{PSA24f}
\]
RMT11 keeps both original $q$-angle lists of the crossed quotient
pairs and proves $|\mathcal B'|\le A_{L,J}$ on these measures.
Its strict positivity argument applies also to this atomic
endpoint: equality $\mathcal B=0$ would place $1$ orthogonal to
$\chi\mathcal P_q$, and pairing with
$\chi^{\#_k}(S)=\sum_j\overline{\chi_j}(k-S)^j$ would give
$0=\int|\chi|^2\,d\mu_x$, contradicting the positive Gram of
the nonzero $\chi$. Thus $\mathcal B>0$ on the whole compact path.
Taking the minimum of this angle derivative bound and the two
fully proved bounds above yields
$|\mathcal B(1)-\mathcal B(0)|\le\mathcal J^{(3)}_{L,J}
\le\mathcal J_{L,J}$. The generic two-form proof remains valid;
this further inequality uses precisely the actual moment measures.
"""
psa=replace_once(psa,"Let $b_1\\le\\cdots\\le b_n$ be all eigenvalues of $D_{L,J}$.",psabridge+"\nLet $b_1\\le\\cdots\\le b_n$ be all eigenvalues of $D_{L,J}$.")
psa=replace_once(psa,r"&\le\mathcal J_{L,J}\\",r"&\le\mathcal J^{(3)}_{L,J}\le\mathcal J_{L,J}\\")
psanonlin=r"""
This also improves the actual sampled endpoint itself in its
nonlinear coordinate. Define
$H_0=2\operatorname{arcosh}(e^{\mathcal B_{h,k}/(2a_q)})$.
RMT16's derivative and inverse, on this identified moment path,
give $|\mathscr H_{a_q}(\mathcal B_{h,k}(L,J))-H_0|
\le\mathcal I_{L,J}\le\log(b_n/b_1)\le\log(\beta/\alpha)$.
Combining the increasing inverse with the just-proved additive
bound yields
\[
 \begin{aligned}
 \mathcal B_{h,k}(L,J)&\ge\max\left\{0,
 \mathcal B_{h,k}-\mathcal J^{(3)}_{L,J},
 2a_q\log\cosh\frac{\max\{0,H_0-\mathcal I_{L,J}\}}2\right\},\\
 \mathcal B_{h,k}(L,J)&\le\min\left\{
 \mathcal B_{h,k}+\mathcal J^{(3)}_{L,J},
 2a_q\log\cosh\frac{H_0+\mathcal I_{L,J}}2\right\}.
 \end{aligned}
 \tag{PSA25a}
\]
All denominators in (PSA24f) are justified by the strict positivity
above, with no uniform lower bound in tensor order presumed.
"""
psa=replace_once(psa,r"\subsubsection{The finite observation map and both Laplacian boundary terms}",psanonlin+"\n"+r"\subsubsection{The finite observation map and both Laplacian boundary terms}")
edit_row(Path("tex/periodized_source_intake_proofs.tex"),psa,"RMT actual sampled-moment PSA24f, tighter PSA25 and nonlinear interval PSA25a")

fc=(OUT/"staged/tex/periodized_curvature_control_bridge.tex").read_text()
fc=replace_once(fc,r"&\le\mathcal J_{L,J}\\",r"&\le\mathcal J^{(3)}_{L,J}\le\mathcal J_{L,J}\\")
fc=replace_once(fc,"Here $\\mathcal J_{L,J}$ is the integral of the exact pointwise\nminimum in (PSA24e).",
 r"""Here $\mathcal J_{L,J}$ is the generic two-bound integral in
(PSA24e), and $\mathcal J^{(3)}_{L,J}$ is the actual-moment
three-bound integral in (PSA24f). Its original measure and its
positive atomic measure are explicitly identified there, so the
RMT angle theorem applies through those same coefficient maps.
The full nonlinear interval (PSA25a) consequently propagates
at these same four endpoints as well.""")
edit_row(Path("tex/periodized_curvature_control_bridge.tex"),fc,"RMT actual sampled specialization in existing FC13a")

rp=OUT/"conclusion_replacements/R58_NEW.tex"
r58=rp.read_text()
r58=replace_once(r58,r"&\le\mathcal J_{L,J}\\",r"&\le\mathcal J^{(3)}_{L,J}\le\mathcal J_{L,J}\\")
r58=replace_once(r58,"The complete proof at (PSA24a)--(PSA25) establishes these source",
 r"""For the actual positive atomic moment measure in this construction,
retain $a_q=2q-1$ and the additional original-angle term
$A(x)=a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}\,d(x)$.
Then $\mathcal J^{(3)}_{L,J}$ is the same integral with this
third term included in the outer minimum. Its full proof and
exact moment/source identification are (PSA24f); strict
$\mathcal B(x)>0$ follows there from the reflected polynomial
$\chi^{\#_k}$ and positivity of its original moment Gram.
The nonlinear endpoint interval is also propagated explicitly
in (PSA25a), using $\mathcal I_{L,J}$ from (PSA24f).
The complete proof at (PSA24a)--(PSA25a) establishes these source""")
rp.write_text(r58,encoding="utf-8")
rmap=json.loads((OUT/"conclusion_replacements/R58_MAP.json").read_text())
rmap["new_sha256"]=hashlib.sha256(rp.read_bytes()).hexdigest()
rmap["proof_dependencies"]=["PSA24a–PSA25a","FC13a","RMT1–18","complete EP angle proof"]
(OUT/"conclusion_replacements/R58_MAP.json").write_text(json.dumps(rmap,indent=2),encoding="utf-8")
dep=OUT/"dependencies/recursive_metric_transport.tex"
dep.parent.mkdir(exist_ok=True)
origin=ROOT/"work/backpropagation_20260913/recursive_metric_transport.tex"
dep.write_bytes(origin.read_bytes())
(OUT/"RMT_DEPENDENCY.json").write_text(json.dumps(dict(source=str(origin),copy=str(dep),
 sha256=hashlib.sha256(dep.read_bytes()).hexdigest(),full_body=True,
 full_read=True,scope="actual continuous or positive atomic original moment measures",
 acyclic_dependencies="RMT uses AT early determinant derivative, AW15–17 and EP angle proof; not revised AT final theorem"),indent=2),encoding="utf-8")
(OUT/"PATCH_MANIFEST.json").write_text(json.dumps(dict(schema="metric-backpropagation-v3",
 isolated_staging=True,original_sources_unchanged=True,rows=rows),indent=2),encoding="utf-8")
print("Completed original-moment three-bound propagation in five full earlier proof sites and R58.")
