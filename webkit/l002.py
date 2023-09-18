import os
os.system("""osascript -e 'tell application "Terminal" to set visible of every window to false'""")

os.system('python3 serv.py')

