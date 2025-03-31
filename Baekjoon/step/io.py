#2557
print(f'Hello World!')
#1000
num1, num2 = map(int, input().split())
print(f'{num1 + num2}')
#1001
num1, num2 = map(int, input().split())
print(f'{num1 - num2}')
#10998
num1, num2 = map(int, input().split())
print(f'{num1 * num2}')
#1008
num1, num2 = map(float, input().split())
print(f'{num1/num2}')
#10869
num1,num2 = map(int,input().split())
print(f'{num1+num2}\n{num1-num2}\n{num1*num2}\n{int(num1/num2)}\n{num1%num2}')
#10926
name = input()
print(f'{name}??!')
#18108
year = int(input())
print(f'{year-543}')
#10430
A,B,C = map(int, input().split())
print(f'{(A+B)%C}\n{((A%C)+(B%C)%C)}\n{(A*B)%C}\n{((A%C)*(B%C))%C}')
#2588
num1 = int(input())
num2 = int(input())
a = num2 // 100
b = (num2//10) - (a*10)
c = num2 - (a*100) - (b*10)
print(f'{num1*c}\n{num1*b}\n{num1*c}\n{num1*num2}')
#11382
num1, num2, num3 = map(int,input().split())
print(f'{num1+num2+num3}')
