
# letters = 'python'
# print(letters[0], letters[2])


# license_plate = "24가 2210"
# print(license_plate[4:])

# string = "홀짝홀짝홀짝"
# print(string[0], string[2], string[4])

# string = "PYTHON"
# print(string[::-1])

phone_number = "010-1111-2222"
# print(phone_number(sep="-"))
# print(phone_number, sep=" ")
# 문자열은 바꿀 수 없다!!!!!!!!
phone_number1 = phone_number.replace("-", " ")  # 010 1111 2222
phone_number1 = phone_number.replace("-", "")  # 01011112222
print(phone_number1)

url = "http://sharebook.kr"
print(url[:-2])  # 틀림
print(url[-2:])

# lang = 'python'
# lang[0] = 'p'
# print(lang)  # Error

# string = 'abcdfe2a354a32a'
# print(string.upper())

string = 'abcd'
string.replace('b', 'B')
print(string)
