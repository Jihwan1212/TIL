---
contents: 2025년 2월 28일 금요일
tags:
  - "#SQL"
  - "#관계형데이터베이스"
  - "#SQL기본"
  - "#SQL활용"
  - "#관리구문"
  - "#데이터베이스"
  - "#스키마"
  - "#데이터무결성"
---

# 1장. SQL 기본
## 관계형 데이터베이스
- DB
	- 특정 기업이나 조직 또는 개인이 필요에 의해 데이터를 일정한 형태로 저장해 놓은 것을 의미
- DBMS
	- 효율적인 데이터 관리뿐만 아니라 예기치 못한 사건으로 인한 데이터의 손상을 피하고, 필요시 데이터를 복구하기 위한 기능의 SW

### 관계형 DB 구성 요소
- 계정: 데이터 접근 제한을 위한 시스템별 계정이 존재
- 테이블: DBMS의 DB안에서 데이터가 저장되는 형식
	- 테이블의 특징
		- 하나의 테이블은 반드시 하나의 유저 소유여야 함
		- 가로 = 행 = 로우 = 튜플 = 인스턴스
		- 세로 = 열 = 컬럼
		- 테이블간 관계는 일대일, 일대다, 다대다의 관계
		- 테이블명은 중복될 수 없음
			- 소유자가 다른 경우 같은 이름으로 생성 가능
- 스키마: 테이블이 어떠한 구성으로 되어있는지 기본적인 구조를 정의

### 관계형 DB 특징
- 데이터 탐색 속도가 빠름
- 신뢰성이 높고 **데이터의 무결성** 보장
	- **개체 무결성**
		- 기본키를 구성하는 컬럼은 Null 값이나 중복값을 가질 수 없음
		- 테이블의 모든 행은 유일하게 식별 가능해야 함
	- **참조 무결성**  
		- 외래키 값은 Null이거나 참조 테이블의 기본키 값과 동일
		- 참조되는 테이블의 기본키가 변경/삭제될 때 참조하는 테이블도 함께 변경되어야 함
	- **도메인 무결성**
		- 주어진 속성 값이 정의된 **도메인**에 속한 값 이어야 함
			- 각 컬럼이 갖는 범위
		- 컬럼에 정의된 데이터 타입, 길이, NULL 여부 등의 제약조건을 만족해야 함
	- **Null 무결성**
		- 특정 속성에 대해 Null을 허용하지 않는 특징
		- NOT NULL 제약조건이 설정된 컬럼은 반드시 값이 입력되어야 함
	- **고유 무결성**
		- 특정 속성에 대해 값이 중복되지 않는 특징
		- UNIQUE 제약조건이 설정된 컬럼은 중복된 값을 가질 수 없음
	- **키 무결성**
		- 하나의 **릴레이션**에는 적어도 하나의 키가 존재해야 함
			- 테이블간 관계를 의미
		- 모든 테이블은 반드시 기본키를 가져야 하며 이를 통해 각 행을 식별할 수 있어야 함
- 기존에 작성된 스키마를 수정하기 어려움

### SQL
- 관계형 데이터베이스에서 데이터 조회 및 조작, DBMS 시스템 관리 기능을 명령하는 언어
- **대, 소문자를 구분하지 않음**

## SELECT문
### SQL 종류
- DDL(Data Definition Language)
	- 데이터베이스 객체의 구조를 정의하는 언어
	- CREATE, ALTER, DROP, TRUNCATE
- DML(Data Manipulation Language)
	- 데이터베이스 내의 데이터를 조작하는 언어
	- INSERT, DELETE, UPDATE, MERGE
- DCL(Data Contrl Language)
	- 데이터베이스에 대한 접근 권한을 제어하는 언어
	- GRANT, REVOKE
- TCL(Transaction Control Language)
	- 트랜잭션을 제어하는 언어
	- COMMIT, ROLLBACK
- DQL(Data Query Language)
	- 데이터베이스에서 데이터를 조회하는 언어
	- SELECT

### SELECT문 구조
- SELECT 문은 다음과 같이 **6개 절로 구성**
- **각 절의 순서대로 작성해야 함**
	- GROUP BY와 HAVING은 서로 바꿀 수 있지만 보통 사용하지 않음
- SELECT 문의 내부 파싱(문법적 해석) 순서는 나열된 순서와 다름
- **실행 순서**(파싱순서)
	- **FROM > WHERE > GROUP BY > HAVING > SELECT > ORDER BY**
``` SQL
SELECT * | 컬럼명 | 표현식 
	FROM 테이블명 또는 뷰명  
WHERE 조회 조건  
GROUP BY 그룹핑 칼럼명  
HAVING 그룹핑 필터링 조건  
	ORDER BY 정렬 칼럼명
```

