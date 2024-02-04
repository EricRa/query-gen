"""
A web search query generator

"""

import subprocess
import sys

import customtkinter as ctk
from icecream import ic

query = ""


def checkbox_event():
    """
    This function should not be run directly.

    Assign this function as a parameter to a ctk checkbox object.
    The function will run when the checkbox is activated from the GUI
    """

    ic(site1_checkbox.get())
    ic(site2_checkbox.get())
    ic(site3_checkbox.get())
    ic(site4_checkbox.get())
    ic(site5_checkbox.get())
    ic(site6_checkbox.get())
    ic(site7_checkbox.get())
    ic(site8_checkbox.get())
    ic(site9_checkbox.get())
    ic(site10_checkbox.get())
    ic(site11_checkbox.get())
    ic(site12_checkbox.get())

def generate_press():
    """
    This function should not be run directly for the purposes of this script.

    Assign this function as a parameter when initalizing a customtkinter
    button object.  The function will then run any time the button is pressed.
    """
    
    

# Set up ctk object
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.title("query-gen")
app.geometry("700x500")
app.resizable(False, False)
#app.grid_columnconfigure(0, weight=1)
#app.grid_rowconfigure(0, weight=1)


# Search term frame
term_frame = ctk.CTkFrame(app)
term_frame.configure(border_width=1, border_color="lightgreen")
term_frame.grid(sticky="w", row=0, column=0, padx=20, pady=5)

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

# Button to generate query


# Checkbox frame
cb_frame = ctk.CTkFrame(app)
cb_frame.configure(border_width=1, border_color="lightgreen")
cb_frame.grid(sticky="w", row=1, column=0, padx=20, pady=5)
#cb_frame.grid_columnconfigure((0), weight=1)

# Checkbox label
cb_label = ctk.CTkLabel(cb_frame, text="Select the sites you want to search:")
cb_label.grid(sticky="w", padx=20, pady=20, row=0, column=0)

# Checkboxes

# site1
site1_check = ctk.StringVar(value="on")
site1_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site1_check,
    onvalue="on",
    offvalue="off",
)
site1_checkbox.grid(sticky="w", row=1, column=0, padx=20, pady=10)

# site2
site2_check = ctk.StringVar(value="on")
site2_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site2_check,
    onvalue="on",
    offvalue="off",
)
site2_checkbox.grid(sticky="w", row=1, column=1, padx=20, pady=10)

# site3
site3_check = ctk.StringVar(value="on")
site3_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site3_check,
    onvalue="on",
    offvalue="off",
)
site3_checkbox.grid(sticky="w", row=1, column=2, padx=20, pady=10)

# site4
site4_check = ctk.StringVar(value="on")
site4_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site4_check,
    onvalue="on",
    offvalue="off",
)
site4_checkbox.grid(sticky="w", row=1, column=3, padx=20, pady=10)

# site5
site5_check = ctk.StringVar(value="on")
site5_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site5_check,
    onvalue="on",
    offvalue="off",
)
site5_checkbox.grid(sticky="w", row=2, column=0, padx=20, pady=10)

# site6
site6_check = ctk.StringVar(value="on")
site6_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site6_check,
    onvalue="on",
    offvalue="off",
)
site6_checkbox.grid(sticky="w", row=2, column=1, padx=20, pady=10)

# site7
site7_check = ctk.StringVar(value="on")
site7_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site7_check,
    onvalue="on",
    offvalue="off",
)
site7_checkbox.grid(sticky="w", row=2, column=2, padx=20, pady=10)

# site8
site8_check = ctk.StringVar(value="on")
site8_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site8_check,
    onvalue="on",
    offvalue="off",
)
site8_checkbox.grid(sticky="w", row=2, column=3, padx=20, pady=10)

# site9
site9_check = ctk.StringVar(value="on")
site9_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site9_check,
    onvalue="on",
    offvalue="off",
)
site9_checkbox.grid(sticky="w", row=3, column=0, padx=20, pady=10)

# site10
site10_check = ctk.StringVar(value="on")
site10_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site10_check,
    onvalue="on",
    offvalue="off",
)
site10_checkbox.grid(sticky="w", row=3, column=1, padx=20, pady=10)

# site11
site11_check = ctk.StringVar(value="on")
site11_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site11_check,
    onvalue="on",
    offvalue="off",
)
site11_checkbox.grid(sticky="w", row=3, column=2, padx=20, pady=10)

# site12
site12_check = ctk.StringVar(value="on")
site12_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="reddit.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site12_check,
    onvalue="on",
    offvalue="off",
)
site12_checkbox.grid(sticky="w", row=3, column=3, padx=20, pady=10)

# Output frame
out_frame = ctk.CTkFrame(app)
out_frame.configure(border_width=1, border_color="lightgreen")
out_frame.grid(sticky="w", row=2, column=0, padx=20, pady=5)

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
#ic(site1_checkbox._text)

# Start ctk window
app.mainloop()