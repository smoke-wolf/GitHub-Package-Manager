print('=======Cache=======')
print('1 | Remove All Git')
print('===================')
inp = input('Enter a value: ')

if inp == '1':
    #require USER_PASS
    import os, time
    cwd = os.getcwd()
    try:
        import User.UserProfile

        PWD = input('Verify Request (password) : ')

        if PWD == User.UserProfile.Password:
            open(f'{cwd}/System/Cache/System/GitHub/Int.py', 'w').close()
            import shutil
            shutil.rmtree(f'{cwd}/System/Cache/System/GitHub/Downloads')

            print('Update Recorded')
            time.sleep(2)
            print(f'\n'*60)
        else:
            print('The password entered is incorrect')

    except:
        print('Something went wrong: Please ensure (FIRST_USE_TOKEN) has been run')