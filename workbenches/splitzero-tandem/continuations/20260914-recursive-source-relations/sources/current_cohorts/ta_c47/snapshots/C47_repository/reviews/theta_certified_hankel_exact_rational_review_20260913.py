"""Independent exact-integer interval replay of the theta certificate.

No flint import, floating-point arithmetic, zero ordinates, or rescaling.
The finite integral pieces and proved tail upper bounds are external inputs;
every subsequent rounding, coefficient recurrence, and LDL sign uses integers.
"""
from __future__ import annotations
import hashlib
import json
import math
import sys
from pathlib import Path
from fractions import Fraction

sys.set_int_max_str_digits(100000)
BASE = Path(__file__).resolve().parent
DIR = BASE / "theta_certified_hankel_20260913"
INPUT = DIR / "certificate_dimension16_1024.json"
REPLAY = DIR / "reviewer_replay_dimension16_1024.json"
OUTPUT = BASE / "theta_certified_hankel_exact_rational_review_20260913.json"
BITS = 4096
Q = 1 << BITS


def read_fraction(d):
    a, b = int(d["numerator"]), int(d["denominator"])
    assert b > 0 and (b & (b - 1)) == 0
    return Fraction(a, b)


def endpoints(d):
    lo, hi = read_fraction(d["lower"]), read_fraction(d["upper"])
    assert lo <= hi
    return lo, hi


