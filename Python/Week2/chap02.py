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
weight = int(input('Enter your weight(g): '))
money = weight * 5
print('name : ', name)
print('address : ', address)
print('money : ', money)

#연산자 / 사칙연산 / 연산자 우선순위 (우선순위가 높은것 부터, 동일할 경우 왼쪽에서 오른쪽 방향으로 계산
#추가지원 // : 몫연산, % : 나머지 연산(modular, mod), ** : 제곱 / 나머지 연산자 없이 나머지 연산 구현해 보기

#문제
#1pound = 0.453592kg
#1kg = 2.204623lb

lb_to_kg_ratio = 0.453592 #lb2kg_ratio
kg_to_lb_ratio = 2.204623 #kg2lb_ratio

input_lb = float(input('Enter ur lb : '))
print(input_lb,'lb: ', input_lb*lb_to_kg_ratio, 'kg')
print(f'{input_lb}lb: {input_lb * lb_to_kg_ratio}kg')
#print(f'{input_lb}lb: {input_lb * lb_to_kg_ratio:.2f}kg') / .2f 소수점 두번째 자리

input_kg = float(input('Enter ur kg : '))
print(input_kg, 'kg: ', input_kg*kg_to_lb_ratio, 'lb')
print(f'{input_kg}kg: {input_kg * kg_to_lb_ratio}lb')

#num1 = 100, 200 /Right Grammer / 튜플과 언패킹으로 인한 문법
#튜플형: 하나의 정보체에 여러개의 값이 있는 형식 ex)mytuple = (5, 15, 25) /type을 사용해 변수의 타입확인 가능
mytuple = (5, 15, 25)
print(mytuple)
mytuple1 = 5, 15, 25
print(type(mytuple1))

#Unpakking : 값이여러개 있는 정보체에 값의 갯수만큼 변수를 준비하면 각 값들의 변수에 넣어줌
n1, n2, n3 = mytuple1
print(f'n1: {n1}, n2 type: {type(n2)}, n3: {n3}')

#스왑
a= 10
b= 20
#c=a, a=b, b=c
a,b = b, a #python swap grammer

#복합 연산자

#편의점 하루 매출 계산기
#buy : rice(900)*10, rice2(3500)*5
#sell : banana(1000)*2, rice2(3500)*4, can(1800)*5

all = 0
for i in range(5):
    total = 0
    menu = input('Sell or Buy menu : ')
    price = int(input('Enter price (+/-): '))
    count = int(input('Enter count : '))

    print(f'{menu}: {price * count} Sell or Buy')
    total += price * count
    all += total
print(all)



