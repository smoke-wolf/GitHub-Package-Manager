import os
import sys


def All():
    cwd = os.getcwd()

    spacer = """===================================================="""

    print('=================Available_Packages=================')
    print('GitHub : 1')
    print('Local : 2')
    print('GitHub-Complex : 3')
    inp = None
    inp = input('Enter value to continue: ')

    try:
        inp = int(inp)
    except:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'input error', Pol=1)

    if inp == 1:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Inp = GitHub', Pol=1)

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
                valuee = input('Enter a value to continue: ')
                value = lines[int(valuee) - 1]
                cc = value
                listOfWords = value.split('&', 1)
                if len(listOfWords) > 0:
                    value = listOfWords[1]

                value = value.split('-', 1)[0]

                cc = cc.split('@', 1)[0]
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'Change Directory: {cc} ', Pol=0)
                try:
                    os.chdir(cc)
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'DirChange = Success! ', Pol=0)
                    EV.NewEvent(
                        event=f'os executed command [!]{value.split("%", 1)[0]}[!] ', Pol=0
                    )
                    try:
                        value = value.split('%', 1)[0]
                        os.system(f'{value}')
                        sys.exit(0)
                    except:
                        print('1 : Purposeful exit')
                        print(spacer)
                        print('2 : Program error')
                        inpo = input('Enter a value: ')
                        if inpo == '1':
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(event=f'Program exited by user', Pol=1)
                        elif inpo == '2':
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(
                                event=f'Program exited by system', Pol=0
                            )

                except:
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'DirChange = Failed ', Pol=0)

    elif inp == 2:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Inp = Local', Pol=1)

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

                EV.NewEvent(event=f'{count1}={count}', Pol=0)
                valuee = input('Enter a value to continue: ')
                value = lines[int(valuee) - 1]
                listOfWords = value.split('-', 1)
                if len(listOfWords) > 0:
                    valueg = listOfWords[1]

                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'Creating value1', Pol=0)
                try:
                    value1 = value.split(f'@', 1)[0]
                    Str = value1[: len(value1) - 1]
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Success: {Str}', Pol=0)
                except:
                    value1 = value.split(f'@', 1)[0]
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Failure: {value1}', Pol=1)

                try:
                    os.system(f'{valueg}')

                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(
                        event=f'Directory changed [!]{value1}[!]', Pol=0
                    )

                except:
                    print('os error')

                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Dir Change Canceled', Pol=0)

                listOfWords = value.split('-', 1)
                if len(listOfWords) > 0:
                    value = listOfWords[1]

                value = value.split('*', 1)[0]

                try:
                    os.system(f'{value}')

                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Command Executed [!]{value}[!]', Pol=0)
                except:
                    import User.UserProfile

                    os.chdir(User.UserProfile.SourceDirectory)
                    print('1 : Purposeful exit')
                    print(spacer)
                    print('2 : Program error')
                    inpo = input('Enter a value: ')
                    if inpo == '1':
                        import System.Drive.Errors_Events.EventMan as EV

                        EV.NewEvent(event=f'Program exited by user', Pol=1)
                    elif inpo == '2':
                        import System.Drive.Errors_Events.EventMan as EV

                        EV.NewEvent(event=f'Program exited by system', Pol=0)

    if inp == 3:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Inp = GitHub_complex', Pol=1)

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

                            EV.NewEvent(event=f'Command {line}', Pol=0)
                            os.system(line)
                        except:
                            import System.Drive.Errors_Events.EventMan as EV

                            EV.NewEvent(event=f'Command failed ', Pol=0)
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

                    EV.NewEvent(event=f'Launch Success! ', Pol=0)
                    EV.NewEvent(event=f'os executed command [!]{A}[!] ', Pol=0)
                    sys.exit(0)
                except:
                    import User.UserProfile

                    os.chdir(User.UserProfile.SourceDirectory)
                    print('1 : Purposeful exit')
                    print(spacer)
                    print('2 : Program error')
                    inpo = input('Enter a value: ')
                    if inpo == '1':
                        import System.Drive.Errors_Events.EventMan as EV

                        EV.NewEvent(event=f'Program exited by user', Pol=1)
                    elif inpo == '2':
                        import System.Drive.Errors_Events.EventMan as EV

                        EV.NewEvent(event=f'Program exited by system', Pol=0)
            else:
                pass
