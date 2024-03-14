'''
March 14th 2024
                           +-----------------+
                           | Start Execution |
                           +--------+--------+
                                    |
                           +--------v--------+
                           | Check First Use |
                           +--------+--------+
                                    |
                   +----------------+----------------+
                   |                                 |
           First Use Exists?                   First Use
                   |                                 |
      +------------+------------+       +------------+------------+
      |                         |       |                         |
  Already Used                |       |  Initialize Configuration |
      |                         |       |          Interface        |
      |                         |       +------------+------------+
+-----v-----+                   |                    |
|           |           Collect User Data       User Interface
|  Process  |                   |                    |
| Existing  |                   |                    |
|   Data    |                   |                    |
|           |                   |                    |
+-----+-----+                   |                    |
      |                         |                    |
      |    +--------------------+--------------------+--------+
      |    |                                                 |
      |    |                Create User Profile               |
      |    |                                                 |
      |    +--------------------+--------------------+--------+
      |                         |                    |
      |                         |                    |
+-----v-----+                   |                    |
|           |           Generate Hashed Password    Remove Token File
|  Hashing  |                   |                    |
|   Data    |                   |                    |
|           |                   |                    |
+-----+-----+                   |                    |
      |                         |                    |
      |                         |                    |
+-----v-----+                   |                    |
|           |            Write GHPM System       System Commands
|  Write    |                   |                    |
|   Data    |                   |                    |
|           |                   |                    |
+-----+-----+                   |                    |
      |                         |                    |
      |                         |                    |
      +-------------------------+--------------------+
                                    |
                           +--------v--------+
                           |  Terminate      |
                           |  Execution      |
                           +-----------------+

'''

import os
import sys
import time
import platform
import hashlib
import uuid
import tkinter as tk
from tkinter import ttk


# Function to check if the OS is macOS
def is_mac_os():
    return platform.system() == "Darwin"


# Function to create a user profile
def create_user_profile():
    cwd = os.getcwd()
    username = username_entry.get()
    password = password_entry.get()
    import requests

    def create_account(username, password, email):
        url = "https://hello2022isthe3nd.000webhostapp.com/createGHPMaccount.php"
        params = {
            'username': username,
            'password': password,
            'email': email,
            'country': "NOT_SET"
        }

        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                print("Account creation successful")
            elif response.status_code == 401:
                print("Account creation failed. Unauthorized.")
            elif response.status_code == 404:
                print("Account creation failed. Not found.")
            elif response.status_code == 400:
                print("Account creation failed. Bad request.")
            else:
                print("Account creation failed with status code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Request failed:", str(e))

    # Usage example
    create_account(username, password, email_entry.get())  # Replace with actual credentials

    user_profile_path = f"{cwd}/User/UserProfile.py"
    with open(user_profile_path, "w") as user_profile:

        hashed_password = generate_hashed_password(password)
        user_privileges = "root" if not is_mac_os() else os.getlogin()
        source_directory = os.getcwd()
        # Get the operating system name
        current_os = platform.system()

        # Assuming source_directory is defined
        if current_os == 'Windows':
            source_directory = r'' + source_directory
            source_directory = source_directory.replace('\\', '\\\\') + '\\\\'
            source_directory = source_directory[2:]
        else:
            source_directory = f'{source_directory}/'

        uuid1 = uuid.uuid1().hex
        uuid4 = uuid.uuid4().hex
        email = email_entry.get()
        user_profile_content = (
            f"Username = '{username}'\n"
            f"Password = '{hashed_password}'\n"
            f"UserPrivileges = '{user_privileges}'\n"
            f"SourceDirectory = '{(source_directory)}'\n"
            f"Force_Import_Request = {force_import.get()}\n"
            f"Forced_Login = {forced_login.get()}\n"
            f"uuid1 = '{uuid1}'\n"
            f"uuid4 = '{uuid4}'\n"
            f"DisplayEvents = {display_events.get()}\n"
            f"PushLogs = {push_logs.get()}\n"
            f"AdvancedL = {advanced_l.get()}\n"
            f"AutoUpdate = {auto_update.get()}\n"
            f"Email = '{email}'\n"
            f"safeInstall = True\n"
            "ConsoleVisability = False\n"
            f"HasGitDownloaded = False\n"
            f"Token = '000instantaneous'\n"

        )

        user_profile.write(user_profile_content)


