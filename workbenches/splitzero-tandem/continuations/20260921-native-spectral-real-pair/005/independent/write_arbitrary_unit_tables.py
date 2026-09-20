"""Print every exact coefficient and short certificate in the proof source."""
from pathlib import Path
import json
import sympy as s
HERE=Path(__file__).resolve().parent
x,y,q=s.symbols('x y q');rt=s.sqrt(5)
src=json.loads((HERE/'ARBITRARY_UNIT_COEFFICIENT_DERIVATION.json').read_text(encoding='utf-8'))
cert=json.loads((HERE/'ARBITRARY_UNIT_MOD101_CERTIFICATE.json').read_text(encoding='utf-8'))
elim=json.loads((HERE/'ARBITRARY_UNIT_NONCONSTANCY_ELIMINATION.json').read_text(encoding='utf-8'))
proof=HERE/'ARBITRARY_UNIT_NONCONSTANCY.tex'
text=proof.read_text(encoding='utf-8')

def replace(start,end,body):
    global text
    a=text.index(start)+len(start);b=text.index(end,a)
    text=text[:a]+'\n'+body+'\n'+text[b:]

lines=[r'\[',r'\begin{gathered}']
for start,end in [(0,9),(10,19)]:
    lines.extend([r'\begin{array}{c|'+'r'*(end-start+1)+'}',
                  r'\text{degree}&'+'&'.join(str(j) for j in range(start,end+1))+r'\\\hline'])
    for label,key in [(r'\bar F','residual'),(r'\bar A','linear_A'),(r'\bar B','linear_B'),
                      ('a','linear_A_inverse'),('Y','phase_root'),('E','fourth_real_at_root'),('e','fourth_real_inverse')]:
        coeff=cert[key]
        lines.append(label+'&'+'&'.join(str(coeff[j] if j<len(coeff) else 0) for j in range(start,end+1))+r'\\')
    lines.append(r'\end{array}')
    if start==0:lines.append(r'\\[1ex]')
lines.extend([r'\end{gathered}',r'\tag{ANP17}',r'\]'])
replace('% BEGIN GENERATED MOD101 TABLES','% END GENERATED MOD101 TABLES','\n'.join(lines))

lines=[r'\[',r'\begin{array}{c|rrrrrr}',r'\text{degree}&0&1&2&3&4&5\\\hline']
for label,key in [(r'\bar P_*','second_phase_real_quotient'),(r'\bar J_*','second_phase_imag_quotient'),
                  ('S','second_phase_bezout_real'),('T','second_phase_bezout_imag')]:
    a=cert[key];lines.append(label+'&'+'&'.join(str(a[j] if j<len(a) else 0) for j in range(6))+r'\\')
lines.extend([r'\end{array}\tag{ANP18}',r'\]'])
replace('% BEGIN GENERATED BOUNDARY MOD101 TABLE','% END GENERATED BOUNDARY MOD101 TABLE','\n'.join(lines))

lines=[]
for n in [2,4]:
    for r in range(5):
        expr=s.sympify(src['coefficients'][str(n)][r],locals={'x':x,'q':q})
        a=[s.factor(s.expand(expr).coeff(q,j)) for j in range(4)]
        lines.extend([r'\[',r'\begin{split}',rf'h_{{{n},{r}}}(x,q)={{}}&{s.latex(a[0])}\\'])
        for j in range(1,4):
            lines.append(r'&{}+q'+('' if j==1 else rf'^{{{j}}}')+r'\left('+s.latex(a[j])+r'\right)'+(r'\\' if j<3 else ''))
        lines.extend([r'\end{split}',rf'\tag{{ANP{19+(0 if n==2 else 5)+r}}}',r'\]'])
F=s.Poly(s.sympify(elim['residual_polynomial'],locals={'x':x}),x,extension=rt)
lines.append(r'The monic residual polynomial is $\mathfrak F(x)=\sum_{r=0}^{19}f_rx^r$, with every coefficient listed below.')
for start,end in [(0,4),(5,9),(10,14),(15,19)]:
    lines.extend([r'\[',r'\begin{array}{c|l}'])
    for r in range(start,end+1):lines.append(str(r)+'&'+s.latex(s.expand(F.nth(r)))+r'\\')
    lines.extend([r'\end{array}',rf'\tag{{ANP{29+start//5}}}',r'\]'])
replace('% BEGIN GENERATED COEFFICIENT TABLE','% END GENERATED COEFFICIENT TABLE','\n'.join(lines))
proof.write_text(text,encoding='utf-8')
print('Wrote all exact proof tables.',flush=True)
