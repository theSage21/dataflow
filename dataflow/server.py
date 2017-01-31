import os
import json
from bottle import static_file, request, Bottle
from dataflow import config, scribe


def readhtml(file):
    with open(os.path.join(config.template_dir, file), 'r') as fl:
        html = fl.read()
    return html

def savejson(file, data):
    with open(os.path.join(config.static_dir, 'scripts', file), 'w') as fl:
        fl.write(json.dumps(data))

#########################################################################
# INTERFACE
#########################################################################
app = Bottle()

@app.get('/loadscript/<name>')
@app.get('/')
def main_page(name=None):
    html = readhtml('main.html')
    if name is not None:
        data = scribe.read_data(name)
        data = 'var existingdata = ' + json.dumps(data) + ';'
        html = html.replace('//placeholderfordata', data)
    return html

@app.get('/scripts/')
def scriptlist():
    string = '<tr><td><a href=/static/scripts/{name}>{name}</td>'
    string +='<td><a href=/loadscript/{name}>{name}</a></td>'
    string +='<td><a href=/makepy/{name}>{name}</a></td></tr>'
    scripts = [string.format(name=i) for i in os.listdir('static/scripts')]
    scripts = '\n'.join(scripts)
    html = readhtml('scripts.html')
    html = html.replace('<Areafortablerows>', scripts)
    return html

@app.post('/savejson')
def savescript():
    name = request.json['scriptname']
    savejson(name, request.json)
    return ''

@app.get('/makepy/<name>')
def makepy(name):
    data = scribe.read_data(name)
    code = scribe.convert_json_to_py(data)
    html = '<html><body><pre>' + code + '</pre></body></html>'
    return html

#########################################################################
# STATIC ROUTES
#########################################################################
@app.get("/static/<filepath:path>")
def css(filepath):
    return static_file(filepath, root=config.static_dir)
