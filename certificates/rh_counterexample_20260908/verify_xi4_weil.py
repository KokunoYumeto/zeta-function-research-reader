"""Full classical Weil form on the actual separated-link multiplier channels.

Independent frequency-side gamma integral, explicit infinite-tail enclosure,
and compact real-space prime correlations. No zero ordinate is an input.
"""
import os
for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
from resource_ceiling import install_memory_ceiling
RESOURCE = install_memory_ceiling()
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import argparse, hashlib, json, math, time
from flint import arb, acb, acb_mat, ctx
import verify_weil_bspline as base

HERE = Path(__file__).resolve().parent
PARAMS = [(F(2),0),(F(-1),0),(F(-1),1),(F(-5,2),0),(F(-9,2),0)]
COEFF = [F(0),-F(59,275184),F(1,336),F(1,1296),F(3,132496)]
T = F(96)
TOL = 100

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def b(q):
    q=F(q)
    return arb(q.numerator)/q.denominator
def transform(z, index):
    sigma, degree=PARAMS[index]
    q=z-b(sigma)
    sinc=(q/2).sinc()
    if not degree: return sinc**4
    # -d/dq sinc(q/2)^4, entire even at q=0.
    return q/3*sinc**3*(-q*q/16).hypgeom_0f1(arb(5)/2)
def gamma_weight(z):
    return (((acb(arb(1)/4)+acb(0,arb(1)/2)*z).digamma()
             +(acb(arb(1)/4)-acb(0,arb(1)/2)*z).digamma())/2
            -arb.pi().log())/(2*arb.pi())
def gamma_tail(i,j):
    a=F(9,2); ell=b(T-a)
    # |Phi_i(t)| <= C_i/(|t|-a)^4 for |t|>=T.
    constants=[b(16) if degree==0 else b(32)+64/ell for _,degree in PARAMS]
    d=arb.const_euler()+8+arb.pi().log()+(1+2*b(T)).log()
    # Concavity log(1+2t) <= log(1+2T)+(t-T)/(T+1/2).
    integral=d/(7*ell**7)+1/(42*(b(T)+b(F(1,2)))*ell**6)
    return constants[i]*constants[j]*integral/arb.pi()
def gamma_entry(i,j):
    segments=[]
    for k in range(-int(T),int(T)):
        value=acb.integral(lambda z, analytic:
            transform(z,i)*transform(z,j)*gamma_weight(z),
            k,k+1,abs_tol=arb(2)**-TOL,rel_tol=arb(2)**-TOL,
            eval_limit=20000,depth_limit=25)
        assert value.is_finite() and value.imag.contains(0), (i,j,k,value)
        segments.append(value.real)
    tail=gamma_tail(i,j)
    central=sum(segments,arb(0))
    enclosure=central+arb(0,tail.upper())
    return enclosure, {"central":str(central),"tail_absolute_bound":str(tail),
                       "segments":[str(v) for v in segments]}
def spline_poly(q, cell):
    return sum(b(F((-1)**k*math.comb(4,k),6))*(q+2-k)**3
               for k in range(cell+3))
def correlation(x,i,j):
    # H_ij(x)=g_j*g_i(x); every g_i satisfies g_i^star=g_i.
    lo,hi=x-2,arb(2)
    knots=[lo,hi]
    for k in range(-2,3):
        for value in (arb(k),x-k):
            if value>lo and value<hi: knots.append(value)
    knots.sort(key=lambda q: float(q.mid()))
    unique=[]
    for q in knots:
        if unique and q==unique[-1]: continue
        if unique: assert q>unique[-1]
        unique.append(q)
    result=acb(0)
    sj,dj=PARAMS[j]; si,di=PARAMS[i]
    for l,r in zip(unique,unique[1:]):
        mid=(l+r)/2
        cj=math.floor(float(mid)); ci=math.floor(float(x-mid))
        assert mid>cj and mid<cj+1 and x-mid>ci and x-mid<ci+1
        def integrand(v,analytic):
            w=x-v
            return (spline_poly(v,cj)*spline_poly(w,ci)
                    *(acb(0,b(sj))*v+acb(0,b(si))*w).exp()
                    *(acb(0,1)*v if dj else 1)*(acb(0,1)*w if di else 1))
        value=acb.integral(integrand,l,r,abs_tol=arb(2)**-TOL,
                          rel_tol=arb(2)**-TOL,eval_limit=20000,depth_limit=25)
        assert value.is_finite()
        result+=value
    return result
