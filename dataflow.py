from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from bottle import get, run, post, static_file, request


@get('/')
def main_page():
    with open('main.html', 'r') as fl:
        html = fl.read()
    return html

@post('/makescript')
def makescript():
    print(request.json)
    return ''


#########################################################################
# STATIC ROUTES
#########################################################################
@get("/static/<filepath:path>")
def css(filepath):
    return static_file(filepath, root="/home/arjoonn/dev/dataflow/static")
run(host='0.0.0.0', port=8080, debug=True)
