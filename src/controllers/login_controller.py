from tkinter import Toplevel, messagebox

#model
import sqlite3
from src.models.user_model import UserModel
from src.models.clan_model import ClanModel

#views
from src.views.login_view import LoginView
from src.views.register_view import RegisterView

#controllers
from src.controllers.home_controller import HomeController

class LoginController:
    def __init__(self, root):
        self.root = root
        self.view = LoginView(self.root)
        self.model = UserModel()
        self.clanmodel = ClanModel()
        self.view.login_button.config(command=self.login)
        self.view.register_button.config(command=self.open_register)
        
        
        
    def login(self):
        account = self.view.username_entry.get()
        password = self.view.password_entry.get()
        user = self.model.login_user(account, password)
        if user:
            self.open_home()
        else:
            messagebox.showerror("login","Nhập sai tài khoản hoặc mật khẩu!")
    
    def open_register(self):
        parent_geometry = self.view.root.geometry()
        register_window = Toplevel(self.view.root)
        register_view = RegisterView(register_window, parent_geometry)
        
        def submit_register():
            username,email,password, confirm_password = register_view.get_inputs()
            if not username or not email or not password or not confirm_password:
                messagebox.showerror("register","vui lòng nhập đầy đủ thông tin")
                return
            if password != confirm_password:
                messagebox.showerror("register","Mật khẩu không trùng nhau")
                return
            try:
                self.model.register_user(username, email, password)
                register_window.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror("register","Tài khoản chưa được tạo!")
        
        register_view.submit_button.config(command=submit_register)
    
    def open_home(self):
        self.root.withdraw()    
        homeWindow = Toplevel(self.view.root)  # Tạo cửa sổ Home
        HomeController(homeWindow, self.root)  # Chuyển sang HomeController
        
            
    
        