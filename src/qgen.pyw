"""
A web search query generator for searching multiple sites at once.  

Currently queries are formatted for DuckDuckGo specifically, but they may work with other search engines as well.

"""

import pyperclip as pc
import customtkinter as ctk
from icecream import ic

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

def safesearch_event():
    """
    This function should not be run directly.

    Assign this function as a parameter to a ctk radiobutton object.

    """
    ic("Safesearch Radio toggled.  Current value: ", safe_search_var.get())

def generate_press():
    """
    
    This is the function that generates the actual query.
    
    This function should not be run directly for the purposes of this script.

    Assign this function as a parameter when initalizing a customtkinter
    button object.  The function will then run any time the button is pressed.
    """
    ic("Button Pressed - Generate Query")
    
    output.delete("0.0", "end")
    
    query = str(term_text.get())    # appends search text
    query = query.rstrip("\n")
    query += " "
    
    if site1_checkbox.get() == "on":
        query += "site:"
        query += site1_checkbox._text
        query += " OR "

    if site2_checkbox.get() == "on":
        query += "site:"
        query += site2_checkbox._text
        query += " OR "
        
    if site3_checkbox.get() == "on":
        query += "site:"
        query += site3_checkbox._text
        query += " OR "

    if site4_checkbox.get() == "on":
        query += "site:"
        query += site4_checkbox._text
        query += " OR "

    if site5_checkbox.get() == "on":
        query += "site:"
        query += site5_checkbox._text
        query += " OR "

    if site6_checkbox.get() == "on":
        query += "site:"
        query += site6_checkbox._text
        query += " OR "

    if site7_checkbox.get() == "on":
        query += "site:"
        query += site7_checkbox._text
        query += " OR "

    if site8_checkbox.get() == "on":
        query += "site:"
        query += site8_checkbox._text
        query += " OR "

    if site9_checkbox.get() == "on":
        query += "site:"
        query += site9_checkbox._text
        query += " OR "

    if site10_checkbox.get() == "on":
        query += "site:"
        query += site10_checkbox._text
        query += " OR "

    if site11_checkbox.get() == "on":
        query += "site:"
        query += site11_checkbox._text
        query += " OR "

    if site12_checkbox.get() == "on":
        query += "site:"
        query += site12_checkbox._text
        query += " "

    ic(query)
    query = query.rstrip(" ")
    query = query.rstrip("OR")

    ic(query)

    output.insert("0.0", query)


def copy_clip():
    """
    
    Copies data to clipboard on button press.
    This function should not be run directly for the purposes of this script.

    Assign this function as a parameter when initalizing a customtkinter
    button object.  The function will then run any time the button is pressed.
    """
    ic("Button Pressed - Copy to Clipboard")
    text = output.get("1.0", "end")
    pc.copy(text)
    ic(text)
    #pc.paste()


# Set up ctk object
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.title("query-gen")
app.geometry("750x500")
app.resizable(False, False)

# App icon
# This code is unusual, but seems to be the only thing that currently
# works with customtkinter.
# See https://github.com/TomSchimansky/CustomTkinter/discussions/1099
app.after(1, lambda :app.iconbitmap("qgen_logo128x128.ico"))

# Font object for labels
label_font = ctk.CTkFont(family="Georgia", size=16, weight="bold")


# Search term frame
term_frame = ctk.CTkFrame(app)
term_frame.configure(border_width=1, border_color="lightgreen")
term_frame.grid(sticky="w", row=0, column=0, padx=20, pady=5)

# Search term label
term_label = ctk.CTkLabel(term_frame, text="Search term:", font=label_font)
term_label.grid(sticky="w", padx=20, pady=20, row=0, column=0)

# Search term field
term_text = ctk.CTkEntry(
    term_frame,
    width=300, 
    height=30, 
)
term_text.grid(sticky="e", padx=20, pady=20, row=0, column=1)

# Safesearch radio frame
safe_search_frame = ctk.CTkFrame(app)
safe_search_frame.configure(border_width=1, border_color="lightgreen")
safe_search_frame.grid(sticky="w", padx=0, pady=5, row=0, column=1)

# Safesearch label
safe_search_label = ctk.CTkLabel(safe_search_frame, text="SafeSearch:",
    font=label_font)
safe_search_label.grid(sticky="w", padx=20, pady=10, row=0, column=0)

# Safesearch ratio buttons

safe_search_var = ctk.IntVar(value=1)

safe_search_on = ctk.CTkRadioButton(
    safe_search_frame,
    text="On",
    command=safesearch_event,
    variable=safe_search_var,
    value=1
)
safe_search_on.grid(padx=5, pady=5, row=1, column=0)

