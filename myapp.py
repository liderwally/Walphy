import os
import sys
from threading import Thread
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from config import config
from appserver import app
import subprocess

class MainWindow(QMainWindow):
    def __init__(self, port):
        super(MainWindow, self).__init__()
        self.url = QUrl("http://127.0.0.1")
        self.url.setPort(port)
        self.browser = QWebEngineView()
        self.browser.setUrl(self.url)
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.resize(config["width"],config["length"])
        

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(self.url)

    def navigate_to_url(self):
        url = QUrl(self.url_bar.text())
        self.browser.setUrl(url)

    def update_url(self, q):
        self.url_bar.setText(q.toString())

def start_server(port):
    # Start your server here
    command = config["phpDir"] + "\\php.exe -S 127.0.0.1:"+ str(port) +" -t " + config["templatesDir"]
    print(command)
    # os.system(command)
    subprocess.Popen(command)

if __name__ == "__main__":
    port = config["thisAppPort"]
    server_thread = Thread(target=start_server, args=(port,))
    server_thread.daemon = True  # Set as daemon so it exits when main thread exits
    server_thread.start()

    app1 = QApplication(sys.argv)
    window = MainWindow(port)
    sys.exit(app1.exec_())