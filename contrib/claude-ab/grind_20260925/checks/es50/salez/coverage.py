# Copied unchanged from the working files of referee pass B (an independent Claude instance, 27 September 2026).
# It implements Salez's seven modular equations (arXiv:1406.6307, Proposition 3) with explicit denominators.
"""
coverage.py -- which classes p mod L (p = 1 mod 24) are covered by a single
modular-equation family (es_families) whose modulus divides L.

Domain: residues p mod L with p = 1 (mod 24), gcd(p, L) = 1, stored as a numpy
boolean array with one axis per prime-power component of L.
"""
import numpy as np
from math import gcd
from itertools import product
from es_families import factor, families_dividing

S840 = [1, 121, 169, 289, 361, 529]


class Domain:
    def __init__(self, L):
        assert L % 24 == 0
        self.L = L
        self.fL = factor(L)
        self.primes = sorted(self.fL)
        self.axes = []   # list of (prime, prime power, values)
        for q in self.primes:
            e = self.fL[q]
            qe = q ** e
            if q == 2:
                vals = [v for v in range(qe) if v % 8 == 1]
            elif q == 3:
                vals = [v for v in range(qe) if v % 3 == 1]
            else:
                vals = [v for v in range(qe) if v % q]
            self.axes.append((q, qe, vals))
        self.shape = tuple(len(a[2]) for a in self.axes)
        self.index = [{v: i for i, v in enumerate(a[2])} for a in self.axes]
        self.cov = np.zeros(self.shape, dtype=bool)
        self.boxes = set()
        self.provenance = {}

    def box_for(self, m, residues):
        """list of boxes (tuples of index tuples) for the class 'p = r mod m, r in residues'."""
        boxes = []
        for r in residues:
            idx = []
            ok = True
            for (q, qe, vals) in self.axes:
                k = 0
                mm = m
                while mm % q == 0:
                    mm //= q
                    k += 1
                if k == 0:
                    idx.append(tuple(range(len(vals))))
                    continue
                qk = q ** k
                allowed = tuple(i for i, v in enumerate(vals) if (v - r) % qk == 0)
                if not allowed:
                    ok = False
                    break
                idx.append(allowed)
            if ok:
                boxes.append(tuple(idx))
        return boxes

    def add_families(self, fams, record=True):
        n = 0
        for (tag, par, m, rs) in fams:
            if self.L % m:
                continue
            for b in self.box_for(m, rs):
                if b in self.boxes:
                    continue
                self.boxes.add(b)
                if record:
                    self.provenance[b] = (tag, par, m)
                self.cov[np.ix_(*b)] = True
                n += 1
        return n

    def coord(self, p):
        return tuple(self.index[i][p % a[1]] for i, a in enumerate(self.axes))

    def fiber_mask(self, fixed):
        """fixed: dict prime -> residue mod that prime's full power in L (or mod the prime for q>=5).
        Returns boolean index of the fiber."""
        idx = []
        for i, (q, qe, vals) in enumerate(self.axes):
            if q in fixed:
                r, mod = fixed[q]
                idx.append([j for j, v in enumerate(vals) if (v - r) % mod == 0])
            else:
                idx.append(list(range(len(vals))))
        return idx

    def fiber_covered(self, fixed):
        idx = self.fiber_mask(fixed)
        sub = self.cov[np.ix_(*idx)]
        return bool(sub.all()), int(sub.sum()), int(sub.size)


def s840_coords(s):
    """(residue mod 8, mod 3, mod 5, mod 7) constraints for s in S840"""
    return {2: (s % 8, 8), 3: (s % 3, 3), 5: (s % 5, 5), 7: (s % 7, 7)}


def is_qr(r, q):
    r %= q
    return r != 0 and pow(r, (q - 1) // 2, q) == 1
