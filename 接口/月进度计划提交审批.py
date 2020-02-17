import requests
# 3、发起人提交审批
session_url = 'http://wisdom_project.yxsoft.net/front/progress_plan/submit'
session_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'f315zU1q9p5hiZgF/9ZvXb8TU7XqzsFvCTNTcmmBNIwU5PajU316QBCN3lNskaiR2i+4jw',
}
form_data = {
    "plan_id":187,
}

r = requests.post(
    session_url,
    headers=session_headers,
    data=form_data

)
print(r.json())
