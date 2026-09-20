"""Exact finite checks for MQ1--45; no assertion is disabled by python -O.

The finite atomic measures and rational diagonal transfers here are algebraic
test models only, never native-moment values or replacement native measures.
Their uncentered S coordinate has real part 3/2 and retains every complex term.
"""
from collections import Counter
import sympy as s

I = s.I
Q = s.Rational
counts = Counter()


def clean(value):
    return s.cancel(s.expand(value))


def mat(value):
    return s.Matrix(value).applyfunc(clean)


def eq(label, left, right):
    if isinstance(left, s.MatrixBase) or isinstance(right, s.MatrixBase):
        diff = mat(s.Matrix(left) - s.Matrix(right))
        okay = all(v == 0 for v in diff)
    else:
        okay = clean(left - right) == 0
    if not okay:
        raise RuntimeError(f"FAILED identity: {label}; difference {diff if 'diff' in locals() else clean(left-right)}")
    counts['identity'] += 1


def nonzero(label, value):
    values = list(value) if isinstance(value, s.MatrixBase) else [value]
    if all(clean(v) == 0 for v in values):
        raise RuntimeError(f"FAILED negative check: {label}")
    counts['negative'] += 1


def psd(label, value):
    value = mat(value)
    eq(label + ' Hermitian', value, value.H)
    from itertools import combinations
    for size in range(1, value.rows + 1):
        for inds in combinations(range(value.rows), size):
            determinant = clean(value.extract(inds, inds).det())
            if determinant.is_nonnegative is not True:
                raise RuntimeError(f"FAILED PSD: {label} minor {inds} = {determinant}")
    counts['PSD'] += 1


def scalar(label, value):
    value = clean(value)
    if value.is_nonnegative is not True:
        raise RuntimeError(f"FAILED scalar inequality: {label} = {value}")
    counts['inequality'] += 1


def inverse(value):
    return mat(value.inv())


def canonical(H, J):
    Hinv = inverse(H)
    G = inverse(mat(J * Hinv * J.H))
    R = mat(Hinv * J.H * G)
    return G, R


def projection(G, observation):
    Gin = inverse(G)
    obsG = inverse(mat(observation * Gin * observation.H))
    obsR = mat(Gin * observation.H * obsG)
    return mat(s.eye(G.rows) - obsR * observation), obsG, obsR


S = s.Symbol('S')
chi = s.Poly((S - (2 + I)) * (S - (1 - I)), S)
d = chi.degree()
nodes = [-2, -1, 0, 1, 2, 3]
weights = [1, 2, 3, 2, 1, 2]
source_k = 3
spectra = [Q(source_k, 2) + I * t for t in nodes]
W = s.diag(*weights)
E = s.diag(2 + I, 1 - I, 3 + 2 * I, 2 - I, 1 + 2 * I, 2 + 3 * I)
T = inverse(E.H)
eq('exact dual operators', T.H * E, s.eye(len(nodes)))
eq('reverse exact dual operators', E.H * T, s.eye(len(nodes)))
D = s.diag(*spectra)
eq('unchanged source generator', D + D.H, source_k * s.eye(len(nodes)))
eq('E commutes with source generator', E * D, D * E)
eq('T commutes with source generator', T * D, D * T)


def source(N):
    V = mat([[z ** j for j in range(N + 1)] for z in spectra])
    columns = []
    for j in range(N + 1):
        remainder = s.rem(s.Poly(S ** j, S), chi)
        columns.append(s.Matrix([remainder.nth(i) for i in range(d)]))
    J = mat(s.Matrix.hstack(*columns))
    relcols = []
    for j in range(N + 1 - d):
        p = s.Poly(S ** j * chi.as_expr(), S)
        relcols.append(s.Matrix([p.nth(i) for i in range(N + 1)]))
    Z = mat(s.Matrix.hstack(*relcols)) if relcols else s.zeros(N + 1, 0)
    H = mat(V.H * W * V)
    HT = mat(V.H * T.H * W * T * V)
    HE = mat(V.H * E.H * W * E * V)
    G, R = canonical(H, J)
    return V, J, Z, H, HT, HE, G, R


