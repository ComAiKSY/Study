select / from / join / where / group by / order by / limit
Insert into 새로만든 테이블 이름 select 테이블 구조에 맞는 자료 from 원래 테이블
upper : 대문자 / format(숫자, 소수점_자릿수) : 자동으로 세칸 , 삽입
turncate / 전체삭제, 빠름, 테이블 남음
11p 5. select sum(price*amount) from buy where mem_id = 'BLK';
11p 6. select mem_name, debut_date from member where addr = '서울' order by debut_date asc;
12p select mem_name, height from member where height between 163 and 165;
13p select mem_name, addr from member where addr in('경기', '경남', '전남');
14p select * from member where mem_name like '우%';
14p select * from member where mem_name like '__핑크';
15p select mem_name, height from member where height > (select height from member where mem_name = '에이핑크') order by height asc;
27p select mem_id "회원 아이디", sum(amount) "총 구매 개수" from buy group by mem_id order by sum(amount) desc;
28p 1. select mem_id "회원 아이디", sum(amount) "구매 개수", sum(amount * price) "구매 금액" from buy group by mem_id;
28p 2. select mem_id "회원 아이디", sum(amount) "구매 개수", sum(amount * price) "구매 금액" from buy group by mem_id order by sum(amount) desc;
29p select mem_id, avg(amount) from buy group by mem_id
31p select mem_id "회원아이디", sum(price*amount) "구매금액" from buy group by mem_id having sum(price*amount) >= 100 and sum(price*amount) <= 1500

3장 확인문제
4. select Name from country where Name like "%ko%";
5. select name from city where countrycode = (select code from country where name like "%Italy%");
6.1 select name from country where Code in (select CountryCode from countrylanguage where Language = "Korean");
6.2 select language from countrylanguage where CountryCode = "USA";
6.3 select  Language "언어", count(CountryCode) "사용국가수" from countrylanguage group by Language order by count(CountryCode) desc limit 5

4장 문제
28p.2
    select M.addr 지역, sum(B.amount*B.price) 금액 from member M
    inner join buy B
    on M.mem_id = B.mem_id
    GROUP BY M.addr
    order by sum(B.amount*B.price) desc

/////////////////////////////4장 확인문제/////////////////////////////

Quiz 1
    DML : select, update, delete,
    DDL : CREATE, DROP, ALTER
    DCL : revoke, grant
    TCL : savepoint, commit, rollback

Quiz 2
    --, /* */

Quiz 3
    select mem_name, height from member where height = (select max(height) from member) or height = (select min(height) from member)

    select mem_name, height from member where height in (select max(height) from member union select min(height) from member)

Quiz 4
    0 1 1

Quiz 5
    현재 날짜, 현재 날짜 및 시간, 쿼리 실행 시간, 함수 실행시간

Quiz 6
    255자 16335자

Quiz 7
    create table buy2 as select mem_id, price from buy
    prepare myquery from 'update buy2 set price = price + (price*?)'
    set  @rate = 0.1;
    execute myquery using @rate;
    set  @rate = -0.1;
    execute myquery using @rate;
    deallocate prepare myquery;

Quiz 8
    select y.name 도시이름, C.name 나라이름, Y.population 도시인구 from city Y inner join country C on C.Code = Y.CountryCode where Y.Population >= 9000000 order by Y.Population desc

    select name  as 도시이름, (select name from country where code = city.countrycode) as 나라이름, population as 도시인구 from city where Population >= 9000000 order by 도시인구 desc;

Quiz 9
    SELECT
    C.Name AS 나라이름,
    C.Code AS code,
    COUNT(*) AS 공식언어수
    FROM countrylanguage L
    INNER JOIN country C ON C.Code = L.CountryCode
    WHERE L.IsOfficial = 'T'
    GROUP BY C.Code
    HAVING COUNT(*) >= 3
    order by COUNT(*) desc;

    SELECT
        (SELECT name FROM country WHERE code = countrylanguage.CountryCode) AS 나라이름,
        CountryCode AS code,
        COUNT(*) AS 공식언어수
        FROM countrylanguage
        WHERE IsOfficial = 'T'
        GROUP BY CountryCode
        HAVING COUNT(*) >= 3
        ORDER BY 공식언어수 DESC;


Quiz 10
    select UPPER(Y.name) as 도시, FORMAT(Y.population,0) as 인구수 from city Y inner join country C on Y.CountryCode = C.code where Y.CountryCode = 'KOR' order by Y.Population desc limit 5

