"""Exact rational polynomial-source checks and separate numerical KG fixtures."""
from pathlib import Path
import itertools
import json
import math
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
exacts, numerics = [], []

def canon(x):
    return sp.cancel(sp.expand_complex(x))

def cm(A):
    return A.applyfunc(canon)

def eq(name, left, right):
    delta = left - right
    terms = list(delta) if isinstance(delta, sp.MatrixBase) else [delta]
    if any(canon(x) != 0 for x in terms):
        raise AssertionError((name, delta))
    exacts.append(name)

def psd(name, matrix):
    eq(name + '_Hermitian', matrix, matrix.conjugate().T)
    for r in range(1, matrix.rows + 1):
        for inds in itertools.combinations(range(matrix.rows), r):
            d = canon(matrix.extract(inds, inds).det())
            if d.is_nonnegative is not True:
                raise AssertionError((name, inds, d))
    exacts.append(name + '_all_principal_minors')

def chk(name, condition, value=None):
    if not bool(condition):
        raise AssertionError((name, value))
    numerics.append({'name':name, 'value':value})

def star(X):
    return X.conjugate().T

def rational_trace_bound(T, G):
    return canon(sp.trace(G.inv() * star(T) * G * T))

def nf(A):
    return np.array(A.evalf(17).tolist(), dtype=complex)

def sqrtmat(A, inverse=False):
    ev, vec = np.linalg.eigh(A)
    return (vec * (ev ** (-0.5 if inverse else 0.5))) @ vec.conj().T

# A complete rational Gaussian polynomial source, retaining mass seven.
# These declared roots and complex observations are auxiliary, not native packet data.
y = sp.symbols('y')
q = 4
poly = y ** 4 + 5 * y ** 2 + 4
def moment(j):
    return sp.Integer(0) if j % 2 else sp.Integer(7) * sp.factorial2(j - 1)
def remainder_column(j):
    p = sp.Poly(sp.rem(y ** j, poly, y), y)
    return sp.Matrix([p.nth(i) for i in range(q)])
M = sp.Matrix.hstack(*(remainder_column(j + 1) for j in range(q)))
u = M.inv()[:, 0]
roots = [sp.I, -sp.I, 2 * sp.I, -2 * sp.I]
Vroot = sp.Matrix([[r ** j for j in range(q)] for r in roots])
G1 = cm(star(Vroot) * sp.diag(1, 2, 3, 4) * Vroot / 10 ** 6)
Lam = sp.Matrix([[1, sp.I, 1, 0], [0, 1, 0, sp.I]])
IK = cm(sp.Matrix.hstack(*Lam.nullspace()))

