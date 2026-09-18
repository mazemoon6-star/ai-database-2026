-- 현재 테이블 확인 / pg_tables : 포스트그레가 생성한 시스템 테이블(현재 있는 테이블이 다 확인가능)

select * from pg_tables;

select * from students s;


-- 테이블 컬럼 사이즈 수정 / 포스트그레에서는 ''만 문자열 "" 상관없음
alter table students 
alter column email type varchar(100);


--- 데이터 삽입
insert into students (age, major)
values (23, '경영학과');

--같은 이메일 입력
insert into students (name, age, email, major)
values ('홍홍홍', 24, 'hong@gmail.com', '일문학과');

-- 학년을 모두 4학년으로
update students set
 grade = 4;

-- 1번학생을 88학년으로
update students set
 grade = 88
 where id = 1;

-- 체크 제약조건 설정 후 새학생 추가
insert into students (name,email, major, grade)
values ('애슐리', 'ashely@gmail.com', '영문학과', 2);

--상품 추가 쿼리
insert into products (name, price, category)
values ('아이폰', 1600000,'전자제품');

insert into products (name, price)
values ('갤럭시S26', 1100000);




