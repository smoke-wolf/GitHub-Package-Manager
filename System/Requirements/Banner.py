import datetime
import time

try:
    import System.Requirements.FTD
except:
    pass
Launcher = """
  _                            _               
| |                          | |              
| |     __ _ _   _ _ __   ___| |__   ___ _ __ 
| |    / _` | | | | '_ \ / __| '_ \ / _ \| __|
| |___| (_| | |_| | | | | (__| | | |  __/ |   
\_____/\__,_|\__,_|_| |_|\___|_| |_|\___|_|    
================================================
"""
try:
    import User.UserProfile

    User = User.UserProfile.Username
except:
    pass


FunctionList = f"""
\033[0;32m|-------------------------------| 
\033[0;32m| \033[0;31m1:: GHPM Information          \033[0;32m| 
\033[0;32m|-------------------------------|
\033[0;32m| \033[0;33m2:: Logs & Cache              \033[0;32m| 
\033[0;32m|-------------------------------|
\033[0;32m| \033[0;31m3:: Package Uninstaller       \033[0;32m|
\033[0;32m|-------------------------------|
\033[0;32m| \033[1;37m4 -> Update                   \033[0;32m|
\033[0;32m|-------------------------------|
\033[0;32m| \033[0;35m0:: Exit                      \033[0;32m|
\033[0;32m|-------------------------------|

"""

Function_Settings = """
|==================================|        
|            Settings              |
|==================================|
|1 | Info                          |
|==================================|
|2 | User Settings                 |
|==================================|
"""
