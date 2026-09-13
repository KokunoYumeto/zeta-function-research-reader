#!/usr/bin/env python3
"""Build a self-contained MathML reader and editable TeX from the note."""
from pathlib import Path
import subprocess, re
ROOT=Path(__file__).resolve().parent
common=['pandoc',str(ROOT/'RESEARCH_NOTE.md'),'--from','markdown+tex_math_dollars','--standalone']
commands=[
 ('pandoc-html.log',common+['--to','html5','--mathml','--toc','--toc-depth=2','--section-divs','--wrap=none','--css=reader.css','-o',str(ROOT/'index.html')]),
 ('pandoc-tex.log',common+['--to','latex','--toc','-V','documentclass=article','-V','fontsize=11pt','-V','geometry:margin=24mm','-o',str(ROOT/'NOTE.tex')])]
for log,command in commands:
 p=subprocess.run(command,capture_output=True,text=True,check=True)
 (ROOT/'checks'/log).write_text(p.stderr)
 if 'Could not convert TeX math' in p.stderr:
  raise RuntimeError('Math rendering failed; read '+log)
text=(ROOT/'index.html').read_text()
def equation(match):
 math=match.group(0)
 tag=re.search(r"\\tag\{([0-9]+)\}",math)
 number=tag.group(1) if tag else None
 ident=(' id="eq-'+number+'"') if number else ''
 label=('<a class="eq-number" href="#eq-'+number+'">('+number+')</a>') if number else ''
 return '<span class="math display"'+ident+'>'+math+label+'</span>'
text=re.sub(r'<math display="block".*?</math>',equation,text,flags=re.S)

text=text.replace('<link rel="stylesheet" href="reader.css" />','<style>\n'+(ROOT/'reader.css').read_text()+'\n</style>')
links='<div class="resource-bar"><a href="NOTE.tex">LaTeX source</a><a href="HANDOFF.md">Formalization handoff</a><a href="PROGRAMME_STATE.md">Programme state</a><a href="SOURCE_REVIEW.md">Source review</a><a href="checks/normal.json">Exact finite checks</a></div>'
text=text.replace('</header>','</header>'+links,1)
text=text.replace('</body>','<footer class="footer">Original arithmetic source retained · Written finite theorems · Exact regression checks · No new uniform purity bound or Lean certificate · No remote changes</footer></body>')
(ROOT/'index.html').write_text(text)
