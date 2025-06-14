-- SQL 명령어는 대소문자 구별이 없으며 
-- 편의를 위해 소문자로 작성했습니다.

-- 본 프로젝트에서 사용되는 
-- DB 파일(vending.sqlite3)과 초기 스키마 파일(init_schema.sql)은 
-- 프로그램 실행 경로 기준 "vending_data/" 폴더 안에 위치합니다.

-- 음료 재고 테이블
drop table if exists inventory;

create table inventory (
    id integer primary key autoincrement, 
    name text not null, 
    price int not null, 
    stock int not null
);

-- 화폐 재고 테이블
drop table if exists cash;

create table cash (
    denomination int primary key, 
    quantity int not null
);

-- 입출금 로그 테이블
drop table if exists log;
create table log (
    id integer primary key autoincrement, 
    role text not null, 
    action text not null, 
    amount int,
    item text, 
    timestamp text default current_timestamp
);

-- 10가지 음료의 초기 데이터 
insert into inventory (name, price, stock) values
('콜라', 1200, 5), 
('사이다', 1200, 5),
('환타', 1100, 5),
('웰치스', 1300, 5),
('레쓰비', 1000, 5),
('게토레이', 1500, 5),
('밀키스', 1400, 5),
('데미소다', 1100, 5),
('칸타타', 1600, 5),
('핫식스', 1700, 5); 

-- 화폐 초기 재고
insert into cash (denomination, quantity) values
(1000, 10),
(500, 10), 
(100, 10),
(50, 10);