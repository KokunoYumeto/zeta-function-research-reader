"""Prepare complete endpoint TeX bodies and exact reversible source maps only."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

WORK=Path(__file__).resolve().parent
OUT=WORK/'endpoint_reader_prepared_20260913'/'proof_bodies'
PROOFS=[
 ('gamma_endpoint_window_bridge_20260913.tex','gamma_endpoint_window_bridge.tex',
  'Exact endpoint windows: Gamma coefficients, paired Schur volumes, and intrinsic sensitivity',
  'e8d6152532c98532a062b5840834d934b28f29490ec926f47c2bce1af3493854'),
 ('arithmetic_endpoint_leading_line_transport_20260913.tex','arithmetic_endpoint_leading_line_transport.tex',
  'The original leading-coefficient line and its arithmetic relation image',
  'ae87f325b66c3e07830eb0362657cad0825d84d23dd38b5c7500f1deda154962'),
 ('endpoint_product_sharpening_20260913.tex','endpoint_product_sharpening.tex',
  'Exact window products, sharp endpoint optimization, and original relation costs',
  'b4f9481976ad03bb8e321464f937d3777af15581241ece1f78aaa5c56e49b924')]

def digest(data):return hashlib.sha256(data).hexdigest()
def require(ok,message):
 if not ok:raise RuntimeError(message)
def braced(text,start):
 require(text[start]=='{','expected brace')
 depth=0
 for end in range(start,len(text)):
  if text[end]=='{' and (end==0 or text[end-1]!='\\'):depth+=1
  if text[end]=='}' and (end==0 or text[end-1]!='\\'):
   depth-=1
   if depth==0:return text[start+1:end],end+1
 raise RuntimeError('unclosed macro body')
def macros(preamble):
 result=[]
 for m in re.finditer(r'\\(?:newcommand|renewcommand|providecommand)\s*',preamble):
  name,end=braced(preamble,m.end())
  while end<len(preamble) and preamble[end].isspace():end+=1
  require(preamble[end]=='{','argument-taking macro requires explicit adapter')
  body,end=braced(preamble,end)
  require(re.fullmatch(r'\\[A-Za-z]+',name) is not None,'unexpected macro name')
  result.append({'name':name,'body':body,'original_declaration':preamble[m.start():end],
                 'local_declaration':'\\def'+name+'{'+body+'}'})
 return result
def index(text):
 return [{'label':m[1],'line':text.count('\n',0,m.start())+1}
         for m in re.finditer(r'\\tag\{([^}]+)\}',text)]
def math_spans(text):
 pattern=r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$|\\begin\{equation\*?\}.*?\\end\{equation\*?\}'
 return re.findall(pattern,text,re.S)
def lower_headings(body):
 return re.sub(r'\\(section|subsection)(?=\*?[\[{])',
               lambda m:'\\'+{'section':'subsection','subsection':'subsubsection'}[m[1]],body)

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 rows=[]
 for source_name,target_name,title,expected in PROOFS:
  raw=(WORK/source_name).read_bytes()
  require(digest(raw)==expected,'source changed: '+source_name)
  source=raw.decode('utf-8-sig')
  require(source.count(r'\begin{document}')==1 and source.count(r'\end{document}')==1,'document boundary count')
  preamble,tail=source.split(r'\begin{document}')
  body,after=tail.split(r'\end{document}')
  require(not after.strip(),'trailing source content')
  require(body.count(r'\maketitle')==1,'sole title command required')
  declarations=macros(preamble)
  require(not re.search(r'\\(?:DeclareMathOperator|def|let)\b',preamble),'unsupported preamble macro')
  retained=lower_headings(body.replace(r'\maketitle','',1))
  prefix='\\begingroup\n'+'\n'.join(x['local_declaration'] for x in declarations)+'\n\\section{'+title+'}\n'
  fragment=(prefix+retained+'\n\\endgroup\n').encode('utf-8')
  # Reconstruct the retained body as a whole; only the listed header operations exist.
  require(fragment.decode()[len(prefix):-len('\n\\endgroup\n')]==retained,'body extent mismatch')
  original_math=math_spans(body)
  require(original_math==math_spans(fragment.decode()),'original ordered mathematical spans changed')
  require([x['label'] for x in index(body)]==[x['label'] for x in index(fragment.decode())],'equation labels changed')
  path=OUT/target_name;path.write_bytes(fragment)
  rows.append({'source':source_name,'source_bytes':len(raw),'source_sha256':expected,
               'prepared_path':path.relative_to(WORK).as_posix(),'suggested_reader_path':'tex/'+target_name,
               'prepared_bytes':len(fragment),'prepared_sha256':digest(fragment),
               'source_document_body_sha256':digest(body.encode()),'retained_body_sha256':digest(retained.encode()),
               'original_math_span_count':len(original_math),'ordered_math_spans_sha256':digest(json.dumps(original_math,ensure_ascii=False).encode()),
               'original_ordered_math_spans_equal':True,
               'complete_body_preserved':True,'changes':['remove sole maketitle','lower section/subsection one level','wrap full body in local macro group and new title'],
               'local_macros':declarations,'source_equations':index(source),'reader_equations':index(fragment.decode()),
               'original_preexisting_environments':['theorem','lemma','proposition','proof'],
               'build_or_typesetting_execution':False})
 receipt={'schema':'endpoint-complete-proof-body-preparation-v1','status':'prepared full bodies only; no cumulative edits/build',
          'proofs':rows,'source_index_scope':'Every equation tag and complete document-body extent; no mathematical rewriting or excerpting.'}
 target=WORK/'endpoint_reader_full_proof_body_plan_20260913.json'
 target.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'receipt':target.name,'sha256':digest(target.read_bytes()),'complete_proofs':len(rows)},indent=2))

if __name__=='__main__':main()
