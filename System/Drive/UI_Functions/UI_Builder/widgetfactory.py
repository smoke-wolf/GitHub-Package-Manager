''' This file contains classes that create objects that are used in the main GUI. '''

import tkinter as tk
import ttkbootstrap as ttk
import ttkbootstrap.constants as cons
import ttkbootstrap.scrolled as scrl


class CustomFrame:
    def __init__(self, name):

        '''
        This class provides a simple interface for creating
        custom frame objects that come packaged with
        methods that allows the user to add widgets.
        '''

        self.frame = ttk.Frame()
        self.name = name
        self.widgetList = []
    
    def addButton(self, name, x=10, y=10, width=None, command=None, buttonBootstyle='default'):

        '''
        Creates an instance of the ModdedButton class.
        '''

        button = ModdedButton(self.frame, name, x, y, command, width, buttonBootstyle)
        self.widgetList.append(button)

    def addScrollText(self, log, x=100, y=100, width=50, height=10,
                      font=('Helvetica', 12), scrollTextBootStyle='default'):
        
        '''
        Creates an instance of the ModdedScrollText class.
        '''

        scrollText = ModdedScrolledText(self.frame, log, x, y, width, height,
                                        font, scrollTextBootStyle)
        self.widgetList.append(scrollText)

    def constructFrame(self):

        '''
        Constructs and packges the finished frame.
        '''

        for widget in self.widgetList:
            widget.place()


class ModdedScrolledText(scrl.ScrolledText):
    def __init__(self, master, log, x, y, width, height, font, bootstyle):

        '''
        Extends the base ttkbootstrap ScrolledText class to store extra information.
        '''

        super().__init__(
            master=master,
            width=width,
            height=height,
            autohide=True,
            wrap=cons.WORD,
            padding=3,
            bootstyle=bootstyle,
            )

        self.font = font
        self.log = log
        self.x = x
        self.y = y
    
    def place(self):

        '''
        Overrides the place method and adds text to the textbox.
        '''

        super().place(x=self.x, y=self.y)
        self.insert(cons.END, self.log)
        self._text.configure(state='disabled', font=self.font)


class ModdedButton(ttk.Button):
    def __init__(self, master, name, x, y, command, width, bootstyle):

        '''
        Extends the base ttkbootstrap Button class to store extra information.
        '''

        super().__init__(
            master=master,
            text=name,
            command=command,
            bootstyle=bootstyle,
            width=width
            )
        
        self.x = x
        self.y = y
    
    def place(self):

        '''
        Overrides the place method.
        '''

        super().place(x=self.x, y=self.y)