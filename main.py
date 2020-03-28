import tkinter as tk

from view.fullscreen_app import FullscreenApp
from view.landing_screen import LandingPage


def main():
    root = FullscreenApp()
    root.title = "Hello world!"
    app = LandingPage(root)
    app.mainloop()

if __name__ == '__main__':
    main()