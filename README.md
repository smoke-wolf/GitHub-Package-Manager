


# GitHub Package Manager  :low_brightness:


### Today's Highlights (Nov 25th, 2023)

----------

We've implemented a significant update to the **Git Listings** today, marking the first of several upcoming changes. Alongside this, we've introduced a new feature called **[Upload Listing](https://maliq-barnard.vercel.app/gpm/upload_listing.html)**, allowing authenticated GHPM users to create their own customized listings [1].

Our **[official members](https://maliq-barnard.vercel.app/ghpm_download.html)** now have access to a new feature called **review**, enabling them to assess their downloads and usage of linked packages [2].

Moreover, members can now conveniently manage their accounts online by changing passwords and deleting accounts via the [**Account Settings**](https://maliq-barnard.vercel.app/gpm/accountsettings.html) page.

Enhancements in account security have been implemented by fortifying the website's database. On the front end, we're actively engaged in a redesign, striving for a more appealing and user-friendly web app and website interface!

**Backend Stuff**
-
- The Account Security Has Been Significantly Improved
- Locked down CORS requests
-  Upload your repos to [**Git Listings**](https://maliq-barnard.vercel.app/gpm/listing.html)
 - We've added account anonymity from the client-side connections. 
 - The security has been improved with some changes to the token authentication system. (extended the length to 32 bytes)
 - Account username protection has been implemented (usernames are unique)
 - Push Authentication; We've been able to prevent incorrect log allocations from the client through token authentication. 
 - Token refresh rates: Each session is under a new token, however, a session can only be initiated through the web app, local devices refresh the saved token state for event pushes. 
 

# What we do :stars:
  
GHPM was developed to address various challenges encountered by GitHub users. We achieve this by focusing on the client side of the GitHub interface. Instead of using the standard `git clone` command, we leverage the Git framework to ensure a standardized and efficient repository download process. Upon successfully obtaining the repository, our system offers invaluable support for building and configuring it through our integrated Dependency Manager (DM) and, most notably, our Entry Point Detection (EPD) feature.

After a successful installation, we continue to guide users in managing and modifying their installation profiles, including updates and reinstalls. The EPD process empowers users to swiftly create and execute applications within a controlled environment, supporting a wide array of commonly used programming languages. Furthermore, our DM is in the process of expanding to incorporate multi-language support, enhancing its versatility.


Whilst GHPM is made up of a small inner core mainly led by **Smoke-Wolf**, we are quick to incorporate any needed improvements and bug fixes. 

Thus far we uphold a stable application with support and an active development team. However, we welcome new members to join and provide their skills to improve the experience for everyone.

We are actively reviewing and monitoring suggestions and feedback, please provide any information on issues and inconveniences.
---



### :currency_exchange: Change Notes: v1.7.0 :currency_exchange:

 

 1. Updated UI
 2. More Secure Accounts
 3. Easier Support with **Send Logs**  :sparkle:
 4. Faster & More Reliable Updates
 5. Small Bugs Fixed In Settings
 6. Post Installation Editing
 7. Small bugs fixed in "activate"
 8. installer features added
 9. Better Bug Logging
 10. Browse Community Projects with **GhPm Recommended**  :sparkle:
 11. Faster Event Monitoring **We've got 'er down to 0.3s	:pray:**
 12. Significantly improved network connectivity redundancies
 13. Reworked checksum fetch structure
 14. Linux support is actively being implemented!
 15. Windows Development in work

GHPM has been improving GitHub users' experience of the application for a while now, roughly since December 2022. 

We have made several changes throughout the last few weeks. A number of these changes are rather important for you to take note of.

To catch up on recent events and download the most recent secure version head over [HERE](https://maliq-barnard.vercel.app/ghpm_download.html).

-----

There are several goals we hope to achieve in the coming weeks. There will be a new look coming to ghpm, with some added os support!

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



# Reference

-   To create a GHPM account, click [here](https://maliq-barnard.vercel.app/ghpm_download.html).
-   Log in to your GHPM account [here](https://maliq-barnard.vercel.app/gpm/Login.html).
-   View Git Listings [here](https://maliq-barnard.vercel.app/gpm/listing.html).
-   Access Account Settings [here](https://maliq-barnard.vercel.app/gpm/accountsettings.html).

1.  Registered GHPM users can fill out a form to create a listing, which will appear on the GitListings webpage and desktop micro-app. Removal of a listed repository requires contact with **Smoke-Wolf**. For safety, avoid including personal details like real names, addresses, or identifying information. Descriptions and project names must refrain from any profanity. Once a repository is listed, it cannot be relisted.
    
2.  The GHPM review provides users with a unique dashboard displaying usage frequency, timing, and other insightful data. Additionally, it contributes to refining the git listings algorithm for better effectiveness.
