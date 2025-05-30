import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE_PATH = os.path.join(BASE_DIR, 'log', 'transaction_log.txt')

# 상품 판매 이력(로그)를 텍스트파일에 저장
def log_transaction(role, action, amount=None, item=None):
    try:
        os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(LOG_FILE_PATH, 'a', encoding='utf-8') as file:
            line = f"[{timestamp}] {role} | {action}"
            if amount is not None:
                line += f" | {amount}원"
            if item:
                line += f" | {item}"
            file.write(line + '\n')
    except Exception as e:
        print("로그 기록 실패 :", e)