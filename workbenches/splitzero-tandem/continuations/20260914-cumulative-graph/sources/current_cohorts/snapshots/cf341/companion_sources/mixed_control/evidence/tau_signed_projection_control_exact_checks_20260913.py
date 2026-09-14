"""Exact complex-Gram checks of SP identities, not arithmetic-packet evidence."""
import hashlib
import json
from pathlib import Path
import sympy as s

OUT = Path(__file__).with_suffix('.json')
Z = s.Symbol('S')


def clean(m):
    return m.applyfunc(s.cancel)


def zero(m):
    return all(s.cancel(v) == 0 for v in m)


def trace(m):
    return s.cancel(s.trace(m))


rows = []
for q in (1, 2):
    n = 2*q + 1
    c = s.Rational(3, 2)
    nodes = list(range(-q, q+1))
    vs = [s.Matrix([[ (c+s.I*j)**a for a in range(n)]]) for j in nodes]
    M0 = clean(sum(((2+j*j)*(v.conjugate().T*v) for j, v in zip(nodes, vs)), s.zeros(n)))
    M1 = clean(sum(((3+(j+1)**2)*(v.conjugate().T*v) for j, v in zip(nodes, vs)), s.zeros(n)))
    dot = M1-M0
    chi = s.expand(s.prod(Z-s.Rational(j+2, 3)-s.I*s.Rational(1,j+4) for j in range(q)))
    for x in (s.Rational(0), s.Rational(1,3), s.Rational(1)):
        M = clean(M0+x*dot)
        Mi = clean(M.inv())
        T = clean(Mi*dot)
        Ps, Qs, Bs, Is = {}, {}, {}, {}
        for N in set((q-1, q, 2*q-1, 2*q)):
            U = s.eye(n)[:, :N+1]
            Is[N] = U
            Ps[N] = clean(U*(U.conjugate().T*M*U).inv()*U.conjugate().T*M)
            if N < q:
                B = s.zeros(n, 0)
                Qs[N] = s.zeros(n)
            else:
                B = s.Matrix(n, N-q+1, lambda a,b:s.expand(chi*Z**b).coeff(Z,a))
                Qs[N] = clean(B*(B.conjugate().T*M*B).inv()*B.conjugate().T*M)
            Bs[N] = B
            assert zero(Ps[N]**2-Ps[N])
            assert zero(Qs[N]**2-Qs[N])
            assert zero(Ps[N].conjugate().T*M-M*Ps[N])
            assert zero(Qs[N].conjugate().T*M-M*Qs[N])
            # Monic coordinates and the exact Schur quotient-volume identity.
            change = s.eye(N+1)[:, :q].row_join(B[:N+1,:])
            assert s.cancel(change.det()) == 1
            K = clean(change.conjugate().T*(U.conjugate().T*M*U)*change)
            Hr = K[q:,q:]
            G = K[:q,:q] if N < q else clean(K[:q,:q]-K[:q,q:]*Hr.inv()*K[q:,:q])
            assert s.cancel((U.conjugate().T*M*U).det()-G.det()*Hr.det()) == 0
        RR = clean(Qs[2*q-1]+Qs[2*q]-Qs[q])
        PP = clean(Ps[2*q-1]-Ps[q-1]+Ps[2*q]-Ps[q])
        AA = clean(RR-PP)
        assert RR.rank() == q+1 and PP.rank() == q+1
        assert trace(RR) == 2*q and trace(PP) == 2*q
        assert trace(RR*RR) == 4*q-2 and trace(PP*PP) == 4*q-2
        ov = trace(RR*PP)
        assert ov.is_Rational and ov >= 1
        assert trace(AA) == 0
        assert trace(AA*AA) == 8*q-4-2*ov
        assert zero(M*T-T.conjugate().T*M)
        signed = trace(T*(Ps[q-1]-Qs[q-1]+Ps[q]-Qs[q]-Ps[2*q-1]+Qs[2*q-1]-Ps[2*q]+Qs[2*q]))
        assert signed == trace(T*AA)
        v = s.Matrix([[ (c+s.I*s.Rational(1,7))**a for a in range(n)]])
        ker = s.S.Zero
        for N,sgn in ((q-1,1),(q,1),(2*q-1,-1),(2*q,-1)):
            U, B = Is[N], Bs[N]
            source_kernel = U*(U.conjugate().T*M*U).inv()*U.conjugate().T
            relation_kernel = s.zeros(n) if N < q else B*(B.conjugate().T*M*B).inv()*B.conjugate().T
            ker += sgn*(v*(source_kernel-relation_kernel)*v.conjugate().T)[0]
        assert s.cancel(ker-(v*AA*Mi*v.conjugate().T)[0]) == 0
        # L = range(RR) intersect range(PP), computed without eigenvectors.
        overlap_dimension = 2*(q+1)-Bs[2*q].row_join(PP).rank()
        assert overlap_dimension >= 1
        rows.append(dict(q=q,x=str(x),rank=q+1,trace=2*q,overlap=str(ov),intersection_dimension=overlap_dimension,all_identities=True))

r,x = s.symbols('r x', positive=True)
f = (r-1)/(1+x*(r-1))
assert s.cancel(s.diff(f,r)-1/(1+x*(r-1))**2) == 0
assert s.cancel(s.diff(s.log(1+x*(r-1)),x)-f) == 0
result = dict(status='PASS',scope='Exact algebra checks on positive discrete complex moment Grams; these samples are not the original arithmetic densities and make no RH or uniform-family assertion.',cases=rows,scalar_derivative_and_antiderivative=True,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
