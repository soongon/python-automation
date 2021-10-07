def main():
    favorite_colors = ['red', 'green', 'blue', 'orange', 'pink', 'tan']

    # 리스트의 각 아이템을 조작할 수 있다. --> 각 아이템의 글자 수를 출력
    for color in favorite_colors:
        print(len(color))

    # '대한민국 만세' 를 10번 출력
    for index in range(1, 1000, 3):
        print(str(index) + ' 대한민국 만세')

    # dict 반복하기
    my_dict = {
        '박찬욱': '올드보이',
        '김기덕': '뫼비우스',
        '봉준호': '기생충',
        '박훈정': '신세계'
    }

    for key, value in my_dict.items():
        print('감독: ' + key + ' 대표작: ' + value)


main()