from Polynomial_To_Lambda import ConvertIntoEquation
import math

def trapeziumRule(f,upper,lower,n,table=False, value=False):
    h = ((upper-lower)/n)
    lower_to_add = lower
    xs = []
    xs.append(lower_to_add)
    for i in range(n):
        lower_to_add = lower + h*(i+1)
        xs.append(lower_to_add)
    if xs[len(xs)-1]> upper:
        xs[len(xs)-1] = upper
    ys = [f(x) for x in xs]
    middle_vals = 0
    for i in range(len(ys) - 2):
        middle_vals += ys[i+1]
    area = 0.5 * h * (ys[0] + ys[len(ys)-1] + 2*(middle_vals))
    if table:
        print("x:\t", end = " ")
        for i in xs:
            print(round(100*i)/100, "\t", end = " ")
        print("\ny:\t", end= " ")
        for i in ys:
            print(round(100*i)/100,"\t", end = " ")
    
        print("\nArea Estimate:\t", end = " ")
        print(str(round(1000000*area)/1000000) + "\t")
    if value:
        return area


def rectangleRule(f,upper,lower,n,table=False,value=False):
    h = ((upper-lower)/n)
    lower_to_add = lower
    xs = [lower_to_add]
    uval = 0
    lval = 0
    for i in range(n):
        lower_to_add = lower + h*(i+1)
        xs.append(lower_to_add)
    if xs[len(xs)-1]> upper:
        xs[len(xs)-1] = upper
    ys = [f(x) for x in xs]
    for i in range(len(ys)):
        if i == 0:
            uval += ys[i]
        elif i == len(ys)-1:
            lval += ys[i]
        else:
            uval += ys[i]
            lval += ys[i]
    lower_area = h*lval
    upper_area = h*uval
    if table:
        print("x:\t", end = " ")
        for i in xs:
            print(round(100*i)/100, "\t", end = " ")
        print("\ny:\t", end= " ")
        for i in ys:
            print(round(100*i)/100,"\t", end = " ")
    
        print("\nLower Bound:\t", end = " ")
        print(str(round(1000000*lower_area)/1000000) + "\t")
        print("Upper Bound:\t", end = " ")
        print(str(round(1000000*upper_area)/1000000) + "\t")
    if value:
        return lower_area, upper_area
    
    
    
