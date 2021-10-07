import requests
from bs4 import BeautifulSoup

res = requests.get('https://music.bugs.co.kr/chart')

soup = BeautifulSoup(res.text, 'html.parser')
title_tag = soup.select_one('#CHARTrealtime > table > tbody > tr:nth-child(1) th > p > a')
artist_tag = soup.select_one('#CHARTrealtime > table > tbody > tr:nth-child(1) td > p > a')
print(title_tag.text)
print(artist_tag.text)
