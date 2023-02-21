print(
    """\n|  |                |============Cache===========|
|  |                |1 | Remove All Git Downloads|
|  |                |2 | Reset Events / Log      |
|  |                |3 | Reset All To Defaults   |
|  |                |4 | Display Logs / Events   |
|  |                |============================|"""
)
inp = input('|  |                Enter a value: ')

if inp == '1':
    import User

    import User.UserProfile

    # require USER_PASS
    import os, time

    cwd = os.getcwd()

    Input = input('Enter Password: ')
    try:
        import System.Drive.Password as PS

        PS.Password(Event='Cache', Input=Input)

        open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
        open(f'{cwd}/System/Cache/System/GitHub/Complex', 'w').close()
        open(f'{cwd}/System/Cache/System/GitHub/Complex_install', 'w').close()
        import shutil

        try:
            shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')
            print('|  |                Update Recorded')
        except:
            raise exit(0)

        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'GitCache cleared', Pol=1)

        time.sleep(2)
        print(f'\n' * 60)

    except:
        Input = input('Enter Password: ')
        try:
            import System.Drive.Password as PS

            PS.Password(Event='Cache', Input=Input)

            open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
            open(f'{cwd}/System/Cache/System/GitHub/Complex', 'w').close()
            open(
                f'{cwd}/System/Cache/System/GitHub/Complex_install', 'w'
            ).close()
            import shutil

            try:
                shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')
                print('|  |                Update Recorded')
            except:
                raise exit(0)

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'GitCache cleared', Pol=1)

            time.sleep(2)
            print(f'\n' * 60)

        except:
            print('Final Attempt')
            Input = input('Enter Password: ')
            try:
                import System.Drive.Password as PS

                PS.Password(Event='Cache', Input=Input)

                open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
                open(f'{cwd}/System/Cache/System/GitHub/Complex', 'w').close()
                open(
                    f'{cwd}/System/Cache/System/GitHub/Complex_install', 'w'
                ).close()
                import shutil

                try:
                    shutil.rmtree(
                        f'{cwd}/System/Cache/System/GitHub/Downloads'
                    )
                    print('|  |                Update Recorded')
                except:
                    raise exit(0)

                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'GitCache cleared', Pol=1)

                time.sleep(2)
                print(f'\n' * 60)

            except:
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(
                    event=f'GitCache clear attempt failed due to user pass',
                    Pol=1,
                )


elif inp == '2':
    import User
    import User.UserProfile

    # require USER_PASS
    import os, time

    cwd = os.getcwd()

    Input = input('Enter Password: ')
    try:
        import System.Drive.Password as PS

        PS.Password(Event='Cache', Input=Input)

        try:
            open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
            open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
            open(
                f'{User.UserProfile.SourceDirectory}System/Cache/System/ErrorLog/Event.db',
                'w',
            )

            print('|  |                Update Recorded')
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Errors & Events cleared', Pol=1)

            time.sleep(2)
            print(f'\n' * 60)
        except:
            pass

    except:
        Input = input('Enter Password: ')
        try:
            import System.Drive.Password as PS

            PS.Password(Event='Cache', Input=Input)

            try:
                open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
                open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
                open(
                    f'{User.UserProfile.SourceDirectory}System/Cache/System/ErrorLog/Event.db',
                    'w',
                )
                print('|  |                Update Recorded')
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'Errors & Events cleared', Pol=1)

                time.sleep(2)
                print(f'\n' * 60)
            except:
                pass

        except:
            print('Final Attempt')
            Input = input('Enter Password: ')
            try:
                import System.Drive.Password as PS

                PS.Password(Event='Cache', Input=Input)

                try:
                    open(
                        f'{cwd}/System/Cache/System/ErrorLog/Events', 'w'
                    ).close()
                    open(
                        f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w'
                    ).close()
                    open(
                        f'{User.UserProfile.SourceDirectory}System/Cache/System/ErrorLog/Event.db',
                        'w',
                    )
                    print('|  |                Update Recorded')
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Errors & Events cleared', Pol=1)

                    time.sleep(2)
                    print(f'\n' * 60)
                except:
                    pass

            except:
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'Failed to reset events and logs', Pol=1)

