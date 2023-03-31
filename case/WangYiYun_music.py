from selenium import webdriver
from selenium.webdriver.common.by import By
from case.Function import Function
from selenium.webdriver.common.keys import Keys
import time
import unittest
URL = 'https://music.163.com/'


class WangYiMusic_test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:

        Function.getcookie(URL)
        self.chromedriver = Function.get_url(URL)
        self.chromedriver.implicitly_wait(10)


    @classmethod
    def tearDownclass(self) -> None:
        time.sleep(10)
        self.chromedriver.close()
        self.chromedriver.quit()



    #搜索歌曲"相安无事"播放
    def test01(self):
        #Function.getcookie('https://music.163.com/')
        #chromedriver = Function.get_url('https://music.163.com/')
        Function.cookie_login(self.chromedriver)
        self.chromedriver.find_element(By.XPATH,"//input[@name='srch']").send_keys("乌梅子酱")
        self.chromedriver.find_element(By.XPATH,"//input[@name='srch']").send_keys(Keys.ENTER)
        #切换iframe
        iframe = self.chromedriver.find_element(By.XPATH, "//iframe[@name='contentFrame']")
        self.chromedriver.switch_to.frame(iframe)
        self.chromedriver.find_element(By.XPATH,"//a[@id='song_1997438791']").click()
        #最后要记得跳转回到主框架页
        self.chromedriver.switch_to.default_content()

        #点击商场按钮
        self.chromedriver.find_element(By.XPATH,"//a[@data-module='store']").click()
        #获取当前所有标签页句柄
        wins_handles = self.chromedriver.window_handles

        print("当前所有句柄:",wins_handles,";")

        #转换商场页面handle
        self.chromedriver.switch_to.window(wins_handles[-1])
        print("当前页面：", self.chromedriver.title, ";")

        #商场页面进行搜索
        self.chromedriver.find_element(By.XPATH,"//input[@class='searchbox']").send_keys('蓝牙耳机')
        self.chromedriver.find_element(By.XPATH, "//input[@class='searchbox']").send_keys(Keys.ENTER)



