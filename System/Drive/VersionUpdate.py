'''
This script is designed to manage updates for a GitHub Package Manager (GHPM) application.
It starts by attempting to remove a specific directory related to cached update data.
The script then checks for compatibility information by sending a GET request to a URL
and compares it to the current version of the application. If a new version is available,
it displays an information dialog to notify the user and proceeds to fetch the new version
and related files. It then changes the working directory to a specific location and uses git
to clone the "UPDATE" branch of the GitHub repository to update the application's files.
Finally, it opens a new Terminal window and runs a Python script to relaunch the updated application,
ensuring that users are using the latest version of the GitHub Package Manager.

Apply changes to accept Windows OS an it's filepath system.

-Revised Monday, October 3, 2023
'''

import shutil
import os
import sys
from tkinter import messagebox

import System.Drive.Errors_Events.EventMan as AR
import User.UserProfile as UserProfile

import requests

try:
    shutil.rmtree(f'{UserProfile.SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager')
except:
    pass
os.chdir(f'{UserProfile.SourceDirectory}System')


def replace_and_remove(directory_a, directory_b):
    # Copy the content of directory B to directory A
    shutil.rmtree(directory_a)  # Remove existing content of directory A
    shutil.copytree(directory_b, directory_a)

    # Remove directory B
    shutil.rmtree(directory_b)


import os
import hashlib
import requests


# Function to generate a checksum for a file
def generate_checksum_for_file(file_path, hash_algorithm='sha256'):
    hasher = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # Read in 64k chunks
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


# Function to generate checksums for all files in the current directory and subdirectories
def generate_checksums_for_current_directory(hash_algorithm='sha256'):
    checksums = {}
    for root, _, files in os.walk(f'{UserProfile.SourceDirectory}System/Drive'):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            checksum = generate_checksum_for_file(file_path, hash_algorithm)
            checksums[file_path] = checksum
    return checksums


# URL to download the remote checksums
url = "https://hello2022isthe3nd.000webhostapp.com/CheckSum"
Update_ = False
response = requests.get(url)
if response.status_code == 200:
    remote_checksums = {}
    for line in response.text.splitlines():
        file_path, checksum = line.split(': ')
        remote_checksums[file_path] = checksum

    # Generate local checksums for the current directory
    local_checksums = generate_checksums_for_current_directory()

    modified_paths = {}
    for path, checksum in local_checksums.items():
        # Find the position of '/System/' in the path
        system_index = path.find('/System/')

        if system_index != -1:
            # Extract everything after and including '/System/' and update the dictionary
            modified_path = path[system_index:]
            modified_paths[modified_path] = checksum
    local_checksums = modified_paths
    for file_path, remote_checksum in remote_checksums.items():
        for ind in local_checksums:
            if file_path[1:-1] == ind:
                print('=====================')
                print(file_path[1:-1])
                print(ind)
                print('=====================')
                if local_checksums[file_path[1:-1]] != remote_checksum[1:-1]:
                    print(f'{local_checksums[file_path[1:-1]]} does not equal {remote_checksum}')
                    print(f"Updated file detected: {file_path}")
                    Update_ = True

    print("Checksum comparison completed.")
    if Update_ is False:
        print('No Update Found')
        sys.exit(0)

else:
    print(f"Failed to fetch content from {url}. Status code: {response.status_code}")

#
# `  ADDED METHOD FOR ALERTS
#

url = "https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/COMPATABLE"

response = requests.get(url)
if response.status_code == 200:
    comp = response.text

    with open(
            f'{UserProfile.SourceDirectory}System/.Cache/System/Version.py',
            'r',
    ) as ver:

        CurrentVersion = ver.read()



    if CurrentVersion[11:-2] in comp:

        pass

    else:
        FuckedWith = True
else:
    print(f"Failed to fetch content from {url}. Status code: {response.status_code}")

#   Try Update

url = "https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/Version.py"

response = requests.get(url)
if response.status_code == 200:
    content = response.text
    # Now, the content of the URL is stored in the 'content' variable
    if FuckedWith:
        import System.Drive.Errors_Events.EventMan as EV
        EV.NewEvent("CHANGING CODE IS NOT ADVISED FOR FUNCTIONALITY", 1)

    else:
        print(f'Welcome to the newest version: {content[10:]}')  # You can print it or process it further
    if FuckedWith:
        messagebox.showinfo(f"ALERT",
                            "Please Stop Messing With The Code")
    else:
        messagebox.showinfo(f"GHPM Update Successful {content[10:]}", "Welcome to the newest version of ghpm, you'll need "
                                                                      "to relaunch.")
    with open(f'{UserProfile.SourceDirectory}System/.Cache/System/Version.py', 'w') as w:
        w.write(content)

    url = "https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/Local/download/server.js"

    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        with open(f'{UserProfile.SourceDirectory}System/.Cache/System/Local/download/server.js', 'w') as w:
            w.write(content)

else:
    print(f"Failed to fetch content from {url}. Status code: {response.status_code}")

os.chdir(f'{UserProfile.SourceDirectory}System/.Cache/System/Update')
os.system('git clone -b UPDATE https://github.com/smoke-wolf/GitHub-Package-Manager.git')
replace_and_remove(f'{UserProfile.SourceDirectory}System/Drive',
                   f'{UserProfile.SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/System/Drive')
relaunch = 'python3 Start.py'
os.system(
    f'osascript -e \'tell application "Terminal" to do script "cd {UserProfile.SourceDirectory}&&{relaunch}"\''
)
