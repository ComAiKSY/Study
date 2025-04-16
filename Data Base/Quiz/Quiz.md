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
