import tkinter as tk
from tkinter import ttk, filedialog
from utils import *

select_clicked = False

FILEOPENOPTIONS = dict(defaultextension=".pdf", 
                       initialdir="/",
                       filetypes=[('pdf file', '*.pdf')])


def init(parent):
    global word_shift_tab

    word_shift_tab = ttk.Frame(parent)
    parent.add(word_shift_tab, text="Word shift - Decode")

    select_location_button = ttk.Button(word_shift_tab, text="Select font", command=call_font_finder)
    select_location_button.pack(pady=10)

    select_location_button = ttk.Button(word_shift_tab, text="Select PDF file", command=call_file_finder)
    select_location_button.pack(pady=10)
    

def call_file_finder(): # We choose pdf that we want to encode based on our text
    selected_file = filedialog.askopenfilename(**FILEOPENOPTIONS)
    file = tk.StringVar()
    file.set(selected_file)
    print(f'File: {file.get()}')

    file_label = ttk.Label(word_shift_tab)
    file_label.config(text=f"Selected File: {file.get()}")
    file_label.pack(pady=10)

    execute_shift = ttk.Button(
        word_shift_tab,
        text="Decode",
        command=lambda: decode(file),
        state="normal"
    )

    execute_shift.pack()    


def call_font_finder():
    global select_clicked
    selected_font = filedialog.askopenfilename()
    print(f'Font file: {selected_font}')

    font = tk.StringVar()
    font.set(selected_font)
    font_label = ttk.Label(word_shift_tab, textvariable=font)

    font_label = ttk.Label(word_shift_tab)
    font_label.config(text=f"Selected font: {font.get()}")
    font_label.pack(pady=10)


def decode(file: ttk.Label = None): #Placeholder for now - Will have to include normal decoding
    decrypted = "Placeholder"

    print(f'Decoded information: {decrypted}')
    text_box = tk.Text(word_shift_tab)
    text_box.insert(tk.INSERT, decrypted)
    text_box.pack()


def send_file_path(file: ttk.Label):
    return file.cget('text')