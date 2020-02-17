import requests
from  configToken import session_headers,url
session_url = url+'/admin/warehousing/add'
#session_url = 'http://wisdom_project.yxsoft.net/front/warehousing/add'

session_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '5146aDP2vTYGPjsxMwpOGtJWezeHajNiStUSGmBxmja13CO8xBZrBjnVcHOsM5jsNggoqA',
}

form_data = {
    "purchasing_id": 149,
    "is_end_purchasing": 0,
    "access_code": "",
    "access_time": '2020-02-12',
    "warehouse_id":26,
    "building_id":3,
    "warehouse_name": "仓库2020010201",
    "building_id": 143,
    "meterial_list[0][meterial_id]": 112,
    "meterial_list[0][num]": 1,
    "meterial_list[0][meterial_name]": "GUTFUG",
    "meterial_list[0][meterial_code]": "R454RYGFHG",
    "meterial_list[0][image]": "http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/64e8c6f5dc105152bfaca08dec2b9f4f.gif",
    "meterial_list[0][unit_price]": 12,
    "meterial_list[0][product_time]": "2020-02-01",
    "meterial_list[0][expire_time]": "2020-02-14"
}


r = requests.post(
    session_url,
    headers=session_headers,
    data=form_data

)
print(r.json())