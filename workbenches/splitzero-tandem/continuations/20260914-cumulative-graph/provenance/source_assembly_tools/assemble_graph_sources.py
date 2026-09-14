"""Freeze complete new proof bodies and propagate their original use sites.

Run only with explicit final source hashes.  No TeX process is launched.
The predecessor article preamble and typography are preserved.  New labels
are bijectively renamed; equation tags and mathematical expressions remain
the source expressions.  A unicode-math-only Gamma presentation is restored
to its exact originating TeX expression for the predecessor math setup.
"""
from pathlib import Path
import argparse, difflib, hashlib, json, re, shutil
from datetime import datetime, timezone
from prepare_successor import BASE, STAGE, HISTORY, SUPPORT, WAVE, sha, row, save, preserve, verify_predecessor

READER=WAVE/'next_phase_graph_intake/reader_v2'
BACKPROP=WAVE/'next_phase_graph_intake/relation_tail_control/backprop'
PREFIX='GraphV2:'
LABEL=re.compile(r'\\(?:label|hypertarget)\{([^{}]+)\}')
REFERENCE=re.compile(r'(\\(?:label|ref|eqref|pageref|autoref|nameref|cref|Cref|vref|Vref|hyperlink|hypertarget)\*?\{)([^{}]+)(\})|(\\hyperref\[)([^\[\]]+)(\])')

def transport(text,mapping):
    changes=[]
    def sub(match):
        if match.group(1) is not None:
            lead,old,tail=match.group(1,2,3)
        else:
            lead,old,tail=match.group(4,5,6)
        # The optional multi-label cref syntax preserves comma-separated order.
        parts=old.split(',')
        new=','.join(mapping.get(item,item) for item in parts)
        if new!=old:
            changes.append({'offset':match.start(),'old':old,'new':new,'command':lead})
        return lead+new+tail
    result=REFERENCE.sub(sub,text)
    inverse={new:old for old,new in mapping.items()}
    def undo(match):
        if match.group(1) is not None: lead,old,tail=match.group(1,2,3)
        else: lead,old,tail=match.group(4,5,6)
        return lead+','.join(inverse.get(item,item) for item in old.split(','))+tail
    if REFERENCE.sub(undo,result)!=text:
        raise RuntimeError('Label transport is not exactly reversible.')
    return result,changes

def write_text(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding='utf-8',newline='\n')