for N in (3, 4, 7, 8):
    source = sp.Matrix(N + 1, N + 1, lambda i, j: moment(i + j))
    J = sp.Matrix.hstack(*(remainder_column(j) for j in range(N + 1)))
    G0 = (J * source.inv() * star(J)).inv()
    Rhat = source.inv() * star(J) * G0
    div = sp.zeros(N + 1)
    for j in range(N):
        div[j, j + 1] = 1
    C0 = G0.inv() * star(Rhat) * sp.Matrix(N + 1, N + 1, lambda i, j: moment(i + j + 1)) * Rhat
    eq(f'N{N}_complete_remainder_section', J * Rhat, sp.eye(q))
    eq(f'N{N}_attained_source_norm', star(Rhat) * source * Rhat, G0)
    eq(f'N{N}_physical_compression_adjoint', star(C0) * G0, G0 * C0)
    eq(f'N{N}_outgoing_rank', (M - C0).rank(), 1)
    psd(f'N{N}_joint_containment', G0 - G1)
    for alpha in (sp.Rational(0), sp.Rational(1, 7), sp.Rational(1)):
        tag = f'N{N}_alpha{alpha}'
        print('Checking ' + tag, flush=True)
        G = cm(((1 - alpha) * G0.inv() + alpha * G1.inv()).inv())
        Q = cm((cm(Lam * G.inv() * star(Lam))).inv())
        L = cm(G.inv() * star(Lam) * Q)
        K0 = cm(star(IK) * G * IK)
        PB = cm(L * Lam)
        eq(tag + '_coisometry_covariance', ((1 - alpha) * G0.inv() + alpha * G1.inv()) * G, sp.eye(q))
        eq(tag + '_observation_section', Lam * L, sp.eye(2))
        eq(tag + '_observation_isometry', star(L) * G * L, Q)
        eq(tag + '_complete_complement', PB + IK * K0.inv() * star(IK) * G, sp.eye(q))
        H = cm(G.inv() * star(M) * G * M)
        K1 = cm(star(IK) * star(M) * G * M * IK)
        K2 = cm(star(IK) * star(H) * G * H * IK)
        A = cm(K0.inv() * K1)
        B = cm(K0.inv() * star(IK) * G * H * L)
        BD = cm(Q.inv() * star(B) * K0)
        DH = cm(Q.inv() * star(L) * G * H * L)
        W = cm(sp.eye(2) + BD * A.inv() ** 2 * B)
        S = cm(DH - BD * A.inv() * B)
        EL = cm(L - IK * A.inv() * B)
        eq(tag + '_energy_lift', Lam * EL, sp.eye(2))
        eq(tag + '_energy_lift_norm', star(EL) * G * EL, Q * W)
        eq(tag + '_energy_lift_energy', star(EL) * G * H * EL, Q * S)
        eq(tag + '_word_mass_determinant', W.det(), K2.det() * K0.det() / K1.det() ** 2)
        eq(tag + '_graph_energy_determinant', S.det() / W.det(), M.det() ** 2 * K1.det() / K2.det())
        for ss in (1, 2):
            Us = sp.Matrix.hstack(*((M ** (-j))[:, 0] for j in range(1, ss + 1)))
            Rs0 = sp.Matrix.vstack(*(Rhat[ss - j, :] for j in range(1, ss + 1)))
            Bs0 = J * div ** ss * Rhat
            Bsa = cm((1 - alpha) * Bs0 * G0.inv() * G + alpha * M ** (-ss) * G1.inv() * G)
            Rsa = cm((1 - alpha) * Rs0 * G0.inv() * G)
            eq(tag + f'_inverse_power{ss}', M ** (-ss), Bsa + Us * Rsa)
            HE = cm(star(Us) * G * Us)
            HB = cm(star(Us) * star(Lam) * Q * Lam * Us)
            ell = 1 / canon(sp.trace(HB.inv() * HE))
            d2 = max(sp.Integer(1), rational_trace_bound(Bs0, G0), rational_trace_bound(M ** (-ss), G1))
            aa = canon(ell / d2)
            Ks = cm(star(M ** ss * IK) * G * (M ** ss * IK))
            psd(tag + f'_power{ss}_gap', Ks - aa * K0)
            Qt = cm(cm(Lam * M ** (-ss) * G.inv() * star(M ** (-ss)) * star(Lam)).inv())
            eq(tag + f'_power{ss}_quotient_determinant', Qt.det() / Q.det(), M.det() ** (2 * ss) * K0.det() / Ks.det())
            if ss == 1:
                a1 = aa
        for jj in (1, 2):
            Kj = cm(star(H ** jj * IK) * G * (H ** jj * IK))
            psd(tag + f'_positive_word{jj}_gap', Kj - a1 ** (2 * jj) * K0)
        z = sp.Rational(2, 7)
        F = cm(z * sp.eye(2) + DH - BD * (A + z * sp.eye(2)).inv() * B)
        eq(tag + '_complete_resolvent', F.inv(), Lam * (H + z * sp.eye(q)).inv() * L)
        eq(tag + '_second_order_pencil', F, S + z * W - z ** 2 * BD * A.inv() ** 2 * (A + z * sp.eye(2)).inv() * B)
        eq(tag + '_same_cutoff_determinant', F.det() / S.det(), (sp.eye(q) + z * H.inv()).det() / (sp.eye(2) + z * A.inv()).det())

# Exact sharp gap and essential leakage fixtures.
T = sp.Matrix([[2, sp.Rational(4, 3)], [0, 1]])
xx = sp.Matrix([sp.Rational(4, 5), sp.Rational(3, 5)])
eq('sharp_gap_image', T.inv() * xx, sp.Matrix([0, sp.Rational(3, 5)]))
eq('sharp_gap_value', (star(xx) * star(T.inv()) * T.inv() * xx)[0], sp.Rational(9, 25))
swap = sp.Matrix([[0, 1], [1, 0]])
eq('leakage_compression_zero', swap[0, 0], 0)
eq('leakage_complete_energy_positive', (star(swap) * swap)[0, 0], 1)

