import sys
import userInterface
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication([])
    window = userInterface.MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()    



