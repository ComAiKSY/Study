import sys

N = int(sys.stdin.readline().strip())

cnt = 0
while N >= 0:
    if N % 5 == 0:
        print(cnt + N // 5)
        break
    N -= 3
    cnt += 1
else:
    # while이 break 없이 끝난 경우
    print(-1)
