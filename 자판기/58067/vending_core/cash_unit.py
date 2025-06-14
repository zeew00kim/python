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

# CashManager : 자판기의 현금 재고(cash 테이블)를 관리하는 클래스
class CashManager:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.inserted = {}  # {화폐단위: 개수} 딕셔너리 형태로 저장

    # 현금 투입
    def insert_cash(self, denomination, quantity=1):
        if denomination not in self.inserted:
            self.inserted[denomination] = 0
        self.inserted[denomination] += quantity

    # 투입된 총 금액 계산
    def get_total_cash(self):
        return sum(denom * qty for denom, qty in self.inserted.items())

    # 현재 DB에 저장된 현금 재고 조회
    def get_cash_stock(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("select denomination, quantity from cash")
                stock = dict(cursor.fetchall())
                return stock
        except sqlite3.Error as e:
            print("DB 오류 (get_cash_stock) :", e)
            return {}

    # 현금 재고 DB 업데이트 (투입 반영)
    def update_cash_stock(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                for denom, qty in self.inserted.items():
                    cursor.execute("update cash set quantity = quantity + ? where denomination = ?", (qty, denom))
                conn.commit()
                self.inserted.clear()
        except sqlite3.Error as e:
            print("DB 오류 (update_cash_stock) :", e)

    # 큰 단위부터 잔돈 계산 및 반환
    def return_change(self, change_amount):
        stock = self.get_cash_stock()
        if not stock:
            return None

        returned = {}

        for denom in sorted(stock.keys(), reverse=True):
            if denom > change_amount or stock[denom] == 0:
                continue
            max_use = min(change_amount // denom, stock[denom])
            if max_use > 0:
                returned[denom] = max_use
                change_amount -= denom * max_use
                stock[denom] -= max_use

        if change_amount == 0:
            try:
                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.cursor()
                    for denom, qty in returned.items():
                        cursor.execute("update cash set quantity = quantity - ? where denomination = ?", (qty, denom))
                    conn.commit()
                return returned
            except sqlite3.Error as e:
                print("DB 오류 (return_change) :", e)
                return None
        else:
            return None