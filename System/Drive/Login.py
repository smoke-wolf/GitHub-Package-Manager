'''
this script handles user authentication by validating
the entered password, with multiple retries if necessary,
and checks for device restrictions based on the device's UUID.
If the device is not restricted, the user is allowed to log in.



'''
import sys
import User.UserProfile

import requests

def login(username, password):
    url = "https://hello2022isthe3nd.000webhostapp.com/backend.php"

    # Send a GET request with the username and password as query parameters
    params = {
        "username": username,
        "password": password
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Check if the response URL contains the token
        token_param = "token"
        if token_param in response.url:
            # Extract the token from the URL
            token = response.url.split(token_param + "=")[1]
            with open(f'{User.UserProfile.SourceDirectory}User/UserProfile.py', 'a') as oc:
                oc.write(f"\nToken='{token}'")

            return token
        else:
            print("Authentication failed. No token found.")
    else:
        print(f"Failed to authenticate. Status code: {response.status_code}")

import datetime

def get_current_date_and_time():
    current_datetime = datetime.datetime.now()
    return current_datetime

# Call the function to get the current date and time
current_date_and_time = get_current_date_and_time()
username = User.UserProfile.Username


def tkn():
    base_url = f"https://hello2022isthe3nd.000webhostapp.com/eventlogger.php?token={User.UserProfile.Token}&data2={User.UserProfile.Username}&data3={current_date_and_time}&data4={User.UserProfile.Email}&data5=requesting token"
    # Send a GET request

    response = requests.get(base_url)

    if response.text == 'Analytics data recorded successfully.':
        return True
    else:

        return False
def Login():
    import time
    tr = tkn()

    if tr:
        print('already logged in')
    else:
        print('''
        ======================================
        [[[[[[[[[[[LOG IN TO CONTINUE]]]]]]]]]
        ======================================''')
        Input = input('Enter Password: ')
        try:
            import System.Drive.Password as PS
            token = login(username, password=Input)

            if token:
                print(f"Authentication successful. Token: {token}")
            else:
                sys.exit()
            PS.Password(Event='Login', Input=Input)
            print('Logged In Successfully!')
            time.sleep(1.54)
            print('\n' * 100)

        except:
            Input = input('Enter Password: ')
            try:
                import System.Drive.Password as PS
                token = login(username, password=Input)

                if token:
                    print(f"Authentication successful. Token: {token}")
                else:
                    sys.exit()
                PS.Password(Event='Login', Input=Input)
                print('Logged In Successfully!')
                time.sleep(1.54)
                print('\n' * 100)
            except:
                print('Final Try')
                Input = input('Enter Password: ')
                try:
                    import System.Drive.Password as PS
                    token = login(username, password=Input)

                    if token:
                        print(f"Authentication successful. Token: {token}")
                    else:
                        sys.exit()
                    PS.Password(Event='Login', Input=Input)
                    print('Logged In Successfully!')
                    time.sleep(1.54)
                    print('\n' * 100)
                except:
                    sys.exit(0)


Blocked = open(f'{User.UserProfile.SourceDirectory}User/Blocked', 'r')
Blocked = Blocked.read()
import uuid

UUID = uuid.uuid1()
UUID = str(f'{UUID}')
uuidToken = UUID[30:]
if uuidToken in Blocked:
    import System.Drive.Errors_Events.EventMan as EV

    EV.NewEvent(event='Device Restricted Due To NonOriginDevice', Pol=0)
    print('This Device Has Been Restricted')
    sys.exit(0)
else:
    Login()