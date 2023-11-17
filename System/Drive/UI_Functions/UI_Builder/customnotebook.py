''' This file contains the class that creates the main instance notebook for the GUI. '''

import time as ti
import random as rd
import tkinter as tk
import ttkbootstrap as ttk
import ttkbootstrap.toast as tst

class Root:
    def __init__(self, root, theme='darkly'):

        '''
        This class provides an interface for creating a notebook
        and the main loading page of the GUI. As of now, the loading
        page is for aesthetics and has no purpose whatsoever.
        '''

        self.style = ttk.Style(theme=theme)
        self.style.configure('TButton', font=('Helvetica', 15))
        self.style.configure('TNotebook.Tab', font=('Helvetica', 12))
        self.root = root
        self.tabList = []
        self.setupToastNotification()
        # self.loadPage()
        self.setupNotebook()

    def loadPage(self):

        '''
        Creates a progressbar that fills by a random amount every 50
        milliseconds.
        '''

        progress = tk.DoubleVar()
        maxProgress = rd.randint(5000, 15000)

        label = ttk.Label(
            master=self.root,
            text="Loading...",
            font=('Helvetica', 50),
            foreground="#0099ff"
            )

        progressBar = ttk.Progressbar(
            master=self.root,
            orient='horizontal',
            length=500,
            maximum=maxProgress,
            variable=progress,
            bootstyle='striped-info'
        )

        centreLine = self.root.winfo_width()//2
        centreParallel = self.root.winfo_height()//2

        label.place(x=centreLine-176, y=centreParallel-75)
        progressBar.place(x=centreLine-250, y=centreParallel+75)

        def loop_function():

            '''
            The function that deals with the filling of
            the progressbar.
            '''

            i = 0

            while i <= maxProgress:
                progress.set(i)
                i += rd.randint(20, 200)
                ti.sleep(0.05)
                self.root.update()
        
        loop_function()
        label.destroy()
        progressBar.destroy()

    def setupToastNotification(self):

        '''
        Sets up a ToastNotification that alerts the user that an
        instance of the GUI has been created.
        '''

        self.notification = tst.ToastNotification(
            title='GhPM is running',
            message='An instance of the GhPM GUI is running.',
            duration=3000,
            bootstyle='dark',
            alert=True,
        )
        self.notification.show_toast()
        self.root.attributes('-topmost', True)

    def setupNotebook(self):

        '''
        Sets up a ttkbootstrap Notebook that stores all the frames/tabs.
        (For those who have gone through the code: No, I didin't create
        a custom notebook widget, because i like to be sane and not 
        psychotic.)
        This particular method also provides keybindings and
        mousebindings for closing tabs.
        '''

        self.noteBook = ttk.Notebook(master=self.root, bootstyle='success')
        self.noteBook.pack(fill=ttk.BOTH, expand=ttk.YES)

        def on_click(event):

            '''
            Checks if the clicked tab is the first/main tab.
            '''

            clickedTab = self.noteBook.tk.call(self.noteBook._w, "identify", "tab", event.x, event.y)
            if clickedTab != 0:
                self.noteBook.forget(clickedTab)
                self.tabList.pop(clickedTab)

        def on_press(event):

            '''
            Checks if the active tab is the first/main tab.
            '''

            activeTab = self.noteBook.index(self.noteBook.select())
            if activeTab != 0:
                self.noteBook.forget(activeTab)
                self.tabList.pop(activeTab)

        self.noteBook.bind('<Button-3>', on_click)
        self.noteBook.bind('<Escape>', on_press)
    
    def addTkFrame(self, tab, tabName):

        '''
        Adds a normal tk/ttk/ttkbootstrap frame to
        the notebook.
        '''

        tab.master = self.noteBook
        self.noteBook.add(child=tab, text=tabName)
    
    def addCustomFrame(self, tab):

        '''
        Adds a CustomFrame instance to the notebook.
        '''

        frame = tab.frame
        frame.master = self.noteBook
        name = tab.name

        if name not in self.tabList:
            self.noteBook.add(child=frame, text=tab.name)
            self.tabList.append(name)
            self.noteBook.select(frame)
