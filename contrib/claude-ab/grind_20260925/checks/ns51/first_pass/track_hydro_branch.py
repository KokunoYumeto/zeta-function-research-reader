"""Numerical (non-rigorous) continuation of the hydrodynamic zero alpha(q) of F(alpha,q) = I'_alpha(q)
from q = 0.05 (series start) to just below the certified collision q* ~ 0.7784728; supplements
certify_collision.py, which certifies the double zero but not which branches meet there."""
import mpmath as mp
mp.mp.dps = 40
F = lambda a, q: (mp.besseli(a - 1, q) + mp.besseli(a + 1, q))/2
ser = lambda q: -q**2/2 - 3*q**4/16 - 29*q**6/192 - mp.mpf(2843)*q**8/18432 - mp.mpf(392029)*q**10/2211840
qc = mp.mpf('0.778472800990330076180356446189'); ac = mp.mpf('-0.569714080972361784438457668663')
q = mp.mpf('0.05'); a = mp.findroot(lambda x: F(x, q), ser(q))
path = []
steps = 0
while q < qc - mp.mpf('1e-6'):
    dq = min(mp.mpf('0.002'), (qc - q)/4)
    qn = q + dq
    # predictor from the local slope da/dq = -F_q/F_a
    Fa = mp.diff(lambda x: F(x, q), a); Fq = mp.diff(lambda y: F(a, y), q)
    guess = a - Fq/Fa*dq
    a = mp.findroot(lambda x: F(x, qn), guess)
    q = qn; steps += 1
    if steps % 60 == 0 or qc - q < mp.mpf('1e-4'):
        path.append((mp.nstr(q, 10), mp.nstr(a, 12)))
for p in path[-6:]:
    print("q = %s   hydrodynamic zero alpha = %s" % p)
qs = qc - mp.mpf('1e-6')
other_guess = ac - (a - ac)
b = mp.findroot(lambda x: F(x, qs), other_guess)
print("at q = q_c - 1e-6: hydrodynamic zero %s, second real zero %s, predicted +/- %s around alpha_c" % (
      mp.nstr(a, 12), mp.nstr(b, 12), mp.nstr(mp.sqrt(2*mp.mpf('1.75035806101434')*mp.mpf('1e-6')/mp.mpf('5.00598854867858')), 6)))
print("hydrodynamic branch reaches the collision from above (alpha > alpha_c):", a > ac, "; distance", mp.nstr(abs(a - ac), 6))
