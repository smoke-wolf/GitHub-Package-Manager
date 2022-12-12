print('=======Cache=======')
print('1 | Remove All Git')
print('===================')
inp = input('Enter a value: ')
import System.Drive.Errors_Events.ErrorMan as ER

if inp == '1':
    #require USER_PASS
    import os, time
    cwd = os.getcwd()
    try:
        import User.UserProfile
        Password = input('Verify Request (password) : ')
        if Password == User.UserProfile.Password:
            open(f'{cwd}/System/Cache/System/GitHub/Int.py', 'w').close()
            import shutil
            try:
                shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')
            except:
                print('010')

            print('Update Recorded')

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'GitCache cleared', Pol=1)

            time.sleep(2)
            print(f'\n' * 60)
        else:
            print('Password incorrect. Try again')
            Password = input('Enter Password: ')
            if Password == User.UserProfile.Password:
                open(f'{cwd}/System/Cache/System/GitHub/Int.py', 'w').close()
                import shutil

                shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')

                print('Update Recorded')
                time.sleep(2)
                print(f'\n' * 60)
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'GitCache cleared', Pol=1)
            else:
                print('Password incorrect. Final attempt')
                Password = input('Enter Password: ')
                if Password == User.UserProfile.Password:
                    open(f'{cwd}/System/Cache/System/GitHub/Int.py', 'w').close()
                    import shutil

                    shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')

                    print('Update Recorded')
                    time.sleep(2)
                    print(f'\n' * 60)
                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'GitCache cleared', Pol=1)
                else:
                    import sys
                    raise ValueError
    except ValueError:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'GitCache clear attempt failed due to user pass', Pol=1)
        ER.NewIssue(Line=48, ErNo=0, SCR='Cache', KeFu=['Password Verification Error', 'Wrong Password'], UserInp=None)