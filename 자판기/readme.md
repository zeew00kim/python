# Python Vending Machine Project

## 프로젝트 개요

이 프로젝트는 Python, SQLite, Tkinter를 활용하여 구현한 데스크톱 자판기 프로그램입니다.  
사용자와 관리자가 사용할 수 있는 두 가지 모드를 제공하며, 음료 구매 및 재고/현금/로그 관리를 포함합니다.

---
## 디렉토리 구조

```yaml
vending_zeew00/  
├── main.py # 프로그램 실행 진입점  
├── vending_data/  
│ ├── vending.sqlite3 # SQLite DB 파일  
│ └── init_schema.sql # DB 초기화 스키마 및 데이터  
├── log/  
│ └── transaction_log.txt # 거래 내역 로그  
└── vending_core/  
├── admin_panel.py # 관리자 모드 UI  
├── beverage.py # Drink 클래스 (음료 재고 관리)  
├── cash_unit.py # CashManager 클래스 (현금 관리)  
├── db_init.py # DB 초기화 로직  
├── event_logger.py # 로그 기록 함수  
└── user_view.py # 사용자 모드 UI
```
---
## 주요 기능

### 사용자 모드
- 음료 선택 후 화폐 투입
- 구매 시 잔액 부족/재고 부족/잔돈 부족 처리
- 잔돈 자동 계산 및 반환
- 재고 차감 및 거래 로그 기록

### 관리자 모드
- 비밀번호 인증 (3회 제한)
- 전체 음료 재고 조회
- 재고 보충 기능
- 거래 로그 조회 (텍스트 파일로 저장된 로그 출력)
---
## DB 테이블 구성 (init_schema.sql)

- `inventory` : 음료 목록 (id, name, price, stock)
- `cash` : 화폐 재고 (denomination, quantity)
- `log` : 거래 내역 (role, action, amount, item, timestamp)
---
## 구현 세부사항

- DB 경로 및 로그 경로는 `os.path.abspath(__file__)` 기반으로 절대경로 처리되어, 실행 위치와 무관하게 정확히 작동함
- 모든 DB 접근은 try-except 블록으로 감싸 예외 발생 시 오류 메시지를 출력하고 프로그램 흐름을 유지함
- GUI는 Tkinter 기반이며, 사용자 입력은 `simpledialog`, 알림은 `messagebox`로 구성됨
- DB 파일이 없을 경우, 최초 실행 시 `init_database()`가 자동 호출되어 `init_schema.sql`의 내용을 기반으로 DB 생성 및 초기화 진행
---
## 실행 방법

```bash
python main.py
```
---
