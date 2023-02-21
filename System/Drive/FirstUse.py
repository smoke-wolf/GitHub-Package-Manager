import os
import sys
import time

cwd = os.getcwd()

FirstUse = os.path.exists(
    f'{cwd}/System/Cache/User/FirstUseToken.txt'
)  # checks if this is the first use

if FirstUse is True:  # Is first use
    print(cwd)
    # System.Drive.Password.write_key()
    UserProfile = open(f'{cwd}/User/UserProfile.py', 'w')

    # import System.Drive.Errors_Events.EventMan as EV
    # EV.NewEvent(event=f'Starting FirstUse', Pol=1)
    print('\n' * 100)
    print(
        "Hey there, as this is the first use we are going to configure a few things. This shouldn't take long."
    )
    time.sleep(1)

    print('Developing User Profile')
    print('=======================')

    def UserName():
        print('Enter The Username You Would Like To Go By.')
        Username = input('Username: ')

        if Username is None:
            UserName()
        else:
            UserProfile.write(f"Username = '{Username}'")
            # import System.Drive.Errors_Events.EventMan as EV

            # EV.NewEvent(event=f'Username Added', Pol=1)

    try:
        UserName()
    except:
        pass
        # ER.NewIssue(Line=31, ErNo=0, SCR='FirstUse', KeFu=['Username=None/IncorrectValue'], UserInp=None)

    def Password():
        print('Create a Password For Protected Functions.')
        password = input('Password: ')
        import hashlib
        import uuid
        import sys

        UUID = uuid.uuid1()

        UserID = os.getlogin()

        salt = '9lk'

        UUID = str(f'{UUID}')

        uuidToken = UUID[30:]

        Password = f'{password}{uuidToken}{UserID}'

        password = Password + salt
        hashed = hashlib.md5(password.encode())
        Password = hashed.hexdigest()

        UserProfile.write(f"\nPassword = '{Password}'")
        import System.Drive.Errors_Events.EventMan as EV

        with open(f'{cwd}/System/Cache/User/local', 'w') as bl:
            bl.write(hashed.hexdigest()[:16])

        EV.NewEvent(event=f'Password created', Pol=1)

    try:
        Password()
    except:
        pass
        # ER.NewIssue(Line=46, ErNo=0, SCR='FirstUse', KeFu=['Password=IncorrectEntry'], UserInp=None)

    print('=======================')

    SourceDirectory = (
        os.getcwd()
    )  # Getting the working directory for executing system calls

    UserPrivileges = os.getlogin()  # Checks if user is root or not

    import uuid

    uuid1 = uuid.uuid1().hex
    uuid4 = uuid.uuid4().hex

    try:
        UserProfile.write(
            f"\nUserPrivileges = '{UserPrivileges}'\nSourceDirectory = '{SourceDirectory}/'\nForce_Import_Request = True \nForced_Login = True\nuuid1 = '{uuid1}'\nuuid4 = '{uuid4}'\nDisplayEvents = True"
        )
        UserProfile.close()

    except:
        pass
        # ER.NewIssue(Line=56, ErNo=0, SCR='FirstUse', KeFu=['UserProfileNotConfigured'], UserInp=None)

    print(f'User Profile Has Been Created.')
    import System.Drive.Errors_Events.EventMan as EV

    EV.NewEvent(event=f'Account Created', Pol=0)

    try:
        os.remove(f'{os.getcwd()}/System/Cache/User/FirstUseToken.txt')
    except:
        print('Token Error')
        sys.exit(0)

    print('Exiting System [1s] - Re-launch')
    time.sleep(1)

    import os

    filename = '.SD.hidden'
    file_path = os.path.join(os.path.expanduser('~'), filename)

    with open(file_path, 'w') as file:
        file.write(f'{SourceDirectory}')
    print(f'Token Saved @ {file_path}')

    sys.exit()
else:
    pass
