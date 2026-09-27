# Group barrier: shell a (R=4a-p, gcd(R,pa)=1) is unoccupied if -1 is not in H=<4, q : q|a> in (Z/R)^x.
from sympy import primerange, divisors, factorint, jacobi_symbol, isprime
def occupied(p, a):
    R = 4*a - p
    return any((4*u+1) % R == 0 or (u+a) % R == 0 for u in divisors(a*a))
def subgroup(gens, R):
    H = {1 % R}; frontier = [1 % R]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = x*g % R
            if y not in H: H.add(y); frontier.append(y)
    return H
def jacobi_div_barrier(p, a, R):
    # Jacobi barrier at some divisor D = 3 mod 4 of R
    qs = list(factorint(a))
    for D in divisors(R):
        if D % 4 == 3 and all(jacobi_symbol(q, D) == 1 for q in qs):
            return True
    return False
n_shell = n_group = n_jac = n_jacdiv = viol = 0; examples = []
for p in primerange(3, 1500):
    for a in range(p//4 + 1, p):
        R = 4*a - p
        if R == 1: continue
        n_shell += 1
        qs = list(factorint(a))
        H = subgroup([4 % R] + [q % R for q in qs], R)
        gb = (R - 1) not in H
        jb = (R % 4 == 3) and all(jacobi_symbol(q, R) == 1 for q in qs)
        jd = jacobi_div_barrier(p, a, R)
        occ = occupied(p, a)
        if gb and occ: viol += 1
        if jb and not gb: viol += 1        # Jacobi barrier must be a special case
        n_group += gb; n_jac += jb; n_jacdiv += jd
        if gb and not jd and len(examples) < 5: examples.append((p, a, R, qs))
print("shells (odd p<1500, p/4<a<p, R>1):", n_shell, "; group barrier applies:", n_group,
      "; Jacobi (at R) applies:", n_jac, "; Jacobi at some divisor D=3 mod 4:", n_jacdiv, "; violations:", viol)
print("group barrier but no divisor-Jacobi barrier, first examples (p,a,R,primes of a):", examples)
p, a = 461, 128; R = 4*a - p
print("p=461 prime:", isprime(461), " a=128 R=", R, " (2/51)=", jacobi_symbol(2, 51), " (2/3)=", jacobi_symbol(2, 3),
      " <2> mod 51 =", sorted(subgroup([2, 4], 51)), " occupied:", occupied(461, 128))
