"""Actual source coefficient at an independently re-isolated Xi zero.

No search and no RH assumption. Reuse the hash-pinned infinite theta integral,
not tabulated zero values. Its full tail bound is added on every call.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sys
from resource_ceiling import install_memory_ceiling

RESOURCE = install_memory_ceiling()
import verify_newman_heat as heat
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
ctx.prec = 256
ctx.threads = 1

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    original = HERE / 'newman_heat_results.json'
    old_hash = sha(original)
    saved = json.loads(original.read_text(encoding='utf-8'))
    assert sha(HERE/'verify_newman_heat.py') == saved['script_sha256']
    row = next(r for r in saved['root_certificates'] if r['t_exact']=='0')
    left, right = Fraction(row['left_exact']), Fraction(row['right_exact'])
    lval, _ = heat.heat(arb(0), heat.scalar(left))
    rval, _ = heat.heat(arb(0), heat.scalar(right))
    assert lval > 0 and rval < 0
    hbox = heat.scalar((left+right)/2)+arb(0,heat.scalar((right-left)/2).upper())
    hd, _ = heat.heat(arb(0), hbox, 1, True)
    assert hd < 0
    gamma = hbox/2
    # Xi(s)=8 H_0(2s), Xi'(s)=16 H'_0(2s).
    shifts = [Fraction(3),Fraction(9,2),Fraction(13,2)]
    values = []
    for shift in shifts:
        v,_ = heat.heat(arb(0),2*(gamma+heat.scalar(shift)),0,True)
        values.append(8*v)
    shifted_derivative,_ = heat.heat(arb(0),2*(gamma+3),1,True)
    shifted_derivative *= 16
    c0,c1,c2 = (heat.scalar(q) for q in
                 [Fraction(-59,275184),Fraction(1,1296),Fraction(3,132496)])
    value = c0*values[0]-shifted_derivative/336+c1*values[1]+c2*values[2]
    assert not value.contains(0)
    derivative = 16*hd
    # Residue of (T_D Xi)(s)/Xi(s) at the unique exact gamma.
    ratio_residue = value/derivative
    assert not ratio_residue.contains(0)
    assert sha(original)==old_hash
    result={
        'schema_version':1,'status':'pass','resource':RESOURCE,
        'script_sha256':sha(Path(__file__)),
        'dependencies':{n:sha(HERE/n) for n in
          ['verify_newman_heat.py','newman_heat_results.json','resource_ceiling.py']},
        'precision_bits':256,'threads':1,
        'root_interval_s_exact':[str(left/2),str(right/2)],
        'H_endpoint_balls':[str(lval),str(rval)],
        'Xi_prime_on_root_interval':str(derivative),
        'unique_simple_real_Xi_zero':True,
        'Xi_at_gamma_plus_shifts':dict(zip(map(str,shifts),map(str,values))),
        'Xi_prime_at_gamma_plus_3':str(shifted_derivative),
        'source_coefficient_TD_Xi_at_gamma':str(value),
        'residue_TD_Xi_over_Xi_at_gamma':str(ratio_residue),
        'theta_n_tail':str(heat.NTAIL),'theta_u_tail':str(heat.UTAIL),
        'source_receipt_unchanged':True,
        'mathematical_scope':'Actual nonzero simple pole of TD(Xi)/Xi at a certified on-critical-line zero; not an off-critical zero or negative Weil value.',
        'RH_counterexample':False,
    }
    if '--write' in sys.argv:
        (HERE/'xi4_trace_pole_results.json').write_text(
            json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
