"""Create an isolated exact-body reader; immutable originals remain byte pinned."""
from pathlib import Path
import hashlib,json,re,shutil,difflib

ROOT=Path(__file__).resolve().parent
INTAKE=ROOT.parent
ORIGINALS=ROOT/'originals'
BODY=ROOT/'tex'/'bodies'
ORIGINALS.mkdir(exist_ok=True,parents=True)
BODY.mkdir(exist_ok=True,parents=True)

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def capture(key,p,expected,title,role):
    target=ORIGINALS/(key+'.tex')
    if not target.exists():
        assert sha(p)==expected,(p,sha(p),expected)
        shutil.copyfile(p,target)
    assert sha(target)==expected
    raw=target.read_bytes()
    original=raw.decode('utf-8-sig')
    source=original.replace('\r\n','\n')
    preamble=postamble=''
    ops=[]
    if '\\begin{document}' in source:
        preamble,source=source.split('\\begin{document}',1)
        source,postamble=source.rsplit('\\end{document}',1)
        ops.append({'kind':'full_document_body','preamble':preamble,'postamble':postamble})
    if '\\maketitle' in source:
        assert source.count('\\maketitle')==1
        source=source.replace('\\maketitle','')
        ops.append({'kind':'title_moved_to_chapter','token':'\\maketitle','title':title})
    for old,new,why in [
        ('\\mathbb C','\\mathbb{C}','Explicit macro argument braces for Unicode mathematics'),
        ('\\mathbb R','\\mathbb{R}','Explicit macro argument braces for Unicode mathematics'),
        ('\\mathbb Q','\\mathbb{Q}','Explicit macro argument braces for Unicode mathematics'),
        ('\\mathbb N','\\mathbb{N}','Explicit macro argument braces for Unicode mathematics'),
        ('_\\R ', '_{\\R} ', 'Explicit subscript braces for retained real-line macro'),
        ('_\\C ', '_{\\C} ', 'Explicit subscript braces for retained complex-field macro'),
        ('\\mathsf\\Gamma','\\symsfup{\\Gamma}','Unicode sans-serif Greek mathematical glyph'),
        ('\\mathord{\\textsf{Î”}}','\\Delta','Repair recorded UTF-8 mojibake of the explicitly defined diagonal Delta'),
        ('\\tableofcontents','', 'Full-reader contents replace embedded duplicate contents'),
    ]:
        if old in source:
            ops.append({'kind':'literal_presentation','old':old,'new':new,'count':source.count(old),'reason':why})
            source=source.replace(old,new)
    def break_hash(match):
        old=match.group(0); new='\\nolinkurl{'+match.group(1)+'}'
        ops.append({'kind':'literal_presentation','old':old,'new':new,'count':1,'reason':'Line-breakable unchanged provenance digest'})
        return new
    source=re.sub(r'\\texttt\{([0-9a-f]{40,64})\}',break_hash,source)
    def brace_subscript(match):
        old=match.group(0);new=match.group(1)+'{'+match.group(2)+'}'
        ops.append({'kind':'literal_presentation','old':old,'new':new,'count':1,'reason':'Explicit script argument for unchanged field macro'})
        return new
    source=re.sub(r'([_^])(\\[RCQNZ])\b',brace_subscript,source)
    presentation_path=ROOT/'DISPLAY_REFLOWS.json'
    if presentation_path.exists():
        for op in json.loads(presentation_path.read_text(encoding='utf-8'))['files'].get(key,[]):
            assert source.count(op['old'])==1,(key,op['reason'])
            source=source.replace(op['old'],op['new'])
            ops.append({'kind':'literal_presentation',**op,'count':1})
    prepared=source
    (BODY/(key+'.tex')).write_text(prepared,encoding='utf-8',newline='\n')
    return {'key':key,'title':title,'role':role,'upstream':str(p),'original':str(target.relative_to(ROOT)),
      'sha256':expected,'bytes':len(raw),'body':str((BODY/(key+'.tex')).relative_to(ROOT)),
      'body_sha256':sha(BODY/(key+'.tex')),'transports':ops,'newline_transport':'CRLF to LF when present; original bytes retained'}

dependencies=json.loads((INTAKE/'source_snapshot/SOURCE_DEPENDENCIES.json').read_text(encoding='utf-8-sig'))['files']
titles=['The full mixed phase boundary on the original arithmetic source','Full-quartet critical values and ordered tensor sums',
'The complete phase attachment to the original theta source','Arithmetic determinant transport and four signed endpoints',
'Actual boundary tilts and convolution tails','All-window arithmetic source envelopes','Gamma orthogonality and recurrence',
'Arithmetic endpoint bounds on the original tau-base source: a uniform polynomial-norm estimate and the four-volume criterion',
'Arithmetic lower-envelope comparison for central quotient volumes','The first canonical window and both arithmetic block budgets']
records=[]
for i,(e,title) in enumerate(zip(dependencies,titles),1):
    records.append(capture(f'dep{i:02}',Path(e['path']),e['sha256'],title,e['role']))

