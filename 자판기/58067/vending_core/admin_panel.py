import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import sys

# 외부 모듈 호출 실패 시 예외처리
try:
    from vending_core.beverage import Drink
    from vending_core.cash_unit import CashManager
    from vending_core.event_logger import (
        log_transaction,
        USER_LOG_PATH,
        REFILL_LOG_PATH,
        CASH_LOG_PATH
    )
except ImportError as e:
    print("필요 모듈 호출 실패 :", e)
    messagebox.showerror("시스템 오류", f"모듈 로딩 실패 : {e}")
    sys.exit(1)


class AdminView:
    def __init__(self, master):
        self.master = master
        self.master.title("관리자 모드")
        self.master.geometry("600x600")
        self.master.configure(bg="#cdeffc")

        self.drink_model = Drink()
        self.cash_manager = CashManager()

        self.attempts = 0
        self.show_password_dialog()

    def show_password_dialog(self):
        def on_submit():
            pw = entry.get()
            dialog.destroy()
            if pw == "2022158067":
                self.build_admin_ui()
            else:
                self.attempts += 1
                remaining = 3 - self.attempts
                if remaining > 0:
                    messagebox.showwarning("오류", f"비밀번호가 틀렸습니다. ({remaining}회 남음)")
                    self.show_password_dialog()
                else:
                    messagebox.showerror("로그인 실패", "최대 시도 횟수를 초과했습니다.")
                    self.master.destroy()

        def on_cancel():
            dialog.destroy()
            self.master.destroy()

        dialog = tk.Toplevel(self.master)
        dialog.title("관리자 로그인")
        dialog.geometry("280x120")
        dialog.resizable(False, False)
        dialog.grab_set()

        tk.Label(dialog, text="관리자 비밀번호를 입력하세요 :").pack(pady=(10, 5))
        entry = tk.Entry(dialog, show='*', width=25)
        entry.pack()
        entry.focus()
        entry.bind("<Return>", lambda event: on_submit())

        button_frame = tk.Frame(dialog)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="확인", width=10, command=on_submit).pack(side="left", padx=5)
        tk.Button(button_frame, text="취소", width=10, command=on_cancel).pack(side="right", padx=5)

    def create_hover_button(self, parent, text, command):
        btn = tk.Button(parent, text=text, font=("맑은 고딕", 10, "bold"),
                        bg="#5aa9e6", fg="white", width=12, relief="solid",
                        command=command, bd=2, activebackground="#3e8ed0", cursor="hand2")
        btn.bind("<Enter>", lambda e: btn.config(bg="#3e8ed0"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#5aa9e6"))
        return btn

    def build_admin_ui(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        outer_frame = tk.Frame(self.master, bg="#cdeffc")
        outer_frame.pack(expand=True)

        tk.Label(outer_frame, text="음료 재고 현황", font=("맑은 고딕", 12, "bold"),
                 fg="blue", bg="#cdeffc").grid(row=0, column=0, columnspan=3, pady=10)
        tk.Label(outer_frame, text="화폐 시재 현황", font=("맑은 고딕", 12, "bold"),
                 fg="blue", bg="#cdeffc").grid(row=0, column=3, columnspan=2)

        self.drinks = self.drink_model.get_all_drinks()
        cash_stock = self.cash_manager.get_cash_stock()
        max_rows = max(len(self.drinks), len(cash_stock))

        for idx in range(max_rows):
            if idx < len(self.drinks):
                drink_id, name, price, stock = self.drinks[idx]
                tk.Label(outer_frame, text=f"{name} : {stock}개",
                         font=("맑은 고딕", 11, 'bold'), bg="#cdeffc").grid(row=1 + idx, column=0, sticky="e", padx=(10, 5), pady=6)
                btn = self.create_hover_button(outer_frame, "보충", lambda d=drink_id: self.refill_prompt(d))
                btn.grid(row=1 + idx, column=1, columnspan=2, sticky="w", padx=(5, 20), pady=6)

            if idx < len(cash_stock):
                denom = sorted(cash_stock.keys(), reverse=True)[idx]
                qty = cash_stock[denom]
                tk.Label(outer_frame, text=f"{denom}원 : {qty}개",
                         font=("맑은 고딕", 11, 'bold'), bg="#cdeffc").grid(row=1 + idx, column=3, sticky="e", padx=(10, 5), pady=6)
                btn = self.create_hover_button(outer_frame, "보충", lambda d=denom: self.add_cash(d))
                btn.grid(row=1 + idx, column=4, sticky="w", padx=(5, 10), pady=6)

        log_frame = tk.Frame(outer_frame, bg="#cdeffc")
        log_frame.grid(row=max_rows + 2, column=0, columnspan=6, pady=30)

        self.create_hover_button(log_frame, "음료 판매 현황", self.show_user_log).grid(row=0, column=0, padx=7)
        self.create_hover_button(log_frame, "음료 보충 목록", self.show_refill_log).grid(row=0, column=1, padx=7)
        self.create_hover_button(log_frame, "화폐 보충 목록", self.show_cash_log).grid(row=0, column=2, padx=7)
        self.create_hover_button(log_frame, "목록 새로고침", self.build_admin_ui).grid(row=0, column=3, padx=7)

    def refill_prompt(self, drink_id):
        try:
            amount = simpledialog.askinteger("재고 보충", "보충할 수량을 입력하세요 :", minvalue=1)
            if amount:
                self.drink_model.refill_stock(drink_id, amount)
                name = next((n for i, n, p, s in self.drinks if i == drink_id), f"음료 ID: {drink_id}")
                log_transaction("관리자", "음료 보충", f"{amount}개", name)
                messagebox.showinfo("완료", "재고가 보충되었습니다.")
                self.build_admin_ui()
        except Exception as e:
            messagebox.showerror("오류", f"보충 중 오류 발생 : {e}")

    def add_cash(self, denomination):
        try:
            amount = simpledialog.askinteger("화폐 보충", f"보충할 {denomination}원 화폐의 수량", minvalue=1)
            if amount:
                self.cash_manager.inserted = {}
                self.cash_manager.insert_cash(denomination, amount)
                self.cash_manager.update_cash_stock()
                log_transaction("관리자", "화폐 보충", f"{amount}개", f"{denomination}원")
                messagebox.showinfo("완료", f"{denomination}원 {amount}개 추가완료")
                self.build_admin_ui()
        except Exception as e:
            messagebox.showerror("오류", f"화폐 보충 중 오류 발생 : {e}")

    def _show_log_window(self, path):
        if not os.path.exists(path):
            messagebox.showwarning("로그 없음", "해당 로그 파일이 존재하지 않습니다.")
            return

        log_window = tk.Toplevel(self.master)
        log_window.title("로그 보기")
        frame = tk.Frame(log_window)
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_area = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, width=70, height=20)
        scrollbar.config(command=text_area.yview)

        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                text_area.insert(tk.END, line)

        text_area.config(state='disabled')
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Button(log_window, text="닫기", command=log_window.destroy).pack(pady=5)

    def show_user_log(self):
        self._show_log_window(USER_LOG_PATH)

    def show_refill_log(self):
        self._show_log_window(REFILL_LOG_PATH)

    def show_cash_log(self):
        self._show_log_window(CASH_LOG_PATH)