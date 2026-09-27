import subprocess, zipfile, io, re, sys, os
REPO = "/home/claude/repos/zeta-function-research-reader"
files = subprocess.run(["git","-C",REPO,"grep","-l","BQC","origin/main"],capture_output=True,text=True).stdout.split()
files = [f.split(":",1)[1] for f in files]
res = {}
for f in files:
    ext = f.rsplit(".",1)[-1]
    if ext not in ("pdf","zip"): continue
    data = subprocess.run(["git","-C",REPO,"show","origin/main:"+f],capture_output=True).stdout
    hits = []
    if ext == "pdf":
        p = subprocess.run(["pdftotext","-q","-","-"],input=data,capture_output=True)
        txt = p.stdout.decode("utf8","replace")
        hits = [l.strip()[:160] for l in txt.splitlines() if "BQC" in l]
    else:
        try:
            z = zipfile.ZipFile(io.BytesIO(data))
            for n in z.namelist():
                if n.lower().endswith((".md",".tex",".txt",".json",".py",".html")):
                    t = z.read(n).decode("utf8","replace")
                    for l in t.splitlines():
                        if "BQC" in l:
                            hits.append(n+": "+l.strip()[:160])
                elif n.lower().endswith(".pdf"):
                    p = subprocess.run(["pdftotext","-q","-","-"],input=z.read(n),capture_output=True)
                    for l in p.stdout.decode("utf8","replace").splitlines():
                        if "BQC" in l: hits.append(n+" [pdf]: "+l.strip()[:160])
        except Exception as e:
            hits = ["ERROR "+str(e)]
    res[f] = hits
    print(("HIT " if hits else "none ") + f + "  " + str(len(hits)), flush=True)
    for h in hits[:6]: print("    ", h)
