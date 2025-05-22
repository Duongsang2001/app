import tkinter as tk

class RegisterView:
    def __init__(self, root, parent_geometry):
        self.root = root
        self.root.title("register")
        self.root.geometry(parent_geometry)

        self.frame = tk.Frame(root, bg="#33CCFF")
        self.frame.place(relwidth=1, relheight=1, relx=0, rely=0)
        
        self.createUser_label = tk.Label(root, text="Tạo tài khoản", font=("arial", 20, "bold"))
        self.createUser_label.pack(pady=5)

        tk.Label(root, text = "New Username:").pack()
        self.new_username_entry = tk.Entry(root)
        self.new_username_entry.pack(pady=5)
        
        tk.Label(root, text="Email:").pack()
        self.new_email_entry = tk.Entry(root)
        self.new_email_entry.pack(pady=5)
        
        
        tk.Label(root, text="password:").pack()
        self.new_password_entry = tk.Entry(root)
        self.new_password_entry.pack(pady=5)
        
        tk.Label(root, text="Confirm Password:").pack()
        self.confirm_password_entry = tk.Entry(root)
        self.confirm_password_entry.pack(pady=5)
        
        self.submit_button = tk.Button(root, text="submit")
        self.submit_button.pack(pady=5)
        
    def get_inputs(self):
            return(
                self.new_username_entry.get(),
                self.new_email_entry.get(),
                self.new_password_entry.get(),
                self.confirm_password_entry.get()
            )