"""Exact supplementary checks for SH15--39; no rendering or external packages."""
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
import random
import re

ROOT = Path(__file__).resolve().parent
source = (ROOT / "SEMILATTICE_HEAT_ZERO.tex").read_text(encoding="utf-8")
stack = []
for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", source):
    kind, env = match.groups()
    if kind == "begin":
        stack.append(env)
    else:
        assert stack and stack.pop() == env, (match.start(), env)
assert not stack
labels = re.findall(r"\\label\{([^}]+)\}", source)
refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", source)
tags = re.findall(r"\\tag\{([^}]+)\}", source)
assert len(labels) == len(set(labels))
assert set(refs) <= set(labels)
assert len(tags) == len(set(tags))
assert len(re.findall(r"(?<!\\)\\\[", source)) == len(re.findall(r"(?<!\\)\\\]", source))
assert not re.search(r"(?<!\\)\b(?:qquad|quad)\b", source)
assert not [c for c in source if ord(c) < 32 and c not in "\n\r\t"]
balance = 0
for pos, char in enumerate(source):
    if char in "{}" and (pos == 0 or source[pos - 1] != "\\"):
        balance += 1 if char == "{" else -1
        assert balance >= 0
assert balance == 0

# Entire two-generator Boolean lattice, not a single support branch.
prime = 5
top = 3
elements = [(0, label) for label in range(4)] + [(a, top) for a in range(1, prime)]

def add(x, y):
    return ((x[0] + y[0]) % prime, x[1] | y[1])

def mul(x, y):
    return ((x[0] * y[0]) % prime, x[1] & y[1])

count = 0
for x, y, z in product(elements, repeat=3):
    assert mul(x, add(y, z)) == add(mul(x, y), mul(x, z))
    count += 1
for x in elements:
    inverse = ((-x[0]) % prime, x[1])
    assert add(x, inverse) == (0, x[1])
    assert mul((0, top), x) == (0, x[1])
    count += 2
    dagger = (pow(x[0], -1, prime), top) if x[0] else x
    assert mul(mul(x, dagger), x) == x
    assert mul(mul(dagger, x), dagger) == dagger
    candidates = [y for y in elements
                  if mul(mul(x, y), x) == x and mul(mul(y, x), y) == y]
    assert candidates == [dagger]
    count += 3

TM, ZN = 3, 10
zero = (0, 0)
indices = list(product(range(TM + 1), range(ZN + 1)))

def heat(x, sign):
    result = {}
    for m, n in indices:
        value = zero
        for j in range(m + 1):
            k = sign**j * factorial(n + 2*j) // (factorial(n) * factorial(j))
            value = add(value, mul((k % prime, top), x.get((m-j, n+2*j), zero)))
        result[m, n] = value
    return result

def closure(x):
    result = {}
    for m, n in indices:
        label = 0
        for j in range(m + 1):
            label |= x.get((m-j, n+2*j), zero)[1]
        result[m, n] = (x.get((m, n), zero)[0], label)
    return result

rng = random.Random(23092026)
for _ in range(100):
    x = {index: rng.choice(elements) for index in indices}
    c = closure(x)
    hp, hm = heat(x, 1), heat(x, -1)
    assert heat(hp, -1) == c
    assert heat(hm, 1) == c
    assert closure(c) == c
    assert heat(c, 1) == hp
    assert closure(hp) == hp
    count += 5
    for n in range(ZN + 1):
        assert hp[0, n] == x[0, n] == hm[0, n] == c[0, n]
        count += 1
x = {(0, 2): (1, top)}
c = closure(x)
assert c[0, 2] == (1, top) and c[1, 0] == (0, top)
assert all(value == zero for index, value in c.items() if index not in {(0, 2), (1, 0)})
count += 1

# Integral composition identity, checked before reduction modulo any ring.
for n in range(15):
    for k in range(12):
        lhs = sum(Fraction((-1)**j * factorial(n+2*k),
                           factorial(n)*factorial(j)*factorial(k-j))
                  for j in range(k+1))
        assert lhs == (1 if k == 0 else 0)
        assert Fraction(factorial(n+2*k), factorial(n)*factorial(k)).denominator == 1
        count += 2

print({"source_lines": len(source.splitlines()), "equation_tags": len(tags),
       "static_checks": "passed", "exact_supplementary_checks": count})
