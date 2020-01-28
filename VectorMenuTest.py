from VectorGui import Ui_Vector
from VectorTest import *
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ApplicationWindow, self).__init__(parent)
        
        self.ui = Ui_Vector()
        self.ui.setupUi(self)
        self.graphlist = []
        
        
        dynamic_canvas = FigureCanvas(Figure())
        self.ui.InsertGraph.addWidget(dynamic_canvas)
        
        self._dynamic_ax = dynamic_canvas.figure.add_subplot(111, projection='3d')    
        
        v1 = Vector(1,2,3)
        self.plotVector(v1)
        self._dynamic_ax.figure.canvas.draw()
        
        self.ui.ClearButton.clicked.connect(self.clearGraph)
        self.ui.PosVecButton.clicked.connect(self.makeVector)
        self.ui.LineButton.clicked.connect(self.makeLine)
        self.ui.PlaneButton.clicked.connect(self.makePlane)
        self.ui.ResVecButton.clicked.connect(self.makeResultant)
        self.ui.NormButton.clicked.connect(self.makeNormal)
    
    def plotVector(self,vector):
        x,y,z = get_xyz_of_vector(vector)
        self._dynamic_ax.scatter(xs=[0],ys=[0],zs=[0])
        self._dynamic_ax.plot(xs=x,ys=y,zs=z)
    
    def plotLine(self,line):
        x,y,z = get_xyz_of_line(line)
        self._dynamic_ax.plot(xs=x,ys=y,zs=z)
        
    def plotPlane(self,plane):
        x,y,z = get_xyz_of_plane(plane)
        self._dynamic_ax.plot(xs=x,ys=y,zs=z, alpha=0.4)
    
    def plotNormal(self,normal,pos_vec):
        temp = normal + pos_vec
        x,y,z = [pos_vec.x],[pos_vec.y],[pos_vec.z]
        x.append(temp.x)
        y.append(temp.y)
        z.append(temp.z)
        self._dynamic_ax.scatter(xs=[pos_vec.x],ys=[pos_vec.y],zs=[pos_vec.z])
        self._dynamic_ax.plot(xs=x,ys=y,zs=z)
    
    def plotResultant(self,v1,v2):
        x,y,z = [0],[0],[0]
        self._dynamic_ax.scatter(xs=x,ys=y,zs=z)
        x.append(v1.array()[0])
        y.append(v1.array()[1])
        z.append(v1.array()[2])
        x.append((v1+v2).array()[0])
        y.append((v1+v2).array()[1])
        z.append((v1+v2).array()[2])
        self._dynamic_ax.plot(xs=x,ys=y,zs=z)
        temp = Vector(x[2],y[2],z[2])
        x1,y1,z1 = get_xyz_of_vector(temp)
        self._dynamic_ax.plot(xs=x1,ys=y1,zs=z1)
    
    def makeVector(self):
        position_vector = self.getPosVec()
        self.plotVector(position_vector)
        self._dynamic_ax.figure.canvas.draw()
    
    def makeNormal(self):
        pos_vec = self.getPosVec()
        d1 = self.getD1Vec()
        d2 = self.getD2Vec()
        normal = Vector_Product(d1,d2)
        
        self.plotNormal(normal*10,pos_vec)
        self._dynamic_ax.figure.canvas.draw()
    
    def makeResultant(self):
        v1 = self.getPosVec()
        v2 = self.getD1Vec()
        self.plotResultant(v1,v2)
        self._dynamic_ax.figure.canvas.draw()
    
    def makeLine(self):
        position_vector = self.getPosVec()
        d1 = self.getD1Vec()
        line = Line(position_vector,d1)
        self.plotLine(line)
        self._dynamic_ax.figure.canvas.draw()
    
    
    def makePerpendicular(self):
        pass
        #pos_vec = self.getPosVec()
        #d1 = self.getD1Vec()
        #vector_list = perpendicular_vectors(d1)
        #for i in vector_list:
        #    line = Line(pos_vec, i)
        #    self.plotLine(line)
        #self._dynamic_ax.figure.canvas.draw()
    
    def makePlane(self):
        pv = self.getPosVec()
        d1 = self.getD1Vec()
        d2 = self.getD2Vec()
        plane = Plane(pv,d1,d2)
        self.plotPlane(plane)
        self._dynamic_ax.figure.canvas.draw()
    
    def getPosVec(self):
        position_vector = Vector(
            self.ui.PosVecX.value(),
            self.ui.PosVecY.value(),
            self.ui.PosVecZ.value()
            )
        return position_vector
    
    def getD1Vec(self):
        d1 = Vector(
            self.ui.D1X.value(),
            self.ui.D1Y.value(),
            self.ui.D1Z.value()
            )
        return d1
    
    def getD2Vec(self):
        d2 = Vector(
            self.ui.D2X.value(),
            self.ui.D2Y.value(),
            self.ui.D2Z.value()
            )
        return d2
    
    
    def clearGraph(self):
        
        self._dynamic_ax.clear()
        self._dynamic_ax.figure.canvas.draw()
        
    
    def _update_canvas(self):
        
        self._dynamic_ax.clear()
        self._dynamic_ax.figure.canvas.draw()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()