Quiz 11
    select C.name as 나라, count(*) as 도시수 from country C inner join city Y on C.code = Y.CountryCode group by C.code order by count(*) desc limit 10

    select (select name from country where Code = city.countrycode) as 나라, count(*) as 도시수 from city group by CountryCode order by count(*) desc limit 10

Quiz 12
    select Y.code as 국가코드, Y.name as 국가명 from country Y left join city C on C.countrycode = Y.code where C.name is null

    SELECT code AS 국가코드, name AS 국가명 FROM country WHERE code NOT IN (
    SELECT DISTINCT CountryCode FROM city);

Quiz 13
    CREATE TABLE pay2 SELECT customer_id, amount, payment_date FROM sakila.payment LIMIT 5000;

Quiz 14
    DESC pay2;
    ❗ 복사 시 유지되지 않는 것들

        항목	유지됨?
        컬럼명	✅ 유지됨
        데이터	✅ 유지됨
        기본키(PK)	❌ 유지 안 됨
        NOT NULL, DEFAULT	❌ 유지 안 됨
        AUTO_INCREMENT	❌ 유지 안 됨
        정확한 타입	❌ 일부 변경됨 가능성 있음 (특히 INT 계열)

Quiz 17
    DELETE FROM pay2 WHERE payment_date < '2005-01-01' OR payment_date > '2006-12-31 23:59:59';

    DELETE FROM pay2 WHERE payment_date NOT BETWEEN '2005-01-01' AND '2006-12-31 23:59:59';

Quiz 18
    SELECT DATE_FORMAT(payment_date, '%Y-%m') AS 년월, COUNT(*) AS 건수, SUM(amount) AS 합계 FROM pay2 GROUP BY 년월 WITH ROLLUP;

    Group by with rollup having

Quiz 19
    SELECT CONCAT(C.first_name, ' ', C.last_name) AS 고객명,COUNT(P.customer_id) AS 건수, SUM(P.amount) AS 합계 FROM pay2 P JOIN sakila.customer C ON P.customer_id = C.customer_id GROUP BY P.customer_id ORDER BY 합계 DESC;

Quiz 20
    SELECT first_name, COUNT(*) AS 수 FROM customer GROUP BY first_name HAVING COUNT(*) >= 2;

Quiz 21
    select concat(first_name, ' ', last_name) as 동명이인 from customer where first_name in (select first_name from customer group by first_name having count(*)>=2) order by 동명이인

Quiz 22
    cursor = conn.cursor()

    # 테이블 삭제 SQL
    sql = "DROP TABLE IF EXISTS pay2"

    # 실행
    cursor.execute(sql)

    # 커밋 및 종료
    conn.commit()
    conn.close()

8장 확인 문제

Quiz 1
    shop_db의 usertable에서

    (1)첫 컬럼 userid를 primary key로 지정하세요.

            ALTER TABLE usertable ADD PRIMARY KEY(userid);

    (2) alter로 PK 지정한 경우와 drop table 후 다시 create table 하면서 PK 지정한 경우 어떤 점이 다를까요?

            ALTER로 PK를 지정한 경우는
            → 테이블이 이미 생성된 이후에 별도로 PK를 추가하는 방식입니다.

            CREATE TABLE에서 PK를 지정한 경우는
            → 테이블을 생성하면서 동시에 PK도 함께 정의합니다.

    (3) primary key를 제거하고 원래 구성으로 돌아오려면?

            ALTER TABLE usertable DROP primary key;

Quiz 2
    usertable에 널을 포함한 데이터를 몇 행 insert하세요.

    (1) 테이블명 다음 괄호에 널 제외한 컬럼명 지정 후 insert

        INSERT INTO usertable (userid, username, regyear) VALUES ('user1', '홍길동', 2024);

    (2)insert문에서 테이블명 다음 괄호 없이 모든 컬럼 순서대로 insert
        INSERT INTO usertable
        VALUES ('user2', '김철수', NULL, 2023);

Quiz 3

