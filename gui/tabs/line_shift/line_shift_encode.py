import tkinter as tk
from tkinter import ttk, filedialog
from utils import *
from .create_pdf import encode_to_pdf
import fitz
from pathlib import Path

data_path = '/Users/lukaszsochacki/Desktop/Studia/Steganografia/steganography-project/data'
select_clicked = False

def init(parent):
    global word_shift_tab

    word_shift_tab = ttk.Frame(parent)
    parent.add(word_shift_tab, text="Line shift - Encode")

    select_location_button = ttk.Button(word_shift_tab, text="Select save location", command=call_directory_finder)
    select_location_button.pack(pady=10)
    

def call_directory_finder(): # We choose pdf that we want to encode based on our text
    global select_clicked
    selected_directory = filedialog.askdirectory()
    print(f'Directory: {selected_directory}')

    directory = tk.StringVar()
    directory_label = ttk.Label(word_shift_tab, textvariable=directory)

    if select_clicked:
        return #Will have to update chosen directory somehow but will be done later i guess
    else:
        select_clicked = True
        directory_label = ttk.Label(word_shift_tab)
        directory_label.config(text=f"Selected Directory: {selected_directory}")
        directory_label.pack(pady=10)
        
        message_label = ttk.Label(word_shift_tab, text="Information to encode")
        message_label.pack()

        text_input = create_text_input_field(word_shift_tab)

        files = create_files_dropdown(word_shift_tab)

        execute_shift = ttk.Button(
            word_shift_tab,
            text="Encode",
            command=lambda: process_data(selected_directory, text_input, files),
            state="normal"
        )

        execute_shift.pack()    


def process_data(dir: str, message: scrolledtext.ScrolledText, file: ttk.Combobox):
    files_list = list_files_directory()
    data = {
        'directory': dir,
        'message': message.get("1.0", tk.END),
        'file': files_list[file.current()]
    }
    print(f'Encoding using provided data: {data}')
    
    bits = msg_to_bits(data['message'])
    print(bits)
    msg_bits = "".join(msg_to_bits(data['message']))
    print(f'Message transformed to bits: {msg_bits}')

    print('Encoding information...')
    doc = fitz.open()

    filename = data['file'].replace('.txt', '')
    save_destination = Path(data['directory'] + '/' + filename + '.pdf')
    print(f'Save destination: {save_destination}')

    with open(data_path + '/' + data['file'], "r", encoding="utf-8") as f:
        data_txt = "".join(f.readlines())
        encode_to_pdf(doc, data_txt, result_path= save_destination, text_to_encode=msg_bits)

    success_label = ttk.Label(word_shift_tab)
    success_label.config(text=f"Encoding process went successfully. Results written to {filename}.pdf file")
    success_label.pack(pady=10)

        