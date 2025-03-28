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


