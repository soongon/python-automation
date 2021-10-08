import requests
import pandas as pd

headers = {
    'Authorization': 'KakaoAK d45fe3d1a84cb2ae6d8e21d820c2bd38'
}
params = {
    'query': '오징어 게임'
}

res = requests.get('https://dapi.kakao.com/v2/search/web', headers=headers, params=params)

results = []
for document in res.json().get('documents'):
    results.append([
        document.get('contents').replace('<b>', '').replace('</b>', ''),
        document.get('datetime'),
        document.get('title').replace('<b>', '').replace('</b>', ''),
        document.get('url')
    ])

df = pd.DataFrame(results)
df.to_excel('squid_game.xlsx', index=False)
