"""Independent interval reproduction; analytic bounds in WITNESS_RECEIVER.tex.
No zero table or numerical zeta evaluator. No optimization-sensitive guards.
"""
from pathlib import Path
import json, math, time
from fractions import Fraction
from mpmath import mp, iv

mp.dps=330; iv.dps=360
base=Path(__file__).resolve().parent
source=base/'inputs'/'rational_witness.json'
if not source.exists(): source=base/'rational_witness.json'
raw=json.loads(source.read_text(encoding='utf-8-sig'))
N=160; panels=24; maxmoment=38; start=time.monotonic()
def need(ok,msg):
    if not ok: raise ArithmeticError(msg)
def leg(ctx,x):
    p0=ctx.mpf(1); p1=x
    for j in range(2,N+1): p0,p1=p1,((2*j-1)*x*p1-(j-1)*p0)/j
    return p1,N*(x*p1-p0)/(x*x-1)
def frac_endpoint(v):
    sign,m,e,b=v
    return (-1)**sign*Fraction(m)*Fraction(2)**e
def endpoints(v): return tuple(map(frac_endpoint,v._mpi_))
def encode(v):
    lo,hi=endpoints(v)
    return {'binary':[list(map(int,t)) for t in v._mpi_], 'display':[mp.nstr(mp.mpf(t[1])*mp.power(2,t[2])*(-1)**t[0],40) for t in v._mpi_], 'sign':1 if lo>0 else -1 if hi<0 else 0}
nodes=[]
for j in range(1,N+1):
    root=mp.cos(mp.pi*(j-mp.mpf('0.25'))/(N+mp.mpf('0.5')))
    for it in range(30):
        value,derivative=leg(mp,root); step=value/derivative; root-=step
        if abs(step)<mp.mpf('1e-315'): break
    else: raise ArithmeticError('Newton did not converge')
    left=mp.nstr(root-mp.mpf('1e-280'),320)
    right=mp.nstr(root+mp.mpf('1e-280'),320)
    lo=iv.mpf(left);hi=iv.mpf(right)
    lv=leg(iv,lo)[0];rv=leg(iv,hi)[0]
    need(bool(lv*rv<0),'Legendre bracket did not isolate a sign change')
    bracket=iv.mpf([left,right]); derivative=leg(iv,bracket)[1]
    need(bool(derivative**2>0),'Derivative interval includes zero')
    weight=2/((1-bracket**2)*derivative**2)
    need(bool(weight>0),'Weight interval not positive')
    nodes.append((bracket,weight))
nodes.sort(key=lambda pair:endpoints(pair[0])[0])
need(endpoints(nodes[0][0])[0]>-1 and endpoints(nodes[-1][0])[1]<1,'Node outside (-1,1)')
for a,b in zip(nodes,nodes[1:]): need(endpoints(a[0])[1]<endpoints(b[0])[0],'Node brackets overlap')
print('All 160 Legendre roots bracketed with disjoint rational intervals.',flush=True)
moments={t:[iv.mpf(0) for _ in range(maxmoment+1)] for t in (-2,0)}
errors={t:[iv.mpf(0) for _ in range(maxmoment+1)] for t in (-2,0)}
h=iv.mpf(1)/16; ell=iv.mpf(1)/8
A=iv.mpf(17)/128; B=iv.mpf(15)/128; kappa=1-(4*B)**2/2
for panel in range(panels):
    center=iv.mpf(2*panel+1)/16
    for node,weight in nodes:
        u=center+h*node; u2=u*u
        e4=iv.exp(4*u);e5=iv.exp(5*u);e9=iv.exp(9*u)
        phi=iv.mpf(0)
        for n in range(1,17):
            phi+=(2*iv.pi**2*n**4*e9-3*iv.pi*n*n*e5)*iv.exp(-iv.pi*n*n*e4)
        value=h*weight*phi; value_negative=value*iv.exp(-2*u2)
        power=iv.mpf(1)
        for k in range(maxmoment+1):
            moments[0][k]+=value*power
            moments[-2][k]+=value_negative*power
            power*=u2
    xp=center+A;xm=center-A;R2=xp*xp+B*B
    pref=(32*iv.exp(9*xp)*sum(n**4 for n in range(1,17))+12*iv.exp(5*xp)*sum(n*n for n in range(1,17)))*iv.exp(-3*iv.exp(4*xm)*kappa)
    for t in (-2,0):
        heat=iv.exp(abs(t)*B*B)
        err=4*ell*pref*heat/(3*iv.mpf(4)**(2*N-1));power=iv.mpf(1)
        for k in range(maxmoment+1):
            errors[t][k]+=err*power;power*=R2
    if (panel+1)%4==0: print(f'Panels {panel+1}/{panels}; elapsed {time.monotonic()-start:.1f}s',flush=True)
