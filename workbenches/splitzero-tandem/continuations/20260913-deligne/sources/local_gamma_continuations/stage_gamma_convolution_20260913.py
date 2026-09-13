from pathlib import Path, PurePosixPath
import hashlib, json, re, shutil, stat, zipfile

W = Path(r'workspace:')
source = Path(r'corpus:Chatnotes\CHat translates and clean\Noether Multilingual\Tau_Gamma_Convolution_Descent_2026-09-13.zip')
dest = W / 'output/split_zero_rh_tandem_2026-09-12/sources/web_gamma_convolution_delivery'
root = dest.resolve()
def sha(b): return hashlib.sha256(b).hexdigest()
with zipfile.ZipFile(source) as archive:
    seen = set(); members = []
    for info in archive.infolist():
        name = info.filename
        pure = PurePosixPath(name)
        if '\\' in name or '\x00' in name or pure.is_absolute() or any(p in ('', '.', '..') for p in pure.parts):
            raise ValueError(('unsafe member', name))
        if not pure.parts or pure.parts[0] != 'Tau_Gamma_Convolution_Descent':
            raise ValueError(('wrong top directory', name))
        for part in pure.parts:
            if ':' in part or part.endswith(('.', ' ')) or re.match(r'^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\.|$)', part, re.I):
                raise ValueError(('unsafe Windows path', name))
        key = str(pure).casefold()
        if key in seen: raise ValueError(('duplicate/case collision', name))
        seen.add(key)
        mode = info.external_attr >> 16
        if stat.S_ISLNK(mode) or (stat.S_IFMT(mode) not in (0, stat.S_IFREG, stat.S_IFDIR)):
            raise ValueError(('non-regular member', name, mode))
        target = (dest / str(pure)).resolve()
        if not target.is_relative_to(root): raise ValueError(('escaped path', name))
        if info.is_dir(): continue
        data = archive.read(info)  # ZipFile validates member CRC on complete read.
        members.append((info, target, data))
    bad = archive.testzip()
    if bad is not None: raise ValueError(('CRC failure', bad))
    if sum(i.file_size for i,_,_ in members) > 30_000_000: raise ValueError('unexpected expansion')
    for info,target,data in members:
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            if target.read_bytes() != data: raise ValueError(('existing file differs', str(target)))
        else:
            with target.open('xb') as out: out.write(data)
    archive_target = dest / source.name
    archive_bytes = source.read_bytes()
    if archive_target.exists():
        if archive_target.read_bytes() != archive_bytes: raise ValueError('archive copy differs')
    else:
        with archive_target.open('xb') as out: out.write(archive_bytes)
    package = dest / 'Tau_Gamma_Convolution_Descent'
    manifest = json.loads((package/'MANIFEST.sha256.json').read_text(encoding='utf-8'))
    receipt = {'archive_name': source.name, 'archive_bytes': len(archive_bytes),
      'archive_sha256': sha(archive_bytes), 'member_count':len(members), 'safety': {
      'paths_contained':True,'windows_reserved_names_rejected':True,'case_collisions_rejected':True,
      'symlinks_rejected':True,'all_member_crcs_verified':True},
      'files':[{'archive_entry':i.filename,'staged_relative_path':i.filename,'bytes':len(b),'sha256':sha(b)} for i,_,b in members],
      'source_manifest_shape':type(manifest).__name__}
    target = dest/'LOCAL_STAGING_PROVENANCE.json'
    raw=(json.dumps(receipt,indent=2)+'\n').encode()
    if target.exists():
        if target.read_bytes()!=raw: raise ValueError('provenance differs')
    else:
        with target.open('xb') as out: out.write(raw)
    print(json.dumps({'staging':str(dest),'archive_sha256':sha(archive_bytes),'members':len(members),
      'note_sha256':sha((package/'NOTE.tex').read_bytes()),'note_lines':len((package/'NOTE.tex').read_text().splitlines()),
      'provenance_sha256':sha(raw),'manifest':manifest},indent=2))
