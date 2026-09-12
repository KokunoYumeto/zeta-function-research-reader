"""Read-only main candidate QA; author outputs only inside main_final_qa."""
from pathlib import Path
from datetime import datetime, timezone
import ast
import hashlib
import json
import re
import fitz
from PIL import Image, ImageDraw

QA=Path(__file__).resolve().parent
E=QA.parent
OUT=QA/'repaired'
OUT.mkdir(exist_ok=True)
C=E/'main_candidate'
ROOT=E.parents[2]
PDF=C/'main.pdf'
EXPECTED='8328222255737fa49c95d1f5aa6d30e981a072daeba68d297d8e838eb03b4676'
checks=[]
def sha(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def check(ok,label):checks.append({'label':label,'passed':bool(ok)})
def text(path):return path.read_text(encoding='utf-8')

build=read(E/'MAIN_CANDIDATE_BUILD.json')
base=read(E/'BASELINE_454.json')
check(sha(PDF)==EXPECTED==build['pdf']['sha256'],'frozen candidate PDF hash')
check(PDF.stat().st_size==3963102==build['pdf']['bytes'],'candidate PDF byte count')
check(sha(ROOT/'tex/main.pdf')==base['pdf_sha256'],'canonical PDF still old baseline')
check(sha(E/'baseline_454/main.pdf')==base['pdf_sha256'],'frozen baseline PDF identity')
check(len(base['tex_dependencies'])==57 and len(build['tex_dependencies'])==59,'57 baseline and 59 candidate snapshots')
candidate_files={p.relative_to(C).as_posix() for p in C.rglob('*.tex')}
check(candidate_files=={r['path'] for r in build['tex_dependencies']},'complete 59 TeX snapshot membership')
for row in build['tex_dependencies']:
    rel=row['path']
    check(sha(C/rel)==row['sha256'] and (C/rel).stat().st_size==row['bytes'],'candidate snapshot: '+rel)
    check((C/rel).read_bytes()==(ROOT/'tex'/rel).read_bytes(),'candidate/live source identity: '+rel)
for row in base['tex_dependencies']:
    rel=row['path']
    check(sha(E/'baseline_454'/rel)==row['sha256'],'frozen old snapshot: '+rel)
    if rel!='main.tex':check(sha(C/rel)==row['sha256'],'old nonmain TeX unchanged: '+rel)
newmain=text(C/'main.tex')
for name in ['29w_toda_source_relation_volumes','29x_gamma_convolution_descent']:
    line='\\input{satellites/'+name+'}\n'
    check(newmain.count(line)==1,'single new chapter include: '+name)
    newmain=newmain.replace(line,'')
check(newmain==text(E/'baseline_454/main.tex'),'main wrapper delta exactly two include lines')

# Compile only the reviewed pure transformation function AST. No script-level
# statements/imports/writers, filesystem actions or assertions outside it run.
def transformation(recipe):
    tree=ast.parse(text(E/recipe))
    nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='transform']
    check(len(nodes)==1,'single pure transform function: '+recipe)
    namespace={'re':re}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),recipe,'exec'),namespace)
    return namespace['transform']

tvb=read(E/'TVB_TRANSFER.json')
tvb_source=E/'original_sources/toda_cv_exact_bridge_20260912.tex'
check(sha(tvb_source)==tvb['source']['sha256'],'TVB original source pin')
tvb_body,tvb_headings=transformation('integrate_toda_reader.py')(tvb_source.read_bytes())
tvb_expected=text(E/'TVB_HEADER.tex')+tvb_body+'\n\\endgroup\n'
tvb_target=C/'satellites/29w_toda_source_relation_volumes.tex'
check(tvb_expected==text(tvb_target),'full TVB mechanical transformation exact')
check(sha(tvb_target)==tvb['target_sha256'],'TVB chapter transfer pin')
check(tvb_headings==tvb['headings'],'all ten TVB source headings preserved')
check(re.findall(r'\\tag\{(TVB\.[^}]+)\}',tvb_body)==tvb['explicit_tags'],'all 49 TVB equation tags preserved')

