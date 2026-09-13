"""Render the complete standalone proof with Poppler; prepare bounded visual QA."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
PREFIX = "gamma_seed_intervals_20260913_source_costs_standalone"
pdf = ROOT / (PREFIX + ".pdf")
qa = ROOT / (PREFIX + "_qa")
qa.mkdir(exist_ok=True)
poppler = shutil.which("pdftoppm")
if not poppler:
    raise RuntimeError("Poppler renderer is required")
completed = subprocess.run([poppler, "-r", "110", "-png", str(pdf), str(qa / "page")],
                           capture_output=True, text=True, timeout=60)
if completed.returncode:
    raise RuntimeError(completed.stderr)
pages = sorted(qa.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
for group in range(0, len(pages), 3):
    chosen = pages[group:group+3]
    images = [Image.open(p).convert("RGB") for p in chosen]
    width = max(i.width for i in images)
    height = max(i.height for i in images)
    sheet = Image.new("RGB", (3*width, height+36), "#dddddd")
    draw = ImageDraw.Draw(sheet)
    for index, (source, img) in enumerate(zip(chosen, images)):
        sheet.paste(img, (index*width, 36))
        draw.text((index*width+15, 10), source.stem, fill="black")
    sheet.save(qa / f"contact-{group//3+1:02d}.png")
document = fitz.open(pdf)
out_of_page = []
for page_number, page in enumerate(document, 1):
    for word in page.get_text("words"):
        x0, y0, x1, y1 = word[:4]
        if x0 < 0 or y0 < 0 or x1 > page.rect.width or y1 > page.rect.height:
            out_of_page.append({"page": page_number, "text": word[4], "rect": list(word[:4])})
log = (ROOT / (PREFIX + ".log")).read_text(encoding="utf-8", errors="replace")
issues = {"latex_error": len(re.findall(r"^!", log, re.M)),
          "warnings": len(re.findall(r"(?:Package [^\n]* Warning:|LaTeX Warning:|pdfTeX warning)", log)),
          "overfull": len(re.findall("Overfull", log)),
          "underfull": len(re.findall("Underfull", log))}
payload = {"schema": "gamma-seed-proof-render-v1", "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
           "pages": len(document), "poppler_dpi": 110, "page_images": len(pages), "log_counts": issues,
           "out_of_page_words": out_of_page,
           "images": [{"file": str(p.relative_to(ROOT)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                      for p in sorted(qa.glob("*.png"))],
           "visual_review": "pending actual viewing"}
out = ROOT / (PREFIX + "_render.json")
out.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"pages": len(document), "issues": issues, "out_of_page_words": len(out_of_page), "qa": str(qa)}))
