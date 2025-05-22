import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys

class HomeView:
    def __init__(self, root):
        self.root = root
        self.root.title("Hội Công đoàn")
        window_width = 1000
        window_height = 600

        # Lấy kích thước màn hình
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Tính toán vị trí để căn giữa
        x_coordinate = (screen_width // 2) - (window_width // 2)
        y_coordinate = (screen_height // 2) - (window_height // 2)

        # Thiết lập kích thước và vị trí của cửa sổ
        root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        
        
        #Thiết lập MENU
        self.menu_frame = tk.Frame(root, bg="#00CCFF", bd=5, relief="sunken")
        self.menu_frame.place(relwidth=0.25, relheight=1.0)
        
        self.menu_label = ttk.Label(self.menu_frame, text="MENU", font=("arial",20))
        self.menu_label.place(x=60, y=20)
        
        self.clan_button = ttk.Button(self.menu_frame,text="TT Hội")
        self.clan_button.place(x=60, y=150, width=85)
        
        self.person_button = ttk.Button(self.menu_frame, text="thành viên")
        self.person_button.place(x=60, y=180, width=85)
        
        self.feedback_button = ttk.Button(self.menu_frame,text="Phản hồi")
        self.feedback_button.place(x=60, y=210, width=85)
        
        self.signoutbutton = ttk.Button(self.menu_frame, text="Đăng xuất")
        self.signoutbutton.place(x=60, y=400, width=85)
        
        # Thiết lập header cho clan
        self.header_frame =tk.Frame(root,bg="blue",bd =5)
        self.header_frame.place(relwidth=0.75,relheight=0.25, relx=0.25)
        
        self.header_label = ttk.Label(self.header_frame, text="WELCOME TO APP!", font=("arial", 24))
        self.header_label.place(x=200, y=50)
        
        
        
        # Thiết lập thông tin cá nhân
        self.user_frame = tk.Frame(root, bd=5)
        self.user_frame.place(relwidth=0.75, relheight=0.75, relx=0.25, rely=0.25)
        
        self.user_label = ttk.Label(self.user_frame, text="Thông tin của Hội trưởng", font=("arial", 24))
        self.user_label.place(x=160, y=10)
        
        self.name_label = ttk.Label(self.user_frame, text="Họ và tên:", font=("arial", 16))
        self.name_label.place(x=50, y=70)
        
        self.cccd_label =ttk.Label(self.user_frame, text="CCCD",font=("arial", 16))
        self.cccd_label.place(x=450, y=70)
        
        self.age_label =ttk.Label(self.user_frame, text="Năm sinh",font=("arial", 16))
        self.age_label.place(x=50,y=110)
        
        self.cb_label =ttk.Label(self.user_frame, text="Cấp bậc",font=("arial", 16))
        self.cb_label.place(x=50, y=150)
        
        self.cv_label =ttk.Label(self.user_frame, text="Chức vụ hội",font=("arial", 16))
        self.cv_label.place(x=50,y=190)
        
        self.dv_label =ttk.Label(self.user_frame, text="Đơn vị",font=("arial", 16))
        self.dv_label.place(x=50, y=230)
        
       
        
    
    
        
        