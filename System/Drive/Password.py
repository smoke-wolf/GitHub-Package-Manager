'''

this script is primarily concerned with password authentication,
device and user identity validation, and decryption of files when
logging in. It ensures security and user authentication for the GitHub
Package Manager application.

-Revised Monday, September 25, 2023

'''
import os
import time

import requests
from cryptography.fernet import Fernet
import hashlib

import User.UserProfile



import System.Drive.Errors_Events.EventMan as EV
import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Password_Authentication', a3='None')

def Password(Event, Input):
    '''E'''
    '''We Have Removed the password checks in the most recent version to lack of nececity- the important actions have been verified else where
    All we do now, is a simple authentication check on your token'''

    print('\033[0;31m')
    response = requests.get(
       f'https://hello2022isthe3nd.000webhostapp.com/verifyR.php?username={User.UserProfile.Username}&token={User.UserProfile.Token}')
    if response.text == 'true':
        pass
    else:
        exit()



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
    EV.AnalyticsRecord(Password)



