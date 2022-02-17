from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PySide2 import QtGui
from openpyxl import load_workbook
from subprocess import call
from tkinter import messagebox

global str_total
global location
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
          super(Ui, self).__init__()
          uic.loadUi('Column_Formwork.ui', self) # Load the .ui file
          self.button = self.findChild(QtWidgets.QPushButton, 'parameter')
          self.button.clicked.connect(self.CalculateParameter)
          self.button = self.findChild(QtWidgets.QPushButton, 'area')
          self.button.clicked.connect(self.CalculateArea)
          self.button = self.findChild(QtWidgets.QPushButton, 'WriteExcel')
          self.button.clicked.connect(self.WriteExcelFunction)
          #pushButton_3
          self.Canvas = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
          self.Canvas.clicked.connect(self.WriteCanvas)
          self.show() # Show the GUI
    def CalculateParameter(self):
          #print('Hello World')
          #print(self.length.text())
          #print(self.width.text())
          #print(self.height.text())
          length = float(self.length.text())
          width = float(self.width.text())
          parameter = ((length/1000) * 2) + ((width/1000)*2)
          print(parameter)
          str_parameter = str(parameter)
          self.ParameterAnswer.setText(str_parameter)
          #(2*l/1000 + 2*w/1000)*h/1000*q
          #print(self.quantity.text())

    def CalculateArea(self):
        length = float(self.length.text())
        width = float(self.width.text())
        height = float(self.height.text())
        quantity = float(self.quantity.text())
        total_area = (2*length/1000 + 2*width /1000) *height/1000 * quantity
        str_total_area = str(total_area)
        self.area_answer.setText(str_total_area)

    def WriteExcelFunction(self):
        #print("Hello World")
        new_row_data = [[self.box1.text(), self.box2.text(), self.box3.text(),self.box4.text(),self.quantity.text(), self.length.text(),self.width.text(),self.height.text(),self.ParameterAnswer.text(),self.area_answer.text(),self.box5.text()]]
        wb = load_workbook("column_formwork.xlsx")
        ws = wb.worksheets[0]
        for row_data in new_row_data:
           ws.append(row_data)

        wb.save("column_formwork.xlsx")
        messagebox.showinfo("Info", "Info: You have written into Excel File")

    def WriteCanvas(self):
        call(["python", "paint.py"])













app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


