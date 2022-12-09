import os
import time

cwd = os.getcwd()


Value = int(input('Enter a value to continue: '))

if Value == 1:  # System info
    import System.Requirements
    print(System.Requirements.Information.SwAT)
    t = input('\n\nHit enter to continue: ')

    import os
    import User.UserProfile
    os.system(f'python3 {User.UserProfile.SourceDirectory}System/Drive/Re.py')

elif Value == 2:    #mcm
    import System.Drive.Cache
    exec('System.Drive.Cache')

elif Value == 3:  # settings
    import System.Requirements
    print(System.Requirements.Banner.Function_Settings)
    import System.Drive.Functions.Settings
    exec('System.Drive.Functions.Settings')
    import os
    import User.UserProfile

    os.system(f'python3 {User.UserProfile.SourceDirectory}System/Drive/Re.py')

elif Value == 4:
    import System.Drive.Functions.PackageInstaller
    exec('System.Drive.Functions.PackageInstaller')
    import os
    import User.UserProfile

    os.system(f'python3 {User.UserProfile.SourceDirectory}System/Drive/Re.py')

elif Value == 5:
    os.system(f'python3 {cwd}/System/Drive/Functions/PackageActivator.py')
    import os
    import User.UserProfile

    os.system(f'python3 {User.UserProfile.SourceDirectory}System/Drive/Re.py')
