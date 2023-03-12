# Main Launch File
import sys
import os
import time

try:
    old_folder_name = f"{os.getcwd()}/System/Cache"
    new_folder_name = f"{os.getcwd()}/System/.Cache"

    os.rename(old_folder_name, new_folder_name)
    print('Hidden!')
except:
    pass

import venv

# Set the name and location of the virtual environment
venv_dir = os.path.join(os.getcwd(), 'venv')


# If the virtual environment doesn't exist, create it
if not os.path.exists(venv_dir):
    print('Creating new virtual environment...')
    venv.create(venv_dir, with_pip=True)
else:
    print('Activating existing virtual environment...')
    os.system('source venv/bin/activate')

import System

try:
    import System.Drive.ModuleVerifier

    exec('System.Drive.ModuleVerifier')
except:
    pass

FirstUse = os.path.exists(f'{os.getcwd()}/System/.Cache/User/FirstUseToken.txt')  # checks if this is the first use
if FirstUse is True:
    import System.Drive.FirstUse

    exec('System.Drive.FirstUse')


import User


def check_password(password):
    try:
        import System.Drive.Password as ps

        ps.Password(Event='Login', Input=password)
        print('Logged In Successfully!')
        return True
    except:
        print('Invalid Password')
        return False


def show_password_popup():
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    import System.Drive.FunctionRequest as fr

    popup = tk.Toplevel()
    popup.title("Password Entry")

    style = ttk.Style()
    style.theme_use('clam')

    mainframe = ttk.Frame(popup, padding="30 20 30 20")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    password_entry = ttk.Entry(mainframe, show="*")
    password_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="Enter Password").grid(column=1, row=0, sticky=(tk.W, tk.E))

    def on_submit():
        entered_password = password_entry.get()
        password_correct = check_password(entered_password)
        if password_correct:
            popup.destroy()
            import System.Drive.FunctionRequest as fr
            popup.destroy()

            fr.GUI()

    submit_button = ttk.Button(mainframe, text="Submit", command=on_submit)
    submit_button.grid(column=1, row=2, sticky=(tk.W, tk.E))
    popup.bind("<Return>", lambda event: on_submit())

    for child in mainframe.winfo_children():
        child.grid_configure(padx=10, pady=10)

    password_entry.focus()
    popup.grab_set()
    popup.wait_window()

    return True


def auth():
    show_password_popup()

try:
    try:
        print('Starting')
        auth()
    except:
        import os

        cwd = os.getcwd()

        FirstUse = os.path.exists(
            f'{cwd}/System/.Cache/User/FirstUseToken.txt'
        )  # checks if this is the first use
        if FirstUse is True:
            pass
        else:
            import os
            import glob
            import struct
            from Crypto.Cipher import AES

            # Set the directory to encrypt
            directory = f'{User.UserProfile.SourceDirectory}System/.Cache'

            with open(
                    f'{User.UserProfile.SourceDirectory}System/.Cache/User/local', 'r'
            ) as lc:
                password = lc.read()

            # Remove any unnecessary whitespaces from the password
            password = password.strip()

            # Pad the password to a multiple of 16 bytes
            password = password.encode('utf-8') + b' ' * (
                    16 - (len(password) % 16)
            )

            # Print out the padded password
            print(f'Padded password: {password}')

            # Iterate over all files in the directory and subdirectories and encrypt them
            for root, dirs, files in os.walk(directory):
                for filename in files:
                    if 'enc' in filename:
                        pass
                    else:
                        filepath = os.path.join(root, filename)
                        with open(filepath, 'rb') as f_in:
                            data = f_in.read()
                            # Create a new AES cipher with a new nonce and the password
                            cipher = AES.new(password, AES.MODE_EAX)
                            # Encrypt the data with the cipher
                            encrypted_data, tag = cipher.encrypt_and_digest(data)
                        with open(filepath + '.enc', 'wb') as f_out:
                            # Write the nonce, tag and encrypted data to a new file with the same name plus the .enc extension
                            f_out.write(cipher.nonce)
                            f_out.write(tag)
                            f_out.write(encrypted_data)
                        # Remove the unencrypted file
                        os.remove(filepath)

            # Print a message indicating the encryption is complete
            print('Encryption complete')
except:
    print('Encryption error: Re-trying')
    import os

    cwd = os.getcwd()

    FirstUse = os.path.exists(
        f'{cwd}/System/.Cache/User/FirstUseToken.txt'
    )  # checks if this is the first use
    if FirstUse is True:
        pass
    else:
        import os
        import glob
        import struct
        from Crypto.Cipher import AES

        # Set the directory to encrypt
        directory = f'{User.UserProfile.SourceDirectory}System/.Cache'
        try:
            with open(
                    f'{User.UserProfile.SourceDirectory}System/.Cache/User/local', 'r'
            ) as lc:
                password = lc.read()

            # Remove any unnecessary whitespaces from the password
            password = password.strip()

            # Pad the password to a multiple of 16 bytes
            password = password.encode('utf-8') + b' ' * (
                    16 - (len(password) % 16)
            )

            # Print out the padded password
            print(f'Padded password: {password}')

            # Iterate over all files in the directory and subdirectories and encrypt them
            for root, dirs, files in os.walk(directory):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    with open(filepath, 'rb') as f_in:
                        data = f_in.read()
                        # Create a new AES cipher with a new nonce and the password
                        cipher = AES.new(password, AES.MODE_EAX)
                        # Encrypt the data with the cipher
                        encrypted_data, tag = cipher.encrypt_and_digest(data)
                    with open(filepath + '.enc', 'wb') as f_out:
                        # Write the nonce, tag and encrypted data to a new file with the same name plus the .enc extension
                        f_out.write(cipher.nonce)
                        f_out.write(tag)
                        f_out.write(encrypted_data)
                    # Remove the unencrypted file
                    os.remove(filepath)

            # Print a message indicating the encryption is complete
            print('Encryption complete')
        except:
            pass
try:
    print('Encryption error: Re-trying')
    import os

    cwd = os.getcwd()

    FirstUse = os.path.exists(
        f'{cwd}/System/.Cache/User/FirstUseToken.txt'
    )  # checks if this is the first use
    if FirstUse is True:
        pass
    else:
        import os
        import glob
        import struct
        from Crypto.Cipher import AES

        # Set the directory to encrypt
        directory = f'{User.UserProfile.SourceDirectory}System/.Cache'

        with open(
                f'{User.UserProfile.SourceDirectory}System/.Cache/User/local', 'r'
        ) as lc:
            password = lc.read()

        # Remove any unnecessary whitespaces from the password
        password = password.strip()

        # Pad the password to a multiple of 16 bytes
        password = password.encode('utf-8') + b' ' * (
                16 - (len(password) % 16)
        )

        # Print out the padded password
        print(f'Padded password: {password}')

        # Iterate over all files in the directory and subdirectories and encrypt them
        for root, dirs, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                with open(filepath, 'rb') as f_in:
                    data = f_in.read()
                    # Create a new AES cipher with a new nonce and the password
                    cipher = AES.new(password, AES.MODE_EAX)
                    # Encrypt the data with the cipher
                    encrypted_data, tag = cipher.encrypt_and_digest(data)
                with open(filepath + '.enc', 'wb') as f_out:
                    # Write the nonce, tag and encrypted data to a new file with the same name plus the .enc extension
                    f_out.write(cipher.nonce)
                    f_out.write(tag)
                    f_out.write(encrypted_data)
                # Remove the unencrypted file
                os.remove(filepath)

        # Print a message indicating the encryption is complete
        print('Encryption complete')
except:
    pass