gamma=read(E/'GAMMA_TRANSFER.json')
gamma_source=E/'gamma_review/source_stage/NOTE.tex'
check(sha(gamma_source)==gamma['source']['sha256'],'Gamma original source pin')
gamma_body,heads,tags,refs,labels=transformation('integrate_gamma_reader.py')(gamma_source.read_bytes())
anchor='comparison keeps the complete unit in (GD.3).\n'
check(gamma_body.count(anchor)==1,'unique primitive insertion anchor')
gamma_expected=text(E/'GAMMA_HEADER.tex')+gamma_body.replace(anchor,anchor+text(E/'GAMMA_PRIMITIVE.tex'))+'\n\\endgroup\n\n'+text(E/'GAMMA_TODA_JOIN.tex')
gamma_target=C/'satellites/29x_gamma_convolution_descent.tex'
check(gamma_expected==text(gamma_target),'complete Gamma transformation plus exact primitive/join')
check(sha(gamma_target)==gamma['chapter_sha256'],'Gamma chapter transfer pin')
check((heads,tags,refs,labels)==(gamma['source_sections'],gamma['source_tags'],gamma['source_equation_references'],gamma['source_labels']),'Gamma all source headings/tags/references/labels preserved')
check(re.findall(r'\\tag\{(GJ\.[^}]+)\}',text(E/'GAMMA_TODA_JOIN.tex'))==['GJ.'+str(i) for i in range(1,9)],'all eight GJ tags')
check(re.findall(r'\\tag\{(GD\.32[^}]+)\}',text(E/'GAMMA_PRIMITIVE.tex'))==['GD.32a','GD.32b'],'literal primitive additions exactly two tags')

for run in build['runs']:
    check(run['returncode']==0 and sha(C/run['log'])==run['log_sha256'],'recorded build pass/log identity: '+str(run['pass']))
log=text(C/'main.log')
warning_patterns={
  'overfull':r'Overfull', 'missing_character':r'Missing character:',
  'undefined_reference':r'(?:Reference|Citation) .+ undefined|There were undefined references',
  'undefined_control':r'Undefined control sequence', 'missing_destination':r'(?:destination|reference).*(?:does not exist|undefined)|name\{.+\} has been referenced but does not exist',
  'duplicate_destination':r'destination with the same identifier',
  'latex_error':r'LaTeX Error|^!|Emergency stop|Fatal error occurred'}
warnings={name:re.findall(pattern,log,re.M|re.I) for name,pattern in warning_patterns.items()}
for name,hits in warnings.items():check(not hits,'log zero '+name)

doc=fitz.open(PDF)
check(len(doc)==482,'482 PDF pages')
toc=doc.get_toc(simple=False)
new_toc=[row for row in toc if 426<=row[2]<=454]
check(any('Arithmetic source and relation volumes' in row[1] and row[2]==426 for row in new_toc),'TVB outline root at page 426, body continues at 427')
check(any('Gamma convolution descent' in row[1] for row in new_toc),'Gamma outline root exists')
links=[];bad_links=[];toc_source_pages=set();uri_links=[]
new_range=set(range(426,455))
for number,page in enumerate(doc,1):
    for link in page.get_links():
        if link['kind']==fitz.LINK_GOTO or (link['kind']==fitz.LINK_NAMED and 'page' in link):
            target=link.get('page',-1)+1
            if target<1 or target>len(doc):bad_links.append({'source':number,'target':target})
            if number in new_range or target in new_range:
                item={'source':number,'target':target,'rect':list(link['from']),
                      'text':page.get_textbox(link['from']),'target_position':list(link['to']),
                      'named_destination':link.get('nameddest')}
                links.append(item)
                if number<50 and target in new_range:toc_source_pages.add(number)
        elif number in new_range:
            item={'source':number,'kind':link['kind'],'uri':link.get('uri'),'text':page.get_textbox(link['from'])}
            uri_links.append(item)
            if link['kind']!=fitz.LINK_URI or not link.get('uri','').startswith(('https://','http://')):bad_links.append(item)
