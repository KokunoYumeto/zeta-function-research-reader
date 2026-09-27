import subprocess, zipfile, io, hashlib
repo = '<clone of KokunoYumeto/yang-mills-interacting-workbench at fa79faf>'
want = {}
for line in open('<MD5 list of the Zenodo record 22883643>'):
    md5, size, key = line.split(' ', 2); want[key.strip()] = (md5, int(size))
local = {'01_','02_','03_','04_','05_','06_','07_','08_','09_','10_','11_','AI_','ALP','REA','REL','SOU','YM_CURRENT','YM_READING_GUIDE_20260921.md','YM_READING_GUIDE_20260921_FIFTH','README.md'}
targets = {k: v for k, v in want.items() if not k.startswith(('quantum_', 'spatial_', 'volume_', 'yang_mills_', 'YM_READING_GUIDE_20260917'))}
print(len(targets), "record files not at HEAD")
bysize = {}
for k, (m, s) in targets.items(): bysize.setdefault(s, []).append((m, k))
ls = subprocess.run(['git', '-C', repo, 'ls-tree', '-r', '-l', 'HEAD'], capture_output=True, text=True).stdout.splitlines()
zips = [l.split('\t', 1)[1] for l in ls if l.split('\t', 1)[1].endswith('.zip')]
found = {}
for zpath in zips:
    data = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + zpath], capture_output=True).stdout
    try: z = zipfile.ZipFile(io.BytesIO(data))
    except Exception as e: print("skip", zpath, e); continue
    for info in z.infolist():
        if info.file_size in bysize:
            h = hashlib.md5(z.read(info)).hexdigest()
            for m, k in bysize[info.file_size]:
                if m == h: found.setdefault(k, []).append(zpath.split('/')[-1] + ':' + info.filename)
for k in sorted(targets): print(("INSIDE A ZIP AT HEAD " if k in found else "not found          ") + k + ("  <- " + found[k][0] + (f" (+{len(found[k])-1} more)" if len(found[k]) > 1 else "") if k in found else ""))
print(len(found), "of", len(targets), "occur byte-identically inside archives committed at HEAD")
