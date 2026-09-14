from pathlib import Path
import fitz,json,re
root=Path(r'workspace:\work\backpropagation_20260913\page_qa\review_0661_0880')
pdf=Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
doc=fitz.open(pdf);out=[]
for n in range(661,881):
 pg=doc[n-1];words=pg.get_text('words')
 for word in words:
  if word[0]<450 or not re.fullmatch(r'\([A-Z]+\.[0-9]+[a-z]?\)|\([A-Z]+[0-9]+[a-z]?\)|\([0-9]+(?:\.[0-9]+[a-z]?)?\)',word[4]):continue
  hits=[]
  tag=fitz.Rect(word[:4])
  for w in words:
   if w==word:continue
   r=fitz.Rect(w[:4]);i=r&tag
   if not i.is_empty and i.width>0.3 and i.height>0.3:hits.append({'word':w[4],'bbox':w[:4],'overlap':list(i)})
  if hits:out.append({'page':n,'tag':word[4],'bbox':word[:4],'hits':hits})
(root/'TAG_OVERLAP_SCREEN.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))

