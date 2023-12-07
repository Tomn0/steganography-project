import os
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog

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
    
    ttk.Label(tab, text = "Select the Month :",  
    font = ("Times New Roman", 10))

    n = tk.StringVar() 
    file_choosen = ttk.Combobox(tab, width = 27,  textvariable = n) 
    
    # Adding combobox drop down list 
    file_choosen['values'] = files 
    
    # Shows february as a default value 
    file_choosen.current(1) 
    file_choosen.pack() 
    return file_choosen