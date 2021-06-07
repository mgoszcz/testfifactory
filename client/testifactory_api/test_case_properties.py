from typing import Dict


class TestCaseProperties:
    def __init__(self, properties: Dict):
        self.test_steps = properties.get('steps')
        self.automation = properties.get('automation')
