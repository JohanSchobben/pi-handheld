from tkinter import Tk, Frame, Label

from view.Title import Title
from view.Button import Button


class LandingPage(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        self.setupMenu()
        self.setupSetting()

    def setupMenu(self):
        label = Title(self.master, text="Hello world")
        label.place(relx=0.1, rely=0.1)

    def setupSetting(self):
        instellingenButton = Button(self.master, "Instellingen", command=self.openSettings)
        instellingenButton.place(relx=0.9, rely=0.1)

    def openSettings(self, event):
        pass
