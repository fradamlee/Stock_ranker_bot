# from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tickers import *
from listOfInvestorsRecord import ListOfInvestorsRecord

class Recorder():
    def __init__(self, browser):
        self.browser = browser
        self.list_of_investors_record = ListOfInvestorsRecord()
        self.page_number = 0
        self.iter_investor = 1
        self.adjustment = 0

    def setBrowser(self, browser):
        self.browser = browser

    def _get_text_of_a_tag_by_xpath(self, xpath):
        tag_ele = self.browser.find_element(By.XPATH, xpath)
        return tag_ele.text

    def _moveScrollToTheCorrectPlace(self):
        if(self.adjustment != 0):
            xpath = f'//*[@id="components-root"]/div[1]/section/main/div[6]/span/div[{self.iter_investor+self.adjustment}]'
            ele_to_scroll_to = self.browser.find_element(By.XPATH, xpath)
            self.browser.execute_script("arguments[0].scrollIntoView();", ele_to_scroll_to)
        else:
            self.browser.execute_script("window.scrollTo(0, 0);")

    def countChildenTagsInsideAParentTag(self, parent_tag_xpath):
        parent_ele = self.browser.find_element(By.XPATH, parent_tag_xpath)
        childenTags = parent_ele.find_elements(By.XPATH, '*')
        return len(childenTags)

    def clickIn(self, xpath, constTime):
        users = self.browser.find_element(By.XPATH, xpath)
        users.click()
        time.sleep(constTime)
    
    def recordInfoOfPage(self, page_number):
        self.page_number = page_number
        self.browser.get(f'https://www.gurufocus.com/guru/list?group=basic&page={self.page_number}')
        self.browser.maximize_window()
        time.sleep(3)
        numberOfInvestors = self.countChildenTagsInsideAParentTag('//*[@id="components-root"]/div[1]/section/main/div[6]/span')
        self._recordInfoOfPage(numberOfInvestors)
        return 0

    def _get_current_investor_name(self):
        curr_xpath1 = f'//*[@id="components-root"]/div[1]/section/main/div[6]/span/div[{self.iter_investor}]/a/div[1]/div[1]/div[1]'
        curr_xpath2 = f'//*[@id="components-root"]/div[1]/section/main/div[6]/span/div[{self.iter_investor}]/a/div[1]/div[2]/div[1]'
        try:
            return self._get_text_of_a_tag_by_xpath(curr_xpath1)
        except Exception:
            return self._get_text_of_a_tag_by_xpath(curr_xpath2)

    def _recordTheMarketCap(self, inv_record):
        self.clickIn('//*[@id="scroll-header"]/tr/th[5]', 1)
        time.sleep(10)
        number_of_tickers = self.countChildenTagsInsideAParentTag('//*[@id="non-sticky-table"]/tbody')
        for i in range(number_of_tickers):
            ticker = self.browser.find_element(By.XPATH, f'//*[@id="{i}"]/td/span[1]/a').text
            str_marketCap_with_comas = self.browser.find_element(By.XPATH, f'//*[@id="{i}"]/td[5]/div/span').text
            marketCap = float(str_marketCap_with_comas.replace(",", ""))
            inv_record.add_ticker_info(ticker, marketCap)
            i+=1
        inv_record.add_percentage_for_each_ticker_from_total()
        self.list_of_investors_record.append_investors_record(inv_record)

    def _recordInfoOfAnInvestor(self):
            self.browser.get(f'https://www.gurufocus.com/guru/list?group=basic&page={self.page_number}')
            curr_investor_name = self._get_current_investor_name()
            inv_record = InvestorsRecord(curr_investor_name)
            self.browser.maximize_window()
            time.sleep(1)
            # self.browser.execute_script("document.body.style.zoom='80%'")
            self._moveScrollToTheCorrectPlace()

            time.sleep(2)
            print('page: ', self.page_number, '\titer_investor: ', self.iter_investor)
            self.clickIn(f'//*[@id="components-root"]/div[1]/section/main/div[6]/span/div[{self.iter_investor}]', 5)
            self.clickIn('//*[@id="components-root"]/div[1]/div/div[3]/div/div/a[3]', 1)
                    
            time.sleep(10)
            
            try:
                self._recordTheMarketCap(inv_record)
            except Exception as err:
                print(err)
            
            self.iter_investor += 1

            # self.browser.back()
            # time.sleep(1.5)
            # self.browser.back()
            # time.sleep(1.5)
            # self.browser.back()
            # time.sleep(4)
            # return 0
    
    def _recordInfoOfPage(self, numberOfInvestors):
        while(self.iter_investor <= numberOfInvestors):
            self._recordInfoOfAnInvestor()
        # self.iter_investor += 1


