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

from .UI_Builder import widgetfactory as wf
from .UI_Builder import utilities as ut
from .UI_Builder import customnotebook as cnb


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


class InfoFrame:
    def __init__(self):
        self.frame = wf.CustomFrame("Info")
        
        infoText = """

        
GHPM (GitHub Package Manager) is a lightweight package manager designed to efficiently manage coding projects and applications.

Key Features:
- Simplified Logic: GHPM focuses on basic and straightforward logic, making it easy to use and understand.
- Code Management: It effectively manages coding projects, allowing you to organize and maintain your codebase.
- Package Installation: GHPM streamlines the installation of project requirements and dependencies.

GHPM is a powerful yet lightweight solution for managing your code projects. Give it a try and experience the simplicity and efficiency it offers!
        """

        self.frame.addScrollText(log=infoText, x=31, y=50, width=70, height=19,
                                font=('Helvetica', 14), scrollTextBootStyle="info")
        self.frame.constructFrame()
    
    def getFrame(self):
        return self.frame


