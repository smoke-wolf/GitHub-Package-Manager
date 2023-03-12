import sys


def ForceLogin_removal():
    # require USER_PASS
    import os, time

    cwd = os.getcwd()
    Input = input('Enter Password: ')
    try:
        import System.Drive.Password as PS

        PS.Password(Event='Forced Login', Input=Input)

        import_token = open(f'{cwd}/User/UserProfile.py', 'a')
        import User.UserProfile

        if User.UserProfile.Forced_Login is True:
            Status = False
        else:
            Status = True

        import_token.write(f'\nForced_Login = {Status}')
        import_token.close()

        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'ForcedLogin = {Status}', Pol=0)
        print('Update Recorded')
        time.sleep(2)
        print(f'\n' * 60)
    except:
        Input = input('Enter Password: ')
        try:
            import System.Drive.Password as PS

            PS.Password(Event='Forced Login', Input=Input)

            import_token = open(f'{cwd}/User/UserProfile.py', 'a')
            import User.UserProfile

            if User.UserProfile.Forced_Login is True:
                Status = False
            else:
                Status = True

            import_token.write(f'\nForced_Login = {Status}')
            import_token.close()

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'ForcedLogin = {Status}', Pol=0)
            print('Update Recorded')
            time.sleep(2)
            print(f'\n' * 60)
        except:
            print('Final Attempt')
            Input = input('Enter Password: ')
            try:
                import System.Drive.Password as PS

                PS.Password(Event='Forced Login', Input=Input)

                import_token = open(f'{cwd}/User/UserProfile.py', 'a')
                import User.UserProfile

                if User.UserProfile.Forced_Login is True:
                    Status = False
                else:
                    Status = True

                import_token.write(f'\nForced_Login = {Status}')
                import_token.close()

                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'ForcedLogin = {Status}', Pol=0)
                print('Update Recorded')
                time.sleep(2)
                print(f'\n' * 60)
            except:
                print('Wrong Password Entered')
                sys.exit(0)

    import System.Drive.Errors_Events.EventMan as EV

    EV.NewEvent(event=f'Updated Canceled', Pol=0)


ForceLogin_removal()
