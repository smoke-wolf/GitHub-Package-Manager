'''
This code creates a PyQt5 application with a WebWindow that displays a local HTML file.
It also includes a "Back" action in the menu bar for navigation. 
The osascript command is used to hide the Terminal window. 
The main purpose is to provide a graphical interface for viewing a local HTML file and navigating backward in the browser-like interface.

-also needs to be fixed
*CrossPlatformCompatibility#002*
'''
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

class WebWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 880, 600)
        self.setWindowTitle('GhPm Recommended')

        # Create a QWebEngineView widget
        self.web_view = QWebEngineView(self)
        self.web_view.setGeometry(0, 0, 880, 600)

        current_directory = os.getcwd()

        self.web_view.setUrl(QUrl.fromLocalFile(f"{current_directory}/index.html"))  # Replace with the actual file path

        self.web_view.urlChanged.connect(self.handleUrlChanged)

        # Create a "Back" action in the menu bar
        back_action = QAction("Back", self)
        back_action.setShortcut("Alt+Left")  # Shortcut to trigger the action
        back_action.triggered.connect(self.web_view.back)

        self.menuBar().addAction(back_action)

        self.setCentralWidget(self.web_view)

        self.show()

    def handleUrlChanged(self, url):
        if url != self.web_view.url():
            self.web_view.setUrl(url)  # Perform the redirect

def main():
    app = QApplication(sys.argv)
    window = WebWindow()
    sys.exit(app.exec_())
    
os.system("""osascript -e 'tell application "Terminal" to set visible of window 1 to false' """)
main()
