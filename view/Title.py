import tkinter as tk

class Title(tk.Label):
    def __init__(self,master, text, **kw):
        super().__init__(master, **kw, text=text, font=("Helvetica", 72))
