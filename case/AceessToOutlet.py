from selenium.webdriver.common.by import By
from case.Function import Function
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
# 1.导包
import unittest

URL = 'https://test-multi-hq.hero-cloud.cn/accounts/hqqccn1/eng/tms/operation'
ex_path='F:\chromedriver\chromedriver109.0.5414.120\chromedriver'
# 2.自定义测试类，需要继承unittest 模块中的 Testcase

class TestDemo(unittest.TestCase):
    #方法初始化，每个方法都需要输入网页地址
    # @classmethod 类夹具@classmethod


    @classmethod
    def setUpClass(self) -> None:
        self.test = 2
        self.chromedriver = Function.get_url(URL)
        self.chromedriver.implicitly_wait(10)
        Function.login(self.chromedriver, 'abel', '1')
        Function.select_outlet(self.chromedriver)
    @classmethod
    def tearDownClass(self) -> None:
        #self.chromedriver.close()
        print('teardown {}'.format(self.test))


    '''
    def setUp(self) -> None:
        self.chromedriver = Function.get_url(URL)
        self.chromedriver.implicitly_wait(10)
        Function.login(self.chromedriver, 'alisa', '1')
        Function.select_outlet(self.chromedriver)

    # 方法结束初始化，运行结束后关闭网址
    def tearDown(self) -> None:
        #self.chromedriver.close()
        print('teardown')

    '''


    def test_01(self):


        self.chromedriver.find_element(By.XPATH, '//input[@name="username"]').send_keys("1")
        self.chromedriver.find_element(By.XPATH, '//input[@name="password"]').send_keys("1")
        time.sleep(3)
        self.chromedriver.find_element(By.XPATH,'//button[text()="Submit"]').click()
        print('验证成功')


    '''预定操作'''
    def test_02(self,TableNumber='120'):
        self.chromedriver.maximize_window()
        #actiondriver=self.chromedriver.find_element(By.XPATH,'//div[@class="sc-jgPznn fPjavr"]')
        actiondriver = self.chromedriver.find_element(By.XPATH,'//span[text()="{}"]'.format(TableNumber))
        ActionChains(self.chromedriver).move_to_element(actiondriver).context_click().perform()
        self.chromedriver.find_element(By.XPATH,'//span[@icon="add"]').click()
        self.chromedriver.find_element(By.XPATH, '//input[@name="username"]').send_keys("1")
        self.chromedriver.find_element(By.XPATH, '//input[@name="password"]').send_keys("1")
        self.chromedriver.find_element(By.XPATH, '//button[text()="Submit"]').click()
        #查看是否为指定桌台
        Actul_Result = self.chromedriver.find_element(By.XPATH, '//span[@class="bp3-text-overflow-ellipsis bp3-fill"]').text
        self.assertEqual(Actul_Result,TableNumber)

        #查看是否重复预定（1）弹出Reservation Full 的提示语
        try:
            res = self.chromedriver.find_element(By.XPATH,"//h4[@class='bp3-heading']").text
            print(res)
            if(res):
                self.chromedriver.find_element(By.XPATH,'//button[text()="Yes"]').click()
        except:
            print('table not full')

        # 查看是否重复预定（1）弹出Reservation Full 的提示语
        #WebDriverWait(self.chromedriver,20).until(lambda driver:self.chromedriver.find_element(By.XPATH,"//h4[@class='bp3-heading']"))

        time.sleep(3)
    '''预定桌台'''
    def test_03(self):
        self.chromedriver.find_element(By.XPATH,'//input[@id="lastName"]').send_keys('Abby')
        time.sleep(3)
        self.chromedriver.find_element(By.XPATH, '//div[@number="Abby0518"]').click()
        self.chromedriver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div[2]/div[1]/table/tbody/tr[14]').click()
        time.sleep(3)
        self.chromedriver.find_element(By.XPATH, '//div[text()="Email"]').click()

        time.sleep(3)
        self.chromedriver.find_element(By.XPATH, '//button[text()="Save"]').click()
        self.chromedriver.find_element(By.XPATH, '//button[text()="Close"]').click()
        self.chromedriver.find_element(By.XPATH, '//span[@icon="time"]').click()
    #查看字样
    def test_04(self):
        self.chromedriver.find_element(By.XPATH,'//span[@icon="calendar"]').click()
        ele = self.chromedriver.find_element(By.XPATH,'//div[@role="separator"]')
        ActionChains(self.chromedriver).click_and_hold(ele).move_by_offset(-600,200).release().perform()
        ele = self.chromedriver.find_element(By.XPATH,'//span[@icon="info-sign"]')
        ActionChains(self.chromedriver).move_to_element(ele).perform()
        res=self.chromedriver.find_element(By.XPATH,'//div[@class="bp3-popover-content"]').text
        self.assertEqual(res,'Reserved/Blocked/Total')





# 3.使用套件添加用例
'''
def test1():
        suite = unittest.TestSuite()
        suite.addTest(TestDemo('登录后询问权限进入营业区_01'))
        suite.addTest(TestDemo('登录后询问权限进入营业区_01'))
        #suite.addTest(unittest.makeSuite(测试类名))

# 4.实例化运行对象
        runner = unittest.TextTestRunner()
        print('1')
# 5.运行对象
        runner.run(suite)
        print('2')


test1()
'''