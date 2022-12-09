import System.Requirements.Information
Value = int(input('Enter a value to continue: '))

if Value == 1:  # Info
    print(System.Requirements.Information.Functions_Settings)

elif Value == 2:    # User Settings
    pass

elif Value == 3:    # System Settings
    print('''
    1 | Toggle Forced Module Import
    2 | Toggle Forced Login
    ''')
    inp = int(input('Enter a value to continue:'))

    if inp == 1:
        import System.Drive.Functions.ForcedModuleImport
        exec('System.Drive.Functions.ForcedModuleImport')

    elif inp == 2:
        import System.Drive.Functions.ForcedLogin
        exec('System.Drive.Functions.ForcedLogin')
