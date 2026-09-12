"""Exact finite calibrations of AP.24--36 and KL.21--32.

The original Gaussian mass is 1 and variance is 1/16, on s=1/2+it.
These polynomial quotient models retain all coefficients and full nilpotents.
The induced theta norm is integrated directly against |h|^2 dnu. These
fixtures certify the displayed finite identities, not actual zeta zeros.
"""
from pathlib import Path
import argparse
import hashlib
import json
from itertools import product
import sys
import sympy as sp
import check_arithmetic_frontier_parity as a

ROOT = Path(__file__).resolve().parents[1]
records = []


def check(name, value):
    records.append({'name': name, 'passed': bool(value)})


def eq(name, left, right):
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        diff = sp.Matrix(left)-sp.Matrix(right)
        check(name, all(a.scalar_zero(x) for x in diff))
    else:
        check(name, a.scalar_zero(left-right))


def symmetric_case(model, degree, negative):
    key = f'symmetric_d{model.d}_k{model.k}_M{degree}'
    tuples = list(product(range(model.d), repeat=model.k))
    orbits = sorted(set(tuple(sorted(t)) for t in tuples))
    I = sp.Matrix([[int(tuple(sorted(t)) == o) for o in orbits] for t in tuples])
    D = I.H*I
    L = D.inv()*I.H
    if negative:
        L[0, :] = 2*L[0, :]
    P = I*L
    K = model.kernel(degree)
    G = K.inv()
    Kn = model.kernel(degree+1)
    Gn = Kn.inv()
    low, high, F, E, O, _, _, _ = model.frontier(degree)
    Oi = O.inv()
    Gs = I.H*G*I
    Ksi = Gs.inv()
    F0, E0 = L*F, L*E
    Cs = L*model.Ck*I
    As = L*model.Ak*I
    W = model.Ak.H*G+G*model.Ak-model.k*G
    Ws = I.H*W*I
    eta = (-1)**(model.k*model.d+degree+1)
    eq(key+':orbit_left_inverse', L*I, sp.eye(len(orbits)))
    eq(key+':orthogonal_projection', P, P.H)
    eq(key+':idempotence', P*P, P)
    eq(key+':metric_commutation', G*P, P*G)
    eq(key+':rectangular_metric', I.H*G, Gs*L)
    eq(key+':inverse_compression', Ksi, L*K*L.H)
    eq(key+':generator', model.Ak*I, I*As)
    eq(key+':original_weight', Ws, As.H*Gs+Gs*As-model.k*Gs)
    eq(key+':frontier_weight', Ws, Gs*(F0*Oi*E0.H+E0*Oi*F0.H)*Gs)
    eq(key+':inverse_update', (I.H*Gn*I).inv(), Ksi+F0*Oi*F0.H)
    eq(key+':reflection', Cs*Cs, sp.eye(len(orbits)))
    eq(key+':reflection_metric', Cs.H*Gs*Cs, Gs)
    eq(key+':first_parity', Cs*F0, eta*F0)
    eq(key+':second_parity', Cs*E0, -eta*E0)
    eq(key+':opposite_pairing', F0.H*Gs*E0, sp.zeros(len(high)))
    Bf, Be = Oi*F0.H*Gs*F0, Oi*E0.H*Gs*E0
    relative = Ksi*Ws
    eq(key+':trace_square', sp.trace(relative**2), 2*sp.trace(Bf*Be))
    # The characteristic identity retains every zero eigenvalue, even if the
    # redundant source dimension is larger than the target dimension.
    z = a.lam
    p = (F0*Oi*E0.H).rank()
    positive_char = (Bf*Be).charpoly(z).as_expr()
    quotient = sp.div(sp.Poly(positive_char, z), sp.Poly(z**(len(high)-p), z))
    check(key+':positive_zero_multiplicity', quotient[1].is_zero)
    expected = z**(len(orbits)-2*p)*quotient[0].as_expr().subs(z,z*z)
    eq(key+':full_characteristic', relative.charpoly(z).as_expr(), expected)
    pi = sp.cancel((I.H*Gn*I).det()/Gs.det())
    eq(key+':volume', 1/pi, (sp.eye(len(high))+Bf).det())
    gamma = max(sum((v+1)*a.variance+(model.k-1)*v*a.variance for v in alpha) for alpha in low)
    psd = gamma*Ksi-E0*Oi*E0.H
    for order in range(1,len(orbits)+1):
        from itertools import combinations
        for selected in combinations(range(len(orbits)),order):
            check(key+':incidence_PSD_'+str(selected), psd.extract(selected,selected).det()>=0)
    # Exact grouping of the complete source frontier with its orbit factorial.
    groups = sorted(set(tuple(sorted(beta)) for beta in high))
    Fg, Eg, norms = [], [], []
    for orbit in groups:
        indices=[j for j,beta in enumerate(high) if tuple(sorted(beta))==orbit]
        f=sum((F0[:,j] for j in indices),sp.zeros(len(orbits),1))
        e=sum((E0[:,j] for j in indices),sp.zeros(len(orbits),1))
        for j in indices:
            eq(key+':orbit_F_'+str(orbit)+str(j), F0[:,j], F0[:,indices[0]])
            eq(key+':orbit_E_'+str(orbit)+str(j), E0[:,j], E0[:,indices[0]])
        Fg.append(f); Eg.append(e); norms.append(len(indices)*O[indices[0],indices[0]])
    FG,EG=sp.Matrix.hstack(*Fg),sp.Matrix.hstack(*Eg)
    OGI=sp.diag(*norms).inv()
    eq(key+':grouped_cross', FG*OGI*EG.H, F0*Oi*E0.H)
    eq(key+':grouped_kernel', FG*OGI*FG.H, F0*Oi*F0.H)
    eq(key+':grouped_incidence', EG*OGI*EG.H, E0*Oi*E0.H)
    return {'case':key,'orbit_counts':list(map(str,D.diagonal())), 'pi':str(pi),
            'relative_charpoly':str(sp.factor(relative.charpoly(z).as_expr())),
            'source_orbit_norms':list(map(str,norms)), 'rank':p}


