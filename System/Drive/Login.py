import sys

import User.UserProfile
import time

def Login():
    Password = input('Enter Password: ')
    if Password == User.UserProfile.Password:
        print('Logged In Successfully!')
        time.sleep(1.54)
        print('\n'*100)
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Login_Success = 1', Pol=0)
    else:
        print('Password incorrect. Try again')
        Password = input('Enter Password: ')
        if Password == User.UserProfile.Password:
            print('Logged In Successfully!')
            time.sleep(1.54)
            print('\n' * 100)
            import System.Drive.Errors_Events.EventMan as EV
            EV.NewEvent(event=f'Login_Success = 2', Pol=0)
        else:
            print('Password incorrect. Final attempt')
            Password = input('Enter Password: ')
            if Password == User.UserProfile.Password:
                print('Logged In Successfully!')
                import System.Drive.Errors_Events.EventMan as EV
                EV.NewEvent(event=f'Login_Success = FinalAttempt', Pol=0)
                time.sleep(1.54)
                print('\n' * 100)
            else:
                sys.exit(0)


if User.UserProfile.Forced_Login == False:
    pass
    import System.Drive.Errors_Events.EventMan as EV

    EV.NewEvent(event=f'Password Aborted Due to User Settings', Pol=0)
else:
    Login()