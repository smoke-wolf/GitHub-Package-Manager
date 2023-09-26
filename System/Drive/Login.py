'''
this script handles user authentication by validating
the entered password, with multiple retries if necessary,
and checks for device restrictions based on the device's UUID.
If the device is not restricted, the user is allowed to log in.



'''
import sys
import User.UserProfile


def Login():
    import time
    print('''
    ======================================
    [[[[[[[[[[[LOG IN TO CONTINUE]]]]]]]]]
    ======================================''')
    Input = input('Enter Password: ')
    try:
        import System.Drive.Password as PS

        PS.Password(Event='Login', Input=Input)
        print('Logged In Successfully!')
        time.sleep(1.54)
        print('\n' * 100)
    except:
        Input = input('Enter Password: ')
        try:
            import System.Drive.Password as PS

            PS.Password(Event='Login', Input=Input)
            print('Logged In Successfully!')
            time.sleep(1.54)
            print('\n' * 100)
        except:
            print('Final Try')
            Input = input('Enter Password: ')
            try:
                import System.Drive.Password as PS

                PS.Password(Event='Login', Input=Input)
                print('Logged In Successfully!')
                time.sleep(1.54)
                print('\n' * 100)
            except:
                sys.exit(0)


Blocked = open(f'{User.UserProfile.SourceDirectory}User/Blocked', 'r')
Blocked = Blocked.read()
import uuid

UUID = uuid.uuid1()
UUID = str(f'{UUID}')
uuidToken = UUID[30:]
if uuidToken in Blocked:
    import System.Drive.Errors_Events.EventMan as EV

    EV.NewEvent(event='Device Restricted Due To NonOriginDevice', Pol=0)
    print('This Device Has Been Restricted')
    sys.exit(0)
else:
    Login()
