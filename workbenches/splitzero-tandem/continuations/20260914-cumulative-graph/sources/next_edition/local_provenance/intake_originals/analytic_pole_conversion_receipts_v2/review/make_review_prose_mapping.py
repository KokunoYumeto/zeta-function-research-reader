"""Exact ordinary-prose mathematics spans in the full original analytic review."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parent.parent
SOURCE=Path('F:/user/Documents/Papors/Chatnotes/Zeta-Function-Foundation/agents/zenodo_workspace_publication/integration_20260913_next/post_pr26_intake/parent_review/f1_unit_gauge/ANALYTIC_POLE_INDEPENDENT_REVIEW.md')
raw=SOURCE.read_bytes();text=raw.decode('utf-8')
assert hashlib.sha256(raw).hexdigest()=='5dc90ea5d545b674faf02d5f05ccdbd32efdeb03c6b27df793fbedaf32f91d0a'
blocked=[(m.start(),m.end(),'original_inline_Code') for m in re.finditer(r'`[^`\r\n]+`',text)]
blocked += [(m.start(),m.end(),'heading') for m in re.finditer(r'^#+[^\r\n]*',text,re.M)]
blocked += [(m.start(),m.end(),'hash') for m in re.finditer(r'\b[0-9a-f]{64}\b',text)]
TYPED={
 'u=t=0':r'u=t=0','Phi(0)=0':r'\Phi(0)=0','A_ext(0)':r'A_{\mathrm{ext}}(0)',
 'Phi(0)':r'\Phi(0)','w(p)':r'w(p)','h(p)':r'h(p)','A(t)':r'A(t)',
 't+ua':r't+ua','n+d':r'n+d','d+r':r'd+r','s-p':r's-p','t/u':r't/u',
 'r>0':r'r>0','d>0':r'd>0','r=0':r'r=0','u=0':r'u=0','p=0':r'p=0','t=0':r't=0',
 '-n':r'-n','Q_0':r'Q_0','e_0':r'e_0','B_0':r'B_0','A_ext':r'A_{\mathrm{ext}}',
 'H_p':r'H_p','wF':r'wF','DQ':r'DQ','nu':r'\nu','Phi':r'\Phi','tau':r'\tau',
 'h':'h','w':'w','M':'M','D':'D','u':'u','Q':'Q','p':'p','F':'F','t':'t',
 'n':'n','d':'d','L':'L','s':'s','W':'W','r':'r',
}
pattern=re.compile(r"(?<![A-Za-z0-9_'’])(?:"+'|'.join(re.escape(s) for s in sorted(TYPED,key=len,reverse=True))+r')(?![A-Za-z0-9_])')
rows=[]
def add(start,end,tex,reason):
 assert not any(start<b and a<end for a,b,_ in blocked)
 original=text[start:end]
 rows.append({'source_byte_start':len(text[:start].encode('utf-8')),'source_byte_end':len(text[:end].encode('utf-8')),
              'source_char_start':start,'source_char_end':end,'source_line':text[:start].count('\n')+1,
              'original':original,'tex':tex,'reason':reason,
              'context_before':text[max(0,start-65):start],'context_after':text[end:end+65]})
for m in pattern.finditer(text):
 if any(m.start()<b and a<m.end() for a,b,_ in blocked):continue
 add(m.start(),m.end(),TYPED[m.group()],
     'Mathematical variable or complete expression in the original proof-review prose; the surrounding original words remain unchanged.')
MANUAL=[
 ('coefficientwise in a.', 'a', 'The finite-flow parameter a; the preceding words make this distinct from the English article.'),
 ('nonzero-a transport', 'a', 'The finite-flow parameter a in the original nonzero-a scope statement.'),
 ('with A. This confirms', 'A', 'The original endpoint companion matrix A in the intertwining statement.'),
 ('original A. At u=t=0', 'A', 'The original quotient action matrix A.'),
 ('commutes with A on the full algebra', 'A', 'The original companion multiplication matrix A whose commuting action is stated.'),
]
for context,token,reason in MANUAL:
 assert text.count(context)==1
 start=text.index(context)
 # The final standalone token a in the first phrase and the single indicated
 # uppercase A are unique within each controlling context.
 hits=list(re.finditer(r'(?<![A-Za-z0-9_])'+re.escape(token)+r'(?![A-Za-z0-9_])',context))
 assert len(hits)==1
 start+=hits[0].start();add(start,start+len(token),token,reason)
rows.sort(key=lambda row:row['source_byte_start'])
for a,b in zip(rows,rows[1:]):assert a['source_byte_end']<=b['source_byte_start']
for row in rows:assert raw[row['source_byte_start']:row['source_byte_end']].decode('utf-8')==row['original']
for i,row in enumerate(rows):row['prose_math_index']=i
result={
 'schema':'complete-original-prose-math-span-map-v1','key':'analytic_pole_review',
 'source':{'path':str(SOURCE),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},
 'prose_math_mappings':rows,
 'excluded_original_code_spans':[{'start_byte':len(text[:a].encode('utf-8')),'end_byte':len(text[:b].encode('utf-8'))} for a,b,kind in blocked if kind=='original_inline_Code'],
 'notation_dictionary':[
  {'original':'nu; Phi; tau','typed':r'\nu;\Phi;\tau','meaning':'The original polynomial unit representative, fixed primitive and tau base; no object or primitive constant is changed.'},
  {'original':'A_ext; A; A(t); W; B_0; Q_0','typed':r'A_{\mathrm{ext}};A;A(t);W;B_0;Q_0','meaning':'The exact original extension/companion matrices, weighted residue matrix, coupling matrix and endpoint columns.'},
  {'original':'a','typed':'a','meaning':'Only the two source occurrences denoting the finite-flow parameter are mapped. English articles and the pronoun I are excluded.'},
 ],
 'scope':'Complete ordinary-prose mathematical notation outside existing Code spans, headings, references and hashes. No source wording, mathematical assertion, source bytes or previously sealed v1 artifact is edited.',
 'source_unchanged':SOURCE.read_bytes()==raw,
}
target=ROOT/'mapping/review_prose_math.json';target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
for row in rows:print(row['prose_math_index'],row['source_line'],repr(row['original']),'=>',repr(row['tex']),repr(row['context_before'][-25:]+row['original']+row['context_after'][:25]))
print(json.dumps({'mapping':str(target),'bytes':len(target.read_bytes()),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'prose_math_spans':len(rows)}))
