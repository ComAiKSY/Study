#2739
N = int(input())
for i in range(1,10):
    print(f'{N} * {i} = {N*i}')

#10950
num = int(input())
for _ in range(num):
    A, B = map(int, input().split())
    print(f'{A+B}')

#8393
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)

#25304
X = int(input())
type = int(input())
price =[0]*type
num = [0]*type
total = 0
for i in range(type):
    price[i], num[i] = map(int, input().split())
    total += price[i]*num[i]
if X == total:
    print(f'Yes')
else:
    print(f'No')

#25314
N = int(input())
num = N//4 #몫연산은 int, 일반 나눗셈은 float
print(f'{'long '*num}int')

#15552
import sys
n = int(sys.stdin.readline())
first = [0]*n
second = [0]*n
total = [0]*n
for _ in range(n):
    first[_], second[_] = map(int, sys.stdin.readline().split())
    total[_] = first[_] + second[_]
for _ in range(n):
    print(total[_])