check(not bad_links,'all PDF internal destinations resolve; new external links are explicit HTTP(S) URIs')
for row in new_toc:
    check(1<=row[2]<=len(doc) and row[3].get('page',-1)+1==row[2], 'outline destination resolves: '+row[1])
    # Named destinations expose PDF-space (bottom-origin) coordinates here.
    destpage=doc[row[2]-1]
    desttop=destpage.rect.height-row[3]['to'].y
    snippet=destpage.get_text(clip=fitz.Rect(60,desttop-5,destpage.rect.width-60,desttop+65))
    normalized=lambda s:''.join(c for c in s.casefold() if c.isalnum())
    check(normalized(row[1]) in normalized(snippet),'outline anchor actually lands at heading: '+row[1])
    anchor=row[3].get('nameddest')
    matching=[link for link in links if link['source'] in toc_source_pages and link['named_destination']==anchor]
    check(len(matching)==1 and matching[0]['target']==row[2] and normalized(row[1]) in normalized(matching[0]['text']),
          'visible TOC entry, anchor and outline agree: '+row[1])
new_source_uris=set(re.findall(r'\\href\{([^}]+)\}',text(tvb_target)+text(gamma_target)))
check(new_source_uris=={'https://dlmf.nist.gov/18.23.E7'},'only new external URI is the stated primary generating-function reference')
check(new_source_uris<=set(link['uri'] for link in uri_links),'all new source hyperlinks survive PDF transfer')

pages=sorted(new_range|{425,455}|toc_source_pages)
page_rows=[];margin_hits=[];page_text=[]
for number in pages:
    page=doc[number-1]
    words=page.get_text('words')
    outside=[w for w in words if w[0]<0 or w[1]<0 or w[2]>page.rect.width or w[3]>page.rect.height]
    crosses=[w for w in words if w[0]<69 or w[2]>page.rect.width-69]
    if outside or crosses:margin_hits.append({'page':number,'outside':outside,'body_margin_candidates':crosses})
    pix=page.get_pixmap(matrix=fitz.Matrix(110/72,110/72),alpha=False)
    output=OUT/f'page-{number:03d}.png'
    pix.save(output)
    page_rows.append({'physical_page':number,'width_pt':page.rect.width,'height_pt':page.rect.height,
                      'render':output.name,'render_sha256':sha(output),'word_count':len(words)})
    page_text.append('PAGE '+str(number)+'\n'+page.get_text())

# Retain initial evidence and verify that this candidate differs only at the
# repaired TOC page across the complete 33-page bounded render set.
initial=read(QA/'MACHINE_QA.json')
initial_pages={r['physical_page']:r['render_sha256'] for r in initial['page_renders']}
changed_render_pages=[r['physical_page'] for r in page_rows if r['render_sha256']!=initial_pages.get(r['physical_page'])]
check(changed_render_pages==[10],'only physical page 10 changed across all 33 reviewed page renders')
plain_heading=r'\subsection{The analytic coefficient map into the same Toda input}'
padded_heading=r'\subsection[\hspace{0.4em}The analytic coefficient map into the same Toda input]{The analytic coefficient map into the same Toda input}'
join_text=text(E/'GAMMA_TODA_JOIN.tex')
check(join_text.count(padded_heading)==1,'unique repaired GJ TOC spacing heading')
old_join=join_text.replace(padded_heading,plain_heading)
check(hashlib.sha256(old_join.encode()).hexdigest()==initial['read_input_pins']['GAMMA_TODA_JOIN.tex'],'only GJ source change is optional TOC spacing')
prior_deps={r['path']:r for r in initial['dependency_snapshot']}
for row in build['tex_dependencies']:
    if row['path']!='satellites/29x_gamma_convolution_descent.tex':
        check(row==prior_deps[row['path']],'repair preserves candidate dependency: '+row['path'])
