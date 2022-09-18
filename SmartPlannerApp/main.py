from cgi import print_directory
import sys
from tkinter.tix import InputOnly
import userInterface
from Parser import *
from Extractor import extractData
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

def main():
    app = QApplication([])
    window = userInterface.MainWindow()
    window.show()

    parse(window.getPath())

    extractData(getPath(), getInput(), getPrereq())

    #extracted_data = extractor(parsed_args.path)
    #instructions = analyzer(extracted_data.input1, extracted_data.input2, extracted_data.input3)
    #output = compiler(extracted_data, instructions)
    #place_output_in_folder(output)

    #sys.exit(app.exec())

if __name__ == "__main__":
    main()



