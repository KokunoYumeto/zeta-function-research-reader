"""Rebuild the complete proof edition from the retained Markdown sources."""
from pathlib import Path
import json,re,shutil,subprocess,sys
sys.stdout.reconfigure(encoding='utf-8')

root=Path(__file__).resolve().parent
stems=['ESCAPING_FIBRE_INFINITESIMAL_DERIVATION','INFINITESIMAL_SUPPORT_POSITIVITY_DERIVATION',
 'NON_EULERIAN_LENGTH_DERIVATION','SHIFTED_WEIL_POSITIVITY_DERIVATION',
 'FULL_SUPPORT_RECONSTRUCTION_DERIVATION','WEIL_PACKET_DERIVATION',
 'WEIL_PACKET_ANALYTIC_DERIVATION','TAU_WEIL_NORM_RECONSTRUCTION',
 'HEAT_ENDPOINT_SIGN_BRIDGE','PRIME_ZERO_SIGN_DEFORMATION_DERIVATION','ES_QUARTER_HEAT_TRACE_DERIVATION','ES_SHELL_HEAT_LIFT_DERIVATION','WEIL_ES_COMPENSATION_DERIVATION','EIGHT_STATE_HEAT_COMPARISON','SUPPORTED_ZERO_PRIME_WEIL_DERIVATION','EIGHT_STATE_HOLONOMY_DERIVATION','HOLONOMY_AVERAGING_WEIL_ENDPOINT_DERIVATION','PRIME_HOLONOMY_SUPPORTED_WEIL_DERIVATION','CLASS_FIELD_SIGNED_HOLONOMY_DERIVATION','SUPPORTED_ZERO_HEAT_IDENTITY_DERIVATION','COLLISION_RESIDUE_DUALITY_DERIVATION','NILRADICAL_COTANGENT_EXTENSION_CLASS_DERIVATION','DISTINGUISHED_COLLISION_PRISM_DERIVATION','SUPPORTED_PRISM_SPECTRUM_DERIVATION','ACTUAL_HEAT_ZERO_DISTRIBUTION_VARIATION','HEAT_CAUCHY_ARITHMETIC_DERIVATION','HEAT_MIXED_PRIME_RECURRENCE','CAUCHY_WEIL_POSITIVITY_CRITERION','CAUCHY_REFLECTION_INDEX_DERIVATION','FINITE_JET_COMPLEMENT_AND_HEAT_TRUNCATION','PRIME_PROJECTOR_MOBIUS_DERIVATION','PRIMITIVE_SHORT_SUPPORT_DERIVATION','UNIVERSAL_PRIMITIVE_TRANSLATION_CRITERION','PRIMITIVE_PRIME_WINDOW_DERIVATION','GLOBAL_PRIMITIVE_CONTACT_VARIATION','CAUSAL_HEAT_ARITHMETIC_DISTRIBUTION','REAL_TIME_HEAT_TRACE_DERIVATION','FIRST_PRIME_FULL_WEIL_COERCIVITY','FIRST_PRIME_WINDOW_BOUND','PRIME_TWO_HEAT_TAIL_DERIVATION','FINITE_PRIME_WINDOW_EXTENSION','FINITE_PRIME_WINDOW_COEFFICIENT_CERTIFICATE','FAITHFUL_THETA_COMPLETION_RETURN','FAITHFUL_UNCOMPLETED_ZETA_HEAT','ORIGINAL_ZETA_COMPACT_WEIL_RECONSTRUCTION','ORIGINAL_ZETA_HEAT_CONTACT_RECONSTRUCTION','ORIGINAL_ZETA_CAUCHY_RECONSTRUCTION','ORIGINAL_ZETA_GAUSSIAN_TRANSLATION_RECONSTRUCTION','ORIGINAL_ZETA_REGULAR_HEAT_REMAP','SECTORIAL_ENDPOINT_ZERO_TRACE_RETURN','SECTORIAL_FILTER_TRACE_DERIVATION','GAUSSIAN_ARITHMETIC_BOUNDARY_RETURN','ENDPOINT_RESONANT_ZERO_DETECTION','ENDPOINT_PAIR_TRANSPORT_AND_WEIL_MATRIX']
