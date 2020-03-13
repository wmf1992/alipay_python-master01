import requests
import time

session_url = 'http://wisdom_project.yxsoft.net/api/quality_Appeal_approval/check'

session_headers = [
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'd8f4p5uf0wHaqcPvRqzOWwCPwV36TQOX+9ONmY4qIR+5tjmcKU3cSopvOIk85IIrzaAKB78'
    },
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'bfcey7919nPJEEjjlXjUufo3k1unipdrniv8bwuUEXxI0bTLNlCp9i0iAUXkX3VHpwQMIvLp'
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
    "files": [{"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/916b6b203b77ce0026381cf014f864a1.xlsx","file_name":"库存计算规则.xlsx","file_ext":"xlsx","width":0,"height":0,"type":1}],
    "images": [],
    "reback_file": [{"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/466f868eeae9c2b23e575dd4f9277420.jpg","file_name":"QQ图片20191017144139.jpg","file_ext":"jpg","width":0,"height":0}],
    "reback_score": 99,
    "approval_opinions": "无意见",
    "check": 1,
    "quality_check_reback": 1,
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
