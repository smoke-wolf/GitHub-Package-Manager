
# GitHub Package Manager

## quick install
### MacOS and Linux
	git clone https://github.com/smoke-wolf/GitHub-Package-Manager.git
	cd GitHub-Package-Manager
	python3 Start.py
### Windows
	git clone https://github.com/smoke-wolf/GitHub-Package-Manager-Windows-.git
	cd GitHub-Package-Manager-Windows-
	python3 Start.py
	
**First Use:**

When you first launch the application, you will be prompted to create a password and username. Once the profile has been created, run the following command.

  

	python3 Start.py

## **update v1.3.3**
Bug Fixes:
- Complex / Advanced Programs failed to install through GUI
- Programs also fail to launch after installation. 
- Settings Returning null/unavailable status

Resolve: 
- GUI Settings Updated 
- Settings / CLI access channelling
- Project restructuring for stand-alone gui compatibility
- Advanced Application Support (GitHub stand-alone)
- Gui simple installation optimized for complex installations

Date: Feb 13th 2023
  

## Information
**GHPM** is a package manager for GitHub, it effectively manages GitHub packages and local directories and file paths. **GHPM** uses strategic logic to install packages with the intent of organising, compiling, and recalling in the future. Packages downloaded are passed through our system to allow for the most user-friendly interface, whereafter the downloaded package can be compiled with minimal struggle. Requirements and other prereqs are handled automatically through GitHub Installations to mitigate preventable exits and errors.

GHPM stands unparalleled to other currently available GitHub PMs, with the primary differentiating feature being the seamlessly user-free installation of applications and projects. With GHPM, all packages are handled with intent and are contained to allow for simple execution in future instances. Other package managers such as ***Huber*** which handles and lists installed packages still have fundamental limitations such as using free installation on large ranges of applications. 

This project *used* to be the most lightweight gh Manager available. Not only that, it is the first manager to allow for cross-instance reference of programs rather.



*You now have access to the GUI, currently it is only available through the Function List. However, it will be linked to a separate repository.*


# Features 1.3.3
 - [->] Cross Version Support *Post v1.2.4*
 - [->] Systematic Application Scraping
 - [->] Password Reset & Account flexibility
 - [->] Structures and Skeletons (*Allow Compileable Application*)
- [->] Install Packages Through GitHub [!] *Note Requires GitClone*
- [->] Link Local Directories To Package
- [->] Embedded DataLogic Prevents Cross UU?D (*User / Device*)
- [->] Beta Data Lock // Encrypted Storage
- [->] Intuitive Configurations Search Package For Potential Launch Scripts
- [->] Install Complex Applications And Packages
- [->] Automatic Requirements Installation For Git Packages [!]*Note Requires pip*
- [->] Comprehensive Event Tracking [!]*Note Saved To System/Cache/System/ErrorLog*
- [->] Fluid Package Launches Using Launch Commands Configured Through Installation
- [->] Seamless Uninstallation For GitHub Installs And Local Imports *Note Deletes Directory*
- [->] Salt & Hash-Based Encryption For Passwords 
- [->] Direct Cache Editing And Altering
- [->] Control System Settings And Personalization
- [->] All Of The Previous Are Now Doable Through The GUI

  
  
  

## Installing 
### GUI
The build for a GUI has been embedded under **9** in the Function List. Activating the GUI gives the user a backend-connected interface with all features found within the CLI. 

*IF* 
	
	./ghpm -> Command Not Found
			
-> GUI will only be accessible within option **9**

*ELSE*
	./ghpm -> Succsesful
			
-> The created **ghpm** executable will be movable everywhere regardless of whether or not it is within the GitHub-Package-Manager directory. 
## Updating Project

**The Versioning Feature**  is displayed in the Feature menu and does not require a password.

With the new **Versioning** feature as of v1.2.4, you are now able to seamlessly update your version to the newest available! 

*As of v1.2.5 Version updates now ensure that your current version is compatible with newer updates.



## Goals & To Do -<Up#v3.3>

1.  SHA256 for files related to updates
2. Cross-Platform Compatability *Requires Windows Update*
3.  Logging and Monitoring (*Solve Errors Intuitivly*)
4.  API account connection and development
5.  Add Third Party Integration
6.  Update Installed Repos
7.  Install APK & DMG Applications
8.  Handle requirements within Local Installations
9.  Reconfigure File Security / Storage with *pyminizip*
10. Patch Null Install / Failed Cleanup for Installations 

### Complete -v1.3.3
1. Allow Separate Profiles (*Profile Locking Built-In*)
2. Create GUI (*v1.1.0*)
3. Smoothen Interfaces & Tidy Code (*Patches and Corrections*)
4. automatic file additions with new versions (*Version Updates facilitate new data*)
5. Add Better Listing Features (*Patched in GUI*)

