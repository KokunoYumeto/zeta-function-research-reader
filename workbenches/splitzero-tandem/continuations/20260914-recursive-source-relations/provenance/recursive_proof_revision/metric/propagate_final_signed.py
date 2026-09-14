from pathlib import Path
import hashlib,json,difflib,shutil,re
R=Path(r"workspace:\work\backpropagation_20260913\metric")
manifest=json.loads((R/"PATCH_MANIFEST.json").read_text())
H=R/"history/accepted_three_control_cut"
H.mkdir(parents=True,exist_ok=True)
if not (H/"PATCH_MANIFEST.json").exists():
    shutil.copy2(R/"PATCH_MANIFEST.json",H/"PATCH_MANIFEST.json")
    for row in manifest["rows"]:
        p=Path(row["revised"]); d=H/p.relative_to(R/"staged");d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,d)
    shutil.copytree(R/"conclusion_replacements",H/"conclusion_replacements",dirs_exist_ok=True)

def once(t,a,b):
    assert t.count(a)==1,(a[:120],t.count(a));return t.replace(a,b,1)

def metric_block(tag, C, A, d, var):
    return r"""
The exact trace norm and the centered Hilbert--Schmidt estimate
are also retained before taking a minimum. On this same source define
\[
 \begin{aligned}
 S_{\rm tr}(VAR)&=\frac{DIAM}{2}\|DIFF\|_1,\\
 \Sigma(VAR)&=\operatorname{Tr}(DER^2)
       -\frac{(\operatorname{Tr}DER)^2}{2q+1},\\
 S_{\rm HS}(VAR)&=\sqrt{\Sigma(VAR)\operatorname{Tr}((DIFF)^2)}.
 \end{aligned}
 \tag{TAG}
\]
The trace-norm inequality follows by subtracting the midpoint
of the extreme eigenvalues from the metric derivative, since the
trace of the signed projection difference is zero. In an orthonormal
eigenbasis of that difference, every diagonal derivative entry is
bounded in modulus by half the spectral diameter; summing with
the absolute eigenvalues proves the assertion.
For the other bound subtract the trace mean
$\operatorname{Tr}(DER)I/(2q+1)$ instead.
The square of its Hilbert--Schmidt norm in the unchanged source
metric is exactly $\Sigma(VAR)$. Hilbert--Schmidt Cauchy--Schwarz
with the signed difference proves that its trace pairing is bounded
by $S_{\rm HS}(VAR)$. Positivity of both factors under the square
root follows from their self-adjointness. Thus both functions bound
the same absolute signed derivative on general positive source forms;
the angle term below still uses the specified moment measures.
These are RMT10a--10b and ISM25--26 through the already proved
original coefficient and projection maps.
""".replace("TAG",tag).replace("DER",C).replace("DIFF",A).replace("DIAM",d).replace("VAR",var)

