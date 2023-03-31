import time

from selenium.webdriver.common.by import By
from pages.base_page import Basepage

MemberNo1 = (By.ID,'memberNo')
#Wed Mar 22 2023
Adult_num=(By.XPATH,"//tr[ @ id = 'adults']/td[3]/div/div")
Adult_num_select =(By.XPATH,"//div[@class=' css-11unzgr']//div[5]")
Member_selector=(By.XPATH,'//*[@id="member_no"]/td[3]/div/div[2]/div')
submit_button=(By.XPATH,"//button[text()='Save Button'])")
Dialog_title=(By.XPATH,"//h4[text()='Confirmation Dialog']")

class ReservationPage(Basepage):
    def Date_select(self,date):
        Day=(By.XPATH, "//div[@aria-label='{}']".format(date))

        self.find_element(*Day).click()

    def Input_Userinfo(self,day):
        self.find_element(*Adult_num).click()
        time.sleep(5)
        self.find_element(*Adult_num_select).click()
        self.Date_select(day)

    def select_member(self,MemberNo):
        self.find_element(*MemberNo1).send_keys(MemberNo)
        self.find_element(*Member_selector).click()

    def save_reservation(self):
        self.find_element(*submit_button).click()

    def check_reservation_success(self):
        return self.find_element(Dialog_title).text
