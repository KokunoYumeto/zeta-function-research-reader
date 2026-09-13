"""Rebuild this edition's local HTML/CSS only; preserve provenance and source files."""
from pathlib import Path
import re, html, json
root=Path(__file__).resolve().parent
tex=root/'NOTE.tex'
css='''
:root{--ink:#182232;--muted:#4d5c70;--line:#d8e0e9;--panel:#f3f6fa;--accent:#174b76;}
*{box-sizing:border-box}body{margin:0;background:#fff;color:var(--ink);font:17px/1.65 Georgia,serif}
main,body>article{max-width:1040px;margin:auto;padding:38px 32px 80px}header{border-bottom:2px solid var(--accent);padding-bottom:20px;margin-bottom:28px}
h1,h2,h3,h4{font-family:system-ui,sans-serif;line-height:1.25;color:var(--accent)}h1{font-size:2rem}h2{margin-top:2.3rem}h3{margin-top:1.7rem}
p{margin:.85rem 0}.subtitle,.scope{color:var(--muted);font:14px/1.55 system-ui,sans-serif}.theorem{border-left:3px solid var(--accent);background:var(--panel);padding:14px 20px;margin:22px 0}.proof{padding:2px 12px}
.eq{position:relative;display:flex;align-items:center;justify-content:center;gap:18px;margin:22px 0;padding:12px 10px;background:#fafbfc;overflow-x:auto;max-width:100%}.eq math{flex-shrink:0;max-width:none}.eqno{margin-left:auto;color:var(--muted);white-space:nowrap;font-size:.9rem}.latex{white-space:pre;overflow-x:auto;font:14px/1.5 ui-monospace,monospace;margin:0}.inline-latex{font-family:ui-monospace,monospace;font-size:.9em}a{color:var(--accent)}details{border:1px solid var(--line);padding:10px 14px;margin:20px 0}summary{cursor:pointer;font-family:system-ui,sans-serif}nav a{margin-right:16px}code{font-size:.9em}math{font-size:1.05em}footer{margin-top:44px;border-top:1px solid var(--line);padding-top:15px}
@media(max-width:650px){main,body>article{padding:22px 16px 50px}body{font-size:16px}h1{font-size:1.6rem}.eq{justify-content:flex-start;padding:10px 4px}.theorem{padding:12px 14px}}
'''
(root/'reader.css').write_text(css, encoding='utf-8', newline='\n')
source=tex.read_text(encoding='utf-8')
status={'renderer':None,'math_fallbacks':0}
# Prefer a native-MathML conversion; keep a full LaTeX source fallback for every equation.
try:
    from latex2mathml.converter import convert
except ImportError:
    convert=None

body=source.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0]
body=body.replace(r'\maketitle','').replace(r'\tableofcontents','')
parts=[]
def token(value):
    key=f'ZZTOKEN{len(parts):05d}ZZ';parts.append(value);return key

def math(latex,display=False):
    tags=re.findall(r'\\tag\{([^{}]+)\}',latex)
    clean=re.sub(r'\\tag\{[^{}]+\}','',latex).strip()
    mml=None
    if convert:
        try:mml=convert(clean,display='block' if display else 'inline')
        except Exception:pass
    if mml is None:
        status['math_fallbacks']+=1
        mml=('<pre class="latex">'+html.escape(clean)+'</pre>') if display else ('<span class="inline-latex">'+html.escape(clean)+'</span>')
    if display:
        number=tags[0] if tags else ''
        return token('<div class="eq"'+(' id="eq-'+html.escape(number)+'"' if number else '')+'>'+mml+('<span class="eqno">('+html.escape(number)+')</span>' if number else '')+'</div>')
    return token(mml)
