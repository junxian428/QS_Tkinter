from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PySide2 import QtGui
from openpyxl import load_workbook
from subprocess import call
from tkinter import messagebox

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
          super(Ui, self).__init__()
          uic.loadUi('Column_Reinforcement.ui', self) # Load the .ui file
          self.button = self.findChild(QtWidgets.QPushButton, 'WriteExcel')
          self.button.clicked.connect(self.WriteExcelFunction)
          #calculateQ
          self.button_1 = self.findChild(QtWidgets.QPushButton, 'calculateQ')
          self.button_1.clicked.connect(self.CalculateQFunction)
          self.button_2 = self.findChild(QtWidgets.QPushButton, 'SubmitExcel')
          self.button_2.clicked.connect(self.Submit)
          self.show() # Show the GUI
    def Submit(self):
          print("Hello World")
          #text1 text2 text3 text4 text5 text6
          #lengthperbar
          #quantity
          #lengthperlink
          #DOLN
          #DBL
          #numberoflink
          #quantity_final
          #location
          new_row_data = [[self.text1.text(), self.text2.text(), self.text3.text(),self.text4.text(),self.text5.text(), self.text6.text(),self.lengthperbar.text(),self.quantity.text(),self.lengthperlink.text(),self.DOLN.text(),self.DBL.text(),self.numberoflink.text(),self.quantity_final.text(),self.location.text()]]
          wb = load_workbook("column_reinforcement.xlsx")
          ws = wb.worksheets[0]
          for row_data in new_row_data:
             ws.append(row_data)

          wb.save("column_reinforcement.xlsx")
          messagebox.showinfo("Info", "Info: You have written into Excel File")

