a=99
if a<100:
    print(f'a는 100보다 작다') # 들여쓰기(indentation) 중요
    print(f'두번째 print 부터는 들여쓰기 상관 X')

a=200
if a<100:
    print(f'100보다 작군요')
else:
    print(f'100보디 크군요')

#중첩 조건문

a=75
if a>50:
    if a<100:
        print(f'50 over 100 under')
    else:
        print(f'100 over')
else:
    print(f'50under')

#중첩 조건문 예제
a=int(input('Enter number : '))
if a>=90:
    print(f'A', end="") #print는 마지막에 자동 줄바꿈
else:
    if a>=80:
        print(f'B', end="")
    else:
        if a>=70:
            print(f'C', end="")
        else:
            if a>=60:
                print(f'D', end="")
            else:
                print(f'E', end="")
print(f'학점입니다')

#삼항연산자 : 조건에 따라 대입되는 값이 결정될 때 사용
score = 70
res = '합격' if score >= 60 else '불합격'
# '변수' = '참일때 대입값' if '조건식' else '거짓일 경우 대입값'

#조건문 예제
age = int(input('Enter age : '))
if age < 20:
    print(f'go home')
else:
    print(f'thx')

#가위바위보
import random
com = random.choice(['가위', '바위', '보'])
human = input(f'가위, 바위, 보 중 하나 선택 :')

print(f'com:{com} human:{human}')
if human == com:
    print('비겼습니다!')
elif (human == '가위' and com == '보') or (human == '바위' and com == '가위') or (human == '보' and com == '바위'):
    print('당신이 이겼습니다!')
else:
    print('당신이 졌습니다!')