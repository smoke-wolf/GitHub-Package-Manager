import os
import User.UserProfile as up

def main():
    os.system(
        f'osascript -e \'tell application "Terminal" to do script "cd {up.SourceDirectory}System/Drive/templates &&python3 {up.SourceDirectory}System/Drive/templates/launchwebpage.py"\''
    )