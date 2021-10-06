import requests

res = requests.get('https://music.bugs.co.kr/chart')
print(res.text)
