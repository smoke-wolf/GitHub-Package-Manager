#

import os


def All():
    import User.UserProfile

    os.chdir(User.UserProfile.SourceDirectory)
    cwd = os.getcwd()

    spacer = '===================================================='

    print('=================Available_Packages=================')
    print('Local : 1')
    print('GitHub : 2')
    inp = None
    inp = int(input('Enter value to continue: '))

    if inp == 2:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Inp = GitHub', Pol=1)

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
            EV.NewEvent(event='Input Error', Pol=1)

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
                EV.NewEvent(event=f'DirRemoval = Success! {co}', Pol=0)

            except:
                print('Project Failed To Removed')
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'DirRemoval = Failed ', Pol=0)

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

            EV.NewEvent(event=f'Removing Directory: {cc}', Pol=0)
            try:
                import System.Drive.Errors_Events.EventMan as EV
                import shutil

                shutil.rmtree(
                    f'{os.getcwd()}/System/.Cache/System/GitHub/Downloads{co}'
                )

                import System.Drive.Errors_Events.EventMan as EV

                print('Project Removed')
                EV.NewEvent(event=f'DirRemoval = Success! ', Pol=0)

            except:
                print('Project Failed To Removed')
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'DirRemoval = Failed ', Pol=0)

    elif inp == 1:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Inp = Local', Pol=1)

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
                EV.NewEvent(event=f'valuee ={valuee}', Pol=1)
                try:
                    valuee = int(valuee)
                except:
                    EV.NewEvent(event=f'Input error', Pol=1)

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

                    EV.NewEvent(event=f'Launch Command Removed', Pol=0)

                except:
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(
                        event=f'Launch Command Failed To Remove', Pol=0
                    )

                try:
                    value1 = value.split(f'-', 1)[0]
                    Str = value1[: len(value1) - 1]
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Success: {Str}', Pol=0)
                except:
                    value1 = value.split(f'@', 1)[0]
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Failure: {value1}', Pol=1)

                try:
                    try:
                        import System.Drive.Errors_Events.EventMan as EV

                        # Remove all characters before the character '-' from string
                        listOfWords = value1.split('"', 1)
                        if len(listOfWords) > 0:
                            v = listOfWords[1]
                            EV.NewEvent(
                                event=f'Attempting [!]{v[1:-1]}[!]', Pol=0
                            )
                            import shutil

                            shutil.rmtree(v[1:-1])
                            EV.NewEvent(
                                event=f'Directory Removed [!]{v[1:-1]}[!]',
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
                                event=f'Attempting [!]{v[:-4]}[!]', Pol=0
                            )
                            import shutil

                            shutil.rmtree(v[:-1])
                            shutil.rmtree(v[:-4])
                            EV.NewEvent(
                                event=f'Directory Removed [!]{v[:-4]}[!]',
                                Pol=0,
                            )
                            print('Project Removed')
                except:
                    print('Project Failed To Remove')
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Dir Removal Canceled', Pol=0)
