#!/usr/bin/env python3
"""Non-interval numerical checks of the explicit ray-period determinant.
The written proof is independent of these quadratures.
"""
import json
from pathlib import Path
import mpmath as mp

ROOT=Path(__file__).resolve().parent

def run(dps):
    mp.mp.dps=dps
    records=[]
    # Actual stated coefficients of calibration polynomials, not zeta packets.
    fixtures=[([mp.mpf('0.2')+mp.mpf('0.1')*1j,mp.mpf('-0.3')],mp.mpf('0.15'),mp.mpf('1.4')),
              ([mp.mpf('0.1'),mp.mpf('0.2')+mp.mpf('0.07')*1j,mp.mpf('-0.15')],mp.mpf('0.11'),mp.mpf('1.2'))]
    for cs,t,u in fixtures:
        q=len(cs);d=q+1
        Phi=lambda s:s**d/d+sum(cs[a]*s**(a+1)/(a+1) for a in range(q))-t*s
        angles=[(mp.arg(u)+mp.pi)/d+2*mp.pi*j/d for j in range(d)]
        integrals=mp.matrix(d,q)
        for j,theta in enumerate(angles):
            v=mp.exp(1j*theta)
            for b in range(q):
                f=lambda r:mp.exp(Phi(r*v)/u)*(r*v)**b*v
                integrals[j,b]=mp.quad(f,[0,1,2,4,8,mp.inf])
        Pi=mp.matrix(q,q);Pm=mp.matrix(q,q)
        for j in range(1,d):
            for b in range(q):
                Pi[j-1,b]=integrals[j,b]-integrals[0,b]
                Pm[j-1,b]=(d*abs(u))**(mp.mpf(b+1)/d)/d*mp.gamma(mp.mpf(b+1)/d)*mp.exp(1j*(b+1)*angles[0])*(mp.exp(2j*mp.pi*j*(b+1)/d)-1)
        roots=mp.polyroots([1]+list(reversed(cs[1:]))+[cs[0]-t],maxsteps=200)
        F=sum(Phi(a) for a in roots)
        det=mp.det(Pi); predicted=mp.det(Pm)*mp.exp(F/u)
        error=abs(det/predicted-1)
        modulus=abs(abs(det)**2/((2*mp.pi*abs(u))**q*mp.exp(2*mp.re(F/u)))-1)
        records.append({'q':q,'u':str(u),'t':str(t),'coefficients':[str(x) for x in cs],
                        'relative_complex_determinant_error':mp.nstr(error,10),
                        'relative_squared_modulus_error':mp.nstr(modulus,10),
                        'critical_trace':mp.nstr(F,30)})
        if error>mp.mpf(10)**(-dps+8):raise RuntimeError('calibration mismatch')
    return {'precision_dps':dps,'scope':'uncertified numerical contour quadrature, not arithmetic data','fixtures':records}

if __name__=='__main__':
    out=run(35)
    (ROOT/'checks'/'period-numerical.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
