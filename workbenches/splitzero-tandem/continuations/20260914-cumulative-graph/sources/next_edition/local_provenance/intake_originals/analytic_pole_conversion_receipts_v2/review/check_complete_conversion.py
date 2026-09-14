"""Independent whole-source transport audit; writes this review's evidence only."""
from pathlib import Path
import copy, hashlib, json, re, subprocess

ROOT=Path(__file__).resolve().parent.parent
OUT=Path(__file__).resolve().parent
FORMAT='markdown+tex_math_dollars+tex_math_single_backslash-inline_notes-footnotes-superscript-subscript'
SOURCES={
 'analytic_pole':('357923aead35c77f2fa98598fbc4ed8bc1f7cd6ebc04760da504a0ded765a652','analytic_pole_full_math_mapping.json'),
 'analytic_pole_review':('5dc90ea5d545b674faf02d5f05ccdbd32efdeb03c6b27df793fbedaf32f91d0a','analytic_pole_review_full_math_mapping.json'),
}
WORDING={
 'analytic_pole':[
  ('The cumulative-reader owner supplied the exact weighted-residue sequence and','The accompanying derivation supplied the exact weighted-residue sequence and'),
  ("The cumulative-reader owner supplied AP3's local-primitive construction and","The accompanying derivation supplied AP3's local-primitive construction and"),
  ('in coordinated messages. Root supplied this full','in the preceding calculation. This note supplies the full'),
  ('root incorporated','the text incorporates'),
  ("and fixed the review's","and includes the review's corrected"),
  ('No remote publication of this new\nnote, new Lean execution, or certified arithmetic-zero computation is claimed.','No new Lean execution or certified arithmetic-zero computation is claimed.'),
 ],
 'analytic_pole_review':[('the root proof','the source proof')],
}
def sha(raw):return hashlib.sha256(raw).hexdigest()
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def nodes(x,path=()):
 if isinstance(x,dict):
  if 't' in x:yield path,x
  for k,v in x.items():yield from nodes(v,path+(k,))
 elif isinstance(x,list):
  for i,v in enumerate(x):yield from nodes(v,path+(i,))
def lits(tree):return [copy.deepcopy(n) for _,n in nodes(tree) if n['t'] in ('Math','Code','CodeBlock','RawInline','RawBlock')]
def inverse(original,changed,edits):
 restored=copy.deepcopy(changed)
 for e in reversed(edits):
  cur=restored
  for k in e['parts'][:-1]:cur=cur[k]
  last=e['parts'][-1];assert cur[last]==e['after'];cur[last]=copy.deepcopy(e['before'])
 assert restored==original
