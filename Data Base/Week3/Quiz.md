1. use world; 의미
    'world'라는 이름을 가진 데이터베이스를 사용하겠다.

2. world 데이터베이스에 있는 테이블 목록을 출력하세요
    use world;
    SHOW TABLES;

3. country 테이블의 행의 수
    select count(*) from country;

4. country 테이블에서 국가명에 ko 포함된 나라를 출력
    select * from country name like %ko%;

5. city 테이블, 우리나라 도시들 출력, 국가코드 모름
    select * from city where CountryCode = (select code from country where name = 'south korea')

6. 1. 한국어 사용 나라
        select * from countrylanguage where language = 'korean'
    
    2. 미국에서 사용하는 언어 출력
        select * from countrylanguage where CountryCode = 'usa'
    
    3. 가장 많은 나라에서 사용되는 상위 5개 언어 출력
        SELECT Language, COUNT(DISTINCT CountryCode) AS CountryCount
        FROM countrylanguage
        GROUP BY Language
        ORDER BY CountryCount DESC
        LIMIT 5;
