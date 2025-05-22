import tkinter as tk
from tkinter import ttk


class TTHoi:
    def __init__(self, root, parent_geometry):
        self.root = root
        self.root.title(" Thông tin hội")
        self.root.geometry(parent_geometry)

        self.header_frame = tk.Frame(root, bg="#66CCFF")
        self. header_frame.place(relheight=1, relwidth=1, relx=0, rely=-0)
        
        self.header_label = tk.Label(root, text="THÔNG TIN HỘI", font=("arial", 20, "bold"))
        self.header_label.pack(pady=20) 

        self.tthoi_frame = tk.Frame(self.root,bd=2, relief="solid", bg="#CCFFFF")
        self.tthoi_frame.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.1)
        
        self.name_hoi_label = tk.Label(self.tthoi_frame, text ="Tên hội:", font=("arial", 16,))
        self.name_hoi_label.place(x=20, y=10)
        
        self.name_thanhvien_label = tk.Label(self.tthoi_frame, text="Thành viên:", font =("arial", 16))
        self.name_thanhvien_label.place(x=20, y=40)

        self.tt_frame = tk.Frame(self.root, bd=2, relief="solid", bg="#CCFFFF")
        self.tt_frame.place(relwidth=0.9, relheight=0.40, relx=0.05, rely=0.4)

        self.thanhtich_label = tk.Label(self.tt_frame, text="Thành tích của Hội:", font=("arial", 16, "bold"))
        self.thanhtich_label.place(x=30, y=15)

        self.htsxnv_label = tk.Label(self.tt_frame, text="HTSXNV:", font=("arial",16))
        self.htsxnv_label.place(x=30, y=55)

        self.httnv_label = tk.Label(self.tt_frame, text="HTTNV:", font=("arial",16))
        self.httnv_label.place(x=260, y=55)

        self.htnv_label = tk.Label(self.tt_frame, text="HTNV:", font=("arial",16))
        self.htnv_label.place(x=490, y=55)

        self.khtnv_label = tk.Label(self.tt_frame, text="KHTNV:", font=("arial",16))
        self.khtnv_label.place(x=720, y=55)

        self.nam_combobox = ttk.Combobox(self.tt_frame, text="chọn năm", font=("arial",16,"bold"), values=["2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025"])
        self.nam_combobox.set("Chọn năm")
        self.nam_combobox.place(x=30, y=90)

        self.note_text = tk.Text(self.tt_frame, height=6, width=50, font=("arial",14))
        self.note_text.place(x=300, y=90)

        self.update_button = tk.Button(self.root, text="Cập nhập", font=("arial",14,"bold"))
        self.update_button.place(x=650, y=500)
        
        self.exit_button = tk.Button(self.root, text="Thoát", font=("arial",14,"bold"))
        self.exit_button.place(x=800, y=500)