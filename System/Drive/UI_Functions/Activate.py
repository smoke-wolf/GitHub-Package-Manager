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
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Activation', a3='None')


def remove_line_by_content(file_path, content_to_remove):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                if content_to_remove not in line:
                    file.write(line)

        print(f"Lines containing '{content_to_remove}' removed from {file_path}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def is_safe_input(input_str):
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    # Regular expression pattern for command injection detection
    command_injection_pattern = r"[;&|`'\"\$()<>]"

    # Check if the input string matches the command injection pattern
    if re.search(command_injection_pattern, input_str):
        return False  # The string contains potential command injection


    return True  # The string is considered safe


def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name


def GH():
    import  tkinter
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    import User

    cwd = User.UserProfile.SourceDirectory

    import os

    with open(f'{cwd}System/.Cache/System/GitHub/int.txt', 'r') as r, open(
            f'{cwd}System/.Cache/System/GitHub/int2.txt', 'w'
    ) as o:
        for line in r:
            if line.strip():
                o.write(line)

    f = open(f'{cwd}System/.Cache/System/GitHub/int2.txt', 'r')

    lines = f.readlines()
    count = len(lines)

    options = []
    lines_r = []
    for line in lines:
        value4 = line.strip()
        lines_r.append(value4)
        Val = value4.split('&', 1)
        if len(Val) > 0:
            value4 = Val[1]

        options.append(value4.split("%", 1)[0])

    window = tkinter.Tk()
    window.title('Activate one of the following')
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 440
    window_height = 460
    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    window.config(bg='#C5E0DC')

    def select_option(selected_option):
        window.destroy()

        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        print('Selected Option:', selected_option)

        value = lines[int(options.index(selected_option))]
        print(value)
        cc = value
        listOfWords = value.split('&', 1)
        if len(listOfWords) > 0:
            value = listOfWords[1]

        value = value.split('≈', 1)[0]

        cc = cc.split('@', 1)[0]
        cc = cc.split("%", 1)[0]
        EV.NewEvent(event=f'Change Directory: {cc} ', Pol=0)
        EV.NewEvent(event=f'os command [!]{value}[!] ', Pol=0)
        try:
            os.system(
                f'osascript -e \'tell application "Terminal" to do script "cd {cc}&&{selected_option}"\''
            )

        except:
            EV.guiEvent(0, f'Directory change failed', inspect.currentframe().f_lineno, os.path.abspath(__file__),
                        False, True,
                        1)
    def reinstall(opt, source):
        import System.Drive.UI_Functions.Install
        value = lines[int(options.index(opt))]
        print(value)
        cc = value
        listOfWords = value.split('&', 1)
        if len(listOfWords) > 0:
            value = listOfWords[1]

        value = value.split('-', 1)[0]

        cc = cc.split('@', 1)[0]
        cc = cc.split("%", 1)[0]


        import tkinter as tk
        from tkinter import messagebox
        import shutil
        shutil.rmtree(cc)
        remove_line_by_content(file_path=f'{User.UserProfile.SourceDirectory}System/.Cache/System/GitHub/int2.txt',
                               content_to_remove=opt)
        remove_line_by_content(file_path=f'{User.UserProfile.SourceDirectory}System/.Cache/System/GitHub/Int.txt', content_to_remove=opt)
        System.Drive.UI_Functions.Install.Installer(value= source)



    def updated(selected_option, source):
        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        value = lines[int(options.index(selected_option))]
        print(value)
        cc = value
        listOfWords = value.split('&', 1)
        if len(listOfWords) > 0:
            value = listOfWords[1]

        value = value.split('-', 1)[0]

        cc = cc.split('@', 1)[0]
        cc = cc.split("%", 1)[0]

        try:
            import tkinter as tk
            from tkinter import messagebox
            print(f"Updating {source}")
            import shutil
            shutil.rmtree(cc)
            os.chdir(f'{User.UserProfile.SourceDirectory}System/.Cache/System/Github/Downloads')
            print('trying update')
            try:
                import tkinter as tk
                from tkinter import messagebox
                if not is_safe_input(source):
                    print("Unsafe input! Potential command injection detected.")
                    return

                command = f'git clone {source}'
                subprocess.call(command, shell=True)
                messagebox.showinfo("Update Successful", "has been successfully updated.")
            except:
                EV.guiEvent(0, f'{get_current_function()} git clone update failed', inspect.currentframe().f_lineno, os.path.abspath(__file__),
                            True, True,
                            1)

        except:
            import tkinter as tk
            from tkinter import messagebox
            print(f'')
            messagebox.showinfo("Update Failed", f"Update Failed {source}")
            EV.guiEvent(0, f'{get_current_function()} Update Failed {source}', inspect.currentframe().f_lineno, os.path.abspath(__file__),
                        False, True,
                        1)

    def open_option_window(event, option):
        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        option_window = tkinter.Toplevel()
        option_window.title(option)
        option_window.geometry("300x200")
        screen_width = option_window.winfo_screenwidth()
        screen_height = option_window.winfo_screenheight()
        window_width = 440
        window_height = 460
        x_coordinate = (screen_width // 2) - (window_width // 2)
        y_coordinate = (screen_height // 2) - (window_height // 2)
        option_window.config(bg='#C5E0DC')
        option_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        for line in lines_r:
            if option in line:
                try:
                    Val = line.split('#', 1)
                    if len(Val) > 0:
                        global date
                        date = Val[1]
                except:
                    print('package install date not available')
                    date = 'unavailable'

                try:
                    Val = line.split('%', 1)
                    if len(Val) > 0:
                        sourcex = Val[1]
                        global source
                        source = sourcex.split("#", 1)[0]
                except:
                    print('Source unavailable')
                    source = 'unavailable'

        information = f'''
        Date downloaded: {date}
        Downloaded from: {source}
        '''

        info_label = ttk.Label(option_window, text=information)
        info_label.pack(pady=10)

        launch_button = ttk.Button(option_window, text="Launch", command=lambda opt=option: ((select_option(opt)),(option_window.destroy())))
        launch_button.pack(pady=5)

        re_button = ttk.Button(option_window, text="Reinstall",command=lambda opt=option, source=source.split("#", 1)[0]: reinstall(opt, source))
        re_button.pack(pady=5)

        update_button = ttk.Button(option_window, text="Update",
                                   command=lambda opt=option, source=source.split("#", 1)[0]: updated(opt, source))
        update_button.pack(pady=5)

        option_window.transient(window)
        option_window.grab_set()
        option_window.focus_set()

    for option in options:
        b = ttk.Button(window, text=option, command=lambda opt=option: select_option(opt))
        b.pack(pady=5)
        b.bind("<Enter>", lambda event, opt=option: open_option_window(event, opt))

    window.mainloop()


def Activate():
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    print(cwd)
    import tkinter as tk
    from tkinter import messagebox

    result1 = messagebox.askyesno('User GitHub Check', 'Use GitHub applications?')

    if result1:
        GH()
    else:
        result2 = messagebox.askyesno('User GitHub Check', 'Use Local applications?')

        if result2:
            options = []

            with open(f'{cwd}System/.Cache/System/Local/Int.txt', 'r') as r, open(
                    f'{cwd}System/.Cache/System/Local/Int2.txt', 'w'
            ) as o:
                for line in r:
                    if line.strip():
                        o.write(line)
            f = open(f'{cwd}System/.Cache/System/Local/Int2.txt', 'r')

            lines = f.readlines()
            count = len(lines)

            count1 = 0
            for line in lines:
                count1 += 1
                options.append(line.strip())

            window = tk.Tk()
            window.title('Activate one of the following')
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            window_width = 440
            window_height = 460
            x_coordinate = (screen_width // 2) - (window_width // 2)
            y_coordinate = (screen_height // 2) - (window_height // 2)
            window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
            window.config(bg='#C5E0DC')

            def select_option(selected_option):
                EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
                print('Selected Option:', selected_option)

                pass  # event=f'{count1}={count} --COMMAND LINE', Pol=0)
                value = lines[int(options.index(selected_option))]
                listOfWords = value.split('≈', 1)
                if len(listOfWords) > 0:
                    valueg = listOfWords[1]
                    print(valueg)

                value1 = value.split(f'@', 1)[0]

                listOfWords = value.split('+', 1)
                if len(listOfWords) > 0:
                    value = listOfWords[1]

                value = value.split('≈', 1)[0]

                try:
                    print(valueg[:-2])
                    print(value)
                    os.system(
                        f'osascript -e \'tell application "Terminal" to do script "cd {value} && {valueg[:-2]}"\''
                    )
                except:
                    EV.guiEvent(0, f'{get_current_function()} either Dir change failed or {valueg[:-2]}', inspect.currentframe().f_lineno,
                                os.path.abspath(__file__), False, True,
                                1)

            for option in options:
                b = tk.Button(
                    window,
                    text=option,
                    command=lambda opt=option: select_option(opt),
                )
                b.pack()

            window.mainloop()

        else:
            result3 = messagebox.askyesno('User Advanced Check', 'Use Advanced GitHub applications?')

            if result3:
                options = []
                with open(f'{cwd}System/.Cache/System/GitHub/Complex', 'r') as r, open(
                        f'{cwd}System/.Cache/System/GitHub/Complex2', 'w'
                ) as o:
                    for line in r:
                        if line.strip():
                            o.write(line)

                f = open(f'{cwd}System/.Cache/System/GitHub/Complex2', 'r')

                linesd = f.readlines()
                count = len(linesd)

                count1 = 0
                options = [line.strip() for line in linesd]

                window = tk.Tk()
                window.title('Activate one of the following')
                screen_width = window.winfo_screenwidth()
                screen_height = window.winfo_screenheight()
                window_width = 440
                window_height = 460
                x_coordinate = (screen_width // 2) - (window_width // 2)
                y_coordinate = (screen_height // 2) - (window_height // 2)
                window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
                window.config(bg='#C5E0DC')

                def select_option(selected_option):
                    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
                    print('Selected Option:', selected_option)

                    def submit():
                        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
                        name = entry_name.get()
                        window2.destroy()
                        window.destroy()
                        Arges = name

                        B = value.split('$', 1)[0]

                        lis = value.split('$', 1)
                        if len(lis) > 0:
                            lis = lis[1]

                        A = f'{lis} {Arges}'

                        r = open(f'{cwd}System/.Cache/System/GitHub/Complex_install', 'r')
                        lines = r.readlines()

                        for line in lines:
                            try:
                                os.system(line)
                            except:
                                EV.guiEvent(0, f'{get_current_function()} failed {line}',
                                            inspect.currentframe().f_lineno, os.path.abspath(__file__), True, True, 1)

                        open(f'{cwd}System/.Cache/System/GitHub/Complex_install', 'w')

                        try:
                            os.system(
                                f'osascript -e \'tell application "Terminal" to do script "cd {B}&&{A}"\''
                            )
                        except:
                            EV.guiEvent(0, f'{get_current_function()} either Dir change failed or {A}',
                                        inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 1)

                    value = selected_option
                    window2 = tk.Tk()
                    window2.title('Package Inform')
                    screen_width = window2.winfo_screenwidth()
                    screen_height = window2.winfo_screenheight()
                    window_width = 440
                    window_height = 460
                    x_coordinate = (screen_width // 2) - (window_width // 2)
                    y_coordinate = (screen_height // 2) - (window_height // 2)
                    window2.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
                    window2.config(bg='#C5E0DC')

                    label_name = tk.Label(
                        window2, text='Any Launch Arguments: '
                    )
                    entry_name = tk.Entry(window2)

                    label_name.pack()
                    entry_name.pack()

                    button = tk.Button(
                        window2, text='Submit', command=submit
                    )
                    button.pack()

                    window2.mainloop()

                for option in options:
                    b = tk.Button(
                        window,
                        text=option,
                        command=lambda opt=option: select_option(opt),
                    )
                    b.pack()

                window.mainloop()
            else:
                pass

