import sys
from dataflow.server import app
from dataflow.scribe import convert_json_to_py, read_data

def runapp():
    app.run(ip='0.0.0.0', port=8080, debug=True)


def main():
    args = list(sys.argv)
    if len(args) > 1:
        if args[1] == 'gen':
            if len(args) > 2:
                name = args[2]
                data = read_data(name)
                print(convert_json_to_py(data))
    else:
        runapp()
