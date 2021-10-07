import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36')

browser = webdriver.Chrome('./chromedriver', options=options)

browser.get('https://www.melon.com/')
time.sleep(3)
# 골드박스 링크를 클릭
browser.find_element_by_css_selector('#gnb_menu > ul:nth-child(1) > li.nth8 > a').click()
time.sleep(3)
browser.close()
