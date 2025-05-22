from tkinter import Toplevel,messagebox
import sys
import webbrowser


from src.models.clan_model import ClanModel
from src.models.thanhvien_model import ThanhVienModel

from src.views.home_view import HomeView

from src.controllers.list_TV_Controller import ListTVController
from src.controllers.tt_controller import Hoi_controller

class HomeController:
    def __init__(self,root, userroot):
        self.root = root
        self.userroot = userroot
        self.view = HomeView(root)
        self.clanModel = ClanModel()
        self.thanhvienModel = ThanhVienModel()
        self.view.person_button.config(command=self.open_list)
        self.view.signoutbutton.config(command=self.on_exit)
        self.view. clan_button.config(command=self.open_TTHoi)
        self.view.feedback_button.config(command=self.phanhoi_controller)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        
        hoitruongData = self.thanhvienModel.Queries_hoitruong()
        self.view.cccd_label.config(text=f"CCCD: {hoitruongData[0][0]}")
        self.view.name_label.config(text =f"Họ và tên: {hoitruongData[0][1]}")
        self.view.age_label.config(text=f"Năm sinh:{hoitruongData[0][2]}")
        self.view.cb_label.config(text =f"Cấp bậc: {hoitruongData[0][3]}")
        self.view.cv_label.config(text=f"Chức vụ Hội:{hoitruongData[0][4]}")
        self.view.dv_label.config(text=f"Đơn vị:{hoitruongData[0][5]}")


        
    def open_TTHoi(self):
        self.root.withdraw()
        hoiroot = Toplevel(self.root)
        parent_geometry = self.view.root.geometry()
        Hoi_controller(hoiroot, self.root,parent_geometry)

    
    def open_list(self):
        self.root.withdraw()  # Ẩn cửa sổ chính
        listWindow = Toplevel(self.root)
        parent_geometry = self.view.root.geometry()
        ListTVController(listWindow,self.root, parent_geometry)
        
    def phanhoi_controller(self):
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    def on_exit(self):
        self.userroot.deiconify()  # Hiển thị cửa sổ đăng nhập
        self.root.destroy()  # Đóng cửa sổ chính
    def on_close(self):
        """
        Xử lý khi người dùng nhấn nút X.
        Hiển thị hộp thoại xác nhận trước khi đóng ứng dụng.
        """
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn kết thúc chương trình?"):
            sys.exit()  # Kết thúc toàn bộ chương trình
