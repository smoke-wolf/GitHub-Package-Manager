import hashlib
import inspect
import os
import platform
import re
import shutil
import subprocess
import time
import uuid
import System.Drive.Errors_Events.EventMan as EV
import requests
import User
import User.UserProfile as UserProfile
from System.Drive.FirstUse import is_mac_os


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


def display_notification(title, message):
    if User.UserProfile.DisplaySystemEvents:
        if platform.system() == 'Darwin':  # Checking if the platform is macOS
            script = f'display notification "{message}" with title "{title}"'
            subprocess.run(['osascript', '-e', script])
        elif platform.system() == 'Windows':  # Checking if the platform is Windows
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=5)  # Display notification for 5 seconds
            except:
                print('Install win10toast for notifications.')
        else:
            print(f'Notifications not supported on {platform.system()}')


def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name


def CheckInternetConection():
    if User.UserProfile.OFFLINE:
        pass
    else:
        try:
            response = requests.get("https://www.google.com", timeout=1)
            if response.status_code == 200:
                pass
        except:
            display_notification("Hold Up!", "To continue using ghpm. Please connect to the internet")

            def check_internet_connection():
                try:
                    response = requests.get("https://www.google.com", timeout=5)
                    return response.status_code == 200
                except requests.ConnectionError:
                    return False

            while True:
                if User.UserProfile.OFFLINE:
                    break
                if check_internet_connection():
                    # Internet connection is available, display thank you message
                    display_notification("Thank you!", " Please continue enjoying ghpm!!")

                    break  # Exit the loop
                else:
                    # Internet connection is not available, wait for a while and check again
                    time.sleep(0.5)  # Wait for 5 seconds before checking again


def is_safe_input(input_str):
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
    # Regular expression pattern for command injection detection
    command_injection_pattern = r"[;&|`'\"\$()<>]"

    # Check if the input string matches the command injection pattern
    if re.search(command_injection_pattern, input_str):
        return False  # The string contains potential command injection


    return True  # The string is considered safe


def remove_line_by_content(file_path, content_to_remove):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                if content_to_remove not in line:
                    file.write(line)

        EV.AnalyticsRecord(f"Lines containing '{content_to_remove}' removed from {file_path}")
    except FileNotFoundError:
        EV.AnalyticsRecord(f"File '{file_path}' not found.")
    except Exception as e:
        EV.AnalyticsRecord(f"An error occurred: {e}")


def replace_and_remove(directory_a, directory_b):
    # Copy the content of directory B to directory A
    shutil.rmtree(directory_a)  # Remove existing content of directory A
    shutil.copytree(directory_b, directory_a)

    # Remove directory B
    shutil.rmtree(directory_b)


def download_zip_from_php():
    php_script_url = 'https://hello2022isthe3nd.000webhostapp.com/update.zip'
    import requests
    import zipfile
    import io
    import os

    zip_url = 'https://hello2022isthe3nd.000webhostapp.com/update.zip'
    download_path = f'{UserProfile.SourceDirectory}System/.Cache/System/Update/update.zip'

    # Download the ZIP file
    response = requests.get(zip_url)
    if response.status_code == 200:
        with open(download_path, 'wb') as f:
            f.write(response.content)
        print('Update file downloaded successfully')
    else:
        print('Failed to download update file')

    # Specify the extraction path
    extraction_path =  f'{UserProfile.SourceDirectory}System/.Cache/System/Update/'  # Specify the extraction path

    # Check if the download was successful before attempting extraction
    if os.path.exists(download_path):
        # Extract the contents of the ZIP file
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)
        print('Update file extracted successfully')
    else:
        print('Extraction failed - download was unsuccessful or file does not exist')


def Storage(directory):
    import os

    total_size = 0
    total_subdirs = 0
    total_files = 0

    for root, dirs, files in os.walk(directory):
        total_subdirs += len(dirs)
        total_files += len(files)
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)

    return total_size, total_subdirs, total_files

def Info():
    import User.UserProfile


    size1, subdirs1, files1 = Storage(f'{User.UserProfile.SourceDirectory}System/.Cache/System')
    size2, subdirs2, files2 = Storage(f'{User.UserProfile.SourceDirectory}System/.Cache/System/GitHub')
    size3, subdirs3, files3 = Storage(f'{User.UserProfile.SourceDirectory}System/.Cache/System/Local')
    size4, subdirs4, files4 = Storage(f'{User.UserProfile.SourceDirectory}System/.Cache/System/ErrorLog')
    size, subdirs, files = Storage(User.UserProfile.SourceDirectory)

    info_text = f"""GHPM (GitHub Package Manager)
    |=====================================
    |Current Usage -> {size/100000} Mb
    |Total Files -> {files}
    |System Usage -> {(size - size1)/100000} Mb
    |System Files -> {(files - files1)}
    |System Dirs -> {(subdirs - subdirs1)}
    |=====================================
    |Github Storage -> {size2/100000} Mb
    |GitHub Sub-dirs -> {subdirs2}
    |=====================================
    |Local Storage -> {size3/100000} Mb
    |Local Sub-dirs -> {subdirs3}
    |=====================================
    |Log Storage -> {size4/100000} Mb
    |Log Sub-dirs -> {subdirs4}
    |====================================="""

    return info_text

