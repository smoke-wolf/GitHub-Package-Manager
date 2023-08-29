import sys
import os
import time
try:
  os.system('pip3 install requests')
except:
  pass
import venv
import System

import platform


def is_mac_os():
  return platform.system() == "Darwin"


def check_first_use():
  first_use_token = f'{os.getcwd()}/System/.Cache/User/FirstUseToken.txt'
  return os.path.exists(first_use_token)


def handle_first_use():
  if check_first_use():
    import System.Drive.FirstUse
    sys.exit(0)


handle_first_use()


def rename_folder(old_folder_name, new_folder_name):
  try:
    os.rename(old_folder_name, new_folder_name)
    print('Hidden!')
  except Exception as e:
    print(f'Error: {e}')


def run_module_verifier():
  try:
    import System.Drive.ModuleVerifier
    exec('System.Drive.ModuleVerifier')
  except Exception as e:
    print(f'Error: {e}')


def main():
  try:
    old_folder_name = f"{os.getcwd()}/System/Cache"
    new_folder_name = f"{os.getcwd()}/System/.Cache"

    rename_folder(old_folder_name, new_folder_name)
  except:
    pass

  run_module_verifier()

  handle_first_use()

  import System.Drive.Errors_Events.EventMan as EV
  import uuid
  EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Login', a3='None')
  if is_mac_os() is not True:
    confirm = input('Use GUI (Linux only) Y/n: ')
    if confirm != 'Y' or 'y':
      import System.WinLin.comline
      exec(System.WinLin.comline.checkpoint())
    else:
      import System.Drive.FunctionRequest as fr
      fr.GUI()

  else:
    import System.Drive.FunctionRequest as fr
    fr.GUI()


if __name__ == '__main__':
  main()
