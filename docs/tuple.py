# tuple 튜플

# () 튜플은 요소 값을 바꿀 수 없다.

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 4, 5, 6
t5 = (1, 2, 3, ('a', 'b', 'c'), 4)

t6 = (1, 2, 'a', 'b')
print(t6[2])
print(t6[-1])
print(t6[:2])
print(t6[2:])

print(t3 + t4)
print(t3 * 2)

print(len(t3))
