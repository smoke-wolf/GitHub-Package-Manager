import datetime
import inspect
import platform
import re
import socket
import subprocess
from tkinter import ttk, simpledialog

import requests

global os
import os
import sys
import time
import User.UserProfile
sd = User.UserProfile.SourceDirectory
import System.Drive.Errors_Events.EventMan as EV
from tkinter import messagebox
import tkinter as tk
cwd = User.UserProfile.SourceDirectory



import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Settings', a3='None')

def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name



def reset_all():
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    import tkinter as tk
    from tkinter import simpledialog

    root = tk.Tk()
    root.title('Reset All')
    root.withdraw()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 440
    window_height = 460
    root.config(bg='#4e073a')
    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    import User.UserProfile

    # require USER_PASS
    import os, time

    pass

    Input = simpledialog.askstring(
        'Password', 'Enter your password:', show='*'
    )
    if Input is None:
        pass
    else:
        sd = User.UserProfile.SourceDirectory[:-1]
        try:
            import System.Drive.Password as PS

            PS.Password(Event='Cache', Input=Input)
            messagebox.showinfo('Password', 'Correct Password')
            time.sleep(0.23)
            try:
                open(f'{cwd}System/.Cache/System/GitHub/Int.txt', 'w').close()
                print('|  |                Int.txt Cleared')
                open(f'{cwd}System/.Cache/System/Local/Int.txt', 'w').close()
                open(f'{cwd}System/.Cache/System/Local/Int2.txt', 'w').close()
                import shutil
                directory = f'{cwd}System/.Cache/System/Local'

                for entry in os.scandir(directory):
                    if entry.is_dir() and entry.name != 'download':
                        shutil.rmtree(entry.path)

                try:
                    shutil.rmtree(f'{cwd}System/.Cache/System/GitHub')
                    os.mkdir(f'{cwd}System/.Cache/System/GitHub')
                except:
                    pass
                print('|  |              dirs made & Cleared')
                open(f'{cwd}System/.Cache/System/ErrorLog/GUIevents', 'w').close()
                open(f'{cwd}System/.Cache/System/ErrorLog/Events', 'w').close()
                open(f'{cwd}System/.Cache/System/ErrorLog/Event.db', 'w').close()

                open(f'{cwd}System/.Cache/System/ErrorLog/GUIevents', 'w')
                open(f'{cwd}System/.Cache/User/FirstUseToken.txt', 'w').close()
                open(f'{cwd}User/UserProfile.py', 'w').close()
                print('|  |                Int.txt Cleared')
                open(f'{cwd}System/.Cache/System/Local/Int.txt', 'w').close()
                open(f'{cwd}System/.Cache/System/Local/Int2.txt', 'w').close()
                open(f'{cwd}System/.Cache/User/local', 'w').close()

                print(f'|  |                Update Recorded')
            except:
                EV.guiEvent(1,
                            f'{get_current_function()} Error: Incorrect password',
                            inspect.currentframe().f_lineno,
                            os.path.abspath(__file__), False, True,
                            3)
                messagebox.showerror('Password', 'Incorrect Password')
                pass  # event=f'Everything Failed To Reset Due To Password Error', Pol=0)
                raise exit(0)

            time.sleep(2)
            print(f'\n' * 60)

        except:
            EV.guiEvent(1,
                        f'{get_current_function()} Error: Incorrect password',
                        inspect.currentframe().f_lineno,
                        os.path.abspath(__file__), False, True,
                        3)
            messagebox.showerror('Password', 'Incorrect Password')
            Input = simpledialog.askstring(
                'Password', 'Enter your password:', show='*'
            )
            if Input is None:
                pass
            else:
                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Cache', Input=Input)
                    messagebox.showinfo('Password', 'Correct Password')
                    try:
                        open(f'{cwd}System/.Cache/System/GitHub/Int.txt', 'w').close()
                        print('|  |                Int.txt Cleared')
                        open(f'{cwd}System/.Cache/System/Local/Int.txt', 'w').close()
                        open(f'{cwd}System/.Cache/System/Local/Int2.txt', 'w').close()
                        import shutil
                        directory = f'{cwd}System/.Cache/System/Local'

                        for entry in os.scandir(directory):
                            if entry.is_dir() and entry.name != 'download':
                                shutil.rmtree(entry.path)
                        try:
                            shutil.rmtree(f'{cwd}System/.Cache/System/GitHub')
                            os.mkdir(f'{cwd}System/.Cache/System/GitHub')
                        except:
                            pass
                        print('|  |              dirs made & Cleared')
                        open(f'{cwd}System/.Cache/System/ErrorLog/GUIevents', 'w').close()
                        open(f'{cwd}System/.Cache/System/ErrorLog/Events', 'w').close()
                        open(f'{cwd}System/.Cache/System/ErrorLog/Event.db', 'w').close()

                        open(f'{cwd}System/.Cache/System/ErrorLog/GUIevents', 'w')
                        open(f'{cwd}System/.Cache/User/FirstUseToken.txt', 'w').close()
                        open(f'{cwd}User/UserProfile.py', 'w').close()
                        print('|  |                Int.txt Cleared')
                        open(f'{cwd}System/.Cache/System/Local/Int.txt', 'w').close()
                        open(f'{cwd}System/.Cache/System/Local/Int2.txt', 'w').close()
                        open(f'{cwd}System/.Cache/User/local', 'w').close()

                        print(f'|  |                Update Recorded')
                    except:
                        EV.guiEvent(1,
                                    f'{get_current_function()} Error: Incorrect password',
                                    inspect.currentframe().f_lineno,
                                    os.path.abspath(__file__), False, True,
                                    3)
                        messagebox.showerror('Password', 'Incorrect Password')
                        pass  # event=f'Everything Failed To Reset Due To Password Error', Pol=0)
                        raise exit(0)

                    time.sleep(2)
                    print(f'\n' * 60)

                except:
                    EV.guiEvent(1,
                                f'{get_current_function()} Error: Incorrect password',
                                inspect.currentframe().f_lineno,
                                os.path.abspath(__file__), False, True,
                                3)

                    messagebox.showinfo('Password', 'Final Attempt')
                    Input = simpledialog.askstring(
                        'Password', 'Enter your password:', show='*'
                    )
                    if Input is None:
                        pass
                    else:
                        try:
                            import System.Drive.Password as PS

                            PS.Password(Event='Cache', Input=Input)
                            messagebox.showinfo('Password', 'Correct Password')
                            try:
                                open(f'{cwd}System/.Cache/System/GitHub/Int.txt', 'w').close()
                                print('|  |                Int.txt Cleared')
                                open(f'{cwd}System/.Cache/System/Local/Int.txt', 'w').close()
                                open(f'{cwd}System/.Cache/System/Local/Int2.txt', 'w').close()
                                import shutil
                                directory = f'{cwd}System/.Cache/System/Local'

                                for entry in os.scandir(directory):
                                    if entry.is_dir() and entry.name != 'download':
                                        shutil.rmtree(entry.path)
                                try:
                                    shutil.rmtree(f'{cwd}System/.Cache/System/GitHub')
                                    os.mkdir(f'{cwd}System/.Cache/System/GitHub')
                                except:
                                    pass

                                print('|  |              dirs made & Cleared')
                                open(f'{cwd}System/.Cache/System/ErrorLog/GUIevents', 'w').close()
                                open(f'{cwd}System/.Cache/System/ErrorLog/Events', 'w').close()
                                open(f'{cwd}System/.Cache/System/ErrorLog/Event.db', 'w').close()

                                open(f'{cwd}System/.Cache/System/ErrorLog/GUIevents', 'w')
                                open(f'{cwd}System/.Cache/User/FirstUseToken.txt', 'w').close()
                                open(f'{cwd}User/UserProfile.py', 'w').close()
                                print('|  |                Int.txt Cleared')
                                open(f'{cwd}System/.Cache/System/Local/Int.txt', 'w').close()
                                open(f'{cwd}System/.Cache/System/Local/Int2.txt', 'w').close()
                                open(f'{cwd}System/.Cache/User/local', 'w').close()

                                print(f'|  |                Update Recorded')
                            except:
                                EV.guiEvent(1,
                                            f'{get_current_function()} Error: Cache refused to clear',
                                            inspect.currentframe().f_lineno,
                                            os.path.abspath(__file__), False, True,
                                            3)

                            time.sleep(2)
                            print(f'\n' * 60)
                        except:
                            EV.guiEvent(1,
                                        f'{get_current_function()} Error: Incorrect password',
                                        inspect.currentframe().f_lineno,
                                        os.path.abspath(__file__), False, True,
                                        3)

