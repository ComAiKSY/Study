print(f'Hello World!')

num1, num2 = map(int, input().split())
print(f'{num1 + num2}')

num1, num2 = map(int, input().split())
print(f'{num1 - num2}')

num1, num2 = map(int, input().split())
print(f'{num1 * num2}')

num1, num2 = map(float, input().split())
print(f'{num1/num2}')

name = input()
print(f'{name}??!')

year = int(input())
print(f'{year-543}')

A,B,C = map(int, input().split())
print(f'{(A+B)%C}\n{((A%C)+(B%C)%C)}\n{(A*B)%C}\n{((A%C)*(B%C))%C}')