"""Build the already assembled standalone proof reader with XeLaTeX."""
from pathlib import Path
import os
import shutil
import subprocess
import json
import hashlib

ROOT=Path(__file__).resolve().parents[1]
def main():
    engine=shutil.which('xelatex')
    if not engine:
        candidate=Path(os.environ.get('LOCALAPPDATA',''))/'Programs/MiKTeX/miktex/bin/x64/xelatex.exe'
        if candidate.is_file():engine=str(candidate)
    if not engine:raise RuntimeError('XeLaTeX is required')
    (ROOT/'build').mkdir(exist_ok=True)
    for turn in range(1,4):
        result=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error','-file-line-error',
              '-output-directory=../build','main.tex'],cwd=ROOT/'tex',capture_output=True)
        (ROOT/'build'/f'pass_{turn}.stdout.txt').write_bytes(result.stdout+result.stderr)
        if result.returncode:
            print(result.stdout.decode('utf-8',errors='replace')[-6500:])
            raise SystemExit(result.returncode)
    out=ROOT/'Tau_Split_Zero_Total_Counterfactual.pdf'
    shutil.copy2(ROOT/'build/main.pdf',out)
    import fitz
    doc=fitz.open(out)
    report={'pages':len(doc),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
      'pdf':str(out),'engine':engine,'passes':3}
    (ROOT/'build/BUILD_RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
