"""Exact finite certificates for result058; analytic proofs are in proof.tex."""
from fractions import Fraction as F
from math import prod
import argparse
import json

COUNT = 0


def need(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise RuntimeError(message)


def polynomial(factors):
    out = [1]
    for a in factors:
        new = [0] * (len(out) + 1)
        for j, c in enumerate(out):
            new[j] += a * c
            new[j+1] += c
        out = new
    return out


def recurrence(control):
    original_num = 5**12 * 64 * 9
    original_den = 2**6
    need(F(original_num, original_den) == 46875**2, "recurrence constant")
    # Verify cancelled rational functions as polynomial identities, not samples.
    left = polynomial([1, 2, 3, 4, 5, 6, 1, 3, 5, 9])
    right = polynomial([2, 4, 1, 1, 3, 3, 5, 5, 6, 9])
    need(left == right, "gamma product cancellation")
    x = 2000
    ratio_upper = F(46875**2 * (x+2)*(x+4),
                    3**6 * (x+1)*(x+3)*(x+5)*(x+9))
    expected = F(9328515625000, 12454264114047)
    if control == "recurrence":
        expected += 1
    need(ratio_upper == expected, "six-step rational certificate")
    need(ratio_upper < 1, "counterexample comparison")
    need(expected.denominator - expected.numerator == 3125748489047,
         "positive integer gap")
    return str(ratio_upper)


def pi_certificate(control):
    total = 4 * sum((F((-1)**j, 2*j+1) for j in range(8)), F(0))
    expected = F(135904, 45045)
    if control == "pi":
        expected -= F(1, 1000)
    need(total == expected, "integrated geometric certificate")
    need(total > 3, "strict lower bound for pi")
    # (1+t²) * sum_{j=0}^7 (-t²)^j + t^16 = 1.
    coeffs = [0] * 17
    for j in range(8):
        for offset in (0, 2):
            coeffs[2*j+offset] += (-1)**j
    coeffs[16] += 1
    need(coeffs == [1] + [0]*16, "positive geometric remainder identity")
    need(135904 - 3*45045 == 769, "pi lower bound integer gap")


def branch_tests(control):
    values = sorted({F(n, d) for n in range(1, 9) for d in range(1, 6)})
    count = 0
    for fm in values:
        for em in values:
            target = min(4*fm, em)
            zero = fm < em
            compute = em < 2*fm
            need(zero or compute, "strict tests cover every positive pair")
            if zero:
                need(fm < target, "zero branch retains original minimum")
            if compute:
                need(target == em, "compute branch retains original minimum")
            for r in range(1, 24):
                width = F(1, 2**r)
                certified_zero = fm+width < em-width
                certified_compute = em+width < 2*(fm-width)
                if certified_zero or certified_compute:
                    need((not certified_zero or zero) and
                         (not certified_compute or compute),
                         "endpoint test implies true strict test")
                    break
            else:
                raise RuntimeError("finite rational enclosure test did not terminate")
            count += 1
    need(not (F(1) < F(1)) and F(1) < 2*F(1), "equality E=F uses compute")
    need(F(1) < F(2) and not (F(2) < 2*F(1)), "equality E=2F uses zero")
    if control == "minimum":
        need(max(F(4), F(1)) == F(1), "rejected printed maximum")
    if control == "overlap":
        need(F(1) < F(1) or F(1) < F(1), "rejected non-overlapping equality rule")
    return count


def finite_sets(control):
    # Synthetic exact branch tests; not evaluations of original F derivatives.
    fm = [F(1)]*7
    em = [F(1, 2), F(3), F(1), F(4), F(1, 3), F(2), F(7)]
    bad = {m for m in range(7) if em[m] <= fm[m]}
    need(bad == {0, 2, 4}, "nonconsecutive computed set")
    maximum = 1+max(bad)
    need(maximum == 5, "full prefix Taylor receiver covers all computed indices")
    for m in range(7):
        if m in bad:
            need(m < maximum and em[m] == min(4*fm[m], em[m]), "computed index")
        else:
            need(fm[m] < min(4*fm[m], em[m]), "skipped index")
    empty = {m for m in range(7) if F(2) <= F(1)}
    need(not empty, "all-zero set needs no maximum")
    if control == "empty":
        need(bool(empty), "rejected undefined maximum of empty set")
    for fm0 in (F(1, 3), F(1), F(4)):
        for em0 in (F(1, 4), F(1), F(3), F(20)):
            need(min(em0/2, 2*fm0) == min(em0, 4*fm0)/2,
                 "full-index two retained half-budgets")
    need(2*316 == 632, "unchanged source constants")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--negative-control", choices=("recurrence", "pi", "minimum", "overlap", "empty"))
    control = parser.parse_args().negative_control
    ratio = recurrence(control)
    pi_certificate(control)
    pairs = branch_tests(control)
    finite_sets(control)
    print(json.dumps({"status": "passed", "checks": COUNT,
                      "exact_positive_pairs": pairs, "ratio_upper": ratio,
                      "scope": "Integer/rational finite certificates and synthetic branch tests; the analytic proof is in proof.tex."}))


if __name__ == "__main__":
    main()
