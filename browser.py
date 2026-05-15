import sys
import os
from PyQt5.QtCore import QUrl, Qt, QStandardPaths
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, QLineEdit, 
                             QAction, QStatusBar, QProgressBar)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

class MiniBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Mini Browser')
        self.setGeometry(100, 100, 800, 600)
        
        profile = QWebEngineProfile.defaultProfile()
        cache_path = os.path.join(os.getcwd(), 'cache')
        os.makedirs(cache_path, exist_ok=True)
        profile.setCachePath(cache_path)
        
        storage_path = os.path.join(os.getcwd(), 'storage')
        os.makedirs(storage_path, exist_ok=True)
        profile.setPersistentStoragePath(storage_path)
        
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl('https://www.bing.com'))
        self.setCentralWidget(self.web_view)
        
        self.create_toolbar()
        self.create_status_bar()
        
        self.web_view.urlChanged.connect(self.update_url_bar)
        self.web_view.loadProgress.connect(self.update_progress)
        self.web_view.loadFinished.connect(self.update_status)
        
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        back_btn = QAction('←', self)
        back_btn.triggered.connect(self.web_view.back)
        toolbar.addAction(back_btn)
        
        forward_btn = QAction('→', self)
        forward_btn.triggered.connect(self.web_view.forward)
        toolbar.addAction(forward_btn)
        
        refresh_btn = QAction('↻', self)
        refresh_btn.triggered.connect(self.web_view.reload)
        toolbar.addAction(refresh_btn)
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)
        
        toolbar.setMovable(False)
        
    def create_status_bar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumWidth(100)
        self.progress_bar.hide()
        self.status_bar.addPermanentWidget(self.progress_bar)
        
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'https://' + url
        self.web_view.load(QUrl(url))
        
    def update_url_bar(self, url):
        self.url_bar.setText(url.toString())
        
    def update_progress(self, progress):
        if progress < 100:
            self.progress_bar.show()
            self.progress_bar.setValue(progress)
        else:
            self.progress_bar.hide()
            
    def update_status(self, ok):
        if ok:
            self.status_bar.showMessage('加载完成', 2000)
        else:
            self.status_bar.showMessage('加载失败', 2000)
            
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F5:
            self.web_view.reload()
        elif event.key() == Qt.Key_Escape:
            self.web_view.stop()
        super().keyPressEvent(event)

def main():
    os.environ['QTWEBENGINE_DISABLE_SANDBOX'] = '1'
    
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    
    browser = MiniBrowser()
    browser.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()