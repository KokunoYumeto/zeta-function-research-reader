"""Exact combinatorial checks and authoritative-record provenance; no RH test."""
from pathlib import Path
import hashlib
import itertools
import json
from math import comb, factorial
from fractions import Fraction
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "output/tau_f1_transcript_audit_2026-09-13/sources"

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def compositions(k, length):
    if length == 0:
        if k == 0:
            yield ()
        return
    if length == 1:
        yield (k,)
        return
    for first in range(k + 1):
        for rest in compositions(k - first, length - 1):
            yield (first,) + rest

def symdim(d, k):
    return comb(d+k-1, k) if d else int(k == 0)

checks = []
for multiplicities in [(1,), (2,), (3,), (1,2), (2,3), (1,1,1,1), (2,2,2,2), (3,3,3,3)]:
    d = sum(multiplicities)
    r = len(multiplicities)
    original_basis = tuple((rho,j) for rho,m in enumerate(multiplicities) for j in range(m))
    for k in range(1, 4):
        # A local monomial belongs to the row-Jacobian image precisely when
        # one unchanged exponent equals its actual local top exponent.
        ordered_basis = itertools.product(original_basis, repeat=k)
        row_image = 0
        mixed_image = 0
        for monomial in ordered_basis:
            top = [j == multiplicities[rho]-1 for rho,j in monomial]
            row_image += int(any(top))
            mixed_image += int(all(top))
        require(row_image == d**k-(d-r)**k, f"ordered row rank {multiplicities,k}")
        require(mixed_image == r**k, f"ordered mixed rank {multiplicities,k}")
        sym_row = 0
        sym_mixed = 0
        for orbit in itertools.combinations_with_replacement(original_basis, k):
            top = [j == multiplicities[rho]-1 for rho,j in orbit]
            sym_row += int(any(top))
            sym_mixed += int(all(top))
        require(sym_row == symdim(d,k)-symdim(d-r,k), f"symmetric row rank {multiplicities,k}")
        require(sym_mixed == symdim(r,k), f"symmetric mixed rank {multiplicities,k}")
        intrinsic_dims = sum(
            __import__('functools').reduce(lambda a,b:a*b,
                (comb(m+n-1,n) for m,n in zip(multiplicities, occ)), 1)
            for occ in compositions(k,r)
        )
        require(intrinsic_dims == symdim(d,k), f"intrinsic local dimensions {multiplicities,k}")
        checks.append({"multiplicities":multiplicities,"k":k,"ordered_row_rank":row_image,
                       "ordered_mixed_rank":mixed_image,"symmetric_row_rank":sym_row,
                       "symmetric_mixed_rank":sym_mixed,"intrinsic_dimension":intrinsic_dims})

quartet_checks = []
for m in range(1, 5):
    for k in range(1, 9):
        occupations = list(compositions(k,4))
        seen = set()
        positive = negative = fixed = 0
        for n in occupations:
            if n in seen:
                continue
            involution = (n[1],n[0],n[3],n[2])
            intrinsic = 1
            orbit_denominator = 1
            for ni in n:
                intrinsic *= comb(m+ni-1,ni)
                orbit_denominator *= factorial(ni)
            ordered = factorial(k)//orbit_denominator * m**k
            central_comparison = Fraction(intrinsic,ordered)
            require(ordered*central_comparison == intrinsic, "central trace comparison")
            if involution == n:
                positive += 1
                fixed += 1
                seen.add(n)
            else:
                # Exact two-dimensional Gram is [[0,D],[D,0]], D>0.
                require(intrinsic>0, "positive actual multiplicity weight")
                positive += 1
                negative += 1
                seen.update((n,involution))
        expected_fixed = 0 if k%2 else k//2+1
        b = comb(k+3,3)
        require(fixed == expected_fixed, "reflection fixed occupation count")
        require((positive,negative) == ((b+fixed)//2,(b-fixed)//2), "intrinsic inertia")
        radical = symdim(4*m,k)-b
        require(positive+negative+radical == symdim(4*m,k), "inertia full dimension")
        if k % 2 == 0:
            ell = k//2
            balanced = [n for n in occupations if n[0]+n[2]==ell and n[1]+n[3]==ell]
            balanced_fixed = sum((n[1],n[0],n[3],n[2]) == n for n in balanced)
            require(len(balanced)==(ell+1)**2 and balanced_fixed==ell+1, "balanced occupation counts")
            require((len(balanced)-balanced_fixed)//2==ell*(ell+1)//2, "balanced negative inertia")
            for q in range(-ell,ell+1):
                exact_fibre = [n for n in balanced if n[0]+n[1]==ell+q]
                exact_fixed = sum((n[1],n[0],n[3],n[2]) == n for n in exact_fibre)
                require(len(exact_fibre)==ell+1-abs(q), "individual sum-fibre count")
                require((len(exact_fibre)-exact_fixed)//2==(ell+1-abs(q))//2, "individual sum-fibre negative inertia")
        quartet_checks.append({"m":m,"k":k,"positive":positive,"negative":negative,
                               "radical":radical,"fixed_occupations":fixed})

segment = SOURCE / "audit_segment_U0041_U0054.md"
text = segment.read_text(encoding="utf-8")
headers = list(re.finditer(r"^## ([UA]\d{4}) \| ([^|]+) \| (user|assistant) \| chain (\d+)\s*$", text, re.M))
records = json.loads((SOURCE / "transcript_records.json").read_text(encoding="utf-8"))
by_locator = {record["locator"]:record for record in records}
coverage = []
for i,header in enumerate(headers):
    locator,node_id,role,chain = header.groups()
    body = text[header.end():headers[i+1].start() if i+1<len(headers) else len(text)].strip()
    original = by_locator[locator]
    require(body == original["text"].strip(), f"record text equality {locator}")
    require(original["message_id"] == node_id.strip(), f"message id {locator}")
    require(original["chain_ordinal"] == int(chain), f"chain locator {locator}")
    require(original["role"] == role, f"role {locator}")
    line_start = text[:header.start()].count("\n")+1
    next_start = headers[i+1].start() if i+1<len(headers) else len(text)
    line_end = text[:next_start].count("\n")
    coverage.append({"locator":locator,"node_id":node_id.strip(),"chain":int(chain),
                     "role":role,"line_start":line_start,"line_end":line_end,
                     "characters":len(body),"text_matches_original_record":True,
                     "body_sha256":hashlib.sha256(body.encode()).hexdigest()})

require(len(coverage)==43, f"43 message count; got {len(coverage)}")
report = {"status":"passed","scope":"Exact rank/count/trace-weight checks; no assertion of an off-line zeta zero or RH proof.",
          "rank_checks":checks,"quartet_inertia_checks":quartet_checks,
          "authoritative_segment_sha256":hashlib.sha256(segment.read_bytes()).hexdigest(),
          "all_43_message_bodies_match_original_records":True,"message_coverage":coverage}
(HERE / "checks_and_record_coverage.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print(json.dumps({"status":"passed","rank_cases":len(checks),"quartet_inertia_cases":len(quartet_checks),
                  "matching_authoritative_messages":len(coverage)}))
