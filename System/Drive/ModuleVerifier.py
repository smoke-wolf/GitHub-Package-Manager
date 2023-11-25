'''
this script is responsible for managing module imports and installations 
and provides information about the success or failure of these operations,
potentially as part of an initialization or setup process for the application.
'''




import os
import sys

try:
    import System.Requirements.Information
    import User.UserProfile
except:
    pass

try:
    if User.UserProfile.Force_Import_Request is False:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Import Test Aborted Due To User Settings', Pol=0)
    else:
        pass

except:
    Modules = System.Requirements.Information.Modules
    for Module in Modules:
        try:
            __import__(Module)
            print('Successfully imported ', Module, '.')
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Import_Success = {Module}', Pol=0)
        except ImportError:
            print('Error importing ', Module, '.')
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Import_Failed = {Module}', Pol=0)
            try:
                os.system(f'python3 -m pip install {Module}')
                os.system(f'pip3 install {Module}')
            except:
                print('Module failed to install')
                sys.exit(0)

    import time

    time.sleep(1)
    print('\n' * 100)
