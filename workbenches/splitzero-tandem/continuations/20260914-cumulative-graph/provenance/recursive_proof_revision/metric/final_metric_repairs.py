from pathlib import Path
import json,hashlib,difflib
R=Path(r"workspace:\work\backpropagation_20260913\metric")
m=json.loads((R/"PATCH_MANIFEST.json").read_text())
def once(s,a,b):assert s.count(a)==1,(a,s.count(a));return s.replace(a,b,1)
for row in m["rows"]:
 p=Path(row["revised"]);s=p.read_text()
 if p.name in ["AT_complete.tex","AW_complete.tex","tau_signed_projection_control.tex","periodized_source_intake_proofs.tex"]:
  # The long five-term nonlinear radius retains every original fraction,
  # merely breaking its original aligned display.
  import re
  s,n=re.subn(r'(\\frac\{S_\{\\rm SP\}(?:\^\{L,J\})?\([tx]\)\}\{a_q\\sqrt\{1-e\^\{-[^}]+\}\}\}),\n( +\\frac\{S_\{\\rm tr\})',
       r'\1,\\right.\n \\\\\n &\\hspace{2em}\\left.\2',s)
  # Generic robust exact alternatives if nested B(t) defeated regex.
  if n==0:
   patterns=[
    r"\frac{S_{\rm SP}(t)}{a_q\sqrt{1-e^{-\mathcal B(t)/a_q}}},"+"\n",
    r"\frac{S_{\rm SP}(x)}{a_q\sqrt{1-e^{-F(x)/a_q}}},"+"\n",
    r"\frac{S_{\rm SP}^{L,J}(x)}{a_q\sqrt{1-e^{-\mathcal B(x)/a_q}}},"+"\n"]
   for a in patterns:
    if a in s:s=once(s,a,a.rstrip()+"\\right.\n \\\\\n &\\hspace{2em}\\left.");n+=1
  assert n==1,(p.name,n)
 if p.name=="AT_complete.tex":
  s=once(s,"Finally (AT19) follows by applying the two signs of the five-bound\nbound to the exact equality",
    "Finally the absolute branches of (AT19) follow by applying both signs\nof (AT18), and its constructed signed branches follow from (AT19bb)\nproved below, to the exact equality")
 if p.name=="AW_complete.tex":
  s=once(s,"Taking the pointwise minimum of this additional proved inequality\nwith (AW16) and (AW16a) gives",
    "Taking the pointwise minimum of this additional proved inequality\nwith (AW16), (AW16a), and both complete bounds in (AW13c) gives")
  s=once(s,"This is substitution of the complete supplied Gamma theorem\ninto the proved first inequality of (AW14).",
    "This substitutes the complete supplied Gamma theorem into the\nlower branches of (AW14) and the constructed signed inequality (AW17ab),\nthen takes their maximum.")
  s=once(s,"The two\nindependent inequalities (AW16) and (AW16a) can be divided by\nthat same factor",
    "The four\nindependent generic inequalities (AW16), (AW16a), and the trace-norm\nand Hilbert--Schmidt inequalities (AW13c) can all be divided by\nthat same factor")
  s=once(s,"Equivalently, with the original values",
    "Combining (AW22) with the signed interval (AW17ab), with the original values")
  s=once(s,r"""\max\{2\log\cosh(\max\{0,A_0-L\}),
          \mathcal B(0)+j_{\ell_N}-e_{\ell_N}\}
 \le\mathcal B(1)\le
 \min\{2\log\cosh(A_0+L),
          \mathcal B(0)+j_{\ell_N}+e_{\ell_N}\}.""",
   r"""\begin{aligned}
 \mathcal B(1)&\ge
 \max\{2\log\cosh(\max\{0,A_0-L\}),
          \mathcal B(0)+j_{\ell_N}-e_{\ell_N}\},\\
 \mathcal B(1)&\le
 \min\{2\log\cosh(A_0+L),
          \mathcal B(0)+j_{\ell_N}+e_{\ell_N}\}.
 \end{aligned}""")
 p.write_text(s,encoding="utf-8",newline="\n")
 old=Path(row["original_copy"]).read_text()
 Path(row["patch"]).write_text("".join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile=row["source"],tofile=str(p))),encoding="utf-8")
 row["revised_sha256"]=hashlib.sha256(p.read_bytes()).hexdigest()
(R/"PATCH_MANIFEST.json").write_text(json.dumps(m,indent=2),encoding="utf-8")
print("Exact dependency prose and display continuation repairs completed.")
