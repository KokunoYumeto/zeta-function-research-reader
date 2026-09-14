#!/usr/bin/env python3
from pathlib import Path
import subprocess
import re
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parent
style='<style>\n'+(root/'reader.css').read_text()+'\n</style>'
head=root/'checks'/'style.html';head.write_text(style)
links='<div class="download-bar"><a href="NOTE.tex">LaTeX source</a><a href="HANDOFF.md">Formalization handoff</a><a href="SOURCE_REVIEW.md">SGA reading record</a><a href="CHECKS.md">Executed checks</a></div>'
pre=root/'checks'/'links.html';pre.write_text(links)
cmd=['pandoc',str(root/'RESEARCH_NOTE.md'),'--from','markdown+tex_math_single_backslash','--standalone','--mathml','--toc','--toc-depth=2','--include-in-header',str(head),'--include-before-body',str(pre),'--metadata','lang=en','-o',str(root/'index.html')]
r=subprocess.run(cmd,capture_output=True,text=True);(root/'checks'/'pandoc-html.log').write_text(r.stdout+r.stderr)
if r.returncode:raise SystemExit(r.returncode)
# Preserve literal displayed equation labels; Pandoc MathML drops TeX \tag.
source=(root/'RESEARCH_NOTE.md').read_text()
blocks=re.findall(r'\$\$(.*?)\$\$',source,re.S)
soup=BeautifulSoup((root/'index.html').read_text(),'html.parser')
maths=soup.find_all('math',attrs={'display':'block'})
if len(blocks)!=len(maths):raise RuntimeError('displayed-equation count mismatch')
for block,math in zip(blocks,maths):
    parent=math.parent
    wrap=soup.new_tag('div',attrs={'class':'equation-block'})
    math.replace_with(wrap);wrap.append(math)
    tag=re.search(r'\\tag\{([^}]+)\}',block)
    if tag:
        label=soup.new_tag('span',attrs={'class':'equation-number'})
        label.string='('+tag.group(1)+')';wrap.append(label)
    if parent.name=='p':parent.unwrap()
(root/'index.html').write_text(str(soup))
cmd=['pandoc',str(root/'RESEARCH_NOTE.md'),'--from','markdown+tex_math_single_backslash','--standalone','--variable','geometry:margin=24mm','--variable','fontsize:11pt','-o',str(root/'NOTE.tex')]
r=subprocess.run(cmd,capture_output=True,text=True);(root/'checks'/'pandoc-tex.log').write_text(r.stdout+r.stderr)
raise SystemExit(r.returncode)
