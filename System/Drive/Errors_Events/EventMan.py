import datetime
import socket
import time
import requests

pileup_push = 0

try:
    import User.UserProfile
except:
    pass
import os

try:
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


def guiEvent(typeerror, event, line, address, terminate=False, record=True, severity=0):
    date = datetime.datetime.now()

    def checktype():
        global typeer
        if typeerror == 1:
            typeer = 'User'
        elif typeerror == 0:
            typeer = 'System'
        elif typeerror == 3:
            typeer = 'Notice'
        elif typeerror == 4:
            typeer = 'CheckPoint'

        Record(typeer)

    def Record(typeer):
        display_format = f'{typeer} --> {event} @ line:{line} severity:{severity}'
        if typeer == 'CheckPoint':
            display_format = f'{typeer} line:{line} function:{address}'
        print(display_format)
        if User.UserProfile.PushLogs:
            url = f"https://gpm-web.vercel.app/usr={User.UserProfile.Username}/log={display_format}"
            import requests
            requests.get(url)

        logfile = f'{User.UserProfile.SourceDirectory}System/.Cache/System/ErrorLog/GUIevents'
        with open (logfile, 'a') as log:
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

def PushAnalytics(a1,a2,a3):

    if User.UserProfile.PushLogs:
        AnalyticsRecord(9)
        import requests
        global analytics_push_id
        analytics_push_id = 0
        ip = socket.gethostbyname(socket.gethostname())

        url = f"https://gpm-web.vercel.app/push={analytics_push_id}/usr={User.UserProfile.Username}/ip{ip}/requesttype={a2}/aditional={a3}"
        requests.get(url)

def AnalyticsRecord(a1):
    push_types = ['install-github0', 'install-local1', 'install-github-complex2', 'activate-local3', 'activate-github4',
                  'activate-github-complex5', 'activator-update6', 'activator-reinstall7', 'settings8', 'send_logs9',
                  'auto_update10','advertisement11']

    bref = f'[{a1}]'
    if os.path.exists(f'{User.UserProfile.SourceDirectory}System/.Cache/User/analytics'):
        with open(f'{User.UserProfile.SourceDirectory}System/.Cache/User/analytics', 'a') as file:
            # Write content to the file
            file.write(f"{bref}")
        from datetime import datetime

        def is_same_date_as_today(file_path):
            # Get today's date in '%Y-%m-%d' format
            today_date = datetime.today().strftime('%Y-%m-%d')

            # Read the first line of the file
            with open(file_path, 'r') as file:
                first_line = file.readline().strip()

            # Compare the first line of the file with today's date
            return first_line == today_date

        with open(f'{User.UserProfile.SourceDirectory}System/.Cache/User/analytics', 'r') as file:
            data = file.read()
            if is_same_date_as_today(f'{User.UserProfile.SourceDirectory}System/.Cache/User/analytics'):
                url = f'''https://gpm-web.vercel.app/analytics={data}'''
                requests.get(url)


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
