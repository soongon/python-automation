import pickle

file = open('./data/task.pickle', 'rb')
list_of_line = pickle.load(file)
print(list_of_line)
