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
  
