from tabs.line_shift.line_shift_encode import init as init_line_shift_encode
from tabs.line_shift.line_shift_decode import init as init_line_shift_decode
from tabs.word_shift.word_shift_encode import init as init_word_shift_encode
from tabs.word_shift.word_shift_decode import init as init_word_shift_decode
from tabs.feature.feature_encode import init as init_feature_encode
from tabs.feature.feature_decode import init as init_feature_decode
from tabs.help.help_tab import init as init_help_tab

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text encoding - Steganography project")
root.geometry("1000x600")

tab_control = ttk.Notebook(root)
init_line_shift_encode(tab_control)
init_line_shift_decode(tab_control)
init_word_shift_encode(tab_control)
init_word_shift_decode(tab_control)
init_feature_encode(tab_control)
init_feature_decode(tab_control)
init_help_tab(tab_control)

# Dodanie zakładek do głównego okna
tab_control.pack(expand=1, fill="both")
root.mainloop()