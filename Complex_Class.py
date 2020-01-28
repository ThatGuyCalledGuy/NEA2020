from sympy.solvers import solve
from sympy import Symbol
import numpy as np
import matplotlib.pyplot as plt


def QRound(num,base):
    return round(num*base)/base
    

class Complex():
    def __init__ (self, real_part=0, imaginary_part=0, mod=0, arg=0):
        self.re = real_part
        self.im = imaginary_part
        self.mod = mod
        self.arg = arg
        self.set_name()
        
    def set_name(self):
        if int(self.im) >= 0:
            self.name = str(QRound(self.re,100)) + " + " + str(QRound(self.im,100)) + "i"
        else:
            self.name = str(QRound(self.re,100)) + " - " + str(-1*QRound(self.im,100)) + "i"

       
    def findReIm(self, update=False):
        im = self.mod * np.sin(self.arg)
        re = self.mod * np.cos(self.arg)
        if not update:
            return re, im
        else:
            self.re = re
            self.im = im
            self.set_name()
    
    
    def findMod(self, update=False):
        mod = np.sqrt((self.re ** 2) + (self.im ** 2))
        if not update:
            return mod
        else:
            self.mod = mod
    
    
    def findArg(self, update=False):
        arg = np.arctan((self.im/self.re))
        if not update:
            return arg
        else:
            self.arg = arg
    
    
    def __add__ (self, other):
        if type(other) != int and type(other) != float and type(other) != Complex:
            pass
        else:
            if type(other) != Complex:
                other = Complex(other,0)
            cr = Complex_Add(self,other)
            return cr
    
    def __radd__ (self, other):
        return self.__add__(other)
    
    
    def __sub__ (self, other):
        if type(other) != int and type(other) != float and type(other) != Complex:
            pass
        else:
            if type(other) != Complex:
                other = Complex(other,0)
            cr = Complex_Sub(self,other)
            return cr
    
    def __rsub__ (self, other):
        return self.__sub__(other)
    
    def __mul__ (self,other):
        if type(other) != int and type(other) != float and type(other) != Complex:
            pass
        else:
            if type(other) != Complex:
                other = Complex(other,0)
            cr = Complex_Mult(self,other)
            return cr
    
    def __rmul__ (self, other):
        return self.__mul__(other)
    
    def __div__ (self,other):
        if type(other) != int and type(other) != float and type(other) != Complex:
            pass
        else:
            if type(other) != Complex:
                other = Complex(other,0)
            cr = Complex_Div(self,other)
            return cr
    def __rdiv__ (self,other):
        if type(other) != int and type(other) != float and type(other) != Complex:
            pass
        else:
            if type(other) != Complex:
                other = Complex(other,0)
            cr = Complex_Div(other,self)
            return cr
    
    def __str__ (self):
        return str(self.name)
                


class Locus():
    def __init__ (self, Locus_type, c1, r=None,c2=None,theta=None):
        fig, ax = plt.subplots(1)
        if Locus_type == "circle":
            # theta goes from 0 to 2pi
            theta = np.linspace(0, 2*np.pi, 100)

            # the radius of the circle
            r = r

            # compute x1 and x2
            x1 = r*np.cos(theta) + c1.re
            x2 = r*np.sin(theta) + c1.im
            
            # create the figure
            ax.plot(x1, x2)
            ax.set_aspect(1)
            plt.plot([c1.re],[c1.im],"ro")
            plt.axhline(y=0, color="k")
            plt.axvline(x=0, color="k")
            plt.xlabel("Re")
            plt.ylabel("Im")
            plt.axis([-16,16,-16,16])
            plt.grid(which="major",linestyle="-",color="blue")
            plt.minorticks_on()
            plt.grid(which="minor",linestyle=":",color="black")
            plt.show()
            
            
        elif Locus_type == "half-line":
            r = 32
            x1 = (r*np.cos(theta)) + c1.re
            y2 = (r*np.sin(theta)) + c1.im

            ax.plot([c1.re,x1], [c1.im,y2])
            ax.set_aspect(1)
            plt.plot([c1.re],[c1.im],"ro")
            plt.axhline(y=0, color="k")
            plt.axvline(x=0, color="k")
            plt.xlabel("Re")
            plt.ylabel("Im")
            plt.axis([-16,16,-16,16])
            plt.grid(which="major",linestyle="-",color="blue")
            plt.minorticks_on()
            plt.grid(which="minor",linestyle=":",color="black")
            plt.show()
         
         
        elif Locus_type == "bisector":
            new_c = Complex((c1.re+c2.re)/2,(c1.im+c2.im)/2)
            if c2.im - c1.im != 0 and c2.re - c1.re != 0:
                grad = (c2.im - c1.im)/(c2.re - c1.re)
                bisect_grad = (-1)/grad
                def f(x):
                    y = bisect_grad*(x-new_c.re) + new_c.im
                    return y
                x = np.arange(-32, 32, 1)
                y = f(x)
                plt.plot(x,y, color="c")
            elif c2.im - c1.im == 0:
                plt.axvline(x=new_c.re, color="c")
            elif c2.re - c1.re == 0:
                plt.axhline(y=new_c.im, color="c")
            ax.set_aspect(1)
            plt.plot([c1.re,c2.re],[c1.im,c2.im],"ro")
            plt.axhline(y=0, color="k")
            plt.axvline(x=0, color="k")
            plt.xlabel("Re")
            plt.ylabel("Im")
            plt.axis([-16,16,-16,16])
            plt.grid(which="major",linestyle="-",color="blue")
            plt.minorticks_on()
            plt.grid(which="minor",linestyle=":",color="black")
            plt.show()
       
       
