# Python code obfuscated by www.development-tools.net
import os
import sys

import System.Requirements.Information
import User.UserProfile

try:
    if User.UserProfile.Force_Import_Request is False:
        import System.Drive.Errors_Events.EventMan as EV
        EV.NewEvent(event=f'Import Test Aborted Due To User Settings', Pol=0)
    else:
        raise ValueError

except ValueError:
    Modules = System.Requirements.Information.Modules
    for Module in Modules:
        try:
            __import__(Module)
            print("Successfully imported ", Module, '.')
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Import_Success = {Module}', Pol=0)
        except ImportError:
            print("Error importing ", Module, '.')
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Import_Failed = {Module}', Pol=0)
            try:
                os.system(f'pip install {Module}')
                os.system(f'pip3 install {Module}')
            except:
                print('Module failed to install')
                sys.exit(0)


    import time
    time.sleep(1)
    print('\n'*100)
