global os
import os
import random
import sys
import time
import System
import User.UserProfile

global cwd

cwd = User.UserProfile.SourceDirectory


def GUI():
    import sys
    import tkinter as tk
    from tkinter import messagebox

    global directories
    directories = []
    from tkinter import simpledialog
    import User

    global os
    import os
    import random
    import sys
    import time
    import System
    import User.UserProfile

    global cwd
    cwd = User.UserProfile.SourceDirectory

    os.system(
        """osascript -e 'tell application "Terminal" to set visible of window 1 to false' """
    )

    def Installer(value):
        import os

        import User.UserProfile

        os.chdir(User.UserProfile.SourceDirectory)
        cwd = User.UserProfile.SourceDirectory
        dir = f'{cwd}System/Cache/System/GitHub/Downloads'
        os.chdir(dir)
        Download_Source = value
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
                    dir1 = f'{cwd}System/Cache/System/GitHub/Downloads/{y}'

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
                                        f'{cwd}System/Cache/System/GitHub/Complex',
                                        'a',
                                    )
                                    ComplexLcaunch.write(
                                        f'\n{dir1}${field1_value}'
                                    )
                                    Complexinstall = open(
                                        f'{cwd}System/Cache/System/GitHub/Complex_install',
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
                                Form = f'{ChangeDir}@{fi[:-3]} = {launch}'
                                #

                                pass  # event=f'Launch Command Created: {Form}', Pol=0)
                                cwdd = User.UserProfile.SourceDirectory
                                f = open(
                                    f'{cwdd}System/Cache/System/GitHub/Int.txt',
                                    'a',
                                )
                                f.write(f'\n{Form}')
                                f.close()
                                print('Installation Complete!')

                            elif ffi == 'c':
                                launch = f'&gcc {fi}'

                                print('[!] CheckPoint 4|4 [!]')
                                print(launch)
                                Form = f'{ChangeDir}@{fi[:-3]} = {launch}'
                                #

                                pass  # event=f'Launch Command Created: {Form}', Pol=0)
                                cwdd = User.UserProfile.SourceDirectory
                                f = open(
                                    f'{cwdd}System/Cache/System/GitHub/Int.txt',
                                    'a',
                                )
                                f.write(f'\n{Form}')
                                f.close()
                                print('Installation Complete!')

                            elif ffi == 'cpp':
                                launch = f'&g++ {fi}'

                                print('[!] CheckPoint 4|4 [!]')
                                print(launch)
                                Form = f'{ChangeDir}@{fi[:-3]} = {launch}'
                                #

                                pass  # event=f'Launch Command Created: {Form}', Pol=0)
                                import User.UserProfile as UP

                                cwdd = UP.SourceDirectory
                                f = open(
                                    f'{cwdd}System/Cache/System/GitHub/Int.txt',
                                    'a',
                                )
                                f.write(f'\n{Form}')
                                f.close()
                                print('Installation Complete!')

                            elif ffi == 'sh':
                                launch = f'&bash {fi}'

                                print('[!] CheckPoint 4|4 [!]')
                                print(launch)
                                Form = f'{ChangeDir}@{fi[:-3]} = {launch}'
                                #

                                pass  # event=f'Launch Command Created: {Form}', Pol=0)
                                cwdd = User.UserProfile.SourceDirectory
                                f = open(
                                    f'{cwdd}System/Cache/System/GitHub/Int.txt',
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

    def toggle_forced_module_import():
        label = tk.Label(settings_window, text='Toggle Forced Module Import')
        label.pack(pady=20)

    def toggle_forced_login():
        label = tk.Label(settings_window, text='Toggle Forced Login')
        label.pack(pady=20)

    def toggle_system_event_display():
        label = tk.Label(settings_window, text='Toggle System Event Display')
        label.pack(pady=20)

    def enable_command_line_interface():
        label = tk.Label(settings_window, text='Enable Command Line Interface')
        label.pack(pady=20)

    def change_username():
        label = tk.Label(settings_window, text='Change UserName')
        label.pack(pady=20)

    def change_password():
        label = tk.Label(settings_window, text='Change Password')
        label.pack(pady=20)

    def reset():
        label = tk.Label(settings_window, text='reset all')
        label.pack(pady=20)

    def reset_all():
        import tkinter as tk
        from tkinter import simpledialog

        root = tk.Tk()
        root.withdraw()

        import User
        import User.UserProfile

        # require USER_PASS
        import os, time

        pass

        Input = simpledialog.askstring(
            'Password', 'Enter your password:', show='*'
        )

        try:
            import System.Drive.Password as PS

            PS.Password(Event='Cache', Input=Input)
            messagebox.showinfo('Password', 'Correct Password')
            try:
                open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
                print('|  |                Int.txt Cleared')
                import shutil

                user = User.UserProfile.Username
                shutil.rmtree(f'{cwd}/System/Cache/System/Local')
                os.mkdir(f'{cwd}/System/Cache/System/Local')
                print('|  |                Local Connections Reset')
                try:
                    shutil.rmtree(
                        f'{cwd}/System/Cache/System/GitHub/Downloads'
                    )
                except:
                    pass
                print('|  |                Downloads Reset')
                open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
                print('|  |                Events Cleared')
                open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
                print('|  |                Errors Cleared')
                open(f'{cwd}/System/Cache/User/FirstUseToken.txt', 'w').close()
                print('|  |                FirstUseToken added')
                open(f'{cwd}/User/UserProfile.py', 'w').close()
                print('|  |                User Profile Wiped')
                open(
                    f'{cwd}/System/Cache/System/GitHub/Complex_install', 'w'
                ).close()
                open(f'{cwd}/System/Cache/System/GitHub/Complex', 'w').close()
                open(f'{cwd}/System/Cache/System/GitHub/Complex2', 'w').close()
                open(f'{cwd}/System/Cache/System/GitHub/int2.txt', 'w').close()
                open(
                    f'{User.UserProfile.SourceDirectory}System/Cache/System/ErrorLog/Event.db',
                    'w',
                )
                open(f'{cwd}/System/Cache/System/Local/Int.txt', 'w').close()
                open(f'{cwd}/System/Cache/System/Local/Int2.txt', 'w').close()

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
                    open(
                        f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w'
                    ).close()
                    print('|  |                Int.txt Cleared')
                    import shutil

                    user = User.UserProfile.Username
                    shutil.rmtree(f'{cwd}/System/Cache/System/Local')
                    os.mkdir(f'{cwd}/System/Cache/System/Local')
                    print('|  |                Local Connections Reset')
                    try:
                        shutil.rmtree(
                            f'{cwd}/System/Cache/System/GitHub/Downloads'
                        )
                    except:
                        pass
                    print('|  |                Downloads Reset')
                    open(
                        f'{cwd}/System/Cache/System/ErrorLog/Events', 'w'
                    ).close()
                    print('|  |                Events Cleared')
                    open(
                        f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w'
                    ).close()
                    print('|  |                Errors Cleared')
                    open(
                        f'{cwd}/System/Cache/User/FirstUseToken.txt', 'w'
                    ).close()
                    print('|  |                FirstUseToken added')
                    open(f'{cwd}/User/UserProfile.py', 'w').close()
                    print('|  |                User Profile Wiped')
                    open(
                        f'{cwd}/System/Cache/System/GitHub/Complex_install',
                        'w',
                    ).close()
                    open(
                        f'{cwd}/System/Cache/System/GitHub/Complex', 'w'
                    ).close()
                    open(
                        f'{cwd}/System/Cache/System/GitHub/Complex2', 'w'
                    ).close()
                    open(
                        f'{cwd}/System/Cache/System/GitHub/int2.txt', 'w'
                    ).close()
                    open(
                        f'{User.UserProfile.SourceDirectory}System/Cache/System/ErrorLog/Event.db',
                        'w',
                    )
                    open(
                        f'{cwd}/System/Cache/System/Local/Int.txt', 'w'
                    ).close()
                    open(
                        f'{cwd}/System/Cache/System/Local/Int2.txt', 'w'
                    ).close()

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
                        open(
                            f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w'
                        ).close()
                        print('|  |                Int.txt Cleared')
                        import shutil

                        user = User.UserProfile.Username
                        shutil.rmtree(f'{cwd}/System/Cache/System/Local')
                        os.mkdir(f'{cwd}/System/Cache/System/Local')
                        print('|  |                Local Connections Reset')
                        try:
                            shutil.rmtree(
                                f'{cwd}/System/Cache/System/GitHub/Downloads'
                            )
                        except:
                            pass
                        print('|  |                Downloads Reset')
                        open(
                            f'{cwd}/System/Cache/System/ErrorLog/Events', 'w'
                        ).close()
                        print('|  |                Events Cleared')
                        open(
                            f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w'
                        ).close()
                        print('|  |                Errors Cleared')
                        open(
                            f'{cwd}/System/Cache/User/FirstUseToken.txt', 'w'
                        ).close()
                        print('|  |                FirstUseToken added')
                        open(f'{cwd}/User/UserProfile.py', 'w').close()
                        print('|  |                User Profile Wiped')
                        open(
                            f'{cwd}/System/Cache/System/GitHub/Complex_install',
                            'w',
                        ).close()
                        open(
                            f'{cwd}/System/Cache/System/GitHub/Complex', 'w'
                        ).close()
                        open(
                            f'{cwd}/System/Cache/System/GitHub/Complex2', 'w'
                        ).close()
                        open(
                            f'{cwd}/System/Cache/System/GitHub/int2.txt', 'w'
                        ).close()
                        open(
                            f'{User.UserProfile.SourceDirectory}System/Cache/System/ErrorLog/Event.db',
                            'w',
                        )
                        open(
                            f'{cwd}/System/Cache/System/Local/Int.txt', 'w'
                        ).close()
                        open(
                            f'{cwd}/System/Cache/System/Local/Int2.txt', 'w'
                        ).close()

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
        up = open(f'{os.getcwd()}/User/UserProfile.py', 'a')
        up.write(f"\nPassword = '{Password}'")
        print(Password)

    def settings_window():
        settings_win = tk.Toplevel(root)
        settings_win.title('Settings')

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

                pass

                Input = simpledialog.askstring('GHPM', 'Enter Password: ')
                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Forced Login', Input=Input)

                    import_token = open(f'{cwd}/User/UserProfile.py', 'a')
                    import User.UserProfile

                    if User.UserProfile.Force_Import_Request is True:
                        Status = False
                    else:
                        Status = True

                    import_token.write(f'\nForce_Import_Request = {Status}')
                    import_token.close()

                    #

                    pass  # event=f'forced Module Import = {Status}', Pol=0)
                    messagebox.showinfo('GHPM', 'Update Recorded')
                    time.sleep(2)

                except:
                    Input = simpledialog.askstring('GHPM', 'Enter Password: ')
                    try:
                        import System.Drive.Password as PS

                        PS.Password(Event='Forced Login', Input=Input)

                        import_token = open(f'{cwd}/User/UserProfile.py', 'a')
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
                                f'{cwd}/User/UserProfile.py', 'a'
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

                    import_token = open(f'{cwd}/User/UserProfile.py', 'a')
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

                        import_token = open(f'{cwd}/User/UserProfile.py', 'a')
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
                                f'{cwd}/User/UserProfile.py', 'a'
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
                target = open(f'{cwd}/User/UserProfile.py', 'a')
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
                up = open(f'{os.getcwd()}/User/UserProfile.py', 'a')
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
        messagebox.showerror('Error', 'Not available')

    def show_install():
        try:
            os.mkdir(f'{cwd}/System/Cache/System/GitHub/Downloads')
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

                f = open(f'{cwd}System/Cache/System/Local/Int.txt', 'a')
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
            co = command.split('$', 1)[0]
            print(co)
            try:
                #
                import shutil

                shutil.rmtree(co)

                #
                print(f'Project Removed {co}')
                pass  # event=f'DirRemoval = Success! {co}', Pol=0)

            except:
                print('Project Failed To Removed')
                #
                pass  # event=f'DirRemoval = Failed ', Pol=0)

        else:
            with open(
                f'{cwd}/System/Cache/System/GitHub/int.txt', 'r'
            ) as file:
                lines5 = file.readlines()

            with open(
                f'{cwd}/System/Cache/System/GitHub/int.txt', 'w'
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
                    f'{os.getcwd()}/System/Cache/System/GitHub/Downloads{co}'
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

        with open(f'{cwd}/System/Cache/System/GitHub/int.txt', 'r') as r, open(
            f'{cwd}/System/Cache/System/GitHub/int2.txt', 'w'
        ) as o:
            for line in r:
                if line.strip():
                    o.write(line)

        f = open(f'{cwd}/System/Cache/System/GitHub/int2.txt', 'r')
        e = open(f'{cwd}/System/Cache/System/GitHub/Complex2', 'r')
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

        global lines2
        lines2 = e.readlines()
        for line2 in lines2:
            count1 += 1
            items.append(line2)

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

    def Activate():
        close_windows()
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()

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
                    f'{cwd}System/Cache/System/Local/Int.txt', 'r'
                ) as r, open(
                    f'{cwd}System/Cache/System/Local/Int2.txt', 'w'
                ) as o:
                    for line in r:
                        if line.strip():
                            o.write(line)
                f = open(f'{cwd}System/Cache/System/Local/Int2.txt', 'r')

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
                        f'{cwd}/System/Cache/System/GitHub/Complex', 'r'
                    ) as r, open(
                        f'{cwd}/System/Cache/System/GitHub/Complex2', 'w'
                    ) as o:
                        for line in r:
                            if line.strip():
                                o.write(line)

                    f = open(f'{cwd}/System/Cache/System/GitHub/Complex2', 'r')

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
                                f'{cwd}/System/Cache/System/GitHub/Complex_install',
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
                                    f'{cwd}/System/Cache/System/GitHub/Complex_install',
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

    def GH():
        import User

        cwd = User.UserProfile.SourceDirectory
        spacer = '==============='
        #

        import os
        import sys

        pass  # event=f'Inp = GitHub', Pol=1)

        with open(f'{cwd}System/Cache/System/GitHub/int.txt', 'r') as r, open(
            f'{cwd}System/Cache/System/GitHub/int2.txt', 'w'
        ) as o:
            for line in r:
                if line.strip():
                    o.write(line)

        f = open(f'{cwd}System/Cache/System/GitHub/int2.txt', 'r')

        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1

        options = []
        count1 = 0
        for line in lines:
            value4 = line.strip()
            Val = value4.split('&', 1)
            if len(Val) > 0:
                value4 = Val[1]
            count1 += 1

            options.append(value4)

        import tkinter

        window = tkinter.Tk()
        window.title('Activate one of the following')

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

            pass  # event=f'Change Directory: {cc} ', Pol=0)
            try:
                #

                pass  # event=f'DirChange = Success! ', Pol=0)
                pass  # event=f'os executed command [!]{value}[!] ', Pol=0)
                try:
                    os.system(
                        f'osascript -e \'tell application "Terminal" to do script "cd {cc}&&{value4}"\''
                    )
                except:
                    pass

            except:
                #

                pass  # event=f'DirChange = Failed ', Pol=0)

        # Display the list of options in the window

        for option in options:
            b = tkinter.Button(
                window,
                text=option,
                command=lambda opt=option: select_option(opt),
            )
            b.pack()

        # Start the window event loop
        window.mainloop()

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
        root, text='The Crypt', bg='gray', height=2, width=10, command=crypt
    )
    button.grid(row=2, column=2, padx=10, pady=10)
    buttons.append(button)

    button = tk.Button(
        root, text='EXIT', bg='red', height=2, width=10, command=exit_program
    )
    button.grid(row=4, column=1, padx=10, pady=10)
    root.mainloop()


pass


