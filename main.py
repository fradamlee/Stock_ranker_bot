from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tickers import *
from listOfInvestorsRecord import ListOfInvestorsRecord
from recorder import Recorder

class RecorderRestorer:
    def __init__(self, recorder, browser):
        self.recorder = recorder
        self.browser = browser
        self.recorder.adjustment = 0
        self.recorder.iter_investor = 1
    
    # def _moveScrollDownToIncreaseOffset(self):
    #     curr_investor = self.recorder.iter_investor
    #     xpath = f'//*[@id="components-root"]/div[1]/section/main/div[6]/span/div[{curr_investor}]'
    #     ele_to_scroll_to = self.browser.find_element(By.XPATH, xpath)
    #     self.browser.execute_script("arguments[0].scrollIntoView();", ele_to_scroll_to)

    def restartBrowser(self):
        self.browser.close()
        time.sleep(3)
        self.browser = webdriver.Safari()
        self.recorder.setBrowser(self.browser)
        self.browser.maximize_window()
        self.browser.get(f'https://www.gurufocus.com/guru/list?group=basic&page={self.recorder.page_number}')
        time.sleep(4)
    
    def tryRecordPage(self, page):
        for i in range(3):
            try:
                res = self.recorder.recordInfoOfPage(page)
                return res
            except Exception as err:
                print(err)
                self.restartBrowser()
                self.recorder.adjustment = -6
                time.sleep(2)

if __name__ == "__main__":
    browser = webdriver.Safari()

    # clickIn('//*[@id="components-root"]/div[1]/section/main/div[6]/span/div[1]', constTime)
    # list_of_investors_record = ListOfInvestorsRecord()

    recorder = Recorder(browser)

    restorer1 = RecorderRestorer(recorder, browser)
    restorer1.tryRecordPage(1)
    restorer2 = RecorderRestorer(recorder, browser)
    restorer2.tryRecordPage(2)

    time.sleep(1)

    lst1 = recorder.list_of_investors_record.get_ranked_list(60, 40)
    # print(recorder.list_of_investors_record.all_tickers_summatory_of_maket_cap.dict_ticker_info)
    # print('\n')
    # print(recorder.list_of_investors_record.all_tickers_summatory_of_contribution.dict_ticker_info)

    print('\n')
    print(lst1)