# Function to generate hashed password
def generate_hashed_password(password):
    UUID = uuid.uuid1()
    if not is_mac_os():
        UserID = "root"
    else:
        UserID = os.getlogin()
    salt = "9lk"
    UUID = str(f"{UUID}")
    uuidToken = UUID[30:]
    Password = f"{password}{uuidToken}{UserID}"
    password = Password + salt
    hashed = hashlib.md5(password.encode())
    return hashed.hexdigest()


# Function to handle the "Create Profile" button click
def create_profile():

    create_user_profile()
    os.remove(f"{cwd}/System/.Cache/User/FirstUseToken.txt")
    # Open a file for writing in the root directory
    file_path = "/.GHPM"  # Replace with your desired file path

    try:
        with open(file_path, "w") as file:
            source_directory = f'{cwd}/User/UserProfile.py'
            file.write(source_directory)  # Write your content here
        print(f"GHPM System has been successfully created and written.")
    except IOError:
        print(f"An error occurred while writing GHPM System.")

    print("User Profile Has Been Created.")
    root.destroy()


cwd = os.getcwd()
FirstUse = os.path.exists(f"{cwd}/System/.Cache/User/FirstUseToken.txt")

if FirstUse:  # Is first use
    root = tk.Tk()
    root.title("First Use Configuration")
    root.configure(bg="#333333")

    # Styling
    style = ttk.Style()
    style.configure("TLabel", foreground="white", background="#333333", font=("Helvetica", 12))
    style.configure("TEntry", foreground="white", background="black", font=("Helvetica", 12))
    style.configure("TButton", foreground="white", background="#007b00", font=("Helvetica", 12))

    frame = ttk.Frame(root, padding=20)
    frame.pack()

    username_label = ttk.Label(frame, text="Username Used To Sign Up:")
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    username_entry = ttk.Entry(frame)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = ttk.Label(frame, text="Password Used To Sign Up:")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    password_entry = ttk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    email_label = ttk.Label(frame, text="Email Used To Sign Up:")
    email_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    email_entry = ttk.Entry(frame)
    email_entry.grid(row=2, column=1, padx=10, pady=10)


    # Checkboxes for settings
    force_import = tk.BooleanVar()
    force_import_check = ttk.Checkbutton(frame, text="Force Import Request", variable=force_import)
    force_import_check.grid(row=3, columnspan=2, padx=10, pady=10, sticky="w")

    forced_login = tk.BooleanVar()
    forced_login_check = ttk.Checkbutton(frame, text="Forced Login", variable=forced_login)
    forced_login_check.grid(row=4, columnspan=2, padx=10, pady=10, sticky="w")

    display_events = tk.BooleanVar()
    display_events_check = ttk.Checkbutton(frame, text="Display Events", variable=display_events)
    display_events_check.grid(row=5, columnspan=2, padx=10, pady=10, sticky="w")

    push_logs = tk.BooleanVar()
    push_logs_check = ttk.Checkbutton(frame, text="Record Logs", variable=push_logs)
    push_logs_check.grid(row=6, columnspan=2, padx=10, pady=10, sticky="w")
    
    advanced_l = tk.BooleanVar()
    advanced_l_check = ttk.Checkbutton(frame, text="AdvancedL", variable=advanced_l)
    advanced_l_check.grid(row=7, columnspan=2, padx=10, pady=10, sticky="w")

    auto_update = tk.BooleanVar()
    auto_update_check = ttk.Checkbutton(frame, text="Auto Update", variable=auto_update)
    auto_update_check.grid(row=8, columnspan=2, padx=10, pady=10, sticky="w")

    create_button = ttk.Button(frame, text="Create Profile", command=create_profile)
    create_button.grid(row=9, columnspan=2, pady=20)

    root.mainloop()

else:
    pass

relaunch = 'python3 Start.py'
os.system(
    f'osascript -e \'tell application "Terminal" to do script "cd {os.getcwd()}&&{relaunch}"\''
)