def current_tests(N):
    V, J, Z, H, HT, HE, G, R = source(N)
    tag = f'N={N}: '
    A = mat(J[:, 1:d+1]) if N >= d else mat(source(d)[1][:, 1:d+1])
    eq(tag + 'full relation basis', J * Z, s.zeros(d, Z.cols))
    eq(tag + 'full relation dimension', Z.cols, N + 1 - d)
    eq(tag + 'onto J', J[:, :d], s.eye(d))
    eq(tag + 'canonical right inverse', J * R, s.eye(d))
    eq(tag + 'canonical Gram', R.H * H * R, G)
    eq(tag + 'full relation orthogonality', R.H * H * Z, s.zeros(d, Z.cols))
    LT, LE = mat(T * V * R), mat(E * V * R)
    eq(tag + 'paired complete quotient Gram', LT.H * W * LE, G)
    eq(tag + 'reverse paired complete quotient Gram', LE.H * W * LT, G)
    eq(tag + 'opposite E relations', LT.H * W * E * V * Z, s.zeros(d, Z.cols))
    eq(tag + 'opposite T relations', LE.H * W * T * V * Z, s.zeros(d, Z.cols))
    B = mat(R * J)
    eq(tag + 'source projector idempotence', B * B, B)
    eq(tag + 'mixed adjoint projector', B.H * H, H * B)
    eq(tag + 'source projector kills full relations', B * Z, s.zeros(N+1, Z.cols))
    eq(tag + 'source complementary range relation', J * (s.eye(N+1)-B), s.zeros(d,N+1))

    GT, RT = canonical(HT, J)
    GE, RE = canonical(HE, J)
    dt, de = mat(RT - R), mat(RE - R)
    Xi = mat(dt.H * H * de)
    CT, CE = mat(R.H * HT * R), mat(R.H * HE * R)
    eq(tag + 'Delta T full relation', J * dt, s.zeros(d,d))
    eq(tag + 'Delta E full relation', J * de, s.zeros(d,d))
    eq(tag + 'full separate cross defect', RT.H * H * RE, G + Xi)
    eq(tag + 'T positive Pythagorean defect', CT - GT, dt.H * HT * dt)
    eq(tag + 'E positive Pythagorean defect', CE - GE, de.H * HE * de)
    psd(tag + 'positive T defect', CT-GT)
    psd(tag + 'positive E defect', CE-GE)
    # Exact constants of this finite test model, not substituted prime values.
    psd(tag + 'model T lower comparison', HT-Q(1,13)*H)
    psd(tag + 'model T upper comparison', Q(1,2)*H-HT)
    psd(tag + 'model E lower comparison', HE-2*H)
    psd(tag + 'model E upper comparison', 13*H-HE)
    if Z.cols:
        KT, KE = mat(Z.H * HT * Z), mat(Z.H * HE * Z)
        eq(tag + 'T explicit full-relation lift', dt, -Z * inverse(KT) * Z.H * HT * R)
        eq(tag + 'E explicit full-relation lift', de, -Z * inverse(KE) * Z.H * HE * R)
        eq(tag + 'full-relation Xi formula', Xi,
           R.H * HT * Z * inverse(KT) * (Z.H * H * Z) * inverse(KE) * Z.H * HE * R)
        nonzero(tag + 'separate minima cannot be identified', Xi)
        nonzero(tag + 'separate cross defect need not be Hermitian', Xi-Xi.H)
    else:
        eq(tag + 'no relation means no separate defect', Xi, s.zeros(d))

    obs = s.Matrix([[1, 1+I]])
    x = s.Matrix([1+I, 2-I])
    P, Qobs, Robs = projection(G, obs)
    a, b = mat(P*x), mat((s.eye(d)-P)*x)
    z, w = clean((a.H*G*A*b)[0]), clean((b.H*G*A*a)[0])
    eq(tag+'original K preserved', obs*P, s.zeros(1,d))
    eq(tag+'original orthogonal projection', P.H*G, G*P)
    eq(tag+'original orthogonal components', (a.H*G*b)[0], 0)
    for u,v in [(a,b),(b,a),(x,s.Matrix([2-I,1+2*I]))]:
        cross = (u.H*Xi*v)[0]
        scalar(tag+'sharp separate-defect Cauchy certificate',
               Q(13,2)*(u.H*(CT-GT)*u)[0]*(v.H*(CE-GE)*v)[0]
               -s.conjugate(cross)*cross)
        scalar(tag+'coarse separate-defect Cauchy certificate',
               Q(11,2)**2*(u.H*G*u)[0]*(v.H*G*v)[0]
               -s.conjugate(cross)*cross)
    eq(tag+'paired z phase', (LT*a).H*W*(LE*A*b), s.Matrix([[z]]))
    eq(tag+'paired w phase', (LT*b).H*W*(LE*A*a), s.Matrix([[w]]))
    eq(tag+'original observed cross-Gram', (LT*Robs).H*W*(LE*Robs), Qobs)
    eq(tag+'observed lift right inverse', obs*Robs, s.eye(1))
    Atadj = mat(inverse(G)*A.H*G)
    eq(tag+'paired action adjoint', (LT*A).H*W*LE, LT.H*W*LE*Atadj)
    zs, ws = clean((a.H*(G+Xi)*A*b)[0]), clean((b.H*(G+Xi)*A*a)[0])
    eq(tag+'separate z correction', zs-z, (a.H*Xi*A*b)[0])
    eq(tag+'separate w correction', ws-w, (b.H*Xi*A*a)[0])
    eq(tag+'separate product full correction', s.conjugate(zs)*ws-s.conjugate(z)*w,
       s.conjugate(zs-z)*w+s.conjugate(z)*(ws-w)+s.conjugate(zs-z)*(ws-w))
    PT = projection(GT, obs)[0]
    PE = projection(GE, obs)[0]
    et, ee = mat((PT-P)*x), mat((PE-P)*x)
    zsp = clean(((a+et).H*(G+Xi)*A*(b-ee))[0])
    wsp = clean(((b-et).H*(G+Xi)*A*(a+ee))[0])
    eq(tag+'separate projection z all terms', zsp-z,
       (et.H*G*A*b-a.H*G*A*ee-et.H*G*A*ee+(a+et).H*Xi*A*(b-ee))[0])
    eq(tag+'separate projection w all terms', wsp-w,
       (b.H*G*A*ee-et.H*G*A*a-et.H*G*A*ee+(b-et).H*Xi*A*(a+ee))[0])

    Vn, Jn, Zn, Hn, _, _, Gn, Rn = source(N+1)
    inc = s.eye(N+2)[:, :N+1]
    shift = s.zeros(N+2, N+1)
    for j in range(N+1):
        shift[j+1,j] = 1
    eq(tag+'cutoff exact inclusion', Jn*inc, J)
    eq(tag+'cutoff exact multiplication', Jn*shift, A*J)
    eq(tag+'native H restriction', inc.H*Hn*inc, H)
    eq(tag+'source differential action', D*V, Vn*shift)
    crel = mat(shift*R-inc*R*A)
    Gamma = mat(R.H*inc.H*Hn*crel)
    boundarypoly = s.Poly(S**(N+1-d)*chi.as_expr(),S)
    boundary = s.Matrix([boundarypoly.nth(j) for j in range(N+2)])
    leading = R[N:N+1,:]
    eq(tag+'complete boundary rank-one formula',Gamma,(R.H*inc.H*Hn*boundary)*leading)
    eq(tag+'boundary remainder still a relation',Jn*(crel-boundary*leading),s.zeros(d))
    eq(tag+'boundary remainder is in old degree', (crel-boundary*leading)[N+1:N+2,:],s.zeros(1,d))
    gaplift = mat(inc*R-Rn)
    eq(tag+'degree-raised action is full relation', Jn*crel, s.zeros(d))
    eq(tag+'cutoff lift gap is full relation', Jn*gaplift, s.zeros(d))
    eq(tag+'exact cutoff Gram decrease', G-Gn, gaplift.H*Hn*gaplift)
    psd(tag+'cutoff Gram decrease', G-Gn)
    eq(tag+'exact cutoff Gamma pairing', Gamma, gaplift.H*Hn*crel)
    eq(tag+'raw differential cross action', LT.H*W*D*LE, G*A+Gamma)
    eq(tag+'original source real part', inc.H*Hn*shift+shift.H*Hn*inc, source_k*H)
    eq(tag+'Gamma Hermitian obstruction', Gamma+Gamma.H, source_k*G-G*A-A.H*G)
    nonzero(tag+'cannot discard degree-raised relation correction', Gamma)
    rz, rw = clean((a.H*Gamma*b)[0]), clean((b.H*Gamma*a)[0])
    zraw, wraw = clean(z+rz), clean(w+rw)
    eq(tag+'raw source phase identity', zraw+s.conjugate(wraw), 0)
    eq(tag+'exact quotient phase obstruction', z+s.conjugate(w), -(a.H*(Gamma+Gamma.H)*b)[0])
    eq(tag+'raw product full correction', s.conjugate(z)*w,
       s.conjugate(zraw)*wraw-s.conjugate(rz)*wraw-s.conjugate(zraw)*rw+s.conjugate(rz)*rw)
    eq(tag+'next cutoff does not have same quotient Gram', Rn.H*Hn*shift*R, Gn*A)
    Phi = mat(crel.H*Hn*crel)
    psd(tag+'joint cutoff correction Gram',
        s.Matrix.vstack(s.Matrix.hstack(G-Gn,Gamma),s.Matrix.hstack(Gamma.H,Phi)))
    for u,v in [(a,b),(b,a),(x,s.Matrix([2-I,1+2*I]))]:
        scalar(tag+'finite Gamma Cauchy certificate',
               (u.H*(G-Gn)*u)[0]*(v.H*Phi*v)[0]
               -s.conjugate((u.H*Gamma*v)[0])*(u.H*Gamma*v)[0])
    gammaTE = mat(RT.H*inc.H*Hn*(shift*RE-inc*RE*A))
    eq(tag+'separate positive lift raw action with both defects',
       (T*V*RT).H*W*D*(E*V*RE), (G+Xi)*A+gammaTE)

    # Full physical CRT frame at both roots, with a nontrivial physical unit.
    # Test multipliers and unit values are not native zeta-derivative values.
    CRT = s.Matrix([[1,2+I],[1,1-I]])
    eta = s.diag(2+I,1-2*I)*CRT
    Bh = s.diag(1+I,2-I)
    Eh = s.diag(2-I,1+I)
    etat, etae = mat(Bh*eta), mat(Eh*eta)
    ZT, ZE = inverse(etat), inverse(etae)
    pg = mat(ZT.H*G*ZE)
    eq(tag+'literal physical mixed Gram', etat.H*pg*etae, G)
    eq(tag+'literal physical separate defect', etat.H*(ZT.H*Xi*ZE)*etae, Xi)
    eq(tag+'literal physical action correction', etat.H*(ZT.H*Gamma*ZE)*etae, Gamma)
    eq(tag+'full unit order positive minimum', ZT.H*GT*ZT,
       inverse(Bh).H*(inverse(eta).H*GT*inverse(eta))*inverse(Bh))
    nonzero(tag+'physical unit cannot be omitted', ZT.H*GT*ZT-inverse(Bh).H*GT*inverse(Bh))
    Apt, Ape = mat(etat*A*ZT), mat(etae*A*ZE)
    PPT, PPE = mat(etat*P*ZT), mat(etae*P*ZE)
    xt, xe = etat*x, etae*x
    eq(tag+'literal physical z', (PPT*xt).H*pg*Ape*((s.eye(d)-PPE)*xe), s.Matrix([[z]]))
    eq(tag+'literal physical w', ((s.eye(d)-PPT)*xt).H*pg*Ape*(PPE*xe), s.Matrix([[w]]))
    eq(tag+'physical action intertwines', Apt*etat, etat*A)
    eq(tag+'physical root action is literal', Apt,s.diag(2+I,1-I))
    eq(tag+'physical observation and kernel', obs*ZT*etat*P, s.zeros(1,d))
    print(f'PASS original-coordinate finite model N={N}', flush=True)


