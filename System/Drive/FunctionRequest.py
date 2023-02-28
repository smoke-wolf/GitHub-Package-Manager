import datetime

global os
import sys
import time
import User.UserProfile

global cwd

cwd = User.UserProfile.SourceDirectory

def GH():
    import User

    cwd = User.UserProfile.SourceDirectory
    spacer = '==============='
    #

    import os

    pass  # event=f'Inp = GitHub', Pol=1)

    with open(f'{cwd}System/.Cache/System/GitHub/int.txt', 'r') as r, open(
            f'{cwd}System/.Cache/System/GitHub/int2.txt', 'w'
    ) as o:
        for line in r:
            if line.strip():
                o.write(line)

    f = open(f'{cwd}System/.Cache/System/GitHub/int2.txt', 'r')

    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1

    options = []
    count1 = 0
    lines_r = []
    for line in lines:
        value4 = line.strip()
        lines_r.append(value4)
        Val = value4.split('&', 1)
        if len(Val) > 0:
            value4 = Val[1]
        count1 += 1

        options.append(value4.split("%", 1)[0])

    import tkinter
    from tkinter import ttk

    window = tkinter.Tk()
    window.title('Activate one of the following')
    window.geometry("400x300")

    # Create the list of options

    # Create a function to be called when the user selects an option
    def select_option(selected_option):
        window.destroy()
        print('Selected Option:', selected_option)

        value = lines[int(options.index(selected_option))]
        print(value)
        cc = value
        listOfWords = value.split('&', 1)
        if len(listOfWords) > 0:
            value = listOfWords[1]

        value = value.split('-', 1)[0]

        cc = cc.split('@', 1)[0]
        #

        cc = cc.split("%", 1)[0]
        pass  # event=f'Change Directory: {cc} ', Pol=0)
        try:
            #

            pass  # event=f'DirChange = Success! ', Pol=0)
            pass  # event=f'os executed command [!]{value}[!] ', Pol=0)
            try:
                os.system(
                    f'osascript -e \'tell application "Terminal" to do script "cd {cc}&&{selected_option}"\''
                )
            except:
                pass

        except:
            #

            pass  # event=f'DirChange = Failed ', Pol=0)

    # Display the list of options in the window

    def updated(selected_option, source):
        value = lines[int(options.index(selected_option))]
        print(value)
        cc = value
        listOfWords = value.split('&', 1)
        if len(listOfWords) > 0:
            value = listOfWords[1]

        value = value.split('-', 1)[0]

        cc = cc.split('@', 1)[0]
        #

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
                os.system(f'git clone {source}')
                messagebox.showinfo("Update Successful", "has been successfully updated.")
            except:
                sys.exit()
        except:
            import tkinter as tk
            from tkinter import messagebox
            print(f'')
            messagebox.showinfo("Update Failed", f"Update Failed {source}")

    def open_option_window(event, option):
        option_window = tkinter.Toplevel()
        option_window.title(option)
        option_window.geometry("300x200")

        for line in lines_r:
            if option in line:

                Val = line.split('#', 1)
                if len(Val) > 0:
                    global date
                    date = Val[1]

                Val = line.split('%', 1)
                if len(Val) > 0:
                    global source
                    source = Val[1]

        information = f'''
        Date downloaded: {date}
        Downloaded from: {source.split("#", 1)[0]}
        '''

        # Create a label with the information
        info_label = ttk.Label(option_window, text=information)
        info_label.pack(pady=10)

        # Create the buttons
        launch_button = ttk.Button(option_window, text="Launch", command=lambda opt=option: select_option(opt))
        launch_button.pack(pady=5)

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

    # Start the window event loop
    window.mainloop()
