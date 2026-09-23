"""Supplementary exact checks; the independent review contains the general proof."""
import json
from pathlib import Path
import sympy as sp
z=sp.symbols("z")
records=[]
for Q in range(1,13):
    for K in range(5):
        M=K+(Q-1)//2
        columns=[]
        for k in range(1,K+1):
            columns.append([-(2*m+1)*sp.Integer(k)**(2*m) for m in range(1,M+1)])
        for r in range(1,(Q-1)//2+1):
            columns.append([2*sp.Integer(Q)**(2*m)*sp.bernoulli(2*m+1,sp.Rational(r,Q)) for m in range(1,M+1)])
        mat=sp.Matrix(M,M,lambda i,j:columns[j][i]) if M else sp.zeros(0,0)
        det=mat.det()
        assert det != 0,(Q,K,det)
        # Polynomial degree and symmetric-germ check on every basis.
        for k in range(1,K+1):
            W=z**k
            C=2
            numerator=sp.expand(z**K*(1-z**Q)*(W+W.subs(z,1/z)-C))
            poly=sp.Poly(numerator,z)
            assert poly.degree()<=2*K+Q
            assert sp.rem(poly,sp.Poly((z-1)**3,z)).is_zero
        for r in range(1,(Q-1)//2+1):
            W=(z**r-z**(Q-r))/(1-z**Q)
            C=sp.Rational(2*(Q-2*r),Q)
            numerator=sp.cancel(z**K*(1-z**Q)*(W+W.subs(z,1/z)-C))
            poly=sp.Poly(numerator,z)
            assert poly.degree()<=2*K+Q
            assert sp.rem(poly,sp.Poly((z-1)**3,z)).is_zero
        records.append({"Q":Q,"K":K,"M":M,"determinant":str(det)})
# Even-periodic rational identity and the independent endpoint equality.
even_records=[]
for Q in range(1,13):
    v={r:sp.Integer(min(r,Q-r)+1) for r in range(Q)}
    V=sum(v[r%Q]*z**r for r in range(1,Q+1))/(1-z**Q)
    assert sp.cancel(V+V.subs(z,1/z)+v[0])==0
    dirichlet_zero=sum(v[r%Q]*(sp.Rational(1,2)-sp.Rational(r,Q)) for r in range(1,Q+1))
    assert dirichlet_zero==-v[0]/2
    even_records.append({"Q":Q,"v_0":str(v[0]),"mean":str(sum(v.values())/Q),"Dirichlet_at_0":str(dirichlet_zero)})
receipt={"status":"passed","certificate_matrices":len(records),"even_periodic_checks":len(even_records),
"scope":"Exact rational Bernoulli moment matrices of the full defect basis; original HCB coefficients retain their specified nonzero pi, factorial and B factors in the proof.",
"matrices":records,"even":even_records}
out=Path(__file__).with_suffix(".json")
out.write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps({"status":"passed","certificate_matrices":len(records),"even_periodic_checks":len(even_records),"receipt":str(out)}))

