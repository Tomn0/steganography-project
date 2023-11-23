#TODO
"""
- przygotowanie krótkich tesktów do testów DONE
- przygotowanie paru liter do testowania DONE
- opanowanie narzędzie fontforge do modyfikacji czcionki DONE
- design GUI
- implementacja GUI w tkinterze
    - ładowanie tesktu z pliku (do ustalenia jaki format!!)
    - podmiana tekstu nową czcionką (do weryfikacji czy fontforge to umożliwia czy trzeba inaczej)
    - zapisywanie podmienionego dokumentu spowrotem na stary format
    - podgląd tekstu w GUI
    - pobieranie tesktu 
    - dekodowanie
- dalszy etap: algorytmy kodowania wiadomości w tekście
"""

import tkinter as tk
from tkinter import ttk

class Decode(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # tk.Frame.__init__(self, parent, *args, **kwargs)
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

class Encode(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # tk.Frame.__init__(self, parent, *args, **kwargs)
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

    def initiate_tab(self):
        pass

class MainApplication(tk.Tk):

    def __init__(self):
        super().__init__()
        # configure the root window
        self.title("Text Hiding")
        self.minsize(800, 600)
        self.geometry("600x400")
        self.configure(bg="#0076CE")    # Dell Blue
        # photo = tk.PhotoImage(file = "lupa.jfif")
        # self.iconphoto(False, photo)

        # Create tabs
        self.tabControl = ttk.Notebook(self)
        self.tab_encode = ttk.Frame(self.tabControl)
        self.tab_decode = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab_encode, text='Encode')
        self.tabControl.add(self.tab_decode, text='Decode')

        self.tabControl.pack(expand=True, fill="both") 


        ###################
        # Encoding window #
        ###################
        self.navbar = tk.Frame(self.tab_encode,  width=200, height=500, pady=3)
        # self.frame = tk.Frame(self.tab_encode, bg="#0076CE",
        #                       width=600, height=500, pady=3)

        self.frame = Encode(self.tab_encode, bg="#0076CE",
                              width=600, height=500, pady=3)
        
        self.frame.initiate_tab()

        self.navbar.pack(anchor=tk.W, fill=tk.Y, expand=False, side=tk.LEFT)
        self.frame.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)

        # Text Widget
        self.textwidget = tk.Text(self.frame)
        self.textwidget.pack(side=tk.TOP)

        textBtn = tk.Button(self.navbar, text='LoadText', command=self.openText)
        textBtn.pack(expand=False, side=tk.TOP)

        ##########################
        #       WIDGETS          #
        ##########################

    def openText(self):
        file = open("data\\ws_mozliwosci.txt").read()
        self.textwidget.insert(0.0, file)



if __name__ == "__main__":
    # root = tk.Tk()
    app = MainApplication()


    app.mainloop()