### SELECT 절
- SELECT 문장을 사용해 불러올 컬럼명, 연산 결과를 작성
- \* 를  사용해 테이블 내 전체 컬럼명을 불러올 수 있음
- 원하는 컬럼을 ,로 나열하여 작성가능
- 표현식: 원래의 컬럼명을 제외한 모든 표현 가능한 대상
	- SELECT 절 특징
		- SELECT절에서 표시할 대상 컬럼에 [[#Alias]](별칭) 지정 가능
		- 대소문자를 구분하지 않아도 됨

### Alias
- 컬럼명 대신 출력할 임시 이름 지정
- select절에서만 정의 가능
- 원본 컬럼명은 변경되지 않음
- 컬럼명 뒤에 AS와 함께 컬럼 별칭 전달(**AS는 생략 가능**)
	- Alias 특징
		- select문 보다 늦게 수행되는 order by 절에서만 컬럼 별칭 사용 가능
		- 한글 사용가능
		- 이미 존재하는 예약어는 별칭으로 사용 불가
			- avg, count, decode
		- **다음의 경우 별칭에 반드시 쌍따옴표 전달 필요**
			- 별칭에 공백을 포함하는 경우
			- 별칭에 특수문자를 포함하는 경우("\_" 제외)
			- 별칭 그대로 전달할 경우(입력한 대소를 그래도 출력시)

``` SQL
select EMPNO, ENAME, SAL * 1.1 AS "NEW SAL"
	FROM EMP;
```
 
## FROM 절
- 데이터를 불러올 테이블명 또는 뷰명 전달
- 테이블 여러 개 전달 가능
	- 컴마로 구분
	- 조인 조건 없이 테이블명만 나열 시 카티시안 곱 발생 주의
- **테이블 별칭 선언 가능**
	- ORACLE은 AS 사용 불가
	- SQL Server는 사용/생략가능
	- 테이블 병칭 선언 시 컬럼 구분자는 테이블 병칭으로만 전달
- ORACLE에서는 FROM절 생략 불가
	- 의미상 필요 없는 경우 DUAL 테이블 선언
- SQL Server에서는 FROM절 필요 없을 경우 생략 가능(오늘 날짜 조회 시)

## 함수
 - input value와 output value의 관계를 정의한 객체
 - from 절을 제외한 모든 절에서 사용 가능
 - 함수의 종류
	 - 단일행 함수
		 - input과 output의 관계가 1:1 
	- 복수행 함수
		- 여러 건의 데이터를 동시에 입력 받아서 하나의 요약값을 리턴
		- 그룹함수 또는 집계함수라고 함
- 입출력값의 타입에 따른 분류
	- [[#문자형 함수]]
		- 문자열 결합, 추출, 삭세 수행
		- 단일행 함수 형태
		- output은 대부분 문자값
	- [[#숫자형 함수]]
		- 단일행 함수 형태의 숫자 함수
		- oracle과 sql 함수 거의 동일
	- [[#날짜형 함수]]
		- oracle과 sql 함수가 아주 차이남
		- 출제빈도는 낮을 것
	- [[#변환함수]]
		- 값의 데이터 타입을 변환
			- 문자를 숫자로
			- 숫자를 문자로
			- 날짜를 문자로
	- [[#그룹함수]]
		- 여러 값이 input값으로 들어가서 하나의 요약된 값으로 리턴
		- group by와 함께 자주 사용
		- oracle과 sql 함수 거의 동일
	- [[#일반함수]]

### 문자형 함수

| 함수명                         | 함수기능                        | 사용예시                          | 출력    | 기타설명                                   |
| --------------------------- | --------------------------- | ----------------------------- | ----- | -------------------------------------- |
| LOWER(대상)                   | 문자를 소문자로 변환                 | LOWER('ABC')                  | abc   |                                        |
| UPPER(대상)                   | 문자를 대문자로 변환                 | UPPER('abc')                  | ABC   |                                        |
| **SUBSTR**(대상, m, n)        | 문자열 중 m위치에서 n개의 문자열 추출      | SUBSTR('ABCDE', 2, 3)         | BCD   | n 생략 시 끝까지 추출                          |
|                             |                             | SUBSTR('ABCDE', -4, 3)        | BCD   | 뒤에서 4번째(B)부터 오른쪽으로 3개의 문자 추출           |
| **INSTR**(대상, 찾을문자열, m, n)  | 대상에서 찾을문자열 위치 반환            | INSTR('A#B#C#', '#')          | 2     | m, n 생략 시 1로 해석                        |
|                             |                             | INSTR('A#B#C#', '#', 3, 2)    | 6     | 3번째부터 두 번째 발견된 위치                      |
|                             |                             | INSTR('A#B#C#', '#', -3, 2)   | 2     | 뒤에서 3번째(#)에서 왼쪽으로 스캔하여 두 번째로 발견된 위치 리턴 |
| L**TRIM**(대상, 삭제문자열)        | 문자열 중 특정 문자를 왼쪽에서 삭제        | LTRIM('AABBAA', 'A')          | BBAA  | 삭제문자열 생략 시 공백 삭제                       |
| R**TRIM**(대상, 삭제문자열)        | 문자열 중 특정 문자를 오른쪽에서 삭제       | RTRIM('AABBAA', 'A')          | AABB  | 삭제문자열 생략 시 공백 삭제                       |
| **TRIM**(대상)                | 문자열 중 특정 문자를 양쪽에서 삭제        | TRIM(' ABCDE ')               | ABCDE | ORACLE TRIM은 공백만 삭제 가능                 |
| L**PAD**(대상, n, 문자열)        | 대상 왼쪽에 문자열을 추가하여 총 n 길이 리턴  | LPAD('ABC', 5, '*')           | **ABC |                                        |
| R**PAD**(대상, n, 문자열)        | 대상 오른쪽에 문자열을 추가하여 총 n 길이 리턴 | RPAD('ABC', 5, '*')           | ABC** |                                        |
| CONCAT(대상1, 대상2)            | 문자열 결합                      | CONCAT('A', 'B')              | AB    | 두 개의 인수만 전달 가능                         |
| LENGTH(대상)                  | 문자열 길이 반환                   | LENGTH('ABCDE')               | 5     |                                        |
| REPLACE(대상, 찾을문자열, 바꿀문자열)   | 문자열 치환 및 삭제                 | REPLACE('ABBA', 'AB', 'ab')   | abBA  | 세 번째 인수를 생략하거나 빈 문자열 전달 시 찾을 문자열 삭제    |
| TRANSLATE(대상, 찾을문자열, 바꿀문자열) | 글자를 1대1로 치환                 | TRANSLATE('ABBA', 'AB', 'ab') | abba  | 매칭되는 글자끼리 1:1 치환, 바꿀문자열 생략 시 삭제됨       |

### 숫자형 함수
| 함수명            | 함수기능                              | 사용예시               | 출력     | 기타설명                               |
| -------------- | --------------------------------- | ------------------ | ------ | ---------------------------------- |
| ABS(숫자)        | 절댓값 반환                            | ABS(-1.5)          | 1.5    | 소수점 둘째자리로 반올림                      |
| ROUND(숫자, 자리수) | 소수점 특정 자리에서 반올림                   | ROUND(123.456, 2)  | 123.46 |                                    |
|                |                                   | ROUND(123.456, -2) | 100    | 자리수가 음수이면 정수자리에서 반올림 (백의 자리에서 반올림) |
| TRUNC(숫자, 자리수) | 소수점 특정 자리에서 버림                    | TRUNC(123.456, 2)  | 123.45 |                                    |
| SIGN(숫자)       | 숫자가 양수면 `1`, 음수면 `-1`, 0이면 `0` 반환 | SIGN(100)          | 1      |                                    |
| FLOOR(숫자)      | 작거나 같은 최대 정수 반환                   | FLOOR(3.5)         | 3      |                                    |
| CEIL(숫자)       | 크거나 같은 최소 정수 반환                   | CEIL(3.5)          | 4      |                                    |
| MOD(숫자1, 숫자2)  | 숫자1을 숫자2로 나눈 나머지 반환               | MOD(7,2)           | 1      |                                    |
| POWER(m,n)     | `m`의 `n` 거듭제곱                     | POWER(2,4)         | 16     |                                    |
| SQRT(숫자)       | 루트값 반환                            | SQRT(16)           | 4      |                                    |

### 날짜형 함수
| 함수명                      | 함수기능                      | 사용예시                              | 출력                         | 기타설명                              |
| ------------------------ | ------------------------- | --------------------------------- | -------------------------- | --------------------------------- |
| SYSDATE                  | 현재 날짜와 시간 리턴              | SYSDATE                           | 2024/02/14 18:44:34        | 날짜출력형식에 따라 다르게 출력됨 (날짜만 출력될 수 있음) |
| CURRENT_DATE             | 현재 날짜 리턴                  | CURRENT_DATE                      | 2024/02/14                 | 날짜출력형식에 따라 다르게 출력됨 (시간이 출력될 수 있음) |
| CURRENT_TIMESTAMP        | 현재 타임스탬프 리턴               | CURRENT_TIMESTAMP                 | 2024/02/14 18:45:29 +09:00 |                                   |
| ADD_MONTHS(날짜, n)        | 날짜에서 `n`개월 후 날짜 리턴        | ADD_MONTHS(SYSDATE, 3)            | 2024/05/14 18:44:34        | `n`이 음수인 경우 `n`개월 이전 날짜 리턴        |
| MONTHS_BETWEEN(날짜1, 날짜2) | 날짜1과 날짜2의 개월 수 리턴         | MONTHS_BETWEEN(SYSDATE, HIREDATE) | 3.7234                     | 날짜1 < 날짜2로 전달 시 음수 리턴             |
| LAST_DAY(날짜)             | 주어진 월의 마지막 날짜 리턴          | LAST_DAY(SYSDATE)                 | 2024/02/29 18:44:34        |                                   |
| NEXT_DAY(날짜, n)          | 주어진 날짜 이후 지정된 요일의 첫 날짜 리턴 | NEXT_DAY(SYSDATE, 1)              | 2024/02/18 18:51:35        | `1: 일요일, 2: 월요일, ... 7: 토요일`      |
| ROUND(날짜, 자리수)           | 날짜 반올림                    | ROUND(SYSDATE, 'MONTH')           | 2024-02-01 00:00           | 월 이전 기준으로 반올림                     |
| TRUNC(날짜, 자리수)           | 날짜 버림                     | TRUNC(SYSDATE, 'MONTH')           | 2024-02-01 00:00           | 월 이전 기준으로 버림                      |
### 변환함수
| 함수명               | 함수기능                     | 사용예시                                | 출력                  | 기타설명                     |
| ----------------- | ------------------------ | ----------------------------------- | ------------------- | ------------------------ |
| TO_NUMBER(문자)     | 숫자 타입으로 변경하여 리턴          | TO_NUMBER('100')                    | 100                 | 문자 `100`을 숫자 `100`으로 리턴  |
| TO_CHAR(대상, 포맷)   | 1) 날짜의 포맷 변경             | TO_CHAR(SYSDATE, 'MM/DD-YYYY')      | 02/14-2024          | 날짜 형식 변경 (리턴은 문자 타입)     |
|                   | 2) 숫자의 포맷 변경             | TO_CHAR(9000, '9,999')              | 9,000               | 천단위 구분기호 생성 (리턴은 문자 타입)  |
|                   |                          | TO_CHAR(9000, '09999')              | 09000               | 총 5자리로 리턴 (앞 자리수 0으로 채움) |
| TO_DATE(문자, 포맷)   | 주어진 문자를 포맷 형식에 맞춰 날짜로 변환 | TO_DATE('2024/01/01', 'YYYY/MM/DD') | 2024/01/01 00:00:00 | 날짜로 변환됨                  |
| FORMAT(날짜, 포맷)    | 날짜의 포맷 변경                | FORMAT(GETDATE(), 'YYYY')           | 2024                | SQL SERVER 함수            |
| CAST(대상 AS 데이터타입) | 대상을 주어진 데이터타입으로 변환       | CAST('100' AS int)                  | 100                 | 문자 `100`을 숫자 `100`으로 리턴  |

### 그룹함수
| 함수명          | 함수기능    | 사용예시                           | 출력      | 기타설명         |
| ------------ | ------- | ------------------------------ | ------- | ------------ |
| COUNT(대상)    | 행의 수 리턴 | SELECT COUNT(SAL) FROM EMP;    | 각 연산 결과 | NULL 무시하고 연산 |
| SUM(대상)      | 총 합 리턴  | SELECT SUM(SAL) FROM EMP;      | 각 연산 결과 | NULL 무시하고 연산 |
| AVG(대상)      | 평균 리턴   | SELECT AVG(SAL) FROM EMP;      | 각 연산 결과 | NULL 무시하고 연산 |
| MIN(대상)      | 최소값 리턴  | SELECT MIN(SAL) FROM EMP;      | 각 연산 결과 | NULL 무시하고 연산 |
| MAX(대상)      | 최대값 리턴  | SELECT MAX(SAL) FROM EMP;      | 각 연산 결과 | NULL 무시하고 연산 |
| VARIANCE(대상) | 분산 리턴   | SELECT VARIANCE(SAL) FROM EMP; | 각 연산 결과 | NULL 무시하고 연산 |
| STDDEV(대상)   | 표준편차 리턴 | SELECT STDDEV(SAL) FROM EMP;   | 각 연산 결과 | NULL 무시하고 연산 |
### 일반함수
| 함수명                                     | 함수기능                                          | 사용예시                    | 출력                                 | 기타설명                              |
| --------------------------------------- | --------------------------------------------- | ----------------------- | ---------------------------------- | --------------------------------- |
| DECODE(대상, 값1, 리턴1, 값2, 리턴2, ..., 그외리턴) | 대상이 값1이면 리턴1, 값2와 같으면 리턴2, 그 외에는 그외리턴값 리턴     | DECODE(DEPTNO,10,A,B)   | A 또는 B                             | 대소비교에 따른 치환 불가, 그외리턴 생략 시 NULL 리턴 |
| **NVL**(대상, 치환값)                        | 대상이 NULL이면 치환값으로 치환하여 리턴                      | NVL(COMM, 0)            | COMM값 또는 0 리턴                      |                                   |
| **NVL2**(대상, 치환값1, 치환값2)                | 대상이 NULL이 아닐 때 치환값1로 치환, NULL이면 치환값2로 치환하여 리턴 | NVL2(COMM, COMM*1.1, 0) | COMM값이면 `COMM*1.1` 리턴, NULL이면 0 리턴 |                                   |
| COALESCE(대상1, 대상2, ..., 그외리턴)           | 대상들 중 NULL이 아닌 값 출력 (가장 첫 번째 값)               | COALESCE(NULL, 100)     | 100                                | 그외리턴값 생략 시 NULL 리턴                |
| ISNULL(대상, 치환값)                         | 대상이 NULL이면 치환값 리턴                             | ISNULL(NULL, 100)       | 100                                | SQL SERVER 함수                     |
| NULLIF(대상1, 대상2)                        | 두 값이 같으면 NULL 리턴, 다르면 대상1 리턴                  | NULLIF(10,20)           | 10                                 |                                   |
| **CASE문**                               | 조건별 치환 및 연산 수행                                | 아래 참고                   |                                    |                                   |

---
contents: 2025년 2월 19일 수요일
tags:
  - Book
---
---
contents: 2025년 2월 19일 수요일
tags:
  - Book
---
ㅇ## WHERE 절
  - 조건에 맞는 데이터만 조회하고 싶을 경우 사용 (필터기능)
  - NULL 조회 시 IS NULL / IS NOT NULL 연산자 사용(= 연산자 조회 불가)
### 연산자 종류

| **연산자 종류**            | **설명**                          |
| --------------------- | ------------------------------- |
| =                     | 같은 조건을 검색                       |
| !=, <>                | 같지 않은 조건을 검색                    |
| >                     | 큰 조건을 검색                        |
| >=                    | 크거나 같은 조건을 검색                   |
| <                     | 작은 조건을 검색                       |
| <=                    | 작거나 같은 조건을 검색                   |
| BETWEEN a AND b       | A와 B 사이에 있는 범위 값을 모두 검색         |
| IN(a, b, c)           | A 이거나 B 이거나 C인 조건을 검색           |
| LIKE                  | 특정 패턴을 가지고 있는 조건을 검색            |
| Is Null / Is Not Null | Null 값을 검색 / Null이 아닌 값을 검색     |
| A AND B               | A 조건과 B 조건을 모두 만족하는 값만 검색       |
| A OR B                | A 조건이나 B 조건 중 한 가지라도 만족하는 값을 검색 |
| NOT A                 | A가 아닌 모든 조건을 검색                 |

```sql
SELECT * | 컬럼명 | 표현식  
FROM 테이블명 또는 뷰명  
WHERE 조회할 데이터 조건;
```

- **주의사항**
	- 문자나 날짜 상수 표현 시 반드시 **홑따옴표(’’)** 사용 (다른 절에서도 동일 적용)
	- **ORACLE**: 문자 상수의 경우 **대소문자 구분**
	- **MSSQL**: 기본적으로 문자 상수의 **대소문자를 구분하지 않음**
  
### LIKE 연산자
- 정확하게 일치하지 않아도 되는 **패턴 조건** 전달 시 사용
- %, _ 와 함께 사용됨
	- % : **자리수 제한 없음**, 모든 값을 의미
	- _ : **한 자리수**를 의미하며 특정 위치의 값을 표현

```sql
ENAME LIKE 'S%'   -- 이름이 S로 시작하는 경우
ENAME LIKE '%S%'  -- 이름에 S가 포함되는 경우
ENAME LIKE '%S'   -- 이름이 S로 끝나는 경우
ENAME LIKE '_S%'  -- 두 번째 글자가 S인 경우
ENAME LIKE '__S__' -- 이름의 가운데 글자가 S이고, 전체 길이가 5글자인 경우
```

### NOT 연산자
- 조건 결과의 반대 집합(여집합)을 출력
- NOT 뒤에 오는 연산 결과의 반대 집합을 출력
	-  **NOT IN, NOT BETWEEN A AND B, NOT LIKE, NOT NULL**

## GROUP BY 절
- 각 행을 특정 조건에 따라 그룹으로 분리하여 계산하도록 하는 구문식
- 그룹에 대한 조건은 WHERE절에서 사용할 수 없음
- GROUP BY 절을 사용하면 데이터가 요약되므로 요약되기 전 데이터와 함께 출력할 수 없음  

## HAVING 절
- 그룹 함수 결과를 조건으로 사용할 때 사용하는 절
- WHERE 절을 사용하여 그룹을 제한할 수 없으므로 HAVING 절에 전달
- GROUP BY절 뒤에 쓰는 것을 권장
- 내부적 연산 순서가 SELECT 절보다 먼저이므로 SELECT 절에서 선언된 Alias 사용 불가

## ORDER BY절
- 출력되는 행의 순서를 사용자가 변경하고자 할 때 사용
- 유일하게 SELECT절에서 정의한 컬럼 별칭 사용 가능
- SELECT 절에 선언된 순서대로의 숫자 전달 가능
	- 컬럼명과 숫자 혼합 사용가능
- 정렬순서
	- 한글: 가, 나, 다
	- 영어: A, B, C
	- 숫자: 1, 2, 3
	- 날짜: 과거 부터 시작해서 최근 날짜로 정렬
	- 문자는 왼쪽부터 값이 작은 순서대로 정렬
		- 값이 같다면 두번째 값이 작은 순서대로 정렬 

```sql
SELECT * | 컬럼명 | 표현식  
FROM 테이블명 또는 뷰명  
WHERE 조회할 데이터 조건  
GROUP BY 그룹핑컬럼명  
HAVING 그룹핑 대상 필터링 조건  
ORDER BY 정렬컬럼명 [ASC | DESC];
```

### 복합정렬
- 먼저 정렬한 값의 동일한 결과가 있을경우 추가적으로 정렬가능
	- 1차 정렬한 값이 같은 경우 그 값 안에서 2차 정렬 컬럽값의 정렬이 일어남
### NULL 정렬
- NULL을 포함한 값의 정렬 시 ORACLE은 기본적으로 NULL을 마지막에 배치
	- SQL은 처음에 배치
- ORACLE은 NULL 정렬 순서 변경 가능
	- ORDER BY절에 NULL LAST / NULL FIRST 명시

## JOIN
- 여러 테이블의 데이터를 사용해 동시 출력하거나 참조 할 경우 사용
- FROM 절에 조인할 테이블 나열
- 동일한 열 이름이 여러 테이블에 존재할 경우
	- 열 이름 앞에 테이블 이름이나 테이블 Alias 붙임

### 조인 종류
- 조건의 형태에 따라
	- **EQUI JOIN (등가 JOIN)**
		- JOIN 조건이 동등(=) 조건인 경우
		- 같은 값을 가지는 행을 연결하여 결과를 얻는 조인 방법
	- **NON EQUI JOIN**
		- JOIN 조건이 동등(=) 조건이 아닌 경우 (예: >, <, >=, <=)
- 조인 결과에 따라
	- *INNER JOIN*
		- JOIN 조건에 성립하는 데이터만 출력
	- *OUTER JOIN*
		- JOIN 조건에 성립하지 않는 데이터도 출력
		- 종류: LEFT OUTER JOIN, RIGHT OUTER JOIN, FULL OUTER JOIN
- 기타 JOIN 종류
	- *NATURAL JOIN*
		- 조인 조건 생략 시 두 테이블의 같은 이름을 가진 컬럼으로 자동 연결
	- *CROSS JOIN*
		- 조인 조건 없이 두 테이블의 가능한 모든 행 조합을 출력
	- **SELF JOIN**
		- 하나의 테이블을 두 번 이상 참조하여 연결하는 조인 (자기 자신과 조인)
		- 테이블명이 중복되므로 반드시 테이블 별칭 사용
		- 한 테이블을 참조할 때마다 명시해야 함

### 표준 조인
- ANSI 표준으로 작성되는 *INNER, CROSS, NATURAL, OUTER JOIN
	- *INNER JOIN*
		- 조인 조건이 일치하는 행만 추출 (ORACLE 조인 기본)
		- ANSI 표준의 경우 **USING** 이나 **ON 조건절**을 필수적으로 사용
			- **USING 조건절**
				- 조인할 컬럼명이 같을 경우 사용
				- Alias나 테이블 이름 같은 접두사 붙이기 불가
				- 괄호필수
			- **ON 조건절**
				- 조인할 양 컬럼의 컬럼명이 서로 다르더라도 사용가능
				- 컬럼명이 같을 경우 테이블 이름이나 별칭을 사용해 명확히 지정
				- ON 조건의 괄초는 옵션 (생략가능)
				- ON조건절에선 조인조건 명시
				- WHERE절에서는 일반조건 명시
	- *CROSS JOIN*
		- 테이블 간 조인 조건이 없는 경우 생성 가능한 모든 데이터들의 조합
		- 카타시안곱 출력
		- 양쪽 에티블 행의 수의 곱한 수의 데이터 조합 발생
	- *NATURAL JOIN*
		- 두 테이블 간의 동일한 이름을 가지는 모든 컬럼들에 대해 EQUI JOIN 수행
		- USING, ON, WHERE 절에서 조건 정의 불가
		- JOIN에 사용된 컬럼들은 데이터 유형이 동일해야 하며 접두사를 사용불가
	- *OUTER JOIN 개념*
		- INNER JOIN과 대비되는 조인 방식
		- JOIN 조건에서 동일한 값이 없는 행도 반환할 때 사용
		- 두 테이블 중 한쪽에 NULL 값이 포함된 경우
			- INNER JOIN에서는 출력되지 않음
			- 이를 포함하여 출력하려면 OUTER JOIN 사용
		- 기준 테이블의 방향에 따라
			- **LEFT OUTER**
				- 왼쪽 테이블이 기준이 되어 오른쪽 테이블 데이터를 채우는 방식
				- 우측 값에서 같은 값이 없는 경우 NULL 값으로 출력
				- LEFT OUTER JOIN 은 LEFT JOIN 으로 생략 가능
			- **RIGHT OUTER**
				- 오른쪽 테이블 기준으로 왼쪽 테이블 데이터를 채우는 방식
			- **FULL OUTER**
				- 두 테이블 전체 기준으로 결과를 생성
				- 중복 데이터는 삭제 후 리턴

# 2장. SQL 활용
## 서브쿼리

### 서브쿼리 개념
- **서브쿼리**란 하나의 SQL 문장에서 **다른 SQL 문장 안에 포함된 SELECT 문**을 의미
- 메인쿼리의 검색 조건을 충족하는 데이터를 추출하기 위해 사용됨
- `SELECT`, `INSERT`, `UPDATE`, `DELETE` 문장에서 활용 가능

### 서브쿼리 유형
- **스칼라 서브쿼리**: 하나의 결과값만 반환
- **단일행 서브쿼리**: 한 행(Row)만 반환 (`=, >, <, >=, <=, <>` 연산자 사용)
- **다중행 서브쿼리**: 여러 개의 행을 반환 (`IN, ANY, ALL` 연산자 사용)
- **다중열 서브쿼리**: 여러 개의 컬럼을 반환 (`(컬럼1, 컬럼2) IN (서브쿼리)`)
- **상관 서브쿼리 (Correlated Subquery)**: 메인쿼리의 각 행에 대해 서브쿼리가 반복 실행됨

### 서브쿼리 사용 위치
- **SELECT 절**: 계산된 값을 생성하기 위해 사용 (스칼라 서브쿼리)
- **FROM 절**: 임시 테이블처럼 활용
- **WHERE 절**: 특정 조건을 만족하는 데이터를 필터링
- **HAVING 절**: 그룹화된 결과에서 특정 조건을 만족하는 데이터만 필터링

### 서브쿼리 예제
- **WHERE 절에서 사용하는 서브쿼리**
  ```sql title:'직원들의 급여가 전체 평균 급여보다 높은 직원 조회'
  SELECT emp_name, salary
  FROM employees
  WHERE salary > (SELECT AVG(salary) FROM employees);
  ```

- **FROM 절에서 사용하는 서브쿼리**
  ```sql title:'부서별 평균 급여를 계산한 후, 부서 정보와 조인'
  SELECT dept_name, avg_salary
  FROM (SELECT dept_id, AVG(salary) AS avg_salary FROM employees GROUP BY dept_id) subquery
  JOIN departments d ON subquery.dept_id = d.dept_id;
  ```

- **SELECT 절에서 사용하는 서브쿼리**
  ```sql title:'각 직원의 급여와 전체 직원 중 최대 급여를 함께 출력'
  SELECT emp_name, salary, (SELECT MAX(salary) FROM employees) AS max_salary
  FROM employees;
  ```

- **상관 서브쿼리 (Correlated Subquery)**
  ```sql title:'같은 부서 내 평균 급여보다 높은 급여를 받는 직원 조회'
  SELECT emp_name, salary
  FROM employees e1
  WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e1.dept_id = e2.dept_id);
  ```

### 서브쿼리 vs 조인
- **서브쿼리**: **단일 값** 또는 **부분 집합**을 반환하여 필터링
- **조인**: 여러 테이블을 결합하여 데이터를 조회
- 데이터량이 많을 경우 **조인**이 성능 면에서 유리할 수 있음

### 서브쿼리 실행 순서
- **서브쿼리 실행**: 먼저 내부 쿼리(서브쿼리)가 실행됨
- **메인쿼리 실행**: 서브쿼리의 결과를 기반으로 메인쿼리가 실행됨

### 서브쿼리 최적화
- `EXISTS`를 활용하면 불필요한 데이터 처리를 줄일 수 있음
- 인덱스를 적절히 활용하여 서브쿼리의 실행 속도를 향상
- 서브쿼리를 조인으로 변경하여 성능 개선 가능

## 집합 연산자 (Set Operators)

### 집합 연산자 개념
- **집합 연산자**는 두 개 이상의 **SELECT 문 결과를 하나로 결합**하는 기능을 제공
- 기본적으로 **각 SELECT 문은 동일한 컬럼 개수 및 데이터 타입을 가져야 함**
- `ORDER BY`는 **전체 결과 집합**에 적용됨

### 집합 연산자의 종류
- **UNION**: 두 SELECT 결과의 **합집합** (중복 제거)
- **UNION ALL**: 두 SELECT 결과의 **합집합** (중복 포함)
- **INTERSECT**: 두 SELECT 결과의 **교집합**
- **MINUS (EXCEPT)**: 첫 번째 SELECT 결과에서 두 번째 SELECT 결과를 **차집합**으로 제거

### 집합 연산자의 특징
- **UNION / UNION ALL**: 두 개의 SELECT 문을 수직으로 결합
- **INTERSECT**: 공통된 데이터만 반환
- **MINUS / EXCEPT**: 첫 번째 결과에서 두 번째 결과를 제외하고 반환
- **모든 SELECT 문은 같은 컬럼 개수 및 데이터 타입을 유지해야 함**
- **NULL 값도 비교 대상으로 포함됨**

### 집합 연산자 예제

- **UNION (중복 제거)**
  ```sql title:'두 테이블에서 직원 이름을 가져오되, 중복된 이름은 제거'
  SELECT emp_name FROM employees_A
  UNION
  SELECT emp_name FROM employees_B;
  ```

- **UNION ALL (중복 포함)**
  ```sql  title:'두 테이블에서 직원 이름을 가져오되, 중복된 이름도 포함'
  SELECT emp_name FROM employees_A
  UNION ALL
  SELECT emp_name FROM employees_B;
  ```

- **INTERSECT (교집합)**
  ```sql title:'두 테이블에서 **공통적으로 존재하는 직원 이름**만 반환'
  SELECT emp_name FROM employees_A
  INTERSECT
  SELECT emp_name FROM employees_B;
  ```

- **MINUS (차집합)**
  ```sql title:'첫 번째 테이블(A)에만 존재하고 두 번째 테이블(B)에는 없는 직원 이름 반환'
  SELECT emp_name FROM employees_A
  MINUS
  SELECT emp_name FROM employees_B;
  ```


### 집합 연산자 사용 시 유의점
- 각 SELECT 문은 동일한 컬럼 개수 및 데이터 타입을 가져야 함
- ORDER BY 절은 마지막 SELECT 문에만 적용 가능
- NULL 값도 비교에 포함됨
- UNION ALL을 사용할 경우, 중복된 데이터까지 포함하여 성능이 향상될 수 있음

### 집합 연산자 실행 순서
- 각 SELECT 문이 개별적으로 실행됨
- 집합 연산자가 적용되어 결과 집합을 병합
- ORDER BY 절이 있으면 최종 결과에서 정렬 수행

### 집합 연산자 vs JOIN
- **JOIN**: 두 개 이상의 테이블을 **가로로 병합**
- **집합 연산자**: 두 개 이상의 결과를 **세로로 병합**
- 조인을 사용할 수 없는 경우 집합 연산자를 활용 가능

## 그룹 함수 (Group Functions)

### 그룹 함수 개념
- **그룹 함수**는 여러 행(Row)의 값을 하나의 결과값으로 집계하는 함수
- `GROUP BY` 절과 함께 사용하여 특정 그룹별로 집계 가능
- `NULL` 값은 대부분의 그룹 함수에서 자동 제외됨

### 그룹 함수의 종류
- **COUNT**: 행(Row) 개수를 반환
- **SUM**: 숫자 데이터의 합계 반환
- **AVG**: 숫자 데이터의 평균 반환
- **MAX**: 최댓값 반환
- **MIN**: 최솟값 반환
- **STDDEV**: 표준 편차 반환
- **VARIANCE**: 분산 반환

### 그룹 함수 사용 방법

- **COUNT 함수**
  ```sql
  SELECT COUNT(*) FROM employees;
  ```
  - 테이블의 전체 행 개수 반환 (NULL 포함)

  ```sql
  SELECT COUNT(salary) FROM employees;
  ```
  - `NULL` 값을 제외한 급여 데이터 개수 반환

- **SUM 함수**
  ```sql
  SELECT SUM(salary) FROM employees;
  ```
  - 전체 급여 총합 계산

- **AVG 함수**
  ```sql
  SELECT AVG(salary) FROM employees;
  ```
  - 전체 급여 평균 계산 (NULL 값 제외)

- **MAX / MIN 함수**
  ```sql
  SELECT MAX(salary), MIN(salary) FROM employees;
  ```
  - 최댓값과 최솟값을 함께 조회

- **STDDEV / VARIANCE 함수**
  ```sql
  SELECT STDDEV(salary), VARIANCE(salary) FROM employees;
  ```
  - 급여의 표준 편차 및 분산 반환

### GROUP BY 절과 그룹 함수
- `GROUP BY` 절을 사용하여 특정 그룹별 집계 가능
  ```sql
  SELECT dept_id, AVG(salary)
  FROM employees
  GROUP BY dept_id;
  ```
  - 부서별 평균 급여 계산

### HAVING 절과 그룹 함수
- `HAVING` 절을 사용하여 그룹 함수의 결과에 대한 조건 설정
  ```sql
  SELECT dept_id, AVG(salary)
  FROM employees
  GROUP BY dept_id
  HAVING AVG(salary) > 5000;
  ```
  - 평균 급여가 5000 초과인 부서만 조회

### 그룹 함수 사용 시 유의점
- **NULL 값은 대부분 자동 제외됨 (COUNT(*) 제외)**
- **GROUP BY 절 없이 사용하면 전체 데이터 기준으로 집계**
- **GROUP BY 절을 사용할 경우 SELECT 절에는 그룹 함수 또는 그룹핑 컬럼만 포함 가능**
- **HAVING 절을 활용하여 그룹 함수의 결과 필터링 가능**

## 윈도우 함수 (Window Functions)

### 윈도우 함수 개념
- **윈도우 함수**는 결과 집합의 **각 행에 대해 특정 범위(윈도우)** 내에서 연산을 수행하는 함수
- 그룹 함수와 달리 **모든 행을 유지하면서 계산 가능**
- `OVER()` 절과 함께 사용하며, **PARTITION BY** 또는 **ORDER BY**와 조합하여 동작

### 윈도우 함수 유형
- **순위 함수**: 각 행의 순위를 반환
  - `RANK()`
  - `DENSE_RANK()`
  - `ROW_NUMBER()`
- **집계 윈도우 함수**: 그룹 함수와 유사하지만 행을 유지
  - `SUM()`
  - `AVG()`
  - `MAX()`
  - `MIN()`
  - `COUNT()`
- **이동(Window) 함수**: 특정 행 기준으로 앞뒤 데이터를 참조하여 계산
  - `LAG()`
  - `LEAD()`
  - `FIRST_VALUE()`
  - `LAST_VALUE()`

### 윈도우 함수 사용법

- **RANK 함수** (동점 시 순위 건너뜀)
  ```sql
  SELECT emp_name, salary, RANK() OVER (ORDER BY salary DESC) AS rank
  FROM employees;
  ```
  - 급여 기준 내림차순 정렬 후 순위 부여

- **DENSE_RANK 함수** (동점 시 순위 연속)
  ```sql
  SELECT emp_name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
  FROM employees;
  ```
  - 급여 기준 내림차순 정렬 후 연속 순위 부여

- **ROW_NUMBER 함수** (순서대로 고유한 번호 부여)
  ```sql
  SELECT emp_name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
  FROM employees;
  ```
  - 급여 기준 내림차순 정렬 후 각 행에 고유 번호 부여

- **SUM 윈도우 함수** (누적 합계 계산)
  ```sql
  SELECT emp_name, salary, SUM(salary) OVER (ORDER BY salary DESC) AS running_total
  FROM employees;
  ```
  - 급여 기준 내림차순 정렬 후 누적 합계 계산

- **LAG 함수** (이전 행 값 참조)
  ```sql
  SELECT emp_name, salary, LAG(salary, 1, 0) OVER (ORDER BY salary DESC) AS prev_salary
  FROM employees;
  ```
  - 현재 행의 이전 행 급여값 조회 (이전 값 없으면 0 반환)

- **LEAD 함수** (다음 행 값 참조)
  ```sql
  SELECT emp_name, salary, LEAD(salary, 1, 0) OVER (ORDER BY salary DESC) AS next_salary
  FROM employees;
  ```
  - 현재 행의 다음 행 급여값 조회 (다음 값 없으면 0 반환)

- **FIRST_VALUE / LAST_VALUE 함수** (윈도우 내 첫 번째/마지막 값 반환)
  ```sql
  SELECT emp_name, salary, 
         FIRST_VALUE(salary) OVER (PARTITION BY dept_id ORDER BY salary DESC) AS top_salary
  FROM employees;
  ```
  - 부서별 최고 급여 조회

### 윈도우 함수의 특징
- `OVER()` 절을 사용하여 개별 행 기준 연산 수행
- `PARTITION BY`를 사용하면 특정 그룹별 연산 가능
- `ORDER BY`를 활용하여 순서 기반 계산 가능
- 모든 행을 유지하면서 연산을 수행하는 점이 일반 그룹 함수와 차이점

### 윈도우 함수 vs 그룹 함수
- **그룹 함수**: `GROUP BY`를 사용하여 **그룹별 하나의 결과**만 반환
- **윈도우 함수**: 개별 행을 유지하면서 **추가적인 분석 값 반환** 가능

## Top N 쿼리 (Top N Query)

### Top N 쿼리 개념
- **Top N 쿼리**는 특정 기준으로 정렬된 데이터에서 **상위 또는 하위 N개의 행을 조회**하는 방식
- `ORDER BY`와 함께 사용하여 정렬된 결과에서 원하는 개수만 출력
- **RDBMS마다 구현 방식이 다름**

### Top N 쿼리 사용 방법

- **ROWNUM을 활용한 Top N 쿼리 (Oracle)**
  ```sql
  SELECT emp_name, salary
  FROM employees
  WHERE ROWNUM <= 5
  ORDER BY salary DESC;
  ```
  - 급여 기준 상위 5명의 직원 조회
  - `ROWNUM`은 실행 순서에 영향을 받기 때문에 **인라인 뷰**를 활용하는 것이 일반적

  ```sql
  SELECT emp_name, salary
  FROM (
      SELECT emp_name, salary FROM employees ORDER BY salary DESC
  )
  WHERE ROWNUM <= 5;
  ```
  - 정렬된 후 `ROWNUM`을 적용하여 정확한 결과 도출

- **TOP을 활용한 Top N 쿼리 (SQL Server)**
  ```sql
  SELECT TOP 5 emp_name, salary
  FROM employees
  ORDER BY salary DESC;
  ```
  - `TOP N`을 사용하여 급여 기준 상위 5명 조회

- **LIMIT을 활용한 Top N 쿼리 (MySQL, PostgreSQL)**
  ```sql
  SELECT emp_name, salary
  FROM employees
  ORDER BY salary DESC
  LIMIT 5;
  ```
  - `LIMIT`을 사용하여 급여 기준 상위 5명 조회

- **FETCH FIRST N ROWS ONLY (Oracle 12c 이상, PostgreSQL)**
  ```sql
  SELECT emp_name, salary
  FROM employees
  ORDER BY salary DESC
  FETCH FIRST 5 ROWS ONLY;
  ```
  - 최신 Oracle 버전에서 `FETCH FIRST`를 사용하여 간결한 Top N 쿼리 작성 가능

### OFFSET을 활용한 페이징 처리
- **MySQL, PostgreSQL**
  ```sql
  SELECT emp_name, salary
  FROM employees
  ORDER BY salary DESC
  LIMIT 5 OFFSET 10;
  ```
  - 11번째 행부터 상위 5개의 행 조회 (페이징 처리)

- **Oracle 12c 이상**
  ```sql
  SELECT emp_name, salary
  FROM employees
  ORDER BY salary DESC
  OFFSET 10 ROWS FETCH NEXT 5 ROWS ONLY;
  ```
  - 11번째 행부터 5개의 행을 조회

### Top N 쿼리 사용 시 유의점
- `ORDER BY` 절이 반드시 포함되어야 함 (정렬 기준 필요)
- `OFFSET`을 사용하면 성능 저하 가능성이 있음 (특히 큰 테이블에서 후반부 데이터 조회 시)
- `ROWNUM`을 직접 사용할 경우 올바른 정렬이 보장되지 않을 수 있으므로 **인라인 뷰 활용 권장**
- 최신 DBMS에서는 `FETCH FIRST N ROWS ONLY`를 활용하는 것이 가장 효율적

### Top N 쿼리 vs 윈도우 함수
- **Top N 쿼리**: 단순히 **상위 N개** 또는 **하위 N개** 데이터를 가져오는 데 사용
- **윈도우 함수 (RANK, DENSE_RANK, ROW_NUMBER)**: 데이터 내에서 **순위를 부여**하여 다양한 방식으로 활용 가능


## 계층형 질의와 셀프 조인 (Hierarchical Query & Self Join)

### 계층형 질의 개념
- **계층형 질의**는 트리 구조와 같은 계층적인 데이터를 조회할 때 사용
- 대표적인 예: 조직도, 카테고리, 제품군 등 **부모-자식 관계**를 가지는 데이터
- `CONNECT BY` (Oracle) 또는 **재귀 CTE (Common Table Expression)**을 활용하여 구현

### 계층형 질의 (Oracle)
- **CONNECT BY**를 사용하여 부모-자식 관계 조회
  ```sql
  SELECT emp_id, emp_name, manager_id
  FROM employees
  START WITH manager_id IS NULL
  CONNECT BY PRIOR emp_id = manager_id;
  ```
  - `START WITH`: 계층 구조의 최상위 레벨 지정 (ex. 최고 관리자)
  - `CONNECT BY PRIOR`: 부모-자식 관계 정의

- **LEVEL을 활용한 계층 깊이 확인**
  ```sql
  SELECT LEVEL, emp_id, emp_name, manager_id
  FROM employees
  START WITH manager_id IS NULL
  CONNECT BY PRIOR emp_id = manager_id;
  ```
  - `LEVEL`을 사용하면 계층의 깊이를 확인 가능

### 계층형 질의 (재귀 CTE - SQL Server, PostgreSQL)
- **WITH RECURSIVE**를 활용하여 계층 구조 표현
  ```sql
  WITH RECURSIVE EmployeeHierarchy AS (
      SELECT emp_id, emp_name, manager_id, 1 AS hierarchy_level
      FROM employees
      WHERE manager_id IS NULL
      UNION ALL
      SELECT e.emp_id, e.emp_name, e.manager_id, eh.hierarchy_level + 1
      FROM employees e
      JOIN EmployeeHierarchy eh ON e.manager_id = eh.emp_id
  )
  SELECT * FROM EmployeeHierarchy;
  ```
  - `UNION ALL`을 사용하여 **재귀적으로 하위 계층 탐색**
  - `hierarchy_level`을 증가시켜 계층 깊이 표시

### 계층형 질의의 주요 키워드
- **START WITH**: 계층 구조의 시작점 지정 (Oracle)
- **CONNECT BY PRIOR**: 부모-자식 관계 정의 (Oracle)
- **LEVEL**: 계층의 깊이 (Oracle)
- **WITH RECURSIVE**: 재귀 CTE를 사용하여 계층형 데이터 조회 (PostgreSQL, SQL Server)

---

### 셀프 조인 개념
- **셀프 조인(Self Join)**은 같은 테이블을 두 번 이상 조인하여 관계를 표현하는 방식
- 주로 **계층 구조 데이터** 또는 **두 개의 동일한 개체를 비교하는 경우** 사용
- `INNER JOIN`, `LEFT JOIN`을 활용하여 구현

### 셀프 조인 예제
- **직원의 상사를 조회하는 셀프 조인**
  ```sql
  SELECT e1.emp_name AS Employee, e2.emp_name AS Manager
  FROM employees e1
  LEFT JOIN employees e2 ON e1.manager_id = e2.emp_id;
  ```
  - `e1`: 직원 (Employee)
  - `e2`: 상사 (Manager)
  - `LEFT JOIN`: 직원이 매니저가 없는 경우도 포함

- **같은 테이블에서 특정 값 비교**
  ```sql
  SELECT e1.emp_name, e2.emp_name AS coworker
  FROM employees e1
  JOIN employees e2 ON e1.dept_id = e2.dept_id AND e1.emp_id <> e2.emp_id;
  ```
  - 같은 부서에 속한 다른 직원 조회

### 셀프 조인의 특징
- 같은 테이블을 조인하기 때문에 **테이블에 별칭(Alias) 지정 필수**
- **자기 자신과의 관계를 표현**하는 데 유용
- 계층형 데이터 조회뿐만 아니라 **데이터 비교**에도 활용 가능

### 계층형 질의 vs 셀프 조인
- **계층형 질의**: **부모-자식 관계**를 트리 형태로 조회
- **셀프 조인**: 같은 테이블을 **서로 다른 개체처럼 조인**하여 관계 표현
- 계층 구조가 필요하면 `CONNECT BY`, `WITH RECURSIVE`를 사용하고, **단순 관계 표현은 셀프 조인**을 활용


## PIVOT 절과 UNPIVOT 절 (PIVOT & UNPIVOT)

### PIVOT 개념
- **PIVOT 절**은 **행 데이터를 열로 변환**하여 가독성을 높이고 분석을 용이하게 하는 기능
- 주로 **집계 함수와 함께 사용**되어 데이터를 그룹화하여 표시
- RDBMS마다 사용법이 다르며, `CASE WHEN` 또는 `GROUP BY`로 유사한 기능을 구현 가능

### PIVOT 사용법 (SQL Server)
```sql
SELECT * 
FROM (SELECT dept_id, emp_name, salary FROM employees) AS SourceTable
PIVOT (
    SUM(salary) 
    FOR dept_id IN ([10], [20], [30])
) AS PivotTable;
```
- `SUM(salary)`: 피벗할 데이터의 집계 함수
- `FOR dept_id IN (...)`: 행 데이터를 열로 변환할 기준 컬럼 지정

### PIVOT을 활용한 수동 구현 (Oracle, MySQL)
```sql
SELECT dept_id,
       SUM(CASE WHEN year = 2021 THEN sales END) AS sales_2021,
       SUM(CASE WHEN year = 2022 THEN sales END) AS sales_2022,
       SUM(CASE WHEN year = 2023 THEN sales END) AS sales_2023
FROM sales_data
GROUP BY dept_id;
```
- `CASE WHEN`을 활용하여 **연도별 매출을 열로 변환**
- `GROUP BY`를 사용하여 부서별 그룹화

---

### UNPIVOT 개념
- **UNPIVOT 절**은 **열 데이터를 행으로 변환**하는 기능
- 테이블에서 여러 개의 열을 하나의 열로 축소하여 표현
- 주로 **정규화된 형태로 데이터를 변환**할 때 사용

### UNPIVOT 사용법 (SQL Server)
```sql
SELECT * 
FROM (SELECT emp_id, Q1, Q2, Q3, Q4 FROM sales) AS SourceTable
UNPIVOT (
    sales_amount FOR quarter IN (Q1, Q2, Q3, Q4)
) AS UnpivotTable;
```
- `FOR quarter IN (Q1, Q2, Q3, Q4)`: 열(Q1~Q4)을 행으로 변환

### UNPIVOT을 활용한 수동 구현 (Oracle, MySQL)
```sql
SELECT emp_id, 'Q1' AS quarter, Q1 AS sales_amount FROM sales
UNION ALL
SELECT emp_id, 'Q2', Q2 FROM sales
UNION ALL
SELECT emp_id, 'Q3', Q3 FROM sales
UNION ALL
SELECT emp_id, 'Q4', Q4 FROM sales;
```
- `UNION ALL`을 활용하여 **수동으로 열을 행으로 변환**
- 각 열에 대해 개별적인 `SELECT` 문을 작성하여 하나의 결과로 합침

---

### PIVOT vs UNPIVOT 비교
| 기능 | PIVOT | UNPIVOT |
|------|-------|---------|
| 변환 방향 | 행 → 열 | 열 → 행 |
| 주요 사용 목적 | 데이터를 가독성 있게 집계 | 정규화된 형태로 변환 |
| 주로 활용하는 함수 | 집계 함수 (SUM, AVG 등) | UNION ALL 또는 직접 변환 |

### PIVOT과 UNPIVOT 사용 시 유의점
- PIVOT은 미리 변환할 열을 지정해야 하므로 동적으로 처리하려면 **동적 SQL**이 필요할 수 있음
- UNPIVOT을 사용할 경우 **NULL 값이 포함된 행도 출력**될 수 있음
- 성능이 중요한 경우 **GROUP BY 또는 UNION ALL을 활용한 변환 방법 고려**


## 정규 표현식 (Regular Expressions)

### 정규 표현식 개념
- **정규 표현식(Regex, Regular Expression)**은 특정한 패턴을 가진 문자열을 검색, 추출, 변환하는 데 사용
- SQL에서도 특정 DBMS에서 **정규 표현식을 지원**하여 문자열 필터링, 패턴 매칭 등에 활용 가능

### 정규 표현식 지원 여부
- **Oracle**: `REGEXP_LIKE`, `REGEXP_INSTR`, `REGEXP_SUBSTR`, `REGEXP_REPLACE`
- **MySQL**: `REGEXP`, `RLIKE`
- **PostgreSQL**: `~`, `~*`, `!~`, `!~*`
- **SQL Server**: 기본적으로 지원하지 않으며, `LIKE` 또는 CLR 함수를 사용하여 구현

### 정규 표현식 연산자 및 기호
| 기호 | 의미 |
|------|------|
| `.` | 임의의 한 문자 |
| `^` | 문자열의 시작 |
| `$` | 문자열의 끝 |
| `*` | 0개 이상 반복 |
| `+` | 1개 이상 반복 |
| `?` | 0개 또는 1개 존재 |
| `{n}` | 정확히 n번 반복 |
| `{n,}` | 최소 n번 이상 반복 |
| `{n,m}` | 최소 n번, 최대 m번 반복 |
| `[]` | 문자 집합 (예: `[abc]` → a, b, c 중 하나) |
| `[^]` | 부정 문자 집합 (예: `[^abc]` → a, b, c 제외) |
| `\d` | 숫자 (0-9) |
| `\D` | 숫자가 아닌 문자 |
| `\w` | 단어 문자 (영문자, 숫자, `_`) |
| `\W` | 단어 문자가 아닌 것 |
| `\s` | 공백 문자 |
| `\S` | 공백이 아닌 문자 |

---

### 정규 표현식 함수 (Oracle)

- **REGEXP_LIKE** (정규 표현식을 활용한 문자열 패턴 검색)
  ```sql
  SELECT emp_name FROM employees WHERE REGEXP_LIKE(emp_name, '^J.*');
  ```
  - `'J'`로 시작하는 모든 직원 이름 조회

- **REGEXP_INSTR** (정규 표현식을 활용한 특정 패턴의 위치 반환)
  ```sql
  SELECT REGEXP_INSTR('abc123xyz', '[0-9]+') FROM dual;
  ```
  - 첫 번째 숫자가 등장하는 위치 반환

- **REGEXP_SUBSTR** (정규 표현식을 활용한 부분 문자열 추출)
  ```sql
  SELECT REGEXP_SUBSTR('abc123xyz', '[0-9]+') FROM dual;
  ```
  - 첫 번째 숫자 그룹 (`123`) 반환

- **REGEXP_REPLACE** (정규 표현식을 활용한 문자열 치환)
  ```sql
  SELECT REGEXP_REPLACE('abc123xyz', '[0-9]+', '###') FROM dual;
  ```
  - 숫자를 `###`로 변경 (`abc###xyz` 반환)

---

### 정규 표현식 함수 (MySQL)
- **REGEXP 또는 RLIKE** 사용하여 특정 패턴을 포함하는 데이터 검색
  ```sql
  SELECT emp_name FROM employees WHERE emp_name REGEXP '^J';
  ```
  - `'J'`로 시작하는 모든 직원 조회

---

### 정규 표현식 함수 (PostgreSQL)
- **정규 표현식 연산자 (`~`, `!~`)** 사용
  ```sql
  SELECT emp_name FROM employees WHERE emp_name ~ '^J';
  ```
  - `'J'`로 시작하는 직원 조회 (`~*` 사용 시 대소문자 구분 없음)

---

### 정규 표현식과 LIKE 비교
| 비교 항목 | 정규 표현식 | LIKE 연산자 |
|-----------|------------|-------------|
| 패턴 매칭 | 복잡한 패턴 검색 가능 | 와일드카드 (`%`, `_`)만 지원 |
| 성능 | 문자열이 길고 패턴이 복잡할 경우 성능 저하 가능 | 상대적으로 단순한 연산 |
| 지원 여부 | 일부 DBMS만 지원 | 모든 DBMS에서 사용 가능 |

---

### 정규 표현식 사용 시 유의점
- 복잡한 패턴을 사용할 경우 성능 저하 가능 (특히 대량 데이터 처리 시)
- DBMS마다 정규 표현식 지원 여부 및 문법 차이가 있음
- `LIKE` 연산자로도 간단한 패턴 검색이 가능하므로 필요에 따라 선택적으로 사용


# 3장. 관리구문
## DML

### DML 개념
- **DML (데이터 조작어)**은 **데이터를 추가, 수정, 삭제, 조회**하는 SQL 명령어
- 데이터베이스의 데이터를 변경하지만 **테이블 구조는 변경하지 않음**
- 트랜잭션과 연계하여 `COMMIT`, `ROLLBACK`으로 변경 사항을 확정 또는 취소 가능

### DML 종류
- **INSERT**: 새로운 데이터 추가
- **UPDATE**: 기존 데이터 수정
- **DELETE**: 기존 데이터 삭제
- **SELECT**: 데이터 조회 (DML에 포함되기도 함)

---

### INSERT (데이터 삽입)
- **전체 컬럼 삽입**
  ```sql
  INSERT INTO employees VALUES (101, 'John Doe', 'Sales', 5000);
  ```
  - 테이블의 모든 컬럼에 값을 입력
  - 컬럼 순서를 반드시 테이블 정의와 동일하게 맞춰야 함

- **특정 컬럼 삽입**
  ```sql
  INSERT INTO employees (emp_id, emp_name, salary) 
  VALUES (102, 'Jane Doe', 6000);
  ```
  - 지정된 컬럼에만 데이터 삽입 (누락된 컬럼은 `NULL` 값이 들어감)

- **다중 행 삽입 (MySQL, PostgreSQL)**
  ```sql
  INSERT INTO employees (emp_id, emp_name, salary) 
  VALUES 
      (103, 'Alice', 7000),
      (104, 'Bob', 5500);
  ```
  - 여러 개의 데이터를 한 번에 삽입 가능

- **서브쿼리를 이용한 INSERT**
  ```sql
  INSERT INTO employees_backup (emp_id, emp_name, salary)
  SELECT emp_id, emp_name, salary FROM employees WHERE dept_id = 10;
  ```
  - 기존 테이블 데이터를 **서브쿼리**를 활용하여 새로운 테이블에 삽입

---

### UPDATE (데이터 수정)
- **특정 데이터 수정**
  ```sql
  UPDATE employees 
  SET salary = salary * 1.1 
  WHERE dept_id = 10;
  ```
  - 부서 ID가 `10`인 직원들의 급여를 10% 인상

- **여러 컬럼 동시에 수정**
  ```sql
  UPDATE employees 
  SET salary = salary + 500, dept_id = 20 
  WHERE emp_id = 101;
  ```
  - 특정 직원의 급여를 500 증가시키고 부서를 변경

- **모든 데이터 수정**
  ```sql
  UPDATE employees SET salary = salary * 1.05;
  ```
  - 모든 직원의 급여를 5% 증가

---

### DELETE (데이터 삭제)
- **특정 행 삭제**
  ```sql
  DELETE FROM employees WHERE emp_id = 101;
  ```
  - 특정 직원의 데이터를 삭제

- **전체 데이터 삭제**
  ```sql
  DELETE FROM employees;
  ```
  - 테이블의 모든 데이터를 삭제 (`WHERE` 절이 없으면 전체 삭제됨)

- **특정 조건의 여러 행 삭제**
  ```sql
  DELETE FROM employees WHERE dept_id = 10;
  ```
  - 부서 ID가 `10`인 모든 직원 삭제

- **DELETE vs TRUNCATE**

| 비교 항목          | DELETE                      | TRUNCATE                      |
|------------------|--------------------------|------------------------------|
| 트랜잭션 가능 여부 | 가능 (`ROLLBACK` 가능)    | 불가능 (`COMMIT` 즉시 적용)   |
| 속도             | 상대적으로 느림            | 상대적으로 빠름               |
| 데이터 삭제 방식 | 행 단위 삭제              | 테이블 전체 삭제              |
| 자동 증가 값 초기화 | 유지                       | 초기화                         |


---

### SELECT (데이터 조회)
- **전체 데이터 조회**
  ```sql
  SELECT * FROM employees;
  ```
  - 모든 행과 컬럼을 조회

- **특정 컬럼 조회**
  ```sql
  SELECT emp_name, salary FROM employees;
  ```
  - `emp_name`과 `salary` 컬럼만 조회

- **조건 조회 (WHERE)**
  ```sql
  SELECT emp_name, salary FROM employees WHERE salary %3E 5000;
  ```
  - 급여가 5000 초과인 직원만 조회

- **정렬 조회 (ORDER BY)**
  ```sql
  SELECT emp_name, salary FROM employees ORDER BY salary DESC;
  ```
  - 급여가 높은 순으로 정렬하여 조회

---

### DML과 트랜잭션
- DML 문장은 **트랜잭션과 연계**하여 데이터 변경을 관리할 수 있음
- **COMMIT**: 변경 사항을 확정
  ```sql
  COMMIT;
  ```
- **ROLLBACK**: 변경 사항을 취소
  ```sql
  ROLLBACK;
  ```
- **SAVEPOINT**: 특정 지점까지 ROLLBACK 가능
  ```sql
  SAVEPOINT sp1;
  UPDATE employees SET salary = salary + 1000 WHERE dept_id = 10;
  ROLLBACK TO sp1;
  ```

---

### DML 사용 시 유의점
- `WHERE` 절을 생략하면 모든 행이 영향을 받으므로 주의 필요
- `ROLLBACK`이 불가능한 `TRUNCATE`와의 차이점을 이해해야 함
- 대량 데이터 업데이트 시 성능을 고려하여 **BATCH UPDATE** 또는 **트랜잭션 활용** 권장>)


## TCL (Transaction Control Language)

### TCL 개념
- **TCL (트랜잭션 제어 언어)**는 **데이터 변경 작업을 제어**하는 SQL 명령어
- DML(`INSERT`, `UPDATE`, `DELETE`)과 함께 사용되며, **변경 사항을 저장 또는 취소**하는 역할
- **트랜잭션(Transaction)**: 하나의 논리적인 작업 단위로, **ALL or NOTHING** 원칙 적용

### TCL 명령어 종류
- **COMMIT**: 트랜잭션의 변경 사항을 **확정**
- **ROLLBACK**: 트랜잭션의 변경 사항을 **취소**
- **SAVEPOINT**: 특정 시점까지 **부분 취소 가능하도록 저장점 설정**
- **SET TRANSACTION**: 트랜잭션의 격리 수준 설정 (DBMS에 따라 다름)

---

### COMMIT (변경 사항 저장)
- **모든 변경 사항을 영구적으로 반영**
- COMMIT이 실행되면 변경된 데이터는 **되돌릴 수 없음**
- 모든 사용자가 변경된 데이터를 조회 가능

```sql
UPDATE employees SET salary = salary * 1.1 WHERE dept_id = 10;
COMMIT;
```
- 부서 ID가 `10`인 직원들의 급여를 10% 증가시키고 변경 사항 저장

---

### ROLLBACK (변경 사항 취소)
- **이전 COMMIT이 실행되기 전의 상태로 복구**
- `DELETE`, `UPDATE`, `INSERT` 등의 DML 실행 후 COMMIT 이전에 실행해야 함

```sql
UPDATE employees SET salary = salary * 1.1 WHERE dept_id = 10;
ROLLBACK;
```
- 부서 ID가 `10`인 직원들의 급여 인상을 취소

---

### SAVEPOINT (저장점 설정)
- **트랜잭션 내에서 특정 지점(SAVEPOINT)을 설정하여 부분적으로 ROLLBACK 가능**
- 긴 트랜잭션에서 **일부 변경 사항만 취소 가능하도록 설정**

```sql
SAVEPOINT sp1;
UPDATE employees SET salary = salary + 500 WHERE dept_id = 10;

SAVEPOINT sp2;
UPDATE employees SET salary = salary + 1000 WHERE dept_id = 20;

ROLLBACK TO sp1; -- sp1 이후 변경 사항만 취소
COMMIT;
```
- `sp1` 저장점 생성 후, 부서 `10`의 급여를 500 증가
- `sp2` 저장점 생성 후, 부서 `20`의 급여를 1000 증가
- `ROLLBACK TO sp1`을 실행하면 `sp1` 이후 변경된 사항만 취소됨
- 이후 `COMMIT` 실행하여 `sp1`까지의 변경 사항을 저장

---

### SET TRANSACTION (트랜잭션 속성 설정)
- **트랜잭션의 격리 수준(Isolation Level) 설정**
- **격리 수준**: 여러 트랜잭션이 동시에 실행될 때 **데이터의 정합성을 보장하는 정도**

#### 격리 수준 종류 (ANSI SQL 기준)
| 격리 수준 | 설명 | 현상 |
|-----------|------|------|
| READ UNCOMMITTED | 커밋되지 않은 데이터 읽기 가능 | **Dirty Read** 발생 가능 |
| READ COMMITTED | 커밋된 데이터만 읽기 가능 | **Non-repeatable Read** 발생 가능 |
| REPEATABLE READ | 동일 트랜잭션 내에서 동일 쿼리 실행 시 항상 같은 결과 반환 | **Phantom Read** 발생 가능 |
| SERIALIZABLE | 트랜잭션을 순차적으로 실행하여 동시성 문제 방지 | 성능 저하 가능 |

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```
- 현재 트랜잭션의 격리 수준을 `SERIALIZABLE`로 설정

---

### TCL 사용 시 유의점
- **DML 실행 후 COMMIT하지 않으면 다른 사용자는 변경 사항을 볼 수 없음**
- **ROLLBACK 이후에는 변경 사항을 복구할 수 없음**
- **TRUNCATE는 COMMIT 또는 ROLLBACK의 영향을 받지 않음** (즉시 반영됨)
- **자동 COMMIT 설정 여부 확인** (`AUTO COMMIT`이 활성화된 경우, COMMIT 없이도 변경 사항이 즉시 반영될 수 있음)

```sql
-- 자동 COMMIT 비활성화 (Oracle, MySQL)
SET AUTOCOMMIT = 0;
```

---

### TCL과 DML의 관계
| 구분 | DML (Data Manipulation Language) | TCL (Transaction Control Language) |
|------|----------------------------------|----------------------------------|
| 역할 | 데이터 추가, 수정, 삭제 | 트랜잭션을 제어 (저장, 취소) |
| 명령어 | `INSERT`, `UPDATE`, `DELETE`, `SELECT` | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |
| 실행 단위 | 개별 SQL 문 | 트랜잭션 단위 |




## DDL (Data Definition Language)

### DDL 개념
- **DDL (데이터 정의어)**는 데이터베이스의 **구조(스키마)를 정의, 변경, 삭제**하는 명령어
- 테이블, 뷰, 인덱스, 트리거 등의 객체를 생성하거나 수정할 때 사용
- DML(`INSERT`, `UPDATE`, `DELETE`)과 다르게 **트랜잭션 제어(COMMIT, ROLLBACK)의 영향을 받지 않음**  
  → 즉, 실행 즉시 변경 사항이 반영됨

---

### DDL 종류
- **CREATE**: 테이블, 인덱스, 뷰 등의 데이터베이스 객체 생성
- **ALTER**: 기존 객체의 구조 변경
- **DROP**: 객체 삭제
- **TRUNCATE**: 테이블의 모든 데이터 삭제 (ROLLBACK 불가)
- **RENAME**: 객체의 이름 변경
- **COMMENT**: 객체에 설명 추가

---

### CREATE (데이터베이스 객체 생성)
- **테이블 생성**
  ```sql
  CREATE TABLE employees (
      emp_id INT PRIMARY KEY,
      emp_name VARCHAR(50) NOT NULL,
      dept_id INT,
      salary DECIMAL(10,2),
      hire_date DATE DEFAULT SYSDATE
  );
  ```
  - `PRIMARY KEY`: 기본 키 설정
  - `NOT NULL`: NULL 허용하지 않음
  - `DEFAULT`: 기본값 설정

- **인덱스 생성**
  ```sql
  CREATE INDEX idx_emp_salary ON employees (salary);
  ```
  - `salary` 컬럼에 대한 인덱스 생성

- **뷰 생성**
  ```sql
  CREATE VIEW emp_view AS 
  SELECT emp_id, emp_name, salary FROM employees WHERE salary > 5000;
  ```
  - 급여가 5000 초과인 직원만 조회하는 뷰 생성

---

### ALTER (데이터베이스 객체 변경)
- **컬럼 추가**
  ```sql
  ALTER TABLE employees ADD phone_number VARCHAR(20);
  ```
  - `phone_number` 컬럼 추가

- **컬럼 수정**
  ```sql
  ALTER TABLE employees MODIFY salary DECIMAL(12,2);
  ```
  - `salary` 컬럼의 데이터 타입 변경

- **컬럼 삭제**
  ```sql
  ALTER TABLE employees DROP COLUMN phone_number;
  ```
  - `phone_number` 컬럼 삭제

- **제약 조건 추가**
  ```sql
  ALTER TABLE employees ADD CONSTRAINT chk_salary CHECK (salary > 0);
  ```
  - `salary` 값이 0보다 커야 하는 조건 추가

---

### DROP (데이터베이스 객체 삭제)
- **테이블 삭제**
  ```sql
  DROP TABLE employees;
  ```
  - `employees` 테이블 삭제 (데이터 및 구조 모두 삭제)

- **인덱스 삭제**
  ```sql
  DROP INDEX idx_emp_salary;
  ```
  - `idx_emp_salary` 인덱스 삭제

- **뷰 삭제**
  ```sql
  DROP VIEW emp_view;
  ```
  - `emp_view` 뷰 삭제

---

### TRUNCATE (테이블 데이터 초기화)
- **모든 데이터 삭제 (ROLLBACK 불가)**
  ```sql
  TRUNCATE TABLE employees;
  ```
  - 테이블의 **모든 데이터 삭제 (구조는 유지)**
  - `DELETE`와 달리 트랜잭션 처리 없이 즉시 반영

| 비교 항목 | DELETE | TRUNCATE |
|----------|--------|----------|
| 삭제 범위 | 특정 행 삭제 가능 (`WHERE` 사용) | 테이블의 모든 행 삭제 |
| 트랜잭션 | `ROLLBACK` 가능 | `ROLLBACK` 불가능 |
| 성능 | 느림 (로그 기록) | 빠름 (로그 기록 최소화) |

---

### RENAME (객체 이름 변경)
- **테이블 이름 변경**
  ```sql
  RENAME employees TO emp_data;
  ```
  - `employees` 테이블을 `emp_data`로 변경

---

### COMMENT (객체에 주석 추가)
- **컬럼에 주석 추가**
  ```sql
  COMMENT ON COLUMN employees.salary IS '직원의 급여';
  ```
  - `salary` 컬럼에 "직원의 급여"라는 설명 추가

---

### DDL 사용 시 유의점
- **DDL 명령어는 자동 COMMIT됨** → 실행 후 ROLLBACK 불가
- **TRUNCATE와 DROP은 DELETE와 다르게 복구할 수 없음**
- **ALTER 사용 시 기존 데이터에 영향이 없는지 확인 필요**
- **RENAME을 사용할 경우 기존 객체를 참조하는 모든 객체에 영향**

---

### DDL과 DML 비교
| 구분 | DDL (Data Definition Language) | DML (Data Manipulation Language) |
|------|-------------------------------|-------------------------------|
| 목적 | 데이터베이스 구조 정의 및 변경 | 데이터 추가, 수정, 삭제 |
| 주요 명령어 | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` | `INSERT`, `UPDATE`, `DELETE`, `SELECT` |
| 트랜잭션 영향 | 자동 COMMIT (ROLLBACK 불가) | COMMIT 또는 ROLLBACK 가능 |
| 데이터 영향 | 테이블 구조 변경 (데이터 포함 가능) | 데이터만 변경 (구조 변경 없음) |




## DCL (Data Control Language)

### DCL 개념
- DCL (데이터 제어 언어)는 **데이터베이스의 보안과 권한을 관리**하는 SQL 명령어
- 특정 사용자에게 **데이터 접근 권한을 부여하거나 회수하는 역할**
- `GRANT`, `REVOKE` 명령어가 대표적이며, DBMS마다 세부적인 차이가 있음

---

### DCL 종류
- **GRANT**: 특정 사용자에게 데이터베이스 객체에 대한 권한 부여
- **REVOKE**: 기존에 부여한 권한을 회수

---

### GRANT (권한 부여)
- 특정 사용자에게 **테이블, 뷰, 프로시저, 시퀀스 등의 객체 접근 권한**을 부여

```sql
GRANT SELECT, INSERT ON employees TO user1;
```
- `user1`에게 `employees` 테이블에 대한 `SELECT`, `INSERT` 권한 부여

```sql
GRANT ALL PRIVILEGES ON employees TO user1;
```
- `user1`에게 `employees` 테이블에 대한 **모든 권한** 부여

```sql
GRANT SELECT ON employees TO user1 WITH GRANT OPTION;
```
- `WITH GRANT OPTION`: `user1`이 다른 사용자에게도 동일한 권한을 부여할 수 있도록 허용

```sql
GRANT CONNECT, RESOURCE TO user1;
```
- `CONNECT`: 데이터베이스 접속 권한
- `RESOURCE`: 객체 생성 권한 (테이블, 인덱스 등)

---

### REVOKE (권한 회수)
- 특정 사용자에게 부여한 권한을 제거

```sql title: ""
REVOKE SELECT, INSERT ON employees FROM user1;
```
- `user1`의 `employees` 테이블에 대한 `SELECT`, `INSERT` 권한 회수

```sql
REVOKE ALL PRIVILEGES ON employees FROM user1;
```
- `user1`의 `employees` 테이블에 대한 **모든 권한** 회수

```sql
REVOKE CONNECT FROM user1;
```
- `user1`의 데이터베이스 접속 권한 제거

---

### DCL 사용 시 유의점
- **DB 관리자(DBA) 또는 권한을 가진 사용자만 GRANT/REVOKE 실행 가능**
- **WITH GRANT OPTION**을 부여받은 사용자는 다른 사용자에게 권한을 부여할 수 있음
- `REVOKE`를 실행하면 해당 사용자가 **다른 사용자에게 부여한 권한도 모두 회수됨**
- DBMS에 따라 `GRANT`와 `REVOKE`의 지원 방식이 다를 수 있음

---

### DCL과 DML, DDL 비교
| 구분 | DCL (Data Control Language) | DML (Data Manipulation Language) | DDL (Data Definition Language) |
|------|----------------------------|----------------------------|----------------------------|
| 목적 | 권한 관리 | 데이터 조작 | 데이터베이스 객체 정의 및 변경 |
| 주요 명령어 | `GRANT`, `REVOKE` | `INSERT`, `UPDATE`, `DELETE`, `SELECT` | `CREATE`, `ALTER`, `DROP` |
| 적용 대상 | 사용자 및 권한 | 테이블의 데이터 | 테이블, 인덱스, 뷰 등 객체 |
| 트랜잭션 영향 | 즉시 적용 (ROLLBACK 불가) | `COMMIT`, `ROLLBACK` 가능 | 자동 `COMMIT` (ROLLBACK 불가) |


 

 

 

 

 
