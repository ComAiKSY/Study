#10807
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