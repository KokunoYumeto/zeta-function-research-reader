from pathlib import Path
import hashlib,json
here=Path(__file__).resolve().parent
gw=here.parent.parent
specs=[
('HBL.tex','baseline_20260914/independent/HOMOGENEOUS_GAMMA_BASELINE.tex','09aff3f27c728e1519c15c916f1a12bf173ca321f3cbaec90b826cd4ded09065'),
('BSL.tex','baseline_20260914/BASELINE_ORIGINAL_PACKET.tex','a53703c284d816930291aa4b02373564fe8cd5cf7c93a1d0517354614f438c30'),
('GDR.tex','low_refinement_20260914/DERIVATIVE_REMAINDER.tex','642fc0b0b60a3253ad577b588b2b93d6d0aa4357cae40b69e7f45098e0c10304'),
('LER.tex','low_refinement_20260914/LOW_ENDPOINT_REFINEMENT.tex','b3607ad6e0cd2480f917bdce057683cb8526d5243f583363eee297835403422e'),
('QLG.tex','q_scale_20260914/independent/QUANTITATIVE_LOG_GAS_PARTITION.tex','52256dd3671db7944c6758ed8a2f7129b7a226a08c433b1f32449985f2137b71'),
('QGT.tex','q_scale_20260914/QUANTITATIVE_ORIGINAL_GAMMA_RETURN.tex','0b552f80782b86651d3876ecf2dfd71a7c3f2e2c04ef005d6cadecb15d9bb629'),
('QGQ.tex','q_scale_20260914/ORIGINAL_M_ONE_QUANTITATIVE_BOUND.tex','9803d6ddf301807a1df7b4678b325241f6785f6ac1f4778c036037607ddc7dc6'),
('IGO.tex','intrinsic_order_20260914/INTRINSIC_EXTERIOR_GAMMA_ORDER.tex','a086f4f2ea260621f5e1a1ec5ca2d0ce8843b464634d35f9affba276a472920f'),
('IFB.tex','intrinsic_four_endpoint_20260914/INTRINSIC_FOUR_ENDPOINT_RELATION_GRAPH.tex','50fc30d31e2b6bdbf8d630f5029cf1091e10618de3e7bd3c22d229cc7ccf340a'),
('GMB.tex','intrinsic_mixed_rows_20260914/ORIGINAL_GAMMA_MIXED_ROW_MORPHISM.tex','32c56427cb2f62c0d41bd2f6830813a84aa01b1bff21a39fd4291e9b54f35556'),
]
manifest=[]
for name,relative,pin in specs:
    source=gw/relative
    actual=hashlib.sha256(source.read_bytes()).hexdigest()
    assert actual==pin,(name,actual,pin)
    manifest.append({'name':name,'source':str(source),'sha256':pin,'typeset':True})
closure=here/'TRANSITIVE_PROVIDER_MANIFEST.json'
if closure.exists():
    manifest.extend(json.loads(closure.read_text(encoding='utf-8')))
(here/'CANONICAL_PROVIDER_MANIFEST.json').write_bytes((json.dumps(manifest,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'new_providers':len(specs),'transitive_providers':len(manifest)-len(specs)},indent=2))
