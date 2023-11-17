'''
 is script creates a graphical user interface for an application
 with buttons for various functionalities and repositories. It
 also handles analytics and checks for updates or forced login
 based on user preferences.
 '''



import inspect
import uuid

import User.UserProfile
import System.Drive.Errors_Events.EventMan as AR
import System.Drive.Errors_Events.EventMan as EV
import System.Drive.UI_Functions.Install

cwd = User.UserProfile.SourceDirectory


def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name


def Activate():
    import System.Drive.UI_Functions.Activate as AC
    AC.Activate()


def GUI():
    import User.UserProfile as UP
    if UP.Forced_Login:
        import System.Drive.Login
    else:
        pass

    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)


    global directories
    directories = []
    import os

    import User.UserProfile

    cwd = User.UserProfile.SourceDirectory

    os.system("""osascript -e 'tell application "Terminal" to set visible of window 1 to false' """)

    import tkinter as tk

    def show_information():
        import System.Drive.UI_Functions.Information as IF
        IF.show_information()

    def settings_window():
        import System.Drive.UI_Functions.Settings as SW
        SW.settings_window()

    def crypt():
        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        try:
            os.system(
                f'''osascript -e 'tell application "Terminal" to do script "cd {User.UserProfile.SourceDirectory[:-1]}&&python3 CLI.py"'
''')
        except:
            EV.guiEvent(0, f'{get_current_function()} Error: CLI.py may not exist',
                        inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)

    def kill_server():
        import System.Drive.UI_Functions.KillServer as KS
        KS.kill_server()

    def update_server():
        import System.Drive.VersionUpdate
        try:
            exec('System.Drive.VersionUpdate')
        except:
            pass

    def show_install():
        import System.Drive.UI_Functions.Install as IN
        IN.show_install()

    def show_list_window():
        import System.Drive.UI_Functions.Uninstall as UN
        UN.show_list_window()

    def open_update_local():
        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        os.system(f'python3 {User.UserProfile.SourceDirectory}serv.py')

    def start_server():
        import System.Drive.UI_Functions.ConnectServer as CS
        CS.start_server()

    global root

    import tkinter as tk
    import ttkbootstrap as ttk

    import UI_Functions.UI_Builder.widgetfactory as wf
    import UI_Functions.UI_Builder.utilities as ut
    import UI_Functions.UI_Builder.customnotebook as cnb

    import UI_Functions.information as inf


    fileHandler = ut.FileHandler()
    log = fileHandler.readTextFile("LOG.txt")

    theme = 'darkly'
    root = ttk.Window(
        title='GHPM',
        themename=theme,
        size=(1000, 650),
        resizable=(False, False),
    )

    GhPM = cnb.Root(root, theme)

    main = wf.CustomFrame("Main")
    main.addButton(name='Local Update', x=30, y=30, buttonBootstyle='warning', width=12, command=open_update_local)
    import System.Drive.templates.main as tmain

    main.addButton(name='Settings', x=30, y=155, buttonBootstyle='Outline', width=12, command=settings_window)
    main.addButton(name='Install', x=30, y=275, buttonBootstyle='success.Outline', width=12, command=show_install)
    main.addButton(name='Activate', x=30, y=345, buttonBootstyle='warning.Outline', width=12, command=Activate)
    main.addButton(name='Uninstall', x=30, y=415, buttonBootstyle='danger.Outline', width=12, command=show_list_window)

    main.addButton(name='Recommended Packages', x=30, y=545, command=tmain.main)
    main.addButton(name='Command Line Interface', x=412, y=545, buttonBootstyle='light.Outline', command=crypt)
    main.addButton(name='Information', x=780, y=545, width=12,
                command=lambda: GhPM.addCustomFrame(inf.InfoFrame().getFrame()))

    main.addButton(name='Start Server', x=340, y=30, buttonBootstyle='success', width=12, command=start_server)
    main.addButton(name='Update Server', x=560, y=30, buttonBootstyle='warning', width=12, command=update_server)
    main.addButton(name='Kill Server', x=780, y=30, buttonBootstyle='danger', width=12, command=kill_server)

    main.addScrollText(log=log, x=240, y=120, width=65, height=16)

    main.constructFrame()

    GhPM.addCustomFrame(main)

    import User.UserProfile
    try:
        with open(f'{User.UserProfile.SourceDirectory}System/.Cache/User/analytics', 'r') as file:
            data = file.read()
            import requests
            url = f'''https://gpm-web.vercel.app/analytics={data}'''
            requests.get(url)
    except:
        pass
    EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Login', a3='None')
    if User.UserProfile.AutoUpdate:
        try:
            import System.Drive.VersionUpdate
            System.Drive.VersionUpdate()

        except:

            root.mainloop()
    else:
        root.mainloop()



