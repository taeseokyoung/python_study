ticker = "btc_krw"

print(ticker.upper())

ticker = "BTC_KRW"

print(ticker.lower())

string = 'hello'

a = string.capitalize()
print(a)

file_name = "보고서.xlsx"
b = file_name.endswith("xlsx")
print(b) #true false

c = file_name.endswith(("xlsx","xls"))
print(c)

file_name = "2020_보고서.xlsx"
d = file_name.startswith("2020")
print(d)

hello = "hello world"
e = hello.split(" ")
print(e)

print(hello.split())

ticker = "btc_krw"
print(ticker.split("_"))

data = "039490     "
rstrip_ = data.rstrip()
print(rstrip_)