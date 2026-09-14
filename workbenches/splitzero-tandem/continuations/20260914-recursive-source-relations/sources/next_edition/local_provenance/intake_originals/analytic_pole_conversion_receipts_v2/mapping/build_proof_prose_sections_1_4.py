"""Exact-span mathematical typing for AP proof prose, sections 1--4 only.

No author-source writes. Line anchors and expected original substrings make
every replacement explicit; byte inversion and protected-span checks fail
closed. ``tex`` fields contain the inline mathematical payload, without the
surrounding \\( and \\) delimiters.
"""
from pathlib import Path
import hashlib
import json
import re

SOURCE = Path('F:/user/Documents/Papors/Chatnotes/Zeta-Function-Foundation/agents/zenodo_workspace_publication/integration_20260913_next/post_pr26_intake/parent_review/f1_unit_gauge/ANALYTIC_POLE_RESIDUE_TRANSPORT.md')
OUT = Path(__file__).resolve().parent
EXPECTED_SHA = '357923aead35c77f2fa98598fbc4ed8bc1f7cd6ebc04760da504a0ded765a652'
raw = SOURCE.read_bytes()
assert len(raw) == 18433 and hashlib.sha256(raw).hexdigest() == EXPECTED_SHA
source = raw.decode('utf-8')
lines = source.splitlines(keepends=True)
line_offsets = []
offset = 0
for line in lines:
    line_offsets.append(offset)
    offset += len(line.encode('utf-8'))
cutoff = raw.index(b'## 5.')
items = []
line_cursors = {}


def add(line_number, original, tex, reason='Types the original mathematical expression without changing its objects or order.'):
    line = lines[line_number - 1]
    assert not line.startswith(('    ', '#')), (line_number, line)
    cursor = line_cursors.get(line_number, 0)
    found = line.find(original, cursor)
    assert found >= 0, (line_number, original, cursor, line)
    start = line_offsets[line_number - 1] + len(line[:found].encode('utf-8'))
    end = start + len(original.encode('utf-8'))
    assert raw[start:end].decode('utf-8') == original and end <= cutoff
    items.append(dict(source_byte_start=start, source_byte_end=end,
                      original=original, tex=tex, reason=reason))
    line_cursors[line_number] = found + len(original)


def variable(line_number, original, tex=None):
    line = lines[line_number - 1]
    cursor = line_cursors.get(line_number, 0)
    match = re.search(r'(?<![A-Za-z0-9_])' + re.escape(original) + r'(?![A-Za-z0-9_])', line[cursor:])
    assert match, (line_number, original, cursor)
    line_cursors[line_number] = cursor + match.start()
    add(line_number, original, tex or original,
        'Types this occurrence of the original mathematical variable or named object.')


# Section 1. All preceding introductory prose contains no untyped math;
# UG1--19 is an unchanged result-label reference.
variable(12, 'h')
add(12, 'd>0', r'd>0')
add(13, 'g=2 xi', r'g=2\xi')
variable(13, 'nu', r'\nu')
variable(13, 'd')
add(14, 'upsilon_h=j_h(g/h)', r'\upsilon_h=j_h(g/h)')
add(14, 'gcd(h,nu)=1', r'\gcd(h,\nu)=1')
variable(14, 'h')
variable(15, 'P_nu', r'P_{\nu}')
variable(16, 'nu', r'\nu')
variable(16, 'r')
add(16, 'r=0', r'r=0')
variable(16, 'nu', r'\nu')
variable(17, 'nu', r'\nu')
variable(17, 'nu', r'\nu')
variable(19, 'Phi', r'\Phi')
add(19, "Phi'=h", r"\Phi'=h")
add(20, 'u in C*', r'u\in\mathbb{C}^{*}')
add(20, 't in C', r't\in\mathbb{C}')
add(26, '[B --D--> B ds]', r'[B\xrightarrow{D}B\,ds]')
add(26, '[B_loc --D--> B_loc ds]', r'[B_{\mathrm{loc}}\xrightarrow{D}B_{\mathrm{loc}}\,ds]')
add(26, '0,1', r'0,1')
add(27, "w D F = u (w F)'", r"w D F = u (w F)'")
variable(27, 'Phi', r'\Phi')
variable(28, 'w')
variable(28, 's')
variable(29, 'M')
variable(29, 'P_nu', r'P_{\nu}')

# Section 2.
add(35, '[F] in M', r'[F]\in M')
add(39, 'Res_w D=0', r'\operatorname{Res}_w D=0')
variable(46, 'F')
add(46, 'n>=1', r'n\geq1')
variable(46, 'p')
add(47, 'c(s-p)^(-n)', r'c(s-p)^{-n}')
add(47, 'D F', r'D F')
add(47, '-u n c(s-p)^(-n-1)', r'-u n c(s-p)^{-n-1}')
add(48, 'h-t', r'h-t')
variable(48, 'n')
add(49, 'D[F]=0', r'D[F]=0')
variable(49, 'M')
variable(49, 'F')
add(49, '[F]=0', r'[F]=0')
variable(51, 'p')
add(51, '1/(w(p)(s-p))', r'1/(w(p)(s-p))')
variable(52, 'p')
variable(52, 'P_nu', r'P_{\nu}')
add(53, 'w(p)', r'w(p)')
add(55, 'Res_w[F]=0', r'\operatorname{Res}_w[F]=0')
variable(55, 'p')
variable(55, 'P_nu', r'P_{\nu}')
add(56, 'wF', r'wF')
add(56, '(s-p)^(-1)', r'(s-p)^{-1}')
variable(57, 'H_p', r'H_p')
add(58, 'Q_p=H_p/(u w)', r'Q_p=H_p/(u w)')
add(58, 'D Q_p=F', r'D Q_p=F')
variable(58, 'Q')
variable(59, 'Q_p', r'Q_p')
variable(59, 'p')
add(60, 'Q-Q_p', r'Q-Q_p')
variable(60, 'p')
add(60, 'DQ-F', r'DQ-F')
add(62, 'D[Q]=[F]', r'D[Q]=[F]')
variable(62, 'M')
variable(73, 'h')
variable(73, 'w')
variable(75, 'h')

