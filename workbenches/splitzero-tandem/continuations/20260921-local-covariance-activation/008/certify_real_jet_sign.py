from pathlib import Path
import json,sympy as s
B=Path(__file__).resolve().parent
d,g,v,t,h=s.symbols('delta gamma v t h',real=True)
data=json.loads((B/'ACTUAL_REAL_JET_DERIVATION.json').read_text())
det=s.sympify(data['determinant'],locals={'delta':d,'gamma':g,'v':v})
denom=367313408*d**4*g**4*(d*d+g*g)**2
F=s.Poly(s.cancel(det*denom,extension=s.sqrt(2)),d,g,v,extension=s.sqrt(2)).as_expr()
print('F:',s.expand(F),flush=True)
rows=[]
for vv in range(0,33):
    pol=s.Poly(s.expand(F.subs({d:t/2,g:2+h,v:vv})),t,h,extension=s.sqrt(2))
    bad=[];bs=[]
    for a in range(5):
        row=[]
        for k in range(5):
            z=s.expand(sum(pol.coeff_monomial(t**j*h**k)*s.binomial(a,j)/s.binomial(4,j) for j in range(a+1)))
            row.append(z)
            if z.is_nonnegative is not True:bad.append((a,k,str(z),float(z)))
        bs.append(row)
    rows.append({'v':vv,'bad':bad,'coefficients':[[str(z) for z in row] for row in bs]})
    print(vv,'bad',bad,flush=True)
out={'F':str(F),'denominator':str(denom),'rows':rows}
(B/'ACTUAL_REAL_JET_SIGN.json').write_text(json.dumps(out,indent=2)+'\n')
