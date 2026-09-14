"""Exact finite checks supplementing TP's full proofs; no zero is invented."""
from pathlib import Path
from itertools import product
from math import factorial, ceil
import hashlib
import json
import re
import sympy as s

base = Path(__file__).resolve().parent
records = []
for m in range(1, 6):
    for k in range(1, 7):
        if m**k > 81:
            continue
        n = m+1
        cap = k*(m-1)
        indices = list(product(range(m), repeat=k))
        index = {b:i for i,b in enumerate(indices)}
        degrees = [sum(b) for b in indices]
        js = s.MutableSparseMatrix(len(indices),len(indices),{})
        for b in indices:
            for i in range(k):
                if b[i]+1 < m:
                    d = list(b)
                    d[i] += 1
                    js[index[tuple(d)], index[b]] += 1
        invariant = [i for i,d in enumerate(degrees) if (d+k)%n == 0]
        q = s.diag(*[int(i in invariant) for i in range(len(indices))])
        d0 = (m**k + m*(-1)**k)//n
        assert len(invariant) == d0
        assert q*js*q == s.zeros(len(indices))
        assert js**(cap+1) == s.zeros(len(indices))
        assert (js**cap)[-1,0] == s.Rational(factorial(cap),factorial(m-1)**k)
        hs = [degrees.count(d) for d in range(cap+1)] + [0]
        actual_rank = 0
        for d in range(cap+1):
            cols = [i for i,deg in enumerate(degrees) if deg == d]
            rows = [i for i,deg in enumerate(degrees) if deg == d+1]
            block = js.extract(rows,cols)
            rank = block.rank()
            assert rank == min(hs[d], hs[d+1])
            if (d+k)%n == 0:
                actual_rank += rank
        kernel = sum(max(hs[d]-hs[d+1],0) for d in range(cap+1) if (d+k)%n == 0)
        assert actual_rank+kernel == d0
        qstar = None
        if invariant:
            dmin = n*ceil(k/n)-k
            qstar = (cap-dmin)//n
            assert qstar == (k*m)//n-ceil(k/n)
            power = s.eye(len(indices))
            for r in range(cap+2):
                compressed = power.extract(invariant,invariant)
                should_nonzero = r%n == 0 and r <= n*qstar
                assert (compressed != s.zeros(d0)) == should_nonzero
                power = power*js
        top = len(indices)-1
        assert int(q[top,top]) == int(k%n == 0)
        assert js[:,top] == s.zeros(len(indices),1)
        if m >= 2 and k >= 2:
            assert actual_rank > 0
        records.append({'m':m,'k':k,'rank':len(indices),'invariants':d0,
                        'outgoing_rank':actual_rank,'invariant_kernel':kernel,
                        'max_return_power_multiple':qstar})

counts = 0
for n in range(2, 15):
    for k in range(1, 31):
        residue = [1]+[0]*(n-1)
        for unused in range(k):
            residue = [sum(residue[(r-l)%n] for l in range(1,n)) for r in range(n)]
        assert residue[0] == ((n-1)**k+(n-1)*(-1)**k)//n
        assert all(v == ((n-1)**k-(-1)**k)//n for v in residue[1:])
        counts += 1

source = base/'tensor_primary_boundary_control.tex'
tags = re.findall(r'\\tag\{TP\.(\d+)\}', source.read_text(encoding='utf-8'))
assert list(map(int,tags)) == list(range(1,41))
result = {'status':'passed','exact_matrix_cases':len(records),
          'exact_character_counts':counts,'unique_TP_tags':len(tags),
          'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
          'cases':records}
(base/'tensor_primary_exact_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:value for key,value in result.items() if key != 'cases'}))
