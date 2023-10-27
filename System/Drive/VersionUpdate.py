'''
This script is designed to manage updates for a GitHub Package Manager (GHPM) application.
It starts by attempting to remove a specific directory related to cached update data.
The script then checks for compatibility information by sending a GET request to a URL
and compares it to the current version of the application. If a new version is available,
it displays an information dialog to notify the user and proceeds to fetch the new version
and related files. It then changes the working directory to a specific location and uses git
to clone the "UPDATE" branch of the GitHub repository to update the application's files.
Finally, it opens a new Terminal window and runs a Python script to relaunch the updated application,
ensuring that users are using the latest version of the GitHub Package Manager.

Apply changes to accept Windows OS an it's filepath system.

-Revised Monday, October 3, 2023
'''


#    Please download the verifyed version
