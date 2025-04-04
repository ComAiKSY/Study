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
