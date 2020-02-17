import requests

session_url = 'http://wisdom_project.yxsoft.net/front/meterial_plan/add'

# session_headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'access-token': '5146aDP2vTYGPjsxMwpOGtJWezeHajNiStUSGmBxmja13CO8xBZrBjnVcHOsM5jsNggoqA'
# }

session_headers = [
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '98bfw9pmlKftaWGjz6/ea7FpXQjMUoaw6ViWwlqegne4aHtpTzDKdd3cQB4b4vUVBVRXsg'
    }

]
form_data = {
    "contract_id": 41,
    "warehouse_id": 6,
    "building_id": 9,
    "plan_time": '2019-09',
    "meterial_list": '[{"meterial_code":"CL12050005","meterial_name":"法国牛排","parent_type_id":6,"second_type_id":8,"type_id":112,"meterial_spec":"500g","meterial_unit":"盒","image":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/e60795e82fd44d539ebb15c1bef823c2.jpg","is_need_approval":1,"type_text":"复合材料三级","meterial_id":13,"desc":"","plan_num":2,"enter_time":"2020-02-11"}]'

}

for session_header in session_headers:
    r = requests.post(
        session_url,
        headers=session_header,
        data=form_data

    )
    print(r.json())