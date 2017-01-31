from dataflow.server import app

def main():
    app.run(ip='0.0.0.0', port=8080, debug=True)
