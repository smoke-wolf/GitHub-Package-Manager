import System.Requirements.Information
import User.UserProfile

try:
    if User.UserProfile.Force_Import_Request is False:
        pass
    else:
        raise ValueError
except ValueError:
    Modules = System.Requirements.Information.Modules
    for Module in Modules:
        try:
            __import__(Module)
            print("Successfully imported ", Module, '.')
        except ImportError:
            print("Error importing ", Module, '.')
    import time
    time.sleep(1)
    print('\n'*100)