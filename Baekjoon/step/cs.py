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