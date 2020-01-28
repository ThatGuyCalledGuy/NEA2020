from Complex_Class import *
from random import randint as ra
import sys

def lociToText(locus_type, c1, r=None, theta=None, c2=None):
    if locus_type == "circle":
        text = "|z - (" + c1.name + ")| = " + str(r)
    elif locus_type == "half-line":
        text = "arg(z - (" + c1.name + ")) = pi/"+str(int(np.pi/theta))
    else:
        textoptions =["|z - (" + c1.name + ")| = |z - (" + c2.name + ")|","|z - (" + c2.name + ")| = |z - (" + c1.name + ")|"]
        return textoptions
    return text
    

def lociTypeDecider(locus_type):
    if locus_type == 1:
        return "circle"
    elif locus_type == 2:
        return "half-line"
    elif locus_type == 3:
        return "bisector"



def lociMarkChecker(user_input="",answer=""):
    print (answer)
    test = answer.split("(")
    test += test[1].split(")")
    print(test)
    #test[2].split("=")
    print(test)
    total_mark = 0
    #parts for bisector |z - (, c1 name, )| = |z - (, c2 name, )| ###White Space not included - accept integers (i.e 1 and 1.0 accepted)
    #parts for circle |z - (, c1 name, )| =, radius
    #parts for half-line arg(z - (, c1 name, )) = , pi/(np.pi/theta)
    
    
        