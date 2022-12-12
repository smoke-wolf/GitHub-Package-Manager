# SwAT
Your First GitHub Manager!

This is the solution to scattered, disorginized git repos.

# Lauch instructions
git clone https://github.com/smoke-wolf/SwAT.git \
cd SwAT\
python3 Start.py

you will need to create a UserProfile, once done you need to re-run 'python3 Start.py'


# Main features:

`	`⁃	Cache -> Clear all git -> wipes all GitHub download data \*Requires password 

`	`⁃	Settings -> User -> None

`	`⁃	System -> ForcedLogin \*requires password -> Toggles the need for a password on launch

`	`⁃	System -> ForcedModuleImport \*requires password -> Toggles imports on launch

`	`⁃	PackageInstaller -> GitRepo -> enter the git repo to clonne -> for launch script, enter the corresponding number (check the repo for launch script name)

`	`⁃	PackageInstaller -> LocalDir -> enter the directory you want to connect -> for launch script, enter the corresponding number

`	`⁃	PackageActivator -> GitHub -> select the package to run from list

`	`⁃  PackageActivator -> local -> select the package to run from list

`	`⁃	PackageUninstaller \* will delete directory as well as launch command\
`	`⁃		Github -> select the package to uninstall from list

`	`⁃		Local -> select the package to uninstall from list

`	`⁃	Events/errors -> all saved in System/Cache/System/ErrorLog/


NOTE\* System.Drive.Functions.Uninstall will not work if you have already launched a package in said instance

NOTE\* Passwords are saved in User.UserProfile

NOTE\* There’s an unknown bug within the System.Drive.Functions.PackageInstaller \*1



* 1
# Errors
{Event at 2022-12-12 02:30:26:User [!]FunctionRequest = PackageInstaller[!]\
Event at 2022-12-12 02:59:42:User [!]Install @GitRepo[!]\
Event at 2022-12-12 02:59:43:System [!]Downloaded from Github[!] ~~~~~~ \*download from git -> no launch file -> no error recorded.\* \
Event at 2022-12-12 02:59:43:User [!]FunctionRequest = PackageInstaller[!]\
Event at 2022-12-12 02:59:58:User [!]Install @GitRepo[!]\
Event at 2022-12-12 02:59:59:System [!]FunctionRequest = PackageInstaller \* Failed[!]\
Event at 2022-12-12 03:00:13:User [!]Install @GitRepo[!]\
Event at 2022-12-12 03:00:15:System [!]FunctionRequest = PackageInstaller \* Failed[!]\
Event at 2022-12-12 03:02:19:User [!]Install @GitRepo[!]\
Event at 2022-12-12 03:02:20:System [!]FunctionRequest = PackageInstaller \* Failed[!]\
Event at 2022-12-12 03:03:07:User [!]Install @GitRepo[!]\
Event at 2022-12-12 03:03:10:System [!]FunctionRequest = PackageInstaller \* Failed[!]\
Event at 2022-12-12 03:04:16:User [!]Install @GitRepo[!]\
Event at 2022-12-12 03:04:18:System [!]FunctionRequest = PackageInstaller \* Failed[!]}\

the bug does not occur regularly. when it does it is noticed by menus not loading -> Packages not activating correctly


# TechInfo

Technical Information #4\
=====================\
SwAT Version = v1.2.2\
GitConnect = v2.0\
LocalConnect = v2.0\
UserPass = v2.2\
ReturnFunction = v2.1\
PackageActivator.py = v3.2\
PackageUnistaller.py = v1.0\
Menu = 7/8\
Version Status = Fully Released\
Version Date = December 12 2022\
Developer = JDX50S, Smoke-wolf\
Version Security = Secure\


Technical Information #3\
=====================\
SwAT Version = v1.1.2\
GitConnect = v1.0\
LocalConnect = v1.0\
UserPass = v2.2\
ReturnFunction = v2.1\
PackageActivator.py = v2.2\
Menu = 6/8\
Version Status = Released\
Version Date = December 10 2022\
Developer = JDX50S, Smoke-wolf\
Version Security = Secure\


Technical Information 0.2\
=====================\
SwAT Version = v1.1\
GitConnect = v1.0\
LocalConnect = v1.0\
UserPass = v2.2\
Menu = 5/8\
Version Status = -BetaRelease\
Version Date = December 9 2022\
Developer = JDX50S, Smoke-wolf\
Version Security = Secure\
