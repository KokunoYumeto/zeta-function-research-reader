# Compare the SL2(Z) representation carried by the shadow vector of the note's
# m=42, K={1,6,14,21} construction (weight 3/2 odd unary theta series) with the
# representation carried by the three characters of the Virasoro minimal model M(2,7).
# Convention: for a vector F of weight k, F(-1/tau) = (-i tau)^k * rhoS * F(tau),
#             F(tau+1) = rhoT * F(tau).  (-i tau)^k uses the principal branch.
import mpmath as mp, itertools
mp.mp.dps = 40
e = lambda x: mp.expjpi(2*x)

# --- the note's projected support vectors in C[Z/84] (Lemma 'three primitive projected vectors')
V = {1:  {1:1,13:-1,29:-1,41:1,43:-1,55:1,71:1,83:-1},
     5:  {5:1,19:1,23:1,37:1,47:-1,61:-1,65:-1,79:-1},
     11: {11:1,17:1,25:1,31:1,53:-1,59:-1,67:-1,73:-1}}
labels = [1,5,11]

def G(a, tau, L=700):
    """weight-3/2 shadow component: sum over l in Z of psi_a(l) * l * q^(l^2/168)"""
    s = mp.mpc(0)
    for l in range(-L, L+1):
        c = V[a].get(l % 84, 0)
        if c:
            s += c * l * mp.exp(2j*mp.pi*tau*mp.mpf(l*l)/168)
    return s

def eta(tau, L=400):
    # eta = sum_n chi12(n) q^(n^2/24)
    s = mp.mpc(0)
    for n in range(1, L):
        c = {1:1,11:1,5:-1,7:-1}.get(n % 12, 0)
        if c: s += c*mp.exp(2j*mp.pi*tau*mp.mpf(n*n)/24)
    return s

def chiM27(s_, tau, L=200):
    """Rocha-Caridi character chi_{1,s}^{(2,7)}"""
    acc = mp.mpc(0)
    for n in range(-L, L+1):
        a = 28*n + 7 - 2*s_; b = 28*n + 7 + 2*s_
        acc += mp.exp(2j*mp.pi*tau*mp.mpf(a*a)/56) - mp.exp(2j*mp.pi*tau*mp.mpf(b*b)/56)
    return acc/eta(tau)

def rhoS(F, k, taus):
    # solve F(-1/tau) = (-i tau)^k M F(tau) for M (3x3) by least squares over sample points
    rows = []; rhs = []
    for t in taus:
        Ft = [F(j, t) for j in range(3)]
        Fs = [F(j, -1/t) for j in range(3)]
        fac = mp.power(-1j*t, k)
        rows.append(Ft); rhs.append([x/fac for x in Fs])
    A = mp.matrix(rows); B = mp.matrix(rhs)
    # M^T solves A M^T = B
    AH = A.H
    N = AH*A
    MT = mp.zeros(3)
    for c in range(3):
        col = mp.lu_solve(N, AH*B.column(c))
        for r_ in range(3): MT[r_, c] = col[r_]
    M = MT.T
    res = mp.mnorm(A*MT - B, 1)
    return M, res

taus = [mp.mpc('0.11','1.02'), mp.mpc('-0.23','0.97'), mp.mpc('0.31','0.95'), mp.mpc('-0.05','1.1'), mp.mpc('0.4','0.92')]

FG = lambda j, t: G(labels[j], t)
FC = lambda j, t: chiM27(j+1, t)
SG, resG = rhoS(FG, mp.mpf(3)/2, taus)
SC, resC = rhoS(FC, 0, taus)
TG = mp.diag([e(mp.mpf(r*r)/168) for r in labels])
TC = mp.diag([e(mp.mpf((7-2*s)**2)/56 - mp.mpf(1)/24) for s in (1,2,3)])

def show(M, name):
    print(name)
    for i in range(3):
        print('   ', '  '.join(mp.nstr(M[i,j], 12) for j in range(3)))
print('fit residuals:', mp.nstr(resG,5), mp.nstr(resC,5))
show(SG, 'rho_shadow(S)  [labels 1,5,11]')
show(SC, 'rho_M(2,7)(S)  [s = 1,2,3]')

def relres(S, T):
    I = mp.eye(3)
    ST = S*T
    return mp.mnorm(ST*ST*ST - S*S, 1), mp.mnorm(S*S*S*S - I, 1)
print('shadow  relations |(ST)^3-S^2|, |S^4-I|:', [mp.nstr(x,5) for x in relres(SG, TG)])
print('M(2,7)  relations |(ST)^3-S^2|, |S^4-I|:', [mp.nstr(x,5) for x in relres(SC, TC)])

# --- search: conj(rho_shadow) = chi * P rho_M27 P^{-1} with P a signed permutation, chi a scalar pair
best = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1,-1], repeat=3):
        P = mp.zeros(3)
        for i in range(3): P[i, perm[i]] = signs[i]
        for conjflag in (False, True):
            A_S = SG.apply(mp.conj) if conjflag else SG
            A_T = TG.apply(mp.conj) if conjflag else TG
            BS = P*SC*P.T; BT = P*TC*P.T
            # scalar ratios
            lamS = A_S[0,0]/BS[0,0] if abs(BS[0,0])>1e-10 else None
            lamT = A_T[0,0]/BT[0,0]
            if lamS is None: continue
            rS = mp.mnorm(A_S - lamS*BS, 1); rT = mp.mnorm(A_T - lamT*BT, 1)
            best.append((rS + rT, perm, signs, conjflag, lamS, lamT))
best.sort(key=lambda x: x[0])
for b in best[:4]:
    print('residual', mp.nstr(b[0],5), 'perm', b[1], 'signs', b[2], 'conj', b[3],
          'lambda_S', mp.nstr(b[4],10), 'lambda_T', mp.nstr(b[5],10),
          ' arg(lambda_T)/2pi =', mp.nstr(mp.arg(b[5])/(2*mp.pi), 10))

# --- the note's 'cubic phase transport' pair: (S_theta, e(-1/24) T_theta^3) on span(v1,v5,v11)
Tcub = mp.diag([e(3*mp.mpf(r*r)/168 - mp.mpf(1)/24) for r in labels])
print('note pair (rho_shadow(S), e(-1/24)T^3) relations:', [mp.nstr(x,5) for x in relres(SG, Tcub)])
