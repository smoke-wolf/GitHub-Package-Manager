'''
this script provides a way to kill a server process 
running on a specific port (in this case, port 3000).
It leverages subprocess commands and logs events for 
analytics tracking.

'''


import datetime
import inspect
import platform
import re
import socket
import subprocess
from tkinter import ttk

global os
import os
import sys
import time
import User.UserProfile
import System.Drive.Errors_Events.EventMan as EV
global cwd

cwd = User.UserProfile.SourceDirectory


import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Kill_server', a3='None')
def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name

def terminate_process_on_port(port):
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    try:
        # Execute the command to find the process ID (PID) using the specified port
        command = f'lsof -ti :{port}'
        pid = subprocess.check_output(command, shell=True).decode('utf-8').strip()

        # Terminate the process using the obtained PID
        subprocess.call(['kill', pid])
        EV.guiEvent(0, f'killed {pid}', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        print(f"Process running on port {port} terminated successfully.")
    except subprocess.CalledProcessError:
        os.system('''osascript -e 'display notification "Server Not Connected" with title "gpm"'
                    ''')
        sys.exit(0)


def kill_server():
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    import subprocess
    try:
        terminate_process_on_port(3000)
        os.system('''osascript -e 'display notification "Server Killed" with title "gpm"'
                ''')
        EV.guiEvent(4, 'server down', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    except:
        pass
