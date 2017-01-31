import os
import json
from functools import reduce
from copy import deepcopy
from dataflow import config

def read_data(name):
    "READ JSON DATA and return a dict"
    with open(os.path.join(config.static_dir, 'scripts', name), 'r') as fl:
        data=  json.loads(fl.read())
    return data

def wrap_in_function(block):
    "Wrap a block in a function and return the code as string"
    inps = [v['label']+'=None' for v in block['properties']['inputs'].values()]
    outs = [v['label'] for v in block['properties']['outputs'].values()]
    kr='(' + ', '.join(inps) + ')'
    return_args=', '.join(outs)

    params = dict(fname=block['properties']['title'],
            kr=kr,
            indented_code=block['program'].replace('\n', '\n    '),
            return_args=return_args)
    function = '''
def {fname}{kr}:
    {indented_code}
    return {return_args}
    '''.format(**params)
    return function

def get_sources(data):
    "Return the sources present in the data"
    ops = data.get('operators')
    sources = dict()
    for key, op in ops.items():
        klass = op['properties']['class']
        if klass == config.source_box_class:
            sources[key] = op
    return sources


def are_inputs_satisfied(opname, data, traversal):
    ops, links = data['operators'], data['links']
    op = ops[opname]
    links_to_op = {k: v for k, v in links.items() if v['toOperator'] == opname}
    dependents = [i['fromOperator'] for i in links_to_op.values()]
    if dependents:
        done_boxes = list(reduce(lambda x, y: list(x)+list(y), [i.keys() for i in traversal]))
        retval = all(i in done_boxes for i in dependents)
        return retval
    else:
        return True




def order_link_traversal(data):
    "Return an ordered list of link traversal"
    traversal = []
    links, ops = deepcopy(data['links']), deepcopy(data['operators'])
    current_step = deepcopy(get_sources(data))
    while len(ops) > 0:
        next_step, this_step, poplist = {}, {}, set()

        for link in links.values():
            frm = link['fromOperator']
            to = link['toOperator']
            if frm in current_step:
                inp_satisfied = are_inputs_satisfied(frm, data, traversal)
                if inp_satisfied:
                    this_step.update({frm: ops[frm]})
                    next_step.update({to: ops[to]})
                    poplist.add(frm)
        current_step = next_step
        for name in poplist:
            ops.pop(name)
        if this_step:
            traversal.append(this_step)
        elif not this_step and not next_step:
            traversal.append(deepcopy(ops))
            ops = {}
    return traversal

def generate_calls_from_traversal(traversal, data):
    "Return a string which has perfectly chained calls as per the traversal"
    calls, variable_map = [], dict()
    # Generate a variable map
    var_name_count = 0
    for link in data['links'].values():
        frm, to = link['fromOperator'], link['toOperator']
        frm_con, to_con = link['fromConnector'], link['toConnector']
        variable_map[frm, frm_con] = 'var' + str(var_name_count)
        variable_map[to, to_con] = 'var' + str(var_name_count)
        var_name_count += 1
    # rename the variables and generate calls
    total_steps = len(traversal)
    for stepindex, step in enumerate(reversed(traversal)):
        for opname, op in step.items():
            inps = op['properties']['inputs']
            outs = op['properties']['outputs']
            args = ', '.join([variable_map[opname, key] for key in inps.keys()])
            outs = ', '.join([variable_map[opname, key] for key in outs.keys()])
            if outs:
                this_call = '{outs} = {name}({args})'.format(outs=outs,
                        name=opname, args=args)
            else:
                this_call = '{name}({args})'.format(outs=outs,
                        name=opname, args=args)


            calls.append(this_call)
        calls.append('# Step --------------------------{}'.format(total_steps - stepindex))
    calls = '\n'.join(reversed(calls))
    return calls

def convert_json_to_py(data):
    script = str(config.code_imports)  # Defensive copy
    for key, op in data['operators'].items():
        script += '\n## ' + key
        script += wrap_in_function(op)
    script += '\n'
    # Functions are defined. Now we define the calls
    traversal = order_link_traversal(data)
    calls = generate_calls_from_traversal(traversal, data)
    script += '\n#########################\n#MAIN\n#########################\n'
    script += '\n# Parts within steps can be run in parallel\n\n'
    script += calls
    return script
