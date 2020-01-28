from MatrixGui import Ui_Dialog
import sys
import numpy as np
from Stack_for_Complex import *
from Polynomial_To_Lambda import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5

e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class p:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def getFromArray(self, arr):
        self.x = arr[0][0]
        self.y = arr[1][0]
    def returnArray(self):
        return [ [self.x],[self.y] ]
    
    def Xset(self,x):
        self.x = x
    def Yset(self,y):
        self.y = y
    def Xget(self):
        return self.x
    def Yget(self):
        return self.y


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ApplicationWindow, self).__init__(parent)
        
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.functionInput.setText("x")
        
        self.matrixStack = Stack()
        
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 5)))
        
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(dynamic_canvas, self))
        
        self.ui.InsertGraphInto.addWidget(dynamic_canvas)
        
        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self.setCanvas()
        
        self.ui.MakeGraph.clicked.connect(self.getEquation)
        self.ui.ApplyTransformation.clicked.connect(self.applyTransformation)
        self.ui.ClearGraph.clicked.connect(self.clearGraph)
        self.ui.UndoButton.clicked.connect(self.undoTransform)
    
    
    def undoTransform(self):
        self.clearGraph()
        self.makeGraph()
        self.matrixStack.pop()
        self.stackInterpret()
    
    def clearGraph(self):
        self._dynamic_ax.clear()
        self.setCanvas()
        self._dynamic_ax.figure.canvas.draw()
    
    
    def stackInterpret(self):
        for i in self.matrixStack.array:
            self.transform(i)
    
    def setCanvas(self):
        self._dynamic_ax.set_aspect(1)
        self._dynamic_ax.axhline(y=0, color="k")
        self._dynamic_ax.axvline(x=0, color="k")
        self._dynamic_ax.axis([-16,16,-16,16])
        self._dynamic_ax.grid(which="major",linestyle="-",color="blue")
        self._dynamic_ax.minorticks_on()
        self._dynamic_ax.grid(which="minor",linestyle=":",color="black")
    
    def transform(self,matrix):
        try:
            new_x = []
            new_y = []
            for i in range(len(self.tst_x)):
               tmp = p(self.tst_x[i],self.tst_y[i])
               a = np.matmul(np.array(matrix),np.array(tmp.returnArray()))
               new_x.append(a[0])
               new_y.append(a[1])
            self._dynamic_ax.plot(new_x,new_y,"c")
            self._dynamic_ax.figure.canvas.draw()
            new_x = []
            new_y = []
            try:
                for i in range(len(self.tst_x_neg)):
                   tmp = p(self.tst_x_neg[i],self.tst_y_neg[i])
                   a = np.matmul(np.array(matrix),np.array(tmp.returnArray()))
                   new_x.append(a[0])
                   new_y.append(a[1])
            except:
                pass
            self._dynamic_ax.plot(new_x,new_y,"c")
            self._dynamic_ax.figure.canvas.draw()
        except:
            pass
    
    
    def applyTransformation(self):
        try:
            tleft = self.ui.TopLeftMatrix.value()
            bleft = self.ui.BottomLeftMatrix.value()
            tright = self.ui.TopRightMatrix.value()
            bright = self.ui.BottomRightMatrix.value()
            self.setCanvas()
            
            matrix = [
                [tleft,tright],
                [bleft,bright]
                            ]
            self.matrixStack.addItem(matrix)
            self.transform(matrix)
            
            
        except:
            pass
        
    
    def getEquation(self):
        try:
            f_ = self.ui.functionInput.text()
            f_ = f_.lower()
            f = ConvertIntoEquation(f_)
            self.equation = f
            self.makeGraph()
        except:
            pass
    
    def makeGraph(self):
        try:
            f = self.equation
            self._dynamic_ax.clear()
            self.setCanvas()
            self.tst_x_neg = []
            self.tst_y_neg = []
            self.tst_x = []
            self.tst_y = []
            for x in range(-3200,3300):
                try:
                    self.tst_x.append(x/100)
                    self.tst_y.append(f(x/100))
                except:
                    del self.tst_x[len(self.tst_x)-1]
                    self.tst_x_neg = self.tst_x
                    self.tst_y_neg = self.tst_y
                    self._dynamic_ax.plot(self.tst_x,self.tst_y, "r")
                    self._dynamic_ax.figure.canvas.draw()
                    self.tst_x = []
                    self.tst_y = []
            
            
            self._dynamic_ax.plot(self.tst_x,self.tst_y, "r")
            self._dynamic_ax.figure.canvas.draw()
            
            
            
        except:
            print("Failure")
        


def main():
    e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()