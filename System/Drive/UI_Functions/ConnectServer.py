
import datetime
import inspect
import platform
import re
import socket
import subprocess
from tkinter import ttk, messagebox

global os
import os
import sys
import time
import User.UserProfile
import System.Drive.Errors_Events.EventMan as EV
global cwd

cwd = User.UserProfile.SourceDirectory

import System.Drive.Errors_Events.EventMan as EV
import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Starting_Server', a3='None')
def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name

def start_server():
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    server_file_path = f"{User.UserProfile.SourceDirectory}System/.Cache/System/Local/download/server.js"
    try:
        os.chdir(f'{User.UserProfile.SourceDirectory}System/.Cache/System/Local/download')
        subprocess.Popen(['node', server_file_path])
        messagebox.showinfo("Success", "Server started successfully!")
        EV.guiEvent(0, 'server started', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start server:\n{str(e)}")