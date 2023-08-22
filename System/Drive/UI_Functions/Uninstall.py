import datetime
import inspect
import platform
import re
import socket
import subprocess
import tkinter as tk
from tkinter import ttk
import User.UserProfile
import System.Drive.Errors_Events.EventMan as EV

import os
import sys
import time

cwd = User.UserProfile.SourceDirectory

global os

import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Uninstall', a3='None')
def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name

def confirm_uninstall(selected_item):
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    import tkinter.messagebox

    result = tk.messagebox.askyesno('Confirm Uninstall', 'Are you sure you want to uninstall ' + selected_item + '?')

    list_window.destroy()
    print(result)
    if result:
        valuee = items.index(selected_item)

        if valuee >= count:
            dr = int(valuee) - count
            command = lines2[dr - 1]
            print(command)

            try:
                import shutil
                co = command.split('@', 1)[0]
                shutil.rmtree(co)

                print(f'Project Removed {co}')

            except:
                print(f'Project Failed To Remove {co}')
                EV.guiEvent(0, f'{get_current_function()} Error: {co} not removed',
                            inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)

        else:
            with open(f'{cwd}System/.Cache/System/GitHub/int.txt', 'r') as file:
                lines5 = file.readlines()

            with open(f'{cwd}System/.Cache/System/GitHub/int.txt', 'w') as file:
                for linef in lines5:
                    if linef.find(selected_item) != -1:
                        rmdir = linef.split('@')[0]
                        try:
                            import shutil
                            shutil.rmtree(rmdir)
                            tk.messagebox.showinfo('Success', f'{rmdir} has been uninstalled.')
                        except:
                            EV.guiEvent(0, f'{get_current_function()} Error: Failed TO remove {rmdir}',
                                        inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)
                    else:
                        file.write(linef)

        return rmdir
    else:
        EV.guiEvent(0, 'Deletion Cancelled', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)

def show_list_window():
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    global list_window
    list_window = tk.Toplevel()

    list_window.title('Uninstall List')
    screen_width = list_window.winfo_screenwidth()
    screen_height = list_window.winfo_screenheight()
    window_width = 440
    window_height = 460
    list_window.config(bg='#C5E0DC')
    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    list_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    list_box = tk.Listbox(list_window, font=('Helvetica', 12), bd=2, relief=tk.SOLID, selectmode=tk.SINGLE)
    list_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    global items
    items = []
    try:
        with open(f'{cwd}System/.Cache/System/GitHub/int.txt', 'r') as r, open(f'{cwd}System/.Cache/System/GitHub/int2.txt', 'w') as o:
            for line in r:
                if line.strip():
                    o.write(line)
    except:
        EV.guiEvent(0, f'{get_current_function()} Error: GitHub data locked or not found',
                    inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 4)

    try:
        e = open(f'{cwd}System/.Cache/System/GitHub/Complex2', 'r')
    except:
        EV.guiEvent(0, f'{get_current_function()} Error: github data cannot be read',
                    inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)

    f = None  # Initialize f variable

    try:
        f = open(f'{cwd}System/.Cache/System/GitHub/int2.txt', 'r')
    except:
        EV.guiEvent(0, f'{get_current_function()} Error: github data cannot be read',
                    inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)

    lines = []
    if f is not None:
        lines = f.readlines()

    global count
    count = 0
    for line in lines:
        count += 1

    count1 = 0
    for line in lines:
        value4 = line.strip()
        Val = value4.split('&', 1)
        if len(Val) > 0:
            value4 = Val[1]
        items.append(value4)
        count1 += 1

    try:
        global lines2
        lines2 = e.readlines()
        for line2 in lines2:
            count1 += 1
            items.append(line2)
    except:
        EV.guiEvent(0, f'{get_current_function()} Error: Readlines failed Complex2',
                    inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)

    for item in items:
        list_box.insert(tk.END, item)

    confirm_button = ttk.Button(list_window, text='Confirm Uninstall',
                                command=lambda: confirm_uninstall(list_box.get(list_box.curselection())),
                                style='Custom.TButton')
    confirm_button.pack(pady=10)

    exit_button = ttk.Button(list_window, text='Exit Uninstaller', command=lambda: list_window.destroy(),
                             style='Custom.TButton')
    exit_button.pack(pady=10)



