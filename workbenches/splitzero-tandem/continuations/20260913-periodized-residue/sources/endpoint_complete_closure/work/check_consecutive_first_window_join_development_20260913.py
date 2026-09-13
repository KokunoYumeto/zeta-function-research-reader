"""Exact original-S Gaussian calibrations of CJ's first-window identity."""
import argparse, json, sys
from pathlib import Path
import sympy as s

def run(mutation):
    S=s.Symbol('S'); X=S-1
    cases=[]; checks=[]
    def check(name, value):
        checks.append({'name':name,'passed':bool(value)})
    for q in (1,2,3,4):
        for mass in (s.Rational(7),s.Rational(5,2)):
            for mean in (s.Rational(0),s.Rational(2,3)):
                label=f'q{q}_mass{mass}_mean{mean}'
                chi=s.Poly(X**q,S,domain=s.QQ_I)
                polys=[s.Poly(1,S),s.Poly(X-s.I*mean,S)]
                for n in range(1,2*q+1):
                    polys.append(s.Poly((X-s.I*mean)*polys[-1].as_expr()+n*polys[-2].as_expr(),S))
                b=[]
                for p in polys:
                    rem=p.rem(chi)
                    b.append(s.Matrix([rem.nth(a) for a in range(q)]))
                omega=[mass*s.factorial(n) for n in range(len(polys))]
                A=s.zeros(q)
                for a in range(q):
                    rem=s.Poly(S**(a+1),S).rem(chi)
                    A[:,a]=s.Matrix([rem.nth(j) for j in range(q)])
                K=s.zeros(q); data={}
                for N in range(2*q+1):
                    K+=b[N]*b[N].conjugate().T/omega[N]
                    if N<q-1:continue
                    G=K.inv(); V=G.det()
                    H=G.inv()*A.conjugate().T*G+A-2*s.eye(q)
                    radius=s.cancel(s.trace(H*H)/2)
                    phase=s.cancel((b[N].conjugate().T*G*b[N+1])[0]/(s.I*omega[N]))
                    data[N]={'K':K.copy(),'G':G,'V':V,'radius':radius,'phase':phase}
                    check(label+f'_N{N}_trace_zero',s.trace(H)==0)
                    check(label+f'_N{N}_rank_two',H.rank()<=2)
                    check(label+f'_N{N}_phase_real',s.im(phase)==0)
                    check(label+f'_N{N}_radius_nonnegative',radius>=0)
                # chi=p_q+sum gamma_j p_j, solved in original S coefficients.
                P=s.Matrix([[polys[j].nth(a) for j in range(q+1)] for a in range(q+1)])
                coeff=P.inv()*s.Matrix([chi.nth(a) for a in range(q+1)])
                nu=s.cancel(sum(s.conjugate(coeff[j])*coeff[j]*omega[j] for j in range(q+1)))
                delta=s.cancel(data[q]['V']/data[q-1]['V'])
                check(label+'_literal_relation_norm_transition',delta==omega[q]/nu)
                check(label+'_first_radius_identity',s.cancel(data[q-1]['radius']+data[q-1]['phase']**2-(nu-omega[q])/omega[q-1])==0)
                for j in range(q,2*q+1):
                    lhs=s.prod(data[N]['radius']+(0 if mutation=='omit_phase' else data[N]['phase']**2) for N in range(q-1,j))
                    terminal=1-data[j]['V']/data[j-1]['V']
                    rhs=omega[j]*data[q-1]['V']/(omega[q-1]*data[j]['V'])
                    rhs*=terminal**(2 if mutation=='terminal_square' else 1)
                    rhs*=s.prod((1-data[N]['V']/data[N-1]['V'])**(1 if mutation=='interior_single' else 2) for N in range(q,j))
                    check(label+f'_first_product_to{j}',s.cancel(lhs-rhs)==0)
                if q>=2 and mean==0 and q%2==1:
                    F=s.Matrix.hstack(*b[q:2*q])
                    check(label+'_retained_zero_first_block',F.rank()<q)
                cases.append({'q':q,'mass':str(mass),'mean':str(mean),'nu0':str(nu),
                              'first_phase':str(data[q-1]['phase']),
                              'first_block_ratio':str(s.cancel(data[q-1]['V']/data[2*q-1]['V']))})
    return {'scope':'Finite Gaussian sources, not zeta packets. Original S=1+iu, all literal masses, tilted means, full quotient multiplicities and phases retained.',
            'runtime':{'python':sys.version.split()[0],'sympy':s.__version__,'optimization':sys.flags.optimize,'__debug__':__debug__},
            'mutation':mutation,'cases':cases,'checks':checks,'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks)}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    parser.add_argument('--mutation',choices=['none','omit_phase','terminal_square','interior_single'],default='none')
    args=parser.parse_args(); out=Path(args.output)
    if out.exists():raise RuntimeError('Refusing to overwrite evidence')
    result=run(args.mutation)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(out),'passed':result['passed'],'failed':result['failed'],'mutation':args.mutation,'runtime':result['runtime']}))
    raise SystemExit(1 if result['failed'] else 0)