for degree in [1,2,3]:
    current_tests(degree)

# Exact finite-prime-shaped scalar bounds for arbitrary r in (0,1).
# Rational r values test the proved elementary inequalities, not a replacement
# prime parameter. Actual prime constants remain the unevaluated MQ9 products.
for r in [Q(1,3),Q(2,5),Q(3,4)]:
    for phase in [1,-1,I,-I,Q(3,5)+Q(4,5)*I]:
        b = 1-r*phase
        e = 1/s.conjugate(b)
        eq('scalar dual Euler-factor identity', s.conjugate(b)*e, 1)
        scalar('exact finite-factor lower bound', s.conjugate(b)*b-(1-r)**2)
        scalar('exact finite-factor upper bound', (1+r)**2-s.conjugate(b)*b)
        scalar('exact inverse-factor lower bound', s.conjugate(e)*e-(1+r)**-2)
        scalar('exact inverse-factor upper bound', (1-r)**-2-s.conjugate(e)*e)

# Complete-order Taylor inversion, including mixed complex derivatives.
for order in range(1,7):
    coeff = [Q(j+2,j+1)+I*Q(2*j+1,j+3) for j in range(order)]
    invcoeff = [1/coeff[0]]
    for j in range(1,order):
        invcoeff.append(clean(-sum(coeff[l]*invcoeff[j-l] for l in range(1,j+1))/coeff[0]))
    B = s.Matrix(order,order,lambda j,l:coeff[j-l] if j>=l else 0)
    Binv = s.Matrix(order,order,lambda j,l:invcoeff[j-l] if j>=l else 0)
    eq(f'complete-order divided jets {order}', B*Binv, s.eye(order))
    nilpotent = s.zeros(order)
    for j in range(order-1):
        nilpotent[j+1,j] = 1
    eq(f'complete-order action commutation {order}', B*nilpotent, nilpotent*B)