## Known Errors
If **Package Installer** errors after checkpoint [3:4] you may end up with a downloaded repo that has no launch command listed.

if there is an error being raised in the Windows version: head to the User/UserProfile.py and make sure that the backslashes are doubled up in the SourceDirectory.


If any are found, email [Maliq.Barnard@gmail.com](mailto:Maliq.Barnard@gmail.com)
or checkout out docs on [contributing](https://github.com/smoke-wolf/GitHub-Package-Manager/blob/main/CONTRIBUTING.md)

# Explanations & Tutorials

## Command Line Connection  

If you want to use the same features from the package without the hassle of using the main application. It is quite straightforward, within the main menu, you will head into Settings >User and select Enable Command Line Interface. This will enable the gh command:

examples:

[gh -I [https://github.com/SomeUser/Something.git](https://github.com/SomeUser/Something.git)] -> this installs the repo following -I\

[gh -IL /Users/Someone/Something] -> this will import all of the files within the specified directory\

Help\

========================= \
-I -> Install (arg{repo})\
-IL -> Install Local (arg{dir})\
========================= \
-LA -> List All Installs\
-LL -> Launch Local Directory\
-LG -> Launch Git Project\
-LC -> Launch Advanced Projects\
========================= \
-UG -> Uninstall GitHub Projects\
-UL -> Uninstall Local directories\

## Installing Programs

When installing files from GitHub you will be asked to enter a GitHub repository Example:  [https://github.com/SomeUser/SomeRepo.git](https://github.com/SomeUser/SomeRepo.git)  After the package has downloaded, there will be a list of files within the repo

-   If the package requires no setup, select the value that corresponds with the Launch file. The interpreter will automatically be selected based on the type of file
    
-   If however, the package requires a more comprehensive installation (i.e. Requires a makefile, etc.) select 0 from the list. This will require you to add any special configuration commands.
    

After the package has been installed, a launch command will be written to [System/Cache/System/GitHub/Downloads/Int.txt] after the installation has been completed you will be free to launch the application through the Package Activator -> Github or Complex.

When importing local packages, it is the same process, however, there is not yet a feature for complex installations.

## Launching Programs

Launching programs is simple, simply select the class from which your program is.

-   If you have downloaded a repo from GitHub, it will be displayed in [Package Activator -> Github]
    
-   If it has been installed through a complex installation, packages will be displayed in [Package Activator -> Complex]
    
-   Finally, if it has been imported through the local installation it will be displayed in [Package Activator -> Local]
    

When a GitHub program has been completed there will be a message asking for the form of exit, if an error with the program has caused it to exit, enter 2. if however, the program completed successfully, or you exited purposefully, enter 1.

The previous does not occur with local programs

## Uninstalling Programs

The process for uninstalling is the same as installing, once a package has been selected from either Local or GitHub it will be uninstalled and deleted from your profile. For GitHub there is no need to manually set complex or basic, it is all done autonomously.

## Updating

*When updating your GHPM client stays the same.

The VersionUpdate first retrieves the most recent version. It then compares your version for compatibility. If it is, Current files are erased and then updated with the contents of the previous version.

## GUI
The build for a GUI has been embedded under **9** in the Function List. Activating the GUI gives the user a backend-connected interface with all features found within the CLI. 

*IF* 
	
	./ghpm -> Command Not Found
			
-> GUI will only be accessible within option **9**

*ELSE*
	./ghpm -> Succsesful
			
-> The created **ghpm** executable will be movable everywhere regardless of whether or not it is within the GitHub-Package-Manager directory. 

### Aditional Support
 *Will be added later*
# Publication Information

**Technical Information #10**
>GHPM Version = v1.3.3\
ChangeUsername = v1.2\
ChangePassword = v1.3\
GitConnect = v2.3\
EventTracker = v2.5\
ErrorTracker = v1.1\
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
Version Status = Fully Released v1.3.3\
Version Date = February 13th, 2023\
Developer = Smoke-wolf\
Version Security = Secure

  

*GUI -> v1.2*

>GUI = v1.2\
GUIInstaller_Local = v1.0\
GUIInstaller_GitHub = v1.0\
GUIInstaller_Advanced = v1.1\
GUIActivator_Local = v1.0\
GUIActivator_GitHub = v1.0\
GUIUninstaller_Complex = v1.1\
GUIUninstaller_GitHub = v1.0\
GUISettings = v1.6

  

*Crypt-> v1.1*\
>Write_Data = v.1.0\
Read_Data = v1.1\
Delete_Data =v1.0\
Read_File = v.1.0

  
  
_________

[MORE INFO](https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/main/System/Cache/System/ErrorLog/Errors)
