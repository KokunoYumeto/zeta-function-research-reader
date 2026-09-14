from pathlib import Path
import re, subprocess, hashlib, json
D=Path(__file__).resolve().parent
src=(D/"COMPLETED_MELLIN_CALCULATIONS.md").read_text(encoding="utf-8")
replacements={
"g=2ξ":r"\(g=2\xi\)",
"E=ℂ":r"\(E=\mathbb C\)",
"Q=𝔅/ΘV":r"\(Q=\mathscr B/\Theta V\)",
"R=𝒪_{ℂ,s₀}":r"\(R=\mathcal O_{\mathbb C,s_0}\)",
"D^mφ*":r"\(D^m\phi_*\)",
"a_m(s)=s^m":r"\(a_m(s)=s^m\)",
"v_m(s)=(1-s)^m":r"\(v_m(s)=(1-s)^m\)",
"c b₊,ₘ+d b₋,ₘ=0":r"\(c b_{+,m}+d b_{-,m}=0\)",
"g(s)(c s^m+d(1-s)^m)=0":r"\(g(s)(c s^m+d(1-s)^m)=0\)",
"(1-s)⁻ᵐ":r"\((1-s)^{-m}\)",
"binom(m+k−1,k)":r"\(\binom{m+k-1}{k}\)",
"βδₘ(f,h)=0":r"\(\beta\delta_m(f,h)=0\)",
"aₘ f=vₘ h":r"\(a_mf=v_mh\)",
"r=Bₘ h+Aₘ f":r"\(r=B_mh+A_mf\)",
"(f,h)=(vₘr,aₘr)":r"\((f,h)=(v_mr,a_mr)\)",
"aₘf−vₘh=0":r"\(a_mf-v_mh=0\)",
"L=𝒫({+,−})":r"\(L=\mathcal P(\{+,-\})\)",
"f↦f⊗b₊,ₘ":r"\(f\mapsto f\otimes b_{+,m}\)",
"h↦−h⊗b₋,ₘ":r"\(h\mapsto-h\otimes b_{-,m}\)",
"b±,ₘ":r"\(b_{\pm,m}\)",
"gaₘ,gvₘ":r"\(ga_m,gv_m\)",
"A=E[t]":r"\(A=E[t]\)",
"M(DF)=s MF":r"\(\mathcal M(DF)=s\mathcal MF\)",
"Δ_P=1⊗P(D)b*−P(s)⊗b*":r"\(\Delta_P=1\otimes P(D)b_*-P(s)\otimes b_*\)",
"(1−t)ᵐ":r"\((1-t)^m\)",
"(−1)ʲ binom(m,j)":r"\((-1)^j\binom mj\)",
"1−D":r"\(1-D\)",
"aU₁/ₐ":r"\(aU_{1/a}\)",
"P(s)sᵐg":r"\(P(s)s^mg\)",
"Q(s)(1−s)ᵐg":r"\(Q(s)(1-s)^mg\)",
"A b*":r"\(A b_*\)",
"P(D)b*=0":r"\(P(D)b_*=0\)",
"b*":r"\(b_*\)",
"A((1−t)ᵐ,tᵐ)":r"\(A((1-t)^m,t^m)\)",
"β_cyc(h⊗b*)=hg":r"\(\beta_{\mathrm{cyc}}(h\otimes b_*)=hg\)",
"(i₊,ₘ,i₋,ₘ)":r"\((i_{+,m},i_{-,m})\)",
"A b*↪𝔅":r"\(A b_*\hookrightarrow\mathscr B\)",
"mρ":r"\(m_\rho\)",
"0<R'<R₀":r"\(0<R'<R_0\)",
"α=(ρ,j)":r"\(\alpha=(\rho,j)\)",
"∏_{σ≠ρ}(∂ᵧ−σ)^{mσ}":r"\(\prod_{\sigma\ne\rho}(\partial_y-\sigma)^{m_\sigma}\)",
"e^{ρy}Pρ(y)":r"\(e^{\rho y}P_\rho(y)\)",
"(∂ᵧ+ρ−σ)^{mσ}":r"\((\partial_y+\rho-\sigma)^{m_\sigma}\)",
"Pρ=0":r"\(P_\rho=0\)",
"Pρ":r"\(P_\rho\)",
"c*Bc=0":r"\(c^*Bc=0\)",
"v∈A_Z":r"\(v\in A_Z\)",
"C_c^∞((e^{-R₀},e^{R₀}))⊂𝔅":r"\(C_c^\infty((e^{-R_0},e^{R_0}))\subset\mathscr B\)",
"x=eʸ":r"\(x=e^y\)",
"J_Z[F_v]=v":r"\(J_Z[F_v]=v\)",
"ι_Z(w)=0":r"\(\iota_Z(w)=0\)",
"1⊗J_Z":r"\(1\otimes J_Z\)",
"R⊗A_Z":r"\(R\otimes_E A_Z\)",
"∑ρmρ":r"\(\sum_{\rho\in Z}m_\rho\)",
"ι_Z":r"\(\iota_Z\)",
"τ↦τ":r"\(\tau\mapsto\tau\)",
"Aτ":r"\(\mathsf A_\tau\)",
"Kτ":r"\(K_\tau\)",
"J_Z":r"\(J_Z\)",
"on the − face":r"on the \(-\) face",
"H⁰=0":r"\(H^0=0\)",
"H¹=R/(g)":r"\(H^1=R/(g)\)",
"H⁰":r"\(H^0\)",
"H¹":r"\(H^1\)",
"b₊,ₘ":r"\(b_{+,m}\)",
"b₋,ₘ":r"\(b_{-,m}\)",
"δₘ":r"\(\delta_m\)",
"Aₘ":r"\(A_m\)",
"Bₘ":r"\(B_m\)",
"sᵐ":r"\(s^m\)",
"tᵐ":r"\(t^m\)",
"m≥1":r"\(m\ge1\)",
"j≥1":r"\(j\ge1\)",
"𝔅":r"\(\mathscr B\)",
"JΘ":r"\(J\Theta\)",
"Θ":r"\(\Theta\)",
"σ":r"\(\sigma\)",
"ρ":r"\(\rho\)",
"η":r"\(\eta\)",
"τ":r"\(\tau\)",
"×g":r"\(\times g\)",
"−1":r"\(-1\)",
"§4":r"Section~4",
"§1":r"Section~1",
"§5":r"Section~5",
}
pattern=re.compile("|".join(re.escape(k) for k in sorted(replacements,key=len,reverse=True)))
chunks=re.split(r"(\\\[[\s\S]*?\\\])",src)
processed="".join(chunk if chunk.startswith(r"\[") else pattern.sub(lambda m:replacements[m[0]],chunk) for chunk in chunks)
# This input is an unsealed rendering aid. It changes only the typesetting of prose formulae.
intermediate=D/"MELLIN_FRAGMENT_RENDER_INPUT.md"
intermediate.write_text(processed,encoding="utf-8")
out=D/"COMPLETED_MELLIN_CALCULATIONS_FRAGMENT.tex"
subprocess.run([r"local:user-profile/AppData/Local/Pandoc/pandoc.exe",str(intermediate),
"-f","markdown+tex_math_single_backslash-superscript-subscript","-t","latex","--wrap=none","-o",str(out)],check=True)
tex=out.read_text(encoding="utf-8")
# Prefix every generated structural label to keep this fragment independent of adjacent chapters.
tex=re.sub(r"\\label\{([^}]+)\}",lambda m:r"\label{typed-mellin:"+m[1]+"}",tex)
# The heading numerals belonged to the Markdown note, not to the combined volume numbering.
tex=re.sub(r"(\\subsection\{)[1-5]\. ",r"\1",tex)
extra=(D/"FOURIER_PHI_STAR_FRAGMENT.tex").read_text(encoding="utf-8")
marker=r"\subsection{The raw two-leg syzygy at every source order}"
if marker not in tex:raise ValueError("Insertion marker missing")
tex=tex.replace(marker,extra+"\n\n"+marker,1)
tex="% Input fragment; packages: amsmath, amssymb, mathrsfs, hyperref.\n% Full display mathematics retained from COMPLETED_MELLIN_CALCULATIONS.md.\n"+tex
# Keep source hashes breakable without changing a digit.
tex=re.sub(r"(?<![0-9A-Fa-f])([0-9a-f]{64})(?![0-9A-Fa-f])",lambda m:r"\nolinkurl{"+m[1]+"}",tex)
tex=tex.replace("§",r"\S{}")
tex=tex.replace(r"that different calculation follows in Section\textasciitilde4.",r"that different calculation is given in Section~\ref{typed-mellin:an-explicit-free-submodule-in-the-raw-realization-kernel}.")
tex=tex.replace(r"Section\textasciitilde",r"source Section~")
out.write_text(tex,encoding="utf-8")
original_math=re.findall(r"\\\[([\s\S]*?)\\\]",src)
rendered_math=re.findall(r"\\\[([\s\S]*?)\\\]",tex)
for i,math in enumerate(original_math):
    if math not in rendered_math:raise ValueError(f"Display formula {i} changed")
nonascii=sorted({c for c in tex if ord(c)>127})
escaped_math_issues=[line for line in tex.splitlines() if r"\textsuperscript" in line or r"\emph" in line or r"\^{}" in line]
report={"source_sha256":hashlib.sha256(src.encode("utf-8")).hexdigest(),"fragment_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),"bytes":out.stat().st_size,"original_display_bodies_preserved":len(original_math),"added_display_bodies":len(rendered_math)-len(original_math),"non_ascii_characters":nonascii,"escaped_math_issues":escaped_math_issues}
(D/"MELLIN_FRAGMENT_RENDER_CHECK.json").write_text(json.dumps(report,ensure_ascii=True,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,ensure_ascii=True,indent=2))
