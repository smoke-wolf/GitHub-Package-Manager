import User.UserProfile
import os
cwd = os.getcwd()
def IssueID(Line):
    Line = int(Line)
    IssueID = hex(Line)
    global IsID
    IsID = IssueID

def NewEvent(event, Pol):
    EventReport = open(f'{cwd}/System/Cache/System/ErrorLog/Events', 'a')
    import datetime
    if Pol == 0:
        print(event)
    else:
        pass

    EventTime = datetime.datetime.now()
    ErNo = int(Pol)
    CRIS = False
    if ErNo == 1:
        CRIS = 'User  '
    elif ErNo == 0:
        CRIS = 'System'
    EventTime = str(EventTime)[:-7]
    Report = f'''Event at {EventTime}:{CRIS} [!]{event}[!]'''
    EventReport.write(f'\n{Report}')
    EventReport.close()


