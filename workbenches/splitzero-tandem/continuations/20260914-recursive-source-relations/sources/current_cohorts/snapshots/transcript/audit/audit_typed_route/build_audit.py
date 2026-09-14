from pathlib import Path
import hashlib
import json
import re

ROOT = Path("workspace:")
OUT = ROOT / "work/tau_f1_transcript_audit_20260913/audit_typed_route"
SOURCE = ROOT / "output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0029_U0040.md"
raw = SOURCE.read_bytes()
source = raw.decode("utf-8-sig")
headers = list(re.finditer(r"(?m)^## ([UA]\d+) \| ([^|]+) \| (user|assistant) \| chain (\d+)\r?$", source))
turns = {}
for i, m in enumerate(headers):
    end = headers[i+1].start() if i+1 < len(headers) else len(source)
    text = source[m.end():end].strip("\r\n")
    turns[m[1]] = {
        "locator": m[1], "node_id": m[2].strip(), "role": m[3], "chain": int(m[4]),
        "character_start": m.start(), "character_end": end,
        "line_start": source[:m.start()].count("\n")+1,
        "body_sha256_utf8": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "text": text,
    }
data = json.loads((OUT / "ledger_data.json").read_text(encoding="utf-8"))
for record in data["records"]:
    if record["id"] == "T23":
        record["quote"] = "is **the image**, not either cohomology group."
    assistant = turns[record["assistant"]]
    user = turns[record["user"]]
    if record["quote"] not in assistant["text"]:
        raise ValueError("Exact quotation missing: " + record["id"] + " " + repr(record["quote"]))
    qoffset = assistant["text"].index(record["quote"])
    record["assistant_node_id"] = assistant["node_id"]
    record["assistant_chain"] = assistant["chain"]
    record["user_node_id"] = user["node_id"]
    record["user_chain"] = user["chain"]
    record["quote_character_offset_in_message"] = qoffset
    record["quote_sha256_utf8"] = hashlib.sha256(record["quote"].encode("utf-8")).hexdigest()

episode_descriptions = {
"U0029": "A1007 announces the concrete sheaf lift; A1021 performs multiplication, gluing, support-prime restriction, nonsplitting, and the supported-null-cycle construction. T01 records its exact scope.",
"U0030": "A1022/A1032 announce the adelic reduction and retention of global norm errors; A1070 constructs HN/spectral filtration lifts, Rees defects, and slope diagnostics. The arithmetic theta specialization remains missing (T02–T04).",
"U0031": "A1071/A1098/A1106 announce the Rees amplification and trace work; A1140 supplies the uniform-family formulas and explicitly admits the absent global cohomological identification. T05–T06 preserve this limit.",
"U0032": "A1142/A1155 explicitly turn to the actual theta source; A1167 supplies the real extension-by-zero, raw analytic realization, smooth full-jet right inverse, and quotient Gram metric (T07–T09). This partly repairs U0031.",
"U0033": "A1169 promises original-congruence propagation; A1206 supplies the internal coequalizer, relation-labelled quotients, transition kernels, actual differentiated theta endpoint families, and support-preserving operators (T10–T11).",
"U0034": "A1210 announces reconciliation with the spectral paper; A1235 changes the primary target to unshifted Weil positivity, computes its exact shift correction, quotient correspondence, and residual/gap comparison, then leaves the central analytic term unestimated (T12–T15).",
"U0035": "This action-continuity correction has no separate substantive assistant reply before U0036. It jointly controls A1280, which acknowledges and repairs the program displacement (T16).",
"U0036": "A1280 restores cohomology/action/Lefschetz order, constructs correspondence saturation and full-jet traces, and retains moment endpoints and the explicit-formula terms. It explicitly leaves infinite cohomological trace and geometric endpoint-degree identifications unproved (T17–T18).",
"U0037": "This demand to apply the program is followed by U0038 before a substantive reply. A1304 responds to both with actual mixed-source endpoint-image and residue calculations; T19 records the result and overstatement.",
"U0038": "A1304 computes all masks, source-induced c_m, endpoint duality, and the J_g trace contraction. Its statement that Deligne had been applied is narrower in its own caveat and later corrected in A1361/A1427 (T20–T21).",
"U0039": "A1306 announces the requested audit; A1361 supplies concrete raw-realization, Frobenius, cohomological-degree, residue-orientation and checker corrections, and preserves their limited scope (T22–T26).",
"U0040": "A1362 announces source/F1/Deligne checking; A1427 supplies actual blueprint/prime/completion maps, proves raw-kernel nonvanishing, constructs balanced realization and finite-jet isomorphisms, and accurately limits its Deligne application status (T27–T30).",
}
user_ids = [key for key, value in turns.items() if value["role"] == "user"]
if user_ids != list(episode_descriptions):
    raise ValueError("User episode coverage mismatch")