# Numerical checks of rank-sensitive relative estimates, complex remainders, poles and heat.
rng = np.random.default_rng(21092026)
for q in range(3, 8):
    for m in range(1, q):
        X = rng.normal(size=(q, q)) + 1j * rng.normal(size=(q, q))
        UL, _ = np.linalg.qr(X)
        X = rng.normal(size=(q, q)) + 1j * rng.normal(size=(q, q))
        UR, _ = np.linalg.qr(X)
        singular = np.r_[3.0, np.linspace(1.2, 0.65, q - 2), 0.008]
        M = UL @ np.diag(singular) @ UR.conj().T
        H = M.conj().T @ M
        A, B, DH = H[:m, :m], H[:m, m:], H[m:, m:]
        n = q - m
        S = DH - B.conj().T @ np.linalg.solve(A, B)
        AB = np.linalg.solve(A, B)
        W = np.eye(n) + AB.conj().T @ AB
        Wroot, Winvroot = sqrtmat(W), sqrtmat(W, True)
        Heff = Winvroot @ S @ Winvroot
        hs, HV = np.linalg.eigh(H)
        lam, fullsoft = hs[0], HV[:, 0]
        theta = float(np.linalg.norm(fullsoft[m:]) ** 2)
        dminus = 2.0
        aa = theta / dminus ** 2
        delta = lam / aa
        tag = f'q{q}_m{m}'
        chk(tag + '_kernel_gap', np.linalg.eigvalsh(A)[0] >= aa - 1e-10, float(np.linalg.eigvalsh(A)[0] - aa))
        chk(tag + '_finite_soft_guard', lam < aa, delta)
        nu = np.linalg.eigvalsh(Heff)
        chk(tag + '_effective_soft_energy', lam - 2e-10 <= nu[0] <= lam / (1 - delta) + 2e-10, float(nu[0] / lam))
        if n >= 2:
            chk(tag + '_effective_fast_gap', nu[1] >= 1 / dminus ** 2 - 1e-10, float(nu[1]))
        b = fullsoft[m:]
        wb = float(np.vdot(b, W @ b).real)
        chk(tag + '_soft_mass', (1 - delta) ** 2 - 1e-10 <= wb <= 1 + 1e-10, wb)
        sm = np.linalg.eigvalsh(S)[0]
        chk(tag + '_static_soft_energy', lam / (theta + lam * dminus ** 2) - 1e-10 <= sm <= lam / theta + 1e-10, float(sm))
        logdet = lambda V: float(np.linalg.slogdet(V)[1])
        dstar = 2 * math.log(3) + 2 * (m - 1) * math.log(1.2)
        chk(tag + '_strong_mass_determinant', logdet(A) + logdet(W) <= dstar + 1e-9, logdet(A) + logdet(W))
        chk(tag + '_strong_mass_norm', np.linalg.norm(W, 2) <= 1 + 9 / aa + 1e-9, float(np.linalg.norm(W, 2)))
        rho = np.linalg.matrix_rank(B)
        for z in (0.0, aa / 100, aa / 2, 2 * aa):
            F = z * np.eye(n) + DH - B.conj().T @ np.linalg.solve(A + z * np.eye(m), B)
            lin = S + z * W
            left = S + z * np.eye(n) + z / (1 + z / aa) * (W - np.eye(n))
            chk(tag + f'_z{z}_lower_pencil', np.linalg.eigvalsh(F - left)[0] >= -1e-9)
            chk(tag + f'_z{z}_upper_pencil', np.linalg.eigvalsh(lin - F)[0] >= -1e-9)
            dg = logdet(lin) - logdet(F)
            chk(tag + f'_z{z}_rank_log_bound', -1e-8 <= dg <= rho * math.log1p(z / aa) + 1e-8, dg)
            resol = Wroot @ np.linalg.inv(F) @ Wroot
            model = np.linalg.inv(z * np.eye(n) + Heff)
            chk(tag + f'_z{z}_resolvent_lower', np.linalg.eigvalsh(resol - model)[0] >= -2e-6)
            chk(tag + f'_z{z}_resolvent_upper', np.linalg.eigvalsh((1 + z / aa) * model - resol)[0] >= -2e-6)
            ratio = logdet(F) - logdet(S) - math.log1p(z / lam)
            chk(tag + f'_z{z}_soft_det_receiver', -m * math.log1p(z / aa) - 1e-8 <= ratio <= (q - 1) * math.log1p(z * dminus ** 2) + 1e-8, ratio)
        for p in (1, 2, 4):
            z = aa * (0.2 + 0.3j)
            F = z * np.eye(n) + DH - B.conj().T @ np.linalg.solve(A + z * np.eye(m), B)
            approx = S + z * W
            Ainv = np.linalg.inv(A)
            for j in range(2, p + 1):
                approx = approx + (-1) ** (j + 1) * z ** j * B.conj().T @ np.linalg.matrix_power(Ainv, j + 1) @ B
            rem = np.linalg.norm(Winvroot @ (F - approx) @ Winvroot, 2)
            bound = abs(z) ** (p + 1) / (aa ** p * (1 - abs(z) / aa))
            chk(tag + f'_complex_order{p}', rem <= bound + 1e-10, float(rem / bound))
        for tau in (0.0, 1.0, 1 / lam, 10 / lam):
            heat = (HV * np.exp(-tau * hs)) @ HV.conj().T
            Y = heat[m:, m:]
            weighted = float(np.trace(W @ Y).real)
            soft = math.exp(-tau * lam)
            bound = (1 - wb) * soft + (np.trace(W).real - wb) * math.exp(-tau / dminus ** 2)
            chk(tag + f'_tau{tau}_weighted_heat', abs(weighted - soft) <= bound + 1e-8, abs(weighted - soft))
            diff = float(np.exp(-tau * hs).sum() - np.exp(-tau * nu).sum())
            bound = delta / (math.e * (1 - delta)) + (q - 1) * math.exp(-tau / dminus ** 2)
            chk(tag + f'_tau{tau}_effective_heat', -1e-8 <= diff <= bound + 1e-8, diff)

result = {'status':'PASS', 'exact_check_count':len(exacts), 'numerical_check_count':len(numerics),
          'scope':'Exact full polynomial-source minima with rational Gaussian moments of mass seven, complex observation, four degree cutoffs and three covariance activations; separate synthetic numerical pole, heat and complex-remainder tests. No native moments or actual period evaluated.',
          'exact_checks':exacts, 'numerical_checks':numerics}
(HERE/'KERNEL_GAP_CHECK_RESULTS.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('exact_checks','numerical_checks')}, indent=2))
