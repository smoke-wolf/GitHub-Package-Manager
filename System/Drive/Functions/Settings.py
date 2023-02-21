import os
import sys


def main():
    import System.Requirements.Information

    Value = input('Enter a value to continue: ')
    cwd = os.getcwd()
    try:
        Value = int(Value)
    except:
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Input Error', Pol=1)

    import System.Drive.Errors_Events.EventMan as EV

    EV.NewEvent(event=f'Launching Settings', Pol=0)
    if Value == 1:  # Info
        print(System.Requirements.Information.Functions_Settings)
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Settings Info', Pol=1)

    elif Value == 2:  # User Settings
        print(
            """
        1 | Toggle Forced Module Import
        2 | Toggle Forced Login
        3 | Toggle System Event display 
        4 | Enable Command Line Interface
        5 | Change UserName
        ----------------------------------
        6 | Change Password
        """
        )
        inp = input('Enter a value to continue:')
        try:
            inp = int(inp)
        except:
            EV.NewEvent(event=f'Input Error', Pol=1)
            sys.exit(0)

        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'System Settings', Pol=1)

        if inp == 1:
            import System.Drive.Functions.ForcedModuleImport
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Launching ForcedModuleImport', Pol=1)
            exec('System.Drive.Functions.ForcedModuleImport')

        elif inp == 2:
            import System.Drive.Errors_Events.EventMan as EV

            EV.NewEvent(event=f'Launching ForcedLogin', Pol=1)
            import System.Drive.Functions.ForcedLogin

            exec('System.Drive.Functions.ForcedLogin')

        elif inp == 3:
            EV.NewEvent(event=f'Launching Event Display', Pol=1)
            target = open(f'{cwd}/User/UserProfile.py', 'a')
            import User

            Cstat = User.UserProfile.DisplayEvents
            if Cstat is True:
                status = False
            else:
                status = False

            target.write(f'\nDisplayEvents = {status}')
            print(f'DisplayEvents set to {status}')

            EV.NewEvent(event=f'DisplayEvents = {status}', Pol=0)

        elif inp == 4:
            EV.NewEvent(event='Creating Global Alias', Pol=10)
            import User

            alias = f"""echo 'alias gh="cd {User.UserProfile.SourceDirectory} &&python3 gh.py"' >> ~/.zshrc && exec zsh -l"""
            try:
                os.system(alias)
                EV.NewEvent(event='Installing Global Alias- Complete', Pol=20)
            except:
                EV.NewEvent(event='Error Installing Global Alias', Pol=20)

            print(System.Requirements.Information.CLI_DOC)

        elif inp == 5:
            Input = input('Enter Password to change username: ')
            try:
                import System.Drive.Password as PS

                PS.Password(Event='Username', Input=Input)
                try:
                    PS.UpdateUser()
                except:
                    pass
            except:
                Input = input('Enter Password to change username: ')
                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Username', Input=Input)
                    try:
                        PS.UpdateUser()
                    except:
                        pass
                except:
                    Input = input('Final try to change username: ')
                    try:
                        import System.Drive.Password as PS

                        PS.Password(Event='Username', Input=Input)
                        import System.Drive.Password as ps

                        try:
                            ps.UpdateUser()
                        except:
                            pass
                    except:
                        print('Username failed to change')
                        EV.NewEvent(
                            event='username change canceled password error',
                            Pol=1,
                        )

        elif inp == 6:
            Input = input('Enter Current Password to change password: ')
            try:
                import System.Drive.Password as PS

                PS.Password(Event='Password Update', Input=Input)
                try:
                    import System.Drive.Password as ps

                    ps.Create()
                except:
                    pass
            except:
                Input = input('Enter Current Password to change password: ')
                try:
                    import System.Drive.Password as PS

                    PS.Password(Event='Password Update', Input=Input)
                    try:
                        import System.Drive.Password as ps

                        ps.Create()
                    except:
                        pass
                except:
                    Input = input('Final try to change password: ')
                    try:
                        import System.Drive.Password as PS

                        PS.Password(Event='Password Update', Input=Input)
                        try:
                            import System.Drive.Password as ps

                            ps.Create()
                        except:
                            pass
                    except:
                        pass

    elif Value == 3:
        print()
