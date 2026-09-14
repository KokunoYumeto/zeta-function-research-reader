from pathlib import Path
import hashlib, json, datetime, shutil
W=Path(__file__).resolve().parent.parent
work=W/'work'
out=W/'output/Deligne_Split_Cohomology'
out.mkdir(parents=True,exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
pin=lambda p:{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
src=work/'deligne_translation_bridge_20260913.tex'
raw=src.read_bytes()
reviewed='39163624c54704c203a69481ff4d7df4262afa108ac1e0989171d5ba8d700c42'
if sha(raw.replace(b'margin=23mm',b'margin=25mm'))!=reviewed:
    raise ValueError('Final source differs from reviewed mathematical source')
build=work/'deligne_translation_build_20260913'
log=(build/'deligne_translation_bridge_20260913.log').read_text(errors='replace')
for defect in ['Overfull','Underfull','Missing character','Warning','duplicate']:
    if defect in log:raise ValueError('Unclosed final TeX finding '+defect)
files=[src,build/'deligne_translation_bridge_20260913.pdf',build/'deligne_translation_bridge_20260913.log',
       work/'deligne_sidebar_independent_review_20260913.md']
files += [build/f'sealed-page-{n}.png' for n in range(1,5)]
files += [build/f'build_{n}.{ext}' for n in [6,7] for ext in ['stdout','stderr']]
files += [build/f'render_sealed.{ext}' for ext in ['stdout','stderr']]
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'complete',
 'source':pin(src),'reviewed_mathematical_source_sha256':reviewed,
 'format_only_change':'Exactly one geometry parameter: margin=25mm became margin=23mm. Reversal reproduces the independently reviewed source hash.',
 'visual':'Root directly viewed all four final sealed-page renders at110dpi. All complete proofs readable; no clipping, empty terminal page or layout warnings.',
 'execution':'Final actual pdflatex passes6 and7 returned0; pdftoppm final render returned0. Full outputs retained. No mathematical checker was run by this sealing script.',
 'files':[pin(p) for p in files]}
(work/'deligne_translation_final_manifest_20260913.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
mapping={
 'Deligne_Split_Cohomology.pdf':work/'deligne_split_sidebar_build_20260913/deligne_split_sidebar_standalone_20260913.pdf',
 'Deligne_Split_Cohomology.tex':work/'deligne_split_sidebar_standalone_20260913.tex',
 'deligne_split_sidebar_20260913.tex':work/'deligne_split_sidebar_20260913.tex',
 'Exponential_Translation_Comparison.pdf':build/'deligne_translation_bridge_20260913.pdf',
 'Exponential_Translation_Comparison.tex':src,
 'Exponential_Period_Determinant.pdf':W/'output/pdf/Deligne_Exponential_Period_Determinant_2026-09-13.pdf',
 'deligne_exponential_determinant_extension_20260913.tex':work/'deligne_exponential_determinant_extension_20260913.tex',
 'Independent_Deligne_Review.md':work/'deligne_sidebar_independent_review_20260913.md',
 'Exponential_Intake.md':work/'deligne_exponential_intake_20260913.md'}
copied=[]
for name,p in mapping.items():
 target=out/name
 if target.exists() and target.read_bytes()!=p.read_bytes():raise ValueError('Different existing output '+name)
 shutil.copyfile(p,target);copied.append({'output':pin(target),'source':pin(p)})
readme='''# Deligne machinery in Split-Zero cohomology

Read `Deligne_Split_Cohomology.pdf` for the complete 12-page sidebar, equations DS1–69. Its full LaTeX is `Deligne_Split_Cohomology.tex` together with `deligne_split_sidebar_20260913.tex`; compile the entry with XeLaTeX from this folder.

`Exponential_Period_Determinant.pdf` gives the complete three-page exact determinant proof, XD1–26. Its editable full body is `deligne_exponential_determinant_extension_20260913.tex`.

`Exponential_Translation_Comparison.pdf` and `.tex` give the complete four-page translation, source-metric, period and Artin–Schreier comparison, DT1–13. Compile with pdfLaTeX.

The current cumulative research paper includes these proofs alongside the original source notes. Their precise claims concern the displayed cohomology families and original metric comparisons; they supply no new uniform upper bound for the remaining RH endpoint.

The separate `../Deligne_Weil_II_S20_LaTeX/typed_latex` folder contains the requested Deligne reference text exports and separately dated historical math-mode sources.
'''
(out/'README.md').write_text(readme,encoding='utf-8')
(out/'DELIVERY_MANIFEST.json').write_text(json.dumps({'utc':receipt['utc'],'copies':copied,'readme':pin(out/'README.md')},indent=2)+'\n',encoding='utf-8')
R=W/'output/split_zero_rh_tandem_2026-09-12'
with (R/'logbook/CONTINUATION_CYCLIC_20260912.md').open('a',encoding='utf-8') as f:
 f.write('\n\n## Completed Deligne mathematical outputs — '+receipt['utc']+'\n\n')
 f.write('Progress: S20 exact direct-folder export completed and inverse-parsed to all232article-page texts; both117pagePDFs compiled withglyph/layoutchecks. FullDS1–69 sidebar independently reviewed and12pagesvisuallyinspected. RootfullDS/XD/intakeproofsread. RootDT1–13 authored, fullperiodinvertibilityadded, independentparentandlocalreviewsaccepted; finalformat-only23mmmarginverifiedagainstreviewedhash, all4finalpagesrootviewed. NewXD1–26 determinantproof3pagescompiledandviewed;exactpotentialfactorproved. CompletepriorOW/CJ/RM/ERclosures nowavailable andintegratingintocumulativepaper. NoRHuniformupperestimateorLeanclaim.\n\n')
 f.write('Direct mathematical deliverable folder: '+str(out)+'. DT final manifest: '+str(work/'deligne_translation_final_manifest_20260913.json')+'. Originalreferenceexports are separate. Currentcumulativebuild/primarycitationaddendum/fullpublicationhandoff remain inprogress; frozenIandDOI22731295unchanged.\n')
print(json.dumps({'translation_manifest':pin(work/'deligne_translation_final_manifest_20260913.json'),'output_folder':str(out),'delivery_manifest':pin(out/'DELIVERY_MANIFEST.json')},indent=2))
