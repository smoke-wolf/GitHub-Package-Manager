
import os
import time

import User.UserProfile

cwd = os.getcwd()
def checkpoint():
    time.sleep(3)
    print('\n' * 100)
    import System.Requirements.Banner
    print(System.Requirements.Banner.FunctionList)
    Value = int(input('Enter a value to continue: '))

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
            ER.NewIssue(Line=21, ErNo=1, SCR='System.Drive.FunctionRequest', KeFu=['Info'], UserInp=None)

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Information * Failed', Pol=0)

        time.sleep(3)
        checkpoint()

    elif Value == 2:  # mcm
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Cache', Pol=1)

            import System.Drive.Cache
            exec('System.Drive.Cache')


        except:
            import System.Drive.Errors_Events.ErrorMan as ER
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Cache * Failed', Pol=0)
            ER.NewIssue(Line=31, ErNo=0, SCR='System.Drive.FunctionRequest', KeFu=['CacheRemoval'], UserInp=None)

    elif Value == 3:  # settings
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Settings', Pol=1)

            import System.Requirements
            print(System.Requirements.Banner.Function_Settings)
            import System.Drive.Functions.Settings
            System.Drive.Functions.Settings.main()



        except:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = Settings * Failed', Pol=0)
            import System.Drive.Errors_Events.ErrorMan as ER
            ER.NewIssue(Line=41, ErNo=1, SCR='System.Drive.FunctionRequest', KeFu=['Settings'], UserInp=None)

        time.sleep(3)
        checkpoint()


    elif Value == 4:
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = PackageInstaller', Pol=1)

            import System.Drive.Functions.PackageInstaller
            System.Drive.Functions.PackageInstaller.main()


        except:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = PackageInstaller * Failed', Pol=0)

            import System.Drive.Errors_Events.ErrorMan as ER
            ER.NewIssue(Line=52, ErNo=1, SCR='System.Drive.FunctionRequest', KeFu=['PackageInstaller'], UserInp=None)
        time.sleep(3)
        checkpoint()


    elif Value == 5:
        try:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = PackageActivator', Pol=1)
            import System.Drive.Functions.PackageActivator
            System.Drive.Functions.PackageActivator.All()


        except:
            import System.Drive.Errors_Events.ErrorMan as ER
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'FunctionRequest = PackageActivator * Failed', Pol=0)
            ER.NewIssue(Line=63, ErNo=1, SCR='System.Drive.FunctionRequest', KeFu=['PackageActivator'], UserInp=None)
        time.sleep(3)
        checkpoint()

    elif Value == 6:
        import System.Drive.Errors_Events.EventMan as EV
        EV.NewEvent(event=f'FunctionRequest = PackageUninstaller', Pol=1)
        EV.NewEvent(event=f'Starting Uninstaller', Pol=0)
        import System.Drive.Functions.Uninstall
        System.Drive.Functions.Uninstall.All()
        checkpoint()

    elif Value == 8:
        print(f'Peace Out {User.UserProfile.Username}!')
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'User Logged Out', Pol=0)
        exit(0)

    else:

        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'FunctionRequest = InvalidEntry', Pol=1)

        import System.Drive.Errors_Events.ErrorMan as ER
        ER.NewIssue(Line=69, ErNo=1, SCR='System.Drive.FunctionRequest', KeFu=['IncorrectInputValue'], UserInp=None)
