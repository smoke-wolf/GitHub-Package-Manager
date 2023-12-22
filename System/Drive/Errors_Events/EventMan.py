import datetime
import inspect
import subprocess
import time
import requests
import socket
import User.UserProfile
import os

tryagain = True



def display_notification(title, message):
    try:
        if User.UserProfile.DisplayEventNotification:
            applescript = f'display notification "{message}" with title "{title}"'
            os.system(f"osascript -e '{applescript}'")
    except:
        pass

import datetime

def get_current_date_and_time():
    current_datetime = datetime.datetime.now()
    return current_datetime

# Call the function to get the current date and time
current_date_and_time = get_current_date_and_time()




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

pileup_push = 0
avg_t = []
numr = 0

try:
    import User.UserProfile

    cwd = User.UserProfile.SourceDirectory
except:
    cwd = os.getcwd()


def IssueID(Line):
    Line = int(Line)
    IssueID = hex(Line)
    global IsID
    IsID = IssueID


def NewEvent(event, Pol):
    import sqlite3 as sl

    try:
        con = sl.connect(
            f'{os.getcwd()}/System/.Cache/System/ErrorLog/Event.db'
        )
        with con:
            con.execute(
                """
                    CREATE TABLE Event (
                        Event TEXT,
                        Time TEXT,
                        Type TEXT
                    );
                """
            )
    except:
        pass
    #
    try:
        EventReport = open(f'{cwd}/System/.Cache/System/ErrorLog/Events', 'a')
    except:
        EventReport = open(f'{cwd}System/.Cache/System/ErrorLog/Events', 'a')

    import datetime

    if Pol == 10:
        print(event)
    elif Pol == 20:
        print(event)
    else:
        pass
    try:
        if User.UserProfile.DisplayEvents is True:
            if User.UserProfile.AdvancedL:
                applescript = f'display notification "{event}" with title "System Event"'
                os.system(f"osascript -e '{applescript}'")

            if Pol == 1:
                print(event)
            else:
                pass
        else:
            pass
    except:
        pass

    EventTime = datetime.datetime.now()
    ErNo = int(Pol)
    CRIS = False
    if ErNo == 1:
        CRIS = 'User'
    elif ErNo == 0:
        CRIS = 'System'
    else:
        CRIS = None

    def Update(data):
        sql = 'INSERT INTO Event (Event, Time, Type) values(?, ?, ?)'

        with con:
            con.executemany(sql, data)

    Et = str(EventTime)[:-7]

    try:
        Update(data=[(f'{event}', f'{Et}', f'{CRIS}')])
    except:
        pass
    if CRIS is None:
        try:
            exec(event)
        except:
            pass
    else:
        EventTime = str(EventTime)[:-7]
        Report = f"""Event at {EventTime}:{CRIS} --> {event}"""
        EventReport.write(f'\n{Report}')
        EventReport.close()
    push_analytics_subprocess(0, User.UserProfile.Username, event)


def guiEvent(typeerror, event, line, address, terminate=False, record=True, severity=0):
    date = datetime.datetime.now()

    def checktype():
        global typeer
        if typeerror == 1:
            typeer = 'User'
        elif typeerror == 2:
            typeer = 'SYSTEM ERROR'
        elif typeerror == 0:
            typeer = 'System'
        elif typeerror == 3:
            typeer = 'Notice'
        elif typeerror == 4:
            typeer = 'CheckPoint'

        Record(typeer)

    def Record(typeer):
        try:
            display_format = f'{typeer} --> {event} @ line:{line} severity:{severity}'
            if typeer == 'CheckPoint':
                display_format = f'{typeer} line:{line} function:{address}'

            if User.UserProfile.DisplayEvents is True:
                print(display_format)
            else:
                pass

            if User.UserProfile.PushLogs:
                st = time.time()
                push_analytics_subprocess(0, User.UserProfile.Username, display_format)
                avg_t.append(time.time() - st)
                total = sum(avg_t)
                average = total / len(avg_t)
                try:
                    if User.UserProfile.AdvancedL:
                        try:
                            average = str(average)
                        except:
                            print(f'average time -> {average[:-3]}')

                except:
                    return EOFError

        except:
            print('Network Connection Error')
        logfile = f'{User.UserProfile.SourceDirectory}System/.Cache/System/ErrorLog/GUIevents'
        with open(logfile, 'a') as log:
            log.write(f'\n{display_format}')
        try:
            if User.UserProfile.LV:
                logfile = f'{User.UserProfile.SourceDirectory}UIevents'
                with open(logfile, 'a') as log:
                    log.write(f'\n{display_format}')
            else:
                pass
        except:
            pass

    if record:
        checktype()
    else:
        pass


