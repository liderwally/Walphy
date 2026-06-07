import os
import sys
from multiprocessing import process, Process
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from config import config

class MainWindow(QMainWindow):
    url = QUrl("http://localhost")

    url.port(config["thisAppPort"])

    print(url)

    def __init__(self, port):
        super(MainWindow, self).__init__()
        self.url.port = port
        self.browser = QWebEngineView()
        self.browser.setUrl(self.url)
        self.setCentralWidget(self.browser)
        self.showMaximized()

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
        self.browser.setUrl(self.url)

    def update_url(self, q):
        self.url = QUrl(q.toString())

