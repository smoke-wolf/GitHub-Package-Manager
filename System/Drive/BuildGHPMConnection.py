import os
import re
import User.UserProfile
import requests

Username = User.UserProfile.Username
Token = User.UserProfile.Token
def create_ghc_file(dir_path,subdir):
    # Task 1: Create 'ghc.py' in the top-level directory with preset data
    ghc_content = f"""
import inspect
import requests
import os
import datetime
token = '{Token}'
username = '{Username}'
"""
    ghc_2 = """
def NewIn(a1=None, a2=None, a3=None):
    mes = input(a1) 

    return mes

def NewEvent(a1=None, a2=None, a3=None):
    mes = a1
    print(mes)
    """
    ghc_file_path = os.path.join(dir_path, 'ghc.py')
    qc = False
    if os.path.exists(ghc_file_path):
        print(f'{subdir} is already connected')
        qc = True

    with open(ghc_file_path, 'w') as ghc_file:
        ghc_file.write(ghc_content)
        ghc_file.write(f'\n{ghc_2}')
        if qc:
            print(f'{subdir} connection updated')
            exit(0)
    tfs = requests.get('https://hello2022isthe3nd.000webhostapp.com/GHPMTestFeatures000:252652075042380523045623452345235')
    tfs = str(tfs.content)
    # Task 2: Add 'import ghc' to the beginning of each Python file in subdirectories
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.py'):
                if str('True') in tfs:
                    print(f'{subdir}/{file} Connection added')
                    if file == 'ghc.py':
                        continue

                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as py_file:
                        lines = py_file.readlines()
                        lines.insert(4, "import ghc\n")
                        with open(file_path, 'w') as py_file:
                            py_file.writelines(lines)

                    # Task 3: Replace 'print(' with 'ghc.newevent('
                    with open(file_path, 'r') as py_file:
                        content = py_file.read()
                        content = re.sub(r'print\(', 'ghc.NewEvent(', content)
                        content = re.sub(r'input\(', 'ghc.NewIn(', content)
                    with open(file_path, 'w') as py_file:
                        py_file.write(content)

def __main__():
    try:
        tfs = requests.get(
            'https://hello2022isthe3nd.000webhostapp.com/GHPMTestFeatures000:252652075042380523045623452345235')
        tfs = str(tfs.content)
        # Replace 'directory_path' with the directory path where you want to perform these operations
        directory_path = f'{User.UserProfile.SourceDirectory}System/.Cache/System/GitHub/Downloads'

        # Get the list of all items (files and directories) in the specified directory
        items = os.listdir(directory_path)

        # Filter out only directories from the items list and get their full paths
        subdirs = [os.path.join(directory_path, item) for item in items if os.path.isdir(os.path.join(directory_path, item))]
        if str('True') in tfs:
            print("Subdirectories:")
            print('============================')
            for subdir in subdirs:
                print(f'updating {subdir} connection')
                try:
                    create_ghc_file(subdir,subdir)
                except:
                    pass
                print(f'{subdir} connection complete')
                print('============================')
    except:
        pass
