#!/usr/bin/env python3
"""Referee 23: what the published Hercher (2023) + Barina (2025) statement gives, compared with Corollary 2.9.
Hercher, J. Integer Seq. 26 (2023) 23.3.5, abstract: to raise the number of odd members of a nontrivial cycle to
K >= 1.375e11 it suffices that every n <= 1536*2^60 = 3*2^69 enters the trivial cycle.
Barina, J. Supercomput. 81 (2025) 810, Sec. 6: all n < 2^71 verified; 'the length of a non-trivial cycle rises to
355 504 839 929 [Hercher 2023]'."""
import mpmath as mp
from fractions import Fraction as Fr
mp.mp.dps = 80
L3 = mp.log(3, 2)
p_next, q_next = 217976794617, 137528045312       # next upper best approximation after 114208327604/72057431991
print("Hercher's K ~ 1.375e11 ->", q_next, "; 1.375e11 <= q_next < 1.376e11:", 1.375e11 <= q_next < 1.376e11)
print("A + m for the next fraction:", p_next + q_next, "(Barina 2025 Sec. 6: 355 504 839 929)", p_next + q_next == 355504839929)
print("q_next * log2 3 =", mp.nstr(q_next * L3, 25), "-> A >= ", p_next)
s71 = mp.mpf(2) ** 71
kb = q_next * (2 - mp.log(3 + 1 / s71, 2))
print("k >= m(2 - log2(3+2^-71)) with m >= q_next:", mp.nstr(kb, 20), "-> k >=", int(mp.ceil(kb)))
print("verification range Hercher needs: 3*2^69 =", 3 * 2**69, "= 2^%.4f" % float(mp.log(3 * mp.mpf(2)**69, 2)), "; Barina 2^71 = 2^71 > 3*2^69:", 2**71 > 3 * 2**69)
s_hi = 1 / (mp.power(2, mp.mpf(114208327604) / 72057431991) - 3)
print("range the plain Eliahou argument needs for the next fraction: s > s_hi =", mp.nstr(s_hi, 8), "= 2^%s" % mp.nstr(mp.log(s_hi, 2), 7))
print("ratio of published length bound to the reader's 186,265,759,595:", mp.nstr(mp.mpf(355504839929) / 186265759595, 6))
