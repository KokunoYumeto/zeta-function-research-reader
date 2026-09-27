# Inventory of the S6 Zenodo record 10.5281/zenodo.22678442 (33 files) against downloaded copies.
# The MD5 list below was read from the record's public metadata on 26 September 2026.
# Usage: python3 s6r_record_inventory.py <folder with downloaded files>
# Prepared by Claude (Opus 5.5) for the S6 reader.
import sys, os, hashlib
RECORD = """
8ffd7d3af44c2d6cf058d9ca3439efdb 433025 00_s6_independent_correction_note_source_v1.0.zip
127608a682709335f38602641a8092e8 459566 00_s6_independent_correction_note_v1.0.pdf
8bf59820e2b0145840a7cde7eb3c8933 1746962 01_s6_peer_verification_monograph_v1.0.pdf
52b18355647fcf66e282d0ea63245cad 1355022 02_s6_annotated_manuscript_v1.0.pdf
84e045b850afb34b555ec033dc6a6d33 1114711 03_s6_clean_latex_reconstruction_v1.0.pdf
bd0c41f4d4d3f5f7eb64303b5ed246d2 20772174 04_s6_peer_verification_sources_and_evidence_v1.0.zip
f2eed888933143a3b1f9a46b32ee78b3 21147 05_s6_public_mathematical_provenance_v1.0.md
f808cedb31f43c10432024314105959d 12208 06_s6_public_provenance_receipt_v1.0.json
cea4ebab96b69c982171d86de35ae032 726648 07_s6_complete_sanitized_conversation_v1.0.jsonl
bbe0c5c586bd916c209052947bd50eae 3657 08_s6_complete_sanitized_conversation_receipt_v1.0.json
bb6a0c3a3482c80fceff9db8a5057d43 3601 09_s6_complete_sanitized_conversation_validation_v1.0.json
3f61d9e4a7eb3f1d9721208ba6f02445 2746333 10_s6_full_typed_record_annex_v2.0.jsonl.gz
762049c0a46345e6ada78db4dcd54207 5684 11_s6_full_typed_record_receipt_v2.0.json
59eb82ec0a7ee493be71e9289b76096a 2769 12_s6_full_typed_record_validation_v2.0.json
ecc8b56da877fd352a1fda803e5845f1 1782 13_s6_full_typed_record_parent_review_v1.0.json
fc50aea01252b9f47f1e76ebc1426d7c 288179 14_s6_topology_update_readers_guide_2026-09-05.pdf
56d95d87c668b9bb587d7286b6df3873 772261 15_s6_higher_torus_and_cusp_update_2026-09-05.pdf
a6faa3860c42f937e723b34d882d8116 898730 16_s6_cone_sphere_routes_2026-09-05.pdf
e99baa8151952ec6d8c89c9b8b5bd2c8 1824082 17_s6_selected_topology_sources_2026-09-05.zip
4ac644417f82559fdd4272ec9e79ad3c 5678 18_s6_topology_update_notes_2026-09-05.md
91680ecf0cfb229ee210f0c7f76c51c1 7136 19_s6_topology_update_manifest_2026-09-05.json
40ec187a4c47b362e0a755790d2237bc 302062 26_s6_key_advances_frozen_2026-09-06.pdf
dd623d5de81c06784ba35311f03dcfb7 14283 27_s6_key_advances_frozen_2026-09-06.tex
ebe511d8752399497d3281b063bcbede 174006509 28_s6_complete_public_project_frozen_2026-09-06.zip
512ab1902d74d4fcbf5cc15804d3a8cd 3707 29_S6_FROZEN_PROJECT_GUIDE_2026-09-09.md
f88836624febcb04828e009a4341552f 2669 30_S6_FROZEN_PROJECT_PACKAGE_MANIFEST_2026-09-09.json
3c2a79f133c0270d86bcb2194e6f026a 1463 CITATION.cff
058eef26b0db689b3cde2450ac7b6225 595 LICENSE_SCOPE.md
63e4013aab0efd5a42342fe67c96399a 2873 README.md
0b93b0dd763b40f81a0559a457aa9c80 2355 RIGHTS_AND_PROVENANCE.md
a4bd41728f9c514cde17ea496e939a5a 6342 s6_peer_verification_v1.0_ROUNDTRIP_RECEIPT.json
223fee28ef2db193b8b7fc782e5f09ac 1997 s6_peer_verification_v1.0_SHA256SUMS.txt
53f1c1dbddb80a6709eec10206bc26a9 2200 zenodo_metadata.v1.json
"""
rows = [line.split() for line in RECORD.strip().splitlines()]
folder = sys.argv[1] if len(sys.argv) > 1 else "."
match = missing = bad = 0
for md5, size, name in rows:
    path = os.path.join(folder, name)
    if not os.path.exists(path):
        missing += 1
        print(f"not local  {name} ({int(size):,} bytes)")
        continue
    h = hashlib.md5(open(path, "rb").read()).hexdigest()
    if h == md5 and os.path.getsize(path) == int(size):
        match += 1
    else:
        bad += 1
        print(f"MISMATCH   {name}")
print(f"{len(rows)} files in the record: {match} local copies match (MD5 and size), {missing} not local, {bad} mismatches")
print("ALL LOCAL COPIES MATCH" if bad == 0 else "SOME COPIES DIFFER")
