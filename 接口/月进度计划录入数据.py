import requests
# 2、试验员录入数据
session_url = 'http://wisdom_project.yxsoft.net/front/progress_plan/testSave'
session_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '2ff7MQ0GpGN/EowbjrlQoxhtMIJf+08tpCi73eE6QNbHakgEuIxTpLbgy5zDe7PK1brCJA',
}
form_data = {
    "plan_id":195,
    "test_info[0][test_name]":"打扫地板",
    "test_info[0][plan_test_time]":"2020-02-14"
}

r = requests.post(
    session_url,
    headers=session_headers,
    data=form_data

)
print(r.json())