results={}
c=[iv.mpf(1000**i)*iv.mpf(n)/iv.mpf(raw['denominator']) for i,n in enumerate(raw['rational_numerators'])]
for t in (-2,0):
    for k in range(maxmoment+1):
        err=errors[t][k]+192*17**4*3**(2*k)*iv.exp(-840)+iv.exp(-2000)
        moments[t][k]+=iv.mpf([-1,1])*err.b
        need(bool(moments[t][k]>0),'Positive theta moment could not be enclosed')
    a=[((-1)**k)*moments[t][k]/math.factorial(2*k) for k in range(maxmoment+1)]
    S=[iv.mpf(0)]
    for n in range(1,maxmoment+1):
        S.append((-2*n*a[n]-sum((a[j]*S[n-j] for j in range(1,n)),iv.mpf(0)))/moments[t][0])
    Sp=[iv.mpf(0)]
    for n in range(1,maxmoment):
        Sp.append(2*n*(sum((S[j]*S[n+1-j] for j in range(1,n+1)),iv.mpf(0))-(2*n+1)*S[n+1]))
    q=sum((c[i]*c[j]*S[i+j+1] for i in range(19) for j in range(19)),iv.mpf(0))
    qp=sum((c[i]*c[j]*Sp[i+j+1] for i in range(19) for j in range(19)),iv.mpf(0))
    values={'q':encode(q),'q_derivative':encode(qp)}
    need(values['q']['sign']==(-1 if t==-2 else 1),'Witness sign not certified')
    need(values['q_derivative']['sign']==1,'Derivative sign not certified')
    coarse={-2:{'q':('-2.385e-46','-2.383e-46'),'q_derivative':('1.0766e-44','1.0767e-44')},0:{'q':('0.00081442298606666852','0.00081442298606666854'),'q_derivative':('0.00218680919457417358','0.00218680919457417359')}}
    for key,current in [('q',q),('q_derivative',qp)]:
        supplied=raw['values'][str(t)][key]['binary']
        s0,s1=map(frac_endpoint,supplied);lo,hi=endpoints(current)
        need(max(lo,s0)<=min(hi,s1),'Independent interval is disjoint from supplied interval')
        outerlo,outerhi=map(Fraction,coarse[t][key])
        need(outerlo<=lo<=hi<=outerhi,'Printed outward bound did not enclose the computed interval')
        values[key]['overlaps_supplied_interval']=True
        values[key]['printed_outward_bound']=coarse[t][key]
    results[str(t)]=values
    print(json.dumps({'time':t,'q':values['q']['display'],'q_derivative':values['q_derivative']['display']}),flush=True)
receipt={'status':'passed','scope':'Original 19-coefficient rational witness and its time derivative at t=-2,0. Complete theta integrals and all root moments; no zero table. Does not certify the supplied 32-dimensional inertia or smaller supplied intervals.',
 'implementation':'Independent mpmath.iv directed-interval quadrature with explicit analytic remainder; no formal verification of interval library.',
 'precision_digits':iv.dps,'nodes_per_panel':N,'panels':panels,'theta_terms':16,'max_moment':maxmoment,
 'elapsed_seconds':time.monotonic()-start,'results':results}
(base/'REPRODUCED_RATIONAL_WITNESS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print('Independent rational-witness reproduction passed.',flush=True)
