"""Exact bounded coefficient checks for the DIP source-scope audit.

Counts multiset weights in Sym^d(Sym^n(C^3)) with Python integers.
No numerical approximations, randomization, external package, or Lean.
It does not verify Chow ranks or the all-degrees semigroup certificate.
"""
import itertools
import json
from pathlib import Path


def sign(perm):
    return (-1) ** sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))


def plethysm_three_rows(d, n, lam):
    assert len(lam) == 3 and sum(lam) == d * n
    assert lam[0] >= lam[1] >= lam[2] >= 0
    delta = (2, 1, 0)
    targets = [tuple(lam[i] + delta[i] - p[i] for i in range(3))
               for p in itertools.permutations(delta)]
    bound_b = max(t[1] for t in targets)
    bound_c = max(t[2] for t in targets)
    # Each factor is (1-t*x1^(n-b-c)*x2^b*x3^c)^(-1).
    states = {(0, 0, 0): 1}
    for b in range(n + 1):
        for c in range(n - b + 1):
            next_states = {}
            for (count, wb, wc), value in states.items():
                for q in range(d - count + 1):
                    kb, kc = wb + q * b, wc + q * c
                    if kb > bound_b or kc > bound_c:
                        break
                    key = (count + q, kb, kc)
                    next_states[key] = next_states.get(key, 0) + value
            states = next_states
    summands = []
    result = 0
    for p, target in zip(itertools.permutations(delta), targets):
        value = states.get((d, target[1], target[2]), 0) if min(target) >= 0 else 0
        # delta has odd reversal, so its permutation's sign relative to
        # delta is the opposite of sign(p) relative to (0,1,2).
        epsilon = -sign(p)
        result += epsilon * value
        summands.append({"delta_permutation": p, "target_weight": target,
                         "sign": epsilon, "weight_multiplicity": value})
    return {"outer_degree_d": d, "inner_degree_n": n, "partition": lam,
            "coefficient": result, "alternant_summands": summands}


def main():
    cases = []
    for n in range(2, 21):
        lam = (n * n - 2, n, 2)
        forward = plethysm_three_rows(n + 1, n, lam)
        reverse = plethysm_three_rows(n, n + 1, lam)
        assert forward["coefficient"] == reverse["coefficient"] + 1
        cases.append({"n": n, "forward": forward, "reverse": reverse,
                      "difference": forward["coefficient"] - reverse["coefficient"]})
    assert cases[4]["forward"]["coefficient"] == 8
    assert cases[4]["reverse"]["coefficient"] == 7
    assert cases[5]["forward"]["coefficient"] == 11
    assert cases[5]["reverse"]["coefficient"] == 10
    receipt = {"status": "passed", "arithmetic": "exact Python integers",
               "scope": "19 finite plethysm coefficient pairs; no Chow-rank or infinite-family proof",
               "cases": cases}
    Path(__file__).with_name("plethysm_check_results.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "cases": len(cases),
                      "n6": [cases[4]["reverse"]["coefficient"], cases[4]["forward"]["coefficient"]],
                      "n7": [cases[5]["reverse"]["coefficient"], cases[5]["forward"]["coefficient"]]}))


if __name__ == "__main__":
    main()
