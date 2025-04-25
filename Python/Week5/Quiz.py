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
	isdigit = 0
	isupper = 0
	islower = 0
	pass1 = input()
	length = len(pass1)

	if length < 5:
		print(f'다시입력')
		continue
	for char in pass1:
		if char.isdigit():
			isdigit = 1
		if char.isupper():
			isupper = 1
		if char.islower():
			islower = 1

	if isdigit == 1 and isupper == 0 and islower == 0:
		print(f'문자입력')
		continue
	if isdigit == 0:
		print(f'숫자입력')
		continue
	elif isupper == 0:
		print(f'대문자')
		continue
	elif islower == 0:
		print(f'소문자')
		continue
	if isdigit == 1 and isupper == 1 and islower == 1:
		print(f'완벽합니다')
		break

#Quiz8
num1, num2 = map(float, input().split())
count = int(num1 // num2)
if num1 - count*num2 > 0:
    print(f'{count}번')
else:
    print(f'{count-1}번')

#Quiz9
import random
weight = int(input())
num1 = int(input())
item = []
for _ in range(num1):
    item.append(random.randint(1, 50))

for i in range(num1):
    print(f'아이템 무게 : {item[i]}')
    weight = weight - item[i]
    if weight < 0:
        print(f'{i}개 담음,{weight+item[i]}남음')
        break

#Quiz10
import random
num1 = int(input())
count = 0
for i in range(num1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    print(f'{a}X{b} = ')
    num2 = int(input())
    if a*b == num2:
        print(f'정답')
        count+=1
    else:
        print(f'오답')
print(f'{count}개 정답')

#Quiz11
height = int(input())
for i in range(height):
    count = i*2+1
    print(f'{" "*(height-i-1)}{"*"*count}{" "*(height-i-1)}')

#Quiz12
num1 = int(input())
count = 0
while True:
    if num1 % 2 == 0:
        num1 = num1//2
        count +=1
    else:
        num1 = num1*3+1
        count +=1
    if num1 == 1:
        print(f'{count}번')
        break

#Quiz13
num1 = int(input())
time = []
money = []
for i in range(num1):
    time.append(int(input()))
    money.append(int(input()))
    if time[i] > 40:
        print(f'{i+1}번째 직원의 주급은 {money[i]*time[i]*1.5}')
    else:
        print(f'{i + 1}번째 직원의 주급은 {money[i] * time[i]}')

#Quiz14
num1 = int(input())
for i in range(2, num1+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f'{i}')

#Quiz15
month = int(input())
day = int(input())
if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print(f'물병')
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print(f'물고기')
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print(f'양')
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print(f'황소')
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    print(f'쌍둥이')
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    print(f'게')
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print(f'사자')
elif (month == 8 and day >= 23) or (month == 9 and day <= 23):
    print(f'처녀')
elif (month == 9 and day >= 24) or (month == 10 and day <= 22):
    print(f'천칭')
elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
    print(f'전갈')
elif (month == 11 and day >= 23) or (month == 12 and day <= 24):
    print(f'사수')
elif (month == 12 and day >= 25) or (month == 1 and day <= 19):
    print(f'염소')



