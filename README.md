GitHub Package Manager Updates ⚡️
=================================

### Highlights (Dec 12th, 2023)

* * * * *

 
> [!NOTE]\
> Please raise an issue. If any errors are occurring, it will significantly improve our response times. thumbs_up:

1.  **Upload Listing Feature**

    -   Authenticated GHPM users now have the ability to create customized listings [1].
2.  **Improved Recommendation Algorithm**

    -   Enjoy personalized listing suggestions based on your viewing history. Further segmentation enhancements are on the horizon [2].
3.  **Member Benefits**

    -   Official members on [GHPM](https://ghpm.vercel.app/) now have access to review features to assess downloads and package usage [3].

    -   The website has been revamped, primarily designed by SyntaxError. Check it out [here](https://ghpm.vercel.app/).

    -   Windows Support (we've added significant support for the first-use protocol, as it has had issues *and still may*)

        -   However, the core functionality works completely without any issues.
            -   The worst comes to the worst. edit a few strings in the user profile to get it working.
    -   Connections to the GHPM online network

        -   Listings
        -   Event Tracking
        -   Faster issue support
    -   Smoother and faster response times for elements and functions

        -   Event processing to x < 0.1 of a second (run through MPS)
            -   multi-process systems
    -   Hugely improved development and versioning frameworks

        -   You'll get some cool perks relating to version swapping and transferring.
    -   Non-git-dependent architecture

        -   This is huge for the following:
            -   BetterGitClone (**BGC**) provides some dope benefits to `git clone.`
                -   `gi {repo}`
                -   It is written in under 150 lines of code.
                    -   It is only dependent on the requests library and could easily be swapped to only rely on curl.
                    -   It allows for automatic branch selection (it'll ask you what branch).
                        -   Commit selection (allow a maximum of 30 *potentially more*) versions to select and download.
        -   ***Note: Currently, the Branch Selection and Commit Section have not been integrated and will be soon.***
            -   A URL will be provided for the **BGC** project; however, as it is not yet publicly available, it cannot be completely integrated with GHPM.
                -   Currently, it will give users the option to use it or git clone; if they use BGC, it will do the equivalent of a base clone into the main branch on the most recent commit.
4.  **Backend Improvements**

    -   Efficiencies were introduced in various areas, including GHPM ads.
        -   The Subtle Boost Algorithm (SBA) was introduced for targeted ad boosts aligned with user interests.
        -   The Obvious Boost Ads (OBA) framework expanded, offering more templates for diverse ad styles.
    -   Enhanced listing capabilities for different user tiers:
        -   Default users have no upload limits but cannot add additional data or re-upload existing repositories.
        -   Paid users gain access to extra data for ads.
        -   Partners and contributors can apply for color-enhanced articles, boosting their reputation and appeal.
5.  **Account Management**

    -   Users can now perform account actions within the webapp via the [Account Settings](https://smoke-wolf.vercel.app/gpm/accountsettings.html) page.
    -   Actions include account deletion, deleting uploaded listings, and more.
6.  **Security Enhancements**

    -   Backend rewriting is ongoing for improved security. Stay tuned for further updates.
    -   Token session timeouts and IP locking were implemented as added security measures.

### Backend Updates Summary:

-   **Recommendation Algorithm**: Personalized suggestions are implemented.
-   **Git Listings Security**:
    -   Protection against profanity and malicious links.
-   **Account Security**:
    -   Enhanced token authentication and username uniqueness.
-   **Token Management**:
    -   Refresh rates are optimized for better security and session management.\
        Stay tuned for more updates! 🚀

What we do 🌠
=============

> [!IMPORTANT]\
> The biggest change: Windows support is now available!

GHPM was developed to address various challenges encountered by GitHub users. We achieve this by focusing on the client side of the GitHub interface. Instead of using the standard `git clone` command, we leverage the Git framework to ensure a standardized and efficient repository download process. Upon successfully obtaining the repository, our system offers invaluable support for building and configuring it through our integrated Dependency Manager (DM) and, most notably, our Entry Point Detection (EPD) feature.

After a successful installation, we continue to guide users in managing and modifying their installation profiles, including updates and reinstalls. The EPD process empowers users to swiftly create and execute applications within a controlled environment, supporting a wide array of commonly used programming languages. Furthermore, our DM is in the process of expanding to incorporate multi-language support, enhancing its versatility.

While GHPM is made up of a small inner core, mainly led by **Smoke-Wolf**, we are quick to incorporate any needed improvements and bug fixes.

Thus far, we have upheld a stable application with support and an active development team. However, we welcome new members to join and provide their skills to improve the experience for everyone.

We are actively reviewing and monitoring suggestions and feedback; please provide any information on issues and inconveniences.
-------------------------------------------------------------------------------------------------------------------------------

GHPM has been improving GitHub users' experience of the application for a while now, roughly since December 2022.

We have made several changes throughout the last few weeks. A number of these changes are rather important for you to take note of.

To catch up on recent events and download the most recent secure version, head over [here](https://ghpm.vercel.app/download).

* * * * *

There are several goals we hope to achieve in the coming weeks. There will be a new look coming to GHPM, with some added OS support!

Make sure to check back here for updates or [join the Discord server](https://discord.gg/h8mzeuFBjF)!

* * * * *

Download the GHPM client.
=========================

> [!IMPORTANT]\
> The biggest change: Windows support is now available!

Download Public Upload 〽️ 💻
----------------------------

### Installation Instructions for MacOS and Linux *v1.5.x*

bashCopy code

`git clone https://github.com/smoke-wolf/GitHub-Package-Manager.git cd GitHub-Package-Manager`

`  python3 Start.py``

or oneline it!

`git clone https://github.com/smoke-wolf/GitHub-Package-Manager.git && cd GitHub-Package-Manager and Python 3 Start.py`

Post-Account Notes:\
You may need to rerun this.\
`python3 Start.py`
--------------------------------------------------------------------

Reference
=========

### Account-Related Links:

-   [Create a GHPM account.](https://ghpm.vercel.app/create)
-   [Log in to your GHPM account.](https://smoke-wolf.vercel.app/gpm/Login.html)
-   [Access Git Listings](https://smoke-wolf.vercel.app/gpm/listing.html)
-   [Account Settings](https://smoke-wolf.vercel.app/gpm/accountsettings.html)
-   [Download GHPM](https://ghpm.vercel.app/download)
-   [Join the Discord server.](https://discord.gg/j95ghjqsz)

1.  Registered GHPM users can fill out a form to create a listing, which will appear on the GitListings webpage and desktop micro-app. Removal of a listed repository requires contact with **Smoke-Wolf**. For safety, avoid including personal details like real names, addresses, or identifying information. Descriptions and project names must refrain from any profanity. Once a repository is listed, it cannot be listed again; adding additional data is limited to authorized users (*get in contact).*

2.  The latest alteration in the algorithm involves referencing user history based on their `REMOTE_IP`. However, this approach presents limitations. Physical movement or network interruptions can reset the algorithm's reference to a particular experience.

    Another concern arises from potential IP assignment issues on smaller networks. In such cases, previously profiled IPs might be assigned to devices that haven't undergone profiling yet. This discrepancy could lead to users receiving algorithm references that don't belong to them.

    The rationale behind utilizing `REMOTE_IP` is to maintain the public availability of the listings page without restrictions. However, transitioning to an account-based system would mitigate the second concern, ensuring personalized and accurate algorithm references for users.

3.  The GHPM review provides users with a unique dashboard displaying usage frequency, timing, and other insightful data. Additionally, it contributes to refining the git listing algorithm for better effectiveness.
