import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 로그 파일 경로 정의
USER_LOG_PATH = os.path.join(BASE_DIR, 'log', 'user_log.txt')
REFILL_LOG_PATH = os.path.join(BASE_DIR, 'log', 'refill_log.txt')
CASH_LOG_PATH = os.path.join(BASE_DIR, 'log', 'cash_log.txt')

def log_transaction(role, action, amount=None, item=None):
    try:
        # 역할과 동작에 따라 파일 분기
        if role == "사용자":
            log_path = USER_LOG_PATH
        elif role == "관리자" and action == "음료 보충":
            log_path = REFILL_LOG_PATH
        elif role == "관리자" and action == "화폐 보충":
            log_path = CASH_LOG_PATH
        else:
            # 예외 상황을 대비한 기본 경로
            log_path = os.path.join(BASE_DIR, 'log', 'etc_log.txt')

        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(log_path, 'a', encoding='utf-8') as file:
            line = f"[{timestamp}] {role} | {action}"
            if amount is not None:
                line += f" | {amount}"
            if item:
                line += f" | {item}"
            file.write(line + '\n')

    except Exception as e:
        print("로그 기록 실패 :", e)