"""Pin the independently read root and signed-source continuation."""
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
def pin(rel):
    p=ROOT/rel
    return {'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

out={
 'schema':'independent-root-propagation-review-v1',
 'reviewed':[pin('root/R67_R74_REVISED.tex'),pin('recursive_metric_transport.tex'),pin('incoming_pr29_metric/incoming_source_metric_control.tex')],
 'root_scope':'R67 and R72-R74 new blocks and changed nonlinear inequality; original R68-R71 retained here pending their owner overlay.',
 'accepted_checks':[
  'R67 maps V/W injectively by [v] to [Theta v]_W; its image is precisely the full-quotient kernel. Coefficient copies retain their independent carrier and mask.',
  'The tensor comparison kernel is exactly (d C_full^(k-1) intersect C_lambda^k)/d C_lambda^(k-1). The displayed class [d Ktilde_v]_lambda requires its top representative in C_lambda^k. Its vanishing criterion uses the boundary d Ktilde_v itself.',
  'The source tower has D:W_m^src to W_(m+1)^src. Full-source low one-leg tail is acyclic; proper-source tail has H1=V/W and the two-leg diagonal stays in H0.',
  'R72 canonical projector equals P_N-Q_N through the original orthogonal decomposition and its literal remainder inverse. Relation matrices and canonical lifts all map to the same original H=P_2q.',
  'Both secant formulas retain positive boundary terms: R1^*M0 R1=G0+Delta^*M0 Delta and R0^*M1 R0=G1+Delta^*M1 Delta imply the stated scaled identities.',
  'Cross-Gram Rj^*M Ri=Gj requires i<=j and yields trace(Pi_i Pi_j)=trace(Gi^-1 Gj) with that restriction explicitly retained.',
  'Centering C uses trace(A)=0 and original weighted self-adjointness; weighted Hilbert-Schmidt Cauchy-Schwarz proves the retained full cross-trace bound.',
  'RMT19 finite geometric identity gives C-C^[L]=H^(L+1)C. Original M0 and Mx weighted self-adjointness are preserved because all factors commute with D.',
  'The exact residual centering subtracts (trace R)^2/(2q+1); its integrated error is at most theta^(L+1) sqrt(K_D(8q-6)). theta<1 is proved for each fixed original pair; no uniform amplified-degree estimate is asserted.',
  'R73 minimum takes only bounds on the same signed derivative. The angle entry is restricted to the actual positive moment path; other four controls remain valid for general positive coefficient forms.',
  'H_m(B)=2 arcosh(exp(B/(2m))) has derivative 1/(m sqrt(1-exp(-B/m))) and inverse 2m log cosh(z/2) for z>=0. Monotonicity yields exactly the displayed lower and upper endpoint intersections with the signed j_L +/- e_L interval.',
  'Final ISM43 first fixes a singleton coefficient carrier with explicit inverse projection/insertion. It then proves the full (V/W)^A kernel using all coordinate projections, and verifies zero-insertion, signed permutations, and the retained empty-mask outer label.'
 ],
 'repairs_requested_and_verified':[
  'R67 typed residual domain and boundary vanishing criterion',
  'R67 full-source acyclic tail versus proper-source V/W and diagonal',
  'R72 cross-Gram admitted degree ordering i<=j',
  'ISM43 one-factor singleton carrier before general-face direct-sum map'
 ],
 'status':'accepted within the stated proof scope; final active route checks recorded separately'
}
(HERE/'ROOT_AND_SIGNED_PROOF_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out['reviewed'],indent=2))
