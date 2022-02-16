from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PySide2 import QtGui
from openpyxl import load_workbook
from subprocess import call

global str_total
global location
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('form.ui', self) # Load the .ui file
        self.button = self.findChild(QtWidgets.QPushButton, 'calculate')
        self.button.clicked.connect(self.printButtonPressed)
        self.Excel = self.findChild(QtWidgets.QPushButton, 'WriteExcel')
        self.Excel.clicked.connect(self.WriteExcelFunction)

        self.DrawFunction = self.findChild(QtWidgets.QPushButton, 'Art')
        self.DrawFunction.clicked.connect(self.functionDraw)
        self.show() # Show the GUI

    def printButtonPressed(self):
        print(self.length.text())
        print(self.width.text())
        print(self.height.text())
        length = float(self.length.text())
        width = float(self.width.text())
        height = float(self.height.text())
        total = (length/1000) * (width/1000) * (height/1000)
        str_total = str(total)
        self.answer.setText(str_total)
        self.submission_answer.setText(str_total)

    def WriteExcelFunction(self):
        print("Hello World")
        new_row_data = [[self.data1.text(), self.data2.text(), self.data3.text(),self.data4.text(),self.data5.text(), self.length.text(),self.width.text(),self.height.text(),self.submission_answer.text(),self.submission_location.text()]]
        wb = load_workbook("column_concrete.xlsx")
        ws = wb.worksheets[0]
        for row_data in new_row_data:
            # Append Row Values
            ws.append(row_data)

        wb.save("column_concrete.xlsx")
    def functionDraw(self):
        call(["python", "paint.py"])


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
