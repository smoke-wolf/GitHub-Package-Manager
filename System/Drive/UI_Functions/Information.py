import datetime
import inspect
import platform
import re
import socket
import subprocess
from tkinter import ttk
import User.UserProfile
import System.Drive.Errors_Events.EventMan as EV
import tkinter as tk
from tkinter.font import Font
cwd = User.UserProfile.SourceDirectory


import System.Drive.Errors_Events.EventMan as EV
import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Information', a3='None')
def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name


def show_information():
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)

    info_window = tk.Tk()
    info_window.title('Information')

    # Set window size and position
    screen_width = info_window.winfo_screenwidth()
    screen_height = info_window.winfo_screenheight()
    window_width = 440
    window_height = 460
    info_window.config(bg='#C5E0DC')
    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    info_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    info_text = """
        GHPM (GitHub Package Manager) is a lightweight package manager designed to efficiently manage coding projects and applications.

        Key Features:
        - Simplified Logic: GHPM focuses on basic and straightforward logic, making it easy to use and understand.
        - Code Management: It effectively manages coding projects, allowing you to organize and maintain your codebase.
        - Package Installation: GHPM streamlines the installation of project requirements and dependencies.

        GHPM is a powerful yet lightweight solution for managing your code projects. Give it a try and experience the simplicity and efficiency it offers!
        """

    container = tk.Frame(info_window, bg='#F2E8C4', bd=2, relief=tk.SOLID)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    text_widget = tk.Label(container, text=info_text, bg='#F2E8C4', fg='#7E4A35', justify=tk.LEFT, wraplength=400)
    text_widget.pack(fill=tk.BOTH, expand=True)

    # Apply text styling
    font = Font(family="TkDefaultFont", size=15, weight="bold")
    text_widget.config(font=font)

    okay_button = ttk.Button(info_window, text='Okay', command=info_window.destroy, style='Custom.TButton')
    okay_button.pack(pady=10)

    info_window.mainloop()


