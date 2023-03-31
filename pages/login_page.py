import time

from pages.base_page import Basepage
from pages.outlet_page import OutletPage
from selenium.webdriver.common.keys import Keys


class LoginPage(Basepage):
    '''
    第二层：
    - 页面元素进行分离，每个元素只定位一次，
    隔离定位，如果页面改变，只需要改变相应的元素定位；
    每当页面发生变化的时候，只需要在用例中寻找变动的部分进行修改
    - 业务逻辑分离 或 操作元素动作分离

    注意：
    - 不要在page页面对象外做元素定位 ,
    - 不在page页面对象里面写断言，除非是页面是否成功加载断言
    - 需要多少个元素就定位多少个，不需要对整个页面的元素进行定位
    - 当你的用例设计页面跳转时，例如登陆操作，登陆完成后跳转首页，
    当页面发生“跳转”，封装的业务逻辑需要返回（return）对应的页面对象的实例
    '''

    #登录名输入框定位（定位分离）
    def form_username(self):
        return self.by_xpath('//input[@id="userName"] ')
       

    def form_password(self):
        return self.by_xpath('//input[@id="password"]')


    def login_button(self):
        return self.by_xpath('//button[text()="Login"]')


    #营业区下拉列表
    def form_outlet(self):
        return self.by_xpath('//div[@id="MainContainer"]/div/div[2]/table/tbody/tr/td[2]/div')
        '''
        可以通过控制台，输入setTimeout(function(){debugger},5000),在界面点击下拉框使之处在下拉状态在，页面进入debug状态后，再进行定位

        这个只要设定好时间，让想要定位的页面在debug状态之前出现就行，后续就用元素选择或者Ctrl+Shift+C来定位想要的元素即可

        
        
        '''

    def Countiue_button(self):
        return self.by_xpath('//button[@type="submit"]')


    def failed_login_text(self):
        return self.by_xpath('//div[text()="Invalid username or password"]').text

    #登录操作（业务逻辑分离）

    def login(self,username,password):
        #输入账号
        self.form_username().send_keys(username)
        #输入密码
        self.form_password().send_keys(password)
        #点击登录按钮
        self.login_button().click()
        # 当你的用例设计页面跳转时，例如登陆操作，登陆完成后跳转首页，
        # 当页面发生“跳转”，封装的业务逻辑需要返回（return）对应的页面对象的实例
        # 返回页面对象实例 （实现页面跳转）



    def outlet_select(self,Outlet):
        #进入营业区
        self.form_outlet().click()
        self.actionchain().send_keys(Outlet).perform()
        time.sleep(0.5)
        self.actionchain().key_down(Keys.ENTER).perform()
        time.sleep(10)
        self.Countiue_button().click()

        return OutletPage(self.driver)

