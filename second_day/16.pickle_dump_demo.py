import pickle

file = open('../data/zen_of_python.txt', 'r')

list_of_line = file.readlines()
list_of_line.append('추가적으로 라인을 추가합니다. \n')
file.close()

pickled_file = open('../data/task.pickle', 'wb')
pickle.dump(list_of_line, pickled_file)

print('file pickled..')
