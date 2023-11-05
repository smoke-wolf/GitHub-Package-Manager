import tkinter as tk
from tkinter import ttk
import os


class ScrollableLabel:
    def __init__(self, master, x, y, text):
        self.x = x
        self.y = y
        self.text = text

        self.frame1 = tk.Frame(master, borderwidth=0, bg="#000000")
        self.frame2 = tk.Frame(master, borderwidth=0, bg="#000000")

        style =ttk.Style()
        style.theme_use("clam")
        self.canvas = tk.Canvas(self.frame2, bg="#000000", scrollregion=((0, 0, 0, 1000)))
        self.vertBar = ttk.Scrollbar(self.frame2, orient="vertical")

        if self.text == None:
            self.label = tk.Label(self.canvas, text="brrrr", foreground="#ffffff", background="#000000")

    def configure(self, width, height):
        self.vertBar.config(command=self.canvas.yview)
        self.canvas.config(width=width, height=height)
        self.canvas.config(yscrollcommand=self.vertBar.set)

        def scroll(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        self.canvas.bind_all("<MouseWheel>", scroll)

    def construct(self):
        self.frame1.place(x=self.x, y=self.y)
        self.frame2.pack(expand=True)

        self.vertBar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        if self.text == None:
            self.labelWindow = self.canvas.create_window(20, 500, anchor=tk.NW, window=self.label)


if __name__ == "__main__":
    
    root = tk.Tk()
    root.geometry("400x400")

    SLN = ScrollableLabel(root)
    SLN.configure(200, 200)
    SLN.construct(10, 10)

    root.mainloop()
