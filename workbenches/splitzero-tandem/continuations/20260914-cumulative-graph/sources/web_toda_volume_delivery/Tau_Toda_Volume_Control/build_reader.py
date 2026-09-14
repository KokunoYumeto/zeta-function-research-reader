#!/usr/bin/env python3
"""Build the self-contained MathML reader and editable LaTeX using Pandoc."""
from pathlib import Path
import subprocess, re
ROOT=Path(__file__).resolve().parent
text=ROOT/'RESEARCH_NOTE.md'
common=['pandoc',str(text),'--from','markdown+tex_math_dollars','--standalone']
commands=[
    common+['--to','html5','--mathml','--toc','--toc-depth=2','--section-divs','--wrap=none','--css=reader.css','-o',str(ROOT/'index.html')],
    common+['--to','latex','--toc','-V','documentclass=article','-V','fontsize=11pt','-V','geometry:margin=24mm','-o',str(ROOT/'NOTE.tex')]
]
for command,name in zip(commands,['pandoc-html.log','pandoc-tex.log']):
    result=subprocess.run(command,check=True,capture_output=True,text=True)
    (ROOT/'checks'/name).write_text(result.stderr)
    if 'Could not convert TeX math' in result.stderr:
        raise RuntimeError('Math conversion failed; inspect '+name)
html=(ROOT/'index.html').read_text()
html=re.sub(r'(<math display="block".*?</math>)', r'<span class="math display">\1</span>',html,flags=re.S)
html=html.replace('<link rel="stylesheet" href="reader.css" />','<style>\n'+(ROOT/'reader.css').read_text()+'\n</style>')
bar='<div class="resource-bar"><a href="NOTE.tex">LaTeX source</a><a href="HANDOFF.md">Formalization handoff</a><a href="PROGRAMME_STATE.md">Programme state</a><a href="SOURCE_REVIEW.md">Source review</a><a href="checks/normal.json">Exact check record</a></div>'
html=html.replace('</header>','</header>\n'+bar,1)
html=html.replace('</body>','<footer class="footer">Written mathematical continuation · Exact finite regression evidence · No new Lean or RH certificate · No remote changes</footer>\n</body>')
(ROOT/'index.html').write_text(html)
