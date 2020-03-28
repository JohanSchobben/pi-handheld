import tkinter as tk


class FullscreenApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.fullScreenState = True
        self.attributes("-fullscreen", self.fullScreenState)
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d" % (self.w, self.h))
        self.bind("<Escape>", self.quit_app)

    def quit_app(self, event):
        self.destroy()