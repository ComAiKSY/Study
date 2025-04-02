#1330
num1, num2 = map(int, input().split())
if num1 > num2:
    print(f'>')
elif num1 < num2:
    print(f'<')
else:
    print(f'==')

#9498
score=int(input())
if 90<=score <=100:
    print(f'A')
elif 80<= score <= 89:
    print(f'B')
elif 70<= score <=79:
    print(f'C')
elif 60<= score <= 69:
    print(f'D')
else:
    print(f'F')

#2753
year = int(input())
if year%4==0 and year%100 !=0 or year%400==0:
    print('1')
else:
    print('0')

#14681
x = int(input())
y = int(input())

if x>0 and y>0:
    print('1')
elif x < 0 < y:
    print('2')
elif x<0 and y<0:
    print('3')
else:
    print('4')

#2884
h,m= map(int, input().split())
if m-45 < 0:
    m = 45 -m
    m = 60 -m
    if h==0:
        h = 23
    else:
        h = h-1
    print(f'{h} {m}')
else:
    print(f'{h} {m}')

#2525
h, m = map(int, input().split())
m1 = int(input())
if m + m1 >= 60:
    h = h+1
    if h == 24:
        h = 0
    m = m+m1 - 60
    if m == 60:
        h=h+1
        if h == 24:
            h=0
        m = 0
        print(f'{h} {m}')
    else:
        print(f'{h} {m}')
else:
    print(f'{h} {m+m1}')