"""Prepare complete source-read angular and fixed-axis proofs in this lane."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
frozen=ROOT/"sources"/"angular_008"
source=Path(r"[local]/Documents\Papors\Chatnotes\Zeta-Function-Foundation\tex\satellites\29l_ns_axis_arithmetic_jet.tex")
data=source.read_bytes()
digest=hashlib.sha256(data).hexdigest()
assert digest=="5a759ec9ac6e7665ade9f33419eccb158e8648af682d816ef434e111bb8b78da",digest
(frozen/source.name).write_bytes(data)
review=Path(r"[local]/Documents\Papors\Chatnotes\Zeta-Function-Foundation\agents\ns_source_operator_20260908\AXIS_JET_REVIEW.md")
(frozen/review.name).write_bytes(review.read_bytes())

angular=(frozen/"ns_angular_mellin.tex").read_text(encoding="utf-8")
angular=angular.replace(r"\section*{",r"\section{").replace(r"\subsection*{",r"\subsection{")
angular=angular.replace(r"\R",r"\mathbb R").replace(r"\C",r"\mathbb C")
angular=angular.replace("{am:","{eq:cq-am:").replace("{nw:","{eq:cq-nw:")
first=angular.index("\n")
angular=angular[:first]+"\n"+r"\label{sec:cq-angular-physical-map}"+"\n\n"+r"The complete companion proof \cite{cqNSAngular} is retained here with its original coordinates and full corrected source fields. The source existence and correction estimates remain the explicit external input \cite{cqNS2026}."+angular[first:]
angular=angular.replace("The source-read receipt\nrecords the corresponding construction locators.",r"The corresponding source locators are (9.21), (10.20)--(10.21), and the unchanged inner-region construction of \cite{cqNS2026}.")
(ROOT/"checks"/"angular_physical_008.tex").write_text(angular,encoding="utf-8")

axis=data.decode("utf-8")
replacements={
 "{sec:ns-axis-arithmetic-jet}":"{sec:cq-ns-axis-arithmetic-jet}",
 "{sec:ns-actual-witness}":"{sec:cq-NS-actual-witness}",
 "{sec:ns-full-flow}":"{sec:cq-NS-profile-transfer}",
 "{naj:":"{eq:cq-naj:",
 "{eq:nh-EM}":"{eq:cq-angular-EM}",
 "{openaiNS2026release}":"{cqNS2026}",
 "{olverDLMF2}":"{cqDLMFEM}",
 "{apostolDLMF25}":"{cqDLMFZeta}"}
for old,new in replacements.items():
    axis=axis.replace(old,new)
needle=r"\subsection{The arithmetic operator on every endpoint derivative}"
em=(ROOT/"checks"/"angular_em_008.tex").read_text(encoding="utf-8")
axis=axis.replace(needle,em+"\n\n"+needle)
axis=axis.replace("The angular-momentum transform can see",r"The complete companion fixed-axis proof \cite{cqNSAxis} is included with a local proof of its endpoint summation formula. The angular-momentum transform can see",1)
axis=axis.replace("For every integer \\(m\\ge0\\)","For every integer \\(m\\ge0\\), with \\((1+h)_m=\\prod_{j=0}^{m-1}(1+h+j)\\) and empty product one")
(ROOT/"checks"/"angular_axis_008.tex").write_text(axis,encoding="utf-8")
receipt={"source":str(source),"source_sha256":digest,"source_read":"root complete content read; current hash differs from earlier reviewed revision",
         "earlier_independent_review_target_sha256":"e43586e0f117344e45536bc8792228e386f2ba65f83bfc74f54264398762a2ac",
         "scope":"earlier review is not claimed byte-identical to current source; root read the entire current proof and its earlier review, retaining the actual imported-source dependency"}
(frozen/"axis_source_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
goal=ROOT/"logbook"/"active_goal.md"
text=goal.read_text(encoding="utf-8").replace("Current durable workflow pointer: checkpoint_007.md","Current durable workflow pointer: checkpoint_008.md")
goal.write_text(text,encoding="utf-8")
print(json.dumps({"axis_sha256":digest,"prepared":["angular_physical_008.tex","angular_axis_008.tex"]}))
