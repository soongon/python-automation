import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

res = requests.get('https://www.coupang.com/np/campaigns/82/components/194176', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
price_tag = soup.select_one('#productList > li:nth-child(1) > a > dl > dd > div.price-area > div > div.price > em > strong')
print(price_tag.text)