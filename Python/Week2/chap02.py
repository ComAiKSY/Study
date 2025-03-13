print('Hello world!')

a=100 #변수 a에 값 100을 대입
b=200
print(a)
print(b)

c=a+b
print(a, '+', b, "=", c)

# 대입 연산자는 우선순위가 낮다, 왼쪽에는 변수가 존재, 오른쪽은 상관없다
# 100 = a+b / Syntax Error

d=a-b
print(a, '-', b, "=", d)

e=a*b
print(a, '*', b, "=", e)

f=a/b #실수형 나눗셈
print(a, '/', b, "=", f)

g=a//b #정수형 나눗셈
print(a, '/', b, "=", g)

msg1 = 'hi'
msg2 = 'hello'
print(msg1, msg2) #쉼표자리 띄어쓰기로 대체
print(msg1+msg2) #문자열 + 문자열 / 연결연산
# print(msg1-msg2) / SyntaxError / 중의적으로 해석

msg3 = msg1*3 #반복 연산
print(msg3)
# 문자열 연산은 연결, 반복만 지원

#변수명 규칙
#나는변수다 = 55 #한글 변수를 지원은 한다
#print(나는변수다)

#변수명에 띄어쓰기 대신에 _ 사용, __ 운영체제 및 커널 코드에서 사용, 숫자로 시작 금지
#예약어는 변수명으로 사용 불가
#print = 777 / 함수이름 변수사용가능은 하지만 이후 함수 작동 불가

#인풋 함수
mymsg = input('Input message: ')
print(mymsg) # print(mtmsg+100) / Syntax Error / Input = String Type / print(mymsg + '100') O

#형변환
mymsg = int(input('Input message: '))
print(mymsg + 50)

#문제
name = input('Enter your name: ')
address = input('Enter your address: ')
weight = input('Enter your weight(g): ')
money = weight * 5
print('name : ', name)
print('address : ', address)
print('money : ', money)



