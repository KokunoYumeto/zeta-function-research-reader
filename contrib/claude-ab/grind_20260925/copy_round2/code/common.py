import numpy as np
from scipy.special import ndtr  # standard normal CDF (real)
import mpmath as mp

SP = 'data/'

def load_zeros(files=('zeros_A.npz', 'zeros_B.npz')):
    G, ZP, Z1 = [], [], []
    for f in files:
        d = np.load(SP + f)
        G.append(d['gamma']); ZP.append(d['zp']); Z1.append(d['z1'])
    g = np.concatenate(G); zp = np.concatenate(ZP); z1 = np.concatenate(Z1)
    assert np.all(np.diff(g) > 0)
    rho = 0.5 + 1j * g
    c = rho * z1 / zp          # velocity c_1(rho) = rho zeta(rho+1)/zeta'(rho)
    return g, zp, z1, c

def sieve_coeffs(N):
    """b(n) = prod_{p|n}(1-p)/n  (coeffs of zeta(s+1)/zeta(s));
       e(n) = phi(n)/n = prod_{p|n}(1-1/p) (coeffs of zeta(s)/zeta(s+1))."""
    prodb = np.ones(N + 1); prode = np.ones(N + 1)
    isp = np.ones(N + 1, bool); isp[:2] = False
    for p in range(2, N + 1):
        if isp[p]:
            isp[2 * p::p] = False
            prodb[p::p] *= (1 - p)
            prode[p::p] *= (1 - 1.0 / p)
    n = np.arange(N + 1, dtype=float); n[0] = 1
    b = prodb / n; e = prode.copy()
    b[0] = 0; e[0] = 0
    return b, e

def M(T):
    """smooth main term T/(4 pi) + i (T^2/(4 pi) - T)"""
    return T / (4 * np.pi) + 1j * (T**2 / (4 * np.pi) - T)

def h_window(u, T1, T2, D):
    return ndtr((u - T1) / D) - ndtr((u - T2) / D)

def explicit_rhs(T1, T2, D, Nmax=None):
    """Right-hand side of the explicit formula for sum_rho c(rho) h(gamma), with
       h = 1_[T1,T2] * gaussian_D, valid up to terms O(exp(-T1^2/(2D^2))) and O(exp(-pi T1))."""
    if Nmax is None:
        Nmax = int(min(np.exp(10.5 / D), 3e6)) + 10
    b, e = sieve_coeffs(Nmax)
    n = np.arange(2, Nmax + 1, dtype=float); xi = np.log(n)
    gh = np.exp(-D**2 * xi**2 / 2)
    E0 = (np.exp(-1j * T1 * xi) - np.exp(-1j * T2 * xi)) / (1j * xi)
    E1 = (T1 * np.exp(-1j * T1 * xi) - T2 * np.exp(-1j * T2 * xi)) / (1j * xi) + E0 / (1j * xi)
    h1 = gh * ((0.5 + D**2 * xi) * E0 + 1j * E1) / (2 * np.pi)
    PR = np.sum(b[2:] * n**-0.5 * h1)
    LB = -np.sum(e[2:] * n**0.5 * gh * (n**(1j * T2) - n**(1j * T1)) / xi)
    main = (T2 - T1) / (4 * np.pi) + 1j * (T2**2 - T1**2) / (4 * np.pi) - 1j * (T2 - T1)
    return main, PR, LB

def Dcal(T, D, Nmax=None):
    """ D_Delta(T) = sum_{n>=2} b(n) n^{-1/2 - iT} exp(-D^2 log^2 n /2)/log n """
    if Nmax is None:
        Nmax = int(min(np.exp(10.5 / D), 3e6)) + 10
    b, e = sieve_coeffs(Nmax)
    n = np.arange(2, Nmax + 1, dtype=float); xi = np.log(n)
    w = b[2:] * n**-0.5 * np.exp(-D**2 * xi**2 / 2) / xi
    T = np.atleast_1d(T)
    return np.array([np.sum(w * np.exp(-1j * t * xi)) for t in T])
