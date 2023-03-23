# 리스트에는 숫자, 문자, 자료형이 들어갈 수 있다.

# 빈 리스트 생성
a = list()
print(a)


# 리스트의 인덱싱과 슬라이싱
a = [1, 2, 3]
print(a)
print(a[0])  # 리스트의 첫 번째 요소
print(a[0] + a[2])  # 리스트의 요소들을 더할 수 있다.
print(a[-1])  # 리스트의 마지막 요소

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3][0])  # 리스트 속 리스트의
print(a[-1][0])  # 위 결과와 같다.

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[-1][-1][0])  # Life
print(a[2][2][0])  # Life

# 리스트를 다중으로 중첩하는 것은 혼란스러워서 잘 하지 않는다고 한다...?

# 리스트의 슬라이싱 - 문자열과 완전히 같다.
a = [1, 2, 3, 4, 5]
print(a[0:3])  # [1,2,3]
print(a[:3])  # [1,2,3]
print(a[3:])  # [1,2,3]
print(a[::-1])  # 반대로 정렬도 가능

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:4])  # 3 ['a','b','c']
print(a[3][:1])  # ['a']

# 리스트 연산하기
a = [1, 2, 3]
b = [4, 5, 6]

print(a+b)  # [1, 2, 3, 4, 5, 6] 리스트 합치기
print(a*3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3] 리스트 반복

# 리스트 길이 **
print(len(b))  # 3

# print(a[2] + 'hi')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 문자랑 숫자는 더할 수 없다.
print(str(a[2]) + 'hi')  # 3hi

# 리스트 수정/삭제 **
a = [1, 2, 3]
a[1] = 10  # 2를 10으로 변경
a.append(4)  # 4 추가
a.append(5)
a.append(6)
print(a)

# 슬라이싱으로 리스트 자르기
del a[1]
print(a)

del a[:2]  # [4,5,6]
print(a)

# list function 리스트 관련 함수
a.append([7, 8, 9])  # 리스트도 추가할 수 있다. [4, 5, 6, [7, 8, 9]]
print(a)

# 숫자와 문자를 순서대로 정렬할 수 있다.
a = [1, 4, 2, 3]
b = ['f', 'g', 'c', 's']
a.sort()
b.sort()
print(a)  # [1, 2, 3, 4]
print(b)  # ['c', 'f', 'g', 's']

# reverse 뒤집기
a = [1, 2, 3, 4]
a.reverse()
print(a)  # [4, 3, 2, 1]

# index 값 반환
b = [5, 6, 7, 8]
# 괄호 안에 적은 값이 리스트에 있다면 그 값의 순서를 출력.
# ValueError
# idx = b.index(2)
# print(idx)

# 2
idx = b.index(7)
print(idx)

# insert 삽입
# insert(a,b) a번째 위치에 b를 삽입
a = [1, 2, 3]
a.insert(3, 4)
print(a)  # [1,2,3,4]

# remove 제거
# remove(x) 리스트의 첫 x를 삭제
a = [3, 5, 7, 8, 5, 3, 2, 5, 1]
a.remove(3)
print(a)  # [5, 7, 8, 5, 3, 2, 5, 1]

# pop 끄집어내기
# pop() 리스트의 맨 마지막 요소를 리턴하고 그 요소를 삭제
a = [1, 2, 3, 4]
a.pop()
print(a)

# pop(x) 리스트의 x번쨰 요소를 리턴하고 그 요소를 삭제
a.pop(2)
print(a)  # [1,2]

# count 개수 세기
# count(x) 리스트 안에 x 갯수를 리턴
b = [1, 2, 1, 2, 1, 2]
count = b.count(2)
print(count)  # 3

# extend 확장
# a.extend([x]) a의 리스트에 x(리스트) 를 추가한다.
a = [1, 2, 3]
x = [4, 5, 6]
a.extend(x)
a.extend([7, 8, 9])
a += [10, 11]  # a = a + [10,11]
print(a)
