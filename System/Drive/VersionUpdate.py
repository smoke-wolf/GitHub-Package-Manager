import shutil
import os
import sys
import requests

import User.UserProfile as UserProfile

def remove_existing_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)

def update_directories(directory_a, directory_b):
    remove_existing_directory(directory_a)
    shutil.copytree(directory_b, directory_a)

def fetch_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request to {url} failed: {str(e)}")

def update_version_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

update_directory = f'{UserProfile.SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager'

remove_existing_directory(f'{UserProfile.SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager')

compatible_url = "https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/COMPATABLE"
version_url = "https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/Version.py"

compatible_content = fetch_content(compatible_url)
if compatible_content:
    with open(f'{UserProfile.SourceDirectory}System/.Cache/System/Version.py', 'r') as version_file:
        current_version = version_file.read()[11:-2]

    if current_version in compatible_content:
        print(current_version)
    else:
        print('No Updates Available')
        sys.exit(0)
else:
    sys.exit(1)

new_version_content = fetch_content(version_url)
if new_version_content:
    print(f'Welcome to the newest version: {new_version_content[10:]}')
    update_version_file(f'{UserProfile.SourceDirectory}System/.Cache/System/Version.py', new_version_content)
else:
    sys.exit(1)

os.chdir(f'{UserProfile.SourceDirectory}System/.Cache/System/Update')
os.system('git clone -b UPDATE https://github.com/smoke-wolf/GitHub-Package-Manager.git')
update_directories(f'{UserProfile.SourceDirectory}System/Drive',
                   f'{UserProfile.SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/System/Drive')
