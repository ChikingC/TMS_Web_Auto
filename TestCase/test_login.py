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


    def setUp(self) :
        self.dr = webdriver.Chrome(executable_path = 'F:\chromedriver\chormedriver111.0.5563.64\chromedriver')


    def tearDown(self) :
        time.sleep(10)
        self.dr.quit()



    def test_login_success(self):
        username = '1'
        password = '1'
        outlet = '1001'


        login_page = LoginPage(driver = self.dr,path='eng/tms/operation/current_view')

        login_page.login(username = username,password=password)
        #login_page.flash_page()
        reservation_page = login_page.outlet_select(Outlet = outlet)
        reservation_page.reservation_table(TableNumber=102)


    def test_login_failed(self):
        time.sleep(5)
        username = '2123123123'
        password = '1231231223'

        login_page = LoginPage(driver = self.dr,path='eng/tms/operation/current_view')
        login_page.login(username=username, password=password)
        mesg = login_page.failed_login_text()
        expect_mesg = 'Invalid username or password\nPlease try again'

        self.assertEqual(mesg,expect_mesg)

