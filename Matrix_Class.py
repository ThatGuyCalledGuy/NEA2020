from random import randint as r
class Matrix():

    def __init__ (self, m=1, n=1):
        if type(m) != int or type(n) != int:
            print ("ERROR: Matrix dimensions must be INTEGERS")
        else:
            self.rows = m
            self.cols = n
            self.gen_Matrix()
        
    
    def gen_Matrix(self):
        self.matrix = []
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                self.matrix[i].append(r(0,9))
    
    def display(self):
        for i in self.matrix:
            print("[", end = " ")
            for j in i:
                print(j, end = " ")
            print ("]")
    
    def transpose(self):
        self.temp_matrix = []
        new_rows = self.cols
        new_cols = self.rows
        for x in range(new_rows):
            self.temp_matrix.append([])
            for y in range(new_cols):
                self.temp_matrix[x].append(self.matrix[y][x])
        self.matrix = self.temp_matrix
            
    
    def strip4det(self, temp_matrix, row):
        rows = len(temp_matrix)
        for y in range(rows):
                if y == row:
                    del temp_matrix[0]
                else:
                    if y > row:
                        del temp_matrix[y-1][0]
                    else:
                        del temp_matrix[y][0]
        return temp_matrix
    
    
    
    def det(self, matrix):
        det_sum = 0
        self.temp_rows = len(matrix)
        if self.temp_rows == 1:
            return matrix[0][0]
        else:
            for i in range(self.temp_rows):
                print(matrix)
                det_matrix = self.cofactors(matrix)
                det_value = det_matrix[i][0]
                print(det_value)
                
                image_matrix = matrix
                image_matrix = self.strip4det(image_matrix, i)
                det_sum += self.det(image_matrix) * det_value
                print (det_sum)
            return det_sum
    
    
    def cofactors(self, matrix):
        count = 1
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if count % 2 == 0:
                    matrix[y][x] *= -1
                if x != len(matrix[y])-1:
                    count += 1
                
                
        return matrix
                
    def isSquare(self):
        if self.cols == self.rows:
            return True
        return False
    
    def det_display(self):
        self.det_sum = 0
        if self.isSquare():
            print("ERROR CANNOT BE DONE WITH THIS MATRIX")
        else:
            self.temp_matrix = self.matrix
            self.determinant = self.det(self.temp_matrix)
            return self.determinant
            
            