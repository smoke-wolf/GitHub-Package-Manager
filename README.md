

# GitHub Package Manager Updates :zap:

> [!IMPORTANT]
> The biggest change: Windows support is now available!

### Highlights (Dec 1st, 2023)
----------

We're thrilled to announce significant updates to the **Git Listings**, marking the second in a series of upcoming changes.

1. **New Feature: [Upload Listing](https://maliq-barnard.vercel.app/gpm/upload_listing.html)**
   - Authenticated GHPM users can now create customized listings [1].

2. **Improved Recommendation Algorithm**
   - Now suggests listings based on your previous views. Expect segmentation-related algorithm enhancements soon [2].

3. **Member Benefits**
   - **[Official Members](https://ghpm.vercel.app/)** now have access to the **review feature** to evaluate downloads and usage of linked packages [3].
   - An enhanced website, primarily designed by syntaxerror, is now live [here](https://ghpm.vercel.app/).

4. **Upcoming Enhancements**
   - Expect significant improvements in website functionality and the account process.

5. **Account Management**
   - Users can now conveniently change passwords and delete accounts through the [**Account Settings**](https://smoke-wolf.vercel.app/gpm/accountsettings.html) page.

6. **Security Enhancements**
   - Database security has been fortified.

### Backend Updates
- **Recommendation Algorithm**: Implemented for personalized suggestions.
- **Git Listings Security**:
  - Profanity and malicious link protection implemented.
- **Account Security**:
  - Enhanced token authentication system for improved protection.
  - Added account username uniqueness and push authentication.
- **Token Management**:
  - Refresh rates for improved security and session management.

Stay tuned for more updates! :rocket:

# What we do :stars:

  > [!IMPORTANT]
> The biggest change: Windows support is now available!


GHPM was developed to address various challenges encountered by GitHub users. We achieve this by focusing on the client side of the GitHub interface. Instead of using the standard `git clone` command, we leverage the Git framework to ensure a standardized and efficient repository download process. Upon successfully obtaining the repository, our system offers invaluable support for building and configuring it through our integrated Dependency Manager (DM) and, most notably, our Entry Point Detection (EPD) feature.

After a successful installation, we continue to guide users in managing and modifying their installation profiles, including updates and reinstalls. The EPD process empowers users to swiftly create and execute applications within a controlled environment, supporting a wide array of commonly used programming languages. Furthermore, our DM is in the process of expanding to incorporate multi-language support, enhancing its versatility.


Whilst GHPM is made up of a small inner core mainly led by **Smoke-Wolf**, we are quick to incorporate any needed improvements and bug fixes. 

Thus far we uphold a stable application with support and an active development team. However, we welcome new members to join and provide their skills to improve the experience for everyone.

We are actively reviewing and monitoring suggestions and feedback, please provide any information on issues and inconveniences.
---



### :currency_exchange: Change Notes: v1.7.14 :currency_exchange:

 

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
 15. Windows Support completed :sparkle:

GHPM has been improving GitHub users' experience of the application for a while now, roughly since December 2022. 

We have made several changes throughout the last few weeks. A number of these changes are rather important for you to take note of.

To catch up on recent events and download the most recent secure version head over [HERE](https://ghpm.vercel.app/download).

-----

There are several goals we hope to achieve in the coming weeks. There will be a new look coming to ghpm, with some added os support!

Make sure to check back here for updates or [join the discord server](https://discord.gg/j95ghjqsz)!



-----
# Download GHPM Client

> [!IMPORTANT]
> The biggest change: Windows support is now available!

## Download Public Upload  :part_alternation_mark: :computer:


### Installation Instructions for MacOS / Linux _v1.5.x_

bashCopy code

`git clone https://github.com/smoke-wolf/GitHub-Package-Manager.git
cd GitHub-Package-Manager
python3 Start.py` 

Post-Account Notes:

bashCopy code

`python3 Start.py` 

## Current Release

### MacOS & Windows v1.7.x

The current version, v1.7.x, is exclusively available on the GHPM website. We'll soon upgrade to v1.8.x after verifying and authenticating the Windows implementations.

Upon the update to v1.8.x, anticipate the repository version to bump up to v1.7.x with added Windows support.
	
[DOWNLOAD GHPM HERE](https://ghpm.vercel.app/download)




  
Certainly! Here's an updated reference section, encompassing all the mentioned links:

----------

# Reference

### Account Related Links:

-   [Create a GHPM account](https://ghpm.vercel.app/create)
-   [Log in to your GHPM account](https://smoke-wolf.vercel.app/gpm/Login.html)
-   [Access Git Listings](https://smoke-wolf.vercel.app/gpm/listing.html)
-   [Account Settings](https://smoke-wolf.vercel.app/gpm/accountsettings.html)
-   [Download GHPM](https://ghpm.vercel.app/download)
-   [Join the Discord server](https://discord.gg/j95ghjqsz)

1.  Registered GHPM users can fill out a form to create a listing, which will appear on the GitListings webpage and desktop micro-app. Removal of a listed repository requires contact with **Smoke-Wolf**. For safety, avoid including personal details like real names, addresses, or identifying information. Descriptions and project names must refrain from any profanity. Once a repository is listed, it cannot be listed again, adding additional data is limited to authorized users (*get in contact*)

2. The latest alteration in the algorithm involves referencing user history based on their `REMOTE_IP`. However, this approach presents limitations. Physical movement or network interruptions can reset the algorithm's reference tied to a particular experience.

	Another concern arises from potential IP assignment issues in smaller networks. In such cases, previously profiled IPs might be assigned to devices that haven't undergone profiling yet. This discrepancy could lead to users receiving algorithm references that don't belong to them.

	The rationale behind utilizing `REMOTE_IP` is to maintain the public availability of the listings page without restrictions. However, transitioning to an account-based system would mitigate the second concern, ensuring personalized and accurate algorithm references for users.
    
3.  The GHPM review provides users with a unique dashboard displaying usage frequency, timing, and other insightful data. Additionally, it contributes to refining the git listings algorithm for better effectiveness.
