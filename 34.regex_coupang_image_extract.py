import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

res = requests.get('https://www.coupang.com/np/campaigns/82/components/194176', headers=headers)

image_regex = re.compile(r'\/\/.+\.jpg')

result = image_regex.findall(res.text)

for image_url in result:
    print(image_url)


