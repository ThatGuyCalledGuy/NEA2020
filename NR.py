import math
from mpmath import *
from Polynomial_To_Lambda import ConvertIntoEquation
def get_NR_equation(f):
    tst = ConvertIntoEquation(f)
    NR = lambda x: x - tst(x)/diff(tst, x)
    return NR
def recur(initx,depth,NR):
    print (initx)
    xn = NR(initx)
    for i in range(depth):
        print(xn)
        xn = NR(xn)