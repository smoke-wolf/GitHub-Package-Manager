


# GitHub Package Manager  :low_brightness:

### What's Cracking Today
-----
We have released a new development branch of the updated gui for testing. We will soon be releasing a beta version for **[official members](https://maliq-barnard.vercel.app/ghpm_download.html)**. As of yesterday changes were implemented to improve server connectivity and reduce some excruciating waits with the logger. 

**Backend Stuff**

 - We've added account anonymity from the client-side connections. 
 - The security has been improved with some changes to the token authentication system. (extended the length to 32 bytes)
 - Account username protection has been implemented (usernames are unique)
 - Push Authentication; We've been able to prevent incorrect log allocations from the client through token authentication. 
 - Token refresh rates: Each session is under a new token, however, a session can only be initiated through the webapp, local devices refresh the saved token state for event pushes. 
 

# What we do :stars:
  
GHPM was developed to address various challenges encountered by GitHub users. We achieve this by focusing on the client side of the GitHub interface. Instead of using the standard `git clone` command, we leverage the Git framework to ensure a standardized and efficient repository download process. Upon successfully obtaining the repository, our system offers invaluable support for building and configuring it through our integrated Dependency Manager (DM) and, most notably, our Entry Point Detection (EPD) feature.

After a successful installation, we continue to guide users in managing and modifying their installation profiles, including updates and reinstalls. The EPD process empowers users to swiftly create and execute applications within a controlled environment, supporting a wide array of commonly used programming languages. Furthermore, our DM is in the process of expanding to incorporate multi-language support, enhancing its versatility.


Whilst GHPM is made up of a small inner core mainly led by **Smoke-Wolf**, we are quick to incorporate any needed improvements and bug fixes. 

Thus far we uphold a stable application with support and an active development team. However, we welcome new members to join and provide their skills to improve the experience for everyone.

We are actively reviewing and monitoring suggestions and feedback, please provide any information on issues and inconveniences.
---



### :currency_exchange: Change Notes: v1.7.0 :currency_exchange:

 

 1. Updated UI
 2. Easier Support with **Send Logs**  :sparkle:
 3. Faster & More Reliable Updates
 4. Small Bugs Fixed In Settings
 5. Post Installation Editing
 6. Small bugs fixed in "activate"
 7. installer features added
 8. Better Bug Logging
 9. Browse Community Projects with **GhPm Recommended**  :sparkle:
 10. Faster Event Monitoring **We've got 'er down to 0.3s	:pray:**
 11. Significantly improved network connectivity redundancies
 12. Reworked checksum fetch structure
 13. Linux support is actively being implemented!
 14. Windows Development in work

GHPM has been improving GitHub users' experience of the application for a while now, roughly since December 2022. 

We have made several changes throughout the last few weeks. A number of these changes are rather important for you to take note of.

To catch up on recent events and download the most recent secure version head over [HERE](https://maliq-barnard.vercel.app/ghpm_download.html).

-----

There are several goals we hope to achieve in the coming weeks. There will be a new look coming to ghpm, with some added os support!!!

Make sure to check back here for updates or [join the discord server](https://discord.gg/j95ghjqsz)!



-----
# Download GHPM Client

## Download Public Upload  :part_alternation_mark: :computer:

### MacOS / Linux *v1.5.x*
	git clone https://github.com/smoke-wolf/GitHub-Package-Manager.git
	cd GitHub-Package-Manager
	python3 Start.py
	
Post-Account notes:
`python3 Start.py `

## Current Release
### MacOS /Linux v1.7.x
This version is currently only available through the GHPM website.
	
### Download For Free With The Following Link
	
	Download From The Following Link: https://maliq-barnard.vercel.app/ghpm_download
	
[DOWNLOAD GHPM HERE](https://maliq-barnard.vercel.app/ghpm_download.html)
