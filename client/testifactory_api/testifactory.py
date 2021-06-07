from testifactory.client.testifactory_api.api_methods.api import get
from testifactory.client.testifactory_api.test_case import TestCase
from testifactory.client.server_url.url import URL
from testifactory.client.testifactory_api.test_execution import TestExecution


class Testifactory:
    def __init__(self):
        self._cases = []

    @property
    def test_cases(self):
        json_cases = get(f'{URL}/cases')
        return [TestCase(case.get('id')) for case in json_cases]

    @property
    def test_executions(self):
        json_executions = get(f'{URL}/executions')
        return [TestExecution(execution.get('id')) for execution in json_executions]

    def test_case(self, test_case_id):
        return TestCase(test_case_id)

    def test_execution(self, execution_id):
        return TestExecution(execution_id)

