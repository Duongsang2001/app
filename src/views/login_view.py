import tkinter as tk


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")
        
        def center_window(window, width, height):
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x = (screen_width // 2) - (width // 2)
            y = (screen_height // 2) - (height // 2)
            window.geometry(f"{width}x{height}+{x}+{y}")
        center_window(self.root, 400, 300)
        
        self.root.configure(background="#f5f5f5")

        self.frame = tk.Frame(root, bg="#33CCFF")
        self.frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        self.logo = tk.Label(root, text="🌟 Login Portal 🌟", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333")
        self.logo.pack(pady=10)

        self.username_label = tk.Label(root, text="Tên đăng nhập:", bg="#f5f5f5", font=("Arial", 12), fg="#555")
        self.username_label.pack()
        self.username_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(root, text="Mật khẩu:", bg="#f5f5f5", font=("Arial", 12), fg="#555")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(root, text="Đăng nhập", bg="#4CAF50", fg="white", font=("Arial", 12), width=10)
        self.login_button.pack(pady=10)

        self.register_button = tk.Button(root, text="Đăng ký", bg="#2196F3", fg="white", font=("Arial", 12), width=10)
        self.register_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", bg="#f5f5f5", font=("Arial", 12), fg="red")
        self.result_label.pack(pady=10)