def Activate():
    print(cwd)
    import tkinter as tk
    from tkinter import messagebox
    result1 = messagebox.askyesno(
        'User GitHub Check', 'Use GitHub applications?'
    )
    if result1:
        GH()
    else:
        result2 = messagebox.askyesno(
            'User GitHub Check', 'Use Local applications?'
        )

        if result2:
            options = []

            #

            with open(
                    f'{cwd}System/.Cache/System/Local/Int.txt', 'r'
            ) as r, open(
                f'{cwd}System/.Cache/System/Local/Int2.txt', 'w'
            ) as o:
                for line in r:
                    if line.strip():
                        o.write(line)
            f = open(f'{cwd}System/.Cache/System/Local/Int2.txt', 'r')

            lines = f.readlines()
            count = 0
            for line in lines:
                count += 1

            count1 = 0
            for line in lines:
                count1 += 1
                options.append(line.strip())

            import tkinter

            window = tkinter.Tk()
            window.title('Activate one of the following')

            # Create the list of options

            # Create a function to be called when the user selects an option

            def select_option(selected_option):
                window.destroy()
                print('Selected Option:', selected_option)

                #

                pass  # event=f'{count1}={count} --COMMAND LINE', Pol=0)
                value = lines[int(options.index(selected_option))]
                listOfWords = value.split('-', 1)
                if len(listOfWords) > 0:
                    valueg = listOfWords[1]
                    print(valueg)

                #

                pass  # event=f'Creating value1 --COMMAND LINE', Pol=0)
                try:
                    value1 = value.split(f'@', 1)[0]
                    Str = value1[: len(value1) - 1]
                    #

                    pass  # event=f'Success: {Str} --COMMAND LINE', Pol=0)
                except:
                    value1 = value.split(f'@', 1)[0]
                    #

                    pass  # event=f'Failure: {value1} --COMMAND LINE', Pol=0)

                listOfWords = value.split('+', 1)
                if len(listOfWords) > 0:
                    value = listOfWords[1]

                value = value.split('-', 1)[0]

                try:
                    print(valueg[:-2])
                    print(value)
                    os.system(
                        f'osascript -e \'tell application "Terminal" to do script "cd {value} && {valueg[:-2]}"\''
                    )
                    #

                    pass  # event=f'Command Executed [!]{value}[!] --COMMAND LINE', Pol=0)
                except:
                    pass

            for option in options:
                b = tkinter.Button(
                    window,
                    text=option,
                    command=lambda opt=option: select_option(opt),
                )
                b.pack()

            # Start the window event loop
            window.mainloop()

        else:
            result3 = messagebox.askyesno(
                'User Advanced Check', 'Use Advanced GitHub applications?'
            )
            if result3:
                options = []
                with open(
                        f'{cwd}System/.Cache/System/GitHub/Complex', 'r'
                ) as r, open(
                    f'{cwd}System/.Cache/System/GitHub/Complex2', 'w'
                ) as o:
                    for line in r:
                        if line.strip():
                            o.write(line)

                f = open(f'{cwd}System/.Cache/System/GitHub/Complex2', 'r')

                linesd = f.readlines()
                count = 0
                for line in linesd:
                    count += 1

                count1 = 0
                for line in linesd:
                    value4 = line.strip()
                    count1 += 1
                    options.append(value4)

                import tkinter

                window = tkinter.Tk()
                window.title('Activate one of the following')

                def select_option(selected_option):
                    print('Selected Option:', selected_option)

                    def submit():
                        name = entry_name.get()
                        window2.destroy()
                        window.destroy()
                        Arges = name

                        B = value.split('$', 1)[0]

                        # Remove all characters before the character '-' from string
                        lis = value.split('$', 1)
                        if len(lis) > 0:
                            lis = lis[1]

                        A = f'{lis} {Arges}'

                        r = open(
                            f'{cwd}System/.Cache/System/GitHub/Complex_install',
                            'r',
                        )
                        lines = r.readlines()
                        try:
                            for line in lines:
                                try:
                                    #
                                    pass  # event=f'Command {line}', Pol=0)
                                    os.system(line)
                                except:
                                    #
                                    pass  # event=f'Command failed ', Pol=0)
                                    exit(0)

                            open(
                                f'{cwd}System/.Cache/System/GitHub/Complex_install',
                                'w',
                            )

                        except:
                            pass

                        try:
                            os.system(
                                f'osascript -e \'tell application "Terminal" to do script "cd {B}&&{A}"\''
                            )
                            #
                            pass  # event=f'Launch Success! ', Pol=0)
                        except:
                            pass

                    value = selected_option
                    window2 = tk.Tk()
                    window2.title('Package Inform')

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
                    b = tkinter.Button(
                        window,
                        text=option,
                        command=lambda opt=option: select_option(opt),
                    )
                    b.pack()

                # Create the list of options

                # Create a function to be called when the user selects an option

                # Start the window event loop

            else:
                pass

