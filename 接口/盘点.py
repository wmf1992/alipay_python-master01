import requests

session_url = 'http://wisdom_project.yxsoft.net/front/inventory/add'

session_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '98bfw9pmlKftaWGjz6/ea7FpXQjMUoaw6ViWwlqegne4aHtpTzDKdd3cQB4b4vUVBVRXsg',
}

form_data = {
    "access_code": "",
    "access_time": '2019-09',
    "warehouse_id":6,
    "meterial_list[0][id]": 3,
    "meterial_list[0][meterial_code]": 'HDPE',
    "meterial_list[0][meterial_name]": "臻力 塑料垃圾桶",
    "meterial_list[0][parent_type_id]": 6,
    "meterial_list[0][second_type_id]": 8,
    "meterial_list[0][type_id]": 112,
    "meterial_list[0][meterial_spec]": "240L",
    "meterial_list[0][meterial_unit]": "套",
    "meterial_list[0][image]": "https://img0.912688.com/4a478b1f-b471-4b11-b7e4-452a20c35b89.jpg#",
    "meterial_list[0][is_need_approval]": 0,
    "meterial_list[0][type_text]": "复合材料三级",
    "meterial_list[0][meterial_id]": 3,
    "meterial_list[0][meterial_total_stock]": 12,
    "meterial_list[0][stock_num]": 12,
    "meterial_list[0][diff_num]": 3,
    "meterial_list[0][desc]":"",
    "meterial_list[0][num]": 15,
    "meterial_list[0][product_time]": "2020-02-12",
    "meterial_list[0][expire_time]": "2020-02-28",
    "meterial_list[0][unit_price]": 44

}


r = requests.post(
    session_url,
    headers=session_headers,
    data=form_data

)
print(r.json())