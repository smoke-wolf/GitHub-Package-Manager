import time


# Main Launch File
import System.Drive.Errors.ErrorMan as ER

time.sleep(4)
print('\n' * 100)

try:
    import System.Requirements.Banner
    import System.Drive.FirstUse
    import User.UserProfile
    import os
except ImportError:
    ER.NewIssue(Line=3, ErNo=0, SCR='Start', KeFu=['Import Error'], UserInp=None)

cwd = os.getcwd()

print(System.Requirements.Banner.FunctionList)
import System.Drive.FunctionRequest
exec('System.Drive.FunctionRequest')


# import os
# os.system(f'{User.UserProfile.SourceDirectory}System/Drive/Re.py')
