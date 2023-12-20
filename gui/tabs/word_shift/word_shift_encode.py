import tkinter as tk
from tkinter import ttk, filedialog
from utils import *

select_clicked = False

def init(parent):
    global word_shift_tab

    word_shift_tab = ttk.Frame(parent)
    parent.add(word_shift_tab, text="Word shift - Encode")

    select_location_button = ttk.Button(word_shift_tab, text="Select save location", command=call_directory_finder)
    select_location_button.pack(pady=10)
    

def call_directory_finder(): # We choose pdf that we want to encode based on our text
    global select_clicked
    selected_directory = filedialog.askdirectory()
    print(f'Directory: {selected_directory}')

    directory = tk.StringVar()
    directory_label = ttk.Label(word_shift_tab, textvariable=directory)

    if select_clicked:
        return #Will have to update chosen directory somehow but will be done
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
            command=lambda: send_data(selected_directory, text_input, files),
            state="normal"
        )

        execute_shift.pack()    


def send_data(dir: str, message: scrolledtext.ScrolledText, file: ttk.Combobox):
    files_list = list_files_directory()
    data = {
        'directory': dir,
        'message': message.get("1.0", tk.END),
        'file': files_list[file.current()]
    }
    print(f'Encoding using provided data: {data}')
    return data