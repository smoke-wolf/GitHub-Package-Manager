from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk


class GHPMMainGui:

    def __init__(self, width, height):
        self.setupRoot(width, height)
        self.setupNoteBook()

    def setupRoot(self, width, height):
        self.root = tk.Tk()
        self.root.title("GitHub Package Manager")

        centerX = (self.root.winfo_screenwidth() - width)/2
        centerY = (self.root.winfo_screenheight() - height)/2

        self.root.geometry("%dx%d+%d+%d" % (width, height, centerX, centerY))
        self.root.resizable(False, False)

    def setupNoteBook(self):
        self.notebook = ttk.Notebook(self.root, style="TNotebook")
        style = ttk.Style()
        style.configure("TNotebook.Tab", font=("Helvetica", 12), padding=[2, 3, 2, 2])
        self.notebook.pack(fill="both", expand=True)

    def addTab(self, tab, tabName):
        if not isinstance(tab, tk.Frame):
            tab = tab.frame
        tab.master = self.notebook
        self.notebook.add(tab, text=tabName)

    def run(self):
        self.root.mainloop()

