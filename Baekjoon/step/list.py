#10807
import sys
from asyncio.windows_events import INFINITE

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
V = int(sys.stdin.readline())
count = 0
for i in range(N):
    if A[i] == V:
        count+=1
print(count)

#10871
N, X = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = []
# for i in range(N):
#     if A[i] < X:
#         B.append(A[i])
# print(B) # 배열출력
for i in A:
    if i < X:
        print(i, end=' ')


#10818
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
min = 10000001
max = 0
for i in A:
    if i < min:
        min = i
    elif i > max:
        max = i
print(f'{min} {max}')

#2526
A=[0]*9
max = 0
max_index = -1
for i in range(9):
    A[i] = int(sys.stdin.readline())

for i in range(9):
    if A[i] > max:
        max = A[i]
        max_index = i+1
print(f'{max}\n{max_index}')

#10810
N, M = map(int,sys.stdin.readline().split())
array = [0]*N
for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    for j in range(a-1,b):
        array[j] = c
for k in range(N):
    print(array[k], end=' ')

#10813
N, M = map(int,sys.stdin.readline().split())
array= [0]*N
for i in range(N):
    array[i] = i+1
for j in range(M):
    a, b = map(int, sys.stdin.readline().split())
    array[a-1], array[b-1] = array[b-1], array[a-1]
for k in range(N):
    print(array[k], end=' ')

#5597
num = 28
count = [0]*30
for i in range(num):
    flag = int(sys.stdin.readline())
    count[flag-1] = 1
for i in range(num):
    if count[i] == 0:
        print(i+1)

#3052
N = [0]*10
remain = [0]*10
count = 10
diff = 0
for i in range(10):
    N[i] = int(sys.stdin.readline())
    remain[i] = N[i]%42
for i in range(1,10):
    for j in range(0,i-1):
        if remain[i] == remain[j]:
            count -=1
print(count)

#10811
N, M = map(int, sys.stdin.readline().split())
array = [i + 1 for i in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a
    a -= 1
    b -= 1
    while a < b:
        array[a], array[b] = array[b], array[a]
        a += 1
        b -= 1

print(*array)

#1546
total = 0
N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
M = max(score)
for i in range(N):
    score[i] = score[i]/M*100
for i in range(N):
    total += score[i]
print(total/N)