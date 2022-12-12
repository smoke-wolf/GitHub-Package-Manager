import User.UserProfile
import os
cwd = os.getcwd()
def IssueID(Line):
    Line = int(Line)
    IssueID = hex(Line)
    global IsID
    IsID = IssueID

def NewIssue(Line, ErNo, SCR, KeFu, UserInp):
    IssueReport = open(f'{cwd}/System/Cache/System/ErrorLog/Errors', 'a')
    IssueID(Line)
    import datetime
    IssueTime = datetime.datetime.now()
    ErNo = int(ErNo)
    CRIS = False
    if ErNo == 1:
        CRIS = False
    elif ErNo == 0:
        CRIS = True
    Report = f'''
=================================
IssueID = {IsID}
IssueTime = {IssueTime}
Critical = {CRIS}
=================================
Script_ID = {SCR}
LineNumber ~ {Line}
KeyWords = {KeFu}
=================================
UserException = "{UserInp}"
UserID = {User.UserProfile.Username}
=================================
'''
    IssueReport.write(f'\n{Report}\n')
    IssueReport.close()

    if CRIS is True:
        import sys
        sys.exit(0)
    else:
        pass

