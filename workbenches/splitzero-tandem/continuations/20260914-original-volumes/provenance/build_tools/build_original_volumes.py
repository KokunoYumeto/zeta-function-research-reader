"""Cut22 source assembly. Preserve exact providers; record every display transport."""
from pathlib import Path
import hashlib,json,shutil,subprocess,zipfile

gw=Path(__file__).resolve().parent
outer=Path(r'C:\Users\[[user]]\Documents\math\output\Split_Zero_Mixed_Boundary_Continuation_2026-09-14')
out=outer/'22_ORIGINAL_VOLUMES'
out.mkdir(exist_ok=True)
for d in ['sources','originals','provenance','qa','dependencies']:
    (out/d).mkdir(exist_ok=True)
prior=outer/'21_GAMMA_GROWTH'/'Gamma_Growth_Complete_Source.zip'
closure=out/'dependencies'/'cut21'
if not closure.exists():
    closure.mkdir()
    with zipfile.ZipFile(prior) as z:
        for info in z.infolist():
            target=(closure/info.filename).resolve()
            if not target.is_relative_to(closure.resolve()):raise ValueError(info.filename)
        z.extractall(closure)

mapping={
 'HBL.tex':gw/'baseline_20260914/independent/HOMOGENEOUS_GAMMA_BASELINE.tex',
 'BSL.tex':gw/'baseline_20260914/BASELINE_ORIGINAL_PACKET.tex',
 'GDR.tex':gw/'low_refinement_20260914/DERIVATIVE_REMAINDER.tex',
 'LER.tex':gw/'low_refinement_20260914/LOW_ENDPOINT_REFINEMENT.tex',
 'IKO.tex':gw/'independent_K_20260914/INDEPENDENT_ORDER_ORIGINAL_MAPS.tex',
 'KME.tex':gw/'independent_K_20260914/equilibrium/MACROSCOPIC_MARKED_EQUILIBRIUM.tex',
 'KEP.tex':gw/'independent_K_20260914/equilibrium/endpoint_existence.tex',
 'MFG.tex':gw/'independent_K_20260914/independent/ACTUAL_MACROSCOPIC_GAMMA_RETURN.tex',
 'KPR.tex':gw/'independent_K_20260914/INDEPENDENT_ORDER_POSITIVE_RETURN.tex',
}
# Additional accepted providers are supplied explicitly by the root before freezing.
extra=gw/'CUT22_ADDITIONAL_ACCEPTED_PROVIDERS.json'
canonical_extra_names=[]
extra_support_files=[]
if extra.exists():
    for x in json.loads(extra.read_text(encoding='utf-8')):
        p=Path(x['path'])
        if hashlib.sha256(p.read_bytes()).hexdigest()!=x['sha256']:raise ValueError(x)
        mapping[x['destination']]=p
        canonical_extra_names.append(x['destination'])
        extra_support_files.extend(x.get('support_files',[]))
pins=[];transports=[]
root_accept_path=out/'ROOT_PROOF_ACCEPTANCE.json'
root_pins={}
if root_accept_path.exists():
    root_accept=json.loads(root_accept_path.read_text(encoding='utf-8'))
    if root_accept.get('status')!='PASS':raise ValueError('Root proof acceptance is not PASS')
    root_pins={str(Path(x['path']).resolve()).casefold():x['sha256'] for x in root_accept['proofs']}
