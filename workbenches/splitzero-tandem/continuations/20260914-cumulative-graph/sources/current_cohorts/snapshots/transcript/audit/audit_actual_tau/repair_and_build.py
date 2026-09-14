from pathlib import Path
import hashlib,json,re,subprocess

base=Path(__file__).parent
p=base/"FULL_SUPPORT_DUAL.md"
s=p.read_text(encoding="utf-8-sig")
out=[]; display=False
for n,line in enumerate(s.splitlines(),1):
    if line==r"\[": display=True
    if not display and n>8:
        line=line.replace(r"\(","(").replace(r"\)",")")
        chars=[]; depth=0
        for ch in line:
            if ch=="(":
                chars.append(r"\(" if depth==0 else "("); depth+=1
            elif ch==")":
                depth-=1
                if depth<0: raise ValueError((n,line))
                chars.append(r"\)" if depth==0 else ")")
            else: chars.append(ch)
        if depth: raise ValueError((n,line,depth))
        line="".join(chars)
    out.append(line)
    if line==r"\]": display=False
s="\n".join(out)+"\n"
assert s.count(r"\(")==s.count(r"\)")
assert not any(ord(c)<32 and c not in "\t\n\r" for c in s)
p.write_text(s,encoding="utf-8",newline="\n")
subprocess.run(["pandoc",str(p),"--from","markdown+tex_math_single_backslash",
 "--to","latex","--standalone","--variable","documentclass=article",
 "--variable","geometry=margin=25mm","--variable","fontsize=11pt",
 "--output",str(base/"FULL_SUPPORT_DUAL.tex")],check=True)
print(json.dumps({"inline_pairs":s.count(r"\("),"display_pairs":s.count(r"\["),
 "sha256_md":hashlib.sha256(p.read_bytes()).hexdigest()},indent=2))
