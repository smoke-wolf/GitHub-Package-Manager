import os
from PIL import Image, ImageTk
import tkinter as tk


class IconButton:
    def __init__(self, master, x, y, command, iconFilePath, iconScale):
        self.master = master
        self.x = x
        self.y = y
        self.command = command
        self.setIconImage(iconFilePath, iconScale)
    
    def setIconImage(self, filePath, iconScale):
        self.image = Image.open(filePath)
        newSize = (int(self.image.size[0] * iconScale), int(self.image.size[1] * iconScale))
        self.image = self.image.resize(newSize)

    def construct(self):
        self.image = ImageTk.PhotoImage(self.image)
        button = tk.Button(self.master, image=self.image, command=self.command, borderwidth=0, bg="black")
        button.place(x=self.x, y=self.y)
        return button
