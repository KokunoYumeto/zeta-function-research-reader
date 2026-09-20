"""Root active-check replay of the unchanged independent exact checker.

Each Assert node becomes a call to an explicit exception-raising check before
compilation. This preserves every original predicate under Python -O.
"""
from pathlib import Path
import argparse
import ast
import hashlib
import json

HERE = Path(__file__).resolve().parent
PIN = '880963f97f8e92fd2dd78a3e3795d0e1e178dc303914c93addfac33e9f316e93'
COUNT = 0


def active(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise RuntimeError(message)


class ActiveChecks(ast.NodeTransformer):
    def visit_Assert(self, node):
        message = 'Original predicate at line ' + str(node.lineno) + ': ' + ast.unparse(node.test)
        return ast.copy_location(ast.Expr(value=ast.Call(
            func=ast.Name(id='active', ctx=ast.Load()),
            args=[node.test, ast.Constant(value=message)], keywords=[])), node)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--negative-control', choices=('coefficient', 'kernel', 'cutoff'))
    control = parser.parse_args().negative_control
    raw = (HERE/'verification.py').read_bytes()
    active(hashlib.sha256(raw).hexdigest() == PIN, 'Original checker changed')
    tree = ActiveChecks().visit(ast.parse(raw))
    ast.fix_missing_locations(tree)
    active(not any(isinstance(n, ast.Assert) for n in ast.walk(tree)), 'Inactive check remains')
    env = {'__name__':'strict_dependency', '__file__':str(HERE/'verification.py'), 'active':active}
    exec(compile(tree, 'original_checker_with_active_predicates', 'exec'), env)
    if control == 'coefficient':
        original = env['exponential_coefficient']
        env['exponential_coefficient'] = lambda n: original(n) + (1 if n == 3 else 0)
    elif control == 'kernel':
        original = env['add_term']
        def changed(poly, degree, u_coefficient=0, constant=0):
            return original(poly, degree, u_coefficient+(1 if degree == 5 else 0), constant)
        env['add_term'] = changed
    elif control == 'cutoff':
        original = env['comb']
        env['comb'] = lambda n,k: original(n,k)+(1 if n == 0 else 0)
    names = ('kernel_identity', 'coefficient_checks', 'derivative_checks',
             'asymptotic_checks', 'cutoff_checks')
    for name in names:
        env[name]()
    print(json.dumps({'status':'passed', 'checks':COUNT, 'groups':len(names),
                      'original_checker_sha256':PIN, 'optimized_mode_safe':True,
                      'scope':'Exact finite predicates preserved; the all-domain proof remains in proof.tex.'}))


if __name__ == '__main__':
    main()
