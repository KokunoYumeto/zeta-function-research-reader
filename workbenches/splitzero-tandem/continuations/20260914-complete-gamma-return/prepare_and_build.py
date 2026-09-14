"""Build the final accepted complete Gamma source cut once pins are supplied.

Run `python prepare_and_build.py prepare` then `... build`. The final
proof pin file is supplied by the mathematical owner. The previous
source documents are copied verbatim; all presentation changes are
recorded as exact reversible strings. Never modifies their author files.
"""
from pathlib import Path
import sys,json,hashlib,re,shutil,subprocess,os
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parent
XELATEX=Path(os.environ.get('XELATEX_BIN') or shutil.which('xelatex') or r'C:\Users\Floris\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p):return {'bytes':p.stat().st_size,'sha256':sha(p)}
def require(v,msg):
    if not v:raise RuntimeError(msg)
def save(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def prepare():
    config=json.loads((BASE/'FINAL_PROOF_PINS.json').read_text())
    require(config['status']=='Final complete proofs accepted for this build','Final proof pins not accepted')
    transforms=[]
    for name,r in config['proofs'].items():
        source=Path(r['path']);require(sha(source)==r['sha256'],'Final author source changed: '+name)
        raw=source.read_bytes();dest=BASE/'originals'/r['original_filename'];dest.parent.mkdir(exist_ok=True)
        require(not dest.exists(),'Preserve existing source snapshot');dest.write_bytes(raw)
        text=raw.decode('utf8');normalized=text.replace('\r\n','\n');body=normalized
        operations=[]
        if '\\begin{document}' in body:
            before,body=body.split('\\begin{document}',1)
            require(body.count('\\end{document}')==1,'Document suffix ambiguous')
            body,after=body.split('\\end{document}',1)
            operations.append({'kind':'document_wrapper_removal','prefix':before+'\\begin{document}','suffix':'\\end{document}'+after})
            require(body.count('\\maketitle')==1,'Source title occurrence differs')
            title_index=body.index('\\maketitle')
            body=body.replace('\\maketitle','',1)
            operations.append({'kind':'source_title_removed','exact':'\\maketitle','index':title_index})
        if name=='PHT':
            old='\\input{independent_contiguous.tex}';new='\\input{sources/HCT.tex}'
            require(body.count(old)==1,'Contiguous input occurrence differs');body=body.replace(old,new,1)
            operations.append({'kind':'relative_input_path','before':old,'after':new})
        fragment=BASE/'sources'/f'{name}.tex';fragment.parent.mkdir(exist_ok=True);fragment.write_text(body,encoding='utf8')
        recovered=fragment.read_text(encoding='utf8')
        for op in reversed(operations):
            if op['kind']=='relative_input_path':
                require(recovered.count(op['after'])==1,'Reverse input path ambiguous');recovered=recovered.replace(op['after'],op['before'],1)
            elif op['kind']=='source_title_removed':recovered=recovered[:op['index']]+op['exact']+recovered[op['index']:]
            elif op['kind']=='document_wrapper_removal':recovered=op['prefix']+recovered+op['suffix']
        require(recovered==normalized,'Full original source is not exactly recovered')
        oldtags=re.findall(r'\\tag\{([^}]+)\}',normalized);newtags=re.findall(r'\\tag\{([^}]+)\}',body)
        require(oldtags==newtags,'Original equation tags differ')
        transforms.append({'name':name,'source':str(source),'original':dest.relative_to(BASE).as_posix(),**pin(dest),'fragment':fragment.relative_to(BASE).as_posix(),'fragment_pin':pin(fragment),'equation_tags':newtags,'line_ending_transport':'CRLF decoded as LF only; raw original bytes retained','exact_full_source_inverse_verified':True,'operations':operations})
    save(BASE/'SOURCE_TRANSPORTS.json',{'utc':datetime.now(timezone.utc).isoformat(),'final_proof_configuration':pin(BASE/'FINAL_PROOF_PINS.json'),'proofs':transforms,'mathematical_changes':0,'all_equation_tags_retained':True})
    print(json.dumps({'status':'Final proof bodies prepared','inputs':len(transforms)}),flush=True)
def build():
    trans=json.loads((BASE/'SOURCE_TRANSPORTS.json').read_text());require(len(trans['proofs'])==3,'Need all three complete source bodies')
    for r in trans['proofs']:
        require(pin(BASE/r['fragment'])==r['fragment_pin'],'Prepared proof differs')
    (BASE/'build').mkdir(exist_ok=True)
    for i in range(1,4):
        cmd=[str(XELATEX),'-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','Complete_Gamma_Return.tex']
        result=subprocess.run(cmd,cwd=BASE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (BASE/'build'/f'pass{i}.stdout.txt').write_bytes(result.stdout)
        require(result.returncode==0,f'Compiler pass{i} failed; see stdout')
    log=(BASE/'Complete_Gamma_Return.log').read_text(encoding='utf8',errors='replace')
    warnings={k:re.findall(pattern,log) for k,pattern in {'overfull':r'Overfull[^\n]*','undefined':r'LaTeX Warning: (?:Reference|Citation)[^\n]*','missing_glyph':r'Missing character[^\n]*','generic':r'(?:LaTeX|Package [^ ]+) Warning:[^\n]*'}.items()}
    import fitz
    pdf=BASE/'Complete_Gamma_Return.pdf';doc=fitz.open(pdf)
    require(len(doc)>0,'Empty PDF')
    receipt={'utc':datetime.now(timezone.utc).isoformat(),'status':'Three-pass combined proof build; actual visual review still required','pdf':{'path':pdf.name,**pin(pdf)},'pages':len(doc),'warnings':warnings,'source_transports':pin(BASE/'SOURCE_TRANSPORTS.json'),'actual_visual_acceptance':False}
    save(BASE/'BUILD_RECEIPT.json',receipt);print(json.dumps(receipt),flush=True)
if __name__=='__main__':
    require(len(sys.argv)==2 and sys.argv[1] in ('prepare','build'),'Use prepare or build')
    (prepare if sys.argv[1]=='prepare' else build)()
