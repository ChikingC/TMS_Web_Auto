import unittest
from selenium.webdriver.common.by import By
from case import Function
import time

URL = 'https://test-multi-hq.hero-cloud.cn/accounts/hqqccn1/eng/tms/operation'

class testdemo(unittest.TestCase):

        def setUp(self) -> None:
            self.name = '1111'
            self.chromedriver = Function.get_url(URL)
            self.chromedriver.implicitly_wait(10)
            Function.login(self.chromedriver, 'abel', '1')
            Function.select_outlet(self.chromedriver)

        def test1(self):

            print('{}'.format(self.name))

        def test2(self):
            print('22')
            print('{}'.format(self.name))



        def test_03(self):
            self.chromedriver.find_element(By.XPATH, '//input[@name="username"]').send_keys("alisa")
            self.chromedriver.find_element(By.XPATH, '//input[@name="password"]').send_keys("1")
            self.chromedriver.find_element(By.XPATH, '//button[text()="Submit"]').click()
            time.sleep(3)
            print('验证成功')

        def tearDown(self) -> None:
            self.chromedriver.close()
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(testdemo('test1'))
    suite.addTest(testdemo('test2'))
    suite.addTest(testdemo('登录后询问权限进入营业区_01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
'''

# suite()
