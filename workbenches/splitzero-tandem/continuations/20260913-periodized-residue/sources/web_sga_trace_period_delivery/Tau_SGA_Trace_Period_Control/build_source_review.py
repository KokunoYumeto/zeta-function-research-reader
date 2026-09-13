from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parent
inventory=[]
read_ranges={
'02a_SGA1_English_Master(1).tex':[[1,60],[300,350]],
'02d5_SGA4half_English_Master(1).tex':[[1,46]],
'02e_SGA5_English_Master(1).tex':[[2140,2269],[3060,3098],[3630,3678],[3850,3925],[4020,4282]],
'02j_SGA7II_English_Master(1).tex':[[1,30],[145,256]],
}
for p in sorted(Path('/mnt/data').glob('02*SGA*English_Master(1).tex')):
 data=p.read_bytes();s=data.decode('utf-8');deps=re.findall(r'\\(?:input|include)\{([^}]+)\}',s)
 inventory.append({'file':p.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'lines':len(s.splitlines()),'input_dependencies':[{'path':x,'available_relative_to_master':any((p.parent/(x+ext)).exists() for ext in ['', '.tex'])} for x in deps],'reading_ranges':read_ranges.get(p.name,[]),'scope':'Selected substantive reading' if p.name=='02e_SGA5_English_Master(1).tex' else 'Master/dependency inspection; only declared inline ranges read'})
(root/'checks'/'source-inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
rows='\n'.join('| '+r['file']+' | '+str(r['lines'])+' | '+str(len(r['input_dependencies']))+' |' for r in inventory)
text='''# Source review and attribution

## Actual intake

The uploaded materials were read directly as LaTeX. Files search returned no indexed results, but Files read successfully parsed the backing SGA 5 master and supplied line-citable excerpts. The same exact bytes were read in the container. No PDF or OCR was used.

| Supplied master | Lines | Explicit input/include dependencies |
| --- | ---: | ---: |
'''+rows+'''

`checks/source-inventory.json` records each SHA-256, byte count, declared dependency, and exact selected reading range. No master filename is treated as evidence that its external components were also received or read. In particular the 46-line SGA 4½ file points to eight component files; the SGA 7 II file is chiefly an ordered component list. This delivery does not redistribute the corpus.

## Mathematical source used

SGA 5, Exposé III, introduction and §§1.1–1.7 were read for the coefficient and Künneth scope. Section 4.1 supplies the evaluation/trace pairing; 4.7–4.8 supply the correspondence trace formula and fixed-support statement. Selected §5.2 text supplies the composition arrows. The coherent appendix §§6.1–6.8 specifies its adjunction, relative-perfection and Tor-independence requirements.

The load-bearing input is **III (6.8.5)**: residue of y times the regular-immersion class is the classical multiplication trace. The preceding conormal construction uses [H] ↦ H' dS. The supplied text explicitly says that this compatibility is not proved in the earlier cited source and points to the one-variable treatment in Raynaud. NOTE §§4–5 give a complete direct proof of our monic one-variable instance, so this qualification is not hidden.

The arbitrary-base finite-free proof in the note is elementary and is not attributed as a new SGA theorem. It gives the actual maps at the original polynomial, including collisions and derived diagonal directions. The coherent dual is a coefficient module dual, not a Hermitian metric or a declaration of Weil positivity.

## Deligne input and scope

The two predecessor deliveries were opened and their complete mathematical notes read for the source constructions. The exponential predecessor supplies the selected Weil II §§3.7.2–3.7.4 comparison, its infinity chart, and its finite-field hypotheses. We retain that reading record as predecessor evidence. This run did not reassemble and reread the whole S20 corpus or claim to independently certify all Weil II.

The explicit finite-field span remains over the shared finitely generated coefficient ring, with u invertible and residual characteristic greater than q+1. The original operator A appears in the characteristic-zero parameter connection. No Frobenius/A intertwiner is manufactured from equality of ranks, trace formalism, or the squared period determinant.

## Outside primary research

NIST DLMF §5.5(iii), in particular (5.5.7), was opened and read for the exact gamma product. The product is retained in NOTE (38)–(41).

Spencer Bloch and Hélène Esnault, *Gauß–Manin determinant connections and periods for irregular connections*, arXiv:math/9912095, was opened at its abstract. It explicitly covers irregular determinant connections and exp(f) periods. The TeX download attempt failed in this runtime. No precise theorem of that full article is claimed as independently read. The contour determinant calculation here has its own complete proof and no global novelty claim.

Primary references: https://dlmf.nist.gov/5.5.E7 and https://arxiv.org/abs/math/9912095. User-supplied SGA master: Exposé III (6.8.5).

## GitHub check

Repository KokunoYumeto/zeta-function-research-reader, main revision c05c709d707bacda335deff70fbb5b841a751d1f, was fetched along with its commit and README. It is a publication successor of 1f7e7c02343884a17df9873566e81a9083c70951. The inspected README retains the original source and threshold-four lower consequence and explicitly says that the opposing upper estimate is unproved. No remote files were written or merged, and no CI report was relabelled as a fresh Lean run.

## Formula qualifications made explicit here

The general reflection-stable condition implies 2 Re Tr A=kq, not necessarily Im Tr A=0. Exact Tr A=kq/2 is used only with the additional conjugation stability, as in the quartet.

For q=1 and the common ray order, Gamma_1 is downward on the imaginary line. The separately displayed upward rank-one calibration is obtained by Gamma_up=−Gamma_1. Both determinant phase and this orientation map are retained.

The trace form's radical is ann(chi') because its map to the dual is beta-flat composed with multiplication by chi'. The residue duality beta remains perfect. This does not infer sesquilinear Weil positivity.
'''
(root/'SOURCE_REVIEW.md').write_text(text)
print(rows)
