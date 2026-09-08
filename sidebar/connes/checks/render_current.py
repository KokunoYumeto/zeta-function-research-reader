"""Render the current standalone PDF with Poppler and make review contact sheets."""
from pathlib import Path
import ast
import ctypes
import hashlib
import json
import os
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
tree = ast.parse((ROOT/"checks"/"verify_exact.py").read_text(encoding="utf-8"))
memory_function = next(n for n in tree.body if isinstance(n,ast.FunctionDef)
                       and n.name == "install_memory_ceiling")
exec(compile(ast.Module(body=[memory_function],type_ignores=[]),"<resource policy>","exec"))
resource = install_memory_ceiling()
from PIL import Image, ImageDraw
import fitz

source = ROOT/"tex"/"main.pdf"
reader = ROOT/"connes_quotient_heat_transport.pdf"
qa = ROOT/"qa"
previous_path = qa/"current_render_receipt.json"
previous = json.loads(previous_path.read_text()) if previous_path.exists() else {}
previous_hashes = {}
if (str(previous.get("visual_inspection","")).startswith("passed")
        and reader.exists()
        and previous.get("pdf_sha256")==hashlib.sha256(reader.read_bytes()).hexdigest()):
    history=qa/"render_history"
    history.mkdir(exist_ok=True)
    archived=history/(previous["pdf_sha256"]+".json")
    if not archived.exists():
        archived.write_text(json.dumps(previous,indent=2)+"\n",encoding="utf-8")
    for number in range(1,previous["pages"]+1):
        prior_page=qa/f"current-page-{number:02}.png"
        if prior_page.exists():
            previous_hashes[number]=hashlib.sha256(prior_page.read_bytes()).hexdigest()
shutil.copyfile(source,reader)
prefix = qa/"current-page"
subprocess.run(["pdftoppm","-r","85","-png",str(reader),str(prefix)],
               check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
with fitz.open(reader) as doc:
    count = len(doc)
    width = max(p.rect.width for p in doc)
    height = max(p.rect.height for p in doc)
paths = [qa/f"current-page-{n:02}.png" for n in range(1,count+1)]
assert all(p.exists() for p in paths)
unchanged=[number for number,path in enumerate(paths,1)
           if previous_hashes.get(number)==hashlib.sha256(path.read_bytes()).hexdigest()]
changed=[number for number in range(1,count+1) if number not in unchanged]
contact_files=[]
for start in range(0,count,4):
    selected=paths[start:start+4]
    with Image.open(selected[0]) as first:
        cell_width,cell_height=first.size
    sheet=Image.new("RGB",(cell_width*2,(cell_height+25)*2),"#e5e5e5")
    draw=ImageDraw.Draw(sheet)
    for k,path in enumerate(selected):
        with Image.open(path) as page:
            x=(k%2)*cell_width
            y=(k//2)*(cell_height+25)
            draw.text((x+10,y+6),f"Page {start+k+1}",fill="black")
            sheet.paste(page,(x,y+25))
    out=qa/f"current-contact-{start//4+1:02}.png"
    sheet.save(out)
    contact_files.append(str(out))
(qa/"current_render_receipt.json").write_text(json.dumps(
    {"pages":count,"render":"Poppler pdftoppm 85 dpi","resource":resource,
     "contact_sheets":contact_files,"visual_inspection":"pending",
     "previous_reviewed_pdf_sha256":previous.get("pdf_sha256"),
     "unchanged_previously_reviewed_pages":unchanged,
     "pages_requiring_inspection":changed,
     "pdf_page_points":[width,height]},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"pages":count,"contact_sheets":len(contact_files),"resource":resource,
                  "unchanged_previously_reviewed":len(unchanged),
                  "pages_requiring_inspection":changed}))
