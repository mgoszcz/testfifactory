"""
Print report from Testifactory
"""
from testifactory.client.testifactory_api.testifactory import Testifactory

t_factory = Testifactory()

print('1. Print all cases id and names and urls')
for case in t_factory.test_cases:
    print(f'\tID: {case.id} Name: {case.name} URL: {case.url}')

print('2. Print all cases properties')
for case in t_factory.test_cases:
    print(f'\tTestcase ID: {case.id}')
    print(f'\t\tAutomated: {case.properties.automation}')
    print(f'\t\tTest steps:')
    for step in case.properties.test_steps:
        print(f'\t\t\t{step}')

print('3. Print name and url of test case "3"')
case = t_factory.test_case(3)
print(f'\tName: {case.name}, URL: {case.url}')

print('4 Print name and results of execution "4"')
execution = t_factory.test_execution(4)
print(f'\tName: {execution.name}')
for result in execution.results:
    print(f'\t\tTest Case: {t_factory.test_case(result.test_case_id).name}')
    print(f'\t\tResult: {result.result}')

print('5. Print all executions report')
for execution in t_factory.test_executions:
    print(f'\tExecution ID: {execution.id} Execution Name: {execution.name}')
    print(f'\t\tResults:')
    for result in execution.results:
        print(
            f'\t\t\tTest Case ID: {result.test_case_id} Test Case Name: {t_factory.test_case(result.test_case_id).name}')
        print(f'\t\t\t\tResult: {result.result}')
