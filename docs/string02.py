string = "Hello World"

# length 문자열 길이
print(len(string)) # 11

# index 문자열 인덱싱
print(string[0]) # H
print(string[1]) # e

print(string[-1]) # d 
# -0과 0은 결과적으로 같은 값이기 때문에 반대로 셀 때는 -1부터

# slice 문자열 슬라이싱
print(string[0:5]) # Hello
print(string[:5]) # Hello
print(string[1:4]) # ell - 슬라이싱에서는 끝번호에 해당하는 것은 포함하지 않는다.


print(string[:]) # Hello World
print(string[::-1]) # dlroW olleH
print(string[4:-1]) # o Worl - 슬라이싱의 끝번호 생략으로 -1번째인 d 생략됨.

# slicing 슬라이싱 예제
slicing = "20230323Rainy"
year = slicing[:4]
day = slicing[4:8]
weather = slicing[8:]
print(year, day, weather)

# pithon을 python으로 바꾸기 예제
wrong = "pithon"
# letter = wrong.append("y")
# letter = wrong[1]
# print(letter)
# AttributeError: 'str' object has no attribute 'append'
# 문자열(문자열 자료형)의 요솟값은 바꿀 수 없다. = immutable한 자료형

# 슬라이싱으로 문자를 나누고 나눠진 파트들을 더하여 새로운 문자열을 만든다.
a = wrong[:1]
b = wrong[2:]
print(a + "y" + b) 

# % 문자열 포매팅
# https://wikidocs.net/13

# f 문자열 포메팅
person = "서경"
cat = "들레"
print(f"나의 이름은 {person}입니다. 나는 고양이 {cat}와 함께 삽니다.")
# 나의 이름은 서경입니다. 나는 고양이 들레와 함께 삽니다.

# 정렬, 공백 채우기, 소수점 표현방법