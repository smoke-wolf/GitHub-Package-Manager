
# GitHub Package Manager

  

## **update v1.3.2**
Bug Fixes: Out Of Date Menu and Other Fertures Of Legacy Version.\
Date: Feb 6th 2023
  

## Information
**GHPM** is a package manager for GitHub, it effectively manages coding projects, applications, and anything else code-able! **GHPM** does not use any highly advanced coding techniques, much the opposite in fact. it uses basic, straight-forward logic, it is the lack of complication that makes this project the most light-weight Manager available. Not only that, it is the first manager to allow for **Launching** of programs rather than solely installing them.

You now have access to the GUI, currently it is only available through the Function List. However, it will be linked in a separate repository.


  

Writeup(https://www.publishthis.email/github-package-manager-Bki9Ejbhi) here:

# Features
- [->] Install Packages Through GitHub [!] *Note Requires GitClone*
- [->] Link Local Directories To Package
- [->] Beta Data Lock // Encrypted Storage
- [->] Intuitive Configurations Search Package For Potential Launch Scripts
- [->] Install Complex Applications And Packages
- [->] Automatic Requirements Installation For Git Packages [!]*Note Requires pip*
- [->] Comprehensive Event Tracking [!]*Note Saved To System/Cache/System/ErrorLog*
- [->] Fluid Package Launches Using Launch Commands Configured Through Installation
- [->] Seamless Uninstallation For GitHub Installs And Local Imports *Note Deletes Directory*
- [->] Salt & Hash Based Encryption For Passwords [!]*Note There Is No Way To Reset Password*
- [->] Direct Cache Editing And Altering
- [->] Control System Settings And Personalization
- [->] All Of The Previous Are Now Doable Through The GUI

  
  
  

## Downloading & Installing

	git clone https://github.com/smoke-wolf/GitHub-Package-Manager.git
	cd GitHub-Package-Manager
	python3 Start.py

**First Use:**

When you first launch the application, you will be prompted to create a password and username. Once the profile has been created, run the following command.

  

	python3 Start.py
	or python Start.py

  

**GUI**

When you have downloaded a package, or connected a local repository, you will be able to access the GHPM-GUI. Simply enter **9** in the Function List.
## Updating Project

With the new **Versioning** feature as of v1.2.4, you are now able to seamlessly update your version to the newest avalable!

*As of v1.2.5 Version updates now ensure that your current version is compatable with newer updates.

**The Versioning Feature** It is displayed in the Feauture menu and does not require a password.

## [](https://github.com/smoke-wolf/GitHub-Package-Manager#goals--to-do)Goals & To Do

1.  SHA256 for files related to updates
2.  Allow Separate Profiles
3.  Add Better Listing Features
4.  Create GUI
5.  Add Third Party Integration
6.  Update Installed Repos
7.  Install APK & DMG Applications
8.  Smoothen Interfaces & Tidy Code
9.  Add automatic file additions with new versions -> Version update

### [](https://github.com/smoke-wolf/GitHub-Package-Manager#complete--v125)Complete -v1.2.6

1.  Add **Password** Reset Feature
2.  Completely updated versioning system

## [](https://github.com/smoke-wolf/GitHub-Package-Manager#known-errors)Known Errors

HOWEVER, if for whatever reason **Package Installer** errors after checkpoint [3:4] you may end up with a downloaded repo that has no launch command listed.

If any are found, email [Maliq.Barnard@gmail.com](mailto:Maliq.Barnard@gmail.com)


# Explanations & Tutorials

## Command Line Connection  

If you want to use the same features from the package without the hassle of using the main application. It is quite straightforward, within the main menu, you will head into Settings >User and select Enable Command Line Interface. This will enable the gh command:

examples:

[gh -I [https://github.com/SomeUser/Something.git](https://github.com/SomeUser/Something.git)] -> this installs the repo following -I

[gh -IL /Users/Someone/Something] -> this will import all of the files within the specified directory

Help

========================= 
-I -> Install (arg{repo})
-IL -> Install Local (arg{dir})
============ ============ 
-LA -> List All Installs
-LL -> Launch Local Directory
-LG -> Launch Git Project
-LC -> Launch Advanced Projects
============ ============ 
-UG -> Uninstall GitHub Projects
-UL -> Uninstall Local directories

## Installing Programs

When installing files from GitHub you will be asked to enter a GitHub repository Example:  [https://github.com/SomeUser/SomeRepo.git](https://github.com/SomeUser/SomeRepo.git)  After the package has downloaded, there will be a list of files within the repo

-   If the package requires no setup, select the value that corresponds with the Launch file. The interpreter will automatically be selected based on the type of file
    
-   If however, the package requires a more comprehensive installation (i.e. Requires a makefile, etc.) select 0 from the list. This will require you to add any special configuration commands.
    

After the package has been installed, a launch command will be written to [System/Cache/System/GitHub/Downloads/Int.txt] after the installation has been completed you will be free to launch the application through the Package Activator -> Github or Complex.

When importing local packages, it is the same process, however there is not yet a feature for complex installations.

## Launching Programs

Launching programs is simple, simply select the class from which your program is.

-   If you have downloaded a repo from GitHub, it will be displayed in [Package Activator -> Github]
    
-   If it has been installed through a complex installation, packages will be displayed in [Package Activator -> Complex]
    
-   Finally, if it has been imported through the local installation it will be displayed in [Package Activator -> Local]
    

When a GitHub program has completed there will be a message asking the form of exit, if an error with the program has caused it to exit, enter 2. if however, the program completed successfully, or you exited purposefully, enter 1.

The previous does not occur with local programs

## Uninstalling Programs

The process for uninstalling is the same as installing, once a package has been selected from either Local or GitHub it will be uninstalled and deleted from your profile. For GitHub there is no need to manually set complex or basic, it is all done autonomously.

## Updating

*When updating the file structure your GHPM client stays the same.

The VersionUpdate first retrieves the most recent version. It then compares your version for compatibility. If it is, Current files are erased and then updated with the contents of the previous version.

GHPM V1.2.6
# Publication Information

**Technical Information #9**
>GHPM Version = v1.3.0\
ChangeUsername = v1.2\
ChangePassword = v1.3\
GitConnect = v2.3\
EventTracker = v2.5\
ErrorTracker = v1.0\
EventDataBase = v1.1\
Information File = v2.4/2.5\
GitComplexConnect = v1.2\
PackageInstaller = v3.6\
RequirementsInstaller = v1.3\
CommandLineConnect = v1.2
LocalConnect = v2.2\
UserPass = v3.3\
Password Implementation = v2.4\
VersioningUpdator = v1.3\
Password Encryption = v2.4\
Previous Method = Salt & Hash & MAC & Login & Fernet\
ReturnFunction = v2.1\
BlockUntrusted = v1.1\
BanUntrusted = v1.1\
FirstUse = v2.3\
UserProfile = v3.2\
PackageActivator.py = v3.5\
PackageUninstaller.py = v2.2\
PackageSettings = v2.4\
LoginFunction = v1.5\
CacheConnect = v3.5\
Menu = 8/8\
Version Status = Fully Released v1.3.0\
Version Date = February 5th, 2023\
Developer = Smoke-wolf\
Version Security = Secure

  

*GUI -> v1.0*

>GUI = v1.1\
GUIInstaller_Local = v1.0\
GUIInstaller_GitHub = v1.0\
GUIInstaller_Advanced = v1.0\
GUIActivator_Local = v1.0\
GUIActivator_GitHub = v1.0\
GUIUninstaller_Complex = v1.0\
GUIUninstaller_GitHub = v1.0

  

*Crypt-> v1.1*

>Write_Data = v.1.0
Read_Data = v1.1
Delete_Data =v1.0
Read_File = v.1.0

  
  

[MORE INFO](https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/main/System/Cache/System/ErrorLog/Errors)
