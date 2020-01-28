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