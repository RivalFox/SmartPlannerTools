import sys
from PySide6.QtWidgets import QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Planner Tool")

        button = QPushButton("Browse")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self):
        print("Clicked!")



