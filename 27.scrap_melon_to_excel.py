import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# 1-100 까지의 정보를 확보
trs = soup.select('#frm > div > table > tbody > tr')

top100_list = []

for tr in trs:
    top100_list.append([
        int(tr.select_one('td:nth-child(2) > div > span.rank').text),
        tr.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text,
        tr.select_one('td:nth-child(7) > div > div > div > a').text,
        tr.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text,
        tr.select_one('td:nth-child(4) > div > a > img')['src']
    ])

# 엑셀파일로 저장
df = pd.DataFrame(top100_list)
df.to_excel('melon_top100.xlsx', index=False, header=['순위', '제목', '앨범', '아티스트', '이미지'])
print('job completed..')
