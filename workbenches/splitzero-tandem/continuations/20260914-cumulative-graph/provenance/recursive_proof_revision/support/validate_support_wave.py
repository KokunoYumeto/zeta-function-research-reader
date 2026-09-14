from pathlib import Path
import hashlib,json,re,subprocess
S=Path(__file__).resolve().parent
base=Path(r'workspace:\work\cumulative_deligne_build_20260913_v2')
staged=S/'updated'
prefix=(base/'tex/main.tex').read_text(encoding='utf-8').split('\\begin{document}')[0]
main=prefix+'\\begin{document}\n'
for f in ['tau_mixed_coefficient_face_attachment.tex','support_diagrams.tex','tau_chain.tex','tau_boundary.tex']:
    main+='\\input{tex/'+f+'}\n'
main+='\\end{document}\n'
(staged/'SUPPORT_WAVE_CHECK.tex').write_text(main,encoding='utf-8')
exe=r'runtime:tex\miktex\bin\x64\lualatex.exe'
results=[]
for iteration in [1,2]:
    p=subprocess.run([exe,'-interaction=nonstopmode','-halt-on-error','SUPPORT_WAVE_CHECK.tex'],cwd=staged,capture_output=True,text=True,encoding='utf-8',errors='replace')
    (S/f'compile_pass_{iteration}.txt').write_text(p.stdout+p.stderr,encoding='utf-8')
    results.append({'pass':iteration,'exit':p.returncode})
    if p.returncode: break
log=(staged/'SUPPORT_WAVE_CHECK.log').read_text(encoding='utf-8',errors='replace')
oldtc=(S/'provenance/tex/tau_chain.tex').read_text(encoding='utf-8')
newtc=(S/'updated/tex/tau_chain.tex').read_text(encoding='utf-8')
oldprefix=oldtc.split('\\subsection{Original supported maps and the precise result delivered}')[0]
oldtail=oldtc[oldtc.index('The new conclusions are'):]
checks={
    'baseline_files_preserved':all((S/'provenance/tex'/f).read_bytes()==(base/'tex'/f).read_bytes() for f in ['support_diagrams.tex','tau_chain.tex','tau_boundary.tex']),
    'D1_D8_full_body_preserved':(S/'updated/tex/support_diagrams.tex').read_text(encoding='utf-8').startswith((S/'provenance/tex/support_diagrams.tex').read_text(encoding='utf-8')),
    'TC1_TC28_full_body_preserved':newtc.startswith(oldprefix),
    'TC_conclusions_full_body_preserved':newtc.endswith(oldtail),
    'compile_passed':all(r['exit']==0 for r in results) and len(results)==2,
}
out={'scope':'Complete staged support wave compile and source-preservation check; other cumulative-reader cross-references require root assembly. PDF is internal compile output, not a delivered visually checked artifact.','checks':checks,'passes':results,'pages':re.findall(r'Output written on .*?\((\d+) pages',log),'undefined_references':re.findall(r"LaTeX Warning: Reference `(.*?)'",log),'overfull_boxes':re.findall(r'Overfull \\[hv]box.*',log)}
(S/'VALIDATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
if not all(checks.values()):raise SystemExit(1)
