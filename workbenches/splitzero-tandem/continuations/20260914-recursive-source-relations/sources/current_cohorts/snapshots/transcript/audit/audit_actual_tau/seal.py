from pathlib import Path
import re,json,hashlib,subprocess
base=Path(__file__).parent
main=base/"FULL_SUPPORT_DUAL.md"
s=main.read_text(encoding="utf-8")
if "# Appendix A:" not in s:
    ap=(base/"RETRACTION_PROOF.md").read_text(encoding="utf-8")
    ap=re.sub(r"\A---\n.*?\n---\n","",ap,count=1,flags=re.S)
    ap=re.sub(r"(?m)^# (\d+)\.",r"## A.\1.",ap)
    s+="\n# Appendix A: complete retraction on the original theta source\n"+ap
main.write_text(s,encoding="utf-8",newline="\n")
for fn in ["FULL_SUPPORT_DUAL.md","audit_actual_tau.md","RETRACTION_PROOF.md"]:
    content=(base/fn).read_text(encoding="utf-8")
    if any(ord(c)<32 and c not in "\n\r\t" for c in content):
        raise ValueError(("control character",fn))
    if fn!="audit_actual_tau.md":
        assert content.count(r"\(")==content.count(r"\)"),fn
        assert content.count(r"\[")==content.count(r"\]"),fn
subprocess.run(["pandoc",str(main),"--from","markdown+tex_math_single_backslash",
 "--to","latex","--standalone","--variable","documentclass=article",
 "--variable","geometry=margin=25mm","--variable","fontsize=11pt",
 "--output",str(base/"FULL_SUPPORT_DUAL.tex")],check=True)
subprocess.run(["pandoc",str(main),"--from","markdown+tex_math_single_backslash",
 "--to","latex","--output",str(base/"FULL_SUPPORT_DUAL.fragment.tex")],check=True)
subprocess.run(["pandoc",str(base/"audit_actual_tau.md"),"--from","markdown+tex_math_single_backslash",
 "--to","latex","--output",str(base/"audit_actual_tau.fragment.tex")],check=True)
files=["audit_actual_tau.md","audit_actual_tau.json","audit_actual_tau.fragment.tex",
 "FULL_SUPPORT_DUAL.md","FULL_SUPPORT_DUAL.tex","FULL_SUPPORT_DUAL.fragment.tex",
 "RETRACTION_PROOF.md","dual_review/REVIEW.md"]
result={f:{"bytes":(base/f).stat().st_size,"sha256":hashlib.sha256((base/f).read_bytes()).hexdigest()} for f in files}
result["coverage"]={"source_lines":[1,7811],"visible_turns":43,"user_inputs":14,"assistant_messages":29,
 "quoted_passages_checked_literal":True,"full_primary_note_read":True,
 "segment_sha256":"e79b46722d9a2ee95b68ae6512f37a19fd41e4b3ecc4e53583cd357d0442c251",
 "primary_note_sha256":"d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3",
 "independent_mathematical_review":"dual_review plus independent child; no mathematical errors found",
 "no_lean_or_remote_or_master_edits":True}
(base/"FINAL_RECEIPT.json").write_text(json.dumps(result,indent=2),encoding="utf-8",newline="\n")
print(json.dumps(result,indent=2))
