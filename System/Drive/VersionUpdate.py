import shutil
import os
import sys
import requests

import System.Drive.Errors_Events.EventMan as AR
import User.UserProfile as UserProfile

def clear_downloads_dir():
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

def check_for_update():
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
            clear_downloads_dir()
            AR.AnalyticsRecord(10)
            pass
    
        else:
            print('No Updates Available')
            sys.exit(0)
    else:
        print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
        sys.exit(0)

#   Try Update
def download_and_apply():
    url = "https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/Version.py"
    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        # Now, the content of the URL is stored in the 'content' variable
        print(f'Welcome to the newest version: {content[10:]}')  # You can print it or process it further
        with open(f'{UserProfile.SourceDirectory}System/.Cache/System/Version.py','w') as w:
            w.write(content)
    
    else:
        print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
    
    os.chdir(f'{UserProfile.SourceDirectory}System/.Cache/System/Update')
    os.system('git clone -b UPDATE https://github.com/smoke-wolf/GitHub-Package-Manager.git')
    replace_and_remove(f'{UserProfile.SourceDirectory}System/Drive',
                       f'{UserProfile.SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/System/Drive')


try:
    check_for_updates()
    download_and_apply()
except:
    pass
