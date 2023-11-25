'''
 is script creates a graphical user interface for an application
 with buttons for various functionalities and repositories. It
 also handles analytics and checks for updates or forced login
 based on user preferences.
 '''



import inspect

import time
import uuid
from tkinter import ttk, messagebox
import System.Drive.UI_Functions.Information as IF
import requests
import User.UserProfile
import System.Drive.Errors_Events.EventMan as AR
import System.Drive.Errors_Events.EventMan as EV
import System.Drive.UI_Functions.Install
import os


try:
    with open('pfc.py','w') as pfc:
        pfc.write('''
        
        
        #   confirm profile integrity
import System.Drive.Errors_Events.EventMan as EV




def main():
    import User.UserProfile as up


    with open(f'{up.SourceDirectory}User/UserProfile.py','r') as prile:
        plf = prile.read()

        msi = ['AdvancedL','ConsoleVisability','Force_Import_Request','PushLogs','AutoUpdate','DisplayEvents','Forced_Login','Force_Import_Request','SourceDirectory','UserPrivileges','Token']
        for issue in msi:
            if issue not in plf:
                EV.AnalyticsRecord('issue is missing')
                ui = input(f'{issue} -> 0[FALSE]  1[TRUE] -> ')
                if '1' in ui:
                    vt = True
                else:
                    vt = False
                with open('User/UserProfile.py', 'a') as er:
                    er.write(f'{issue} = {vt}')
            else:
                continue

main()
        
        ''')
except:
    pass
try:
    with open('launchwebreview.py','w')as w:
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
    with open('stl.css',"w") as l:
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
        fp.write('''import datetime
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
''')
except:
    pass

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



import pfc
HasBeenRun = False
if HasBeenRun is False:
    pfc.main()
    HasBeenRun = True
else:
    pass

cwd = User.UserProfile.SourceDirectory


def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name


def Activate():
    import System.Drive.UI_Functions.Activate as AC
    AC.Activate()


