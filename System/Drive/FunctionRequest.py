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
    from UI_Functions.UI_Builder import ghpmmaingui as gmg
    from UI_Functions.UI_Builder import iconfilepaths as ifp
    from UI_Functions.UI_Builder import formbuilder as fb

    iconDict = ifp.generateFilePathDict("Assets")

    root = gmg.GHPMMainGui(1000, 650)

    main = fb.CustomFrame(bgImage=iconDict["logo"])

    main.setupIconButton(20, 20, iconDict["misc"]["local_update_button"], iconScale=0.30, command=open_update_local)

    main.setupIconButton(20, 160, iconDict["side_panel"]["settings_button"], iconScale=0.25, command=settings_window)
    main.setupIconButton(20, 230, iconDict["side_panel"]["install_button"], iconScale=0.25, command=show_install)
    main.setupIconButton(20, 300, iconDict["side_panel"]["activate_button"], iconScale=0.25, command=Activate)
    main.setupIconButton(20, 370, iconDict["side_panel"]["uninstall_button"], iconScale=0.25, command=show_list_window)
    main.setupIconButton(20, 484, iconDict["misc"]["recommended_button"], iconScale=0.40, command=System.Drive.templates.main.main)

    main.setupIconButton(550, 540, iconDict["misc"]["command_line_button"], iconScale=0.25, command=crypt)
    main.setupIconButton(772, 540, iconDict["misc"]["information_button"], iconScale=0.25, command=show_information)

    main.setupIconButton(822, 10, iconDict["server_icons"]["start_server"], iconScale=0.10, command=start_server)
    main.setupIconButton(878, 10, iconDict["server_icons"]["update_server"], iconScale=0.10, command=update_server)
    main.setupIconButton(934, 10, iconDict["server_icons"]["kill_server"], iconScale=0.10, command=kill_server)

    main.constructFrame()

    root.addTab(main, "Main")

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

            root.run()
    else:
        root.run()



