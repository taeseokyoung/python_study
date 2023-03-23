# 1. string 문자열이란 : 문자, 단어 등으로 구성된 문자들의 집합.
# "Life is too short, You need Python!"
# "yummy"
# "0323"


# 표현방식
print("Hello World")
print("""Hello World""")
print('Hello World')
print('''Hello World''')


# 문자열에 작은 따옴표 추가
print("Hello I'm cheese") # Hello I'm cheese
print("Hello I'm 'cheese'") # Hello I'm 'cheese'


# 문자열에 큰따옴표 추가
print('Hello "Im cheese"') # Hello "Im cheese"


# \ 백슬래시 사용하여 따옴표들을 문자열에 포함시키기 
# \', \" 를 입력한다.
print('Hello "I\'m cheese"') # Hello "I'm cheese"
print("\"Python is very easy.\" seokyoung says.") #"Python is very easy." seokyoung says.


# 여러줄의 문자열을 변수에 대입
hello = "Hello\nI'm cheese"

# '''를 """로 사용할수도 있다.
hello = '''
Hello
I'm
cheese
'''
print(hello)



# 이스케이프 코드 : \를 사용하는 프로그래밍 문자 조합
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World") # Hello\World
print("Hello\'World") # Hello'World
print("Hello\"World") # Hello"World


# 문자열 연산
head = "Hello"
tail = " I'm cheese"
print(head+tail)
# Hello I'm cheese

a = "PYTHON"
print(a*2) #PYTHONPYTHON


# 프로그램명을 이렇게 띄우면 좋겠다.
print("=" * 50)
print("My Program")
print("=" * 50)