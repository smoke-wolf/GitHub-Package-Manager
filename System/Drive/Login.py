import sys

import User.UserProfile
import time

def Login():
    Password = input('Enter Password: ')
    if Password == User.UserProfile.Password:
        print('Logged In Successfully!')
        time.sleep(1.54)
        print('\n'*100)
    else:
        print('Password incorrect. Try again')
        Password = input('Enter Password: ')
        if Password == User.UserProfile.Password:
            print('Logged In Successfully!')
            time.sleep(1.54)
            print('\n' * 100)
        else:
            print('Password incorrect. Final attempt')
            Password = input('Enter Password: ')
            if Password == User.UserProfile.Password:
                print('Logged In Successfully!')
                time.sleep(1.54)
                print('\n' * 100)
            else:
                sys.exit(0)


if User.UserProfile.Forced_Login == False:
    pass
else:
    Login()