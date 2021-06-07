from testifactory.client.testifactory_api.api_methods.api import get
from testifactory.client.testifactory_api.test_case_properties import TestCaseProperties
from testifactory.client.server_url.url import URL
from testifactory.client.testifactory_api.test_execution import TestExecution


class TestCase:
    def __init__(self, case_id: int):
        self._case = get(f'{URL}/cases/{case_id}')
        self.id = self._case.get('id')
        self.name = self._case.get('name')
        self.url = self._case.get('url')
        self.properties = TestCaseProperties(self._case.get('properties'))
        self.executions = self._get_executions()

    def _get_executions(self):
        executions = []
        for execution in self._case.get('executions'):
            executions.append(TestExecution(execution))
        return executions

