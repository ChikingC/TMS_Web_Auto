from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import json

ex_path = 'F:\chromedriver\chromedriver109.0.5414.120\chromedriver'



class Function():

    def get_url(url):
        chromedriver = webdriver.Chrome(executable_path=ex_path)
        chromedriver.get(url)
        chromedriver.implicitly_wait(10)
        chromedriver.maximize_window()
        return chromedriver


    def login(chromedriver, account, password):
        chromedriver.find_element(By.XPATH, '//input[@id="userName"]').send_keys(account)
        chromedriver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
        chromedriver.find_element(By.XPATH, '//button[@type="submit"]').click()


    def select_outlet(chromedriver):
        chromedriver.find_element(By.XPATH, '//div[@id="MainContainer"]/div/div[2]/table/tbody/tr/td[2]/div').click()
        # chromedriver.find_element(By.XPATH, '//div[@id="MainContainer"]/div/div[2]/table/tbody/tr/td[2]/div').send_keys('alisa')
        # chromedriver.find_element(By.CSS_SELECTOR, 'div#css-ck91yh-menu div:nth-child(3)').click()
        time.sleep(2)
        ActionChains(chromedriver).send_keys('QC Test 6').perform()
        time.sleep(2)
        ActionChains(chromedriver).key_down(Keys.ENTER).perform()
        # chromedriver.find_element(By.XPATH, '//div[text()=”Alisa-Hong Kong (C001)“]').click()
        chromedriver.find_element(By.XPATH, '//button[@type="submit"]').click()



    # 首次登录获取cookie
    def getcookie(url):
        # 进入页面
        chromedriver = Function.get_url(url)
        # 扫码操作
        time.sleep(30)
        # 获取Cookie实现免登录
        cookie = chromedriver.get_cookies()

        # 保存到txt文件
        with open('cookie.txt', 'w') as f:
            # 转换为json保存
            jsonCookie = json.dumps(cookie)
            f.write(jsonCookie)
            chromedriver.close()


    def cookie_login(chromedriver):
        with open('cookie.txt', 'r') as f:
            cookies = json.loads(f.read())
            print(cookies)
        for cookie in cookies:
            cookie_dict = {
                'domain':  cookie.get('domain'),
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expiry": cookie.get('expiry'),
                'path': '/',
                'httpOnly': cookie.get('httpOnly'),
                'Secure': cookie.get('Secure')
            }
            chromedriver.add_cookie(cookie_dict)

        chromedriver.refresh()
        chromedriver.maximize_window()
        time.sleep(20)
    # s = Select(ChromeDriver.find_element(By.CSS_SELECTOR,'div[class=" css-1hwfws3"]'))
    # s.select_by_index(4)
