import tkinter as tk
from tkinter import ttk, filedialog
from utils import *
from .encode import encode_to_pdf, merge_paragraphs
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
    status = "???"
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

    filename = data['file'].replace('.txt', '')
    save_destination = Path(data['directory'] + '/' + filename + '.pdf')
    print(f'Save destination: {save_destination}')

    with open(data_path + '/' + data['file'], "r", encoding="utf-8") as f:
        doc = fitz.open()
        print('Trying to encode information...')
        lines = f.readlines()
        if(len(lines) < len(msg_bits)):
            status = f"Too many message bits compared to text length,\n \
            cannot perform word shift (Lines count: {len(lines)}, bits count: {len(msg_bits)})\n. Try longer text or shorter message."
        else:
            data_txt = merge_paragraphs("".join(lines))
            encode_to_pdf(doc, data_txt, name=save_destination, text_to_encode=msg_bits)
            status = f"Encoding process went successfully. Results written to {filename}.pdf file"

    status_label = create_status_popup(word_shift_tab, status)
    status_label.pack()
        