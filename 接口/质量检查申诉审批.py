import requests
import time

session_url = 'http://wisdom_project.yxsoft.net/front/quality_Appeal_approval/check'

session_headers = [
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '2a15RHv88ArWFfuXbFQtt+qB66zGTDuEFg+b6UoNNLHrQyTDucELdeqZZQk9ac2veqqeH8zg'
    },
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'c5632XwHyFZs7X/1P2jG+Vh4fmhwUaSnmW+TpxAnAOwDI67+esR1ITJzggQDmnhUH6vgSaS9'
    },
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
    "approval_opinions": "无意见",
    "check": 1,
    "quality_check_reback": 0,
    "quality_appeal_id": 133
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
