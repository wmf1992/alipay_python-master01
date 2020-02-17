import requests
import time

session_url = 'http://wisdom_project.yxsoft.net/front/contract_apply_approval/add'

session_headers = [
    # {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'access-token': 'dfc7vFXsi5Q/s5RuF1aqVwoqX/nBx162i2izEMwebGv2pi6xz0EMaygIbv6Xc2TI4nWBeVM'
    # },
    # {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'access-token': '824705R+n8tFLOnsQ5/UfQT1CqPTGQwva58y0VZq5bi98h2+3JnNEuGdkiBF5dNDVk5kyPw'
    # },
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '9aa3XwD6DSteYR6g1Xvv35VVqJN20fIDCEbJG4IEzR5gZAOmPtwLfrjmMTto6Sp9lTCh6a6C'
    },
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'd2bdlZDUPv5NUoD3ec4xuHe1Cpogl/4TezlDuQuiZUT0odG1OFM2pec4N+rU+AdutPx0jyUB'
    }
]

form_data = {
    "apply_record_id": 122,
    "approval_opinions": "无意见",
    "check": 1,
    "back": "",

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