safe_search_off = ctk.CTkRadioButton(
    safe_search_frame,
    text="Off",
    command=safesearch_event,
    variable=safe_search_var,
    value=2
)
safe_search_off.grid(padx=5, pady=5, row=1, column=1)

# Checkbox frame
cb_frame = ctk.CTkFrame(app)
cb_frame.configure(border_width=1, border_color="lightgreen")
cb_frame.grid(sticky="w", row=1, column=0, padx=20, pady=5)
#cb_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
#cb_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

# Checkbox label
cb_label = ctk.CTkLabel(cb_frame, text="Select the sites you want to search:", font=label_font)
cb_label.grid(sticky="w", padx=20, pady=20, row=0, column=0)

# Checkboxes

# site1
site1_check = ctk.StringVar(value="on")
site1_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="stackexchange.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site1_check,
    onvalue="on",
    offvalue="off",
)
site1_checkbox.grid(sticky="w", row=1, column=0, padx=8, pady=10)

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
site2_checkbox.grid(sticky="w", row=1, column=1, padx=8, pady=10)

# site3
site3_check = ctk.StringVar(value="on")
site3_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="twitter.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site3_check,
    onvalue="on",
    offvalue="off",
)
site3_checkbox.grid(sticky="w", row=1, column=2, padx=8, pady=10)

# site4
site4_check = ctk.StringVar(value="on")
site4_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="npr.org", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site4_check,
    onvalue="on",
    offvalue="off",
)
site4_checkbox.grid(sticky="w", row=1, column=3, padx=8, pady=10)

# site5
site5_check = ctk.StringVar(value="on")
site5_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="news.ycombinator.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site5_check,
    onvalue="on",
    offvalue="off",
)
site5_checkbox.grid(sticky="w", row=2, column=0, padx=8, pady=10)

# site6
site6_check = ctk.StringVar(value="on")
site6_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="restofworld.org", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site6_check,
    onvalue="on",
    offvalue="off",
)
site6_checkbox.grid(sticky="w", row=2, column=1, padx=8, pady=10)

# site7
site7_check = ctk.StringVar(value="on")
site7_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="ft.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site7_check,
    onvalue="on",
    offvalue="off",
)
site7_checkbox.grid(sticky="w", row=2, column=2, padx=8, pady=10)

# site8
site8_check = ctk.StringVar(value="on")
site8_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="propublica.org", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site8_check,
    onvalue="on",
    offvalue="off",
)
site8_checkbox.grid(sticky="w", row=2, column=3, padx=8, pady=10)

# site9
site9_check = ctk.StringVar(value="on")
site9_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="developer.mozilla.org", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site9_check,
    onvalue="on",
    offvalue="off",
)
site9_checkbox.grid(sticky="w", row=3, column=0, padx=8, pady=10)

# site10
site10_check = ctk.StringVar(value="on")
site10_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="youtube.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site10_check,
    onvalue="on",
    offvalue="off",
)
site10_checkbox.grid(sticky="w", row=3, column=1, padx=8, pady=10)

# site11
site11_check = ctk.StringVar(value="on")
site11_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="amazon.com", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site11_check,
    onvalue="on",
    offvalue="off",
)
site11_checkbox.grid(sticky="w", row=3, column=2, padx=8, pady=10)

# site12
site12_check = ctk.StringVar(value="on")
site12_checkbox = ctk.CTkCheckBox(
    cb_frame,
    text="docs.python.org", #change this text to customize which sites to search
    command=checkbox_event,
    variable=site12_check,
    onvalue="on",
    offvalue="off",
)
site12_checkbox.grid(sticky="w", row=3, column=3, padx=8, pady=10)

# Button to generate query
gen_button = ctk.CTkButton(app, text="Generate Query", command=generate_press)
gen_button.grid(sticky="we", row=2, column=0, padx=10, pady=10)

# Output frame
out_frame = ctk.CTkFrame(app)
out_frame.configure(border_width=1, border_color="lightgreen")
out_frame.grid(sticky="w", row=3, column=0, padx=20, pady=5)

# Output label
out_label = ctk.CTkLabel(out_frame, text="Your query:", font=label_font)
out_label.grid(sticky="w", padx=20, pady=20, row=1)

# Query output
output = ctk.CTkTextbox(
    out_frame,
    width=350,
    height=100
)
output.grid(sticky="w", padx=2, pady=20, row=1, column=1)

# Button to copy to clipboard
clip = ctk.CTkButton(out_frame, text="Copy to clipboard", command=copy_clip)
clip.grid(sticky="ew", row=1, column=2, padx=10, pady=10)

#ic(site1_checkbox._text)

# Start ctk window
app.mainloop()

