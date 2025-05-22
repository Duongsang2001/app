import tkinter as tk
from tkinter import ttk


class ListTVView:
    def __init__(self, root, parent_geometry):
        self.root = root
        self.root.title("Danh sách thành viên")
        self.root.geometry(parent_geometry)
        
        # Header Label
        self.header_label = tk.Label(self.root, text="Danh sách thành viên", font=("arial", 20, "bold"))
        self.header_label.pack(pady=20)  # Centering the label at the top
        
        # table Frame for Table
        table_frame = tk.Frame(self.root)
        table_frame.place(relwidth=0.9, relheight=0.75, relx=0.05, rely=0.1)
        
        # Scrollbars for Table
        y_scrollbar = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        self.table = ttk.Treeview(table_frame,
    columns=("cccd", "ho_ten", "nam_sinh", "cap_bac", "chuc_vu", "don_vi"),
    yscrollcommand=y_scrollbar.set)

        
        # Table (Treeview)
        self.table = ttk.Treeview(table_frame, columns=("cccd", "ho_ten", "nam_sinh", "cap_bac", "chuc_vu", "don_vi"), yscrollcommand=y_scrollbar.set)
        self.table.heading("cccd", text="CCCD")
        self.table.column("cccd", width=100, anchor="center")  # Adjust column width
        self.table.heading("ho_ten", text="Họ và Tên")
        self.table.column("ho_ten", width=150, anchor="center")
        self.table.heading("nam_sinh", text="Năm Sinh")
        self.table.column("nam_sinh", width=80, anchor="center")
        self.table.heading("cap_bac", text="Cấp Bậc")
        self.table.column("cap_bac", width=100, anchor="center")
        self.table.heading("chuc_vu", text="Chức Vụ")
        self.table.column("chuc_vu", width=120, anchor="center")
        self.table.heading("don_vi", text="Đơn Vị")
        self.table.column("don_vi", width=150, anchor="center")
        self.table["show"] = "headings"
        
        # Bố trí các widget
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Thanh cuộn ở bên phải
        self.table.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)  # Treeview bên trái

        
        
        
        # button frame
        button_frame = tk.Frame(self.root)
        button_frame.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.85)
        
        # Add button
        self.add_button = tk.Button(button_frame, text="Thêm")
        self.add_button.pack(side=tk.LEFT, padx=10)
        
        self.adds_button = tk.Button(button_frame, text="Thêm nhiều")
        self.adds_button.pack(side=tk.LEFT, padx=10)
        
        # Update button
        self.print_button = tk.Button(button_frame, text="Print")
        self.print_button.pack(side=tk.LEFT, padx=10)
        
        # Delete button
        self.delete_button = tk.Button(button_frame, text="Xóa")
        self.delete_button.pack(side=tk.LEFT, padx=10)
        
        # Search button
        self.search_combobox = ttk.Combobox(button_frame,text="chọn dữ liệu", values=["CCCD", "Họ và Tên", "Năm Sinh", "Cấp Bậc", "Chức Vụ", "Đơn Vị"])
        self.search_combobox.set("chọn dữ liệu")
        self.search_combobox.pack(side=tk.LEFT, padx=30)
        
        self.search_entry = tk.Entry(button_frame, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=10)
        self.search_button = tk.Button(button_frame, text="Tìm kiếm")
        self.search_button.pack(side=tk.LEFT, padx=10)
        
        self.exit_button = tk.Button(button_frame, text="Thoát")
        self.exit_button.pack(side=tk.LEFT, padx=30)
        