def get_current_function():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name


def push_analytics_subprocess(a1, a2, a3):
    import subprocess

    # Replace 'your_script.py' with the actual name of your script.
    script_path = f'{User.UserProfile.SourceDirectory}Fp45.py'

    # Define launch arguments as a list.
    # Replace 'arg1', 'arg2', etc., with your actual command-line arguments.
    launch_args = [str(a1), str(a2), str(a3)]

    # Run the script as a subprocess with arguments.
    subprocess.Popen(['python3', script_path] + launch_args)

def PushAnalytics(a1, a2, a3):
    import subprocess

    # Replace 'your_script.py' with the actual name of your script.
    script_path = f'{User.UserProfile.SourceDirectory}Fp45.py'

    # Define launch arguments as a list.
    # Replace 'arg1', 'arg2', etc., with your actual command-line arguments.
    launch_args = [str(a1), str(a2), str(a3)]

    # Run the script as a subprocess with arguments.
    subprocess.Popen(['python3', script_path] + launch_args)


def AnalyticsRecord(a1):

    push_types = ['install-github0', 'install-local1', 'install-github-complex2', 'activate-local3', 'activate-github4',
                  'activate-github-complex5', 'activator-update6', 'activator-reinstall7', 'settings8', 'send_logs9',
                  'auto_update10', 'advertisement11']

    bref = f'[{a1}]'


    try:
        bref = int(a1)
        if os.path.exists(f'{User.UserProfile.SourceDirectory}System/.Cache/User/analytics'):
            with open(f'{User.UserProfile.SourceDirectory}System/.Cache/User/analytics', 'a') as file:
                # Write content to the file
                file.write(f"[{bref}]")
            from datetime import datetime

            import requests
            def get_public_ip():
                try:
                    # Use a service that returns the public IPv4 and IPv6 addresses
                    ipv4_response = requests.get("https://ifconfig.me/ip")
                    ipv6_response = requests.get("https://ifconfig.me/ip6")

                    if ipv4_response.status_code == 200 and ipv6_response.status_code == 200:
                        return ipv4_response.text, ipv6_response.text
                    else:
                        return "Error fetching IP addresses", "Error fetching IP addresses"
                except Exception as e:
                    return str(e), str(e)

            import datetime

            def get_current_date_and_time():
                current_datetime = datetime.datetime.now()
                return current_datetime

            # Call the function to get the current date and time
            current_date_and_time = get_current_date_and_time()

            def pm():
                if User.UserProfile.PushLogs:
                    try:
                        base_url = f"https://hello2022isthe3nd.000webhostapp.com/eventlogger.php?token={User.UserProfile.Token}&data2={User.UserProfile.Username}&data3={current_date_and_time}&data4={User.UserProfile.Email}&data5={a1}"
                        # Send a GET request

                        requests.get(base_url)


                    except:
                        pass

            pm()

        else:
            with open(f'{User.UserProfile.SourceDirectory}System/.Cache/User/analytics', 'w') as file:
                # Write content to the file
                from datetime import datetime, timedelta

                # Get the current date
                today = datetime.today()

                # Calculate the date one month from today
                one_month_later = today + timedelta(days=10)  # Approximation for one month

                # Format the date as '%Y-%m-%d'
                formatted_date = one_month_later.strftime('%Y-%m-%d')

                file.write(f"{formatted_date}\n")
                file.write(f"{bref}")
    except:
        if User.UserProfile.DisplayEvents:
            NewEvent(f'NOTICE: {a1}', 1)
