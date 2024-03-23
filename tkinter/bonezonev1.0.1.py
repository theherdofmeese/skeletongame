# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:35:23 2024

@author: thehe
"""

import tkinter as tk
import random

class TheBoneZone(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Bone Zone")
        self.geometry("800x600")
        self.create_start_page()

    def create_start_page(self):
        self.config(bg='#7C5E8C')
        tk.Label(self, text="The BONE ZONE", bg="#1E90FF", 
                 fg="white", font=('Helvetica', 32, "bold")).pack(pady=50) 

        tk.Button(self, text="Begin", bg="#FFFACD", font=('sans-serif', 22, "bold"), 
                  command=self.create_options_page).pack(pady=50) 

    def create_options_page(self):
        for widget in  self.winfo_children():
            widget.destroy()
        self.config(bg='#8c8878')
        tk.Label(self, text="What would you like to do?:", bg="#ADD8E6", 
				font=('Verdana', 16)).pack(pady=20)
        # Add code for creating the options page here
        options = [("loot"),("heal"),("explore")]
        self.selected_option = tk.IntVar()
        for option in options:
            tk.Radiobutton(self, text=option,bg='8c8878', font = (
                'Times New Roman',20).pack.pady(20)
                #command=self.create_combat_page)
                
if __name__ == '__main__':
    app = TheBoneZone() 
    app.mainloop()
