numlist = [10,20,30]
numlist[1:2] = [200, 201] #Slice 형태 리스트 내 범위 바꾸기
print(numlist) 

my_list = [10,20,30]
my_list = my_list[:-1] + [200, 201] # 끝자리 이어 붙이기
 
my_list = my_list[:1] + [200, 201] + my_list[:2] # 중간자리 이어 붙이기 10, 200, 201, 30

while 10 in  my_list: # my_list 안에 10이 있으면 다 지워질때까지 돌리기
    my_list.remove(10) 
