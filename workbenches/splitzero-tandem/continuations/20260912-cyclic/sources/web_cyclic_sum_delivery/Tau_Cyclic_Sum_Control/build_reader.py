from pathlib import Path
import re,subprocess
from bs4 import BeautifulSoup
base=Path(__file__).resolve().parent
subprocess.run(['pandoc',str(base/'RESEARCH_NOTE.md'),'--from=markdown+tex_math_dollars','--to=html5','--standalone','--mathml','--toc','--toc-depth=2','--metadata','title=Sum-generated arithmetic cohomology and conormal depth','--include-in-header='+str(base/'style.html'),'--include-before-body='+str(base/'nav.html'),'--output='+str(base/'index.html')],check=True)
soup=BeautifulSoup((base/'index.html').read_text(),'html.parser')
heads=soup.find_all('h1')
if len(heads)>1:
    heads[0]['id']=heads[1].get('id','note');heads[1].decompose()
for m in soup.find_all('math',attrs={'display':'block'}):
    par=m.parent;annotation=m.find('annotation');label=re.search(r'\\tag\{([^}]+)\}',annotation.get_text() if annotation else '')
    wrap=soup.new_tag('div',attrs={'class':'equation'});scroll=soup.new_tag('div',attrs={'class':'equation-scroll'})
    par.insert_before(wrap);wrap.append(scroll);scroll.append(m.extract())
    if label:
        tag=soup.new_tag('span',attrs={'class':'equation-label'});tag.string='('+label.group(1)+')';wrap.append(tag)
    if not par.get_text(strip=True):par.decompose()
(base/'index.html').write_text(str(soup))
subprocess.run(['pandoc',str(base/'RESEARCH_NOTE.md'),'--from=markdown+tex_math_dollars','--to=latex','--standalone','--metadata','title=Sum-generated arithmetic cohomology and exact conormal depth','--output='+str(base/'NOTE.tex')],check=True)
