import time

from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36')
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome('./chromedriver', options=options)

browser.get('https://www.melon.com/chart/index.htm')
time.sleep(2)

source = browser.page_source

browser.close()

soup = BeautifulSoup(source, 'html.parser')
count = int(soup.select_one('#lst50 > td:nth-child(8) > div > button > span.cnt')
            .text.strip().split('\n')[1].replace(',', ''))
print(count)
