from openpyxl import Workbook
from openpyxl.drawing.image import Image

class Read:

    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        print("Reading file: ", self.filename)

    def returnfilename(self):
        return self.filename


   