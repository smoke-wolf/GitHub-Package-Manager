SwAT = '''
GHPM is a package manager, it effectively manages coding projects, applications, and anything else code-able! GHPM 
does not use any highly advanced coding techniques, much the opposite in fact. it uses basic, straight-forward 
logic, it is the lack of complication that makes this project the most light-weight Manager available.

Technical Information #9

GHPM Version = v1.3.0
ChangeUsername = v1.2
ChangePassword = v1.3
GitConnect = v2.3
EventTracker = v2.5
ErrorTracker = v1.0
EventDataBase = v1.1
Information File = v2.4/2.5
GitComplexConnect = v1.2
PackageInstaller = v3.6
RequirementsInstaller = v1.3
CommandLineConnect = v1.2 LocalConnect = v2.2
UserPass = v3.3
Password Implementation = v2.4
VersioningUpdator = v1.3
Password Encryption = v2.4
Previous Method = Salt & Hash & MAC & Login & Fernet
ReturnFunction = v2.1
BlockUntrusted = v1.1
BanUntrusted = v1.1
FirstUse = v2.3
UserProfile = v3.2
PackageActivator.py = v3.5
PackageUninstaller.py = v2.2
PackageSettings = v2.4
LoginFunction = v1.5
CacheConnect = v3.5
Menu = 8/8
Version Status = Fully Released v1.3.0
Version Date = February 5th, 2023
Developer = Smoke-wolf
Version Security = Secure

GUI -> v1.0

GUI = v1.1
GUIInstaller_Local = v1.0
GUIInstaller_GitHub = v1.0
GUIInstaller_Advanced = v1.0
GUIActivator_Local = v1.0
GUIActivator_GitHub = v1.0
GUIUninstaller_Complex = v1.0
GUIUninstaller_GitHub = v1.0
'''

Modules = ['os', 'platform', 'sys', 'time', 'socket', 'random', 'json', 'hashlib', 'base64','cryptography','tkinter','requests']

Functions_Settings = '''Settings Info:

The Manual Cache Management feature enables users to interact with system function as well as their own data. 
Resulting changes to the MCM files will depend on the privilege of the user, as well as the source of the 
alteration. (System changes will be implemented in (System.Drive), whereas user changes will be implemented 
in (Cache.USER))

Notation* 

Changes to System Settings will be reflected on package functionality and will result in changes to the user 
experience. However, changes made to User Settings may not directly affect the experience of the user.
(User Settings are related to Data Collection and Implementation) '''

CLI_COC = '''
To Launch The CLI, In your terminal all you need to do is run gh (arg)

examples:
    [gh -I https://github.com/SomeUser/Something.git] -> this installs the repo following -I
    [gh -IL  /Users/Someone/Something] -> this will import all of the files within the specified directory

======================================
    Help
    ====
    -I -> Install (arg<repo>)
    -IL -> Install Local (arg<dir>)

    -LA -> List All Installs
    -LL -> Launch Local Directory
    -LG -> Launch Git Project
    -LC -> Launch Advanced Projects

    -UG -> Uninstall GitHub Projects
    -UL -> Uninstall Local directories
'''
