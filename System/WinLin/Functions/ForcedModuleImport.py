def ForceImport_removal():
    # require USER_PASS
    import os, time

    cwd = os.getcwd()

    Input = input('Enter Password: ')
    try:
        import System.Drive.Password as PS

        PS.Password(Event='Forced Login', Input=Input)

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
        print(f'\n' * 60)
    except:
        Input = input('Enter Password: ')
        try:
            import System.Drive.Password as PS

            PS.Password(Event='Forced Login', Input=Input)

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
            print(f'\n' * 60)
        except:
            print('Final Attempt')
            Input = input('Enter Password: ')
            try:
                import System.Drive.Password as PS

                PS.Password(Event='Forced Login', Input=Input)

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
                print(f'\n' * 60)

            except:
                print('Incorrect Password')


ForceImport_removal()
