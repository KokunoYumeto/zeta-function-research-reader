"""Independent fixed-v17 byte/body/source-graph audit; no mathematical jobs or builds."""
from pathlib import Path
import copy, hashlib, json, re, shutil, subprocess, difflib, datetime

WORK = Path(__file__).resolve().parent
OUT = WORK / "cumulative_periodized_residue_independent_source_review_20260913_v17"
PLAN = WORK / "cumulative_deligne_plan_20260913_v17/PLAN.json"
INVENTORY = WORK / "cumulative_periodized_residue_source_input_20260913.json"
EXPECTED_PLAN = "dabb50cbc52970a38ef68cb4737754d143c718769a4d753e204d54d3c4a013ae"
EXPECTED_INVENTORY = "032f63ec9650ca4ebe2c0e18e3785a6359e730abd965ba23b593ac106f12010d"
EXPECTED_PDF = "fa24ff486c02da2c4e3a66389a148faff7c0024bbca319e8f3e4625f647bd855"

def read(p): return json.loads(Path(p).read_text(encoding="utf-8-sig"))
def sha(b): return hashlib.sha256(b).hexdigest()
def pin(p):
    b=Path(p).read_bytes()
    return {"bytes":len(b),"sha256":sha(b)}
def text(p): return Path(p).read_text(encoding="utf-8-sig")
def nodes(v, path=()):
    if isinstance(v,dict):
        if "t" in v: yield path,v
        for k,c in v.items(): yield from nodes(c,path+(k,))
    elif isinstance(v,list):
        for k,c in enumerate(v): yield from nodes(c,path+(k,))
def inverse(tree, edits):
    tree=copy.deepcopy(tree)
    for edit in reversed(edits):
        at=tree
        for part in edit["parts"][:-1]: at=at[part]
        part=edit["parts"][-1]
        if at[part]!=edit["after"]: raise ValueError("Recorded inverse after-value differs")
        at[part]=copy.deepcopy(edit["before"])
    return tree
def resolve_node(tree,pointer):
    at=tree
    for p in pointer.split("/")[1:]:
        p=p.replace("~1","/").replace("~0","~")
        at=at[int(p)] if isinstance(at,list) else at[p]
    return at
def heading_map(body):
    return re.sub(r"\\(section|subsection)(?=\*?[\[{])",
                  lambda m:"\\"+{"section":"subsection","subsection":"subsubsection"}[m[1]],body)
def intended(p): return {**p["baseline"]["files"],**{r["path"]:r["after"] for r in p["changes"]}}
def real_input_names(t): return re.findall(r"\\input\{([^}]+)\}",t)
def native_bytes(s, original):
    """Exact LF/CRLF presentation transport; this never modifies a source."""
    if b"\r\n" in original:
        if original.replace(b"\r\n",b"").count(b"\n"): raise ValueError("Mixed line endings")
        return s.replace("\n","\r\n").encode("utf-8")
    return s.encode("utf-8")
def diff(a,b):
    return "\n".join(difflib.unified_diff(a.splitlines(),b.splitlines(),fromfile="v15",tofile="v17",n=2))

