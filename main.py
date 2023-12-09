from selenium import webdriver
from tickers import *
from recorder import Recorder
import time

if __name__ == "__main__":
    browser = webdriver.Safari()

    # recorder1 = Recorder(browser, 1, start_from_investor_number=6)
    recorder2 = Recorder(browser, 1)