def run(manifest_pin,backprop_pin):
    if sha(READER/'SOURCE_MANIFEST.json')!=manifest_pin:
        raise RuntimeError('Reader freeze manifest changed.')
    if sha(BACKPROP/'INSERTION_RECEIPT.json')!=backprop_pin:
        raise RuntimeError('Backward use receipt changed.')
    receipt_path=STAGE/'provenance/GRAPH_SUCCESSOR_SOURCE_ASSEMBLY.json'
    if receipt_path.exists():
        raise RuntimeError('A frozen source assembly already exists; preserve before revising.')
    manifest=json.loads((READER/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
    backprop=json.loads((BACKPROP/'INSERTION_RECEIPT.json').read_text(encoding='utf-8'))
    order=manifest['order']; items={item['key']:item for item in manifest['files']}
    if len(order)!=len(set(order)) or set(order)!=set(items):
        raise RuntimeError('Reader order and manifest membership differ.')
    if sha(READER/'tex/main.tex')!=manifest['main_sha256']:
        raise RuntimeError('Reader main differs from its pinned manifest.')
    bodies={}
    for key in order:
        item=items[key]
        original=READER/item['original']; body=READER/item['body']
        if sha(original)!=item['sha256'] or original.stat().st_size!=item['bytes']:
            raise RuntimeError('Original source changed: '+key)
        if sha(body)!=item['body_sha256']:
            raise RuntimeError('Prepared source changed: '+key)
        bodies[key]=body.read_text(encoding='utf-8')
    for item in backprop['files']:
        if sha(Path(item['replacement_path']))!=item['replacement_sha256']:
            raise RuntimeError('Backward use source changed: '+item['name'])
    for key in ['ACM','HC']:
        back=next(x for x in backprop['files'] if x['name']==key+'.tex')
        if items[key]['sha256']!=back['replacement_sha256']:
            raise RuntimeError('Reader and backward use are not synchronized: '+key)

    # Retain the complete source-only reader tree, including earlier source
    # revisions and exact original files.  Rendered/generated images/PDFs stay
    # in the independently manifested reader output, not in this source layer.
    source_root=STAGE/'sources/phase_graph_20260914/reader_snapshot'
    copied=[]
    for path in sorted(READER.rglob('*')):
        if not path.is_file() or path.suffix.lower() not in ['.tex','.py','.json','.md','.bib','.sty']:
            continue
        relative=path.relative_to(READER)
        if relative.parts[0] in ['build','page_qa','__pycache__']:
            continue
        target=source_root/relative; target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(path,target)
        if row(path)!=row(target): raise RuntimeError('New original copy differs: '+str(relative))
        copied.append({'path':target.relative_to(STAGE).as_posix(),**row(target)})
    back_root=STAGE/'sources/phase_graph_20260914/backward_use'
    for path in sorted(BACKPROP.rglob('*')):
        if path.is_file() and path.suffix.lower() in ['.tex','.json','.md','.py']:
            target=back_root/path.relative_to(BACKPROP); target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(path,target)
            if row(path)!=row(target): raise RuntimeError('Backward provenance copy differs.')
    names={}; duplicate=[]
    for key,text in bodies.items():
        for label in LABEL.findall(text):
            if label in names: duplicate.append([label,names[label],key])
            names[label]=key
    if duplicate:
        raise RuntimeError('Ambiguous reader labels require explicit source resolution: '+repr(duplicate))
    mapping={name:PREFIX+name for name in names}
    transport_rows=[]
    for key in order:
        original=bodies[key]
        text,changes=transport(original,mapping)
        gamma_old=r'\symsfup{\Gamma}'; gamma_new=r'\mathsf\Gamma'
        gamma_count=text.count(gamma_old)
        if gamma_count:
            if key!='dep07' or gamma_count!=5:
                raise RuntimeError('Unexpected unicode-math-specific Gamma source change.')
            text=text.replace(gamma_old,gamma_new)
        if '\\symsf' in text:
            raise RuntimeError('Unsupported unicode-math body command remains: '+key)
        target=STAGE/f'tex/phase_graph_v2/{key}.tex'
        write_text(target,text)
        restored=text.replace(gamma_new,gamma_old) if gamma_count else text
        if gamma_count and original.count(gamma_new):
            raise RuntimeError('Gamma inverse requires position-specific transport.')
        inverse={v:k for k,v in mapping.items()}
        restored,_=transport(restored,inverse)
        if restored!=original: raise RuntimeError('Full prepared body cannot be recovered: '+key)
        transport_rows.append({'key':key,'source':items[key]['body'],
            'source_sha256':items[key]['body_sha256'],'target':target.relative_to(STAGE).as_posix(),
            **row(target),'label_changes':changes,'gamma_original_expression_restorations':gamma_count,
            'full_inverse_replay':'identical prepared body characters and exact source file retained'})

    # The actual earlier ACM/HC use sites receive their complete current bodies.
    # Existing cohort labels keep CFStage, and references to the new proof
    # chapters use the explicit GraphV2 mapping.
    baseline_cf_names={}
    for path in (BASE/'tex/cohorts/cf').glob('*.tex'):
        for name in LABEL.findall(path.read_text(encoding='utf-8')):
            if name.startswith('CFStage:'):
                baseline_cf_names[name[len('CFStage:'):]]=name
    use_site_rows=[]
    for key,relative in [('ACM','tex/cohorts/cf/13_ACM.tex'),('HC','tex/cohorts/cf/31_HC.tex')]:
        owned=set(LABEL.findall(bodies[key]))
        cf_mapping=dict(mapping)
        cf_mapping.update(baseline_cf_names)
        cf_mapping.update({name:'CFStage:'+name for name in owned})
        revised,changes=transport(bodies[key],cf_mapping)
        old=(BASE/relative).read_text(encoding='utf-8')
        old_tags=re.findall(r'\\tag\*?\{([^{}]+)\}',old)
        new_tags=re.findall(r'\\tag\*?\{([^{}]+)\}',revised)
        if not set(old_tags)<=set(new_tags):
            raise RuntimeError('An earlier tagged statement is absent: '+key)
        preserve(relative); write_text(STAGE/relative,revised)
        use_site_rows.append({'key':key,'target':relative,'predecessor':row(BASE/relative),
            'replacement':row(STAGE/relative),'prepared_complete_source_sha256':items[key]['body_sha256'],
            'new_original_sha256':items[key]['sha256'],'retained_original_tags':old_tags,
            'label_changes':changes,'preservation':'Complete predecessor bytes retained in history.'})

    # Replace exactly R63--R66.  Enforce insertion-only preservation of every
    # predecessor line after its explicitly recorded CRLF-to-LF read transport.
    conclusion_relative='tex/research_conclusion.tex'
    conclusion=(BASE/conclusion_relative).read_text(encoding='utf-8')
    start=conclusion.index(r'\paragraph{Result R63:')
    end=conclusion.index(r'\paragraph{Result R67:',start)
    old_block=conclusion[start:end]
    replacement_file=BACKPROP/'replacement/R63_R66_COMPLETE_NEXT_WAVE.tex'
    replacement=replacement_file.read_text(encoding='utf-8')
    operations=difflib.SequenceMatcher(None,old_block.splitlines(True),replacement.splitlines(True),autojunk=False).get_opcodes()
    if any(op[0] not in ['equal','insert'] for op in operations):
        raise RuntimeError('R63--R66 transport removed or changed predecessor statements.')
    replacement,conclusion_labels=transport(replacement,mapping)
    preserve(conclusion_relative)
    write_text(STAGE/conclusion_relative,conclusion[:start]+replacement+conclusion[end:])
    use_site_rows.append({'key':'R63_R66','target':conclusion_relative,
        'predecessor':row(BASE/conclusion_relative),'replacement':row(STAGE/conclusion_relative),
        'insertions_by_line':operations,'old_start_character':start,'old_end_character':end,
        'outside_selected_range':'identical characters after CRLF-to-LF transport',
        'label_changes':conclusion_labels,'complete_original':replacement_file.name,
        'complete_original_sha256':sha(replacement_file)})

    wrapper='\\clearpage\\part{The original phase graph, mixed residual, relation rows and signed arithmetic return}\n'
    wrapper+='% Complete proof bodies, with their original source files retained and label transports recorded.\n'
    for key in order:
        wrapper+='\\clearpage\n\\begingroup\n\\input{tex/phase_graph_v2/'+key+'.tex}\n\\endgroup\n'
    write_text(STAGE/'tex/current_phase_graph_successor.tex',wrapper)
    main=(BASE/'tex/main.tex').read_text(encoding='utf-8')
    anchor='\\input{tex/research_conclusion.tex}'
    if main.count(anchor)!=1: raise RuntimeError('Cumulative conclusion input anchor is ambiguous.')
    revised_main=main.replace(anchor,'\\input{tex/current_phase_graph_successor.tex}\n'+anchor)
    preserve('tex/main.tex'); write_text(STAGE/'tex/main.tex',revised_main)
    if revised_main.replace('\\input{tex/current_phase_graph_successor.tex}\n','')!=main:
        raise RuntimeError('Main insertion changed the predecessor preamble or other inputs.')
    save(STAGE/'provenance/GRAPH_LABEL_TRANSPORT.json',{
        'mapping':mapping,'full_body_transports':transport_rows,'actual_earlier_use_sites':use_site_rows,
        'preamble':'The predecessor article preamble remains identical.'})

    # Build acceptance remains separate.  Explicit prepared-input pins describe
    # the anticipated closure; the compiler must record the actual FLS closure.
    predecessor_pins=json.loads((HISTORY/'provenance/CURRENT_COMPILED_SOURCE_PINS.json').read_text(encoding='utf-8'))
    expected=dict(predecessor_pins['files'])
    for relative in ['tex/main.tex','tex/research_conclusion.tex','tex/cohorts/cf/13_ACM.tex','tex/cohorts/cf/31_HC.tex',
                     'tex/current_phase_graph_successor.tex']+[f'tex/phase_graph_v2/{key}.tex' for key in order]:
        expected[relative]=row(STAGE/relative)
    save(STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json',{
        'status':'static_source_assembly_expectations_not_compiler_receipt','files':dict(sorted(expected.items())),
        'count':len(expected),'next_build':'python scripts/build_current_reader.py --record-source-pins',
        'preamble_unchanged':True,'tex_runs':0,'new_pdf_certified':False})
    preservation=verify_predecessor()
    result={'status':'complete_source_stage_ready_for_serial_cumulative_build',
        'created_utc':datetime.now(timezone.utc).isoformat(),
        'reader_source_manifest_sha256':manifest_pin,'backward_use_receipt_sha256':backprop_pin,
        'whole_proof_bodies':len(order),'order':order,'original_files_preserved':copied,
        'body_transports':transport_rows,'use_sites':use_site_rows,
        'baseline_files_preserved':preservation['count'],
        'baseline_files_changed_at_current_path':preservation['preserved_at_historical_path'],
        'baseline_mutations':0,'preamble_changed':False,'tex_runs':0,'new_pdf_certified':False,
        'next':'Run the cumulative builder serially, check its actual FLS closure against ASSEMBLED_SOURCE_EXPECTATIONS, inspect rendered changes.'}
    save(receipt_path,result)
    save(STAGE/'provenance/SUCCESSOR_SOURCE_ASSEMBLY_STATE.json',{k:v for k,v in result.items() if k not in ['body_transports','original_files_preserved','use_sites']})
    print(json.dumps({'status':result['status'],'bodies':len(order),'expected_compiler_inputs':len(expected),
                      'receipt_sha256':sha(receipt_path),'predecessor_files':preservation['count'],'tex_runs':0}))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--reader-manifest-sha256',required=True)
    parser.add_argument('--backprop-receipt-sha256',required=True)
    args=parser.parse_args(); run(args.reader_manifest_sha256,args.backprop_receipt_sha256)
