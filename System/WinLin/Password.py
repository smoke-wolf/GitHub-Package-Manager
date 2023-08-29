import os
import time
from typing import ParamSpecKwargs

from cryptography.fernet import Fernet
import hashlib

import User.UserProfile


def Password(Event, Input):
  pass


def Create():
  pass


def Crypt(key, Password):
  pass
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
  pass


def decrypt(filename, key):
  pass


def LAUNCH(Password):
  pass


def write_key():
  pass


def main(message, password, f, address):
  pass