for dest,src in mapping.items():
    raw=src.read_bytes()
    if root_pins and root_pins.get(str(src.resolve()).casefold())!=hashlib.sha256(raw).hexdigest():
        raise ValueError(('provider differs from root acceptance',src))
    (out/'originals'/dest).write_bytes(raw)
    text=raw.decode('utf-8')
    changes=[]
    if '\\begin{document}' in text:
        prefix,body=text.split('\\begin{document}',1)
        body,suffix=body.rsplit('\\end{document}',1)
        changes.append({'before':prefix+'\\begin{document}','after':'','purpose':'remove standalone preamble; preserve exact original'})
        changes.append({'before':'\\end{document}'+suffix,'after':'','purpose':'remove standalone terminator; preserve exact original'})
        text=body
        if '\\maketitle' in text:
            changes.append({'before':'\\maketitle','after':'','purpose':'main paper supplies one title'})
            text=text.replace('\\maketitle','',1)
    if dest=='KME.tex':
        before='\\input{endpoint_existence.tex}';after='\\input{sources/KEP.tex}'
        if text.count(before)!=1:raise ValueError('KEP input')
        text=text.replace(before,after,1)
        changes.append({'before':before,'after':after,'purpose':'exact local dependency path; KEP printed once'})
    reflow_path=gw/'CUT22_DISPLAY_REFLOWS.json'
    if reflow_path.exists():
        for r in json.loads(reflow_path.read_text(encoding='utf-8')):
            if r['file']!=dest:continue
            if text.count(r['before'])!=1:raise ValueError(('nonunique display reflow',r))
            text=text.replace(r['before'],r['after'],1);changes.append(r)
    transported=raw.decode('utf-8')
    for change in changes:
        if transported.count(change['before'])!=1:raise ValueError(('nonunique reversible transport',dest,change))
        change['offset_before']=transported.index(change['before'])
        transported=transported.replace(change['before'],change['after'],1)
    if transported!=text:raise ValueError(('transport reconstruction failed',dest))
    restored=text
    for change in reversed(changes):
        i=change['offset_before'];after=change['after']
        if restored[i:i+len(after)]!=after:raise ValueError(('reverse mismatch',dest,change))
        restored=restored[:i]+change['before']+restored[i+len(after):]
    if restored.encode('utf-8')!=raw:raise ValueError(('original-byte round trip failed',dest))
    display=text.encode('utf-8');(out/'sources'/dest).write_bytes(display)
    pins.append({'source':str(src),'destination':'sources/'+dest,'original':'originals/'+dest,
                 'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),
                 'typeset_sha256':hashlib.sha256(display).hexdigest()})
    transports.append({'file':dest,'changes':changes,'exact_original_byte_round_trip_verified':True})

reviewdirs=[gw/'baseline_20260914/review',gw/'independent_K_20260914/review']
for d in reviewdirs:
    target=out/'provenance'/d.parent.name/d.name
    shutil.copytree(d,target,dirs_exist_ok=True)
for rel in ['low_refinement_20260914/LOW_REFINEMENT_PROOF_RECEIPT.json',
            'independent_K_20260914/equilibrium/KME_FINAL_INDEPENDENT_AUDIT_RECEIPT.json',
            'independent_K_20260914/equilibrium/KME_INDEPENDENT_PROOF_AUDIT.md',
            'independent_K_20260914/independent/MFG_INDEPENDENT_REVIEW.md']:
    src=gw/rel;target=out/'provenance'/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,target)
for item in extra_support_files:
    src=Path(item['path']);target=out/'provenance'/item['destination']
    if not target.resolve().is_relative_to((out/'provenance').resolve()):raise ValueError(item)
    if hashlib.sha256(src.read_bytes()).hexdigest()!=item['sha256']:raise ValueError(item)
    target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,target)
for family in ['q_scale_20260914','intrinsic_order_20260914',
               'intrinsic_four_endpoint_20260914','intrinsic_mixed_rows_20260914']:
    folder=gw/family
    if not folder.exists():continue
    for src in folder.rglob('*'):
        rel=src.relative_to(folder)
        if not src.is_file() or src.suffix not in ['.md','.json','.py','.tex']:continue
        if not any(part in ['review','final_review','circle_review','history'] for part in rel.parts):continue
        target=out/'provenance'/family/rel
        target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,target)

tex=r'''\documentclass[11pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Cambria}
\setsansfont{Calibri}
\setmonofont{Consolas}
\usepackage[margin=23mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage[unicode,hidelinks]{hyperref}
\hypersetup{pdftitle={Original Gamma Volumes and Intrinsic Spectral Sums},pdfauthor={Split-Zero research programme}}
\newcommand{\C}{\mathbb C}
\newcommand{\R}{\mathbb R}
\allowdisplaybreaks
\emergencystretch=2em
\title{Original Gamma Volumes and Intrinsic Spectral Sums\\[3pt]
\large The unchanged packet, exact endpoint refinements and proved comparison families}
\author{Split-Zero research programme}
\date{14 September 2026}
\begin{document}
\maketitle
This continuation retains the original packet order $k$, the original
dimension $q=[1+k(m-1)](k+1)^2$, the source coordinate $S=k/2+iy$,
all roots and all four endpoints. Every new proof is printed below.
The complete preceding source closure, including the positive recurrence,
source transport, equilibrium and mixed kernel--boundary maps, accompanies
this paper in \texttt{dependencies/cut21}.

The first part concerns the unchanged construction. The second part
preserves the calculations for a separately chosen Gamma order $K$,
with their exact comparison maps and their stated scope. The exploratory
choice $K=q+1$ is not a rule supplied by the original construction and
does not replace its canonical source. The intrinsic constructions in
the first part are derived from the original spaces and operators.

\tableofcontents
\clearpage
\part{The original construction and its volume calculation}
\input{sources/HBL.tex}
\clearpage
\input{sources/BSL.tex}
\clearpage
\input{sources/GDR.tex}
\clearpage
\input{sources/LER.tex}
'''
for name in canonical_extra_names:
    tex+='\\clearpage\n\\input{sources/'+name+'}\n'
