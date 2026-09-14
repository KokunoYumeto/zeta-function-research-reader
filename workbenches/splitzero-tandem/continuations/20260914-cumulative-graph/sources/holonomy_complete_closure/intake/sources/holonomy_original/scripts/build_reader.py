#!/usr/bin/env python3
from pathlib import Path
import re,subprocess,json
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]
text=(root/'NOTE.md').read_text()
def untag(m):
    b=m.group(1);tags=re.findall(r'\\tag\{([^}]+)\}',b)
    b=re.sub(r'\\tag\{[^}]+\}','',b).strip()
    return '$$\n'+b+'\n$$\n\n'+(' <div class="eqno">('+tags[0]+')</div>\n' if tags else '')
html_md=root/'checks/html-source.md'
html_md.write_text(re.sub(r'\$\$\n(.*?)\n\$\$',untag,text,flags=re.S))
cmd=['pandoc',str(html_md),'-f','markdown+tex_math_single_backslash','--standalone','--mathml','--toc','--toc-depth=2','-o',str(root/'index.html')]
p=subprocess.run(cmd,capture_output=True,text=True)
(root/'checks/html-build.log').write_text(p.stdout+p.stderr);p.check_returncode()
p=subprocess.run(['pandoc',str(root/'NOTE.md'),'-f','markdown+tex_math_single_backslash','--standalone','-t','latex','-V','geometry:margin=24mm','-o',str(root/'NOTE.tex')],capture_output=True,text=True)
(root/'checks/latex-build.log').write_text(p.stdout+p.stderr);p.check_returncode()
soup=BeautifulSoup((root/'index.html').read_text(),'html.parser')
for el in list(soup.find_all('math')):
    if el.get('display')=='block':
        parent=el.parent; wrapper=soup.new_tag('div',attrs={'class':'math display'})
        if parent.name=='p':
            nxt=parent.find_next_sibling();parent.replace_with(wrapper);wrapper.append(el.extract())
            if nxt and 'eqno' in nxt.get('class',[]):wrapper.append(nxt.extract())
        else:el.wrap(wrapper)
    else:el.wrap(soup.new_tag('span',attrs={'class':'math inline'}))
style=soup.new_tag('style');style.string=(root/'reader.css').read_text();soup.head.append(style)
(root/'index.html').write_text(str(soup))
report={'display_equations':len(soup.select('math[display="block"]')),'labels':len(soup.select('.eqno')),'external_scripts':len(soup.select('script[src]')),'raw_latex_spans':len(soup.select('.math:not(:has(math))'))}
(root/'checks/reader-build.json').write_text(json.dumps(report,indent=2));print(report)
