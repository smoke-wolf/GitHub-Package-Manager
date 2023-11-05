from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
from . import iconbuttons as ib
from . import scrollablelabel as sl

class CustomFrame:

    def __init__(self, bgImage=None):
        self.frame = tk.Frame()
        
        if bgImage != None:
            self.canvas = tk.Canvas(self.frame, width=1000, height=650, bg="white")
            self.canvas.pack(fill="both")

            self.file = Image.open(bgImage)
            self.img = ImageTk.PhotoImage(self.file.resize((464, 164), Image.ANTIALIAS))
            self.bg = self.canvas.create_image(300, 0, anchor=tk.NW, image=self.img)
            self.bgCheck = True

        self.bgCheck = False
        self.widgets = []
    
    def setupLabel(self, x, y, width, height, filePath=None, text=None):
        if self.bgCheck:
            label = sl.ScrollableLabel(self.canvas, x, y, text)
            label.configure(width, height)
            self.labelWindow = self.canvas.create_window(x, y, anchor=tk.NW, window=label.frame1)
        
        else:
            label = sl.ScrollableLabel(self.frame, x, y, text)
            label.configure(width, height)
            self.widgets.append(label)

    def setupIconButton(self, x, y, iconPath, iconScale=1, command=lambda: print("Hi Mom!!")):
        if self.bgCheck:
            button = ib.IconButton(self.canvas, x, y, command, iconPath, iconScale)
            self.buttonWindow = self.canvas.create_window(x, y, anchor=tk.NW, window=button)
        
        else:
            button = ib.IconButton(self.frame, x, y, command, iconPath, iconScale)
            self.widgets.append(button)

    def constructFrame(self):
        for widget in self.widgets:
            widget.construct()
