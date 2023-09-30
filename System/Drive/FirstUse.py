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
            f"Force_Import_Request = False\n"
            f"Forced_Login = True\n"
            f"uuid1 = '{uuid1}'\n"
            f"uuid4 = '{uuid4}'\n"
            f"DisplayEvents = False\n"
            f"PushLogs = True\n"
            f"AdvancedL = True\n"
            f"AutoUpdate = True\n"
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
        print(f"GHPM Sytem has been successfully created and written.")
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

    create_button = ttk.Button(frame, text="Create Profile", command=create_profile)
    create_button.grid(row=2, columnspan=2, pady=20)

    root.mainloop()

else:
    pass


relaunch = 'python3 Start.py'
os.system(
                f'osascript -e \'tell application "Terminal" to do script "cd {os.getcwd()}&&{relaunch}"\''
            )
