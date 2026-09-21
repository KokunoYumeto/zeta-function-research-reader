from pathlib import Path
from fractions import Fraction as F
import json
P=Path(__file__).parent
def atan_bounds(x,n):
 s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
 t=(-1)**n*x**(2*n+1)/F(2*n+1)
 return min(s,s+t),max(s,s+t)
a,b=atan_bounds(F(1,5),14)
c,d=atan_bounds(F(1,239),4)
pl,ph=16*a-4*d,16*b-4*c
tl=(4-ph)/(4+ph);th=(4-pl)/(4+pl)
def logsum(t,n):return 2*sum((t**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
n=16
al=logsum(tl,n)
ah=logsum(th,n)+2*th**(2*n+1)/(F(2*n+1)*(1-th**2))
Cl=F(1353893,1000000);Ch=F(1354751,1000000)
lo,hi=Cl-2*ah,Ch-2*al
# Decimal outer endpoints are rational assertions, independent of floating display.
assert F(870764,1000000)<lo
assert hi<F(871623,1000000)
assert Cl>4*ah and al>0
out={"method":"Machin's exact pi identity, alternating arctangent bounds, and positive logarithm-series tail bound. Cpartial interval is inherited from its already-certified elliptic calculation.","pi_lower":str(pl),"pi_upper":str(ph),"a0_lower":str(al),"a0_upper":str(ah),"new_coefficient_lower":str(lo),"new_coefficient_upper":str(hi),"display_bounds":[0.870764,0.871623],"strict_original_heat_order":True}
(P/"CRITICAL_COEFFICIENT_CERTIFICATE.json").write_text(json.dumps(out,indent=2),encoding="utf-8")
print(json.dumps({"coefficient_interval":out["display_bounds"],"a0_approx":float((al+ah)/2),"heat_order":out["strict_original_heat_order"]}))

