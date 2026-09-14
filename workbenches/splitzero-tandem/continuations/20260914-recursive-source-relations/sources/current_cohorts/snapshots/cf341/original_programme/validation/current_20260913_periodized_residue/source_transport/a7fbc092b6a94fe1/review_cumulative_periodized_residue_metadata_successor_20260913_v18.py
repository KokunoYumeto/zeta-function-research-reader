"""Bounded successor transport. Extends immutable v17 acceptance without AST/math reruns."""
from pathlib import Path
import json,hashlib,datetime,argparse
W=Path(__file__).resolve().parent
SELECTOR="sources/periodized_residue_complete_closure/integration/PUBLIC_SOURCE_SELECTION.json"
BASE=W/"cumulative_periodized_residue_independent_source_review_20260913_v17.json"
OUT=W/"cumulative_periodized_residue_independent_source_review_20260913_v18_addendum.json"
def read(p):return json.loads(Path(p).read_text(encoding="utf-8-sig"))
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
 b=Path(p).read_bytes();return {"bytes":len(b),"sha256":sha(b)}
def intended(p):return {**p["baseline"]["files"],**{r["path"]:r["after"] for r in p["changes"]}}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--plan-sha256",required=True);ap.add_argument("--selector-sha256",required=True);args=ap.parse_args()
 issues=[];checks=0
 def check(ok,msg):
  nonlocal checks
  checks+=1
  if not ok:issues.append(msg)
 def cp(p,expected,msg):
  exists=Path(p).is_file();got=pin(p) if exists else None
  check(got=={k:expected[k] for k in ("bytes","sha256")},msg)
  return got
 check(pin(BASE)["sha256"]=="6418b800a27fb670ba8e1456e40380dc2ad104e219f72c74b56ea516770c3d2e","Sealed v17 JSON differs")
 md=BASE.with_suffix(".md");check(pin(md)["sha256"]=="ba1a9c7e8e830eab6c2da52d778563e6dfeaa8b5a7c202cb7e48f9806d391364","Sealed v17 Markdown differs")
 base=read(BASE);old=Path(base["workspace"]);planpath=W/"cumulative_deligne_plan_20260913_v18/PLAN.json";plan=read(planpath);root=Path(plan["destination"])
 check(pin(planpath)["sha256"]==args.plan_sha256,"Final v18 plan pin differs")
 check(root==W/"cumulative_deligne_build_20260913_v18","Unexpected successor workspace")
 priorplan=read(base["plan"]["path"]);cp(base["plan"]["path"],base["plan"],"Fixed v17 plan differs")
 inv=read(base["inventory"]["path"]);cp(base["inventory"]["path"],base["inventory"],"Authoritative inventory differs")
 before=intended(priorplan);after=intended(plan)
 non_generated=lambda rel:not rel.startswith("build/") and rel!="Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf"
 oldnames={x for x in before if non_generated(x)};newnames={x for x in after if non_generated(x)}
 check(oldnames==newnames,"Successor planned non-generated path set differs")
 changed=[];transport=[]
 for rel in sorted(oldnames):
  cp(old/rel,before[rel],"Fixed v17 planned source changed: "+rel)
  cp(root/rel,after[rel],"Actual v18 planned source differs: "+rel)
  if before[rel]!=after[rel]:changed.append({"path":rel,"old":before[rel],"new":after[rel]})
  else:transport.append({"path":rel,**after[rel]})
 check([x["path"] for x in changed]==[SELECTOR],"Declared planned byte delta exceeds selector")
 check(set(priorplan["input_files"])==set(plan["input_files"]),"Support input path set differs")
 support=[]
 for rel,row in plan["input_files"].items():
  cp(root/rel,row,"Actual v18 support differs: "+rel)
  oldrow=priorplan["input_files"][rel]
  if rel!=SELECTOR:check({k:row[k] for k in ("sha256","bytes")}=={k:oldrow[k] for k in ("sha256","bytes")},"Support payload changed beyond selector: "+rel)
  support.append({"path":rel,**pin(root/rel)})
 check(plan["proofs"]==priorplan["proofs"],"Whole proof body map changed")
 check(plan["markdown_witnesses"]==priorplan["markdown_witnesses"],"Complete witness definitions changed")
 check(plan["ordered_reader_inputs"]==priorplan["ordered_reader_inputs"],"Main reader order changed")
 generated=[]
 for row in base["findings"]["actual_build_tex_inputs"]:
  cp(root/row["path"],row,"Compiled TeX input changed: "+row["path"]);generated.append(row)
 for row in base["findings"]["complete_source_conversions"]:
  for kind,artifact in row["artifact_pins"].items():
   cp(root/artifact["path"],artifact,"Accepted conversion artifact changed: "+artifact["path"])
  cp(root/row["source"],row["source_pin"],"Complete Markdown source changed: "+row["key"])
 for row in base["findings"]["original_witnesses"]:
  cp(root/row["converted"],row["converted_pin"],"Original generated witness changed: "+row["converted"])
  cp(root/row["source"],row["source_pin"],"Original witness source changed: "+row["source"])
 oldbuild=read(old/"build/build_receipt.json");newbuild=read(root/"build/build_receipt.json")
 check(oldbuild["tex_inputs"]==newbuild["tex_inputs"],"Compiled TeX hash graph changed")
 check(oldbuild["source_notes"]==newbuild["source_notes"],"Complete47-source build graph changed")
 pdf=root/"build/reader.pdf";cp(pdf,base["findings"]["pdf_identity_only"],"Accepted PDF bytes changed")
 check(newbuild["pages"]==821 and newbuild["pdf_sha256"]==base["findings"]["pdf_identity_only"]["sha256"],"Successor PDF receipt identity differs")
 selectorpath=root/SELECTOR;check(pin(selectorpath)["sha256"]==args.selector_sha256,"Final selector pin differs")
 selector=read(selectorpath)
 check(selector["schema"]=="periodized-residue-public-source-selection-v2","Selector schema differs")
 def project(row,keys):return {k:row[k] for k in keys}
 public={r["archive_path"]:r for r in inv["public_support_files"]}
 local={r["archive_path"]:r for r in inv["local_provenance_support_files"]}
 public_extra={r["archive_path"]:r for r in inv["notes"]+inv["public_wrappers"]}
 files=selector["files"];filekeys=("archive_path","sha256","bytes","role")
 expected_files=[project(public[k],filekeys) for k in sorted(public)]
 check(files==expected_files and selector["public_source_count"]==351,"Selector does not enumerate exact authoritative351 public rows")
 note_keys=("key","archive_path","sha256","bytes","title","source_role","equation_namespace")
 proof_keys=("role","archive_path","sha256","bytes","title","reader_filename")
 check(selector["notes"]==[project(r,note_keys) for r in inv["notes"]],"Selector complete note descriptions differ")
 check(selector["proofs"]==[project(r,proof_keys) for r in inv["public_wrappers"]],"Selector complete proof descriptions differ")
 check(not(set(public)&set(local)),"Public/local authoritative paths intersect")
 checked_public=[]
 for r in files+selector["notes"]+selector["proofs"]:
  cp(root/r["archive_path"],r,"Public selected bytes differ: "+r["archive_path"])
  check(r["archive_path"] not in local,"Local provenance path enters public selector")
  checked_public.append(r)
 expected_mappings=[];excluded_mappings=[]
 for r in inv["selection_coverage"]:
  rel=r["selected_archive_path"]
  if rel in public or rel in public_extra:
   expected_mappings.append({"selection":r["selection"],"selected_destination":r["selected_destination"],"public_archive_path":rel,"bytes":r["selected_bytes"],"sha256":r["selected_sha256"],"original_source_pin":project(r["raw_source"],("sha256","bytes")),"handling":r["handling"]})
  else:
   check(rel in local,"Unclassified omitted authoritative mapping: "+rel)
   excluded_mappings.append({"selection":r["selection"],"selected_destination":r["selected_destination"],"local_archive_path":rel})
 check(selector["public_selection_mappings"]==expected_mappings and len(expected_mappings)==93,"Public93 mappings differ from authoritative exact destinations")
 check(len(excluded_mappings)==34 and selector["local_selection_mapping_count_excluded"]==34,"Local34 mapping exclusion differs")
 check(selector["local_provenance_file_count_excluded"]==len(local)==57 and selector["local_provenance_targets_in_public_selection"] is False,"Local57 exclusion counts differ")
 check(not any(x["public_archive_path"] in local for x in selector["public_selection_mappings"]),"Public mapping points to local provenance")
 derived=inv["public_derivations"][0];candidate=selector["public_derivations"]
 check(len(candidate)==1,"Public derivation count differs")
 pubder=candidate[0]
 check(pubder["original_source_pin"]==project(derived["raw"],("sha256","bytes")),"Derivation original pin differs")
 check(project(pubder["public_source"],("sha256","bytes"))==project(derived["derived"],("sha256","bytes")),"Selected derivative bytes differ")
 check(project(pubder["derivation_record"],("sha256","bytes"))==project(derived["receipt"],("sha256","bytes")),"Derivation receipt pin differs")
 for k in ("deleted_original_lines_inclusive","deleted_byte_interval_half_open","original_mathematics_lines_inclusive","full_mathematical_suffix_bytes","full_mathematical_suffix_sha256"):check(pubder[k]==derived[k],"Exact public derivation map differs: "+k)
 for k in ("public_source","derivation_record"):
  cp(root/pubder[k]["archive_path"],pubder[k],"Actual public derivation file differs: "+k)
 target="sources/residue_constituent_review/supplied_replay/fourth_jet_paper_audit.md"
 fourth=[r for r in expected_mappings if r["selected_destination"]==target]
 check(len(fourth)==1 and fourth[0]["public_archive_path"]==target and fourth[0]["sha256"]=="5050f2deee2dbb44e992b671d3551125b481b48e478cdbd26e595595a12f0bba","Fourth-jet selector defect persists")
 rawpath="sources/periodized_residue_local_provenance/fourth_jet_paper_audit_raw.md"
 check(rawpath not in {r["archive_path"] for r in checked_public} and not any(r["public_archive_path"]==rawpath for r in expected_mappings),"Raw local fourth-jet included")
 # Reproduce the entire actual successor tree ledger; no payload execution/extraction.
 transportpath=planpath.parent/"METADATA_SUCCESSOR_TRANSPORT.json";trans=read(transportpath)
 check(pin(transportpath)["sha256"]=="537ba91e486abeded5e894f4c5eb3c21ff85f26dcc370340b84a2ac22679ddea","Sealed successor transport differs")
 actual_before={p.relative_to(old).as_posix():pin(p) for p in old.rglob("*") if p.is_file()}
 actual_after={p.relative_to(root).as_posix():pin(p) for p in root.rglob("*") if p.is_file()}
 check(actual_before==trans["source_before"],"Actual complete v17 tree differs from sealed transport ledger")
 check(actual_after==trans["source_after"],"Actual complete v18 tree differs from sealed transport ledger")
 check(set(actual_before)==set(actual_after) and len(actual_before)==4903,"Complete actual source tree membership differs")
 delta=[k for k in sorted(actual_before) if actual_before[k]!=actual_after.get(k)]
 check(delta==[SELECTOR],"Complete actual tree differs beyond selector")
 preparationpath=W/"cumulative_deligne_inputs_20260913_v18/PREPARATION_RECEIPT.json";prep=read(preparationpath)
 check(pin(preparationpath)["sha256"]=="1874f08e0f21f522d11f09dea7ca19913ed6ea03b3490b6283698373fdeeca3e","Final preparation receipt differs")
 cp(prep["unchanged_visual_acceptance"]["path"],prep["unchanged_visual_acceptance"],"Accepted visual receipt changed")
 result={"schema":"independent-periodized-residue-metadata-successor-closure-v18","created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"status":"source-closure-verified" if not issues else "source-closure-findings","issues":issues,"checks":checks,"plan":str(planpath),"plan_pin":pin(planpath),"workspace":str(root),"prior_source_review":{"path":str(BASE),**pin(BASE)},"prior_source_review_markdown":{"path":str(md),**pin(md)},"inventory":{"path":base["inventory"]["path"],**pin(base["inventory"]["path"])},"script":{"path":str(Path(__file__)),**pin(Path(__file__))},"scope":"Exact metadata-only v18 successor transport and public whitelist closure. The immutable full-body/AST/prose/literal/graph v17 review remains the source acceptance; no mathematical or AST re-audit, builds, rendering, source edits or remote operations.","changed_planned_members":changed,"unchanged_planned_members":transport,"support_inputs":support,"compiled_tex_inputs":generated,"pdf":{"path":str(pdf),**pin(pdf),"pages":821},"selector":{"path":str(selectorpath),**pin(selectorpath)}}
 result.update({"whole_actual_source_tree_transport":{"files_each":len(actual_before),"byte_identical_files":len(actual_before)-len(delta),"changed_paths":delta,"transport_receipt":{"path":str(transportpath),**pin(transportpath)},"actual_complete_before_ledger":actual_before,"actual_complete_after_ledger":actual_after},"public_selection_proof":{"public_files":files,"whole_notes":selector["notes"],"whole_proofs":selector["proofs"],"public_mappings":expected_mappings,"excluded_local_mapping_count":len(excluded_mappings),"excluded_local_mappings":excluded_mappings,"excluded_local_file_count":len(local),"public_derivation":pubder,"fourth_jet_defect_closed":len(fourth)==1 and fourth[0]["public_archive_path"]==target,"raw_local_fourth_jet_excluded":rawpath not in {r["archive_path"] for r in checked_public}},"preparation_receipt":{"path":str(preparationpath),**pin(preparationpath)},"visual_acceptance":prep["unchanged_visual_acceptance"],"publication_scope":"The corrected increment whitelist excludes local provenance and agrees with the authoritative public rows. The work tree intentionally retains local provenance, and its historical PUBLIC_SOURCE_MANIFEST remains earlier-edition evidence. This source-closure addendum does not itself publish or certify a wholesale work-tree upload."})
 OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"path":str(OUT),"pin":pin(OUT),"status":result["status"],"issues":issues,"checks":checks},indent=2))
if __name__=="__main__":main()
