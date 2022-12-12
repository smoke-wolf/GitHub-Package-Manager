def ForceLogin_removal():
    # require USER_PASS
    import os, time
    cwd = os.getcwd()
    try:
        import User.UserProfile

        PWD = input('Verify Request (password) : ')

        if PWD == User.UserProfile.Password:
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
        else:
            print('The password entered is incorrect')
            re_try = input('Would you like to try again [1=yes] : ')
            if re_try == "1":
                ForceLogin_removal()

                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'PasswordReEntered', Pol=1)
            else:
                print('Setting Changes Aborted')

                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'Password Failed', Pol=1)
    except:
        print('Something went wrong: Please ensure (FIRST_USE_TOKEN) has been run')

        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Updated Canceled', Pol=0)

ForceLogin_removal()