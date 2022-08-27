import sys
import os
try:
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtWebEngineWidgets import *
except:
    os.system('pip install pyqt5')
    os.system('pip install PyQtWebEngine')
    input('Перазапустите программу')
    sys.exit(1)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        navbar.setAutoFillBackground(True)
        navbar.setStyleSheet('QToolBar { background: yellow; }')

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

        Alis_btn = QAction('Alis', self)
        Alis_btn.triggered.connect(self.Alis)
        navbar.addAction(Alis_btn)
        

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def spotify(self):
        self.browser.setUrl(QUrl('https://open.spotify.com'))

    def Alis(self):
        self.browser.setUrl(QUrl('https://sites.google.com/view/coderprogrammers'))

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Alis browser')
window = MainWindow()
app.exec_()