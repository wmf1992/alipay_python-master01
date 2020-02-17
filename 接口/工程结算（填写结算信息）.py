import requests
import time

session_url = 'http://wisdom_project.yxsoft.net/front/project_settlement_approval/add'

session_headers = [
    # {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'access-token': 'd8f4p5uf0wHaqcPvRqzOWwCPwV36TQOX+9ONmY4qIR+5tjmcKU3cSopvOIk85IIrzaAKB78'
    # },
    # {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'access-token': '824705R+n8tFLOnsQ5/UfQT1CqPTGQwva58y0VZq5bi98h2+3JnNEuGdkiBF5dNDVk5kyPw'
    # },
    # {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'access-token': '9aa3XwD6DSteYR6g1Xvv35VVqJN20fIDCEbJG4IEzR5gZAOmPtwLfrjmMTto6Sp9lTCh6a6C'
    # },
    # {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'access-token': 'd2bdlZDUPv5NUoD3ec4xuHe1Cpogl/4TezlDuQuiZUT0odG1OFM2pec4N+rU+AdutPx0jyUB'
    # }
]

form_data = {
    "files": [],
    "images": [],
    "approval_opinions": "无",
    "score": 3,
    "check": 1,
    "project_settlement_id": 81
}


# r = requests.post(
#     session_url,
#     headers=session_headers,
#     data=form_data
#
# )
#批量执行审批操作
for session_header in session_headers:
    r = requests.post(
        session_url,
        headers=session_header,
        data=form_data

    )
    print(r.json())
    time.sleep(3)