def norm_case(h, name, reflected, negative):
    model=a.Packet(h,1)
    d=model.d
    eps=model.U.inv()
    s=a.s
    qs=[]; norms=[]; metrics=[]; remainders=[]; ratios=[]
    for j in range(4):
        Q=s**j
        for old, norm in zip(qs,norms):
            Q-=old*a.gram_gaussian(h*old,h*s**j)/norm
        Q=sp.expand(Q)
        norm=a.gram_gaussian(h*Q,h*Q)
        qs.append(Q);norms.append(norm)
        n=d+j
        v=[model.remainder(a.q(l)) for l in range(n+1)]
        K=sum((v[l]*v[l].H/a.kappa(l) for l in range(n)),sp.zeros(d))
        Ki=K.inv()
        G=eps.H*Ki*eps
        Kn=K+v[n]*v[n].H/a.kappa(n)
        Gn=eps.H*Kn.inv()*eps
        r=sp.cancel(Gn.det()/G.det())
        ratios.append(r)
        metrics.append(G)
        H=a.kappa(n)+(v[n].H*Ki*v[n])[0]
        key=name+f':j{j}'
        eq(key+':original_norm', H,norm)
        eq(key+':volume_norm', a.kappa(n),norm*r)
        numerator=a.q(n)-sum((a.q(l)*(v[l].H*Ki*v[n])[0]/a.kappa(l) for l in range(n)),sp.Integer(0))
        eq(key+':full_polynomial_identity', numerator,h*Q)
        for old in qs[:-1]:
            eq(key+':original_orthogonality_'+str(qs.index(old)), a.gram_gaussian(h*old,h*Q),0)
        remainders.append((v,Ki,G,H))
    eq(name+':initial_theta',qs[0],1)
    for m in range(3):
        n=d+m+1
        v,Ki,G,H=remainders[m+1]
        k=a.kappa(n-1)
        row0=-v[n-1].H*Ki*eps/k
        row1=-v[n].H*Ki*eps/H
        alpha=(v[n-1].H*Ki*v[n-1])[0]/k
        beta=(v[n].H*Ki*v[n])[0]/k
        gamma=(v[n].H*Ki*v[n-1])[0]/k
        c=(row0*G.inv()*row1.H)[0]
        key=name+f':m{m}'
        eq(key+':row_a',(row0*G.inv()*row0.H)[0],alpha/k)
        eq(key+':row_b',(row1*G.inv()*row1.H)[0],k*beta/H**2)
        expected=gamma if negative and name=='complex' and m==0 else sp.conjugate(gamma)
        eq(key+':conjugate_cross', H*c,expected)
        eq(key+':two_norm_ratio',a.kappa(n)/k,(norms[m+1]/norms[m])*(ratios[m+1]/ratios[m]))
        eq(key+':alpha_volume',alpha,1-ratios[m])
        eq(key+':beta_volume',beta,(a.kappa(n)/k)*(1-ratios[m+1])/ratios[m+1])
        if reflected:
            eq(key+':quartet_cross',gamma,0)
            eq(key+':original_energy',alpha*beta-sp.conjugate(gamma)*gamma,
               (norms[m+1]/norms[m])*(1/ratios[m]-1)*(1-ratios[m+1])-H**2*sp.conjugate(c)*c)
    return {'case':name,'h':str(sp.expand(h)), 'monic_theta_polynomials':list(map(str,qs)),
            'original_theta_norms':list(map(str,norms)), 'volume_ratios':list(map(str,ratios))}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=ROOT/'checks/frontier_symmetric_norm_bridge.json')
    p.add_argument('--negative-control',action='store_true')
    args=p.parse_args()
    pair=(a.s-sp.Rational(1,4))*(a.s-sp.Rational(3,4))
    repeated=pair**2
    cases=[symmetric_case(a.Packet(pair,2),M,args.negative_control and M==2) for M in (2,3,4)]
    cases.append(symmetric_case(a.Packet(repeated,1),4,False))
    cases.extend(symmetric_case(a.Packet(a.q(2),1),M,False) for M in (1,2))
    cases.append(norm_case(repeated,'repeated',True,False))
    cases.append(norm_case((a.s-sp.Rational(1,4))*(a.s-sp.Rational(2,3)+sp.I/5),'complex',False,args.negative_control))
    failed=[r['name'] for r in records if not r['passed']]
    data={'scope':__doc__.strip(),'passed':len(records)-len(failed),'total':len(records),
          'all_passed':not failed,'failed':failed,'checks':records,'cases':cases,
          'negative_control':args.negative_control,'optimization':sys.flags.optimize,
          'sympy_version':sp.__version__,'source_hashes':{str(x.relative_to(ROOT)):hashlib.sha256(x.read_bytes()).hexdigest()
          for x in [Path(__file__),Path(a.__file__),ROOT/'tex/arithmetic_frontier_parity.tex',ROOT/'tex/kernel_layer_continuation.tex']}}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:data[k] for k in ('all_passed','total','passed','failed','optimization')}))
    return 0 if not failed else 1


if __name__=='__main__':
    sys.exit(main())
