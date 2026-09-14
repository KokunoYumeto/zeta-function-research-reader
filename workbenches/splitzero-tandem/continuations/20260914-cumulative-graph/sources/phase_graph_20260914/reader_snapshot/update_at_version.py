"""Transport the full accepted AT edition into its earlier dependency slot."""
from pathlib import Path
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parent
source=Path(r'workspace:\work\rh_counterfactual_20260913\total_object\propagation_metric\derived\tex\modules\AT.tex')
expected='438fd058f4745056945a3a747eaeb63f2b36a0f146335ed72018acdb28b93727'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(source)==expected
hist=ROOT/'history/AT_full_refinement';hist.mkdir(parents=True,exist_ok=True)
paths=[ROOT/'originals/dep04.tex',ROOT/'tex/bodies/dep04.tex',ROOT/'SOURCE_DEPENDENCIES.json']
preserved=[]
for p in paths:
    dest=hist/p.relative_to(ROOT);dest.parent.mkdir(parents=True,exist_ok=True)
    if not dest.exists():shutil.copyfile(p,dest)
    preserved.append({'path':str(dest.relative_to(ROOT)),'sha256':sha(dest)})
deps=ROOT/'SOURCE_DEPENDENCIES.json';data=json.loads(deps.read_text(encoding='utf-8-sig'))
old=data['files'][3].copy()
data['files'][3].update(path=str(source),sha256=expected,bytes=source.stat().st_size,
    role='Complete accepted AT refinement, retaining the original source and adding AT21a–AT21e invoked by ACM and HC')
shutil.copyfile(source,ROOT/'originals/dep04.tex')
deps.write_text(json.dumps(data,indent=2)+'\n')
(hist/'VERSION_TRANSPORT.json').write_text(json.dumps({'old':old,'current':data['files'][3],'preserved':preserved,
    'review':r'workspace:\work\rh_counterfactual_20260913\total_object\propagation_metric\review\ROOT_INDEPENDENT_MATH_REVIEW.json',
    'scope':'Whole accepted source replaces its whole earlier slot; no excerpt or omitted predecessor body'},indent=2)+'\n')
print(expected)
