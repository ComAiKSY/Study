#Quiz 1
from pkgutil import resolve_name

num1 = int(input())
a,b,c,d,e,f,g = map(int, input().split())
day = [a,b,c,d,e,f,g]

if num1 - a < 0:
    print('1')
elif num1*2 - (a+b) < 0:
    print('2')
elif num1*3 - (a+b+c) < 0:
    print('3')
elif num1*4 - (a+b+c+d) < 0:
    print('4')
elif num1*5 - (a+b+c+d+e) < 0:
    print('5')
elif num1*6 - (a+b+c+d+e+f) < 0:
    print('6')
elif num1*7 - (a+b+c+d+e+f+g) < 0:
    print('7')


#Quiz2
num1, num2 = map(int, input().split())

#Quiz3
num1 = int(input())
while True:
        num2 = int(input())
        if num1 == num2:
            print(f'정답')
            break
        elif num1 > num2:
            print('낮음')
        else:
            print('높음')

#Quiz4
while True:
    num1 = int(input())
    if num1 % 1000 != 0:
        print(f'다시 입력하세요')
    else:
        count1 = num1 // 50000
        num1 = num1 - count1 * 50000
        count2 = num1 // 10000
        num1 = num1 - count2 * 10000
        count3 = num1 // 5000
        num1 = num1 - count3 * 5000
        count4 = num1 // 1000
        num1 = num1 - count4 * 1000
        print(f'50000 : {count1}, 10000 : {count2}, 5000 : {count3}, 1000 : {count4}')

#Quiz5
num1 = int(input())
if num1 >= 100000:
    print(f'총 금액 : {num1 - (num1*0.1)}')
elif num1 >= 50000:
    print(f'총 금액 : {num1 - (num1*0.05)}')
else:
    print(f'총 금액 : {num1}')

#Quiz6
num1 = int(input())
score = []
for _ in range(num1):
    value = int(input())
    score.append(value)

for i in range(num1):
    if 90<=score[i]<=100:
        print(f'{i+1}번째 학생의 등급은 A입니다')
    elif 80<=score[i]<=89:
        print(f'{i+1}번째 학생의 등급은 B입니다')
    elif 70<=score[i]<=79:
        print(f'{i+1}번째 학생의 등급은 C입니다')
    elif 60<=score[i]<=69:
        print(f'{i+1}번째 학생의 등급은 D입니다')
    else:
        print(f'{i+1}번째 학생의 등급은 F입니다')

#Quiz7
while True:
    text = input()
    length = len(text)
    isdigit =0
    isupper = 0
    islower = 0
    if length < 8:
        print(f'8자리 이상 입력')
    else:
        for char in text:
            if char.isdigit():
                isdigit = 1
            elif char.isupper():
                isupper=1
            elif char.islower():
                islower=1

        if isupper != 1 and islower != 1 and isdigit != 1:
            print(f'대문자 입력 필요')
            print(f'소문자 입력 필요')
            print(f'숫자 입력 필요')
        elif islower != 1 and isdigit != 1:
            print(f'소문자 입력 필요')
            print(f'숫자 입력 필요')
        elif isdigit != 1:
            print(f'숫자 입력 필요')
        else:
            print(f'안전한 비밀번호 입니다.')


