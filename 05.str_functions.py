my_str = 'Hello world'

# in, not in 연산자 -> bool 값을 반환
result = 'llo' in my_str
print(result)

result2 = 'o w' not in my_str
print(result2)

# upper() lower() isupper() islower()
print(type(my_str))
print(my_str.upper())
print(my_str.lower())
print(my_str.islower())

# starstwith(), endwith()
starswith_str = 'http://www.naver.com/'
endswith_str = 'flower.jpg'

print(starswith_str.startswith('http'))
print(endswith_str.endswith('.jpg'))

# split()
split_str = 'red|blue|white|purple|tan|black'
colors = split_str.split('|')
print(colors)