def Create():
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    import User.UserProfile
    import hashlib
    import uuid

    Input = simpledialog.askstring(
        'Change Password', 'ENTER NEW PASSWORD:', show='*'
    )
    UUID = uuid.uuid1()

    UserID = os.getlogin()

    salt = '9lk'

    UUID = str(f'{UUID}')

    uuidToken = UUID[30:]
    DefaultTkn = User.UserProfile.uuid1

    Password = f'{Input}{uuidToken}{UserID}'

    password = Password + salt
    hashed = hashlib.md5(password.encode())
    Password = hashed.hexdigest()
    messagebox.showinfo('Update', "Click 'Ok' To Accesses New Key")
    SourceDirectory = User.UserProfile.SourceDirectory
    up = open(f'{SourceDirectory}User/UserProfile.py', 'a')
    up.write(f"\nPassword = '{Password}'")
    up.close()
    print(Password)

def create_custom_style():
    style = ttk.Style()
    style.configure(
        "Custom.TButton",
        foreground="#2471ed",
        background="#3498db",
        relief="flat",
        padding=10,
        font=("Helvetica", 18, "bold")
    )



def settings_window():
    print()

    def do_something(index):
        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        if index == 0:
            # require USER_PASS
            import os, time

            Input = simpledialog.askstring('GHPM', 'Enter Password: ')
            if Input is None:
                pass
            else:
                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Forced Login', Input=Input)

                    try:
                        with open(f'{cwd}User/UserProfile.py', 'a') as file:
                            pass
                    except:
                        EV.guiEvent(0,
                                    f'{get_current_function()} Error: UserProfile.py May still be encrypted',
                                    inspect.currentframe().f_lineno,
                                    os.path.abspath(__file__), False, True,
                                    4)

                    import User.UserProfile as up
                    if up.Force_Import_Request is True:
                        Status = False

                    else:
                        Status = True

                    fileid = open(f'{cwd}User/UserProfile.py', 'a')
                    fileid.write(f'\nForce_Import_Request = {Status}')
                    fileid.close()

                    messagebox.showinfo('GHPM', 'Update Recorded')
                    time.sleep(2)

                except:
                    EV.guiEvent(1,
                                f'{get_current_function()} Error: Incorrect password: settings not changed',
                                inspect.currentframe().f_lineno,
                                os.path.abspath(__file__), False, True,
                                3)
                    Input = simpledialog.askstring('GHPM', 'Enter Password: ')
                    if Input is None:
                        pass
                    else:
                        try:
                            import System.Drive.Password as PS

                            PS.Password(Event='Forced Login', Input=Input)

                            import_token = open(f'{sd}/User/UserProfile.py', 'a')
                            import User.UserProfile

                            if User.UserProfile.Force_Import_Request is True:
                                Status = False
                            else:
                                Status = True

                            import_token.write(
                                f'\nForce_Import_Request = {Status}'
                            )
                            import_token.close()

                            #

                            pass  # event=f'forced Module Import = {Status}', Pol=0)
                            messagebox.showinfo('GHPM', 'Update Recorded')
                            time.sleep(2)

                        except:
                            EV.guiEvent(1,
                                        f'{get_current_function()} Error: Incorrect password: settings not changed',
                                        inspect.currentframe().f_lineno,
                                        os.path.abspath(__file__), False, True,
                                        3)
                            messagebox.showinfo('Final Attempt')
                            Input = simpledialog.askstring(
                                'GHPM', 'Enter Password: '
                            )
                            if Input is None:
                                pass
                            else:
                                try:
                                    import System.Drive.Password as PS

                                    PS.Password(Event='Forced Login', Input=Input)

                                    import_token = open(
                                        f'{sd}/User/UserProfile.py', 'a'
                                    )
                                    import User.UserProfile

                                    if User.UserProfile.Force_Import_Request is True:
                                        Status = False
                                    else:
                                        Status = True

                                    import_token.write(
                                        f'\nForce_Import_Request = {Status}'
                                    )
                                    import_token.close()

                                    #

                                    pass  # event=f'forced Module Import = {Status}', Pol=0)
                                    messagebox.showinfo('GHPM', 'Update Recorded')
                                    time.sleep(2)

                                except:
                                    EV.guiEvent(1,
                                                f'{get_current_function()} Error: Incorrect password: settings not changed',
                                                inspect.currentframe().f_lineno,
                                                os.path.abspath(__file__), False, True,
                                                3)
                                    messagebox.showinfo('GHPM', 'Incorrect Password')

        elif index == 1:
            # require USER_PASS
            import os, time

            pass
            Input = simpledialog.askstring('GHPM', 'Enter Password: ')
            if Input is None:
                pass
            else:

                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Forced Login', Input=Input)

                    import_token = open(f'{sd}/User/UserProfile.py', 'a')
                    import User.UserProfile

                    if User.UserProfile.Forced_Login is True:
                        Status = False
                    else:
                        Status = True

                    import_token.write(f'\nForced_Login = {Status}')
                    import_token.close()

                    #

                    pass  # event=f'ForcedLogin = {Status}', Pol=0)
                    messagebox.showinfo('GHPM', 'Update Recorded')
                    time.sleep(2)

                except:
                    EV.guiEvent(1,
                                f'{get_current_function()} Error: Incorrect password: settings not changed',
                                inspect.currentframe().f_lineno,
                                os.path.abspath(__file__), False, True,
                                3)
                    Input = simpledialog.askstring('GHPM', 'Enter Password: ')
                    if Input is None:
                        pass
                    else:
                        try:
                            import System.Drive.Password as PS

                            PS.Password(Event='Forced Login', Input=Input)

                            import_token = open(f'{sd}/User/UserProfile.py', 'a')
                            import User.UserProfile

                            if User.UserProfile.Forced_Login is True:
                                Status = False
                            else:
                                Status = True

                            import_token.write(f'\nForced_Login = {Status}')
                            import_token.close()

                            #

                            pass  # event=f'ForcedLogin = {Status}', Pol=0)
                            messagebox.showinfo('GHPM', 'Update Recorded')
                            time.sleep(2)
                            messagebox.showinfo(f'\n' * 60)
                        except:
                            EV.guiEvent(1,
                                        f'{get_current_function()} Error: Incorrect password: settings not changed',
                                        inspect.currentframe().f_lineno,
                                        os.path.abspath(__file__), False, True,
                                        3)
                            messagebox.showinfo('Final Attempt')

                            simpledialog.askstring('GHPM', 'Enter Password: ')
                            try:
                                import System.Drive.Password as PS

                                PS.Password(Event='Forced Login', Input=Input)

                                import_token = open(
                                    f'{sd}/User/UserProfile.py', 'a'
                                )
                                import User.UserProfile

                                if User.UserProfile.Forced_Login is True:
                                    Status = False
                                else:
                                    Status = True

                                import_token.write(f'\nForced_Login = {Status}')
                                import_token.close()

                                #

                                pass  # event=f'ForcedLogin = {Status}', Pol=0)
                                messagebox.showinfo('GHPM', 'Update Recorded')
                                time.sleep(2)
                                messagebox.showinfo(f'\n' * 60)
                            except:
                                EV.guiEvent(1,
                                            f'{get_current_function()} Error: Incorrect password: settings not changed',
                                            inspect.currentframe().f_lineno,
                                            os.path.abspath(__file__), False, True,
                                            3)
                                messagebox.showinfo(
                                    'GHPM', 'Wrong Password Entered'
                                )
                                pass

            #

            pass  # event=f'Updated Canceled', Pol=0)

        elif index == 2:
            target = open(f'{sd}/User/UserProfile.py', 'a')
            import User

            Cstat = User.UserProfile.DisplayEvents
            if Cstat is True:
                status = False
            else:
                status = True

            target.write(f'\nDisplayEvents = {status}')
            target.close()
            messagebox.showinfo('Update', f'DisplayEvents set to {status}')

        elif index == 3:
            import os

            pass  # event='Creating Global Alias', Pol=10)
            import User

            alias = f"""echo 'alias gh="cd {User.UserProfile.SourceDirectory} &&python3 gh.py"' >> ~/.zshrc && exec zsh -l"""
            try:
                print(alias)
                os.system(alias)
            except:
                EV.guiEvent(0,
                            f'{get_current_function()} Error: Global alias not installed',
                            inspect.currentframe().f_lineno,
                            os.path.abspath(__file__), False, True,
                            4)

            messagebox.showinfo(
                'GHPM',
                f"""To Launch The CLI, In your terminal all you need to do is run gh (arg)

    examples:
    [gh -I https://github.com/SomeUser/Something.git] -> this installs the repo following -I
    [gh -IL  /Users/Someone/Something] -> this will import all of the files within the specified directory

    ======================================
    Help
    ====
    -I -> Install (arg<repo>)
    -IL -> Install Local (arg<dir>)

    -LA -> List All Installs
    -LL -> Launch Local Directory
    -LG -> Launch Git Project
    -LC -> Launch Advanced Projects

    -UG -> Uninstall GitHub Projects
    -UL -> Uninstall Local directories""",
            )
            messagebox.showinfo('CLI', 'now available')
        elif index == 4:
            import os

            Name = simpledialog.askstring(
                'GHPM', 'Enter Your Desired UserName: '
            )
            up = open(f'{sd}/User/UserProfile.py', 'a')
            up.write(f"\nUsername = '{Name}'")
            up.close()
            messagebox.showinfo('Update', 'UserName Updated')

        elif index == 5:
            Input = simpledialog.askstring(
                'Change Password', 'Enter your password:', show='*'
            )
            if Input is None:
                pass
            else:
                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Password Update', Input=Input)
                    try:
                        import System.Drive.Password as ps

                        Create()
                    except:
                        import os
                        EV.guiEvent(0,
                                    f'{get_current_function()} Error: New Password failed',
                                    inspect.cursrentframe().f_lineno,
                                    os.path.abspath(__file__), False, True,
                                    3)
                except:

                    Input = simpledialog.askstring(
                        'Change Password', 'Enter your password:', show='*'
                    )
                    if Input is None:
                        pass
                    else:
                        try:
                            import System.Drive.Password as PS

                            PS.Password(Event='Password Update', Input=Input)
                            try:
                                import System.Drive.Password as ps

                                Create()
                            except:
                                EV.guiEvent(0,
                                            f'{get_current_function()} Error: New Password failed',
                                            inspect.currentframe().f_lineno,
                                            os.path.abspath(__file__), False, True,
                                            3)
                        except:
                            EV.guiEvent(0,
                                        f'{get_current_function()} Error: Password failed',
                                        inspect.currentframe().f_lineno,
                                        os.path.abspath(__file__), False, True,
                                        3)
                            Input = simpledialog.askstring(
                                'Change Password', 'Enter your password:', show='*'
                            )
                            if Input is None:
                                pass
                            else:
                                try:
                                    import System.Drive.Password as PS

                                    PS.Password(Event='Password Update', Input=Input)
                                    try:
                                        import System.Drive.Password as ps

                                        Create()
                                    except:
                                        EV.guiEvent(0,
                                                    f'{get_current_function()} Error: New Password failed',
                                                    inspect.currentframe().f_lineno,
                                                    os.path.abspath(__file__), False, True,
                                                    3)
                                except:
                                    EV.guiEvent(0,
                                                f'{get_current_function()} Error: Password failed',
                                                inspect.currentframe().f_lineno,
                                                os.path.abspath(__file__), False, True,
                                                3)

        elif index == 6:
            reset_all()

        elif index == 7:
            import User.UserProfile
            with open(f'{User.UserProfile.SourceDirectory}System/.Cache/System/ErrorLog/GUIevents', 'r') as ev:
                log = f'https://priv-mu.vercel.app/{ev.read()}'

                print(requests.get(log))
        elif index == 8:
            target = open(f'{sd}/User/UserProfile.py', 'a')
            import User

            Cstat = User.UserProfile.PushLogs
            if Cstat is True:
                status = False
            else:
                status = True

            target.write(f'\nPushLogs = {status}')
            target.close()
            messagebox.showinfo('Update', f'PushLogs set to {status}')
        elif index == 9:
            target = open(f'{sd}/User/UserProfile.py', 'a')
            import User

            Cstat = User.UserProfile.AutoUpdate
            if Cstat is True:
                status = False
            else:
                status = True

            target.write(f'\nAutoUpdate = {status}')
            target.close()
            messagebox.showinfo('Update', f'AutoUpdate set to {status}')

        elif index == 10:
            target = open(f'{sd}/User/UserProfile.py', 'a')
            import User

            Cstat = User.UserProfile.AdvancedL
            if Cstat is True:
                status = False
            else:
                status = True

            target.write(f'\nAdvancedL = {status}')
            target.close()
            messagebox.showinfo('Update', f'PAdvancedL set to {status}')


        elif index == 11:
            settings_win.destroy()

    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    import User
    from tkinter import ttk
    settings_win = tk.Tk()
    settings_win.title('Settings')

    # Set window size and position
    screen_width = settings_win.winfo_screenwidth()
    screen_height = settings_win.winfo_screenheight()
    window_width = 440
    window_height = 460
    settings_win.config(bg='#C5E0DC')
    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    settings_win.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    options = [
        'Toggle Forced Module Import',
        'Toggle Forced Login',
        'Toggle System Event display',
        'Enable Command Line Interface',
        'Change UserName',
        'Change Password',
        'reset all',
        'Send Logs',
        'Toggle Push Logs',
        'Toggle Auto Update',
        'Toggle Advanced Logging',
        'Exit Settings',
    ]

    button_color = "#3498db"
    hover_color = "#2980b9"

    for i, option in enumerate(options):
        button = tk.Button(
            settings_win,
            text=option,
            command=lambda i=i: do_something(i),
            bg=button_color,
            fg="#a8138a",
            activebackground=hover_color,
            activeforeground="white",
            padx=10,
            pady=4,
            font=("Helvetica", 14, "bold"),
            borderwidth=0,  # Remove border
            highlightthickness=0  # Remove highlight
        )
        button.pack(pady=5, padx=10, fill=tk.X)

    settings_win.mainloop()