new=[
 ('PGS',INTAKE/'source_snapshot/phase_graph_schur.tex','c2c158cf03dc6b6b8eafbc98ee732fad5b2f9f71c942c6ff4d57fb56f03343ff','The original phase graph and its Schur metric'),
 ('PGD',INTAKE/'source_snapshot/density_bounds.tex','102a7faf27e13a99604a1eaf45a9ed54e137ae7cc769f6039a4b0767192f58dc','Density and endpoint bounds for the phase graph'),
 ('PGM',INTAKE/'source_snapshot/strict_mixed_residual_v2.tex','105a4a7fc7a4f1853aea5884f58fc45a6dae74aab52a86784401e3662f310b40','The strict mixed-fibre component of the original phase observation'),
 ('PGB',INTAKE/'phase_graph_averaged_bridge.tex','8b0ffbd004af4b7dffd81dc870d531e7474f779fbaf31890f0b887ed5eeeb2c6','The exact phase-graph map to the averaged quotient and its completion'),
 ('PGMB',INTAKE/'mixed_residual_completion_addendum.tex','7b7af4a1c566461f6601ca96f49799124cc36264accf5d60971a209992ea5486','The completed mixed residual and the exact relative metric cost'),
 ('PGGT',INTAKE/'phase_graph_generator_transport.tex','3ba5308e8bf4a4a48dc27cffa04c1553faf4439a7d4db177acdf973b8ad876cd','Exact generator control on the graph and strict mixed quotient'),
]
for key,p,h,title in new: records.append(capture(key,p,h,title,'Complete new proof body'))
hcd=INTAKE/'source_snapshot/accepted/holonomy_hcd_complete.tex'
records.append(capture('HCD',hcd,sha(hcd),'Continuous holonomy cochains and the original relation metric','Accepted complete continuous descent proof'))
extra_path=ROOT/'EXTRA_DEPENDENCIES.json'
if extra_path.exists():
    for e in json.loads(extra_path.read_text())['files']:
        records.append(capture(e['key'],Path(e['path']),e['sha256'],e['title'],e['role']))

bykey={e['key']:e for e in records}
order=['dep02','dep03','dep01','dep04','dep07','dep08','dep05','dep06','dep09','dep10']
order.extend(k for k in bykey if k not in order+['HCD','PGS','PGD','PGM','PGB','PGMB','PGGT'])
order = [k for k in order if k not in ['PGRT','PGGL']]
order.extend(['HCD','PGS','PGD','PGM','PGB','PGMB','PGGT','PGRT','PGGL'])
preamble=r'''\documentclass[11pt,a4paper,oneside,openany]{book}
\usepackage[margin=21mm,headheight=15pt]{geometry}
\usepackage{amsmath,amssymb,amsthm,amscd,mathtools,mathrsfs,fix-cm}
\DeclareFontFamily{U}{rsfs}{}
\DeclareFontShape{U}{rsfs}{m}{n}{<->rsfs10}{}
\usepackage{fontspec,unicode-math}
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\setmonofont[Scale=0.85]{Latin Modern Mono}
\setmathfont{Latin Modern Math}
\setmathfont[version=bold]{Latin Modern Math}
\usepackage{longtable,booktabs,array,xcolor,microtype,enumitem}
\usepackage[unicode,hidelinks]{hyperref}
\usepackage{bookmark,xurl,fancyhdr}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small Split-Zero: the original phase graph and mixed residual}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\setlength{\parindent}{0pt}\setlength{\parskip}{5pt plus 1pt minus 1pt}
\setlength{\emergencystretch}{4em}
\setcounter{secnumdepth}{0}\setcounter{tocdepth}{0}
\allowdisplaybreaks[2]
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\providecommand{\C}{\mathbb C}\providecommand{\R}{\mathbb R}
\providecommand{\Q}{\mathbb Q}\providecommand{\N}{\mathbb N}
\providecommand{\Tr}{\operatorname{Tr}}\providecommand{\im}{\operatorname{im}}
\providecommand{\ar}{\mathrm{ar}}\providecommand{\Ga}{\Gamma}
\providecommand{\cP}{\mathcal P}\providecommand{\cB}{\mathcal B}
\providecommand{\cR}{\mathcal R}\providecommand{\av}{\operatorname{av}}
\hypersetup{pdftitle={The original phase graph, mixed residual and completed quotient},pdfauthor={},pdfcreator={XeLaTeX}}
\begin{document}
\begin{titlepage}
\vspace*{18mm}
{\Huge\bfseries The original phase graph, mixed residual and completed quotient\par}
\vspace{12mm}
{\Large Split-Zero research programme\par}
\vspace{8mm}
{\large Complete proof sources and their direct analytic dependencies\par}
\vfill
This isolated reader contains the complete PGS, PGD, PGM, PGB and PGMB calculations together with the original supporting proofs identified in its source manifest. Original files are retained byte for byte in the companion source repository. The mathematical objects, full units, ordered tensor data, constants, signs and source coordinates are retained. Presentation transports are recorded explicitly.
\vspace{8mm}
14 September 2026
\end{titlepage}
\tableofcontents
'''
parts=[preamble]
for key in order:
    e=bykey[key]
    parts.append('\\chapter{'+e['title']+'}\n\\begingroup\n\\input{tex/bodies/'+key+'.tex}\n\\endgroup\n')
parts.append('\\end{document}\n')
(ROOT/'tex/main.tex').write_text(''.join(parts),encoding='utf-8',newline='\n')
(ROOT/'SOURCE_MANIFEST.json').write_text(json.dumps({'scope':'Isolated next-wave reader; no cumulative edition edited','order':order,'files':records},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'source_count':len(records),'order':order}))
