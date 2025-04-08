#27866
import sys

word = str(sys.stdin.readline().strip())
array = list(word)
i = int(sys.stdin.readline())
print(array[i-1])

#2743
word = str(sys.stdin.readline().strip())
length = len(word)
print(length)

#9086
T = int(sys.stdin.readline())
result = [0]*T
for i in range(T):
    W = str(sys.stdin.readline().strip())
    length = len(W)
    array = list(W)
    result[i] = array[0] + array[length-1]

for i in range(T):
    print(result[i])
