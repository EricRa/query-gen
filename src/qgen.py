"""
A web search query generator

"""

import subprocess
import sys

import customtkinter as ctk
from icecream import ic

query = ""

# Set up ctk object
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.title("query-gen")
app.geometry("600x400")
app.resizable(False, False)
app.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

# Search term label
term_label = ctk.CTkLabel(app, text="Search Term:")
term_label.grid(sticky="w", padx=20, pady=20, row=0, column=0)

# Search term field
term_text = ctk.CTkTextbox(
    app,
    width =300, 
    height=30, 
    activate_scrollbars=False,
    wrap="none"
)
term_text.grid(sticky="w", padx=20, pady=20, row=0, column=1)


# Start ctk window
app.mainloop()