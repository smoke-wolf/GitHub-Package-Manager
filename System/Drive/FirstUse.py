import os
import sys
import time
cwd = os.getcwd()

FirstUse = os.path.exists(f'{cwd}/System/Cache/User/FirstUseToken.txt')  # checks if this is the first use

UserProfile = open(f'{cwd}/User/UserProfile.py', 'a')

if FirstUse is True:  # Is first use
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
    UserName()


    def Password():
        print('Create a Password For Protected Functions.')
        password = input('Password: ')
        if password is None:
            Password()
        else:
            UserProfile.write(f"\nPassword = '{password}'")
    Password()

    print("=======================")

    SourceDirectory = os.getcwd()  # Getting the working directory for executing system calls

    UserPrivileges = os.getlogin()  # Checks if user is root or not

    UserProfile.write(f"\nUserPrivileges = '{UserPrivileges}'\nSourceDirectory = '{SourceDirectory}/'\nForce_Import_Request = True \nForced_Login = True")
    UserProfile.close()

    print(f'User Profile Has Been Created.')

    os.remove(f"{cwd}/System/Cache/User/FirstUseToken.txt")

    print('Exiting System [1s] - Re-launch')
    time.sleep(1)
    sys.exit()
