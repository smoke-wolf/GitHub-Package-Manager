
# GitHub Package Manager


## Bug Fixes v1.3.7
issues with uninstaller and settings, installer bug patched as well.

GHPM is a powerful package manager for GitHub that helps users to organize, compile, and recall packages with ease.

It offers a user-friendly interface, and packages are downloaded and compiled with minimal struggle. GHPM automatically handles requirements and other prerequisites, making it easier for users to install applications and projects.

Compared to other GitHub package managers, GHPM offers unparalleled features such as cross-instance reference of programs, and it's the most lightweight manager available.

Whether you're a beginner or an experienced programmer, GHPM offers the tools you need to take your programming experience to the next level.

## quick install
### MacOS and Linux *v1.3.6*
	git clone https://github.com/smoke-wolf/GitHub-Package-Manager.git
	cd GitHub-Package-Manager
	python3 Start.py
### Windows *v1.3.3*
	git clone https://github.com/smoke-wolf/GitHub-Package-Manager-Windows-.git
	cd GitHub-Package-Manager-Windows-
	python3 Start.py
	
**First Use:**

#### *Recomended to checkout this [documentation](https://github.com/smoke-wolf/GitHub-Package-Manager/wiki)*
When you first launch the application, you will be prompted to create a password and username. Once the profile has been created, run the following command.

	python3 Start.py

## Version 1.3.6 Patch Notes

-   Settings Issue #BFPER: The GUI implementation of the settings did not load correctly.
-   DisplayEvents Issue #PNCFM: Display events were fixed to True, but the toggle switch did not work.
    -   **Patch:** Fixed an arbitrary boolean of DisplayEvents to False.
-   ChangeUsername Issue #CBQPK: The change password feature did not implement the new password to the UserProfile.
    -   **Patch:** Dependent implementation of 'os.getcwd()' was replaced with User.UserProfile.SourceDirectory.
-   Critical Launch Issue #FMGHH: The user could log in even if the password was entered incorrectly. However, if the password was entered incorrectly and then correctly, the GUI failed to launch.
    -   **Description:** If the password was entered correctly the first time, the GUI launched without issue. If the password was entered incorrectly and then correctly, the GUI failed.
-    Systemic Installer Issue #SBDSS: An installer error occurred after extensive use of the package.\
    -   **Patch:** When installing, the program would `os.chdir` into the installed application, thus making any more `os.getcwd()` calls incorrect in regards to the current location. Dependent implementation of 'os.getcwd()' was replaced with User.UserProfile.SourceDirectory.
-   Uninstaller Issue #CRKAJ: The uninstaller failed to remove the directory, but successfully removed the address within Int.txt.
    -   **Patch:** Dependent implementation of 'os.getcwd()' was replaced with User.UserProfile.SourceDirectory.
-   Activator Error Issue #CHBEJ: When activating, the program would `os.chdir` into the activated application, thus making any more `os.getcwd()` calls incorrect in regards to the current location.
    -   **Patch:** Dependent implementation of 'os.getcwd()' was replaced with User.UserProfile.SourceDirectory.
Date: March 11th 2023


## Publication Info
**Technical Information #12**
>GHPM Version = v1.3.6\
ChangeUsername = v2.0\
ChangePassword = v1.4\
GitConnect = v2.5\
EventTracker = v3.0\
EventDataBase = v1.1\
Information File = v2.4/2.5\
GitComplexConnect = v1.4\
PackageInstaller = v3.8\
RequirementsInstaller = v1.5\
CommandLineConnect = v1.3\
LocalConnect = v2.4\
UserPass = v3.4\
Password Implementation = v3.0\
VersioningUpdator = v1.3\
Password Encryption = v2.4\
Previous Method = Salt & Hash & MAC & Login & Fernet\
Global DataLock = v1.0\
ReturnFunction = v2.1\
BlockUntrusted = v1.1\
BanUntrusted = v1.1\
FirstUse = v2.4\
UserProfile = v3.3\
PackageActivator.py = v3.6\
PackageUninstaller.py = v2.3\
PackageSettings = v2.5\
LoginFunction = v2.0\
CacheConnect = v3.6\
Menu = 8/8\
Version Status = Fully Released v1.3.6\
Version Date = March 11th, 2023\
Developer = Smoke-wolf\
Version Security = Secure

  

*GUI -> v1.4*
>GUI = v1.4\
GUIInstaller_Local = v1.3\
GUIInstaller_GitHub = v1.4\
GUIInstaller_Advanced = v1.4\
GUIActivator_Local = v1.4\
GUIActivator_GitHub = v1.5\
GUIUninstaller_Complex = v1.3\
GUIUninstaller_GitHub = v1.3\
GUICommand_LineConnet = v1.3\
GUIUser_Authentication = v1.2\
GUISettings = v2.0

  
  
_________

[MORE INFO](https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/main/System/Cache/System/ErrorLog/Errors)
