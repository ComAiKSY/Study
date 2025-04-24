"""
택시 요금 계산
기본 요금 : 3000원
1km 당 1000원 추가
총 요금 계산
"""
total = 3000
dis = int(input('Enter Dis : '))
total = total + dis*1000
print(f'총 택시 요금 :{total}')

"""
온도 변환기
섭씨 -> 화씨 변환 (F = (C*9/5) + 32)
입력 : 섭씨(정수)
출력 : 화씨(정수)
"""
C = int(input("Enter C:"))
F = C*9/5 + 32
print(f'화씨온도 :{F}')
# print(f'화씨온도 :{int(C*9/5 + 32)}')

"""
구매 가능 개수와 잔돈 계산
입력 : 사탕 1개 가격, 가진 돈
출력 : 구매 개수, 구매후 남는 돈
"""

#price = int(input('Enter candy price : '))
#money = int(input('Enter ur money : '))
price, money = map(int, input('price & money : ').split())

amount = money//price
money = money - amount*price

print(f'구매 개수 :{amount}, 남는 돈 :{money}')

"""
입력 : 이름, 나이
출력: 인삿말, 내년 나이
"""
name = input('Enter name : ')
age = int(input('Enter age : '))

print(f'{name}님, 내년에는 {age+1}살이 되네요.')

"""
홀짝 판별
입력 : 정수
출력 : 정수의 홀/짝 판별
"""
num = int(input('Enter number : '))
if num%2 == 0:
    print(f'{num}은 짝수입니다.')
else:
    print(f'{num}은 홀수입니다.')

"""
주급 계산
입력: 일한 시간, 시급
출력 : 총 주급
"""
time = int(input('Enter time : '))
pay = int(input('Enter pay : '))
total = time*pay

print(f'총 주급은 {total}입니다.')

"""
평균 점수 계산
입력 : 국어, 영어, 수학 점수
출력 : 세과목 평균(정수)
"""
korean = int(input('Enter korean score : '))
eng = int(input('Enter english score : '))
math = int(input('Enter math score : '))
avg = int((korean + eng + math)/3) #기본 자료형 float(?)

print(f'평균점수 {avg}입니다.')

"""
두 수 중 큰 값 출력
입력 : 두 정수
출력 : 더 큰 값(동일 시 그 값)
"""

num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
if num1 > num2:
    print(f'{num1}')
elif num2 > num1:
    print(f'{num2}')
elif num1 == num2:
    print(f'{num1}')

"""
일수를 주와 일로 환산하기
입력: 일수
출력 : Y주 z일
"""
day = int(input('Enter day : '))
week = day//7

print(f'{week}주 {day - week*7}일') #주환산 안될경우 나중에 추가

"""
성인 판단
입력: 나이
출력 : 성인 여부
"""
age = int(input('Enter age : '))z
if age < 18:
    print(f'미자')
else:
    print(f'성인')