def signed_block(tag, dictionary):
    return r"""
For every integer $\ell_N\ge0$ the constructed signed approximation
is applied on these exact endpoint forms as well. DICTIONARY
Write $\mathsf D=(\mathsf M_0)^{-1}\mathsf M_1$, with its complete
ordered positive eigenvalues $b_1,\ldots,b_{2q+1}$, and let
$\mathsf A_z$ be this same signed projection difference. Define
\[
 \begin{aligned}
 \alpha_z^\circ&=\frac{2(1-z)+z(b_1+b_{2q+1})}{2},&
 H_z^\circ&=I-\frac{(1-z)I+z\mathsf D}{\alpha_z^\circ},\\
 C_z^{[\ell_N]}&=(\alpha_z^\circ)^{-1}
       \sum_{r=0}^{\ell_N}(H_z^\circ)^r(\mathsf D-I),&
 R_z^{[\ell_N]}&=(H_z^\circ)^{\ell_N+1}\mathsf C_z,\\
 E_z^{[\ell_N]}&=R_z^{[\ell_N]}
          -\frac{\operatorname{Tr}R_z^{[\ell_N]}}{2q+1}I .
 \end{aligned}
 \tag{TAGa}
\]
The symbols $\alpha_z^\circ,H_z^\circ$ preserve every original
source parameter and relation map; $\ell_N$ is only the finite
series truncation. Multiplication of the finite geometric sum
gives $\mathsf C_z-C_z^{[\ell_N]}=R_z^{[\ell_N]}$.
All factors are real functions of the positive relative
operator $\mathsf D$, hence self-adjoint in the original
$\mathsf M_z=\mathsf M_0((1-z)I+z\mathsf D)$ metric.
Since $\operatorname{Tr}\mathsf A_z=0$, the derivative of the same
four-volume function is its signed center
$\operatorname{Tr}(C_z^{[\ell_N]}\mathsf A_z)$ plus
$\operatorname{Tr}(E_z^{[\ell_N]}\mathsf A_z)$.
Consequently
\[
 \begin{aligned}
 j_{\ell_N}&=\int_0^1
       \operatorname{Tr}(C_z^{[\ell_N]}\mathsf A_z)\,dz,\\
 e_{\ell_N}&=\int_0^1
       \sqrt{\operatorname{Tr}((E_z^{[\ell_N]})^2)
                     \operatorname{Tr}(\mathsf A_z^2)}\,dz,\\
 j_{\ell_N}-e_{\ell_N}
 &\le\mathcal B(1)-\mathcal B(0)\le j_{\ell_N}+e_{\ell_N}.
 \end{aligned}
 \tag{TAGb}
\]
For this block $\mathcal B$ denotes precisely the four-volume
function identified above. The signed inequalities follow by
Hilbert--Schmidt Cauchy--Schwarz in that unchanged metric and
integration of the exact derivative.
The full residual calculation ISM29--37, equivalently RMT19--21,
uses
$\vartheta=(b_{2q+1}-b_1)/(b_{2q+1}+b_1)<1$ and
$K_{\mathsf D}=\sum_j(|b_j-1|/\min\{1,b_j\})^2$ to prove
\[
 0\le e_{\ell_N}\le
    \vartheta^{\ell_N+1}\sqrt{K_{\mathsf D}(8q-6)}
       \longrightarrow0.
 \tag{TAGc}
\]
Indeed every eigenvalue of $H_z^\circ$ has modulus at most
$\vartheta$, centering the residual subtracts a nonnegative square
from its squared Hilbert--Schmidt norm, and
$\operatorname{Tr}(\mathsf A_z^2)\le8q-6$ by the full flag spectra
and the common range. This proves the bound with all eigenvalue
multiplicities retained. The displayed integrals are exact; a
numerical evaluation must retain its own integration error.
Intersecting this proved signed interval with the already proved
absolute and nonlinear intervals supplies the additional endpoint
entries below, for every specified $\ell_N$.
""".replace("TAG",tag).replace("DICTIONARY",dictionary)

