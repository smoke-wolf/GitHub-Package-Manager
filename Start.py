import os
from tkinter import messagebox
import venv
import sys
import importlib
import requests


Dailmess = False #  Change this to True for a daily messag easter egg

# Retrieving command-line arguments
args = sys.argv

# Function to swap content between two files
def swap_file_content(file1_path, file2_path):
    try:
        # Read content from the first file
        with open(file1_path, 'r') as file1:
            file1_content = file1.read()

        # Read content from the second file
        with open(file2_path, 'r') as file2:
            file2_content = file2.read()

        # Write the content of the first file into the second file
        with open(file2_path, 'w') as file2:
            file2.write(file1_content)

        # Write the content of the second file into the first file
        with open(file1_path, 'w') as file1:
            file1.write(file2_content)

        print(f"Profile Switched")
    except FileNotFoundError:
        print("User Profile Not Found")


# Function to reload a Python module
def reload_module(module_name):
    try:
        module = importlib.import_module(module_name)
        importlib.reload(module)
        print(f"{module_name} reloaded successfully.")
    except Exception as e:
        print(f"Error reloading {module_name}: {e}")

# Function to check if it's the first use and take action accordingly
def check_first_use():
    first_use_token = f'{os.getcwd()}/System/.Cache/User/FirstUseToken.txt'
    return os.path.exists(first_use_token)

# Handling the first use scenario
def handle_first_use():
    if check_first_use():
        import System.Drive.FirstUse
        sys.exit(0)

# Function to rename a folder
def rename_folder(old_folder_name, new_folder_name):
    try:
        os.rename(old_folder_name, new_folder_name)
        print('Hidden!')
    except Exception as e:
        print(f'Error: {e}')

# Function to create a virtual environment
def create_virtual_environment(venv_dir):
    if not os.path.exists(venv_dir):
        print('Creating new virtual environment...')
        venv.create(venv_dir, with_pip=True)
    else:
        print('Activating existing virtual environment...')
        os.system('source venv/bin/activate')

# Function to run a module verifier
def run_module_verifier():
    try:
        import System.Drive.ModuleVerifier
        exec('System.Drive.ModuleVerifier')
    except Exception as e:
        print(f'Error: {e}')


def DailyM():
    limit = 1
    api_url = 'https://v2.jokeapi.dev/joke/Programming,Miscellaneous?blacklistFlags=nsfw,explicit&format=txt&type=single'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        return(response.text)


# Checking and responding to first use status
handle_first_use()

try:
    old_folder_name = f"{os.getcwd()}/System/Cache"
    new_folder_name = f"{os.getcwd()}/System/.Cache"

    rename_folder(old_folder_name, new_folder_name)
except:
    pass

# Creating/activating a virtual environment
venv_dir = os.path.join(os.getcwd(), 'venv')
create_virtual_environment(venv_dir)

# Running a module verifier
run_module_verifier()

# Importing the user profile and reloading it
import User.UserProfile
reload_module('User.UserProfile')

# Handling errors and continuing the flow
import System.Drive.Errors_Events.EventMan as EV
import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Login', a3='None')

# Check if the desired launch argument exists (-nu {filepath})
if "-nu" in args:
    index = args.index("-nu")
    if index + 1 < len(args):
        file_path = args[index + 1]  # Get the file path
        file_path = (f'{file_path}/User/UserProfile.py')
        print(f"New User provided: {file_path}")
        import User.UserProfile  # Importing the user profile
        swap_file_content(file_path, f'{os.getcwd()}/User/UserProfile.py')
    else:
        print("No file path provided after -tu")
try:
    import System.Drive.FunctionRequest as fr
    import System.Drive.BuildGHPMConnection as bgc
    bgc.__main__()
    if Dailmess:
        messagebox.showinfo(f"Daily Joke", f"{DailyM()}")
    fr.GUI()
    try:
        swap_file_content(file_path, f'{os.getcwd()}/User/UserProfile.py')
    except Exception:
        print(Exception)
except Exception:
    print(Exception)
    swap_file_content(file_path, f'{os.getcwd()}/User/UserProfile.py')
