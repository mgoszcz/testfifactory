import requests

from testifactory.client.server_url.url import URL


def get_cases():
    cases = requests.get(f'{URL}/cases')
    return cases.json()


def get_case(case_id):
    case = requests.get(f'{URL}/cases/{case_id}')
    return case.json()


def get_case_name(case_id):
    case = requests.get(f'{URL}/cases/{case_id}').json()
    return case.get('name')


def get_case_url(case_id):
    case = requests.get(f'{URL}/cases/{case_id}').json()
    return case.get('url')


def get_case_steps(case_id):
    case = requests.get(f'{URL}/cases/{case_id}').json()
    return case.get('properties').get('steps')


def get_case_automation_status(case_id):
    case = requests.get(f'{URL}/cases/{case_id}').json()
    return case.get('properties').get('automation')


print(get_cases())
for id in range(1, 4):
    print(get_case(id))
