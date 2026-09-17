"""Render every page with Poppler and assemble numbered contact sheets."""
from pathlib import Path
import json
import math
import subprocess
import hashlib
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
BUILD = HERE.parent / "build"
RENDER = BUILD / "rendered"
RENDER.mkdir(exist_ok=True)
pdf = BUILD / "DUAL_WEB_PROOF_SUPPLEMENT.pdf"
pdf_sha256 = hashlib.sha256(pdf.read_bytes()).hexdigest()
subprocess.run(["pdftoppm", "-r", "110", "-png", str(pdf), str(RENDER / "page")], check=True)
if hashlib.sha256(pdf.read_bytes()).hexdigest() != pdf_sha256:
    raise RuntimeError("PDF changed during rendering")
pages = sorted(RENDER.glob("page-*.png"))
sheet_files = []
for start in range(0, len(pages), 12):
    subset = pages[start:start+12]
    canvas = Image.new("RGB", (1200, 600*math.ceil(len(subset)/3)), "#dddddd")
    draw = ImageDraw.Draw(canvas)
    for i, path in enumerate(subset):
        im = Image.open(path).convert("RGB")
        im.thumbnail((390, 560))
        x, y = (i % 3)*400 + 5, (i // 3)*600 + 25
        canvas.paste(im, (x, y))
        draw.text((x+8, y-18), f"Page {start+i+1}", fill="black")
    dest = RENDER / f"contact-{start+1:03d}-{start+len(subset):03d}.png"
    canvas.save(dest)
    sheet_files.append(str(dest))
(BUILD / "RENDER_INDEX.json").write_text(json.dumps({"pdf_sha256":pdf_sha256,"pages_rendered":len(pages),"dpi":110,"contact_sheets":sheet_files,"page_pngs":[{"path":str(p),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in pages]},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"pages_rendered":len(pages),"contact_sheets":sheet_files},indent=2))
