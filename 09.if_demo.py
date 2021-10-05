# 단어 번역기 연습문제
# input() 으로 단어를 입력받아 첫글자를 마지막으로 옮기고 'ay'를 추가
# 단어의 길이가 0이거나 글자가 아닐때는 'invalid word' 라고 출력
print('단어를 입력하세요:')
original = input()

if len(original) == 0 or not original.isalpha():
    print('invalid word')
else:
    print(original[1:] + original[0] + 'ay')
