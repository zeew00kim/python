import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'vending_data', 'vending.sqlite3')
SCHEMA_PATH = os.path.join(BASE_DIR, 'vending_data', 'init_schema.sql')

def init_database():
    if not os.path.exists(DB_PATH):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            schema = f.read()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.executescript(schema)
        conn.commit()
        conn.close()
        print("DB 생성 및 초기화 완료")
    else:
        print("이미 존재하는 DB (초기화 생략)")
