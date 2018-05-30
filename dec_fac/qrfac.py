import numpy as np
import scipy.linalg


# Using Scipy lib for the QR factorization
def qr_scipy_example():
    A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])  # From the Wikipedia Article on QR Decomposition
    Q, R = scipy.linalg.qr(A)
    print(A)
    print(Q)
    print(R)


# My implementation
def transpose_matrix(M):
    return np.transpose(M)


def normalize_vector(u):
    return np.linalg.norm(u)


def multiply_matrix(M, N):
    tupleM_size = M.shape
    tupleN_size = N.shape
    if (tupleM_size[1] != tupleN_size[0]):
        return 'Cant multiply'
    else:
        return np.matmul(M, N)
    return 0


def householder(A):
    return 0


def main():
    A = np.array([[12, 4, -6], [3, 5, 12], [10, 23, 19]])
    B = np.array([[13, 13, 12], [3, 2, 1], [1, 2, 1]])
    R = multiply_matrix(A, B)
    print(R)

main()
