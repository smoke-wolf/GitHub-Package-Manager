

# GitHub Package Manager

**GHPM** is a package manager for GitHub, it effectively manages coding projects, applications, and anything else code-able! **GHPM** does not use any highly advanced coding techniques, much the opposite in fact. it uses basic, straight-forward logic, it is the lack of complication that makes this project the most light-weight Manager available. Not only that, it is the first manager to allow for **Launching** of programs rather than solely installing them. 

# Features

 - [->] Install Packages Through GitHub [!] *Note Requires GitClone*
 - [->] Link Local Directories To Package
 - [->] Intuitive Configurations Search Package For Potential Launch Scripts
 - [->] Install Complex Applications And Packages
 - [->] Automatic Requirements Installation For Git Packages [!]*Note Requires pip*
 - [->] Comprehensive Event Tracking  [!]*Note Saved To System/Cache/System/ErrorLog*
 - [->] Fluid Package Launches Using Launch Commands Configured Through Installation
 - [->]  Seamless Uninstallation For GitHub Installs And Local Imports *Note Deletes Directory*
 - [->] Salt & Hash Based Encrypting For Passwords  [!]*Note There Is No Way To Reset Password*
 - [->] Direct Cache Editing And Altering 
 - [->] Control System Settings And Personalization 



## Downloading & Installing
    git clone https://github.com/smoke-wolf/GitHub-Package-Manager.git
    cd GitHub-Package-Manager
	python3 Start.py
**First Use:**
When you first launch the application, you will be prompted to create a password and username. Once the profile has been created, run the following command.

	python3 Start.py
	or python Start.py


## Updating Project 
When updating the application, you can save the contents of [**User/UserProfile.py**].
If you want to save the projects and repos installed through GitHub save the contents of [**System/Cache/System/GitHub/Downloads**] && [**Int.txt**] and [**Int2.txt**]. 

In the future I will aim to implement a versioning feature to allow for easier updates.

## Goals & To Do

 1.  Add **Password** Reset Feature
 2.  Allow Separate Profiles
 3.  Add Better Listing Features 
 4.  Create GUI
 5.  Add Third Party Integration
 6.  Update Installed Repos
 7. Install APK & DMG Applications 
 8. Smoothen Interfaces & Tidy Code
 9. Find A Solid Obfuscation Function

### Complete -v1.2.4
1.  Add Easier Versioning ---ADDED
2. Implement More Personalization settings ---ADDED
3. Improve Password Utilities ---ADDED
4. Allow For CL Installation ---ADDED

## Known Errors

*Watch out for your MAC address being added to the **Blocked** list <User/Blocked>*

HOWEVER, if for whatever reason **Package Installer** errors after checkpoint [3:4] you may end up with a downloaded repo that has no launch command listed.

If any are found, email Maliq.Barnard@gmail.com

# Explanations & Tutorials
A comprehensive and detailed walk-through for different features

## Command Line Connection
If you want to use the same features from the package without the hassel of using the main application. It is quite straight forward, within the main menu, you will head into **Settings >User** and select **Enable Command Line Interface**. This will enable the **gh** command:

