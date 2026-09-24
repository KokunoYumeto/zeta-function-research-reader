from pathlib import Path
import hashlib, json, shutil, subprocess, re
r=Path(__file__).resolve().parent
parts=json.loads((r/'proof_inputs.json').read_text(encoding='utf-8'))
for row in parts:
    assert hashlib.sha256((r/row['path']).read_bytes()).hexdigest()==row['sha256'], row['path']
for stem, selected, heading in [
 ('DELIGNE_WEIGHT_CONTROL_FULL',parts[:8],'Complete reading and witness record'),
 ('RECONSTRUCTION_AND_WEIGHT_FULL',parts,'Current Deligne reading coverage and witness record')]:
    out=(r/(stem+'.introduction.md')).read_text(encoding='utf-8')
    for row in selected:
        p=r/row['path']
        out+='\n\n---\n\n# '+row['title']+'\n\nProof source: `'+p.name+'`.\n\n'+p.read_text(encoding='utf-8-sig')+'\n'
    out+='\n\n---\n\n# '+heading+'\n\n'+(r/'DELIGNE_FULL_READING_LOG.md').read_text(encoding='utf-8')
    public='https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/'
    def proof_link(m):
        target=m[1]
        if '://' in target or target.startswith('#'):return m[0]
        filename=target.split('#')[0].split('/')[-1]
        anchor=('#'+target.split('#',1)[1]) if '#' in target else ''
        if (r/'proofs'/filename).is_file():return ']('+public+'proofs/'+filename+anchor+')'
        if (r/filename).is_file():return ']('+public+filename+anchor+')'
        return m[0]
    out=re.sub(r'\]\(([^)]+\.md(?:#[^)]*)?)\)',proof_link,out)
    md=r/(stem+'.md'); md.write_text(out,encoding='utf-8')
    pandoc=shutil.which('pandoc')
    if pandoc:
        subprocess.run([pandoc,str(md),'--from=markdown+tex_math_single_backslash','--to=latex','--standalone','--toc','--lua-filter='+str(r/'typesetting-code.lua'),'-V','documentclass=report','-V','geometry:margin=25mm','-V','colorlinks=true','--include-in-header='+str(r/'publication-preamble.tex'),'--resource-path='+str(r),'--output='+str(r/(stem+'.tex'))],check=True)
        tex=r/(stem+'.tex'); text=tex.read_text(encoding='utf-8')
        text=re.sub(r'(\\includegraphics(?:\[[^\]]*\])?\{)https://raw\.githubusercontent\.com/[^}]+/([^/}]+)(\})',lambda m:m[1]+m[2]+m[3],text)
        text=re.sub(r'\\texttt\{([a-fA-F0-9]{64})\}',lambda m:r'\sourcehash{'+m[1]+'}',text)
        text=re.sub(r'(?<=[\s:])([a-f0-9]{40,64})(?=[\s,.;])',lambda m:r'\sourcehash{'+m[1]+'}',text)
        text=re.sub(r'\\\(\\sourcehash\{([a-fA-F0-9]{40,64})\}\\\)',lambda m:r'\sourcehash{'+m[1]+'}',text)
        tex.write_text(text,encoding='utf-8')
    else:
        print('Markdown rebuilt; install Pandoc to regenerate the included TeX.')
print('All proof-input hashes verified; complete readers rebuilt.')
