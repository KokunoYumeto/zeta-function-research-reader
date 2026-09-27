# Referee machinery (independent of all workbench code): Peter-Weyl block coefficients of products of
# SU(2) plaquette traces, with per-link Clebsch-Gordan couplings, for the Fourier-algebra norms F4-F6.
#
# A function is written f(U) = sum T[alpha; beta] prod_o U_{e(o)}[alpha_o, beta_o] over 'occurrences' o
# (inverse letters are rewritten with U^{-1} = eps U^T eps^{-1}).  For a per-link intertwiner
# J_e : V_{s_e} -> (C^2)^{(x) k_e} (standard Condon-Shortley basis m = s, s-1, ..., -s), the block of spin
# assignment j has coefficient  A_j[m, m'] = sum T[alpha;beta] conj(J[beta, m]) J[alpha, m'],
# so that f_j(U) = Tr(A_j D^j(U)).  Its Fourier-algebra norm is the trace norm of A_j.
import itertools, functools
import numpy as np
import opt_einsum as oe
from fractions import Fraction as Fr
from sympy.physics.quantum.cg import CG
from sympy import Rational, nsimplify

HALF = Fr(1, 2)
eps = np.array([[0., 1.], [-1., 0.]]); epsinv = np.linalg.inv(eps)

def dim(s): return int(2 * s + 1)

@functools.lru_cache(maxsize=None)
def cg_tensor(j1, j2, J):
    """C[m1, m2, M] = <j1 m1 j2 m2 | J M>, index k <-> m = j - k."""
    j1, j2, J = Fr(j1), Fr(j2), Fr(J)
    C = np.zeros((dim(j1), dim(j2), dim(J)))
    for a in range(dim(j1)):
        for b in range(dim(j2)):
            for c in range(dim(J)):
                m1, m2, M = j1 - a, j2 - b, J - c
                if m1 + m2 != M: continue
                val = CG(Rational(j1.numerator, j1.denominator), Rational(m1.numerator, m1.denominator),
                         Rational(j2.numerator, j2.denominator), Rational(m2.numerator, m2.denominator),
                         Rational(J.numerator, J.denominator), Rational(M.numerator, M.denominator)).doit()
                C[a, b, c] = float(val)
    return C

def intertwiner(path):
    """path = list of intermediate spins [1/2, s2, s3, ...] obtained by coupling occurrences one at a time
    (first occurrence has spin 1/2).  Returns J with shape (2,)*k + (dim(s_k),)."""
    J = np.eye(2)                           # V_{1/2} -> C^2
    cur = HALF
    for s in path[1:]:
        C = cg_tensor(cur, HALF, s)         # V_s -> V_cur (x) C^2
        # J_new[o_1..o_k, o_{k+1}, M] = sum_mc J[o_1..o_k, mc] C[mc, o_{k+1}, M]
        J = np.tensordot(J, C, axes=([J.ndim - 1], [0]))
        cur = s
    return J

def su2(q):
    q = np.asarray(q, float); q = q / np.linalg.norm(q)
    return np.array([[q[0] + 1j * q[3], q[2] + 1j * q[1]], [-q[2] + 1j * q[1], q[0] - 1j * q[3]]])

def D(s, U):
    """standard D^s(U) = J^* U^{(x)2s} J with the symmetric coupling path."""
    if s == 0: return np.ones((1, 1), complex)
    path = [HALF + HALF * k for k in range(int(2 * s))]
    J = intertwiner(path)
    k = int(2 * s)
    Jm = J.reshape(2**k, dim(s))
    Uk = functools.reduce(np.kron, [U] * k)
    return Jm.conj().T @ Uk @ Jm

# ---------------------------------------------------------------- lattice words
def plaquette(n, i, j):
    ei = tuple(1 if k == i else 0 for k in range(3)); ej = tuple(1 if k == j else 0 for k in range(3))
    add = lambda a, b: tuple(x + y for x, y in zip(a, b))
    return ((n, i, j), [((n, i), +1), ((add(n, ei), j), +1), ((add(n, ej), i), -1), ((n, j), -1)])

