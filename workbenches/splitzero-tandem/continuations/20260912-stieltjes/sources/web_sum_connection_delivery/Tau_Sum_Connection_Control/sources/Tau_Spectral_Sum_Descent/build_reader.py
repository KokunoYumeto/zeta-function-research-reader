from pathlib import Path
import re
import subprocess
from bs4 import BeautifulSoup
base=Path(__file__).resolve().parent
subprocess.run(['pandoc',str(base/'RESEARCH_NOTE.md'),'--from=markdown+tex_math_dollars','--to=html5','--standalone','--mathml','--toc','--toc-depth=2','--metadata','title=Spectral-sum descent with the relative arithmetic fibre retained','--include-in-header='+str(base/'style.html'),'--include-before-body='+str(base/'nav.html'),'--output='+str(base/'index.html')],check=True)
soup=BeautifulSoup((base/'index.html').read_text(),'html.parser')
headers=soup.find_all('h1')
if len(headers)>1:
    headers[0]['id']=headers[1].get('id','research-note')
    headers[1].decompose()
for math in soup.find_all('math',attrs={'display':'block'}):
    old=math.parent
    wrapper=soup.new_tag('div',attrs={'class':'equation'})
    scroll=soup.new_tag('div',attrs={'class':'equation-scroll'})
    wrapper.append(scroll)
    anno=math.find('annotation')
    label=re.search(r'\\tag\{([^}]+)\}',anno.get_text() if anno else '')
    old.insert_before(wrapper)
    scroll.append(math.extract())
    if label:
        tag=soup.new_tag('span',attrs={'class':'equation-label'})
        tag.string='('+label.group(1)+')'
        wrapper.append(tag)
    if not old.get_text(strip=True):
        old.decompose()
style=soup.new_tag('style')
style.string='''
.equation{display:flex;align-items:center;gap:14px;border-left:3px solid var(--line);padding:15px 8px;margin:20px 0;max-width:100%;box-sizing:border-box}
.equation-scroll{overflow-x:auto;overflow-y:hidden;min-width:0;flex:1;padding:4px 0}
.equation-label{color:var(--muted);font:13px system-ui,sans-serif;flex:none;align-self:center}
.equation math{display:block;width:max-content;min-width:0;max-width:none;margin:auto}
body{box-sizing:border-box}p{overflow-wrap:break-word}#TOC{overflow-wrap:anywhere}
'''
soup.head.append(style)
(base/'index.html').write_text(str(soup))
