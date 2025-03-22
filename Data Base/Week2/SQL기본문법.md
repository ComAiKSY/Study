# SELECT 문


# BETWEEN ~ AND 문
  BETWEEN A AND B 로 사용한다, A ~ B 사이값을 찾을 때 사용한다.
  BETWEEN 160 ~ 150 : 문법적으로 틀리지 않았지만 출력결과 없음

# IN()
  특정 데이터 찾을 때 사용한다.
  WHERE addr IN('경기', '전남', '경남');

# like %_
  특정 조건으로 시작하거나 끝나는 데이터 찾을 때 사용한다.
  WHERE name LIKE '우%'; : '우'로 시작하는 데이터를 찾을 때 사용
  WHERE name LIKE '__우'; : 앞에 두글자(__)가 있고 '우'로 끝나는 데이터를 찾을 때 사용

# 서브쿼리
  SELECT height FROM member WHERE mem_name = '에이핑크';
  SELECT mem_namem, height FROM member WHERE height > 164;
  에이핑크보다 큰 키를 가진 회원을 찾고자 할 때 에이핑크를 찾은 후 164 초과인 사람을 찾는다. 즉 두번의 실행이 필요함

  SELECT mem_name, height FROM member WHERE height > (SELECT height FROM member WHERE mem_name = '에이핑크')
  mem_name 과 height 을 출력할것이다, member로 부터 조건은 height 이 ()보다 큰것
  () member 테이블의 height을 출력할것이다. mem_name이 에이핑크
  따라서 에이핑크의 height을 출력한 후 그 출력값을 조건문으로 사용함

# ORDER BY
  DESC : 내림차순
  ASC : 오름차순

# LIMIT
  from ~ limit 0, 2; (시작위치, 행의 개수)
  from ~ limit 2; (시작위치 생략 가능 : 생략시 시작위치 기본 0)

# DISTINCT
  중복 결과 제거
  