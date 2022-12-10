# Main Launch File
import System.Drive.Errors.ErrorMan as ER
import System.Drive.FirstUse

try:
    import System.Requirements.Banner
    exec('System.Drive.FirstUse')
    import User.UserProfile
    import System.Drive.ModuleVerifier
    import os
except ImportError:
    ER.NewIssue(Line=3, ErNo=0, SCR='Start', KeFu=['Import Error'], UserInp=None)

cwd = os.getcwd()

print(System.Requirements.Banner.Launcher)  # Loads banner
exec('System.Drive.ModuleVerifier')

try:
    print(f'Welcome Back {User.UserProfile.Username}!')  # forces userLogin
    import System.Drive.Login
    exec('System.Drive.Login')
except:
    ER.NewIssue(Line=19, ErNo=0, SCR='System.Drive.Login', KeFu=['Login''UserID'], UserInp=None)


import System.Drive.FunctionRequest
System.Drive.FunctionRequest.checkpoint()

