
def main():
    import System.Requirements.Information
    Value = int(input('Enter a value to continue: '))
    import System.Drive.Errors_Events.EventMan as EV
    EV.NewEvent(event=f'Launching Settings', Pol=0)
    if Value == 1:  # Info
        print(System.Requirements.Information.Functions_Settings)
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'Settings Info', Pol=1)
    elif Value == 2:    # User Settings
        import System.Drive.Errors_Events.EventMan as EV

        EV.NewEvent(event=f'User Settings', Pol=1)

    elif Value == 3:    # System Settings
        print('''
        1 | Toggle Forced Module Import
        2 | Toggle Forced Login
        ''')
        inp = int(input('Enter a value to continue:'))

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
