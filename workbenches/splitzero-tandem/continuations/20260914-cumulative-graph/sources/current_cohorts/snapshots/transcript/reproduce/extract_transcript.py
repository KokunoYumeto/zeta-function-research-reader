"""Decode the share page's embedded React Router table without executing it."""
import collections, hashlib, json, pathlib, re, sys
from bs4 import BeautifulSoup

sys.setrecursionlimit(30000)
OUT = pathlib.Path(__file__).resolve().parents[1] / 'sources'
raw = (OUT / 'share_page.html').read_bytes()
soup = BeautifulSoup(raw.decode('utf-8'), 'html.parser')
scripts = [s.get_text() for s in soup.find_all('script')]
chunks = []
for script in scripts:
    prefix = 'window.__reactRouterContext.streamController.enqueue('
    if script.startswith(prefix):
        chunks.append(json.loads(script[len(prefix):script.rindex(')')]))
table = json.loads(chunks[0])
memo = {}
def decode(index):
    if index == -5:
        return None
    if index < 0:
        return {'__stream_special__': index}
    if index in memo:
        return memo[index]
    val = table[index]
    if isinstance(val, dict):
        out = {}; memo[index] = out
        for key, ref in val.items():
            if not key.startswith('_'):
                raise ValueError(('unexpected table key',key))
            out[decode(int(key[1:]))] = decode(ref)
        return out
    if isinstance(val, list):
        out = []; memo[index] = out
        for ref in val:
            out.append(decode(ref) if isinstance(ref,int) else {'__stream_literal__': ref})
        return out
    memo[index] = val
    return val

root = decode(0)
route = root['loaderData']['routes/share.$shareId.($action)']
data = route['serverResponse']['data']
(OUT/'share_conversation.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8',newline='')
mapping = data['mapping']
chain=[]; node=data['current_node']; seen=set()
while node is not None:
    if node in seen: raise ValueError('cycle in parent chain')
    seen.add(node)
    record=mapping[node]; chain.append(record); node=record.get('parent')
chain.reverse()
linear=data['linear_conversation']
linear_ids=[r['id'] for r in linear]
chain_ids=[r['id'] for r in chain]
manifest={
 'share_url':'https://chatgpt.com/share/'+route['sharedConversationId'],
 'title':data['title'],'backing_conversation_id':data.get('backing_conversation_id'),
 'current_node':data['current_node'],'source_bytes':len(raw),
 'source_sha256':hashlib.sha256(raw).hexdigest(),
 'mapping_nodes':len(mapping),'linear_nodes':len(linear),'current_parent_chain_nodes':len(chain),
 'linear_order_matches_parent_chain':linear_ids==chain_ids,
 'reversed_linear_matches_parent_chain':linear_ids[::-1]==chain_ids,
 'linear_ids_missing_from_chain':list(set(linear_ids)-set(chain_ids)),
 'chain_ids_missing_from_linear':list(set(chain_ids)-set(linear_ids)),
 'stream_closed':any('streamController.close()' in s for s in scripts),
 'stream_chunk_count':len(chunks),
 'scope':'Complete embedded mapping and current parent chain. No linked attachment bodies are inferred from message text.'
}
records=[]; user_count=0; assistant_count=0; role_counts=collections.Counter(); channel_counts=collections.Counter()
all_text=['# Complete shared transcript: current parent chain','', 'Message text is retained verbatim; headings below are extraction locators. All roles and channels are retained.','']
human_text=['# User and assistant conversation','', 'Chronological current parent chain; mathematical Markdown remains verbatim. Tool and other records are preserved separately.','']
turn_dir=OUT/'turns'; turn_dir.mkdir(exist_ok=True)
for ordinal,record in enumerate(chain,1):
    msg=record.get('message')
    if not msg: continue
    role=msg.get('author',{}).get('role','unknown'); channel=msg.get('channel')
    role_counts[role]+=1; channel_counts[str(channel)]+=1
    content=msg.get('content',{})
    parts=content.get('parts',[])
    if content.get('content_type')=='text':
        text='\n'.join(p if isinstance(p,str) else json.dumps(p,ensure_ascii=False,indent=2) for p in parts)
    else:
        text=json.dumps(content,ensure_ascii=False,indent=2)
    if role=='user':
        user_count+=1; locator=f'U{user_count:04d}'
    elif role=='assistant':
        assistant_count+=1; locator=f'A{assistant_count:04d}'
    else: locator=f'N{ordinal:05d}'
    header=f'## {locator} | node {record["id"]} | {role} | channel {channel} | chain {ordinal}'
    block=header+'\n\n'+text+'\n\n'
    all_text.append(block)
    if role in ('user','assistant'): human_text.append(block)
    entry={'locator':locator,'chain_ordinal':ordinal,'node_id':record['id'],'message_id':msg.get('id'),'role':role,'channel':channel,'recipient':msg.get('recipient'),'create_time':msg.get('create_time'),'content_type':content.get('content_type'),'text':text,'text_sha256':hashlib.sha256(text.encode()).hexdigest(),'characters':len(text),'metadata':msg.get('metadata',{})}
    records.append(entry)
    if role in ('user','assistant'):
        (turn_dir/(locator+'.md')).write_text(block,encoding='utf-8',newline='')
manifest.update(role_counts=dict(role_counts),channel_counts=dict(channel_counts),messages=len(records),user_turns=user_count,assistant_messages=assistant_count)
(OUT/'transcript_records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8',newline='')
(OUT/'TRANSCRIPT_FULL.md').write_text('\n'.join(all_text),encoding='utf-8',newline='')
(OUT/'TRANSCRIPT_USER_ASSISTANT.md').write_text('\n'.join(human_text),encoding='utf-8',newline='')
(OUT/'TRANSCRIPT_USER_INPUTS.md').write_text('\n'.join((turn_dir/(r['locator']+'.md')).read_text(encoding='utf-8',newline='') for r in records if r['role']=='user'),encoding='utf-8',newline='')
(OUT/'COVERAGE.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8',newline='')
print(json.dumps({k:v for k,v in manifest.items() if not isinstance(v,list)},indent=2,ensure_ascii=False))
print('Set differences:',len(manifest['linear_ids_missing_from_chain']),len(manifest['chain_ids_missing_from_linear']))
for r in records[-8:]: print(r['locator'],r['role'],r['channel'],r['characters'],r['text'][:220].replace('\n',' '))
