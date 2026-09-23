"""Rebuild the complete proof edition from the retained Markdown sources."""
from pathlib import Path
import json,re,shutil,subprocess

root=Path(__file__).resolve().parent
stems=['ESCAPING_FIBRE_INFINITESIMAL_DERIVATION','INFINITESIMAL_SUPPORT_POSITIVITY_DERIVATION',
 'NON_EULERIAN_LENGTH_DERIVATION','SHIFTED_WEIL_POSITIVITY_DERIVATION',
 'FULL_SUPPORT_RECONSTRUCTION_DERIVATION','WEIL_PACKET_DERIVATION',
 'WEIL_PACKET_ANALYTIC_DERIVATION','TAU_WEIL_NORM_RECONSTRUCTION',
 'HEAT_ENDPOINT_SIGN_BRIDGE','PRIME_ZERO_SIGN_DEFORMATION_DERIVATION','ES_QUARTER_HEAT_TRACE_DERIVATION','ES_SHELL_HEAT_LIFT_DERIVATION','WEIL_ES_COMPENSATION_DERIVATION','EIGHT_STATE_HEAT_COMPARISON','SUPPORTED_ZERO_PRIME_WEIL_DERIVATION','EIGHT_STATE_HOLONOMY_DERIVATION','HOLONOMY_AVERAGING_WEIL_ENDPOINT_DERIVATION']
header=r'''\usepackage{mathrsfs}
\usepackage{mathtools}
\usepackage{xurl}
\emergencystretch=3em
\setcounter{tocdepth}{1}
\newcommand{\Beta}{\mathrm{B}}
\DeclareUnicodeCharacter{00B2}{\ensuremath{^2}}
\DeclareUnicodeCharacter{00B1}{\ensuremath{\pm}}
\DeclareUnicodeCharacter{00D7}{\ensuremath{\times}}
\DeclareUnicodeCharacter{2192}{\ensuremath{\to}}
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
'''
(root/'TEX_HEADER.tex').write_text(header,encoding='utf-8')
front='''---
title: "Split-Zero: escaping fibres and separated-zeta positivity"
date: "Proofs of 22–23 September 2026"
---

This edition contains the complete seventeen derivations in the order listed below. Its finite algebra, analytic explicit formulas and exact comparison maps retain their own hypotheses. The source and reading guide follows the proofs.

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
for iteration in range(2):
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
