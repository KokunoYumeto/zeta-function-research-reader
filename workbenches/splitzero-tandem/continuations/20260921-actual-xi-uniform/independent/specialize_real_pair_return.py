"""Rigorous propagation of the saved real-pair enclosures; no new period evaluation."""
from pathlib import Path
import json,hashlib
from flint import arb,acb,ctx
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
ctx.prec=256
cert=json.loads((ROOT/'REAL_PAIR_CERTIFICATE.json').read_text(encoding='utf-8'))
assert cert['status']=='CERTIFIED' and all(cert['checks'].values())
c=arb(cert['period_order2_coefficient_c']);b=arb(cert['half_mu2'])
R=arb(cert['mixed_first_moment_dreal']);Q=arb(cert['generic_pole_factor'])
mu2=2*b;absDelta=abs(R)*abs(Q)
z=arb(cert['z_center'])+arb(0,cert['z_radius']);u=1/z
def parse_complex(text):
    if text=='0':return acb(0)
    if text.endswith('j'):
        re,im=text[:-1].rsplit(' + ',1)
        return acb(arb(re),arb(im))
    return acb(arb(text))
moments=[parse_complex(v).real for v in cert['original_moments_0_through_5']]
f=abs(moments[3]/6-2*moments[2])
rho1=arb(2).sqrt();rho2=(arb(8)/3).sqrt();rho3=(arb(16)/5).sqrt()
S=(b*rho2)**2+(f*rho3)**2+(b*rho3/rho1)**2
P=(b*b*rho2*rho3/rho1)**2
sigma_plus=((S+(S*S-4*P).sqrt())/2).sqrt()
sigma_minus=P.sqrt()/sigma_plus
data={'mu2':mu2,'c':c,'R':R,'abs_Delta':absDelta,'u0':u,
      'inverse_rank1_without_rho3':absDelta/c**4,
      'inverse_rank2_without_rho2rho3_over_rho1':b*b/c**4,
      'inverse_rank4':1/c**4,
      'new_four_label_determinant':-arb(16)/29*mu2**4,
      's1_inverse_rank1':absDelta/c**4*(arb(16)/5).sqrt(),
      's1_inverse_rank2':b*b/c**4*8/arb(15).sqrt(),
      'mu3':moments[3],'mu4':moments[4],'mu5':moments[5],
      'abs_g3':f,'s1_forward_sigma_plus':sigma_plus,'s1_forward_sigma_minus':sigma_minus,
      's1_inverse_rank3':sigma_plus/c**4,
      's1_inverse_second_singular_constant':b*b*rho2/(absDelta*rho1),
      's1_inverse_third_singular_limit':1/sigma_minus,
      's1_inverse_fourth_singular_limit':1/sigma_plus,
      's1_original_u_rank1':u**10*absDelta/c**4*(arb(16)/5).sqrt(),
      's1_original_u_rank2':u**16*b*b/c**4*8/arb(15).sqrt(),
      's1_original_u_rank3':u**16*sigma_plus/c**4,
      'original_u_rank4':u**16/c**4}
assert mu2>0 and c>0 and absDelta>0
out={'status':'pass','source_certificate_sha256':hashlib.sha256((ROOT/'REAL_PAIR_CERTIFICATE.json').read_bytes()).hexdigest(),
     'values':{key:value.str(35) for key,value in data.items()},
     'scope':'Propagated interval enclosures from the full original real-pair certificate, including all four exterior constants and exact moments through5. No new full-series evaluation.'}
(HERE/'REAL_PAIR_RETURN_CONSTANTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2),flush=True)