def run():
    ctx.prec=192; ctx.threads=1
    started=time.time()
    powers=base.prime_powers(4)
    rows=[]; matrix=[[arb(0) for _ in PARAMS] for _ in PARAMS]
    for i in range(5):
        for j in range(i,5):
            pole=2*(transform(acb(0,arb(1)/2),i)
                    *transform(acb(0,arb(1)/2),j)).real
            gamma,gr=gamma_entry(i,j)
            prime=arb(0); prime_rows=[]
            for n,p,r in powers:
                h=correlation(arb(n).log(),i,j)
                prime+=2*arb(p).log()/arb(n).sqrt()*h.real
                prime_rows.append({"n":n,"p":p,"r":r,"correlation":str(h)})
            value=pole+gamma-prime
            matrix[i][j]=matrix[j][i]=value
            rows.append({"i":i,"j":j,"value":str(value),"pole":str(pole),
                         "gamma":gr,"prime":str(prime),"prime_terms":prime_rows})
            print("XI4_WEIL_ENTRY",i,j,str(value),flush=True)
    determinants=[]
    for k in range(1,6):
        det=acb_mat([[matrix[i][j] for j in range(k)] for i in range(k)]).det()
        assert det.imag.contains(0) and det.real>0, (k,det)
        determinants.append(str(det.real))
    value=sum(b(COEFF[i])*matrix[i][j]*b(COEFF[j])
              for i in range(5) for j in range(5))
    cross=sum(matrix[0][j]*b(COEFF[j]) for j in range(5))
    schur=value-cross**2/matrix[0][0]
    old=json.loads((HERE/"endpoint_weil_results.json").read_text(encoding="utf-8"))
    assert matrix[0][0].overlaps(arb(old["entries"][0]["real"]))
    assert value>0 and schur>0
    return {"id":"XI4-ACTUAL-WEIL-20260908-001","computed_utc":datetime.now(timezone.utc).isoformat(),
        "status":"pass","resource":RESOURCE,"parameters":{"b_endpoint":"8","sigma":"2",
          "channels":[{"frequency":str(s),"degree_iu":d} for s,d in PARAMS],
          "source_coefficients":[str(c) for c in COEFF],"support":["-2","2"],
          "gamma_cutoff":str(T),"precision_bits":ctx.prec,"tolerance_bits":TOL},
        "entries":rows,"matrix":[[str(v) for v in row] for row in matrix],
        "positive_leading_determinants":determinants,"source_multiplier_Weil_value":str(value),
        "original_source_cross_term":str(cross),"source_after_optimal_seed_subtraction":str(schur),
        "independent_prior_real_space_overlap":True,"prime_powers":powers,
        "source_hashes":{p.name:sha(p) for p in [Path(__file__),Path(base.__file__),HERE/"resource_ceiling.py"]},
        "zero_ordinates_used":False,"RH_counterexample":False,"Lean_verified":False,
        "scope":"Five explicit source-directed C_c^2 channels with all poles, gamma tails, primes and cross terms",
        "elapsed_seconds":time.time()-started}
if __name__=="__main__":
    parser=argparse.ArgumentParser(); parser.add_argument("--write",action="store_true")
    args=parser.parse_args(); result=run()
    if args.write:
        (HERE/"xi4_weil_results.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print("XI4_WEIL_COMPLETE",result["source_multiplier_Weil_value"],
          result["source_after_optimal_seed_subtraction"],flush=True)
