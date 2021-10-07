# create dictionary
my_dict = {
    '박찬욱': '올드보이',
    '김기덕': '뫼비우스',
    '봉준호': '기생충',
    '박훈정': '신세계'
}

# CRUD .. Read --> indexing
# print(my_dict['홍상수'])
print(my_dict.get('박훈정'))  # 키가 없을 때 None 을 리턴하여 에러를 방지

# CRUD .. Create
my_dict['홍상수'] = '지금은 맞고 그때는 틀리다'
print(my_dict)

# CRUD .. Update
my_dict['박찬욱'] = '아가씨'
print(my_dict)

# CRUD .. Delete
if len(my_dict['김기덕']) >= 5:
    del my_dict['김기덕']
else:
    del my_dict['박찬욱']

print(my_dict)