def showLocus(Locus_type, c1, r=None, theta=None, c2=None):
    Locus(Locus_type, c1, r, c2, theta)
        
def plot(cList, labels=False):
    fig, ax = plt.subplots(1)
    ax.set_aspect(1)
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    for i in cList:
        plt.plot([0,i.re],[0,i.im], "r")
        if labels:
           plt.text(i.re, i.im, i.name)
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.axis([-16,16,-16,16])
    plt.grid(which="major",linestyle="-",color="blue")
    plt.minorticks_on()
    plt.grid(which="minor",linestyle=":",color="black")
    plt.show()


def Complex_Conj(c1):
    return Complex(c1.re, -1*c1.im)


def Complex_Add(c1, c2):
    re_s = c1.re + c2.re
    im_s = c1.im + c2.im
    return Complex(re_s,im_s)


def Complex_Sub(c1, c2):
    return Complex_Add(c1, c2*-1)


def Complex_Div(c1, c2):
    top = Complex_Mult(c1,Complex_Conj(c2))
    bottom = Complex_Mult(c2,Complex_Conj(c2)).re
    return Complex(top.re/bottom, top.im/bottom)


def Complex_Mult(c1, c2):
    re_s = c1.re * c2.re + -1 *(c1.im * c2.im)
    im_s = c1.re * c2.im + c2.re * c1.im
    return Complex(re_s,im_s)


def deMoivre(c1,n):
    r = c1.findMod()
    theta = c1.findArg()
    ctmp = (r**n)*Complex(np.cos(n*theta), np.sin(n*theta))
    return ctmp

def Roots_of_Unity(n):
    clist = [Complex(np.cos((2*k*np.pi)/n),np.sin((2*k*np.pi)/n)) for k in range(0,n)]
    return clist


def plot_r_n(clist):
    for i in clist:
        print(i.name)
    fig, ax = plt.subplots(1)
    theta = np.linspace(0, 2*np.pi, 100)
    x1 = np.cos(theta)
    x2 = np.sin(theta)
    xs = [x.re for x in clist]
    xs.append(clist[0].re)
    ys = [y.im for y in clist]
    ys.append(clist[0].im)
    ax.plot(xs,ys)
    ax.scatter(xs,ys)
    ax.plot(x1, x2, ":")
    ax.set_aspect(1)
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.axis([-1.5,1.5,-1.5,1.5])
    plt.grid(which="major",linestyle="-",color="blue")
    plt.minorticks_on()
    plt.grid(which="minor",linestyle=":",color="black")
    plt.show()
    

def Complex_Index(c1, index):
    cR = c1
    for i in range(index - 1):
        cR = Complex_Mult(c1,cR)
    return cR
        
        
def Complex_Root(c1):
    if c1.im == 0:
        return Complex(np.sqrt(c1.re),0),Complex(-1*np.sqrt(c1.re),0)
    a = Symbol("a")
    b = Symbol("b")
    real_values = solve((a**4) - (c1.re * a**2) - (0.5 * c1.im) ** 2, a)
    del real_values[2]
    del real_values[2]
    imaginary_values = []
    for i in real_values:
        b = (0.5 * c1.im)/i
        imaginary_values.append(b)
    return Complex(real_values[0], imaginary_values[0]),Complex(real_values[1], imaginary_values[1])


def return_Roots(c1):
    roots = Complex_Root(c1)
    print (roots[0].name + ", " + roots[1].name)