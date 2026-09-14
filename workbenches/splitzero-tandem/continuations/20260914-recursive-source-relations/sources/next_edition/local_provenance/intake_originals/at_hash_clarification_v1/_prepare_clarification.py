"""Author an additive clarification; never changes the sealed artifact or stage."""
import base64
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
WORK = HERE.parent
STAGE = WORK / 'cumulative_next_edition_staging_20260913_v19'
ARTIFACT = STAGE / 'reader/sources/next_edition/tau_arithmetic_determinant'


def pin(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def filepin(path):
    return {'path': str(path.resolve()), **pin(path.read_bytes())}


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def b64(data):
    return base64.b64encode(data).decode('ascii')


def require(value, message):
    if not value:
        raise ValueError(message)


def main():
    locators = {
        'original_source': 'originals/AT_original.tex', 'accepted_reader': 'proofs/AT.tex',
        'body_extraction': 'evidence/BODY_EXTRACTION.json', 'layout_map': 'evidence/LAYOUT.json',
        'manifest': 'MANIFEST.json',
    }
    data = {k:(ARTIFACT / v).read_bytes() for k,v in locators.items()}
    sealed = {k:{'path':locators[k], **pin(v)} for k,v in data.items()}
    require(sealed['original_source']['sha256'] == '24cf7ce5be6a43cc656641b516185df10b2e4d7824600ece657120d1c549deae', 'Final original identity')
    require(sealed['accepted_reader']['sha256'] == '9fa19a509edf91f5aa0a9cb4762485449196d0b1ff521f2445f791fa3290cc75', 'Final accepted reader identity')
    extraction, layout = (json.loads(data[k]) for k in ['body_extraction', 'layout_map'])
    prefix = b'\n\\maketitle\n\n'
    original_body = extraction['original_body'].encode('utf-8')
    require(original_body.startswith(prefix), 'Exact body title prefix')
    pre_lf = original_body[len(prefix):]
    require(b'\r' not in pre_lf, 'Original LF frame')
    lf, crlf = pre_lf, pre_lf.replace(b'\n', b'\r\n')
    frames = {'pre_layout_LF': pin(lf), 'pre_layout_CRLF': pin(crlf)}
    steps = []
    for i, change in enumerate(layout['changes'], 1):
        old, new = (change[k].encode('utf-8') for k in ['old', 'new'])
        oldc, newc = (x.replace(b'\n', b'\r\n') for x in [old, new])
        require(lf.count(old) == crlf.count(oldc) == 1, 'Exactly one occurrence at each layout step')
        a, c = lf.index(old), crlf.index(oldc)
        step = {
            'step': i, 'reason_in_sealed_layout_map': change['reason'],
            'old_LF_text': change['old'], 'new_LF_text': change['new'],
            'old_LF_base64': b64(old), 'new_LF_base64': b64(new),
            'source_span_LF': {'start': a, 'end': a + len(old)},
            'source_span_CRLF': {'start': c, 'end': c + len(oldc)},
            'before_LF': pin(lf), 'before_CRLF': pin(crlf),
        }
        lf, crlf = lf.replace(old, new), crlf.replace(oldc, newc)
        step.update(after_LF=pin(lf), after_CRLF=pin(crlf))
        steps.append(step)
    require(len(steps) == 10 and crlf == data['accepted_reader'], 'Ten changes give the complete final reader')
    frames.update(post_layout_LF=pin(lf), post_layout_CRLF=pin(crlf))
    require(frames['post_layout_LF']['sha256'] == extraction['pre_layout_reader_body_sha256'], 'Identified historical field')
    names = ['preamble', 'begin_document_boundary', 'original_body', 'end_document_boundary', 'postamble']
    parts = [extraction['preamble'].encode('utf-8'), b'\\begin{document}', original_body,
             b'\\end{document}', extraction['postamble'].encode('utf-8')]
    components = []
    cursor = 0
    for name, part in zip(names, parts):
        components.append({'name': name, 'start': cursor, 'end': cursor + len(part), **pin(part)})
        cursor += len(part)
    require(b''.join(parts) == data['original_source'], 'Complete original reconstruction')
    recipe = {
        'schema': 'AT-extraction-hash-frame-clarification-v1',
        'status': 'exact-current-source-and-reader-frames-identified',
        'title': 'Exact identification of the AT extraction hash',
        'date': '2026-09-13',
        'scope': 'Additive byte-provenance clarification for the sealed Arithmetic Determinant Transport artifact. The full accepted source and reader remain unchanged.',
        'sealed_artifact': 'Tau_Arithmetic_Determinant_Transport_2026-09-13',
        'sealed_inputs': sealed,
        'legacy_metadata': {
            'file': 'evidence/BODY_EXTRACTION.json', 'field': 'pre_layout_reader_body_sha256',
            'retained_value': extraction['pre_layout_reader_body_sha256'],
            'retained_hash_stage_note': extraction.get('hash_stage_note'),
            'exact_identification': 'The complete final post-layout reader body with every CRLF replaced by LF.',
            'identified_frame': 'post_layout_LF',
            'finding': 'The digest is an exact final-reader LF digest. The pre_layout field name and its explanatory note identify the wrong processing stage.',
            'sealed_metadata_edited': False,
        },
        'frames': frames,
        'line_endings': {
            'pre_layout_LF': {'LF': pre_lf.count(b'\n'), 'CR': pre_lf.count(b'\r')},
            'pre_layout_CRLF': {'CRLF': pre_lf.count(b'\n')},
            'post_layout_LF': {'LF': lf.count(b'\n'), 'CR': lf.count(b'\r')},
            'post_layout_CRLF': {'CRLF': crlf.count(b'\r\n')},
        },
        'byte_offset_convention': 'Zero-based byte offsets, start included and end excluded, in the explicitly named source frame.',
        'body_prefix_removed_base64': b64(prefix),
        'body_prefix_removed_text': prefix.decode(),
        'original_file_components': components,
        'original_preamble_utf8': extraction['preamble'],
        'original_postamble_utf8': extraction['postamble'],
        'retained_body_span_in_original_file': {
            'start': components[2]['start'] + len(prefix), 'end': components[2]['end'], **pin(pre_lf)},
        'layout_steps': steps,
        'forward_rule': 'Remove exactly the stated title prefix from original_body; apply the ten sealed LAYOUT changes in order. In the CRLF frame convert every LF in the body and both sides of every layout change to CRLF before replacement. Each replaced source span occurs exactly once.',
        'inverse_rule': 'From the accepted CRLF reader, reverse the ten layout changes in reverse order, converting their old/new LF payloads to CRLF. Replace each CRLF with LF, prepend exactly the recorded title prefix, and concatenate the original preamble, literal begin-document boundary, restored body, literal end-document boundary and original postamble. The result is every byte of the sealed original.',
        'full_original_reconstruction': pin(data['original_source']),
        'equation_tag_tokens_in_order': [x.decode() for x in re.findall(rb'\\tag\{([^}]+)\}', data['original_source'])],
        'proof_source_and_preamble_retained_entire': True,
        'new_mathematical_claim_or_check': False, 'new_document_build': False,
        'source_or_seal_mutation': False,
    }
    write_json(HERE / 'CLARIFICATION.json', recipe)
    spec = importlib.util.spec_from_file_location('at_byte_reconstruction_verifier', HERE / 'verify_reconstruction.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    verified = module.verify(ARTIFACT, recipe)

    table = '\n'.join('| ' + label.replace('_', ' ') + ' | ' + str(frame['bytes']) + ' | `' + frame['sha256'] + '` |'
                      for label, frame in frames.items())
    components_table = '\n'.join('| ' + c['name'].replace('_', ' ') + ' | [' + str(c['start']) + ', ' + str(c['end']) + ') | ' + str(c['bytes']) + ' | `' + c['sha256'] + '` |' for c in components)
    step_table = '\n'.join('| ' + str(s['step']) + ' | ' + str(s['source_span_LF']['start']) + '–' + str(s['source_span_LF']['end']) + ' | ' + str(s['after_LF']['bytes']) + ' | `' + s['after_LF']['sha256'] + '` |' for s in steps)
    md = f'''# Exact identification of the AT extraction hash

This additive record identifies a metadata-frame mismatch in the sealed Arithmetic Determinant Transport artifact. The complete accepted original, accepted reader, proof paragraphs, original preamble and all 23 equation tags remain unchanged.

The value `{extraction['pre_layout_reader_body_sha256']}` in `evidence/BODY_EXTRACTION.json`, under `pre_layout_reader_body_sha256`, is the exact **final post-layout reader body in LF encoding**. Its byte count is {frames['post_layout_LF']['bytes']}. The accepted reader itself has CRLF line endings and {len(crlf)} bytes. Replacing each CRLF in that accepted reader by LF gives the identified value exactly. The field name and its `hash_stage_note` therefore name the wrong processing stage. This record leaves that historical metadata untouched and identifies all four actual frames.

| Complete body frame | Bytes | SHA-256 |
|---|---:|---|
{table}

## Fixed sealed inputs

All paths in this section are relative to `Tau_Arithmetic_Determinant_Transport_2026-09-13`. Exact pins are retained in [CLARIFICATION.json](CLARIFICATION.json).

''' + '\n'.join(f"- `{v['path']}`: {v['bytes']} bytes; SHA-256 `{v['sha256']}`." for v in sealed.values()) + f'''

## Exact original-file reconstruction

Every interval below uses zero-based byte offsets, with the end excluded. Concatenating the five components in order recovers all {len(data['original_source'])} original bytes and the original SHA-256 `{sealed['original_source']['sha256']}`. The complete original preamble and postamble are also retained literally in the JSON record; the complete body remains in the pinned original source.

| Component | Original byte interval | Bytes | SHA-256 |
|---|---|---:|---|
{components_table}

The literal prefix removed from the original body is the 13-byte sequence `\\n\\\\maketitle\\n\\n` (base64 `{b64(prefix)}`). No proof prose is part of that prefix. The retained LF body occupies original bytes [{recipe['retained_body_span_in_original_file']['start']}, {recipe['retained_body_span_in_original_file']['end']}). Its exact pin is the pre-layout LF row above. Replacing every LF in that retained body by CRLF gives the pre-layout CRLF row above; no other byte is changed in this step.

## All ten forward and inverse layout transformations

The sealed `evidence/LAYOUT.json` supplies ten ordered pairs of complete strings. Nine pairs move an existing equation tag outside an inner alignment, and the tenth records the determinant-line wrap. For every step, the complete old and new payloads are included as both literal text and base64 in [CLARIFICATION.json](CLARIFICATION.json), together with exact source spans and all before/after pins in both line-ending frames. The transformations are applied in that recorded order, each to its unique exact source occurrence.

| Step | LF source span, end excluded | LF bytes after step | LF SHA-256 after step |
|---:|---|---:|---|
{step_table}

Applying all ten transformations to the {len(pre_lf)}-byte LF body gives the {len(lf)}-byte final LF body. Applying the same transformations to the CRLF body, after converting every LF in each old/new payload to CRLF, gives every byte of the accepted {len(crlf)}-byte reader. Thus the retained hash `{extraction['pre_layout_reader_body_sha256']}` has an exact identified final-body preimage.

For the inverse, start from the accepted CRLF reader and visit the ten pairs in reverse order. Replace each unique new CRLF payload by its old CRLF payload. This recovers the complete pre-layout CRLF body. Replace its CRLF sequences by LF, restore the exact 13-byte title prefix, then concatenate the original preamble, the literal `\\begin{{document}}` boundary, the restored complete body, the literal `\\end{{document}}` boundary and the original postamble. Exact byte comparison recovers the pinned original. This comparison retains all original definitions, proof prose, constants, signs, macros and equation tags because it recovers the entire source file, including its preamble.

## Reproducible byte verification

The complete standard-library verification program is [verify_reconstruction.py](verify_reconstruction.py). Given the sealed artifact directory, run:

```text
python verify_reconstruction.py --artifact-root PATH_TO_SEALED_AT_ARTIFACT
```

The program checks all five input pins, every intermediate layout pin and source span, both final line-ending frames, all ten inverse substitutions and every original-file component. It writes no source file and executes no mathematical code or document build. The accompanying local audit records successful verification against the pinned staged public artifact. This clarification adds no mathematical theorem or new mathematical execution claim.
'''
    require(len(prefix) == 13, 'Documented title-prefix length')
    (HERE / 'CLARIFICATION.md').write_text(md, encoding='utf-8')

    def texescape(value):
        return value.replace('_', r'\_').replace('&', r'\&').replace('%', r'\%').replace('#', r'\#')
    tex_rows = '\n'.join(texescape(k.replace('_', ' ')) + ' & ' + str(v['bytes']) + r' & \nolinkurl{' + v['sha256'] + r'} \\' for k,v in frames.items())
    tex = r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,array,longtable,booktabs}
\usepackage[margin=22mm]{geometry}
\usepackage{fvextra,xurl}
\usepackage[unicode,hidelinks]{hyperref}
\setlength{\emergencystretch}{3em}
\title{Exact identification of the AT extraction hash}
\author{}
\date{13 September 2026}
\begin{document}
\maketitle
This additive record identifies the processing frame of a retained metadata
hash. The entire accepted AT proof source and reader, including the original
preamble and all 23 equation tags, remain unchanged.

\section{The exact identified value}
The value in the sealed
\nolinkurl{evidence/BODY_EXTRACTION.json} field
\nolinkurl{pre_layout_reader_body_sha256} is
\nolinkurl{42b97470bfe0f67e0a0247e5cefcb95609c487b8ff20c275457aeebc02b7b706}.
It identifies the complete final \emph{post-layout} reader body in LF
encoding, with 17149 bytes. Replacing each CRLF in the 17558-byte accepted
reader by LF gives this value exactly. The retained field name and its
explanatory note name the wrong processing stage. The four exact frames are:

\begin{longtable}{@{}p{.23\linewidth}r p{.57\linewidth}@{}}
\toprule Complete body frame & Bytes & SHA-256 \\
\midrule
''' + tex_rows + r'''
\bottomrule
\end{longtable}

\section{Complete forward and inverse reconstruction}
Read the pinned original source, extraction record and ten-entry layout
record. The exact original body begins with the 13-byte sequence whose
base64 representation is \nolinkurl{ClxtYWtldGl0bGUKCg==}.
Remove exactly that title prefix; no proof prose is removed.
The remaining complete LF body has 17113 bytes. Replacing each LF by CRLF
gives its 17520-byte CRLF representation.

Apply all ten ordered old/new pairs from the sealed layout map. In the
CRLF representation, convert every LF in both sides of each pair to CRLF.
Each old payload occurs exactly once at its recorded byte span. The final
LF and CRLF results are the complete final bodies identified above.
The full payloads, source spans and before/after hashes for every step are
retained in \nolinkurl{CLARIFICATION.json}.

For the inverse, start with the accepted CRLF reader and reverse all ten
pairs in reverse order, replacing each unique new payload by the complete
old payload. This recovers the entire pre-layout CRLF body. Replace each
CRLF by LF and restore the exact removed title prefix. Then concatenate
the original preamble, the literal begin-document boundary, the restored
complete body, the literal end-document boundary and the original
postamble. The result is every byte of the pinned original source,
whose SHA-256 is
\nolinkurl{24cf7ce5be6a43cc656641b516185df10b2e4d7824600ece657120d1c549deae}.
The JSON record gives exact zero-based byte intervals and hashes for all
five original-file components, and retains the complete original preamble
and postamble literally. The source itself retains every proof paragraph.

\section{Complete byte-verification program}
The following standard-library program checks the five sealed input pins,
the exact source spans and every intermediate hash in both representations,
the ten reverse transformations and all original-file components. It
writes no source file, imports no mathematical program and performs no
document build. Invoke it with \nolinkurl{--artifact-root} naming the
sealed artifact directory. Its complete JSON recipe accompanies this file.
\VerbatimInput[fontsize=\footnotesize,breaklines=true,breakanywhere=true]{verify_reconstruction.py}
\end{document}
'''
    (HERE / 'CLARIFICATION.tex').write_text(tex, encoding='utf-8')
    public_names = ['CLARIFICATION.md', 'CLARIFICATION.tex', 'CLARIFICATION.json', 'verify_reconstruction.py']
    public_manifest = {
        'schema': 'AT-extraction-hash-clarification-public-files-v1',
        'title': 'Exact identification of the AT extraction hash',
        'scope': 'Complete additive explanation, exact transformation recipe and portable byte verifier; the sealed mathematical source remains unchanged.',
        'files': [{'path':name, **pin((HERE / name).read_bytes())} for name in public_names],
        'manifest_self_excluded': True,
        'local_only_files': ['LOCAL_FULL_INVERSE_RECEIPT.json', '_prepare_clarification.py'],
    }
    write_json(HERE / 'PUBLIC_MANIFEST.json', public_manifest)
    local = {
        'schema': 'AT-extraction-hash-local-full-inverse-receipt-v1',
        'status': verified['status'], 'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'visibility': 'local-only; contains source filesystem locators',
        'public_manifest': filepin(HERE / 'PUBLIC_MANIFEST.json'),
        'sealed_inputs': {k:filepin(ARTIFACT / v) for k,v in locators.items()},
        'fixed_source_stage_audit': filepin(WORK / 'cumulative_v19_at_aw_source_stage_audit_20260913.json'),
        'source_components_full_bytes': [{**c, 'base64':b64(part)} for c,part in zip(components, parts)],
        'full_inverse_original_base64': b64(b''.join(parts)),
        'all_ten_layout_steps': steps, 'verification_result': verified,
        'verification_program': filepin(HERE / 'verify_reconstruction.py'),
        'public_recipe': filepin(HERE / 'CLARIFICATION.json'),
        'actual_byte_verifier_executed': True, 'mathematical_code_or_build_executed': False,
        'stage_and_sealed_files_modified': False,
    }
    for label, relative in locators.items():
        require((ARTIFACT / relative).read_bytes() == data[label], 'Sealed input changed during preparation')
    local['all_five_sealed_input_pins_rechecked_unchanged'] = True
    write_json(HERE / 'LOCAL_FULL_INVERSE_RECEIPT.json', local)
    print(json.dumps({'status': local['status'], 'public_files': public_manifest['files'],
                      'public_manifest': filepin(HERE / 'PUBLIC_MANIFEST.json'),
                      'local_full_inverse_receipt': filepin(HERE / 'LOCAL_FULL_INVERSE_RECEIPT.json')}, indent=2))


if __name__ == '__main__':
    main()
