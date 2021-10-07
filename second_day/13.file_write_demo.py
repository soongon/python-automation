def main():
    file = open('../data/test_write.txt', 'w', encoding='UTF-8')

    file.write('test test test\n')
    file.write('한글 테스트 입니다.\n')

    file.close()

    # list of line
    lines = [
        'sldkfjlsdfjdsklfj',
        'sldkfjlsdfjsklfjslkfjks',
        '한글아ㅣㄴㅇ렁나ㅣ러니ㅏ런미러니ㅏㅇ러'
    ]
    # 각 라인별로 \n 문자 추가
    lines_with_new_line = []
    for line in lines:
        lines_with_new_line.append(line + '\n')

    file2 = open('../data/test_write.txt', 'w', encoding='UTF-8')
    file2.writelines(lines_with_new_line)
    file2.close()
    print('job completed..')


if __name__ == '__main__':
    main()
