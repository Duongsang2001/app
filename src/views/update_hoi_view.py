import tkinter as tk
from tkinter import ttk

from src.views.hoi_view import TTHoi 

class UpdateHoi(TTHoi):
    def __init__(self, root, parent_geometry):
        super().__init__(root, parent_geometry)

        self.name_entry = tk.Entry(self.tthoi_frame, width=20, font=("arial",16 ))
        self.name_entry.place(x=150, y=10)


        self.htsxnv_entry = tk.Entry(self.tt_frame, width=5, font =("aria", 16))
        self.htsxnv_entry.place(x=120, y=55)

        self.httnv_entry = tk.Entry(self.tt_frame, width=5, font =("aria", 16))
        self.httnv_entry.place(x=350, y=55)

        self.htnv_entry = tk.Entry(self.tt_frame, width=5, font =("aria", 16))
        self.htnv_entry.place(x=580, y=55)

        self.khtnv_entry = tk.Entry(self.tt_frame, width=5, font =("aria", 16))
        self.khtnv_entry.place(x=810, y=55)
        

        self.note_text.config(state="normal")

        self.exit_button.config(text ="Đóng")

    def get_nv(self):
        return[
            self.htsxnv_entry.get(),
            self.httnv_entry.get(),
            self.htnv_entry.get(),
            self.khtnv_entry.get()
        ]