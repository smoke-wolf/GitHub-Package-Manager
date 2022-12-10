import time
import System.Requirements.Banner
import System.Drive.FirstUse
import User.UserProfile
import os

# Main Launch File
import System.Drive.Errors.ErrorMan as ER


print('\n' * 100)

cwd = os.getcwd()
print(System.Requirements.Banner.FunctionList)
import System.Drive.FunctionRequest
time.sleep(4)
os.system(f'{cwd}/System/Drive/FunctionRequest.py')

# import os
# os.system(f'{User.UserProfile.SourceDirectory}System/Drive/Re.py')
