# Referee computation (independent of all workbench code), fast version.
# A 'block function' is f(U) = sum_{m,m'} A[m, m'] prod_e D^{s_e}(U_e)[m'_e, m_e] for a fixed spin assignment
# (s_e) on a finite link set (standard Condon-Shortley basis).  Its Fourier-algebra norm is ||A||_1.
# Products of blocks decompose link by link with Clebsch-Gordan tensors:
#   (f g)_{s'} : A'[M, M'] = sum C[m, n, M] A_f[m, m'] A_g[n, n'] C[m', n', M'] on each shared link.
import itertools, functools
import numpy as np
from fractions import Fraction as Fr
from ym_blocks import cg_tensor, word_tensor_signs, plaquette, links_of, su2, D, dim, HALF, trace_norm

class Block:
    __slots__ = ('links', 'spins', 'A')
    def __init__(self, links, spins, A):
        self.links = list(links); self.spins = list(spins); self.A = A     # A has 2n indices: rows then cols
    def key(self): return tuple(zip(self.links, self.spins))
    def matrix(self):
        d = int(np.prod([dim(s) for s in self.spins])) if self.spins else 1
        return self.A.reshape(d, d)
    def evaluate(self, conf):
        Dm = np.ones((1, 1), complex)
        for e, s in zip(self.links, self.spins): Dm = np.kron(Dm, D(s, conf[e]))
        return np.trace(self.matrix() @ Dm)

def plaquette_block(p):
    """W_p as a Block with spin 1/2 on its four links (sorted link order)."""
    signs = tuple(s for _, s in p[1]); T = word_tensor_signs(signs)          # T[alpha_1..4, beta_1..4]
    order = sorted(range(4), key=lambda k: p[1][k][0])
    links = [p[1][k][0] for k in order]
    # A[m (beta), m' (alpha)]: rows = beta in sorted order, cols = alpha in sorted order
    A = np.transpose(T, [4 + k for k in order] + [k for k in order])
    return Block(links, [HALF] * 4, A.copy())

def product_blocks(f, g):
    """All blocks of f*g: yields (Block, dict shared_link -> (sf, sg, s'))."""
    shared = [e for e in f.links if e in g.links]
    allinks = sorted(set(f.links) | set(g.links))
    fs = dict(zip(f.links, f.spins)); gs = dict(zip(g.links, g.spins))
    options = [[abs(fs[e] - gs[e]) + k for k in range(int(fs[e] + gs[e] - abs(fs[e] - gs[e])) + 1)] for e in shared]
    nf, ng = len(f.links), len(g.links)
    # outer product with index layout: f rows, f cols, g rows, g cols
    AB = np.multiply.outer(f.A, g.A)
    for choice in itertools.product(*options):
        T = AB
        # current index bookkeeping: list of (kind, link, side) for each axis
        axes = [('f', e, 'r') for e in f.links] + [('f', e, 'c') for e in f.links] + [('g', e, 'r') for e in g.links] + [('g', e, 'c') for e in g.links]
        for e, s2 in zip(shared, choice):
            C = cg_tensor(fs[e], gs[e], s2)                   # C[mf, mg, M]
            for side in ('r', 'c'):
                i1 = axes.index(('f', e, side)); i2 = axes.index(('g', e, side))
                T = np.tensordot(T, C, axes=([i1, i2], [0, 1]))
                axes = [ax for k, ax in enumerate(axes) if k not in (i1, i2)] + [('n', e, side)]
        # final layout: rows over allinks (sorted), then cols
        spins, links, perm_r, perm_c = [], [], [], []
        for e in allinks:
            if e in shared: s = choice[shared.index(e)]; kind = 'n'
            elif e in fs: s = fs[e]; kind = 'f'
            else: s = gs[e]; kind = 'g'
            if s == 0:
                # a spin-0 coupled link: drop the trivial (size-1) axes
                continue
            links.append(e); spins.append(s)
            perm_r.append(axes.index((kind, e, 'r'))); perm_c.append(axes.index((kind, e, 'c')))
        # remove size-1 axes of dropped spin-0 links
        keep = perm_r + perm_c
        drop = [k for k in range(len(axes)) if k not in keep]
        for k in drop: assert T.shape[k] == 1
        T = np.transpose(T, keep + drop).reshape([T.shape[k] for k in keep])
        yield Block(links, spins, T), {e: (fs[e], gs[e], c) for e, c in zip(shared, choice)}

def casimir(block): return sum(s * (s + 1) for s in block.spins)

def B_of(r_block, X_block):
    """B(W_r, X) = sum over blocks j of (gamma_j / c_j) (W_r X)_j, with Gamma(W_r, X) = sum gamma_j (W_r X)_j."""
    out = []
    for blk, sh in product_blocks(X_block, r_block):
        gamma = Fr(0)
        for e, (sx, sr, s2) in sh.items():
            # 2 Gamma_e(f, h) = (c_f + c_h - E_e)(f h) on link e
            gamma += (sx * (sx + 1) + sr * (sr + 1) - s2 * (s2 + 1)) / 2
        out.append((blk, gamma, casimir(blk)))
    return out
