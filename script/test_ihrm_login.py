# 导包
import unittest, requests
from parameterized import  parameterized

# 创建测试类
from utils import read_data


class Test_Ihrm_Login(unittest.TestCase):
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    def tearDown(self):
        pass
    @parameterized.expand(read_data())
    def test01_login(self,case_name,request_body,message):
        json = request_body
        response = requests.post(url=self.login_url, json=json)

        print(response.json())

        self.assertIn(message, response.json().get("message"))
