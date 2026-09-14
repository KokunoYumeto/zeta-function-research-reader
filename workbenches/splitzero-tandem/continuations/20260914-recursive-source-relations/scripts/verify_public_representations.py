"""Verify exact lossless public evidence representations without changing files."""
from pathlib import Path
import gzip,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def identity(p):
    h=hashlib.sha256();size=0
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b);size+=len(b)
    return {'bytes':size,'sha256':h.hexdigest()}
def verify():
    m=json.loads((ROOT/'PUBLIC_REPRESENTATIONS.json').read_bytes())
    for row in m['representations']:
        p=(ROOT/row['stored_public_path']).resolve()
        if not p.is_relative_to(ROOT) or identity(p)!=row['compressed']:raise RuntimeError('stored evidence identity differs')
        h=hashlib.sha256();size=0
        with gzip.open(p,'rb') as f:
            for b in iter(lambda:f.read(1048576),b''):h.update(b);size+=len(b)
        if {'bytes':size,'sha256':h.hexdigest()}!=row['decompressed']:raise RuntimeError('decompressed evidence identity differs')
    return {'status':'PASS','lossless_representations':len(m['representations']),'files_changed':False}
def main():
    print(json.dumps(verify()))
if __name__=='__main__':main()
