try:
    file = open('./data/not_exist.txt', 'r')
    file.readlines()
    file.close()
except FileNotFoundError:
    print('no file')
