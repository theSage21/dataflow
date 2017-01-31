import json
#from dataflow import to_code

def comment(string):
    comment = '\n'
    comment += '#'*20 + '\n'
    comment += '#  ' + string.strip() + '\n'
    comment += '#'*20 + '\n'
    return comment

class Graph:
    def __init__(self, ops, links, name):
        self.name = name
        self.verts = set()
        self.edges = set()

        # setup
        for key, v in ops.items():
            p = v['properties']
            tuple_ = [key, p['title'],
                    [i['label'] for i in p['inputs'].values()],
                    [i['label'] for i in p['outputs'].values()],
                    v['program']]
            self.verts.add(tuple(tuple_))

        for key, v in links.items():
            tuple_ = [key, v['fromOperator'], v['fromConnector'],
                    v['toOperator'], v['toConnector']]
            self.edges.add(tuple(tuple_))

    def get_neighbours(self, vid):
        to_ids = set()
        for tuple_ in self.edges:
            _0, _1, fo, fc, to, tc = tuple_
            if fo == vid:
                to_ids.add(to)
        N = [i for i in self.verts if i[0] in to_ids]
        return N



def to_code(chart):
    text = ''
    return text


with open('static/scripts/script', 'r') as fl:
    chart = json.load(fl)

script = to_code(chart)
print('-'*30)
print(script)
