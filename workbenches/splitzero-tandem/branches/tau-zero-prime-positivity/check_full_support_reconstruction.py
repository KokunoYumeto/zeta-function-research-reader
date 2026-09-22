"""Exact finite checks accompanying FSR1--FSR36; proofs remain in the paper."""
from pathlib import Path
from itertools import product
import json
import sympy as sp

OUT = Path(__file__).resolve().parent
checks = 0

def require(value, message):
    global checks
    assert value, message
    checks += 1

def order_ideals(size, relations):
    return [mask for mask in range(1 << size)
            if all(not(mask >> j & 1) or (mask >> i & 1)
                   for i, j in relations)]

lattices = {
    'chain_4': order_ideals(3, [(0, 1), (1, 2), (0, 2)]),
    'boolean_2': order_ideals(2, []),
    'boolean_3': order_ideals(3, []),
    'fork_5': order_ideals(3, [(0, 1), (0, 2)]),
}
receipts = []
T = sp.Symbol('T')
for name, L in lattices.items():
    top = max(L)
    positive = [a for a in L if a]
    J = [a for a in positive
         if all((x | y) != a or x == a or y == a for x in L for y in L)]
    Z = sp.Matrix([[int(a & b == a) for b in positive] for a in positive])
    require(abs(Z.det()) == 1, (name, 'integral incidence inverse'))
    basis_idempotents = Z.inv()
    for i, a in enumerate(positive):
        for j, b in enumerate(positive):
            left = basis_idempotents[:, i]
            right = basis_idempotents[:, j]
            actual = sp.zeros(len(positive), 1)
            for u, lu in enumerate(positive):
                for v, lv in enumerate(positive):
                    meet = lu & lv
                    if meet:
                        actual[positive.index(meet)] += left[u] * right[v]
            expected = left if i == j else sp.zeros(len(positive), 1)
            require(actual == expected, (name, a, b, 'orthogonal projectors'))
    branch_matrix = sp.Matrix([[int(j & a == j) for a in positive] for j in J])
    require(branch_matrix.rank() == len(J), (name, 'branch rank'))
    require(len(branch_matrix.nullspace()) == len(L)-1-len(J), (name, 'kernel dimension'))
    for idx, a in enumerate(positive):
        require((branch_matrix * basis_idempotents[:, idx] == sp.zeros(len(J), 1))
                == (a not in J), (name, a, 'exact missing sectors'))
    for n in [2, 3, 4]:
        S = [(0, a) for a in L] + [(r, top) for r in range(1, n)]
        tau = (0, 0)
        e = (0, top)
        unit = (1, top)
        def add(x, y):
            return ((x[0]+y[0]) % n, x[1] | y[1])
        def mul(x, y):
            return ((x[0]*y[0]) % n, x[1] & y[1])
        for x, y in product(S, repeat=2):
            require(add(x, y) in S and mul(x, y) in S, (name, n, 'closure'))
            for j in J:
                beta = lambda z: (z[0], int(j & z[1] == j))
                bx, by = beta(x), beta(y)
                require(beta(add(x,y)) == ((bx[0]+by[0]) % n, bx[1] | by[1]), 'branch sum')
                require(beta(mul(x,y)) == ((bx[0]*by[0]) % n, bx[1] & by[1]), 'branch product')
        require(len({tuple((x[0], int(j & x[1] == j)) for j in J) for x in S})
                == len(S), (name, n, 'joint semiring injection'))
        for x, y, z in product(S, repeat=3):
            require(mul(x, add(y,z)) == add(mul(x,y),mul(x,z)), 'distributivity')
        # Exhaustively classify prime ideals in the actual finite semiring.
        primes = []
        for bits in range(1 << len(S)):
            I = {S[i] for i in range(len(S)) if bits >> i & 1}
            if tau not in I or unit in I:
                continue
            if not all(add(x,y) in I for x in I for y in I):
                continue
            if not all(mul(x,y) in I for x in I for y in S):
                continue
            if all(mul(x,y) not in I or x in I or y in I for x in S for y in S):
                primes.append(frozenset(I))
        support_primes = [frozenset((0,a) for a in L if not(j & a == j)) for j in J]
        ring_primes = list(sp.factorint(n))
        amplitude_primes = [frozenset(x for x in S if x[0] % p == 0) for p in ring_primes]
        require(set(primes) == set(support_primes+amplitude_primes), (name,n,'complete spectrum'))
        basis = [x for x in S if x != tau]
        def matrix(a):
            A = sp.zeros(len(basis))
            for col, x in enumerate(basis):
                y = mul(a,x)
                if y != tau:
                    A[basis.index(y), col] = 1
            return A
        E = matrix(e)
        require(E*E == E and E.rank() == len(L)-1, (name,n,'zero-prime projector'))
        require(sp.expand((sp.eye(len(basis))-T*E).det()) == sp.expand((1-T)**(len(L)-1)),
                (name,n,'zero determinant'))
        for a in range(n):
            A = matrix((a, top))
            amplitude = sp.zeros(n-1)
            for r in range(1,n):
                ar = a*r % n
                if ar:
                    amplitude[ar-1,r-1] = 1
            require(sp.expand((sp.eye(len(basis))-T*A).det())
                    == sp.expand((1-T)**(len(L)-1)*(sp.eye(n-1)-T*amplitude).det()),
                    (name,n,a,'full determinant factorization'))
            for k in [1,2,3,4]:
                require(sp.trace(A**k) == len(L)-2+sp.gcd(a**k-1,n),
                        (name,n,a,k,'fixed point trace'))
        receipts.append({'lattice':name,'residue_n':n,'support_elements':len(L),
                         'join_irreducibles':len(J),'hidden_rank':len(L)-1-len(J),
                         'semiring_elements':len(S),'prime_ideals':len(primes)})

# The two-channel mixed vector has vanishing branch values and a nonzero form.
J2 = sp.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
v = sp.Matrix([1,-1,0,0])
require((v.T*J2*v)[0] == -2, 'mixed negative packet value')
positive = sp.Matrix([1,1,0,0])
require((positive.T*J2*positive)[0] == 2, 'mixed positive packet value')
require(sp.expand((1-T)**3*(1-T**2))
        == 1-3*T+2*T**2+2*T**3-3*T**4+T**5, 'F3 two-channel Euler polynomial')
report = {'status':'passed','exact_checks':checks,'cases':receipts,
          'scope':'Finite examples supporting the complete symbolic proofs; no RH verification.'}
(OUT/'FULL_SUPPORT_EXACT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
