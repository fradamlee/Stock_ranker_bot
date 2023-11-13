from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == "__main__":
    browser = webdriver.Safari()
    browser.get('https://www.gurufocus.com/guru/david%2Btepper/stock-picks?view=table')
