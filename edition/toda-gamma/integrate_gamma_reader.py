"""Mechanically retain the complete gamma proof, with declared typography only."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = HERE / 'gamma_review/source_stage/NOTE.tex'
TARGET = ROOT / 'tex/satellites/29x_gamma_convolution_descent.tex'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def transform(raw):
    source = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')
    assert source.count(r'\maketitle') == 2  # one comment, one actual title
    body = source.split(r'\begin{document}', 1)[1].split('\\maketitle\n', 1)[1].split(r'\end{document}', 1)[0]
    assert r'\begin{document}' not in body and r'\maketitle' not in body
    toc = '{\n\\setcounter{tocdepth}{3}\n\\tableofcontents\n}\n'
    assert body.count(toc) == 1
    body = body.replace(toc, '')
    # Numerical parenthesized occurrences in this source are equation references.
    main_body, bibliography = body.split(r'\section{References and exact source', 1)
    refs = re.findall(r'\((\d+)\)', main_body)
    assert all(1 <= int(n) <= 36 for n in refs)
    body = (re.sub(r'\((\d+)\)', lambda m: '(GD.' + m[1] + ')', main_body)
            + r'\section{References and exact source' + bibliography)
    tags = re.findall(r'\\tag\{(\d+)\}', body)
    assert tags == [str(n) for n in range(1, 37)]
    body = re.sub(r'\\tag\{(\d+)\}', lambda m: r'\tag{GD.' + m[1] + '}', body)
    labels = re.findall(r'\\label\{([^{}]+)\}', body)
    body = re.sub(r'\\label\{([^{}]+)\}', lambda m: r'\label{gammad-' + m[1] + '}', body)
    assert r'\ref{' not in body and r'\eqref{' not in body
    body = re.sub(r'\\subsection\{(?:\d+\.\d+\s+)?([^{}]+)\}',
                  lambda m: r'\subsubsection{' + m[1] + '}', body)
    headings = re.findall(r'\\section\{(?:\d+\.\s*)?([^{}]+)\}', body)
    assert len(headings) == 11
    body = re.sub(r'\\section\{(?:\d+\.\s*)?([^{}]+)\}',
                  lambda m: r'\subsection[\hspace{0.4em}' + m[1] + ']{' + m[1] + '}', body)
    # The seven-row numerical table is not multi-page; retain every cell.
    old = ('\\begin{longtable}[]{@{}lr@{}}', '\\end{longtable}',
           '\\endhead\n\\bottomrule\\noalign{}\n\\endlastfoot\n')
    assert all(body.count(x) == 1 for x in old)
    body = body.replace(old[0], r'\begin{center}\begin{tabular}{@{}lr@{}}')
    body = body.replace(old[1], r'\bottomrule\end{tabular}\end{center}')
    body = body.replace(old[2], '').replace(r'\noalign{}', '')
    body = body.replace('§§', r'\S\S')
    body = re.sub(r'\\texttt\{([^{}]+)\}',
                  lambda m: r'\path{' + m[1].replace(r'\_', '_') + '}', body)
    citation = r'\path{811210d24b80813a08972ca23f919db015383137},' + '\n'
    assert body.count(citation) == 1
    body = body.replace(citation, citation.rstrip('\n') + '\\par\n')
    chain_start = r'\text{original split-supported polynomial source}'
    chain_end = r'\longrightarrow\text{the same source--boundary Toda determinant ratio}.'
    assert body.count(chain_start) == body.count(chain_end) == 1
    first, rest = body.split(chain_start)
    chain, last = rest.split(chain_end)
    chain = chain.replace('\n\\longrightarrow', '\\\\\n\\longrightarrow')
    body = (first + '\\begin{gathered}\n' + chain_start + chain
            + '\\\\\n' + chain_end + '\n\\end{gathered}' + last)
    return body, headings, tags, refs, labels

receipt = json.loads((HERE / 'gamma_review/INTAKE_RECEIPT.json').read_text())
expected = next(r for r in receipt['files'] if r['path'] == 'NOTE.tex')
raw = SOURCE.read_bytes()
assert sha(raw) == expected['sha256'] and len(raw) == expected['bytes']
body, headings, tags, refs, labels = transform(raw)
header = (HERE / 'GAMMA_HEADER.tex').read_text(encoding='utf-8')
join = (HERE / 'GAMMA_TODA_JOIN.tex').read_text(encoding='utf-8')
primitive = (HERE / 'GAMMA_PRIMITIVE.tex').read_text(encoding='utf-8')
anchor = 'comparison keeps the complete unit in (GD.3).\n'
assert body.count(anchor) == 1
body = body.replace(anchor, anchor + primitive)
chapter = header + body + '\n\\endgroup\n\n' + join
if TARGET.exists():
    old_record = json.loads((HERE / 'GAMMA_TRANSFER.json').read_text())
    assert sha(TARGET.read_bytes()) == old_record['chapter_sha256'], 'Unrecorded target edits'
TARGET.write_text(chapter, encoding='utf-8', newline='\n')
record = {'status': 'complete_gamma_body_and_analytic_join_transferred',
          'source': expected, 'archive_sha256': receipt['archive']['sha256'],
          'chapter': str(TARGET), 'chapter_sha256': sha(TARGET.read_bytes()),
          'source_sections': headings, 'source_tags': tags,
          'source_equation_references': refs, 'source_labels': labels,
          'original_body_mathematics_abridged': False,
          'transforms': ['Strip standalone preamble, title, contents and end wrapper',
                         'Demote headings; remove source heading numeric prefixes',
                         'Prefix equation numbers/references GD and labels gammad-',
                         'Seven-row longtable to tabular with every cell retained',
                         'Breakable literal paths and vertical display of the same map chain',
                         'Section symbol to TeX; line endings to LF'],
          'additions': ['Separate context and explicit inherited degree domains',
                        'GD.32a--b explicit boundary and cochain primitive',
                        'GJ.1--8 analytic source map, inverse and finite metric jet proof'],
          'new_lean_execution': False}
(HERE / 'GAMMA_TRANSFER.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status': record['status'], 'tags': len(tags), 'sections': len(headings)}))
