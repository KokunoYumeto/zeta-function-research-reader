"""Render every PDF page and create contact sheets plus geometric text checks."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
import subprocess
from pathlib import Path

import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = ROOT / "Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--dpi", type=int, default=95)
    args = parser.parse_args()
    out = ROOT / "build" / "qa"
    pages_dir = out / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    # Only prior generated page images in this checked output directory are
    # removed; otherwise a shorter revised PDF could retain obsolete pages.
    for prior in pages_dir.glob("page-*.png"):
        if prior.resolve().parent != pages_dir.resolve():
            raise RuntimeError("Unexpected render cleanup target")
        prior.unlink()
    poppler = shutil.which("pdftoppm")
    if not poppler:
        raise RuntimeError("pdftoppm is required for the complete visual render")
    result = subprocess.run([poppler, "-r", str(args.dpi), "-png", str(args.pdf),
                             str(pages_dir / "page")], capture_output=True, text=True)
    (out / "poppler.log").write_text(result.stdout + result.stderr, encoding="utf-8")
    if result.returncode:
        raise RuntimeError("Poppler render failed")
    document = fitz.open(args.pdf)
    out_of_page = []
    margin_crossings = []
    texts = []
    for index, page in enumerate(document):
        texts.append(page.get_text())
        for x0, y0, x1, y1, word, *_ in page.get_text("words"):
            if x0 < -0.5 or y0 < -0.5 or x1 > page.rect.width + 0.5 or y1 > page.rect.height + 0.5:
                out_of_page.append({"page": index + 1, "text": word,
                                    "box": [x0, y0, x1, y1]})
            if 75 < y0 < page.rect.height - 65 and (x0 < 55 or x1 > page.rect.width - 55):
                margin_crossings.append({"page": index + 1, "text": word,
                                         "box": [x0, y0, x1, y1]})
    (out / "extracted_text.txt").write_text("\n\n\f\n\n".join(texts), encoding="utf-8")
    rendered = sorted(pages_dir.glob("page-*.png"),
                      key=lambda p: int(p.stem.split("-")[-1]))
    if len(rendered) != len(document):
        raise RuntimeError("Rendered page count does not equal PDF page count")
    columns, rows = 3, 2
    cell_w, cell_h = 500, 730
    sheets = []
    for start in range(0, len(rendered), columns * rows):
        sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "#d9dde3")
        draw = ImageDraw.Draw(sheet)
        for offset, file in enumerate(rendered[start:start + columns * rows]):
            im = Image.open(file).convert("RGB")
            im.thumbnail((cell_w - 20, cell_h - 40))
            x = (offset % columns) * cell_w + (cell_w - im.width) // 2
            y = (offset // columns) * cell_h + 25
            sheet.paste(im, (x, y))
            draw.text(((offset % columns) * cell_w + 12,
                       (offset // columns) * cell_h + 7), f"Page {start + offset + 1}", fill="black")
        path = out / f"contact-{start // (columns * rows) + 1:03d}.jpg"
        sheet.save(path, quality=88)
        sheets.append(str(path))
    receipt = {
        "pdf": str(args.pdf), "pdf_sha256": hashlib.sha256(args.pdf.read_bytes()).hexdigest(),
        "pages": len(document), "rendered_pages": len(rendered), "dpi": args.dpi,
        "out_of_page_words": out_of_page, "body_margin_crossings": margin_crossings,
        "contact_sheets": sheets,
        "visual_review": "Rendered for inspection; this script does not assert visual approval.",
    }
    (out / "qa_receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps({"pages": len(document), "contact_sheets": len(sheets),
                      "out_of_page_words": len(out_of_page),
                      "body_margin_crossings": len(margin_crossings),
                      "receipt": str(out / "qa_receipt.json")}))


if __name__ == "__main__":
    main()
