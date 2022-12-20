def ForceImport_removal():
    #require USER_PASS
    import os, time
    cwd = os.getcwd()
    try:
        import User.UserProfile

        PWD = input('Verify Request (password) : ')

        if PWD == User.UserProfile.Password:
            import_token = open(f'{cwd}/User/UserProfile.py', 'a')
            import User.UserProfile
            if User.UserProfile.Force_Import_Request is True:
                Status = False
            else:
                Status = True

            import_token.write(f'\nForce_Import_Request = {Status}')
            import_token.close()

            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'forced Module Import = {Status}', Pol=0)
            print('Update Recorded')
            time.sleep(2)
            print(f'\n'*60)
        else:
            print('The password entered is incorrect')
            re_try = input('Would you like to try again [1=yes] : ')
            if re_try == "1":
                ForceImport_removal()

                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'Password ReEntered', Pol=1)
            else:
                print('Setting Changes Aborted')

                import System.Drive.Errors_Events.EventMan as EV

                EV.NewEvent(event=f'Password = Incorrect', Pol=1)
    except:
        print('Something went wrong: Please ensure (FIRST_USE_TOKEN) has been run')

        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Update Canceled', Pol=0)

ForceImport_removal()