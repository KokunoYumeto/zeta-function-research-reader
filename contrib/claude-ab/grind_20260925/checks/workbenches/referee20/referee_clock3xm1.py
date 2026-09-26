from fractions import Fraction as Fr
X, K = 50000, 4
def orbit_min(n):
    seen = set(); x = n; mn = n
    while x not in seen:
        seen.add(x); mn = min(mn, x)
        x = x//2 if x % 2 == 0 else 3*x - 1
    return mn
def S_min(m):   # odd orbit of the shortened 3x-1 map
    seen = set(); x = m; mn = m
    while x not in seen:
        seen.add(x); mn = min(mn, x)
        y = 3*x - 1
        while y % 2 == 0: y //= 2
        x = y
    return mn
lhs = sum(1.0/n for n in range(1, X + 1) if orbit_min(n) > K)
rhs = 0.0; a = 0
while 2**a <= X:
    rhs += 2.0**(-a) * sum(1.0/m for m in range(1, X//2**a + 1, 2) if S_min(m) > K); a += 1
print(f"3x-1 clock identity at X={X}, K={K}: LHS={lhs:.4f} RHS={rhs:.4f}")
