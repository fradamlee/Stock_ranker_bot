from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def clickIn(xpath, constTime):
    users = browser.find_element(By.XPATH, xpath)
    users.click()
    time.sleep(constTime)

def clickInByClass(className, constTime):
    button = browser.find_elements(By.CLASS_NAME, className)
    button[0].click()
    time.sleep(constTime)

def sendKeys(xpath, message, constTime):
    u = browser.find_element(By.XPATH, xpath)
    u.send_keys(message)
    time.sleep(constTime)

if __name__ == "__main__":
    browser = webdriver.Safari()
    constTime = 1
    browser.get('https://www.gurufocus.com/guru/list?group=basic&page=1')
    browser.maximize_window()

    # clickIn('//*[@id="components-root"]/div[1]/section/main/div[6]/span/div[1]', constTime)
    clickIn('//*[@id="components-root"]/div[1]/section/main/div[6]/span/div[2]', constTime)

    clickIn('//*[@id="components-root"]/div[1]/div/div[3]/div/div/a[3]', 1)
    time.sleep(10)
    clickIn('//*[@id="scroll-header"]/tr/th[5]', 1)
    time.sleep(10)

    for j in range(10):
        try:
            i = 0
            while(True):
                t = browser.find_element(By.XPATH, f'//*[@id="{i}"]/td[5]/div/span').text
                print(t)
                i+=1
        except Exception as err:
            print('---------')
            clickIn(f'//*[@id="components-root"]/div[1]/div/div[4]/div/div/div[2]/div/div/div[6]/div[2]/ul/li[{j}]', 6)
            print('after')

    # Text of branchB v3

    input()