expected_assistants = {r["assistant"] for r in data["records"]}
progress = [k for k,v in turns.items() if v["role"]=="assistant" and k not in expected_assistants]
episodes = []
for idx, uid in enumerate(user_ids):
    start = list(turns).index(uid)
    stop = list(turns).index(user_ids[idx+1]) if idx+1 < len(user_ids) else len(turns)
    followers = [key for key in list(turns)[start+1:stop] if turns[key]["role"]=="assistant"]
    episodes.append({
        "user":uid,"user_node_id":turns[uid]["node_id"],
        "following_assistants_before_next_user":followers,
        "disposition":episode_descriptions[uid],
        "records":[r["id"] for r in data["records"] if r["user"]==uid],
    })

coverage = {
    "source":str(SOURCE).replace("\\","/"),
    "source_bytes":len(raw),
    "source_sha256":hashlib.sha256(raw).hexdigest(),
    "source_characters_codepoints":len(source),
    "source_characters_utf16":len(source.encode("utf-16-le"))//2,
    "read_complete":True,
    "read_method":"Every character of the assigned segment read in contiguous chunks, old UTF-16 positions [0,14000),[14000,28000),…,[154000,163701); both primary source and canonical route read completely. Root then removed duplicated CR/LF translation; source messages and UUIDs unchanged. Current hash/offsets below recomputed.",
    "initial_read_segment_sha256":"7b748621e8a274e875d1e709820d51a53eb70e1acb347753dc934127bef2e5c3",
    "newline_repair":"Reported by root; final source hash recomputed. Quotes independently checked against final normalized source. Exact UUID and short passage are primary locators.",
    "retained_turns":len(turns),"users":len(user_ids),
    "assistants":sum(v["role"]=="assistant" for v in turns.values()),
    "substantive_assistant_turns":sorted(expected_assistants,key=lambda k:turns[k]["chain"]),
    "progress_assistant_turns_classified":progress,
    "quotes_exactly_validated":len(data["records"]),
    "message_hash_convention":"SHA-256 over readable-extraction message body after removing surrounding CR/LF separators; these are extraction hashes, not asserted to be original provider-message hashes.",
    "primary_source_sha256":"d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3",
    "canonical_route_sha256":"a8cdd18817a2c3596778c60a04ef9d76125a03ae5404759835a2bc2b18fa4c74",
}
for tid,turn in turns.items():
    turn["coverage_disposition"] = "user directive read verbatim" if turn["role"]=="user" else (
        "substantive reply audited in records " + ", ".join(r["id"] for r in data["records"] if r["assistant"]==tid)
        if tid in expected_assistants else "progress statement; classified in its controlling user episode; not treated as an independent completed theorem"
    )
