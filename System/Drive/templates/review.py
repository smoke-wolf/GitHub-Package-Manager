'''
The code initiates an analytics record, then runs a command to open a new Terminal window
and execute a Python script that launches a webpage using the osascript command and os.system().

-todo
    fix os dependancy for mac
'''

import os
import User.UserProfile as up
import System.Drive.Errors_Events.EventMan as AR

def main():
    AR.AnalyticsRecord(11)
    os.system(
        f'osascript -e \'tell application "Terminal" to do script "cd {up.SourceDirectory} &&python3 launchwebreview.py"\''
    )


