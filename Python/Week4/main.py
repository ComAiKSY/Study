#for : for 변수 in {순서가 있는 데이터 형 : list, 문자열, range, 객체}
#while : while 조건식
a = [1,3,6] #list
for n in a:
    print(n)

for i in range(0,3,1): # 0 ~ 2까지 1씩 증가하는 수열, range type = class range
    # 시작값 : 0, 증감값 : 1
    print(f'hello')
    print(i)

print(list(range(10))) # range(끝값+1), range(시작값, 끝값+1), range(시작값, 끝값+1, 증감값)
#range와 같은 숫자를 나열하는 형태끼리는 서로 type 변경 가능

i=1
while i <=5:
    print(i)
    i+=1

# wildcard : _ , 변수가 위치할 자리에 배치하여 들어오는 정보를 저장하지 않고 버림
# a,b,c = 3, 7, 2
# a,b,_ = 3,7,2 : 2는 버려짐

for i in range(2, -1, -1):
    print(i)

for i in range(1,6,1):
    print(i)

# 합 구하기
hap=0
for i in range(1,11,1):
    # hap = hap + i
    hap += i
print(hap)

# 구구단
for i in range(2,10):
    for n in range(1,10):
        print(f'{i} * {n} = {i * n}')

i = 2
n = 1
while i <= 9:
    while n <= 9:
        if n==5:
            break # 가장 가까운 반복문만 종료 즉 i 는 반복
        print(f'{i} * {n} = {i * n}')
        n += 1
    n = 1 # n 초기화 필요 변수값 관리 필수
    i+= 1



