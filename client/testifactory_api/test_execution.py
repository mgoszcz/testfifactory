from testifactory.client.testifactory_api.api_methods.api import get
from testifactory.client.server_url.url import URL
from testifactory.client.testifactory_api.test_execution_result import TestExecutionResult


class TestExecution:
    def __init__(self, execution_id: int):
        self._execution = get(f'{URL}/executions/{execution_id}')
        self.id = self._execution.get('id')
        self.name = self._execution.get('name')
        self.results = self._get_results()

    def _get_results(self):
        results = []
        for case_id, result in self._execution.get('results').items():
            results.append(TestExecutionResult(case_id, result))
        return results
