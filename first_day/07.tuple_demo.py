# Tuple 은 괄호를 리터럴 기호로 사용
my_tuple = 'red', 'blue', 'orange'

print(type(my_tuple))

# destruction, 구조분해
a, b, c = my_tuple

print(b)

# indexing, slicing 은 리스트와 동일
print(my_tuple[2])
print(my_tuple[0:2])
