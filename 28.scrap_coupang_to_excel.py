import requests
from bs4 import BeautifulSoup
import pandas as pd


def save_to_excel(list_of_list):
    df = pd.DataFrame(list_of_list)
    df.to_excel('coupang_rocket.xlsx', index=False)
    print('excel save completed')


def get_header():
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }


def main():
    res = requests.get('https://www.coupang.com/np/campaigns/82/components/194176', headers=get_header())
    soup = BeautifulSoup(res.text, 'html.parser')

    lists = soup.select('#productList > li')

    products = []

    for li in lists:
        products.append([
            li.select_one('a > dl > dd > div.name').text.strip(),
            int(li.select_one('a > dl > dd > div.price-area > div > div.price > em > strong').text.replace(',', '')),
            int(li.select_one('a > dl > dd > div.other-info > div > span.rating-total-count').text[1:-1]),
            'https:' + li.select_one('a > dl > dt > img')['src']
        ])

    save_to_excel(products)


if __name__ == '__main__':
    main()
