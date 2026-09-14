"""Collect exact reviewed continuation sources into the self-contained reader.

The frozen baseline is never edited. Rebuilding the collected TeX needs no
workspace source paths; only this provenance/assembly step uses those paths.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import ast

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parents[1] / 'work/rh_counterfactual_20260913/continuation2'
BASE = ROOT.parent / 'tau_split_zero_counterfactual_reconstruction_20260913'
AGT = ROOT.parent / 'Tau_All_Degree_Angle_Transport_2026-09-13'
TOTAL = WORK.parent / 'total_object'
HANKEL = ROOT.parent / 'Tau_Theta_Hankel_Certification_2026-09-13'
MIXED = ROOT.parent / 'Deligne_Mixed_Control_Continuation_2026-09-13'
TOTAL_SOURCES = [
 ('TO','total_object.tex'),
 ('CAU','coherent_assembly.tex'),
 ('AG','arithmetic_gluing.tex'),
 ('PAM','purity_amplification_match.tex'),
 ('AAM','arithmetic_amplification_match.tex'),
 ('DA','deligne_amplification.tex'),
 ('DII','weil_ii_amplification.tex'),
 ('HK','certified_hankel_attachment.tex'),
 ('CFA','coefficient_face_cochain_attachment.tex'),
 ('MFC','full_mixed_carrier_attachment.tex'),
 ('MAI','mixed_amplification_identity.tex'),
 ('WDB','weil_ii_dyadic_bootstrap.tex'),
 ('SPC','single_primary_boundary_control.tex'),
 ('TP','tensor_primary_boundary_control.tex'),
 ('MLT','marked_localization_tor.tex'),
 ('ACM','combined_original_metric_control.tex'),
 ('EPE','empty_packet_endpoint.tex'),
]
SOURCES = [
 ('OCQ','coherent_comparison/original_coherent_comparison.tex'),
 ('DC','coherent_review/derived_coherent_bidual.tex'),
 ('QT','quotient_transport/quotient_transport.tex'),
 ('VR','quotient_transport/review/unitary_repair_coefficient_review.tex'),
 ('BT','arithmetic_tail/boundary_tilt_full.tex'),
 ('TW','arithmetic_tail/arithmetic_tail_windows.tex'),
 ('FPK','fixed_packet_kernel/fixed_gamma_full_jet_asymptotic.tex'),
 ('LC','fixed_packet_kernel/lower_comparison/lower_comparison.tex'),
 ('HG','fixed_packet_kernel/hilbert_completion_geometry.tex'),
 ('CA','combined_arithmetic_restriction.tex'),
]

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def document_fragment(src, code):
    """Preserve complete article body, marking its source-level definitions."""
    text=src.read_text(encoding='utf-8-sig')
    if text.count(r'\begin{document}')!=1 or text.count(r'\end{document}')!=1:
        raise RuntimeError('Unexpected document boundaries: '+str(src))
    preamble, rest=text.split(r'\begin{document}',1)
    body=rest.split(r'\end{document}',1)[0]
    for control in [r'\maketitle', r'\tableofcontents']:
        body=body.replace(control,'')
    body=body.replace(r'\begin{abstract}',r'\paragraph{Original abstract.}')
    body=body.replace(r'\end{abstract}','')
    for label in re.findall(r'\\label\{([^}]+)\}',body):
        for command in ['label','ref','eqref','pageref','autoref']:
            body=body.replace('\\'+command+'{'+label+'}',
                              '\\'+command+'{'+code+':'+label+'}')
    macros=[]
    for line in preamble.splitlines():
        if line.startswith(r'\newcommand'):
            macros.append(line.replace(r'\newcommand',r'\providecommand',1))
        elif line.startswith(r'\DeclareMathOperator'):
            match=re.fullmatch(r'\\DeclareMathOperator\{(\\\w+)\}\{([^}]+)\}',line)
            if not match:raise RuntimeError('Unparsed operator: '+line)
            macros.append(r'\providecommand{'+match[1]+r'}{\operatorname{'+match[2]+'}}')
    return '\n'.join(macros)+'\n'+body

def main():
    missing = [str(WORK/p) for _,p in SOURCES if not (WORK/p).is_file()]
    missing += [str(TOTAL/p) for _,p in TOTAL_SOURCES if not (TOTAL/p).is_file()]
    if missing:
        raise RuntimeError('Required complete proof inputs are absent: '+repr(missing))
    entries=[]
    for code,rel in TOTAL_SOURCES:
        src=TOTAL/rel
        dst=ROOT/'tex/continuation'/f'{code}.tex'
        shutil.copy2(src,dst)
        entries.append({'code':code,'source':str(src),'source_sha256':digest(src),
                        'included':str(dst.relative_to(ROOT)),
                        'included_sha256':digest(dst),'transformation':'identity bytes'})
    for code,rel in SOURCES:
        src=WORK/rel
        dst=ROOT/'tex/continuation'/f'{code}.tex'
        shutil.copy2(src,dst)
        entries.append({'code':code,'source':str(src),'source_sha256':digest(src),
                        'included':str(dst.relative_to(ROOT)),
                        'included_sha256':digest(dst),'transformation':'identity bytes'})
    src=AGT/'proofs/AGT.tex'
    dst=ROOT/'tex/continuation/AGT.tex'
    shutil.copy2(src,dst)
    entries.append({'code':'AGT','source':str(src),'source_sha256':digest(src),
                    'included':str(dst.relative_to(ROOT)),
                    'included_sha256':digest(dst),'transformation':'identity bytes',
                    'attribution':'Coordinating programme; all-degree angle transport'})
    for code,rel in [('TC','proofs/TC.tex'),('WBR','support_reader/typed/WBR.tex'),
                     ('GF','support_reader/typed/GF.tex')]:
        src=HANKEL/rel
        dst=ROOT/'tex/continuation'/f'{code}.tex'
        shutil.copy2(src,dst)
        entries.append({'code':code,'source':str(src),'source_sha256':digest(src),
                        'included':str(dst.relative_to(ROOT)),
                        'included_sha256':digest(dst),'transformation':'identity bytes',
                        'attribution':'Coordinating programme; certified original theta Hankel source'})
    mixed_manifest=json.loads((MIXED/'sources/SOURCE_MANIFEST.json').read_text(encoding='utf8'))
    for row in mixed_manifest['files']:
        if digest(MIXED/row['path']) != row['sha256']:
            raise RuntimeError('Mixed source manifest mismatch: '+row['path'])
    for code, name in [('MCF','MCF.tex'),('MW','MW.tex'),('MRE','MRE.tex'),
                       ('SP','SP.tex'),('BC','BC.tex'),
                       ('MP','MARKED_PRODUCT_ORIGINAL_NOTE.tex')]:
        src=MIXED/'sources'/name
        dst=ROOT/'tex/continuation'/f'{code}.tex'
        if code in ['BC','MP']:
            dst.write_text(document_fragment(src,code),encoding='utf8')
            transform='Complete document body; remove document/title/TOC wrappers; abstract becomes paragraph; namespace only cross-reference identifiers; retain source macro meanings with providecommand.'
        else:
            shutil.copy2(src,dst)
            transform='identity bytes'
        entries.append({'code':code,'source':str(src),'source_sha256':digest(src),
                        'original_copy':f'companion_sources/mixed_control/sources/{name}',
                        'included':str(dst.relative_to(ROOT)),
                        'included_sha256':digest(dst),'transformation':transform,
                        'attribution':'Coordinating programme; complete original mixed and marked-boundary proof'})
    def ignore(path,names):
        if Path(path).name=='single_primary_finite_field':
            return [n for n in names if n=='sources' or n in ('build','__pycache__') or n.endswith(('.aux','.log','.out','.toc','.pdf','.png','.synctex.gz'))]
        return [n for n in names if n in ('build','__pycache__') or n.endswith(
            ('.aux','.log','.out','.toc','.pdf','.png','.synctex.gz'))]
    shutil.copytree(WORK,ROOT/'continuation_sources',dirs_exist_ok=True,ignore=ignore)
    shutil.copytree(TOTAL,ROOT/'total_object_sources',dirs_exist_ok=True,ignore=ignore)
    shutil.copytree(HANKEL,ROOT/'companion_sources/theta_hankel',
                    dirs_exist_ok=True,ignore=ignore)
    shutil.copytree(MIXED,ROOT/'companion_sources/mixed_control',
                    dirs_exist_ok=True,ignore=ignore)
    carrier=ROOT/'companion_sources/mixed_carriers'
    carrier.mkdir(parents=True,exist_ok=True)
    carrier_sources=[
        Path('reference-library:/Chatnotes/split_zero_projective_monads_surcomplex/split_support_absolute_arithmetic_curve_v5.tex'),
        ROOT.parent/'split_zero_rh_tandem_2026-09-12/sources/Split_Support_Adelic_Weights_2026-09-11/sources/mixed_support_ledger.tex',
        WORK.parents[1]/'mixed_support_full_carrier_morphisms_subreview_20260913.md',
        WORK.parents[1]/'split_support_actual_control_audit_20260913.md',
    ]
    carrier_records=[]
    for src in carrier_sources:
        shutil.copy2(src,carrier/src.name)
        carrier_records.append({'source':str(src),'copy':src.name,'sha256':digest(src)})
    (carrier/'SOURCE_MANIFEST.json').write_text(json.dumps(carrier_records,indent=2),encoding='utf8')
    # Read the coordinating builder's literal errata without executing it.
    tree=ast.parse((MIXED/'BUILD_READER.py').read_text(encoding='utf8'))
    errata=next(ast.literal_eval(node.value) for node in tree.body
                if isinstance(node,ast.Assign) and any(
                   isinstance(target,ast.Name) and target.id=='ERRATA' for target in node.targets))
    errata=errata.replace(r'\appendix','').replace(r'\clearpage','')
    errata=re.sub(r'\\addcontentsline\{toc\}\{section\}\{[^}]+\}','',errata)
    (ROOT/'tex/continuation/MP_ERRATA.tex').write_text(errata,encoding='utf8')
    shutil.copytree(AGT/'evidence',ROOT/'continuation_sources/AGT_evidence',
                    dirs_exist_ok=True,ignore=ignore)
    shutil.copy2(AGT/'SOURCE_GUIDE.json',ROOT/'continuation_sources/AGT_SOURCE_GUIDE.json')
    shutil.copy2(BASE/'tex/main.tex',ROOT/'provenance/BASELINE_MAIN.tex')
    original=(BASE/'tex/main.tex').read_text(encoding='utf8')
    original=original.replace('The RH counterfactual in the original',
        'The total counterfactual object in the original')
    original=original.replace('Adversarial reconstruction and complete new calculations',
        'One constructed object and its exact amplification maps')
    original=original.replace('\\mainmatter',
        '\\mainmatter\n\\input{total_object_chapters.tex}\n'
        '\\part{Complete original programme and proof inputs}\n')
    original=original.replace('Adversarial reconstruction and complete new calculations',
        'Arithmetic continuation and complete source comparisons')
    original=original.replace('This edition gives proved new restrictions',
        'This cumulative continuation gives proved new restrictions')
    original=original.replace('This cumulative continuation gives proved new restrictions on an actual hypothetical\n'
        'off-critical packet.',
        'This edition constructs the total original counterfactual object and proves\n'
        'its exact amplification, phase-boundary and arithmetic comparison maps.')
    original=original.replace('\\providecommand{\\C}{\\mathbb C}',
        '\\providecommand{\\C}{\\mathbb C}\n'
        '\\providecommand{\\R}{\\mathbb R}\n'
        '\\providecommand{\\Q}{\\mathbb Q}\n')
    original=original.replace('\\end{document}',
        '\\chapter{The certified finite moment observation on the same total object}\n'
        '\\input{continuation/HK.tex}\n'
        '\\chapter{Complete original moment and separator proofs}\n'
        '\\input{continuation/WBR.tex}\n'
        '\\input{continuation/GF.tex}\n'
        '\\input{continuation/TC.tex}\n'
        '\\chapter{The complete original marked-product source}\n'
        '\\input{continuation/MP_ERRATA.tex}\n'
        '\\begingroup\\sloppy\\emergencystretch=8em\n'
        '\\input{continuation/MP.tex}\n'
        '\\endgroup\n'
        '\\end{document}')
    original=original.replace('\\chapter{The combined restriction on the actual counterfactual}',
        '\\chapter{The preceding combined counterfactual restriction}')
    original=original.replace('\\chapter{Proof provenance and reproducibility}',
        '\\input{continuation_chapters.tex}\n\\chapter{Proof provenance and reproducibility}')
    original=original.replace('The source repository contains',
        'The original 109-page increment is retained in full above. '
        'The additional chapters contain the coherent and derived comparison, '
        'exact quotient repairs, arithmetic boundary tilt, both growing norm windows, '
        'full fixed-packet kernel asymptotics, and their original-object consequences. '
        'The new exact-byte source manifest is '
        '\\nolinkurl{provenance/CONTINUATION_INPUT_MANIFEST.json}. '
        'The complete original authored continuation sources and mathematical review '
        'receipts are retained in \\texttt{continuation\\_sources/}. '
        'AGT is an attributed coordinating-programme calculation. The nonlinear '
        'general method and original theta primitive already occur in inherited EW; '
        'AGT supplies the stated cross-pair reduction to $2q-1$ angle contributions.\n\n'
        'The source repository contains')
    (ROOT/'tex/main.tex').write_text(original,encoding='utf8')
    (ROOT/'tex/total_object_chapters.tex').write_text(r'''\chapter{The total original counterfactual object}
\input{continuation/TO.tex}
\input{continuation/CAU.tex}
\input{continuation/AG.tex}
\chapter{Every independent mixed face and its exact source maps}
\input{continuation/MFC.tex}
\input{continuation/MCF.tex}
\input{continuation/EPE.tex}
\input{continuation/CFA.tex}
\chapter{Mixed support: filtrations, extensions and the original arithmetic class}
\input{continuation/MW.tex}
\input{continuation/MRE.tex}
\input{continuation/MAI.tex}
\chapter{The marked boundary family and the signed source control}
\input{continuation/BC.tex}
\input{continuation/SP.tex}
\input{continuation/ACM.tex}
\chapter{The full primary packet at the singular boundary}
\input{continuation/SPC.tex}
\chapter{Ordered tensors, original inertia and the retained cyclic lattice}
\input{continuation/TP.tex}
\chapter{The original localization triangle and its marked derived fibre}
\input{continuation/MLT.tex}
\chapter{The exact amplification and exclusion calculation}
\input{continuation/PAM.tex}
\input{continuation/AAM.tex}
\chapter{Deligne's amplification and the earlier exclusion}
\input{continuation/DA.tex}
\input{continuation/DII.tex}
\input{continuation/WDB.tex}
''',encoding='utf8')
    chapters=r'''\chapter{The full coherent quotient and its derived kernel}
\input{continuation/OCQ.tex}
\input{continuation/DC.tex}
\chapter{Original arithmetic coefficients under repaired source maps}
\input{continuation/QT.tex}
\input{continuation/VR.tex}
\chapter{The cross-pair angle refinement in the coordinating programme}
\input{continuation/AGT.tex}
\chapter{The actual arithmetic boundary tilt and complete Gamma derivation}
\input{continuation/BT.tex}
\chapter{Uniform original arithmetic polynomial norms}
\input{continuation/TW.tex}
\chapter{Every fixed-packet jet in the original quotient volume}
\input{continuation/FPK.tex}
\input{continuation/LC.tex}
\input{continuation/HG.tex}
\chapter{The strengthened actual arithmetic restriction}
\input{continuation/CA.tex}
'''
    (ROOT/'tex/continuation_chapters.tex').write_text(chapters,encoding='utf8')
    prior=(BASE/'tex/combined_restriction.tex').read_text(encoding='utf8')
    prior=prior.replace('\\section{The exact status after these calculations}',
        '\\section{Status at the preceding proof increment}\n'
        'The later chapters in this cumulative reader sharpen the arithmetic '
        'norm, volume, and coherent comparisons. The following records the '
        'scope of the preceding bounds, all of which remain valid.\n')
    (ROOT/'tex/combined_restriction.tex').write_text(prior,encoding='utf8')
    (ROOT/'provenance/CONTINUATION_INPUT_MANIFEST.json').write_text(
        json.dumps({'entries':entries,'baseline_manifest':
            'provenance/PROOF_INPUT_MANIFEST.json','source_closed':True},indent=2),encoding='utf8')
    builder=(BASE/'scripts/build_reader.py').read_text(encoding='utf8').replace(
        'Tau_Split_Zero_Counterfactual_Reconstruction.pdf',
        'Tau_Split_Zero_Total_Counterfactual.pdf')
    (ROOT/'scripts/build_reader.py').write_text(builder,encoding='utf8')
    print(json.dumps({'new_modules':len(entries),'identity_copies':
        sum(e['source_sha256']==e['included_sha256'] for e in entries),
        'explicit_document_transformations':[e['code'] for e in entries
            if e['source_sha256']!=e['included_sha256']]},indent=2))

if __name__=='__main__':
    main()
