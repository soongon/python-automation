import time

from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')

browser.get('https://www.coupang.com')

time.sleep(5)

browser.close()