# Genuine rectangular cyclic physical image, retaining tensor factors and unit.
s0 = Q(1,2)+I
localS = s.Matrix([[s0,0],[1,s0]])
unit = s.Matrix([2+I,1-I])
localB = s.Matrix([[2-I,0],[1+I,2-I]])
localE = s.Matrix([[1+2*I,0],[2-I,1+2*I]])
totS = s.kronecker_product(localS,s.eye(2))+s.kronecker_product(s.eye(2),localS)
tensorunit = s.kronecker_product(unit,unit)
eta = mat(s.Matrix.hstack(*[totS**j*tensorunit for j in range(3)]))
eq('complete multiplicity nilpotence upper order', (totS-2*s0*s.eye(4))**3, s.zeros(4))
nonzero('complete multiplicity nilpotence exact lower order', (totS-2*s0*s.eye(4))**2*tensorunit)
eq('tensor cyclic dimension retains multiplicity', eta.rank(), 3)
BT = s.kronecker_product(localB,localB)
ET = s.kronecker_product(localE,localE)
etat, etae = mat(BT*eta), mat(ET*eta)
etaleft = mat(inverse(mat(eta.H*eta))*eta.H)
ZT, ZE = mat(etaleft*inverse(BT)),mat(etaleft*inverse(ET))
eq('rectangular original cyclic inverse', etaleft*eta,s.eye(3))
eq('rectangular T physical inverse on image',ZT*etat,s.eye(3))
eq('rectangular E physical inverse on image',ZE*etae,s.eye(3))
Gtest = s.Matrix([[3,1+I,0],[1-I,4,I],[0,-I,2]])
psd('rectangular model class Gram',Gtest)
eq('rectangular physical complete pairing',etat.H*(ZT.H*Gtest*ZE)*etae,Gtest)
nonzero('tensor multiplier cannot be collapsed to b(total S)', BT-(2-I)*s.eye(4)-(1+I)*(totS-s0*s.eye(4)))

# Colliding tensor sums with complete double jets: the exponent at the middle
# sum is max(3,3)=3, not 6. This checks the exact multiplicity in MQ4.
rhoa, rhob = Q(1,3)+I,Q(2,3)-I
sa, sb = s.Matrix([[rhoa,0],[1,rhoa]]),s.Matrix([[rhob,0],[1,rhob]])
local = s.diag(sa,sb)
sumop = s.kronecker_product(local,s.eye(4))+s.kronecker_product(s.eye(4),local)
u = s.Matrix([2+I,1-I,3-I,2+I])
tu = s.kronecker_product(u,u)
columns = [tu]
for degree in range(1,9):
    columns.append(mat(sumop*columns[-1]))
collision_eta = mat(s.Matrix.hstack(*columns))
eq('complete colliding cyclic relation degree',collision_eta.rank(),9)
chimat = s.eye(16)
for root in [2*rhoa,rhoa+rhob,2*rhob]:
    chimat = mat(chimat*(sumop-root*s.eye(16))**3)
eq('complete colliding multiplicity annihilator',chimat,s.zeros(16))

print('PASS all exact checks:', sum(counts.values()), dict(sorted(counts.items())), flush=True)
