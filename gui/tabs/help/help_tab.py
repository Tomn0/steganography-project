import tkinter as tk
from tkinter import ttk, filedialog
from utils import *

select_clicked = False

def init(parent):
    global word_shift_tab

    word_shift_tab = ttk.Frame(parent)
    parent.add(word_shift_tab, text="Help")

    # about_label = ttk.Label(word_shift_tab)
    # about_label.config(text=f"A window application for text-based steganography project. GUI allows\
    #                   to choose three methods for text encryption:\n Line shift coding\nWord shift coding\
    #                   \nFeature coding\n Each method has tabs for encoding and decoding information")
    # about_label.pack(pady=20)
    
    #Fonts 
    font_label = ttk.Label(word_shift_tab)
    font_label.config(text=f"Click \'Select font\' button in Feature tabs to choose your font file")
    font_label.pack()

    select_font_button = ttk.Button(word_shift_tab, text="Select font", command=print('lol'))
    select_font_button.pack(pady=10)

    #pdf
    pdf_label = ttk.Label(word_shift_tab)
    pdf_label.config(text=f"Click \'Select PDF file\' button in decoding tabs to select document with information encoded within text")
    pdf_label.pack()

    select_pdf_button = ttk.Button(word_shift_tab, text="Select PDF file", command=print('lol'))
    select_pdf_button.pack(pady=10)

    #save location
    save_label = ttk.Label(word_shift_tab)
    save_label.config(text=f"Click \'Select save location\' button in encode tabs to select to which directory document with encoded information should be saved")
    save_label.pack()

    select_save_button = ttk.Button(word_shift_tab, text="Select save location", command=print('lol'))
    select_save_button.pack(pady=10)

    #Encode
    encode_label = ttk.Label(word_shift_tab)
    encode_label.config(text=f"Click \'Encode\' button in encode tabs to send provided input data for encoding procedure. Creates new document with encoded message")
    encode_label.pack()

    select_encode_button = ttk.Button(word_shift_tab, text="Encode", command=print('lol'))
    select_encode_button.pack(pady=10)

    #Decode
    decode_label = ttk.Label(word_shift_tab)
    decode_label.config(text=f"Click \'Decode\' button in decode tabs to extract hiiden information from provided PDF file. Print a message in text field as result")
    decode_label.pack()

    select_decode_button = ttk.Button(word_shift_tab, text="Decode", command=print('lol'))
    select_decode_button.pack(pady=10)

    #Text
    text_label = ttk.Label(word_shift_tab)
    text_label.config(text=f"With text input field below you can type message you would like to encode in text (Present in encoding tabs)")
    text_label.pack() 

    text_input = create_text_input_field(word_shift_tab)
    text_input.pack()
