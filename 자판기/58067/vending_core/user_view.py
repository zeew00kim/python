import tkinter as tk
from tkinter import messagebox

try:
    from vending_core.beverage import Drink
    from vending_core.cash_unit import CashManager
    from vending_core.event_logger import log_transaction
except ImportError as e:
    print("필요 모듈 호출 실패 :", e)

class UserView:
    def __init__(self, master):
        self.master = master
        self.master.title("사용자 모드")
        self.master.geometry("630x500")
        self.master.resizable(False, False)
        self.master.configure(bg="#cdeffc")

        self.drink_model = Drink()
        self.cash_manager = CashManager()
        self.selected_drink_id = None
        self.selected_button = None

        self.build_ui()

    def build_ui(self):
        container = tk.Frame(self.master, bg="#cdeffc")
        container.pack(pady=10)

        tk.Label(container, text="원하는 음료를 선택하세요.",
                 font=('맑은 고딕', 15, 'bold'), bg="#cdeffc").grid(row=0, column=0, columnspan=4, pady=(10, 15))

        drinks = self.drink_model.get_all_drinks()
        for idx, (drink_id, name, price, stock) in enumerate(drinks):
            def make_command(d_id, btn):
                return lambda: self.select_drink(d_id, btn)
            btn = tk.Button(container, text=f"{name} ({price}원)", width=15, height=2,
                            bg="#3c82e0", fg="white", font=('맑은 고딕', 10, 'bold'),
                            bd=2, relief="solid", cursor="hand2")
            btn.grid(row=1 + idx // 4, column=idx % 4, padx=8, pady=6)
            btn.config(command=make_command(drink_id, btn))
            self.add_hover_effect(btn, "#3c82e0", "#1e5bb8")

        tk.Label(container, text="음료의 금액을 투입해주세요.",
                 font=('맑은 고딕', 15, 'bold'), bg="#cdeffc").grid(row=4, column=0, columnspan=4, pady=(20, 10))

        cash_frame = tk.Frame(container, bg="#cdeffc")
        cash_frame.grid(row=5, column=0, columnspan=4)
        for i, denom in enumerate([1000, 500, 100, 50]):
            def make_insert_command(d):
                return lambda: self.insert_money(d)
            btn = tk.Button(cash_frame, text=f"{denom}원", width=10, height=2,
                            bg="#3c82e0", fg="white", font=('맑은 고딕', 10, 'bold'),
                            bd=2, relief="solid", cursor="hand2",
                            command=make_insert_command(denom))
            btn.grid(row=0, column=i, padx=5, pady=5)
            self.add_hover_effect(btn, "#3c82e0", "#1e5bb8")

        bottom_frame = tk.Frame(container, bg="#cdeffc")
        bottom_frame.grid(row=6, column=0, columnspan=4, pady=(20, 10))

        self.money_label = tk.Label(bottom_frame, text="투입 금액 : 0원",
                                    font=('맑은 고딕', 12, 'bold'), bg="#cdeffc")
        self.money_label.pack(side=tk.LEFT, padx=(10, 20))

        self.buy_btn = tk.Button(bottom_frame, text="구매", width=8, height=2,
                                 bg="#90ee90", fg="black",
                                 font=('맑은 고딕', 12, 'bold'),
                                 bd=2, relief="solid", cursor="hand2",
                                 command=self.try_purchase)
        self.buy_btn.pack(side=tk.LEFT)
        self.add_hover_effect(self.buy_btn, "#90ee90", "#5cb85c")

    def add_hover_effect(self, widget, normal_color, hover_color):
        widget.bind("<Enter>", lambda e: widget.config(bg=hover_color))
        widget.bind("<Leave>", lambda e: widget.config(bg=normal_color))

    def select_drink(self, drink_id, button):
        stock = self.drink_model.get_stock(drink_id)
        if stock is None or stock <= 0:
            name = [d[1] for d in self.drink_model.get_all_drinks() if d[0] == drink_id]
            name = name[0] if name else f"ID:{drink_id}"
            messagebox.showwarning("재고 부족", f"{name} 재고가 부족합니다.\n다른 음료를 선택해주세요.")
            return

        self.selected_drink_id = drink_id
        name = [d[1] for d in self.drink_model.get_all_drinks() if d[0] == drink_id][0]
        messagebox.showinfo("음료 선택 완료", f"{name}을 선택했습니다.")
        if self.selected_button:
            self.selected_button.config(bg="#3c82e0")
        if button:
            button.config(bg="#87CEFA")
            self.selected_button = button

    def insert_money(self, denom):
        self.cash_manager.insert_cash(denom)
        total = self.cash_manager.get_total_cash()
        self.money_label.config(text=f"투입 금액 : {total}원")

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

        change = total - price
        if change > 0:
            returned = self.cash_manager.return_change(change)
            if returned is None:
                messagebox.showerror("잔돈 부족", "잔돈이 부족하여 거래를 취소합니다.")
                return
            else:
                msg = ", ".join([f"{k}원 x {v}개" for k, v in returned.items()])
                messagebox.showinfo("잔돈 반환", msg)

        success = self.drink_model.decrease_stock(self.selected_drink_id)
        if not success:
            messagebox.showwarning("재고 부족", "해당 음료의 재고가 부족합니다.")
            return

        drinks = self.drink_model.get_all_drinks()
        name = next((d[1] for d in drinks if d[0] == self.selected_drink_id), "Unknown")
        log_transaction("사용자", "구매", f"{price}원", name)

        self.cash_manager.update_cash_stock()
        messagebox.showinfo("구매 완료", f"{name}의 구매가 완료되었습니다.")
        self.master.destroy()