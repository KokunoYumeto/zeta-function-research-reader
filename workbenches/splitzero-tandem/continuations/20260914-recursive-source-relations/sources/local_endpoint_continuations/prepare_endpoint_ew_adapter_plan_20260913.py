"""Prepare byte/AST-exact EW public replay adapters; never execute checkers.

Only writes its own work/endpoint_reader_prepared_20260913 directory and receipt.
The current cumulative reader and all publication stages are outside its write set.
"""
from __future__ import annotations
import ast
import copy
import hashlib
import json
from pathlib import Path

WORK = Path(__file__).resolve().parent
OUT = WORK / 'endpoint_reader_prepared_20260913'
PREFIX = 'sources/local_endpoint_continuations/'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def pin(path):
    data = path.read_bytes()
    return {'path':path.name, 'bytes':len(data), 'sha256':sha(data)}

def alias_receipt(name):
    source = WORK / name
    raw = source.read_bytes()
    before = json.loads(raw)
    after = copy.deepcopy(before)
    edits = []
    def edit(container, key, value, pointer):
        original = container[key]
        if original != value:
            edits.append({'pointer':pointer, 'original_value_sha256':sha(str(original).encode()),
                          'replacement':value})
            container[key] = value
    edit(after, 'python_executable', '{python}', '/python_executable')
    for index, job in enumerate(after['jobs']):
        command = job['command']
        require(command[0] == before['python_executable'], 'unexpected Python command')
        edit(command, 0, '{python}', f'/jobs/{index}/command/0')
        slot = 2 if job['optimized'] else 1
        basename = command[slot].replace('\\','/').rsplit('/',1)[-1]
        require(basename == source.with_suffix('.py').name, 'unexpected checker command')
        edit(command, slot, PREFIX + basename, f'/jobs/{index}/command/{slot}')
    # Reversibly remove exactly the declared locator slots and compare every other value.
    def strip(value):
        value = copy.deepcopy(value)
        value.pop('python_executable')
        for job in value['jobs']:
            job.pop('command')
        return value
    require(strip(before) == strip(after), 'non-location receipt value changed')
    for a,b in zip(before['jobs'], after['jobs']):
        require(a['result'] == b['result'], 'mathematical payload changed')
        # The command options, including optimization and mutant choices, also stay exact.
        aargs = a['command'][3 if a['optimized'] else 2:]
        bargs = b['command'][3 if b['optimized'] else 2:]
        require(aargs == bargs, 'checker arguments changed')
    public = (json.dumps(after, indent=2)+'\n').encode()
    target = OUT / 'public_metadata' / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(public)
    return {'source':pin(source), 'public':pin(target), 'prepared_path':target.relative_to(WORK).as_posix(),
            'archive_path':PREFIX+name, 'edits':edits,
            'all_other_values_equal':True, 'all_job_mathematical_payloads_equal':True,
            'historical_execution_code_and_dependency_pins_retained':True}

def adapt_code(name, replacements):
    source = WORK / name
    raw = source.read_bytes()
    text = raw.decode('utf-8')
    before = ast.parse(text)
    assigned = {}
    for node in ast.walk(before):
        if isinstance(node, ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
            if node.targets[0].id in replacements:
                require(isinstance(node.value,ast.Constant) and isinstance(node.value.value,str), 'pin not literal')
                require(node.targets[0].id not in assigned, 'duplicate pin assignment')
                assigned[node.targets[0].id] = node.value.value
    require(set(assigned)==set(replacements), 'missing pin assignment')
    edits=[]
    for variable,new in replacements.items():
        old=assigned[variable]
        old_statement=f'{variable} = "{old}"'
        new_statement=f'{variable} = "{new}"'
        require(text.count(old_statement)==1, 'nonunique literal source edit')
        text=text.replace(old_statement,new_statement,1)
        edits.append({'assigned_name':variable,'original_literal':old,'public_literal':new})
    public=text.encode('utf-8')
    after=ast.parse(text)
    for node in ast.walk(after):
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
            variable=node.targets[0].id
            if variable in assigned:
                require(node.value.value==replacements[variable], 'public literal mismatch')
                node.value.value=assigned[variable]
    require(ast.dump(before,include_attributes=False)==ast.dump(after,include_attributes=False), 'AST changed outside declared pin literals')
    target=OUT/'adapted_public_checkers'/name
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(public)
    return {'source':pin(source),'public':pin(target),'prepared_path':target.relative_to(WORK).as_posix(),
            'original_archive_path':PREFIX+'original_checkers/'+name,
            'adapted_archive_path':PREFIX+name,'edits':edits,
            'full_AST_equal_after_reversing_declared_literals':True,
            'all_undeclared_source_bytes_preserved':True,
            'execution_status':'prepared adapted code; not executed by this task'}

def main():
    fixture=alias_receipt('gamma_endpoint_window_bridge_fixture_20260913.json')
    supplement=alias_receipt('gamma_endpoint_window_bridge_supplement_20260913.json')
    adapters=[adapt_code('gamma_endpoint_window_bridge_supplement_20260913.py',
                        {'SAVED_SHA':fixture['public']['sha256']}),
              adapt_code('gamma_endpoint_window_bridge_projection_review_final_numeric_20260913.py',
                        {'RECEIPT_HASH':supplement['public']['sha256']})]
    receipt={'schema':'endpoint-ew-public-replay-adapter-plan-v1',
             'status':'prepared-only; no checker execution and no cumulative/stage edits',
             'metadata':[fixture,supplement], 'adapters':adapters,
             'exact_unadapted_runtime_files':[
                 pin(WORK/'gamma_endpoint_window_bridge_fixture_20260913.py'),
                 pin(WORK/'gamma_endpoint_window_bridge_20260913.tex'),
                 pin(WORK/'gamma_endpoint_window_bridge_projection_review_calibration_20260913.py')],
             'dependency_edges':[
                 {'consumer':adapters[0]['adapted_archive_path'],'input':fixture['archive_path'],
                  'required_sha256':fixture['public']['sha256']},
                 {'consumer':adapters[0]['adapted_archive_path'],'input':PREFIX+'gamma_endpoint_window_bridge_fixture_20260913.py',
                  'required_sha256':'56be6cbd66ffd5272440e95f01104a0154bf0c4b5a2bab1d0a60cb7945071048'},
                 {'consumer':adapters[1]['adapted_archive_path'],'input':supplement['archive_path'],
                  'required_sha256':supplement['public']['sha256']},
                 {'consumer':adapters[1]['adapted_archive_path'],'input':PREFIX+'gamma_endpoint_window_bridge_20260913.tex',
                  'required_sha256':'e8d6152532c98532a062b5840834d934b28f29490ec926f47c2bce1af3493854'}],
             'historical_evidence_rule':'Aliased historical receipts preserve their original executed checker and input hashes; these are original execution records, not claims that adapted code ran. New public execution must record actual adapted code and companion hashes separately.',
             'fresh_runtime_rule':'Run jobs in isolated public support trees. Do not overwrite an input historical receipt by dispatching --replay in its directory. Direct per-mode stdout jobs retain original test semantics.'}
    target=WORK/'endpoint_ew_public_adapter_plan_20260913.json'
    target.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'receipt':target.name,'sha256':sha(target.read_bytes()),
                      'metadata_aliases':len(receipt['metadata']),'adapters':len(adapters),
                      'checker_executions':0},indent=2))

if __name__=='__main__':
    main()
