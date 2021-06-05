import requests

from server.server_url.url import URL


def get_cases():
    cases = requests.get(f'{URL}/testifactory/cases')
    return cases.json()

def get_case(case_id):
    case = requests.get(f'{URL}/testifactory/cases/{case_id}')
    return case.json()

print(get_cases())
for id in range(1,4):
    print(get_case(id))
