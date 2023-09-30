'''
 is script creates a graphical user interface for an application
 with buttons for various functionalities and repositories. It
 also handles analytics and checks for updates or forced login
 based on user preferences.
 '''



import inspect
import uuid
from tkinter import ttk

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

    def kill_r():
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

    root = tk.Tk()
    root.title('GHpm')
    root.config(bg='#403736')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.resizable(False, False)
    window_width = 526
    window_height = 505
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    bg_color = '#403736'
    button_color = '#301c1b'
    button_hover_color = '#D8D8D8'
    text_color = '#732c03'
    text_color_other = '#81BDA4'

    button_font = ('Helvetica', 14)

    toolbar = tk.Frame(root, bg=bg_color, width=120, height=window_height)
    toolbar.pack(side='left', fill='y')

    update_button = tk.Button(
        root,
        text='Update Local',
        bg=button_color,
        fg=text_color,
        height=3,
        width=12,
        font=button_font,
        command=open_update_local
    )
    update_button.pack(side='top', anchor='ne', fill='x', expand=True, padx=10, pady=10)

    server_buttons_frame = tk.Frame(root, bg=bg_color)
    server_buttons_frame.pack(side='top', anchor='nw', padx=10, pady=10)

    start_server_button = tk.Button(
        server_buttons_frame,
        text='Start Server',
        bg=button_color,
        fg='#006b73',
        height=3,
        width=7,
        font=button_font,
        command=start_server
    )
    start_server_button.pack(side='left', padx=10)

    kill_server_button = tk.Button(
        server_buttons_frame,
        text='Kill Server',
        bg=button_color,
        fg='#006b73',
        height=3,
        width=7,
        font=button_font,
        command=kill_server
    )
    kill_server_button.pack(side='left', padx=10)

    kill_server_butto3n = tk.Button(
        server_buttons_frame,
        text='Update',
        bg=button_color,
        fg='#006b73',
        height=3,
        width=7,
        font=button_font,
        command=kill_r
    )
    kill_server_butto3n.pack(side='left', padx=10)

    buttons = []

    button_texts = ['Information', 'Settings', 'Install', 'Activate', 'Uninstall','CommandL']
    button_commands = [show_information, settings_window, show_install, Activate, show_list_window,crypt]

    for text, command in zip(button_texts, button_commands):
        button = tk.Button(
            toolbar,
            text=text,
            bg=button_color,
            fg=text_color,
            height=3,
            width=12,
            font=button_font,
            command=command,
        )
        button.pack(side='top', padx=15, pady=15)
        buttons.append(button)
    import System.Drive.templates.main
    bottom_button = tk.Button(
        root,
        text='GhPm Recommended',
        bg='#C54034',
        fg='white',
        height=3,
        width=15,
        font=button_font,
        command=System.Drive.templates.main.main,
    )
    bottom_button.pack(side='bottom', padx=10, pady=15)

    # Peppermint theme colors
    bg_color = "#C5E0DC"  # Light blue
    text_color = "#732c03"  # Dark gray
    button_color = "#391e6b"  # Light teal

    # Border color for the frame
    border_color = "#391e6b"  # A light gold color

    # Apply Peppermint theme to canvas and scrollbar
    style = ttk.Style()
    style.theme_use("clam")  # Using the "clam" theme for a modern look
    style.configure("Vertical.TScrollbar", gripcount=0, background=bg_color, troughcolor=bg_color, bordercolor=bg_color, borderwidth=1)
    style.map("Vertical.TScrollbar", background=[("active", button_color), ("disabled", bg_color)])

    # Create a canvas and add a scrollbar
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview, style="Vertical.TScrollbar")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Create a frame inside the canvas to hold the content with a colored border
    content_frame = ttk.Frame(canvas, borderwidth=4, relief="solid")
    content_frame["style"] = "My.TFrame"  # Define a custom style for the frame
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Configure canvas scrolling
    def configure_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    content_frame.bind("<Configure>", configure_scroll_region)

    # Generate git rows function
    def generate_git_row(repo_name, repo_url, description):

        git_row_frame = ttk.Frame(content_frame)

        repo_name_label = tk.Label(
            git_row_frame,
            text=repo_name,
            bg=bg_color,
            fg=text_color,
            font="Helvetica 12 bold",
            padx=10,
            pady=5,
        )
        repo_name_label.pack(side="left")
        import System.Drive.UI_Functions
        download_button = tk.Button(
            git_row_frame,
            text="Download",
            bg=button_color,
            fg=text_color,
            padx=10,
            pady=5,
            command=lambda: (System.Drive.UI_Functions.Install.Installer(value=repo_url)),
        )
        download_button.pack(side="right")

        git_row_frame.pack(fill="x", padx=10, pady=10)

        description_label = tk.Label(
            content_frame,
            text=description,
            bg=bg_color,
            fg=text_color,
            padx=10,
            pady=5,
            wraplength=300,  # Adjust the value as needed
        )
        description_label.pack(anchor="w", padx=10)

        spacer_frame = tk.Frame(content_frame, bg=bg_color, height=10)
        spacer_frame.pack()

    git_rows = [
        {
            "repo_name": "Thank You For Downloading!",
            "repo_url": "",
            "description": "Hope you enjoy using GHPM",
        },
        {
            "repo_name": "GHPM Powered Custom Shell",
            "repo_url": "https://github.com/smoke-wolf/GHPM-CUSTOM-SHELL",
            "description": '''GHPM-CUSTOM-SHELL add-on for easy implementation
            of shortcuts and user preference modifications within 
            the terminal interface''',
        },
        {
            "repo_name": "Requirement-Scanner",
            "repo_url": "https://github.com/smoke-wolf/ReqScanner",
            "description": "Compile a list of all pip packages used in a python application",
        },
        {
            "repo_name": "Local Weather",
            "repo_url": "https://github.com/smoke-wolf/weather",
            "description": "Get a Local Weather Report",
        },
        {
            "repo_name": "Touch Script",
            "repo_url": "https://github.com/smoke-wolf/TouchScript",
            "description": '''.touch is a lightweight and user-friendly scripting language
        designed to automate common tasks
        on your computer.''',
        },
        {
            "repo_name": "GPlock",
            "repo_url": "https://github.com/smoke-wolf/GpLock",
            "description": "Compile a list of all pip packages used in a python application",
        },
    ]

    for git_row in git_rows:
        generate_git_row(
            git_row["repo_name"], git_row["repo_url"], git_row["description"]
        )

    # Define the custom style for the frame border
    style.configure("My.TFrame", bordercolor=border_color)

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



