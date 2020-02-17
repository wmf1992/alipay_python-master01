import requests

session_url = 'http://wisdom_project.yxsoft.net/front/project_settlement/add'

session_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '98bfw9pmlKftaWGjz6/ea7FpXQjMUoaw6ViWwlqegne4aHtpTzDKdd3cQB4b4vUVBVRXsg',
}

form_data = {
    "start_time": "2020-02-11",
    "end_time": "2020-02-29",
    "contract_id": 232,
    "labor_contract_id": 242,
    "building_id": 131,
    "sub_project_ids": 6,
    "compliant": "委托人1",
    "project_side": "劳务公司110501",
    "pay_rate": 90,
    "labour_contract_id":"" ,
    "settlement_list[0][construction_content]": "粉刷墙壁",
    "settlement_list[0][quantities_count]": 1,
    "settlement_list[0][quantities_unit]": 1,
    "settlement_list[0][unit_price]": 200,
    "settlement_list[0][desc]": "无",
}


r = requests.post(
    session_url,
    headers=session_headers,
    data=form_data

)
print(r.json())