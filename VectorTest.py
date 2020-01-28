#####VECTOR EXPERIMENT#####
import numpy as np
from sympy.solvers import solve
from sympy import Symbol
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


class Vector():
    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    def get_magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    def __str__(self):
        return str(self.array())
    def array(self):
        return [self.x, self.y, self.z]
    def __add__ (self, other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__ (self,other):
        return self.__add__(other*-1)
    def __radd__ (self,other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
    def __mul__ (self, other):
        if type(other) == int or type(other) == float:
            return Vector(other*self.x,other*self.y,other*self.z)
    def __rmul__ (self,other):
        return self.__mul__(other)
    

def Scalar_Product(v1,v2):
    return (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z)

def Get_Angle(v1,v2, degrees=False):
    #(a.b)/|a||b| = cos(th)
    val = Scalar_Product(v1,v2)
    val /= v1.get_magnitude()*v2.get_magnitude()
    theta = np.arccos(val)
    if degrees:
        theta *= (180/np.pi)
    return theta
    

def Vector_Product(v1,v2):
    new_x = (v1.y*v2.z) - (v1.z*v2.y)
    new_y = (v1.z*v2.x) - (v1.x*v2.z)
    new_z = (v1.x*v2.y) - (v1.y*v2.x)
    return Vector(new_x,new_y,new_z)

class Line():
    def __init__ (self, position_vector, direction_vector):
        self.f = lambda mu: (mu*direction_vector) + position_vector


class Plane():
    def __init__ (self, position_vector, d1_vector, d2_vector):
        self.f = lambda mu, nu: position_vector + mu*d1_vector + nu*d2_vector


def get_xyz_of_line(line):
    x,y,z = [], [], []
    for i in range(-160,160):
        temp = line.f(i/10)
        x.append(temp.array()[0])
        y.append(temp.array()[1])
        z.append(temp.array()[2])
    return x,y,z
        
def get_xyz_of_plane(plane):
    x, y, z = [], [], []
    for i in range(-160,160):
        for j in range(-160,160):
            temp = plane.f(i/10,j/10)
            x.append(temp.array()[0])
            y.append(temp.array()[1])
            z.append(temp.array()[2])
    return x,y,z

def get_xyz_of_vector(vector,normal=False,pos_vec=None):
    if not normal:
        x,y,z = [0],[0],[0]
    else:
        x,y,z = [pos_vec.x],[pos_vec.y],[pos_vec.z]
    x.append(vector.array()[0])
    y.append(vector.array()[1])
    z.append(vector.array()[2])
    return x,y,z

def get_xyz_of_resultant_vector(v1,v2):
    x,y,z = [0],[0],[0]
    x.append(v1.array()[0])
    y.append(v1.array()[1])
    z.append(v1.array()[2])
    x.append((v1+v2).array()[0])
    y.append((v1+v2).array()[1])
    z.append((v1+v2).array()[2])
    return x,y,z

def perpendicular_vectors(v):
    pass
    

def plot_resultant(v1,v2):
    x,y,z = [0],[0],[0]
    ax.scatter(xs=x,ys=y,zs=z)
    x.append(v1.array()[0])
    y.append(v1.array()[1])
    z.append(v1.array()[2])
    x.append(v1.array()[0] + v2.array()[0])
    y.append(v1.array()[1] + v2.array()[1])
    z.append(v1.array()[2] + v2.array()[2])
    ax.plot(xs=x,ys=y,zs=z)
    temp = Vector(x[2],y[2],z[2])
    x1,y1,z1 = get_xyz_of_vector(temp)
    ax.plot(xs=x1,ys=y1,zs=z1)


    


v1 = Vector(1,2,3)
v2 = Vector(-1,3,1)
v3 = Vector(4,2,-2)
#n = Vector_Product(v1,v2)
#r = Line(v3,n)
#p = Plane(v3, v1, v2)

#p1 = Plane(v3, v3, v2)

#x,y,z = get_xyz_of_line(r)
#x1,y1,z1 = get_xyz_of_plane(p)
#x2,y2,z2 = get_xyz_of_plane(p1)
#ax.plot(xs=x2,ys=y2,zs=z2, alpha=0.4)
#ax.plot(xs=x1,ys=y1,zs=z1, alpha=0.4)
#ax.plot(xs=x,ys=y,zs=z)
#plt.show()
