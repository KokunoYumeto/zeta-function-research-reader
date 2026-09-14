"""Render every fixed-reader page with Poppler for complete independent inspection."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,shutil,subprocess,math
ROOT=Path(__file__).resolve().parent
PDF=ROOT/'Phase_Graph_Mixed_Residual_Reader.pdf'
build=json.loads((ROOT/'BUILD_RECEIPT.json').read_text())
PIN=build['pdf_sha256'];pages=build['pages']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(PDF)==PIN
engine=shutil.which('pdftoppm');assert engine
qa=ROOT/'page_qa'/PIN[:16];qa.mkdir(parents=True,exist_ok=True)
chunk=math.ceil(pages/6)
ranges=[(first,min(first+chunk-1,pages)) for first in range(1,pages+1,chunk)]
def render(bounds):
    first,last=bounds;dest=qa/f'pages_{first:03}_{last:03}';dest.mkdir(exist_ok=True)
    p=subprocess.run([engine,'-f',str(first),'-l',str(last),'-r','180','-png',str(PDF),str(dest/'page')],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    assert p.returncode==0,p.stdout.decode(errors='replace')
    files=[]
    for n in range(first,last+1):
        png=dest/f'page-{n:03}.png';assert png.exists(),png
        files.append({'page':n,'path':str(png),'sha256':sha(png),'bytes':png.stat().st_size})
    receipt={'pdf':str(PDF),'pdf_sha256':PIN,'dpi':180,'engine':engine,'first':first,'last':last,'files':files,'visual_inspection':'pending'}
    (dest/'RENDER_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'first':first,'last':last,'rendered':len(files),'directory':str(dest)}),flush=True)
    return receipt
with ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(render,ranges))
assert sha(PDF)==PIN
(qa/'RENDER_INVENTORY.json').write_text(json.dumps({'pdf_sha256':PIN,'pages':pages,'ranges':results},indent=2)+'\n')