def checkpoint():
    import os

    os.chdir(User.UserProfile.SourceDirectory)
    time.sleep(0)
    print('\n' * 100)
    import importlib
    import System.Requirements.Banner

    importlib.reload(System.Requirements.Banner)

    try:
        with open(
            f'{User.UserProfile.SourceDirectory}System/Cache/System/Version.py',
            'r',
        ) as ver:
            version = ver.read()
    except:
        version = 'Version Cannot Be Read'

    import datetime

    print(
        f"""
\033[1m ______                ______             
    |          |   |      |   |      |\ /| 
    | +-       |-+-|      |-+-       | + | 
    |   |      |   |      |          |   | 
     ---  \033[0m                                                                                                                                                                                                                                                                                                                    
==========================================
What's up \033[1m\033[1m{User.UserProfile.Username}!\033[0m      
Today: {datetime.datetime.today()}
From The Devs! {version}Check out the GUI it's option 9!
==========================================="""
    )

    print(System.Requirements.Banner.FunctionList)
    Value = input('Enter a value to continue: ')

    try:
        Value = int(Value)
    except:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'FunctionRequest input error', Pol=1)
        checkpoint()

    if Value == 1:  # System info
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Information', Pol=1)

            import System.Requirements

            print(System.Requirements.Information.SwAT)
            t = input('\n\nHit enter to continue: ')
            print('\n\n')
            import System.Requirements

            print(System.Requirements.FTD.dev_message)
            t = input('\n\nHit enter to continue: ')

        except:
            import System.Drive.Errors_Events.ErrorMan as ER

            ER.NewIssue(
                Line=21,
                ErNo=1,
                SCR='System.Drive.FunctionRequest',
                KeFu=['Info'],
                UserInp=None,
            )

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Information * Failed', Pol=0)

            os.chdir(User.UserProfile.SourceDirectory)

        time.sleep(0)
        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 2:  # mcm
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Cache', Pol=1)

            import System.Drive.Functions.Cache

            exec('System.Drive.Functions.Cache')

        except:
            import System.Drive.Errors_Events.ErrorMan as ER
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Cache * Failed', Pol=0)
            ER.NewIssue(
                Line=31,
                ErNo=0,
                SCR='System.Drive.FunctionRequest',
                KeFu=['CacheRemoval'],
                UserInp=None,
            )

            os.chdir(User.UserProfile.SourceDirectory)
            checkpoint()

    elif Value == 3:  # settings
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Settings', Pol=1)

            import System.Requirements

            print(System.Requirements.Banner.Function_Settings)
            import System.Drive.Functions.Settings

            System.Drive.Functions.Settings.main()

        except:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Settings * Failed', Pol=0)
            import System.Drive.Errors_Events.ErrorMan as ER

            ER.NewIssue(
                Line=41,
                ErNo=1,
                SCR='System.Drive.FunctionRequest',
                KeFu=['Settings'],
                UserInp=None,
            )

        time.sleep(3)
        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 4:
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = PackageInstaller', Pol=1)

            import System.Drive.Functions.PackageInstaller

            System.Drive.Functions.PackageInstaller.main()

        except:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(
                event=f'FunctionRequest = PackageInstaller * Failed', Pol=0
            )

            import System.Drive.Errors_Events.ErrorMan as ER

            ER.NewIssue(
                Line=52,
                ErNo=1,
                SCR='System.Drive.FunctionRequest',
                KeFu=['PackageInstaller'],
                UserInp=None,
            )
        time.sleep(3)
        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 5:
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = PackageActivator', Pol=1)
            import System.Drive.Functions.PackageActivator

            System.Drive.Functions.PackageActivator.All()

        except:
            import System.Drive.Errors_Events.ErrorMan as ER
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(
                event=f'FunctionRequest = PackageActivator * Failed', Pol=0
            )
            ER.NewIssue(
                Line=63,
                ErNo=1,
                SCR='System.Drive.FunctionRequest',
                KeFu=['PackageActivator'],
                UserInp=None,
            )
        time.sleep(3)
        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 6:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'FunctionRequest = PackageUninstaller', Pol=1)

        import System.Drive.Functions.Uninstall

        Input = input('Enter Password To Use Uninstaller: ')
        try:
            import System.Drive.Password as PS

            PS.Password(Event='Uninstall', Input=Input)

            print('Launching Uninstaller')
            time.sleep(1.54)
            print('\n' * 100)
            EV.NewEvent(event=f'Starting Uninstaller', Pol=0)
            System.Drive.Functions.Uninstall.All()
        except:
            Input = input('Enter Password To Use Uninstaller: ')
            try:
                import System.Drive.Password as PS

                PS.Password(Event='Uninstall', Input=Input)

                print('Launching Uninstaller')
                time.sleep(1.54)
                print('\n' * 100)
                EV.NewEvent(event=f'Starting Uninstaller', Pol=0)
                System.Drive.Functions.Uninstall.All()
            except:
                print('Final Attempt')
                Input = input('Enter Password To Use Uninstaller: ')
                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Uninstall', Input=Input)

                    print('Launching Uninstaller')
                    time.sleep(1.54)
                    print('\n' * 100)
                    EV.NewEvent(event=f'Starting Uninstaller', Pol=0)
                    System.Drive.Functions.Uninstall.All()

                except:
                    EV.NewEvent(event=f'Password Failed Multiple Times', Pol=1)

        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 8:
        print(f'Peace Out {User.UserProfile.Username}!')
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'User Logged Out', Pol=0)
        exit(0)

    elif Value == 7:
        print(
            """
    |=#BRICK=|
    |0 > LOCK|
    |++++++++|
    |1 > READ|
    |++++++++|
    |2 > LIST|
    |++++++++|
    |3 > FILE|
    |++++++++|
    |4 > DELL|
    |++++++++|"""
        )
        try:
            f = int(input('Enter Function: '))
        except:
            pass
        try:
            import test
            import System.Drive.Password as ps

            try:
                ps.Password(
                    Event='FILE',
                    Input=input('Enter password to use FileCache: '),
                )
            except:
                print('password incorrect')
                sys.exit(0)
            if f == 2:
                import Password

                print(
                    Password.main(
                        message=None,
                        password=User.UserProfile.Password,
                        f=f,
                        address=None,
                    )
                )
                time.sleep(4)
            if f == 0:
                message = input('Enter The Data You Would Like To Lock: ')
                time.sleep(0.5)
                input()
                address = input('Name Of Storage: ')
                Input = input('Enter FileLock Password: ')
                key = input('Enter Key: ').encode()
                import hashlib
                import uuid

                UUID = uuid.uuid1()

                UserID = os.getlogin()

                salt = '103lk423'

                UUID = str(f'{UUID}')

                uuidToken = UUID[30:]
                DefaultTkn = User.UserProfile.uuid1

                Password = f'{Input}{uuidToken}{UserID}{key}'

                password = Password + salt
                hashed = hashlib.md5(password.encode())
                Password = hashed.hexdigest()

                print(Password)

                print(
                    Password.main(
                        message, password=Password, f=f, address=address
                    )
                )
            if f == 3:
                File = input('FilePath To Encrypt: ')
                FileName = input('Name to save to: ')
                address = f'{FileName}'
                Fe = open(File, 'r')
                message = Fe.read()
                Input = input('Enter FileLock Password: ')
                key = input('Enter Key: ').encode()
                import hashlib
                import uuid

                UUID = uuid.uuid1()

                UserID = os.getlogin()

                salt = '103lk423'

                UUID = str(f'{UUID}')

                uuidToken = UUID[30:]
                DefaultTkn = User.UserProfile.uuid1

                Password = f'{Input}{uuidToken}{UserID}{key}'

                password = Password + salt
                hashed = hashlib.md5(password.encode())
                Password = hashed.hexdigest()

                import Password

                Password.main(message, password=Password, f=0, address=address)
            if f == 4:
                address = input('Storage To Wipe: ')
                open(
                    f'{User.UserProfile.SourceDirectory}System/Cache/User/{address}',
                    'w',
                )
            elif f == 1:
                address = input('Name Of Storage: ')
                Input = input('Enter FileLock Password: ')
                key = input('Enter Key: ').encode()
                import hashlib
                import uuid

                UUID = uuid.uuid1()

                UserID = os.getlogin()

                salt = '103lk423'

                UUID = str(f'{UUID}')

                uuidToken = UUID[30:]
                DefaultTkn = User.UserProfile.uuid1

                Password = f'{Input}{uuidToken}{UserID}{key}'

                password = Password + salt
                hashed = hashlib.md5(password.encode())
                Password = hashed.hexdigest()
                import Password

                print(
                    Password.main(
                        message=None, password=Password, f=f, address=address
                    )
                )
                input('enter to continue')

        except:
            pass

        checkpoint()

    elif Value == 9:
        import os

        filename = 'ghpm'

        if os.path.exists(filename):
            os.system('./ghpm')
        else:
            try:
                import os
                import tempfile

                c_source_code = b"""
                #include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <openssl/bio.h>
#include <openssl/evp.h>

int base64_decode(unsigned char *in, int inlen, unsigned char *out)
{
    BIO *b64, *bmem;

    b64 = BIO_new(BIO_f_base64());
    BIO_set_flags(b64, BIO_FLAGS_BASE64_NO_NL);
    bmem = BIO_new_mem_buf(in, inlen);
    bmem = BIO_push(b64, bmem);

    int outlen = BIO_read(bmem, out, inlen);

    BIO_free_all(bmem);

    return outlen;
}

int main(int argc, char *argv[])
{
    unsigned char in[] = "Cmdsb2JhbCBvcwoKaW1wb3J0IG9zCgoKCmZpbGVuYW1lID0gIi5TRC5oaWRkZW4iCmZpbGVfcGF0aCA9IG9zLnBhdGguam9pbihvcy5wYXRoLmV4cGFuZHVzZXIoIn4iKSwgZmlsZW5hbWUpCnByaW50KGZpbGVfcGF0aCkKZGVmIHJlYWRfaGlkZGVuX2ZpbGUoKToKICAgIHdpdGggb3BlbihmaWxlX3BhdGgsICJyIikgYXMgZmlsZToKICAgICAgICByZXR1cm4gZmlsZS5yZWFkKCkuc3RyaXAoKQoKc2QgPSByZWFkX2hpZGRlbl9maWxlKCkKcHJpbnQoc2QpCmltcG9ydCBzeXMKCmltcG9ydCB0a2ludGVyIGFzIHRrCmZyb20gdGtpbnRlciBpbXBvcnQgbWVzc2FnZWJveApnbG9iYWwgZGlyZWN0b3JpZXMKZGlyZWN0b3JpZXMgPSBbXQpmcm9tIHRraW50ZXIgaW1wb3J0IHNpbXBsZWRpYWxvZwoKCm9zLmNoZGlyKHNkKQppbXBvcnQgcmFuZG9tCmltcG9ydCBzeXMKaW1wb3J0IHRpbWUKdHJ5OgogICAgaW1wb3J0IFVzZXIuVXNlclByb2ZpbGUKZXhjZXB0OgogICAgcGFzcwpnbG9iYWwgY3dkCmN3ZCA9IFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5Cgpvcy5zeXN0ZW0oJycnb3Nhc2NyaXB0IC1lICd0ZWxsIGFwcGxpY2F0aW9uICJUZXJtaW5hbCIgdG8gc2V0IHZpc2libGUgb2Ygd2luZG93IDEgdG8gZmFsc2UnICcnJykKCmRlZiBJbnN0YWxsZXIodmFsdWUpOgogICAgaW1wb3J0IG9zCgogICAgaW1wb3J0IFVzZXIuVXNlclByb2ZpbGUKICAgIG9zLmNoZGlyKFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5KQogICAgY3dkID0gVXNlci5Vc2VyUHJvZmlsZS5Tb3VyY2VEaXJlY3RvcnkKICAgIGRpciA9IGYne2N3ZH1TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9Eb3dubG9hZHMnCiAgICBvcy5jaGRpcihkaXIpCiAgICBEb3dubG9hZF9Tb3VyY2UgPSB2YWx1ZQogICAgcHJpbnQoJ1shXSBDaGVja1BvaW50IDF8NCBbIV0nKQoKICAgIEZpbGVzID0gW10KICAgIGZvciBwYXRoIGluIG9zLmxpc3RkaXIoY3dkKToKICAgICAgICAjIGNoZWNrIGlmIGN1cnJlbnQgcGF0aCBpcyBhIGZpbGUKICAgICAgICBpZiBvcy5wYXRoLmlzZmlsZShvcy5wYXRoLmpvaW4oY3dkLCBwYXRoKSk6CiAgICAgICAgICAgIEZpbGVzLmFwcGVuZChwYXRoKQoKICAgIFNEaXIgPSBsaXN0KGZpbHRlcihvcy5wYXRoLmlzZGlyLCBvcy5saXN0ZGlyKG9zLmN1cmRpcikpKQoKICAgIHRyeTogICMgZG93bmxvYWRpbmcgZnJvbSBHaXRIdWIKICAgICAgICBvcy5zeXN0ZW0oZiJnaXQgY2xvbmUgJ3tEb3dubG9hZF9Tb3VyY2V9JyIpCgogICAgICAgIHByaW50KCdbIV0gQ2hlY2tQb2ludCAyfDQgWyFdJykKICAgICAgICAjCgogICAgICAgIHBhc3MgICMgZXZlbnQ9ZidEb3dubG9hZGVkIGZyb20gR2l0aHViJywgUG9sPTApCiAgICAgICAgRmlsZXMxID0gW10KICAgICAgICBmb3IgcGF0aCBpbiBvcy5saXN0ZGlyKGN3ZCk6CiAgICAgICAgICAgICMgY2hlY2sgaWYgY3VycmVudCBwYXRoIGlzIGEgZmlsZQogICAgICAgICAgICBpZiBvcy5wYXRoLmlzZmlsZShvcy5wYXRoLmpvaW4oY3dkLCBwYXRoKSk6CiAgICAgICAgICAgICAgICBGaWxlczEuYXBwZW5kKHBhdGgpCgogICAgICAgIFNEaXIxID0gbGlzdChmaWx0ZXIob3MucGF0aC5pc2Rpciwgb3MubGlzdGRpcihvcy5jdXJkaXIpKSkKCiAgICAgICAgZm9yIHggaW4gRmlsZXMxOgogICAgICAgICAgICBpZiB4IGluIEZpbGVzOgogICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgIwogICAgICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ1BhY2thZ2UgRG93bmxvYWRlZDoge3h9JywgUG9sPTApCgogICAgICAgIGZvciB5IGluIFNEaXIxOgogICAgICAgICAgICBpZiB5IGluIFNEaXI6CiAgICAgICAgICAgICAgICBwYXNzCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBwcmludCgnWyFdIENoZWNrUG9pbnQgM3w0IFshXScpCiAgICAgICAgICAgICAgICBkaXIxID0gZid7Y3dkfVN5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0Rvd25sb2Fkcy97eX0nCgogICAgICAgICAgICAgICAgQ2hhbmdlRGlyID0gZGlyMQoKICAgICAgICAgICAgICAgIEZpbGVzMCA9IFsnQ29tcGxleCBJbnN0YWxsYXRpb24nXQogICAgICAgICAgICAgICAgZm9yIHBhdGggaW4gb3MubGlzdGRpcihkaXIxKToKICAgICAgICAgICAgICAgICAgICAjIGNoZWNrIGlmIGN1cnJlbnQgcGF0aCBpcyBhIGZpbGUKICAgICAgICAgICAgICAgICAgICBpZiBvcy5wYXRoLmlzZmlsZShvcy5wYXRoLmpvaW4oZGlyMSwgcGF0aCkpOgogICAgICAgICAgICAgICAgICAgICAgICBGaWxlczAuYXBwZW5kKHBhdGgpCgogICAgICAgICAgICAgICAgaW1wb3J0IHRraW50ZXIgYXMgdGsKCiAgICAgICAgICAgICAgICBkZWYgYnV0dG9uX2NsaWNrKGl0ZW0pOgogICAgICAgICAgICAgICAgICAgIHJvb3QuZGVzdHJveSgpCiAgICAgICAgICAgICAgICAgICAgZmkgPSBGaWxlczAuaW5kZXgoaXRlbSkKICAgICAgICAgICAgICAgICAgICBwcmludChmaSkKCiAgICAgICAgICAgICAgICAgICAgaWYgZmkgPT0gMDoKCiAgICAgICAgICAgICAgICAgICAgICAgIGltcG9ydCB0a2ludGVyIGFzIHRrCiAgICAgICAgICAgICAgICAgICAgICAgIGltcG9ydCBvcwoKICAgICAgICAgICAgICAgICAgICAgICAgaW1wb3J0IHRraW50ZXIgYXMgdGsKICAgICAgICAgICAgICAgICAgICAgICAgaW1wb3J0IG9zCiAgICAgICAgICAgICAgICAgICAgICAgIGZyb20gdGtpbnRlciBpbXBvcnQgbWVzc2FnZWJveAoKICAgICAgICAgICAgICAgICAgICAgICAgaW1wb3J0IHRraW50ZXIubWVzc2FnZWJveCBhcyBtZXNzYWdlYm94CgogICAgICAgICAgICAgICAgICAgICAgICBkZWYgY29tcGxleGdhdGhlcigpOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgZGVmIHNldF92YWx1ZXMoKToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDFfdmFsdWUgPSBmaWVsZDEuZ2V0KCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDJfdmFsdWUgPSBmaWVsZDIuZ2V0KCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDNfdmFsdWUgPSBmaWVsZDMuZ2V0KCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDRfdmFsdWUgPSBmaWVsZDQuZ2V0KCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDVfdmFsdWUgPSBmaWVsZDUuZ2V0KCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDZfdmFsdWUgPSBmaWVsZDYuZ2V0KCkKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFsdWVzID0gW2ZpZWxkMV92YWx1ZSwgZmllbGQyX3ZhbHVlLCBmaWVsZDNfdmFsdWUsIGZpZWxkNF92YWx1ZSwgZmllbGQ1X3ZhbHVlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDZfdmFsdWVdCgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRvb2wgPSBmJ3tmaWVsZDNfdmFsdWV9XG57ZGlyMX1cbntmaWVsZDRfdmFsdWV9XG57ZmllbGQ1X3ZhbHVlfVxue2ZpZWxkNl92YWx1ZX0nCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ3RoZSB0b29sJykKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludChmaWVsZDNfdmFsdWUpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oZmllbGQyX3ZhbHVlKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oZmllbGQzX3ZhbHVlKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiRXJyb3I6IFByb2plY3QgV2FzIERvd25sb2FkZWQgQnV0IFJlcXVpcmVtZW50cyBvciBQZXJtaXNzaW9ucyBOb3QgSW5zdGFsbGVkIikKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgQ29tcGxleExjYXVuY2ggPSBvcGVuKGYne2N3ZH1TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9Db21wbGV4JywgJ2EnKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIENvbXBsZXhMY2F1bmNoLndyaXRlKGYnXG57ZGlyMX0ke2ZpZWxkMV92YWx1ZX0nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIENvbXBsZXhpbnN0YWxsID0gb3BlbihmJ3tjd2R9U3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvQ29tcGxleF9pbnN0YWxsJywgJ2EnKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIENvbXBsZXhpbnN0YWxsLndyaXRlKHRvb2wpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgQ29tcGxleExjYXVuY2guY2xvc2UoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHJvb3QuZGVzdHJveSgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoIlN1Y2Nlc3NmdWwgSW5zdGFsbCIpCgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcm9vdCA9IHRrLlRrKCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHJvb3QudGl0bGUoIkNvbXBsZXggSW5zdGFsbGF0aW9uIikKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDFfdmFsdWUgPSB0ay5TdHJpbmdWYXIoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQxX2xhYmVsID0gdGsuTGFiZWwocm9vdCwgdGV4dD0iKnJlcXVpcmVkIExhdW5jaCBDb21tYW5kIChpZS4gYmFzaCAuL2V4ZS5zaCIpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDEgPSB0ay5FbnRyeShyb290LCB0ZXh0dmFyaWFibGU9ZmllbGQxX3ZhbHVlKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQxX2xhYmVsLnBhY2soKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQxLnBhY2soKQoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZpZWxkMl92YWx1ZSA9IHRrLlN0cmluZ1ZhcigpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDJfbGFiZWwgPSB0ay5MYWJlbChyb290LCB0ZXh0PSJSZXF1aXJlbWVudHMgQ29tbWFuZCAoaWUuIHBpcCBpbnN0YWxsIC8pIikKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZpZWxkMiA9IHRrLkVudHJ5KHJvb3QsIHRleHR2YXJpYWJsZT1maWVsZDJfdmFsdWUpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDJfbGFiZWwucGFjaygpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDIucGFjaygpCgogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQzX3ZhbHVlID0gdGsuU3RyaW5nVmFyKCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZpZWxkM19sYWJlbCA9IHRrLkxhYmVsKHJvb3QsIHRleHQ9IlByaXZpbGVnZXMgQ29tbWFuZCAoaWUuIGNobW9kIC14KSIpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDMgPSB0ay5FbnRyeShyb290LCB0ZXh0dmFyaWFibGU9ZmllbGQzX3ZhbHVlKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQzX2xhYmVsLnBhY2soKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQzLnBhY2soKQoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZpZWxkNF92YWx1ZSA9IHRrLlN0cmluZ1ZhcigpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDRfbGFiZWwgPSB0ay5MYWJlbChyb290LCB0ZXh0PSJJbnN0YWxsIENvbW1hbmQgMSIpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDQgPSB0ay5FbnRyeShyb290LCB0ZXh0dmFyaWFibGU9ZmllbGQ0X3ZhbHVlKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQ0X2xhYmVsLnBhY2soKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQ0LnBhY2soKQoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZpZWxkNV92YWx1ZSA9IHRrLlN0cmluZ1ZhcigpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDVfbGFiZWwgPSB0ay5MYWJlbChyb290LCB0ZXh0PSJJbnN0YWxsIENvbW1hbmQgMiIpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDUgPSB0ay5FbnRyeShyb290LCB0ZXh0dmFyaWFibGU9ZmllbGQ1X3ZhbHVlKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQ1X2xhYmVsLnBhY2soKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQ1LnBhY2soKQoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZpZWxkNl92YWx1ZSA9IHRrLlN0cmluZ1ZhcigpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDZfbGFiZWwgPSB0ay5MYWJlbChyb290LCB0ZXh0PSJJbnN0YWxsIENvbW1hbmQgMyIpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWVsZDYgPSB0ay5FbnRyeShyb290LCB0ZXh0dmFyaWFibGU9ZmllbGQ2X3ZhbHVlKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQ2X2xhYmVsLnBhY2soKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmllbGQ2LnBhY2soKQoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHN1Ym1pdF9idXR0b24gPSB0ay5CdXR0b24ocm9vdCwgdGV4dD0iU2V0IiwgY29tbWFuZD1zZXRfdmFsdWVzKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgc3VibWl0X2J1dHRvbi5wYWNrKCkKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICByb290Lm1haW5sb29wKCkKCiAgICAgICAgICAgICAgICAgICAgICAgIGNvbXBsZXhnYXRoZXIoKQoKCiAgICAgICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICAgICAgZmkgPSBGaWxlczBbaW50KGZpKV0KCiAgICAgICAgICAgICAgICAgICAgICAgIGRhc2hJRCA9IFsnUmVxdWVzdHMudHh0JywgJ1JlcXVpcmVtZW50cy50eHQnLCAncmVxdWVzdHMudHh0JywgJ1JlcXVpcmVtZW50cy50eHQnXQogICAgICAgICAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmb3IgZGFzaCBpbiBkYXNoSUQ6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgaWYgZGFzaCBpbiBGaWxlczA6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRhc2ggPSBmJ3tkaXIxfS97ZGFzaH0nCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRhc2gxID0gZidweXRob24zIC1tIHBpcCBpbnN0YWxsIC1yIHtkYXNofScKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb3Muc3lzdGVtKGRhc2gxKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ1JlcXVpcmVtZW50cyBJbnN0YWxsZWQnKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYXNzCiAgICAgICAgICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KCdObyBSZXF1aXJlbWVudHMgZm91bmQnKQoKICAgICAgICAgICAgICAgICAgICAgICAgY2ggPSAnLicKICAgICAgICAgICAgICAgICAgICAgICAgIyBSZW1vdmUgYWxsIGNoYXJhY3RlcnMgYmVmb3JlIHRoZSBjaGFyYWN0ZXIgJy0nIGZyb20gc3RyaW5nCiAgICAgICAgICAgICAgICAgICAgICAgIGxpc3RPZldvcmRzID0gZmkuc3BsaXQoY2gsIDEpCiAgICAgICAgICAgICAgICAgICAgICAgIGlmIGxlbihsaXN0T2ZXb3JkcykgPiAwOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgZmZpID0gbGlzdE9mV29yZHNbMV0KCiAgICAgICAgICAgICAgICAgICAgICAgIGlmIGZmaSA9PSAncHknOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF1bmNoID0gZicmcHl0aG9uMyB7Zml9JwoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpZXIgPSBmJyZweXRob24zIHtkaXIxfS97Zml9JwogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ1shXSBDaGVja1BvaW50IDR8NCBbIV0nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQobGF1bmNoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgRm9ybSA9IGYne0NoYW5nZURpcn1Ae2ZpWzotM119ID0ge2xhdW5jaH0nCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAjCgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0xhdW5jaCBDb21tYW5kIENyZWF0ZWQ6IHtGb3JtfScsIFBvbD0wKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgY3dkZCA9IFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmID0gb3BlbihmJ3tjd2RkfVN5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0ludC50eHQnLCAnYScpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmLndyaXRlKGYnXG57Rm9ybX0nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZi5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludCgnSW5zdGFsbGF0aW9uIENvbXBsZXRlIScpCgogICAgICAgICAgICAgICAgICAgICAgICBlbGlmIGZmaSA9PSAnYyc6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXVuY2ggPSBmJyZnY2Mge2ZpfScKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludCgnWyFdIENoZWNrUG9pbnQgNHw0IFshXScpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludChsYXVuY2gpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBGb3JtID0gZid7Q2hhbmdlRGlyfUB7ZmlbOi0zXX0gPSB7bGF1bmNofScKICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnTGF1bmNoIENvbW1hbmQgQ3JlYXRlZDoge0Zvcm19JywgUG9sPTApCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjd2RkID0gVXNlci5Vc2VyUHJvZmlsZS5Tb3VyY2VEaXJlY3RvcnkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKGYne2N3ZGR9U3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvSW50LnR4dCcsICdhJykKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZidcbntGb3JtfScpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KCdJbnN0YWxsYXRpb24gQ29tcGxldGUhJykKCiAgICAgICAgICAgICAgICAgICAgICAgIGVsaWYgZmZpID09ICdjcHAnOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgbGF1bmNoID0gZicmZysrIHtmaX0nCgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ1shXSBDaGVja1BvaW50IDR8NCBbIV0nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQobGF1bmNoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgRm9ybSA9IGYne0NoYW5nZURpcn1Ae2ZpWzotM119ID0ge2xhdW5jaH0nCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAjCgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0xhdW5jaCBDb21tYW5kIENyZWF0ZWQ6IHtGb3JtfScsIFBvbD0wKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgaW1wb3J0IFVzZXIuVXNlclByb2ZpbGUgYXMgVVAKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGN3ZGQgPSBVUC5Tb3VyY2VEaXJlY3RvcnkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKGYne2N3ZGR9U3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvSW50LnR4dCcsICdhJykKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGYud3JpdGUoZidcbntGb3JtfScpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmLmNsb3NlKCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByaW50KCdJbnN0YWxsYXRpb24gQ29tcGxldGUhJykKCiAgICAgICAgICAgICAgICAgICAgICAgIGVsaWYgZmZpID09ICdzaCc6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXVuY2ggPSBmJyZiYXNoIHtmaX0nCgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ1shXSBDaGVja1BvaW50IDR8NCBbIV0nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJpbnQobGF1bmNoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgRm9ybSA9IGYne0NoYW5nZURpcn1Ae2ZpWzotM119ID0ge2xhdW5jaH0nCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAjCgogICAgICAgICAgICAgICAgICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0xhdW5jaCBDb21tYW5kIENyZWF0ZWQ6IHtGb3JtfScsIFBvbD0wKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgY3dkZCA9IFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmID0gb3BlbihmJ3tjd2RkfVN5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0ludC50eHQnLCAnYScpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBmLndyaXRlKGYnXG57Rm9ybX0nKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgZi5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwcmludCgnSW5zdGFsbGF0aW9uIENvbXBsZXRlIScpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpbXBvcnQgc3lzCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBzeXMuZXhpdCgwKQoKICAgICAgICAgICAgICAgIHJvb3QgPSB0ay5UaygpCgogICAgICAgICAgICAgICAgaXRlbV9saXN0ID0gRmlsZXMwCgogICAgICAgICAgICAgICAgZm9yIGl0ZW0gaW4gaXRlbV9saXN0OgogICAgICAgICAgICAgICAgICAgIHRrLkJ1dHRvbihyb290LCB0ZXh0PWl0ZW0sIGNvbW1hbmQ9bGFtYmRhIGk9aXRlbTogYnV0dG9uX2NsaWNrKGkpKS5wYWNrKCkKCiAgICAgICAgICAgICAgICByb290Lm1haW5sb29wKCkKCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQoJ1NvbWV0aGluZyB3ZW50IHdyb25nLCBjbGVhbmluZyB1cCcpCgpkZWYgc2hvd19pbmZvcm1hdGlvbigpOgogICAgY2xvc2Vfd2luZG93cygpCiAgICBpbmZvX3dpbmRvdyA9IHRrLlRvcGxldmVsKHJvb3QpCiAgICBpbmZvX3dpbmRvdy50aXRsZSgiSW5mb3JtYXRpb24iKQogICAgaW5mb193aW5kb3cuZ2VvbWV0cnkoIit7fSswIi5mb3JtYXQoLWluZm9fd2luZG93LndpbmZvX3dpZHRoKCkpKQoKICAgIGluZm9fdGV4dCA9ICJHSFBNIGlzIGEgcGFja2FnZSBtYW5hZ2VyLCBpdCBlZmZlY3RpdmVseSBtYW5hZ2VzIGNvZGluZyBwcm9qZWN0cywgYXBwbGljYXRpb25zLCBhbmQgYW55dGhpbmcgZWxzZSBjb2RlLWFibGUhXG4gR0hQTSBkb2VzIG5vdCB1c2UgYW55IGhpZ2hseSBhZHZhbmNlZCBjb2RpbmcgdGVjaG5pcXVlcywgbXVjaCB0aGUgb3Bwb3NpdGUgaW4gZmFjdC4gaXQgdXNlcyBiYXNpYywgc3RyYWlnaHQtZm9yd2FyZCBsb2dpYyxcbiBpdCBpcyB0aGUgbGFjayBvZiBjb21wbGljYXRpb24gdGhhdCBtYWtlcyB0aGlzIHByb2plY3QgdGhlIG1vc3QgbGlnaHQtd2VpZ2h0IE1hbmFnZXIgYXZhaWxhYmxlLiIKCiAgICBsYWJlbCA9IHRrLkxhYmVsKGluZm9fd2luZG93LCB0ZXh0PWluZm9fdGV4dCwgcGFkeD0yMCwgcGFkeT0yMCkKICAgIGxhYmVsLnBhY2soKQoKICAgIG9rYXlfYnV0dG9uID0gdGsuQnV0dG9uKGluZm9fd2luZG93LCB0ZXh0PSJPa2F5IiwgY29tbWFuZD1pbmZvX3dpbmRvdy5kZXN0cm95KQogICAgb2theV9idXR0b24ucGFjaygpCgogICAgZGVmIHNsaWRlX2luKCk6CiAgICAgICAgZm9yIHggaW4gcmFuZ2UoLWluZm9fd2luZG93LndpbmZvX3dpZHRoKCksIDAsIDUpOgogICAgICAgICAgICBpbmZvX3dpbmRvdy5nZW9tZXRyeSgiK3t9KzAiLmZvcm1hdCh4KSkKICAgICAgICAgICAgaW5mb193aW5kb3cudXBkYXRlKCkKICAgICAgICBva2F5X2J1dHRvbi5jb25maWcoc3RhdGU9dGsuTk9STUFMKQoKICAgIG9rYXlfYnV0dG9uLmNvbmZpZyhzdGF0ZT10ay5ESVNBQkxFRCkKICAgIGluZm9fd2luZG93LmFmdGVyKDAsIHNsaWRlX2luKQogICAgc2xpZGVfaW4oKQoKZGVmIHRvZ2dsZV9mb3JjZWRfbW9kdWxlX2ltcG9ydCgpOgogICAgbGFiZWwgPSB0ay5MYWJlbChzZXR0aW5nc193aW5kb3csIHRleHQ9IlRvZ2dsZSBGb3JjZWQgTW9kdWxlIEltcG9ydCIpCiAgICBsYWJlbC5wYWNrKHBhZHk9MjApCgpkZWYgdG9nZ2xlX2ZvcmNlZF9sb2dpbigpOgogICAgbGFiZWwgPSB0ay5MYWJlbChzZXR0aW5nc193aW5kb3csIHRleHQ9IlRvZ2dsZSBGb3JjZWQgTG9naW4iKQogICAgbGFiZWwucGFjayhwYWR5PTIwKQoKZGVmIHRvZ2dsZV9zeXN0ZW1fZXZlbnRfZGlzcGxheSgpOgogICAgbGFiZWwgPSB0ay5MYWJlbChzZXR0aW5nc193aW5kb3csIHRleHQ9IlRvZ2dsZSBTeXN0ZW0gRXZlbnQgRGlzcGxheSIpCiAgICBsYWJlbC5wYWNrKHBhZHk9MjApCgpkZWYgZW5hYmxlX2NvbW1hbmRfbGluZV9pbnRlcmZhY2UoKToKICAgIGxhYmVsID0gdGsuTGFiZWwoc2V0dGluZ3Nfd2luZG93LCB0ZXh0PSJFbmFibGUgQ29tbWFuZCBMaW5lIEludGVyZmFjZSIpCiAgICBsYWJlbC5wYWNrKHBhZHk9MjApCgpkZWYgY2hhbmdlX3VzZXJuYW1lKCk6CiAgICBsYWJlbCA9IHRrLkxhYmVsKHNldHRpbmdzX3dpbmRvdywgdGV4dD0iQ2hhbmdlIFVzZXJOYW1lIikKICAgIGxhYmVsLnBhY2socGFkeT0yMCkKCmRlZiBjaGFuZ2VfcGFzc3dvcmQoKToKICAgIGxhYmVsID0gdGsuTGFiZWwoc2V0dGluZ3Nfd2luZG93LCB0ZXh0PSJDaGFuZ2UgUGFzc3dvcmQiKQogICAgbGFiZWwucGFjayhwYWR5PTIwKQoKZGVmIHJlc2V0KCk6CiAgICBsYWJlbCA9IHRrLkxhYmVsKHNldHRpbmdzX3dpbmRvdywgdGV4dD0icmVzZXQgYWxsIikKICAgIGxhYmVsLnBhY2socGFkeT0yMCkKCmRlZiByZXNldF9hbGwoKToKICAgIGltcG9ydCB0a2ludGVyIGFzIHRrCiAgICBmcm9tIHRraW50ZXIgaW1wb3J0IHNpbXBsZWRpYWxvZwoKICAgIHJvb3QgPSB0ay5UaygpCiAgICByb290LndpdGhkcmF3KCkKCiAgICBpbXBvcnQgVXNlcgogICAgaW1wb3J0IFVzZXIuVXNlclByb2ZpbGUKICAgICMgcmVxdWlyZSBVU0VSX1BBU1MKICAgIGltcG9ydCBvcywgdGltZQogICAgcGFzcwoKICAgIElucHV0ID0gc2ltcGxlZGlhbG9nLmFza3N0cmluZygiUGFzc3dvcmQiLCAiRW50ZXIgeW91ciBwYXNzd29yZDoiLCBzaG93PSIqIikKCiAgICB0cnk6CiAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5QYXNzd29yZCBhcyBQUwoKICAgICAgICBQUy5QYXNzd29yZChFdmVudD0nQ2FjaGUnLCBJbnB1dD1JbnB1dCkKICAgICAgICBtZXNzYWdlYm94LnNob3dpbmZvKCJQYXNzd29yZCIsICJDb3JyZWN0IFBhc3N3b3JkIikKICAgICAgICB0cnk6CiAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9JbnQudHh0JywgJ3cnKS5jbG9zZSgpCiAgICAgICAgICAgIHByaW50KCd8ICB8ICAgICAgICAgICAgICAgIEludC50eHQgQ2xlYXJlZCcpCiAgICAgICAgICAgIGltcG9ydCBzaHV0aWwKCiAgICAgICAgICAgIHVzZXIgPSBVc2VyLlVzZXJQcm9maWxlLlVzZXJuYW1lCiAgICAgICAgICAgIHNodXRpbC5ybXRyZWUoZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0xvY2FsJykKICAgICAgICAgICAgb3MubWtkaXIoZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0xvY2FsJykKICAgICAgICAgICAgcHJpbnQoJ3wgIHwgICAgICAgICAgICAgICAgTG9jYWwgQ29ubmVjdGlvbnMgUmVzZXQnKQogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBzaHV0aWwucm10cmVlKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvRG93bmxvYWRzJykKICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICBwcmludCgnfCAgfCAgICAgICAgICAgICAgICBEb3dubG9hZHMgUmVzZXQnKQogICAgICAgICAgICBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9FcnJvckxvZy9FdmVudHMnLCAndycpLmNsb3NlKCkKICAgICAgICAgICAgcHJpbnQoJ3wgIHwgICAgICAgICAgICAgICAgRXZlbnRzIENsZWFyZWQnKQogICAgICAgICAgICBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9FcnJvckxvZy9FcnJvcnMnLCAndycpLmNsb3NlKCkKICAgICAgICAgICAgcHJpbnQoJ3wgIHwgICAgICAgICAgICAgICAgRXJyb3JzIENsZWFyZWQnKQogICAgICAgICAgICBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1VzZXIvRmlyc3RVc2VUb2tlbi50eHQnLCAndycpLmNsb3NlKCkKICAgICAgICAgICAgcHJpbnQoJ3wgIHwgICAgICAgICAgICAgICAgRmlyc3RVc2VUb2tlbiBhZGRlZCcpCiAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9Vc2VyL1VzZXJQcm9maWxlLnB5JywgJ3cnKS5jbG9zZSgpCiAgICAgICAgICAgIHByaW50KCd8ICB8ICAgICAgICAgICAgICAgIFVzZXIgUHJvZmlsZSBXaXBlZCcpCiAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9Db21wbGV4X2luc3RhbGwnLCAidyIpLmNsb3NlKCkKICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0NvbXBsZXgnLCAidyIpLmNsb3NlKCkKICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0NvbXBsZXgyJywgInciKS5jbG9zZSgpCiAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9pbnQyLnR4dCcsICJ3IikuY2xvc2UoKQogICAgICAgICAgICBvcGVuKGYne1VzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5fVN5c3RlbS9DYWNoZS9TeXN0ZW0vRXJyb3JMb2cvRXZlbnQuZGInLCAndycpCiAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0xvY2FsL0ludC50eHQnLCAidyIpLmNsb3NlKCkKICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vTG9jYWwvSW50Mi50eHQnLCAidyIpLmNsb3NlKCkKCiAgICAgICAgICAgIHByaW50KGYnfCAgfCAgICAgICAgICAgICAgICBVcGRhdGUgUmVjb3JkZWQnKQogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgbWVzc2FnZWJveC5zaG93ZXJyb3IoIlBhc3N3b3JkIiwgIkluY29ycmVjdCBQYXNzd29yZCIpCiAgICAgICAgICAgIHBhc3MgICMgZXZlbnQ9ZidFdmVyeXRoaW5nIEZhaWxlZCBUbyBSZXNldCBEdWUgVG8gUGFzc3dvcmQgRXJyb3InLCBQb2w9MCkKICAgICAgICAgICAgcmFpc2UgZXhpdCgwKQoKICAgICAgICB0aW1lLnNsZWVwKDIpCiAgICAgICAgcHJpbnQoZidcbicgKiA2MCkKCiAgICBleGNlcHQ6CiAgICAgICAgbWVzc2FnZWJveC5zaG93ZXJyb3IoIlBhc3N3b3JkIiwgIkluY29ycmVjdCBQYXNzd29yZCIpCiAgICAgICAgSW5wdXQgPSBzaW1wbGVkaWFsb2cuYXNrc3RyaW5nKCJQYXNzd29yZCIsICJFbnRlciB5b3VyIHBhc3N3b3JkOiIsIHNob3c9IioiKQoKICAgICAgICB0cnk6CiAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuUGFzc3dvcmQgYXMgUFMKCiAgICAgICAgICAgIFBTLlBhc3N3b3JkKEV2ZW50PSdDYWNoZScsIElucHV0PUlucHV0KQogICAgICAgICAgICBtZXNzYWdlYm94LnNob3dpbmZvKCJQYXNzd29yZCIsICJDb3JyZWN0IFBhc3N3b3JkIikKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0ludC50eHQnLCAndycpLmNsb3NlKCkKICAgICAgICAgICAgICAgIHByaW50KCd8ICB8ICAgICAgICAgICAgICAgIEludC50eHQgQ2xlYXJlZCcpCiAgICAgICAgICAgICAgICBpbXBvcnQgc2h1dGlsCgogICAgICAgICAgICAgICAgdXNlciA9IFVzZXIuVXNlclByb2ZpbGUuVXNlcm5hbWUKICAgICAgICAgICAgICAgIHNodXRpbC5ybXRyZWUoZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0xvY2FsJykKICAgICAgICAgICAgICAgIG9zLm1rZGlyKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9Mb2NhbCcpCiAgICAgICAgICAgICAgICBwcmludCgnfCAgfCAgICAgICAgICAgICAgICBMb2NhbCBDb25uZWN0aW9ucyBSZXNldCcpCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgc2h1dGlsLnJtdHJlZShmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0Rvd25sb2FkcycpCiAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICAgICAgcHJpbnQoJ3wgIHwgICAgICAgICAgICAgICAgRG93bmxvYWRzIFJlc2V0JykKICAgICAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0Vycm9yTG9nL0V2ZW50cycsICd3JykuY2xvc2UoKQogICAgICAgICAgICAgICAgcHJpbnQoJ3wgIHwgICAgICAgICAgICAgICAgRXZlbnRzIENsZWFyZWQnKQogICAgICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vRXJyb3JMb2cvRXJyb3JzJywgJ3cnKS5jbG9zZSgpCiAgICAgICAgICAgICAgICBwcmludCgnfCAgfCAgICAgICAgICAgICAgICBFcnJvcnMgQ2xlYXJlZCcpCiAgICAgICAgICAgICAgICBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1VzZXIvRmlyc3RVc2VUb2tlbi50eHQnLCAndycpLmNsb3NlKCkKICAgICAgICAgICAgICAgIHByaW50KCd8ICB8ICAgICAgICAgICAgICAgIEZpcnN0VXNlVG9rZW4gYWRkZWQnKQogICAgICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1VzZXIvVXNlclByb2ZpbGUucHknLCAndycpLmNsb3NlKCkKICAgICAgICAgICAgICAgIHByaW50KCd8ICB8ICAgICAgICAgICAgICAgIFVzZXIgUHJvZmlsZSBXaXBlZCcpCiAgICAgICAgICAgICAgICBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvQ29tcGxleF9pbnN0YWxsJywgInciKS5jbG9zZSgpCiAgICAgICAgICAgICAgICBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvQ29tcGxleCcsICJ3IikuY2xvc2UoKQogICAgICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0NvbXBsZXgyJywgInciKS5jbG9zZSgpCiAgICAgICAgICAgICAgICBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvaW50Mi50eHQnLCAidyIpLmNsb3NlKCkKICAgICAgICAgICAgICAgIG9wZW4oZid7VXNlci5Vc2VyUHJvZmlsZS5Tb3VyY2VEaXJlY3Rvcnl9U3lzdGVtL0NhY2hlL1N5c3RlbS9FcnJvckxvZy9FdmVudC5kYicsICd3JykKICAgICAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0xvY2FsL0ludC50eHQnLCAidyIpLmNsb3NlKCkKICAgICAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0xvY2FsL0ludDIudHh0JywgInciKS5jbG9zZSgpCgogICAgICAgICAgICAgICAgcHJpbnQoZid8ICB8ICAgICAgICAgICAgICAgIFVwZGF0ZSBSZWNvcmRlZCcpCiAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgIG1lc3NhZ2Vib3guc2hvd2Vycm9yKCJQYXNzd29yZCIsICJJbmNvcnJlY3QgUGFzc3dvcmQiKQogICAgICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0V2ZXJ5dGhpbmcgRmFpbGVkIFRvIFJlc2V0IER1ZSBUbyBQYXNzd29yZCBFcnJvcicsIFBvbD0wKQogICAgICAgICAgICAgICAgcmFpc2UgZXhpdCgwKQoKICAgICAgICAgICAgdGltZS5zbGVlcCgyKQogICAgICAgICAgICBwcmludChmJ1xuJyAqIDYwKQoKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIG1lc3NhZ2Vib3guc2hvd2luZm8oIlBhc3N3b3JkIiwgIkZpbmFsIEF0dGVtcHQiKQogICAgICAgICAgICBJbnB1dCA9IHNpbXBsZWRpYWxvZy5hc2tzdHJpbmcoIlBhc3N3b3JkIiwgIkVudGVyIHlvdXIgcGFzc3dvcmQ6Iiwgc2hvdz0iKiIpCgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLlBhc3N3b3JkIGFzIFBTCgogICAgICAgICAgICAgICAgUFMuUGFzc3dvcmQoRXZlbnQ9J0NhY2hlJywgSW5wdXQ9SW5wdXQpCiAgICAgICAgICAgICAgICBtZXNzYWdlYm94LnNob3dpbmZvKCJQYXNzd29yZCIsICJDb3JyZWN0IFBhc3N3b3JkIikKICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvSW50LnR4dCcsICd3JykuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgIHByaW50KCd8ICB8ICAgICAgICAgICAgICAgIEludC50eHQgQ2xlYXJlZCcpCiAgICAgICAgICAgICAgICAgICAgaW1wb3J0IHNodXRpbAoKICAgICAgICAgICAgICAgICAgICB1c2VyID0gVXNlci5Vc2VyUHJvZmlsZS5Vc2VybmFtZQogICAgICAgICAgICAgICAgICAgIHNodXRpbC5ybXRyZWUoZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0xvY2FsJykKICAgICAgICAgICAgICAgICAgICBvcy5ta2RpcihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vTG9jYWwnKQogICAgICAgICAgICAgICAgICAgIHByaW50KCd8ICB8ICAgICAgICAgICAgICAgIExvY2FsIENvbm5lY3Rpb25zIFJlc2V0JykKICAgICAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgICAgIHNodXRpbC5ybXRyZWUoZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9Eb3dubG9hZHMnKQogICAgICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICAgICAgICAgIHByaW50KCd8ICB8ICAgICAgICAgICAgICAgIERvd25sb2FkcyBSZXNldCcpCiAgICAgICAgICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vRXJyb3JMb2cvRXZlbnRzJywgJ3cnKS5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ3wgIHwgICAgICAgICAgICAgICAgRXZlbnRzIENsZWFyZWQnKQogICAgICAgICAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0Vycm9yTG9nL0Vycm9ycycsICd3JykuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgIHByaW50KCd8ICB8ICAgICAgICAgICAgICAgIEVycm9ycyBDbGVhcmVkJykKICAgICAgICAgICAgICAgICAgICBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1VzZXIvRmlyc3RVc2VUb2tlbi50eHQnLCAndycpLmNsb3NlKCkKICAgICAgICAgICAgICAgICAgICBwcmludCgnfCAgfCAgICAgICAgICAgICAgICBGaXJzdFVzZVRva2VuIGFkZGVkJykKICAgICAgICAgICAgICAgICAgICBvcGVuKGYne2N3ZH0vVXNlci9Vc2VyUHJvZmlsZS5weScsICd3JykuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgIHByaW50KCd8ICB8ICAgICAgICAgICAgICAgIFVzZXIgUHJvZmlsZSBXaXBlZCcpCiAgICAgICAgICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0NvbXBsZXhfaW5zdGFsbCcsICJ3IikuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9Db21wbGV4JywgInciKS5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0NvbXBsZXgyJywgInciKS5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL2ludDIudHh0JywgInciKS5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgb3BlbihmJ3tVc2VyLlVzZXJQcm9maWxlLlNvdXJjZURpcmVjdG9yeX1TeXN0ZW0vQ2FjaGUvU3lzdGVtL0Vycm9yTG9nL0V2ZW50LmRiJywgJ3cnKQogICAgICAgICAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0xvY2FsL0ludC50eHQnLCAidyIpLmNsb3NlKCkKICAgICAgICAgICAgICAgICAgICBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9Mb2NhbC9JbnQyLnR4dCcsICJ3IikuY2xvc2UoKQoKICAgICAgICAgICAgICAgICAgICBwcmludChmJ3wgIHwgICAgICAgICAgICAgICAgVXBkYXRlIFJlY29yZGVkJykKICAgICAgICAgICAgICAgIGV4Y2VwdDoKCiAgICAgICAgICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0V2ZXJ5dGhpbmcgRmFpbGVkIFRvIFJlc2V0IER1ZSBUbyBQYXNzd29yZCBFcnJvcicsIFBvbD0wKQogICAgICAgICAgICAgICAgICAgIHJhaXNlIGV4aXQoMCkKCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDIpCiAgICAgICAgICAgICAgICBwcmludChmJ1xuJyAqIDYwKQogICAgICAgICAgICBleGNlcHQgVmFsdWVFcnJvcjoKICAgICAgICAgICAgICAgICMKCiAgICAgICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnRnVsbCByZXNldCBmYWlsZWQgZHVlIHRvIHVzZXIgcGFzcycsIFBvbD0xKQoKZGVmIENyZWF0ZSgpOgogICAgaW1wb3J0IFVzZXIuVXNlclByb2ZpbGUKICAgIGltcG9ydCBoYXNobGliCiAgICBpbXBvcnQgdXVpZAoKICAgIElucHV0ID0gc2ltcGxlZGlhbG9nLmFza3N0cmluZygiQ2hhbmdlIFBhc3N3b3JkIiwgIkVOVEVSIE5FVyBQQVNTV09SRDoiLCBzaG93PSIqIikKICAgIFVVSUQgPSB1dWlkLnV1aWQxKCkKCiAgICBVc2VySUQgPSBvcy5nZXRsb2dpbigpCgogICAgc2FsdCA9ICI5bGsiCgogICAgVVVJRCA9IHN0cihmJ3tVVUlEfScpCgogICAgdXVpZFRva2VuID0gVVVJRFszMDpdCiAgICBEZWZhdWx0VGtuID0gVXNlci5Vc2VyUHJvZmlsZS51dWlkMQoKICAgIFBhc3N3b3JkID0gZid7SW5wdXR9e3V1aWRUb2tlbn17VXNlcklEfScKCiAgICBwYXNzd29yZCA9IFBhc3N3b3JkICsgc2FsdAogICAgaGFzaGVkID0gaGFzaGxpYi5tZDUocGFzc3dvcmQuZW5jb2RlKCkpCiAgICBQYXNzd29yZCA9IGhhc2hlZC5oZXhkaWdlc3QoKQogICAgbWVzc2FnZWJveC5zaG93aW5mbygiVXBkYXRlIiwgIkNsaWNrICdPaycgVG8gQWNjZXNzZXMgTmV3IEtleSIpCiAgICB1cCA9IG9wZW4oZid7b3MuZ2V0Y3dkKCl9L1VzZXIvVXNlclByb2ZpbGUucHknLCAnYScpCiAgICB1cC53cml0ZShmIlxuUGFzc3dvcmQgPSAne1Bhc3N3b3JkfSciKQogICAgcHJpbnQoUGFzc3dvcmQpCgpkZWYgc2V0dGluZ3Nfd2luZG93KCk6CiAgICBzZXR0aW5nc193aW4gPSB0ay5Ub3BsZXZlbChyb290KQogICAgc2V0dGluZ3Nfd2luLnRpdGxlKCJTZXR0aW5ncyIpCgogICAgb3B0aW9ucyA9IFsKICAgICAgICAiVG9nZ2xlIEZvcmNlZCBNb2R1bGUgSW1wb3J0IiwKICAgICAgICAiVG9nZ2xlIEZvcmNlZCBMb2dpbiIsCiAgICAgICAgIlRvZ2dsZSBTeXN0ZW0gRXZlbnQgZGlzcGxheSIsCiAgICAgICAgIkVuYWJsZSBDb21tYW5kIExpbmUgSW50ZXJmYWNlIiwKICAgICAgICAiQ2hhbmdlIFVzZXJOYW1lIiwKICAgICAgICAiQ2hhbmdlIFBhc3N3b3JkIiwKICAgICAgICAicmVzZXQgYWxsIgogICAgXQoKICAgIGRlZiBkb19zb21ldGhpbmcoaW5kZXgpOgogICAgICAgIGlmIGluZGV4ID09IDA6CiAgICAgICAgICAgICMgcmVxdWlyZSBVU0VSX1BBU1MKICAgICAgICAgICAgaW1wb3J0IG9zLCB0aW1lCiAgICAgICAgICAgIHBhc3MKCiAgICAgICAgICAgIElucHV0ID0gc2ltcGxlZGlhbG9nLmFza3N0cmluZygiR0hQTSIsICdFbnRlciBQYXNzd29yZDogJykKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5QYXNzd29yZCBhcyBQUwogICAgICAgICAgICAgICAgUFMuUGFzc3dvcmQoRXZlbnQ9J0ZvcmNlZCBMb2dpbicsIElucHV0PUlucHV0KQoKICAgICAgICAgICAgICAgIGltcG9ydF90b2tlbiA9IG9wZW4oZid7Y3dkfS9Vc2VyL1VzZXJQcm9maWxlLnB5JywgJ2EnKQogICAgICAgICAgICAgICAgaW1wb3J0IFVzZXIuVXNlclByb2ZpbGUKICAgICAgICAgICAgICAgIGlmIFVzZXIuVXNlclByb2ZpbGUuRm9yY2VfSW1wb3J0X1JlcXVlc3QgaXMgVHJ1ZToKICAgICAgICAgICAgICAgICAgICBTdGF0dXMgPSBGYWxzZQogICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICBTdGF0dXMgPSBUcnVlCgogICAgICAgICAgICAgICAgaW1wb3J0X3Rva2VuLndyaXRlKGYnXG5Gb3JjZV9JbXBvcnRfUmVxdWVzdCA9IHtTdGF0dXN9JykKICAgICAgICAgICAgICAgIGltcG9ydF90b2tlbi5jbG9zZSgpCgogICAgICAgICAgICAgICAgIwoKICAgICAgICAgICAgICAgIHBhc3MgICMgZXZlbnQ9Zidmb3JjZWQgTW9kdWxlIEltcG9ydCA9IHtTdGF0dXN9JywgUG9sPTApCiAgICAgICAgICAgICAgICBtZXNzYWdlYm94LnNob3dpbmZvKCJHSFBNIiwgJ1VwZGF0ZSBSZWNvcmRlZCcpCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDIpCgogICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICBJbnB1dCA9IHNpbXBsZWRpYWxvZy5hc2tzdHJpbmcoIkdIUE0iLCAnRW50ZXIgUGFzc3dvcmQ6ICcpCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5QYXNzd29yZCBhcyBQUwogICAgICAgICAgICAgICAgICAgIFBTLlBhc3N3b3JkKEV2ZW50PSdGb3JjZWQgTG9naW4nLCBJbnB1dD1JbnB1dCkKCiAgICAgICAgICAgICAgICAgICAgaW1wb3J0X3Rva2VuID0gb3BlbihmJ3tjd2R9L1VzZXIvVXNlclByb2ZpbGUucHknLCAnYScpCiAgICAgICAgICAgICAgICAgICAgaW1wb3J0IFVzZXIuVXNlclByb2ZpbGUKICAgICAgICAgICAgICAgICAgICBpZiBVc2VyLlVzZXJQcm9maWxlLkZvcmNlX0ltcG9ydF9SZXF1ZXN0IGlzIFRydWU6CiAgICAgICAgICAgICAgICAgICAgICAgIFN0YXR1cyA9IEZhbHNlCiAgICAgICAgICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgICAgICAgICAgU3RhdHVzID0gVHJ1ZQoKICAgICAgICAgICAgICAgICAgICBpbXBvcnRfdG9rZW4ud3JpdGUoZidcbkZvcmNlX0ltcG9ydF9SZXF1ZXN0ID0ge1N0YXR1c30nKQogICAgICAgICAgICAgICAgICAgIGltcG9ydF90b2tlbi5jbG9zZSgpCgogICAgICAgICAgICAgICAgICAgICMKCiAgICAgICAgICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ2ZvcmNlZCBNb2R1bGUgSW1wb3J0ID0ge1N0YXR1c30nLCBQb2w9MCkKICAgICAgICAgICAgICAgICAgICBtZXNzYWdlYm94LnNob3dpbmZvKCJHSFBNIiwgJ1VwZGF0ZSBSZWNvcmRlZCcpCiAgICAgICAgICAgICAgICAgICAgdGltZS5zbGVlcCgyKQoKICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICBtZXNzYWdlYm94LnNob3dpbmZvKCdGaW5hbCBBdHRlbXB0JykKICAgICAgICAgICAgICAgICAgICBJbnB1dCA9IHNpbXBsZWRpYWxvZy5hc2tzdHJpbmcoIkdIUE0iLCAnRW50ZXIgUGFzc3dvcmQ6ICcpCiAgICAgICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLlBhc3N3b3JkIGFzIFBTCiAgICAgICAgICAgICAgICAgICAgICAgIFBTLlBhc3N3b3JkKEV2ZW50PSdGb3JjZWQgTG9naW4nLCBJbnB1dD1JbnB1dCkKCiAgICAgICAgICAgICAgICAgICAgICAgIGltcG9ydF90b2tlbiA9IG9wZW4oZid7Y3dkfS9Vc2VyL1VzZXJQcm9maWxlLnB5JywgJ2EnKQogICAgICAgICAgICAgICAgICAgICAgICBpbXBvcnQgVXNlci5Vc2VyUHJvZmlsZQogICAgICAgICAgICAgICAgICAgICAgICBpZiBVc2VyLlVzZXJQcm9maWxlLkZvcmNlX0ltcG9ydF9SZXF1ZXN0IGlzIFRydWU6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBTdGF0dXMgPSBGYWxzZQogICAgICAgICAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgU3RhdHVzID0gVHJ1ZQoKICAgICAgICAgICAgICAgICAgICAgICAgaW1wb3J0X3Rva2VuLndyaXRlKGYnXG5Gb3JjZV9JbXBvcnRfUmVxdWVzdCA9IHtTdGF0dXN9JykKICAgICAgICAgICAgICAgICAgICAgICAgaW1wb3J0X3Rva2VuLmNsb3NlKCkKCiAgICAgICAgICAgICAgICAgICAgICAgICMKCiAgICAgICAgICAgICAgICAgICAgICAgIHBhc3MgICMgZXZlbnQ9Zidmb3JjZWQgTW9kdWxlIEltcG9ydCA9IHtTdGF0dXN9JywgUG9sPTApCiAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2Vib3guc2hvd2luZm8oIkdIUE0iLCAnVXBkYXRlIFJlY29yZGVkJykKICAgICAgICAgICAgICAgICAgICAgICAgdGltZS5zbGVlcCgyKQoKCiAgICAgICAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlYm94LnNob3dpbmZvKCJHSFBNIiwgJ0luY29ycmVjdCBQYXNzd29yZCcpCgogICAgICAgIGVsaWYgaW5kZXggPT0gMToKICAgICAgICAgICAgIyByZXF1aXJlIFVTRVJfUEFTUwogICAgICAgICAgICBpbXBvcnQgb3MsIHRpbWUKICAgICAgICAgICAgcGFzcwogICAgICAgICAgICBJbnB1dCA9IHNpbXBsZWRpYWxvZy5hc2tzdHJpbmcoIkdIUE0iLCAnRW50ZXIgUGFzc3dvcmQ6ICcpCiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuUGFzc3dvcmQgYXMgUFMKICAgICAgICAgICAgICAgIFBTLlBhc3N3b3JkKEV2ZW50PSdGb3JjZWQgTG9naW4nLCBJbnB1dD1JbnB1dCkKCiAgICAgICAgICAgICAgICBpbXBvcnRfdG9rZW4gPSBvcGVuKGYne2N3ZH0vVXNlci9Vc2VyUHJvZmlsZS5weScsICdhJykKICAgICAgICAgICAgICAgIGltcG9ydCBVc2VyLlVzZXJQcm9maWxlCiAgICAgICAgICAgICAgICBpZiBVc2VyLlVzZXJQcm9maWxlLkZvcmNlZF9Mb2dpbiBpcyBUcnVlOgogICAgICAgICAgICAgICAgICAgIFN0YXR1cyA9IEZhbHNlCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIFN0YXR1cyA9IFRydWUKCiAgICAgICAgICAgICAgICBpbXBvcnRfdG9rZW4ud3JpdGUoZidcbkZvcmNlZF9Mb2dpbiA9IHtTdGF0dXN9JykKICAgICAgICAgICAgICAgIGltcG9ydF90b2tlbi5jbG9zZSgpCgogICAgICAgICAgICAgICAgIwoKICAgICAgICAgICAgICAgIHBhc3MgICMgZXZlbnQ9ZidGb3JjZWRMb2dpbiA9IHtTdGF0dXN9JywgUG9sPTApCiAgICAgICAgICAgICAgICBtZXNzYWdlYm94LnNob3dpbmZvKCJHSFBNIiwgJ1VwZGF0ZSBSZWNvcmRlZCcpCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDIpCgogICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICBJbnB1dCA9IHNpbXBsZWRpYWxvZy5hc2tzdHJpbmcoIkdIUE0iLCAnRW50ZXIgUGFzc3dvcmQ6ICcpCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5QYXNzd29yZCBhcyBQUwogICAgICAgICAgICAgICAgICAgIFBTLlBhc3N3b3JkKEV2ZW50PSdGb3JjZWQgTG9naW4nLCBJbnB1dD1JbnB1dCkKCiAgICAgICAgICAgICAgICAgICAgaW1wb3J0X3Rva2VuID0gb3BlbihmJ3tjd2R9L1VzZXIvVXNlclByb2ZpbGUucHknLCAnYScpCiAgICAgICAgICAgICAgICAgICAgaW1wb3J0IFVzZXIuVXNlclByb2ZpbGUKICAgICAgICAgICAgICAgICAgICBpZiBVc2VyLlVzZXJQcm9maWxlLkZvcmNlZF9Mb2dpbiBpcyBUcnVlOgogICAgICAgICAgICAgICAgICAgICAgICBTdGF0dXMgPSBGYWxzZQogICAgICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgICAgIFN0YXR1cyA9IFRydWUKCiAgICAgICAgICAgICAgICAgICAgaW1wb3J0X3Rva2VuLndyaXRlKGYnXG5Gb3JjZWRfTG9naW4gPSB7U3RhdHVzfScpCiAgICAgICAgICAgICAgICAgICAgaW1wb3J0X3Rva2VuLmNsb3NlKCkKCiAgICAgICAgICAgICAgICAgICAgIwoKICAgICAgICAgICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnRm9yY2VkTG9naW4gPSB7U3RhdHVzfScsIFBvbD0wKQogICAgICAgICAgICAgICAgICAgIG1lc3NhZ2Vib3guc2hvd2luZm8oIkdIUE0iLCAnVXBkYXRlIFJlY29yZGVkJykKICAgICAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKDIpCiAgICAgICAgICAgICAgICAgICAgbWVzc2FnZWJveC5zaG93aW5mbyhmJ1xuJyAqIDYwKQogICAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgICAgIG1lc3NhZ2Vib3guc2hvd2luZm8oJ0ZpbmFsIEF0dGVtcHQnKQogICAgICAgICAgICAgICAgICAgIElucHV0CiAgICAgICAgICAgICAgICAgICAgc2ltcGxlZGlhbG9nLmFza3N0cmluZygiR0hQTSIsICdFbnRlciBQYXNzd29yZDogJykKICAgICAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuUGFzc3dvcmQgYXMgUFMKICAgICAgICAgICAgICAgICAgICAgICAgUFMuUGFzc3dvcmQoRXZlbnQ9J0ZvcmNlZCBMb2dpbicsIElucHV0PUlucHV0KQoKICAgICAgICAgICAgICAgICAgICAgICAgaW1wb3J0X3Rva2VuID0gb3BlbihmJ3tjd2R9L1VzZXIvVXNlclByb2ZpbGUucHknLCAnYScpCiAgICAgICAgICAgICAgICAgICAgICAgIGltcG9ydCBVc2VyLlVzZXJQcm9maWxlCiAgICAgICAgICAgICAgICAgICAgICAgIGlmIFVzZXIuVXNlclByb2ZpbGUuRm9yY2VkX0xvZ2luIGlzIFRydWU6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBTdGF0dXMgPSBGYWxzZQogICAgICAgICAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgU3RhdHVzID0gVHJ1ZQoKICAgICAgICAgICAgICAgICAgICAgICAgaW1wb3J0X3Rva2VuLndyaXRlKGYnXG5Gb3JjZWRfTG9naW4gPSB7U3RhdHVzfScpCiAgICAgICAgICAgICAgICAgICAgICAgIGltcG9ydF90b2tlbi5jbG9zZSgpCgogICAgICAgICAgICAgICAgICAgICAgICAjCgogICAgICAgICAgICAgICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnRm9yY2VkTG9naW4gPSB7U3RhdHVzfScsIFBvbD0wKQogICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlYm94LnNob3dpbmZvKCJHSFBNIiwgJ1VwZGF0ZSBSZWNvcmRlZCcpCiAgICAgICAgICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMikKICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZWJveC5zaG93aW5mbyhmJ1xuJyAqIDYwKQogICAgICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZWJveC5zaG93aW5mbygiR0hQTSIsICdXcm9uZyBQYXNzd29yZCBFbnRlcmVkJykKICAgICAgICAgICAgICAgICAgICAgICAgcGFzcwoKICAgICAgICAgICAgIwoKICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ1VwZGF0ZWQgQ2FuY2VsZWQnLCBQb2w9MCkKCiAgICAgICAgZWxpZiBpbmRleCA9PSAyOgogICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnTGF1bmNoaW5nIEV2ZW50IERpc3BsYXknLCBQb2w9MSkKICAgICAgICAgICAgdGFyZ2V0ID0gb3BlbihmJ3tjd2R9L1VzZXIvVXNlclByb2ZpbGUucHknLCAnYScpCiAgICAgICAgICAgIGltcG9ydCBVc2VyCiAgICAgICAgICAgIENzdGF0ID0gVXNlci5Vc2VyUHJvZmlsZS5EaXNwbGF5RXZlbnRzCiAgICAgICAgICAgIGlmIENzdGF0IGlzIFRydWU6CiAgICAgICAgICAgICAgICBzdGF0dXMgPSBGYWxzZQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgc3RhdHVzID0gRmFsc2UKCiAgICAgICAgICAgIHRhcmdldC53cml0ZShmJ1xuRGlzcGxheUV2ZW50cyA9IHtzdGF0dXN9JykKICAgICAgICAgICAgbWVzc2FnZWJveC5zaG93aW5mbygiVXBkYXRlIiwgZidEaXNwbGF5RXZlbnRzIHNldCB0byB7c3RhdHVzfScpCgoKCiAgICAgICAgZWxpZiBpbmRleCA9PSAzOgogICAgICAgICAgICBpbXBvcnQgb3MKICAgICAgICAgICAgcGFzcyAgIyBldmVudD0nQ3JlYXRpbmcgR2xvYmFsIEFsaWFzJywgUG9sPTEwKQogICAgICAgICAgICBpbXBvcnQgVXNlcgogICAgICAgICAgICBhbGlhcyA9IGYnJydlY2hvICdhbGlhcyBnaD0iY2Qge1VzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5fSAmJnB5dGhvbjMgZ2gucHkiJyA+PiB+Ly56c2hyYyAmJiBleGVjIHpzaCAtbCcnJwogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBwcmludChhbGFpcykKICAgICAgICAgICAgICAgIG9zLnN5c3RlbShhbGlhcykKICAgICAgICAgICAgICAgIHBhc3MgICMgZXZlbnQ9J0luc3RhbGxpbmcgR2xvYmFsIEFsaWFzLSBDb21wbGV0ZScsIFBvbD0yMCkKICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgcGFzcyAgIyBldmVudD0nRXJyb3IgSW5zdGFsbGluZyBHbG9iYWwgQWxpYXMnLCBQb2w9MjApCgogICAgICAgICAgICBtZXNzYWdlYm94LnNob3dpbmZvKCJHSFBNIiwgZicnJ1RvIExhdW5jaCBUaGUgQ0xJLCBJbiB5b3VyIHRlcm1pbmFsIGFsbCB5b3UgbmVlZCB0byBkbyBpcyBydW4gZ2ggKGFyZykKCmV4YW1wbGVzOgpbZ2ggLUkgaHR0cHM6Ly9naXRodWIuY29tL1NvbWVVc2VyL1NvbWV0aGluZy5naXRdIC0+IHRoaXMgaW5zdGFsbHMgdGhlIHJlcG8gZm9sbG93aW5nIC1JCltnaCAtSUwgIC9Vc2Vycy9Tb21lb25lL1NvbWV0aGluZ10gLT4gdGhpcyB3aWxsIGltcG9ydCBhbGwgb2YgdGhlIGZpbGVzIHdpdGhpbiB0aGUgc3BlY2lmaWVkIGRpcmVjdG9yeQoKPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KSGVscAo9PT09Ci1JIC0+IEluc3RhbGwgKGFyZzxyZXBvPikKLUlMIC0+IEluc3RhbGwgTG9jYWwgKGFyZzxkaXI+KQoKLUxBIC0+IExpc3QgQWxsIEluc3RhbGxzCi1MTCAtPiBMYXVuY2ggTG9jYWwgRGlyZWN0b3J5Ci1MRyAtPiBMYXVuY2ggR2l0IFByb2plY3QKLUxDIC0+IExhdW5jaCBBZHZhbmNlZCBQcm9qZWN0cwoKLVVHIC0+IFVuaW5zdGFsbCBHaXRIdWIgUHJvamVjdHMKLVVMIC0+IFVuaW5zdGFsbCBMb2NhbCBkaXJlY3RvcmllcycnJykKICAgICAgICAgICAgbWVzc2FnZWJveC5zaG93aW5mbygiQ0xJIiwgIm5vdyBhdmFpbGFibGUiKQogICAgICAgIGVsaWYgaW5kZXggPT0gNDoKICAgICAgICAgICAgaW1wb3J0IG9zCiAgICAgICAgICAgIE5hbWUgPSBzaW1wbGVkaWFsb2cuYXNrc3RyaW5nKCJHSFBNIiwgJ0VudGVyIFlvdXIgRGVzaXJlZCBVc2VyTmFtZTogJykKICAgICAgICAgICAgdXAgPSBvcGVuKGYne29zLmdldGN3ZCgpfS9Vc2VyL1VzZXJQcm9maWxlLnB5JywgJ2EnKQogICAgICAgICAgICB1cC53cml0ZShmIlxuVXNlcm5hbWUgPSAne05hbWV9JyIpCiAgICAgICAgICAgIHVwLmNsb3NlKCkKICAgICAgICAgICAgbWVzc2FnZWJveC5zaG93aW5mbygiVXBkYXRlIiwgIlVzZXJOYW1lIFVwZGF0ZWQiKQoKICAgICAgICBlbGlmIGluZGV4ID09IDU6CgogICAgICAgICAgICBJbnB1dCA9IHNpbXBsZWRpYWxvZy5hc2tzdHJpbmcoIkNoYW5nZSBQYXNzd29yZCIsICJFbnRlciB5b3VyIHBhc3N3b3JkOiIsIHNob3c9IioiKQogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLlBhc3N3b3JkIGFzIFBTCiAgICAgICAgICAgICAgICBQUy5QYXNzd29yZChFdmVudD0nUGFzc3dvcmQgVXBkYXRlJywgSW5wdXQ9SW5wdXQpCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgaW1wb3J0IFN5c3RlbS5Ecml2ZS5QYXNzd29yZCBhcyBwcwogICAgICAgICAgICAgICAgICAgIENyZWF0ZSgpCiAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICBJbnB1dCA9IHNpbXBsZWRpYWxvZy5hc2tzdHJpbmcoIkNoYW5nZSBQYXNzd29yZCIsICJFbnRlciB5b3VyIHBhc3N3b3JkOiIsIHNob3c9IioiKQogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuUGFzc3dvcmQgYXMgUFMKICAgICAgICAgICAgICAgICAgICBQUy5QYXNzd29yZChFdmVudD0nUGFzc3dvcmQgVXBkYXRlJywgSW5wdXQ9SW5wdXQpCiAgICAgICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLlBhc3N3b3JkIGFzIHBzCiAgICAgICAgICAgICAgICAgICAgICAgIENyZWF0ZSgpCiAgICAgICAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgICAgICAgICBwYXNzCiAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgSW5wdXQgPSBzaW1wbGVkaWFsb2cuYXNrc3RyaW5nKCJDaGFuZ2UgUGFzc3dvcmQiLCAiRW50ZXIgeW91ciBwYXNzd29yZDoiLCBzaG93PSIqIikKICAgICAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgICAgIGltcG9ydCBTeXN0ZW0uRHJpdmUuUGFzc3dvcmQgYXMgUFMKICAgICAgICAgICAgICAgICAgICAgICAgUFMuUGFzc3dvcmQoRXZlbnQ9J1Bhc3N3b3JkIFVwZGF0ZScsIElucHV0PUlucHV0KQogICAgICAgICAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpbXBvcnQgU3lzdGVtLkRyaXZlLlBhc3N3b3JkIGFzIHBzCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBDcmVhdGUoKQogICAgICAgICAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYXNzCiAgICAgICAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgICAgICAgICBwYXNzCgogICAgICAgIGVsaWYgaW5kZXggPT0gNjoKICAgICAgICAgICAgcmVzZXRfYWxsKCkKCiAgICB0cnk6CiAgICAgICAgZm9yIGksIG9wdGlvbiBpbiBlbnVtZXJhdGUob3B0aW9ucyk6CiAgICAgICAgICAgIGJ1dHRvbiA9IHRrLkJ1dHRvbihzZXR0aW5nc193aW4sIHRleHQ9b3B0aW9uLCBjb21tYW5kPWxhbWJkYSBpPWk6IGRvX3NvbWV0aGluZyhpKSkKICAgICAgICAgICAgYnV0dG9uLnBhY2soKQogICAgZXhjZXB0OgogICAgICAgIHBhc3MKCmRlZiBjcnlwdCgpOgogICAgbWVzc2FnZWJveC5zaG93ZXJyb3IoIkVycm9yIiwgIk5vdCBhdmFpbGFibGUiKQoKZGVmIHNob3dfaW5zdGFsbCgpOgogICAgdHJ5OgogICAgICAgIG9zLm1rZGlyKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvRG93bmxvYWRzJykKICAgIGV4Y2VwdDoKICAgICAgICBwYXNzCiAgICBjbG9zZV93aW5kb3dzKCkKICAgIGdsb2JhbCBpbnN0YWxsX3dpbmRvdwoKICAgIGZyb20gdGtpbnRlciBpbXBvcnQgZmlsZWRpYWxvZwogICAgZnJvbSB0a2ludGVyIGltcG9ydCB0dGsKCiAgICBkZWYgY2hvb3NlX2ZvbGRlcigpOgogICAgICAgIGZvbGRlcl9wYXRoID0gZmlsZWRpYWxvZy5hc2tkaXJlY3RvcnkoKQogICAgICAgIGluc3RhbGxfZW50cnkuaW5zZXJ0KDAsIGZvbGRlcl9wYXRoKQoKICAgIGluc3RhbGxfd2luZG93ID0gdGsuVG9wbGV2ZWwocm9vdCkKICAgIGluc3RhbGxfd2luZG93Lmdlb21ldHJ5KCI0MDB4NDAwIikKICAgIGluc3RhbGxfd2luZG93LnRpdGxlKCJJbnN0YWxsIikKCiAgICBpbnN0YWxsX2xhYmVsID0gdGsuTGFiZWwoaW5zdGFsbF93aW5kb3csIHRleHQ9IkVudGVyIGEgcGF0aCB0byBhIGxvY2FsIGRpcmVjdG9yeSBvciBhIEdpdEh1YiByZXBvc2l0b3J5IFVSTDoiKQogICAgaW5zdGFsbF9sYWJlbC5wYWNrKCkKCiAgICBpbnN0YWxsX2VudHJ5ID0gdGsuRW50cnkoaW5zdGFsbF93aW5kb3cpCiAgICBpbnN0YWxsX2VudHJ5LnBhY2soKQoKICAgIGNob29zZV9mb2xkZXJfYnV0dG9uID0gdHRrLkJ1dHRvbihpbnN0YWxsX3dpbmRvdywgdGV4dD0iQ2hvb3NlIGZvbGRlciIsIGNvbW1hbmQ9Y2hvb3NlX2ZvbGRlcikKICAgIGNob29zZV9mb2xkZXJfYnV0dG9uLnBhY2soKQoKICAgIGluc3RhbGxfc3VibWl0ID0gdGsuQnV0dG9uKGluc3RhbGxfd2luZG93LCB0ZXh0PSJTdWJtaXQiLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY29tbWFuZD1sYW1iZGE6IGRvX3NvbWV0aGluZ193aXRoX3ZhbHVlKGluc3RhbGxfZW50cnkuZ2V0KCkpKQogICAgaW5zdGFsbF9zdWJtaXQucGFjaygpCgpkZWYgZG9fc29tZXRoaW5nX3dpdGhfdmFsdWUodmFsdWUpOgogICAgZnJvbSB1cmxsaWIucGFyc2UgaW1wb3J0IHVybHBhcnNlCiAgICBpbnN0YWxsX3dpbmRvdy5kZXN0cm95KCkKCiAgICBkZWYgaXNfdXJsKHN0cmluZyk6CiAgICAgICAgcGFyc2VkX3VybCA9IHVybHBhcnNlKHN0cmluZykKICAgICAgICByZXR1cm4gYm9vbChwYXJzZWRfdXJsLnNjaGVtZSkKCiAgICBpZiBpc191cmwoc3RyaW5nPXZhbHVlKSBpcyBUcnVlOgoKICAgICAgICBpbnN0YWxsX3dpbmRvdy5kZXN0cm95KCkKICAgICAgICB0cnk6CiAgICAgICAgICAgIEluc3RhbGxlcih2YWx1ZSkKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIHBhc3MKICAgIGVsc2U6CiAgICAgICAgRmlsZXMwID0gW10KICAgICAgICBJbXBvcnREaXJlY3RvcnkgPSB2YWx1ZQogICAgICAgIGZvciBwYXRoIGluIG9zLmxpc3RkaXIoSW1wb3J0RGlyZWN0b3J5KToKICAgICAgICAgICAgIyBjaGVjayBpZiBjdXJyZW50IHBhdGggaXMgYSBmaWxlCiAgICAgICAgICAgIGlmIG9zLnBhdGguaXNmaWxlKG9zLnBhdGguam9pbihJbXBvcnREaXJlY3RvcnksIHBhdGgpKToKICAgICAgICAgICAgICAgIEZpbGVzMC5hcHBlbmQocGF0aCkKICAgICAgICAjCgogICAgICAgIHBhc3MgICMgZXZlbnQ9ZidGaWxlcyBDb25uZWN0ZWQgLS1DT01NQU5EIExJTkUnLCBQb2w9MCkKCiAgICAgICAgY291bnRlciA9IDAKICAgICAgICBmb3IgZmlsZSBpbiBGaWxlczA6CiAgICAgICAgICAgIGNvdW50ZXIgKz0gMQogICAgICAgICAgICBwcmludChmJ3tjb3VudGVyfSB8IHtmaWxlfScpCgogICAgICAgIGRlZiBidXR0b25fY2xpY2soaXRlbSk6CiAgICAgICAgICAgIHJvb3QuZGVzdHJveSgpCiAgICAgICAgICAgIGZpID0gRmlsZXMwLmluZGV4KGl0ZW0pCgogICAgICAgICAgICBmaSA9IEZpbGVzMFtpbnQoZmkpXQogICAgICAgICAgICAjIFJlbW92ZSBhbGwgY2hhcmFjdGVycyBiZWZvcmUgdGhlIGNoYXJhY3RlciAnLScgZnJvbSBzdHJpbmcKICAgICAgICAgICAgZmUgPSBmaS5zcGxpdCgnLicsIDEpCiAgICAgICAgICAgIGlmIGxlbihmZSkgPiAwOgogICAgICAgICAgICAgICAgZmZpID0gZmVbMV0KCiAgICAgICAgICAgIGlmICdweScgaW4gZmZpOgogICAgICAgICAgICAgICAgcDEgPSBmJyt7SW1wb3J0RGlyZWN0b3J5fSAtcHl0aG9uMyB7SW1wb3J0RGlyZWN0b3J5fS97Zml9KicKICAgICAgICAgICAgaWYgZmZpID09ICcuYyc6CiAgICAgICAgICAgICAgICBwMSA9IGYnK3tJbXBvcnREaXJlY3Rvcnl9IC1nY2Mge0ltcG9ydERpcmVjdG9yeX0ve2ZpfSonCiAgICAgICAgICAgIGVsaWYgJ2NwcCcgaW4gZmZpOgogICAgICAgICAgICAgICAgcDEgPSBmJyt7SW1wb3J0RGlyZWN0b3J5fSAtZ3BwIHtJbXBvcnREaXJlY3Rvcnl9L3tmaX0qJwogICAgICAgICAgICBlbGlmICdzaCcgaW4gZmZpOgogICAgICAgICAgICAgICAgcDEgPSBmJyt7SW1wb3J0RGlyZWN0b3J5fSAtYmFzaCB7SW1wb3J0RGlyZWN0b3J5fS97Zml9KicKCiAgICAgICAgICAgIHByaW50KCdbIV0gQ2hlY2tQb2ludCA0fDQgWyFdJykKCiAgICAgICAgICAgIEZvcm0gPSBmJ3tmaVs6LTNdfSA9ICJ7cDF9IicKICAgICAgICAgICAgIwoKICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0xhdW5jaCBDb21tYW5kIENvbXBsZXRlOiB7Rm9ybX0gLS1DT01NQU5EIExJTkUnLCBQb2w9MCkKCiAgICAgICAgICAgIGYgPSBvcGVuKGYne2N3ZH1TeXN0ZW0vQ2FjaGUvU3lzdGVtL0xvY2FsL0ludC50eHQnLCAnYScpCiAgICAgICAgICAgIGYud3JpdGUoZidcbntGb3JtfScpCiAgICAgICAgICAgIGYuY2xvc2UoKQogICAgICAgICAgICBpbXBvcnQgVXNlcgogICAgICAgICAgICBwcmludCgnSW5zdGFsbGF0aW9uIENvbXBsZXRlIScpCiAgICAgICAgICAgIG9zLmNoZGlyKFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5KQoKICAgICAgICByb290ID0gdGsuVGsoKQoKICAgICAgICBpdGVtX2xpc3QgPSBGaWxlczAKCiAgICAgICAgZm9yIGl0ZW0gaW4gaXRlbV9saXN0OgogICAgICAgICAgICB0ay5CdXR0b24ocm9vdCwgdGV4dD1pdGVtLCBjb21tYW5kPWxhbWJkYSBpPWl0ZW06IGJ1dHRvbl9jbGljayhpKSkucGFjaygpCgogICAgICAgIHJvb3QubWFpbmxvb3AoKQoKZGVmIGNvbmZpcm1fdW5pbnN0YWxsKHNlbGVjdGVkX2l0ZW0pOgogICAgaW1wb3J0IHRraW50ZXIubWVzc2FnZWJveAogICAgcmVzdWx0ID0gdGsubWVzc2FnZWJveC5hc2t5ZXNubygiQ29uZmlybSBVbmluc3RhbGwiLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiQXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHVuaW5zdGFsbCAiICsgc2VsZWN0ZWRfaXRlbSArICI/IikKICAgICMgcmVtb3ZlIGEgbGluZSBjb250YWluaW5nIGEgc3RyaW5nCiAgICBsaXN0X3dpbmRvdy5kZXN0cm95KCkKCiAgICB2YWx1ZWUgPSBpdGVtcy5pbmRleChzZWxlY3RlZF9pdGVtKQoKICAgIGlmIHZhbHVlZSA+PSBjb3VudDoKICAgICAgICBkciA9IGludCh2YWx1ZWUpIC0gY291bnQKICAgICAgICBjb21tYW5kID0gbGluZXMyW2RyIC0gMV0KICAgICAgICBwcmludChjb21tYW5kKQogICAgICAgIGNvID0gY29tbWFuZC5zcGxpdCgnJCcsIDEpWzBdCiAgICAgICAgcHJpbnQoY28pCiAgICAgICAgdHJ5OgogICAgICAgICAgICAjCiAgICAgICAgICAgIGltcG9ydCBzaHV0aWwKCiAgICAgICAgICAgIHNodXRpbC5ybXRyZWUoY28pCgogICAgICAgICAgICAjCiAgICAgICAgICAgIHByaW50KGYnUHJvamVjdCBSZW1vdmVkIHtjb30nKQogICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnRGlyUmVtb3ZhbCA9IFN1Y2Nlc3MhIHtjb30nLCBQb2w9MCkKCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBwcmludCgnUHJvamVjdCBGYWlsZWQgVG8gUmVtb3ZlZCcpCiAgICAgICAgICAgICMKICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0RpclJlbW92YWwgPSBGYWlsZWQgJywgUG9sPTApCgogICAgZWxzZToKICAgICAgICB3aXRoIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9pbnQudHh0JywgJ3InKSBhcyBmaWxlOgogICAgICAgICAgICBsaW5lczUgPSBmaWxlLnJlYWRsaW5lcygpCgogICAgICAgIHdpdGggb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL2ludC50eHQnLCAndycpIGFzIGZpbGU6CiAgICAgICAgICAgIGZvciBsaW5lZiBpbiBsaW5lczU6CiAgICAgICAgICAgICAgICAjIGZpbmQoKSByZXR1cm5zIC0xIGlmIG5vIG1hdGNoIGlzIGZvdW5kCiAgICAgICAgICAgICAgICBpZiBsaW5lZi5maW5kKHNlbGVjdGVkX2l0ZW0pICE9IC0xOgogICAgICAgICAgICAgICAgICAgIHBhc3MKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgZmlsZS53cml0ZShsaW5lZikKCiAgICAgICAgdmFsdWUgPSBsaW5lc1tpbnQodmFsdWVlKSAtIDFdCiAgICAgICAgY2MgPSB2YWx1ZQogICAgICAgIGxpc3RPZldvcmRzID0gdmFsdWUuc3BsaXQoJyYnLCAxKQogICAgICAgIGlmIGxlbihsaXN0T2ZXb3JkcykgPiAwOgogICAgICAgICAgICB2YWx1ZSA9IGxpc3RPZldvcmRzWzFdCgogICAgICAgIHZhbHVlID0gdmFsdWUuc3BsaXQoJy0nLCAxKVswXQoKICAgICAgICBjYyA9IGNjLnNwbGl0KCdAJywgMSlbMF0KCiAgICAgICAgbGlzdE9mV29yZHMgPSBjYy5zcGxpdCgnL0Rvd25sb2FkcycsIDEpCgogICAgICAgIGlmIGxlbihsaXN0T2ZXb3JkcykgPiAwOgogICAgICAgICAgICBjbyA9IGxpc3RPZldvcmRzWzFdCgogICAgICAgICMKICAgICAgICBwYXNzICAjIGV2ZW50PWYnUmVtb3ZpbmcgRGlyZWN0b3J5OiB7Y2N9JywgUG9sPTApCiAgICAgICAgdHJ5OgogICAgICAgICAgICAjCiAgICAgICAgICAgIGltcG9ydCBzaHV0aWwKCiAgICAgICAgICAgIHNodXRpbC5ybXRyZWUoZid7b3MuZ2V0Y3dkKCl9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0Rvd25sb2Fkc3tjb30nKQoKICAgICAgICAgICAgIwogICAgICAgICAgICBwcmludCgnUHJvamVjdCBSZW1vdmVkJykKICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0RpclJlbW92YWwgPSBTdWNjZXNzISAnLCBQb2w9MCkKCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICBwcmludCgnUHJvamVjdCBGYWlsZWQgVG8gUmVtb3ZlZCcpCiAgICAgICAgICAgICMKICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0RpclJlbW92YWwgPSBGYWlsZWQgJywgUG9sPTApCgogICAgdGsubWVzc2FnZWJveC5zaG93aW5mbygiU3VjY2VzcyIsIHNlbGVjdGVkX2l0ZW0gKyAiIGhhcyBiZWVuIHVuaW5zdGFsbGVkLiIpCiAgICByZXR1cm4gc2VsZWN0ZWRfaXRlbQoKZGVmIHNob3dfbGlzdF93aW5kb3coKToKICAgIGNsb3NlX3dpbmRvd3MoKQogICAgZ2xvYmFsIGxpc3Rfd2luZG93CiAgICBsaXN0X3dpbmRvdyA9IHRrLlRvcGxldmVsKCkKICAgIGxpc3Rfd2luZG93Lmdlb21ldHJ5KCIzMDB4MzAwKzIwMCsyMDAiKQogICAgbGlzdF93aW5kb3cudGl0bGUoIlVuaW5zdGFsbCBMaXN0IikKICAgIGxpc3QgPSB0ay5MaXN0Ym94KGxpc3Rfd2luZG93KQogICAgbGlzdC5wYWNrKCkKICAgIGdsb2JhbCBpdGVtcwogICAgaXRlbXMgPSBbXQoKICAgIHdpdGggb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL2ludC50eHQnLCAncicpIGFzIHIsIG9wZW4oCiAgICAgICAgICAgIGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvaW50Mi50eHQnLAogICAgICAgICAgICAndycpIGFzIG86CiAgICAgICAgZm9yIGxpbmUgaW4gcjoKICAgICAgICAgICAgaWYgbGluZS5zdHJpcCgpOgogICAgICAgICAgICAgICAgby53cml0ZShsaW5lKQoKICAgIGYgPSBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvaW50Mi50eHQnLCAiciIpCiAgICBlID0gb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0NvbXBsZXgyJywgInIiKQogICAgZ2xvYmFsIGxpbmVzCiAgICBsaW5lcyA9IGYucmVhZGxpbmVzKCkKICAgIGdsb2JhbCBjb3VudAogICAgY291bnQgPSAwCiAgICBmb3IgbGluZSBpbiBsaW5lczoKICAgICAgICBjb3VudCArPSAxCgogICAgY291bnQxID0gMAogICAgZm9yIGxpbmUgaW4gbGluZXM6CiAgICAgICAgdmFsdWU0ID0gbGluZS5zdHJpcCgpCiAgICAgICAgVmFsID0gdmFsdWU0LnNwbGl0KCcmJywgMSkKICAgICAgICBpZiBsZW4oVmFsKSA+IDA6CiAgICAgICAgICAgIHZhbHVlNCA9IFZhbFsxXQogICAgICAgIGl0ZW1zLmFwcGVuZCh2YWx1ZTQpCiAgICAgICAgY291bnQxICs9IDEKCiAgICBnbG9iYWwgbGluZXMyCiAgICBsaW5lczIgPSBlLnJlYWRsaW5lcygpCiAgICBmb3IgbGluZTIgaW4gbGluZXMyOgogICAgICAgIGNvdW50MSArPSAxCiAgICAgICAgaXRlbXMuYXBwZW5kKGxpbmUyKQoKICAgIGZvciBpdGVtIGluIGl0ZW1zOgogICAgICAgIGxpc3QuaW5zZXJ0KHRrLkVORCwgaXRlbSkKICAgIGNvbmZpcm1fYnV0dG9uID0gdGsuQnV0dG9uKGxpc3Rfd2luZG93LCB0ZXh0PSJDb25maXJtIFVuaW5zdGFsbCIsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjb21tYW5kPWxhbWJkYTogY29uZmlybV91bmluc3RhbGwobGlzdC5nZXQobGlzdC5jdXJzZWxlY3Rpb24oKSkpKQogICAgY29uZmlybV9idXR0b24ucGFjaygpCgpkZWYgZXhpdF9wcm9ncmFtKCk6CiAgICBzeXMuZXhpdCgwKQoKZGVmIGNsb3NlX3dpbmRvd3MoKToKICAgIHBhc3MKCnJvb3QgPSB0ay5UaygpCnJvb3QudGl0bGUoIkdIUE0iKQpzY3JlZW5fd2lkdGggPSByb290LndpbmZvX3NjcmVlbndpZHRoKCkKc2NyZWVuX2hlaWdodCA9IHJvb3Qud2luZm9fc2NyZWVuaGVpZ2h0KCkKd2luZG93X3dpZHRoID0gNDM3CndpbmRvd19oZWlnaHQgPSA0MDAKeF9jb29yZGluYXRlID0gKHNjcmVlbl93aWR0aCAvIDIpIC0gKHdpbmRvd193aWR0aCAvIDIpCnlfY29vcmRpbmF0ZSA9IChzY3JlZW5faGVpZ2h0IC8gMikgLSAod2luZG93X2hlaWdodCAvIDIpCnJvb3QuZ2VvbWV0cnkoIiVkeCVkKyVkKyVkIiAlICh3aW5kb3dfd2lkdGgsIHdpbmRvd19oZWlnaHQsIHhfY29vcmRpbmF0ZSwgeV9jb29yZGluYXRlKSkKcm9vdC5jb25maWcoYmc9ImJsYWNrIikKCmRlZiBBY3RpdmF0ZSgpOgogICAgY2xvc2Vfd2luZG93cygpCiAgICBpbXBvcnQgdGtpbnRlciBhcyB0awogICAgZnJvbSB0a2ludGVyIGltcG9ydCBtZXNzYWdlYm94CgogICAgcm9vdCA9IHRrLlRrKCkKICAgIHJvb3Qud2l0aGRyYXcoKQoKICAgIHJlc3VsdDEgPSBtZXNzYWdlYm94LmFza3llc25vKCJVc2VyIEdpdEh1YiBDaGVjayIsICJVc2UgR2l0SHViIGFwcGxpY2F0aW9ucz8iKQogICAgaWYgcmVzdWx0MToKICAgICAgICBHSCgpCiAgICBlbHNlOgoKICAgICAgICByZXN1bHQyID0gbWVzc2FnZWJveC5hc2t5ZXNubygiVXNlciBHaXRIdWIgQ2hlY2siLCAiVXNlIExvY2FsIGFwcGxpY2F0aW9ucz8iKQoKICAgICAgICBpZiByZXN1bHQyOgoKICAgICAgICAgICAgb3B0aW9ucyA9IFtdCgogICAgICAgICAgICAjCgogICAgICAgICAgICB3aXRoIG9wZW4oZid7Y3dkfVN5c3RlbS9DYWNoZS9TeXN0ZW0vTG9jYWwvSW50LnR4dCcsICdyJykgYXMgciwgb3BlbigKICAgICAgICAgICAgICAgICAgICBmJ3tjd2R9U3lzdGVtL0NhY2hlL1N5c3RlbS9Mb2NhbC9JbnQyLnR4dCcsCiAgICAgICAgICAgICAgICAgICAgJ3cnKSBhcyBvOgogICAgICAgICAgICAgICAgZm9yIGxpbmUgaW4gcjoKICAgICAgICAgICAgICAgICAgICBpZiBsaW5lLnN0cmlwKCk6CiAgICAgICAgICAgICAgICAgICAgICAgIG8ud3JpdGUobGluZSkKICAgICAgICAgICAgZiA9IG9wZW4oZid7Y3dkfVN5c3RlbS9DYWNoZS9TeXN0ZW0vTG9jYWwvSW50Mi50eHQnLCAiciIpCgogICAgICAgICAgICBsaW5lcyA9IGYucmVhZGxpbmVzKCkKICAgICAgICAgICAgY291bnQgPSAwCiAgICAgICAgICAgIGZvciBsaW5lIGluIGxpbmVzOgogICAgICAgICAgICAgICAgY291bnQgKz0gMQoKICAgICAgICAgICAgY291bnQxID0gMAogICAgICAgICAgICBmb3IgbGluZSBpbiBsaW5lczoKICAgICAgICAgICAgICAgIGNvdW50MSArPSAxCiAgICAgICAgICAgICAgICBvcHRpb25zLmFwcGVuZChsaW5lLnN0cmlwKCkpCgogICAgICAgICAgICBpbXBvcnQgdGtpbnRlcgogICAgICAgICAgICB3aW5kb3cgPSB0a2ludGVyLlRrKCkKICAgICAgICAgICAgd2luZG93LnRpdGxlKCJBY3RpdmF0ZSBvbmUgb2YgdGhlIGZvbGxvd2luZyIpCgogICAgICAgICAgICAjIENyZWF0ZSB0aGUgbGlzdCBvZiBvcHRpb25zCgogICAgICAgICAgICAjIENyZWF0ZSBhIGZ1bmN0aW9uIHRvIGJlIGNhbGxlZCB3aGVuIHRoZSB1c2VyIHNlbGVjdHMgYW4gb3B0aW9uCgogICAgICAgICAgICBkZWYgc2VsZWN0X29wdGlvbihzZWxlY3RlZF9vcHRpb24pOgogICAgICAgICAgICAgICAgd2luZG93LmRlc3Ryb3koKQogICAgICAgICAgICAgICAgcHJpbnQoIlNlbGVjdGVkIE9wdGlvbjoiLCBzZWxlY3RlZF9vcHRpb24pCgogICAgICAgICAgICAgICAgIwoKICAgICAgICAgICAgICAgIHBhc3MgICMgZXZlbnQ9Zid7Y291bnQxfT17Y291bnR9IC0tQ09NTUFORCBMSU5FJywgUG9sPTApCiAgICAgICAgICAgICAgICB2YWx1ZSA9IGxpbmVzW2ludChvcHRpb25zLmluZGV4KHNlbGVjdGVkX29wdGlvbikpXQogICAgICAgICAgICAgICAgbGlzdE9mV29yZHMgPSB2YWx1ZS5zcGxpdCgnLScsIDEpCiAgICAgICAgICAgICAgICBpZiBsZW4obGlzdE9mV29yZHMpID4gMDoKICAgICAgICAgICAgICAgICAgICB2YWx1ZWcgPSBsaXN0T2ZXb3Jkc1sxXQogICAgICAgICAgICAgICAgICAgIHByaW50KHZhbHVlZykKCiAgICAgICAgICAgICAgICAjCgogICAgICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0NyZWF0aW5nIHZhbHVlMSAtLUNPTU1BTkQgTElORScsIFBvbD0wKQogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIHZhbHVlMSA9IHZhbHVlLnNwbGl0KGYnQCcsIDEpWzBdCiAgICAgICAgICAgICAgICAgICAgU3RyID0gdmFsdWUxWzpsZW4odmFsdWUxKSAtIDFdCiAgICAgICAgICAgICAgICAgICAgIwoKICAgICAgICAgICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnU3VjY2Vzczoge1N0cn0gLS1DT01NQU5EIExJTkUnLCBQb2w9MCkKICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICB2YWx1ZTEgPSB2YWx1ZS5zcGxpdChmJ0AnLCAxKVswXQogICAgICAgICAgICAgICAgICAgICMKCiAgICAgICAgICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0ZhaWx1cmU6IHt2YWx1ZTF9IC0tQ09NTUFORCBMSU5FJywgUG9sPTApCgogICAgICAgICAgICAgICAgbGlzdE9mV29yZHMgPSB2YWx1ZS5zcGxpdCgnKycsIDEpCiAgICAgICAgICAgICAgICBpZiBsZW4obGlzdE9mV29yZHMpID4gMDoKICAgICAgICAgICAgICAgICAgICB2YWx1ZSA9IGxpc3RPZldvcmRzWzFdCgogICAgICAgICAgICAgICAgdmFsdWUgPSB2YWx1ZS5zcGxpdCgnLScsIDEpWzBdCgogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIHByaW50KHZhbHVlZ1s6LTJdKQogICAgICAgICAgICAgICAgICAgIHByaW50KHZhbHVlKQogICAgICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgKICAgICAgICAgICAgICAgICAgICAgICAgZiJvc2FzY3JpcHQgLWUgJ3RlbGwgYXBwbGljYXRpb24gXCJUZXJtaW5hbFwiIHRvIGRvIHNjcmlwdCBcImNkIHt2YWx1ZX0gJiYge3ZhbHVlZ1s6LTJdfVwiJyIpCiAgICAgICAgICAgICAgICAgICAgIwoKICAgICAgICAgICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnQ29tbWFuZCBFeGVjdXRlZCBbIV17dmFsdWV9WyFdIC0tQ09NTUFORCBMSU5FJywgUG9sPTApCiAgICAgICAgICAgICAgICBleGNlcHQ6CgogICAgICAgICAgICAgICAgICAgIHBhc3MKCiAgICAgICAgICAgIGZvciBvcHRpb24gaW4gb3B0aW9uczoKICAgICAgICAgICAgICAgIGIgPSB0a2ludGVyLkJ1dHRvbih3aW5kb3csIHRleHQ9b3B0aW9uLCBjb21tYW5kPWxhbWJkYSBvcHQ9b3B0aW9uOiBzZWxlY3Rfb3B0aW9uKG9wdCkpCiAgICAgICAgICAgICAgICBiLnBhY2soKQoKICAgICAgICAgICAgIyBTdGFydCB0aGUgd2luZG93IGV2ZW50IGxvb3AKICAgICAgICAgICAgd2luZG93Lm1haW5sb29wKCkKCiAgICAgICAgZWxzZToKICAgICAgICAgICAgcmVzdWx0MyA9IG1lc3NhZ2Vib3guYXNreWVzbm8oIlVzZXIgQWR2YW5jZWQgQ2hlY2siLCAiVXNlIEFkdmFuY2VkIEdpdEh1YiBhcHBsaWNhdGlvbnM/IikKICAgICAgICAgICAgaWYgcmVzdWx0MzoKICAgICAgICAgICAgICAgIG9wdGlvbnMgPSBbXQogICAgICAgICAgICAgICAgd2l0aCBvcGVuKGYne2N3ZH0vU3lzdGVtL0NhY2hlL1N5c3RlbS9HaXRIdWIvQ29tcGxleCcsICdyJykgYXMgciwgb3BlbigKICAgICAgICAgICAgICAgICAgICAgICAgZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9Db21wbGV4MicsICd3JykgYXMgbzoKICAgICAgICAgICAgICAgICAgICBmb3IgbGluZSBpbiByOgogICAgICAgICAgICAgICAgICAgICAgICBpZiBsaW5lLnN0cmlwKCk6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBvLndyaXRlKGxpbmUpCgogICAgICAgICAgICAgICAgZiA9IG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9Db21wbGV4MicsICJyIikKCiAgICAgICAgICAgICAgICBsaW5lc2QgPSBmLnJlYWRsaW5lcygpCiAgICAgICAgICAgICAgICBjb3VudCA9IDAKICAgICAgICAgICAgICAgIGZvciBsaW5lIGluIGxpbmVzZDoKICAgICAgICAgICAgICAgICAgICBjb3VudCArPSAxCgogICAgICAgICAgICAgICAgY291bnQxID0gMAogICAgICAgICAgICAgICAgZm9yIGxpbmUgaW4gbGluZXNkOgogICAgICAgICAgICAgICAgICAgIHZhbHVlNCA9IGxpbmUuc3RyaXAoKQogICAgICAgICAgICAgICAgICAgIGNvdW50MSArPSAxCiAgICAgICAgICAgICAgICAgICAgb3B0aW9ucy5hcHBlbmQodmFsdWU0KQoKICAgICAgICAgICAgICAgIGltcG9ydCB0a2ludGVyCiAgICAgICAgICAgICAgICB3aW5kb3cgPSB0a2ludGVyLlRrKCkKICAgICAgICAgICAgICAgIHdpbmRvdy50aXRsZSgiQWN0aXZhdGUgb25lIG9mIHRoZSBmb2xsb3dpbmciKQoKICAgICAgICAgICAgICAgIGRlZiBzZWxlY3Rfb3B0aW9uKHNlbGVjdGVkX29wdGlvbik6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoIlNlbGVjdGVkIE9wdGlvbjoiLCBzZWxlY3RlZF9vcHRpb24pCgogICAgICAgICAgICAgICAgICAgIGRlZiBzdWJtaXQoKToKICAgICAgICAgICAgICAgICAgICAgICAgbmFtZSA9IGVudHJ5X25hbWUuZ2V0KCkKICAgICAgICAgICAgICAgICAgICAgICAgd2luZG93Mi5kZXN0cm95KCkKICAgICAgICAgICAgICAgICAgICAgICAgd2luZG93LmRlc3Ryb3koKQogICAgICAgICAgICAgICAgICAgICAgICBBcmdlcyA9IG5hbWUKCiAgICAgICAgICAgICAgICAgICAgICAgIEIgPSB2YWx1ZS5zcGxpdCgnJCcsIDEpWzBdCgogICAgICAgICAgICAgICAgICAgICAgICAjIFJlbW92ZSBhbGwgY2hhcmFjdGVycyBiZWZvcmUgdGhlIGNoYXJhY3RlciAnLScgZnJvbSBzdHJpbmcKICAgICAgICAgICAgICAgICAgICAgICAgbGlzID0gdmFsdWUuc3BsaXQoJyQnLCAxKQogICAgICAgICAgICAgICAgICAgICAgICBpZiBsZW4obGlzKSA+IDA6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBsaXMgPSBsaXNbMV0KCiAgICAgICAgICAgICAgICAgICAgICAgIEEgPSBmJ3tsaXN9IHtBcmdlc30nCgogICAgICAgICAgICAgICAgICAgICAgICByID0gb3BlbihmJ3tjd2R9L1N5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL0NvbXBsZXhfaW5zdGFsbCcsICdyJykKICAgICAgICAgICAgICAgICAgICAgICAgbGluZXMgPSByLnJlYWRsaW5lcygpCiAgICAgICAgICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZvciBsaW5lIGluIGxpbmVzOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIwogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnQ29tbWFuZCB7bGluZX0nLCBQb2w9MCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb3Muc3lzdGVtKGxpbmUpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBhc3MgICMgZXZlbnQ9ZidDb21tYW5kIGZhaWxlZCAnLCBQb2w9MCkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZXhpdCgwKQoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9wZW4oZid7Y3dkfS9TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9Db21wbGV4X2luc3RhbGwnLCAndycpCgogICAgICAgICAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwYXNzCgogICAgICAgICAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oZiJvc2FzY3JpcHQgLWUgJ3RlbGwgYXBwbGljYXRpb24gXCJUZXJtaW5hbFwiIHRvIGRvIHNjcmlwdCBcImNkIHtCfSYme0F9XCInIikKICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBhc3MgICMgZXZlbnQ9ZidMYXVuY2ggU3VjY2VzcyEgJywgUG9sPTApCiAgICAgICAgICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBhc3MKCiAgICAgICAgICAgICAgICAgICAgdmFsdWUgPSBzZWxlY3RlZF9vcHRpb24KICAgICAgICAgICAgICAgICAgICB3aW5kb3cyID0gdGsuVGsoKQogICAgICAgICAgICAgICAgICAgIHdpbmRvdzIudGl0bGUoIlBhY2thZ2UgSW5mb3JtIikKCiAgICAgICAgICAgICAgICAgICAgbGFiZWxfbmFtZSA9IHRrLkxhYmVsKHdpbmRvdzIsIHRleHQ9IkFueSBMYXVuY2ggQXJndW1lbnRzOiAiKQogICAgICAgICAgICAgICAgICAgIGVudHJ5X25hbWUgPSB0ay5FbnRyeSh3aW5kb3cyKQoKICAgICAgICAgICAgICAgICAgICBsYWJlbF9uYW1lLnBhY2soKQogICAgICAgICAgICAgICAgICAgIGVudHJ5X25hbWUucGFjaygpCgogICAgICAgICAgICAgICAgICAgIGJ1dHRvbiA9IHRrLkJ1dHRvbih3aW5kb3cyLCB0ZXh0PSJTdWJtaXQiLCBjb21tYW5kPXN1Ym1pdCkKICAgICAgICAgICAgICAgICAgICBidXR0b24ucGFjaygpCgogICAgICAgICAgICAgICAgICAgIHdpbmRvdzIubWFpbmxvb3AoKQoKICAgICAgICAgICAgICAgIGZvciBvcHRpb24gaW4gb3B0aW9uczoKICAgICAgICAgICAgICAgICAgICBiID0gdGtpbnRlci5CdXR0b24od2luZG93LCB0ZXh0PW9wdGlvbiwgY29tbWFuZD1sYW1iZGEgb3B0PW9wdGlvbjogc2VsZWN0X29wdGlvbihvcHQpKQogICAgICAgICAgICAgICAgICAgIGIucGFjaygpCgogICAgICAgICAgICAgICAgIyBDcmVhdGUgdGhlIGxpc3Qgb2Ygb3B0aW9ucwoKICAgICAgICAgICAgICAgICMgQ3JlYXRlIGEgZnVuY3Rpb24gdG8gYmUgY2FsbGVkIHdoZW4gdGhlIHVzZXIgc2VsZWN0cyBhbiBvcHRpb24KCiAgICAgICAgICAgICAgICAjIFN0YXJ0IHRoZSB3aW5kb3cgZXZlbnQgbG9vcAoKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHBhc3MKCmRlZiBHSCgpOgogICAgaW1wb3J0IFVzZXIKICAgIGN3ZCA9IFVzZXIuVXNlclByb2ZpbGUuU291cmNlRGlyZWN0b3J5CiAgICBzcGFjZXIgPSAnPT09PT09PT09PT09PT09JwogICAgIwoKICAgIGltcG9ydCBvcwogICAgaW1wb3J0IHN5cwoKICAgIHBhc3MgICMgZXZlbnQ9ZidJbnAgPSBHaXRIdWInLCBQb2w9MSkKCiAgICB3aXRoIG9wZW4oZid7Y3dkfVN5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL2ludC50eHQnLCAncicpIGFzIHIsIG9wZW4oCiAgICAgICAgICAgIGYne2N3ZH1TeXN0ZW0vQ2FjaGUvU3lzdGVtL0dpdEh1Yi9pbnQyLnR4dCcsICd3JykgYXMgbzoKICAgICAgICBmb3IgbGluZSBpbiByOgogICAgICAgICAgICBpZiBsaW5lLnN0cmlwKCk6CiAgICAgICAgICAgICAgICBvLndyaXRlKGxpbmUpCgogICAgZiA9IG9wZW4oZid7Y3dkfVN5c3RlbS9DYWNoZS9TeXN0ZW0vR2l0SHViL2ludDIudHh0JywgInIiKQoKICAgIGxpbmVzID0gZi5yZWFkbGluZXMoKQogICAgY291bnQgPSAwCiAgICBmb3IgbGluZSBpbiBsaW5lczoKICAgICAgICBjb3VudCArPSAxCgogICAgb3B0aW9ucyA9IFtdCiAgICBjb3VudDEgPSAwCiAgICBmb3IgbGluZSBpbiBsaW5lczoKICAgICAgICB2YWx1ZTQgPSBsaW5lLnN0cmlwKCkKICAgICAgICBWYWwgPSB2YWx1ZTQuc3BsaXQoJyYnLCAxKQogICAgICAgIGlmIGxlbihWYWwpID4gMDoKICAgICAgICAgICAgdmFsdWU0ID0gVmFsWzFdCiAgICAgICAgY291bnQxICs9IDEKCiAgICAgICAgb3B0aW9ucy5hcHBlbmQodmFsdWU0KQoKICAgIGltcG9ydCB0a2ludGVyCiAgICB3aW5kb3cgPSB0a2ludGVyLlRrKCkKICAgIHdpbmRvdy50aXRsZSgiQWN0aXZhdGUgb25lIG9mIHRoZSBmb2xsb3dpbmciKQoKICAgICMgQ3JlYXRlIHRoZSBsaXN0IG9mIG9wdGlvbnMKCiAgICAjIENyZWF0ZSBhIGZ1bmN0aW9uIHRvIGJlIGNhbGxlZCB3aGVuIHRoZSB1c2VyIHNlbGVjdHMgYW4gb3B0aW9uCiAgICBkZWYgc2VsZWN0X29wdGlvbihzZWxlY3RlZF9vcHRpb24pOgogICAgICAgIHdpbmRvdy5kZXN0cm95KCkKICAgICAgICBwcmludCgiU2VsZWN0ZWQgT3B0aW9uOiIsIHNlbGVjdGVkX29wdGlvbikKCiAgICAgICAgdmFsdWUgPSBsaW5lc1tpbnQob3B0aW9ucy5pbmRleChzZWxlY3RlZF9vcHRpb24pKV0KICAgICAgICBwcmludCh2YWx1ZSkKICAgICAgICBjYyA9IHZhbHVlCiAgICAgICAgbGlzdE9mV29yZHMgPSB2YWx1ZS5zcGxpdCgnJicsIDEpCiAgICAgICAgaWYgbGVuKGxpc3RPZldvcmRzKSA+IDA6CiAgICAgICAgICAgIHZhbHVlID0gbGlzdE9mV29yZHNbMV0KCiAgICAgICAgdmFsdWUgPSB2YWx1ZS5zcGxpdCgnLScsIDEpWzBdCgogICAgICAgIGNjID0gY2Muc3BsaXQoJ0AnLCAxKVswXQogICAgICAgICMKCiAgICAgICAgcGFzcyAgIyBldmVudD1mJ0NoYW5nZSBEaXJlY3Rvcnk6IHtjY30gJywgUG9sPTApCiAgICAgICAgdHJ5OgoKICAgICAgICAgICAgIwoKICAgICAgICAgICAgcGFzcyAgIyBldmVudD1mJ0RpckNoYW5nZSA9IFN1Y2Nlc3MhICcsIFBvbD0wKQogICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnb3MgZXhlY3V0ZWQgY29tbWFuZCBbIV17dmFsdWV9WyFdICcsIFBvbD0wKQogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oZiJvc2FzY3JpcHQgLWUgJ3RlbGwgYXBwbGljYXRpb24gXCJUZXJtaW5hbFwiIHRvIGRvIHNjcmlwdCBcImNkIHtjY30mJnt2YWx1ZTR9XCInIikKICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgcGFzcwoKCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAjCgogICAgICAgICAgICBwYXNzICAjIGV2ZW50PWYnRGlyQ2hhbmdlID0gRmFpbGVkICcsIFBvbD0wKQoKICAgICMgRGlzcGxheSB0aGUgbGlzdCBvZiBvcHRpb25zIGluIHRoZSB3aW5kb3cKCiAgICBmb3Igb3B0aW9uIGluIG9wdGlvbnM6CiAgICAgICAgYiA9IHRraW50ZXIuQnV0dG9uKHdpbmRvdywgdGV4dD1vcHRpb24sIGNvbW1hbmQ9bGFtYmRhIG9wdD1vcHRpb246IHNlbGVjdF9vcHRpb24ob3B0KSkKICAgICAgICBiLnBhY2soKQoKICAgICMgU3RhcnQgdGhlIHdpbmRvdyBldmVudCBsb29wCiAgICB3aW5kb3cubWFpbmxvb3AoKQoKYnV0dG9ucyA9IFtdCgpidXR0b24gPSB0ay5CdXR0b24ocm9vdCwgdGV4dD0iSW5mb3JtYXRpb24iLCBiZz0iZ3JheSIsIGhlaWdodD0yLCB3aWR0aD0xMCwgY29tbWFuZD1zaG93X2luZm9ybWF0aW9uKQpidXR0b24uZ3JpZChyb3c9MSwgY29sdW1uPTAsIHBhZHg9MTAsIHBhZHk9MTApCmJ1dHRvbnMuYXBwZW5kKGJ1dHRvbikKCnNldHRpbmdzX2J1dHRvbiA9IHRrLkJ1dHRvbihyb290LCB0ZXh0PSJTZXR0aW5ncyIsIGJnPSJncmF5IiwgaGVpZ2h0PTIsIHdpZHRoPTEwLCBjb21tYW5kPXNldHRpbmdzX3dpbmRvdykKc2V0dGluZ3NfYnV0dG9uLmdyaWQocm93PTEsIGNvbHVtbj0xLCBwYWR4PTEwLCBwYWR5PTEwKQpidXR0b25zLmFwcGVuZChidXR0b24pCgpidXR0b24gPSB0ay5CdXR0b24ocm9vdCwgdGV4dD0iSW5zdGFsbCIsIGJnPSJncmF5IiwgaGVpZ2h0PTIsIHdpZHRoPTEwLCBjb21tYW5kPXNob3dfaW5zdGFsbCkKYnV0dG9uLmdyaWQocm93PTEsIGNvbHVtbj0yLCBwYWR4PTEwLCBwYWR5PTEwKQpidXR0b25zLmFwcGVuZChidXR0b24pCgpidXR0b24gPSB0ay5CdXR0b24ocm9vdCwgdGV4dD0iQWN0aXZhdGUiLCBiZz0iZ3JheSIsIGhlaWdodD0yLCB3aWR0aD0xMCwgY29tbWFuZD1BY3RpdmF0ZSkKYnV0dG9uLmdyaWQocm93PTIsIGNvbHVtbj0wLCBwYWR4PTEwLCBwYWR5PTEwKQpidXR0b25zLmFwcGVuZChidXR0b24pCgpidXR0b24gPSB0ay5CdXR0b24ocm9vdCwgdGV4dD0iVW5pbnN0YWxsIiwgYmc9ImdyYXkiLCBoZWlnaHQ9Miwgd2lkdGg9MTAsIGNvbW1hbmQ9c2hvd19saXN0X3dpbmRvdykKYnV0dG9uLmdyaWQocm93PTIsIGNvbHVtbj0xLCBwYWR4PTEwLCBwYWR5PTEwKQpidXR0b25zLmFwcGVuZChidXR0b24pCgpidXR0b24gPSB0ay5CdXR0b24ocm9vdCwgdGV4dD0iVGhlIENyeXB0IiwgYmc9ImdyYXkiLCBoZWlnaHQ9Miwgd2lkdGg9MTAsIGNvbW1hbmQ9Y3J5cHQpCmJ1dHRvbi5ncmlkKHJvdz0yLCBjb2x1bW49MiwgcGFkeD0xMCwgcGFkeT0xMCkKYnV0dG9ucy5hcHBlbmQoYnV0dG9uKQoKYnV0dG9uID0gdGsuQnV0dG9uKHJvb3QsIHRleHQ9IkVYSVQiLCBiZz0icmVkIiwgaGVpZ2h0PTIsIHdpZHRoPTEwLCBjb21tYW5kPWV4aXRfcHJvZ3JhbSkKYnV0dG9uLmdyaWQocm93PTQsIGNvbHVtbj0xLCBwYWR4PTEwLCBwYWR5PTEwKQpyb290Lm1haW5sb29wKCkK"; // base64-encoded Python script
    int inlen = strlen(in);

    unsigned char out[inlen];
    int outlen = base64_decode(in, inlen, out);
    out[outlen] = '\0';

    int fd[2];
    pipe(fd);

    if (!fork()) {
        close(fd[0]);
        dup2(fd[1], STDOUT_FILENO);
        dup2(fd[1], STDERR_FILENO);
        char *args[] = {"python3", "-c", out, NULL};
        execvp("python3", args);
    } else {
        close(fd[1]);
        wait(NULL);
    }

    return 0;
}


                """

                # Write the C source code to a temporary file
                with tempfile.NamedTemporaryFile(
                    delete=False, suffix='.c'
                ) as temp_c_file:
                    temp_c_file.write(c_source_code)
                    temp_c_file.flush()
                    c_file_name = temp_c_file.name

                # Compile the C source code into an executable
                os.system(f'gcc -o ghpm {c_file_name}')

                # Remove the temporary C source code file
                os.remove(c_file_name)

                # Run the compiled executable

                if os.path.exists(filename):
                    os.system(f'ghpm')
                else:
                    GUI()
            except:
                sys.exit(0)

    elif Value == 0:
        import System.Drive.VersionUpdate

        exec('System.Drive.VersionUpdate')
    else:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'FunctionRequest = InvalidEntry', Pol=1)

        import System.Drive.Errors_Events.ErrorMan as ER

        ER.NewIssue(
            Line=69,
            ErNo=1,
            SCR='System.Drive.FunctionRequest',
            KeFu=['IncorrectInputValue'],
            UserInp=None,
        )
