import os
import tkinter as tk
import shutil
import User.UserProfile

def list_subdirectories(fp):
    subdirectories = []
    for item in os.listdir(fp):
        item_path = os.path.join(fp, item)
        if os.path.isdir(item_path) and item != 'node_modules':
            subdirectories.append(item_path)
    return subdirectories

def move_directory(source_directory, destination_directory):
    try:
        shutil.move(source_directory, destination_directory)
        return destination_directory
    except shutil.Error as e:
        error_message = str(e)
        if "already exists" in error_message:
            print("Destination directory already exists")
            # Add your notification logic here to display the error message
        else:
            print("Error moving directory:", error_message)
            # Add your notification logic here to display the error message
    except Exception as e:
        print("Error moving directory:", str(e))
        # Add your notification logic here to display the error message
    return None

def create_buttons(subdir):
    root = tk.Tk()
    root.title('Local Installer')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 440
    window_height = 400
    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    source_directory = subdir
    destination_directory = f"{User.UserProfile.SourceDirectory}System/.Cache/System/GitHub/Downloads/{source_directory.split('/')[-1]}"

    # Check if the source directory is 'node_modules' and skip it
    if os.path.basename(source_directory) == 'node_modules':
        root.destroy()
        return

    moved_directory = move_directory(source_directory, destination_directory)
    if moved_directory is None:
        # Skip if moving failed
        root.destroy()
        return

    print("Moved directory path:", moved_directory)
    ImportDirectory = moved_directory

    Files0 = []
    for path in os.listdir(ImportDirectory):
        # check if current path is a file
        if os.path.isfile(os.path.join(ImportDirectory, path)):
            Files0.append(path)

    def button_click(item):
        fi = item
        # Remove all characters before the character '-' from string
        fe = fi.split('.', 1)
        if len(fe) > 0:
            ffi = fe[1]

        if 'py' in ffi:
            p1 = f'+{ImportDirectory} ≈python3 {os.path.join(ImportDirectory, fi)}*'
        elif ffi == '.c':
            p1 = f'+{ImportDirectory} ≈gcc {os.path.join(ImportDirectory, fi)}*'
        elif 'cpp' in ffi:
            p1 = f'+{ImportDirectory} ≈gpp {os.path.join(ImportDirectory, fi)}*'
        elif 'sh' in ffi:
            p1 = f'+{ImportDirectory} ≈bash {os.path.join(ImportDirectory, fi)}*'

        print('[!] CheckPoint 4|4 [!]')
        Form = f'{fi[:-3]} = "{p1}"'

        with open(f'{User.UserProfile.SourceDirectory}/System/.Cache/System/Local/Int.txt', 'a') as f:
            f.write(f'\n{Form}')
        print(Form)
        print('Installation Complete!')
        root.destroy()

    item_list = Files0

    for item in item_list:
        tk.Button(
            root, text=item, command=lambda i=item: button_click(i)
        ).pack()

    root.mainloop()

directory_path = f"{User.UserProfile.SourceDirectory}System/.Cache/System/local/download/"
subdirs = list_subdirectories(directory_path)

for subdir in subdirs:
    create_buttons(subdir)
