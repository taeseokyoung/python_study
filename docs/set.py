# set 집합 자료형

s1 = set([1, 2, 3])
print(s1)

s2 = set('dandelion')
print(s2)
# 순서가 없다. 중복을 허용하지 않는다. - 자료형의 중복 필터로 사용

s3 = set(['kyoung', 'hoon', 'young', 'seong'])
print(s3)

# 순서가 없기 때문에 인덱스가 없다. : 딕셔너리와 비슷하다.
# 리스트, 튜플로 변화시켜서 인덱스로 접근해야 한다.


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
# print(s1 & s2) = s1.intersection(s2)

# 합칩합
# print(s1 | s2) = s1.union(s2)

print(s1 | s2)

# 순서가 안중요한가? 합치는거니까 안중요하다
print(s1.union(s2))
print(s2.union(s1))

# 차집합 - 순서에 따라 값이 달라진다.
print(s1 - s2)  # {1, 2, 3}
print(s2 - s1)  # {8, 9, 7}

# s1.difference(s2) / s2.difference(s1)

# functions
# add : 값 추가
s1.add(99)
print(s1)

# update : 여러 개 값 추가
s1.update([100, 200, 300])
print(s1)

# remove : 특정 값 제거
s1.remove(2)
print(s1)
