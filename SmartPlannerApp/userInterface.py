import sys
from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
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
            print(f)



        # button = QPushButton("Browse")
        # button.setCheckable(True)
        # button.clicked.connect(self.button_clicked)

        # self.setCentralWidget(button)

#     def button_clicked(self):
#         print("Clicked!")



