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
app.geometry("700x500")
app.resizable(False, False)
#app.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)


# Search term frame
term_frame = ctk.CTkFrame(app)
term_frame.grid(sticky="w", row=0, column=0, padx=20, pady=20)

# Search term label
term_label = ctk.CTkLabel(term_frame, text="Search term:")
term_label.grid(sticky="w", padx=20, pady=20, row=0, column=0)

# Search term field
term_text = ctk.CTkTextbox(
    term_frame,
    width=300, 
    height=30, 
    activate_scrollbars=False,
    wrap="none"
)
term_text.grid(sticky="w", padx=20, pady=20, row=0, column=1)

# Checkbox frame
#cb_frame = ctk.CTkFrame(app)
#cb_frame = 

# Output frame
out_frame = ctk.CTkFrame(app)
out_frame.grid(sticky="w", row=1, column=0, padx=20, pady=20)

# Output label
out_label = ctk.CTkLabel(out_frame, text="Your query:")
out_label.grid(sticky="w", padx=20, pady=20, row=1)

# Query output
output = ctk.CTkTextbox(
    out_frame,
    width=400,
    height=100
)
output.grid(sticky="w", padx=20, pady=20, row=1, column=1)

# Start ctk window
app.mainloop()