'''
This script appears to be responsible for creating a user profile 
during the first use of a program and then initiating a relaunch of the program.
Here's a brief description of its logic:

The script defines several functions to check the operating system,
create a user profile, and generate a hashed password.

is_mac_os() function checks if the current operating system is macOS by comparing
the result of platform.system() with "Darwin."

create_user_profile() function creates a user profile with various user-related
information like username, hashed password, user privileges, source directory, and others.
It writes this information to a file named "UserProfile.py" in the "User" directory.

generate_hashed_password() function generates a hashed password by combining the provided
password with a salt and other values, then using MD5 hashing.

create_profile() function is called when a "Create Profile" button is clicked. 
It creates the user profile, deletes a "FirstUseToken.txt" file, and writes some information to a "/.GHPM" file
(you should replace this with your desired file path). After this,
it prints messages indicating the actions performed and closes the GUI window.

The script checks if it's the first use by looking for the existence of a "FirstUseToken.txt" file.

If it's the first use, the script opens a GUI window using tkinter to prompt the user to enter a username and password.
After filling out this information and clicking "Create Profile," the user profile is created, and the GUI window closes.

After creating the user profile (or if it's not the first use), the script initiates a relaunch of the program. 
It executes the "Start.py" file in a new terminal window by using os.system and AppleScript to run a command in Terminal.

In summary, this script is used to set up a user profile during the first use of a program, and then it relaunches the program
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
    user_profile_path = f"{cwd}/User/UserProfile.py"
    with open(user_profile_path, "w") as user_profile:
        username = username_entry.get()
        password = password_entry.get()
        hashed_password = generate_hashed_password(password)
        user_privileges = "root" if not is_mac_os() else os.getlogin()
        source_directory = os.getcwd()
        uuid1 = uuid.uuid1().hex
        uuid4 = uuid.uuid4().hex

        user_profile_content = (
            f"Username = '{username}'\n"
            f"Password = '{hashed_password}'\n"
            f"UserPrivileges = '{user_privileges}'\n"
            f"SourceDirectory = '{source_directory}/'\n"
            f"Force_Import_Request = {force_import.get()}\n"
            f"Forced_Login = {forced_login.get()}\n"
            f"uuid1 = '{uuid1}'\n"
            f"uuid4 = '{uuid4}'\n"
            f"DisplayEvents = {display_events.get()}\n"
            f"PushLogs = {push_logs.get()}\n"
            f"AdvancedL = {advanced_l.get()}\n"
            f"AutoUpdate = {auto_update.get()}\n"
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

    username_label = ttk.Label(frame, text="Enter Username:")
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    username_entry = ttk.Entry(frame)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = ttk.Label(frame, text="Create Password:")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    password_entry = ttk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Checkboxes for settings
    force_import = tk.BooleanVar()
    force_import_check = ttk.Checkbutton(frame, text="Force Import Request", variable=force_import)
    force_import_check.grid(row=2, columnspan=2, padx=10, pady=10, sticky="w")

    forced_login = tk.BooleanVar()
    forced_login_check = ttk.Checkbutton(frame, text="Forced Login", variable=forced_login)
    forced_login_check.grid(row=3, columnspan=2, padx=10, pady=10, sticky="w")

    display_events = tk.BooleanVar()
    display_events_check = ttk.Checkbutton(frame, text="Display Events", variable=display_events)
    display_events_check.grid(row=4, columnspan=2, padx=10, pady=10, sticky="w")

    push_logs = tk.BooleanVar()
    push_logs_check = ttk.Checkbutton(frame, text="Push Logs", variable=push_logs)
    push_logs_check.grid(row=5, columnspan=2, padx=10, pady=10, sticky="w")

    advanced_l = tk.BooleanVar()
    advanced_l_check = ttk.Checkbutton(frame, text="AdvancedL", variable=advanced_l)
    advanced_l_check.grid(row=6, columnspan=2, padx=10, pady=10, sticky="w")

    auto_update = tk.BooleanVar()
    auto_update_check = ttk.Checkbutton(frame, text="Auto Update", variable=auto_update)
    auto_update_check.grid(row=7, columnspan=2, padx=10, pady=10, sticky="w")

    create_button = ttk.Button(frame, text="Create Profile", command=create_profile)
    create_button.grid(row=8, columnspan=2, pady=20)

    root.mainloop()

else:
    pass

relaunch = 'python3 Start.py'
os.system(
    f'osascript -e \'tell application "Terminal" to do script "cd {os.getcwd()}&&{relaunch}"\''
)
