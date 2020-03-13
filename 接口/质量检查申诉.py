import requests

session_url = 'http://wisdom_project.yxsoft.net/front/quality_appeal/add'

session_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '9532cxzK4wduJbHeUds32hwHICPwETRZUPG+dGYAaBzRVSFtBMpJPpfdCUW9JIuvoLO17Nw',
}

form_data = {
    "appeal_file": [],
    "reback_file": '[{"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/916b6b203b77ce0026381cf014f864a1.xlsx","file_name":"库存计算规则.xlsx","file_ext":"xlsx","width":0,"height":0}]',
    "appeal_reason": "申诉",
    "quality_check_id": 172

}


r = requests.post(
    session_url,
    headers=session_headers,
    data=form_data

)
print(r.json())