import datetime
global os
import sys
import time
import User.UserProfile

global cwd

cwd = User.UserProfile.SourceDirectory


def checkpoint():
    import os
    import time
    os.chdir(User.UserProfile.SourceDirectory)
    time.sleep(0)
    print('\n' * 100)
    import importlib
    import System.Requirements.Banner

    importlib.reload(System.Requirements.Banner)

    try:
        with open(
                f'{User.UserProfile.SourceDirectory}System/.Cache/System/Version.py',
                'r',
        ) as ver:
            version = ver.read()
    except:
        version = 'Version Cannot Be Read'

    import datetime

    print(
        f"""
\033[1m ______                ______             
    |          |   |      |   |      |\ /| 
    | +-       |-+-|      |-+-       | + | 
    |   |      |   |      |          |   | 
     ---  \033[0m                                                                                                                                                                                                                                                                                                                    
==========================================
What's up \033[1m\033[1m{User.UserProfile.Username}!\033[0m      
Today: {datetime.datetime.today()}
From The Devs! {version}Check out the GUI it's option 9!
==========================================="""
    )

    print(System.Requirements.Banner.FunctionList)
    Value = input('Enter a value to continue: ')

    try:
        Value = int(Value)
    except:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'FunctionRequest input error', Pol=1)
        checkpoint()

    if Value == 1:  # System info
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Information', Pol=1)

            import System.Requirements

            print(System.Requirements.Information.SwAT)
            t = input('\n\nHit enter to continue: ')
            print('\n\n')
            import System.Requirements

            print(System.Requirements.FTD.dev_message)
            t = input('\n\nHit enter to continue: ')

        except:
            import System.Drive.Errors_Events.ErrorMan as ER

            ER.NewIssue(
                Line=21,
                ErNo=1,
                SCR='System.Drive.FunctionRequest',
                KeFu=['Info'],
                UserInp=None,
            )

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Information * Failed', Pol=0)

            os.chdir(User.UserProfile.SourceDirectory)

        time.sleep(0)
        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 2:  # mcm
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Cache', Pol=1)

            import System.Drive.Functions.Cache

            exec('System.Drive.Functions.Cache')

        except:
            import System.Drive.Errors_Events.ErrorMan as ER
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Cache * Failed', Pol=0)
            ER.NewIssue(
                Line=31,
                ErNo=0,
                SCR='System.Drive.FunctionRequest',
                KeFu=['CacheRemoval'],
                UserInp=None,
            )

            os.chdir(User.UserProfile.SourceDirectory)
            checkpoint()


    elif Value == 3:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'FunctionRequest = PackageUninstaller', Pol=1)

        import System.Drive.Functions.Uninstall

        Input = input('Enter Password To Use Uninstaller: ')
        try:
            import System.Drive.Password as PS

            PS.Password(Event='Uninstall', Input=Input)

            print('Launching Uninstaller')
            time.sleep(1.54)
            print('\n' * 100)
            EV.NewEvent(event=f'Starting Uninstaller', Pol=0)
            System.Drive.Functions.Uninstall.All()
        except:
            Input = input('Enter Password To Use Uninstaller: ')
            try:
                import System.Drive.Password as PS

                PS.Password(Event='Uninstall', Input=Input)

                print('Launching Uninstaller')
                time.sleep(1.54)
                print('\n' * 100)
                EV.NewEvent(event=f'Starting Uninstaller', Pol=0)
                System.Drive.Functions.Uninstall.All()
            except:
                print('Final Attempt')
                Input = input('Enter Password To Use Uninstaller: ')
                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Uninstall', Input=Input)

                    print('Launching Uninstaller')
                    time.sleep(1.54)
                    print('\n' * 100)
                    EV.NewEvent(event=f'Starting Uninstaller', Pol=0)
                    System.Drive.Functions.Uninstall.All()

                except:
                    EV.NewEvent(event=f'Password Failed Multiple Times', Pol=1)

        os.chdir(User.UserProfile.SourceDirectory)
        checkpoint()

    elif Value == 0:
        print(f'Peace Out {User.UserProfile.Username}!')
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'User Logged Out', Pol=0)
        exit(0)

    elif Value == 4:
        import System.Drive.VersionUpdate

        exec('System.Drive.VersionUpdate')
    else:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'FunctionRequest = InvalidEntry', Pol=1)

        import System.Drive.Errors_Events.ErrorMan as ER

        ER.NewIssue(
            Line=69,
            ErNo=1,
            SCR='System.Drive.FunctionRequest',
            KeFu=['IncorrectInputValue'],
            UserInp=None,
        )


checkpoint()
