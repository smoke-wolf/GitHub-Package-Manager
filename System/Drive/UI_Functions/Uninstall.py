import datetime
import inspect
import tkinter as tk
from tkinter import ttk
import User.UserProfile
import System.Drive.Errors_Events.EventMan as EV
import os
import uuid

# Set the current working directory from UserProfile
current_working_directory = User.UserProfile.SourceDirectory

# Generate a unique UUID and send an analytics event
unique_id = uuid.uuid1().hex
EV.PushAnalytics(a1=unique_id, a2='Uninstall', a3='None')

# Function to retrieve the current function's name
def get_current_function_name():
    stack = inspect.stack()
    frame = stack[1]
    code = frame[0]
    return code.f_code.co_name

# Function to confirm the uninstallation
def confirm_uninstall(selected_item):
    # Send a GUI event to confirm uninstallation
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function_name(), False, True, 1)
    import tkinter.messagebox

    result = tk.messagebox.askyesno('Confirm Uninstall', f'Are you sure you want to uninstall {selected_item}?')

    # Close the list window
    list_window.destroy()

    if result:
        value_index = items.index(selected_item)

        if value_index >= count:
            dr = int(value_index) - count
            command = lines2[dr - 1]
            print(command)

            try:
                import shutil
                directory_to_remove = command.split('@', 1)[0]
                shutil.rmtree(directory_to_remove)

                print(f'Project Removed: {directory_to_remove}')

            except:
                print(f'Project Failed To Remove: {directory_to_remove}')
                EV.guiEvent(0, f'{get_current_function_name()} Error: {directory_to_remove} not removed',
                            inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)

        else:
            with open(f'{current_working_directory}System/.Cache/System/GitHub/int.txt', 'r') as file:
                lines5 = file.readlines()

            with open(f'{current_working_directory}System/.Cache/System/GitHub/int.txt', 'w') as file:
                for line_in_file in lines5:
                    if line_in_file.find(selected_item) != -1:
                        rmdir = line_in_file.split('@')[0]
                        try:
                            import shutil
                            shutil.rmtree(rmdir)
                            tk.messagebox.showinfo('Success', f'{rmdir} has been uninstalled.')
                        except:
                            EV.guiEvent(0, f'{get_current_function_name()} Error: Failed to remove {rmdir}',
                                        inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)
                    else:
                        file.write(line_in_file)

        return rmdir
    else:
        EV.guiEvent(0, 'Deletion Cancelled', inspect.currentframe().f_lineno, get_current_function_name(), False, True, 1)

# Function to display the list of items to uninstall
def show_list_window():
    # Send a GUI event to show the list window
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, get_current_function_name(), False, True, 1)
    global list_window
    list_window = tk.Toplevel()

    list_window.title('Uninstall List')
    screen_width = list_window.winfo_screenwidth()
    screen_height = list_window.winfo_screenheight()
    window_width = 440
    window_height = 460
    list_window.config(bg='#C5E0DC')
    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    list_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    list_box = tk.Listbox(list_window, font=('Helvetica', 12), bd=2, relief=tk.SOLID, selectmode=tk.SINGLE)
    list_box.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    global items
    items = []
    try:
        with open(f'{current_working_directory}System/.Cache/System/GitHub/int.txt', 'r') as original_file, open(f'{current_working_directory}System/.Cache/System/GitHub/int2.txt', 'w') as copy_file:
            for line in original_file:
                if line.strip():
                    copy_file.write(line)
    except:
        EV.guiEvent(0, f'{get_current_function_name()} Error: GitHub data is locked or not found',
                    inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 4)

    try:
        e = open(f'{current_working_directory}System/.Cache/System/GitHub/Complex2', 'r')
    except:
        EV.guiEvent(0, f'{get_current_function_name()} Error: GitHub data cannot be read',
                    inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)

    f = None  # Initialize f variable

    try:
        f = open(f'{current_working_directory}System/.Cache/System/GitHub/int2.txt', 'r')
    except:
        EV.guiEvent(0, f'{get_current_function_name()} Error: GitHub data cannot be read',
                    inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)

    lines = []
    if f is not None:
        lines = f.readlines()

    global count
    count = 0
    for line in lines:
        count += 1

    count1 = 0
    for line in lines:
        value4 = line.strip()
        Val = value4.split('&', 1)
        if len(Val) > 0:
            value4 = Val[1]
        items.append(value4)
        count1 += 1

    try:
        global lines2
        lines2 = e.readlines()
        for line2 in lines2:
            count1 += 1
            items.append(line2)
    except:
        EV.guiEvent(0, f'{get_current_function_name()} Error: Readlines failed for Complex2',
                    inspect.currentframe().f_lineno, os.path.abspath(__file__), False, True, 3)

    for item in items:
        list_box.insert(tk.END, item)

    confirm_button = ttk.Button(list_window, text='Confirm Uninstall',
                                command=lambda: confirm_uninstall(list_box.get(list_box.curselection())),
                                style='Custom.TButton')
    confirm_button.pack(pady=10)

    exit_button = ttk.Button(list_window, text='Exit Uninstaller', command=lambda: list_window.destroy(),
                             style='Custom.TButton')
    exit_button.pack(pady=10)
