import ttkbootstrap as ttk
import widgetfactory as wf
import utilities as ut
import customnotebook as cnb

fileHandler = ut.FileHandler()
lorem = fileHandler.readTextFile("lorem.txt")

theme = 'darkly'
root = ttk.Window(
    title='GHPM',
    themename=theme,
    size=(1100, 700),
    resizable=(False, False),
)

SLN = cnb.Root(root, theme)

frame1 = ttk.Frame()
label = ttk.Label(frame1, text="hello")
label.pack()

frame2 = ttk.Frame()
label = ttk.Label(frame2, text="hello")
label.pack()

frame3 = wf.CustomFrame("PEPE")
frame3.addScrollText(lorem, 200, 200)
frame3.constructFrame()

frame4 = wf.CustomFrame("LOL")
frame4.addButton("Kanada", 100, 100, command=lambda: SLN.addCustomFrame(frame3))
frame4.addScrollText(lorem, 200, 200)
frame4.constructFrame()

SLN.addTkFrame(frame1, "KEK")
SLN.addTkFrame(frame2, "LUL")
SLN.addCustomFrame(frame4)

root.mainloop()
