import os
import json
# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from bottle import get, run, post, static_file, request


#########################################################################
# FLOW generator
#########################################################################

def to_code(chart):
    """convert chart to code"""


#########################################################################
# INTERFACE
#########################################################################
@get('/')
def main_page():
    scripts = ''
    with open('main.html', 'r') as fl:
        html = fl.read()
    html = html.replace('{generatedscripts}', scripts)
    return html

@get('/scripts/')
def scritlist():
    scripts = ['<tr><td><a href=/static/scripts/{}>{}</td></tr>'.format(i, i) for i in os.listdir('static/scripts')]
    scripts = '\n'.join(scripts)
    with open('scripts.html', 'r') as fl:
        html = fl.read()
        html = html.replace('<Areafortablerows>', scripts)
    return html

@post('/makescript')
def makescript():
    name = request.json['scriptname']
    print(type(request.json))
    with open('static/scripts/{}'.format(name), 'w') as fl:
        fl.write(json.dumps(request.json))
    return ''


#########################################################################
# STATIC ROUTES
#########################################################################
@get("/static/<filepath:path>")
def css(filepath):
    return static_file(filepath, root="/home/arjoonn/dev/dataflow/static")
if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)
