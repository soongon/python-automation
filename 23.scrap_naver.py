import requests
from bs4 import BeautifulSoup

# 1단계 데이터가 있는 페이지를 확보
res = requests.get('https://finance.naver.com/')

# 2단계 확보한 데이터(HTML)을 파싱하여 원하는 데이터를 추출
# Beautifulsoup 파싱 도구를 사용하여 파싱
soup = BeautifulSoup(res.text, 'html.parser')
the_tag = soup.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num')
print(the_tag.text)

# 24.문제 .. bugs 뮤직 차트로 가서(https://music.bugs.co.kr/chart) 1등곡과 아티스트 2개 데이터 출력
