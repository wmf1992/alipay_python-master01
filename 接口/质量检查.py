import requests

session_url = 'http://wisdom_project.yxsoft.net/front/quality_check/add'

session_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '98bfw9pmlKftaWGjz6/ea7FpXQjMUoaw6ViWwlqegne4aHtpTzDKdd3cQB4b4vUVBVRXsg',
}

form_data = {
    "sub_project_id": 6,
    "tender_contract_id": 78,
    "building_id": 17,
    "check_time": "2020-02-12",
    "labour_score": 93,
    "owner_score": 90,
    "lack_num": 0,
    "deal_num": 0,
    "undeal_num": 0,
    "modify_ids": "82,79",
    "check_desc": "无",
    "check_file": '[{"file_name":"组织架构导入成员下载模板.xlsx","file_ext":"xlsx","width":0,"height":0,"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/fb341e023efbc28b149a86b5935e8675.xlsx"}]',
    "labour_file": '[{"file_name":"库存计算规则.xlsx","file_ext":"xlsx","width":0,"height":0,"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/916b6b203b77ce0026381cf014f864a1.xlsx"}]',
    "owner_file": '[{"file_name":"组织架构导入成员下载模板.xlsx","file_ext":"xlsx","width":0,"height":0,"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/fb341e023efbc28b149a86b5935e8675.xlsx"}]',
    "labour_contract_id":"",
    "goodness_score": 97

}


r = requests.post(
    session_url,
    headers=session_headers,
    data=form_data

)
print(r.json())