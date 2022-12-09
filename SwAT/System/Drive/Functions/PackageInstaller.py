
#import System.Drive.Functions.PackageInstaller
#exec('System.Drive.Functions.PackageInstaller')


print(f'''
=================package_installer==================
1 = From GitHub repo: 
====================================================
2 = From Local Folder
====================================================''')
Route = input('Enter Value To Continue: ')

spacer = '===================================================='

if Route == '1':

    import os
    cwd = os.getcwd()
    try:
        os.mkdir(f'{cwd}/System/Cache/System/GitHub/Downloads')
    except:
        pass
    Source = cwd
    print(spacer)
    Download_Source = input('GitHub Repo To Download From: ')
    dir = f'{cwd}/System/Cache/System/GitHub/Downloads'
    os.chdir(dir)
    print('[!] CheckPoint 1|4 [!]')

    Files = []
    for path in os.listdir(cwd):
        # check if current path is a file
        if os.path.isfile(os.path.join(cwd, path)):
            Files.append(path)

    SDir = list(filter(os.path.isdir, os.listdir(os.curdir)))

    try:    # downloading from GitHub
        os.system(f"git clone '{Download_Source}'")

        print('[!] CheckPoint 2|4 [!]')
        Files1 = []
        for path in os.listdir(cwd):
            # check if current path is a file
            if os.path.isfile(os.path.join(cwd, path)):
                Files1.append(path)

        SDir1 = list(filter(os.path.isdir, os.listdir(os.curdir)))

        for x in Files1:
            if x in Files:
                pass
            else:
                print(x)

        for y in SDir1:
            if y in SDir:
                pass
            else:
                print(y)
                print('[!] CheckPoint 3|4 [!]')
                dir1 = f'{cwd}/System/Cache/System/GitHub/Downloads/{y}'

                Files0 = []
                for path in os.listdir(dir1):
                    # check if current path is a file
                    if os.path.isfile(os.path.join(dir1, path)):
                        Files0.append(path)

                print(spacer)
                print(f'''Files Downloaded:''')

                counter = 0
                for file in Files0:
                    counter += 1
                    print(f'{counter}:{file}')
                print(spacer)
                fi = input('Enter launch file number: ')

                fi = Files0[int(fi)-1]

                launch = f'+python3 {dir1}/{fi}-'
                print('[!] CheckPoint 4|4 [!]')

                print(launch)
                Form = f'{fi[:-3]} = "{launch}"'

                os.chdir(Source)
                cwdd = os.getcwd()
                f = open(f'{cwdd}/System/Cache/System/GitHub/Int.py', 'a')
                f.write(f'\n{Form}')
                f.close()
                print('Installation Complete!')
    except:
        print('Something went wrong, cleaning up.')
elif Route == '2':
    import os
    cwd =os.getcwd()

    ImportDirectory = input('please give the import directory: ')

    Files0 = []
    for path in os.listdir(ImportDirectory):
        # check if current path is a file
        if os.path.isfile(os.path.join(ImportDirectory, path)):
            Files0.append(path)

    print(spacer)
    print(f'''Files Connected: ''')

    counter = 0
    for file in Files0:
        counter += 1
        print(f'{counter} | {file}')

    print(spacer)
    fi = input('Enter launch file number: ')

    fi = Files0[int(fi) - 1]

    p1 = f'+cd {ImportDirectory}-python3 {ImportDirectory}/{fi}*'

    print('[!] CheckPoint 4|4 [!]')

    Form = f'{fi[:-3]} = "{p1}"'

    f = open(f'{cwd}/System/Cache/System/Local/Int.py', 'a')
    f.write(f'\n{Form}')
    f.close()
    print('Installation Complete!')