body=re.sub(r'\\\[(.*?)\\\]',lambda m:math(m.group(1),True),body,flags=re.S)
body=re.sub(r'\\\((.*?)\\\)',lambda m:math(m.group(1)),body,flags=re.S)
body=re.sub(r'(?<!\\)\$(.*?)(?<!\\)\$',lambda m:math(m.group(1)),body,flags=re.S)
body=re.sub(r'\\section\*?\{([^{}]*)\}',lambda m:token('<h2>'+m.group(1)+'</h2>'),body)
body=re.sub(r'\\subsection\*?\{([^{}]*)\}',lambda m:token('<h3>'+m.group(1)+'</h3>'),body)
body=re.sub(r'\\begin\{(theorem|proposition|lemma|definition|remark)\}(?:\[([^\]]*)\])?',lambda m:token('<div class="theorem"><p><strong>'+m.group(1).title()+(' — '+m.group(2) if m.group(2) else '')+'</strong></p>'),body)
body=re.sub(r'\\end\{(?:theorem|proposition|lemma|definition|remark)\}',lambda m:token('</div>'),body)
body=body.replace(r'\begin{proof}',token('<div class="proof"><p><strong>Proof.</strong></p>')).replace(r'\end{proof}',token('<p>□</p></div>'))
body=body.replace(r'\begin{abstract}',token('<div class="theorem"><h2>Abstract</h2>')).replace(r'\end{abstract}',token('</div>'))
body=html.escape(body)
for command,tag in [('textbf','strong'),('emph','em'),('texttt','code')]:
    body=re.sub(r'\\'+command+r'\{([^{}]*)\}',lambda m:'<'+tag+'>'+m.group(1)+'</'+tag+'>',body)
body=body.replace(r"\'e",'é').replace(r'\"u','ü').replace(r'\_','_').replace(r'\&','&amp;').replace('``','“').replace("''",'”').replace('---','—').replace('--','–')
paragraphs=[]
for para in re.split(r'\n\s*\n',body.strip()):
    paragraphs.append('<p>'+para.replace('\n',' ')+'</p>')
body='\n'.join(paragraphs)
# Tokens are nested because headings can contain already-tokenized inline mathematics.
for _ in range(4):
    for i,value in enumerate(parts):body=body.replace(f'ZZTOKEN{i:05d}ZZ',value)
body=re.sub(r'<p>\s*(<(?:div|h2|h3)\b)',r'\1',body)
body=re.sub(r'(</(?:div|h2|h3)>)\s*</p>',r'\1',body)
status['renderer']='latex2mathml/native MathML' if convert else 'readable LaTeX equations with complete editable source'
header='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Marked τ-base and signed four-endpoint control</title><link rel="stylesheet" href="reader.css"></head><body><main><header><p class="subtitle">Split-Zero research continuation · 13 September 2026 · Public-readable derivative</p><h1>The marked τ-base and the signed arithmetic correction</h1><p>A weight-matched external packet family; the actual common-source four-endpoint calculation; retained theta relation norms.</p><nav><a href="NOTE.tex">Editable LaTeX</a><a href="HANDOFF.md">Formalization handoff</a><a href="SOURCE_REVIEW.md">Source record</a><a href="PUBLIC_PROVENANCE.md">Edition provenance</a><a href="checks/PUBLIC_REPLAY.json">Fresh finite checks</a><a href="checks/EXECUTION.json">Inherited execution record</a></nav></header>'''
footer='''<footer><p class="scope">The equations and proofs are in NOTE.tex. Finite symbolic tests, numerical evaluations, inherited analytic inputs, and finite-field applications have their separate stated scopes. This note does not claim an RH proof or failure of the entire τ-based programme.</p></footer></main></body></html>'''
(root/'index.html').write_text(header+body+footer, encoding='utf-8', newline='\n')
(root/'RENDER.json').write_text(json.dumps(status,indent=2)+'\n', encoding='utf-8', newline='\n')
print(json.dumps({'tex':'NOTE.tex','html':'index.html','render':status,
                  'scope':'Reader generation only; provenance, manifests, archives, and historical inputs are not overwritten.'},indent=2))
