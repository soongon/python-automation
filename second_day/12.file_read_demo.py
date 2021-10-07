file = open('../data/zen_of_python.txt', 'r')

lines = file.readlines()

for line in lines:
    print(line)

file.close()
