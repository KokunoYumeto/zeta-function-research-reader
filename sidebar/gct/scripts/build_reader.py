"""Build the standalone cumulative reader within this output root."""
from pathlib import Path
import subprocess, json, re
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'build').mkdir(parents=True,exist_ok=True)
(ROOT/'checks').mkdir(parents=True,exist_ok=True)
base=(ROOT/'bibliography.bib').read_text(encoding='utf-8')
parts=[base]
for name in ['agents/nonstandard_rh/nonstandard_rh_sources.bib','agents/gct_obstruction_literature/sources.bib',
             'agents/coefficient_geometry/additions.bib',
             'agents/compressed_permanent_trace/additions.bib',
             'agents/ns_scaling_bridge/additions.bib']:
    path=ROOT/name
    parts.append(path.read_text(encoding='utf-8'))
(ROOT/'build/combined.bib').write_text('\n'.join(parts),encoding='utf-8')
cmds=[['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build','tex/main.tex'],
      ['bibtex','build/main'],
      ['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build','tex/main.tex'],
      ['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build','tex/main.tex']]
records=[]
for i,cmd in enumerate(cmds):
    run=subprocess.run(cmd,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    text=run.stdout.decode('utf-8',errors='replace')
    (ROOT/f'build/build_step_{i}.txt').write_text(text,encoding='utf-8')
    records.append({'command':cmd,'returncode':run.returncode})
    if run.returncode:
        print(text[-7000:]); raise SystemExit(run.returncode)
log=(ROOT/'build/main.log').read_text(encoding='utf-8',errors='replace')
warnings=[x for x in log.splitlines() if any(t in x for t in ['Overfull','undefined','multiply defined','LaTeX Warning'])]
(ROOT/'checks/build.json').write_text(json.dumps({'commands':records,'warnings':warnings},indent=2),encoding='utf-8')
if warnings:
    print(json.dumps({'warnings':warnings})); raise SystemExit(1)
(ROOT/'reader.pdf').write_bytes((ROOT/'build/main.pdf').read_bytes())
print(json.dumps({'pdf':str(ROOT/'reader.pdf'),'warnings':warnings}))