Quiz 4
    데이터에 null이 있는 경우 리스트박스에 인서트가 안 되어서
    파이썬 화면에 나오는 데이터와 원본과 다를 수 있습니다.
    아래 3가지 방법으로 널처리 (하이픈, 점, 스페이스 같은 특수
    기호가 나오도록 구현) 하세요.

    (1)select할 때 미리 ifnull(컬럼,대체) 해서 가져옴.
        SELECT userid, username, IFNULL(email, '-'), IFNULL(regyear, '.') FROM usertable;

    (2)strData2,3,4에 넣을 때 one-line if문 사용
        strData2 = row[1] if row[1] != None else '-'
        strData3 = row[2] if row[2] != None else '-'
        strData4 = row[3] if row[3] != None else '.'

    (3)리스트박스에 넣을 때 one-line if문 사용
        listbox.insert('', 'end', values=(
            row[0],
            row[1] if row[1] != None else '-',
            row[2] if row[2] != None else '-',
            row[3] if row[3] != None else '.'
        ))

Quiz 5
     [앞 문제에서 계속 연결] 삭제 버튼을 추가하세요. - where 조건은 첫 번째 Entry (기본키인 userid)

        import pymysql
        from tkinter import *

        def delete_data():
            conn = pymysql.connect(host='localhost', user='root',
                                password='1234', db='shop_db', charset='utf8')
            cur = conn.cursor()

            uid = entry1.get()  # 첫 번째 Entry에 입력된 값 (userid)

            sql = "DELETE FROM usertable WHERE userid = %s"
            cur.execute(sql, (uid,))
            conn.commit()

            conn.close()
            print(f"{uid} 삭제 완료!")

        # GUI 설정 예시
        window = Tk()
        window.title("삭제 예제")

        Label(window, text="사용자 ID").grid(row=0, column=0)
        entry1 = Entry(window)
        entry1.grid(row=0, column=1)

        deleteBtn = Button(window, text="삭제", command=delete_data)
        deleteBtn.grid(row=1, column=0, columnspan=2)

        window.mainloop()

Quiz #6
 [앞 문제들의 결과를 모두 반영해서] market_db의 member 테이블에 대한 입력/조회/삭제 프로그램을 구현하세요.
 - (primary key 는 이미 설정되어 있으므로 생략)
 - 널 처리
 - 삭제버튼 추가

    import pymysql
    from tkinter import *
    from tkinter import messagebox

    def insert_member():
        uid = entry_id.get()
        name = entry_name.get()
        addr = entry_addr.get()

        # 널 처리: 입력 없으면 하이픈 대체
        name = name if name else '-'
        addr = addr if addr else '-'

        conn = pymysql.connect(host='localhost', user='root', password='1234', db='market_db', charset='utf8')
        cur = conn.cursor()
        sql = "INSERT INTO member(mem_id, mem_name, addr) VALUES (%s, %s, %s)"
        try:
            cur.execute(sql, (uid, name, addr))
            conn.commit()
            messagebox.showinfo("성공", "회원 등록 완료")
        except:
            messagebox.showerror("오류", "중복 ID 혹은 입력 오류")
        conn.close()

    def select_member():
        listbox.delete(0, END)
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='market_db', charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT mem_id, IFNULL(mem_name, '-'), IFNULL(addr, '-') FROM member")
        rows = cur.fetchall()
        for row in rows:
            listbox.insert(END, f"{row[0]} | {row[1]} | {row[2]}")
        conn.close()

    def delete_member():
        uid = entry_id.get()
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='market_db', charset='utf8')
        cur = conn.cursor()
        sql = "DELETE FROM member WHERE mem_id = %s"
        cur.execute(sql, (uid,))
        conn.commit()
        conn.close()
        messagebox.showinfo("삭제 완료", f"{uid} 삭제됨")

    # GUI
    window = Tk()
    window.title("회원 관리 시스템")

    Label(window, text="ID").grid(row=0, column=0)
    Label(window, text="이름").grid(row=1, column=0)
    Label(window, text="주소").grid(row=2, column=0)

    entry_id = Entry(window)
    entry_name = Entry(window)
    entry_addr = Entry(window)

    entry_id.grid(row=0, column=1)
    entry_name.grid(row=1, column=1)
    entry_addr.grid(row=2, column=1)

    btn_insert = Button(window, text="입력", command=insert_member)
    btn_select = Button(window, text="조회", command=select_member)
    btn_delete = Button(window, text="삭제", command=delete_member)

    btn_insert.grid(row=3, column=0)
    btn_select.grid(row=3, column=1)
    btn_delete.grid(row=3, column=2)

    listbox = Listbox(window, width=50)
    listbox.grid(row=4, column=0, columnspan=3)

    window.mainloop()
