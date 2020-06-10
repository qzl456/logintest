import requests

url = "http://ihrm-test.itheima.net/api/sys/login"
json= {"mobile":"13800000002","password":"123456"}
response = requests.post(url=url,json=json)

print(response.json())