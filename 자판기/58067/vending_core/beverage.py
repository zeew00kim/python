import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'vending_data', 'vending.sqlite3')

# class Drink : 음료의 재고(inventory) 정보를 관리하는 클래스
class Drink:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path

    # 모든 음료 목록 조회
    def get_all_drinks(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("select id, name, price, stock from inventory")
        drinks = cursor.fetchall()
        conn.close()
        return drinks

    # 특정 음료 가격 조회
    def get_price(self, drink_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("select price from inventory where id = ?", (drink_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    # 특정 음료 재고 조회
    def get_stock(self, drink_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("select stock from inventory where id = ?", (drink_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    # 재고 수량 1ea 감소
    def decrease_stock(self, drink_id):        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("update inventory set stock = stock - 1 where id = ? and stock > 0", (drink_id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0  # True 값일 경우 성공적으로 감소

    # 재고 보충하기 (관리자용)
    def refill_stock(self, drink_id, amount):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("update inventory set stock = stock + ? where id = ?", (amount, drink_id))
        conn.commit()
        conn.close()