tex+=r'''
\clearpage
\part{Exploratory independent-order comparison with exact maps}
The independent order in this part is a tested comparison parameter.
Its source changes are carried simultaneously through the baseline,
the Gamma return and the arithmetic identity. All original parameters
remain present in the comparison. No selection of a replacement
canonical order is inferred from these calculations.
\input{sources/IKO.tex}
\clearpage
\input{sources/KME.tex}
\clearpage
\input{sources/MFG.tex}
\clearpage
\input{sources/KPR.tex}
\end{document}
'''
(out/'Original_Gamma_Volumes_and_Intrinsic_Spectral_Sums.tex').write_bytes(tex.encode())
cumulative_intro=r'''
\part*{Complete preceding Gamma source and growth proofs}
The following complete proof bodies are preserved from the accepted
preceding edition. Its historical receiving statements have current
successors in \texttt{current\_receiving}; the newer volume calculations
follow in full after these prerequisite proofs.
\input{dependencies/cut21/sources/LET.tex}
\clearpage
\input{dependencies/cut21/sources/PHT.tex}
\clearpage
\input{dependencies/cut21/sources/growth/WGP.tex}
\clearpage
\input{dependencies/cut21/sources/growth/RWB.tex}
\clearpage
\paragraph{Exact parameter dictionary for the auxiliary equilibrium.}
The elliptic modulus $k$ in EIQ is $\kappa=k_{\rm EIQ}\in(0,1)$.
Its midpoint is $m_{\rm EIQ}=(u^2+v^2)/2$.
The original packet still has $k_{\rm packet}=4l+1$ and its original
integer multiplicity $m_{\rm packet}$. GEL3 supplies the parameter map
$\alpha=a/n$, $\beta=\pi q/(2n)$, converging to $(2,\pi)$.
\input{dependencies/cut21/sources/growth/EIQ.tex}
\clearpage
\input{dependencies/cut21/sources/growth/GEL.tex}
\clearpage
\input{dependencies/cut21/sources/growth/WGR.tex}
\clearpage
'''
cumulative=tex.replace('\\begin{document}',
    '\\makeatletter\n\\def\\input@path{{dependencies/cut21/}}\n\\renewcommand\\@pnumwidth{2.5em}\n\\renewcommand\\@tocrmarg{3.5em}\n\\makeatother\n\\begin{document}',1)
cumulative=cumulative.replace('\\part{The original construction and its volume calculation}',
    cumulative_intro+'\\part{The original construction and its volume calculation}',1)
(out/'Cumulative_Original_Gamma_Proofs.tex').write_bytes(cumulative.encode())
(out/'NEW_PROOF_SOURCE_PINS.json').write_bytes(json.dumps(pins,indent=2).encode())
(out/'DISPLAY_AND_BODY_TRANSPORTS.json').write_bytes(json.dumps(transports,indent=2).encode())
(out/'PREDECESSOR_CLOSURE.json').write_bytes(json.dumps({'archive':str(prior),'sha256':hashlib.sha256(prior.read_bytes()).hexdigest(),'uncompressed_members':len(list(closure.rglob('*'))),'purpose':'one complete preserved cut21 source closure'},indent=2).encode())
args=['xelatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','Original_Gamma_Volumes_and_Intrinsic_Spectral_Sums.tex']
for run in [1,2,3]:
    result=subprocess.run(args,cwd=out,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (out/f'build_run_{run}.txt').write_bytes(result.stdout.encode())
    if result.returncode:print(result.stdout[-7000:]);raise SystemExit(result.returncode)
print(json.dumps({'output':str(out),'providers':len(mapping),'build':'three xelatex passes completed'},indent=2))
