print("-" * 80)

t1 = 'python'
t2 = 'java'
# t3 = (t1, t2)*3
# print(t3)


print((t1+' '+t2+' ')*3)

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13


print("이름: %s 나이:%d" % (name1, age1))
print("이름: %s 나이:%d" % (name2, age2))

print("이름:{} 나이:{}".format(name1, age1))
print("이름:{} 나이:{}".format(name2, age2))

print(f"이름:{name1} 나이:{age1}")
print(f"이름:{name2} 나이:{age2}")


상장주식수 = "5,969,782,550"

상장주식수 = "5,969,782,550".replace(",", "")
타입변환 = int(상장주식수)
print(타입변환, type(타입변환))


분기 = "2020/03(E) (IFRS연결)"

print(분기[:11])
print(분기[:7]) # 1부터 세자

data = "   삼성전자    "

data1 = data.strip()
print(data1)