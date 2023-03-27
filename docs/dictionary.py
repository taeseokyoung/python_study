# dictionary 딕셔너리 {}

# a = {
#     'key': 'value',
#     'key2': 'value2',
#     'key3': 'value3',
#     4: 'value4',
#     'a': [1, 2, 3]
# }

# 추가
a = {
    'key': 'value'
}
# a[key] = 'value'
a['key2'] = 'value2'

# 삭제

# del a[key]
del a['key2']

print(a)

# keys - key 리스트 만들기
age = {'kyoung': 32, 'young': 31}
print(age['kyoung'])  # 32

# key에 list는 쓸 수 없으나 tuple은 쓸 수 있다.

# functions
# a.keys()  a의 key만을 모아 객체를 리턴한다.

# for k in a.keys():
#     print(k)
# 리턴된 객체는 리스트 고유의 append, insert, pop, remove, sort 함수들은 사용할 수 없다.

# Values - value 리스트 만들기
# a.values() a의 value만을 모아 객체를 리턴한다.

# items - key, value의 쌍을 얻기
# a.items() a의 쌍을 튜플로 묶은 값을 객체로 리턴한다.

# clear - key, value의 쌍을 모두 지우기
# 딕셔너리 안의 모든 요소들을 삭제하고 { } 로 표현한다.

# get - key에 맞는 value를 리턴
# return a.get(x) = a[x]
# return None != Error (존재하지 않는 값)
# 만약 key에 맞는 value 없을 때 None을 띄우고 싶지 않다면 a.get(x,띄울 값)

# in - 해당 key가 딕셔너리 안에 있는지 조사 : boolean을 리턴
# 'key' in a
