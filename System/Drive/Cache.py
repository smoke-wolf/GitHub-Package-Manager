print('''\n|  |                |============Cache===========|
|  |                |1 | Remove All Git Downloads|
|  |                |2 | Reset Events / Log      |
|  |                |3 | Reset All To Defaults   |
|  |                |============================|''')
inp = input('|  |                Enter a value: ')
import System.Drive.Errors_Events.ErrorMan as ER

if inp == '1':
    #require USER_PASS
    import os, time
    cwd = os.getcwd()
    try:
        import User.UserProfile
        Password = input('|  |                Verify Request (password) : ')
        if Password == User.UserProfile.Password:
            open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
            open(f'{cwd}/System/Cache/System/GitHub/Complex', "w").close()
            import shutil
            try:
                shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')
                print('|  |                Update Recorded')
            except:
                raise exit(0)



            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'GitCache cleared', Pol=1)

            time.sleep(2)
            print(f'\n' * 60)
        else:
            print('|  |                Password incorrect. Try again')
            Password = input('|  |                Enter Password: ')
            if Password == User.UserProfile.Password:
                open(f'{cwd}/System/Cache/System/GitHub/Complex', "w").close()
                open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
                import shutil

                shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')

                print('|  |                Update Recorded')
                time.sleep(2)
                print(f'\n' * 60)
                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'GitCache cleared', Pol=1)
            else:
                print('|  |                Password incorrect. Final attempt')
                Password = input('|  |                Enter Password: ')
                if Password == User.UserProfile.Password:
                    open(f'{cwd}/System/Cache/System/GitHub/Complex', "w").close()
                    open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
                    import shutil

                    shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')

                    print('|  |                Update Recorded')
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
elif inp == '2':

    # require USER_PASS
    import os, time

    cwd = os.getcwd()
    try:
        import User.UserProfile

        Password = input('|  |                Verify Request (password) : ')
        if Password == User.UserProfile.Password:
            # require USER_PASS
            import os, time

            cwd = os.getcwd()
            try:
                import User.UserProfile

                Password = input('|  |                Verify Request (password) : ')
                if Password == User.UserProfile.Password:

                    try:
                        open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
                        open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
                        print('|  |                Update Recorded')
                    except:
                        pass
            except:
                os.exit(0)

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Errors & Events cleared', Pol=1)

            time.sleep(2)
            print(f'\n' * 60)
        else:
            print('|  |                Password incorrect. Try again')
            Password = input('|  |                Enter Password: ')
            if Password == User.UserProfile.Password:
                # require USER_PASS
                import os, time

                cwd = os.getcwd()
                try:
                    import User.UserProfile

                    Password = input('|  |                Verify Request (password) : ')
                    if Password == User.UserProfile.Password:

                        try:
                            open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
                            open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
                            print('|  |                Update Recorded')
                        except:
                            pass
                except:
                    os.exit(0)

                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'Errors & Events cleared', Pol=1)

                time.sleep(2)
                print(f'\n' * 60)
            else:
                print('|  |                Password incorrect. Final attempt')
                Password = input('|  |                Enter Password: ')
                if Password == User.UserProfile.Password:
                    # require USER_PASS
                    import os, time

                    cwd = os.getcwd()
                    try:
                        import User.UserProfile

                        Password = input('|  |                Verify Request (password) : ')
                        if Password == User.UserProfile.Password:

                            try:
                                open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
                                open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
                                print('|  |                Update Recorded')
                            except:
                                pass
                    except:
                        os.exit(0)

                    import System.Drive.Errors_Events.EventMan as EV

                    EV.NewEvent(event=f'Errors & Events cleared', Pol=1)

                    time.sleep(2)
                    print(f'\n' * 60)
    except ValueError:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Failed to reset events and logs', Pol=1)
if inp == '3':
    #require USER_PASS
    import os, time
    cwd = os.getcwd()
    try:
        import User.UserProfile
        Password = input('|  |                Verify Request (password) : ')
        if Password == User.UserProfile.Password:
            try:
                open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
                print('|  |                Int.txt Cleared')
                import shutil

                user = User.UserProfile.Username
                shutil.rmtree(f'{cwd}/System/Cache/System/Local')
                os.mkdir(f'{cwd}/System/Cache/System/Local')
                print('|  |                Local Connections Reset')
                try:
                    shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')
                except:
                    pass
                print('|  |                Downloads Reset')
                open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
                print('|  |                Events Cleared')
                open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
                print('|  |                Errors Cleared')
                open(f'{cwd}/System/Cache/User/FirstUseToken.txt', 'w').close()
                print('|  |                FirstUseToken added')
                open(f'{cwd}/User/UserProfile.py', 'w').close()
                print('|  |                User Profile Wiped')
                print(f'|  |                Update Recorded- Good Knowing You {User}')
            except:
                EV.NewEvent(event=f'Everything Failed To Reset', Pol=0)
                raise exit(0)

            time.sleep(2)
            print(f'\n' * 60)

        else:
            print('|  |                Password incorrect. Try again')
            Password = input('|  |                Enter Password: ')
            if Password == User.UserProfile.Password:
                try:
                    open(f'{cwd}/System/Cache/System/GitHub/Int.txt', 'w').close()
                    print('|  |                Int.txt Cleared')
                    import shutil

                    user = User.UserProfile.Username
                    shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')
                    print('|  |                Downloads Reset')
                    open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
                    print('|  |                Events Cleared')
                    open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
                    print('|  |                Errors Cleared')
                    open(f'{cwd}/System/Cache/User/FirstUseToken.txt', 'w').close()
                    print('|  |                FirstUseToken added')
                    open(f'{cwd}/User/UserProfile.py', 'w').close()
                    open(f'{cwd}/System/Cache/System/GitHub/Complex', "w").close()
                    print('|  |                User Profile Wiped')
                    print(f'|  |                Update Recorded- Good Knowing You {User}')
                except:
                    EV.NewEvent(event=f'Everything Failed To Reset', Pol=0)
                    raise exit(0)
            else:
                print('|  |                Password incorrect. Final attempt')
                Password = input('|  |                Enter Password: ')
                if Password == User.UserProfile.Password:
                    try:
                        open(f'{cwd}/System/Cache/System/GitHub/Int.py', 'w').close()
                        print('|  |                Int.txt Cleared')
                        import shutil

                        open(f'{cwd}/System/Cache/System/GitHub/Complex', "w").close()
                        user = User.UserProfile.Username
                        shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')
                        print('|  |                Downloads Reset')
                        open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'w').close()
                        print('|  |                Events Cleared')
                        open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'w').close()
                        print('|  |                Errors Cleared')
                        open(f'{cwd}/System/Cache/User/FirstUseToken.txt', 'w').close()
                        print('|  |                FirstUseToken added')
                        open(f'{cwd}/User/UserProfile.py', 'w').close()
                        print('|  |                User Profile Wiped')
                        print(f'|  |                Update Recorded- Good Knowing You {User}')
                    except:
                        EV.NewEvent(event=f'Everything Failed To Reset', Pol=0)
                        raise exit(0)
                else:
                    import sys
                    raise ValueError
    except ValueError:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Full reset failed due to user pass', Pol=1)
        ER.NewIssue(Line=48, ErNo=0, SCR='Cache', KeFu=['Password Verification Error', 'Wrong Password'], UserInp=None)
