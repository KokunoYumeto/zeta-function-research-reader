# Inventory of the Yang-Mills Zenodo record 10.5281/zenodo.22883643 (43 files) against the repository
# KokunoYumeto/yang-mills-interacting-workbench at commit fa79faf and against downloaded copies.
# The MD5 list below was read from the record's public metadata on 26 September 2026.
# Usage: python3 ymr_record_inventory.py <path to a clone of the repository> [<folder with downloaded files>]
# Prepared by Claude (Opus 5.5) for the Yang-Mills reader.
import sys, os, subprocess, hashlib
RECORD = """
783d1f6e75afb9d64e36b6568dcf9c19 636393 01_quantum_blocking_local_energy_2026-09-08.pdf
f0b0d237155d2826c444c6d926ffe0c1 841819 02_spatial_continuum_checkpoint_2026-09-08.pdf
8c2ba2fcdb03c40fb53cb265ccb370d6 2066890 03_complete_checkpoint_sources_2026-09-08.zip
6b54f25bfc33c07f97613f619eb7e607 756811 04_quantum_author_packet_2026-09-08.zip
127674c438ad8b2d870696d67d1e96f5 707690 05_quantum_full_local_spectrum_53p_2026-09-08.pdf
1b501f88e369c25f2974e592cadfb132 1097486 06_spatial_continuum_108p_2026-09-08.pdf
2f78e4d014fda0b53fdaf58690619bd4 877234 07_volume_uniform_vacuum_62p_2026-09-08.pdf
9b70e477cad82fe95d07362a36e787e6 87146164 08_entire_public_overleaf_workbench_c501b11f.zip
d0b8282cbeadd2c4de65e98aaa8d3c99 7657 09_FULL_WORKBENCH_READING_MAP.md
6c6a9525f9c4a41daa164adfceaee112 8090 10_ENTIRE_WORKBENCH_EDITION_GUIDE.md
454b9a0fdd684719c1fb998631707f4a 3893 11_FULL_WORKBENCH_RELEASE_MANIFEST.json
6a7f749e372e30bb05d3195a00576dcf 22546 AI_READING_INDEX.md
c63dda7abbfc8547afc9b335bef2b2cd 6460 ALPOGE_ATTRIBUTION_20260921.md
5f07b5c0894424bed3daa93a021fcb16 4041 READER_PROVENANCE.json
a4227dc33390844411a7b887ca35c1f9 9294 README.md
aa720054940467cf48a1ebcb9d8e3321 1267 RELEASE_MANIFEST.json
4f103724c28a0ac2d980a37720d324fd 55396 SOURCE_MANIFEST.json
28b84617710225cc5efb7e96c9c0d6c8 5932 YM_CURRENT_READING_GUIDE_20260909.md
47b273c3da94d1fb76df31587668e2e7 6182 YM_READING_GUIDE_20260917.md
8b379d1e8a41133291a9cdc2b458bb40 13937 YM_READING_GUIDE_20260921.md
7d9e97824ff7230ef507a450f5c23aa1 12498 YM_READING_GUIDE_20260921_FIFTH.md
5b71c13cfcf0cc1e22960f3a40c17eb1 887944 quantum_coarse_graining.pdf
cbc8f064f220b7e0fbb08e5ef98655ab 837741 quantum_interacting_tensor_band.pdf
27b7b31154fabb00ac1923f9c0624456 778286 quantum_nonabelian_vertex.pdf
21747f2eee08175030036245c379cd1b 1243123 spatial_continuum.pdf
eb02bbedf9355bd504161ec208362d61 1015304 volume_uniform_vacuum.pdf
6fd0b1e4774a453c3b3451f9a414a753 8737128 yang_mills_complete_available_sources_20260916.zip
84a4882456cc4a8a1862bd850112cfed 11674732 yang_mills_cumulative_20260921_fifth_reference.zip
79958d5ed0820fcf24a14c118bf987a1 9009616 yang_mills_cumulative_20260921_heat.zip
19cf7aa4cfd90069a05c6a9451dbf232 10096063 yang_mills_cumulative_20260921_volume.zip
43fae6520e88c07d7e71bf098240efa3 6178283 yang_mills_current_sources_2026-09-09.zip
47dfe21e30054fbd2f5f4c43dd6b7f75 59174 yang_mills_fifth_reference_20260921.md
9a2edf240bfe1b7ec99a8109a4d781f8 164325 yang_mills_fifth_reference_20260921.pdf
868ca1d90348bbb4c2a3ce9547e92ea2 97610 yang_mills_fifth_reference_20260921.tex
5097d23bd97a7fc25ea20ff8e2f256ac 92201 yang_mills_fifth_reference_20260921_reader_sources.zip
07dc41a6bb34fd22c1c03a710ffab3ee 112346 yang_mills_heat_volume_20260921.md
5e3ae20c7aea7a29778e1b2bcff7482b 217617 yang_mills_heat_volume_20260921.pdf
0def677864a92ee471013ed4f8062771 166376 yang_mills_heat_volume_20260921.tex
fdb4d45e6c3e5dc29f7bdf5ce0e083c1 153636 yang_mills_heat_volume_reader_sources_20260921.zip
7dcd46be3ebe666dda8acb89b0066602 1309150 yang_mills_quartic_comparison_sources_20260917.zip
010336b1c2529f2af2140398dd93504d 236579 yang_mills_quartic_cube_reader.pdf
a3642538f3f12483771d9ea329f62730 181839 yang_mills_quartic_cube_reader.tex
3945830e7dc2abf332b24d43d28c6f89 1079797 yang_mills_web_continuation.pdf
"""
want = {}
for line in RECORD.strip().splitlines():
    md5, size, key = line.split(' ', 2); want[key.strip()] = (md5, int(size))
repo = sys.argv[1]
head = subprocess.run(['git', '-C', repo, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
ls = subprocess.run(['git', '-C', repo, 'ls-tree', '-r', '-l', 'HEAD'], capture_output=True, text=True).stdout.splitlines()
bysize = {}
for k, (m, s) in want.items(): bysize.setdefault(s, []).append((m, k))
p = subprocess.Popen(['git', '-C', repo, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
found = {}
for line in ls:
    meta, path = line.split('\t', 1); mode, typ, sha, size = meta.split()
    if typ != 'blob' or size == '-' or int(size) not in bysize: continue
    p.stdin.write((sha + '\n').encode()); p.stdin.flush()
    hdr = p.stdout.readline().split(); n = int(hdr[2]); data = p.stdout.read(n); p.stdout.read(1)
    h = hashlib.md5(data).hexdigest()
    for m, k in bysize[n]:
        if m == h: found.setdefault(k, path)
p.stdin.close()
print(f"repository HEAD {head}: {len(found)} of {len(want)} record files are byte-identical to a file at HEAD")
dl = sys.argv[2] if len(sys.argv) > 2 else None
okdl = 0; missing = []
for k in sorted(want):
    if k in found: print("  in repository:", k, "<-", found[k]); continue
    if dl and os.path.exists(os.path.join(dl, k)):
        h = hashlib.md5(open(os.path.join(dl, k), 'rb').read()).hexdigest()
        ok = (h == want[k][0]); okdl += ok
        print("  downloaded   :", k, "MD5", "matches the record" if ok else "DIFFERS")
    else:
        missing.append(k); print("  not local    :", k, f"({want[k][1]} bytes)")
print(f"{len(found)} in the repository, {okdl} downloaded with matching MD5, {len(missing)} not local: {missing}")
