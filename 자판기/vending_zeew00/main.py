import tkinter as tk
from tkinter import messagebox

# 외부 모듈 호출 예외 처리
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

        tk.Label(root, text="자판기 사용 모드를 선택하세요.", font=("Arial", 14)).pack(pady=15)

        tk.Button(root, text="사용자 모드", width=20, height=2,
                  command=self.launch_user_view).pack(pady=5)

        tk.Button(root, text="관리자 모드", width=20, height=2,
                  command=self.launch_admin_view).pack(pady=5)

        tk.Button(root, text="종료", width=20, height=2,
                  command=root.quit).pack(pady=20)

    # 사용자 모드 실행
    def launch_user_view(self):
        user_window = tk.Toplevel(self.root)
        UserView(user_window)

    # 관리자 모드 실행
    def launch_admin_view(self):
        admin_window = tk.Toplevel(self.root)
        AdminView(admin_window)

# 실제 실행 시 메인 루프 진입
if __name__ == "__main__":
    root = tk.Tk()
    app = VendingApp(root)
    root.mainloop()