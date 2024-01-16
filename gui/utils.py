import os
import tkinter as tk
from tkinter import ttk, scrolledtext
import fitz

def create_input(tab, input_label: str, entry_type: str = 'input'):
    label = ttk.Label(tab, text=input_label)
    label.pack()

    if entry_type == 'input':
        entry = ttk.Entry(tab)

    entry.pack()
    return entry


def create_text_input_field(tab):
    text_input = scrolledtext.ScrolledText(tab, wrap=tk.WORD, width=40, height=15)
    text_input.pack(pady=20)
    return text_input


def list_files_directory(dir_path: str = '/Users/lukaszsochacki/Desktop/Studia/Steganografia/steganography-project/data'):
    res = []
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    return res


def create_files_dropdown(tab):
    files = list_files_directory()
    
    file_label = ttk.Label(tab, text = "Select file to encode in :")
    n = tk.StringVar() 
    file_choosen = ttk.Combobox(tab, width = 27,  textvariable = n) 
    
    # Adding combobox drop down list 
    file_choosen['values'] = files 
    
    # Shows february as a default value 
    file_label.pack()

    file_choosen.pack() 
    file_choosen.current(1) 
    return file_choosen


def msg_to_bits(msg: str) -> list[str]: # We assume that each symbol will be represented by 8 bits
    res = []
    for s in msg:
        if s.isalnum():
            bits = bin(ord(s))[2:]
            bits = '0'*(8 - len(bits)) + bits
            res.append(bits)
    return res


def split_list(input_list, n): #Splitting input array into chunks of length n - Smaller if cannot split list any more
    return [input_list[i * n:(i + 1) * n] for i in range((len(input_list) + n - 1) // n )]


def bits_to_symbol(bits: list[int]) -> str: #Transform array of 8 bits into a symbol
    if len(bits) < 8:
        bits = [0]*(8 - len(bits)) + bits
    
    bits_str = "".join(list(map(lambda x: str(x), bits)))
    ascii_code = int(bits_str, 2)
    #print(f'Ascii: {ascii_code}')
    return chr(ascii_code)


def create_status_popup(parent_tab, status_text: str) -> ttk.Label:
    status_window = tk.Toplevel(parent_tab)
    status_window.geometry("500x50")
    status_window.title("Shift status")
    return ttk.Label(status_window, text=status_text)


def get_page_count(pdf_path) -> int:
    doc = fitz.open(pdf_path)
    pages = len(doc)
    doc.close()
    return pages