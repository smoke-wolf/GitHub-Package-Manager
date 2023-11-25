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

-Revised Monday, September 25, 2023
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

def replace_and_remove(directory_a, directory_b):
    # Copy the content of directory B to directory A
    shutil.rmtree(directory_a)  # Remove existing content of directory A
    shutil.copytree(directory_b, directory_a)

    # Remove directory B
    shutil.rmtree(directory_b)


url = "https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/COMPATABLE"

response = requests.get(url)
if response.status_code == 200:
    comp = response.text

    with open(
            f'{UserProfile.SourceDirectory}System/.Cache/System/Version.py',
            'r',
    ) as ver:
        global CurrentVersion
        CurrentVersion = ver.read()

        print(CurrentVersion[11:-2])

    if CurrentVersion[11:-2] in comp:
        AR.AnalyticsRecord(10)
        pass

    else:
        print('No Updates Available')
        sys.exit(0)
else:
    print(f"Failed to fetch content from {url}. Status code: {response.status_code}")

#   Try Update

url = "https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/Version.py"

response = requests.get(url)
if response.status_code == 200:
    content = response.text
    # Now, the content of the URL is stored in the 'content' variable
    print(f'Welcome to the newest version: {content[10:]}')  # You can print it or process it further
    messagebox.showinfo(f"GHPM Update Successful {content[10:]}", "Welcome to the newest version of ghpm, you'll need "
                                                                  "to relaunch.")
    with open(f'{UserProfile.SourceDirectory}System/.Cache/System/Version.py','w') as w:
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