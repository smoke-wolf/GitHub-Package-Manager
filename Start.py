import sys
import os
import time


import venv
import System


def check_first_use():
    first_use_token = f'{os.getcwd()}/System/.Cache/User/FirstUseToken.txt'
    return os.path.exists(first_use_token)


def handle_first_use():
    if check_first_use():
        import System.Drive.FirstUse
        sys.exit(0)


handle_first_use()

import System.Drive.FunctionRequest as fr


def rename_folder(old_folder_name, new_folder_name):
    try:
        os.rename(old_folder_name, new_folder_name)
        print('Hidden!')
    except Exception as e:
        print(f'Error: {e}')


def create_virtual_environment(venv_dir):
    if not os.path.exists(venv_dir):
        print('Creating new virtual environment...')
        venv.create(venv_dir, with_pip=True)
    else:
        print('Activating existing virtual environment...')
        os.system('source venv/bin/activate')


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

    venv_dir = os.path.join(os.getcwd(), 'venv')
    create_virtual_environment(venv_dir)

    run_module_verifier()

    handle_first_use()

    import System.Drive.Errors_Events.EventMan as EV
    import uuid
    EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Login', a3='None')

    fr.GUI()


if __name__ == '__main__':
    main()
