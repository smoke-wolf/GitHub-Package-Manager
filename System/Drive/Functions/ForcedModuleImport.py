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
            print('Update Recorded')
            time.sleep(2)
            print(f'\n'*60)
        else:
            print('The password entered is incorrect')
            re_try = input('Would you like to try again [1=yes] : ')
            if re_try == "1":
                ForceImport_removal()
            else:
                print('Setting Changes Aborted')
    except:
        print('Something went wrong: Please ensure (FIRST_USE_TOKEN) has been run')

ForceImport_removal()