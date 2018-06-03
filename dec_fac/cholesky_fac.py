import numpy as np
from math import sqrt

"""
As seen in GeeksforGeeks: 

The Cholesky decomposition or Cholesky factorization is a decomposition 
of a Hermitian, positive-definite matrix into the product of a lower triangular 
matrix and its conjugate transpose. 

"""
def cholesky(A):
    L = np.zeros(A.shape)
    for row in range(len(L)):
        for col in range(row+1):
            sum = np.dot(L[row, :col], L[col, :col])
            """
            Dealing with the diagonal
            """
            if (row == col):
                L[row][col] = sqrt(max(A[row][row] - sum, 0))
            else:
                L[row][col] = (A[row][col] - sum)/L[col][col]

    return L, np.transpose(L)


def main():
    A = np.array([[4, 12, -16],
                  [12, 37, -43],
                  [-16, -43, 98]])

    L, Lt = cholesky(A)
    print("L: \n")
    print(L)
    print('\n')
    print('Lt: \n')
    print(Lt)
    print('\n')


main()