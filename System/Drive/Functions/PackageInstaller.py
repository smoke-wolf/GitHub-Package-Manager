# import System.Drive.Functions.PackageInstaller
# exec('System.Drive.Functions.PackageInstaller')
global launch


def main():
    print(
        f"""
=================package_installer==================
1 = From GitHub repo: 
====================================================
2 = From Local Folder
===================================================="""
    )
    Route = input('Enter Value To Continue: ')

    spacer = '===================================================='

    if Route == '1':
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Install @GitRepo', Pol=1)

        import os

        cwd = os.getcwd()
        try:
            os.mkdir(f'{cwd}/System/Cache/System/GitHub/Downloads')

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(
                event=f'{cwd}/System/Cache/System/GitHub/Downloads : Created',
                Pol=0,
            )
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

        try:  # downloading from GitHub
            os.system(f"git clone '{Download_Source}'")
            print(os.getcwd())
            print('[!] CheckPoint 2|4 [!]')
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Downloaded from Github', Pol=0)
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
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Package Downloaded: {x}', Pol=0)

            for y in SDir1:
                if y in SDir:
                    pass
                else:
                    print('[!] CheckPoint 3|4 [!]')
                    dir1 = f'{cwd}/System/Cache/System/GitHub/Downloads/{y}'

                    ChangeDir = dir1

                    Files0 = []
                    for path in os.listdir(dir1):
                        # check if current path is a file
                        if os.path.isfile(os.path.join(dir1, path)):
                            Files0.append(path)

                    print(spacer)
                    print(f"""Files Downloaded:""")
                    print('0 -> Complex Install')

                    counter = 0
                    for file in Files0:
                        counter += 1
                        print(f'{counter}:{file}')
                    print(spacer)
                    fi = input('Enter launch file number: ')
                    if fi == '0':
                        Launch = input('Launch command: ')
                        print('Requirements command: leave blank for none')
                        Req = input('Requirements Command: ')
                        print('Privileges argument: leave black for none ')
                        Priv = input('Privileges argument: ')
                        print('Install command: ')
                        In1 = input('Install command (1): ')
                        In2 = input(
                            'Install command (2) leave black for none: '
                        )
                        In3 = input(
                            'Install command (3) leave black for none: '
                        )

                        print('Starting Install: [1/2]')

                        try:
                            os.system(Req)
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(
                                event=f'Requirements Downloaded With: {Req}',
                                Pol=0,
                            )

                        except:
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(
                                event=f'Requirements did not download', Pol=0
                            )
                        print('Install: [2/2]')

                        tool = f'{Priv} {dir1}\n{In1}\n{In2}\n{In3}'

                        ComplexLcaunch = open(
                            f'{cwd}/System/Cache/System/GitHub/Complex', 'a'
                        )
                        ComplexLcaunch.write(f'\n{dir1}${Launch}')
                        Complexinstall = open(
                            f'{cwd}/System/Cache/System/GitHub/Complex_install',
                            'a',
                        )
                        Complexinstall.write(tool)
                        ComplexLcaunch.close()

                        print('Fully installed!')

                    else:
                        fi = Files0[int(fi) - 1]

                        dashID = [
                            'Requests.txt',
                            'Requirements.txt',
                            'requests.txt',
                            'Requirements.txt',
                        ]
                        try:
                            for dash in dashID:
                                if dash in Files0:
                                    dash = f'{dir1}/{dash}'
                                    dash1 = f'python3 -m pip install -r {dash}'
                                    try:
                                        os.system(dash1)
                                        print('Requirements Installed')
                                    except:
                                        pass
                        except:
                            print('No Requirements found')

                        ch = '.'
                        # Remove all characters before the character '-' from string
                        listOfWords = fi.split(ch, 1)
                        if len(listOfWords) > 0:
                            ffi = listOfWords[1]

                        if ffi == 'py':
                            launch = f'&python3 {fi}'

                            tier = f'&python3 {dir1}/{fi}'
                            print('[!] CheckPoint 4|4 [!]')
                            print(launch)
                            Form = f'{ChangeDir}@{fi[:-3]} = {launch}'
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(
                                event=f'Launch Command Created: {Form}', Pol=0
                            )
                            os.chdir(Source)
                            cwdd = os.getcwd()
                            f = open(
                                f'{cwdd}/System/Cache/System/GitHub/Int.txt',
                                'a',
                            )
                            f.write(f'\n{Form}')
                            f.close()
                            print('Installation Complete!')

                        elif ffi == 'c':
                            launch = f'&gcc {fi}'

                            print('[!] CheckPoint 4|4 [!]')
                            print(launch)
                            Form = f'{ChangeDir}@{fi[:-3]} = {launch}'
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(
                                event=f'Launch Command Created: {Form}', Pol=0
                            )
                            os.chdir(Source)
                            cwdd = os.getcwd()
                            f = open(
                                f'{cwdd}/System/Cache/System/GitHub/Int.txt',
                                'a',
                            )
                            f.write(f'\n{Form}')
                            f.close()
                            print('Installation Complete!')

                        elif ffi == 'cpp':
                            launch = f'&g++ {fi}'

                            print('[!] CheckPoint 4|4 [!]')
                            print(launch)
                            Form = f'{ChangeDir}@{fi[:-3]} = {launch}'
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(
                                event=f'Launch Command Created: {Form}', Pol=0
                            )
                            os.chdir(Source)
                            cwdd = os.getcwd()
                            f = open(
                                f'{cwdd}/System/Cache/System/GitHub/Int.txt',
                                'a',
                            )
                            f.write(f'\n{Form}')
                            f.close()
                            print('Installation Complete!')

                        elif ffi == 'sh':
                            launch = f'&bash {fi}'

                            print('[!] CheckPoint 4|4 [!]')
                            print(launch)
                            Form = f'{ChangeDir}@{fi[:-3]} = {launch}'
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(
                                event=f'Launch Command Created: {Form}', Pol=0
                            )
                            os.chdir(Source)
                            cwdd = os.getcwd()
                            f = open(
                                f'{cwdd}/System/Cache/System/GitHub/Int.txt',
                                'a',
                            )
                            f.write(f'\n{Form}')
                            f.close()
                            print('Installation Complete!')

        except:
            print('Something went wrong, cleaning up.')
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Installation Error', Pol=0)
        import User

        os.chdir(User.UserProfile.SourceDirectory)
    elif Route == '2':
        import os

        cwd = os.getcwd()
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Imported @Local', Pol=1)

        ImportDirectory = input('please give the import directory: ')

        Files0 = []
        for path in os.listdir(ImportDirectory):
            # check if current path is a file
            if os.path.isfile(os.path.join(ImportDirectory, path)):
                Files0.append(path)
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Files Connected', Pol=0)

        print(spacer)
        print(f"""Files Connected: """)

        counter = 0
        for file in Files0:
            counter += 1
            print(f'{counter} | {file}')

        print(spacer)
        fi = input('Enter launch file number: ')

        fi = Files0[int(fi) - 1]
        # Remove all characters before the character '-' from string
        fe = fi.split('.', 1)
        if len(fe) > 0:
            ffi = fe[1]

        if 'py' in ffi:
            p1 = f'+{ImportDirectory} -python3 {ImportDirectory}/{fi}*'
        if ffi == '.c':
            p1 = f'+{ImportDirectory} -gcc {ImportDirectory}/{fi}*'
        elif 'cpp' in ffi:
            p1 = f'+{ImportDirectory} -gpp {ImportDirectory}/{fi}*'
        elif 'sh' in ffi:
            p1 = f'+{ImportDirectory} -bash {ImportDirectory}/{fi}*'

        print('[!] CheckPoint 4|4 [!]')

        Form = f'{fi[:-3]} = "{p1}"'
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Launch Command Complete: {Form}', Pol=0)

        f = open(f'{cwd}/System/Cache/System/Local/Int.txt', 'a')
        f.write(f'\n{Form}')
        f.close()
        import User

        print('Installation Complete!')
        os.chdir(User.UserProfile.SourceDirectory)
