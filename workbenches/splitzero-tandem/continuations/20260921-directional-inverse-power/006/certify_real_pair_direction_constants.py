"""Propagate the certified original root enclosure to its real tangent map."""
from pathlib import Path
import json, hashlib
from flint import arb, acb, arb_mat, ctx

ROOT = Path(__file__).resolve().parent.parent
ctx.prec = 256
source = ROOT/'REAL_PAIR_CERTIFICATE.json'
cert = json.loads(source.read_text(encoding='utf-8'))
assert cert['status'] == 'CERTIFIED' and all(cert['checks'].values())
assert cert['script_sha256'] == hashlib.sha256((ROOT/'certify_real_pair.py').read_bytes()).hexdigest()
def complex_ball(s):
    if s == '0': return acb(0)
    real, imag = s[:-1].rsplit(' + ', 1)
    return acb(arb(real), arb(imag))
P = arb_mat([[arb(v) for v in row] for row in cert['exact_dyadic_preconditioner']])
E = arb_mat([[arb(v) for v in row] for row in cert['jacobian_defect']])
J = P.inv()*(arb_mat([[1,0],[0,1]])-E)
f2 = complex_ball(cert['all_original_factor_jets'][1][0])
A = complex_ball(cert['G_z'])
C = f2*acb(J[0,1],J[1,1])
B = complex_ball(cert['G_xi'])
L = arb_mat([[A.real,C.real],[A.imag,C.imag]])
det = L.det()
assert not det.contains(0)
Li = L.inv()
H = L.transpose()*L
assert H[0,0] > 0 and H.det() > 0
rays = []
for k in range(1,4):
    angle = arb.pi()*k/4
    target = B*acb(angle.cos(),angle.sin())
    v = Li*arb_mat([[target.real],[target.imag]])
    rays.append({'D':3,'k':k,'definition':'Lambda^{-1}(B exp(i*k*pi/4))',
                 'v_z':v[0,0].str(35),'v_x':v[1,0].str(35),
                 'target_real':target.real.str(35),'target_imag':target.imag.str(35)})
out = {'status':'CERTIFIED','source_certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Interval propagation at the unique certified real pair, using its original Jacobian enclosure. No new series evaluation or arithmetic zeta identification.',
 'Jacobian_recovery':'DF=P^{-1}(I-E); G_x=f2*(DF_01+i*DF_11) at f1=0.',
 'G_z':str(A),'G_x':str(C),'G_xi':str(B),
 'Lambda_determinant':det.str(35),
 'quadratic_form_matrix':[[H[i,j].str(35) for j in range(2)] for i in range(2)],
 'quadratic_form_determinant':H.det().str(35),
 'degree3_resonance_line_vectors':rays,
 'original_coordinate_rule':'z=z*+tau*v_z, x=x*+tau*v_x, a=alpha*(1+i*x); u=1/z exactly. Vectors represent unoriented lines; neither source coordinate is discarded.'}
(ROOT/'independent/REAL_PAIR_DIRECTION_CONSTANTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
