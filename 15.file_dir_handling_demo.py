# py-automation 디렉토리에 test 라는 디렉토리를 만든다.
# 00. 으로 시작되는 파일을 test 디렉토리로 복사한다.
import os
import glob
import shutil


def main():
    os.chdir('/Users/soongonkim/Desktop/py-automation')
    try:
        os.mkdir('test')
    except FileExistsError:
        pass

    file_list = glob.glob('00.*')
    for file in file_list:
        shutil.copy(file, './test')
        print('copy completed..')

    print('job completed..')


if __name__ == '__main__':
    main()
