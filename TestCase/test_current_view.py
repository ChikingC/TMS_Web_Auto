import unittest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.outlet_page import OutletPage

import pytest




class LoginCase(unittest.TestCase):
    '''
      第三层
      使用单元测试框架对业务逻辑进行测试
    '''

    def setUp(self):
        self.dr = webdriver.Chrome(executable_path='F:\chromedriver\chormedriver111.0.5563.64\chromedriver')

    def tearDown(self):
        time.sleep(10)
        self.dr.quit()


    def test_current_view_search(self):
        username = '1'
        password = '1'
        outlet = '1001'

        login_page = LoginPage(driver=self.dr, path='eng/tms/operation/current_view')

        login_page.login(username=username, password=password)
        # login_page.flash_page()
        current_view=login_page.outlet_select(Outlet=outlet)
        current_view.search(text='11')