#
    def CalculateQFunction(self):
          #quantity reinforce_link numberoflink
          print("Hello")
          if(self.quantity.text()== "" or self.reinforce_link.text() == "" or self.numberoflink.text() == ""):
              messagebox.showinfo("Error", "Info:You need to have the reinforcement bar,reinforce_link and number of link before operations")
          else:
              float_quantity = float(self.quantity.text())
              float_reinforce_link = float(self.reinforce_link.text())
              float_numberoflink = float(self.numberoflink.text())
              float_answer = (float_quantity + float_reinforce_link) * float_numberoflink
              str_answer = str(float_answer)
              self.quantity_final.setText(str_answer)
              print("Hello")

    def WriteExcelFunction(self):
        #print("Hello World")
        #print(self.comboBox.currentText())
        #comboBox_2
        #print(self.comboBox_2.currentText())
        #radioButton
        if(self.radioButton.isChecked() == True):
            print("High Tensile Steel Main Bars")
            print(self.DOLN.text())
            print(self.DBL.text())
            if(self.comboBox.currentText() == "select your diammeter"):
                messagebox.showinfo("Error", "Info:You have not selected diammeter")
            elif (self.comboBox.currentText() == "8mm diammeter"):
                print("8mm diammeter is selected")
                float_lengthperbar = float(self.lengthperbar.text())
                diammeter = 0.008
                answer = 6 * diammeter * (float_lengthperbar/1000)
                str_answer = str(answer)
                print(str_answer)
                self.quantity.setText(str_answer)


            elif (self.comboBox.currentText() == "10mm diammeter"):
                print("10mm diammeter is selected")
                float_lengthperbar = float(self.lengthperbar.text())
                diammeter = 0.01
                answer = 6 * diammeter * (float_lengthperbar/1000)
                str_answer = str(answer)
                print(str_answer)
                self.quantity.setText(str_answer)

            elif (self.comboBox.currentText() == "12mm diammeter"):
                print("12mm diammeter is selected")
                float_lengthperbar = float(self.lengthperbar.text())
                diammeter = 0.012
                answer = 6 * diammeter * (float_lengthperbar/1000)
                str_answer = str(answer)
                print(str_answer)
                self.quantity.setText(str_answer)
            elif (self.comboBox.currentText() == "16mm diammeter"):
                 print("16mm diammeter is selected")
                 float_lengthperbar = float(self.lengthperbar.text())
                 diammeter = 0.016
                 answer = 6 * diammeter * (float_lengthperbar/1000)
                 str_answer = str(answer)
                 print(str_answer)
                 self.quantity.setText(str_answer)
            elif (self.comboBox.currentText() == "20mm diammeter"):
                 print("20mm diammeter is selected")
                 float_lengthperbar = float(self.lengthperbar.text())
                 diammeter = 0.02
                 answer = 6 * diammeter * (float_lengthperbar/1000)
                 str_answer = str(answer)
                 print(str_answer)
                 self.quantity.setText(str_answer)
            elif (self.comboBox.currentText() == "25mm diammeter"):
                 print("25mm diammeter is selected")
                 float_lengthperbar = float(self.lengthperbar.text())
                 diammeter = 0.025
                 answer = 6 * diammeter * (float_lengthperbar/1000)
                 str_answer = str(answer)
                 print(str_answer)
                 self.quantity.setText(str_answer)
            elif (self.comboBox.currentText() == "32mm diammeter"):
                 print("32mm diammeter is selected")
                 float_lengthperbar = float(self.lengthperbar.text())
                 diammeter = 0.032
                 answer = 6 * diammeter * (float_lengthperbar/1000)
                 str_answer = str(answer)
                 print(str_answer)
                 self.quantity.setText(str_answer)
            else:
                print("Invalid Option")

        #Mild Steel Links
        if(self.radioButton_2.isChecked() == True):
            print("Mild Steel Links")
            if(self.comboBox_2.currentText() == "select your diammeter"):
                messagebox.showinfo("Error", "Info:You have not selected diammeter")
            elif (self.comboBox_2.currentText() == "8mm diammeter"):
                print("8mm diammeter is selected")
                diammeter = 0.008
                float_length = float(self.lengthperlink.text())
                reinforcement_link = (diammeter * 4 * 6) + (float_length/1000)
                str_reinforce = str(reinforcement_link)
                self.reinforce_link.setText(str_reinforce)
                float_DOLN = float(self.DOLN.text())
                float_DBL = float(self.DBL.text())
                float_answer = ((float_DOLN/1000) /(float_DBL/1000)) + 1
                str_answer = str(float_answer)
                self.numberoflink.setText(str_answer)


            elif (self.comboBox_2.currentText() == "10mm diammeter"):
                print("10mm diammeter is selected")
                diammeter = 0.01
                float_length = float(self.lengthperlink.text())
                reinforcement_link = (diammeter * 4 * 6) + (float_length/1000)
                str_reinforce = str(reinforcement_link)
                self.reinforce_link.setText(str_reinforce)
                float_DOLN = float(self.DOLN.text())
                float_DBL = float(self.DBL.text())
                float_answer = ((float_DOLN/1000) /(float_DBL/1000)) + 1
                str_answer = str(float_answer)
                self.numberoflink.setText(str_answer)
            elif (self.comboBox_2.currentText() == "12mm diammeter"):
                print("12mm diammeter is selected")
                diammeter = 0.012
                float_length = float(self.lengthperlink.text())
                reinforcement_link = (diammeter * 4 * 6) + (float_length/1000)
                str_reinforce = str(reinforcement_link)
                self.reinforce_link.setText(str_reinforce)
                float_DOLN = float(self.DOLN.text())
                float_DBL = float(self.DBL.text())
                float_answer = ((float_DOLN/1000) /(float_DBL/1000)) + 1
                str_answer = str(float_answer)
                self.numberoflink.setText(str_answer)
            elif (self.comboBox_2.currentText() == "16mm diammeter"):
                print("16mm diammeter is selected")
                diammeter = 0.016
                float_length = float(self.lengthperlink.text())
                reinforcement_link = (diammeter * 4 * 6) + (float_length/1000)
                str_reinforce = str(reinforcement_link)
                self.reinforce_link.setText(str_reinforce)
                float_DOLN = float(self.DOLN.text())
                float_DBL = float(self.DBL.text())
                float_answer = ((float_DOLN/1000) /(float_DBL/1000)) + 1
                str_answer = str(float_answer)
                self.numberoflink.setText(str_answer)
            elif (self.comboBox_2.currentText() == "20mm diammeter"):
                print("20mm diammeter is selected")
                diammeter = 0.202
                float_length = float(self.lengthperlink.text())
                reinforcement_link = (diammeter * 4 * 6) + (float_length/1000)
                str_reinforce = str(reinforcement_link)
                self.reinforce_link.setText(str_reinforce)
                float_DOLN = float(self.DOLN.text())
                float_DBL = float(self.DBL.text())
                float_answer = ((float_DOLN/1000) /(float_DBL/1000)) + 1
                str_answer = str(float_answer)
                self.numberoflink.setText(str_answer)
            elif (self.comboBox_2.currentText() == "25mm diammeter"):
                print("25mm diammeter is selected")
                diammeter = 0.025
                float_length = float(self.lengthperlink.text())
                reinforcement_link = (diammeter * 4 * 6) + (float_length/1000)
                str_reinforce = str(reinforcement_link)
                self.reinforce_link.setText(str_reinforce)
                float_DOLN = float(self.DOLN.text())
                float_DBL = float(self.DBL.text())
                float_answer = ((float_DOLN/1000) /(float_DBL/1000)) + 1
                str_answer = str(float_answer)
                self.numberoflink.setText(str_answer)
            elif (self.comboBox_2.currentText() == "32mm diammeter"):
                print("32mm diammeter is selected")
                diammeter = 0.032
                float_length = float(self.lengthperlink.text())
                reinforcement_link = (diammeter * 4 * 6) + (float_length/1000)
                str_reinforce = str(reinforcement_link)
                self.reinforce_link.setText(str_reinforce)
                float_DOLN = float(self.DOLN.text())
                float_DBL = float(self.DBL.text())
                float_answer = ((float_DOLN/1000) /(float_DBL/1000)) + 1
                str_answer = str(float_answer)
                self.numberoflink.setText(str_answer)
            else:
                print("Invalid Option")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