def links_of(p): return frozenset(e for e, _ in p[1])

@functools.lru_cache(maxsize=None)
def word_tensor_signs(signs):
    """T[alpha_1..alpha_l, beta_1..beta_l] for tr(M_1...M_l), M_i = U_i or U_i^{-1} by sign."""
    l = len(signs)
    T = np.zeros((2,) * (2 * l))
    for r in itertools.product(range(2), repeat=l):
        facs = []
        for k, s in enumerate(signs):
            ri, rn = r[k], r[(k + 1) % l]
            if s == +1: facs.append([((ri, rn), 1.0)])
            else: facs.append([((al, be), eps[ri, be] * epsinv[al, rn]) for al in range(2) for be in range(2)
                               if eps[ri, be] * epsinv[al, rn] != 0])
        for combo in itertools.product(*facs):
            c = 1.0; ia = []; ib = []
            for (al, be), w in combo: c *= w; ia.append(al); ib.append(be)
            T[tuple(ia) + tuple(ib)] += c
    return T

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def block_coefficient(plaqs, couplings):
    """plaqs: list of plaquettes (the product of their traces, in this order).
    couplings: dict link -> (list of occurrence ids (plaquette index, letter position) in coupling order,
                             coupling path of spins).  Every occurrence must appear exactly once.
    Returns (sorted list of (link, spin) with spin > 0, A_j as a matrix)."""
    # einsum operands
    labels = iter(LETTERS)
    alpha, beta = {}, {}
    operands = []
    for pi, p in enumerate(plaqs):
        signs = tuple(s for _, s in p[1])
        T = word_tensor_signs(signs)
        ia = []; ib = []
        for pos in range(4):
            alpha[(pi, pos)] = next(labels); beta[(pi, pos)] = next(labels)
            ia.append(alpha[(pi, pos)]); ib.append(beta[(pi, pos)])
        operands.append((T, ia + ib))
    out_rows, out_cols, spins = [], [], []
    for e in sorted(couplings):
        occ, path = couplings[e]
        s = path[-1]
        J = intertwiner(path)
        if s == 0:
            # spin-0 output: contract and drop the (1-dim) index
            J = J[..., 0]
            operands.append((J, [alpha[o] for o in occ]))
            operands.append((J.conj(), [beta[o] for o in occ]))
            continue
        mrow, mcol = next(labels), next(labels)
        operands.append((J, [alpha[o] for o in occ] + [mcol]))
        operands.append((J.conj(), [beta[o] for o in occ] + [mrow]))
        out_rows.append(mrow); out_cols.append(mcol); spins.append((e, s))
    args = []
    for arr, idx in operands:
        args += [arr, idx]
    # np.einsum with sublist format requires integer labels
    lab_map = {}
    def to_int(ls): return [lab_map.setdefault(c, len(lab_map)) for c in ls]
    args2 = []
    for arr, idx in operands:
        args2 += [arr, to_int(idx)]
    res = oe.contract(*args2, to_int(out_rows + out_cols), optimize='dp')
    dr = int(np.prod([dim(s) for _, s in spins])) if spins else 1
    return spins, res.reshape(dr, dr)

def eval_block(spins, A, Uconf):
    """f_j(U) = Tr(A_j D^j(U))."""
    Dm = np.ones((1, 1), complex)
    for e, s in spins: Dm = np.kron(Dm, D(s, Uconf[e]))
    return np.trace(A @ Dm)

def eval_word(p, Uconf):
    M = np.eye(2, dtype=complex)
    for e, s in p[1]: M = M @ (Uconf[e] if s == 1 else np.linalg.inv(Uconf[e]))
    return np.trace(M)

def trace_norm(A): return float(np.linalg.svd(A, compute_uv=False).sum())
