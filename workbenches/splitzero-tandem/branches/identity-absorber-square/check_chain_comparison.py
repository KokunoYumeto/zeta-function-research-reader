"""Finite basis restrictions of the exact chain-comparison examples."""
from pathlib import Path
import json
import sympy as s
vals=[-2,-1,1,2]
pairs=[(x,y) for x in range(-2,3) for y in range(-2,3) if (x,y)!=(0,0)]
pos={v:i for i,v in enumerate(pairs)}
P=s.zeros(len(pairs),len(vals))
D=s.zeros(len(vals),len(pairs))
for j,x in enumerate(vals):P[pos[(x,0)],j]=1
for j,(x,y) in enumerate(pairs):
    if y:D[vals.index(y),j]=1
assert D*P==s.zeros(len(vals),len(vals))
basis=s.zeros(len(pairs),len(vals)**2)
for j,(x,y) in enumerate((x,y) for x in vals for y in vals):
    basis[pos[(x,y)],j]=1
    basis[pos[(0,y)],j]=-1
assert D*basis==s.zeros(len(vals),len(vals)**2)
assert P.row_join(basis).rank()==len(vals)+len(vals)**2
assert len(pairs)-D.rank()-P.rank()==len(vals)**2
odd=[v for v in range(-8,9) if v%2]
image={2*v for v in range(-4,5) if v}
assert set(range(-8,9))-{0}-image==set(odd)
report={"scope":"Exact matrices on specified finite basis restrictions; infinite basis and universal claims are proved in CHAIN_COMPARISON.md.",
        "contractible_input_window":{"x":vals,"y":vals,"middle_free_rank":len(pairs),
                                    "d0_rank":P.rank(),"d1_rank":D.rank(),"extra_h1_rank":16,
                                    "proposed_classes_cycles_and_independent_mod_boundaries":True},
        "times_two_output_window":[-8,8],"times_two_odd_basis":odd,"status":"passed"}
(Path(__file__).resolve().parent/"CHAIN_CHECKS.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print(json.dumps(report,indent=2))
