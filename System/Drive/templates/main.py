import os
import User.UserProfile as up
import System.Drive.Errors_Events.EventMan as AR

def main():
    AR.AnalyticsRecord(11)
    os.system(
        f'osascript -e \'tell application "Terminal" to do script "cd {up.SourceDirectory}System/Drive/templates &&python3 {up.SourceDirectory}System/Drive/templates/launchwebpage.py"\''
    )
