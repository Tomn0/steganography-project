import tkinter as tk
from tkinter import ttk, filedialog
from utils import *
from pathlib import Path
from .decode import *

select_clicked = False

FILEOPENOPTIONS = dict(defaultextension=".pdf", 
                       initialdir="/",
                       filetypes=[('pdf file', '*.pdf')])


def init(parent):
    global word_shift_tab

    word_shift_tab = ttk.Frame(parent)
    parent.add(word_shift_tab, text="Line shift - Decode")

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


def decode(file: tk.StringVar = None): #Placeholder for now - Will have to include normal decoding
    if file is None:
        print('No input file provided, returning default message...')
        text_box = tk.Text(word_shift_tab)
        text_box.insert(tk.INSERT, "No to idziemy na Destiny")
        text_box.pack()
    else:
        file_path = file.get()
        print(f'Path to input pdf: {file_path}')

        page_count = get_page_count(file_path)
        print(f'Total pages in the document: {page_count}')
        
        print('Processing input text...')
        informations = []
        for page_idx in range(page_count):
            page_inf = get_line_spacing(file_path, page_idx)
            informations += page_inf

        print(f'All information from text: {informations}')
        
        chunked_inf = split_list(informations, 8) # Assume we are operating on 8-bit symbols
        print(chunked_inf)

        msg = ""
        print('Transforming bits into information...')
        for bits_seq in chunked_inf:
            msg += bits_to_symbol(bits_seq)

        print(f'Decoded message: {msg}')
        text_box = tk.Text(word_shift_tab)
        text_box.insert(tk.INSERT, msg)
        text_box.pack()