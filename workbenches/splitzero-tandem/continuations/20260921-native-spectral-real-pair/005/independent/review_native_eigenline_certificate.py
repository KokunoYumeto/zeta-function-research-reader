"""Independent determinant review from stored NV balls, without xi evaluation."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import re
import flint
from flint import arb,acb,acb_mat,ctx
ctx.prec=1024;ctx.threads=1
base=Path(__file__).resolve().parent.parent
certificate=base/'ORIGINAL_NATIVE_WEIL_CERTIFICATES.json'
raw=certificate.read_bytes();data=json.loads(raw)
script_sha=hashlib.sha256((base/'certify_original_native_weil.py').read_bytes()).hexdigest()
assert script_sha==data['script_sha256']
def parse_acb(text):
 balls=re.findall(r'\[[^\[\]]*\]',text)
 if len(balls)==2:
  assert text==balls[0]+' + '+balls[1]+'j'
  return acb(arb(balls[0]),arb(balls[1]))
 if len(balls)==1:
  if text.endswith('j'):
   assert text==balls[0]+'j'
   return acb(0,arb(balls[0]))
  assert text==balls[0]
  return acb(arb(balls[0]))
 return acb(text)
def realq(x):
 x=Fraction(x)
 return arb(x.numerator)/x.denominator
def strict_inertia(A):
 signs=[1]
 for k in range(1,5):
  det=acb_mat([[A[i,j] for j in range(k)] for i in range(k)]).det()
  assert det.imag.contains(0)
  sign=1 if det.real>0 else -1 if det.real<0 else 0
  assert sign
  signs.append(sign)
 return sum(signs[j]!=signs[j-1] for j in range(1,5)),signs

reviews=[]
for record in data['rows']:
 H=acb_mat([[parse_acb(v) for v in row] for row in record['native_Gram_entries']])
 cs=[parse_acb(v) for v in record['coefficients_full_weil']]
 T=acb_mat([[cs[j-i] if j>=i else cs[i-j].conjugate() for j in range(4)] for i in range(4)])
 assert strict_inertia(H)[0]==0
 assert strict_inertia(T)[0]==0
 previous=Fraction(0);rowcheck={'tau':record['pole_imag'],'positive_native_Gram_verified_from_stored_balls':True,'positive_arithmetic_Gram_verified_from_stored_balls':True,'intervals':[]}
 for j,rec in enumerate(record['eigenvalue_intervals'],1):
  lo=Fraction(rec['lower_exact']);hi=Fraction(rec['upper_exact'])
  assert previous<lo<hi and (hi-lo)/lo<Fraction(1,10**60)
  previous=hi
  il,sl=strict_inertia(T-H*acb(realq(lo)))
  iu,su=strict_inertia(T-H*acb(realq(hi)))
  assert (il,iu)==(j-1,j)
  assert sl==rec['lower_leading_minor_signs'] and su==rec['upper_leading_minor_signs']
  box=realq((lo+hi)/2)+arb(0,realq((hi-lo)/2))
  assert box.contains(realq(lo)) and box.contains(realq(hi))
  Abox=T-H*acb(box)
  k=rec['nonzero_eigenvector_certificate']['column_zero_based'];ix=[n for n in range(4) if n!=k]
  cofactor=acb_mat([[Abox[p,q] for q in ix] for p in ix]).det()
  assert cofactor.imag.contains(0) and not cofactor.real.contains(0)
  rowcheck['intervals'].append({'index':j,'endpoint_inertias':[il,iu],'relative_width_less_than_1e_minus_60':True,'entire_box_contains_both_rational_endpoints':True,'nonzero_principal_cofactor_column':k,'independent_cofactor_ball':str(cofactor)})
 reviews.append(rowcheck)
out={'certificate_sha256':hashlib.sha256(raw).hexdigest(),'producer_script_sha256_verified':script_sha,'independent_library':'python-flint '+flint.__version__,'independent_precision_bits':ctx.prec,'method':'All 40 endpoint inertias, 160 leading-minor strict signs, 20 entire-interval cofactors, and positive H/T independently re-enclosed from stored full matrix balls. No completed-xi, zeta, Gamma or zero calculation repeated.','rows':reviews,'all_checks_passed':True}
Path(__file__).with_name('NV_INDEPENDENT_CERTIFICATE_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('Stored certificate SHA256:',out['certificate_sha256'])
print('Producer hash verified:',script_sha)
print('All 40 endpoint inertias, 160 minor signs, 20 interval cofactors, and 10 positive matrix tests independently passed.')