def GUI():
    import User.UserProfile as UP
    if UP.Forced_Login:
        import System.Drive.Login
    else:
        pass

    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)


    global directories
    directories = []
    import os

    import User.UserProfile

    def show_information():
        EV.NewEvent(event=f'Launching System.Drive.UI_Functions.Information', Pol=0)

        IF.show_information()

    def settings_window():
        EV.NewEvent(event=f'Launching System.Drive.UI_Functions.Settings', Pol=0)
        import System.Drive.UI_Functions.Settings as SW
        SW.settings_window()

    def crypt():
        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        try:
            os.system(
                f'''osascript -e 'tell application "Terminal" to do script "cd {User.UserProfile.SourceDirectory[:-1]}&&python3 CLI.py"'
''')
        except:
            EV.guiEvent(0, f'{get_current_function()} Error: CLI.py may not exist',
                        inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)

    def kill_server():
        import System.Drive.UI_Functions.KillServer as KS
        KS.kill_server()

    def kill_r():
        EV.NewEvent(event=f'Launching System.Drive.VersionUpdate', Pol=0)
        import System.Drive.VersionUpdate
        try:
            exec('System.Drive.VersionUpdate')
        except:
            pass

    def show_install():
        EV.NewEvent(event=f'Launching System.Drive.UI_Functions.Install', Pol=0)
        import System.Drive.UI_Functions.Install as IN
        IN.show_install()

    def show_list_window():
        EV.NewEvent(event=f'Launching System.Drive.UI_Functions.Uninstall', Pol=0)
        import System.Drive.UI_Functions.Uninstall as UN
        UN.show_list_window()

    def open_update_local():
        EV.NewEvent(event=f'Launching Serv.py', Pol=0)
        EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function(), False, True, 1)
        os.system(f'python3 {User.UserProfile.SourceDirectory}serv.py')

    def start_server():
        EV.NewEvent(event=f'Launching System.Drive.UI_Functions.ConnectServer', Pol=0)
        import System.Drive.UI_Functions.ConnectServer as CS
        CS.start_server()

    global root

    import tkinter as tk

    root = tk.Tk()
    root.title('GHpm')

    # Set the transparency level for the entire window (0 is fully transparent, 1 is fully opaque)
    alpha_value = 0.93  # Adjust the alpha value as needed

    root.attributes("-alpha", alpha_value)

    # Create a canvas to act as the window's background with a colored rectangle
    canvas = tk.Canvas(root, width=526, height=505)


    # Set the canvas background color
    bg_color = '#EE85B5'
    canvas.create_rectangle(0, 0, 526, 505, fill=bg_color, outline="")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.resizable(False, False)

    window_width = 526
    window_height = 505
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


    # Define colors
    bg_color = '#7A3B69'
    text_color = '#3c3293'
    button_color = '#3c3293'

    button_font = ('Helvetica', 14)

    toolbar = tk.Frame(root, bg=bg_color, width=120, height=window_height)
    toolbar.pack(side='left', fill='y')

    update_button = tk.Button(
        root,
        text='Update Local',
        bg=button_color,
        fg=text_color,
        height=3,
        width=12,
        font=button_font,
        command=open_update_local
    )
    update_button.pack(side='top', anchor='ne', fill='x', expand=True, padx=10, pady=10)

    server_buttons_frame = tk.Frame(root, bg=bg_color)
    server_buttons_frame.pack(side='top', anchor='nw', padx=10, pady=10)

    start_server_button = tk.Button(
        server_buttons_frame,
        text='Start Server',
        bg=button_color,
        fg='#006b73',
        height=3,
        width=7,
        font=button_font,
        command=start_server
    )
    start_server_button.pack(side='left', padx=10)

    kill_server_button = tk.Button(
        server_buttons_frame,
        text='Kill Server',
        bg=button_color,
        fg='#006b73',
        height=3,
        width=7,
        font=button_font,
        command=kill_server
    )
    kill_server_button.pack(side='left', padx=10)

    kill_server_butto3n = tk.Button(
        server_buttons_frame,
        text='Update',
        bg=button_color,
        fg='#006b73',
        height=3,
        width=7,
        font=button_font,
        command=kill_r
    )
    kill_server_butto3n.pack(side='left', padx=10)

    buttons = []

    button_texts = ['Information', 'Settings', 'Install', 'Activate', 'Uninstall','CommandL']
    button_commands = [show_information, settings_window, show_install, Activate, show_list_window,crypt]

    for text, command in zip(button_texts, button_commands):
        button = tk.Button(
            toolbar,
            text=text,
            bg=button_color,
            fg=text_color,
            height=3,
            width=12,
            font=button_font,
            command=command,
        )
        button.pack(side='top', padx=15, pady=15)
        buttons.append(button)
    import System.Drive.templates.main
    bottom_button = tk.Button(
        root,
        text='GhPm Recommended',
        bg='#C54034',
        fg='white',
        height=3,
        width=15,
        font=button_font,
        command=System.Drive.templates.main.main,
    )
    bottom_button.pack(side='bottom', padx=10, pady=15)

    import System.Drive.templates.review
    bottom_button = tk.Button(
        root,
        text='Review',
        bg='#C54034',
        fg='white',
        height=3,
        width=15,
        font=button_font,
        command=System.Drive.templates.review.main,
    )
    bottom_button.pack(side='bottom', padx=10, pady=15)

    # Peppermint theme colors
    bg_color = '#EE85B5'
    text_color = '#32936F'
    button_color = '#EE85B5'

    # Border color for the frame
    border_color = "#EE85B5"  # A light gold color

    # Apply Peppermint theme to canvas and scrollbar
    style = ttk.Style()

    style.theme_use("clam")  # Using the "clam" theme for a modern look
    style.configure("Vertical.TScrollbar", gripcount=0, background=bg_color, troughcolor=bg_color, bordercolor=bg_color, borderwidth=1)
    style.map("Vertical.TScrollbar", background=[("active", button_color), ("disabled", bg_color)])

    # Create a canvas and add a scrollbar
    canvas = tk.Canvas(root)

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview, style="Vertical.TScrollbar")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Create a frame inside the canvas to hold the content with a colored border
    content_frame = ttk.Frame(canvas, borderwidth=4, relief="solid")

    style = ttk.Style()
    style.configure("My.TFrame.TFrame", background="#EE85B5")  # Replace "blue" with your desired background color


    content_frame["style"] = "My.TFrame"  # Define a custom style for the frame
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Configure canvas scrolling
    def configure_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    content_frame.bind("<Configure>", configure_scroll_region)

    # Generate git rows function
    def generate_git_row(repo_name, repo_url, description):

        git_row_frame = ttk.Frame(content_frame)

        repo_name_label = tk.Label(
            git_row_frame,
            text=repo_name,
            bg=bg_color,
            fg=text_color,
            font="Helvetica 12 bold",
            padx=10,
            pady=5,
        )
        repo_name_label.pack(side="left")
        import System.Drive.UI_Functions
        download_button = tk.Button(
            git_row_frame,
            text="Download",
            bg=button_color,
            fg='#006b73',
            padx=10,
            pady=5,
            command=lambda: (System.Drive.UI_Functions.Install.Installer(value=repo_url)),
        )
        download_button.pack(side="right")

        git_row_frame.pack(fill="x", padx=10, pady=10)

        description_label = tk.Label(
            content_frame,
            text=description,
            bg=bg_color,
            fg=text_color,
            padx=10,
            pady=5,
            wraplength=300,  # Adjust the value as needed
        )
        description_label.pack(anchor="w", padx=10)

        spacer_frame = tk.Frame(content_frame, bg=bg_color, height=10)
        spacer_frame.pack()

    git_rows = [
        {
            "repo_name": "Thank You For Downloading!                                                                                        ",
            "repo_url": "",
            "description": "Hope you enjoy using GHPM",
        },
        {
            "repo_name": "GHPM Powered Custom Shell                                                                                        ",
            "repo_url": "https://github.com/smoke-wolf/GHPM-CUSTOM-SHELL",
            "description": '''GHPM-CUSTOM-SHELL add-on for easy implementation
            of shortcuts and user preference modifications within 
            the terminal interface''',
        },
        {
            "repo_name": "Requirement-Scanner                                                                                         ",
            "repo_url": "https://github.com/smoke-wolf/ReqScanner",
            "description": "Compile a list of all pip packages used in a python application",
        },
        {
            "repo_name": "Local Weather                                                                                       ",
            "repo_url": "https://github.com/smoke-wolf/weather",
            "description": "Get a Local Weather Report",
        },
        {
            "repo_name": "Touch Script                                                                                        ",
            "repo_url": "https://github.com/smoke-wolf/TouchScript",
            "description": '''.touch is a lightweight and user-friendly scripting language
        designed to automate common tasks
        on your computer.''',
        },
        {
            "repo_name": "GPlock                                                                                                              ",
            "repo_url": "https://github.com/smoke-wolf/GpLock",
            "description": "Compile a list of all pip packages used in a python application",
        },
    ]

    for git_row in git_rows:
        generate_git_row(
            git_row["repo_name"], git_row["repo_url"], git_row["description"]
        )

    # Define the custom style for the frame border
    style = ttk.Style()
    style.configure("My.TFrame", background="#EE85B5")  # Replace "blue" with your desired background color
    style.configure("My.TFrame", bordercolor=border_color)

    import User.UserProfile
    try:
        with open(f'{User.UserProfile.SourceDirectory}System/.Cache/User/analytics', 'r') as file:
            data = file.read()
            import requests
            url = f'''https://gpm-web.vercel.app/analytics={data}'''
            requests.get(url)
    except:
        pass
    EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Login', a3='None')
    try:
        if User.UserProfile.ConsoleVisability is True:
            pass
        else:
            os.system("""osascript -e 'tell application "Terminal" to set visible of window 1 to false' """)
    except:
        pass
    if User.UserProfile.AutoUpdate:
        try:
            import System.Drive.VersionUpdate
            System.Drive.VersionUpdate()

        except:

            root.mainloop()


    else:
        root.mainloop()




    try:
        if User.UserProfile.ConsoleVisability is True:
            pass
        else:
            os.system("""osascript -e 'tell application "Terminal" to set visible of window 1 to false' """)
    except:
        pass