import os
import json
from bottle import static_file, request, Bottle
from dataflow import config


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

@app.get('/')
def main_page():
    scripts = ''
    html = readhtml('main.html')
    html = html.replace('{generatedscripts}', scripts)
    return html

@app.get('/scripts/')
def scritlist():
    scripts = ['<tr><td><a href=/static/scripts/{}>{}</td></tr>'.format(i, i) for i in os.listdir('static/scripts')]
    scripts = '\n'.join(scripts)
    html = readhtml('scripts.html')
    html = html.replace('<Areafortablerows>', scripts)
    return html

@app.post('/makescript')
def makescript():
    name = request.json['scriptname']
    savejson(name, request.json)
    return ''


#########################################################################
# STATIC ROUTES
#########################################################################
@app.get("/static/<filepath:path>")
def css(filepath):
    return static_file(filepath, root=config.static_dir)
