#encoding:utf8
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.logger import logger



logger = logger(logger='BasePgae').getlog()


class Basepage():
    '''
      第一层：对Selenium 进行二次封装，定义一个所有页面都继承的 BasePage ，
      封装 Selenium 基本方法 例如：元素定位，元素等待，导航页面 ，
      不需要全部封装，用到多少方法就封装多少方法。
    '''

    def __init__(self,driver,path=None):
        '''
                :param driver: Webdriver实例对象
                :param path:   传入URI
        '''




        self.driver = driver
        self.url = 'https://test-multi-hq.hero-cloud.cn/accounts/hqqccn1/'

        #设置全局元素定位等待时间10秒
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.load_page(path)

    def by_xpath(self,xpath):
        return self.driver.find_element(By.XPATH,xpath)



    def find_element(self,*selector):
        try:
            element = self.driver.find_element(*selector)
            logger.info("The element looked up is {}{} ".format(*selector))
            return element
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)

    def flash_page(self):
        self.driver.refresh()
        logger.info("refresh page")


    def actionchain(self):
        return  ActionChains(self.driver)

    def load_page(self,path=None):
        if path == None:
            url = None
        else:
            url = self.url + path

        if url != None:
            self.driver.get(url)
            logger.info("Load_page:{}".format(url))