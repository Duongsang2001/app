from tkinter import Toplevel, messagebox
from tkinter import filedialog

import sys
from docx import Document


from src.models.thanhvien_model import ThanhVienModel
from src.views.list_thanhvien_view import ListTVView
from src.views.add_thanhvien_view import AddThanhVienView

class ListTVController:
    def __init__(self, root,homeRoot, parent):
        self.parent = parent
        self.root = root
        self.homeRoot = homeRoot
        self.model = ThanhVienModel()
        self.view = ListTVView(self.root, parent)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.view.exit_button.config(command=self.on_exit)
        self.view.add_button.config(command=self.add_person)
        self.view.delete_button.config(command=self.delete_person)
        self.view.search_button.config(command=self.search_list)
        self.view.adds_button.config(command=self.open_file)
        self.view.print_button.config(command=self.print_list)
        self.load_data_to_table()
        
    
    def load_data_to_table(self):
        for item in self.view.table.get_children():  # Lấy tất cả các ID mục
            self.view.table.delete(item)  # Xóa từng mục

        data = self.model.get_all_thanhvien()
        for record in data:
            self.view.table.insert("", "end", values=record)


    def add_person(self):
        add_root = Toplevel(self.root)
        addThanhVienView = AddThanhVienView(add_root)
        
        def add():
            cccd,name,namsinh,cb,cv,dv = addThanhVienView.add_thanhvien()
            if not cccd or not name or not namsinh or not cb or not cv or not dv:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
                return
            self.model.add_thanhvien(cccd,name,namsinh,cb,cv,dv)
            self.load_data_to_table()
            add_root.destroy()
            
        addThanhVienView.add_btn.config(command=add)
        
    def search_list(self):
        column = self.view.search_combobox.get()
        value = self.view.search_entry.get().lower()
        if not column or not value:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return
        column_map = {
            "CCCD": "cccd",
            "Họ và Tên": "fullname",
            "Năm Sinh": "nam_sinh",
            "Cấp Bậc": "cb",
            "Chức Vụ": "cvh",
            "Đơn Vị": "dv",
        }
        search_column = column_map.get(column)
        if not search_column:
            messagebox.showerror("Lỗi", "Cột tìm kiếm không hợp lệ")
            return
        data = self.model.search_thanhvien(search_column, value.lower())
        for item in self.view.table.get_children():
            self.view.table.delete(item)
    # Kiểm tra kết quả
        if not data:
            messagebox.showinfo("Thông báo", "Không tìm thấy kết quả nào")
            return
    # Hiển thị kết quả lên bảng
        for record in data:
            self.view.table.insert("", "end", values=record)

    
    
    def open_file(self):
         # Hiển thị giao diện chọn file
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Excel files", "*.xlsx *.xls")]
            )
        except Exception as e:
            print(f"Lỗi xảy ra: {e}")
        
        if file_path:
            print("mở thành công")

    def print_list(self):
        selected_item_open = self.view.table.selection()
        if not selected_item_open:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một hàng để xóa.")
            return
        values_open = self.view.table.item(selected_item_open[0], "values")
        if not values_open:
            messagebox.showerror("Lỗi", "Không thể lấy dữ liệu từ hàng được chọn.")
            return
        print(values_open)
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("word files", "*.docx *.doc")]
            )
        except Exception as e:
            print(f"Lỗi xảy ra: {e}")
        
        if file_path:
            doc = Document(file_path)
            data = {
                "CCCD:":0,
                "Họ và tên:":1,
                "Năm sinh:":2,
                "Cấp bậc:":3,
                "Chức vụ hội:":4,
                "Đơn vị:":5
            }
            for para in doc.paragraphs:
                for key, value in data.items():
                    if key in para.text:
                        para.text = para.text +" "+values_open[int(value)]
        doc.save(file_path)
    
    def delete_person(self):
        selected_item = self.view.table.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một hàng để xóa.")
            return

    # Lấy giá trị của hàng được chọn
        values = self.view.table.item(selected_item[0], "values")
        if not values:
            messagebox.showerror("Lỗi", "Không thể lấy dữ liệu từ hàng được chọn.")
            return

        cccd = values[0] 
        self.model.delete_person_model(cccd)
        self.load_data_to_table()
        messagebox.showinfo("Thành công", "Xóa thành công.")
        
    
    def on_exit(self):
        self.homeRoot.deiconify()
        self.root.destroy()
        
    def on_close(self):
        """
        Xử lý khi người dùng nhấn nút X.
        Hiển thị hộp thoại xác nhận trước khi đóng ứng dụng.
        """
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn kết thúc chương trình?"):
            sys.exit()  # Kết thúc toàn bộ chương trình()
