import json

from flask import Flask, jsonify

app = Flask(__name__)

cases = []
executions = []


@app.route('/testifactory')
def testifactory():
    """home page"""
    return "Welcome to Testifactory!"


@app.route('/testifactory/cases')
def get_cases():
    return jsonify(cases)


@app.route('/testifactory/cases/<int:case_id>', methods=['GET'])
def get_case(case_id):
    for case in cases:
        if case.get('id') == case_id:
            return jsonify(case)


@app.route('/testifactory/executions/<int:execution_id>', methods=['GET'])
def get_execution(execution_id):
    for execution in executions:
        if execution.get('id') == execution_id:
            return jsonify(execution)



@app.route('/testifactory/executions')
def get_executions():
    return jsonify(executions)


def load_data():
    global cases, executions
    with open('cases.json') as file:
        cases = json.load(file)
    with open('executions.json') as file:
        executions = json.load(file)


if __name__ == '__main__':
    load_data()
    app.run(debug=True)
