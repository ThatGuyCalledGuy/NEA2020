from ComplexGui import Ui_MainGui
from ComplexLociGui import Ui_LociGui
from ComplexCalcGui import Ui_C
from VectorGui import Ui_Vector
from VectorTest import *
from Complex_Class import *
from MatrixGui import Ui_Dialog
from Polynomial_To_Lambda import *
from ComplexRoots import Ui_Dialog as Ui_Roots
from Stack_for_Complex import Stack
from Point_Class import p
import MatrixTests as mt
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


class VectorWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(VectorWindow, self).__init__(parent)
        
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
        self._dynamic_ax.scatter(xs=[],ys=[],zs=[])
        self._dynamic_ax.plot(xs=x,ys=y,zs=z)
        
    def plotPlane(self,plane):
        x,y,z = get_xyz_of_plane(plane)
        self._dynamic_ax.scatter(xs=[],ys=[],zs=[])
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
        self._dynamic_ax.scatter(xs=[],ys=[],zs=[])
    
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


class RootWindow(QtWidgets.QMainWindow):
    def __init__ (self,parent=None):
        super(RootWindow, self).__init__(parent)
        
        self.ui = Ui_Roots()
        self.ui.setupUi(self)
        self.ui.MakeRootButton.clicked.connect(self.makeRoot)
        
        
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 5)))
        
        
        self.ui.InsertGraph.addWidget(dynamic_canvas)
        
        self.addToolBar(QtCore.Qt.BottomToolBarArea,
                        NavigationToolbar(dynamic_canvas, self))
        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self._dynamic_ax.set_aspect(1)
        self._dynamic_ax.axhline(y=0, color="k")
        self._dynamic_ax.axvline(x=0, color="k")
        self._dynamic_ax.axis([-1.5,1.5,-1.5,1.5])
        self._dynamic_ax.grid(which="major",linestyle="-",color="blue")
        self._dynamic_ax.minorticks_on()
        self._dynamic_ax.grid(which="minor",linestyle=":",color="black")
    
    def clearGraph(self):
        self._dynamic_ax.clear()
        self.setCanvas()
        self._dynamic_ax.figure.canvas.draw()
    
    def setCanvas(self):    
        self._dynamic_ax.set_aspect(1)
        self._dynamic_ax.axhline(y=0, color="k")
        self._dynamic_ax.axvline(x=0, color="k")
        self._dynamic_ax.axis([-1.5,1.5,-1.5,1.5])
        self._dynamic_ax.grid(which="major",linestyle="-",color="blue")
        self._dynamic_ax.minorticks_on()
        self._dynamic_ax.grid(which="minor",linestyle=":",color="black")

    def makeRoot(self):
        self.clearGraph()
        n = self.ui.NthRoot.value()
        clist = Roots_of_Unity(n)
        theta = np.linspace(0, 2*np.pi, 100)
        x1 = np.cos(theta)
        x2 = np.sin(theta)
        xs = [x.re for x in clist]
        xs.append(clist[0].re)
        ys = [y.im for y in clist]
        ys.append(clist[0].im)
        self._dynamic_ax.plot(xs,ys)
        self._dynamic_ax.scatter(xs,ys)
        self._dynamic_ax.plot(x1, x2, ":")
        self._dynamic_ax.figure.canvas.draw()


class CalcWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(CalcWindow, self).__init__(parent)
        
        self.ui = Ui_C()
        self.ui.setupUi(self)
        
        self.ui.AdditionButton.clicked.connect(self.Add)
        self.ui.SubtractionButton.clicked.connect(self.Sub)
        self.ui.MultiplyButton.clicked.connect(self.Mult)
        self.ui.DivideButton.clicked.connect(self.Div)
        self.ui.RootButton.clicked.connect(self.Root)
        self.ui.ConjButton.clicked.connect(self.Conj)
        
    
    
    def DisplayResult(self, List=False):
        if List:
            list_string = ""
            for i in self.resultList:
                if i == self.resultList[0]:
                    list_string += i.name + ", "
                else:
                    list_string += i.name
            self.ui.textBrowser.setHtml('''<html><body><p>''' + list_string + '''</p></body></html>''')
        else:
            self.ui.textBrowser.setHtml('''<html><body><p>''' + self.result.name + '''</p></body></html>''')
    
    def GetCurrentComplex(self):
        self.c1 = Complex(self.ui.RealPartBox.value(),self.ui.ImaginaryPartBox.value())
        self.c2 = Complex(self.ui.RealPartBox_2.value(),self.ui.ImaginaryPartBox_2.value())
    
    def Add(self):
        self.GetCurrentComplex()
        self.result = Complex_Add(self.c1,self.c2)
        self.DisplayResult()
    
    def Sub(self):
        self.GetCurrentComplex()
        self.result = Complex_Sub(self.c1,self.c2)
        self.DisplayResult()

    def Mult(self):
        self.GetCurrentComplex()
        self.result = Complex_Mult(self.c1,self.c2)
        self.DisplayResult()
    
    def Div(self):
        self.GetCurrentComplex()
        self.result = Complex_Div(self.c1,self.c2)
        self.DisplayResult()
    
    def Root(self):
        self.GetCurrentComplex()
        self.resultList = Complex_Root(self.c1)
        self.DisplayResult(List=True)
    
    def Conj(self):
        self.GetCurrentComplex()
        self.result = Complex_Conj(self.c1)
        self.DisplayResult()


class LociWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(LociWindow, self).__init__(parent)
        
        self.ui = Ui_LociGui()
        self.ui.setupUi(self)

        self.ui.MakeCircleButton.clicked.connect(self.circle_clicked)
        self.ui.MakeBisectorButton.clicked.connect(self.bisect_clicked)
        self.ui.MakeHalfLineButton.clicked.connect(self.halfline_clicked)
        self.ui.clearButton.clicked.connect(self.clearGraph)
        self.ui.undoButton.clicked.connect(self.undo)
        
        
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 5)))
        
        self.ui.InsertGraph.addWidget(dynamic_canvas)
        
        self._dynamic_ax = dynamic_canvas.figure.subplots()
        self.setCanvas()
        
        
        self.lociStack = Stack()
    
    
    
    def interpretStack(self):
        
        for i in self.lociStack.array:
            if i[0] == "c":
                self.displayCircle(r = i[2],c1 = i[1])
                
            elif i[0] == "h":
                self.displayHalfLine(theta = i[2],c1 = i[1])
                
            else:
                self.displayBisector(c2= i[2],c1 = i[1])
                
    
    def undo(self):
        
        tst = self.lociStack.pop()
        self._dynamic_ax.clear()
        self.setCanvas()
        self._dynamic_ax.figure.canvas.draw()
        self.interpretStack()
    
    
    
    def setCanvas(self):
        
        self._dynamic_ax.set_aspect(1)
        self._dynamic_ax.axhline(y=0, color="k")
        self._dynamic_ax.axvline(x=0, color="k")
        self._dynamic_ax.axis([-16,16,-16,16])
        self._dynamic_ax.grid(which="major",linestyle="-",color="blue")
        self._dynamic_ax.minorticks_on()
        self._dynamic_ax.grid(which="minor",linestyle=":",color="black")
    
    def clearGraph(self):
        
        self._dynamic_ax.clear()
        self.lociStack.clear()
        self.setCanvas()
        self._dynamic_ax.figure.canvas.draw()
    
    def displayCircle(self,r = 1,c1 = Complex(0,0)):
        
        self.CurrentComplexUpdate()
        
        # theta goes from 0 to 2pi
        theta = np.linspace(0, 2*np.pi, 100)
        
        # compute x1 and x2
        x1 = r*np.cos(theta) + c1.re
        x2 = r*np.sin(theta) + c1.im
        
        
        # create the figure
        
        
        self.setCanvas()
        self._dynamic_ax.plot(x1, x2)
        self._dynamic_ax.plot([c1.re],[c1.im],"ro")
        
        
        self._dynamic_ax.figure.canvas.draw()
    
    
    def displayHalfLine(self,theta = 0,c1 = Complex(0,0)):
        
        
        r = 32
        
        #parametric equation for a circle, however, because theta is at a set value, not like the list above, it produces a point on a circle where the angle is theta, producing a half-line
        
        x1 = (r*np.cos(theta)) + c1.re
        y2 = (r*np.sin(theta)) + c1.im
        
        #creates the figure
        
        self.setCanvas()
        
        self._dynamic_ax.plot([c1.re,x1], [c1.im,y2])
        
        self._dynamic_ax.plot([c1.re],[c1.im],"ro")
        
        self._dynamic_ax.figure.canvas.draw()
        
        
    def displayBisector(self,c1 = Complex(0,0),c2 = Complex(1,1)):
        self.CurrentComplexUpdate()
        
        #finds the midpoiny between the two
        
        new_c = Complex((c1.re+c2.re)/2,(c1.im+c2.im)/2)
        
        # Finds the gradient between the two lines and then finds the normal, the gradient for the new line
        
        if c2.im - c1.im != 0 and c2.re - c1.re != 0:
            grad = (c2.im - c1.im)/(c2.re - c1.re)
            bisect_grad = (-1)/grad
            f = lambda x: bisect_grad * (x-new_c.re) + new_c.im
            x = np.arange(-32, 32, 1)
            y = f(x)
            self._dynamic_ax.plot(x,y)
        elif c2.im - c1.im == 0:
            self._dynamic_ax.axvline(x=new_c.re)
        elif c2.re - c1.re == 0:
            self._dynamic_ax.axhline(y=new_c.im)
        
        self._dynamic_ax.plot([c1.re,c2.re],[c1.im,c2.im],"ro")
        
        self.setCanvas()
        
        self._dynamic_ax.figure.canvas.draw()
    
    def CurrentComplexUpdate(self):
        self.currentRe = self.ui.RealPartBox.value()
        
        self.currentIm = self.ui.ImaginaryPartBox.value()
        
        self.currentC = Complex(self.currentRe, self.currentIm)
    
    
    def circle_clicked(self):
        self.CurrentComplexUpdate()
        self.currentR = self.ui.RadiusBox.value()
        self.lociStack.addItem(["c",self.currentC,self.currentR])
        self.displayCircle(r=self.currentR, c1=self.currentC)
        #showLocus("circle", self.currentC, r=self.currentR)
    
    
    def halfline_clicked(self):
        self.CurrentComplexUpdate()
        self.currentTh = self.ui.ThetaBox.value()
        self.lociStack.addItem(["h",self.currentC,self.currentTh])
        self.displayHalfLine(theta=self.currentTh,c1=self.currentC)
        #showLocus("half-line", self.currentC, theta=self.currentTh)
        
    
    def bisect_clicked(self):
        self.CurrentComplexUpdate()
        self.currentC2 = Complex(self.ui.BisectRealBox.value(),self.ui.BisectImBox.value())
        self.lociStack.addItem(["b",self.currentC,self.currentC2])
        self.displayBisector(c1=self.currentC,c2=self.currentC2)
        #showLocus("bisector", self.currentC, c2=self.currentC2)
        

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ApplicationWindow, self).__init__(parent)
        
        self.ui = Ui_MainGui()
        self.ui.setupUi(self)
        self.graphlist = []
        
        
        dynamic_canvas = FigureCanvas(Figure(figsize=(5, 5)))
        
        
        self.ui.InsertGraph.addWidget(dynamic_canvas)
        
        self._dynamic_ax = dynamic_canvas.figure.subplots()
        plt.xlabel("Re")
        plt.ylabel("Im")
        self._dynamic_ax.set_aspect(1)
        self._dynamic_ax.axhline(y=0, color="k")
        self._dynamic_ax.axvline(x=0, color="k")
        self._dynamic_ax.axis([-16,16,-16,16])
        self._dynamic_ax.grid(which="major",linestyle="-",color="blue")
        self._dynamic_ax.minorticks_on()
        self._dynamic_ax.grid(which="minor",linestyle=":",color="black")
        
        
        self.ui.AddToGraphButton.clicked.connect(self.addtolist_click)
        self.ui.ClearGraphListButton.clicked.connect(self.clear_click)
        self.ui.MakeGraphButton.clicked.connect(self.makegraph_click)
        self.ui.LociButton.clicked.connect(self.go_to_loci_clicked)
        self.ui.CalculatorButton.clicked.connect(self.go_to_calc_clicked)
        self.ui.MatrixButton.clicked.connect(self.go_to_matrix)
        self.ui.RootButton.clicked.connect(self.go_to_root)
        self.ui.VectorButton.clicked.connect(self.go_to_vector)
        self.loci = LociWindow(self)
        self.calc = CalcWindow(self)
        self.mat = MatrixWindow(self)
        self.root = RootWindow(self)
        self.vct = VectorWindow(self)
    
    def _update_canvas(self):
        label = self.getRadioState()
        self._dynamic_ax.clear()
        self._dynamic_ax.set_aspect(1)
        self._dynamic_ax.axhline(y=0, color="k")
        self._dynamic_ax.axvline(x=0, color="k")
        self._dynamic_ax.axis([-16,16,-16,16])
        self._dynamic_ax.grid(which="major",linestyle="-",color="blue")
        self._dynamic_ax.minorticks_on()
        self._dynamic_ax.grid(which="minor",linestyle=":",color="black")
        
        for i in self.graphlist:
            self._dynamic_ax.plot([0,i.re],[0,i.im], "r")
            if label:
               self._dynamic_ax.text(i.re, i.im, i.name)
        
        self._dynamic_ax.figure.canvas.draw()
    
    def go_to_loci_clicked(self):
        self.loci.show()
    
    def go_to_calc_clicked(self):
        self.calc.show()
    
    def go_to_matrix(self):
        self.mat.show()
    
    def go_to_root(self):
        self.root.show()
        
    def go_to_vector(self):
        self.vct.show()
    
    def getRadioState(self):
        return self.ui.LabelRadio.isChecked()
    
    def makegraph_click(self):
        self._update_canvas()
        
    def clear_click(self):
        self.graphlist = []
        self.display_list(self.graphlist)
        self._update_canvas()
    
    def display_list(self,cList):
        list_string = ""
        for i in cList:
            list_string += i.name + "<br>"
        self.ui.ListDisplay.setHtml('''<html><body><p>'''+list_string+'''</p></body></html>''')
        

    def addtolist_click(self):
        self.currentRe = self.ui.RealPartBox.value()
        self.currentIm = self.ui.ImaginaryPartBox.value()
        self.currentC = Complex(self.currentRe, self.currentIm)
        self.graphlist.append(self.currentC)
        self.display_list(self.graphlist)
        self._update_canvas()


class MatrixWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MatrixWindow, self).__init__(parent)
        
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.functionInput.setText("x")
        self.ui.SquareDim.setValue(5.00)
        
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
        self.ui.SquareButton.clicked.connect(self.plotSquare)
    
    
    def undoTransform(self):
        self._dynamic_ax.clear()
        self.setCanvas()
        self._dynamic_ax.plot(self.tst_x,self.tst_y, "r", linewidth=2)
        self._dynamic_ax.plot(self.tst_x_neg,self.tst_y_neg, "r", linewidth=2)
        self._dynamic_ax.figure.canvas.draw()
        self.matrixStack.pop()
        self.stackInterpret()
    
    def clearGraph(self):
        self._dynamic_ax.clear()
        self.matrixStack.clear()
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
        #Creates a matrix of all the points on the graph, then multiplies that matrix by the matrix set in the GUI
        try:
            new_x = []
            new_y = []
            for i in range(len(self.tst_x)):
               tmp = p(self.tst_x[i],self.tst_y[i])
               a = mt.mult_mat_point(tmp.returnArray(),matrix) # calls function in matrix tests file that multiplies a point by a matrix
               new_x.append(a[0])
               new_y.append(a[1])
            self._dynamic_ax.plot(new_x,new_y,"m", linewidth=2)
            self._dynamic_ax.figure.canvas.draw()
            new_x = []
            new_y = []
            try:
                for i in range(len(self.tst_x_neg)): # support for asymptote
                   tmp = p(self.tst_x_neg[i],self.tst_y_neg[i])
                   a = mt.mult_mat_point(tmp.returnArray(),matrix)
                   new_x.append(a[0])
                   new_y.append(a[1])
            except:
                pass
            self._dynamic_ax.plot(new_x,new_y,"m", linewidth=2)
            self._dynamic_ax.figure.canvas.draw()
        except:
            pass
    
    
    def applyTransformation(self):
        try:
            tleft = self.ui.TopLeftMatrix.value()
            bleft = self.ui.BottomLeftMatrix.value()
            tright = self.ui.TopRightMatrix.value()
            bright = self.ui.BottomRightMatrix.value()
            
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
    
    def plotSquare(self):
        dim = self.ui.SquareDim.value()
        
        self.clearGraph()
        self.tst_x = [0,0,1*dim,1*dim,0]
        self.tst_y = [0,1*dim,1*dim,0,0]
        self.tst_x_neg = []
        self.tst_y_neg = []
        self.setCanvas()
        self._dynamic_ax.plot(self.tst_x,self.tst_y, "r", linewidth=2)
        self._dynamic_ax.figure.canvas.draw()
    
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
                    self.tst_y.append(f(x/100)) # tries to get every value, but if there's an asymptote it won't work
                except:
                    del self.tst_x[len(self.tst_x)-1] # so it removes the last piece of data
                    self.tst_x_neg = self.tst_x # and plots that half of the data
                    self.tst_y_neg = self.tst_y
                    self._dynamic_ax.plot(self.tst_x,self.tst_y, "r", linewidth=2)
                    self._dynamic_ax.figure.canvas.draw()
                    self.tst_x = [] # then resumes plotting the rest of the graph beyond the asymptote
                    self.tst_y = [] # splits data in half to have a negative end and a positive end
            
            
            self._dynamic_ax.plot(self.tst_x,self.tst_y, "r", linewidth=2)
            self._dynamic_ax.figure.canvas.draw()
            
            
            
        except:
            print("Failure")


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()