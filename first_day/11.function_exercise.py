def cube(number):
    """
    cube 라는 이름의 함수를 만들어서 number 라는 파라미터를 받는다.
    파라미터로 받은 숫자를 세제곱하여 반환(리턴)한다. (자기 숫자를 세번 곱한다)
    :param number:
    :return:
    """
    return number ** 3


def by_three(number1=0, number2=0, number3=0):
    """
    by_three 라는 두 번째 함수를 만들고 number 라는 파라미터를 받는다.
    그 숫자가 3으로 나누어지면 cube함수를 호출해서 결과를 넘겨주고, 그렇지 않으면 False 를 리턴한다.
    :param number1:
    :param number2:
    :return:
    """
    if number1 % 3 == 0:
        return cube(number1 + number2)
    else:
        return False


def main():
    print(by_three(number3=5))


if __name__ == '__main__':
    main()
