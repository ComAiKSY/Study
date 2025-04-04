import pymysql

connect = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='market_db', charset='utf8')
cursor = connect.cursor()

cursor.execute("SELECT * FROM member")  # 예시 테이블 이름

print("사용자ID     사용자이름이메일가입연도")
print("---------------------------------------------------------")

while True:
    row = cursor.fetchone()
    if row == None:
        break
    print("%-5s  %-10s  %2d  %-4s  %-4s  %-10s  %3d  %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

connect.close()