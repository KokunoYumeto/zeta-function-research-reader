from pathlib import Path
import re

base = Path(__file__).resolve().parent
path = base / 'fragments' / 'tensor_primary_update.tex'
text = path.read_text(encoding='utf-8')
text = text.replace('coefficient subring \\(A\\subset\\mathbb C\\), its already specified',
                    'coefficient subring \\(A\\subset\\mathbb C\\) containing \\(\\rho\\), its already specified')
text = text.replace('^{,k}', '^{k}')
# Preserve the original PC sum coordinate S by naming the coefficient ring explicitly.
text = text.replace('_S', r'_{\mathscr S}').replace('^S', r'^{\mathscr S}')
text = re.sub(r'(?<![A-Za-z\\])S(?![A-Za-z])', lambda _: r'\mathscr S', text)
# The replacement also visits the S inside newly written mathscr tokens.
text = text.replace(r'\mathscr \mathscr S', r'\mathscr S')
for tag in ['BPC.2', 'BTP.2']:
    end = text.index(r'\tag{' + tag + '}')
    start = text.rfind(r'\begin{split}', 0, end)
    part = text[start:end]
    if r'\end{split}' not in part:
        raise ValueError(tag)
    text = text[:start] + part.replace(r'\begin{split}', r'\begin{aligned}', 1).replace(r'\end{split}', r'\end{aligned}', 1) + text[end:]
path.write_text(text, encoding='utf-8', newline='\n')

path = base / 'fragments' / 'PC30_coefficient_insertion.tex'
text = path.read_text(encoding='utf-8').replace('^{,p}', '^{p}')
end = text.index(r'\tag{PC30a}')
start = text.rfind(r'\begin{split}', 0, end)
part = text[start:end]
text = text[:start] + part.replace(r'\begin{split}', r'\begin{aligned}', 1).replace(r'\end{split}', r'\end{aligned}', 1) + text[end:]
path.write_text(text, encoding='utf-8', newline='\n')

compile_dir = base / 'compile'
compile_dir.mkdir(exist_ok=True)
wrapper = r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=24mm]{geometry}
\usepackage{amsmath,amssymb,mathrsfs}
\usepackage{hyperref}
\begin{document}
\input{../fragments/tensor_primary_update.tex}
\input{../fragments/PC30_coefficient_insertion.tex}
\end{document}
'''
(compile_dir / 'tensor_update_review.tex').write_text(wrapper, encoding='utf-8')
print('Corrected and prepared the two complete fragments for compilation.')
