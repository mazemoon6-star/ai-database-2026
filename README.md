# AI-database-2026

AI에이전트 개발자 데이터베이스 리포지토리

## 1일차

### PostgreSQL 개요 (C+S+v / 편집기)

데이터베이스. 데이터를 한군데에서 관리하는 목적의 시스템

줄여서 Postgre, Postgres 라고 통칭. **관계형** 데이터베이스.

`SQL` 을 통해서 데이터를 저장, 수정, 삭제, 조회 할 수 있는 시스템

- 기타 관계형 데이터베이스

  - Oracle
  - MySQL / MariaDB
  - SQL Server

  위 대부분 상용 소프트웨어, Postgre는 **오픈소스 시스템** . 라이선스 비용 X

### DB의 특징

- 데이터 무결성(고유값.변동없음)
- 데이터 안정성(영구적 보관)
- 데이터 동시성
- 표준SQL 지원
- 확장성

### PostgreSQL 설치

![alt text](image-3.png)

#### 기본 설치

- 자신의 OS에 직접 설치하는 방법

* postgresql-18.6-3-windows-x64.ex 실행
  ![alt text](20260915_112053_image (2).png)

![alt text](image.png)

- superuser id  - postgre 패스워드 지정
- port 5432 기억할것 (port 는 내가 사용하면 다른 사람은 사용이 안됨)

### Docker 설치

- 윈도우 버전으로 다운로드 후 설치
- http://docs.docker.com/desktop/setup/install/windows-install/

  ![](assets/20260915_162234_image.png)
- Close and Restart 이후
- WSL(Windows Subsystem for Linux) 추가 설치

  ![](assets/20260915_175128_20260915_135904_image.png)

  ![](assets/20260915_175142_20260915_143106_image.png)

  - 설치 완료 후 화면
  - 사용자 user생성 비밀번호 입력

#### Docker 란,

- 환경의존성을 문제를 해결한 컨테이너 기술 솔루션
- __*가상환경*__ 상 프로그램을 실행하도록 제공
- 컨테이너란, OS, 라이브러리, 설정 등 하나의 패키지로 만들어진 이미지
- 기본 Docker(명령어) 실행파일 -> Docker Desktop(마우스로) 윈도우에서 Docker를 편하게 사용하도록

#### DBeaver 설치

GUI DB관리 실행 툴

- https://dbeaver.io/download
  ![alt text](image-4.png)

DB접속

![alt text](20260915_121803_image.png)

1. DBeaver 실행
2. 새 데이터베이스 연결
3. 데이터베이스 설정

![alt text](image-6.png)

4. Test Connection 클릭 Driver 다운로드 후
5. Connected 나오면 정상접속 확인 후 완료 >> 마우스로 만든 거

![alt text](image-7.png)
![alt text](image-8.png)

### PostgreSQL 이미지 다운로드

- 이미지 : 도커 리포지토리에 미리 만들어놓은 시스템 패키지
- 컨테이너 : 나의 도커에서 미리 다운로드 받은 이미지를 동작시킨 시스템

  ##### 도커 명령어 기본


  ```bash
  docker --version
  ```
- 설치된 도커 확인

  ##### 도커에서 PostgreSQL 이미지 다운로드


  ```bash
  docker pull postgres:latest
  ```
- Docker Desktop 전체 검색에서 pull(다운로드)

#### 컨테이너 실행

##### 도커 명령어로 실행

- 여러 옵션으로 실행 해야 하므로 거의 대부분 명령어로 실행
  ```bash
  docker run --name my-postgres -e POSTGRES_PASSWORD=123456 -p 25432:5432 -d postgres:latest
  ```

![](assets/20260915_165430_image.png)

#### DBeaver에서 접속

### DB 기본 사용법

#### PostgreSQL 기본구조

![](assets/20260915_143339_image.png)

- ai_db : 데이터베이스(프로젝트 전체 공간)
- Schemas : 프로젝트 폴더
- Tables : 실제 데이터를 담는 표
- *DB 만든 후 f5 새로고침으로 확인하기*

![](assets/20260915_170503_image.png)

- docker 포터 25432 로 생성 후 DBeaver 에서 새로운 postgres DB생성

#### DB생성

- DBeaver SQL편집기 클릭
- 새 이름으로 저장 , *(특정이름).sql 로 저장
- 아래의 코드를 작성

  ```sql
  create database ai_db;
  ```
- Ctrl + Enter 로 쿼리 실행
- DB 접속 정보에서 Show All Databases를 체크하고 재접속
- 데이터베이스 생성 확인

##### 테이블 생성

- 데이터베이스 스키마를 사용할 데이터베이스로 **반드시** 선택

![](assets/20260915_150520_image.png)

- 아래의 코드를 작성

  ```sql
  create table students (
       id int generated always as identity primary key, -- id 학생구분값 자동증가
       name varchar (50) not null, -- 이름
       age int,-- 나이
       email varchar(100), -- 이메일
       creatated_at timestamp default current_timestamp -- 현재 작성된 일자
  );
  ```

##### 데이터 생성

- insert (삽입) 쿼리 / select (확인) 쿼리 작성 > 난이도가 올라감 / update (수정) 쿼리 / delete (삭제) 쿼리 >> 직접 입력해서 만든 거
- ```sql
  -- 데이터 삽입(INSERT)
  insert into public.students (name, age, email)
  values ('홍길동', 20, 'honggd@example.com');

  insert into public.students (name, age, email)
  values ('김철수', 21, 'chulsu@gmail.com'),
  ('이영희', 21, 'lee@gmail.com'),
  ('박민수', 22, 'park@gmail.com'),
  ('성명건', 50, 'sung@gmail.com');

  -- 데이터 확인(SELECT)
  select * from public.students;

  -- 데이터 수정(UPDATE)
  update students set
  email = 'hong@kakao.com'
  where id = 1;

  --데이터 삭제(DELETE)
  delete from students
  where name = '홍길동';
  ```
- CRUD > Create, Read, Update, Delete 의 약자

  - C - INSERT
  - R - SELECT
  - U - UPDATE
  - D - DELETE

#### Postgres 기본 타입


| 데이터 타입 | 설명                     | 예제                |
| :---------- | ------------------------ | :------------------ |
| INT         | 정수                     | 10,25,-9            |
| BIGINT      | 큰 정수                  | 10000000            |
| NUMERIEC    | 정확한 소수              | 12000.56            |
| VARCHAR(n)  | 길이 제한 문자열(4000자) | '홍길동'            |
| TEXT        | 긴 문자열(1G)            | 뉴스 게시물 본문    |
| BOOLEAN     | 참 또는 거짓             | true, false         |
| DATE        | 날짜                     | 2026-09-15          |
| TIMESTAMP   | 일자(날짜와 시간)        | 2026-09-15 16:00:20 |
| JSONB       | JSON 데이터              | {"name" : "홍길동"} |
