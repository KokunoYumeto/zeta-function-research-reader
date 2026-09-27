# Upper bound for the relative upper density (among primes p = 2 mod 3) of primes with a two-edge shear path:
# a two-edge path with residual R forces R(R+4) | p+4 and p = -R (mod 4), a single class mod 4R(R+4).
# delta_R = (1 + [3 | R(R+4)]) / (2 phi(R(R+4)))  (relative to p = 2 mod 3).
from sympy import totient
N=200001
s=0.0; s1=0.0
for R in range(1,N,2):
    m=R*(R+4); ph=int(totient(R))*int(totient(R+4))   # gcd(R,R+4)=1
    s+= (1+(1 if m%3==0 else 0))/(2*ph); s1+=1/ph
print("sum_{R<%d} delta_R = %.6f ; sum 1/phi(R(R+4)) = %.6f"%(N,s,s1))
# tail bound: phi(n) >= n/(e^gamma loglog n + 3/loglog n) for n>=3 (Rosser-Schoenfeld 1962, Thm 15);
# for R >= N: phi(R)phi(R+4) >= R^2 / f(R)^2 with f(R) = e^g loglog(R+4) + 3/loglog(R+4) <= 2.2 for R+4 <= 10^30 (checked below);
import math
g=0.5772156649015329
f=lambda n: math.exp(g)*math.log(math.log(n))+3/math.log(math.log(n))
print("f at 2e5, 1e30:",f(2e5),f(1e30))
# for R in [N, 1e30]: 1/phi <= f^2/R^2 <= f(1e30)^2 / R^2 ; sum over odd R >= N of 1/R^2 <= 1/(2(N-2))
tail1=f(1e30)**2/(2*(N-2))
# beyond 1e30: f(n) <= 2 loglog n for such n, and sum_{R>1e30} (2 loglog R)^2/R^2 is < 1e-25
print("tail bound (R >= %d, both sums): %.6f"%(N,tail1))
print("so sum_R delta_R < %.4f and the lower relative density of primes = 2 mod 3 WITHOUT a two-edge path is > %.4f"%(s+tail1,1-(s+tail1)))