payload={"coverage":coverage,"episodes":episodes,"records":data["records"],"turns":list(turns.values()),"additional_source_caution":{"location":"Primary (49); original arithmetic_input.tex (A10)–(A11); source_maps/VERIFIED_SOURCE_MAPS_FRAGMENT.tex sections 7–8","statement":"The finite-quotient argument alone does not construct a source eigenline. The actual original section does: R_ref=S_h Theta(R_Z(u)(D) phi_star), with the full epsilon=j_h(h/g) retained, gives sigma=q R_ref:E_h->Q[h(D)], Jbar_Z sigma=id. The proved finite source cocycle U_a R_ref-R_ref a^A=Theta c_a establishes Ubar_a sigma=sigma a^A for every a>0. Consequently L_rho=sigma iota_rho t_rho:C->Q and L_rho tensor r:C tensor r->Q tensor r are explicit nonzero equivariant injections. This closes the source-lift question; it is not left as an open gap.","scope":"The source representative R_ref need not be strictly equivariant in B: its exact discrepancy is the original boundary Theta c_a. The completed source lift retains g=2xi, all unit coefficients, full jets, tensor signs, and supported masks. No upper weight or purity estimate follows merely from this completed lift."}}
(OUT/"AUDIT_TYPED_ROUTE.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

parts = [
"# Passage-by-passage typed-route audit: U0029–U0040",
"",
"This is a mathematical continuation audit of the full assigned transcript segment. It makes no inference about the model's motives. Exact short passages and UUIDs below are checked against the final source extraction. Later corrections are part of each finding.",
"",
"## Coverage and source provenance",
"",
f"The assigned segment contains {len(user_ids)} user turns and {coverage['assistants']} assistant turns, including progress replies, in exact retained order. All were read. Final extraction: {len(raw):,} bytes, SHA-256 {coverage['source_sha256']}. The first full reading used the pre-newline-repair hash recorded in the JSON; root subsequently removed doubled CR/LF translation without changing message text. Quotes were revalidated after that repair.",
"",
"The complete primary Tau Base NOTE.md (SHA-256 d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3) and complete canonical source route (SHA-256 a8cdd18817a2c3596778c60a04ef9d76125a03ae5404759835a2bc2b18fa4c74) were read. Dependencies named in those sources are not thereby claimed as freshly read in full. The companion source-map verifier separately read support_diagrams.tex in full and supplied its proofs and source pins.",
"",
"The ledger's 'actual result' states the scope of the displayed argument, independently checking its elementary typed algebra. This audit does not claim a fresh independent verification of all cited external books, every historical package, or historical test counts. Root owns the separate analytic and replay lanes.",
"",
"## Controlling continuation",
"",
"The current primary construction is the structural blueprint map F1,τ→B_R and its spectrum map to bτ; the four-point upper-set chart; Aτ=RΓ(P,−); the distinct derived restriction resσ; the complete supported H¹ fibres carrying Q; Kτ≃SηW[1]; the full-jet map Q→A_Z; the residue injection into RHom(T,Kτ(L1)); and actual tensor powers Q⊗r. They are equations (1)–(50) of the primary source, not missing hypothetical objects.",
"",
"The earlier transcript predates that completed primary note. Its missing-arrow statements must be updated using the later exact constructions rather than repeated as the present state. In particular Boolean generic-stalk restriction is a proved comparison with Aτ, not its definition or replacement.",
"",
"An additional typed comparison is now completed: the finite-quotient argument alone places the socle eigenline in Aρ, but original arithmetic_input.tex (A10)–(A11) already supplies sigma=qR_ref:E_h→Q[h(D)], with Jbar_Z sigma=id and the complete unit epsilon=j_h(h/g). The proved finite cocycle U_aR_ref−R_ref a^A=Theta c_a establishes equivariance for every positive a. The full source lift is therefore Lρ=sigma iotaρ tρ:C→Q, and its tensor is a nonzero equivariant injection into Q⊗r. Section 8 of the companion source-map proof gives the complete original construction, source estimates, retained boundary, full jet insertion, explicit left inverse, and tensor homotopy signs. The earlier quotient argument's limited scope is retained; the source eigenline lift is no longer described as missing. The upper weight estimate remains a different calculation.",
"",
"## Every user-response episode",
""]
for ep in episodes:
    parts += [f"### {ep['user']} — {ep['user_node_id']}", "", ep["disposition"], ""]
parts += ["## Exact passage ledger", ""]
for r in data["records"]:
    parts += [
        f"### {r['id']}: {r['status']}",
        "",
        f"**User:** {r['user']} ({r['user_node_id']}, chain {r['user_chain']}). **Reply:** {r['assistant']} ({r['assistant_node_id']}, chain {r['assistant_chain']}).",
        "",
        "> " + r["quote"],
        "",
        "**Requested calculation.** " + r["request"],
        "",
        "**Original objects and maps.** " + r["objects"],
        "",
        "**Actual result and proof scope.** " + r["proved"],
        "",
        "**Left uncalculated.** " + r["missed"],
        "",
        "**Exact obstruction scope.** " + r["scope"],
        "",
        "**Later completion or correction.** " + r["later"],
        "",
        "**Concrete surviving derivation.** " + r["next"],
        "",
    ]
parts += [
"## Completed work delivered with this audit",
"",
"COMPLETED_MELLIN_CALCULATIONS.md proves the raw two-leg syzygy for every original differentiated-theta order m≥1, retains each mask, supplies the exact operator-balancing relation, and calculates the honest cycles in the saturated original two-leg source. It also uses the actual smooth full-jet right inverse to inject a free rank-Σmρ module into the raw Mellin-realization kernel. These results neither assume vanishing of the balanced kernel nor replace the theta source.",
"",
"source_maps/VERIFIED_SOURCE_MAPS.md proves the exact structural/base-restriction relation, Aτ and Kτ maps, all-support versus categorical kernels, and the opposite dual-index arrows. It additionally gives the explicit equivariant factorization Aρ→E→Aρ of J_g, with the retained coefficient mρuρ(0) and the actual socle eigenline inside the full nilpotent packet.",
"",
"## Prioritized continuation for integration",
"",
"1. Integrate the later primary Aτ/Kτ construction into the historical findings first. The missing right adjoint and finite residue-to-dual arrow are now completed; no generic-stalk substitute is needed.",
"2. Carry the raw and operator-balanced Mellin maps as separate exact comparisons. The raw kernel is provably nonzero; the balanced kernel requires actual calculation on Q with its topology and action. The attached all-order calculations give explicit subcomplexes and kernel elements.",
"3. Calculate the original theta relation estimates with all boundary terms, masses, Fourier/scaling factors, and the retained unshifted trace correction. The unproved uniform residual/gap term and unsupported norm transfer are identifiable interruptions, not complete results.",
"4. Establish the trace on a specified infinite arithmetic realization and account for its kernel/cone contribution. Finite full-jet traces and an absolutely convergent spectral distribution alone do not provide that theorem.",
"5. Retain valid obstructions at their exact scope: pointed-section nonsplitting, filtered-map nonstrictness, unshifted-form descent, raw realization non-quasi-isomorphism, and formal covariance without positivity. Each has an explicit surviving map in this ledger. None proves failure of the entire τ-base program.",
"",
"These are integration priorities for the original program. They are not conditional theorems in which a missing bound or vanishing is assumed.",
"",
"## Retained-turn index",
"",
"| Locator | UUID | Chain | Disposition |",
"|---|---|---:|---|",
]
for t in turns.values():
    parts.append(f"| {t['locator']} | {t['node_id']} | {t['chain']} | {t['coverage_disposition']} |")
(OUT/"AUDIT_TYPED_ROUTE.md").write_text("\n".join(parts)+"\n",encoding="utf-8")

user_blocks=[]
for i,m in enumerate(headers):
    if m[3]=="user":
        end=headers[i+1].start() if i+1<len(headers) else len(source)
        user_blocks.append(source[m.start():end])
(OUT/"USER_TURNS_VERBATIM.md").write_text("".join(user_blocks),encoding="utf-8",newline="")
(OUT/"COVERAGE.json").write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(coverage,ensure_ascii=False,indent=2))
