import os
import time

from cryptography.fernet import Fernet
import hashlib

import User.UserProfile



import System.Drive.Errors_Events.EventMan as EV
import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Password_Authentication', a3='None')

def Password(Event, Input):
    print('\033[0;31m')
    import User.UserProfile
    import hashlib
    import uuid
    import sys
    import os
    import System.Drive.Errors_Events.EventMan as EV
    import uuid
    EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Password_Authentication', a3='None')
    UUID = uuid.uuid1()

    UserID = os.getlogin()

    salt = '9lk'

    UUID = str(f'{UUID}')

    uuidToken = UUID[30:]
    DefaultTkn = User.UserProfile.uuid1

    if uuidToken in DefaultTkn:
        EV.NewEvent(event='Same Device As Created On = True', Pol=0)
    elif uuidToken == DefaultTkn:
        EV.NewEvent(event='Same Device As Created On = True', Pol=0)
    else:
        EV.NewEvent(
            event='Same Device As Created On = False! ->> WARNING Separate Device',
            Pol=0,
        )
        Usr = open(f'{User.UserProfile.SourceDirectory}User/Blocked', 'a')
        Usr.write(f'\n{uuidToken}')
        Usr.close()

    if UserID == User.UserProfile.UserPrivileges:
        EV.NewEvent(event='Same User As Configured = True', Pol=0)
    else:
        print(UserID)
        EV.NewEvent(
            event='Same User As Configured = False! ->> WARNING Not Original User',
            Pol=0,
        )

    Password = f'{Input}{uuidToken}{UserID}'

    password = Password + salt
    hashed = hashlib.md5(password.encode())
    Password = hashed.hexdigest()

    if Password == User.UserProfile.Password:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Password Correct {Event}\033[0;35m', Pol=1)

    else:
        print('Password incorrect. Try again\033[0;35m')
        sys.exit(0)

    if Event == 'Login':
        try:
            print('initiate')
            import User.UserProfile as up
            import os
            import glob
            import struct
            from Crypto.Cipher import AES

            # Set the directory to decrypt and the password to use
            directory = f'{User.UserProfile.SourceDirectory}System/.Cache'

            password = hashed.hexdigest()[:16]

            # Pad the password to a multiple of 16 bytes
            password = password + ' ' * (16 - (len(password) % 16))

            # Iterate over all files in the directory and its subdirectories and decrypt them
            for filename in glob.glob(
                os.path.join(directory, '**'), recursive=True
            ):
                if os.path.isfile(filename) and filename.endswith('.enc'):
                    with open(filename, 'rb') as f_in:
                        # Read the nonce, tag, and encrypted data from the file
                        nonce = f_in.read(16)
                        tag = f_in.read(16)
                        encrypted_data = f_in.read()
                        # Create a new AES cipher with the password and mode
                        cipher = AES.new(
                            password.encode('utf-8'), AES.MODE_EAX, nonce=nonce
                        )
                        try:
                            # Decrypt the data with the cipher
                            data = cipher.decrypt_and_verify(
                                encrypted_data, tag
                            )
                        except ValueError:
                            print(f'Failed to decrypt file: {filename}')
                            continue
                    with open(filename[:-4], 'wb') as f_out:
                        # Write the decrypted data to a new file with the same name but without the .enc extension
                        f_out.write(data)
                        # Remove the encrypted file
                        os.remove(filename)

            # Print a message indicating the decryption is complete
            print('Decryption complete')

        except:
            pass


def Create():
    import User.UserProfile
    import hashlib
    import uuid

    Input = input('Enter Your New Password: ')
    UUID = uuid.uuid1()

    UserID = os.getlogin()

    salt = '9lk'

    UUID = str(f'{UUID}')

    uuidToken = UUID[30:]
    DefaultTkn = User.UserProfile.uuid1

    Password = f'{Input}{uuidToken}{UserID}'

    password = Password + salt
    hashed = hashlib.md5(password.encode())
    Password = hashed.hexdigest
    up = open(f'{os.getcwd()}/User/UserProfile.py', 'a')
    up.write(f"\nPassword = '{Password}'")
    with open(
        f'{User.UserProfile.SourceDirectory}System/.Cache/User/local', 'w'
    ) as bl:
        bl.write(hashed.hexdigest()[:16])
    print(Password)



