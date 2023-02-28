import os
import time
try:
    from cryptography.fernet import Fernet
    import hashlib
except:
    pass

import User.UserProfile


def Password(Event, Input):
    print('\033[0;31m')
    import User.UserProfile
    import hashlib
    import uuid
    import sys
    import os
    import System.Drive.Errors_Events.EventMan as EV

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
        sys.exit()

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
    Password = hashed.hexdigest()
    input('Return ENTER To Accesses New Key')
    up = open(f'{os.getcwd()}/User/UserProfile.py', 'a')
    up.write(f"\nPassword = '{Password}'")
    with open(
        f'{User.UserProfile.SourceDirectory}System/.Cache/User/local', 'w'
    ) as bl:
        bl.write(hashed.hexdigest()[:16])
    print(Password)


def Crypt(key, Password):
    UserKey = f'{key}{Password}'
    import User.UserProfile
    import hashlib
    import uuid

    UUID = uuid.uuid1()

    UserID = os.getlogin()

    salt = '69dicks'

    UUID = str(f'{UUID}')

    uuidToken = UUID[30:]
    DefaultTkn = User.UserProfile.uuid1

    Password = f'{UserKey}{uuidToken}{UserID}'

    password = Password + salt
    hashed = hashlib.md5(password.encode())
    Password = hashed.hexdigest()

    up = open(f'{User.UserProfile.SourceDirectory}User/UserProfile.py', 'a')
    up.write(f'\nUserKey = {Password}')


def UpdateUser():
    Name = input('Enter Your Desired UserName: ')
    input('Return ENTER To confirm')
    up = open(f'{os.getcwd()}/User/UserProfile.py', 'a')
    up.write(f"\nUsername = '{Name}'")
    up.close()
    print('Username Updated!')
    time.sleep(1.2600)
    print(f'Hi there {User.UserProfile.Username}')


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)

    with open(filename, 'rb') as file:
        # read all file data
        file_data = file.read()

    # encrypt data
    encrypted_data = f.encrypt(file_data)

    # write the encrypted file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, 'wb') as file:
        file.write(decrypted_data)


def LAUNCH(Password):
    """
    Generates a key and save it into a file
    """
    import User.UserProfile

    er = open(f'{User.UserProfile.SourceDirectory}User/UserKey.key', 'r')
    key = er.read()
    UserKey = f'{key}{Password}'

    import hashlib
    import uuid

    UUID = uuid.uuid1()

    UserID = os.getlogin()

    salt = '69dicks'

    UUID = str(f'{UUID}')

    uuidToken = UUID[30:]
    DefaultTkn = User.UserProfile.uuid1

    Password = f'{UserKey}{uuidToken}{UserID}'

    password = Password + salt
    hashed = hashlib.md5(password.encode())
    Password = hashed.hexdigest()

    if Password in User.UserProfile.UserKey:
        decrypt(
            f'{User.UserProfile.SourceDirectory}System/.Cache/System/ErrorLog/Event.db'
        )
        print('DATABASE ENABLED')
    else:
        print('DATABASE LOCKED- SUGGESTED UPDATE')


def write_key():
    key = Fernet.generate_key()
    import User

    with open(
        f'{User.UserProfile.SourceDirectory}/User/UserKey.key', 'wb'
    ) as key_file:
        key_file.write(key)

    Crypt(
        key, Password=input('Please Enter Your Password To Add Encryption: ')
    )


def main(message, password, f, address):
    import secrets
    from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

    from cryptography.fernet import Fernet
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    backend = default_backend()
    iterations = 100_000

    def _derive_key(
        password: bytes, salt: bytes, iterations: int = iterations
    ) -> bytes:
        """Derive a secret key from a given password and salt"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=iterations,
            backend=backend,
        )
        return b64e(kdf.derive(password))

    def password_encrypt(
        message: bytes, password: str, iterations: int = iterations
    ) -> bytes:
        salt = secrets.token_bytes(16)
        key = _derive_key(password.encode(), salt, iterations)
        return b64e(
            b'%b%b%b'
            % (
                salt,
                iterations.to_bytes(4, 'big'),
                b64d(Fernet(key).encrypt(message)),
            )
        )

    def password_decrypt(token: bytes, password: str) -> bytes:
        decoded = b64d(token)
        salt, iter, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
        iterations = int.from_bytes(iter, 'big')
        key = _derive_key(password.encode(), salt, iterations)
        return Fernet(key).decrypt(token)

    if f == 2:
        import User.UserProfile

        addy = (
            f'{User.UserProfile.SourceDirectory}System/.Cache/User/ADDRESSLOG'
        )
        fr = open(addy, 'r')
        print('==============')
        line = fr.read()
        print(line)

    if f == 0:
        import User.UserProfile

        addy = (
            f'{User.UserProfile.SourceDirectory}System/.Cache/User/ADDRESSLOG'
        )
        fr = open(addy, 'a')
        fr.write(f'{address}')
        fr.close()
        cont_B = password_encrypt(message.encode(), password)
        import User.UserProfile

        fl = f'{User.UserProfile.SourceDirectory}System/.Cache/User/{address}'
        fl = open(fl, 'wb')
        fl.write(cont_B)
        fl.close()

    if f == 1:
        import User

        fl = f'{User.UserProfile.SourceDirectory}System/.Cache/User/{address}'
        fl = open(fl, 'r')
        cs = fl.read()
        data = password_decrypt(token=cs, password=password).decode()
        return data
