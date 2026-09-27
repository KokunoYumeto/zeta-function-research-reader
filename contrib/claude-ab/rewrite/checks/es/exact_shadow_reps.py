# Exact verification (in the cyclotomic field Q(zeta_N)) of the two representation isomorphisms:
#  (i)  m=42, K={1,6,14,21}, labels 1,5,11:  conj(rho_sh) (x) eps^3  ==  P rho_{M(2,7)} P^-1
#  (ii) m=30, K={1,6,10,15}, labels 1,7:     rho_sh (x) eps^-3       ==  Fibonacci modular data
# Convention: F(-1/tau) = (-i tau)^k rho(S) F(tau); eps = multiplier of eta, eps(S)=1, eps(T)=e(1/24).
# For the odd weight-3/2 series G_a = sum_r c_a(r) theta^1_{m,r}, rho_sh(S)_{ab} = kappa * sum_r c_a(r) e(-r b/2m),
# kappa = i/sqrt(2m). This formula is first checked numerically against a direct evaluation.
import sympy as sp, mpmath as mp, itertools
mp.mp.dps = 30

def formula_S(V, labels, m):
    return mp.matrix([[ (1j/mp.sqrt(2*m))*sum(c*mp.expjpi(-2*mp.mpf(r*b)/(2*m)) for r,c in V[a].items())
                        for b in labels] for a in labels])

def numeric_S(V, labels, m):
    def G(a,tau,L=600):
        return sum(V[a].get(l%(2*m),0)*l*mp.exp(2j*mp.pi*tau*mp.mpf(l*l)/(4*m)) for l in range(-L,L+1))
    taus=[mp.mpc('0.11','1.02'),mp.mpc('-0.23','0.97'),mp.mpc('0.31','0.95'),mp.mpc('-0.05','1.1')]
    n=len(labels); rows=[]; rhs=[]
    for t in taus:
        rows.append([G(a,t) for a in labels]); fac=mp.power(-1j*t,mp.mpf(3)/2)
        rhs.append([G(a,-1/t)/fac for a in labels])
    A=mp.matrix(rows); B=mp.matrix(rhs); AH=A.H; N=AH*A; MT=mp.zeros(n)
    for c in range(n):
        col=mp.lu_solve(N,AH*B.column(c))
        for r_ in range(n): MT[r_,c]=col[r_]
    return MT.T

V42 = {1:{1:1,13:-1,29:-1,41:1,43:-1,55:1,71:1,83:-1},
       5:{5:1,19:1,23:1,37:1,47:-1,61:-1,65:-1,79:-1},
       11:{11:1,17:1,25:1,31:1,53:-1,59:-1,67:-1,73:-1}}
V30 = {1:{1:1,11:1,19:1,29:1,31:-1,41:-1,49:-1,59:-1},
       7:{7:1,13:1,17:1,23:1,37:-1,43:-1,47:-1,53:-1}}
for V,labels,m in ((V42,[1,5,11],42),(V30,[1,7],30)):
    d = mp.mnorm(formula_S(V,labels,m)-numeric_S(V,labels,m),1)
    print(f'm={m}: |formula - direct evaluation| = {mp.nstr(d,3)}')

z = sp.symbols('z')
def red(expr, N):
    return sp.rem(sp.expand(expr), sp.cyclotomic_poly(N, z), z)
def zeta(k, n, N):   # zeta_n^k inside Q(zeta_N), zeta_N = z
    return z**((k*(N//n)) % N)

# (i) m = 42 against M(2,7).  sqrt(84)*conj(rho_sh(S))_{ab} = -i * sum_r c_a(r) zeta_84^{r b}
#     sqrt(84)*S_{2,7}(s,t) = -2 (zeta_3 - zeta_3^2) (-1)^{s+t} (zeta_7^{st} - zeta_7^{-st})
N = 168
lab = [1,5,11]; perm = {1:2, 5:3, 11:1}; sign = {1:1, 5:1, 11:-1}
ok = True
for a in lab:
    for b in lab:
        lhs = -zeta(1,4,N)*sum(c*zeta(r*b,84,N) for r,c in V42[a].items())
        s,t = perm[a], perm[b]
        rhs = sign[a]*sign[b]*(-2)*(zeta(1,3,N)-zeta(2,3,N))*(-1)**(s+t)*(zeta(s*t,7,N)-zeta(-s*t,7,N))
        ok &= (red(lhs-rhs, N) == 0)
from fractions import Fraction as F
Tsh = {r: F(r*r,168) for r in lab}
Tvir = {s: (F((7-2*s)**2,56) - F(1,24)) % 1 for s in (1,2,3)}
okT = all(((-Tsh[a] + F(1,8)) - Tvir[perm[a]]) % 1 == 0 for a in lab)
print('m=42: conj(rho_sh(S)) == P S_{M(2,7)} P^-1 exactly:', ok, '; conj(rho_sh(T))*e(1/8) == P T_{M(2,7)} P^-1:', okT)

# (ii) m = 30 against the Fibonacci data  S = (2/sqrt5)[[sin pi/5, sin 2pi/5],[sin 2pi/5, -sin pi/5]],
#      T = diag(e(-7/60), e(17/60)).  sqrt(60)*rho_sh(S)_{ab} = i * sum_r c_a(r) zeta_60^{-r b};
#      sqrt(60)*(2/sqrt5) sin(k pi/5) = -2 (zeta_3 - zeta_3^2)(zeta_10^k - zeta_10^-k)
N = 120
fib = {(1,1):1, (1,7):2, (7,1):2, (7,7):-1}   # entry = sign * k  with value sin(|k| pi/5)
ok2 = True
for a in (1,7):
    for b in (1,7):
        lhs = zeta(1,4,N)*sum(c*zeta(-r*b,60,N) for r,c in V30[a].items())
        k = fib[(a,b)]; sg = 1 if k>0 else -1; k = abs(k)
        rhs = sg*(-2)*(zeta(1,3,N)-zeta(2,3,N))*(zeta(k,10,N)-zeta(-k,10,N))
        ok2 &= (red(lhs-rhs, N) == 0)
okT2 = ((F(1,120) - F(1,8)) - F(-7,60)) % 1 == 0 and ((F(49,120) - F(1,8)) - F(17,60)) % 1 == 0
print('m=30: rho_sh(S) == Fibonacci S exactly:', ok2, '; rho_sh(T)*e(-1/8) == diag(e(-7/60), e(17/60)):', okT2)
# Lee-Yang M(2,5): S = (2/sqrt5)[[-sin 2pi/5, sin pi/5],[sin pi/5, sin 2pi/5]]; its diagonal entries have
# absolute value (2/sqrt5) sin(2pi/5), those of rho_sh(S) have (2/sqrt5) sin(pi/5). A signed permutation
# combined with a unimodular scalar preserves the multiset of |diagonal entries|, so no such twist matches.
print('|diag| shadow:', mp.nstr(2/mp.sqrt(5)*mp.sin(mp.pi/5),12), ' |diag| Lee-Yang:', mp.nstr(2/mp.sqrt(5)*mp.sin(2*mp.pi/5),12))
