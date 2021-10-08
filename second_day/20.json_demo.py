url = 'https://api.github.com/users'

# web agent.. requests
# pip install requests 로 requests 모듈 설치
import requests

res = requests.get(url)

# user 데이터 중 html_url 의 값을 리스트로 반환
result_list = []
for user in res.json():
    result_list.append(user.get('html_url'))

print(result_list, len(result_list))

