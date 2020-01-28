class Stack():
    def __init__(self):
        self.array = []
    
    def addItem(self,item):
        if item not in self.array:
            self.array.append(item)
    
    def pop(self):
        if len(self.array) != 0:
            item = self.array[len(self.array)-1]
            del self.array[len(self.array)-1]
            return item
        else:
            return None
        
    def clear(self):
        self.array = []