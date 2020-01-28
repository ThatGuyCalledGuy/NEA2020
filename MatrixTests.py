#Matrix Operations test # Only for 2x2 & 3x3
#Multiplication - Strassen algorithm
#Determinant
#Inverse


def _round(A):
    mat_result = [
        [round(A[0][0]*1000)/1000, round(A[0][1]*1000)/1000],
        [round(A[1][0]*1000)/1000, round(A[1][1]*1000)/1000]
        ]
    
    return mat_result

mat_1 = [
    [8,2],
    [4,6]
    ]
mat_2 = [
    [4,1],
    [5,3]
    ]

def multiply_mat(A,B):
    #Uses the Strassen Algorithm for square matrices
    m1 = (A[0][0] + A[1][1])*(B[0][0] + B[1][1])
    m2 = (A[1][0] + A[1][1]) * B[0][0]
    m3 = A[0][0] * (B[0][1] - B[1][1])
    m4 = A[1][1] * (B[1][0] - B[0][0])
    m5 = (A[0][0] + A[0][1]) * B[1][1]
    m6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1])
    m7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1])
    
    mat_result = [
        [m1 + m4 - m5 + m7, m3 + m5],
        [m2 + m4, m1 - m2 + m3 + m6]
        ]
    return mat_result

def mult_mat_point(point, A):
    result_x = point[0][0] * A[0][0] + point[1][0] * A[0][1]
    result_y = point[0][0] * A[1][0] + point[1][0] * A[1][1]
    
    return [result_x,result_y]


def determinant(A):
    return (A[0][0]*A[1][1]) - (A[0][1]*A[1][0])

def scalar_mult(A,n):
    
    mat_result = [
        [A[0][0] * n, A[0][1] * n],
        [A[1][0] * n, A[1][1] * n]
        ]
    
    return mat_result

def inverse(A):
    
    mat_result = [
        [A[1][1], -1* A[0][1]],
        [-1* A[1][0], A[0][0]] 
        ]
    
    return scalar_mult(mat_result,1/determinant(A))

