import os
import time

cwd = os.getcwd()
def checkpoint():
    print('\n'*100)
    import System.Requirements.Banner
    print(System.Requirements.Banner.FunctionList)
    Value = int(input('Enter a value to continue: '))

    if Value == 1:  # System info
        import System.Requirements
        print(System.Requirements.Information.SwAT)
        t = input('\n\nHit enter to continue: ')
        time.sleep(3)
        checkpoint()

    elif Value == 2:    #mcm
        import System.Drive.Cache
        exec('System.Drive.Cache')

    elif Value == 3:  # settings
        import System.Requirements
        print(System.Requirements.Banner.Function_Settings)
        import System.Drive.Functions.Settings
        exec('System.Drive.Functions.Settings')
        time.sleep(3)
        checkpoint()


    elif Value == 4:
        import System.Drive.Functions.PackageInstaller
        exec('System.Drive.Functions.PackageInstaller')
        time.sleep(3)
        checkpoint()


    elif Value == 5:
        import System.Drive.Functions.PackageActivator
        System.Drive.Functions.PackageActivator.All()
        
        time.sleep(3)
        checkpoint()

