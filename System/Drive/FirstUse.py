import os
import sys
import time
cwd = os.getcwd()

FirstUse = os.path.exists(f'{cwd}/System/Cache/User/FirstUseToken.txt')  # checks if this is the first use


if FirstUse is True:  # Is first use
    print(cwd)
    UserProfile = open(f'{cwd}/User/UserProfile.py', 'w')
    print('1')
    import System.Drive.Errors_Events.EventMan as EV
    EV.NewEvent(event=f'Starting FirstUse', Pol=1)
    print('\n' * 100)
    print("Hey there, as this is the first use we are going to configure a few things. This shouldn't take long.")
    time.sleep(1)

    print("Developing User Profile")
    print("=======================")


    def UserName():
        print('Enter The Username You Would Like To Go By.')
        Username = input('Username: ')

        if Username is None:
            UserName()
        else:
            UserProfile.write(f"Username = '{Username}'")
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Username Added', Pol=1)
    try:
        UserName()
    except:
        import System.Drive.Errors_Events.ErrorMan as ER
        ER.NewIssue(Line=31, ErNo=0, SCR='FirstUse', KeFu=['Username=None/IncorrectValue'], UserInp=None)


    def Password():
        print('Create a Password For Protected Functions.')
        password = input('Password: ')
        if password is None:
            Password()
        else:
            UserProfile.write(f"\nPassword = '{password}'")
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Password created', Pol=1)
    try:
        Password()
    except:
        import System.Drive.Errors_Events.ErrorMan as ER
        ER.NewIssue(Line=46, ErNo=0, SCR='FirstUse', KeFu=['Password=IncorrectEntry'], UserInp=None)

    print("=======================")

    SourceDirectory = os.getcwd()  # Getting the working directory for executing system calls

    UserPrivileges = os.getlogin()  # Checks if user is root or not
    try:
        UserProfile.write(f"\nUserPrivileges = '{UserPrivileges}'\nSourceDirectory = '{SourceDirectory}/'\nForce_Import_Request = True \nForced_Login = True")
        UserProfile.close()


    except:
        import System.Drive.Errors_Events.ErrorMan as ER
        ER.NewIssue(Line=56, ErNo=0, SCR='FirstUse', KeFu=['UserProfileNotConfigured'], UserInp=None)

    print(f'User Profile Has Been Created.')
    import System.Drive.Errors_Events.EventMan as EV

    EV.NewEvent(event=f'Account Created', Pol=0)
    os.remove(f"{cwd}/System/Cache/User/FirstUseToken.txt")

    print('Exiting System [1s] - Re-launch')
    time.sleep(1)
    sys.exit()
