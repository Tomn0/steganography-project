import tkinter as tk
from tkinter import ttk, filedialog
from utils import *

selected_directory = ""

def init(parent):
    word_shift_tab = ttk.Frame(parent)
    parent.add(word_shift_tab, text="Word shift coding")
    global selected_directory

    select_location_button = ttk.Button(word_shift_tab, text="Select save location", command=call_directory_finder)
    select_location_button.pack(pady=10)

    directory_label = ttk.Label(word_shift_tab, text="Selected Directory:\n")
    directory_label.pack(pady=10)
    directory_label.config(text=f"Selected Directory: {selected_directory}")

    message_label = ttk.Label(word_shift_tab, text="Message to encode")
    message_label.pack()
    text_input = create_text_input_field(word_shift_tab)

    files = create_files_dropdown(word_shift_tab)

    execute_shift = ttk.Button(
        word_shift_tab,
        text="Encode",
        command=lambda: print('XD'),
        state="normal"
    )
    execute_shift.pack()
    

def call_directory_finder(): # We choose pdf that we want to encode based on our text
    selected_directory = filedialog.askdirectory()
