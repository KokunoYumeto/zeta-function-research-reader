"""Exact RF.18--RF.26 fixtures, independently including full polynomial matrices.

Usage: python [-O] this_file.py EXPECTED_OPTIMIZATION OUTPUT_JSON
No historical file is written.  Every check uses explicit control flow.
"""
from pathlib import Path
import hashlib
import json
import sys

W = Path(__file__).resolve().parent
sys.path.insert(0, str(W / 'kernel_layer_replay_dependencies_20260912'))
import sympy as sp
if sp.__version__ != '1.14.0':
    raise RuntimeError('SymPy 1.14.0 required')
if len(sys.argv) != 3:
    raise RuntimeError('Provide expected optimization flag and a new output path')
expected_mode = int(sys.argv[1])
target = Path(sys.argv[2]).resolve()
if target.parent != W or target.exists():
    raise RuntimeError('Result must be a new file directly in work/')
source = W / 'endpoint_reflected_relation_fibre_product_20260913.tex'
source_pin = '0847a516e883e7814c414f4c1bc26abfc2dd4f8493b0aac384b109888c5dc749'
historical = {
    'endpoint_reflected_relation_complete_review_20260913.md': 'a8dfad53905dfb7742b403401a7d0850e776c071478dbbab2a8485a674c512cd',
    'endpoint_reflection_independent_typing_review_20260913.md': '2af9df8b95cfd8cd5bd69f158eb7f4e16a489ae97092f3b52dc326aa77405dfd',
    'endpoint_reflected_relation_fixtures_20260913.py': '3e174144a5661ae608090c8568c529b5f562e086fceef72935532b5d82351ee1',
    'endpoint_reflected_relation_fixtures_20260913.json': 'd9b06e8c0b878cc62f3fc93fcee77eafc1178d480303f652e8efc4b5d35bbab7',
}
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

checks = []
def check(case, name, condition):
    result = bool(condition)
    checks.append({'fixture': case, 'name': name, 'passed': result})
    if not result:
        raise RuntimeError(case + ': ' + name)

check('runtime', 'actual optimization mode', sys.flags.optimize == expected_mode)
check('runtime', 'actual __debug__ mode', __debug__ == (expected_mode == 0))
check('provenance', 'current source pin before fixtures', sha(source) == source_pin)
for name, pin in historical.items():
    check('provenance', 'historical preserved before: ' + name, sha(W / name) == pin)

S = sp.Symbol('S')
I = sp.I
def poly(f):
    return sp.Poly(f, S, extension=I)
def deg(f):
    return int(poly(f).degree())
def rem(f, m):
    return sp.rem(poly(f), poly(m)).as_expr().expand()
def bar(f):
    return sum(sp.conjugate(c) * S**j[0] for j, c in poly(f).terms()).expand()
def star(f):
    return bar(f).subs(S, 2 - S).expand()
def dag(f):
    return ((-1)**deg(f) * star(f)).expand()
def equal(a, b):
    if isinstance(a, sp.MatrixBase) or isinstance(b, sp.MatrixBase):
        return a.shape == b.shape and all(sp.expand(x-y) == 0 for x, y in zip(a, b))
    return sp.expand(a-b) == 0
def vec(f, m):
    p = poly(rem(f, m))
    return sp.Matrix([p.nth(j) for j in range(deg(m))])
def mult(f, m):
    return sp.Matrix.hstack(*(vec(f*S**j, m) for j in range(deg(m))))
def conjugate_matrix(m):
    return m.applyfunc(sp.conjugate)
def expanded_matrix(m):
    return m.applyfunc(sp.expand)
def textpoly(f):
    return str(sp.expand(f))

