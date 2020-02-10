import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd


lst = [[0.1,0.3481],[0.2,0.6561],[0.3,0.9801],[0.40,1.3225],[0.5,1.6384],[0.6,1.9044]]
giver = lambda rng: [rng, rng+((random.randint(-20,20)/10)*((random.randint(1,15))))]
def generateList(n):
    lst1 = [giver(random.randint(0,1000)/10) for x in range(n)]
    return lst1

def getlst():
    terms = int(input("n >>> "))
    lst = []
    for i in range(terms):
        print("\n")
        x = float(input("x >>> "))
        y = float(input("y >>> "))
        lst.append([x,y])
    return lst
def plot(lst=None):
    if lst == None:
        lst = getlst()  
    lst.sort(key=lambda x: x[0])

    Sigxy = sum([x[0]*x[1] for x in lst])
    
    n = len(lst)
    xs = [x[0] for x in lst]
    ys = [x[1] for x in lst]
    
    logy = []
    for y in ys:
        logy.append(np.log(y))
        
    
    
    tmp = []
    for i in range(len(xs)):
        tmp.append(xs[i] * logy[i])
        
    
    LSigxy = sum(tmp)
    Sigx = sum(xs)
    Sigx2 = sum([x**2 for x in xs])
    Sigy = sum(ys)
    Sigy2 = sum([y**2 for y in ys])
    
    LSigy = sum(logy)
    LSigy2 = sum([y**2 for y in logy])
    
    meanx = Sigx/n
    meany = Sigy/n
    Lmeany = LSigy/n
    
    sxy = Sigxy - (Sigx*Sigy)/n
    Lsxy = LSigy -(Sigx*LSigy)/n
    sxx = Sigx2 - (Sigx**2)/n
    syy = Sigy2 - (Sigy**2)/n
    Lsyy = LSigy2 - (Sigy**2)/n
    
    Lb = Lsxy/sxx
    b = sxy/sxx
    grad = ((2*np.pi)**2)/b
    Lgrad = ((2*np.pi)**2)/b
    
    pmcc = sxy/(sxx*syy)**0.5
    a = meany - b*meanx
    La = Lmeany - Lb*meanx
    #logy = logA + xlogr
    #La = logA => e^a = A
    #Lb = logr => e^b = r
    A = np.exp(La)
    r = np.exp(Lb)
    print(f"Equation\t \ty = {round(a*1000)/1000} + {round(b*1000)/1000}x")
    #print(f"G or K Value\t \t{grad}")
    print(f"PMCC\t \t{pmcc}")
    f = lambda x: (a + b*x)
    f_ = lambda x: A*(r**x)
    xss = [x/100 for x in range(0,int(100*xs[len(xs)-1]+1))]
    yss = [f(x/100) for x in range(0,int(100*xs[len(xs)-1]+1))]
    xsss = [x/100 for x in range(int(100*xs[0]),int(100*xs[len(xs)-1]+1))]
    ysss = [f_(x/100) for x in range(int(100*xs[0]),int(100*xs[len(xs)-1]+1))]
    fig, ax = plt.subplots(1)
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.scatter(xs,ys, alpha=0.9)
    plt.plot(xss,yss, "#f58742")
    #plt.plot(xsss,ysss)
    plt.grid(which="major",linestyle="-",color="blue")
    plt.minorticks_on()
    plt.grid(which="minor",linestyle=":",color="black")
    plt.show()

def rplot(n):
    plot(generateList(n))

rplot(200)