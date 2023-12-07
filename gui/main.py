from word_shift_coding import init as init_word_shift_coding

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text encoding - Steganography project")
root.geometry("900x600")

tab_control = ttk.Notebook(root)
init_word_shift_coding(tab_control)



# Dodanie zakładek do głównego okna
tab_control.pack(expand=1, fill="both")
root.mainloop()