header=r'''\usepackage{mathrsfs}
\newcommand{\Log}{\operatorname{Log}}
\usepackage{mathtools}
\usepackage{xurl}
\emergencystretch=3em
\setcounter{tocdepth}{1}
\newcommand{\Beta}{\mathrm{B}}
\DeclareUnicodeCharacter{00B2}{\ensuremath{^2}}
\DeclareUnicodeCharacter{00B1}{\ensuremath{\pm}}
\DeclareUnicodeCharacter{00D7}{\ensuremath{\times}}
\DeclareUnicodeCharacter{2192}{\ensuremath{\to}}
\DeclareUnicodeCharacter{21D2}{\ensuremath{\Rightarrow}}
\DeclareUnicodeCharacter{21A6}{\ensuremath{\mapsto}}
\DeclareUnicodeCharacter{2208}{\ensuremath{\in}}
\DeclareUnicodeCharacter{2209}{\ensuremath{\notin}}
\DeclareUnicodeCharacter{2212}{\ensuremath{-}}
\DeclareUnicodeCharacter{2227}{\ensuremath{\wedge}}
\DeclareUnicodeCharacter{2228}{\ensuremath{\vee}}
\DeclareUnicodeCharacter{2260}{\ensuremath{\ne}}
\DeclareUnicodeCharacter{2264}{\ensuremath{\le}}
\DeclareUnicodeCharacter{2265}{\ensuremath{\ge}}
\DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
\DeclareUnicodeCharacter{00B3}{\ensuremath{^3}}
\DeclareUnicodeCharacter{2074}{\ensuremath{^4}}
\DeclareUnicodeCharacter{2076}{\ensuremath{^6}}
\DeclareUnicodeCharacter{03BB}{\ensuremath{\lambda}}
\DeclareUnicodeCharacter{03BC}{\ensuremath{\mu}}
\DeclareUnicodeCharacter{03B5}{\ensuremath{\epsilon}}
\DeclareUnicodeCharacter{03C4}{\ensuremath{\tau}}
\DeclareUnicodeCharacter{03A6}{\ensuremath{\Phi}}
\DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}
\DeclareUnicodeCharacter{03C3}{\ensuremath{\sigma}}
\DeclareUnicodeCharacter{03B4}{\ensuremath{\delta}}
\DeclareUnicodeCharacter{03C0}{\ensuremath{\pi}}
\DeclareUnicodeCharacter{039B}{\ensuremath{\Lambda}}
\DeclareUnicodeCharacter{2202}{\ensuremath{\partial}}
\DeclareUnicodeCharacter{0393}{\ensuremath{\Gamma}}
\DeclareUnicodeCharacter{2205}{\ensuremath{\varnothing}}
\DeclareUnicodeCharacter{221E}{\ensuremath{\infty}}
\DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
\DeclareUnicodeCharacter{00B9}{\ensuremath{^1}}
\DeclareUnicodeCharacter{00B0}{\ensuremath{{}^\circ}}
\DeclareUnicodeCharacter{211D}{\ensuremath{\mathbb{R}}}
'''
(root/'TEX_HEADER.tex').write_text(header,encoding='utf-8')
front='''---
title: "Split-Zero: escaping fibres and separated-zeta positivity"
date: "Proofs of 22–23 September 2026"
---

This edition contains the complete 54 derivations in the order listed below. Its finite algebra, analytic explicit formulas and exact comparison maps retain their own hypotheses. The source and reading guide follows the proofs. The original-zeta reconstruction chapters retain the full meromorphic function, its signed divisor, every Gamma and endpoint factor, and all lattice support. Earlier auxiliary calculations must be read through those exact maps. The raw full-divisor pairing is not assigned the positivity of the compensated Weil receiver.

'''
book=front
for stem in stems:book+='\n\\clearpage\n\n'+(root/(stem+'.md')).read_text(encoding='utf-8')
book+='\n\\clearpage\n\n'+(root/'SOURCES.md').read_text(encoding='utf-8')
(root/'TAU_ZERO_PRIME_POSITIVITY.md').write_text(book,encoding='utf-8')
pandoc=shutil.which('pandoc');latex=shutil.which('pdflatex')
if not pandoc or not latex:raise SystemExit('Pandoc and pdflatex are required.')
for stem in stems+['TAU_ZERO_PRIME_POSITIVITY']:
    cmd=[pandoc,stem+'.md','--from=markdown+tex_math_single_backslash','--standalone','--toc',
         '-V','geometry:margin=22mm','-V','fontsize=10pt','-V','papersize=a4',
         '--include-in-header=TEX_HEADER.tex','-o',stem+'.tex']
    subprocess.run(cmd,cwd=root,check=True,capture_output=True)
    p=root/(stem+'.tex');text=p.read_text(encoding='utf-8')
    # Allow long source filenames and exact hashes to wrap without changing characters.
    def wrap_code(m):
        v=re.sub(r'([/:.\-])',r'\1\\allowbreak{}',m[1]).replace(r'\_',r'\_\allowbreak{}')
        v=re.sub(r'(?<![a-fA-F0-9])[a-fA-F0-9]{40,}(?![a-fA-F0-9])',lambda h:r'\allowbreak{}'.join(h[0][i:i+8] for i in range(0,len(h[0]),8)),v)
        return r'\texttt{'+v+'}'
    text=re.sub(r'\\texttt\{([^{}]*)\}',wrap_code,text)
    p.write_text(text,encoding='utf-8')
for iteration in range(3):
    run=subprocess.run([latex,'-interaction=nonstopmode','-halt-on-error','-file-line-error','TAU_ZERO_PRIME_POSITIVITY.tex'],cwd=root,capture_output=True,text=True,encoding='utf-8',errors='replace')
    if run.returncode:
        print(run.stdout[-5500:]);raise SystemExit(run.returncode)
log=(root/'TAU_ZERO_PRIME_POSITIVITY.log').read_text(encoding='utf-8',errors='replace')
overfull=re.findall(r'Overfull[^\n]*(?:\n[^\n]*)?',log)
report={'status':'compiled','overfull_boxes':overfull,'missing_characters':re.findall(r'Missing character[^\n]*',log),
 'undefined_references':re.findall(r'LaTeX Warning: (?:Reference|There were undefined)[^\n]*',log),'proof_files':len(stems),
 'pdf':'TAU_ZERO_PRIME_POSITIVITY.pdf','scope':'Typesetting checks; mathematical proofs and separate symbolic checks accompany this edition.'}
(root/'BUILD_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
