import os
import json
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from bottle import get, run, post, static_file, request


@get('/')
def main_page():
    scripts = ''
    with open('main.html', 'r') as fl:
        html = fl.read()
    html = html.replace('{generatedscripts}', scripts)
    return html

@get('/scripts/')
def scritlist():
    scripts = ['<li><a href=/static/scripts/{}>{}</a></li>'.format(i, i) for i in os.listdir('static/scripts')]
    scripts = '\n'.join(scripts)
    scripts = '<ul>'+scripts+'</ul>'
    html = '<html><body><h1>Scripts</h1>{}</body></html>'.format(scripts)
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
run(host='0.0.0.0', port=8080, debug=True)
