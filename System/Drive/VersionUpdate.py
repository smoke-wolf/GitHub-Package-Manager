#   Try to download System/.Cache/System/Version.py to notify for new versions
import sys
import time
import requests

# this workwed

#   Libraries
import os
import System

import System.Drive.Errors_Events.EventMan as EV
import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Update', a3='None')

#   Local File Imports
global Version

import User.UserProfile as UserProfile

#   Define Variables
try:
    with open(
            f'{UserProfile.SourceDirectory}System/.Cache/System/Version.py',
            'r',
    ) as ver:
        global CurrentVersion
        CurrentVersion = ver.read()
except:
    CurrentVersion = 'Version Cannot Be Read'
CurrentDirectory = os.getcwd()
SourceDirectory = UserProfile.SourceDirectory
UpdateFolderDir = f'{SourceDirectory}System/.Cache/System/Update'


#   Updatable Files


def parish():
    import shutil

    print(
        f'Update Complete! You are now on a new version!'
    )
    try:
        vp = f'{UserProfile.SourceDirectory}System/.Cache/System/Version.py'
        with open(vp, 'w') as vpp:
            response = requests.get(
                'https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/Version.py',
                stream=True,
            )
            v = response.content
            print('passed')
            vpp.write(v.decode('utf-8'))
            print('updated')
    except:
        pass

    tokenL = open(f'{SourceDirectory}System/.Cache/System/Update/Token', 'a')
    tokenL.write(f'{CurrentVersion} -> ')
    tokenL.close()
    shutil.rmtree(f'{UpdateFolderDir}/GitHub-Package-Manager')


#   Start Update
def dl():
    try:
        os.chdir(UpdateFolderDir)  # Change directory to download update
        pass
    except:
        print('Update Folder Does Not Exist')
        raise exit(0)  # Raise an exit because no source to update

    try:
        os.system(
            'git clone -b UPDATE https://github.com/smoke-wolf/GitHub-Package-Manager.git'
        )  # Download Updated Version
    except:
        print(
            'Network may have timed out- Please ensure you are connected to the internet'
        )
        raise exit(0)  # Exiting due to a None response from GitHub

    Update()
    parish()


def Update():
    AllContents_Downloaded = os.listdir(
        f'{SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager'
    )
    AllContents = os.listdir(SourceDirectory)

    try:
        ver2 = open(
            f'{SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/System/.Cache/System/Version.py',
            'r',
        )
        ver4 = ver2.read()
        print(
            f"""
        Current Version= {CurrentVersion}
        Updated {ver4}"""
        )
        time.sleep(2)
    except:
        pass

    for Attempt in AllContents:
        if Attempt in AllContents_Downloaded:
            print(f'Common Found {Attempt}')

            try:
                open(f'{SourceDirectory}{Attempt}', 'w').close()

                SourceClean = open(f'{SourceDirectory}{Attempt}', 'a')

                Update = open(
                    f'{SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/{Attempt}',
                    'r',
                )
                UpdateData = Update.read()
                SourceClean.write(UpdateData)
            except:
                SourceFolder = os.listdir(f'{SourceDirectory}{Attempt}')
                UpdateFolder = os.listdir(
                    f'{SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/{Attempt}'
                )

                for Attempt_i in SourceFolder:
                    if Attempt_i in UpdateFolder:
                        print(f'Common Found {Attempt_i}')
                        if Attempt_i == 'index':
                            pass
                        else:
                            try:
                                open(
                                    f'{SourceDirectory}{Attempt}/{Attempt_i}',
                                    'w',
                                ).close()

                                SourceClean = open(
                                    f'{SourceDirectory}{Attempt}/{Attempt_i}',
                                    'a',
                                )

                                Update = open(
                                    f'{SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/{Attempt}/{Attempt_i}',
                                    'r',
                                )
                                UpdateData = Update.read()
                                SourceClean.write(UpdateData)
                            except:
                                SourceFolder_i = os.listdir(
                                    f'{SourceDirectory}{Attempt}/{Attempt_i}'
                                )
                                UpdateFolder_i = os.listdir(
                                    f'{SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/{Attempt}/{Attempt_i}'
                                )

                                for Attempt_ii in SourceFolder_i:
                                    if Attempt_ii in UpdateFolder_i:
                                        print(f'Common Found {Attempt_ii}')
                                        try:
                                            open(
                                                f'{SourceDirectory}{Attempt}/{Attempt_i}/{Attempt_ii}',
                                                'w',
                                            ).close()

                                            SourceClean = open(
                                                f'{SourceDirectory}{Attempt}/{Attempt_i}/{Attempt_ii}',
                                                'a',
                                            )
                                            Update = open(
                                                f'{SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/{Attempt}/{Attempt_i}/{Attempt_ii}',
                                                'r',
                                            )
                                            UpdateData = Update.read()
                                            SourceClean.write(UpdateData)
                                        except:
                                            SourceFolder_ii = os.listdir(
                                                f'{SourceDirectory}{Attempt}/{Attempt_i}/{Attempt_ii}'
                                            )
                                            UpdateFolder_ii = os.listdir(
                                                f'{SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/{Attempt}/{Attempt_i}/{Attempt_ii}'
                                            )

                                            for Attempt_iii in SourceFolder_ii:
                                                if (
                                                        Attempt_iii
                                                        in UpdateFolder_ii
                                                ):
                                                    print(
                                                        f'Common Found {Attempt_iii}'
                                                    )
                                                    try:
                                                        open(
                                                            f'{SourceDirectory}{Attempt}/{Attempt_i}/{Attempt_ii}/{Attempt_iii}',
                                                            'w',
                                                        ).close()

                                                        SourceClean = open(
                                                            f'{SourceDirectory}{Attempt}/{Attempt_i}/{Attempt_ii}/{Attempt_iii}',
                                                            'a',
                                                        )
                                                        Update = open(
                                                            f'{SourceDirectory}System/.Cache/System/Update/GitHub-Package-Manager/{Attempt}/{Attempt_i}/{Attempt_ii}/{Attempt_iii}',
                                                            'r',
                                                        )
                                                        UpdateData = (
                                                            Update.read()
                                                        )
                                                        SourceClean.write(
                                                            UpdateData
                                                        )

                                                    except:
                                                        pass


try:
    response = requests.get(
        'https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/Version.py',
        stream=True,
    )
    v = response.content
    version2 = v.decode('utf-8')
    if CurrentVersion in version2:
        sys.exit(0)
    try:
        response = requests.get(
            'https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/UPDATE/System/Cache/System/COMPATABLE',
            stream=True,
        )
        v = response.content
        version = v.decode('utf-8')

        vr = open(f'{SourceDirectory}temp', 'w')
        vr.write(version)
        vr.close()
        vr2 = open(f'{SourceDirectory}temp', 'r')
        vrl = vr2.read()

        print('-----------------')
        print('version status')
        print(version.split('\n'))
        print('-----------------')
        cont = True
        print(version)
        for version in version.split('\n'):
            if cont is True:
                if version in str(CurrentVersion):

                    print(f'{version} in {CurrentVersion}')
                    print('Update Is Present')
                    e3 = input('Press enter to Confirm update [0 to cancel]: ')
                    if '0' in e3:
                        print('Operation frozen')
                        pass
                    else:
                        dl()
                        cont = False
                else:
                    print(
                        f'Version {CurrentVersion}, is either already updated or is not recent enough to be compatible'
                    )

        vr = open(f'{SourceDirectory}temp', 'w')
    except:
        vr = open(f'{SourceDirectory}temp', 'w')
        print('User IsNot Connected To Internet')
except:
    print('sorry!')
    print('You already have this version')
