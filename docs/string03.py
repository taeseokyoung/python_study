# string function 문자열 함수

cat = "dandelion"
string = "Life is too short, You need Python!"


# count 문자 개수 세기 
print(cat.count('d')) #2

# find 위치 알려주기 - 0부터 센다.
print(cat.find('d')) # 0 처음으로 나온 위치를 반환.
print(cat.find('z')) # -1 존재하지 않는다.

# index 위치 알려주기 2
print(string.index('y')) # 29
print(string.index('Y')) # 19 대소문자 구분하기!
# print(string.index('a')) ValueError: substring not found

# join 삽입
print("a".join('bnn🍌')) 
print(",".join('banana'))
print(",".join(['banana','apple','peach'])) #list
print(",".join(('banana','apple','peach'))) #tuple

# 소문자 > 대문자
a = "banana"
print(a.upper())

# 대문자 > 소문자
b = "BANANA"
print(b.lower())

# strip(양쪽), lstrip(왼쪽), rstrip(오른쪽) 공백 지우기 

# replace 문자열 바꾸기 
food = "I like kimbob"
print(food.replace("kimbob" ,"hamburgers"))

# split 문자열 나누기
# 문자열은 나누고나면 list [] 에 들어간다.
cat = "My name is dandelion"
print(cat.split()) # ['My', 'name', 'is', 'dandelion'] 기본값은 공백(스페이스,탭,엔터..)

cat2 = "My:name:is:dandelion"
print(cat2.split(':')) # ['My', 'name', 'is', 'dandelion']