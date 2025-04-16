11p 5. select sum(price*amount) from buy where mem_id = 'BLK';
11p 6. select mem_name, debut_date from member where addr = '서울' order by debut_date asc;
12p select mem_name, height from member where height between 163 and 165;
13p select mem_name, addr from member where addr in('경기', '경남', '전남');
14p select * from member where mem_name like '우%';
14p select * from member where mem_name like '__핑크';
15p select mem_name, height from member where height > (select height from member where mem_name = '에이핑크') order by height asc;