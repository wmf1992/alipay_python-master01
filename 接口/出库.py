import requests

session_url = 'http://wisdom_project.yxsoft.net/front/outbound/add'

session_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'b50cSJIIXtGbFMCd1pL+Er00xdF3LPW88ZMu2rcdK89/ZCXLfP5SDT8jii0LAzgCu226KbA',
}

form_data = {
    "plan_id": 288,
    "access_code": "",
    "access_time": '2020-02-11',
    "warehouse_id":6,
    "building_id":9,
    "meterial_list": '[{"meterial_id":13,"meterial_name":"法国牛排","meterial_code":"CL12050005","num":1,"froze_num":2,"stock_num":18,"image":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/e60795e82fd44d539ebb15c1bef823c2.jpg"}]',
    "images":'[{"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/466f868eeae9c2b23e575dd4f9277420.jpg","file_name":"QQ图片20191017144139.jpg","file_ext":"jpg","width":0,"height":0,"type":0}]',
    "files":'[{"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/916b6b203b77ce0026381cf014f864a1.xlsx","file_name":"库存计算规则.xlsx","file_ext":"xlsx","width":0,"height":0,"type":1}]'

}


r = requests.post(
    session_url,
    headers=session_headers,
    data=form_data

)
print(r.json())