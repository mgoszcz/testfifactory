import json

from flask import Flask, jsonify

app = Flask(__name__)

cases = []
executions = []


@app.route('/testifactory')
def index():
    """home page"""
    return "Welcome to Testifactory!"


@app.route('/testifactory/cases')
def get_cases():
    return jsonify(cases)


@app.route('/testifactory/cases/<int:case_id>', methods=['GET'])
def get_task(case_id):
    return jsonify(cases[str(case_id)])


@app.route('/testifactory/executions')
def get_executions():
    return jsonify(executions)


def load_backup():
    global cases
    with open('cases.json') as file:
        data = json.load(file)
    cases = data


if __name__ == '__main__':
    load_backup()
    app.run(debug=True)
