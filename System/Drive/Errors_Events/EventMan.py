import datetime

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
