import sys
import userInterface
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

if __name__ == "__main__":
    app = QApplication([])

    window = userInterface.MainWindow()
    window.show()


    app.exec_()