old_chapter=text(gamma_target).replace(padded_heading,plain_heading)
check(hashlib.sha256(old_chapter.encode()).hexdigest()==prior_deps['satellites/29x_gamma_convolution_descent.tex']['sha256'],'only integrated chapter change is optional TOC spacing')
for name,pin in initial['read_input_pins'].items():
    if name not in {'GAMMA_TODA_JOIN.tex','GAMMA_TRANSFER.json','MAIN_CANDIDATE_BUILD.json'}:
        check(sha(E/name)==pin,'repair preserves input: '+name)

# Contact sheets supplement, not replace, selected native-size review.
for first in range(0,len(pages),6):
    batch=pages[first:first+6]
    sheet=Image.new('RGB',(1350,1240),'white');draw=ImageDraw.Draw(sheet)
    for i,number in enumerate(batch):
        with Image.open(OUT/f'page-{number:03d}.png') as im:
            im.thumbnail((430,580))
            x=(i%3)*450+10;y=(i//3)*620+25
            draw.text((x,y-18),'Physical PDF page '+str(number),fill='black')
            sheet.paste(im,(x,y))
    sheet.save(OUT/f'contact-{first//6+1:02d}.png')

result={'schema':'main-candidate-independent-source-and-layout-machine-qa-v1',
 'created_utc':datetime.now(timezone.utc).isoformat(), 'candidate_pdf_sha256':sha(PDF),
 'candidate_bytes':PDF.stat().st_size,'candidate_pages':len(doc),'checks':checks,
 'failures':[c['label'] for c in checks if not c['passed']], 'visual_review_complete':False,
 'read_only_scope':'No source/PDF writer or heavy mathematical replay executed; pure AST transform functions evaluated on immutable source bytes.',
 'dependency_snapshot':build['tex_dependencies'], 'baseline_snapshot':base['tex_dependencies'],
 'read_input_pins':{p:sha(E/p) for p in ['TVB_HEADER.tex','GAMMA_HEADER.tex','GAMMA_PRIMITIVE.tex','GAMMA_TODA_JOIN.tex','integrate_toda_reader.py','integrate_gamma_reader.py','TVB_TRANSFER.json','GAMMA_TRANSFER.json','MAIN_CANDIDATE_BUILD.json','BASELINE_454.json']},
 'toc_source_pages':sorted(toc_source_pages),'new_outline':new_toc,'relevant_internal_links':links,
 'new_external_links':uri_links,'bad_links':bad_links,'warnings':warnings,'page_renders':page_rows,'margin_candidates':margin_hits,
 'repair_comparison':{'initial_candidate_sha256':initial['candidate_pdf_sha256'],
                     'initial_machine_receipt_sha256':sha(QA/'MACHINE_QA.json'),
                     'compared_render_pages':pages,'changed_render_pages':changed_render_pages,
                     'comparison_scope':'All 33 bounded reviewed page renders; no all-482-page visual or pixel-identity assertion.'},
 'review_script_sha256':sha(Path(__file__))}
(OUT/'MACHINE_QA.json').write_text(json.dumps(result,indent=2,default=str)+'\n',encoding='utf-8')
(OUT/'page_text.txt').write_text('\n\n'.join(page_text),encoding='utf-8')
print(json.dumps({'failures':result['failures'],'checks':len(checks),'toc_source_pages':sorted(toc_source_pages),
 'new_outline_count':len(new_toc),'relevant_internal_links':len(links),'new_external_links':len(uri_links),
 'rendered_pages':pages,'margin_candidate_pages':[r['page'] for r in margin_hits]},indent=2))
