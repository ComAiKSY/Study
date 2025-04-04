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

#11021
T = int(sys.stdin.readline())
A = [0]*T
B = [0]*T
total = [0]*T
for i in range(T):
    A[i], B[i] = map(int, sys.stdin.readline().split())
    total[i] = A[i]+B[i]
for i in range(T):
    print(f'Case #{i+1}: {total[i]}')

#11022
T = int(sys.stdin.readline())
A = [0]*T
B = [0]*T
total = [0]*T
for i in range(T):
    A[i], B[i] = map(int, sys.stdin.readline().split())
    total[i] = A[i]+B[i]
for i in range(T):
    print(f'Case #{i+1}: {A[i]} + {B[i]} = {total[i]}')

#2438
N = int(sys.stdin.readline())
for i in range(N):
    print(f'{'*'*(i+1)}')

#2439
N = int(sys.stdin.readline())
for i in range(N):
    print(f'{' '*(N-1-i)}{'*'*(i+1)}')

#10952
A = []
B = []
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==0 and b==0:
        break
    A.append(a)
    B.append(b)
length = len(A)
for i in range(length):
    print(f'{A[i]+B[i]}')

#10951
A=[]
B=[]

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        A.append(a)
        B.append(b)
    except:
        break
length = len(A)
for i in range(length):
    print(f'{A[i]+B[i]}')
