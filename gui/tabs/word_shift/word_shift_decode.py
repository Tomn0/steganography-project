import tkinter as tk
from tkinter import ttk, filedialog
from utils import *
from .decode import *

select_clicked = False

FILEOPENOPTIONS = dict(defaultextension=".pdf", 
                       initialdir="/",
                       filetypes=[('pdf file', '*.pdf')])


def init(parent):
    global word_shift_tab

    word_shift_tab = ttk.Frame(parent)
    parent.add(word_shift_tab, text="Word shift - Decode")

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
        command=lambda: process_data(file),
        state="normal"
    )

    execute_shift.pack()    


def process_data(file: tk.StringVar = None):
    status = ""
    if file is None:
        status = 'No input file provided, returning default message...'
        msg = "No to idziemy na Destiny"
    else:
        file_path = file.get()
        print(f'Path to input pdf: {file_path}')

        page_count = get_page_count(file_path)
        print(f'Total pages in the document: {page_count}')
        
        print('Processing input text...')
        informations = decode(get_word_spacing(file_path))
        print(f'All information from text: {informations}')
        
        chunked_inf = split_list(informations, 8) # Assume we are operating on 8-bit symbols
        print(chunked_inf)

        msg = ''
        print('Transforming bits into information...')
        for bits_seq in chunked_inf:
            msg += bits_to_symbol(bits_seq)

        status = 'Message decoding went successfully.'
        print(f'Decoded message: {msg}')

    status_label = create_status_popup(word_shift_tab, status)
    status_label.pack()

    text_box = tk.Text(word_shift_tab)
    text_box.insert(tk.INSERT, msg)
    text_box.pack()