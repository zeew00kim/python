import tkinter as tk
from tkinter import messagebox

# 외부 모듈 호출 실패 시 예외처리 구문 실행
try:
    from vending_core.beverage import Drink
    from vending_core.cash_unit import CashManager
    from vending_core.event_logger import log_transaction
except ImportError as e:
    print("필요 모듈 호출 실패 :", e)


# UserView : 사용자 인터페이스(UI) 클래스 == (음료 선택 -> 화폐 투입 -> 구매 흐름)
class UserView:
    def __init__(self, master):
        self.master = master
        self.master.title("사용자 모드")
        
        self.drink_model = Drink()              
        self.cash_manager = CashManager()       
        self.selected_drink_id = None           
        
        self.build_ui()

    # 전체 UI 구성
    def build_ui(self):
        # 음료 선택 버튼 영역
        tk.Label(self.master, text="원하는 음료를 선택하세요.").grid(row=0, column=0, columnspan=4)
        drinks = self.drink_model.get_all_drinks()
        for idx, (drink_id, name, price, stock) in enumerate(drinks):
            def make_command(d_id):
                return lambda: self.select_drink(d_id)
            btn = tk.Button(self.master, text=f"{name} ({price}원)", width=15,
                    command=make_command(drink_id))
            btn.grid(row=1 + idx // 4, column=idx % 4, padx=5, pady=5)

        # 화폐 투입 버튼 영역
        tk.Label(self.master, text="음료의 금액을 투입해주세요.").grid(row=5, column=0, columnspan=4)
        for i, denom in enumerate([1000, 500, 100, 50]):
            def make_insert_command(d):
                return lambda: self.insert_money(d)
            btn = tk.Button(self.master, text=f"{denom}원", width=10,
                    command=make_insert_command(denom))
            btn.grid(row=6, column=i, padx=5, pady=5)


        # 투입 금액 표시 및 구매 버튼
        self.money_label = tk.Label(self.master, text="투입 금액 : 0원")
        self.money_label.grid(row=7, column=0, columnspan=2)

        self.buy_btn = tk.Button(self.master, text="구매", command=self.try_purchase)
        self.buy_btn.grid(row=7, column=2, columnspan=2)

    # 음료 선택 처리
    def select_drink(self, drink_id):
        self.selected_drink_id = drink_id
        name = [d[1] for d in self.drink_model.get_all_drinks() if d[0] == drink_id][0]
        messagebox.showinfo("음료 선택 완료", f"{name}을 선택했습니다.")

    # 금액 투입 처리
    def insert_money(self, denom):
        self.cash_manager.insert_cash(denom)
        total = self.cash_manager.get_total_cash()
        self.money_label.config(text=f"투입 금액 : {total}원")

    # 구매 시도 처리
    def try_purchase(self):
        if self.selected_drink_id is None:
            messagebox.showwarning("오류", "음료를 먼저 선택해주세요.")
            return

        price = self.drink_model.get_price(self.selected_drink_id)
        total = self.cash_manager.get_total_cash()

        if price is None:
            messagebox.showerror("오류", "해당 음료 정보를 찾을 수 없습니다.")
            return

        if total < price:
            messagebox.showwarning("잔액 부족", f"{price}원이 필요합니다.")
            return

        # 잔돈 계산 및 반환
        change = total - price
        if change > 0:
            returned = self.cash_manager.return_change(change)
            if returned is None:
                messagebox.showerror("잔돈 부족", "잔돈이 부족하여 거래를 취소합니다.")
                return
            else:
                msg = ", ".join([f"{k}원 x {v}개" for k, v in returned.items()])
                messagebox.showinfo("잔돈 반환", msg)

        # 재고 차감
        success = self.drink_model.decrease_stock(self.selected_drink_id)
        if not success:
            messagebox.showwarning("재고 부족", "해당 음료의 재고가 부족합니다.")
            return

        # 로그 기록
        drinks = self.drink_model.get_all_drinks()
        name = next((d[1] for d in drinks if d[0] == self.selected_drink_id), "Unknown")

        log_transaction("사용자", "구매", price, name)

        # 현금 재고 반영 및 안내
        self.cash_manager.update_cash_stock()
        messagebox.showinfo("구매 완료", f"{name}의 구매가 완료되었습니다.")
        self.master.destroy()