"""Rebuild the complete editable proof volume using LuaLaTeX."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--engine',default='lualatex')
    args=p.parse_args()
    engine=shutil.which(args.engine)
    if not engine: raise SystemExit('LuaLaTeX is required; install a standard TeX distribution including the packages used in actual-cohomology-proofs.tex.')
    root=Path(__file__).resolve().parent
    build=root/'rebuild';build.mkdir(exist_ok=True)
    source=root/'actual-cohomology-proofs.tex'
    for n in range(1,4):
        run=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+str(build),source.name],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
        (build/f'pass-{n}.txt').write_bytes(run.stdout)
        if run.returncode:
            sys.stdout.buffer.write(run.stdout[-7000:])
            return run.returncode
    pdf=build/'actual-cohomology-proofs.pdf'
    print(json.dumps({'pdf':str(pdf),'bytes':pdf.stat().st_size,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()},indent=2))
    return 0
if __name__=='__main__':sys.exit(main())