if inp == '3':
    import User
    import User.UserProfile

    # require USER_PASS
    import os, time

    cwd = os.getcwd()

    Input = input('Enter Password: ')
    try:
        import System.Drive.Password as PS

        PS.Password(Event='Cache', Input=Input)

        try:
            open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
            print('|  |                Int.txt Cleared')
            import shutil

            user = User.UserProfile.Username
            shutil.rmtree(f'{cwd}/System/Cache/System/Local')
            os.mkdir(f'{cwd}/System/Cache/System/Local')
            print('|  |                Local Connections Reset')
            try:
                shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')
            except:
                pass
            print('|  |                Downloads Reset')
            open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
            print('|  |                Events Cleared')
            open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
            print('|  |                Errors Cleared')
            open(f'{cwd}/System/Cache/User/FirstUseToken.txt', 'w').close()
            print('|  |                FirstUseToken added')
            open(f'{cwd}/User/UserProfile.py', 'w').close()
            print('|  |                User Profile Wiped')
            open(
                f'{cwd}/System/Cache/System/GitHub/Complex_install', 'w'
            ).close()
            open(f'{cwd}/System/Cache/System/GitHub/Complex', 'w').close()
            open(f'{cwd}/System/Cache/System/GitHub/Complex2', 'w').close()
            open(f'{cwd}/System/Cache/System/GitHub/int2.txt', 'w').close()
            open(
                f'{User.UserProfile.SourceDirectory}System/Cache/System/ErrorLog/Event.db',
                'w',
            )
            open(f'{cwd}/System/Cache/System/Local/Int.txt', 'w').close()
            open(f'{cwd}/System/Cache/System/Local/Int2.txt', 'w').close()

            print(f'|  |                Update Recorded')
        except:
            EV.NewEvent(
                event=f'Everything Failed To Reset Due To Password Error',
                Pol=0,
            )
            raise exit(0)

        time.sleep(2)
        print(f'\n' * 60)

    except:
        Input = input('Enter Password: ')
        try:
            import System.Drive.Password as PS

            PS.Password(Event='Cache', Input=Input)

            try:
                open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
                print('|  |                Int.txt Cleared')
                import shutil

                user = User.UserProfile.Username
                shutil.rmtree(f'{cwd}/System/Cache/System/Local')
                os.mkdir(f'{cwd}/System/Cache/System/Local')
                print('|  |                Local Connections Reset')
                try:
                    shutil.rmtree(
                        f'{cwd}/System/Cache/System/GitHub/Downloads'
                    )
                except:
                    pass
                print('|  |                Downloads Reset')
                open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
                print('|  |                Events Cleared')
                open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
                print('|  |                Errors Cleared')
                open(f'{cwd}/System/Cache/User/FirstUseToken.txt', 'w').close()
                print('|  |                FirstUseToken added')
                open(f'{cwd}/User/UserProfile.py', 'w').close()
                print('|  |                User Profile Wiped')
                open(
                    f'{cwd}/System/Cache/System/GitHub/Complex_install', 'w'
                ).close()
                open(f'{cwd}/System/Cache/System/GitHub/Complex', 'w').close()
                open(f'{cwd}/System/Cache/System/GitHub/Complex2', 'w').close()
                open(f'{cwd}/System/Cache/System/GitHub/int2.txt', 'w').close()
                open(
                    f'{User.UserProfile.SourceDirectory}System/Cache/System/ErrorLog/Event.db',
                    'w',
                )
                open(f'{cwd}/System/Cache/System/Local/Int.txt', 'w').close()
                open(f'{cwd}/System/Cache/System/Local/Int2.txt', 'w').close()

                print(f'|  |                Update Recorded')
            except:
                EV.NewEvent(
                    event=f'Everything Failed To Reset Due To Password Error',
                    Pol=0,
                )
                raise exit(0)

            time.sleep(2)
            print(f'\n' * 60)

        except:
            print('Final Attempt')
            Input = input('Enter Password: ')
            try:
                import System.Drive.Password as PS

                PS.Password(Event='Cache', Input=Input)

                try:
                    open(
                        f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w'
                    ).close()
                    print('|  |                Int.txt Cleared')
                    import shutil

                    user = User.UserProfile.Username
                    shutil.rmtree(f'{cwd}/System/Cache/System/Local')
                    os.mkdir(f'{cwd}/System/Cache/System/Local')
                    print('|  |                Local Connections Reset')
                    try:
                        shutil.rmtree(
                            f'{cwd}/System/Cache/System/GitHub/Downloads'
                        )
                    except:
                        pass
                    print('|  |                Downloads Reset')
                    open(
                        f'{cwd}/System/Cache/System/ErrorLog/Events', 'w'
                    ).close()
                    print('|  |                Events Cleared')
                    open(
                        f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w'
                    ).close()
                    print('|  |                Errors Cleared')
                    open(
                        f'{cwd}/System/Cache/User/FirstUseToken.txt', 'w'
                    ).close()
                    print('|  |                FirstUseToken added')
                    open(f'{cwd}/User/UserProfile.py', 'w').close()
                    print('|  |                User Profile Wiped')
                    open(
                        f'{cwd}/System/Cache/System/GitHub/Complex_install',
                        'w',
                    ).close()
                    open(
                        f'{cwd}/System/Cache/System/GitHub/Complex', 'w'
                    ).close()
                    open(
                        f'{cwd}/System/Cache/System/GitHub/Complex2', 'w'
                    ).close()
                    open(
                        f'{cwd}/System/Cache/System/GitHub/int2.txt', 'w'
                    ).close()
                    open(
                        f'{User.UserProfile.SourceDirectory}System/Cache/System/ErrorLog/Event.db',
                        'w',
                    )
                    open(
                        f'{cwd}/System/Cache/System/Local/Int.txt', 'w'
                    ).close()
                    open(
                        f'{cwd}/System/Cache/System/Local/Int2.txt', 'w'
                    ).close()

                    print(f'|  |                Update Recorded')
                except:
                    EV.NewEvent(
                        event=f'Everything Failed To Reset Due To Password Error',
                        Pol=0,
                    )
                    raise exit(0)

                time.sleep(2)
                print(f'\n' * 60)
            except ValueError:
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'Full reset failed due to user pass', Pol=1)

if inp == '4':
    import sys
    import sqlite3 as sl

    import User.UserProfile

    con = sl.connect(
        f'{User.UserProfile.SourceDirectory}System/Cache/System/ErrorLog/Event.db'
    )

    with con:
        dataSs = con.execute("SELECT * FROM Event WHERE Type == 'System'")
        print('\nsystem Events\n')

        for row in dataSs:
            print(row)

        dataUs = con.execute("SELECT * FROM Event WHERE Type == 'User'")
        print('\nUser Events\n')

        for row in dataUs:
            print(row)

    print('Disconcerting- Re-launch')
    import time

    time.sleep(2)
    import sys

    sys.exit(0)
