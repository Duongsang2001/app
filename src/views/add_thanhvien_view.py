import tkinter as tk
from tkinter import ttk

class AddThanhVienView():
    def __init__(self, root):
        self.root = root
        self.root.title("Thêm Thành Viên")
        self.root.geometry("400x350")

        self.header_frame = tk.Frame(root, bg="#66CCFF")
        self. header_frame.place(relheight=1, relwidth=1, relx=0, rely=-0)
        
        self.header_label = tk.Label(self.root, text="Thêm thành viên", font=("arial", 20, "bold"))
        self.header_label.place(x=100, y=10)
        
        self.add_cccd_label = tk.Label(self.root, text="Nhập CCCD:", font=("arial", 14))
        self.add_cccd_label.place(x=40, y=60)
        self.add_cccd_entry = tk.Entry(self.root, width=25)
        self.add_cccd_entry.place(x=180, y=60)
        
        self.add_name_label = tk.Label(self.root, text="Nhập tên:", font=("arial", 14))
        self.add_name_label.place(x=40, y=100)
        self.add_name_entry = tk.Entry(self.root, width=25)
        self.add_name_entry.place(x=180, y=100)
        
        self.add_namsinh_label = tk.Label(self.root, text="năm sinh:", font=("arial", 14))
        self.add_namsinh_label.place(x=40, y=140)
        self.add_namsinh_entry = tk.Entry(self.root, width=25)
        self.add_namsinh_entry.place(x=180, y=140)
        
        self.add_cb_label = tk.Label(self.root, text="Cấp bậc:", font=("arial", 14))
        self.add_cb_label.place(x=40, y=180)
        self.add_cb_entry = tk.Entry(self.root, width=25)
        self.add_cb_entry.place(x=180, y=180)
        
        self.add_cv_label = tk.Label(self.root, text="Chức vụ hội:", font=("arial", 14))
        self.add_cv_label.place(x=40, y=220)
        self.add_cv_entry = tk.Entry(self.root, width=25)
        self.add_cv_entry.place(x=180, y=220)
        
        self.add_dv_label = tk.Label(self.root, text="Đơn vị:", font=("arial", 14))
        self.add_dv_label.place(x=40, y=260)
        self.add_dv_entry = tk.Entry(self.root, width=25)
        self.add_dv_entry.place(x=180, y=260)
        
        self.add_btn = tk.Button(self.root, text="Thêm", width=5)
        self.add_btn.place(x=250, y=300)
        
        
        
    def add_thanhvien(self):
        return(
        self.add_cccd_entry.get(),
        self.add_name_entry.get(),
        self.add_namsinh_entry.get(),
        self.add_cb_entry.get(),
        self.add_cv_entry.get(),
        self.add_dv_entry.get()
        )
 
   