def ceildiv(a, b):
    assert b > 0
    return -((-a) // b)


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo, self.hi = lo, lo if hi is None else hi
        assert self.lo <= self.hi

    @staticmethod
    def integer(n):
        return Interval(n * Q)

    @staticmethod
    def from_fractions(lo, hi):
        assert lo <= hi
        return Interval((lo.numerator * Q) // lo.denominator,
                        ceildiv(hi.numerator * Q, hi.denominator))

    @staticmethod
    def exported(d):
        return Interval.from_fractions(*endpoints(d))

    def __add__(self, other):
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return Interval(min(products) // Q, ceildiv(max(products), Q))

    def square(self):
        high = max(self.lo**2, self.hi**2)
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return Interval(low // Q, ceildiv(high, Q))

    def reciprocal(self):
        assert self.lo > 0 or self.hi < 0
        if self.hi < 0:
            return -((-self).reciprocal())
        return Interval(Q**2 // self.hi, ceildiv(Q**2, self.lo))

    def __truediv__(self, other):
        return self * other.reciprocal()

    def by_integer(self, n):
        assert n != 0
        if n < 0:
            return -self.by_integer(-n)
        return Interval(self.lo // n, ceildiv(self.hi, n))

    def times_integer(self, n):
        return Interval(min(self.lo * n, self.hi * n),
                        max(self.lo * n, self.hi * n))

    def as_fractions(self):
        return Fraction(self.lo, Q), Fraction(self.hi, Q)

    def exported_endpoints(self):
        def encode(n):
            f = Fraction(n, Q)
            return {"numerator": str(f.numerator), "denominator": str(f.denominator)}
        return {"lower": encode(self.lo), "upper": encode(self.hi)}

    def overlaps(self, d):
        lo, hi = endpoints(d)
        return Fraction(self.lo, Q) <= hi and Fraction(self.hi, Q) >= lo


def isum(items):
    out = Interval.integer(0)
    for item in items:
        out = out + item
    return out


def validate_all_endpoints(obj, counts):
    if isinstance(obj, dict):
        if "lower" in obj and "upper" in obj:
            endpoints(obj)
            counts[0] += 1
        for v in obj.values():
            validate_all_endpoints(v, counts)
    elif isinstance(obj, list):
        for v in obj:
            validate_all_endpoints(v, counts)


def pure_numeric_payload(obj):
    if isinstance(obj, dict):
        return {k: pure_numeric_payload(v) for k, v in obj.items()
                if k not in {"seconds", "platform"}}
    if isinstance(obj, list):
        return [pure_numeric_payload(v) for v in obj]
    return obj


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    replay = json.loads(REPLAY.read_text(encoding="utf-8"))
    assert data["source_sha256"] == sha(DIR / "certify_theta_hankel.py")
    assert replay["source_sha256"] == data["source_sha256"]
    assert data["status"] == replay["status"] == "positive_definite_certified"
    assert data["dimension"] == 16 and data["first_omitted_n"] == 20 and data["length"] == 4
    assert data["precision_bits"] == 1024 and data["target_bits"] == 850
    assert data["python_flint_version"] == "0.9.0"
    counts = [0]
    validate_all_endpoints(data, counts)
    validate_all_endpoints(replay, [0])
    assert len(data["moments"]) == 33 and len(data["a"]) == 33 and len(data["b"]) == 32
    moments = []
    moment_checks = []
    for index, row in enumerate(data["moments"]):
        assert row["J"] == 2 * index
        assert len(row["pieces"]) == 8
        for j, piece in enumerate(row["pieces"]):
            assert Fraction(piece["left"]) == Fraction(j, 2)
            assert Fraction(piece["right"]) == Fraction(j + 1, 2)
            lo, hi = endpoints(piece["imag"])
            assert lo <= 0 <= hi
        ilo, ihi = endpoints(row["finite_imaginary"])
        assert ilo <= 0 <= ihi
        nlo, nhi = endpoints(row["omitted_n_bound"])
        ylo, yhi = endpoints(row["omitted_y_bound"])
        dlo, dhi = endpoints(row["decay_denominator"])
        assert nlo > 0 and ylo > 0 and dlo > 0
        # Independently add exported integral pieces, then [0,T_upper+Y_upper].
        # No use of the stored finite_integral, moment, a, b, L, or pivot values.
        finite = isum(Interval.exported(p["real"]) for p in row["pieces"])
        tail = Interval.from_fractions(Fraction(0), nhi + yhi)
        moment = finite + tail
        assert moment.lo > 0
        assert finite.overlaps(row["finite_integral"])
        assert moment.overlaps(row["moment"])
        moments.append(moment)
        moment_checks.append({"J": row["J"], "moment": moment.exported_endpoints()})

    a = [m.by_integer(math.factorial(2*j)).times_integer((-1)**j)
         for j, m in enumerate(moments)]
    assert a[0].lo > 0
    b = []
    for n in range(32):
        numerator = a[n+1].times_integer(-(n+1)) - isum(a[j] * b[n-j] for j in range(1,n+1))
        b.append(numerator / a[0])
    assert all(x.overlaps(y) for x,y in zip(a,data["a"]))
    assert all(x.overlaps(y) for x,y in zip(b,data["b"]))

    matrices = {}
    for shift in (0,1):
        size = 16
        lower = [[Interval.integer(int(i == j)) for j in range(size)] for i in range(size)]
        diag = []
        determinant = Interval.integer(1)
        rows = []
        for j in range(size):
            pivot = b[2*j+shift] - isum(lower[j][k].square() * diag[k] for k in range(j))
            assert pivot.lo > 0, (shift,j,"independent pivot failed")
            diag.append(pivot)
            determinant = determinant * pivot
            assert determinant.lo > 0
            supplied = data["matrices"][str(shift)]["rows"][j]
            assert supplied["dimension"] == j+1
            assert pivot.overlaps(supplied["pivot"])
            assert determinant.overlaps(supplied["leading_determinant"])
            rows.append({"dimension": j+1, "pivot": pivot.exported_endpoints(),
                         "leading_determinant": determinant.exported_endpoints()})
            for i in range(j+1,size):
                numerator = b[i+j+shift] - isum(lower[i][k] * lower[j][k] * diag[k] for k in range(j))
                lower[i][j] = numerator / pivot
                assert lower[i][j].overlaps(data["matrices"][str(shift)]["L"][i][j])
        matrices[str(shift)] = {"positive_pivots": size, "rows": rows,
            "L": [[v.exported_endpoints() for v in row] for row in lower]}

    # Verify the literal readable interval TC28 against exact exported endpoints.
    mid = Fraction("1.9493355548191422147398782191721395e-9")
    rad = Fraction("5.60e-45")
    h1 = data["matrices"]["0"]["rows"][1]["leading_determinant"]
    h1lo,h1hi = endpoints(h1)
    display_contains_exact = mid-rad <= h1lo <= h1hi <= mid+rad
    assert display_contains_exact

    result = {"status": "positive_definite_by_independent_exact_integer_interval_recursion",
              "scope": "original H15 and shifted H15 only; no infinite-dimensional conclusion",
              "arithmetic": "Python standard-library integers and Fraction; no flint import or floating point",
              "absolute_dyadic_denominator_bits": BITS,
              "source_sha256": sha(Path(__file__)),
              "integrator_sha256": data["source_sha256"],
              "original_certificate_sha256": sha(INPUT),
              "fresh_replay_certificate_sha256": sha(REPLAY),
              "original_endpoints_validated": counts[0],
              "replay_identical_numeric_payload": pure_numeric_payload(data) == pure_numeric_payload(replay),
              "TC28_readable_interval_contains_exact_certificate": display_contains_exact,
              "moments": moment_checks,
              "a": [v.exported_endpoints() for v in a],
              "b": [v.exported_endpoints() for v in b],
              "matrices": matrices}
    OUTPUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k not in {"moments","a","b","matrices"}},indent=2))
    print("32 positive pivots and 32 positive leading determinants certified using exact integer intervals.")
    print("Output:",OUTPUT)


if __name__ == "__main__":
    main()