rows=[]
for row in manifest["rows"]:
    p=Path(row["revised"]);t=p.read_text()
    name=p.name
    if name in ["AT_complete.tex","AW_complete.tex"]:
        tag="AT18c" if name.startswith("AT") else "AW13c"
        marker="The original-moment angle calculation supplies a further simultaneous"
        t=once(t,marker,metric_block(tag,"C(t)","U(t)-W(t)","d(t)","t")+"\n"+marker)
        t=t.replace(r"S_{\rm SP}(t),A_{h,k}(t)",r"S_{\rm tr}(t),S_{\rm SP}(t),S_{\rm HS}(t),A_{h,k}(t)")
        old=r"\frac{S_{\rm SP}(t)}{a_q\sqrt{1-e^{-\mathcal B(t)/a_q}}}\right\}"
        new=r"""\frac{S_{\rm SP}(t)}{a_q\sqrt{1-e^{-\mathcal B(t)/a_q}}},
   \frac{S_{\rm tr}(t)}{a_q\sqrt{1-e^{-\mathcal B(t)/a_q}}},
   \frac{S_{\rm HS}(t)}{a_q\sqrt{1-e^{-\mathcal B(t)/a_q}}}\right\}"""
        t=once(t,old,new)
        t=t.replace(r"\mathcal J_{h,k}^{(3)}",r"\mathcal J_{h,k}^{(5)}")
        t=t.replace("three-bound","five-bound").replace("all three inequalities","all five inequalities").replace("three derivative bounds","five derivative bounds")
        if name.startswith("AT"):
            dictionary=r"""Here $\mathsf M_z=M_*(t)|_{t=z}$,
$\mathsf C_z=C(t)|_{t=z}$, $\mathsf A_z=(U(t)-W(t))|_{t=z}$,
and $\mathsf D=D_*$. Thus the RMT/ISM coefficient map is the
identity with $x_{\rm RMT}=z=t$, and its $\mathcal B$ is (AT14)."""
            t=once(t,"The same actual-moment calculation also propagates to the nonlinear",signed_block("AT19b",dictionary)+"\nThe same actual-moment calculation also propagates to the nonlinear")
            t=once(t,r"2a_q\log\cosh\frac{\max\{0,H_0-\mathcal I_{h,k}\}}2\right\}",r"2a_q\log\cosh\frac{\max\{0,H_0-\mathcal I_{h,k}\}}2,"+"\n"+r" \mathcal B^\Ga_{h,k}+j_{\ell_N}-e_{\ell_N}\right\}")
            t=once(t,r"2a_q\log\cosh\frac{H_0+\mathcal I_{h,k}}2\right\}",r"2a_q\log\cosh\frac{H_0+\mathcal I_{h,k}}2,"+"\n"+r" \mathcal B^\Ga_{h,k}+j_{\ell_N}+e_{\ell_N}\right\}")
            # Existing AT19 interval gets the signed intersection too.
            t=once(t,r"\mathcal B^\Ga_{h,k}-\mathcal J_{h,k}^{(5)}"+"\n"+r" \le\mathcal B^\ar_{h,k}"+"\n"+r" \le\mathcal B^\Ga_{h,k}+\mathcal J_{h,k}^{(5)}.",
              r"""\max\{\mathcal B^\Ga_{h,k}-\mathcal J_{h,k}^{(5)},
        \mathcal B^\Ga_{h,k}+j_{\ell_N}-e_{\ell_N}\}
 \le\mathcal B^\ar_{h,k}
 \le\min\{\mathcal B^\Ga_{h,k}+\mathcal J_{h,k}^{(5)},
        \mathcal B^\Ga_{h,k}+j_{\ell_N}+e_{\ell_N}\}.""")
            t=once(t,r" \tag{AT19}"+"\n"+r"\]",r" \tag{AT19}"+"\n"+r"\]"+"\n"+r"Here the constructed $j_{\ell_N},e_{\ell_N}$ are defined and proved in (AT19ba)--(AT19bc) below.")
            t=once(t,"The last denominator is positive for every $q\\ge1$.",
                 r"""The signed branch also yields
$\mathcal B^\ar_{h,k}\ge
4q\log(\delta k/(2\sqrt5))+j_{\ell_N}-e_{\ell_N}$:
substitute the same Gamma lower bound into
$\mathcal B^\ar_{h,k}\ge\mathcal B^\Ga_{h,k}
+j_{\ell_N}-e_{\ell_N}$. This branch and (AT22) are both
retained by their maximum.
The last denominator is positive for every $q\ge1$.""")
        else:
            dictionary=r"""Here $\mathsf M_z=M(t)|_{t=z}$,
$\mathsf C_z=C(t)|_{t=z}$ and
$\mathsf A_z=(U(t)-W(t))|_{t=z}$, with $\mathsf D=D$.
The exact RMT/ISM source arrow is the identity,
and $\mathcal B$ is the function (AW5)."""
            t=once(t,"The original quartet Gamma theorem,",signed_block("AW17a",dictionary)+"\nThe original quartet Gamma theorem,")
            t=once(t,r"-\mathcal J_{h,k}^{(5)}."+"\n"+r" \tag{AW18}",r"+\max\{-\mathcal J_{h,k}^{(5)},j_{\ell_N}-e_{\ell_N}\}."+"\n"+r" \tag{AW18}")
            t=once(t,r"2\log\cosh(\max\{0,A_0-L\})"+"\n"+r" \le\mathcal B(1)\le2\log\cosh(A_0+L).",
              r"""\max\{2\log\cosh(\max\{0,A_0-L\}),
          \mathcal B(0)+j_{\ell_N}-e_{\ell_N}\}
 \le\mathcal B(1)\le
 \min\{2\log\cosh(A_0+L),
          \mathcal B(0)+j_{\ell_N}+e_{\ell_N}\}.""")
    elif name=="tau_signed_projection_control.tex":
        marker="On the original moment source (SP1a),"
        t=once(t,marker,metric_block("SP13d","T_x",r"\mathcal R_x-\mathcal P_x","d_x","x")+"\n"+marker)
        t=t.replace(r"\min\{S_{\rm AW}(x),S_{\rm SP}(x),A(x)\}",r"\min\{S_{\rm AW}(x),S_{\rm tr}(x),S_{\rm SP}(x),S_{\rm HS}(x),A(x)\}")
        t=once(t,r"\frac{S_{\rm SP}(x)}{a_q\sqrt{1-e^{-F(x)/a_q}}}\right\}",r"""\frac{S_{\rm SP}(x)}{a_q\sqrt{1-e^{-F(x)/a_q}}},
 \frac{S_{\rm tr}(x)}{a_q\sqrt{1-e^{-F(x)/a_q}}},
 \frac{S_{\rm HS}(x)}{a_q\sqrt{1-e^{-F(x)/a_q}}}\right\}""")
        t=t.replace("J^{(3)}","J^{(5)}").replace("three derivative bounds","five derivative bounds").replace("three-bound","five-bound")
        dic=r"""Use $\mathsf M_z=M_x|_{x=z}$,
$\mathsf C_z=T_x|_{x=z}$,
$\mathsf A_z=(\mathcal R_x-\mathcal P_x)|_{x=z}$,
and $\mathsf D=R$. The same-source RMT/ISM function $\mathcal B$
is exactly $F$ in SP5."""
        t=once(t,"For $H_0=2\\operatorname{arcosh}",signed_block("SP13e",dic)+"\nFor $H_0=2\\operatorname{arcosh}")
        t=once(t,r"2a_q\log\cosh\frac{\max\{0,H_0-I\}}2\right\}",r"2a_q\log\cosh\frac{\max\{0,H_0-I\}}2,F(0)+j_{\ell_N}-e_{\ell_N}\right\}")
        t=once(t,r"2a_q\log\cosh\frac{H_0+I}2\right\}",r"2a_q\log\cosh\frac{H_0+I}2,F(0)+j_{\ell_N}+e_{\ell_N}\right\}")
    elif name=="periodized_source_intake_proofs.tex":
        marker="The actual source in (PSA24a) has additional moment structure."
        t=once(t,marker,metric_block("PSA24g","C(x)","U-W","d(x)","x")+"\n"+marker)
        t=t.replace(r"\min\{S_{\rm AW}^{L,J}(x),S_{\rm SP}^{L,J}(x),A_{L,J}(x)\}",r"\min\{S_{\rm AW}^{L,J}(x),S_{\rm tr}(x),S_{\rm SP}^{L,J}(x),S_{\rm HS}(x),A_{L,J}(x)\}")
        t=once(t,r"\frac{S_{\rm SP}^{L,J}(x)}{a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}}\right\}",r"""\frac{S_{\rm SP}^{L,J}(x)}{a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}},
 \frac{S_{\rm tr}(x)}{a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}},
 \frac{S_{\rm HS}(x)}{a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}}\right\}""")
        t=t.replace(r"\mathcal J^{(3)}",r"\mathcal J^{(5)}").replace("three-bound","five-bound")
        dic=r"""Use $\mathsf M_z=M(x)|_{x=z}$,
$\mathsf C_z=C(x)|_{x=z}$,
$\mathsf A_z=(U(x)-W(x))|_{x=z}$ and
$\mathsf D=D_{L,J}$. These are the actual continuous/sampled
moment forms in (PSA24a), and the RMT/ISM function $\mathcal B$
is precisely the original sampled-path four-volume function.
The truncation $\ell_N$ differs from both the circle length $L$
and the original derivative order $p$."""
        t=once(t,"This also improves the actual sampled endpoint itself",signed_block("PSA25b",dic)+"\nThis also improves the actual sampled endpoint itself")
        t=once(t,r"2a_q\log\cosh\frac{\max\{0,H_0-\mathcal I_{L,J}\}}2\right\}",r"2a_q\log\cosh\frac{\max\{0,H_0-\mathcal I_{L,J}\}}2,"+"\n"+r"\mathcal B_{h,k}+j_{\ell_N}-e_{\ell_N}\right\}")
        t=once(t,r"2a_q\log\cosh\frac{H_0+\mathcal I_{L,J}}2\right\}",r"2a_q\log\cosh\frac{H_0+\mathcal I_{L,J}}2,"+"\n"+r"\mathcal B_{h,k}+j_{\ell_N}+e_{\ell_N}\right\}")
    elif name=="periodized_curvature_control_bridge.tex":
        t=t.replace(r"\mathcal J^{(3)}",r"\mathcal J^{(5)}").replace("three-bound","five-bound")
        t=once(t,"The full nonlinear interval (PSA25a) consequently propagates\nat these same four endpoints as well.",
           r"""The full nonlinear and signed interval (PSA25a) consequently
propagates at these same four endpoints. Explicitly, if
$\mathcal B_0=\mathcal B$ is the original endpoint, define
$a_q=2q-1$, $H_0=2\operatorname{arcosh}(e^{\mathcal B_0/(2a_q)})$
and retain the five-entry radius $\mathcal I_{L,J}$ of (PSA24f).
The constructed $j_{\ell_N},e_{\ell_N}$ in
(PSA25ba)--(PSA25bc) use precisely $M_{2q},M_{2q}(L,J)$,
their original projectors and the same source inclusions; the
finite-series index $\ell_N$ does not change the circle length.
Thus the actual endpoint also obeys
\[
 \begin{aligned}
 \mathcal B(L,J)&\ge\max\left\{0,
 \mathcal B_0-\mathcal J^{(5)}_{L,J},
 2a_q\log\cosh\frac{\max\{0,H_0-\mathcal I_{L,J}\}}2,
 \mathcal B_0+j_{\ell_N}-e_{\ell_N}\right\},\\
 \mathcal B(L,J)&\le\min\left\{
 \mathcal B_0+\mathcal J^{(5)}_{L,J},
 2a_q\log\cosh\frac{H_0+\mathcal I_{L,J}}2,
 \mathcal B_0+j_{\ell_N}+e_{\ell_N}\right\}.
 \end{aligned}\tag{FC13b}
\]
Each bound is the proved same-source specialization of
RMT22; taking the intersection preserves its exact endpoint.""")
    else: raise RuntimeError(name)
    # Current five-min text explicitly preserves the earlier three-entry bound as a consequence.
    t=t.replace("all three preceding","all five preceding").replace("all three derivative","all five derivative")
    p.write_text(t,encoding="utf-8",newline="\n")
    old=Path(row["original_copy"]).read_text(encoding="utf-8")
    Path(row["patch"]).write_text("".join(difflib.unified_diff(old.splitlines(True),t.splitlines(True),fromfile=row["source"],tofile=str(p))),encoding="utf-8")
    row["revised_sha256"]=hashlib.sha256(p.read_bytes()).hexdigest()
    row["claims"]+=["Five simultaneous controls, exact constructed signed Neumann interval and nonlinear intersection at earlier claim sites"]
    rows.append(row)

