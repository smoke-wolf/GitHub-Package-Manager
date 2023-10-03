import datetime
import inspect
import subprocess
from tkinter import ttk
import System.Drive.Errors_Events.EventMan as AR
global os
import User.UserProfile

import System.Drive.Errors_Events.EventMan as EV
global cwd
cwd = User.UserProfile.SourceDirectory
import tkinter as tk
import os

def do_something_with_value(value):
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    from urllib.parse import urlparse

    def is_url(string):
        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        parsed_url = urlparse(string)
        return bool(parsed_url.scheme)

    if is_url(string=value):
        install_window.destroy()
        try:
            Installer(value)
        except:
            EV.guiEvent(0,
                        f'{get_current_function()} Error: Package Installer Failed {value}',
                        inspect.currentframe().f_lineno,
                        os.path.abspath(__file__), False, True,
                        4)
    else:
        Files0 = []
        ImportDirectory = value
        for path in os.listdir(ImportDirectory):
            if os.path.isfile(os.path.join(ImportDirectory, path)):
                Files0.append(path)

        counter = 0
        for file in Files0:
            counter += 1
            print(f'{counter} | {file}')

        def button_click(item):
            EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
            root.destroy()
            fi = Files0.index(item)
            fi = Files0[int(fi)]

            fe = fi.split('.', 1)
            if len(fe) > 0:
                ffi = fe[1]

            if 'py' in ffi:
                p1 = f'+{ImportDirectory} ≈python3 {ImportDirectory}/{fi}*'
            elif ffi == '.c':
                p1 = f'+{ImportDirectory} ≈gcc {ImportDirectory}/{fi}*'
            elif 'cpp' in ffi:
                p1 = f'+{ImportDirectory} ≈gpp {ImportDirectory}/{fi}*'
            elif 'sh' in ffi:
                p1 = f'+{ImportDirectory} ≈bash {ImportDirectory}/{fi}*'

            Form = f'{fi[:-3]} = "{p1}"'

            f = open(f'{cwd}System/.Cache/System/Local/Int.txt', 'a')
            f.write(f'\n{Form}')
            f.close()
            AR.AnalyticsRecord(1)
            import User

            print('Installation Complete!')
            os.chdir(User.UserProfile.SourceDirectory)

        root = tk.Tk()
        root.title('Local Installer')

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = 440
        window_height = 460
        root.config(bg='#C5E0DC')
        x_coordinate = (screen_width // 2) - (window_width // 2)
        y_coordinate = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        item_list = Files0

        style = ttk.Style()
        style.configure('Custom.TButton', font=('Helvetica', 12), padding=10, background='#DF5D22', foreground='white')



        for item in item_list:
            ttk.Button(
                root,
                text=item,
                command=lambda i=item: button_click(i),
                style='Custom.TButton'
            ).pack(pady=5)

        root.mainloop()


def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name

def show_install():
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    try:
        os.mkdir(f'{cwd}System/.Cache/System/GitHub/Downloads')
    except:
        EV.guiEvent(0,
                    f'{get_current_function()} Downloads Dir Already Exists',
                    inspect.currentframe().f_lineno,
                    os.path.abspath(__file__), False, True,
                    3)

    global install_window

    from tkinter import filedialog
    from tkinter import ttk

    def choose_folder():
        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        folder_path = filedialog.askdirectory()
        install_entry.insert(0, folder_path)

    # Create a Toplevel window for the installation
    install_window = tk.Tk()
    install_window.title('Install')
    install_window.grab_set()
    # Set window size and position
    screen_width = install_window.winfo_screenwidth()
    screen_height = install_window.winfo_screenheight()
    window_width = 440
    window_height = 460

    alpha_value = 0.93  # Adjust the alpha value as needed

    install_window.attributes("-alpha", alpha_value)

    # Create a canvas to act as the window's background with a colored rectangle
    canvas = tk.Canvas(install_window, width=526, height=505)

    # Set the canvas background color
    bg_color = '#EE85B5'
    canvas.create_rectangle(0, 0, 526, 505, fill=bg_color, outline="")

    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    install_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Define the container frame within the installation window
    install_frame = tk.Frame(install_window, bg='#EE85B5', bd=2, relief=tk.SOLID)
    install_frame.pack(padx=20, pady=20)

    # Create the installation label with custom font and padding
    install_label = tk.Label(
        install_frame,
        text='Enter a path to a local directory or a GitHub repository URL:',
        bg="#A6D8CD",
        font=('Helvetica', 12, 'bold'),
        padx=10,
        pady=10
    )
    install_label.pack()

    # Create the installation entry field with custom font and padding
    install_entry = tk.Entry(
        install_frame,
        font=('Helvetica', 12),
        bd=2,
        relief=tk.SOLID
    )
    install_entry.pack(pady=10)

    # Create the "Choose folder" button with custom styling
    choose_folder_button = ttk.Button(
        install_frame,
        text='Choose Folder',
        command=choose_folder,
        style='Custom.TButton'
    )
    choose_folder_button.pack(pady=10)

    # Create the "Submit" button with custom styling
    install_submit = ttk.Button(
        install_frame,
        text='Submit',
        command=lambda: do_something_with_value(install_entry.get()),
        style='Custom.TButton'
    )
    install_submit.pack(pady=20)

    # Create the installation label with custom font and padding
    installer_label = tk.Label(
        install_frame,
        text='''--Requirements Auto Install
--Packages can be updated later
--Local dirs cannot be deleted through GHPM
--Read .cache files if you want edit commands
fp: System/.Cache/System/Local/Int.txt''',
        bg="#A6D8CD",
        font=('Helvetica', 12, 'bold'),
        padx=10,
        pady=10
    )
    installer_label.pack()

    # Define custom styles for the buttons
    install_window.tk.call('source', 'azure.tcl')  # Load custom styling file
    install_window.tk.call('set_theme', 'light')  # Set the theme to light
    install_window.tk.call(
        'ttk::style', 'configure', 'Custom.TButton',
        '-padding', '10 5',
        '-background', '#DF5D22',
        '-foreground', 'white',
        '-font', 'Helvetica 12',
        '-relief', 'raised'
    )

    install_window.mainloop()



def Installer(value):
    import System.Drive.Errors_Events.EventMan as EV
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    import os

    cwd = User.UserProfile.SourceDirectory
    print('checkpoint')
    dir = f'{cwd}System/.Cache/System/GitHub/Downloads'
    try:
        os.mkdir(dir)
        EV.guiEvent(0, 'Download dir made', inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 1)
    except:
        EV.guiEvent(0, f'{get_current_function()} download dir already exists',
                    inspect.currentframe().f_lineno,
                    os.path.abspath(__file__), False, True,
                    1)
    print(dir)
    os.chdir(dir)
    print('checkpoint')
    Download_Source = value
    SourceURI = value
    print('[!] CheckPoint 1|4 [!]')
    EV.guiEvent(0, f'downloading from {Download_Source}', inspect.currentframe().f_lineno, os.path.abspath(__file__),
                False, True, 2)
    Files = []
    for path in os.listdir(cwd):
        # check if current path is a file
        if os.path.isfile(os.path.join(cwd, path)):
            Files.append(path)

    SDir = list(filter(os.path.isdir, os.listdir(os.curdir)))

    try:  # downloading from GitHub
        import System.Drive.Errors_Events.EventMan as EV
        import uuid

        EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Installation', a3=f'downloadined_from={Download_Source}')
        os.system(f"git clone '{Download_Source}'")
        EV.guiEvent(0, f'{get_current_function()} download complete', inspect.currentframe().f_lineno,
                    os.path.abspath(__file__), False, True,
                    1)
        print('[!] CheckPoint 2|4 [!]')

        Files1 = []
        for path in os.listdir(cwd):
            # check if current path is a file
            if os.path.isfile(os.path.join(cwd, path)):
                Files1.append(path)

        SDir1 = list(filter(os.path.isdir, os.listdir(os.curdir)))

        for x in Files1:
            if x in Files:
                pass
            else:
                #
                pass  # event=f'Package Downloaded: {x}', Pol=0)

        for y in SDir1:
            if y in SDir:
                pass
            else:
                print('[!] CheckPoint 3|4 [!]')
                dir1 = f'{cwd}System/.Cache/System/GitHub/Downloads/{y}'

                ChangeDir = dir1

                Files0 = ['Complex Installation']
                for path in os.listdir(dir1):
                    # check if current path is a file
                    if os.path.isfile(os.path.join(dir1, path)):
                        Files0.append(path)

                import tkinter as tk

                def button_click(item):
                    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
                    root.destroy()
                    fi = Files0.index(item)
                    print(fi)

                    if fi == 0:
                        AR.AnalyticsRecord(2)
                        import tkinter as tk
                        import os
                        from tkinter import messagebox

                        import tkinter.messagebox as messagebox

                        def complexgather():
                            EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True,
                                        1)

                            def set_values():
                                EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False,
                                            True, 1)
                                field1_value = field1.get()
                                field2_value = field2.get()
                                field3_value = field3.get()
                                field4_value = field4.get()
                                field5_value = field5.get()
                                field6_value = field6.get()

                                values = [
                                    field1_value,
                                    field2_value,
                                    field3_value,
                                    field4_value,
                                    field5_value,
                                    field6_value,
                                ]

                                import tkinter as tk



                                for value in values:
                                    print(f'{values.index(value)} : {value}')
                                    # Call the function to show the notification

                                try:
                                    # Change the current working directory

                                    messagebox.showinfo(f"Hold Tight! We're installing {os.path.basename(dir1)}")
                                    command = (f'cd {dir1} && {field2_value}', f'cd {dir1} && {field3_value}', f'cd {dir1} && {field4_value}', f'cd {dir1} && {field5_value}', f'cd {dir1} && {field6_value}')
                                    for i in command:
                                        print(f'running command : {i}')
                                        subprocess.call(i, shell=True)



                                except:
                                    EV.guiEvent(0,
                                                f'{get_current_function()} Error: Project Was Downloaded But Requirements or Permissions Not Installed',
                                                inspect.currentframe().f_lineno,
                                                os.path.abspath(__file__), False, True,
                                                3)

                                ComplexLcaunch = open(
                                    f'{cwd}System/.Cache/System/GitHub/Complex',
                                    'a',
                                )
                                ComplexLcaunch.write(
                                    f'\n{dir1}${field1_value}'
                                )
                                Complexinstall = open(
                                    f'{cwd}System/.Cache/System/GitHub/Complex_install',
                                    'a',
                                )
                                Complexinstall.write(
                                    f'{field3_value}\n{dir1}\n{field4_value}\n{field5_value}\n{field6_value}')
                                ComplexLcaunch.close()
                                Complexinstall.close()
                                root.destroy()
                                print('Successful Install')

                            root = tk.Tk()
                            root.title('Complex Installation')
                            screen_width = root.winfo_screenwidth()
                            screen_height = root.winfo_screenheight()
                            window_width = 440
                            window_height = 460
                            x_coordinate = (screen_width // 2) - (window_width // 2)
                            y_coordinate = (screen_height // 2) - (window_height // 2)
                            root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
                            root.config(bg='#4e073a')

                            field1_value = tk.StringVar()
                            field1_label = tk.Label(
                                root,
                                text='*required Launch Command (ie. bash ./exe.sh',
                            )
                            field1 = tk.Entry(
                                root, textvariable=field1_value
                            )
                            field1_label.pack()
                            field1.pack()

                            field2_value = tk.StringVar()
                            field2_label = tk.Label(
                                root,
                                text='Requirements Command (ie. pip install /)',
                            )
                            field2 = tk.Entry(
                                root, textvariable=field2_value
                            )
                            field2_label.pack()
                            field2.pack()

                            field3_value = tk.StringVar()
                            field3_label = tk.Label(
                                root,
                                text='Privileges Command (ie. chmod -x)',
                            )
                            field3 = tk.Entry(
                                root, textvariable=field3_value
                            )
                            field3_label.pack()
                            field3.pack()

                            field4_value = tk.StringVar()
                            field4_label = tk.Label(
                                root, text='Install Command 1'
                            )
                            field4 = tk.Entry(
                                root, textvariable=field4_value
                            )
                            field4_label.pack()
                            field4.pack()

                            field5_value = tk.StringVar()
                            field5_label = tk.Label(
                                root, text='Install Command 2'
                            )
                            field5 = tk.Entry(
                                root, textvariable=field5_value
                            )
                            field5_label.pack()
                            field5.pack()

                            field6_value = tk.StringVar()
                            field6_label = tk.Label(
                                root, text='Install Command 3'
                            )
                            field6 = tk.Entry(
                                root, textvariable=field6_value
                            )
                            field6_label.pack()
                            field6.pack()

                            submit_button = tk.Button(
                                root, text='Set', command=set_values
                            )
                            submit_button.pack()

                            root.mainloop()

                        complexgather()

                    else:
                        AR.AnalyticsRecord(0)
                        fi = Files0[int(fi)]

                        dashID = [
                            'Requests.txt',
                            'Requirements.txt',
                            'requests.txt',
                            'Requirements.txt',
                        ]
                        try:
                            for dash in dashID:
                                if dash in Files0:
                                    dash = f'{dir1}/{dash}'
                                    dash1 = (
                                        f'python3 -m pip install -r {dash}'
                                    )
                                    import os
                                    try:
                                        os.system(dash1)

                                        print('Requirements Installed')
                                    except:
                                        EV.guiEvent(0,
                                                    f'{get_current_function()} Error: Requirements or Permissions Not Installed',
                                                    inspect.currentframe().f_lineno,
                                                    os.path.abspath(__file__), False, True,
                                                    3)
                        except:
                            EV.guiEvent(0,
                                        f'{get_current_function()} No requirements found',
                                        inspect.currentframe().f_lineno,
                                        os.path.abspath(__file__), False, True,
                                        2)

                        ch = '.'
                        # Remove all characters before the character '-' from string
                        listOfWords = fi.split(ch, 1)
                        if len(listOfWords) > 0:
                            ffi = listOfWords[1]

                        if ffi == 'py':
                            launch = f'&python3 {fi}'

                            tier = f'&python3 {dir1}/{fi}'
                            print('[!] CheckPoint 4|4 [!]')
                            print(launch)
                            import time
                            Form = f'{ChangeDir}@{fi[:-3]} = {launch}%{SourceURI}#{datetime.datetime.today()}'
                            #

                            pass  # event=f'Launch Command Created: {Form}', Pol=0)
                            cwdd = User.UserProfile.SourceDirectory
                            f = open(
                                f'{cwdd}System/.Cache/System/GitHub/Int.txt',
                                'a',
                            )
                            f.write(f'\n{Form}')
                            f.close()
                            print('Installation Complete!')

                        elif ffi == 'c':
                            launch = f'&gcc {fi}'

                            print('[!] CheckPoint 4|4 [!]')
                            print(launch)
                            import time
                            Form = f'{ChangeDir}@{fi[:-3]} = {launch}%{SourceURI}#{datetime.datetime.today()}'
                            #

                            pass  # event=f'Launch Command Created: {Form}', Pol=0)
                            cwdd = User.UserProfile.SourceDirectory
                            f = open(
                                f'{cwdd}System/.Cache/System/GitHub/Int.txt',
                                'a',
                            )
                            f.write(f'\n{Form}')
                            f.close()
                            print('Installation Complete!')

                        elif ffi == 'cpp':
                            launch = f'&g++ {fi}'

                            print('[!] CheckPoint 4|4 [!]')
                            print(launch)
                            import time
                            Form = f'{ChangeDir}@{fi[:-3]} = {launch}%{SourceURI}#{datetime.datetime.today()}'
                            #

                            pass  # event=f'Launch Command Created: {Form}', Pol=0)
                            import User.UserProfile as UP

                            cwdd = UP.SourceDirectory
                            f = open(
                                f'{cwdd}System/.Cache/System/GitHub/Int.txt',
                                'a',
                            )
                            f.write(f'\n{Form}')
                            f.close()
                            print('Installation Complete!')

                        elif ffi == 'sh':
                            launch = f'&bash {fi}'

                            print('[!] CheckPoint 4|4 [!]')
                            print(launch)
                            import time
                            Form = f'{ChangeDir}@{fi[:-3]} = {launch}%{SourceURI}#{datetime.datetime.today()}'
                            #

                            pass  # event=f'Launch Command Created: {Form}', Pol=0)
                            cwdd = User.UserProfile.SourceDirectory
                            f = open(
                                f'{cwdd}System/.Cache/System/GitHub/Int.txt',
                                'a',
                            )
                            f.write(f'\n{Form}')
                            f.close()
                            print('Installation Complete!')
                            import sys

                import tkinter as tk
                from tkinter import ttk

                root = tk.Tk()
                root.title('Installed Files')

                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                window_width = 440
                window_height = 460
                x_coordinate = (screen_width // 2) - (window_width // 2)
                y_coordinate = (screen_height // 2) - (window_height // 2)
                root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

                root.config(bg='#C5E0DC')

                item_list = Files0

                # Define custom button style
                style = ttk.Style()
                style.configure('Custom.TButton', font=('Helvetica', 12), padding=10, background='#DF5D22',
                                foreground='white')


                for item in item_list:
                    ttk.Button(
                        root,
                        text=item,
                        command=lambda i=item: button_click(i),
                        style='Custom.TButton'
                    ).pack(pady=5)

                root.mainloop()
                root.destroy()


    except:
        EV.guiEvent(0,
                    f'{get_current_function()} Error: Project Was Not Installed',
                    inspect.currentframe().f_lineno,
                    os.path.abspath(__file__), False, True,
                    3)