**examples:**
> [gh -I https://github.com/SomeUser/Something.git] -> this installs the repo following -I 
> [gh -IL  /Users/Someone/Something] -> this will import all of the files within the specified directory
>**Help** 
=========================
-I -> Install (arg{repo})  
-IL -> Install Local (arg{dir})  
============  ============
-LA -> List All Installs  
-LL -> Launch Local Directory  
-LG -> Launch Git Project  
-LC -> Launch Advanced Projects  
 ============ ============
-UG -> Uninstall GitHub Projects  
-UL -> Uninstall Local directories

## Installing Programs
When installing files from GitHub you will be asked to enter a GitHub repository `Example: https://github.com/SomeUser/SomeRepo.git `
After the package has downloaded, there will be a list of files within the repo
>*  If the package requires no setup, select the value that corresponds with the Launch file. The interpreter will automatically be selected based on the type of file
>* If however, the package requires a more comprehensive installation (i.e. Requires a makefile, etc.) select **0** from the list. This will require you to add any special configuration commands.

After the package has been installed, a launch command will be written to [**System/Cache/System/GitHub/Downloads/Int.txt**] after the installation has been completed you will be free to launch the application through the **Package Activator -> Github or Complex**.

When importing **local packages**, it is the same process, however there is not yet a feature for **complex installations**.

## Launching Programs
Launching programs is simple, simply select the class from which your program is.
* If you have downloaded a repo from **GitHub**, it will be displayed in [**Package Activator -> Github**]
* If it has been installed through a **complex** installation, packages will be displayed in [**Package Activator -> Complex**]
* Finally, if it has been imported through the **local** installation it will be displayed in [**Package Activator -> Local**]

When a GitHub program has complete there will be a message asking the form of exit, if an error with the program has caused it to exit, enter **2**. if however, the program completed successfully, or you exited purposefully, enter **1**.

The previous does not occur with **local** programs

## Uninstalling Programs
The presses for **uninstalling** is the same as installing, once a package has been selected from either **Local** or **GitHub** it will be uninstalled and deleted from your profile. For **GitHub** there is no need to manually set complex or basic, it is all done autonomously. 


# Publication Information 


**Technial Information #6**
>GHPM Version = v1.2.4\
GitConnect = v2.3\
Information File = v2.3\
GitComplexConnect = v1.2\
PackageInstaller = v3.4\
RequirementsInstaller = v1.3\
CommandLineConnect = v1.0
LocalConnect = v2.1\
UserPass = v3.1\
Password Implementation = v2.2\
VersioningUpdator = v1.0\
Password Encryption = v2.2\
Previous Method = Salt & Hash & MAC & Login\
ReturnFunction = v2.1\
FirstUse = v2.2\
UserProfile = v3.2\
PackageActivator.py = v3.4\
PackageUninstaller.py = v2.1\
PackageSettings = v2.3\
LoginFunction = v1.3\
CacheConnect = v3.3\
Menu = 7/7\
Version Status = Fully Released\
Version Date = January 4th, 2023\
Developer = Smoke-wolf\
Version Security = Secure

**Technical Information #5**
>=====================\
GHPM Version = v1.2.3\
GitConnect = v2.2\
Information File = v2.3\
GitComplexConnect = v1.1\
PackageInstaller = v3.3\
RequirementsInstaller = v1.3\
LocalConnect = v2.0\
UserPass = v3.0\
Password Implementation = v2.1\
Password Encryption = v2.1\
Previous Method = Salt & Hash\
ReturnFunction = v2.1\
FirstUse = v2.1\
UserProfile = v3.1\
PackageActivator.py = v3.3\
PackageUninstaller.py = v2.0\
PackageSettings = v2.2\
LoginFunction = v1.2\
CacheConnect = v3.2\
Menu = 7/7\
Version Status = Fully Released\
Version Date = December 27 2022\
Developer = JDX50S, Smoke-wolf\
Version Security = Secure

**Technical Information #4**
>=====================\
SwAT Version = v1.2.2\
GitConnect = v2.0\
LocalConnect = v2.0\
UserPass = v2.2\
ReturnFunction = v2.1\
PackageActivator.py = v3.2\
PackageUninstaller.py = v1.0\
Menu = 7/8\
Version Status = Fully Released\
Version Date = December 12, 2022\
Developer = JDX50S, Smoke-wolf\
Version Security = Secure\


**Technical Information #3**
>=====================\
SwAT Version = v1.0.0\
GitConnect = v1.0\
LocalConnect = v1.0\
UserPass = v2.2\
ReturnFunction = v2.1\
PackageActivator.py = v2.2\
Menu = 6/8\
Version Status = Released\
Version Date = December 10, 2022\
Developer = JDX50S, Smoke-wolf\
Version Security = Secure


**Technical Information #2**
>=====================\
SwAT Version = v0.3.1\
GitConnect = v1.0\
LocalConnect = v1.0\
UserPass = v2.2\
Menu = 5/8\
Version Status = -BetaRelease\
Version Date = December 9, 2022\
Developer = JDX50S, Smoke-wolf\
Version Security = Secure


**Technical Information #1**
>=====================\
SwAT Version = 0.0.1\
Version Status = Development\
Version Date = Development\
Developer = JDX50S\
Version Security = Unsure

