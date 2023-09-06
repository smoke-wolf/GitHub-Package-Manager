import pty
import subprocess
import sys
import os
import threading
import time

# HIII
args = sys.argv


def Main():
    spacer = '===================================================='
    import User.UserProfile

    cwd = User.UserProfile.SourceDirectory
    import sys
    import os

    args = sys.argv

    # Install arguments
    if args[1] == '-I':  # Intalling through Git takes 2 arguments
        try:
            Repo = args[2]
        except:
            print('Lacking Repository URL')



        spacer = '===================================================='

        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Install @GitRepo --COMMAND LINE', Pol=0)

        import os

        cwd = os.getcwd()
        try:
            os.mkdir(f'{cwd}/System/.Cache/System/GitHub/Downloads')

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(
                event=f'{cwd}/System/.Cache/System/GitHub/Downloads : Created --COMMAND LINE',
                Pol=0,
            )
        except:
            pass
        Source = cwd
        print(spacer)
        Download_Source = Repo

        if args[2] == '-H':
            dir = f'{cwd}/System/.Cache/System/Local/download'
            os.chdir(dir)
            os.system(f"git clone '{args[3]}'")
        else:
            dir = f'{cwd}/System/.Cache/System/GitHub/Downloads'
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

                print('[!] CheckPoint 2|4 [!]')
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'Downloaded from Github --COMMAND LINE', Pol=0)
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

                        EV.NewEvent(
                            event=f'Package Downloaded: {x} --COMMAND LINE', Pol=0
                        )

                for y in SDir1:
                    if y in SDir:
                        pass
                    else:
                        print('[!] CheckPoint 3|4 [!]')
                        dir1 = f'{cwd}/System/.Cache/System/GitHub/Downloads/{y}'

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
                                    event=f'Requirements Downloaded With: {Req}--COMMAND LINE',
                                    Pol=0,
                                )

                            except:
                                import System.Drive.Errors_Events.EventMan as EV

                                EV.NewEvent(
                                    event=f'Requirements did not download--COMMAND LINE',
                                    Pol=0,
                                )
                            print('Install: [2/2]')

                            tool = f'{Priv} {dir1}\n{In1}\n{In2}\n{In3}'

                            ComplexLcaunch = open(
                                f'{cwd}/System/.Cache/System/GitHub/Complex', 'a'
                            )
                            ComplexLcaunch.write(f'\n{dir1}${Launch}')
                            Complexinstall = open(
                                f'{cwd}/System/.Cache/System/GitHub/Complex_install',
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
                                    event=f'Launch Command Created: {Form} --COMMAND LINE',
                                    Pol=0,
                                )
                                os.chdir(Source)
                                cwdd = os.getcwd()
                                f = open(
                                    f'{cwdd}/System/.Cache/System/GitHub/Int.txt',
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
                                    event=f'Launch Command Created: {Form} --COMMAND LINE',
                                    Pol=0,
                                )
                                os.chdir(Source)
                                cwdd = os.getcwd()
                                f = open(
                                    f'{cwdd}/System/.Cache/System/GitHub/Int.txt',
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
                                    event=f'Launch Command Created: {Form} --COMMAND LINE',
                                    Pol=0,
                                )
                                os.chdir(Source)
                                cwdd = os.getcwd()
                                f = open(
                                    f'{cwdd}/System/.Cache/System/GitHub/Int.txt',
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
                                    event=f'Launch Command Created: {Form} --COMMAND LINE',
                                    Pol=0,
                                )
                                os.chdir(Source)
                                cwdd = os.getcwd()
                                f = open(
                                    f'{cwdd}/System/.Cache/System/GitHub/Int.txt',
                                    'a',
                                )
                                f.write(f'\n{Form}')
                                f.close()
                                print('Installation Complete!')
            except:
                pass  #

    elif args[1] == '-IL':
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Imported @Local --COMMAND LINE', Pol=0)

        ImportDirectory = args[2]

        Files0 = []
        for path in os.listdir(ImportDirectory):
            # check if current path is a file
            if os.path.isfile(os.path.join(ImportDirectory, path)):
                Files0.append(path)
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Files Connected --COMMAND LINE', Pol=0)

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

        EV.NewEvent(
            event=f'Launch Command Complete: {Form} --COMMAND LINE', Pol=0
        )

        f = open(f'{cwd}/System/.Cache/System/Local/Int.txt', 'a')
        f.write(f'\n{Form}')
        f.close()
        import User

        print('Installation Complete!')
        os.chdir(User.UserProfile.SourceDirectory)

    # Listing arguments & Activate
    elif args[1] == '-LA':  # list all
        spacer = '===================================================='

        print(
            """   Local!
    ===================================================="""
        )
        try:
            with open(
                f'{cwd}/System/.Cache/System/Local/Int.txt', 'r'
            ) as r, open(
                f'{cwd}/System/.Cache/System/Local/Int2.txt', 'w'
            ) as o:
                for line in r:
                    if line.strip():
                        o.write(line)
            f = open(f'{cwd}/System/.Cache/System/Local/Int2.txt', 'r')

            lines = f.readlines()
            count = 0
            for line in lines:
                count += 1

            count1 = 0
            for line in lines:
                count1 += 1
                print('{} | {}'.format(count1, line.strip()))
                print(spacer)
        except:
            print('None Found')

        with open(f'{cwd}/System/.Cache/System/GitHub/int.txt', 'r') as r, open(
            f'{cwd}/System/.Cache/System/GitHub/int2.txt', 'w'
        ) as o:
            for line in r:
                if line.strip():
                    o.write(line)

        f = open(f'{cwd}/System/.Cache/System/GitHub/int2.txt', 'r')

        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1

        count1 = 0

        print(
            """   Github   
    ===================================================="""
        )
        try:
            for line in lines:
                value4 = line.strip()
                Val = value4.split('&', 1)
                if len(Val) > 0:
                    value4 = Val[1]
                count1 += 1

                print('{} | {}'.format(count1, value4))
                print(spacer)
                if count is None:
                    print('No Packages Yet')
                else:
                    pass
        except:
            print('None found')

        print(
            """   Advanced
    ===================================================="""
        )

        spacer = '===================================================='

        with open(f'{cwd}/System/.Cache/System/GitHub/Complex', 'r') as r, open(
            f'{cwd}/System/.Cache/System/GitHub/Complex2', 'w'
        ) as o:
            for line in r:
                if line.strip():
                    o.write(line)

        f = open(f'{cwd}/System/.Cache/System/GitHub/Complex2', 'r')

        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1

        try:
            count1 = 0
            for line in lines:
                value4 = line.strip()
                Val = value4.split('&', 1)
                if len(Val) > 0:
                    value4 = Val[1]
                count1 += 1
                print('{} | {}'.format(count1, value4))
                print(spacer)
        except:
            print('None Found')

    elif args[1] == '-LL':  # list local
        import System.Drive.Errors_Events.EventMan as EV

        with open(f'{cwd}/System/.Cache/System/Local/Int.txt', 'r') as r, open(
            f'{cwd}/System/.Cache/System/Local/Int2.txt', 'w'
        ) as o:
            for line in r:
                if line.strip():
                    o.write(line)
        f = open(f'{cwd}/System/.Cache/System/Local/Int2.txt', 'r')

        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1

        count1 = 0
        for line in lines:
            count1 += 1
            print('{} | {}'.format(count1, line.strip()))
            print(spacer)
            if count1 == count:
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'{count1}={count} --COMMAND LINE', Pol=0)
                valuee = args[2]

                value = lines[int(valuee) - 1]
                listOfWords = value.split('≈', 1)
                if len(listOfWords) > 0:
                    valueg = listOfWords[1]
                    LaunchCommand = valueg[:-2]

                value1 = value.split(f'@', 1)[0]

                listOfWords = value.split('+', 1)
                if len(listOfWords) > 0:
                    dir = listOfWords[1]

                dir = dir.split('≈', 1)[0]


                try:
                    EV.NewEvent(
                        event=f'cd {dir} && {LaunchCommand}',
                        Pol=0,
                    )
                    print('\n'*100)
                    subshell = LaunchCommand.split(' ')
                    subshell = subshell[0]
                    entrypoint = LaunchCommand.split('/')

                    # Get the last part
                    entrypoint = entrypoint[-1]
                    print(f'''


█▀▀ █░█ █▀█ █▀▄▀█   █░░ █▀█ █▀▀ ▄▀█ █░░   █▀ █░█ █▀▀ █░░ █░░ ▀
█▄█ █▀█ █▀▀ █░▀░█   █▄▄ █▄█ █▄▄ █▀█ █▄▄   ▄█ █▀█ ██▄ █▄▄ █▄▄ ▄ 
========================================================================================================================
Is Alive: \033[91m True \033[0m  ||     Entrypoint File: \033[91m{entrypoint}\033[0m ||       Current SubShell: \033[91m{subshell}\033[0m 
Shell Directory: \033[91m{dir}\033[0m  
========================================================================================================================
''')
                    try:
                        start_time = time.time()
                        LaunchCommand2 = f'''cd {dir} && {LaunchCommand}'''

                        os.system(LaunchCommand2)

                        sys.exit(0)

                    except:
                        end_time = time.time()  # Record the end time when the exception is raised
                        elapsed_time = end_time - start_time  # Calculate the elapsed time
                        print(f'''
========================================================================================================================
Shell Quit After \033[91m{elapsed_time:.2f}\033[0m seconds 
''')




                except:
                    print('os error')

                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(
                        event=f'Dir Change Canceled --COMMAND LINE', Pol=0
                    )



    elif args[1] == '-LG':  # list git
        spacer = '===================================================='


        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Inp = GitHub --COMMAND LINE', Pol=0)

        with open(f'{cwd}/System/.Cache/System/GitHub/int.txt', 'r') as r, open(
            f'{cwd}/System/.Cache/System/GitHub/int2.txt', 'w'
        ) as o:
            for line in r:
                if line.strip():
                    o.write(line)

        f = open(f'{cwd}/System/.Cache/System/GitHub/int2.txt', 'r')

        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1

        count1 = 0
        for line in lines:
            value4 = line.strip()
            Val = value4.split('&', 1)
            if len(Val) > 0:
                value4 = Val[1]
            count1 += 1

            print('{} | {}'.format(count1, value4))
            print(spacer)
            if count is None:
                print('No Packages Yet')
            else:
                pass

            if count1 == count:
                valuee = args[2]
                value = lines[int(valuee) - 1]
                cc = value
                listOfWords = value.split('&', 1)
                if len(listOfWords) > 0:
                    value = listOfWords[1]

                value = value.split('≈', 1)[0]

                cc = cc.split('@', 1)[0]

                value = value.split("%", 1)[0]
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(
                    event=f'Change Directory: {cc}  --COMMAND LINE', Pol=0
                )
                try:
                    os.chdir(cc)
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(
                        event=f'DirChange = Success! --COMMAND LINE', Pol=0
                    )
                    EV.NewEvent(
                        event=f'os executed command [!]{value}[!] --COMMAND LINE',
                        Pol=0,
                    )
                    try:
                        os.system(f'{value}')
                        sys.exit(0)
                    except:
                        pass
                    EV.NewEvent(event='Program ended', Pol=0)
                except:
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(
                        event=f'DirChange = Failed --COMMAND LINE', Pol=0
                    )

    elif args[1] == '-LC':
        spacer = '===================================================='
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Inp = GitHub_complex --COMMAND LINE', Pol=0)

        with open(f'{cwd}/System/.Cache/System/GitHub/Complex', 'r') as r, open(
            f'{cwd}/System/.Cache/System/GitHub/Complex2', 'w'
        ) as o:
            for line in r:
                if line.strip():
                    o.write(line)

        f = open(f'{cwd}/System/.Cache/System/GitHub/Complex2', 'r')

        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1

        count1 = 0
        for line in lines:
            value4 = line.strip()
            Val = value4.split('&', 1)
            if len(Val) > 0:
                value4 = Val[1]
            count1 += 1
            print('{} | {}'.format(count1, value4))
            print(spacer)

            if count1 == count:
                valuee = input('Enter a value to continue: ')
                value = lines[int(valuee) - 1]

                Arges = input('Any Launch Arguments: ')
                B = value.split('$', 1)[0]

                # Remove all characters before the character '-' from string
                lis = value.split('$', 1)
                if len(lis) > 0:
                    lis = lis[1]

                A = f'{lis} {Arges}'

                os.chdir(B)
                print('Directory changed')

                r = open(
                    f'{cwd}/System/.Cache/System/GitHub/Complex_install', 'r'
                )
                lines = r.readlines()
                try:
                    for line in lines:
                        try:
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(
                                event=f'Command {line} --COMMAND LINE', Pol=0
                            )
                            os.system(line)
                        except:
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(
                                event=f'Command failed --COMMAND LINE', Pol=0
                            )
                            exit(0)

                    open(
                        f'{cwd}/System/.Cache/System/GitHub/Complex_install',
                        'w',
                    )

                except:
                    pass

                try:
                    os.system(A)
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Launch Success! --COMMAND LINE', Pol=0)
                    EV.NewEvent(
                        event=f'os executed command [!]{A}[!] --COMMAND LINE',
                        Pol=0,
                    )
                    sys.exit(0)
                except:
                    EV.NewEvent(event='Program exited --COMMAND LINE', Pol=0)
                    pass
            else:
                pass

    #   Uninstalling
    elif args[1] == '-UG':
        spacer = '===================================================='
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Inp = GitHub --COMMAND LINE', Pol=0)

        with open(f'{cwd}/System/.Cache/System/GitHub/int.txt', 'r') as r, open(
            f'{cwd}/System/.Cache/System/GitHub/int2.txt', 'w'
        ) as o:
            for line in r:
                if line.strip():
                    o.write(line)

        f = open(f'{cwd}/System/.Cache/System/GitHub/int2.txt', 'r')
        e = open(f'{cwd}/System/.Cache/System/GitHub/Complex2', 'r')
        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1

        count1 = 0
        for line in lines:
            value4 = line.strip()
            Val = value4.split('&', 1)
            if len(Val) > 0:
                value4 = Val[1]
            count1 += 1

            print('{} | {}'.format(count1, value4))
            print(spacer)

        lines2 = e.readlines()
        for line2 in lines2:
            count1 += 1
            print('{} | {}'.format(count1, line2))

        valuee = input('Enter a value to continue: ')
        # remove a line containing a string

        try:
            valuee = int(valuee)
        except:
            EV.NewEvent(event='Input Error --COMMAND LINE', Pol=0)

        if valuee > count:
            dr = int(valuee) - count
            command = lines2[dr - 1]
            print(command)
            co = command.split('$', 1)[0]
            print(co)
            try:
                import System.Drive.Errors_Events.EventMan as EV
                import shutil

                shutil.rmtree(co)

                import System.Drive.Errors_Events.EventMan as EV

                print(f'Project Removed {co}')
                EV.NewEvent(
                    event=f'DirRemoval = Success! --COMMAND LINE', Pol=0
                )

            except:
                print('Project Failed To Removed')
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'DirRemoval = Failed --COMMAND LINE', Pol=0)

        else:
            with open(
                f'{cwd}/System/.Cache/System/GitHub/int.txt', 'r'
            ) as file:
                lines5 = file.readlines()

            with open(
                f'{cwd}/System/.Cache/System/GitHub/int.txt', 'w'
            ) as file:
                for linef in lines5:
                    # find() returns -1 if no match is found
                    if linef.find(value4) != -1:
                        pass
                    else:
                        file.write(linef)

            value = lines[int(valuee) - 1]
            cc = value
            listOfWords = value.split('&', 1)
            if len(listOfWords) > 0:
                value = listOfWords[1]

            value = value.split('-', 1)[0]

            cc = cc.split('@', 1)[0]

            listOfWords = cc.split('/Downloads', 1)

            if len(listOfWords) > 0:
                co = listOfWords[1]

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(
                event=f'Removing Directory: {cc} --COMMAND LINE', Pol=0
            )
            try:
                import System.Drive.Errors_Events.EventMan as EV
                import shutil

                shutil.rmtree(
                    f'{os.getcwd()}/System/.Cache/System/GitHub/Downloads{co}'
                )

                import System.Drive.Errors_Events.EventMan as EV

                print('Project Removed')
                EV.NewEvent(
                    event=f'DirRemoval = Success! --COMMAND LINE', Pol=0
                )

            except:
                print('Project Failed To Removed')
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'DirRemoval = Failed --COMMAND LINE', Pol=0)

    elif args[1] == '-UL':
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Inp = Local --COMMAND LINE', Pol=0)

        f = open(f'{cwd}/System/.Cache/System/Local/Int2.txt', 'r')

        with open(f'{cwd}/System/.Cache/System/Local/Int.txt', 'r') as r, open(
            f'{cwd}/System/.Cache/System/Local/Int2.txt', 'w'
        ) as o:
            for line in r:
                if line.strip():
                    o.write(line)
        f = open(f'{cwd}/System/.Cache/System/Local/Int2.txt', 'r')

        lines = f.readlines()
        count = 0
        for line in lines:
            count += 1

        count1 = 0
        for line in lines:
            count1 += 1
            print('{} | {}'.format(count1, line.strip()))
            print(spacer)
            if count1 == count:
                import System.Drive.Errors_Events.EventMan as EV

                valuee = input('Enter a value to continue: ')
                EV.NewEvent(event=f'valuee ={valuee} --COMMAND LINE', Pol=0)
                try:
                    valuee = int(valuee)
                except:
                    EV.NewEvent(event=f'Input error --COMMAND LINE', Pol=0)

                value = lines[valuee - 1]
                listOfWords = value.split('-', 1)

                if len(listOfWords) > 0:
                    valueg = listOfWords[1]

                with open(
                    f'{cwd}/System/.Cache/System/Local/Int.txt', 'r'
                ) as file:
                    lines55 = file.readlines()
                try:
                    with open(
                        f'{cwd}/System/.Cache/System/Local/Int.txt', 'w'
                    ) as file:
                        for lineff in lines55:
                            if lineff.find(value) != -1:
                                pass
                            else:
                                file.write(lineff)
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(
                        event=f'Launch Command Removed --COMMAND LINE', Pol=0
                    )

                except:
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(
                        event=f'Launch Command Failed To Remove --COMMAND LINE',
                        Pol=0,
                    )

                try:
                    value1 = value.split(f'-', 1)[0]
                    Str = value1[: len(value1) - 1]
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Success: {Str} --COMMAND LINE', Pol=0)
                except:
                    value1 = value.split(f'@', 1)[0]
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(
                        event=f'Failure: {value1} --COMMAND LINE', Pol=0
                    )

                try:
                    try:
                        import System.Drive.Errors_Events.EventMan as EV

                        # Remove all characters before the character '-' from string
                        listOfWords = value1.split('"', 1)
                        if len(listOfWords) > 0:
                            v = listOfWords[1]
                            EV.NewEvent(
                                event=f'Attempting [!]{v[1:-1]}[!] --COMMAND LINE',
                                Pol=0,
                            )
                            import shutil

                            shutil.rmtree(v[1:-1])
                            EV.NewEvent(
                                event=f'Directory Removed [!]{v[1:-1]}[!] --COMMAND LINE',
                                Pol=0,
                            )
                            print('Project Removed')
                    except:
                        import System.Drive.Errors_Events.EventMan as EV

                        # Remove all characters before the character '-' from string
                        listOfWords = value1.split('+', 1)
                        if len(listOfWords) > 0:
                            v = listOfWords[1]
                            EV.NewEvent(
                                event=f'Attempting [!]{v[:-4]}[!] --COMMAND LINE',
                                Pol=0,
                            )
                            import shutil

                            shutil.rmtree(v[:-1])
                            shutil.rmtree(v[:-4])
                            EV.NewEvent(
                                event=f'Directory Removed [!]{v[:-4]}[!] --COMMAND LINE',
                                Pol=0,
                            )
                            print('Project Removed')
                except:
                    print('Project Failed To Remove')
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(
                        event=f'Dir Removal Canceled --COMMAND LINE', Pol=0
                    )

    else:
        print(
            """
        Help
        ====
        -I -> Install (arg<repo>)
        -IL -> Install Local (arg<dir>)

        -LA -> List All Installs
        -LL -> Launch Local Directory
        -LG -> Launch Git Project
        -LC -> Launch Advanced Projects

        -UG -> Uninstall GitHub Projects
        -UL -> Uninstall Local directories
        """
        )


try:
    ct = args[1]
    Main()
except:
    pass
