import inspect
from tkinter import ttk
import User.UserProfile
import System.Drive.PAMap.Patch0 as p0
import tkinter as tk
from tkinter.font import Font
cwd = User.UserProfile.SourceDirectory
import System.Drive.PAMap.Style as A
import System.Drive.Errors_Events.EventMan as EV
import uuid
EV.PushAnalytics(a1=uuid.uuid1().hex, a2='Information', a3='None')


def show_information():
    EV.guiEvent(4, '', inspect.currentframe().f_lineno, p0.get_current_function(), False, True, 1)

    info_window = tk.Tk()
    info_window.title('Information')

    # Set window size and position
    screen_width = info_window.winfo_screenwidth()
    screen_height = info_window.winfo_screenheight()
    window_width = 440
    window_height = 460

    alpha_value = 0.93  # Adjust the alpha value as needed

    info_window.attributes("-alpha", alpha_value)

    # Create a canvas to act as the window's background with a colored rectangle
    canvas = tk.Canvas(info_window, width=526, height=505)

    # Set the canvas background color
    bg_color = A.bg_color_info
    canvas.create_rectangle(0, 0, 526, 505, fill='#f0f0f0', outline="")

    x_coordinate = (screen_width // 2) - (window_width // 2)
    y_coordinate = (screen_height // 2) - (window_height // 2)
    info_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    info_text = p0.Info()

    container = tk.Frame(info_window, bg=A.bg, bd=2, relief=tk.SOLID)
    container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    text_widget = tk.Label(container, text=info_text, bg='#f0f0f0', fg=A.text_color, justify=tk.LEFT, wraplength=400)
    text_widget.pack(fill=tk.BOTH, expand=True)

    # Apply text styling
    font = Font(family="TkDefaultFont", size=15, weight="bold")
    text_widget.config(font=font)

    okay_button = ttk.Button(info_window, text='Okay', command=info_window.destroy, style='Custom.TButton')
    okay_button.pack(pady=10)

    info_window.mainloop()
