"""Read-only navigation, metadata and literal page-number inspection."""
from pathlib import Path
import hashlib
import json
import argparse
import fitz

ROOT=Path(__file__).resolve().parent
PDF=ROOT.parents[2]/'output/Split_Zero_Recursive_Integration_2026-09-13/repository/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
PIN='a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
parser=argparse.ArgumentParser()
parser.add_argument('--pdf',type=Path,default=PDF)
parser.add_argument('--sha256',default=PIN)
parser.add_argument('--output',type=Path,default=ROOT/'GLOBAL_NAVIGATION_CHECK.json')
args=parser.parse_args()
PDF=args.pdf;PIN=args.sha256
assert hashlib.sha256(PDF.read_bytes()).hexdigest()==PIN
document=fitz.open(PDF)
toc=document.get_toc(simple=False)
bad_toc=[row[:3] for row in toc if not 1<=row[2]<=len(document)]
footer_mismatches=[]
internal_links=0
bad_links=[]
for number,page in enumerate(document,1):
    footer=page.get_text(clip=fitz.Rect(0,785,page.rect.width,page.rect.height)).strip()
    # The current main.tex titlepage has two physical pages. LaTeX's
    # titlepage environment resets the following contents page to page 1.
    expected='' if number==1 else '2' if number==2 else str(number-2)
    if footer!=expected:footer_mismatches.append({'page':number,'literal_footer_text':footer,'expected':expected})
    for link in page.get_links():
        if link.get('kind')==fitz.LINK_GOTO:
            internal_links+=1
            if not 0<=link.get('page',-1)<len(document):bad_links.append({'source_page':number,'link':link})
report={'scope':'Read-only global navigation and literal page-number checks; visual acceptance recorded separately.',
        'pdf':str(PDF),'pdf_sha256':PIN,'pages':len(document),'metadata':document.metadata,
        'outline_entries':len(toc),'invalid_outline_destinations':bad_toc,
        'internal_links':internal_links,'invalid_internal_links':bad_links,
        'pagination_rule':f'Physical page 1 has no footer; physical page 2 is title continuation numbered 2; titlepage end resets physical page 3 to 1, then consecutive through printed page {len(document)-2}.',
        'footer_text_mismatches':footer_mismatches,
        'pdf_unchanged':hashlib.sha256(PDF.read_bytes()).hexdigest()==PIN}
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='metadata'},indent=2))
