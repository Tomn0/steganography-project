from line_shift_encode import init as init_line_shift_encode
from line_shift_decode import init as init_line_shift_decode
from word_shift_encode import init as init_word_shift_encode
from word_shift_decode import init as init_word_shift_decode
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text encoding - Steganography project")
root.geometry("900x600")

tab_control = ttk.Notebook(root)
init_line_shift_encode(tab_control)
init_line_shift_decode(tab_control)
init_word_shift_encode(tab_control)
init_word_shift_decode(tab_control)


# Dodanie zakładek do głównego okna
tab_control.pack(expand=1, fill="both")
root.mainloop()