import sys
from PySide6.QtWidgets import QMainWindow

path = "./Input"

class MainWindow(QMainWindow):
    global path

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Planner Tool")
        self.resize(720, 480)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            path = f
    
    def getPath(self):
        return path
