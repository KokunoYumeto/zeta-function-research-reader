import collections, hashlib, json, pathlib

root=pathlib.Path(__file__).resolve().parents[1]
p=root/'sources'
data=json.loads((p/'share_conversation.json').read_text(encoding='utf-8'))
records=json.loads((p/'transcript_records.json').read_text(encoding='utf-8'))
coverage=json.loads((p/'COVERAGE.json').read_text(encoding='utf-8'))
def require(value, message):
    if not value: raise RuntimeError(message)
raw=(p/'share_page.html').read_bytes()
require(len(raw)==14471434,'raw byte count')
require(hashlib.sha256(raw).hexdigest()==coverage['source_sha256'],'source hash')
ids=[]; cur=data['current_node']; visited=set()
while cur is not None:
    require(cur not in visited,'cycle')
    visited.add(cur); ids.append(cur); cur=data['mapping'][cur].get('parent')
ids.reverse()
require(ids==[x['id'] for x in data['linear_conversation']],'entire original linear ordering')
require(set(ids)==set(data['mapping']),'entire mapping coverage')
require(len(ids)==5350,'node count')
rr=[]
for n,node_id in enumerate(ids,1):
    node=data['mapping'][node_id]; msg=node.get('message')
    if not msg: continue
    content=msg.get('content',{})
    text=('\n'.join(x if isinstance(x,str) else json.dumps(x,ensure_ascii=False,indent=2) for x in content.get('parts',[])) if content.get('content_type')=='text' else json.dumps(content,ensure_ascii=False,indent=2))
    r=records[len(rr)];rr.append(r)
    require(r['node_id']==node_id and r['chain_ordinal']==n,'locator correspondence')
    require(r['text']==text,'exact message text')
    require(r['text_sha256']==hashlib.sha256(text.encode()).hexdigest(),'message hash')
    if r['role'] in ('user','assistant'):
        block=(p/'turns'/(r['locator']+'.md')).read_bytes().decode('utf-8')
        require(block.split('\n\n',1)[1]==text+'\n\n','individual turn text')
require(len(rr)==len(records)==5349,'all message records')
require(collections.Counter(r['role'] for r in records)==collections.Counter(coverage['role_counts']),'role counts')
vis=json.loads((p/'visible_records.json').read_text(encoding='utf-8'))
require(len(vis)==215,'visible coverage')
require([r for r in records if r['role']=='user' or (r['role']=='assistant' and r['content_type']=='text' and r['recipient'] in (None,'all'))]==vis,'exact visible selection')
receipt={'status':'PASS','raw_sha256':coverage['source_sha256'],'nodes':len(ids),'messages':len(records),'visible_records':len(vis),'checks':['exact full parent-chain/linear/mapping equality','raw bytes and SHA256','all 5349 texts and text hashes','all individual turn files','role counts','full visible prose selection']}
(p/'TRANSCRIPT_VERIFICATION.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
