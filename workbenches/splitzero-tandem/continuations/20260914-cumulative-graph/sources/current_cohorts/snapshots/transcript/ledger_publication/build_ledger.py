"""Rebuild this packaged ledger using only paths relative to this file."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,unicodedata

HERE=Path(__file__).resolve().parent
manifest=json.loads((HERE/'sources_manifest.json').read_text(encoding='utf-8'))
receipt={'source_validation':[],'tables':[],'unicode_text_math_chars':[]}

def cells(line):
    out=[];buf=[];code=False;math=False;i=0
    line=line.strip()
    if line.startswith('|'):line=line[1:]
    if line.endswith('|'):line=line[:-1]
    while i<len(line):
        c=line[i]
        if c=='`':code=not code
        if not code and line[i:i+2] in ('\\(','\\)'):
            math=line[i+1]=='(';buf.append(line[i:i+2]);i+=2;continue
        if c=='|' and not code and not math and (not buf or buf[-1]!='\\'):
            out.append(''.join(buf).strip());buf=[]
        else:buf.append(c)
        i+=1
    out.append(''.join(buf).strip())
    return out

def expand_tables(text,slug,baselevel):
    ls=text.splitlines();out=[];i=0;preserved=[]
    while i<len(ls):
        line=ls[i]
        if line.lstrip().startswith('|') and i+1<len(ls) and re.match(r'^\s*\|[\s:|\-]+\|\s*$',ls[i+1]):
            headers=cells(line);rows=[];i+=2
            while i<len(ls) and ls[i].lstrip().startswith('|'):
                row=cells(ls[i]);rows.append(row);i+=1
            out+=['',f'**Complete table entries ({len(rows)} rows).**','']
            for n,row in enumerate(rows,1):
                if len(row)!=len(headers):
                    raise ValueError(f'{slug}: table row {n}: {len(row)} columns, expected {len(headers)}: {row}')
                out += ['\\Needspace{5\\baselineskip}',f'**Entry {n}.**','']
                for key,value in zip(headers,row):
                    out += [f'**{key}:** {value}','']
                    if value and value not in '\n'.join(out):raise ValueError('Cell lost')
            receipt['tables'].append(dict(source=slug,headers=headers,rows=len(rows),cells=sum(map(len,rows))))
        else:
            match=re.match(r'^(#{1,6}) (.*)$',line)
            if match:
                out.append('#'*min(6,len(match[1])+baselevel)+' '+match[2])
                preserved.append(match[2])
            else:out.append(line);preserved.append(line)
            i+=1
    transformed='\n'.join(out)
    for line in preserved:
        if line and line not in transformed:raise ValueError(f'{slug}: lost non-table line')
    return transformed

parts=['# Complete mathematical continuation ledger','',
 'This volume preserves the complete passage audits, including their historical repairs and exact scope statements. The separate proof volume contains the newly completed calculations. Long coverage tables have been expanded into labelled row entries without dropping cells.','']
for m in manifest:
    p=HERE/m['packaged_path'];b=p.read_bytes()
    actual=hashlib.sha256(b).hexdigest()
    if actual!=m['sha256']:raise ValueError('Source snapshot hash mismatch: '+m['slug'])
    text=b.decode('utf-8-sig')
    changed=expand_tables(text,m['slug'],m['level'])
    if m['level']==1:parts+=['','\\clearpage','']
    parts += ['#'*m['level']+' '+m['title'],'',changed,'']
    ids=set(re.findall(r'\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b',text))
    if not ids.issubset(set(re.findall(r'\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b',changed))):raise ValueError('Lost UUID')
    receipt['source_validation'].append(dict(source=m['slug'],sha256=actual,unique_uuids=len(ids),non_table_lines_preserved=True))
combined='\n'.join(parts)
(HERE/'ledger.md').write_text(combined,encoding='utf-8')
# Map text-mode Greek/mathematical Unicode to the Unicode math font. The
# mathematical text itself is unchanged; existing Math AST nodes stay intact.
special=sorted({c for c in combined if ord(c)>127 and (unicodedata.category(c)=='Sm' or 0x370<=ord(c)<=0x3ff or 0x1d400<=ord(c)<=0x1d7ff or c in 'ℓℝℂℤℕℚℬ𝔢〈〉')})
receipt['unicode_text_math_chars']=special
lua='''local chars = {}\n'''+''.join('chars['+json.dumps(c,ensure_ascii=False)+'] = true\n' for c in special)+r'''
local function esc(s)
  return (s:gsub('([#$%%&_{}])','\\%1'):gsub('~','\\textasciitilde{}'):gsub('%^','\\textasciicircum{}'))
end
local function piece(s,code)
  if code or #s>=35 then return '\\protect\\path{'..s..'}' else return esc(s) end
end
local function output(s,code)
  local o={}; local acc={}; local has=false
  for _,v in utf8.codes(s) do
    local c=utf8.char(v)
    if chars[c] then
      has=true
      if #acc>0 then table.insert(o,piece(table.concat(acc),code));acc={} end
      local cm=c
      if c=='〈' then cm='\\langle' end
      if c=='〉' then cm='\\rangle' end
      table.insert(o,'\\allowbreak{}\\ensuremath{'..cm..'}\\allowbreak{}')
    else table.insert(acc,c) end
  end
  if not has and not code and #s<35 then return nil end
  if #acc>0 then table.insert(o,piece(table.concat(acc),code)) end
  return pandoc.RawInline('latex',table.concat(o))
end
function Str(el) return output(el.text,false) end
function Code(el) return output(el.text,true) end
function Math(el)
 if el.mathtype=='DisplayMath' then return pandoc.RawInline('latex','\\LedgerDisplay{'..el.text..'}') end
end
'''
(HERE/'layout.lua').write_text(lua,encoding='utf-8')
header=r'''\usepackage{amsmath,amssymb,mathtools}
\usepackage{microtype}
\usepackage{xurl}
\usepackage{fvextra}
\usepackage{fancyhdr}
\usepackage{needspace}
\usepackage{graphicx}
\newsavebox{\ledgermathbox}
\newcommand{\LedgerDisplay}[1]{\sbox{\ledgermathbox}{$\displaystyle #1$}\[\ifdim\wd\ledgermathbox>\linewidth\resizebox{\linewidth}{!}{\usebox{\ledgermathbox}}\else\usebox{\ledgermathbox}\fi\]}
\RecustomVerbatimEnvironment{verbatim}{Verbatim}{breaklines=true,fontsize=\small}
\setlength{\emergencystretch}{5em}
\setlength{\parskip}{5pt plus 1pt}
\setlength{\parindent}{0pt}
\allowdisplaybreaks
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Original tau-base programme: passage ledger}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\setlength{\headheight}{15pt}
\urlstyle{same}
\makeatletter
\renewcommand{\@pnumwidth}{2.5em}
\renewcommand{\@tocrmarg}{3.5em}
\makeatother
\let\ledgermaketitle\maketitle
\renewcommand{\maketitle}{\hypersetup{pageanchor=false}\ledgermaketitle\clearpage\pagenumbering{roman}\hypersetup{pageanchor=true}}
\let\ledgertoc\tableofcontents
\renewcommand{\tableofcontents}{\ledgertoc\clearpage\pagenumbering{arabic}}
'''
(HERE/'layout.tex').write_text(header,encoding='utf-8')
args=['pandoc','ledger.md','--from=markdown+tex_math_single_backslash','--standalone','--to=latex','--output=ledger.tex',
 '--toc','--toc-depth=2','--number-sections','--lua-filter=layout.lua','--include-in-header=layout.tex',
 '--variable=documentclass:report','--top-level-division=chapter','--variable=fontsize:10pt',
 '--variable=geometry:a4paper,top=23mm,bottom=23mm,left=23mm,right=23mm',
 '--variable=mainfont:DejaVu Serif','--variable=sansfont:DejaVu Sans','--variable=monofont:DejaVu Sans Mono',
 '--variable=mathfont:Latin Modern Math','--metadata=title:Mathematical continuation audit — complete passage ledger',
 '--metadata=date:13 September 2026','--syntax-highlighting=none']
subprocess.run(args,cwd=HERE,check=True)
(HERE/'BUILD_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if '--tex-only' not in sys.argv:
    for i in range(2):
        with (HERE/f'latex_pass_{i+1}.txt').open('w',encoding='utf-8') as log:
            p=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','ledger.tex'],cwd=HERE,stdout=log,stderr=subprocess.STDOUT)
        if p.returncode:raise RuntimeError(f'LaTeX pass {i+1} failed; see latex_pass_{i+1}.txt')
print(json.dumps({'sources':len(manifest),'tables_expanded':len(receipt['tables']),'table_rows':sum(x['rows'] for x in receipt['tables']),'uuid_checks':'pass','tex':'ledger.tex'},indent=2))