audits=[]
for key,(source_sha,mapping_name) in SOURCES.items():
 receipt_path=ROOT/'receipts'/f'{key}.json';receipt=load(receipt_path)
 mapping_path=ROOT/'mapping'/mapping_name;mapping=load(mapping_path)
 for field in ('original_source','raw_snapshot','public_source','adapter','wrapper'):
  assert pin(receipt[field]['path'])==receipt[field]
 original=Path(receipt['original_source']['path']).read_bytes()
 public=Path(receipt['public_source']['path']).read_bytes()
 assert sha(original)==source_sha==mapping['source']['sha256']
 assert original==Path(receipt['raw_snapshot']['path']).read_bytes()
 assert len(original)==mapping['source']['bytes']
 inline={r['code_index']:r for r in mapping.get('math_code_mappings',[])}
 retained={r['code_index']:r for r in mapping.get('retained_code',[])}
 blocks={r['codeblock_index']:r for r in mapping.get('display_codeblock_mappings',[])}
 prose={(r['source_byte_start'],r['source_byte_end']):r for r in mapping['prose_math_mappings']}
 assert len(prose)==len(mapping['prose_math_mappings'])==(228 if key=='analytic_pole' else 117)
 for component in mapping['component_maps']:assert pin(component['path'])==component
 component_prose=[r for c in mapping['component_maps'] for r in load(c['path']).get('prose_math_mappings',[])]
 assert sorted(component_prose,key=lambda r:r['source_byte_start'])==mapping['prose_math_mappings']
 spans=list(re.finditer(rb'`([^`\r\n]+)`',original))
 assert set(inline).isdisjoint(retained) and set(inline)|set(retained)==set(range(len(spans)))
 for i,span in enumerate(spans):
  row=inline.get(i,retained.get(i))
  assert row['original']==span.group(1).decode('utf-8')
  assert (row['source_byte_start'],row['source_byte_end'])==(span.start(),span.end())
 expected_counts=(28,0,0) if key=='analytic_pole' else (0,46,3)
 assert (len(blocks),len(inline),len(retained))==expected_counts
 edits=receipt['publication_and_typing_byte_edits'];rebuilt=bytearray();last=0;wording=[];seen_inline=[];seen_blocks=[];seen_prose=[]
 for e in edits:
  start,end=e['source_start_byte'],e['source_end_byte']
  assert start>=last and original[start:end]==e['before'].encode('utf-8')
  rebuilt.extend(original[last:start]);assert len(rebuilt)==e['public_start_byte']
  rebuilt.extend(e['after'].encode('utf-8'));assert len(rebuilt)==e['public_end_byte'];last=end
  if e['kind']=='mathematical_code_to_typed_math':
   i=e['code_index'];row=inline[i]
   assert e['before']=='`'+row['original']+'`' and e['after']==r'\('+row['tex']+r'\)'
   seen_inline.append(i)
  elif e['kind']=='mathematical_codeblock_to_typed_display':
   i=e['codeblock_index'];row=blocks[i]
   assert (start,end)==(row['source_byte_start'],row['source_byte_end'])
   assert e['before']==row['original_source_span'] and e['after']==row['replacement_markdown']
   assert e['typed_math_payload']==row['tex']
   seen_blocks.append(i)
  elif e['kind']=='mathematical_prose_to_typed_math':
   row=prose[(start,end)]
   assert e['before']==row['original'] and e['after']==r'\('+row['tex']+r'\)'
   seen_prose.append((start,end))
  else:
   assert e['kind']=='public_source_reference';wording.append((e['before'],e['after']))
 rebuilt.extend(original[last:]);assert bytes(rebuilt)==public
 assert sorted(seen_inline)==sorted(inline) and sorted(seen_blocks)==sorted(blocks)
 assert sorted(seen_prose)==sorted(prose)
 assert sorted(wording)==sorted(WORDING[key])
 restored=public
 for e in reversed(edits):
  start,end=e['public_start_byte'],e['public_end_byte']
  assert restored[start:end]==e['after'].encode('utf-8')
  restored=restored[:start]+e['before'].encode('utf-8')+restored[end:]
 assert restored==original
 def parse(path,suffix):
  tree=json.loads(subprocess.check_output(['pandoc',str(path),'--from='+FORMAT,'--to=json']))
  (OUT/f'{key}_independent_{suffix}_AST.json').write_text(json.dumps(tree,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
  return tree
 rawtree=parse(receipt['original_source']['path'],'raw');publictree=parse(receipt['public_source']['path'],'public')
 assert rawtree==load(receipt['raw_original_ast']['path']) and publictree==load(receipt['public_original_ast']['path'])
 original_literals=lits(rawtree);ci=bi=0;expected_events=[]
 for node in original_literals:
  if node['t']=='Code':
   if ci in inline:
    row=inline[ci];expected_events.append((row['source_byte_start'],{'t':'Math','c':[{'t':'InlineMath'},row['tex']]}))
   else:
    row=retained[ci];expected_events.append((row['source_byte_start'],node))
   ci+=1
  elif node['t']=='CodeBlock':
   row=blocks[bi]
   assert node==row['original_node'] and node['c']==[row['original_attrs'],row['original']]
   expected_events.append((row['source_byte_start'],{'t':'Math','c':[{'t':'DisplayMath'},row['tex']]}));bi+=1
  else:raise AssertionError('Unexpected original Math/raw node; must preserve and map explicitly')
 for (start,end),row in prose.items():
  assert original[start:end]==row['original'].encode('utf-8')
  expected_events.append((start,{'t':'Math','c':[{'t':'InlineMath'},row['tex']]}))
 expected=[node for _,node in sorted(expected_events,key=lambda pair:pair[0])]
 assert expected==lits(publictree)
 assert len(rawtree['blocks'])==len(publictree['blocks'])
 assert [n['c'] for _,n in nodes(rawtree) if n['t']=='Header']==[n['c'] for _,n in nodes(publictree) if n['t']=='Header']
 row=receipt['adapter_row'];adapter_path=ROOT/row['conversion_receipt'];adapter=load(adapter_path)
 assert sha(adapter_path.read_bytes())==row['conversion_receipt_sha256']
 art=adapter['artifacts'];adapter_original=load(ROOT/art['original_ast']);prepared=load(ROOT/art['prepared_ast']);writer=load(ROOT/art['writer_ast'])
 assert adapter_original==publictree
 inverse(adapter_original,prepared,adapter['prepared_edits']);inverse(prepared,writer,adapter['writer_edits'])
 math=[n['c'] for _,n in nodes(publictree) if n['t']=='Math'];emissions=adapter['literal_emission_spans']
 texpath=ROOT/art['converted'];tex=texpath.read_bytes();assert sha(tex)==row['converted_sha256']
 assert len(math)==len(emissions)
 last=-1
 for i,(payload,span) in enumerate(zip(math,emissions)):
  assert span['index']==i and span['node_type']=='Math' and span['original_c']==payload
  start,end=span['payload_start_byte'],span['payload_end_byte']
  assert span['fragment_start_byte']>=last
  assert tex[start:end]==payload[1].encode('utf-8') and sha(tex[start:end])==span['payload_sha256']
  assert tex[span['fragment_start_byte']:start]==span['opening'].encode('utf-8')
  assert tex[end:span['fragment_end_byte']]==span['closing'].encode('utf-8')
  last=span['fragment_end_byte']
 assert '\\input{'+art['converted']+'}' in Path(receipt['wrapper']['path']).read_text(encoding='utf-8')
 reread=json.loads(subprocess.check_output(['pandoc',str(texpath),'--from=latex','--to=json']))
 assert reread==load(ROOT/art['roundtrip_ast'])
 parsed_math=[n['c'] for _,n in nodes(reread) if n['t']=='Math'];assert len(parsed_math)==len(math)
 differences=[]
 for i,(source,parsed) in enumerate(zip(math,parsed_math)):
  assert source[0]==parsed[0]
  if source!=parsed:
   assert source[0]['t']=='DisplayMath' and source[1]=='\n'+parsed[1]+'\n'
   differences.append({'ordered_math_index_zero_based':i,'source_c':source,'rereader_c':parsed,'exact_byte_relation':'source = 0x0A || rereader || 0x0A','source_literal_emission_span':emissions[i]})
 assert len(differences)==(28 if key=='analytic_pole' else 0)
 assert bool(not differences)==row['latex_roundtrip_ordered_math_c_equal']
 audits.append({'key':key,'status':'accepted','original_source':receipt['original_source'],'public_source':receipt['public_source'],'mapping':pin(mapping_path),'component_maps':mapping['component_maps'],'source_typing_receipt':pin(receipt_path),'adapter_receipt':pin(adapter_path),'converted_tex':pin(texpath),'wrapper':receipt['wrapper'],'typed_display_blocks':len(blocks),'typed_inline_code':len(inline),'typed_prose_math':len(prose),'retained_nonmathematical_code':len(retained),'all_original_headings_and_block_counts_retained':True,'entire_source_and_prose_byte_forward_and_inverse_exact':True,'independently_reparsed_original_and_public_ASTs_equal_saved_trees':True,'complete_ordered_literal_transport_exact':True,'entire_prepared_and_writer_AST_inverses_exact':True,'all_emitted_math_payloads_and_delimiters_exact':True,'public_wording_edits':wording,'rereader_exact_differences':differences,'original_source_unchanged':Path(receipt['original_source']['path']).read_bytes()==original})

layout_path=ROOT/'layout/PROVENANCE_WRAP.json';layout=load(layout_path)
for field in ('original_tex','reader_tex','original_wrapper','reader_wrapper'):
 record=layout[field];actual=pin(ROOT/record['path'])
 assert actual['bytes']==record['bytes'] and actual['sha256']==record['sha256']
base=(ROOT/layout['original_tex']['path']).read_bytes();reader=(ROOT/layout['reader_tex']['path']).read_bytes()
assert len(layout['edits'])==4
rebuilt=bytearray();last=0
for e in layout['edits']:
 start,end=e['original_start_byte'],e['original_end_byte']
 assert start>=last and base[start:end]==e['before'].encode('utf-8')
 assert e['before'].replace(r'\_','_')==e['visible_token']
 assert e['after']==r'\nolinkurl{'+e['visible_token']+'}'
 rebuilt.extend(base[last:start]);assert len(rebuilt)==e['reader_start_byte']
 rebuilt.extend(e['after'].encode('utf-8'));assert len(rebuilt)==e['reader_end_byte'];last=end
rebuilt.extend(base[last:]);assert bytes(rebuilt)==reader
restored=reader
for e in reversed(layout['edits']):
 start,end=e['reader_start_byte'],e['reader_end_byte']
 assert restored[start:end]==e['after'].encode('utf-8')
 restored=restored[:start]+e['before'].encode('utf-8')+restored[end:]
assert restored==base
base_adapter=load(audits[0]['adapter_receipt']['path'])
assert len(layout['math_payload_byte_transport'])==len(base_adapter['literal_emission_spans'])==256
for span,transport in zip(base_adapter['literal_emission_spans'],layout['math_payload_byte_transport']):
 assert span['index']==transport['index']
 assert (span['payload_start_byte'],span['payload_end_byte'])==(transport['original_start_byte'],transport['original_end_byte'])
 payload=span['original_c'][1].encode('utf-8')
 assert base[transport['original_start_byte']:transport['original_end_byte']]==payload
 assert reader[transport['reader_start_byte']:transport['reader_end_byte']]==payload
 assert sha(payload)==transport['payload_sha256'] and len(payload)==transport['bytes']
base_wrapper=(ROOT/layout['original_wrapper']['path']).read_bytes();reader_wrapper=(ROOT/layout['reader_wrapper']['path']).read_bytes()
before=layout['wrapper_path_edit']['before'].encode('utf-8');after=layout['wrapper_path_edit']['after'].encode('utf-8')
assert base_wrapper.count(before)==reader_wrapper.count(after)==1
assert base_wrapper.replace(before,after)==reader_wrapper and reader_wrapper.replace(after,before)==base_wrapper
assert after==layout['reader_tex']['path'].encode('utf-8')
layout_evidence={'receipt':pin(layout_path),'original_tex':pin(ROOT/layout['original_tex']['path']),'reader_tex':pin(ROOT/layout['reader_tex']['path']),'original_wrapper':pin(ROOT/layout['original_wrapper']['path']),'reader_wrapper':pin(ROOT/layout['reader_wrapper']['path']),'four_filename_hash_wrappings_preserve_all_visible_characters':True,'entire_TeX_byte_forward_and_inverse_exact':True,'all_256_math_payload_transport_spans_exact':True,'complete_wrapper_path_only_forward_and_inverse_exact':True,'actual_reader_wrapper_input_points_to_reader_derivative':True}
cross_review_path=ROOT/'mapping/proof_prose_cross_review.json';cross_review=load(cross_review_path)
assert pin(cross_review_path)['sha256']=='317b03b05d7d666a46424c7021a2f8ff58a8ae238877f016b969e1f8af08ba28'
result={'schema':'analytic-pole-complete-source-typing-and-transport-review-v2','status':'accepted','authorship_scope':'This reviewer authored the earlier explicit 28-block display dictionary and the current 117-review-prose map. The conversion owner independently accepted both. This reviewer independently read all 228 main-proof prose spans and the owner\'s 46-inline dictionary against the complete original sources, and audited all complete source/public, adapter and reader-layout transformations. The additional main-proof prose cross-review is pinned. This receipt is a source-typing audit, not a new mathematical proof seal.','scope':'Complete source typing including ordinary prose, byte and AST transport, literal emission, exact LaTeX re-reader clarification and four nonmathematical provenance wraps. No source fixture, arithmetic-zero computation, Lean run, PDF build or visual acceptance.','sources':audits,'total_typed_display_math':28,'total_typed_inline_code_math':46,'total_typed_prose_math':345,'total_inline_math':391,'total_math_spans_verified':419,'source_mathematics_removed':False,'reader_layout':layout_evidence,'main_prose_cross_review':pin(cross_review_path),'review_script':pin(Path(__file__))}
target=OUT/'REVIEW.json';target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'review':pin(target),'status':'accepted','display_blocks':28,'inline_formulas':391,'math_spans':419,'reader_layout_math_spans':256}))
