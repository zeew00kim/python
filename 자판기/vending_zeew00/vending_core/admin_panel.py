import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import sys

# 외부 모듈 호출 실패 시 예외처리
try:
    from vending_core.beverage import Drink
    from vending_core.cash_unit import CashManager
    from vending_core.event_logger import LOG_FILE_PATH, log_transaction
except ImportError as e:
    print("필요 모듈 호출 실패 :", e)
    messagebox.showerror("시스템 오류", f"모듈 로딩 실패 : {e}")
    sys.exit(1)

# AdminView : 관리자 모드 (로그인 -> 재고 확인, 보충, 로그 확인)
class AdminView:
    def __init__(self, master):
        self.master = master
        self.master.title("관리자 모드")

        self.drink_model = Drink()
        self.cash_manager = CashManager()
        self.build_login_screen()

    # 로그인 화면 구성 (로그인 시도 3회 실패 시 화면 종료)
    def build_login_screen(self):
        MAX_TRIES = 3
        for attempt in range(MAX_TRIES):
            pw = simpledialog.askstring("로그인", "관리자 비밀번호를 입력하세요 :", show='*')
            if pw == "2022158067":
                self.build_admin_ui()
                return
            else:
                remaining = MAX_TRIES - (attempt + 1)
                if remaining > 0:
                    messagebox.showwarning("오류", f"비밀번호가 틀렸습니다. ({remaining}회 남음)")
                else:
                    messagebox.showerror("로그인 실패", "최대 시도 횟수를 초과했습니다.")
                    self.master.destroy()

    # 관리자 화면 구성 
    def build_admin_ui(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="현재 음료 재고 현황").grid(row=0, column=0, columnspan=3)
        tk.Label(self.master, text="화폐 재고 현황").grid(row=0, column=3, columnspan=2)

        self.drinks = self.drink_model.get_all_drinks()
        cash_stock = self.cash_manager.get_cash_stock()
        max_rows = max(len(self.drinks), len(cash_stock))

        for idx in range(max_rows):
            if idx < len(self.drinks):
                drink_id, name, price, stock = self.drinks[idx]
                tk.Label(self.master, text=f"{name} ({price}원) : {stock}개").grid(row=1 + idx, column=0, columnspan=2)
                tk.Button(self.master, text="보충", command=lambda d=drink_id: self.refill_prompt(d)).grid(row=1 + idx, column=2)

            if idx < len(cash_stock):
                denom = sorted(cash_stock.keys(), reverse=True)[idx]
                qty = cash_stock[denom]
                tk.Label(self.master, text=f"{denom}원 : {qty}개").grid(row=1 + idx, column=3)

                def make_add_command(d=denom):
                    return lambda: self.add_cash(d)

                tk.Button(self.master, text="보충", command=make_add_command(denom)).grid(row=1 + idx, column=4)

        tk.Button(self.master, text="입출금 로그 보기", command=self.show_log).grid(
            row=max_rows + 2, column=0, columnspan=5, pady=10
        )

    # 음료 재고 보충
    def refill_prompt(self, drink_id):
        try:
            amount = simpledialog.askinteger("재고 보충", "보충할 수량을 입력하세요 :", minvalue=1)
            if amount:
                self.drink_model.refill_stock(drink_id, amount)
                messagebox.showinfo("완료", "재고가 보충되었습니다.")
                self.build_admin_ui()
        except Exception as e:
            messagebox.showerror("오류", f"보충 중 오류 발생 : {e}")

    # 화폐 보충 처리
    def add_cash(self, denomination):
        try:
            amount = simpledialog.askinteger("화폐 보충", f"보충할 {denomination}원 화폐의 수량", minvalue=1)
            if amount:
                self.cash_manager.inserted = {}
                self.cash_manager.insert_cash(denomination, amount)
                self.cash_manager.update_cash_stock()
                log_transaction("관리자", "화폐 보충", amount, f"{denomination}원")
                messagebox.showinfo("완료", f"{denomination}원 {amount}개 추가완료")
                self.build_admin_ui()
        except Exception as e:
            messagebox.showerror("오류", f"화폐 보충 중 오류 발생 : {e}")

    # 로그 보기
    def show_log(self):
        if os.path.exists(LOG_FILE_PATH):
            log_window = tk.Toplevel(self.master)
            log_window.title("입출금 로그")

            frame = tk.Frame(log_window)
            frame.pack(fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            text_area = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, width=60, height=20)
            scrollbar.config(command=text_area.yview)

            with open(LOG_FILE_PATH, 'r', encoding='utf-8') as f:
                content = f.read()
                text_area.insert(tk.END, content)

            text_area.config(state='disabled')
            text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            tk.Button(log_window, text="닫기", command=log_window.destroy).pack(pady=5)
        else:
            messagebox.showwarning("로그 없음", "해당 로그 파일이 존재하지 않습니다.")
