from PyQt5 import QtWidgets
from ComplexQuizGui import Ui_Dialog
from Complex_Class import *
from Complex_Quiz import *
from random import randint as ra
import numpy as np
import sys


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ApplicationWindow, self).__init__(parent)
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.resetValues()
        self.newlocus()
        
        
        self.ui.NewLociButton.clicked.connect(self.newlocus)
        self.ui.ShowLociButton.clicked.connect(self.showLoci)
        self.ui.CheckButton.clicked.connect(self.textCheck)
        
        
    def textCheck(self):
        self.textinput = self.ui.TextInput.text()
        print(self.textinput)
    
    def showLoci(self):
        self.loci_text = lociToText(self.locus_type_text, self.c1, self.radius, self.theta, self.c2)
        print(self.loci_text)
        Locus(self.locus_type_text, self.c1, r=self.radius, theta=self.theta, c2=self.c2)
        
        
    def resetValues(self):
        self.c1 = None
        self.locus_type = None
        self.radius = None
        self.theta = None
        self.c2 = Complex(0,0)
    
  
    def newlocus(self):
        self.resetValues()
        self.c1 = Complex(ra(-16,16),ra(-16,16))
        self.locus_type = ra(1,3)
        if self.locus_type == 1:

            self.radius = ra(1,10)
            
        elif self.locus_type == 2:

            self.c1 = Complex(ra(-12,12),ra(-12,12))
            self.rand = ra(-8,8)
            while self.rand == 0:
               self.rand = ra(-8,8)
            self.theta = np.pi / self.rand
        elif self.locus_type == 3:

            self.c2 = Complex(ra(-16,16),ra(-16,16))
        self.locus_type_text = lociTypeDecider(self.locus_type)
        
        
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()