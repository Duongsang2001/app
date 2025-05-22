from tkinter import Toplevel, messagebox

import sys

from src.models.clan_model import ClanModel
from src.models.thanhtich_nam_model import ThanhtichNamModel
from src.models.thanhtich_model import ThanhtichModel
from src.models.thanhvien_model import ThanhVienModel

from src.views.hoi_view import TTHoi
from src.views.update_hoi_view import UpdateHoi
class Hoi_controller:
    def __init__(self, root, homeroot, parent):
        self.root= root
        self.homeroot = homeroot
        self.parent = parent
        self.clanmodel = ClanModel()
        self.thanhtichmodel = ThanhtichModel()
        self.thanhtichnammodel = ThanhtichNamModel()
        self.thanhvienmodel = ThanhVienModel()
        self.view = TTHoi(self.root, parent)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.view.exit_button.config(command=self.on_exit)
        self.view.update_button.config(command=self.update_hoi)
        self.update_tt()


    def update_tt(self):
        name = self.clanmodel.get_nameHoi()
        thanhvien = self.thanhvienmodel.count_thanhvien()
        print(str(thanhvien))
        data_thanhtich = self.thanhtichmodel.get_thanhtich()
        self.view.name_hoi_label.config(text=f"Tên hội:"+name )
        self.view.name_thanhvien_label.config(text=f"Thành viên: "+ str(thanhvien))
        self.view.htsxnv_label.config(text=f"HTXSNV:{data_thanhtich[0][0]}")
        self.view.httnv_label.config(text=f"HTTNV:{data_thanhtich[0][1]}")
        self.view.htnv_label.config(text=f"HTNV:{data_thanhtich[0][2]}")
        self.view.khtnv_label.config(text=f"KHTNV:{data_thanhtich[0][3]}")
        self.view.nam_combobox.bind("<<ComboboxSelected>>", self.on_combobox_select)

    
    def on_combobox_select(self, event):
        select_value = self.view.nam_combobox.get()
        text = self.thanhtichnammodel.note_thanhtich(select_value)
        print(str(text))
        self.view.note_text.config(state="normal")
        self.view.note_text.delete("1.0", "end")
        self.view.note_text.insert("1.0", str(text))
        self.view.note_text.config(state="disabled")


    def update_hoi(self):
        updateroot = Toplevel(self.root)
        upDateHoi = UpdateHoi(updateroot, self.parent)
        self.root.withdraw()
       

        def update_data_hoi():
            name = upDateHoi.name_entry.get()
            if name:
                self.clanmodel.update_name(name)

            sx,t,nv,kht = upDateHoi.get_nv()
            if all([sx,t,nv,kht]):
                self.thanhtichmodel.update_thanhtich(sx,t,nv,kht)
            self.update_tt()
            on_exit_update()
        def on_exit_update():
            updateroot.destroy()
            self.root.deiconify()
        

        upDateHoi.exit_button.config(command=on_exit_update)
        upDateHoi.update_button.config(command=update_data_hoi)

    def on_exit(self):
        self.homeroot.deiconify()
        self.root.destroy()
        
    def on_close(self):
        """
        Xử lý khi người dùng nhấn nút X.
        Hiển thị hộp thoại xác nhận trước khi đóng ứng dụng.
        """
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn kết thúc chương trình?"):
            sys.exit()  # Kết thúc toàn bộ chương trình()