A = S-(2+I)
B = S-I
C = S-(3+2*I)
D = S-(-1+2*I)
fixtures = [
    ('mixed', A**2*B, [(2+I,2,1), (I,1,2)], 3),
    ('disjoint', A**2, [(2+I,2,0), (I,0,2)], None),
    ('stable_pair', A**2*B**2, [(2+I,2,2), (I,2,2)], 2),
    ('stable_fixed_root', (S-(1+3*I))**3, [(1+3*I,3,3)], 2),
    ('mixed_with_persistent_double_root', A**2*B*C**2,
     [(2+I,2,1), (I,1,2), (3+2*I,2,0), (-1+2*I,0,2)], None),
]
rows = []
for name, chi, rootdata, nilindex in fixtures:
    chi = sp.expand(chi)
    q = deg(chi)
    dagger = dag(chi)
    N = sp.expand(chi*dagger)
    chi2 = sp.expand(chi**2)
    check(name, 'all reflected root multiplicities', equal(dagger, sp.prod((S-lam)**b for lam,a,b in rootdata)))
    check(name, 'monic reflected involution including phase', equal(dag(dagger), chi) and equal(star(chi), (-1)**q*dagger))
    CF = sp.Matrix.hstack(*(vec((2-S)**j, dagger) for j in range(q)))
    CG = sp.Matrix.hstack(*(vec((2-S)**j, chi) for j in range(q)))
    check(name, 'G F and F G are identity on full coefficient spaces', equal(CG*conjugate_matrix(CF), sp.eye(q)) and equal(CF*conjugate_matrix(CG), sp.eye(q)))
    check(name, 'full reflected original S operator law', equal(CF*conjugate_matrix(mult(S,chi)), (2*sp.eye(q)-mult(S,dagger))*CF))
    p = (1+2*I)*S**2+(3-I)*S+2*I
    check(name, 'full nonreal polynomial scalar operator law', equal(CF*conjugate_matrix(mult(p,chi)), mult(star(p),dagger)*CF))
    f = S**(q+1)+(2+3*I)*S+1-I
    h = (1-I)*S**2+2*S+3*I
    j = (2+I)*S+3
    check(name, 'F formula for nonreal polynomial coefficients', equal(CF*conjugate_matrix(vec(f,chi)), vec(star(f),dagger)))
    check(name, 'G formula for nonreal polynomial coefficients', equal(CG*conjugate_matrix(vec(h,dagger)), vec(star(h),chi)))
    check(name, 'nonreal scalar conjugation with alpha 2+3i', equal(CF*conjugate_matrix(vec((2+3*I)*f,chi)), (2-3*I)*CF*conjugate_matrix(vec(f,chi))))
    check(name, 'F representative independence under literal chi injection', equal(rem(chi*(star(f+chi*h)-star(f)),N), 0))
    check(name, 'G representative independence under literal chi injection', equal(rem(chi*(star(h+dagger*j)-star(h)),chi2), 0))
    injN = sp.Matrix.hstack(*(vec(chi*S**r,N) for r in range(q)))
    inj2 = sp.Matrix.hstack(*(vec(chi*S**r,chi2) for r in range(q)))
    check(name, 'both literal kernel parametrizations injective', injN.rank() == q and inj2.rank() == q)
    check(name, 'annihilator generators on entire kernels', equal(mult(dagger,N)*injN,sp.zeros(2*q,q)) and equal(mult(chi,chi2)*inj2,sp.zeros(2*q,q)))
    check(name, 'original A_chi action on norm kernel iff dagger stable', equal(mult(chi,N)*injN,sp.zeros(2*q,q)) == equal(chi,dagger))
    diamond = lambda x,y: rem(chi*x*y,dagger)
    check(name, 'transported diamond equals literal ideal product', equal(rem(chi*diamond(f,h),N),rem((chi*f)*(chi*h),N)))
    check(name, 'diamond representative independence', equal(diamond(f+dagger*j,h+dagger*f),diamond(f,h)))
    check(name, 'diamond associativity with all chi factors', equal(diamond(diamond(f,h),j),diamond(f,diamond(h,j))))
    check(name, 'diamond commutativity', equal(diamond(f,h),diamond(h,f)))
    # Matrix rank in the full 2q-dimensional quotient independently evaluates
    # every tested ideal dimension, rather than applying the root-order formula.
    multiplication = mult(chi,N)
    power = sp.eye(2*q)
    powers = []
    bounds = [int(sp.ceiling(sp.Rational(a+b,a))) for lam,a,b in rootdata if a>0]
    stabilization = max(bounds)
    for t in range(1,max(q+2,stabilization+1)+1):
        power = expanded_matrix(multiplication*power)
        rank = int(power.rank())
        formula = sum(max(b-(t-1)*a,0) for lam,a,b in rootdata)
        check(name, 'full multiplication matrix power rank t='+str(t), rank == formula)
        check(name, 'matrix power equals literal chi power t='+str(t), equal(power,mult(chi**t,N)))
        powers.append({'t':t,'actual_matrix_rank':rank,'root_formula':formula})
    persistent_dimension = sum(b for lam,a,b in rootdata if a==0)
    check(name, 'computed stable dimension', powers[-1]['actual_matrix_rank'] == persistent_dimension)
    if nilindex is not None:
        theoretical = max(int(sp.ceiling(sp.Rational(a+b,a))) for lam,a,b in rootdata if b>0)
        check(name, 'exact first zero ideal and nilpotence threshold', theoretical == nilindex and powers[nilindex-1]['actual_matrix_rank'] == 0 and powers[nilindex-2]['actual_matrix_rank'] > 0)
    else:
        check(name, 'persistent reflected-only root prevents nilpotence', persistent_dimension > 0 and all(row['actual_matrix_rank'] > 0 for row in powers))
    row = {'fixture':name,'q':q,'chi':textpoly(chi),'dagger':textpoly(dagger),'N':textpoly(N),
           'root_orders':[{'root':str(lam),'a':a,'b':b} for lam,a,b in rootdata],
           'powers':powers,'nilpotence_index':nilindex,'persistent_dimension':persistent_dimension,
           'stabilization_bound':stabilization,
           'F_coefficient_matrix':[[str(v) for v in line] for line in CF.tolist()],
           'G_coefficient_matrix':[[str(v) for v in line] for line in CG.tolist()]}
    if persistent_dimension:
        E = sp.expand(sp.prod((S-lam)**b for lam,a,b in rootdata if a==0))
        M, remainder = sp.div(N,E,S)
        M = sp.expand(M)
        check(name, 'persistent polynomial divisor with every root order', equal(remainder,0) and deg(E) == persistent_dimension)
        U,V,one = sp.gcdex(M,E,S)
        check(name, 'persistent exact Bezout identity', equal(U*M+V*E,1))
        e = rem(U*M,N)
        check(name, 'persistent idempotent original supported-zero amplitude', equal(rem(e*e-e,N),0) and equal(rem(e,E),1) and equal(rem(e,M),0) and equal(rem(e,chi),0) and not equal(e,0))
        embedding = sp.Matrix.hstack(*(vec(e*S**r,N) for r in range(deg(E))))
        reduction = sp.Matrix.hstack(*(vec(S**r,E) for r in range(deg(N))))
        check(name, 'full persistent CRT algebra injection and inverse', embedding.rank() == deg(E) and equal(reduction*embedding,sp.eye(deg(E))))
        check(name, 'persistent unit ideal has retained length', mult(e,N).rank() == deg(E))
        check(name, 'persistent algebra product under exact idempotent injection', equal(rem((e*f)*(e*h)-e*rem(f*h,E),N),0))
        for t in range(1,max(q+2,stabilization+1)+1):
            inv = sp.invert(poly(chi**t),poly(E)).as_expr()
            lift = rem(e*inv,N)
            check(name, 'persistent idempotent explicit chi^t ideal membership t='+str(t), equal(rem(chi**t*lift-e,N),0))
        lam,b = [(lam,b) for lam,a,b in rootdata if a==0][0]
        if b==2 and deg(E)==2:
            n = rem(e*(S-lam),N)
            check(name, 'persistent double-root sector keeps nonzero nilpotent', not equal(n,0) and equal(rem(n*n,N),0) and equal(rem(e*n-n,N),0))
        row.update({'E_persistent':textpoly(E),'M_complement':textpoly(M),'bezout_U':textpoly(U),'bezout_V':textpoly(V),'persistent_idempotent':textpoly(e)})
    if name == 'mixed':
        d = sp.expand(A**3*B**2)
        R = 1+S+I
        Q = S**2-3*I
        P = sp.expand(Q+d*R)
        T = sp.expand(P+R*chi2/2)
        check(name, 'mixed exact squared-generator residue with minus two', equal(rem(chi2,N),-2*d))
        check(name, 'mixed common-refinement signed half lift', equal(T,Q+R*N/2) and equal(rem(T-P,chi2),0) and equal(rem(T-Q,N),0))
        check(name, 'mixed complete first three power dimensions', [p['actual_matrix_rank'] for p in powers[:3]] == [3,1,0])
        row.update({'mixed_d':textpoly(d),'mixed_R':textpoly(R),'mixed_P':textpoly(P),'mixed_Q':textpoly(Q),'mixed_T':textpoly(T)})
    rows.append(row)

check('provenance','current source pin after fixtures',sha(source)==source_pin)
for name,pin in historical.items():
    check('provenance','historical preserved after: '+name,sha(W/name)==pin)
out = {
    'schema':'endpoint-reflected-kernel-powers-exact-fixtures/v1',
    'scope':'Exact finite Gaussian-rational fixtures for RF.18--RF.26 and explicit persistent CRT maps. General proofs are reviewed separately. No realized arithmetic packet or zero-location claim.',
    'runtime':{'python':sys.version,'sympy':sp.__version__,'optimization':sys.flags.optimize,'__debug__':__debug__},
    'source':{'path':source.name,'sha256':source_pin},
    'checker':{'path':Path(__file__).name,'sha256':sha(Path(__file__))},
    'historical_files_preserved':historical,
    'passed':len(checks),'failed':0,'fixtures':rows,'checks':checks,
}
target.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'path':str(target),'sha256':sha(target),'passed':len(checks),'failed':0,'optimization':sys.flags.optimize,'__debug__':__debug__},indent=2))
