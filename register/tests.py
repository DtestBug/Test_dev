from django.test import TestCase

# Create your tests here.
import requests
# ipt_data = input('请输入：')
ipt_data = 'test0003'

url = 'http://127.0.0.1:8000/register/'

data = {
    "username": ipt_data,
    "password": '123456',
    "email": '%s@163.com' % ipt_data,
    "password_confirm": '123456',
}

res = requests.post(url, data)
print(res.json())
print(res.status_code)