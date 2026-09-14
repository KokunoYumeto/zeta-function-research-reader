"""Compile complete converted fragments under the inherited reader preamble.
This is a syntax/integration check only. It does not assert visual acceptance.
"""
import hashlib,json,re,shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
baseline=ROOT.parent/'cumulative_deligne_build_20260913_v18/tex/main.tex'
keys=sys.argv[1:] or ['tau_base','gamma_review','purity_review','f1_reflection','determinant_review']
target=ROOT/'syntax_check';target.mkdir(exist_ok=True)
preamble=baseline.read_text(encoding='utf-8').split(r'\begin{document}',1)[0]
master=preamble+'\n\\begin{document}\n'+''.join('\\input{tex/'+key+'.tex}\n' for key in keys)+'\\end{document}\n'
tex=target/'syntax_check.tex';tex.write_text(master,encoding='utf-8',newline='')
engine=shutil.which('xelatex')
if not engine:raise RuntimeError('XeLaTeX unavailable')
cmd=[engine,'-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory=syntax_check','syntax_check/syntax_check.tex']
proc=subprocess.run(cmd,cwd=ROOT,capture_output=True)
(target/'engine_output.log').write_bytes(proc.stdout+b'\n'+proc.stderr)
log=(target/'syntax_check.log').read_text(encoding='utf-8',errors='replace') if (target/'syntax_check.log').exists() else ''
receipt={'scope':'Complete fragment compiler syntax check under the inherited cumulative preamble; no visual PDF acceptance or mathematical re-audit.',
 'keys':keys,'engine':engine,'exit_code':proc.returncode,'source_preamble_sha256':hashlib.sha256(preamble.encode()).hexdigest(),
 'overfull_boxes':re.findall(r'Overfull \\hbox[^\n]*',log),'missing_glyphs':re.findall(r'Missing character[^\n]*',log),
 'undefined_controls':'Undefined control sequence' in log,'latex_errors':re.findall(r'^.*(?:LaTeX Error:|^! ).*$',log,re.M),
 'pages_match':re.findall(r'Output written on .*?\((\d+) pages?',log),
 'pdf_created':(target/'syntax_check.pdf').exists(),'visual_acceptance':False}
(target/'SYNTAX_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))
sys.exit(proc.returncode)
