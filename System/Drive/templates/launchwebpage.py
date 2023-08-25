import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

class WebWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('GhPm Recommended')

        # Create a QWebEngineView widget
        self.web_view = QWebEngineView(self)
        self.web_view.setGeometry(0, 0, 800, 600)

        current_directory = os.getcwd()

        self.web_view.setUrl(QUrl.fromLocalFile(f"{current_directory}/index.html"))  # Replace with the actual file path

        self.web_view.urlChanged.connect(self.handleUrlChanged)

        self.setCentralWidget(self.web_view)

        self.show()

    def handleUrlChanged(self, url):
        if url != self.web_view.url():
            self.web_view.setUrl(url)  # Perform the redirect

def main():
    app = QApplication(sys.argv)
    window = WebWindow()
    sys.exit(app.exec_())


main()