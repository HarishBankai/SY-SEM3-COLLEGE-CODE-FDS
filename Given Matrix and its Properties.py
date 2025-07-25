import numpy as np

A = np.array([[3, 5] ,                                                                              #array for matrix
              [8, 9]])

rank = np.linalg.matrix_rank(A)                                                                        #syntax for rank
determinant = np.linalg.det(A)                                                                      #syntax for determinant

if(determinant != 0):
    inverse = np.linalg.inv(A)                                                                        #check if det is 0 or not
else:
    print("Inverse doesn't exist. Determinant is 0 and thus is singular")                            #print result if det = 0

transpose = A .T                                                                                     #syntax for transpose
eigenvalues , eigenvectors = np.linalg.eig(A)                                                         #syntax for eigen 

print("Rank of a matrix : ", rank)                                                                    #print rank
print("Determinant of a matrix : ", determinant)                                                        #print determinant
print("Inverse of a matrix : ", inverse)                                                                #print inverse
print("Transpose of a matrix : ", transpose)                                                          #print transpose
print("Eigenvalues of a matrix : ", eigenvalues)                                                            #print eigenvalues
print("Eigenvectors of a matrix : ", eigenvectors)                                                    #print eigenvectors




#For multiplication, add a new matrix


B = np.array([[4, 6] ,
              [10, 12]])

result = np.dot(A, B)                                                                                   #syntax for multiplication of matrix[.dot]
print("Multiplication of two matrix : ", result)                                                      #print multiplication of matrix