# Section 3.
add(79, 'H^0=0', r'H^0=0')
add(79, 'H^1', r'H^1')
variable(79, 'd')
add(80, '1,s,...,s^(d-1)', r'1,s,\ldots,s^{d-1}')
variable(80, 'n')
add(81, 'DF', r'DF')
add(81, 'n+d', r'n+d')
variable(82, 'd')
variable(83, 'H_pol', r'H_{\mathrm{pol}}')
add(85, 'H^0', r'H^0')
add(86, 'DF=0', r'DF=0')
variable(92, 'F')
add(93, 'DQ', r'DQ')
variable(93, 'Q')
variable(93, 'Q')
add(95, 'DQ', r'DQ')
variable(98, 'H_loc', r'H_{\mathrm{loc}}')
add(102, 'sum_p (Res_w F)_p r_p/w(p)', r'\sum_p (\operatorname{Res}_w F)_p r_p/w(p)')
variable(103, 'D')
variable(104, 'd')
add(105, 'w(p)!=0', r'w(p)\ne0')
add(106, 'dim H_loc=d+r', r'\dim H_{\mathrm{loc}}=d+r')
variable(107, 'd')
variable(107, 'h')

# Section 4.
add(112, 'L=u d/dt-s', r'L=u\,d/dt-s')
variable(112, 'D')
add(117, 'C* x C', r'\mathbb{C}^{*}\times\mathbb{C}')
add(118, 'A(t)', r'A(t)')
add(118, 'h-t', r'h-t')
variable(119, 'e_0', r'e_0')
add(128, 's^d', r's^d')
add(128, 'D(1)=h-t', r'D(1)=h-t')
add(129, 'A(t)', r'A(t)')
add(134, '(u,t)', r'(u,t)')
add(134, 'u!=0', r'u\ne0')
variable(134, 'A_ext', r'A_{\mathrm{ext}}')
variable(135, 'u')
add(136, '(d+r)', r'(d+r)')
add(136, 'u=0', r'u=0')
add(138, 'W=diag(w(p;u,t))', r'W=\operatorname{diag}(w(p;u,t))')
add(146, 'u d/dt', r'u\,d/dt')
add(147, 'u d/dt-P', r'u\,d/dt-P')
variable(148, 'W')
add(150, 'r_p/w(p)', r'r_p/w(p)')
add(156, '-e_0/w(p)', r'-e_0/w(p)')
add(157, 'diag(I_d,W^-1)', r'\operatorname{diag}(I_d,W^{-1})')

items.sort(key=lambda row: row['source_byte_start'])
previous_end = 0
for row in items:
    start, end = row['source_byte_start'], row['source_byte_end']
    assert previous_end <= start < end <= cutoff
    assert raw[start:end].decode('utf-8') == row['original']
    previous_end = end

# Reconstruct a private review derivative and prove literal reversal without
# newline conversion. All source outside spans remains byte-for-byte intact.
typed = bytearray()
cursor = 0
output_spans = []
for row in items:
    start, end = row['source_byte_start'], row['source_byte_end']
    typed.extend(raw[cursor:start])
    replacement = ('\\(' + row['tex'] + '\\)').encode('utf-8')
    o_start = len(typed)
    typed.extend(replacement)
    output_spans.append((o_start, len(typed), raw[start:end]))
    cursor = end
typed.extend(raw[cursor:])
restored = bytes(typed)
for start, end, original_bytes in reversed(output_spans):
    restored = restored[:start] + original_bytes + restored[end:]
assert restored == raw
assert SOURCE.read_bytes() == raw

document = {
    'source': {'path': SOURCE.as_posix(), 'bytes': len(raw), 'sha256': EXPECTED_SHA},
    'prose_math_mappings': items,
    'scope': 'Introductory prose and Sections 1–4; all headings, labels and indented CodeBlocks untouched.',
    'tex_field_format': 'Math payload only; replace the source span by \\( + tex + \\).',
    'mapping_count': len(items),
    'section_5_source_byte_start': cutoff,
    'exact_inverse_verified': True,
    'author_source_unchanged': True,
}
path = OUT / 'proof_prose_sections_1_4.json'
path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
(OUT / 'proof_prose_sections_1_4_review_derivative.md').write_bytes(typed)
print(json.dumps({'path': str(path), 'bytes': path.stat().st_size, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'count': len(items), 'exact_inverse': restored == raw}, ensure_ascii=False))
