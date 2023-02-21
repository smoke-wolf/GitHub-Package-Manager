# Main Launch File
import sys
import os
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
import System.Drive.ModuleVerifier

try:
    exec('System.Drive.ModuleVerifier')
except:
    pass


try:
    import System.Drive.FirstUse

    exec('System.Drive.FirstUse')
except:
    print('First Use Failed')
    sys.exit(0)

import System.Drive.Errors_Events.EventMan as EV

import User

try:

    def gui():
        #   Code to handel GUI function if launch arguments contain '-gui'
        import System.Drive.FunctionRequest as fr

        fr.GUI()

    try:
        try:
            if sys.argv[1] == '-gui':
                try:
                    gui()
                except:
                    pass
            else:
                sys.exit(0)
        except:
            sys.exit(0)
    except:
        try:
            #   Do rest of code for CLI launcher
            # Print launcher banner
            try:
                print(System.Requirements.Banner.Launcher)
            except:
                print(
                    """    
     _                            _               
    | |                          | |              
    | |     __ _ _   _ _ __   ___| |__   ___ _ __ 
    | |    / _` | | | | '_ \ / __| '_ \ / _ \| __|
    | |___| (_| | |_| | | | | (__| | | |  __/ |   
    \_____/\__,_|\__,_|_| |_|\___|_| |_|\___|_|    
    ================================================"""
                )

            # Print welcome message for logged in user
            try:
                print(f'Welcome Back {User.UserProfile.Username}!')
                import System.Drive.Login
                import importlib
                import os

                EV.NewEvent(
                    event=f'{User.UserProfile.Username} Logged In\n', Pol=1
                )
            except:
                sys.exit(0)
        except:
            sys.exit(0)

        import System.Drive
        import System.Drive.FunctionRequest as fr

        # Run function requests and checkpoint
        System.Drive.FunctionRequest.checkpoint()

    import os

    cwd = os.getcwd()

    FirstUse = os.path.exists(
        f'{cwd}/System/Cache/User/FirstUseToken.txt'
    )  # checks if this is the first use
    if FirstUse is True:
        pass
    else:
        import os
        import glob
        import struct
        from Crypto.Cipher import AES

        # Set the directory to encrypt
        directory = f'{User.UserProfile.SourceDirectory}System/Cache'

        with open(
            f'{User.UserProfile.SourceDirectory}System/Cache/User/local', 'r'
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

    import os

    cwd = os.getcwd()

    FirstUse = os.path.exists(
        f'{cwd}/System/Cache/User/FirstUseToken.txt'
    )  # checks if this is the first use

    if FirstUse is True:
        pass
    else:
        import os
        import glob
        import struct
        from Crypto.Cipher import AES

        # Set the directory to encrypt
        directory = f'{User.UserProfile.SourceDirectory}System/Cache'

        with open(
            f'{User.UserProfile.SourceDirectory}System/Cache/User/local', 'r'
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