rp=R/"conclusion_replacements/R58_NEW.tex";s=rp.read_text()
s=s.replace(r"\mathcal J^{(3)}",r"\mathcal J^{(5)}").replace("three-bound","five-bound")
start=s.index("For the actual positive atomic moment measure")
end=s.index("The complete proof at (PSA24a)",start)
s=s[:start]+r"""For the actual positive atomic moment measure in this construction,
the complete five-entry bound in (PSA24f)--(PSA24g) additionally retains
the exact trace term
$S_{\rm tr}(x)=d(x)\|U-W\|_1/2$, the centered Hilbert--Schmidt term
$S_{\rm HS}(x)=
\sqrt{(\operatorname{Tr}C^2-(\operatorname{Tr}C)^2/(2q+1))
                         \operatorname{Tr}((U-W)^2)}$,
and the original-angle term
$(2q-1)\sqrt{1-e^{-\mathcal B(x)/(2q-1)}}d(x)$.
Thus $\mathcal J^{(5)}_{L,J}$ is the integral of the minimum of
these three functions and the two original functions in
$\mathcal J_{L,J}$. All five bound the same signed derivative.
Strict $\mathcal B(x)>0$ is proved on this actual moment measure
by the reflected polynomial $\chi^{\#_k}$ and positivity of its Gram.
The constructed finite Neumann control in (PSA25ba)--(PSA25bc)
also gives $j_{\ell_N}-e_{\ell_N}
\le\mathcal B(L,J)-\mathcal B\le j_{\ell_N}+e_{\ell_N}$,
with the complete finite matrix center and
$e_{\ell_N}\le\vartheta^{\ell_N+1}\sqrt{K_{D_{L,J}}(8q-6)}
\to0$ on this fixed original pair of forms.
Let $a_q=2q-1$ and
$H_0=2\operatorname{arcosh}(e^{\mathcal B/(2a_q)})$.
The five-entry nonlinear radius $\mathcal I_{L,J}$ is proved in
(PSA24f) and includes all four linear-control numerators divided
by $a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}$. Consequently the earlier
finite-circle endpoint now has the full simultaneous enclosure
\[
 \begin{aligned}
 \mathcal B(L,J)&\ge\max\left\{0,
 \mathcal B-\mathcal J^{(5)}_{L,J},
 2a_q\log\cosh\frac{\max\{0,H_0-\mathcal I_{L,J}\}}2,
 \mathcal B+j_{\ell_N}-e_{\ell_N}\right\},\\
 \mathcal B(L,J)&\le\min\left\{
 \mathcal B+\mathcal J^{(5)}_{L,J},
 2a_q\log\cosh\frac{H_0+\mathcal I_{L,J}}2,
 \mathcal B+j_{\ell_N}+e_{\ell_N}\right\}.
 \end{aligned}
\]
This is precisely (PSA25a) and (FC13b), with the unchanged
continuous and positive atomic measures explicitly identified.
The exact signed center retains its integration error in any
numerical evaluation.
""" +s[end:]
rp.write_text(s,encoding="utf-8",newline="\n")
rm=json.loads((R/"conclusion_replacements/R58_MAP.json").read_text())
rm["new_sha256"]=hashlib.sha256(rp.read_bytes()).hexdigest()
rm["proof_dependencies"]=["PSA24a–PSA25bc","FC13a–b","RMT1–22","ISM1–43","complete EP angle proof"]
(R/"conclusion_replacements/R58_MAP.json").write_text(json.dumps(rm,indent=2),encoding="utf-8")
deps=[]
for original in [R.parent/"recursive_metric_transport.tex",R.parent/"incoming_pr29_metric/incoming_source_metric_control.tex"]:
    dst=R/"dependencies"/original.name;dst.write_bytes(original.read_bytes())
    deps.append(dict(source=str(original),copy=str(dst),sha256=hashlib.sha256(dst.read_bytes()).hexdigest(),full_read=True))
(R/"FINAL_SIGNED_DEPENDENCIES.json").write_text(json.dumps(deps,indent=2),encoding="utf-8")
manifest.update(schema="metric-backpropagation-v4-final-signed",rows=rows)
(R/"PATCH_MANIFEST.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
print("Final five-entry/signed interval propagated to five complete proof bodies and R58.")
