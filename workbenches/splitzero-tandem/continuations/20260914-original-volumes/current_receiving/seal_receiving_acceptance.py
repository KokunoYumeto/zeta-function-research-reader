from pathlib import Path
import hashlib,json,re
here=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt=json.loads((here/'FULL_RECEIVING_RECEIPT.json').read_text(encoding='utf-8'))
body_names=['BASELINE_RECEIVING_BODY.tex','LOW_REFINEMENT_RECEIVING_BODY.tex',
            'QUANTITATIVE_RECEIVING_BODY.tex','MIXED_ROW_RECEIVING_BODY.tex',
            'INTRINSIC_RECEIVING_BODY.tex']
checks={}
for name in ['CURRENT_JOINT_SCHUR_NOTE','SIGNED_RETURN_RECEIVER']:
    log=(here/'qa_compile'/f'{name}.log').read_text(encoding='utf-8',errors='replace')
    forbidden=['There were undefined references','multiply defined','Missing character:','LaTeX Error:']
    assert not any(x in log for x in forbidden),(name,[x for x in forbidden if x in log])
    assert 'Output written' in log
    checks[name]={'input_compile_passed':True,'undefined_reference_or_character_errors':False,
                  'pdf_is_internal_input_check_only':True,'visual_delivery_owned_by':'principal cut22 reader'}
result={
    'scope':'Root complete proof reads and actual receiving-site acceptance, exact source pins, and source-input verification.',
    'root_acceptance':'Root explicitly accepted complete BRI1–9, LRI1–4, QRI1–9, MRI1–5, IRI1–5 and every nonduplicated actual after-span in messages on 2026-09-14. No mathematical repair was identified.',
    'independent_receiving_review':'QRI1–8 fully independently accepted; review records that exact pre-QRI9 body pin. QRI9 is direct sign transport of independently accepted QGQ9, fully read and accepted by root.',
    'receiver_pins':[{k:r[k] for k in ['file','successor_sha256','bytes','exact_predecessor_byte_roundtrip']} for r in receipt['receivers']],
    'receiving_body_pins':[{'path':'spans/'+n,'sha256':sha(here/'spans'/n)} for n in body_names],
    'full_reversible_receipt_sha256':sha(here/'FULL_RECEIVING_RECEIPT.json'),
    'canonical_manifest_sha256':sha(here/'CANONICAL_PROVIDER_MANIFEST.json'),
    'transitive_manifest_sha256':sha(here/'TRANSITIVE_PROVIDER_MANIFEST.json'),
    'compile_checks':checks,
    'canonical_source_constraint':'Original input orders s=1,k only, original packet unchanged, all intrinsic polynomial components and kernels retained. Independent K=q+1 remains exploratory outside these receivers.',
    'publication':'No publication performed by this bounded integration task.'}
(here/'ROOT_RECEIVING_ACCEPTANCE.json').write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'acceptance_sha256':sha(here/'ROOT_RECEIVING_ACCEPTANCE.json'),'body_pins':result['receiving_body_pins']},indent=2))
