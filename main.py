import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),"src"))
from tkinter import messagebox
import tkinter as tk
from src.controllers.login_controller import LoginController

def on_close():
    """
    Hàm xử lý khi người dùng nhấn nút X để đóng cửa sổ.
    """ 
    if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn kết thúc chương trình?"):
        sys.exit()  # Kết thúc chương trình
    else:
        pass  # Hủy hành động đóng cửa sổ


if __name__ == "__main__":
    root = tk.Tk()  
    controller = LoginController(root)
    root.protocol("WM_DELETE_WINDOW", on_close)

    root.mainloop() 