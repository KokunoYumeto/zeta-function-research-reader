from pathlib import Path
import json,re,hashlib
from datetime import datetime, timezone

OUT=Path(__file__).resolve().parent
BASE=Path('workspace:')
ROOT=BASE/'work/backpropagation_20260913/cumulative_source_v1'
graph=json.loads((OUT/'ACTIVE_TEX_SCAN.json').read_text(encoding='utf-8'))

def file_record(path):
    raw=path.read_bytes()
    return {'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}

def group(s,i,left='{',right='}'):
    while i<len(s) and s[i].isspace(): i+=1
    if i>=len(s) or s[i]!=left: raise ValueError((i,s[max(0,i-20):i+50]))
    start=i
    depth=1
    i+=1
    while i<len(s):
        if s[i]=='\\' and i+1<len(s) and s[i+1] in '{}[]\\%':
            i+=2
            continue
        if s[i]==left: depth+=1
        elif s[i]==right: depth-=1
        if depth==0:return s[start+1:i],i+1
        i+=1
    raise ValueError('Unclosed group')

links=[]
errors=[]
for row in graph['roots']['stage']['files']:
    text=(ROOT/row['path']).read_text(encoding='utf-8-sig')
    for m in re.finditer(r'\\(href|hyperlink)\b',text):
        try:
            i=m.end()
            while text[i].isspace():i+=1
            if text[i]=='[':_,i=group(text,i,'[',']')
            target,i=group(text,i)
            display,i=group(text,i)
            kind=('confirmed_mathematical_link_parser_corruption' if (target=='x' and display=='N') or (target=='k+1' and display==r'1+k(m\allowbreak{}\ensuremath{−}\allowbreak{}1)')
                  else 'external_hyperlink' if re.match(r'\w+://|mailto:',target)
                  else 'internal_cross_reference' if m[1]=='hyperlink' or target.startswith('#')
                  else 'source_document_link')
            links.append({'path':row['path'],'line':text.count('\n',0,m.start())+1,
                          'command':m[1],'target':target,'display':display,'complete_command':text[m.start():i],
                          'classification':kind})
        except Exception as e:
            errors.append({'path':row['path'],'line':text.count('\n',0,m.start())+1,'error':str(e)})

source_inherited=BASE/'work/backpropagation_20260913/cohort_staging/ta_c47/snapshots/C47_repository/dependencies/dependencies/MATHEMATICAL_NOTE.md'
source_pr13=ROOT/'sources/web_pr_13/files/workbenches/tau-orthogonal-boundary-control/RESEARCH_NOTE.md'
inherited_old=r'I\textsuperscript{G=p}(-1)(I)'
pr13_old=r'f\_j\^{}\href{x}{N}'
proposals=[
    {'id':'inherited_paired_caret_exponents','active_relative_path':'tex/cohorts/inherited/MATHEMATICAL_NOTE_COMPLETE.tex',
     'active_line':100,'source':file_record(source_inherited),'source_line':49,
     'source_exact_phrase':'For I⊲R let I^G=p^(-1)(I)=I union {tau}.',
     'source_full_line':source_inherited.read_text(encoding='utf-8-sig').splitlines()[48],
     'old_tex':inherited_old,'proposed_tex':r'\(I^G=p^{(-1)}(I)\)',
     'reason':'Pandoc consumed the independent exponent carets surrounding G=p as a single superscript delimiter pair. The source assigns exponent G to I and exponent (-1) to p, retaining the displayed argument (I).',
     'additional_source_confirmation':{'line':53,'exact_phrase':'Equivalently every J is either {tau} or uniquely I^G. The whole ideal poset has one additional bottom element below (0_R)^G={tau,e}.'},
     'original_source_changed':False},
    {'id':'pr13_bracket_exponent_and_argument_as_link','active_relative_path':'build/source_pr_13.tex',
     'active_line':272,'source':file_record(source_pr13),'source_line':168,
     'source_exact_phrase':'For f_j^[N](x)=2 sum_(n=1)^N P_j(nx)exp(-pi n^2x^2), put',
     'source_full_line':source_pr13.read_text(encoding='utf-8-sig').splitlines()[167],
     'old_tex':pr13_old,'proposed_tex':r'\(f_j^{[N]}(x)\)',
     'reason':'Markdown parsed [N](x) as a link label N with target x. That removes the original visible [N] truncation exponent and argument (x). The source context and adjacent truncation estimate both explicitly retain [N].',
     'additional_source_confirmation':[{'line':174,'exact_phrase':'    ||f_j-f_j^[N]||_L2([1,infinity))'},
                                       {'line':185,'source_full_line':source_pr13.read_text(encoding='utf-8-sig').splitlines()[184]}],
     'original_source_changed':False}
]
for p in proposals:
    text=(ROOT/p['active_relative_path']).read_text(encoding='utf-8-sig')
    p['active_source']=file_record(ROOT/p['active_relative_path'])
    p['old_tex_occurrences_in_active_file']=text.count(p['old_tex'])
    if p['old_tex_occurrences_in_active_file']!=1: raise ValueError(p['id'])

raw={'active_relative_path':'build/source_pr_13.tex','active_line':281,
     'tex':'||f_j-f_j^[N]||_L2([1,infinity))','environment':'verbatim',
     'original_markdown_source':file_record(source_pr13),'original_line':174,
     'classification':'correctly_preserved_literal_formula','action':'none'}

pr13_caret_candidates=[]
for lineno,line in enumerate(source_pr13.read_text(encoding='utf-8-sig').splitlines(),1):
    for m in re.finditer(r'\^\[',line):
        pr13_caret_candidates.append({'original_line':lineno,'column':m.start()+1,'source_full_line':line,
                                     'classification':('confirmed_hyperlink_corruption' if lineno==168
                                                       else 'correctly_preserved_verbatim' if lineno==174
                                                       else 'correctly_preserved_literal_caret_and_brackets'),
                                     'active_line':272 if lineno==168 else 281 if lineno==174 else 299})

receipt={'created_utc':datetime.now(timezone.utc).isoformat(),
         'scope':'All href and hyperlink commands in the 239 active files from the inclusion graph, parsed with balanced braces and optional arguments; all targets retained in this receipt.',
         'included_file_count':len(graph['roots']['stage']['files']),
         'command_count':len(links),'parse_errors':errors,
         'classifications':{kind:sum(x['classification']==kind for x in links) for kind in sorted(set(x['classification'] for x in links))},
         'links':links,'confirmed_conversion_proposals':proposals,'raw_caret_bracket_classification':raw,
         'pr13_all_original_caret_bracket_occurrences':pr13_caret_candidates,
         'active_edits_performed':False,'pdf_build_performed':False}
(OUT/'LINK_AND_LOCAL_PROPOSALS.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['command_count','parse_errors','classifications']},indent=2))
print('proposals',len(proposals),'sha256',file_record(OUT/'LINK_AND_LOCAL_PROPOSALS.json')['sha256'])
