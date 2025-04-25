
mainvalue = int(input('Enter main value: '))
secondvalue = int(input('Enter second value: '))
firstvalue = mainvalue // secondvalue
result = mainvalue - (secondvalue * firstvalue)
print(result)

n = int(input())
for i in range(2, n+1):
	count = 0
	for j in range (1, i+1):
		if i %j == 0:
			count +=1
	if count == 2:
		print(f'{i}는 소수입니다')

num1 = int(input())
for i in range(2, num1+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f'{i}')