from pages.base_page import Basepage
from pages.reservation_page import ReservationPage

class OutletPage(Basepage):
    '''
    第二层：
    - 页面元素进行分离，每个元素只定位一次，隔离定位，
    如果页面改变，只需要改变相应的元素定位；
    - 业务逻辑分离 或 操作元素动作分离
    '''

    def Table_select(self,TableNumber):
        return self.by_xpath('//span[text()="{}"]'.format(TableNumber))

    def reservation_list_new_reservation(self):
        return self.by_xpath('//span[@icon="add"]')


    def reservation_search(self):
        return self.by_xpath('//input[@name="search"]')


    #预定桌台（操作元素分离）

    def reservation_table(self,TableNumber):

        ele = self.Table_select(TableNumber)
        self.actionchain().move_to_element(ele).context_click().perform()
        self.reservation_list_new_reservation().click()
        return(ReservationPage(self.driver))

        
    def search(self,text):
        ele = self.reservation_search()
        ele.send_keys(text)




