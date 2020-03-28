import tkinter as tk

class Button(tk.Button):
    def __init__(self,master, text, **kw):
        super().__init__(master, text=text, fg="#ffffff", relief="flat", padx=10, pady=5, bg="#A3CBEA", **kw)
