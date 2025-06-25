import tkinter as tk
import sys
import random

but_loc_x = [200, 600, 1000]
but_loc_y = [200, 350, 600]

def copy():
    new_window = tk.Toplevel(box)
    new_window.title("CRY ABOUT IT.")
    new_window.geometry("1200x800")

    label = tk.Label(new_window, text="AWWW TOO BAD", font=("Arial", 23))
    label.pack(pady=50)

    btn_generate = tk.Button(new_window, text="""ALRIGHT FINE YOU CAN LEAVE NOW:( """, width=65, height=7, command=copy)
    btn_generate.pack(pady=50)
    btn_generate.place(x=600, y=350, anchor=tk.CENTER)

    btn_generate.bind("<Enter>", lambda event: button_hover(event, btn_generate, new_window))
    
    new_window.protocol("WM_DELETE_WINDOW", on_close)
    new_window.bind("q", exit_program)

def on_close():
    copy()

def exit_program(event):
    sys.exit()

def button_hover(event, btn, window=None):
    btn_pos_x = random.choice(but_loc_x)
    btn_pos_y = random.choice(but_loc_y)
    btn.place_configure(x=btn_pos_x, y=btn_pos_y)

    if window is not None:
        copy()

box = tk.Tk()
box.title("TOOO BADDDDDDD")
box.geometry("1200x800")
box.resizable(False, False)

title_label = tk.Label(box, text="CRYBABY", font=("Arial", 23))
title_label.pack(pady=50)

but_generate = tk.Button(box, text="IDK ANYMORE", width=65, height=7, command=copy)
but_generate.pack(pady=50)
but_generate.place(x=600, y=350, anchor=tk.CENTER)

but_generate.bind("<Enter>", lambda event: button_hover(event, but_generate))

box.protocol("WM_DELETE_WINDOW", on_close)
box.bind("q", exit_program)

box.mainloop()
