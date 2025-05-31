import tkinter as tk
from tkinter import messagebox

# 외부 모듈 호출 실패 시 예외처리
try:
    from vending_core.user_view import UserView
    from vending_core.admin_panel import AdminView
    from vending_core.db_init import init_database
    init_database()
except ImportError as e:
    print("필요 모듈 로딩 실패 :", e)
    temp_root = tk.Tk()
    temp_root.withdraw()
    messagebox.showerror("시스템 오류", f"모듈 불러오기 실패 : {e}")
    temp_root.destroy()
    import sys
    sys.exit(1)

# VendingApp : 사용자 | 관리자 모드를 선택할 수 있는 창
class VendingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("자판기 프로그램")
        self.root.geometry("320x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#cdeffc")  # 연한 하늘 배경

        tk.Label(
            root,
            text="자판기 사용 모드를 선택하세요.",
            font=("맑은 고딕", 14, "bold"),
            bg="#cdeffc"
        ).pack(pady=(30, 25))

        # 버튼 생성 함수 (hover 효과 포함)
        def create_hover_button(parent, text, command):
            btn = tk.Button(
                parent,
                text=text,
                command=command,
                width=20,
                height=2,
                font=("맑은 고딕", 12, "bold"),
                bg="#5aa9e6",
                fg="white",
                bd=2,
                relief="solid",
                activebackground="#3e8ed0",
                cursor="hand2"
            )

            # Hover 효과 정의
            def on_enter(e):
                btn.config(bg="#3e8ed0")

            def on_leave(e):
                btn.config(bg="#5aa9e6")

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

            btn.pack(pady=10)
            return btn

        # 버튼 생성
        create_hover_button(root, "사용자 모드", self.launch_user_view)
        create_hover_button(root, "관리자 모드", self.launch_admin_view)
        create_hover_button(root, "사용 종료", root.quit)

    # 사용자 모드 실행
    def launch_user_view(self):
        user_window = tk.Toplevel(self.root)
        UserView(user_window)

    # 관리자 모드 실행
    def launch_admin_view(self):
        admin_window = tk.Toplevel(self.root)
        AdminView(admin_window)

# 실제 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = VendingApp(root)
    root.mainloop()