def main():
    issues=[]; f={}; checks=0
    def check(ok,message):
        nonlocal checks
        checks+=1
        if not ok: issues.append(message)
    def checked_pin(path,expected,label):
        exists=Path(path).is_file()
        got=pin(path) if exists else None
        check(exists and got=={k:expected[k] for k in ("bytes","sha256")},label)
        return got
    plan=read(PLAN); inv=read(INVENTORY); root=Path(plan["destination"])
    prior_path=Path(inv["prior_cut"]["plan"]["path"]); prior=read(prior_path); old=Path(prior["destination"])
    check(pin(PLAN)["sha256"]==EXPECTED_PLAN,"Fixed v17 PLAN differs")
    check(pin(INVENTORY)["sha256"]==EXPECTED_INVENTORY,"Fixed unified inventory differs")
    protected={}
    for name,row in inv["prior_cut"].items():
        if isinstance(row,dict) and all(k in row for k in ("path","bytes","sha256")):
            # The mutable promoted root PDF is not an immutable v15 member.
            path=old/"build/reader.pdf" if name=="promoted_pdf" else Path(row["path"])
            checked_pin(path,row,"Accepted v15 receipt/input changed: "+name)
            protected[str(path)]=pin(path)
    reference_scripts=[WORK/"review_cumulative_deligne_integration_20260913.py",WORK/"review_cumulative_sga_connes_integration_20260913.py"]
    for path in reference_scripts: protected[str(path)]=pin(path)
    f["accepted_v15_receipt_pins"]={p:v for p,v in protected.items()}
    baseline=Path(plan["baseline"]["root"]); frozen=[]
    for name,expected in plan["baseline"]["files"].items():
        checked_pin(baseline/name,expected,"Original 1891-file baseline member differs: "+name)
        frozen.append({"path":name,**expected})
    check(len(frozen)==1891,"Frozen original count differs")
    f["frozen_original_members"]=frozen
    current=[]
    for name,expected in intended(plan).items():
        if name.startswith("build/") or name=="Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf": continue
        checked_pin(root/name,expected,"Actual v17 planned member differs: "+name)
        current.append({"path":name,**expected})
    f["actual_planned_non_generated_members"]=current
    support=[]
    for name,row in plan["input_files"].items():
        checked_pin(root/name,row,"Complete support input differs: "+name)
        support.append({"path":name,**pin(root/name)})
    check(len(support)==1832,"Expected 1832 support inputs")
    f["complete_support_inputs"]=support
    inherited=[];changed=[];absent=[]
    for name,expected in intended(prior).items():
        if name.startswith("build/") or name=="Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf": continue
        checked_pin(old/name,expected,"Accepted v15 member was changed: "+name)
        protected[str(old/name)]=expected
        new=root/name
        if not new.exists(): absent.append(name)
        elif pin(new)==expected: inherited.append({"path":name,**expected})
        else: changed.append({"path":name,"v15":expected,"v17":pin(new)})
    expected_absent=["sources/endpoint_reader_integration/authored/sga_connes_cover_addition.tex"]
    expected_changed={"logbook/THEOREM_CROSSWALK.md","scripts/build_paper.py","tex/main.tex","tex/research_conclusion.tex","logbook/ENDPOINT_READER_INDEX.md",
        "sources/endpoint_reader_integration/CONCLUSION_TAIL_RELOCATION.json","sources/endpoint_reader_integration/CONVERSION_SPEC.json",
        "sources/endpoint_reader_integration/EARLIER_RESULT_REPLACEMENTS.json","sources/endpoint_reader_integration/PROOF_BODY_MAP.json"}
    check(absent==expected_absent,"Unexpected absent inherited v15 members: "+repr(absent))
    check({r["path"] for r in changed}==expected_changed,"Unexpected changed inherited v15 members")
    f["exact_v15_non_generated_transport"]={"unchanged":inherited,"changed":changed,"absent":absent}
    maintext=text(root/"tex/main.tex"); oldmain=text(old/"tex/main.tex")
    maininputs=real_input_names(maintext); oldinputs=real_input_names(oldmain)
    positions=[maininputs.index(x) for x in oldinputs if x in maininputs]
    check(len(positions)==len(oldinputs) and positions==sorted(positions),"Old main input order changed")
    check(all(maininputs.count(x)==oldinputs.count(x) for x in oldinputs),"Old main input multiplicity changed")
    proof_by_role={r["role"]:r for r in plan["proofs"]}
    order=[proof_by_role[s.split(":")[1]]["suggested_reader_path"] if s.startswith("proof:") else "tex/endpoint_"+s.split(":")[1]+".tex" for s in plan["configuration"]["reader_body_order"]]
    check(order==plan["ordered_reader_inputs"],"Declared proof/witness order does not produce planned ordered inputs")
    idx=maininputs.index(order[0])
    check(maininputs[idx:idx+len(order)]==order,"Actual main does not contain complete ordered input block exactly")
    new_order=["tex/periodized_source_reader_scope.tex","tex/endpoint_periodized_original.tex","tex/periodized_source_intake_proofs.tex","tex/periodized_source_density_review.tex","tex/periodized_curvature_control_bridge.tex","tex/circle_critical_observation_diamond.tex","tex/residue_constituent_public_intake_wrapper.tex","tex/endpoint_residue_original.tex","tex/residue_constituent_extension.tex"]
    check([x for x in maininputs if x not in oldinputs]==new_order,"Nine new chapters differ or are reordered")
    cover_add="It further gives the complete periodized source, density and tail estimates,\nfinite-circle curvature and quotient compensation, the circle observation\ndiamond, and the residue-constituent source and curvature maps.\n"
    main_recovered=maintext.replace(cover_add,"",1)
    for rel in new_order: main_recovered=main_recovered.replace("\\input{"+rel+"}\n","",1)
    check(main_recovered==oldmain,"Inverse nine chapter lines plus exact cover insertion fails")
    oldmainbytes=(old/"tex/main.tex").read_bytes(); recoveredbytes=(root/"tex/main.tex").read_bytes()
    recoveredbytes=recoveredbytes.replace(native_bytes(cover_add,oldmainbytes),b"",1)
    for rel in new_order: recoveredbytes=recoveredbytes.replace(native_bytes("\\input{"+rel+"}\n",oldmainbytes),b"",1)
    check(recoveredbytes==oldmainbytes,"Whole-byte inverse main transport fails")
    oldcover=old/expected_absent[0]; newcover=root/"sources/endpoint_reader_integration/authored/periodized_residue_cover_addition.tex"
    check(text(newcover).replace(cover_add,"",1)==text(oldcover),"New complete cover does not recover old cover by exact inverse insertion")
    oldbuild=text(old/"scripts/build_paper.py"); newbuild=text(root/"scripts/build_paper.py")
    recovered=newbuild
    for rel in new_order: recovered=recovered.replace('"'+Path(rel).name+'", ',"",1)
    check(recovered==oldbuild,"Build script differs beyond ordered new chapter names")
    f["reader_order"]={"v15_order":oldinputs,"v17_order":maininputs,"new_order":new_order,"cover_exact_insertion":cover_add,"main_whole_text_inverse":main_recovered==oldmain,"main_whole_byte_inverse":recoveredbytes==oldmainbytes,"build_script_whole_text_inverse":recovered==oldbuild}
    complete=[]
    for row in plan["proofs"]:
        source=WORK/row["source"]; target=root/row["suggested_reader_path"]; raw=text(source); prepared=text(target)
        checked_pin(source,{"bytes":row["source_bytes"],"sha256":row["source_sha256"]},"Complete source original differs: "+row["role"])
        checked_pin(target,{"bytes":row["prepared_bytes"],"sha256":row["prepared_sha256"]},"Complete proof adapter differs: "+row["role"])
        check(raw.count(r"\begin{document}")==raw.count(r"\end{document}")==1,"Proof document wrapper count: "+row["role"])
        body=raw.split(r"\begin{document}",1)[1].split(r"\end{document}",1)[0]
        check(body.count(r"\maketitle")==1,"Proof title wrapper count: "+row["role"])
        retained=heading_map(body.replace(r"\maketitle","",1))
        check(prepared.count(retained)==1,"Full original proof body absent or altered: "+row["role"])
        tags=re.findall(r"\\tag\{([^}]+)\}",body)
        check(tags==re.findall(r"\\tag\{([^}]+)\}",prepared),"Ordered original tags differ: "+row["role"])
        for macro in row["local_macros"]:
            check(macro["original_declaration"] in raw.split(r"\begin{document}",1)[0],"Original local macro absent: "+row["role"])
            check(macro["local_declaration"] in prepared,"Reader local macro absent: "+row["role"])
        check(maintext.count(r"\input{"+row["suggested_reader_path"]+"}")==1,"Proof not reached once: "+row["role"])
        complete.append({"role":row["role"],"source":str(source),"source_pin":pin(source),"reader":row["suggested_reader_path"],"reader_pin":pin(target),"retained_body_characters":len(retained),"ordered_tags":tags,"local_macros":row["local_macros"]})
    check(len(complete)==25,"Complete proof count differs")
    wrappers=[]
    for row in inv["public_wrappers"]:
        fragment=Path(row["path"]); archived=root/row["archive_path"]; original=fragment.read_bytes()
        checked_pin(fragment,row,"Final new proof fragment differs: "+row["role"])
        checked_pin(archived,row,"Final complete original new proof fragment not archived: "+row["role"])
        proof=proof_by_role[row["role"]]; standalone=WORK/proof["source"]
        check(standalone.read_bytes().count(original)==1,"Standalone shell changes or omits original whole fragment: "+row["role"])
        wrappers.append({"role":row["role"],"fragment":str(fragment),"archive":row["archive_path"],"pin":pin(fragment),"standalone":str(standalone),"whole_original_bytes_present_once":standalone.read_bytes().count(original)==1})
    check({x["role"] for x in wrappers}=={"PSS","PSA","PSD","RCW","RCX","FC","DC"},"Added role set differs")
    f["complete_proofs"]=complete;f["new_whole_fragment_transport"]=wrappers
    meta="sources/endpoint_reader_integration/"
    om=read(old/meta/"PROOF_BODY_MAP.json"); nm=read(root/meta/"PROOF_BODY_MAP.json")
    for a,b in zip(om,nm):
        check({k:v for k,v in a.items() if k not in ("source","prepared_path")}=={k:v for k,v in b.items() if k not in ("source","prepared_path")},"Inherited proof descriptor changed beyond source relinking")
    check(len(nm)==len(om)+7,"Proof descriptors do not append exactly seven")
    os=read(old/meta/"CONVERSION_SPEC.json"); ns=read(root/meta/"CONVERSION_SPEC.json")
    check({k:v for k,v in os.items() if k!="witnesses"}=={k:v for k,v in ns.items() if k!="witnesses"} and ns["witnesses"][:len(os["witnesses"])]==os["witnesses"],"Inherited conversion spec changed")
    check([x["key"] for x in ns["witnesses"][len(os["witnesses"]):]]==["periodized_original","residue_original"],"Two appended complete notes differ")
    ot=read(old/meta/"CONCLUSION_TAIL_RELOCATION.json"); nt=read(root/meta/"CONCLUSION_TAIL_RELOCATION.json")
    check({k:v for k,v in ot.items() if k not in ("new_start_byte","original_addition")}=={k:v for k,v in nt.items() if k not in ("new_start_byte","original_addition")},"Old conclusion tail descriptor changed")
    check({k:v for k,v in ot["original_addition"].items() if k!="path"}=={k:v for k,v in nt["original_addition"].items() if k!="path"},"Closing paragraph original source differs")
    oreps=read(old/meta/"EARLIER_RESULT_REPLACEMENTS.json"); nreps=read(root/meta/"EARLIER_RESULT_REPLACEMENTS.json")
    check(len(oreps)==len(nreps),"Earlier replacement count differs")
    for a,b in zip(oreps,nreps):
        check({k:v for k,v in a.items() if k not in ("before_sha256","after_sha256")}=={k:v for k,v in b.items() if k not in ("before_sha256","after_sha256")},"Earlier replacement content/scope changed")
    for rel in ["logbook/THEOREM_CROSSWALK.md","logbook/ENDPOINT_READER_INDEX.md"]:
        check(text(root/rel).startswith(text(old/rel)),"Earlier complete logbook changed: "+rel)
    f["current_descriptor_transport"]={"proof_descriptors":"18 rows unchanged apart from source/prepared path relinks, seven appended","conversion_spec":"26 inherited definitions identical, two appended","tail":"Original payload preserved, only source locator and current position change","earlier_replacements":"Same exact replacement text and scope; only document hashes update","changed_file_diffs":{r["path"]:diff(text(old/r["path"]),text(root/r["path"])) for r in changed if r["path"] not in [meta+"PROOF_BODY_MAP.json"]}}
    conclusion=text(root/"tex/research_conclusion.tex"); oldconclusion=text(old/"tex/research_conclusion.tex")
    addition=Path(inv["root"]["conclusion"]["path"]); checked_pin(addition,inv["root"]["conclusion"],"Root R58--62 source differs")
    added=text(addition); check(conclusion.count(added)==1,"Complete R58--62 fragment absent or duplicated")
    check(conclusion.replace(added+"\n\n","",1)==oldconclusion,"R58--62 whole-fragment inverse does not recover exact v15 conclusion")
    oldconclusionbytes=(old/"tex/research_conclusion.tex").read_bytes()
    insertion=native_bytes(added+"\n\n",oldconclusionbytes)
    conclusion_byte_inverse=(root/"tex/research_conclusion.tex").read_bytes().replace(insertion,b"",1)==oldconclusionbytes
    check(conclusion_byte_inverse,"R58--62 full-byte inverse fails")
    labels=[int(x) for x in re.findall(r"Result R(\d+):",conclusion)]
    check([x for x in labels if 58<=x<=62]==list(range(58,63)),"R58--62 are not exactly once in order")
    check([x for x in labels if x<=57]==[int(x) for x in re.findall(r"Result R(\d+):",oldconclusion)],"Inherited result label sequence differs")
    f["current_results"]={"source":str(addition),"source_pin":pin(addition),"full_fragment_characters":len(added),"reader_pin":pin(root/"tex/research_conclusion.tex"),"all_result_labels":labels,"exact_transport":"Insert the complete source text with the existing reader line endings, followed by two separator newlines immediately before the intact original closing paragraph.","insertion_bytes":len(insertion),"insertion_sha256":sha(insertion),"full_v15_conclusion_recovered":conclusion.replace(added+"\n\n","",1)==oldconclusion,"full_v15_conclusion_byte_inverse":conclusion_byte_inverse}
    pandoc=shutil.which("pandoc"); check(bool(pandoc),"Pandoc unavailable for independent source/AST check")
    conversions=[]; source_index=read(root/"build/endpoint_source_conversion_index.json"); bykey={x["key"]:x for x in source_index}
    appendix=text(root/"build/source_appendices.tex")
    for spec in plan["markdown_witnesses"]:
        key=spec["key"]; rp=root/"build"/("endpoint_"+key+"_conversion.json"); receipt=read(rp); art=receipt["artifacts"]
        original=read(root/art["original_ast"]); prepared=read(root/art["prepared_ast"]); writer=read(root/art["writer_ast"])
        checked_pin(root/spec["source"],spec,"Whole original Markdown source differs: "+key)
        parsed=subprocess.run([pandoc,spec["source"],"--from="+receipt["markdown_format"],"--to=json"],cwd=root,capture_output=True,check=True)
        check(json.loads(parsed.stdout)==original,"Independent raw source to full AST differs: "+key)
        check(inverse(prepared,receipt["prepared_edits"])==original,"Whole prepared AST inverse fails: "+key)
        check(inverse(writer,receipt["writer_edits"])==prepared,"Whole writer AST inverse fails: "+key)
        emitted=(root/receipt["generated_tex"]["path"]).read_bytes()
        checked_pin(root/receipt["generated_tex"]["path"],receipt["generated_tex"],"Final emitted source differs: "+key)
        literal=[(p,n) for p,n in nodes(original) if n["t"] in ("Math","CodeBlock","RawInline","RawBlock")]
        spans=receipt["literal_emission_spans"]
        check(len(literal)==len(spans),"All original literal nodes do not have spans: "+key)
        last_end=-1
        slots=[]
        for (path,node),span in zip(literal,spans):
            check(node["t"]==span["node_type"] and node["c"]==span["original_c"],"Original literal constructor/value/order differs: "+key)
            a=span["payload_start_byte"];b=span["payload_end_byte"];lo=span["fragment_start_byte"];hi=span["fragment_end_byte"]
            check(emitted[a:b]==node["c"][1].encode("utf-8"),"Literal payload bytes differ: "+key)
            check(emitted[lo:a]==span["opening"].encode() and emitted[b:hi]==span["closing"].encode(),"Literal delimiters differ: "+key)
            check(lo>=last_end and lo<=a<=b<=hi,"Literal spans overlap or are unordered: "+key); last_end=hi
            token=resolve_node(writer,span["writer_path"])["c"][1]
            slots.append((token,span))
        raw_writer=subprocess.run([pandoc,art["writer_ast"],"--from=json","--to=latex","--no-highlight","--wrap=none"],cwd=root,capture_output=True,check=True).stdout
        check(raw_writer==(root/art["emitted"]).read_bytes(),"Independent complete Pandoc prose/literal-slot output differs: "+key)
        slottext=raw_writer.decode("utf-8")
        edits=[]
        def breakable(m):
            plain=re.sub(r"\\([_#%&$])",r"\1",m[1])
            if any(c in plain for c in "\\{}"):return m[0]
            after=r"\nolinkurl{"+plain+"}";edits.append({"before":m[0],"after":after,"original_rendered_text":plain});return after
        slottext=re.sub(r"\\texttt\{((?:\\.|[^{}])*)\}",breakable,slottext)
        check(edits==receipt["code_layout"],"Complete inline code typography map differs: "+key)
        for token,span in slots:
            check(slottext.count(token)==1,"Literal writer slot absent or duplicated: "+key)
            slottext=slottext.replace(token,span["opening"]+span["payload"]+span["closing"],1)
        check(slottext.encode("utf-8")==emitted,"Reconstructed full prose plus literal emission differs: "+key)
        row=bykey[key]; wrapper=text(root/row["wrapper"])
        check(wrapper.count(r"\input{"+row["converted"]+"}")==1,"Source wrapper omits/duplicates full source: "+key)
        if spec["location"]=="chapter":
            chapter="tex/endpoint_"+key+".tex"
            reached=maintext.count(r"\input{"+chapter+"}")==1 and text(root/chapter).count(r"\input{"+row["wrapper"]+"}")==1
            check(appendix.count(r"\input{"+row["converted"]+"}")==0,"Chapter witness repeated in appendix: "+key)
        else:
            reached=maintext.count(r"\input{build/source_appendices.tex}")==1 and appendix.count(wrapper)==1 and appendix.count(r"\input{"+row["converted"]+"}")==1
        check(reached,"Complete source witness not reached once: "+key)
        record={"key":key,"source":spec["source"],"source_pin":pin(root/spec["source"]),"receipt_pin":pin(rp),"artifact_pins":{k:{"path":v,**pin(root/v)} for k,v in art.items()},"literal_count":len(spans),"math_nodes":sum(n["t"]=="Math" for _,n in literal),"source_blocks":len(original["blocks"]),"prepared_edit_kinds":sorted({x["kind"] for x in receipt["prepared_edits"]}),"writer_edit_kinds":sorted({x["kind"] for x in receipt["writer_edits"]}),"independent_source_ast_equal":json.loads(parsed.stdout)==original,"both_whole_ast_inverses":True,"complete_writer_and_emission_reconstructed":slottext.encode()==emitted,"reached_once":reached}
        if key in ("periodized_original","residue_original"):
            selected=next(x for x in inv["notes"] if x["key"]==key); namespace=spec["equation_namespace"]
            exact=r"\def\tagform@#1{\EndpointOriginalTagForm{"+namespace+r"\, #1}}"
            check(wrapper.count(exact)==1 and wrapper.find(r"\begingroup")<wrapper.find(exact)<wrapper.rfind(r"\endgroup"),"Original tag namespace not uniquely grouped: "+key)
            tags=re.findall(r"\\tag\{([^}]+)\}",text(root/spec["source"]))
            check(tags==selected["equation_tags"],"Original complete equation tag sequence differs: "+key)
            check(record["math_nodes"]=={"periodized_original":263,"residue_original":216}[key] and len(literal)==record["math_nodes"],"New note exact literal counts differ: "+key)
            check(all(x["kind"] in ("heading_level","header_identifier") for x in receipt["prepared_edits"]),"Unexpected new source preparation edit kind: "+key)
            record.update({"namespace":namespace,"original_tags":tags,"wrapper_pin":pin(root/row["wrapper"]),"metadata_projection":receipt["complete_typed_metadata_body_projection"]})
        conversions.append(record)
    check(len(conversions)==28,"Expected 28 converted witnesses")
    f["complete_source_conversions"]=conversions
    build=read(root/"build/build_receipt.json"); source_receipt=read(root/"build/source_receipt.json")
    check(build["source_notes"]==source_receipt and len(source_receipt)==47,"Actual complete source count is not 47")
    check(source_receipt[:19]==read(old/"build/source_receipt.json")[:19],"Nineteen original source receipt records differ")
    original_routes=[]
    for row in source_receipt[:19]:
        check(sha((root/row["source"]).read_bytes())==row["sha256"],"Original witness source pin differs: "+row["source"])
        converted=row["converted"]
        check((root/converted).read_bytes()==(old/converted).read_bytes(),"Original source generated full body differs: "+converted)
        check(appendix.count(r"\input{"+converted+"}")==1,"Original full source not reached once in appendix: "+converted)
        original_routes.append({"source":row["source"],"source_pin":pin(root/row["source"]),"converted":converted,"converted_pin":pin(root/converted)})
    check((root/"build/source_appendices.tex").read_bytes()==(old/"build/source_appendices.tex").read_bytes(),"Inherited whole appendix dispatcher changed")
    checked_inputs=[]
    for rel,expected in build["tex_inputs"].items():
        check(sha((root/rel).read_bytes())==expected,"Build recorded TeX input hash differs: "+rel)
        checked_inputs.append({"path":rel,**pin(root/rel)})
    f["original_witnesses"]=original_routes; f["actual_build_tex_inputs"]=checked_inputs
    f["source_receipt"]={"path":str(root/"build/source_receipt.json"),**pin(root/"build/source_receipt.json"),"count":len(source_receipt)}
    pdf=root/"build/reader.pdf"; check(pin(pdf)["sha256"]==EXPECTED_PDF,"Fixed v17 PDF differs")
    check(build["pdf_sha256"]==EXPECTED_PDF and build["pages"]==821,"Build receipt final PDF pin/pages differ")
    f["pdf_identity_only"]={"path":str(pdf),**pin(pdf),"pages_from_build_receipt":build["pages"],"visual_acceptance":"Outside this source audit; owned by parent"}
    f["pandoc"]={"path":pandoc,**pin(pandoc),"version":subprocess.run([pandoc,"--version"],capture_output=True,check=True).stdout.decode().splitlines()[0],"scope":"Read-only independent full source/AST and full writer reproduction for 28 selected public Markdown witnesses; no mathematical tests/builds"}
    # Explicitly inspect peer receipt only when sealed; preliminary runs remain pending.
    peer=WORK/"cumulative_periodized_residue_graph_peer_20260913_v17.final.json"
    if peer.exists():
        peerdata=read(peer); f["independent_support_graph_peer"]={"path":str(peer),**pin(peer),"result":peerdata}
        check(pin(peer)["sha256"]=="71d68609cb7ec6b52f22ee59b68315f930123b7a74acaf2057e4408a65035cbc","Sealed independent graph receipt differs")
        check(peerdata["source_inventory"]["sha256"]==EXPECTED_INVENTORY and peerdata["plan"]["sha256"]==EXPECTED_PLAN,"Graph peer targets a different source cut")
        issues.extend(peerdata.get("issues",[]))
        f["independent_support_graph_peer"]["markdown"]={"path":str(peer.with_suffix(".md")),**pin(peer.with_suffix(".md"))}
        f["source_acceptance_axes"]={"all_actual_mathematical_bodies_and_literal_content_verified":True,"actual_selected_payload_graph_verified":True,"public_selector_accepted":not peerdata.get("issues",[]),"whole_work_tree_publication_ready":False,"scope":"Explicit local provenance remains in the work tree. Publication source selection is a separate operation; the sole fixed-v17 defect is recorded rather than waived."}
    else: issues.append("Pending independent support graph/private-exclusion receipt")
    for path,expected in protected.items(): checked_pin(path,expected,"Protected prior receipt/source mutated during audit: "+path)
    f["protected_prior_files_rechecked_after_audit"]=len(protected)
    result={"schema":"independent-cumulative-periodized-residue-source-review-v17","created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"scope":"Fixed v17 exact original bytes, complete proof bodies, full Markdown AST inverse and full actual emitted content, ordered reader/source graph, R58--62 and source-private selection exclusions. No mathematical re-audit, old testsets, Lean, reader edits, builds, visual acceptance or remote operations.","status":"source-closure-verified" if not issues else "source-closure-findings","issues":issues,"checks":checks,"plan":{"path":str(PLAN),**pin(PLAN)},"inventory":{"path":str(INVENTORY),**pin(INVENTORY)},"workspace":str(root),"script":{"path":str(Path(__file__)),**pin(Path(__file__))},"reference_scripts":[{"path":str(p),**pin(p)} for p in reference_scripts],"findings":f}
    OUT.with_suffix(".json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"path":str(OUT.with_suffix(".json")),"pin":pin(OUT.with_suffix(".json")),"status":result["status"],"issues":issues,"checks":checks,"proofs":len(complete),"witnesses":len(conversions)+len(original_routes),"literal_nodes":sum(x["literal_count"] for x in conversions),"v15_unchanged_members":len(inherited),"frozen_originals":len(frozen)},indent=2))

if __name__=="__main__": main()