def GUI():
    import tkinter as tk
    from tkinter import messagebox

    global directories
    directories = []
    from tkinter import simpledialog

    global os
    import os
    import sys
    import User.UserProfile

    global cwd
    cwd = User.UserProfile.SourceDirectory

    os.system(
        """osascript -e 'tell application "Terminal" to set visible of window 1 to false' """
    )

    def Installer(value):
        import os

        print('https://github.com/smoke-wolf/GitHub-Package-Manager.git')


        cwd = User.UserProfile.SourceDirectory
        csw = os.getcwd()
        print('checkpoint')
        dir = f'{csw}/System/.Cache/System/GitHub/Downloads'
        try:
            os.mkdir(dir)
        except:
            pass
        os.chdir(dir)
        print('checkpoint')
        Download_Source = value
        SourceURI = value
        print('[!] CheckPoint 1|4 [!]')

        Files = []
        for path in os.listdir(cwd):
            # check if current path is a file
            if os.path.isfile(os.path.join(cwd, path)):
                Files.append(path)

        SDir = list(filter(os.path.isdir, os.listdir(os.curdir)))

        try:  # downloading from GitHub
            os.system(f"git clone '{Download_Source}'")

            print('[!] CheckPoint 2|4 [!]')
            #

            pass  # event=f'Downloaded from Github', Pol=0)
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
                        root.destroy()
                        fi = Files0.index(item)
                        print(fi)

                        if fi == 0:
                            import tkinter as tk
                            import os

                            import tkinter as tk
                            import os
                            from tkinter import messagebox

                            import tkinter.messagebox as messagebox

                            def complexgather():
                                def set_values():
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

                                    tool = f'{field3_value}\n{dir1}\n{field4_value}\n{field5_value}\n{field6_value}'
                                    print('the tool')
                                    print(field3_value)
                                    try:
                                        os.system(field2_value)
                                        os.system(field3_value)
                                    except:
                                        print(
                                            'Error: Project Was Downloaded But Requirements or Permissions Not Installed'
                                        )

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
                                    Complexinstall.write(tool)
                                    ComplexLcaunch.close()
                                    root.destroy()
                                    print('Successful Install')

                                root = tk.Tk()
                                root.title('Complex Installation')

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
                                        try:
                                            os.system(dash1)

                                            print('Requirements Installed')
                                        except:
                                            pass
                            except:
                                print('No Requirements found')

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

                                sys.exit(0)

                    root = tk.Tk()

                    item_list = Files0

                    for item in item_list:
                        tk.Button(
                            root,
                            text=item,
                            command=lambda i=item: button_click(i),
                        ).pack()

                    root.mainloop()
                    os.chdir(User.UserProfile.SourceDirectory[:-1])



        except:
            print('Something went wrong, cleaning up')

    def show_information():
        close_windows()
        info_window = tk.Toplevel(root)
        info_window.title('Information')
        info_window.geometry('+{}+0'.format(-info_window.winfo_width()))

        info_text = 'GHPM is a package manager, it effectively manages coding projects, applications, and anything else code-able!\n GHPM does not use any highly advanced coding techniques, much the opposite in fact. it uses basic, straight-forward logic,\n it is the lack of complication that makes this project the most light-weight Manager available.'

        label = tk.Label(info_window, text=info_text, padx=20, pady=20)
        label.pack()

        okay_button = tk.Button(
            info_window, text='Okay', command=info_window.destroy
        )
        okay_button.pack()

        def slide_in():
            for x in range(-info_window.winfo_width(), 0, 5):
                info_window.geometry('+{}+0'.format(x))
                info_window.update()
            okay_button.config(state=tk.NORMAL)

        okay_button.config(state=tk.DISABLED)
        info_window.after(0, slide_in)
        slide_in()

    def reset_all():
        import tkinter as tk
        from tkinter import simpledialog

        root = tk.Tk()
        root.withdraw()

        import User.UserProfile

        # require USER_PASS
        import os, time

        pass

        Input = simpledialog.askstring(
            'Password', 'Enter your password:', show='*'
        )
        sd = User.UserProfile.SourceDirectory[:-1]
        try:
            import System.Drive.Password as PS

            PS.Password(Event='Cache', Input=Input)
            messagebox.showinfo('Password', 'Correct Password')
            time.sleep(0.23)
            try:
                open(f'{cwd}/System/.Cache/System/GitHub/Int.txt', 'w').close()
                print('|  |                Int.txt Cleared')
                import shutil

                user = User.UserProfile.Username
                shutil.rmtree(f'{cwd}/System/.Cache/System/Local')
                os.mkdir(f'{cwd}/System/.Cache/System/Local')
                shutil.rmtree(f'{cwd}/System/.Cache/System/GitHub')
                os.mkdir(f'{cwd}/System/.Cache/System/GitHub')

                open(f'{cwd}/System/.Cache/System/ErrorLog/Events', 'w').close()
                open(f'{cwd}/System/.Cache/System/ErrorLog/Event.db', 'w').close()
                open(f'{cwd}/System/.Cache/System/ErrorLog/Errors', 'w').close()

                open(f'{cwd}/System/.Cache/User/FirstUseToken.txt', 'w').close()
                open(f'{cwd}/User/UserProfile.py', 'w').close()
                open(f'{cwd}/System/.Cache/User/local', 'w').close()

                print(f'|  |                Update Recorded')
            except:
                messagebox.showerror('Password', 'Incorrect Password')
                pass  # event=f'Everything Failed To Reset Due To Password Error', Pol=0)
                raise exit(0)

            time.sleep(2)
            print(f'\n' * 60)

        except:
            messagebox.showerror('Password', 'Incorrect Password')
            Input = simpledialog.askstring(
                'Password', 'Enter your password:', show='*'
            )

            try:
                import System.Drive.Password as PS

                PS.Password(Event='Cache', Input=Input)
                messagebox.showinfo('Password', 'Correct Password')
                try:
                    open(f'{cwd}/System/.Cache/System/GitHub/Int.txt', 'w').close()
                    print('|  |                Int.txt Cleared')
                    import shutil

                    user = User.UserProfile.Username
                    shutil.rmtree(f'{cwd}/System/.Cache/System/Local')
                    os.mkdir(f'{cwd}/System/.Cache/System/Local')
                    shutil.rmtree(f'{cwd}/System/.Cache/System/GitHub')
                    os.mkdir(f'{cwd}/System/.Cache/System/GitHub')

                    open(f'{cwd}/System/.Cache/System/ErrorLog/Events', 'w').close()
                    open(f'{cwd}/System/.Cache/System/ErrorLog/Event.db', 'w').close()
                    open(f'{cwd}/System/.Cache/System/ErrorLog/Errors', 'w').close()

                    open(f'{cwd}/System/.Cache/User/FirstUseToken.txt', 'w').close()
                    open(f'{cwd}/User/UserProfile.py', 'w').close()
                    open(f'{cwd}/System/.Cache/User/local', 'w').close()
                    print(f'|  |                Update Recorded')
                except:
                    messagebox.showerror('Password', 'Incorrect Password')
                    pass  # event=f'Everything Failed To Reset Due To Password Error', Pol=0)
                    raise exit(0)

                time.sleep(2)
                print(f'\n' * 60)

            except:
                messagebox.showinfo('Password', 'Final Attempt')
                Input = simpledialog.askstring(
                    'Password', 'Enter your password:', show='*'
                )

                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Cache', Input=Input)
                    messagebox.showinfo('Password', 'Correct Password')
                    try:
                        open(f'{cwd}/System/.Cache/System/GitHub/Int.txt', 'w').close()
                        print('|  |                Int.txt Cleared')
                        import shutil

                        user = User.UserProfile.Username
                        shutil.rmtree(f'{cwd}/System/.Cache/System/Local')
                        os.mkdir(f'{cwd}/System/.Cache/System/Local')
                        shutil.rmtree(f'{cwd}/System/.Cache/System/GitHub')
                        os.mkdir(f'{cwd}/System/.Cache/System/GitHub')

                        open(f'{cwd}/System/.Cache/System/ErrorLog/Events', 'w').close()
                        open(f'{cwd}/System/.Cache/System/ErrorLog/Event.db', 'w').close()
                        open(f'{cwd}/System/.Cache/System/ErrorLog/Errors', 'w').close()

                        open(f'{cwd}/System/.Cache/User/FirstUseToken.txt', 'w').close()
                        open(f'{cwd}/User/UserProfile.py', 'w').close()
                        open(f'{cwd}/System/.Cache/User/local', 'w').close()
                        print(f'|  |                Update Recorded')
                    except:
                        pass  # event=f'Everything Failed To Reset Due To Password Error', Pol=0)
                        raise exit(0)

                    time.sleep(2)
                    print(f'\n' * 60)
                except ValueError:
                    #

                    pass  # event=f'Full reset failed due to user pass', Pol=1)

    def Create():
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
        up = open(f'{os.getsd()}/User/UserProfile.py', 'a')
        up.write(f"\nPassword = '{Password}'")
        print(Password)

    def settings_window():
        import User
        settings_win = tk.Toplevel(root)
        settings_win.title('Settings')
        sd = User.UserProfile.SourceDirectory[:-1]
        options = [
            'Toggle Forced Module Import',
            'Toggle Forced Login',
            'Toggle System Event display',
            'Enable Command Line Interface',
            'Change UserName',
            'Change Password',
            'reset all',
        ]

        def do_something(index):
            if index == 0:
                # require USER_PASS
                import os, time



                Input = simpledialog.askstring('GHPM', 'Enter Password: ')
                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Forced Login', Input=Input)

                    try:
                        with open(f'{os.getcwd()}/User/UserProfile.py', 'a') as file:
                            pass
                    except:
                        pass

                    import User.UserProfile as up
                    if up.Force_Import_Request is True:
                        Status = False

                    else:
                        Status = True

                    fileid = open(f'{os.getcwd()}/User/UserProfile.py', 'a')
                    fileid.write(f'\nForce_Import_Request = {Status}')
                    fileid.close()

                    messagebox.showinfo('GHPM', 'Update Recorded')
                    time.sleep(2)

                except:
                    Input = simpledialog.askstring('GHPM', 'Enter Password: ')
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
                        messagebox.showinfo('Final Attempt')
                        Input = simpledialog.askstring(
                            'GHPM', 'Enter Password: '
                        )
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
                            messagebox.showinfo('GHPM', 'Incorrect Password')

            elif index == 1:
                # require USER_PASS
                import os, time

                pass
                Input = simpledialog.askstring('GHPM', 'Enter Password: ')
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
                    Input = simpledialog.askstring('GHPM', 'Enter Password: ')
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
                        messagebox.showinfo('Final Attempt')
                        Input
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
                            messagebox.showinfo(
                                'GHPM', 'Wrong Password Entered'
                            )
                            pass

                #

                pass  # event=f'Updated Canceled', Pol=0)

            elif index == 2:
                pass  # event=f'Launching Event Display', Pol=1)
                target = open(f'{sd}/User/UserProfile.py', 'a')
                import User

                Cstat = User.UserProfile.DisplayEvents
                if Cstat is True:
                    status = False
                else:
                    status = False

                target.write(f'\nDisplayEvents = {status}')
                messagebox.showinfo('Update', f'DisplayEvents set to {status}')

            elif index == 3:
                import os

                pass  # event='Creating Global Alias', Pol=10)
                import User

                alias = f"""echo 'alias gh="cd {User.UserProfile.SourceDirectory} &&python3 gh.py"' >> ~/.zshrc && exec zsh -l"""
                try:
                    print(alais)
                    os.system(alias)
                    pass  # event='Installing Global Alias- Complete', Pol=20)
                except:
                    pass  # event='Error Installing Global Alias', Pol=20)

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
                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Password Update', Input=Input)
                    try:
                        import System.Drive.Password as ps

                        Create()
                    except:
                        pass
                except:
                    Input = simpledialog.askstring(
                        'Change Password', 'Enter your password:', show='*'
                    )
                    try:
                        import System.Drive.Password as PS

                        PS.Password(Event='Password Update', Input=Input)
                        try:
                            import System.Drive.Password as ps

                            Create()
                        except:
                            pass
                    except:
                        Input = simpledialog.askstring(
                            'Change Password', 'Enter your password:', show='*'
                        )
                        try:
                            import System.Drive.Password as PS

                            PS.Password(Event='Password Update', Input=Input)
                            try:
                                import System.Drive.Password as ps

                                Create()
                            except:
                                pass
                        except:
                            pass

            elif index == 6:
                reset_all()

        try:
            for i, option in enumerate(options):
                button = tk.Button(
                    settings_win,
                    text=option,
                    command=lambda i=i: do_something(i),
                )
                button.pack()
        except:
            pass

    def crypt():
        try:
            os.system(
                f'''osascript -e 'tell application "Terminal" to do script "cd {User.UserProfile.SourceDirectory[:-1]}&&python3 CLI.py"'
''')
        except:
            print('Version Complete')

    def show_install():
        try:
            os.mkdir(f'{sd}/System/.Cache/System/GitHub/Downloads')
        except:
            pass
        close_windows()
        global install_window

        from tkinter import filedialog
        from tkinter import ttk

        def choose_folder():
            folder_path = filedialog.askdirectory()
            install_entry.insert(0, folder_path)

        install_window = tk.Toplevel(root)
        install_window.geometry('400x400')
        install_window.title('Install')

        install_label = tk.Label(
            install_window,
            text='Enter a path to a local directory or a GitHub repository URL:',
        )
        install_label.pack()

        install_entry = tk.Entry(install_window)
        install_entry.pack()

        choose_folder_button = ttk.Button(
            install_window, text='Choose folder', command=choose_folder
        )
        choose_folder_button.pack()

        install_submit = tk.Button(
            install_window,
            text='Submit',
            command=lambda: do_something_with_value(install_entry.get()),
        )
        install_submit.pack()

    def do_something_with_value(value):
        from urllib.parse import urlparse

        install_window.destroy()

        def is_url(string):
            parsed_url = urlparse(string)
            return bool(parsed_url.scheme)

        if is_url(string=value) is True:
            install_window.destroy()
            try:
                Installer(value)
            except:
                pass
        else:
            Files0 = []
            ImportDirectory = value
            for path in os.listdir(ImportDirectory):
                # check if current path is a file
                if os.path.isfile(os.path.join(ImportDirectory, path)):
                    Files0.append(path)
            #

            pass  # event=f'Files Connected --COMMAND LINE', Pol=0)

            counter = 0
            for file in Files0:
                counter += 1
                print(f'{counter} | {file}')

            def button_click(item):
                root.destroy()
                fi = Files0.index(item)

                fi = Files0[int(fi)]
                # Remove all characters before the character '-' from string
                fe = fi.split('.', 1)
                if len(fe) > 0:
                    ffi = fe[1]

                if 'py' in ffi:
                    p1 = f'+{ImportDirectory} -python3 {ImportDirectory}/{fi}*'
                if ffi == '.c':
                    p1 = f'+{ImportDirectory} -gcc {ImportDirectory}/{fi}*'
                elif 'cpp' in ffi:
                    p1 = f'+{ImportDirectory} -gpp {ImportDirectory}/{fi}*'
                elif 'sh' in ffi:
                    p1 = f'+{ImportDirectory} -bash {ImportDirectory}/{fi}*'

                print('[!] CheckPoint 4|4 [!]')

                Form = f'{fi[:-3]} = "{p1}"'
                #

                pass  # event=f'Launch Command Complete: {Form} --COMMAND LINE', Pol=0)

                f = open(f'{cwd}System/.Cache/System/Local/Int.txt', 'a')
                f.write(f'\n{Form}')
                f.close()
                import User

                print('Installation Complete!')
                os.chdir(User.UserProfile.SourceDirectory)

            root = tk.Tk()

            item_list = Files0

            for item in item_list:
                tk.Button(
                    root, text=item, command=lambda i=item: button_click(i)
                ).pack()

            root.mainloop()

    def confirm_uninstall(selected_item):
        import tkinter.messagebox

        result = tk.messagebox.askyesno(
            'Confirm Uninstall',
            'Are you sure you want to uninstall ' + selected_item + '?',
        )
        # remove a line containing a string
        list_window.destroy()

        valuee = items.index(selected_item)

        if valuee >= count:
            dr = int(valuee) - count
            command = lines2[dr - 1]
            print(command)

            try:
                #
                import shutil
                co = command.split('@', 1)[0]
                shutil.rmtree(co)

                #
                print(f'Project Removed {co}')
                pass  # event=f'DirRemoval = Success! {co}', Pol=0)

            except:
                print(f'Project Failed To Removed {co}')
                #
                pass  # event=f'DirRemoval = Failed ', Pol=0)

        else:
            with open(
                    f'{cwd}/System/.Cache/System/GitHub/int.txt', 'r'
            ) as file:
                lines5 = file.readlines()

            with open(
                    f'{cwd}/System/.Cache/System/GitHub/int.txt', 'w'
            ) as file:
                for linef in lines5:
                    # find() returns -1 if no match is found
                    if linef.find(selected_item) != -1:
                        pass
                    else:
                        file.write(linef)

            value = lines[int(valuee) - 1]
            cc = value
            listOfWords = value.split('&', 1)
            if len(listOfWords) > 0:
                value = listOfWords[1]

            value = value.split('-', 1)[0]

            cc = cc.split('@', 1)[0]

            listOfWords = cc.split('/Downloads', 1)

            if len(listOfWords) > 0:
                co = listOfWords[1]

            #
            pass  # event=f'Removing Directory: {cc}', Pol=0)
            try:
                #
                import shutil

                shutil.rmtree(
                    f'{os.getcwd()}/System/.Cache/System/GitHub/Downloads{co}'
                )

                #
                print('Project Removed')
                pass  # event=f'DirRemoval = Success! ', Pol=0)

            except:
                print('Project Failed To Removed')
                #
                pass  # event=f'DirRemoval = Failed ', Pol=0)

        tk.messagebox.showinfo(
            'Success', selected_item + ' has been uninstalled.'
        )
        return selected_item

    def show_list_window():
        close_windows()
        global list_window
        list_window = tk.Toplevel()
        list_window.geometry('300x300+200+200')
        list_window.title('Uninstall List')
        list = tk.Listbox(list_window)
        list.pack()
        global items
        items = []
        try:
            with open(f'{cwd}System/.Cache/System/GitHub/int.txt', 'r') as r, open(
                    f'{cwd}System/.Cache/System/GitHub/int2.txt', 'w'
            ) as o:
                for line in r:
                    if line.strip():
                        o.write(line)
        except:
            pass
        try:
            f = open(f'{cwd}System/.Cache/System/GitHub/int2.txt', 'r')
            e = open(f'{cwd}System/.Cache/System/GitHub/Complex2', 'r')
        except:
            pass

        global lines
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
            pass
        for item in items:
            list.insert(tk.END, item)
        confirm_button = tk.Button(
            list_window,
            text='Confirm Uninstall',
            command=lambda: confirm_uninstall(list.get(list.curselection())),
        )
        confirm_button.pack()

    def exit_program():
        sys.exit(0)

    def close_windows():
        pass

    global root
    root = tk.Tk()
    root.title('GHPM')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 437
    window_height = 400
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    root.geometry(
        '%dx%d+%d+%d'
        % (window_width, window_height, x_coordinate, y_coordinate)
    )
    root.config(bg='black')






    buttons = []

    button = tk.Button(
        root,
        text='Information',
        bg='gray',
        height=2,
        width=10,
        command=show_information,
    )
    button.grid(row=1, column=0, padx=10, pady=10)
    buttons.append(button)

    settings_button = tk.Button(
        root,
        text='Settings',
        bg='gray',
        height=2,
        width=10,
        command=settings_window,
    )
    settings_button.grid(row=1, column=1, padx=10, pady=10)
    buttons.append(button)

    button = tk.Button(
        root,
        text='Install',
        bg='gray',
        height=2,
        width=10,
        command=show_install,
    )
    button.grid(row=1, column=2, padx=10, pady=10)
    buttons.append(button)

    button = tk.Button(
        root, text='Activate', bg='gray', height=2, width=10, command=Activate
    )
    button.grid(row=2, column=0, padx=10, pady=10)
    buttons.append(button)

    button = tk.Button(
        root,
        text='Uninstall',
        bg='gray',
        height=2,
        width=10,
        command=show_list_window,
    )
    button.grid(row=2, column=1, padx=10, pady=10)
    buttons.append(button)

    button = tk.Button(
        root, text='Command Line Version', bg='gray', height=2, width=10, command=crypt
    )
    button.grid(row=2, column=2, padx=10, pady=10)
    buttons.append(button)

    button = tk.Button(
        root, text='EXIT', bg='red', height=2, width=10, command=exit_program
    )
    button.grid(row=4, column=1, padx=10, pady=10)
    root.mainloop()
